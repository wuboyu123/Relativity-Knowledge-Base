---
title: "Kibana Troubleshooting"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Kibana_Troubleshooting.htm
collection: user
fetched_at: 2026-06-22T06:11:22+00:00
sha256: 63572d187c0564cf80bdb02da2876886f86c0a9fc52b78790a9334753fa07c9a
---

Kibana Troubleshooting Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Kibana Troubleshooting

This document provides troubleshooting guidance for common Kibana issues encountered during installation, configuration, and operation in Relativity environments.

This guide assumes a default Kibana installation path of C:\elastic\kibana . Adjust paths according to your actual installation directory.

## Windows service issues

The following troubleshooting steps apply only if Kibana was set up as a Windows service (e.g., using Relativity Windows Service Manager (RWSM) or a similar tool). If you did not install Kibana as a Windows service, you must ensure that kibana.bat is running in a command prompt or as a scheduled task.

### Kibana service not starting

Symptoms:

- Kibana service fails to start

- Service stops immediately after starting

Troubleshooting Steps:

-

Check Service Status and Configuration:

Copy

```text
Get-Service -Name kibana

```

Expected output:

Copy

```text
Status   Name   DisplayName

```

Copy

```text
Running  kibana Kibana

```

```powershell

Get-CimInstance -ClassName Win32_Service -Filter "Name='kibana'" | Select-Object Name, State, StartMode, StartName

```

```

-

Verify the service is running under Local System account (default configuration).

-

Check Kibana Logs:

- Navigate to C:\elastic\kibana\logs\

- Review the latest log files ( kibana.log ) for error messages.

- Look for configuration errors or Elasticsearch connection issues (for example: Unable to connect to Elasticsearch at https://<host or ip address>:9200 ).

-

Start Service Manually:

Copy

```text
Start-Service kibana

```

Expected output

Copy

```text
(No output if successful. Service status will be "Running" after execution.)

```

### Service crashes or stops unexpectedly

Symptoms:

- Kibana service starts but stops after a short period

- Service status shows "Stopped" unexpectedly

- Users lose access to Kibana interface

Troubleshooting Steps:

-

Check Kibana Logs:

- Navigate to C:\elastic\kibana\logs\

- Review the latest log files ( kibana.log ) for crash details

- Look for memory issues or connection failures

-

Review Kibana Configuration:

- Check C:\elastic\kibana\config\kibana.yml file

- Verify Elasticsearch connection settings

- Ensure all required configuration parameters are present

-

Verify Elasticsearch Connectivity:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "https://<hostname_or_ip>:9200/"

```

Expected output:

Copy

```text
{

   "name" : "EMTTEST",

   "cluster_name" : "elasticsearch",

   "cluster_uuid" : "PwBZoINKQjGZ53WH4gFfBg",

   "version" : {

      "number" : "8.19.8",

      "build_flavor" : "default",

      "build_type" : "zip",

      "build_hash" : "a091390de485bd4b127884f7e565c0cad59b10d2",

      "build_date" : "2025-02-28T10:07:26.089129809Z",

      "build_snapshot" : false,

      "lucene_version" : "9.12.0",

      "minimum_wire_compatibility_version" : "7.17.0",

      "minimum_index_compatibility_version" : "7.0.0"

   },

   "tagline" : "You Know, for Search"

}

```

-

Check Memory Usage:

- Monitor Kibana process memory consumption using Task Manager or Resource Monitor.

- Verify sufficient system memory is available.

## Authentication issues

### Username/Password authentication issues

Symptoms:

- Login failures at Kibana interface

- "Invalid username or password" errors

- Users cannot access Kibana dashboards

Troubleshooting Steps:

-

Verify User Configuration:

- Ask the user to log in using the elastic username credentials.

- Check C:\elastic\kibana\config\kibana.yml : Copy

```text
elasticsearch.username: "<username>"

elasticsearch.password: "<password>"

```

-

Test Elasticsearch Credentials Independently:

-

Use the elastic username and password from kibana.yml to verify connectivity to Elasticsearch:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "https://<hostname_or_ip>:9200/"

