---
title: "Monitoring Overview"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Monitoring_Overview.htm
collection: user
fetched_at: 2026-06-22T06:20:26+00:00
sha256: 6daa9eb6ac398164a17d21c4b3edba247eb4fd6a67104a62827a2f761c6338a5
---

Monitoring Overview

# Monitoring Overview

This dashboard provides a centralized view of telemetry collection and monitoring health across the Relativity environment. It aggregates signals, logs, metrics, and traces to help administrators validate monitoring coverage, detect anomalies, and ensure that data collection agents are functioning properly. This dashboard is essential for operational visibility and proactive troubleshooting.

## Monitoring Health and Signal Trends

This section provides an overall health indicator for monitoring services, along with key metrics such as total signals, logs, metrics, and traces collected. It also displays time-based trends for signal activity and distribution across hosts. These insights help relativity administrators confirm that monitoring agents are active, data ingestion is consistent, and telemetry coverage meets expectations. Sudden drops or spikes in signal counts may indicate connectivity issues or abnormal system behavior requiring investigation.

## Signal and Telemetry Breakdown by Host and Type

This section lists signal counts grouped by host and by telemetry type (logs, metrics, traces). It enables relativity administrators to compare data collection across servers and identify gaps or imbalances in monitoring coverage. Consistent distribution across hosts indicates healthy monitoring, while missing or low counts may point to agent misconfiguration or resource constraints. Reviewing telemetry type breakdown helps ensure that all critical data streams are captured for comprehensive observability.

## Use Cases

Use Case Description

Validate monitoring coverage Confirm that signals, logs, metrics, and traces are being collected across all hosts.

Detect anomalies Identify sudden changes in telemetry volume that may indicate system or agent issues.

Troubleshoot monitoring gaps Use host-level breakdowns to pinpoint missing or incomplete data collection.

Assess monitoring health Quickly verify the operational status of monitoring agents and overall telemetry ingestion.
