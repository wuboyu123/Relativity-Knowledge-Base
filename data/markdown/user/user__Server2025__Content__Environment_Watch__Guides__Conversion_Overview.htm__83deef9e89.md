---
title: "Conversion Overview"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Conversion_Overview.htm
collection: user
fetched_at: 2026-06-22T06:20:37+00:00
sha256: be7c2058240785ecab775e5919ab307790f77a862ec16f7af1cdd7c522e8db11
---

Conversion Overview

# Conversion Overview

This dashboard provides a consolidated view of document conversion activity across your Relativity environment. It tracks conversion volume, queue health, and performance efficiency to help maintain smooth and consistent document processing. It helps detect queue delays, identify conversion bottlenecks, and ensure that documents move efficiently through the conversion and rendering process.

## Conversion Status and Activity Summary

The Conversion Status and Activity Summary section presents key indicators of conversion health and throughput. The Conversion health indicator reflects whether any active alerts exist for document conversion. A healthy status means no conversion-related alerts are currently active. Metrics such as Total Documents, Conversion Queues, and Very Long Conversion (30+ seconds) highlight workload volume and potential performance issues. The metric indicators for Total Documents by Result and Total Documents by Priority show how many conversions were completed, pending, failed, or in process, helping to monitor conversion reliability and prioritization.

The Total Requests Over Time chart visualizes conversion demand across time intervals, enabling trend analysis and identification of spikes that may align with high workload periods. The Conversion Overview Table provides detailed records, including workspace, document ID, conversion type, and processing duration, offering granular visibility into each conversion request.

### Use Cases

Use Case Description

Monitor conversion throughput Track the total number of conversion requests processed and identify when workloads increase to maintain balanced performance across agents.

Troubleshoot slow or failed conversions Review Very Long Conversion counts, cache hit rate, and queue metrics to pinpoint performance constraints or service interruptions.

Assess cache efficiency Monitor the DVS Cache Hit Rate to evaluate how effectively cached content is leveraged for repeat document conversions.

Analyze conversion load distribution Review Total Documents by Priority and Requests Over Time metrics to see how conversion work is divided between ConvertAhead, OnTheFly, and MassConvert tasks.

### Associated Alerts

- On-the-Fly Conversion (P1) - Queue Backlog Threshold Exceeded

- Convert Ahead (P2) - Queue Backlog Threshold Exceeded

- Mass Convert (P3) - Queue Backlog Threshold Exceeded

- Conversion Agent connection to RabbitMQ is broken
