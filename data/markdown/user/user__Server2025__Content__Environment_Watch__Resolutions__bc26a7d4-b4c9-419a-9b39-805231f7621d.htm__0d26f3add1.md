---
title: "CPU has been exceeding threshold on at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/bc26a7d4-b4c9-419a-9b39-805231f7621d.htm
collection: user
fetched_at: 2026-06-22T06:19:07+00:00
sha256: a6cce121f772873ce784e5cc78f6b98df1659888bb22b9b0f131d85a901ae9c0
---

CPU has been exceeding threshold on at least one host Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

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

On this page

- CPU has been exceeding threshold on at least one host

- Description

- Resolution Guidance

- Impact When Active

- To resolve this alert, you can try below steps:

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
