---
title: "Convert Ahead (P2) - Queue Backlog Threshold Exceeded"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/3e34cb20-f810-48ef-b2fc-a4e2dc91ceb6.htm
collection: user
fetched_at: 2026-06-22T06:19:13+00:00
sha256: f06c5694dffbf37c3737f98ee3e516b619a65059309fe4eb42c548660df84eae
---

Convert Ahead (P2) - Queue Backlog Threshold Exceeded Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

3e34cb20-f810-48ef-b2fc-a4e2dc91ceb6

# Convert Ahead (P2) - Queue Backlog Threshold Exceeded

## Description

This alert is triggered when the message backlog in the Convert Ahead (P2) ConversionAgent and ConversionCompleteAgent queues exceeds 1,000 messages for more than 10 minutes, indicating potential processing delays.

## Resolution Guidance

### Impact When Active

- A backlog in the Convert Ahead Conversion queue leads to slower or failed document rendering in the viewer, delaying review workflows.

- Risk of further backlog accumulation if not addressed.

### How To Resolve

- In RabbitMQ, locate the affected queues:

- conversions_RP*_ConversionAgent_Priority2*

- conversionresponses_ConversionCompleteAgent_Priority2* Confirm the message count is greater than 1,000 (the threshold) and observe whether the count is decreasing or increasing/static.

- Queues to check: ConversionAgent / ConversionCompleteAgent.

- Check the message count in each queue.

- Observe the trend:

- Decreasing: Agents are actively processing messages.

- Increasing or static: Agents may be stalled or underperforming.

- Check the status of the ConversionAgent / ConversionCompleteAgent in Relativity:

- Log into Relativity

- Go to the Agents tab

- Filter by name containing 'conversion'

- Ensure RabbitMQ is running and healthy.

- After remediation, monitor the backlog until it falls below the threshold.

##### You can also try..

If the queue continues to remain backlogged. You can try following:

- Restart the kCura services on the Conversion Agent servers.

- Review system resources (CPU, memory, disk) on Conversion Agent and RabbitMQ hosts.

## Alert Details

This alert monitors the message count of the Mass Convert (Priority 2) Conversion Agent and Conversion Complete Agent queues. It triggers if the backlog exceeds 1,000 messages for more than 10 minutes.

### Alert Condition Details

Name Value Description

Rule Type Metric threshold

Data View metrics-*

Filter Query ((labels.rabbitmq_queue_name: conversions_RP*_ConversionAgent_Priority2* AND NOT labels.rabbitmq_queue_name: conversions_RP- _ConversionAgent_Priority2 ) OR labels.rabbitmq_queue_name: conversionresponses_ConversionCompleteAgent_Priority2* ) Target both P2 conversion queues

Aggregation max Highest queue depth within the time window

Group by labels.rabbitmq_queue_name Evaluate per queue

Threshold >= 1000 Alert when queue depth exceeds 1,000

Time Window 10 minutes Evaluate the last 10 minutes

Frequency 2 minutes Check every 2 minutes

### Alert Metric Details

Metric Name: rabbitmq.message.current

Metric Description: The alert is true when a queue's message count remains above 1,000 for the last 10 minutes.

Metric Attributes:

Attribute Name Description

labels.rabbitmq_queue_name The name of the RabbitMQ queue

rabbitmq.message.current Current number of messages in the queue

On this page

- Convert Ahead (P2) - Queue Backlog Threshold Exceeded

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

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
