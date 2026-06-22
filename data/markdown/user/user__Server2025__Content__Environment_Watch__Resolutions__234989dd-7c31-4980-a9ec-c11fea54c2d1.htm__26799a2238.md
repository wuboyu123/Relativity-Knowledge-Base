---
title: "Memory is exceeding threshold on at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/234989dd-7c31-4980-a9ec-c11fea54c2d1.htm
collection: user
fetched_at: 2026-06-22T06:19:06+00:00
sha256: 3500ba33502429052281afbf3f83eb9aca9a9383e7975dc0ec827b594ed34c84
---

Memory is exceeding threshold on at least one host

234989dd-7c31-4980-a9ec-c11fea54c2d1

# Memory is exceeding threshold on at least one host

## Description

This alert is triggered when RAM is exceeding the defined threshold on at least one host for at least 5 consecutive minutes.

## Resolution Guidance

### Impact When Active

When memory usage remains above the threshold on a host for an extended period, the server may experience performance degradation, such as slower response times, increased memory swapping to disk, or a higher risk of out-of-memory conditions that can disrupt applications or services.

### To resolve this alert, you can try:

- Login to Kibana.

- Click on the alert link in Relativity to navigate to Kibana Dashboard.

- Identify the affected host from the navigated alert dashboard.

- Investigate the processes consuming high memory on the affected host.

- Review recent changes or workload increases that may have caused the memory spike.

- If high memory usage persists, consider scaling memory resources or redistributing workloads.

- Monitor the host to ensure memory utilization returns to normal levels.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Group Average

Filter Query labels.state : "used"

Threshold > 0.96

Time Window 5 min

Frequency 1 min

Group alerts by host.name

### Alert Metric Details

Metric Name: system.memory.utilization

Metric Description: Alert triggers when RAM is exceeding 96% on at least one host for at least 5 consecutive minutes.

Metric Attributes:

Attribute Name Description

labels.state Breakdown of memory usage by type.
