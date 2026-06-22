---
title: "One or more agents are disabled"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/dae7d8e9-c33d-470c-b36a-5b6e380e0a25.htm
collection: user
fetched_at: 2026-06-22T06:18:15+00:00
sha256: 733b049d213745e61ef75d865c2d37db16a29dfe68328e8b68f6f881d632c6ad
---

One or more agents are disabled Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

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

On this page

- One or more agents are disabled

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
