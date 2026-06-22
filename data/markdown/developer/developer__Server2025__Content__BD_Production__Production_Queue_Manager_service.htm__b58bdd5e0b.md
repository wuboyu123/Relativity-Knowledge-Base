---
title: "Production Queue Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Queue_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:27:49+00:00
sha256: 980335473041d3f634bcfe4312b769aa070f757098674f9e27aef3e43f6204d8
---

Production Queue Manager (REST)

# Production Queue Manager (REST)

The Production Queue contains all production jobs currently running in your Relativity environment. For general information, see Production Queue on the Relativity Server 2025 Documentation site.

The Production Queue Manager service exposes endpoints used to cancel a single or multiple production jobs, to retry multiple jobs, or to set the priority for them. You can identify the jobs for canceling or retrying by mass operation token or Artifact ID.

You can also use the Production Queue Manager service through .NET. For more information, see Production Queue Manager (.NET) .

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

## Cancel a production job

To cancel a single production job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/production-queue/production-jobs/cancel
```

The request must a jobRef object with the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production. This field isn't required if you set the JobID field.

- ProductionID - the Artifact ID of the production. This field isn't required if you set the JobID field.

- JobID - the Artifact ID of the production job.

Copy

```text
1
2
3
4
5
6
7
{

    "jobRef": {

        "WorkspaceID": 100,

        "ProductionID": 200,

        "JobID": 300

    }

}
```

The response contains the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production.

- ProductionID - the Artifact ID of the production.

- JobID - the Artifact ID of the production job.

- CancelSuccessfullySent - a Boolean value indicating whether the cancel request was successfully sent.

- Errors - an array of errors that occurred during the cancel operation.

Copy

```text
1
2
3
4
5
6
7
{

    "WorkspaceID": 100,

    "ProductionID": 200,

    "JobID": 0,

    "CancelSuccessfullySent": true,

    "Errors": []

}
```

## Cancel production jobs by mass operation token

You can cancel a collection of production jobs by using mass operation token. This endpoint uses GUID to identify a collection of production jobs. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/production-queue/mass-cancel
```

The request body must contain the following field:

- databaseToken - a GUID that represents the collection of jobs.

Copy

```text
1
2
3
{

    "databaseToken": "F420E383-7D4D-4DB1-BC60-959791685857"

}
```

The response contains the following fields:

- TotalJobsRequested - the total number of production queue jobs requested for the operation.

- TotalJobsSuccessful - the total number of jobs successfully operated on.

- ProductionQueueResults - an array containing the results per job. Each job contains the following fields:

- JobID - the Artifact ID of the production job.

- ProductionID - the Artifact ID of the production.

- WorkspaceID - the Artifact ID of the workspace containing the production.

- Errors - an array of errors that occurred during the cancel operation.

- RequestSent - a Boolean value indicating whether the cancel request was successfully sent.

- Errors - an array of errors for the overall mass operation.

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
{

    "TotalJobsRequested": 2,

    "TotalJobsSuccessful": 2,

    "ProductionQueueResults": [

        {

            "JobID": 2123,

            "ProductionID": 1041791,

            "WorkspaceID": 1027293,

            "Errors": [],

            "RequestSent": true

        },

        {

            "JobID": 2124,

            "ProductionID": 1041793,

            "WorkspaceID": 1027293,

            "Errors": [],

            "RequestSent": true

        }

    ],

    "Errors": []

}
```

## Cancel production jobs by ID

To cancel multiple production jobs by ID, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/production-queue/production-jobs/mass-cancel
```

The request must contain a jobsToBeCanceled object with the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production. This field isn't required if you set the JobID field.

- ProductionID - the Artifact ID of the production. This field isn't required if you set the JobID field.

- JobID - the Artifact ID of the production job.

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
{

    "jobsToBeCanceled": [

        {

            "WorkspaceID": 100,

            "ProductionID": 200,

            "JobID": 300

        },

        {

            "WorkspaceID": 101,

            "ProductionID": 201,

            "JobID": 301

        }

    ]

}
```

The response contains the following fields

- NumberOfJobsRequestedForCancel - the total number of production queue jobs requested for the operation.

- NumberOfJobsCancelWasRequestedSuccessfully - the total number of jobs successfully operated on.

- CancelJobResults - an array containing the results for each requested job cancellation. Each job contains the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production.

- ProductionID - the Artifact ID of the production.

- JobID - the Artifact ID of the production job.

- CancelSuccessfullySent - a Boolean value indicating whether the cancel request was successfully sent.

- Errors - an array of errors that occurred during the cancel operation.

- Errors - an array of error messages for the overall mass operation.

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
{

    "NumberOfJobsRequestedForCancel": 2,

    "NumberOfJobsCancelWasRequestedSuccessfully": 1,

    "CancelJobResults": [

        {

            "WorkspaceID": 100,

            "ProductionID": 200,

            "JobID": 300,

            "CancelSuccessfullySent": true,

            "Errors": []

        },

        {

            "WorkspaceID": 101,

            "ProductionID": 201,

            "JobID": 301,

            "CancelSuccessfullySent": false,

            "Errors": [

                "Invalid Production JobRef. Cannot find Production based on WorkspaceID and ProductionID, or based on JobID."

            ]

        }

    ],

    "Errors": []

}
```

