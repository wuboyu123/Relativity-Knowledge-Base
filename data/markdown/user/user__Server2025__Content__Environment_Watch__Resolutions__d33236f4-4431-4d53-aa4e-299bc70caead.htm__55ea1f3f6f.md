---
title: "Billing agent is disabled"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/d33236f4-4431-4d53-aa4e-299bc70caead.htm
collection: user
fetched_at: 2026-06-22T06:18:26+00:00
sha256: b75330b4cfb3ab1ab0227e411e63d8d7c440fc45639dd93c1a6a17b7fe320a90
---

Billing agent is disabled

d33236f4-4431-4d53-aa4e-299bc70caead

# Billing agent is disabled

## Description

This alert is triggered when the Relativity Billing Agent is found to be disabled on the environment.

## Resolution Guidance

### Impact When Active

The Billing Agent collects system usage and billing information for Relativity. This agent must be enabled to keep your Relativity access enabled. If the Billing Agent does not run successfully for seven days, Relativity access becomes restricted. Once access has been restricted, only system admins are able to access the system; other users are locked out. This limited access allows administrators to log in to Relativity and address the problem, for example, by re-enabling the agent.

### How To Resolve

-

Log into Relativity.

-

Go to the Agents tab in Relativity.

-

Filter for the agent with Name = 'Billing Agent'.

-

Check if the field Enabled is set to 'yes'.

-

Click on Billing Agent.

-

Click on 'Enable Agent' in the console.

-

If it fails to start, ensure the agent server is online and the agent server is assigned to an active resource pool that is associated with the Billing Agent.

### If the Billing agent continues to fail to start you can try....

-

Navigate to the Billing Agent Dashboard.

-

Confirm the agent's recent activity, including:

- Last run time

- Workspaces processed

- Errors, if any

-

If you notice that a workspace is missing from the Billing Agent dashboard or if error details are visible, it may indicate a misconfiguration or failure during the last billing job run. Here are a few steps you can take to investigate:

- Check if the Workspace is Active. Go to Workspace tab in relativity.

- Make sure the workspace is not deleted or archived. Its status is set to 'Active'.

- On the agent server, restart the Relativity Service Host Manager to initiate a reload of agents. For detailed instructions on properly forcing the billing agent to re-run, please refer here

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.agent.disabled : 1 and labels.agent_type_name:"Billing Agent"

Group Count

Threshold > 0

Time Window 1 min

Frequency 30 sec

### Alert Metric Details

Metric Name: relsvr.agent.disabled

Metric Description: Alert triggers on disabled agent count greater than 0 for last 30 seconds.

Metric Attributes:

Attribute Name Description

labels.agent_name Relativity Agent Name

labels.agent_type_name Relativity Agent Type

labels.application_name Application Name

labels.exception_message Any exception message on Agent

labels.message Message describes the issue

labels.name Name of metric

labels.relsvr_artifact_id Relativity agent artifact Id

labels.relsvr_subsystem Agent Name Billing Agent

labels.relsvr_system System name Agents
