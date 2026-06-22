---
title: "Mass Convert (P3) - Queue Backlog Threshold Exceeded"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/355ae3f2-b016-4aa8-8aab-8fcd9d332d8c.htm
collection: user
fetched_at: 2026-06-22T06:19:15+00:00
sha256: ade3494487315ce51d99897f017a3977672435e257cc058e6d7037681ba4c346
---

Mass Convert (P3) - Queue Backlog Threshold Exceeded

355ae3f2-b016-4aa8-8aab-8fcd9d332d8c

# Mass Convert (P3) - Queue Backlog Threshold Exceeded

## Description

This alert is triggered when the message backlog in the Mass Convert (P3) Conversion Agent or Conversion Complete Agent queues stays above 10,000 messages for more than 20 minutes, indicating processing delays or bottlenecks.

## Resolution Guidance

### Impact When Active

- A backlog in the Mass Conversion queue leads to slower or failed document rendering in the viewer, delaying review workflows.

- May affect batching, tagging, or analytics workflows that depend on timely document conversion.

- Risk of further backlog accumulation if not addressed.

### How To Resolve

- In RabbitMQ, locate the affected queues:

- conversions_RP*_ConversionAgent_Priority3*

- conversionresponses_ConversionCompleteAgent_Priority3* Confirm whether each queue has more than 10,000 messages and observe the trend (decreasing = draining; increasing/static = backlog).

- Queues to check: ConversionAgent / ConversionCompleteAgent.

- Check the message count in each queue.

- Observe the trend:

- Decreasing: Agents are actively processing messages.

- Increasing or static: Agents may be stalled or underperforming.

- Check the status of the ConversionAgent / ConversionCompleteAgent in Relativity:

- Log into Relativity

- Go to the Agents tab

- Filter by name containing 'conversion'

- Check the status and ensure all relevant agents are running as expected.

- Ensure RabbitMQ is running and healthy.

- After remediation, monitor the backlog until it falls below the threshold.

##### You can also try..

If the queue continues to remain backlogged. You can try following:

- Restart the kCura services on the Conversion Agent servers.

- Review system resources (CPU, memory, disk) on Conversion Agent and RabbitMQ hosts.

## Alert Details

This alert monitors the message count of the Mass Convert (Priority 3) Conversion Agent and Conversion Complete Agent queues. It triggers if the backlog exceeds 10,000 messages for more than 20 minutes.

### Alert Condition Details

Name Value Description

Rule Type Metric threshold

Data View metrics-*

Filter Query ((labels.rabbitmq_queue_name: conversions_RP*_ConversionAgent_Priority3* AND NOT labels.rabbitmq_queue_name: conversions_RP- _ConversionAgent_Priority3 ) OR labels.rabbitmq_queue_name: conversionresponses_ConversionCompleteAgent_Priority3* ) Target both P3 conversion queues

Aggregation max Highest queue depth within the time window

Group by labels.rabbitmq_queue_name Evaluate per queue

Threshold >= 10000 Alert when queue depth exceeds 10,000

Time Window 20 minutes Evaluate the last 20 minutes

Frequency 2 minutes Check every 2 minutes

### Alert Metric Details

Metric Name: rabbitmq.message.current

Metric Description: The alert is true when a queue's message count remains above 10,000 for the last 20 minutes.

Metric Attributes:

Attribute Name Description

labels.rabbitmq_queue_name The name of the RabbitMQ queue

rabbitmq.message.current Current number of messages in the queue
