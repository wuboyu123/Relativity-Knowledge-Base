---
title: "One-Time Relativity Elastic License Migration: Platinum to Basic"
url: https://help.relativity.com/Server2025/Content/Elasticstack/One-Time_Relativity_Elastic_License_Migration_Platinum_to_Basic.htm
collection: user
fetched_at: 2026-06-22T06:11:14+00:00
sha256: a577eb87a02fc9693584c43232dc135f04542f671b9d12e271962368dbe5efb8
---

One-Time Relativity Elastic License Migration: Platinum to Basic

# One-Time Relativity Elastic License Migration: Platinum to Basic

## Overview

Relativity Server 2024 Patch 1 introduced a new API key-based authentication model for Data Grid Audit that no longer requires the Elasticsearch Custom Realms plug-in or the Relativity-provided Elasticsearch Platinum license. Customers using Data Grid Audit on self-managed Elasticsearch clusters must complete a one-time license migration after Elasticsearch is running on a supported version. This migration replaces the Relativity-provided Platinum license with a Basic (free/open) Elastic license or a customer-owned paid license. The migration is not part of the Elastic Stack installation or upgrade process and applies only to environments previously using the Relativity-provided Platinum license.

All affected customers must complete the required upgrade and migration steps by April 1, 2026 to avoid service disruption. Core Data Grid Audit functionality is not impacted when using the Basic (free/open) license.

This document applies only to customers upgrading from earlier Elasticsearch versions (7.x or before) that used the Relativity-provided Elasticsearch Platinum license for Data Grid Audit. This migration is not required for new Elastic Stack v8+ installations.

## Prerequisite: Enable API key-Based Authentication

To cut over the new authentication API key, Datagrid Audit must be configured using the CLI. Follow the link below to configure API key-based authentication.

- Enable API Key Based Authentication

## Scope

Applicable for any customer that began using Data Grid Audit before ever running the CLI to enable API key-based authentication.

## Key Considerations

If you are using any Elastic Platinum license features outside of standard Data Grid Audit functionality (e.g. machine learning, cross-cluster replication, etc.), you will need to procure or apply your own organizational Platinum license to continue using these features after April 1, 2026. See here for details on Elastic features that are not supported under a basic license.

## Pre-Migration Validation Checklist

### License and Cluster State

-

Confirm current license status is active and license type is Platinum

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_license

```

Expected Response:

Copy

```text
  {

    "license": {

      "type": "platinum",

      "status": "active"

    }

  }

```

-

No unassigned primary shards

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_cluster/health

```

Expected Response:

Copy

```text
{

  "status": "green",

  "unassigned_primary_shards": 0,

}

```

### Snapshot Safety Check (Recommended)

-

Recent snapshot exists

-

Snapshot status is SUCCESS

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_snapshot/_all/_all

```

Expected Response:

Copy

```text
{

  "snapshots": [

    {

      "state": "SUCCESS"

    }

  ]

}

```

## Scripted Health Check (Pre-Migration)

Execute the following scripts before license migration and save the output.

Copy

```text
curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_license

curl -k -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_cluster/health

curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_cat/nodes?v"

curl -k -u <USER>:<PASSWORD> -X GET "https://<ES_HOST>:9200/_cat/indices?v"

```

## Remove Custom Realm Plugin and Configuration

On each Elasticsearch node:

### Stop Elasticsearch Service

Copy

```text
net stop elasticsearch

```

Or using PowerShell:

Copy

```text
Stop-Service elasticsearch

```

### Remove Custom Realm Plugin (If Installed)

Run from Elasticsearch install directory

Copy

```text
bin\elasticsearch-plugin.bat list

```

Expected Output (Example):

Copy

```text
analysis-icu

repository-s3

custom-realm-plugin

kCuraRealm-7.17.9

```

If a custom realm plugin is listed, remove it:

Copy

```text
bin\elasticsearch-plugin.bat remove <plugin-name>

```

### Remove Realm Configuration from elasticsearch.yml

Edit elasticsearch.yml and remove non-native realms :

Copy

```text
xpack.security.authc.realms.ldap.ldap1:

xpack.security.authc.realms.saml.saml1:

xpack.security.authc.realms.oidc.oidc1:

xpack.security.authc.realms.custom.custom1:

xpack.security.authc.realms.kCuraRealm.jwks:

```

Ensure only native realm remains (default is implicit, no config needed):

Copy

```text
xpack.security.authc.realms.native.native1:

  order: 0

```

## Restart Elasticsearch Nodes

Restart nodes one by one (rolling restart recommended)

Copy

```text
net stop elasticsearch

net start elasticsearch

```

Or using PowerShell:

Copy

```text
Restart-Service elasticsearch

```

## License Migration Procedure

### Activate Basic License (Platinum to Basic One-Time Action)

Run the following API call to downgrade the license from Platinum to Basic :

Copy

```text
curl -k -u <USER>:<PASSWORD> -X POST "https://<ES_HOST>:9200/_license/start_basic?acknowledge=true"

```

### Expected Response

Copy

```text
{

  "basic_was_started": true

}

```

This response confirms that the Basic license has been successfully activated .

Warning This step is irreversible .

## Post-Migration Validation

### License Verification

Copy

```text
curl -u <USER>:<PASSWORD> -X GET https://<ES_HOST>:9200/_license

```

Expected:

Copy

```text
{

  "license": {

    "type": "basic",

    "status": "active"

  }

}

```

### Scripted Health Check (Post-Migration)

Run the same script used in pre-migration and compare results.

### Kibana Validation (If Kibana Exists)

- Navigate to Stack Management | License Management

- Confirm license shows Basic

- Check Kibana logs for license or feature warnings

## Rollback Strategy

Rollback is not supported .

To re-enable paid features, a new paid license file must be purchased and installed .

## References

Official Elastic documentation links for validation and audit purposes:

-

License APIs https://www.elastic.co/guide/en/elasticsearch/reference/current/licensing-apis.html

-

Start Basic License API https://www.elastic.co/guide/en/elasticsearch/reference/current/start-basic.html

-

Elastic Subscriptions and Feature Matrix https://www.elastic.co/subscriptions

-

Kibana Authentication Providers https://www.elastic.co/guide/en/kibana/current/security-settings-kb.html
