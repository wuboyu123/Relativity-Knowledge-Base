---
title: "Elasticsearch Upgrade and Migration Guide"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Elasticsearch_Upgrade_and_Migration_Guide.htm
collection: user
fetched_at: 2026-06-22T06:04:42+00:00
sha256: 00c34ff58f424ae638e8812588a93befd75f8b8ff338588ed0f9baa0a57a03a2
---

Elasticsearch Upgrade and Migration Guide Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Elasticsearch Upgrade and Migration Guide

This document provides high-level, generic guidance for upgrading or migrating Elasticsearch clusters between major and minor versions. It is intended to assist with planning and executing safe, reliable upgrades or migrations, and references official Elastic documentation for detailed, version-specific steps.

Refer to the official Elastic documentation for the most current and detailed procedures:

- Upgrade a deployment or cluster : https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/elasticsearch

- Snapshot and Restore : https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore

- Prepare to upgrade and Upgrade Assistant : https://www.elastic.co/docs/deploy-manage/upgrade/prepare-to-upgrade

## Upgrade vs Migration

Operation Description

Upgrade In-place version bump within a compatible version range (typically minor or patch releases).

Migration Moving data between incompatible major versions. This usually requires either snapshot/restore or reindexing.

For major version changes, treat the process as a migration due to breaking changes and index compatibility differences. Always consult Elastic's official guidance for the specific version path.

## Upgrade and Migration Strategies

### 1. Rolling Upgrade (In-Place)

- Upgrade nodes one at a time within the same major version.

- Supported only within minor or patch versions, or as dictated by Elastic.

- Not suitable for major version jumps.

Applicable when:

- Upgrading within the same major version (e.g., 8.17 - 8.19).

### 2. Snapshot and Restore

- Back up data from the source cluster to a snapshot repository.

- Restore the snapshot into the target cluster.

- Works only if snapshots and created indices are compatible with the target version.

- See full details here: https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore

Applicable when:

- A snapshot infrastructure is available.

- Snapshot and index versions are compatible with the target Elasticsearch version.

### 3. Reindex from Remote

- Read data from the source cluster and write into a new index on the target cluster using the _reindex API.

- Useful when snapshot restore of older indices is not compatible.

Applicable when:

- Direct snapshot restore is not possible due to version compatibility.

## Recommended Migration/Upgrade Strategies and Version Matrix

When planning an Elasticsearch upgrade or migration, choose the strategy based on the source and target versions. The following matrix summarizes recommended approaches:

Source Version Target Version Snapshot Restore Reindex from Remote Rolling Upgrade Notes

6.x 8.x/9.x ❌ ✅ ❌ Use intermediate upgrade or reindex.

7.x 8.x ✅ (may require reindex) ✅ ❌ Use Upgrade Assistant before migration.

7.x 9.x ❌ ✅ ❌ Use intermediate upgrade or reindex.

8.x 9.x ✅ ✅ ✅ (minor only) Upgrade to latest 8.x before migration.

Legend:

- ✅ = Supported

- ❌ = Not supported

Recommendations:

- Always upgrade to the latest patch of the current major version before attempting a major migration.

- Run the Upgrade Assistant to identify and resolve issues before migration.

- Prefer snapshot and restore for supported direct migrations; otherwise, reindex from remote.

- Rolling upgrades are only supported within the same major version (minor/patch upgrades).

- Test all migrations in a non-production environment before production deployment.

## Index Compatibility for Snapshot Restore

Any index restored from a snapshot must also be compatible with the current cluster's version. Attempting to restore an index created in an incompatible version will cause the restore attempt to fail.

Index creation version 8.3-8.19 9.0.0-9.2.3

6.0-6.7 ✅ ¹ ✅ ¹

6.8 ✅ ¹ ✅ ¹

7.0-7.1 ✅ ✅ ¹ ²

7.2-7.17 ✅ ✅ ¹ ²

8.0-8.19 ✅ ✅

9.0.0-9.2.3 ❌ ✅

¹ These indices must be reindexed to upgrade them to 7.x or later.

² These indices must be reindexed to upgrade them to 8.x or later.

For the most up-to-date compatibility matrix, see Elastic's official docs: https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore#index-compatibility

## Elasticsearch Upgrade Approaches

### Upgrade Using Snapshot and Restore

#### When to Use

- Major version upgrades (e.g., 6.x - 8.x / 9.x)

- Cluster replacement or hardware refresh

- When downtime is acceptable

#### 1. Pre-Upgrade Checks

Verify that:

-

Cluster health status is green .

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_cluster/health

```

Expected responses (examples):

Copy

```text
{

  "cluster_name": "es-cluster",

  "status": "green",

  "number_of_nodes": 3,

  "active_shards": 120

}

