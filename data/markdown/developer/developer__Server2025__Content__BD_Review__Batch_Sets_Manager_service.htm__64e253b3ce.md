---
title: "Batch Sets Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Review/Batch_Sets_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:22+00:00
sha256: a64f1263f78087b6fd0f222b4e394fd61ab33606771d168ce80f78134405bd47
---

Batch Sets Manager (REST)

# Batch Sets Manager (REST)

A batch set is a group of batches, which contain documents for review as part of the e-discovery process. For more information, see Batches .

The Batch Sets Manager service exposes CRUD operations for batch sets. It also supports creating and purging batches for a batch set. As a sample use case, you could use the Batch Sets Manager service to implement an application that programmatically creates a batch set and the batches contained in it.

You can also use the Batch Sets Manager service through .NET. For more information, see Batch Sets Manager (.NET) .

## Guidelines for the Batch Sets Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a batch set:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets/{batchSetID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {workspaceID} to the Artifact ID of the workspace that contains the batch set.

- {batchSetID} to the Artifact ID of a specific batch set.

## Client code sample

To use the Batch Sets Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for reading the properties of a batch set. For more information, see Read a batch set .

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
public async Task<BatchSet> ReadBatchSetViaREST(int workspaceID, int batchSetID)

{

    BatchSet result = null;

    string email = "username@email.com";

    string password = "password";

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes($"{email}:{password}")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        var url = $"http://localhost/Relativity.REST/api/relativity-review/v1/workspaces/{workspaceID}/batch-sets/{batchSetID}";

        var response = await client.GetAsync(url);

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<BatchSet>(content);

    }

    return result;

}
```

## Create a batch set

To create a batch set, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets
```

### Request field descriptions

The body of the request must contain a batchSet object with the following fields:

- Name - the user-friendly name of the batch set.

- BatchPrefix - a string used as the prefix for batch numbering.

- BatchSize - the maximum number of documents in a batch in the batch set.

- DataSource - a saved search containing documents that you want added to batches in the batch set. It contains these fields:

- Value - contains the following field:

- ArtifactID - the unique identifier for a saved search.

### Sample JSON request

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
{

    "batchSet": {

        "Name": "Test Batch Set",

        "BatchPrefix": "TEST",

        "BatchSize": 10,

        "DataSource": {

            "Value": {

                "ArtifactID": 1238203

            }

        }

    }

}
```

### Response field descriptions

The response contains the following fields:

- BatchSetID - the Artifact ID for the batch set.

- Name - the user-friendly name of the batch set.

- BatchPrefix - a string used as the prefix for batch numbering.

- BatchSize - the maximum number of documents in a batch in the batch set.

-

DataSource - a saved search containing documents that you want added to batches in the batch set. It contains these fields:

- Secured - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following:

- Name - the user-friendly name of the saved search.

- ArtifactID - the unique identifier for the saved search.

- Guids - an array of GUIDs used to identify the saved search.

- BatchUnitField - optional Relativity field used as the batch set's Batch Unit Field. Only documents sharing the same value for this field will be grouped together in the same batch, unless the Family Field overrides this.

- FamilyField - optional Relativity field used as the batch set's Family Field. Documents sharing the same value for this field will be grouped in the same batch, regardless of how big the batch set becomes.

- ReviewedField - optional Relativity field used as the batch set's Reviewed Field. Indicates which field should be used in order to keep a tally of how many documents in a given batch have been reviewed

- AutoBatchsetting - Batch set Auto Batch settings. This property is only populated when Auto Batch has been enabled for the batch set

- AutoBatchProgress - indicates the number of remaining documents to batch for the batch set. This field is only populated when Auto Batching is enabled.

- CreatedBy - the name and unique identifier for the user who created the batch set.

- Secured - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following:

- Name - the name of the user who created the batch set.

- ArtifactID - a unique identifier for the user.

- Guids - an array of GUIDs used to identify the user.

- CreatedOn - the date and time when the batch set was added to Relativity.

- LastModifiedBy - the name and unique identifier for the user who last updated the batch set.

- Secured - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following:

- Name - the name of the user who updated the batch set.

- ArtifactID - a unique identifier for the user.

- Guids - an array of GUIDs used to identify the user.

- LastModifiedOn - the date and time when the batch set was last updated.

- Keywords - optional keywords associated with the batch set.

- Notes - optional words or phrases used to describe the batch set.

### Sample JSON response

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
27
28
29
30
31
32
33
34
35
{

  "BatchSetID": 1597094,

  "Name": "Test Batch Set",

  "BatchPrefix": "TEST",

  "BatchSize": 10,

  "DataSource": {

    "Secured": false,

    "Value": {

      "Name": "John",

      "ArtifactID": 1238203,

      "Guids": []

    }

  },

  "AutoBatchProgress": {},

  "CreatedBy": {

    "Secured": false,

    "Value": {

      "Name": "Doe, John",

      "ArtifactID": 1000000000,

      "Guids": []

    }

  },

  "CreatedOn": "2021-01-06T21:32:07.617",

  "LastModifiedBy": {

    "Secured": false,

    "Value": {

      "Name": "Doe, John",

      "ArtifactID": 1000000000,

      "Guids": []

    }

  },

  "LastModifiedOn": "2021-01-06T21:32:07.617",

  "Keywords": "",

  "Notes": ""

}
```

