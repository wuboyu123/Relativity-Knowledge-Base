---
title: "Windows Service is stopped for at least one Resource Server"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/d14f3e28-fa2b-4df8-8b02-4d35d45bb800.htm
collection: user
fetched_at: 2026-06-22T06:19:09+00:00
sha256: d2cea42346d9c7fef172277af90f858f2f2184adf6ca830659d2cfeb656f804b
---

Windows Service is stopped for at least one Resource Server Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

d14f3e28-fa2b-4df8-8b02-4d35d45bb800

# Windows Service is stopped for at least one Resource Server

## Description

This alert is triggered when a monitored Windows Service is stopped on at least one Resource Server. The following services are monitored:

- kCura EDDS Web Processing Manager

- kCura Service Host Manager

- kCura EDDS Agent Manager

- Relativity Analytics Engine

- W3SVC (World Wide Web Publishing Service)

- Elasticsearch

- apm-server

- Relativity Secret Store

- QueueManager (Invariant Queue Manager)

- RabbitMQ

Note: This alert can also include custom Windows services that have been configured through Custom JSON Configuration.

## Resolution Guidance

### Impact When Active

When a monitored Windows Service is stopped on a Resource Server, that server will not function as expected and will not be able to process tasks or handle workloads assigned to it.

### How To Resolve

From the alert in Relativity, navigate to the linked Kibana dashboard to identify:

- The affected server

- The specific Windows service that has stopped

Access the affected Host Server and perform the following steps:

- Open the Windows Services management console.

- Locate the Windows service identified in Kibana.

- Start the stopped Windows service.

- Return to Kibana and verify that the service status has updated to Running.

#### You can also try

If the Windows service fails to start or stops again after being started:

- Verify that the service Startup Type is configured correctly (e.g., Automatic).

- Review the Windows Event Logs for error messages or warnings related to the service.

- Consider restarting the server if the service continues to fail.

- Contact Relativity Support for further assistance if the issue persists.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elasticsearch Query

Data View metrics-*

Filter Query relsvr.windows_service.running : 0

Group Count

Threshold > 0

Time Window 90 sec

Frequency 30 sec

### Alert Metric Details

Metric Name: relsvr.windows_service.running

Metric Description: Alert triggers on at least one windows service stopped for at least 90 seconds.

Metric Attributes:

Attribute Name Description

Display Name Name of Service

host.name host name

Is Service Running 0/1

On this page

- Windows Service is stopped for at least one Resource Server

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- Alert Details

- Alert Condition Details

- Alert Metric Details


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
