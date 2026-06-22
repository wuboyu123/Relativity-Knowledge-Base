---
title: "One or More Integration Points Jobs Are Stuck"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/fdd136e8-5a72-4d0a-a529-1158873b5b8e.htm
collection: user
fetched_at: 2026-06-22T06:18:47+00:00
sha256: 378bd9ef662ea7bfe3677ef3a533ab5bfd426b4428364eb5d9fd1b1bbcd88df3
---

One or More Integration Points Jobs Are Stuck Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

fdd136e8-5a72-4d0a-a529-1158873b5b8e

# One or More Integration Points Jobs Are Stuck

## Description

An alert is triggered when one or more Integration Points jobs are stuck. This indicates that the jobs are unable to progress or complete as expected.

## Resolution Guidance

### Impact When Active

- The import/export job will remain in a pending state and will not be processed.

### How To Resolve

-

Verify that at least one Integration Points Agent has been added to the Agent server and the active Resource Pool. If missing, create a new Integration Points Agent:

- Navigate to the Agent page.

- Click the New Agent button.

- Choose Integration Point Agent as the Agent Type.

- Select the appropriate Agent Server.

-

Enable the Integration Point Agent if it is disabled.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.rip.stuck_jobs : *

Group Count

Threshold > 0

Time Window 30 min

Frequency 10 min

### Alert Metric Details

Metric Name:

relsvr.rip.stuck_jobs

Metric Description:

Displays the total number of jobs that are currently stuck, providing insight into any jobs that are not progressing as expected.

Metric Attributes:

Attribute Name Description

labels.relsvr_agent_name Agent Name

labels.relsvr_host_installed_products Products installed

labels.relsvr_server_type Servers to be verified

labels.service_namespace Service name

On this page

- One or More Integration Points Jobs Are Stuck

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
