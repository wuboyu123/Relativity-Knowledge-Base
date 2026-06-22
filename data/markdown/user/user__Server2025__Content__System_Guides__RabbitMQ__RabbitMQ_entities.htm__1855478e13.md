---
title: "RabbitMQ entities"
url: https://help.relativity.com/Server2025/Content/System_Guides/RabbitMQ/RabbitMQ_entities.htm
collection: user
fetched_at: 2026-06-22T06:21:12+00:00
sha256: 1b6120480ac6dc358a5212ecd3ac57158545ea3b8d1be2bf3a00c69a827474a1
---

RabbitMQ entities

# RabbitMQ entities

The following page explains how the Topics and Subscription entities in the Relativity Service Bus translate to the new entities in RabbitMQ. Where service bus has Topics, Subscriptions, and Queues, RabbitMQ has Exchanges, Queues, and Bindings:

- Exchange – serves as message routing mechanisms. There are two types of exchanges used by Relativity:

- Fanout Exchange - each message sent to a fanout exchange has a copy sent to each queue and exchange bound to the fanout exchange receiving the message.

- Direct Exchange – each message sent to a direct exchange has a copy sent to each queue and exchange bound to the direct exchange where the routing key of the message matches the routing key of the binding.

All exchanges used by Relativity are durable which means they persist to disk and survive server restarts.

- Queue – stores messages and delivers them to clients as requested.

- All queues used by Relativity are durable which means they persist to disk and survive server restarts.

- All messages in queues used by Relativity persist to disk and survive server restarts.

- Bindings – rules used to route messages between exchanges and queues.

- In general, a binding between an exchange and another exchange or an exchange and a queue causes a copy of each message sent to the first exchange to be routed to the bound exchange or queue.

- Direct exchanges support bindings with a routing key that will only accept messages when the message’s routing key matches.

For more information, see AMQP 0-9-1 Model on the RabbitMQ website .

Exchanges Queues Bindings

None If a filtered subscription is present: a binding from the fanout exchange to the direct exchange.

Deadletter exchange to forward failed messaged to the subscription’s deadletter queue named {Topic}_{Subscription}-DLE.

Same as subscription Same as subscription

You can use the RabbitMQ management UI to view the current status of entities on the Relativity Service Bus. For more information, see RabbitMQ management UI .
