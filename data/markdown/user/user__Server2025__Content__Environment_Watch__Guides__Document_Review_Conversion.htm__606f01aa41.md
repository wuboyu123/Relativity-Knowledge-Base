---
title: "Document Review Conversion"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Document_Review_Conversion.htm
collection: user
fetched_at: 2026-06-22T06:20:39+00:00
sha256: 1baa151fa82d903cfe8892b929b5671e759362c223c0fb8400d70bb74a4ef8bb
---

Document Review Conversion

# Document Review Conversion

This dashboard provides insight into document caching performance within Relativity's Review Interface. It helps users track conversion activity, cache efficiency, and document rendering speeds - key factors that directly affect reviewer performance and overall system responsiveness. Monitoring these patterns helps administrators identify delays caused by cache misses and take steps such as pre-converting frequently accessed documents or adjusting cache configurations to improve review performance.

## Conversion and Cache Efficiency

The Conversion and Cache Efficiency section visualizes metrics that describe how effectively the document viewer leverages cached content versus performing new conversions. The Conversion Cache Miss Rate graph indicates the percentage of documents that required real-time conversion instead of loading from cache. Higher cache miss rates may indicate increased processing times.

### Use Cases

Use Case Description

Monitor cache efficiency Track how frequently documents are loaded from cache versus converted in real time.

Troubleshoot rendering delays Review cache miss and conversion data to determine whether slow document loading stems from real-time conversions, cache invalidation, or document retrieval latency.

Assess viewer performance under load Observe caching effectiveness during periods of increased review activity to ensure the viewer maintains fast rendering as demand increases.
