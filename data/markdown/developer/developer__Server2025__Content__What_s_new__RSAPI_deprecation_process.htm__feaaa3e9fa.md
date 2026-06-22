---
title: "RSAPI deprecation process"
url: https://platform.relativity.com/Server2025/Content/What_s_new/RSAPI_deprecation_process.htm
collection: developer
fetched_at: 2026-06-22T06:22:25+00:00
sha256: 91ba8f743b94e401b1ad715107d537be56fa85dc132faf401a8755e63fe32021
---

RSAPI deprecation process

# RSAPI deprecation process

This page provides a comprehensive set of communications and guidance about the RSAPI removal process.

See this related page:

- RSAPI migration strategy

## API Life cycle summary and definition

This list defines the support offered by Relativity as the APIs transition through different phases of the deprecation life cycle.

The following terms refer to the different phases of the API deprecation life cycle:

- General Availability : In the General Availability (GA) phase, the API is released and available for use.

- Deprecated : In the deprecated phase, we no longer recommend using the API. While deprecated classes and methods are still available, they are tagged obsolete because they will be removed in future releases. You shouldn't use them when implementing new code. Additionally, begin upgrading any existing code, so that it no longer references these obsolete classes and methods.

- Removed : In the removed phase, Relativity no longer exposes the API. Any functionality using the removed API will break.

## Removal process

All RSAPI APIs have been removed in RelativityOne and in Relativity Server 2023.

When What Details

Server 2021 Release Deprecation Tag Similar to the RelativityOne 11.3 release, obsolete tags were added to our 2021 Server release codebase. At this point, there was no impact to customers.

Downloadable Server Patch (Q3 2021) New Kepler APIs A separate, downloadable Server Patch is available to all Server customers since Q3 2021. This patch includes new Kepler APIs like Script Run to help with the transition.

Server 2023 (Q3 2023) RSAPI Removal RSAPI has been removed as of the Relativity Server 2023 release.

## API migration matrix

The following table contains legacy features that have been removed, and links to newer APIs that support similar functionality. The replacement APIs allow code compatibility between Relativity Server and RelativityOne.

To sort the contents, click on a table heading.

RSAPI Feature Deprecated in version Removal schedule Replacement .NET service Replacement REST service Replacement SDK link Replacement release version

Agent Server 2021 Server 2023 Agent Manager (.NET) Agent Manager (REST) Relativity.Server.Infrastructure.SDK 10.0

Batch Server 2021 Server 2023 Batches Manager (.NET) Batches Manager (REST) Relativity.Server.Review.SDK 9.5

Batch Set Server 2021 Server 2023 Batch Sets Manager (.NET) Batch Sets Manager (REST) Relativity.Server.Review.SDK Downloadable Server Patch (Q3 2021)

Choice Server 2021 Server 2023 Choice Manager (.NET) Choice Manager (REST) Relativity.Server.ObjectModel.SDK Server 2021

Client Server 2021 Server 2023 Client Manager (.NET) Client Manager (REST) Relativity.Server.Identity.SDK Downloadable Server Patch (Q3 2021)

Document Server 2021 Server 2023 Document File Manager (.NET)

Object Manager (.NET) Document File Manager (REST)

Object Manager (REST) Relativity.Server.ObjectModel.SDK

Relativity.Server.ObjectManager.SDK 10.3

Error Server 2021 Server 2023 Error Manager (.NET) Error Manager (REST) Relativity.Server.Environment.SDK Downloadable Server Patch (Q3 2021)

Field Server 2021 Server 2023 Field Manager (.NET) Field Manager (REST) Relativity.Server.ObjectModel.SDK 10.2

File Transfer Server 2021 Server 2023 File Field Manager (.NET)

Object Manager (.NET) File Field Manager (REST)

Object Manager (REST)

Import API Relativity.Server.ObjectModel.SDK

Relativity.Server.ObjectManager.SDK

Relativity.Server.Transfer.SDK TBD

Folder Server 2021 Server 2023 Folder Manager (.NET) Folder Manager (REST) Relativity.Server.Services.Interfaces.SDK 9.3

GenerateRelativityAuthenticationToken** Server 2021 Server 2023 Unsupported** Unsupported** N/A N/A

GetAdminChoiceTypes** Server 2021 Server 2023 Unsupported** Unsupported** N/A N/A

GetProcessState** Server 2021 Server 2023 Unsupported** Unsupported** N/A N/A