```

Expected output:

Copy

```text
{

   "name" : "EMTTEST",

   "cluster_name" : "elasticsearch",

   ...

}

```

For port-related issues, see the Port Configuration Troubleshooting guide.

## Memory issues

### Insufficient memory allocation

Symptoms:

- Kibana becomes unresponsive

- Slow loading of dashboards and visualizations

- Out of memory errors in logs

Troubleshooting Steps:

-

Check Current Memory Usage:

Copy

```text
Get-Process -Name node | Where-Object {$_.ProcessName -eq "node"} | Select-Object WorkingSet, VirtualMemorySize

```

Expected output:

Copy

```text
WorkingSet VirtualMemorySize

```

Copy

```text
12345678   23456789

```

```

- Review Out of Memory Errors in Logs:

- Review Out of Memory Errors in Logs:

- Check for "out of memory" or "heap" errors in C:\elastic\kibana\logs\kibana.log .

Out of memory errors typically indicate insufficient system memory or improper Node.js heap settings. Review the error details in the log for specific causes and recommended actions.

- Verify Disk Space:

- Insufficient disk space can also cause memory-related failures.

- For disk space troubleshooting steps, see Verify Disk Space .

## Kibana encryption keys configuration

### Missing or invalid encryption keys

Symptoms:

- Kibana fails to start with encryption-related errors

- "Saved objects encryption key is missing" warnings

- Unable to save or retrieve saved objects

Troubleshooting Steps:

-

Generate Encryption Keys:

Copy

```text
cd C:\elastic\kibana\bin

.\kibana-encryption-keys.bat generate

```

Expected output:

Copy

```text
xpack.encryptedSavedObjects.encryptionKey: "<randomly-generated-key-1>"

xpack.reporting.encryptionKey: "<randomly-generated-key-2>"

xpack.security.encryptionKey: "<randomly-generated-key-3>"

```

-

Configure Required Encryption Keys in kibana.yml:

- Copy the generated lines above and paste them into your C:\elastic\kibana\config\kibana.yml file.

## Service verification

### Verifying Kibana health and status

Symptoms:

- Need to confirm Kibana is operating correctly

- Performance monitoring requirements

- Health check automation

Troubleshooting Steps:

-

Check Kibana Status:

Copy

```text
curl.exe -k -u <username>:<password> -X GET "http://<hostname_or_ip>:5601/api/status"

```

Expected output:

Copy

```text
{

  "name": "kibana",

  "version": {

    "number": "8.x.x"

  },

  "status": {

    "overall": {

      "level": "available"

    }

  }

}

```

## Additional diagnostic commands

### Configuration validation

-

Validate YAML syntax

Copy

```text
C:\elastic\kibana\bin\kibana.bat

```

Expected output:

Copy

```text
# There is no built-in --validate-config option in Kibana 8.x.

# Configuration is validated when Kibana starts.

# If there are errors in kibana.yml, they will be shown in the console output and Kibana will fail to start.

```

## Installation issues

### Long path issues during extraction

Symptoms:

- Errors when extracting the kibana-8.xx.x-windows-x86_64.zip file.

- The extraction process fails due to file paths exceeding the Windows default limit.

Troubleshooting Steps:

-

Enable Long Paths in Windows: Windows must be configured to support long file paths. This can be enabled via the Local Group Policy Editor.

-

Run gpedit.msc to open the Local Group Policy Editor.

-

Navigate to Computer Configuration | Administrative Templates | System | Filesystem .

-

Double-click on Enable Win32 long paths and set it to Enabled .

-

Re-extract the Kibana zip file:

- After enabling long path support, attempt to extract the kibana-8.xx.x-windows-x86_64.zip file again.

On this page

- Kibana Troubleshooting

- Windows service issues

- Kibana service not starting

- Service crashes or stops unexpectedly

- Authentication issues

- Username/Password authentication issues

- Memory issues

- Insufficient memory allocation

- Kibana encryption keys configuration

- Missing or invalid encryption keys

- Service verification

- Verifying Kibana health and status

- Additional diagnostic commands

- Configuration validation

- Installation issues

- Long path issues during extraction


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