## Read a batch set

To read the properties of a batch set , send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets/{batchSetID}
```

The body of the request is empty.

The response for a read operation contains the same fields as those for a create response. See the field descriptions for the response in Create a batch set .

### Sample JSON response

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
27
28
29
30
31
32
33
34
35
{

  "BatchSetID": 1597093,

  "Name": "Test Batch Set",

  "BatchPrefix": "TEST",

  "BatchSize": 10,

  "DataSource": {

    "Secured": false,

    "Value": {

      "Name": "John",

      "ArtifactID": 1238203,

      "Guids": []

    }

  },

  "AutoBatchProgress": {},

  "CreatedBy": {

    "Secured": false,

    "Value": {

      "Name": "Doe, John",

      "ArtifactID": 1000000000,

      "Guids": []

    }

  },

  "CreatedOn": "2021-01-06T21:31:13.223",

  "LastModifiedBy": {

    "Secured": false,

    "Value": {

      "Name": "Doe, John",

      "ArtifactID": 1000000000,

      "Guids": []

    }

  },

  "LastModifiedOn": "2021-01-06T21:31:42.287",

  "Keywords": "",

  "Notes": ""

}
```

## Update a batch set

To update a batch set, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets
```

The body of the request must contain a batchSet field, which represents a request for updating a batch set. It should contain the same fields as a create response. See the field descriptions for the response in Create a batch set .

### Sample JSON request

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
27
28
29
30
31
32
33
34
35
36
37
{

    "batchSet": {

        "BatchSetID": 1597093,

        "Name": "Test Batch Set Updated",

        "BatchPrefix": "TEST",

        "BatchSize": 10,

        "DataSource": {

            "Secured": false,

            "Value": {

                "Name": "John",

                "ArtifactID": 1238203,

                "Guids": []

            }

        },

        "AutoBatchProgress": {},

        "CreatedBy": {

            "Secured": false,

            "Value": {

                "Name": "Doe, John",

                "ArtifactID": 1000000000,

                "Guids": []

            }

        },

        "CreatedOn": "2021-01-06T21:31:13.223",

        "LastModifiedBy": {

            "Secured": false,

            "Value": {

                "Name": "Doe, John",

                "ArtifactID": 1000000000,

                "Guids": []

            }

        },

        "LastModifiedOn": "2021-01-06T21:31:13.223",

        "Keywords": "",

        "Notes": ""

    }

}
```

When the batch set is successfully updated, the response returns the status code of 200.

## Delete a batch set

To remove a batch set from Relativity, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets/{batchSetID}
```

The body of the request is empty.

When the batch set is successfully deleted, the response returns the status code of 200.

## Create batches

To add batches to a batch set, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets/{batchSetID}/batches/create
```

The body of the request is empty.

The response returns an integer indicating the number of batches that were created.

Copy

```text
1
500
```

## Purge batches

To remove batches from a batch set, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-review/{versionNumber}/workspaces/{workspaceID}/batch-sets/{batchSetID}/batches/purge
```

The body of the request is empty.

The response returns an integer indicating the number of batches that were purged.

Copy

```text
1
500
```
