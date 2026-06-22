---
title: "Conversion Agent connection to RabbitMQ is broken"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/ad07e3b0-631d-4eb5-9ded-2b3b12cdbde4.htm
collection: user
fetched_at: 2026-06-22T06:19:18+00:00
sha256: 17d896a9b47f6bf9e66d7953d6bfdcf3476556b95533723968489a876f2a6557
---

Conversion Agent connection to RabbitMQ is broken Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

ad07e3b0-631d-4eb5-9ded-2b3b12cdbde4

# Conversion Agent connection to RabbitMQ is broken

## Description

This alert is triggered when one or more RabbitMQ queues for the Conversion Agent or Conversion Complete Agent do not have any consumers.

## Resolution Guidance

### Impact When Active

- Conversion jobs will not be processed, resulting in document conversion failures.

- A backlog of unprocessed messages will accumulate in the RabbitMQ queue.

- This may impact downstream systems or workflows that rely on conversion (e.g. document viewer).

### How To Resolve

-

Check the status of the Conversion Agent or Conversion Complete Agent by navigating to the Agents tab in Relativity:

- Login to Relativity.

- Go to the Agents tab.

- Filter by the name containing 'conversion'.

- Enable the agent if it is disabled.

- If enabling the agent does not resolve the alert, follow the steps below.

-

Verify RabbitMQ is running and healthy.

- Check service status: Run rabbitmqctl status on the RabbitMQ server or use your operating system's service manager (e.g. Services MMC on Windows).

- Check the management UI: If enabled, access the RabbitMQ management UI (typically at http://localhost:15672 ) and verify the node and queue health.

- Check queue and consumer counts: In the management UI, navigate to the Queues page, add the Consumers column, and review the relevant queues for message and consumer counts.

- Review logs: Examine RabbitMQ logs for errors or warnings (default location: %APPDATA%\RabbitMQ\log\ on Windows).

- Test connectivity: From the agent host, use telnet <rabbitmq_host> 5672 or a similar tool to confirm network connectivity to RabbitMQ.

-

Restart the RabbitMQ Windows Service, if needed.

-

Ensure network connectivity between the Conversion Agent or Conversion Complete Agent and the RabbitMQ server (check firewalls, DNS, and routing).

-

Confirm the RabbitMQ credentials and connection settings in the the Relativity Instance Settings page.

-

Please refer to the help page at https://help.relativity.com/Server2024/Content/System_Guides/Instance_Setting_Guide/Instance_setting_descriptions.htm

Instance Settings

EnableTLSForServiceBus

Provider

ServiceBusFullyQualifiedDomainName

ServiceNamespace

SharedAccessKey

SharedAccessKeyName

-

After making corrections, enable the Conversion Agent or Conversion Complete Agent and monitor the queue for active consumers.

-

Verify conversion jobs have resumed successfully:

- Confirm Conversion Agent connection to RabbitMQ is broken Relativity alert is recovered.

- Monitor a few documents to ensure that conversions have completed without errors.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query ((labels.rabbitmq_queue_name: conversions_RP*_ConversionAgent_Priority* AND NOT labels.rabbitmq_queue_name: conversions_RP- _ConversionAgent_Priority ) OR labels.rabbitmq_queue_name: conversionresponses_ConversionCompleteAgent_Priority*) AND rabbitmq.consumer.count <= 0

Group Count

Threshold <= 0

Time Window 5 Mins

Frequency 2 Min

### Alert Metric Details

Metric Name: rabbitmq.consumer.count

Metric Description: The alert is triggered when one of the conversion queues has no consumers.

Metric Attributes:

Attribute Name Description

rabbitmq_queue_name The name of the RabbitMQ queue

rabbitmq.consumer.count The number of consumers currently reading from the queue.

On this page

- Conversion Agent connection to RabbitMQ is broken

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
