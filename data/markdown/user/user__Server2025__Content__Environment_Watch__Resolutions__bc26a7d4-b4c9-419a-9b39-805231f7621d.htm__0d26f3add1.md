---
title: "CPU has been exceeding threshold on at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/bc26a7d4-b4c9-419a-9b39-805231f7621d.htm
collection: user
fetched_at: 2026-06-22T06:19:07+00:00
sha256: a6cce121f772873ce784e5cc78f6b98df1659888bb22b9b0f131d85a901ae9c0
---

CPU has been exceeding threshold on at least one host

bc26a7d4-b4c9-419a-9b39-805231f7621d

# CPU has been exceeding threshold on at least one host

## Description

This alert is triggered when CPU has exceeded the defined threshold for more than 15 minutes on at least one host.

## Resolution Guidance

### Impact When Active

When CPU usage remains above the threshold on a host for an extended period, server performance may be impacted. This can result in slower response times, delayed task processing, and timeouts for running operations.

### To resolve this alert, you can try below steps:

- Login to Kibana.

- Click on the alert link in Relativity to navigate to Kibana Dashboard.

- Identify the affected host from the navigated alert dashboard.

- Investigate the processes consuming high CPU on the affected host.

- Review recent changes or workload increases that may have caused the spike.

- Consider scaling resources or redistributing workload if the high CPU usage is sustained.

- Monitor the host to ensure CPU utilization returns to normal levels.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Group Average

Threshold > 0.9

Time Window 15 min

Frequency 1 min

Group alerts by host.name

### Alert Metric Details

Metric Name: system.cpu.utilization

Metric Description: Alert triggers on CPU has exceeded 90% for at least 15 minutes on at least one host.

Metric Attributes:

Attribute Name Description

labels.cpu Logical CPU number starting at 0.

labels.state Breakdown of CPU usage by type.
