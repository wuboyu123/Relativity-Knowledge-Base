---
title: "Install and Configure APM Server"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Install_and_Configure_APM_Server.htm
collection: user
fetched_at: 2026-06-22T06:11:11+00:00
sha256: 64505a67c23a31a3b6a0a126ebc36fc25bad95e9cbe6e2d6b79f1874c6a7f6df
---

Install and Configure APM Server

# Install and Configure APM Server

## Install and Configure APM Server (Required for Environment Watch Only)

APM Server is required for Environment Watch only.

Official Documentation: For detailed APM Server installation and configuration guidance, see Elastic's official APM Server documentation and APM Server configuration .

### Prerequisites to Set Up APM Server

- Elastic and Kibana should be configured and services should be up and running.

### Download APM Server 8.x.x or 9.x.x

- Visit Elastic's APM Server page .

- Download the 8.x.x or 9.x.x Windows ZIP file.

- Before extracting, see How to Unblock Downloaded Files .

- Extract the files to C:\elastic (e.g., C:\elastic\apm-server-x.x.x ).

### Enable TLS for APM

Use elasticsearch-certutil

Note: Single Cluster with Multiple Nodes: Run the following commands on the master node server.

-

Open an elevated PowerShell window in C:\elastic\elasticsearch-x.x.x\bin .

-

Create CA by running:

Copy

```text
.\elasticsearch-certutil.bat ca --silent --pem --out "C:\elastic\secrets\apm_ca.zip"

```

-

Extract apm_ca.zip contents into C:\elastic\secrets\apm-ca\ (you should have ca.crt and ca.key inside the folder).

-

Create server cert for APM. Build SAN args with your DNS and IPs, e.g., --dns <fqdn> --dns <shortname> --ip <server-ip> , then run:

Copy

```text
.\elasticsearch-certutil.bat cert --silent --pem --ca-cert "C:\elastic\secrets\apm-ca\ca.crt" --ca-key "C:\elastic\secrets\apm-ca\ca.key" --name apm-server [SAN args] --out "C:\elastic\secrets\apm-server.zip"

```

-

Extract zip contents into C:\elastic\secrets\apm-server\ to get apm-server.crt and apm-server.key.

-

Create C:\elastic\apm-server-x.x.x\config\certs directory.

-

Copy the certificate files:

Copy

```text
C:/elastic/secrets/apm-server/apm-server.crt -> C:/elastic/apm-server-x.x.x/config/certs/apm-server.crt

C:/elastic/secrets/apm-server/apm-server.key -> C:/elastic/apm-server-x.x.x/config/certs/apm-server.key

C:/elastic/secrets/apm-ca/ca.crt -> C:/elastic/apm-server-x.x.x/config/certs/ca.crt

```

-

Install CA to Windows trust (Local Machine Root) so browsers trust APM. Run mmc, add Certificates snap-in for Computer account, import ca.crt under Trusted Root Certification Authorities, or run:

Copy

```text
certutil.exe -addstore -f Root "C:\elastic\apm-server-x.x.x\config\certs\ca.crt"

```

### Configure APM Server

#### Create an API Key for APM / Beats

- Log in to Kibana at https://<hostname_or_ip>:5601 using the elastic user.

- Use the global search to find API keys and select it.

- Click Create API key .

- Enter a descriptive name (e.g., "APM Server Key").

- Click Create API key .

- In Privileges , select Beats for recommended permissions.

- The system will generate the API key. Copy and securely store the generated id and api_key values.

Copy and save the id and api_key values immediately. Store them securely according to your organization's credential management and security policies.

#### Edit the APM Server Configuration

-

Navigate to the APM Server folder (e.g., C:\elastic\apm-server-x.x.x ).

-

Open apm-server.yml in a text editor.

-

Update the file to match the following sample configuration, replacing all placeholder values with your actual environment values:

Show sample apm-server.yml configuration Copy

```text
apm-server:

    host: "0.0.0.0:8200"

    ssl.enabled: true

    ssl.certificate: "C:/elastic/apm-server-x.x.x/config/certs/apm-server.crt"

    ssl.key: "C:/elastic/apm-server-x.x.x/config/certs/apm-server.key"

output.elasticsearch:

    hosts:

        - "https://your-elasticsearch-host:9200"

    api_key: "your_api_id:your_api_key"

    ssl.enabled: true

    ssl.certificate_authorities:

        - "C:/elastic/elasticsearch-x.x.x/config/certs/http_ca.crt"

    ssl.verification_mode: full

setup.kibana:

    host: "https://your-kibana-host:5601"

    ssl.enabled: true

    ssl.certificate_authorities:

        - "C:/elastic/elasticsearch-x.x.x/config/certs/http_ca.crt"

instrumentation:

    enabled: true

    environment: production

# Stack Monitoring for APM Server (disabled by default)

# Uncomment and set enabled: true only if needed for troubleshooting

# monitoring:

#     enabled: false

#     elasticsearch:

#         hosts:

#             - "https://your-elasticsearch-host:9200"

#         api_key: "your_api_id:your_api_key"

#         ssl:

#             certificate_authorities:

#                 - "C:/elastic/elasticsearch-x.x.x/config/certs/http_ca.crt"

```

