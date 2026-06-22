---
title: "One or more Required Agents does not exist"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/034d0230-bd3b-4c50-b17d-7b7fdd85ccd0.htm
collection: user
fetched_at: 2026-06-22T06:18:19+00:00
sha256: 2267a66ffca07cb1c2e2f99aed265b0e40fddf20c9c169f96b15f648c445ab10
---

One or more Required Agents does not exist Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

034d0230-bd3b-4c50-b17d-7b7fdd85ccd0

# One or more Required Agents does not exist

## Description

This alert is triggered when there are no Agent instances for Agent Types that require at least one Agent.

## Resolution Guidance

### Impact When Active

-

Missing required agents lead to important workflow failures in Relativity.

- Core Relativity operations performed by the missing Agent Type will not run.

- Automated or background jobs that rely on the missing Agent Type may fail or may not be scheduled.

- System health and performance may degrade depending on the role of the missing Agent Type.

### How To Resolve

- Click on the Alert link in Relativity to go to the Kibana search named

[Relativity] Required Agents that do not exist

- The Kibana search identifies the Agent Type of the missing agents.

- In Relativity, navigate to the Agents Tab. Then create a new Agent, of the identified Agent Type.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.agent.exists : 0 and labels.relsvr_agent_required : 1

Group Count

Threshold >= 1

Time Window Last 35 sec

Frequency 5 min

### Alert Metric Details

Metric Name: relsvr.agent.exists

Metric Description: Whether the agent exists

- A value of 0 indicates that the Agent does not exist.

- A value of 1 indicates that at least one Agent does exist.

Metric Attributes:

Attribute Name Description

host.name Hostname of the affected Agent Server

labels.application_name Application Name

labels.name Name of the metric

labels.relsvr_system System Name

labels.relsvr_subsystem Subsystem Name

labels.relsvr_agent_required Whether the agent is required

labels.relsvr_agent_type_name Agent Type Name

labels.relsvr_agent_type_guid Agent Type Guid

labels.message Message describes the issue

On this page

- One or more Required Agents does not exist

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
