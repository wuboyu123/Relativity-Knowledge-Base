---
title: "dtSearch Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_dtSearch/dtSearch_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:50+00:00
sha256: f4ba7c3805ffbd9f5ffc6fadd32635d8207598e8073c39ac276d01aaea120ecd
---

dtSearch Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# dtSearch Manager (.NET)

Relativity's dtSearch engine provides advanced search functionality such as proximity, stemming, fuzzy searches, and Boolean operators. For more information, see dtSearch on the Relativity Documentation site.

In order to perform a dtSearch search, you must build and activate a dtSearch index. The dtSearch Index Manager API exposes these operations, and others, letting you programmatically manage dtSearch Indexes. A sample use case for the dtSearch Manager API is creating a custom application to programmatically run through the stages of index build rather than manually performing these tasks through the Relativity UI.

You can also use the dtSearch Manager API services through REST. These interfaces support the same functionality as the .NET interfaces. For more information, see dtSearch Manager Service .

## Fundamentals for the dtSearch Manager API

Review the following information to learn about the methods used by the dtSearch Index Manager service. In order to use the service, the instance must have the Relativity.DtSearch RAP installed. This is a required application and is available in the Application library.

### Methods

The Relativity.Compute.dtSearch.Services.Interfaces namespace contains the IDtSearchIndexManager interface that exposes the following methods.

- CreateAsync() method - adds a new dtSearch index to the workspace. It returns the Artifact ID of the newly created dtSearch Index. See Create a dtSearch index .

- UpdateAsync() method - updates an existing dtSearch index . See Update a dtSearch index .

- ReadAsync() method - retrieves metadata information about a dtSearch index. This method takes the Artifact ID of the workspace and the Artifact ID of the dtSearch index and returns DtSearchIndexResponse object. See Retrieve index metadata .

- DeleteAsync() method - deletes an existing dtSearch index. See Delete index.

- MoveIndexAsync() method - moves an existing dtSearch index. See Move index .

- FullBuildIndexAsync() method - initiates a full index build operation on the specified dtSearch index in a workspace. This method takes the Artifact ID of the workspace, Artifact ID of the dtSearch Index, and a Boolean value to indicate whether to activate or deactivate the index after the build operation successfully completes. See Build Index: Full .

- IncrementalBuildIndexAsync() method - initiates an incremental build operation on the specified dtSearch index in a workspace. This method takes the Artifact ID of the workspace, the Artifact ID of the dtSearch index, and a Boolean value to indicate whether to activate or deactivate the index after the build operation successfully completes. See Build Index: Incremental .

- BuildIndexAsync() method - initiates an incremental dtSearch build operation if possible. If not, then a full dtSearch index build operation occurs for the specified dtSearch index in a workspace. This method takes the Artifact ID of the workspace, the Artifact ID of the dtSearch index, and a Boolean value to indicate whether to activate or deactivate the index after the build operation successfully completes. See Run Build dtSearch Index .

- SwapIndexAsync() method - swaps the search provider metadata. This method takes the Artifact ID of the workspace and the Artifact ID for the current search provider and the Artifact ID of the new Search Provider. See Swap a dtSearch index .

- CompressIndexAsync() method - initiates a Compress Job on the dtSearch index . This method takes the Artifact ID of the workspace and the Artifact ID of the dtSearch index. See Compress a dtSearch index .

- ActivateIndexAsync() method - activates a dtSearch index. This method takes the Artifact ID of the workspace and the Artifact ID of the dtSearch index. See Activate a dtSearch index .

- DeactivateIndexAsync() method - deactivates a dtSearch Index. This method takes the Artifact ID of the workspace and the Artifact ID of the dtSearch index . See Deactivate a dtSearch index .

- CancelIndexBuildAsync() method - cancels any queued/ongoing dtSearch index build operation. This method takes the Artifact ID of the workspace and the Artifact ID of the dtSearch index. See Cancel a dtSearch index build .

- RetryErrorsAsync() method - retries any document/index level errors on the dtSearch index build . This method takes the Artifact ID of the workspace and the Artifact ID of the dtSearch index . See Retry errors on a dtSearch index .

## CRUD operations

The dtSearch Manager API supports create, read, update, and delete operations on dtSearch indexes.

### Create a dtSearch index

