---
title: "Batches Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Review/Batches_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:19+00:00
sha256: d0c809f68f5417b0dcbecc83e389c8a3ac334553fa60ba12266b1427799e7f75
---

Batches Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Batches Manager (REST)

A batch is a collection of documents that a Relativity admin has grouped together based on a specific set of criteria. During the review phase of the e-discovery process, the admin assigns a batch to a reviewer. The reviewer checks out the batch to determine the relevancy of its documents to a case, and then checks the batch in after coding the documents. For more information, see Batches .

The Batches Manager service supports retrieving information about existing batches as well as checking batches in and out. As a sample use case, you could use the Batches Manager service to implement application logic that automatically checks batches in and out on behalf of reviewers.

You can also use the Batches Manager service through .NET. For more information, see Batches Manager (.NET) .

## Guidelines for the Batches Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a batch:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batches/{batchID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {workspaceID} to the Artifact ID of the workspace that contains the batch.

- {batchID} to the Artifact ID of a specific batch.

## Client code sample

To use the Batches Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for reading the properties of a batch. For more information, see Read a batch .

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
public async Task<Batch> ReadBatchViaREST(int workspaceID, int batchID)

{

    Batch result = null;

    string email = "username@email.com";

    string password = "password";

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes($"{email}:{password}")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");



        var url = $"http://localhost/Relativity.REST/api/relativity-review/v1/workspaces/{workspaceID}/batches/{batchID}";

        var response = await client.GetAsync(url);

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<Batch>(content);

    }



    return result;

}
```

## Read a batch

To retrieve the properties of a batch, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/v1/workspaces/{workspaceID}/batches/{batchID}
```

The body of the request is empty.

The response contains the following fields:

- BatchID - the Artifact ID for the batch.

- Name - the user-friendly name of the batch.

- Status - the following statuses are available for a batch:

- None - indicates that the batch isn't checked out.

- InProgress - indicates that the batch is checked out but not completed.

- Completed - indicates that the batch is completed and checked in.

- AssignedUserID - the user who has checked out the batch.

- Secured - indicates whether the current user has permissions to view the setting in the Value field.

- Value - the Artifact ID for the user assigned to the batch.

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
{

  "BatchID": 1593398,

  "Name": "TEST200001",

  "Status": "InProgress",

  "AssignedUserID": {

    "Secured": false,

    "Value": 1021804

  }

}
```

## Check out a batch

To check out a batch, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/v1/workspaces/{workspaceID}/batches/{batchID}/checkout
```

The body of the request must contain a request object with a UserID field. Set this field to the Artifact ID for the user who should be assigned to the batch.

Copy

```text
1
2
3
4
5
{

    "request": {

        "UserID": 1021804

    }

}
```

When the batch is successfully checked out, the response returns the status code of 200.

## Check in a batch

To check in a batch, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/v1/workspaces/{workspaceID}/batches/{batchID}/checkin?completed=true
```

In the query string, you can set the optional ?completed query string parameter as follows:

- ?completed=true - updates the batch status to Completed . The batch remains assigned to the current user. You can omit the ?completed=true query string parameter. The default value of false is then used.

- ?completed=false - updates the batch status to None and removes the user assignment. This query string value explicitly checks in the batch as incomplete.

This endpoint fails if you attempt to check in a batch with a status other than InProgress .

The body of the request is empty.

When the batch is successfully checked in, the response returns the status code of 200.

On this page

- Batches Manager (REST)

- Guidelines for the Batches Manager service

- URLs

- Client code sample

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
