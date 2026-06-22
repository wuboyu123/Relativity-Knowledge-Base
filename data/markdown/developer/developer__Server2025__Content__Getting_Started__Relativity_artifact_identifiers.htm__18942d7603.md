---
title: "Relativity artifact identifiers"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Relativity_artifact_identifiers.htm
collection: developer
fetched_at: 2026-06-22T06:29:21+00:00
sha256: 4a42d5a358d33f11713996a070629bb7ddb55cdcd2c385c0bc7cf9a474be991c
---

Relativity artifact identifiers

# Relativity artifact identifiers

Most of the Relativity data are stored in the database as artifacts . You can use several key values, including artifact IDs, artifact types, and GUIDs, to interact with the artifacts through the Relativity APIs.

## Artifact ID

Relativity artifacts are identified by unique Artifact IDs, corresponding to the primary database table identifier. The following is an example of querying the Documents table workspace database with the Artifact ID.

You can also find the Artifact ID from the Relativity user interface. The following is an example of the Documents view displaying the Artifact ID field.

The following is an example of the Workspaces view displaying the Case Artifact ID field.

Artifact ID is widely used when interacting with objects through the Relativity APIs. ArtifactID is a property of the generic Artifact class. The property is also available on all strongly-typed data transfer objects (DTOs).

The artifact ID is also used when interacting with the data through the REST API . It is returned as a JSON property of all Relativity objects.

All IDs (including Artifact IDs) are unique only within the scope of a single workspace. It is possible that an Artifact ID may be the same for two items in different workspaces, for example. To ensure unique identifiers, use the GUID instead.

## Artifact type

Artifact type designates the type of Relativity artifact, for example, users, layouts, views, field, and choices.

Artifact type values are stored in the workspace database table.

Note that in the Services API, objects are created as strongly-typed DTOs (with the type already build-in). In cases when you need to reference common artifact types, use the ArtifactType enumeration.

Member name Value Description

Batch 27 ArtifactType of Batch

BatchSet 24 ArtifactType of BatchSet

Case 8 ArtifactType of Workspace or Case

Client 5 ArtifactType of Client

Code 7 ArtifactType of Code or Choice

Document 10 ArtifactType of Document

Error 18 ArtifactType of Error

Field 14 ArtifactType of Field

Folder 9 ArtifactType of Folder

Group 3 ArtifactType of Group

Layout 16 ArtifactType of Layout

Matter 6 ArtifactType of ResourceServer

MarkupSet 22 ArtifactType of MarkupSet

ObjectType 25 ArtifactType of ObjectType

RelativityScript 28 ArtifactType of RelativityScript

ResourcePool 31 ArtifactType of ResourcePool

ResourceServer 32 ArtifactType of ResourceServer

SearchIndex 29 ArtifactType of SearchIndex

Search 15 ArtifactType of Search

Tab 23 ArtifactType of Tab

User 2 ArtifactType of User

View 4 ArtifactType of View

## GUID

Relativity objects are identified by the GUIDs as well as Artifact ID. You can find object GUIDS by using the application in Developer Mode. For more information, see View component GUIDs .

You can also query Relativity database to find object GUIDs. The following example illustrates how to find workspace GUIDs by joining edds.Case and edds.ArtifactGuid tables on ArtifactID:

Unique GUIDs enable application portability across Relativity instances and databases. When developing custom Relativity applications, it is strongly recommended that you use GUIDs when referring to Fields, object types, and Choices. This approach offers significant advantages over programming against artifact name or artifact IDs (that may not be unique) when using the Application Deployment System (ADS). For more information, see Best practices for building applications .
