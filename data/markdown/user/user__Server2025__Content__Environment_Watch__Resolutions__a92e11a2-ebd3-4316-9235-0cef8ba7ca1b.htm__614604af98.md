---
title: "Environment Watch monitoring agent is offline for at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/a92e11a2-ebd3-4316-9235-0cef8ba7ca1b.htm
collection: user
fetched_at: 2026-06-22T06:19:20+00:00
sha256: 0fdc67c599004abd8529f44fbfff29a176d395a98e64bf1f8c7d905af41f0730
---

Environment Watch monitoring agent is offline for at least one host

a92e11a2-ebd3-4316-9235-0cef8ba7ca1b

# Environment Watch monitoring agent is offline for at least one host

## Description

This alert is triggered when the Environment Watch monitoring agent fails to check in from any host, signaling that the agent may be stopped or unresponsive.

## Resolution Guidance

### Impact When Active

- Monitoring data from the affected host is not collected — key metrics such as service status, resource usage, and application health are missing.

- When the monitoring agent is not functioning on a server—such as a web server—it will not report any metrics for that host. As a result, issues like a Windows service failure or high drive usage on that server will go undetected, and related alerts may be suppressed.

- Dashboards show incomplete or outdated data, impacting visibility into system health and issue correlation.

### How To Resolve

-

Click on the Alert link in the Relativity to go to Kibana.

-

Log into Kibana using valid credentials.

-

If access is unavailable, contact a Relativity administrator within your organization.

-

Upon successful login, Navigate to Monitoring Agents dashboard.

-

In the dashboard, review the Last Check-In column.

-

Locate the server where the agent has not checked in—this is the affected host.

-

Log into the identified server.

-

Restart the service: Relativity Environment Watch Agent.

### If the Service Fails to Start You can also try..

- Open Windows Event Viewer and check for any related error messages.

- If the issue persists, please contact Relativity support.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View [Relativity] Hosts Heartbeat

Filter Query numeric_labels.heartbeat_count> 0

Group Count

Threshold < 0

Time Window 2 min

Frequency 1 min

### Alert Metric Details

Metric Name: numeric_labels.heartbeat_count

Metric Description: Alert will be true when Environment Watch monitoring agent is offline for at least one host.

Metric Attributes:

Attribute Name Description

labels.application_name Name of the application

host.name Host name

labels.relsvr_system Agents

labels.relsvr_subsystem Custom Agent

labels.server_address Server address
