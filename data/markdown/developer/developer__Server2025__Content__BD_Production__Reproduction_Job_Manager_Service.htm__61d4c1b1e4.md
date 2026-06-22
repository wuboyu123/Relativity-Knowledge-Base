---
title: "Re-production Job Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Reproduction_Job_Manager_Service.htm
collection: developer
fetched_at: 2026-06-22T06:27:53+00:00
sha256: 7abe43610ac6d30cf8b223ecae0ffe1cff33f2997dae35077845e9f06fbb2164
---

Re-production Job Manager (REST)

# Re-production Job Manager (REST)

A re-production job provides you with the ability to select specific documents from a completed production job and re-run them. After a re-production job finishes running, the modified documents are merged into the original production set. These documents overwrite those that were previously produced. For general information, see Re-production on the Relativity Server 2025 Documentation site.

The Re-production Job Manager service provides the following functionality:

- Creating re-production jobs

- Retrieving re-production job IDs

- Retrieving re-production job statuses

You can also use the Re-production Job Manager service through .NET. For more information, see Re-production Job Manager (.NET) .

See these related pages:

- Production

- Production Manager (REST)

- Production Data Source Manager (REST)

- Production Placeholder Manager (REST)

- Production Queue Manager (REST)

## Guidelines for productions in REST

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

