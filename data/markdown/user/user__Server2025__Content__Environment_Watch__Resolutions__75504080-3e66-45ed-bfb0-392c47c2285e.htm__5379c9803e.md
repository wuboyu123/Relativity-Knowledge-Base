---
title: "On-the-Fly Conversion (P1) - Queue Backlog Threshold Exceeded"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/75504080-3e66-45ed-bfb0-392c47c2285e.htm
collection: user
fetched_at: 2026-06-22T06:19:16+00:00
sha256: 903841510df414fc79d1c52817d48a7bd9faaa95abc77744f0831106841c0d5b
---

On-the-Fly Conversion (P1) - Queue Backlog Threshold Exceeded

75504080-3e66-45ed-bfb0-392c47c2285e

# On-the-Fly Conversion (P1) - Queue Backlog Threshold Exceeded

## Description

This alert is triggered when the message backlog in the On-the-Fly Conversion (P1) ConversionAgent and ConversionCompleteAgent queues exceeds 50 messages for more than 5 minutes, indicating potential processing delays.

## Resolution Guidance

### Impact When Active

- A backlog in the On-the-Fly Conversion queue leads to slower or failed document rendering in the viewer, delaying review workflows.

- Risk of further backlog accumulation if not addressed.

### How To Resolve

- In RabbitMQ, locate the affected queues:

- conversions_RP*_ConversionAgent_Priority1*

- conversionresponses_ConversionCompleteAgent_Priority1* Confirm the message count is greater than 50 (the threshold) and observe whether the count is decreasing or increasing/static.

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

This alert monitors the message count of the On-the-Fly Conversion (P1) Conversion Agent and Conversion Complete Agent queues. It triggers if the backlog exceeds 50 messages for more than 5 minutes.

### Alert Condition Details

Name Value Description

Rule Type Metric threshold

Data View metrics-*

Filter Query ((labels.rabbitmq_queue_name: conversions_RP*_ConversionAgent_Priority1* AND NOT labels.rabbitmq_queue_name: conversions_RP- _ConversionAgent_Priority1 ) OR labels.rabbitmq_queue_name: conversionresponses_ConversionCompleteAgent_Priority1* ) Target both P1 conversion queues

Aggregation max Highest queue depth within the time window

Group by labels.rabbitmq_queue_name Evaluate per queue

Threshold >= 50 Alert when queue depth exceeds 50

Time Window 5 minutes Evaluate the last 5 minutes

Frequency 2 minutes Check every 2 minutes

### Alert Metric Details

Metric Name: rabbitmq.message.current

Metric Description: The alert is true when a queue's message count remains above 50 for the last 5 minutes.

Metric Attributes:

Attribute Name Description

labels.rabbitmq_queue_name The name of the RabbitMQ queue

rabbitmq.message.current Current number of messages in the queue
