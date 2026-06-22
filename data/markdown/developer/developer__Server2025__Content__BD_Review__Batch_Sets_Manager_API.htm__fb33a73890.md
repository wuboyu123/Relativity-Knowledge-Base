---
title: "Batch Sets Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Review/Batch_Sets_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:21+00:00
sha256: c0237ae63498c89489f11a28fcf4894ec501bf13a99f5805f49b96d3bf7c80f5
---

Batch Sets Manager (.NET)

# Batch Sets Manager (.NET)

A batch set is a group of batches, which contain documents for review as part of the e-discovery process. For more information, see Batches .

The Batch Sets Manager API exposes CRUD operations for batch sets. It also supports creating and purging batches for a batch set. As a sample use case, you could use the Batch Sets Manager API to implement an application that programmatically creates a batch set and the batches contained in it.

You can also use the Batch Sets Manager API through REST. For more information, see Batch Sets Manager (REST) .

## Fundamentals for the Batch Sets Manager API

The Batch Sets Manager API contains the following methods and classes.

### Methods

The Batch Sets Manager API exposes the following methods on the IBatchSetsManager interface in the Relativity.Review.Server.Versioned.<VersionNumber>.BatchSets namespace:

- CreateAsync() method - adds a new batch set to a workspace. This method takes the Artifact ID of the workspace where the batch set is to be created and a BatchSet object. It returns a BatchSet object. See Create a batch set .

- ReadAsync() method - retrieves the properties for a batch set. This method takes the Artifact ID of the workspace containing the batch set and the Artifact ID of the batch set. It returns a BatchSet object, which contains information about the batch set. See Read a batch set .

- UpdateAsync() method - modifies an existing batch set. This method takes the Artifact ID of the workspace containing the batch set and a BatchSet object containing the data used to modify the existing batch set. It returns a BatchSet object, which contains the updated properties. See Update a batch set .

- DeleteAsync() method - removes a batch set from Relativity. This method takes the Artifact ID of the workspace containing the batch set and the Artifact ID of the batch set. See Delete a batch set .

- CreateBatchesAsync() method - creates batches in a batch set. This method takes the Artifact ID of the workspace containing the batch set and the Artifact ID of the batch set. It returns the number of batches created. See Create batches in a batch set .

- PurgeBatchesAsync() method - deletes the batches from a batch set. This method takes the Artifact ID of the workspace containing the batch set and the Artifact ID of the batch set. It returns the number of batches deleted. See Remove batches from a batch set .

You can query for batch sets by using the Object Manager API. This API provides conditions for querying based on the batch set name. For more information, see Object Manager (.NET) .

### Classes and enumerations

The Batch Sets Manager API includes the following classes available in the Relativity.Review.Server.Domain.BatchSets.Models.<VersionNumber> namespace:

- BatchSet class - represents information about a specific batch set. Its properties include Artifact ID of the batch set, its user-friendly name, its prefix, number of documents in each batch, and others.

- AutoBatchSettings class - represents the settings used to automatically batch documents in a batch set. Its properties include the time interval in minutes for creating the batches and the minimum batch size.

- AutoBatchProgress class - represents the number of documents remaining to be batched. Its properties include number of documents to be batched, the time of the last successful run, and Auto Batch status.

- AutoBatchStatus enumeration - represents the status of an Auto Batch job as follows:

- Pending - the job was submitted and is waiting to be processed.

- Processing - the job was submitted and is being processed.

- Error - the job was submitted but not completed due to an error.

## Create a batch set

Use the CreateAsync() method to add a new batch set to a workspace. This method takes the following arguments:

- The Artifact ID of the workspace where the batch set is to be created

- A BatchSet object

It returns a BatchSet object.

View code sample Copy

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
public async Task<BatchSet> CreateBatchSet(int workspaceID, string batchSetName, int dataSourceID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    BatchSet createdBatchSet;

    var parameters = new BatchSet()

    {

        Name = batchSetName,

        BatchPrefix = "TEST",

        BatchSize = 10,

        DataSource = new DisplayableObjectIdentifier()

        {

            ArtifactID = dataSourceID,

        },

    };

    using (var batchSetsManager = serviceFactory.CreateProxy<IBatchSetsManager>())

    {

        createdBatchSet = await batchSetsManager.CreateAsync(workspaceID, parameters);

    }

    return createdBatchSet;

}
```

## Read a batch set

Use the ReadAsync() method to retrieve the properties of a batch set. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch set

- The Artifact ID of the batch set

It returns a BatchSet object.

View code sample Copy

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
public async Task<BatchSet> ReadBatchSet(int workspaceID, int batchSetID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    BatchSet batchSet;

    using (var batchSetsManager = serviceFactory.CreateProxy<IBatchSetsManager>())

    {

        batchSet = await batchSetsManager.ReadAsync(workspaceID, batchSetID);

    }

    return batchSet;

}
```

## Update a batch set

Use the UpdateAsync() method to modify the properties of a batch set. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch set

- A BatchSet object containing the data used to modify the existing batch set.

It returns an updated BatchSet object.

View code sample Copy

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
public async Task<BatchSet> UpdateBatchSet(int workspaceID, int batchSetID, string newName)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    BatchSet updatedBatchSet;

    using (var batchSetsManager = serviceFactory.CreateProxy<IBatchSetsManager>())

    {

        BatchSet existingSet = await batchSetsManager.ReadAsync(workspaceID, batchSetID);

        existingSet.Name = newName;

        updatedBatchSet = await batchSetsManager.UpdateAsync(workspaceID, existingSet);

    }

    return updatedBatchSet;

}
```

## Delete a batch set

Use the DeleteAsync() method to remove a batch set from Relativity. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch set

- The Artifact ID of the batch set

View code sample Copy

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
public async Task DeleteBatchSet(int workspaceID, int batchSetID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    using (var batchSetsManager = serviceFactory.CreateProxy<IBatchSetsManager>())

    {

        await batchSetsManager.DeleteAsync(workspaceID, batchSetID);

    }

}
```

## Create batches in a batch set

Use the CreateBatchesAsync() method to create batches in a batch set. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch set

- The Artifact ID of the batch set

It returns the number of batches created.

View code sample Copy

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
public async Task<int> CreateBatches(int workspaceID, int batchSetID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    int batchCount;

    using (var batchSetsManager = serviceFactory.CreateProxy<IBatchSetsManager>())

    {

        batchCount = await batchSetsManager.CreateBatchesAsync(workspaceID, batchSetID);

    }

    return batchCount;

}
```

## Remove batches from a batch set

Use the PurgeBatchesAsync() method to delete batches from a batch set. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch set

- The Artifact ID of the batch set

It returns the number of batches deleted.

View code sample Copy

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
public async Task<int> PurgeBatches(int workspaceID, int batchSetID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    int batchCount;

    using (var batchSetsManager = serviceFactory.CreateProxy<IBatchSetsManager>())

    {

        batchCount = await batchSetsManager.PurgeBatchesAsync(workspaceID, batchSetID);

    }

    return batchCount;

}
```
