---
title: "System Artifact Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/System_Artifact_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:28:18+00:00
sha256: 1fcbeb70d268ad6e54ac36362b1627f7968e89f862feb2f152c55c2126458ee8
---

System Artifact Manager (.NET)

# System Artifact Manager (.NET)

The System Artifact Manager API exposes the ReadArtifactIDAsync() method used to retrieve the Artifact ID of a system artifact. Use this method when you want to create top-level tabs or object types in a custom application. The system Artifact ID retrieved by this method is then passed to create requests as the parent of the new object that you want to create.

You can also use System Artifact Manager API through REST. For more information, see System Artifact Manager (REST) .

## System Artifact Manager API fundamentals

The System Artifact Manager API includes the following method available on the ISystemArtifactManager interface in the Relativity.ObjectModel.<VersionNumber>.SystemArtifact namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- ReadArtifactIDAsync() method – retrieves the Artifact ID of a system artifact with the specified identifier.

## Retrieve the Artifact ID of a system artifact

Use the ReadArtifactIDAsync() method to retrieve the Artifact ID of a system artifact. Pass the following arguments to this method:

- workspaceID - the workspace containing the system artifact.

- artifactIdentifier - the string identifier for the system artifact.

This method returns an integer representing the Artifact ID of the system artifact.

Use -1 for the workspaceID to refer to the admin workspace.

View code sample.

This code sample illustrates how to add a top-level parent tab to a workspace. It uses the System Artifact Manager API to retrieve the Artifact ID for the system. It then passes this Artifact ID is then CreateAsync() method in the Tab Manager API to create the new tab.

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
public async Task ReadSystemArtifactID()

{

    using (ISystemArtifactManager systemArtifactManager = _serviceFactory.CreateProxy<ISystemArtifactManager>())

    {

        int workspaceID = 1022092;

        string artifactIdentifier = "System";

        int systemArtifactID = await systemArtifactManager.ReadArtifactIDAsync(workspaceID, artifactIdentifier);

        // Use Tab Manager API to create a top-level parent tab in the workspace.

        using (ITabManager tabManager = _serviceFactory.CreateProxy<ITabManager>())

        {

            TabRequest tabRequest = new TabRequest()

            {

                Name = "New Tab",

                Parent = new Securable<ObjectIdentifier>()

                {   // Supply artifactID of "System" as parent identifier

                    Value = new ObjectIdentifier() {ArtifactID = systemArtifactID}

                },

                IsVisible = true,

                LinkType = TabLinkTypeEnum.Parent,

                Order = 500

            };

            TabResponse tabResponse = await tabManager.CreateAsync(workspaceID, tabRequest);

        }

    }

}
```