The following example illustrates how to set the path parameters when deleting a data source, but the same convention applies to all URLs in the Production APIs:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-data-sources/{DataSourceID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {WorkspaceID} to the Artifact ID of the workspace that contains the data source.

- {DataSourceID} to the Artifact ID of a specific data source.

## Create a re-production job

You can create a re-production job based on a list of document IDs or a mass operation token. For additional guidelines, see Re-production Job Manager (.NET) .

- This endpoint doesn't run re-production jobs. To run these jobs, use the stage and run endpoint or the mass stage and run endpoint. See Production Manager (REST) .

- To use these endpoints, you must have the document view permission, and the production view, edit, and add permissions.

### Use document IDs to create a job

To create a re-production job using document IDs, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/re-productions/re-production-job-with-documents
```

View field descriptions for a request

The request contains the following fields:

- reproductionOptions - includes the following fields:

- ReproductionType - a required field indicating the production type. For more information, see Re-production Job Manager (.NET) .

Use an integer listed in the following table:

Re-production type Input

Re-produce document 0

Replace document with placeholder 1

Replace placeholder with document 2

- ReproduceDocumentOptions - includes the following fields:

- IncludeNatives - a Boolean value indicating whether to produce native documents.

- BurnRedactions - a Boolean value indicating whether to burn redactions on re-produced images. This option requires a valid markup set.

- MarkupSetID - the Artifact ID for a markup set used to burn redactions on re-produced documents.

- ReplaceDocumentWithPlaceholderOptions - includes the following fields:

- PlaceholderID - the Artifact ID of the placeholder used when reproducing documents.

- IncludeNatives - a Boolean value indicating whether to produce native documents.

- ReplacePlaceholderWithDocumentOptions - includes the following fields:

- Delimiter - the delimiter used between the original placeholder Bates number and the suffixed page number.

- NumberOfDigits - the number of digits used for the suffixed page numbers.

- IncludeNatives - a Boolean value indicating whether to produce native documents.

- BurnRedactions - a Boolean value indicating whether to burn redactions on re-produced images. This option requires a valid markup set.

- MarkupSetID - the Artifact ID for a markup set used to burn redactions on re-produced documents.

- productions - an array of production IDs, which are Artifact IDs. At least one production must be included in the request. The re-production job modifies these productions.

-

documents - an array of Artifact IDs for the documents to reproduce.

We recommend creating re-production jobs with under 10,000 documents. If you want to create a larger job, split the requests up into batches.

View a sample JSON request Copy

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
{

    "reproductionOptions":{

        "ReproductionType": 2,

        "ReproduceDocumentOptions":{

            "IncludeNatives":false,

            "BurnRedactions":false,

            "MarkupSetID":1034197

        },

        "ReplaceDocumentWithPlaceholderOptions":{

            "PlaceholderID":1039993,

            "IncludeNatives":false

        },

        "ReplacePlaceholderWithDocumentOptions":{

            "Delimiter":"_",

            "NumberOfDigits":4,

            "IncludeNatives":true,

            "BurnRedactions":false,

            "MarkupSetID":1

        }

    },

    "productions":[

        {

            "ProductionID":1045549

        },

        {

            "ProductionID":1047151

        }

    ],

    "documents":[

       1045081,

       1045082

    ]

}
```

View field descriptions for a response

The response contains a ReproductionJobResult object with the following fields:

- ReproductionJobID - the ID of the re-production job.

- Errors - an array of strings providing error messages if the job or associated production sets weren't created.

- Messages - an array of strings providing additional information about the job.

- Warnings - an array of strings providing warnings about the job.

- WasJobCreated - a Boolean value indicating whether the job was created.

- ProductionsCreated - an array of Artifact IDs representing the productions that were created.

- Results - an array of InnerReproductionJobResult objects with the following fields:

- ProductionID - the Artifact ID of the re-production run in this job. This value is 0 when the re-production isn't created.

- ParentProductionID - the Artifact ID of the production that has been reproduced.

- Errors - an array of strings providing error messages for a re-production that wasn't created.

- Warnings - an array of strings providing warning messages about the creation of a re-production.

- Messages - an array of strings providing informational messages about a re-production.

View a sample JSON response Copy

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
{

    "ReproductionJobID": 3,

    "Errors": [],

    "Messages": [],

    "Warnings": [],

    "WasJobCreated": true,

    "ProductionsCreated": [

        1054586,

        1054588

    ],

    "Results": [

        {

            "ProductionID": 1054586,

            "ParentProductionID": 1045549,

            "Errors": [],

            "Warnings": [],

            "Messages": []

        },

        {

            "ProductionID": 1054588,

            "ParentProductionID": 1047151,

            "Errors": [],

            "Warnings": [],

            "Messages": []

        }

    ]

}
```

### Use a mass operation token to create a job

To create a reproduction job with a mass operation token, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/re-productions/re-production-job
```

View field descriptions for a request

The request for a create operation with a mass operation token contains the same fields as those required for document IDs. Instead of a documents field, this request requires a databaseToken as follows:

- databaseToken - a GUID representing a collection of documents to re-produce. At least one production and database token must be included in the request.

Use the following steps to generate a database token for select documents:

- Create a custom mass operation. See Develop Mass Operation handlers .

- In Relativity, navigate to the Resource Files tab and add the custom mass operation by clicking New Resource File .

- Navigate to the Object Type tab and link the custom mass operation to the Document object. See Adding a custom mass operation .

- Navigate to the Documents tab within a workspace.

- Select the documents that you want to retrieve produced production information for.

-

In the mass operations bar, click the custom mass operation. A database token is generated that corresponds to a table in the database that holds the selected documents. The database token is at the end of the URL on the page that opens.

Passing a database token eliminates a second server trip to retrieve the requested document IDs of the custom mass operation.

View a sample JSON request Copy

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
{

    "reproductionOptions":{

        "ReproductionType": 2,

        "ReproduceDocumentOptions":{

            "IncludeNatives":false,

            "BurnRedactions":false,

            "MarkupSetID":1034197

        },

        "ReplaceDocumentWithPlaceholderOptions":{

            "PlaceholderID":1039666,

            "IncludeNatives":false

        },

        "ReplacePlaceholderWithDocumentOptions":{

            "Delimiter":"_",

            "NumberOfDigits":4,

            "IncludeNatives":false,

            "BurnRedactions":false,

            "MarkupSetID":1

        }

    },

    "productions":[

        {

            "ProductionID":1039709

        },

        {

            "ProductionID":1039714

        }

    ],

    "databaseToken":"08a250a1-1933-4295-aeac-fbfaad8d8cf0"

}
```

The response for a create operation with a mass operation token contains the same fields as those returned when using document IDs. See the field descriptions for the response in Use document IDs to create a job .

View a sample JSON response Copy

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
{

    "ReproductionJobID": 18,

    "Errors": [],

    "Messages": [],

    "Warnings": [],

    "WasJobCreated": true,

    "ProductionsCreated": [

        1039782,

        1039784

    ],

    "Results": [

        {

            "ProductionID": 1039782,

            "ParentProductionID": 1039709,

            "Errors": [],

            "Warnings": [],

            "Messages": []

        },

        {

            "ProductionID": 1039784,

            "ParentProductionID": 1039714,

            "Errors": [],

            "Warnings": [],

            "Messages": []

        }

    ]

}
```

## Retrieve re-production job IDs

To retrieve the re-production job IDs in a workspace, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/re-productions/jobs
```

The request body is empty.

You must have view permissions for productions to retrieve re-production job IDs.

The response contains an array of integers representing job IDs.

Copy

```text
1
2
3
4
[

    1,

    2

]
```

## Retrieve the status for a re-production job

You can retrieve the status for a re-production job. For example, you might use this endpoint to determine whether a job has completed after creating and running it.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/re-productions/{reproductionJobID}/status
```

The request body is empty.

The response contains ReproductionStatusResult object, which includes the following fields:

- Errors - an array of strings providing error messages if the job or associated production sets weren't created.

- Messages - an array of strings providing additional information about the job.

- Warnings - an array of strings providing warnings about the job.

-

ReproductionStatus - current re-production status.

View re-production statuses

The following list includes re-production statuses:

- Created - a re-production job was been created, but not yet run.

-

Running - a re-production job is currently running without errors. When a production has a Staged status, the re-production status is Running because the job is between being New and Produced.

- RunningWithErrors - a re-production job is currently running but some productions have errors.

- Completed - a re-production job has completed all productions successfully.

- CompletedWithErrors - a reproduction job has completed all productions, but some productions have errors.

- DoesNotExist - invalid re-production job. If all productions in the re-production job are deleted, a status of DoesNotExist is returned.

- ProductionStatusResults - an array of ProductionStatusResult objects containing the following fields:

- ArtifactID - the Artifact ID of the production.

- Status - the status of the production, such as New, Staging, Branding and others.

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
{

    "Errors": [],

    "Messages": [],

    "Warnings": [],

    "ReproductionStatus": "Created",

    "ProductionStatusResults": [

        {

            "ArtifactID": 1054586,

            "Status": "New"

        },

        {

            "ArtifactID": 1054588,

            "Status": "New"

        }

    ]

}
```