Group Server 2021 Server 2023 Group Manager (.NET) Group Manager (REST) Relativity.Server.Identity.SDK Downloadable Server Patch (Q3 2021)

Instance Setting Server 2021 Server 2023 Instance Setting Manager (.NET) Instance Setting Manager (REST) Relativity.Server.Environment.SDK 10.2

Layout Server 2021 Server 2023 Layout Manager (.NET) Layout Manager (REST) Relativity.Server.DataVisualization.SDK Downloadable Server Patch (Q3 2021)

Library Application Server 2021 Server 2023 Library Application (.NET) Library Application (REST) Relativity.Server.Environment.SDK 10.3

MarkupSet Server 2021 Server 2023 Object Manager (.NET) Object Manager (REST) Relativity.Server.ObjectManager.SDK 9.5

Matter Server 2021 Server 2023 Matter Manager (.NET) Matter Manager (REST) Relativity.Server.Environment.SDK 10.3

Object Rule Server 2021 Server 2023 Object Rule Manager (.NET) Object Rule Manager (REST) Relativity.Server.DataVisualization.SDK 10.1

ObjectType Server 2021 Server 2023 Object Type Manager (.NET) Object Type Manager (REST) Relativity.Server.ObjectModel.SDK 10.1

Productions Server 2021 Server 2023 Production Manager (.NET) Production Manager (REST) Relativity.Server.Productions.SDK 9.6

Relativity Application (Workspace Level) Server 2021 Server 2023 Export (.NET) Export (REST) Relativity.Server.Environment.SDK Server 2022)

Relativity Dynamic Object (RDO) Server 2021 Server 2023 Object Manager (.NET) Object Manager (REST) Relativity.Server.ObjectManager.SDK 9.5

Resource File Server 2021 Server 2023 Resource File (.NET) Resource File (REST) Relativity.Server.Environment.SDK Server 2022

Resource Pool Server 2021 Server 2023 Resource Server / Resource Pool (.NET / REST) Resource Server / Resource Pool (.NET / REST) Relativity.Server.Infrastructure.SDK Server 2022

Resource Server Server 2021 Server 2023 Resource Server / Resource Pool (.NET / REST) Resource Server / Resource Pool (.NET / REST) Relativity.Server.Infrastructure.SDK Server 2022

Script Run Server 2021 Server 2023 Script Manager (.NET) Script Manager (REST) Relativity.Server.Extensibility.SDK Server 2021

Script Server 2021 Server 2023 Script Manager (.NET) Script Manager (REST) Relativity.Server.Extensibility.SDK Server 2021

Search Server 2021 Server 2023 dtSearch Manager (.NET)

Keyword Search Manager (.NET) for saved searches dtSearch Manager (REST)

Keyword Search Manager (REST) for saved searches Downloadable Server Patch (Q3 2021)

Search Provider Server 2021 Server 2023 Search Provider (.NET) Search Provider (REST) Relativity.Server.Extensibility.SDK 9.3

Tab Server 2021 Server 2023 Tab Manager (.NET) Tab Manager (REST) Relativity.Server.DataVisualization.SDK 10.0

User Server 2021 Server 2023 User Manager (.NET) User Manager (REST) Relativity.Server.Identity.SDK Downloadable Server Patch (Q3 2021)

View Server 2021 Server 2023 View Manager (.NET) View Manager (REST) Relativity.Server.DataVisualization.SDK 9.6

Workspace Server 2021 Server 2023 Workspace Manager (.NET) Workspace Manager (REST) Relativity.Server.Environment.SDK Downloadable Server Patch (Q3 2021)

* New coverage is planned for release and will be available prior to removal.

** This feature is deprecated and will no longer be supported.

## Identifying RSAPI usage

Your code may be relying on RSAPI, even if you are calling Relativity REST services. To determine whether your code is still using RSAPI, you can search for IRSAPIClient in your code if you are calling Relativity .NET APIs, or search for Relativity.REST/Relativity or Relativity.REST/Workspace routes/paths in your code if you are calling Relativity REST endpoints.

## Support

For more information about the RSAPI deprecation process, consult the resources below

- RSAPI migration strategy

- RSAPI Removal Webinar

- Relativity Developer Group for the latest updates

You can also contact our Support team with questions about Relativity's deprecation strategy.

- RSAPI deprecation process

- API Life cycle summary and definition

- Removal process

- API migration matrix

- Identifying RSAPI usage

- Support
