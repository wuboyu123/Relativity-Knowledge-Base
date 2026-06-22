---
title: "Relativity Service Bus"
url: https://help.relativity.com/Server2025/Content/System_Guides/Relativity_Service_Bus/Relativity_Service_Bus.htm
collection: user
fetched_at: 2026-06-22T06:03:36+00:00
sha256: bf3accc5a02e80e6885c9eb0ed1d7803ff3bbf76af69c863d0261ccb6763cf55
---

Relativity Service Bus

# Relativity Service Bus

Relativity no longer supports Service Bus for Windows. RabbitMQ is now the only the message broker option available for use with Relativity.

The Relativity Service Bus is a message delivery service that communicates information about agent jobs to different application components. This infrastructure feature supports this communication by routing messages between application components. For example, Relativity uses the service bus for submitting conversion jobs to agents and returning converted documents.

Before installing or upgrading, you must install and configure your environment’s message broker. Next, install or upgrade your primary SQL Server and the Relativity Service Bus. You can find information about your environment’s message broker in Pre-installation . For installation instructions, see Relativity installation .

The Relativity Service Bus supports the following features:

- Guaranteed delivery of messages to ensure reliable communication between application components.

- High throughput performance for successful message delivery over the service bus.

- Support for arbitrary messages.

- High scalability to ensure that service bus can support an increasing number of resources added to your Relativity environment.

- Fault tolerance and high availability to guarantee that the service bus continues operating even when a component fails.

## Relativity Service Bus infrastructure

The Relativity Service Bus is built on your environment’s message broker, so it leverages the capabilities offered by these industry-standard software. You must install it on a node in your environment’s message broker. The Relativity installer updates the Instance setting table on your primary SQL Server with information about the location of the Relativity Service Bus that you provide during installation. It updates the following instance settings:

ServiceBusFullyQualifiedDomainName

Table section Relativity.ServiceBus

Value localhost

Description Specifies the fully-qualified domain name for the machine hosting your Relativity Service Bus provider. The Relativity installer automatically sets this value during an installation or upgrade based on the inputs in the RelativityResponse.txt file. For more information, see Relativity installation or Upgrading Relativity Service Bus .

The value for this setting should match the FarmDNS output from the Get-SBFarm command available in the Service Bus PowerShell utility. For more information, see .

When using RabbitMQ, Relativity also supports the IP address for the Server or cluster.

ServiceNamespace

Table section Relativity.ServiceBus

Value Relativity

Description

RabbitMQ - the virtual host to be used by Relativity Service Bus

SharedAccessKey

Table section Relativity.ServiceBus

Value Default value varies by environment.

Description

RabbitMQ - Specifies the value of the Relativity RabbitMQ user’s password used when authenticating.

SharedAccessKeyName

Table Section Relativity.ServiceBus

Value Relativity

Description

RabbitMQ - Specifies Relativity RabbitMQ username used when authenticating.

Provider

Table Section Relativity.ServiceBus

Value RabbitMQ

Description

Specifies the message broker that Relativity will use for Service Bus messaging.

RabbitMQ is the only acceptable value here.

EnableTLSForServiceBus

Table Section Relativity.ServiceBus

Value False

Description

Only used for RabbitMQ. Specifies whether or not client connections to RabbitMQ should use TLS.

If set to True, your RabbitMQ server or cluster must be configured for TLS.

The web and agent servers request information about the location of the Relativity Service Bus from the primary SQL Server. The Relativity Service Bus then facilitates communication between application components by sending and receiving messages. A typical Relativity installation requires only one message broker server. You can optionally configure your environment to have multiple servers. This can be accomplished by leveraging a RabbitMQ cluster. The following diagram illustrates how the Relativity Service Bus integrates with your environment's infrastructure in a typical installation.

## Service Bus installation overview

To install the Relativity Service Bus, you must first install and configure your environment’s message broker. You next run the Relativity installer to add the Relativity Service Bus to your environment and complete other related tasks. The following diagram illustrates the installation process for a typical Relativity installation for service bus. You can optionally install your environment’s message broker on multiple hosts.

Use the following workflow to install the Relativity Service Bus in your environment:

- For a typical installation, install and configure your environment’s message broker. For a high availability configuration, install your environment’s message broker on the servers or VMs for this purpose. For information about installing and configuring a message broker, see RabbitMQ .

- Run the Relativity installer to install or upgrade your primary SQL Server and any necessary distributed servers. For more information, see the following pages :

- New installation - see Relativity installation .

- Upgrade - see Upgrading Relativity Service Bus

For general troubleshooting information, see Troubleshooting RabbitMQ .

- Install or upgrade the Relativity Service Bus server:

- RabbitMQ - Run on any server with network connectivity to both the Primary SQL Server and the RabbitMQ server / cluster.

- Install or upgrade the agent server.

- Install or upgrade the web server.

- Install or upgrade other servers used in your environment. For example, you might install the worker manager or Analytics server depending on your organization’s needs.
