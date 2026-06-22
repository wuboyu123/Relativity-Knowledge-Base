---
title: "Mass Import Details"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Mass_Import_Details.htm
collection: user
fetched_at: 2026-06-22T06:20:06+00:00
sha256: ac52b8359726bb0aa9ab16a83b7260a0787900621b70f3e6cfe3253fc6fde363
---

Mass Import Details

# Mass Import Details

This dashboard provides low-level performance visibility into Mass Import batch execution within your Relativity environment. It expands on the Mass Import Overview dashboard by exposing detailed timing metrics for overall batch duration, SQL execution performance, and individual import processing stages. This dashboard supports in-depth troubleshooting and performance analysis when import jobs experience latency, failures, or inconsistent throughput.

## Batch and Stage-Level Performance Analysis

The dashboard provides time-series visibility into Mass Import performance at both the batch and stage levels. Batch-level metrics include:

- Batch Overall Performance - Measures total end-to-end batch processing duration over time, helping identify prolonged import execution.

- Batch SQL Performance - Tracks database execution time associated with batch processing, highlighting potential SQL bottlenecks or database resource contention.

Stage-level metrics break down performance within the import pipeline, including activities such as:

- Folder creation

- Copying extracted text to Data Grid

- Copying full text from file share

- Load column definition caching

By reviewing batch and stage metrics together, administrators can determine whether performance delays originate from SQL execution, overall batch orchestration, or a specific import stage.

### Use Cases

Use Case Description

Troubleshoot slow import batches Determine whether delays are caused by SQL processing, overall batch handling, or a specific import stage.

Diagnose database bottlenecks Use SQL performance trends to identify sustained or recurring database latency.

Investigate stage-level latency Isolate infrastructure or file share performance issues affecting specific import steps.
