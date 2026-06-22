---
title: "One or More Integration Points Jobs Are Stuck"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/fdd136e8-5a72-4d0a-a529-1158873b5b8e.htm
collection: user
fetched_at: 2026-06-22T06:18:47+00:00
sha256: 378bd9ef662ea7bfe3677ef3a533ab5bfd426b4428364eb5d9fd1b1bbcd88df3
---

One or More Integration Points Jobs Are Stuck

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
