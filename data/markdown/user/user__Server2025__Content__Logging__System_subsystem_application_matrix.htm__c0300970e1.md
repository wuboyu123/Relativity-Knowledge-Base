---
title: "System-subsystem-application matrix for logging"
url: https://help.relativity.com/Server2025/Content/Logging/System_subsystem_application_matrix.htm
collection: user
fetched_at: 2026-06-22T06:06:07+00:00
sha256: 5c72337c80086c5a4017e6ab05e75d05420d72e38a938953c608a28c186f7fdf
---

System-subsystem-application matrix for logging

# Logging system-subsystem-application matrix

You can identify Relativity system components that log messages based on the system-subsystem-application designation. When troubleshooting, use the system-subsystem-application matrix to configure logging to target specific Relativity components.

## Relativity systems

Systems are the top-level components of Relativity. They are typically IIS applications, Windows services, or executables.

Logging systems are as follows:

System

Description

Agent Agent windows service running as kCura EDDS Agent Manager .

Invariant Relativity Invariant processing and conversion engine.

Relativity Relativity web site under IIS installed by default as /Relativity .

RelativityDistributed Relativity web site for downloads installed by default as /Relativity.Distributed .

RelativityRest Relativity RESTful web services installed by default as /Relativity.Rest .

RelativityServices Relativity web services installed by default as /Relativity.Services .

RelativityWebAPI Relativity web services installed by default as /RelativityWebAPI .

ServiceHost Windows service for running hosted services. Installed by default as kCura Service Host Manager .

WebProcessing

Agent windows service running as kCura EDDS Web Processing Manager .

The following image presents the Relativity components hosted in IIS. They correspond to the logging systems listed in the table above.

## Subsystems

Subsystems are Relativity components called from one or more systems. Generally, they are designated based on similar functionality.

Logging subsystems are as follows:

Subsystem

Description

Container Web API for dynamic endpoints for RESTful services.

CustomAgent Background process of an agent that is part of an application or a resource file.

CustomPage Custom Pages are IIS applications deployed under /Relativity/CustomPage/<GUID> .

EventHandler Event handlers that run custom code build on the Relativity platform.

HealthCheck Enables Information level health check logs to be persisted without requiring the overall log level to be set to Information.

IdentityServer Authentication server that is used for managing tokens for user login.

Kepler Web API for dynamic endpoints for RESTful services.

RelativityAgent Background process of an agent that is part of the Relativity.

InvariantAPI Invariant API hosted in the Invariant Queue Manager service for processing and conversion requests.

InvariantAdminAPI Invariant Admin API hosted in the Invariant Queue Manager service for managing processing workers.

## Relativity applications

Applications are unique identifiers of the context the code is running in. Applications are identified by GUID.

Logging applications are as follows:

Application Description

51b4e374-ef1b-43a0-b5a8-e2841ac3efe1 Analytics

62284add-91f5-4f35-a582-bbcfa439ad8c Analytics Core

81ceb2f0-747a-4e8b-aad5-7c40d864d96d Assisted Review

62ab9904-2f5e-442e-9d5e-259636eae79c Binders

6a8c2341-6888-44da-b1a4-5bdce0d1a383 Data Grid Core

293c50ad-7b6d-45d0-9121-7f3826e1cca5 Data Grid for Audit

3e86b18f-8b55-45c4-9a57-9e0cbd7baf46 Default (Resource File Default)

5725cab5-ee63-4155-b227-c74cc9e26a76 Document Viewer

5975ec2c-ef13-4358-a062-aff4891b2343 Fact Manager

c9e4322e-6bd8-4a37-ae9e-c3c9be31776b Imaging

3e258ac2-2b63-498e-a895-9515ecea8df4 Layout Builder

e5fdddf9-b55b-454c-8d96-b8285d0de2be Lists

901c56a1-bdbc-4b48-a5e9-fe3f17211149 Mass Operation Handler

8354d537-689a-4dde-b057-5ef2fe4dba2b OCR

60a1d0a3-2797-4fb3-a260-614cbfd3fa0d Performance Dashboard

ed0e23f9-da60-4298-af9a-ae6a9b6a9319 Processing

51b19ab2-3d45-406c-a85e-f98c01b033ec Production

98f31698-90a0-4ead-87e3-dac723fed2a6 Relativity Legal Hold

2ff16b11-a4ca-4f02-8bbb-1f07f23fe713 Relativity List Page

3d20c75d-e2a8-468d-86c3-7544c035a11d Relativity Telemetry

3b884f04-f8ec-45f3-8427-2fdbeed9bbfc Review Manager

f807ac5a-6f0c-4ef3-9c7d-db2bae51a5f4 Search Terms Report

Custom Relativity applications can also use logging and be identified by GUID.
