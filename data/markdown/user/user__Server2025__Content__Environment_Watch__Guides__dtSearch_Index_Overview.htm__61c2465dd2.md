---
title: "dtSearch Index Overview"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/dtSearch_Index_Overview.htm
collection: user
fetched_at: 2026-06-22T06:19:41+00:00
sha256: 41a7d7dfc49bee7fa4a84f67d5e87564c53631c14762d6c62201d413af73661e
---

dtSearch Index Overview

# dtSearch Index Overview

This dashboard provides a consolidated view of key dtSearch indexing activity within a Relativity environment. It highlights index availability, indexing workload, job performance, and throughput trends. Administrators use this dashboard as part of ongoing environment monitoring to ensure that dtSearch resources remain responsive, index builds complete successfully, and overall search performance stays healthy.

## Overview Summary

The health indicator provides a quick view of dtSearch indexing status. It shows whether the system is healthy, the number of jobs executed in the selected time frame, success and failure counts, and any long-queued jobs. Supporting metrics include median job duration and total throughput, helping users confirm that indexing operations are running smoothly and identify potential issues early. The throughput section illustrates data throughput for dtSearch indexing operations over time. By reviewing this trend, administrators can understand typical indexing load patterns and identify anomalies such as unexpected slowdowns, unusual spikes, or drops in activity. This supports capacity planning and helps isolate performance issues that may originate from infrastructure constraints or configuration problems.

### Use Cases

Use Case Description

Monitor overall dtSearch health Users can track availability and job success to confirm that dtSearch indexing components are functioning correctly and responding within expected parameters.

Diagnose indexing delays Metrics such as job duration, throughput, and job queue information help identify bottlenecks when index builds take longer than expected or appear stalled.

Support troubleshooting during incident response When users report slow or incomplete search results, the dashboard provides immediate context on indexing volume, failures, or performance degradation that may contribute to the issue.