```

Warning

In development environments, cluster health may show yellow due to single-node setup or unassigned replicas. This is expected.

For production upgrades, ensure the cluster health status is green before proceeding.

-

No snapshot or reindex tasks are currently running.

Copy

```text
# Filter reindex tasks

curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_tasks?detailed=true&actions=*reindex"

# Filter snapshot tasks

curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_tasks?detailed=true&actions=*snapshot*"

```

Expected responses (examples):

Copy

```text
{

  "nodes": {}

}

```

#### 2. Configure Snapshot Repository

Repository path must be configured in path.repo on all nodes . The path must be accessible and shared across all nodes.

elasticsearch.yml

Copy

```text
path.repo: ["\\\\sharedPath\\es-backups"]

```

Restart all nodes after updating the configuration.

Create repository:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X PUT "https://<ES_HOST>:9200/_snapshot/es_backup_repo" -H 'Content-Type: application/json' -d '

{

  "type": "fs",

  "settings": {

    "location": "\\\\sharedPath\\es-backups",

    "compress": true

  }

}'

```

Expected response:

Copy

```text
{ "acknowledged": true }

```

Verify repository:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X POST "https://<ES_HOST>:9200/_snapshot/es_backup_repo/_verify"

```

Expected response (example):

Copy

```text
{ "nodes": { /* ... node details ... */ }  }

```

#### 3. Take Snapshot

Copy

```text
curl -k -u <USER>:<PASSWORD> -X PUT "https://<ES_HOST>:9200/_snapshot/es_backup_repo/pre_upgrade_snapshot" -H 'Content-Type: application/json' -d '

{

  "indices": "app-index-*,logs-*,metrics-*",

  "ignore_unavailable": true,

  "include_global_state": false

}'

```

Replace app-index-* , logs-* , and metrics-* with your actual business index patterns (for example: audit_* , customers-* , monitoring-* ).

This ensures only application indices are included in the snapshot and avoids conflicts with existing system indices during restore.

Expected response (example):

Copy

```text
{ "accepted": true }

```

Check snapshot status:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_snapshot/es_backup_repo/pre_upgrade_snapshot"

```

Expected response (example):

Copy

```text
{

  "snapshots": [

    { "snapshot": "pre_upgrade_snapshot", "state": "SUCCESS", "indices": ["my-index"] }

  ]

}

```

#### 4. Install New Elasticsearch Version

-

Stop Elasticsearch Service on All Nodes

Copy

```text
net stop <service-name>

```

Or using PowerShell:

Copy

```text
Stop-Service <service-name>

```

-

Uninstall Elasticsearch on All Nodes Run from Elasticsearch install directory

Copy

```text
bin\elasticsearch-service.bat remove <service-name>

```

-

Install new Elasticsearch version

Refer to the Installation Guide

#### 5. Configure Snapshot Repository on New Version

Same repository path must be configured in path.repo on all nodes . The path must be accessible and shared across all nodes.

elasticsearch.yml

Copy

```text
path.repo: ["\\\\sharedPath\\es-backups"]

```

Restart all nodes after updating the configuration.

Register repository again:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X PUT "https://<ES_HOST>:9200/_snapshot/es_backup_repo" -H 'Content-Type: application/json' -d '

{

  "type": "fs",

  "settings": {

    "location": "\\\\sharedPath\\es-backups"

  }

}'

```

Expected response:

Copy

```text
{ "acknowledged": true }

```

Verify repository:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X POST "https://<ES_HOST>:9200/_snapshot/es_backup_repo/_verify"

```

Expected response (example):

Copy

```text
{ "nodes": { /* ... node details ... */ }  }

```

#### 6. Restore Snapshot on New Cluster

Restore snapshot:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X POST "https://<ES_HOST>:9200/_snapshot/es_backup_repo/pre_upgrade_snapshot/_restore" \

-H "Content-Type: application/json" -d '

{

  "indices": "app-index-*,logs-*,metrics-*",

  "ignore_unavailable": true,

  "include_global_state": false

}'

```

Do not use "indices": "*" during restore, as system indices (e.g., .security , .kibana ) may already exist in the target cluster and can cause restore conflicts.

Always restore only application indices by replacing app-index-* , logs-* , and metrics-* with your actual business index patterns (for example: audit* , customers-* , monitoring-* ).

Expected response (example):

Copy

```text
{ "accepted": true }

```

Monitor restore:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_cat/recovery?v"

```

Expected response (example):

Copy

```text
index recovery_source shard time

my-index snapshot        0    30s

```

#### 7. Post-Restore Validation

Verify that:

-

Cluster health status is green .

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_cluster/health

```

Expected responses (examples):

Copy

```text
{

  "cluster_name": "es-cluster",

  "status": "green",

  "number_of_nodes": 3,

  "active_shards": 120

}

```

Warning

In development environments, cluster health may show yellow due to single-node setup or unassigned replicas. This is expected.

For production upgrades, ensure the cluster health status is green before proceeding.

-

Verify indices.

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_cat/indices?v"

```

