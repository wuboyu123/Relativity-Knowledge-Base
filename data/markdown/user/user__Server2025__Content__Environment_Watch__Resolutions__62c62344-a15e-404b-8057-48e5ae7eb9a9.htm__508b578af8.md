---
title: "Custom Page Deployment Manager has not updated its status recently"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/62c62344-a15e-404b-8057-48e5ae7eb9a9.htm
collection: user
fetched_at: 2026-06-22T06:18:41+00:00
sha256: e4f3b1cb9817bdf2a093f83fb507f0b01b05ac62ebb26ab2f9e666920aa7c9a0
---

Custom Page Deployment Manager has not updated its status recently

62c62344-a15e-404b-8057-48e5ae7eb9a9

# Custom Page Deployment Manager has not updated its status recently

## Description

This alert is triggered when at least one Custom Page Deployment Manager agent has not updated for 3 or more minutes. Normally, the "kCura Web Processing Manager" Windows service will periodically update these agents. These updates consist of:

- Checking if the agent has been deleted

- Setting the enabled status, logging level, and interval

- Updating the Agents table in the EDDS database

- Replacing the currently running agent if a new version has been uploaded to Relativity.

If the alert is active, then these updates have not taken place within the last 3 minutes and the agent may be the wrong version or have the wrong settings.

## Resolution Guidance

### Impact When Active

- Custom page or application updates may not properly propagate to all Web Servers.

- Users may experience outdated or missing custom pages when interacting with the application.

- The issue may persist until the affected Custom Page Deployment Manager agent is restored to a healthy state.

### How To Resolve

- In Kibana, navigate to the [Relativity] Custom Page Deployment Managers without recent updates saved search.

- Identify the agents that have not updated recently.

- In Relativity:

- Go to the Agents tab.

- Locate each Custom Page Deployment Manager agent.

- Check if the Enabled column has a value of No.

- Enable any agents with Enabled = No .

If agents do not update after being enabled:

- Open the [Relativity] Windows Services dashboard in Kibana.

- Look for any entries for kCura EDDS Web Processing Manager where Is Service Running is No.

- For each affected Web Server:

- Log into the server.

- Open the Windows Services control panel.

- Locate and start the kCura EDDS Web Processing Manager service if it is not already running.

Otherwise:

- Monitor the agents to confirm they are updating successfully and the alert clears.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic query

Data View metrics-*

Filter Query relsvr.agent.updating: 0 and labels.relsvr_agent_type_guid: BC5A8102-C038-432E-B3A7-C34C86412996

Group Count

Threshold > 0

Time Window Last 1 minute

Frequency Every 3 minutes

### Alert Metric Details

Metric Name: relsvr.agent.updating

Metric Description: Whether the agent has updated in the last 3 minutes

Metric Attributes:

Attribute Name Description

labels.application_name Application Name

labels.name Name of the metric

labels.relsvr_system System Name

labels.relsvr_subsystem Subsystem Name

labels.relsvr_agent_name Name of the agent that is not updating

labels.message A string containing the server name, agent name, time of the last update from the agent, whether the agent is enabled, and the agent run interval

labels.relsvr_server_name The name of the Web Background Processing server

labels.relsvr_server_state Whether the resource server is active

labels.relsvr_agent_status The current status of the agent

labels.relsvr_agent_type_name The name of the agent type of the stale agent

labels.relsvr_agent_type_guid The GUID of the agent type of the stale agent