## Set the priority on production jobs

To set the priority on a collection of production jobs in the queue, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/production-queue/mass-prioritize
```

The request must contain the following fields:

- databaseToken - a GUID representing a collection of production jobs in the queue.

- priority - an integer value representing the new priority to assign to the jobs.

Copy

```text
1
2
3
4
{

    "databaseToken": "F420E383-7D4D-4DB1-BC60-959791685857",

    "priority": 10

}
```

The response contains the following fields:

- TotalJobsRequested - total number of production queue jobs requested for the operation.

- TotalJobsSuccessful - the total number of jobs successfully operated on.

- ProductionQueueResults - an array containing the results per job. Each job contains the following fields:

- JobID - the Artifact ID of the production job.

- ProductionID - the Artifact ID of the production.

- WorkspaceID - the Artifact ID of the workspace containing the production.

- Errors - an array of errors that occurred during the cancel operation.

- RequestSent - a Boolean value indicating whether the request was successfully sent.

- Errors - an array of errors for the overall mass operation.

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
{

    "TotalJobsRequested": 2,

    "TotalJobsSuccessful": 2,

    "ProductionQueueResults": [

        {

            "JobID": 2123,

            "ProductionID": 1041791,

            "WorkspaceID": 1027293,

            "Errors": [],

            "RequestSent": true

        },

        {

            "JobID": 2124,

            "ProductionID": 1041793,

            "WorkspaceID": 1027293,

            "Errors": [],

            "RequestSent": true

        }

    ],

    "Errors": []

}
```

## Retry production jobs by mass operation token

You can retry a collection of production jobs by using a mass operation token. This endpoint uses GUID to identify a collection of production jobs.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/production-queue/mass-retry
```

The request body must contain the following field:

- databaseToken - a GUID representing a collection of production jobs in the queue.

Copy

```text
1
2
3
{

    "databaseToken": "F420E383-7D4D-4DB1-BC60-959791685857"

}
```

The response contains the following fields:

- TotalJobsRequested - total number of production queue jobs requested for the operation.

- TotalJobsSuccessful - the total number of jobs successfully operated on.

- ProductionQueueResults - an array containing the results per job. Each job contains the following fields:

- JobID - the Artifact ID of the production job.

- ProductionID - the Artifact ID of the production.

- WorkspaceID - the Artifact ID of the workspace containing the production.

- Errors - an array of errors that occurred during the cancel operation.

- RequestSent - a Boolean value indicating whether the request was successfully sent.

- Errors - an array of errors for the overall mass operation.

The results don't indicate whether the productions were successfully rerun. They only indicate that the retries were successfully submitted.

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
{

    "TotalJobsRequested": 2,

    "TotalJobsSuccessful": 2,

    "ProductionQueueResults": [

        {

            "JobID": 2123,

            "ProductionID": 1041791,

            "WorkspaceID": 1027293,

            "Errors": [],

            "RequestSent": true

        },

        {

            "JobID": 2124,

            "ProductionID": 1041793,

            "WorkspaceID": 1027293,

            "Errors": [],

            "RequestSent": true

        }

    ],

    "Errors": []

}
```

## Retry production jobs by ID

To retry multiple production jobs by ID, send a POST request with a URL in the following format:

Copy

```text
1
<host>//Relativity.REST/api/relativity-productions/{versionNumber}/production-queue/production-jobs/mass-retry
```

The request must contain a jobsToBeRetried object with the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production. This field isn't required if you set the JobID field.

- ProductionID - the Artifact ID of the production. This field isn't required if you set the JobID field.

- JobID - the Artifact ID of the production job.

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
{

    "jobsToBeRetried": [

        {

            "WorkspaceID": 100,

            "ProductionID": 200,

            "JobID": 300

        },

        {

            "WorkspaceID": 101,

            "ProductionID": 201,

            "JobID": 301

        }

    ]

}
```

The response contains the following fields:

- NumberOfJobsRequestedForRetry - total number of production queue jobs requested for the operation.

- NumberOfJobsRetryWasRequestedSuccessfully - the total number of jobs successfully operated on.

- RetryJobResults - an array containing the results per job. Each job contains the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production.

- ProductionID - the Artifact ID of the production.

- JobID - the Artifact ID of the production job.

- RetrySuccessfullySent - a Boolean value indicating whether the request was successfully sent.

- Errors - an array of errors that occurred during the retry operation.

- Errors - an array of errors for the overall mass operation.

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
{

    "NumberOfJobsRequestedForRetry": 2,

    "NumberOfJobsRetryWasRequestedSuccessfully": 1,

    "RetryJobResults": [

        {

            "WorkspaceID": 100,

            "ProductionID": 200,

            "JobID": 300,

            "RetrySuccessfullySent": true,

            "Errors": []

        },

        {

            "WorkspaceID": 101,

            "ProductionID": 201,

            "JobID": 301,

            "RetrySuccessfullySent": false,

            "Errors": [

                "Invalid Production JobRef. Cannot find Production based on WorkspaceID and ProductionID, or based on JobID."

            ]

        }

    ],

    "Errors": []

}
```
