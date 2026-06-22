---
title: "One or more agent servers have not been responding for [n] minutes"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/18778d10-60f1-4703-ba94-759175f04ce4.htm
collection: user
fetched_at: 2026-06-22T06:18:17+00:00
sha256: 09ed80c38099f78e1df98a7ef9aae54e71eb7fe1e08b074a9f7fb25ac53600c7
---

One or more agent servers have not been responding for [n] minutes Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

18778d10-60f1-4703-ba94-759175f04ce4

# One or more agent servers have not been responding for [n] minutes

## Description

This alert is triggered when the Server Manager agent is unable to contact one or more Agent Servers for a specific period of time. This indicates the Agent Server may be unresponsive or has failed to check in.

## Resolution Guidance

### Impact When Active

-

The Agent Server is likely not functioning correctly.

-

All Agents on the server may stop responding and will not perform their assigned work.

-

Agent check-in times will stop updating and jobs may remain unprocessed.

-

If left unresolved, this may delay workflows or cause job queues to grow.

### How To Resolve

-

Log in to the host referenced by the alert.

-

Use the Relativity Service account credentials to access the back end of the Agent Server.

-

Open the Services control panel on the server.

-

Locate this service:

- kCura EDDS Agent Manager

-

If the service is not running:

-

Right-click on the service name and choose Start.

-

If already running but not responding, right-click and select Stop, then Start to restart it.

-

If the issue persists after restarting services:

-

Open Event Viewer on the Agent Server.

-

Review Windows Logs | Application and System logs for any error messages related to the failing services.

-

Use the information to identify underlying issues preventing the services from starting or functioning properly.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.agent.disabled : 0 and labels.relsvr_agent_status : "not responding"

Group Count

Threshold >= 1

Time Window 1 min

Frequency 30 sec

### Alert Metric Details

Metric Name: labels.relsvr_agent_status

Metric Description: Indicates the agent status. Possible values are Running , Inactive , and Not Responding .

Metric Attributes:

Attribute Name Description

host.name Hostname of the affected Agent Server

labels.agent_name Relativity Agent Name

labels.agent_type_name Relativity Agent Type

labels.application_name Application Name

labels.exception_message Any exception message on Agent

labels.message Message describes the issue

labels.name Name of metric

labels.relsvr_artifact_id Relativity Agent Artifact Id

labels.relsvr_subsystem Agent Name

labels.relsvr_system System name

labels.relsvr_agent_status The current status of the agent

labels.relsvr_agent_type The name of the agent type of the stale agent

labels.relsvr_resource_server_name The name of the server

relsvr.agent.disabled Indicates whether the agent is disabled If 1, the agent is disabled

On this page

- One or more agent servers have not been responding for [n] minutes

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
