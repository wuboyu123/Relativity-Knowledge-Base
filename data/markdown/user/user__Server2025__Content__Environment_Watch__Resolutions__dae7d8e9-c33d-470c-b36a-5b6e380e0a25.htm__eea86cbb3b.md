---
title: "One or more agents are disabled"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/dae7d8e9-c33d-470c-b36a-5b6e380e0a25.htm
collection: user
fetched_at: 2026-06-22T06:18:15+00:00
sha256: 733b049d213745e61ef75d865c2d37db16a29dfe68328e8b68f6f881d632c6ad
---

One or more agents are disabled

dae7d8e9-c33d-470c-b36a-5b6e380e0a25

# One or more agents are disabled

## Description

This alert is triggered when one or more Relativity agents are in a disabled state.

## Resolution Guidance

### Impact When Active

- Agents are process managers that run in the background of Relativity to complete scheduled jobs. Each agent is responsible for a specific type of task. For example, if the Production Manager agent is disabled, any jobs related to Production will fail to run in an Instance.

- To understand the impact of an individual agent type being disabled, you must understand what that specific agent is responsible for and if being disabled will impact Relativity functionality that you need to be working. For more details on what each agent type is responsible for, visit the Agents page for the version of Relativity Server you are currently running.

### How To Resolve

- Log into Relativity.

- Go to the Agents tab.

- Identify agents with the Enabled value set to No by applying a filter on the 'Enabled' field.

- Enable the disabled agent, if necessary.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.agent.disabled : 1

Group Count

Threshold > 0

Time Window 1 min

Frequency 30 sec

### Alert Metric Details

Metric Name: relsvr.agent.disabled

Metric Description: Alert triggers on disabled agents count greater than 0 for last 30 seconds.

Metric Attributes:

Attribute Name Description

labels.agent_name Relativity Agent Name

labels.agent_type_name Relativity Agent Type

labels.application_name Application Name

labels.exception_message Any exception message on Agent

labels.message Message describes the issue

labels.name Name of metric

labels.relsvr_artifact_id Relativity agent artifact Id

labels.relsvr_subsystem Agent Name

labels.relsvr_system System name Agents