Certificate Paths:

- APM Server certificates : Created in the Enable TLS for APM section, typically stored in C:/elastic/apm-server-x.x.x/config/certs/

- Elasticsearch HTTP CA certificate : Auto-generated during Elasticsearch first run, located at C:/elastic/elasticsearch-x.x.x/config/certs/http_ca.crt

- Replace x.x.x with your actual version numbers (e.g., 8.19.8 or 9.3.0 )

- Replace your-elasticsearch-host and your-kibana-host with actual hostnames or IP addresses

- Replace your_api_id:your_api_key with the API key values from the previous step

### Install APM Server as a Windows Service

-

Open an elevated PowerShell window.

-

Change directory to the APM Server installation folder (e.g., cd C:\elastic\apm-server-x.x.x ).

-

Run the following command to install the service:

Copy

```text
PowerShell.exe -ExecutionPolicy Unrestricted -File .\install-service.ps1

```

The output should look similar to:

Copy

```text
Installing service apm-server...

Service "apm-server" has been successfully installed.

```

### Start the APM Server service

-

Open an elevated PowerShell window and run the following command:

Copy

```text
Start-Service -Name "apm-server"

```

If PowerShell fails to start the APM Server service: You can use the Windows Services application as an alternative:

- Open the Start menu, type services.msc , and press Enter .

- In the Services window, locate apm-server .

- Right-click the service and select Start .

- Use this method if you encounter permission or environment issues with PowerShell.

- After instrumentation is configured, verify it in Kibana:

- Navigate to APM in the Kibana menu

- Confirm that services and traces appear in the APM interface

- Check that the APM Server is successfully receiving data

### Verify APM Server

Open an elevated Command Prompt and run the following command (replace <hostname_or_ip> with your actual value). Validate TLS using the CA certificate rather than using -k :

Copy

```text
curl.exe --cacert C:\elastic\apm-server-x.x.x\config\certs\ca.crt https://<hostname_or_ip>:8200

```

On Windows, use curl.exe to avoid PowerShell aliasing.

Or with PowerShell:

Copy

```text
Invoke-RestMethod -Uri https://<hostname_or_ip>:8200

```

The response should indicate publish_ready is true and will look similar to:

Show sample response Copy

```text
{

  "build_date": "2025-02-27T18:17:35Z",

  "build_sha": "f6b917b725e1a22af433e5b52c5c6f0ff9164adf",

  "publish_ready": true,

  "version": "8.x.x"

}

```

Alternative to browser: If you cannot access the APM Server endpoint in a browser, use the above curl or Invoke-RestMethod commands in your terminal to verify the server status. This is useful for headless environments or remote servers.

## Additional Setup and Verification

### Add Elastic APM Integration Package

Skipping the steps below will cause the Relativity Server CLI to fail.

-

Log in to Kibana and navigate to Integrations (use the menu or search bar).

-

Search for "Elastic APM" and select it from the integration catalog.

-

Click the Add Elastic APM button in the top right corner.

-

Configure the integration:

- Integration name: Enter a descriptive name (e.g., "APM Server")

- Host: <hostname_or_ip>:8200

- URL: https://<hostname_or_ip>:8200

-

Click Save and Continue .

-

Select Add Elastic Agent later (Agent is not required for initial setup).

### Verify APM Data View

Before proceeding with EW CLI, check if the APM data view is created in Kibana:

-

Open a browser and navigate to:

Copy

```text
https://<hostname_or_ip>:5601

```

-

Log in using elastic credentials

-

Navigate to Discover (use the menu or search bar)

-

Confirm the APM data view is present in the data view dropdown (e.g., traces-apm* , metrics-apm* , logs-apm* )

### Verify Cluster Health

Click to expand Verify Cluster Health details 1. Open an elevated Command Prompt and run the following command (replace `username`, `password`, and `hostname_or_ip` with your actual values). In production validate TLS with the CA certificate: Copy

```text
```bash

curl.exe -u <username>:<password> --cacert C:\elastic\secrets\ca\ca.crt https://<hostname_or_ip>:9200/_cat/health

```

```

On Windows, use curl.exe to avoid PowerShell aliasing.

Browser Access: While you can navigate to https://<hostname_or_ip>:9200/_cat/health in a browser, authentication may not work reliably in all browsers. The curl or PowerShell methods above are recommended for consistent results.

Or with PowerShell:

Copy

```text
Invoke-RestMethod -Uri https://<hostname_or_ip>:9200/_cat/health -Credential (Get-Credential)

```

Show sample response

-

You should see a response similar to:

Copy

```text
1690219200 10:00:00 elasticsearch green 1 1 0 0 0 0 0 0 - 100.0%

```

