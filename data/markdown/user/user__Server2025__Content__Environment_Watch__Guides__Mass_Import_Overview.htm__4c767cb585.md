---
title: "Mass Import Overview"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Mass_Import_Overview.htm
collection: user
fetched_at: 2026-06-22T06:20:04+00:00
sha256: 0ef95a94482578b415670e871cfa9e0ca4f2de2e61ed10ae71bea62e15407a79
---

Mass Import Overview

# Mass Import Overview

This dashboard provides real-time insight into the health and activity of the Mass Import backend service used by Import API and Relativity Desktop Client (RDC). It enables administrators to monitor import throughput, job success rates, SQL performance, and artifact processing volume. This dashboard helps validate that import operations are processing efficiently, identifies performance bottlenecks, and supports proactive capacity planning across the Relativity Server environment.

## Mass Import Health and Throughput

The dashboard summarizes Mass Import service health and operational metrics for the selected time range. Key indicators include:

- Service Health - Confirms overall Mass Import service status.

- Batch Jobs (Total) - Indicates total import job volume.

- Artifacts Created / Updated - Measures document and metadata throughput.

- Files Processed (Total) - Reflects file ingestion volume.

- SQL Load File Bytes (Total) - Tracks load file data processed.

- Job Success Rate - Validates reliability of import execution.

- Batch SQL Duration (Average) - Highlights database execution performance.

- Batch Overall Duration (Average) - Reflects end-to-end batch processing time.

- Data Grid Bytes - Indicates Data Grid utilization when applicable.

Import type and execution source breakdowns provide additional visibility into workload distribution, helping administrators understand how imports are being executed across APIs and native processes.

### Use Cases

Use Case Description

Troubleshoot slow imports Identify elevated SQL duration or overall batch duration that may indicate database or infrastructure bottlenecks.

Validate post-installation or upgrade health Confirm Mass Import services report healthy status and maintain expected success rates after deployment changes.

Monitor ingestion throughput Track artifacts created, files processed, and load file volume to evaluate processing efficiency.

Plan capacity and scaling Review long-term job volume and duration trends to determine resource requirements and optimize performance.
