---
title: "IIS Latency"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/IIS_Latency.htm
collection: user
fetched_at: 2026-06-22T06:20:49+00:00
sha256: 296fb43cc6234a6e681f503f909ecd930145ceea38f5c2ee3cb8423536518674
---

IIS Latency

# IIS Latency

This dashboard provides visibility into the response times of IIS-hosted services across your Relativity environment. It helps users to monitor web request performance, detect slow endpoints, and identify latency patterns that could impact user experience or system responsiveness. It plays a vital role in performance monitoring and post-installation validation . By tracking both request and redirection times, users can quickly isolate inefficiencies in API or web component responses, ensuring Relativity's web layer performs optimally.

## Latency Overview and Slowest Requests

The IIS Latency dashboard provides a summary of key timing metrics at the top of the view, including 'maximum response time' and 'maximum redirection time', giving administrators an at-a-glance understanding of system performance during the selected time window. Below the summary metrics, two data tables list the 'Top 20 Slowest POST Requests' and 'Top 20 Slowest GET Requests', with detailed response times per endpoint. These tables highlight which API calls or web requests experience the most latency, helping identify bottlenecks caused by inefficient code, overloaded services, or slow backend dependencies. By reviewing the endpoints with the highest average response times, users can target specific areas for optimization or confirm whether performance degradation aligns with known workload spikes.

### Use Cases

Use Case Description

Detect slow or inefficient endpoints Use latency tables to identify IIS endpoints with consistently long response times, pinpointing inefficient APIs or services needing optimization.

Troubleshoot user-reported delays Correlate reports of web interface slowness with specific high-latency endpoints to determine whether IIS or backend services are the source.

Benchmark performance Use latency data to establish performance baselines, compare response trends over time, and evaluate the impact of infrastructure or configuration changes on IIS performance.