Expected Responses - Indices List (examples) :

Copy

```text
#/cat/indices sample output

health status index        uuid                   pri rep docs.count docs.deleted store.size pri.store.size

green  open   my-index     someUuid               5   1       1000            0     10mb          5mb

```

### Upgrade Using Reindex from Remote

#### When to Use

- Snapshot restore is not supported between versions

- Need selective index migration

- Zero or minimal downtime required

#### 1. Prepare New Elasticsearch Cluster

- Install new Elasticsearch version

Refer to the Installation Guide

- Verify that cluster health status is green

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_cluster/health

```

Expected response (example):

Copy

```text
  {

    "cluster_name": "es-cluster",

    "status": "green",

    "number_of_nodes": 3,

    "active_shards": 120

  }

```

Warning

In development environments, cluster health may show yellow due to single-node setup or unassigned replicas. This is expected.

For production upgrades, ensure the cluster health status is green before proceeding.

#### 2. Add Reindex Setting to the New Elasticsearch Cluster

This step adds old cluster to the reindex.remote.whitelist, points old cluster CA bundle to be trusted by the new cluster using the setting reindex.ssl.certificate_authorities.

On the new cluster, update elasticsearch.yml

Copy

```text
reindex.remote.whitelist: ["{OLD-ES-HOST}:{PORT}"]

reindex.ssl.certificate_authorities: "/app/config/old_cluster_ca/cacert.pem"

reindex.ssl.verification_mode: "full"

```

You can optionally set reindex.ssl.verification_mode to full, certificate or none depending on the validity of hostname and the certificate path.

Restart Elasticsearch.

#### 3. Reindex Individual Index

Copy

```text
curl -k -u <USER>:<PASSWORD> -X POST "https://<ES_HOST>:9200/_reindex" \

-H "Content-Type: application/json" \

-d '{

  "source": {

    "remote": {

      "host": "https://<OLD_ES_HOST>:9200",

      "username": "<OLD_USER>",

      "password": "<OLD_PASSWORD>"

    },

    "index": "source_index"

  },

  "dest": {

    "index": "target_index"

  }

}'

```

#### 4. Reindex All Indexes (One by One)

Elasticsearch does not support wildcard reindex directly.

Example script logic:

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET "https://<OLD_ES_HOST>:9200/_cat/indices?h=index"

```

Expected response (example):

Copy

```text
my-index

another-index

```

Reindex each index individually by running the _reindex API for each index.

#### 5. Monitor Reindex Progress

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_tasks?detailed=true&actions=*reindex"

```

Expected response (example):

Copy

```text
{ "nodes": { /* task details */ } }

```

#### 6. Post-Reindex Validation

Verify that:

-

Cluster health status is green .

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_cluster/health

```

Expected responses (examples):

Copy

```text
{

  "cluster_name": "es-cluster",

  "status": "green",

  "number_of_nodes": 3,

  "active_shards": 120

}

```

Warning

In development environments, cluster health may show yellow due to single-node setup or unassigned replicas. This is expected.

For production upgrades, ensure the cluster health status is green before proceeding.

-

Verify indices.

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_cat/indices?v"

```

Expected Responses - Indices List (examples) :

Copy

```text
#/cat/indices sample output

health status index        uuid                   pri rep docs.count docs.deleted store.size pri.store.size

green  open   my-index     someUuid               5   1       1000            0     10mb          5mb

```

Compare document counts between old and new clusters.

## Post-Upgrade Checklist

- Cluster health is green

- All required indices restored/reindexed

- Applications connected successfully

- Old cluster decommissioned (after validation)

## Troubleshooting

- Mapping conflicts: inspect index mappings with GET <index>/_mapping and resolve conflicts before reindexing.

- Snapshot failures: inspect repository verification and Elasticsearch logs; use GET _snapshot/<repo>/_status .

- Reindex slow or stuck: inspect _tasks and consider slicing, throttling, or increasing resources.

- Plugin incompatibility: verify that required plugins are installed and compatible on the target cluster.

## Rollback

- Keep snapshots until validation is complete.

- To rollback, restore the snapshot to the original cluster or redeploy the previous cluster using saved configuration and snapshots.

- Verify application functionality after rollback.

On this page

- Elasticsearch Upgrade and Migration Guide

- Upgrade vs Migration

- Upgrade and Migration Strategies

- 1. Rolling Upgrade (In-Place)

- 2. Snapshot and Restore

- 3. Reindex from Remote

- Recommended Migration/Upgrade Strategies and Version Matrix

- Index Compatibility for Snapshot Restore

- Elasticsearch Upgrade Approaches

- Upgrade Using Snapshot and Restore

- Upgrade Using Reindex from Remote

- Post-Upgrade Checklist

- Troubleshooting

- Rollback


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