The following code sample illustrates how to create a dtSearch using the CreateAsync() method of the IdtSearchIndexManager interface.:

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
public async Task<int> CreateDtSearchIndexAsync(int workspaceId, string alphabetText, string emailAddress, int indexSharedId, string name, string defaultNoiseWords, int savedSearchId)

{

    using (var dtSearchManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        DtSearchIndexRequest request = new DtSearchIndexRequest()

        {

            AccentSensitive = true,

            AlphabetText = alphabetText,

            DirtySettings = string.Empty,

            EmailAddress = emailAddress,

            FragmentationThreshold = 9,

            IndexShareCodeArtifactID = indexSharedId,

            Name = name,

            NoiseWords = defaultNoiseWords,

            Order = 1,

            Priority = 1,

            RecognizeDates = false,

            SearchSearchID = savedSearchId,

            SkipNumericValues = false,

            SubIndexSize = 1000

        };

        //returns artifactId of the newly created dtsearch index

        return await dtSearchManagerService.CreateAsync(workspaceId, request);

    }

}
```

### Retrieve index metadata

The following code sample illustrates how to read a dtSearch DTO using the ReadAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task<DtSearchIndexResponse> GetDtSearchIndexAsync(int workspaceId, int dtSearchArtifactId)

{

    using (var dtSearchManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        return await dtSearchManagerService.ReadAsync(workspaceId, dtSearchArtifactId);

    }

}
```

### Update a dtSearch index

The following code sample illustrates how to update a dtSearch using the UpdateAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task UpdateDtSearchIndexAsync(int workspaceId, int dtSearchArtifactId, DtSearchIndexRequest updatedDtSearchReq)

{

    using (var dtSearchManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchManagerService.UpdateAsync(workspaceId, dtSearchArtifactId, updatedDtSearchReq);

    }

}
```

### Delete a dtSearch index

The following code sample illustrates how to delete a dtSearch using the DeleteAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task DeleteDtSearchIndexAsync(int workspaceId, int dtSearchArtifactId)

{

    using (var dtSearchManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchManagerService.DeleteAsync(workspaceId, dtSearchArtifactId);

    }

}
```

### Move a dtSearch index

The following code sample illustrates how to move a dtSearch using the MoveIndexAsync() method of the IdtSearchIndexManager interface:

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
public async Task MoveDtSearchIndex(Relativity.Services.ServiceProxy.ServiceFactory factory, int workspaceID, int dtSearchArtifactID)

{

    using (var proxy = factory.CreateProxy<IDtSearchIndexManager>())

    {

        // POST https://<hostname>/Relativity.Rest/API/relativity-dtsearch/v1/workspaces/{workspaceID:int}/dtsearch-indexes/{dtsearchArtifactID:int}/move-index

        await proxy.MoveIndexAsync(workspaceID, dtSearchArtifactID);

    }

}
```

## Index build operations

The dtSearch Manager API supports programmatically managing index builds, activation, and other operations performed in Relativity on the dtSearch index console. For more information, see on the Relativity Documentation site.

### Build Index: Full

You must run a full build after initially creating a dtSearch index. The following code sample illustrates how to run a full index build on a dtSearch index using the FullBuildIndexAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task RunFullBuildAsync(int workspaceId, int dtSearchArtifactId, bool activateIndex)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.FullBuildIndexAsync(workspaceId, dtSearchArtifactId, activateIndex);

    }

}
```

### Build Index: Incremental

You can run an incremental build after adding or removing documents from your search. The following code sample illustrates how to run an incremental index build on a dtSearch index using the IncrementalBuildIndexAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task RunIncrementalBuildAsync(int workspaceId, int dtSearchArtifactId, bool activateIndex)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.IncrementalBuildIndexAsync(workspaceId, dtSearchArtifactId, activateIndex);

    }

}
```

### Build Index

The following code sample illustrates how to run a build that first initiates an incremental dtSearch index build operation, if possible, or else runs a full dtSearch index build operation. This uses the RunBuildAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task RunBuildAsync(int workspaceId, int dtSearchArtifactId, bool activateIndex)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.BuildIndexAsync(workspaceId, dtSearchArtifactId, activateIndex);

    }

}
```

### Cancel a dtSearch index build

