---
title: "Elasticsearch Troubleshooting"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Elasticsearch_Troubleshooting.htm
collection: user
fetched_at: 2026-06-22T06:11:21+00:00
sha256: ad04edfaf32f0ad0892071fac9b69b92f8906e98af173b37dd41ba080a6492af
---

Elasticsearch Troubleshooting Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Elasticsearch Troubleshooting

This document provides troubleshooting guidance for common Elasticsearch issues encountered during installation, configuration, and operation in Relativity Server environments.

This guide assumes a default Elasticsearch installation path of C:\elastic\elasticsearch . Adjust paths according to your actual installation directory.

## Windows service issues

Before troubleshooting Elasticsearch, verify that all required Elastic Stack services are running. If any of these are not running, other troubleshooting steps may be irrelevant.

Check all required services:

Copy

```text
Get-Service -Name elasticsearch-service-x64, kibana, apm-server | Format-Table -AutoSize

```

OR

Copy

```text
Get-Service -Name elasticsearch, kibana, apm-server | Format-Table -AutoSize

```

Expected output:

Copy

```text
Status   Name           DisplayName

------   ----           -----------

Running  elasticsearch  elasticsearch

Running  kibana         kibana

Running  apm-server     apm-server

```

- The kibana Windows service may not exist if Kibana was not installed as a Windows service (e.g., via Relativity Windows Service Manager (RWSM)). RWSM is not required; Kibana can be run manually or as a scheduled task. Only check for the kibana service if you have installed it as a service.

- If Kibana is not in running state, click here for Kibana troubleshooting .

- If APM is not in running state, click here for APM troubleshooting

### Elasticsearch service not starting

Symptoms:

- Elasticsearch service fails to start

- Service stops immediately after starting

- Error messages in Elasticsearch logs

Troubleshooting Steps:

-

Check Service Status:

Copy

```text
Get-Service -Name elasticsearch-service-x64 | Select-Object Status, StartType, Name

```

OR

Copy

```text
Get-Service -Name elasticsearch | Select-Object Status, StartType, Name

```

Expected output:

Copy

```text
Status   StartType Name

```

Running Automatic elasticsearch

Copy

```text

2. Verify Service Configuration:

```powershell

(Get-CimInstance Win32_Service -Filter "Name = 'elasticsearch-service-x64'").StartName

```

OR

Copy

```text
(Get-CimInstance Win32_Service -Filter "Name = 'elasticsearch'").StartName

```

Expected output:

Copy

```text
LocalSystem

```

-

Check Elasticsearch Logs:

- Navigate to the log directory (default: C:\elastic\elasticsearch-{version}\logs\ ).

- Review the Elasticsearch log file ( elasticsearch.log ) for error messages.

- Check the slow logs and garbage collection logs if present.

- For every error in the Elasticsearch log, provide troubleshooting for that specific error.

- For detailed logging information, refer to the official Elasticsearch logging documentation

- Elasticsearch includes a bundled Java runtime, so a separate Java installation is not required.

- If the JAVA_HOME environment variable is defined, Elasticsearch will use the specified Java version instead of the bundled one.

- If you want to use a specific Java version, ensure JAVA_HOME is set correctly.

-

Start Service Manually:

Copy

```text
Start-Service elasticsearch-service-x64

```

OR

Copy

```text
Start-Service elasticsearch

```

Expected output:

Copy

```text
(No output if successful. Service status will be "Running" after execution.)

```

### Service crashes or stops unexpectedly

Symptoms:

- Elasticsearch service starts but stops after a short period

- Service status shows "Stopped" unexpectedly

Troubleshooting Steps:

-

Check Elasticsearch Logs:

- Navigate to C:\elastic\elasticsearch\logs\

- Review the Elasticsearch log file ( elasticsearch.log ) for errors

- For every error in the Elasticsearch log, provide troubleshooting for that specific error.

Always check the latest error in the Elasticsearch log and troubleshoot accordingly. This approach should be followed everywhere.

-

Verify Disk Space:

-

Ensure sufficient disk space on data and log directories (minimum 15% free)

-

Verify data and log files are on separate drives from the Operating System drive. If you store Elasticsearch data on a network share, ensure the share is accessible and has sufficient free space. Some environments may not use mapped drives.

Copy

```text
# Check disk space