The word green in the response means the cluster is healthy. The word yellow in the response means the cluster is partially healthy. If you see red , investigate further.

### Elasticsearch Snapshot Repository Setup (Optional)

Click to expand Elasticsearch Snapshot Repository Setup details

Note: Optional for backup and recovery. Snapshot repositories enable backup and restore capabilities but are not required for basic Elasticsearch operation.

Official Documentation: For comprehensive snapshot and restore guidance, see Elastic's snapshot and restore documentation .

Important: For single cluster with multiple nodes, path.repo must be configured in elasticsearch.yml on every node . All nodes must have access to the same backup location (shared network drive or replicated storage).

#### Create and Configure Backup Directory

-

Create a backup directory on a dedicated high-performance volume (not C:):

Copy

```text
# Use a dedicated volume for backups

mkdir X:\es-backups

```

-

Grant the Elasticsearch service account full read/write permissions:

Copy

```text
# For LocalSystem (default service account)

icacls "X:\es-backups" /grant "NT AUTHORITY\SYSTEM:(OI)(CI)F" /T

# For custom service account (replace DOMAIN\svc_elasticsearch)

# icacls "X:\es-backups" /grant "DOMAIN\svc_elasticsearch:(OI)(CI)F" /T

# Verify permissions

icacls "X:\es-backups"

```

-

Configure the snapshot repository path in elasticsearch.yml on all nodes :

Copy

```text
path.repo: ["X:/es-backups"]

```

-

Restart Elasticsearch on all nodes to apply the changes:

Copy

```text
Restart-Service -Name "elasticsearch-service-x64"

```

#### Register Snapshot Repository

-

Open Kibana and navigate to Dev Tools (Management > Dev Tools).

-

Run the following command to register the repository:

Copy

```text
PUT _snapshot/my_backup

{

    "type": "fs",

    "settings": {

        "location": "X:/es-backups",

        "compress": true

    }

}

```

Note: Verify that the location path matches the path.repo value configured in elasticsearch.yml .

#### Verify Snapshot Repository

-

In Kibana Dev Tools , run the following command:

Copy

```text
POST _snapshot/my_backup/_verify

```

-

You should see a response confirming the repository is valid:

Copy

```text
{

    "nodes": {

        "node_id": {

            "name": "node_name"

        }

    }

}

```

#### Test Snapshot and Restore Operations

Show snapshot test commands

-

Create a test snapshot:

Copy

```text
PUT _snapshot/my_backup/test_snapshot_001

{

    "indices": "*",

    "ignore_unavailable": true,

    "include_global_state": false

}

```

-

Monitor snapshot progress:

Copy

```text
GET _snapshot/my_backup/test_snapshot_001/_status

```

-

List available snapshots:

Copy

```text
GET _snapshot/my_backup/_all

```

-

Test restore (creates a renamed copy to avoid overwriting):

Copy

```text
POST _snapshot/my_backup/test_snapshot_001/_restore

{

    "indices": "your-index-name",

    "ignore_unavailable": true,

    "include_global_state": false,

    "rename_pattern": "(.+)",

    "rename_replacement": "restored_$1",

    "include_aliases": false

}

```

-

Monitor restore progress:

Copy

```text
GET _recovery?human

```

-

Clean up test snapshot after verification:

Copy

```text
DELETE _snapshot/my_backup/test_snapshot_001

```

Creating Manual Snapshots: To create a snapshot manually at any time, use: PUT _snapshot/my_backup/snapshot_name

Automated Backups: For automated scheduled snapshots, consider implementing Snapshot Lifecycle Management (SLM). See the official SLM documentation for details.

### Multi-Cluster: Cross-Cluster Replication (CCR) (Optional)

Click to expand Cross-Cluster Replication (CCR) details

CCR replicates indices from a leader cluster to a follower cluster.

IMPORTANT: CCR requires appropriate Elastic licensing/features and configuration. Confirm your subscription/supportability before enabling.

#### Example: Create a Follower Index

Assume:

- Leader cluster alias: audit-cluster (registered in Register Remote Cluster Connection )

- Leader cluster name: secondary-cluster

- Leader index: my-index-000001

- Follower cluster (primary-cluster) is where you run this command

Copy

```text
PUT /my-index-000001-follower/_ccr/follow

{

  "remote_cluster": "audit-cluster",

  "leader_index": "my-index-000001"

}

```

Check follower status:

Copy

```text
GET /my-index-000001-follower/_ccr/info

```

### Operational Commands (Single Cluster with Multiple Nodes / Multi-Cluster)

Click to expand Operational Commands details

### Verify Cluster Health (local)

Copy

```text
GET _cluster/health?pretty

```

### Verify Nodes

Copy

```text
GET _cat/nodes?v

```

### Verify Remote Clusters (CCS/CCR)

Copy

```text
GET _remote/info

```

### Rolling Restart (High Level)

- Stop one data node

- Wait for shard relocation / health stabilization

- Start the node

- Repeat for remaining data nodes

- Then master nodes (one at a time)
