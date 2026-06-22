---
title: "Analytics engine heap memory exceeds 95% on at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/2153195e-2fff-49ee-a636-75d85c4910ed.htm
collection: user
fetched_at: 2026-06-22T06:19:12+00:00
sha256: f42b4661318cc27e9519b337a43a0c821af86d3e9e03af883e080ca644ebe74e
---

Analytics engine heap memory exceeds 95% on at least one host Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

2153195e-2fff-49ee-a636-75d85c4910ed

# Analytics engine heap memory exceeds 95% on at least one host

## Description

This alert is triggered when the Analytics engine heap memory usage reaches or exceeds the defined threshold while a job is actively running, indicating potential performance degradation or memory leaks.

## Resolution Guidance

### Impact When Active

When this alert is active, it indicates that the heap memory on the Analytics engine has reached or exceeded a critical threshold. This can result in:

- Slower processing of large data sets

- Job failures or unexpected behavior due to insufficient memory

- Potential memory leaks causing long-term stability issues

### How To Resolve

- Identify Active Analytics Jobs

- Check which jobs are currently running on the Analytics engine. Focus on:

- Large index builds

- Structured analytics jobs

- Concurrent operations

- Use Relativity Job Monitor or database queries to identify active workloads.

- Review Heap Usage

- Query the memory_used_pct field in metrics-* index to confirm actual heap usage.

- If memory usage remains consistently over 90-95%, continue with steps below.

- Evaluate JVM Heap Size Configuration Check current JVM settings (-Xmx and -Xms) in env.cmd file: \CAAT\bin\env.cmd

#### General Sizing Guidelines (from Relativity):

Server Role Recommended -Xmx

Structured Analytics only ~85% of total RAM (leave 10 GB for DB)

Indexing only ~85% of total RAM (leave 10 GB for DB)

Combined (Indexing + Structured) ~85% of total RAM (leave 10 GB for DB)

Copy

```text
Adjust -Xmx accordingly and restart the CAAT service for changes to apply.

Follow the instructions provided in the [Relativity documentation](https://help.relativity.com/Server2024/Content/System_Guides/Environment_Optimization_Guide/Configuring_the_Analytics_server.htm#JavaheapsizeJVM) for configuring the CAAT environment.

```

- Optimize or Restructure Workloads

- Break up large analytics jobs into smaller batches.

- Optimize training sets and reduce number of documents per job.

- Avoid concurrent resource-intensive jobs on the same server.

- Disable Unused Analytics Indexes

- Navigate to any unused Analytics indexes and click "Disable Queries" to free RAM.

- Restart CAAT if Memory Is Fully Consumed

- If the Analytics engine becomes unresponsive:

- Restart the Relativity Analytics Engine (CAAT) Windows service.

### Long-Term Recommendations

- Monitor heap usage trends using telemetry or APM tools.

- Increase physical memory if usage consistently trends high.

- Scale horizontally by adding dedicated servers for indexing or structured analytics.

- Follow Relativity's memory formula: Documents * 6000 = JVM bytes required e.g., 1M docs ˜ 6 GB heap

## Alert Details

### Alert Condition Details

Name Value Description

Rule Type Elasticsearch query

Data View metrics-*

Filter Query (doc['jvm.memory.used'].value / doc['jvm.memory.limit'].value) * 100 > 95 To fetch the data when analytics engine heap memory usage exceeds 95%

Threshold > 95% When analytics engine heap memory usage exceeds 95% alert triggers

Time Window 5min Verified data for last 5 minutes

Rule schedule 1 minute Checks for every 1 minute

### Alert Metric Details

Metric Name: jvm.memory.used

Metric Description: The alert triggers when jvm.memory.used reaches 95% of the allocated heap memory.

Metric Attributes:

Attribute Name Description Value

jvm.memory.limit Indicates the maximum memory allocation for the JVM in bytes Amount of memory available to the JVM

jvm.memory.used Indicates the amount of memory used by the JVM in bytes Amount of memory used by the JVM

On this page

- Analytics engine heap memory exceeds 95% on at least one host

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- Long-Term Recommendations

- Alert Details

- Alert Condition Details

- Alert Metric Details


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