The following code sample illustrates how to cancel a dtSearch index build using the CancelIndexBuildAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task CancelIndexBuildAsync(int workspaceId, int dtSearchArtifactId)

{

    using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.CancelBuildIndexAsync(workspaceId, dtSearchIndexId);

    }

}
```

### Activate a dtSearch index

The following code sample illustrates how to activate a dtSearch index for searching using the ActivateIndexAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task ActivateDtSearchIndexAsync(int workspaceId, int dtSearchArtifactId)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.ActivateIndexAsync(workspaceId, dtSearchId);

    }

}
```

### Deactivate a dtSearch index

The following code sample illustrates how to deactivate a dtSearch index using the DeactivateIndexAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task DeactivateDtSearchIndexAsync(int workspaceId, int dtSearchArtifactId)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.DeactivateIndexAsync(workspaceId, dtSearchId);

    }

}
```

### Compress a dtSearch index

You can compress a dtSearch index returning all sub-indexes with a fragmentation level greater than zero to a fragmentation level of zero. The following code sample illustrates how to compress a dtSearch index using the CompressIndexAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task RunCompressAsync(int workspaceId, int dtSearchArtifactId, bool activateIndex)

{

    using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.CompressIndexAsync(workspaceId, dtSearchArtifactId, activateIndex);

    }

}
```

### Swap a dtSearch index

You can swap your index with a replacement index in order to use its resources while your index builds or is inactive or disabled for any reason. The following code sample illustrates how to swap a dtSearch index using the SwapIndexAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task SwapDtSearchIndex(int workspaceId, int currentIndexId, int newIndexId)

{

    using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.SwapIndexAsync(workspaceId, currentIndexId, newIndexId);

    }

}
```

### Retry errors on a dtSearch index

The following code sample illustrates how to retry errors on a dtSearch index using the RetryErrorsAsync() method of the IdtSearchIndexManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task RetryErrorsAsync(int workspaceId, int dtSearchArtifactId)

{

    using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

    {

        await dtSearchIndexManagerService.RetryErrorsAsync(workspaceId, dtSearchId);

    }

}
```

## Helper methods

The dtSearch Manager API provides the following helper methods for returning workspace parameters for populating dtSearch saved search properties.

### Get active indexes

The following illustrates how to get a list of active indexes for a given workspace:

Copy

```text
1
2
3
4
5
6
7
public async Task<NameIDPair> GetActiveIndexes(int workspaceId)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

{

return await dtSearchIndexManagerService.GetActiveIndexes(workspaceId);

}

}
```

### Get saved searches

The following illustrates how to get a list of saved searches for a given workspace:

Copy

```text
1
2
3
4
5
6
7
public async Task<NameIDPair> GetSavedSearches(int workspaceId)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

{

return await dtSearchIndexManagerService.GetSearchableSetAsync(workspaceId);

}

}
```

### Get index share locations

The following illustrates how to get a list of index share locations for a given workspace:

Copy

```text
1
2
3
4
5
6
7
public async Task<NameIdPair> GetIndexShareLocationAsync(int workspaceId)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

{

return await dtSearchIndexManagerService.GetIndexShareLocationAsync(workspaceId);

}

}
```

### Track dtSearch index build progress

The following illustrates how to get the progress on an index build:

Copy

```text
1
2
3
4
5
6
7
public async Task<DtSearchIndexJobProgressResponse> (int workspaceId, int dtSearchArtifactId)

{

  using (var dtSearchIndexManagerService = proxy.GetClient<IDtSearchIndexManager>())

{

return await dtSearchIndexManagerService.GetIndexJobProgressAsync(workspaceId, dtSearchId);

}

}
```

On this page

- dtSearch Manager (.NET)

- Fundamentals for the dtSearch Manager API

- Methods

- CRUD operations

- Create a dtSearch index

- Retrieve index metadata

- Update a dtSearch index

- Delete a dtSearch index

- Move a dtSearch index

- Index build operations

- Build Index: Full

- Build Index: Incremental

- Build Index

- Cancel a dtSearch index build

- Activate a dtSearch index

- Deactivate a dtSearch index

- Compress a dtSearch index

- Swap a dtSearch index

- Retry errors on a dtSearch index

- Helper methods

- Get active indexes

- Get saved searches

- Get index share locations

- Track dtSearch index build progress


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
