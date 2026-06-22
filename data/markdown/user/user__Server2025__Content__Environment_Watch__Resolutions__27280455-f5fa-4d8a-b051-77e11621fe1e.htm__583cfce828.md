---
title: "Primary SQL Server is inaccessible"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/27280455-f5fa-4d8a-b051-77e11621fe1e.htm
collection: user
fetched_at: 2026-06-22T06:18:43+00:00
sha256: 630093717a7eed07a73080125023b8a1a662e34a15e6ef40cff664dfae162e32
---

Primary SQL Server is inaccessible Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

27280455-f5fa-4d8a-b051-77e11621fe1e

# Primary SQL Server is inaccessible

## Description

This alert is triggered when the primary SQL Server is inaccessible, indicating a potential outage or connectivity issue that would severely impact Relativity functionality.

## Resolution Guidance

### Impact When Active

- Relativity becomes unavailable and users cannot log in or access any workspaces.

- Document review, audits, and workspace configurations are inaccessible.

- All background jobs (indexing, imaging, processing, production) fail to start or remain pending.

- Agents and services stop functioning as they rely on SQL for task management.

### How To Resolve

### There can be multiple reasons why SQL Server becomes inaccessible. While there is no single guaranteed fix, you can try the following steps to investigate and resolve the issue:

- Log into Kibana using valid credentials.

- If access is unavailable, contact a Relativity administrator within your organization.

- Upon successful login, Navigate to 'SQL Overview' dashboard.

- On the dashboard, review the Windows Services Health Check section to identify the SQL Server if the services are not running.

- Check SQL Server status- Log into the SQL Server and ensure the SQL Server (MSSQLSERVER) service is running.

- Verify connectivity - Ensure that the SQL Server is reachable from the Relativity Web, Agent, and Worker servers (e.g., using ping or telnet on port 1433)

- Review logs - Inspect SQL Server logs and Windows Event Viewer for any critical errors or root causes (e.g., disk space, authentication, service crashes).

- Verify if there have been any updates to SQL Server user credentials and ensure the EDDSDBO user is correctly configured.

- Engage a Relativity database administrator from your organization - Involve the database administration team for further investigation and resolution.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.sqlserver.running : 0

Group Count

Threshold > 0

Time Window 90 sec Verified data for last 90 sec

Frequency 30 sec Checks for each 30 seconds

### Alert Metric Details

Metric Name: relsvr.sqlserver.running

Metric Description: Alert triggers on primary SQL Server is inaccessible for last 90 seconds.

Metric Attributes:

Attribute Name Description

labels.name Name of Database

labels.state State of SQL Server

On this page

- Primary SQL Server is inaccessible

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- There can be multiple reasons why SQL Server becomes inaccessible. While there is no single guaranteed fix, you can try the following steps to investigate and resolve the issue:

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
