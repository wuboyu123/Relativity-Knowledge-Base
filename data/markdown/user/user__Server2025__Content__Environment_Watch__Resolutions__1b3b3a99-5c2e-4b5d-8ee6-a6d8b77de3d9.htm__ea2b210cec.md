---
title: "One or more Resource Servers are inactive"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/1b3b3a99-5c2e-4b5d-8ee6-a6d8b77de3d9.htm
collection: user
fetched_at: 2026-06-22T06:19:02+00:00
sha256: de1216e46bae7577975cde26460739b442988bf6e928e0e420a971949272c593
---

One or more Resource Servers are inactive

1b3b3a99-5c2e-4b5d-8ee6-a6d8b77de3d9

# One or more Resource Servers are inactive

## Description

This alert is triggered when any server's 'Status' field is marked as 'Inactive', indicating potential unavailability or failure of that server.

## Resolution Guidance

### Impact When Active

Inactive Resource Servers will not function as expected. If the Resource Server is not expected to perform any functions within a Resource Pool, then having a status of Inactive will have no impact on your environment.

### How To Resolve

- Log into Relativity.

- Go to the Servers tab.

- Locate any server that has a status of Inactive.

- Open it, and edit the Status field to be Active.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.server.inactive : 1

Group Count

Threshold > 0

Time Window 1 m

Frequency 30 sec

### Alert Metric Details

Metric Name: relsvr.server.inactive

Metric Description: Alert triggers on inactive resource server count greater than 0 for last 30 seconds.

Metric Attributes:

Attribute Name Description

labels.application_name Application Name

labels.message Message describes the issue

labels.name Name of metric

labels.relsvr_artifact_id Resource Server Artifact Id

labels.relsvr_subsystem Resource Server Name

labels.relsvr_system System name
