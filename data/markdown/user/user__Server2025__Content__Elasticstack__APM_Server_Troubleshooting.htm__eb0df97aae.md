---
title: "APM Server Troubleshooting"
url: https://help.relativity.com/Server2025/Content/Elasticstack/APM_Server_Troubleshooting.htm
collection: user
fetched_at: 2026-06-22T06:11:23+00:00
sha256: 29cef591ee7eb251538649b6dc94676abe7b86e270638ea6bbe63ed478e9c6e7
---

APM Server Troubleshooting Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# APM Server Troubleshooting

This document provides troubleshooting guidance for common APM Server issues encountered during installation, configuration, and operation in Relativity Server environments.

This guide assumes a default APM Server installation path of C:\elastic\apm-server . Adjust paths according to your actual installation directory.

## Windows Service issues

### APM Server service not starting

Symptoms:

- APM Server service fails to start

- Service stops immediately after starting

- Error messages in APM Server logs

Troubleshooting Steps:

-

Check APM Server Status:

Copy

```text
Get-Service -Name apm-server

```

Expected Response:

Copy

```text
Status   Name        DisplayName

```

Running apm-server Elastic APM Server

Copy

```text

2. Verify Service Configuration:

```powershell

(Get-CimInstance Win32_Service -Filter "Name = 'apm-server'").StartName

```

Expected Response:

Copy

```text
LocalSystem

```

-

Check APM Server Logs:

-

Navigate to C:\Program Files\apm-server\logs\

-

Review the latest log files ( apm-server.log ) for error messages

-

Look for configuration errors or connection issues with Elasticsearch

For Elasticsearch connection issues, see Elasticsearch Troubleshooting

-

Verify Configuration File:

Copy

```text
C:\elastic\apm-server\apm-server.exe test config -c "C:\elastic\apm-server\apm-server.yml"

```

Expected Response:

Copy

```text
Config OK

```

### Service crashes or stops unexpectedly

Symptoms:

- APM Server service starts but stops after a short period

- Service status shows "Stopped" unexpectedly

- APM data collection stops working

Troubleshooting Steps:

-

Check APM Server Logs (See steps above)

-

Review APM Server Configuration:

- Check apm-server.yml file in C:\elastic\apm-server\

- Verify Elasticsearch connection settings (see Elasticsearch Troubleshooting for detailed troubleshooting)

- Common configuration issues:

- TLS : Ensure correct protocol ( http vs https )

- Hostname : Verify correct Elasticsearch server hostname

- Port : Confirm correct Elasticsearch port (usually 9200)

API keys are the preferred authentication method and expire by default in 6 months. Consider switching from username/password to API key authentication. For API key creation, see Kibana Troubleshooting .

Copy

```text
output.elasticsearch:

  hosts: ["https://<hostname_or_ip>:9200"]

  api_key: "your-api-key-here"

  # OR (not recommended)

  # username: "<username>"

  # password: "<password>"

```

This section in apm-server.yml configures how APM Server connects to your Elasticsearch cluster.

- hosts : The URL(s) of your Elasticsearch node(s).

- api_key : The recommended authentication method.

- username / password : Legacy authentication (not recommended; use API keys instead). For instructions on creating an API key, see Kibana Troubleshooting .

-

To verify the connection, run:

Copy

```text
C:\elastic\apm-server\apm-server.exe test output -c "C:\elastic\apm-server\apm-server.yml"

```

Expected output for successful connection:

Copy

```text
elasticsearch: https://<hostname_or_ip>:9200...

  parse url... OK

  connection...

    parse host... OK

    dns lookup... OK

    addresses: fe80::61a7:3f3f:210:8d65%Ethernet 2, 10.0.2.2

    dial up... OK

  TLS...

    security... WARN server's certificate chain verification is disabled

    handshake... OK

    TLS version: TLSv1.3

    dial up... OK

  talk to server... OK

  version: 8.19.8

```

-

To verify Elasticsearch connectivity, see Elasticsearch Troubleshooting .

### Permission and access issues

Symptoms:

- Access denied errors when starting service

- Unable to write to log directories

- Configuration file access errors

Troubleshooting Steps:

- The APM Server Windows service runs under Local System account by default.

- Verify access to C:\elastic\apm-server\ directory.

- Check write permissions to C:\Program Files\apm-server\logs\ directory.

## Memory issues

### High memory usage

Symptoms:

- APM Server consuming excessive memory

- System performance degradation

- Out of memory errors in logs

Troubleshooting Steps:

-

Check APM Server Logs:

- Look for memory-related error messages or stack traces. Example error message: Copy

```text
fatal error: out of memory

```

-

Review APM Server Configuration:

- Check apm-server.yml for memory-related settings.

- Common settings to review:

- apm-server.memory.limit : Maximum memory APM Server can use.

- apm-server.memory.queue : Size of the memory queue for incoming events. Example configuration:

Copy

```text
apm-server:

  memory:

    limit: 512mb

    queue: 1000

```

-

Monitor System Resources:

- Use Task Manager or Resource Monitor to check APM Server memory usage.

- Compare with configured limits in apm-server.yml .

-

Adjust Memory Settings:

- If APM Server is using too much memory, consider adjusting the following settings in apm-server.yml :

- apm-server.memory.limit : Decrease the maximum memory limit.

- apm-server.memory.queue : Decrease the memory queue size.

- Example: Copy

```text
apm-server:

memory:

limit: 256mb

queue: 500

```

-

Restart APM Server:

-

After making changes, restart the APM Server service:

Copy

```text
Restart-Service apm-server

```

Expected response:

Copy

```text
WARNING: Waiting for service 'apm-server

(apm-server)' to stop...

```

## Self-Instrumentation

Symptoms:

- Need to monitor APM Server itself for performance and health metrics

- Want to enable self-monitoring and observability for the APM Server

Troubleshooting Steps:

-

Enable Self-Instrumentation:

- Self-instrumentation allows APM Server to monitor its own performance.

- This feature is configured in the apm-server.yml file.

- Refer to the Installing Elastic Stack guide for complete configuration details.

-

Verify Self-Instrumentation:

-

After configuration, restart the APM Server service:

Copy

```text
Restart-Service apm-server

```

Expected response:

Copy

```text
WARNING: Waiting for service 'apm-server

(apm-server)' to stop...

```

-

Check Kibana to verify that APM Server metrics are being collected

## Service verification

### Verifying APM Server Health

Symptoms:

- Need to confirm APM Server is operating correctly

- Health check automation

Troubleshooting Steps:

-

Check APM Server Status:

Copy

```text
curl.exe -k "http://<hostname_or_ip>:8200/"

```

Expected reponse:

Copy

```text
{

  "build_date": "...",

  "build_sha": "...",

  "publish_ready": true,

  "version": "8.19.8"

}

```

On this page

- APM Server Troubleshooting

- Windows Service issues

- APM Server service not starting

- Service crashes or stops unexpectedly

- Permission and access issues

- Memory issues

- High memory usage

- Self-Instrumentation

- Service verification

- Verifying APM Server Health


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
