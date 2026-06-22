---
title: "Resource Server / Resource Pool (.NET / REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Infrastructure/Resource_Server_Resource_Pool_API.htm
collection: developer
fetched_at: 2026-06-22T06:27:58+00:00
sha256: 6a0b1a97382437e3f743333ada31ab3ce4b2289f406a84d85b6bcb47b997639a
---

Resource Server / Resource Pool (.NET / REST)

# Resource Server / Resource Pool (.NET / REST)

The Resource Server / Resource Pool APIs provide endpoints to interact with Relativity servers. The type of interaction is based on the type of server. All server types support read and update operations. Some server types also support create and delete operations, console actions, and other operations.

Use cases for these APIs include:

- Checking the status of Relativity servers

- Manipulating agents

- Restarting services on servers

- Manipulating server credentials

You can download the Relativity.Infrastructure.SDK to use the service through .NET.

You can also use this service through REST. The Infrastructure package linked above contains an OpenAPI.json file that should be used with the Swagger workflow to review the available REST API endpoint documentation for Resource Server / Resource Pool operations.

## Resource Server / Resource Pool fundamentals

### Overview

The service is accessible by instantiating a proxy using contracts defined in the Relativity.Infrastructure.{versionNumber} namespace.

For general actions on resource servers, use the nuget package and a proxy for a contract. This proxy allows one to retrieve available server types, eligible server status values as well as metadata for a particular server, without specifying the type.

The methods on these APIs operate on the admin level context. Ensure that users have appropriate permissions.

### REST guidelines

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

### Server types

The following table pairs the Server Type in Relativity to the relevant API interface namespace.

Server Type on Servers tab in Relativity API interface namespaces

Agent Relativity.Infrastructure.{versionNumber}.AgentServerManager.IAgentServerManager

Analytics Server Relativity.Infrastructure.{versionNumber}.AnalyticsServer.IAnalyticsServerManager

Cache Location Server Relativity.Infrastructure.{versionNumber}.CacheLocationServer.ICacheLocationServerManager

Fileshare Relativity.Infrastructure.{versionNumber}.FileRepositoryServer.IFileRepositoryServerManager

any type Relativity.Infrastructure.{versionNumber}.ResourceServer.IResourceServerManager

Services Relativity.Infrastructure.{versionNumber}.ServicesServer.IServicesServerManager

SQL - Distributed Relativity.Infrastructure.{versionNumber}.SQLDistributed.ISqlDistributedServerManager

SQL - Primary Relativity.Infrastructure.{versionNumber}.SQLPrimary.ISqlPrimaryServerManager

WebAPI:Forms Authentication Relativity.Infrastructure.{versionNumber}.WebApiFormsAuthServerManager.IWebApiFormsAuthServerManager

WebAPI Relativity.Infrastructure.{versionNumber}.WebApiServer.IWebApiServerManager

WebAPI:AD Authentication Relativity.Infrastructure.{versionNumber}.WebApiWindowsAuthServer.IWebApiWindowsAuthServerManager

Web Background Processing Relativity.Infrastructure.{versionNumber}.WebBackgroundProcessingServer.IWebBackgroundProcessingServerManager

Web - Distributed:Forms Authentication Relativity.Infrastructure.{versionNumber}.WebDistributedFormsAuthServer.IWebDistributedFormsAuthServerManager

Web - Distributed Relativity.Infrastructure.{versionNumber}.WebDistributedServer.IWebDistributedServerManager

Web - Distributed:AD Authentication Relativity.Infrastructure.{versionNumber}.WebDistributedWindowsAuthServer.IWebDistributedWindowsAuthServerManager

Web:Forms Authentication Relativity.Infrastructure.{versionNumber}.WebFormsAuthServer.IWebFormsAuthServerManager

Web Relativity.Infrastructure.{versionNumber}.WebServerManager.IWebServerManager

Web:AD Authentication Relativity.Infrastructure.{versionNumber}.WebWindowsAuthServer.IWebWindowsAuthServerManager

Worker Manager Server Relativity.Infrastructure.{versionNumber}.WorkerManagerServer.IWorkerManagerServerManager

Worker Relativity.Infrastructure.{versionNumber}.WorkerServer.IWorkerServerManager
