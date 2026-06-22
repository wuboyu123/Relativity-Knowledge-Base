---
title: "A RabbitMQ node is inactive"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/4fede300-02e8-4fee-b8bb-f1898c5f53f3.htm
collection: user
fetched_at: 2026-06-22T06:18:54+00:00
sha256: 578dafcf02ef6207d452b913c0c7236f363c64185149af754f700b4eac217f02
---

A RabbitMQ node is inactive Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

4fede300-02e8-4fee-b8bb-f1898c5f53f3

# A RabbitMQ node is inactive

## Description

This alert is triggered when a RabbitMQ node becomes inactive, indicating potential messaging disruptions.

## Resolution Guidance

### Impact When Active

- Document conversion jobs will fail, preventing users from viewing documents in the Relativity Viewer.

- A backlog of unprocessed messages will build up in the RabbitMQ queue, increasing system load and delaying job processing.

- Downstream systems and workflows that depend on conversion results (e.g., document previewing or review workflows) may also be affected.

### How To Resolve

Complete the following steps if Agent is unable to connect to RabbitMQ:

- Verify the RabbitMQ server and/or cluster is running by logging into management UI and verifying each expected server is present and displaying as green under nodes. For more information, see RabbitMQ management UI .

- On the Overview tab in the management UI, ensure RabbitMQ is listening on the expected ports:

- amqp: 5672

- amqp/ssl: 5671 (if configured for TLS, see Configure RabbitMQ For TLS )

- http: 15672

- https:15671 (if configured for TLS, see Configure RabbitMQ For TLS )

- Verify RabbitMQ can be reached by navigating to the management page from the affected server(s).

- Additionally, ensure the settings do not contain any trailing or leading whitespace, and ensure the casing matches for RabbitMQ's SharedAccessKey, SharedAccessKeyName, and ServiceNamespace settings.

- Ensure the RabbitMQ user being used for authentication has full permission for the configured virtual host, see Configuring RabbitMQ

## Alert Details

### Alert Condition Details

Name Value Description

Rule Type Elastic Query

Data View metrics-*

Filter Query labels.rabbitmq_node_name : * If the RabbitMQ node exist in the last 45 seconds

Group Count Number of RabbitMQ node exist

Threshold <= 0 If the count is lest than or equal to 0, alert triggers

Time Window Last 45 sec Verified data for last 45 seconds

Frequency 30 sec Checks every 30 sec

### Alert Metric Details

Metric Name: labels.rabbitmq_node_name

Metric Description: RabbitMQ node name

Metric Attributes:

Attribute Name Description Value

labels.rabbitmq_queue_name The name of the RabbitMQ queue.

labels.rabbitmq_vhost_name The name of the RabbitMQ vHost.

On this page

- A RabbitMQ node is inactive

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
