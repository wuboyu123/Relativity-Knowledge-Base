---
title: "Batches Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Review/Batches_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:17+00:00
sha256: c555b808e8778c52c668e4964774bc05a6d3e88f454009ebe934fac1cb3999bd
---

Batches Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Batches Manager (.NET)

A batch is a collection of documents that a Relativity admin has grouped together based on a specific set of criteria. During the review phase of the e-discovery process, the admin assigns a batch to a reviewer. The reviewer checks out the batch to determine the relevancy of its documents to a case, and then checks the batch in after coding the documents. For more information, see Batches .

The Batches Manager API supports retrieving information about existing batches as well as checking batches in and out. As a sample use case, you could use the Batches Manager API to implement application logic that automatically checks batches in and out on behalf of reviewers.

You can also use the Batches Manager API through REST. For more information, see Batches Manager (REST) .

## Fundamentals for the Batches Manager API

The Batches Manager API contains the following methods and classes.

### Methods

The Batches Manager API exposes the following methods on the IBatchesManager interface in the Relativity.Review.Server.Versioned.<VersionNumber>.BatchSets namespace:

- ReadAsync() method - retrieves the properties for a batch. This method takes the Artifact ID of the workspace containing the batch and the Artifact ID of the batch. It returns a Batch object, which contains information about the batch. See Read a batch .

- CheckoutAsync() method - checks out a batch and assigns it to a specific user. This method takes the Artifact ID of the workspace containing the batch, the Artifact ID of the batch, and a CheckoutRequest object. See Check out a batch .

- CheckinAsync() method - checks in a specific batch and updates its status. This method takes the Artifact ID of the workspace containing the batch, the Artifact ID of the batch, and an optional Boolean value indicating whether the review of the batch is complete. See Check in a batch .

You can query for batches by using the Object Manager API. This API provides conditions for querying based on the batch name and the user assigned to the batch. For more information, see Object Manager (.NET) .

### Classes and enumerations

The Batches Manager API includes the following classes available in the Relativity.Review.Server.Domain.BatchSets.Models.<VersionNumber> namespace:

- Batch class - represents information about a specific batch. Its properties include the Artifact ID of the batch, a user-friendly name, a status, and the user assigned to the batch.

- BatchStatus enumeration - includes the following statuses for a batch:

- None - indicates that the batch isn't checked out.

- InProgress - indicates that the batch is checked out but not completed.

- Completed - indicates that the batch is completed and checked in.

- CheckoutRequest class - indicates the user that the batch is assigned to. The UserID property on this class contains the Artifact ID of the user.

## Read a batch

Use the ReadAsync() method to retrieve the properties of a batch. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch

- The Artifact ID of the batch

It returns a Batch object.

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
public async Task<Batch> ReadBatch(int workspaceID, int batchID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);



    Batch batch;



    using (var batchesManager = serviceFactory.CreateProxy<IBatchesManager>())

    {

        batch = await batchesManager.ReadAsync(workspaceID, batchID);

    }



    return batch;

}
```

## Check out a batch

Use the CheckoutAsync() method to check out a specific batch and assign it to a user. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch

- The Artifact ID of the batch

- A CheckoutRequest object that indicates how the batch is check out. It includes the Artifact ID of the user assigned to the batch.

After you check out a batch, its status is updated to InProgress .

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
public async Task CheckoutBatch(int workspaceID, int batchID, int userID)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);



    var parameters = new CheckoutRequest()

    {

        UserId = userID,

    };



    using (var batchesManager = serviceFactory.CreateProxy<IBatchesManager>())

    {

        await batchesManager.CheckoutAsync(workspaceID, batchID, parameters);

    }

}
```

## Check in a batch

Use the CheckinAsync() method to check in a batch. This method takes the following arguments:

- The Artifact ID of the workspace containing the batch

- The Artifact ID of the batch

- An optional Boolean value indicating whether the review of the batch is complete:

- True - updates the batch status to Completed . The batch remains assigned to the current user.

- False - updates the batch status to None and removes the user assignment.

This method fails if you attempt to check in a batch with a status other than InProgress .

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
public async Task CheckinBatch(int workspaceID, int batchID, bool completed)

{

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);



    using (var batchesManager = serviceFactory.CreateProxy<IBatchesManager>())

    {

        await batchesManager.CheckinAsync(workspaceID, batchID, completed);

    }

}
```

On this page

- Batches Manager (.NET)

- Fundamentals for the Batches Manager API

- Methods

- Classes and enumerations

- Read a batch

- Check out a batch

- Check in a batch


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
