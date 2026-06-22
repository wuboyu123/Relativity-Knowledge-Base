---
title: "Relativity REST API architecture"
url: https://platform.relativity.com/Server2025/Content/REST_API/REST_API_concepts/Relativity_REST_API_architecture.htm
collection: developer
fetched_at: 2026-06-22T06:29:44+00:00
sha256: e137a3b11f1e195013cc02fb65fbecbb4f5a998c090a3275e31f19700fa01448
---

Relativity REST API architecture

# Relativity REST API architecture

Using RESTful architectural conventions, the REST API provides you with the ability to access functionality available through the Services API. The REST API passes requests to the Services API, which handles all interactions with the Relativity business engine. You must set up and configure the Services API before you can use the REST API. For information about supported services, see Relativity Server APIs .

The REST API uses named pipes to communicate with the Services API. This communication method offers a fast, in-memory service connection designed to minimize latency in calls made between the two services. Since the system uses named pipes on a localhost, the REST and the Services endpoints must be located on the same machine. Relativity has made significant performance improvements to Services API ensuring that a fast and efficient connection exists between the services. The following diagram illustrates the interconnections between the REST and Services APIs.

In addition, the REST API requires a connection to the Relativity (EDDS) database, which it uses only to load configuration data.