Get-WmiObject -Class Win32_LogicalDisk | Select-Object DeviceID, @{Name="FreeSpace(%)";Expression={[math]::Round(($_.FreeSpace/$_.Size)*100,2)}}

```

Expected output:

Copy

```text
DeviceID FreeSpace(%)

```

Copy

```text
   C:       22.15

   D:       48.92

   ```

```

For port-related issues, see the Port Configuration Troubleshooting guide.

## Memory issues

### Insufficient memory allocation

Symptoms:

- OutOfMemoryError in Elasticsearch logs

- Poor performance or slow queries

- Node becomes unresponsive

Troubleshooting Steps:

-

Check Current Memory Usage:

Copy

```text
Get-WmiObject -Class Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum

```

Expected output:

Copy

```text
Count    : 2

Average  :

Sum      : 34359738368

Property : Capacity

```

Sum is the total RAM in bytes (e.g., 34359738368 bytes = 32 GB).

-

Review JVM Heap Settings:

- Edit C:\elastic\elasticsearch\config\jvm.options file. (If the file does not exist, create it.) Copy

```text
# Recommended: Set Xms and Xmx to same value

# Example for system with 8GB+ RAM:

-Xms4g

-Xmx4g

```

Set heap to 50% of available RAM, maximum 32GB. Monitor current memory usage before making changes.

-

Check for Memory Leaks:

- Monitor heap usage over time

- Look for continuously increasing memory consumption

- Review application logs for memory-related warnings

## Authentication issues

### Username/Password authentication issues

Symptoms:

- Login failures

- "authentication failed" errors

- Cannot access Elasticsearch with credentials

Troubleshooting Steps:

-

Verify User Exists:

Copy

```text
curl.exe -k -X GET "https://<hostname_or_ip>:9200/_security/user/<username>" -u <username>:<password>

```

Expected output:

Copy

```text
{

  "<username>": {

    "username": "<username>",

    "roles": [

      "superuser"

    ],

    ...

  }

}

```

-

Reset Password:

Copy

```text
C:\elastic\elasticsearch\bin\elasticsearch-reset-password.bat -u <username>

```

Expected output:

Copy

```text
Password for the [<username>] user successfully reset.

```

-

Verify Security Configuration:

- Check C:\elastic\elasticsearch\config\elasticsearch.yml : Copy

```text
xpack.security.enabled: true

```

Also verify that the URL you are using is https://<username>:9200/

## Service verification

### Verifying Elasticsearch health

Symptoms:

- Uncertainty about cluster status

- Need to confirm proper operation

- Performance monitoring

Troubleshooting Steps:

-

Check Cluster Health:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "https://<hostname_or_ip>:9200/_cluster/health?pretty"

```

Expected response for healthy cluster: :

Copy

```text
{

  "cluster_name": "elasticsearch",

  "status": "green",

  "timed_out": false,

  "number_of_nodes": 3,

  "number_of_data_nodes": 3

}

```

-

Verify Node Status:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "https://<hostname_or_ip>:9200/_cat/nodes?v"

```

Expected output:

Copy

```text
ip            heap.percent ram.percent cpu load_1m load_5m load_15m     node.role      master name

<ip>          14           95          28                               cdfhilmrstw *  <node name>

```

-

Check Index Health:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "https://<hostname_or_ip>:9200/_cat/indices?v"

```

Expected output:

Copy

```text
health status index    uuid                   pri rep docs.count docs.deleted store.size pri.store.size

green  open   myindex  1a2b3c4d5e6f7g8h9i0j   1   1   1000       0            1.2mb      600kb

```

-

Monitor Performance:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "https://<hostname_or_ip>:9200/_nodes/stats?pretty"

```

Expected output:

Copy

```text
{

  "nodes": {

    "node_id": {

      "name": "node-1",

      "host": "10.0.0.1",

      ...

    }

  }

}

```

On this page

- Elasticsearch Troubleshooting

- Windows service issues

- Elasticsearch service not starting

- Service crashes or stops unexpectedly

- Memory issues

- Insufficient memory allocation

- Authentication issues

- Username/Password authentication issues

- Service verification

- Verifying Elasticsearch health


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
