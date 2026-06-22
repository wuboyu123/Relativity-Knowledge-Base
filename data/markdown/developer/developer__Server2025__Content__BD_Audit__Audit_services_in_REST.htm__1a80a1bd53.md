---
title: "Audit (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Audit/Audit_services_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:22:41+00:00
sha256: bcb3282da87ad08a91642fd9ce970d9362c6472375ba99ad38b797a9955a3c44
---

Audit (REST)

# Audit (REST)

The Audit services available through REST include multiple endpoints that you can use to programmatically revert, retrieve, and search Relativity audit records stored in Elasticsearch. These services support interactions with both instance-level and workspace-level audit records. The following services provide endpoints for this functionality:

- Audit Metrics service - includes an endpoint for retrieving information about the number and size of the audits in a specific workspace.

- Audit Revert service - includes endpoints for reverting document update actions. It provides endpoints for reverting a single action or list of actions, and for verifying whether the revert operation can be performed on an action.

- Reviewer Statistics service - includes endpoints for retrieving information about reviewer actions, such as the number of actions performed by a reviewer on a document, the usage time per review, a summary report of reviewer actions, and others.

- Audit Query service - includes an endpoint for querying on a specific audit record.

- Audit Object Manager UI service - includes endpoints for querying on audit details to display in the Relativity UI, including filtering on the returned data.

These APIs don't support working with audit records stored in an SQL Server database.

Sample use cases for the Audit services include building custom applications to perform the following tasks:

- Transfer data to other applications and tools for analysis and reporting, such as a third-party software applications or web-based visualization tools.

- Implement an audit record query as part of a larger solution that captures query results and then manipulates the results using a visualization solution.

- Programmatically generate a reviewer statistics report.

- Retrieve or aggregate audit data or execute pivot queries on the data.

You can access the Audit API services through .NET interfaces. These interfaces support the same functionality as available through REST. For more information, see Audit (.NET) .

## Guidelines for Audit services

Review the following guidelines for working with the Audit services.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve the number and size of audits in a workspace:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audit-metrics/
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {Workspace ID} to the Artifact ID of the workspace containing the required audit metrics.

### Operations supported by the Audit services

The following table list operations that you can perform using the Audit services.

Service name Endpoints available for these operations

Audit Metrics Retrieve the total number and size of audits

Audit Revert Validate a revert operation for an audit action

Revert an audit

Mass revert a list of audits

Audit Pivot Query with Pivot on audit data

Reviewer Statistics Retrieve action counts for updated documents

Retrieve the usage time per reviewer

Retrieve size of the extracted text for reviewed documents

Retrieve an aggregation of user actions by hour

Retrieve choices reviewed by users

Retrieve a summary report of reviewer statistics

Audit Query Query for an audit record

Audit Object Manager UI Query on audit fields

Query for a specific audit object

Query with additional query options

Query on audit fields and return a smaller payload

### Query conditions

You can specify conditions for an audit query in the condition or rowCondition fields in a JSON request. Setting these fields is equivalent to using conditions and list filtering in the Relativity UI. For information about rendering audit details in the Relativity UI, see Audit on the Relativity Documentation site.

View examples of query conditions

- Action Copy

```text
1
(('Action' IN CHOICE [1048406, 1048444]))
```

Audit actions are Relativity choices. You can find the value of Artifact IDs of the choices on the Data Grid Audit Field Mapping tab (Relativity Choice ID Column). You can also query the choices for the Action field programmatically.

- Artifact ID - the ID of the Relativity artifact associated with the audit record. Copy

```text
1
(('Artifact ID' == 1003663))
```

- Audit record ID Copy

```text
1
(('Audit ID' == 393901))
```

- Complex condition - an example is a complex condition that combines date, object type, and action. Copy

```text
1
2
3
(('Timestamp' >= 2017-11-01T00:00:00.00Z AND 'Timestamp' <= 2017-11-23T23:59:00.00Z))

     AND (('Object Type' == CHOICE 1048471))

          AND (('Action' IN CHOICE [1048406, 1048444]))
```

- Execution Time (in milliseconds) Copy

```text
1
(('Execution Time (ms)' > 1000))
```

- Object type Copy

```text
1
(('Object Type' == CHOICE 1048471))
```

Object Type values are Relativity choices. You can find the value of Artifact IDs of the choices on the tab by filtering for Data Grid Audit object type and the Object Type field. You can also query the choices for the Object Type field programmatically.

- Old value or new value Copy

```text
1
(('New Value' LuceneSearch 'oil OR gas'))
```

Beginning in 10.1.290.1 , Lucene Search is deprecated in Relativity.

- Timestamp Copy

```text
1
(('Timestamp' >= 2017-11-01T00:00:00.00Z AND 'Timestamp' <= 2017-11-23T23:59:00.00Z))
```

## Audit Metrics service

The Audit Metrics service supports the retrieval of information about the number and size of the audits in a specific workspace.

### Retrieve the total number and size of audits

You can retrieve the total count of all audits in a workspace, and the total size of the audits in bytes. Send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audit-metrics/
```

The body of the request is empty.

The response contains the following fields:

- Count - the number of audits existing in the specified workspace.

- SizeInBytes - the total size of the all the audits in bytes.

Copy

```text
1
2
3
4
{

  "Count": 1579490,

  "SizeInBytes": 813470096

}
```

## Audit Revert service

The Audit Revert service supports reverting document update actions. It provides endpoints for reverting a single action or list of actions, and for verifying whether the revert operation can be performed on an action.

For example, you can use an endpoint on this service as a programmatic shortcut for reverting incorrect coding decisions.

### Validate a revert operation for an audit action

To validate that an audit action can be reverted, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/revert/validate/
```

View the field descriptions and sample JSON for a request

The request must contain the following fields:

- workspaceId - the Artifact ID of the workspace containing the action that you want to revert. This field is optional in the request. If a mismatch occurs between the ID in this field and the URL, then the ID in the URL is used in the request.

- request - represents a request to revert an action. It contains the following fields:

- AuditId - the identifier assigned by Relativity to an audit action.

- Timestamp - the date and time of the audit action.

The request requires the Timestamp and Id fields to uniquely identify the audit record.

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

    "workspaceId": 1018053,

    "request": {

        "AuditId": "430133",

        "Timestamp": "2019-04-25T16:05:24.867"

    }

}
```

View the field descriptions and sample JSON for a response

The response contains the following fields:

- AuditId - the identifier assigned by Relativity to an audit.

- Timestamp - the date and time of the audit action.

- IsRevertable - a Boolean value indicating whether you can revert an audit action.

- Message - information explaining why an audit action can't be reverted.

##### An audit that can be reverted

Copy

```text
1
2
3
4
5
{

    "AuditId": "1409184",

    "Timestamp": "2019-05-22T15:10:42.877",

    "IsRevertable": true

}
```

##### An audit that can't be reverted

Copy

```text
1
2
3
4
5
6
{

    "AuditId": "430133",

    "Timestamp": "2019-04-25T16:05:24.867",

    "IsRevertable": false,

    "Message": "This audit does not represent the most recent change to this document."

}
```

### Revert an audit

To revert an audit action, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/revert/
```

Before reverting an action, consider calling the ValidateRevertAuditAsync() method to verify that the revert operation can succeed.

View the field descriptions and sample JSON for a request

The request contains the following fields:

- workspaceId - the Artifact ID of the workspace containing the action that you want to revert. This field is optional in the request. If a mismatch occurs between the ID in this field and the URL, then the ID in the URL is used in the request.

- request - represents a request to revert an action. It contains the following fields:

- AuditId - the identifier assigned by Relativity to an audit action.

- Timestamp - the date and time of the audit action.

The request requires the Timestamp and Id fields to uniquely identify the audit record.

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

    "workspaceId": 1018053,

    "request": {

        "AuditId": "4301335",

        "Timestamp": "2019-04-25T16:05:24.867"

    }

}
```

View the field descriptions and sample JSON for a response

The response contains the following fields

- Success - a Boolean value indicating whether the action was reverted.

- ValidationResponse - contains the following fields:

- AuditId - the identifier assigned by Relativity to an audit.

- Timestamp - the date and time of the audit action.

- IsRevertable - a Boolean value indicating whether the audit action was reverted.

- Message - information explaining why an audit action can't be reverted.

- Message - additional information about the revert operation.

##### A reverted audit

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
{

  "Success": true,

  "ValidationResponse": {

    "AuditId": "1409184",

    "Timestamp": "2019-05-22T15:10:42.877",

    "IsRevertable": true,

    "Message": null

  },

  "Message": null

}
```

##### An audit that can't be reverted

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
{

  "Success": false,

  "ValidationResponse": {

    "AuditId": "1409184",

    "Timestamp": "2019-05-22T15:10:42.877",

    "IsRevertable": false,

    "Message": "This audit does not represent the most recent change to this document."

  },

  "Message": null

}
```

### Mass revert a list of audits

You can control the maximum number of Audits that can be reverted during a mass operation by updating the RevertMaxAuditCount instance setting. For more information, see Instance settings descriptions on the Relativity Documentation site.

This endpoint validates that each action can be successfully reverted before performing this operation.

To revert a list of audit actions, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/mass-revert/
```

View the field descriptions and sample JSON for a request

The request must contain the following fields:

- Request - represents a request to revert multiple actions. It contains the following fields:

- RevertAuditRequests - an array of audit actions to revert. Each audit action includes the following fields:

- AuditId - the identifier assigned by Relativity to an audit.

- Timestamp - the date and time of the audit action.

The request requires the Timestamp and Id fields to uniquely identify the audit record.

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

    "request": {

        "RevertAuditRequests": [

            {

                "AuditId": "1409184",

                "Timestamp": "2019-05-22T15:10:42.877"

            },

            {

                "AuditId": "1409411",

                "Timestamp": "2019-05-22T15:35:01.947"

            }

        ]

    }

}
```

View the field descriptions and sample JSON for a response

The response contains the following fields:

- Success - a Boolean value indicating whether the action was reverted.

- ValidationResponses - contains the following fields for each action:

- AuditId - the identifier assigned by Relativity to an audit.

- Timestamp - the date and time of the audit action.

- IsRevertable - a Boolean value indicating whether the audit action was reverted.

- Message - information explaining why an audit action can't be reverted.

View a sample JSON response for reverting a list of audits

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
{

  "Success": false,

  "ValidationResponses": [

    {

      "AuditId": "1409184",

      "Timestamp": "2019-05-22T15:10:42.877",

      "IsRevertable": false,

      "Message": "This audit does not represent the most recent change to this document."

    },

    {

      "AuditId": "1409411",

      "Timestamp": "2019-05-22T15:35:01.947",

      "IsRevertable": true,

      "Message": null

    }

  ]

}
```

## Audit Pivot service

The Audit Pivot service supports running pivot queries on audit data. You can query with the group by and pivot on operations for object type, action, username, and timestamp fields.

After the call returns the pivot results, you can render them as graphs and charts with third-party visualization tools. Pivot queries on audit records use the same query pattern as Relativity Pivot. For more information, see Pivot Manager (REST) .

### Query with Pivot on audit data

To query on audit pivot data, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/pivots/
```

View the descriptions of fields in the request

The request contains the following fields:

- workspaceId - the Artifact ID of the target workspace. This field is optional in the request. If a mismatch occurs between the ID in this field and the URL, then the ID in the URL is used in the request.

- settings - represents the pivot fields to query. It contains the following fields:

- GroupBy - the Artifact ID of the object to group by, such as the audit action or username.

- PivotOn - the Artifact ID of the field to use as the pivot on value in the query and result set. For example, you might use the audit action, object type, or username. The field must have pivot functionality enabled on it.

- ObjectSetQuery - defines a base set of documents or objects to run a Pivot query against. You can use the following properties on the ObjectSetQuery object for filtering:

- Condition - the search criteria used in the query. This field is optional.

- RowCondition - a filtering condition criteria for the result set. This field is optional. For example, you might set this field as follows: "RowCondition": "((('Audit ID' LIKE ['1409579'])))" .

- ConvertNumberFieldValuesToString - a Boolean value indicating whether to convert response field values to strings. This field is optional.

- TimeZone - a time zone URL.

- cancel - a required field that contains the following:

- RequestId - a GUID.

- TicketId - a GUID.

- progress - a required field that contains the following:

- RequestId - a GUID.

- TicketId - a GUID.

The use of progress indicators and cancellation tokens isn't supported, but you must include the cancel and progress fields in the request.

View a sample JSON request for a pivot query on an audit Copy

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
{

    "workspaceId": 1018053,

    "settings": {

        "GroupBy": {

            "ArtifactID": 1039619

        },

        "PivotOn": {

            "ArtifactID": 1039617

        },

        "ObjectSetQuery": {

            "Condition": "",

            "RowCondition": "(('User Name' == CHOICE 1039872))"

        },

        "ConvertNumberFieldValuesToString": true,

        "TimeZone": "America/Chicago"

    },

    "cancel": {

        "RequestId": "e54e41a4-d2fb-439c-b517-1717dafc00ee",

        "TicketId": "e54e41a4-d2fb-439c-b517-1717dafc00ee"

    },

    "progress": {

        "RequestId": "e54e41a4-d2fb-439c-b517-1717dafc00ee",

        "TicketId": "e54e41a4-d2fb-439c-b517-1717dafc00ee"

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- Results - an array of items that meet the criteria specified in the pivot query.

- Timestamp - the date and time of the audit action.

- List of data

- Grand Total - the number of data elements.

- TotalCount - the total number of results returned by the pivot.

- QueryToken - reserved for future use.

- Success - a Boolean value indicating whether the query succeeded.

- Message - a message indicating the status of a pivot query. If the query failed, the message contains information about the errors that occurred.

- PivotIdToDisplayValueMap - if a PivotOn field is specified in the request, the object maps the system-generated pivot item IDs to display values for visualization.

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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
{

    "Results": [

        {

            "Timestamp": "2019-04-16T05:00:00",

            "_x0039_": 5,

            "_x0033_": 1,

            "_x0032_8": 1,

            "_x0032_": 0,

            "_x0031_": 0,

            "_x0033_2": 0,

            "_x0032_9": 0,

            "_x0033_3": 0,

            "_x0033_5": 0,

            "_x0031_0": 0,

            "_x0035_8": 0,

            "_x0035_9": 0,

            "Grand Total": 7

        },

        {

            "Timestamp": "2019-04-17T05:00:00",

            "_x0039_": 0,

            "_x0033_": 0,

            "_x0032_8": 0,

            "_x0032_": 0,

            "_x0031_": 0,

            "_x0033_2": 0,

            "_x0032_9": 0,

            "_x0033_3": 0,

            "_x0033_5": 0,

            "_x0031_0": 0,

            "_x0035_8": 0,

            "_x0035_9": 0,

            "Grand Total": 0

        },

        {

            "Timestamp": "2019-04-18T05:00:00",

            "_x0039_": 0,

            "_x0033_": 0,

            "_x0032_8": 0,

            "_x0032_": 0,

            "_x0031_": 0,

            "_x0033_2": 0,

            "_x0032_9": 0,

            "_x0033_3": 0,

            "_x0033_5": 0,

            "_x0031_0": 0,

            "_x0035_8": 0,

            "_x0035_9": 0,

            "Grand Total": 0

        },

               ...

    ],

    "TotalCount": 37,

    "QueryToken": "",

    "Success": true,

    "Message": "SUCCESS",

    "PivotIdToDisplayValueMap": [

        [

            "Timestamp",

            "Timestamp"

        ],

        [

            "_x0039_",

            "Delete"

        ],

        [

            "_x0033_",

            "Update"

        ],

        [

            "_x0032_8",

            "Document Query"

        ],

        [

            "_x0032_",

            "Create"

        ],

        [

            "_x0031_",

            "View"

        ],

        [

            "_x0033_2",

            "Import"

        ],

        [

            "_x0032_9",

            "Query"

        ],

        [

            "_x0033_3",

            "Export"

        ],

        [

            "_x0033_5",

            "RelativityScriptExecution"

        ],

        [

            "_x0031_0",

            "Security"

        ],

        [

            "_x0035_8",

            "Update - Revert"

        ],

        [

            "_x0035_9",

            "Update - Mass Revert"

        ],

        [

            "Grand Total",

            "Grand Total"

        ]

    ]

}
```

## Reviewer Statistics service

The Reviewer Statistics service provides endpoints for returning information about reviewer actions, such as the number of actions performed by a reviewer on a document, the usage time per review, a summary report of reviewer actions, and others.

See the following subsections for more information:

- Retrieve action counts for updated documents

- Retrieve the usage time per reviewer

- Retrieve size of the extracted text for reviewed documents

- Retrieve an aggregation of user actions by hour

- Retrieve choices reviewed by users

- Retrieve a summary report of reviewer statistics

### Retrieve action counts for updated documents

You can retrieve the total action counts for all the updated documents in a workspace for a specified time frame. Additionally, you can list specific actions that you want counted per document. Send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/document-action-counts/
```

View the descriptions of fields in the request

The request contains the following fields:

- criteria - represents the actions, users, and timeframe used when retrieving counts for audit actions. It contains the following fields:

- AuditActionIds - an array of identifiers for the audit actions performed on document. This endpoint retrieves the counts for the following supported actions:

Name Value

View 1

Update 3

Mass edits 4

Propagation 6

- UserIds - an array of Artifact IDs for Relativity users whose audit actions are included in the report.

If you pass an empty array, the report is computed for all the users in the workspace.

- StartDate - the initial date for the reporting period.

- EndDate - the final date for the reporting period.

- TimeZone - a time zone URL.

View a sample JSON request for total action counts on a document Copy

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

    "criteria": {

        "AuditActionIds": [

            1,

            4,

            3

        ],

        "UserIds": [

            9,

            777

        ],

        "StartDate": "2019-05-01T22:53:55.1169908+00:00",

        "EndDate": "2019-05-22T22:54:19.7619193+00:00",

        "TimeZone": "US/Central"

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- ReviewerStatistics - includes information returned for specific reviewer criteria. It contains the following fields:

- UserId - the Artifact ID for a Relativity user.

- Statistics -includes information about the action counts returned. It contains the following field:

- ActionCounts - an array of counts returned for a user. It contains the following fields:

- AuditActionId - the identifier for an audit actions performed on document.

- Count - the total number of actions performed on a document object.

- DistinctDocumentCount - the total number of actions performed on distinct documents.

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
{

  "ReviewerStatistics": [

    {

      "UserId": 9,

      "Statistics": {

        "ActionCounts": [

          {

            "AuditActionId": 1,

            "Count": 13,

            "DistinctDocumentCount": 3

          },

          {

            "AuditActionId": 3,

            "Count": 13,

            "DistinctDocumentCount": 2

          }

        ]

      }

    }

  ]

}
```

### Retrieve the usage time per reviewer

To compute the total usage time in seconds per reviewer, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/usage-time/
```

View the descriptions of fields in the request

The request contains the following fields:

- criteria - represents the actions, users, and timeframe used when retrieving counts for usage times. It contains the following fields:

- AuditActionIds - an array of identifiers for the audit actions performed on document.

- UserIds - an array of Artifact IDs for Relativity users whose audit actions are included in the report.

If you pass an empty array, the report is computed for all the users in the workspace.

- StartDate - the initial date for the reporting period.

- EndDate - the final date for the reporting period.

- TimeZone - a time zone URL.

- DownTime - the number of seconds used to determine whether a null session action should be joined to a non-null session action. If the time difference for the performance of a null session action is larger than this maximum duration, the null session is counted as one minute. The default value is 900 secs.

View a sample JSON request for retrieving usage time per reviewer Copy

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
{

    "criteria": {

        "AuditActionIds": [

            1,

            4,

            3

        ],

        "UserIds": [

            9,

            777

        ],

        "StartDate": "2019-05-01T22:53:55.1169908+00:00",

        "EndDate": "2019-05-22T22:54:19.7619193+00:00",

        "TimeZone": "US/Central",

        "DownTime": 900

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- ReviewerStatistics - includes information returned for specific reviewer criteria. It contains the following fields:

- UserId - the Artifact ID for a Relativity user.

- Statistics - includes information about the usage time. It contains the following field:

- TotalSeconds - the total number of seconds that a reviewer used to complete the specified actions.

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
{

  "ReviewerStatistics": [

    {

      "UserId": 777,

      "Statistics": {

        "TotalSeconds": 1081

      }

    },

    {

      "UserId": 9,

      "Statistics": {

        "TotalSeconds": 12939

      }

    }

  ]

}
```

### Retrieve size of the extracted text for reviewed documents

To retrieve the size of the extracted text for all documents reviewed per reviewer, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/total-reviewed-text-size/
```

View the descriptions of fields in the request

The request contains the following fields:

- criteria - represents the actions, users, and timeframe used when retrieving the size of extracted text for reviewed documents. It contains the following fields:

- AuditActionIds - an array of identifiers for the audit actions performed on document.

- UserIds - an array of Artifact IDs for Relativity users whose audit actions are included in the report.

If you pass an empty array, the report is computed for all the users in the workspace.

- StartDate - the initial date for the reporting period.

- EndDate - the final date for the reporting period.

- TimeZone - a time zone URL.

- ExtractedTextFieldArtifactId - the Artifact ID of an extracted text field in the specified workspace.

View a sample JSON request for the extracted text size of reviewed documents Copy

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
{

    "criteria": {

        "AuditActionIds": [

            1,

            4,

            3

        ],

        "UserIds": [

            9,

            777

        ],

        "StartDate": "2019-05-01T22:53:55.1169908+00:00",

        "EndDate": "2019-05-22T22:54:19.7619193+00:00",

        "TimeZone": "US/Central",

        "ExtractedTextFieldArtifactId": 1003668

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- ReviewerStatistics - includes information returned for specific reviewer criteria. It contains the following fields:

- UserId - the Artifact ID for a Relativity user.

- Statistics - includes information about the extracted text size. It contains the following field:

- TotalBytes - the total number of bytes of extracted text size for all of documents reviewed by the specified reviewer.

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
{

  "ReviewerStatistics": [

    {

      "UserId": 9,

      "Statistics": {

        "TotalBytes": 5312

      }

    }

  ]

}
```

### Retrieve an aggregation of user actions by hour

You can aggregate the total distinct document actions performed by each reviewer, grouped by the hour of the day in which the action was performed. Send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/distinct-document-actions-per-hour-of-day/
```

View the descriptions of fields in the request

The request contains the following fields:

- criteria - represents the actions, users, and timeframe used when retrieving an aggregate of user actions per hour. It contains the following fields:

- AuditActionIds - an array of identifiers for the audit actions performed on document.

- UserIds - an array of Artifact IDs for Relativity users whose audit actions are included in the report.

If you pass an empty array, the report is computed for all the users in the workspace.

- StartDate - the initial date for the reporting period.

- EndDate - the final date for the reporting period.

- TimeZone - a time zone URL.

View a sample JSON request for an aggregation of user actions Copy

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
{

    "criteria": {

        "AuditActionIds": [

            3,

            4

        ],

        "UserIds": [

            9,

            777

        ],

        "StartDate": "2019-05-15T00:00:00.2770527-05:00",

        "EndDate": "2019-05-22T00:00:00.2770527-05:00",

        "TimeZone": "America/Chicago"

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- ReviewerStatistics - includes information returned for specific reviewer criteria. It contains the following fields:

- UserId - the Artifact ID for a Relativity user.

- Statistics - includes information about the hour buckets returned. It contains the following field:

- HourBuckets - an array of counts returned for a user. It contains the following fields:

- HourOfDay - the hour of day when that the user performed the audit actions. This field uses the 24-hour clock format.

- ActionCount - the number of audit actions that the user performed within the hour.

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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
{

  "ReviewerStatistics": [

    {

      "UserId": 9,

      "Statistics": {

        "HourBuckets": [

          {

            "HourOfDay": 0,

            "ActionCount": 0

          },

          {

            "HourOfDay": 1,

            "ActionCount": 0

          },

          {

            "HourOfDay": 2,

            "ActionCount": 0

          },

          {

            "HourOfDay": 3,

            "ActionCount": 0

          },

          {

            "HourOfDay": 4,

            "ActionCount": 0

          },

          {

            "HourOfDay": 5,

            "ActionCount": 0

          },

          {

            "HourOfDay": 6,

            "ActionCount": 0

          },

          {

            "HourOfDay": 7,

            "ActionCount": 0

          },

          {

            "HourOfDay": 8,

            "ActionCount": 0

          },

          {

            "HourOfDay": 9,

            "ActionCount": 0

          },

          {

            "HourOfDay": 10,

            "ActionCount": 4

          },

          {

            "HourOfDay": 11,

            "ActionCount": 0

          },

          {

            "HourOfDay": 12,

            "ActionCount": 2

          },

          {

            "HourOfDay": 13,

            "ActionCount": 0

          },

          {

            "HourOfDay": 14,

            "ActionCount": 1

          },

          {

            "HourOfDay": 15,

            "ActionCount": 4

          },

          {

            "HourOfDay": 16,

            "ActionCount": 0

          },

          {

            "HourOfDay": 17,

            "ActionCount": 0

          },

          {

            "HourOfDay": 18,

            "ActionCount": 0

          },

          {

            "HourOfDay": 19,

            "ActionCount": 0

          },

          {

            "HourOfDay": 20,

            "ActionCount": 0

          },

          {

            "HourOfDay": 21,

            "ActionCount": 0

          },

          {

            "HourOfDay": 22,

            "ActionCount": 0

          },

          {

            "HourOfDay": 23,

            "ActionCount": 0

          }

        ]

      }

    }

  ]

}
```

### Retrieve choices reviewed by users

You can retrieve information about the choices reviewed by users in a specific workspace. This endpoint supports retrieving statistics for single choice fields, multiple choice fields, and Yes/No fields. Send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/reviewer-choices/
```

View the descriptions of fields in the request

The request contains the following fields:

- reviewerChoicesCriteria - represents the fields, users, and timeframe used when retrieving choices set in reviews. It contains the following fields:

- FieldIds - an array of Artifact IDs for fields used to compute the choices selected by reviewers. You can retrieve statistics for single choice fields, multiple choice fields, and Yes/No fields.

- StartDate - the initial date for the reporting period.

- EndDate - the final date for the reporting period.

- TimeZone - a time zone URL.

- UserIdsToExcludeInReport - an array of Artifact IDs for users who choice selections must be excluded from the report.

- UserIdsToIncludeInReport - an array of Artifact IDs for users who choice selections must be included in the report.

If you pass an empty array for the UserIdsToExcludeInReport or the UserIdsToIncludeInReport field, the report is computed for all the users in the workspace.

View a sample JSON request for choices set in reviews Copy

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

    "reviewerChoicesCriteria": {

        "FieldIds": [

            1035357

        ],

        "EndDate": "2019-05-22T16:20:16.000",

        "StartDate": "2019-05-01T16:20:16.000",

        "TimeZone": "America/Chicago",

        "UserIdsToExcludeInReport": [

            777

        ],

        "UserIdsToIncludeInReport": [

            9

        ]

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- ReviewerStatistics - includes information returned for specific reviewer criteria. It contains the following fields:

- UserId - the Artifact ID for a Relativity user.

- Statistics - includes information about the choices that are set by reviewers. It contains the following field:

- ReviewedFieldChoices - an array of fields reviewed by a user. Each item in the array contains the following fields:

- FieldId - the Artifact ID of the field in Relativity.

- ReviewedChoices - an array of choices that a reviewer used for coding. Each choice contains the following information:

- ChoiceId - the Artifact ID of the choice in Relativity.

- Count - the number of times this choice was set on the field.

- TotalChoicesUnset - an integer value indicating the number of choices on this field that weren't used by a reviewer for coding.

- FieldType - an integer that Relativity uses to identify the type of a field. The FieldType enumeration contains the following values.

Name Value

MultipleChoice 0

SingleChoice 1

YesOrNo 2

- TotalDocsUpdated - an integer value indicating the total number of documents that the reviewer coded with a choice.

- TotalChoicesUnset - an integer value indicating the total number of choices that weren't used by a reviewer for coding.

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
28
29
30
31
32
33
34
35
36
{

  "ReviewerStatistics": [

    {

      "UserId": 9,

      "Statistics": {

        "ReviewedFieldChoices": [

          {

            "FieldId": 1035357,

            "ReviewedChoices": [

              {

                "ChoiceId": 1035871,

                "Count": 0

              },

              {

                "ChoiceId": 1035850,

                "Count": 0

              },

              {

                "ChoiceId": 1035916,

                "Count": 0

              },

              {

                "ChoiceId": 1035891,

                "Count": 2

              }

            ],

            "TotalChoicesUnset": 0,

            "FieldType": 1

          }

        ],

        "TotalDocsUpdated": 2,

        "TotalChoicesUnset": 0

      }

    }

  ]

}
```

### Retrieve a summary report of reviewer statistics

You can programmatically generate a report similar to the reviewer statistics report available through the Relativity UI. For more information, see Reviewer statistics on the Relativity Documentation site.

You must specify the time zone of the reviewers and indicate whether to include system admin statistics in the data.

To generate a summary report, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/summary-report/
```

View the descriptions of fields in the request

The request contains the following fields:

- reviewerStatsDataRequest - a request to generate a report based on the specified settings. It contains the following fields:

- startDate - the initial date of the reporting period.

- endDate - the final date of the reporting period.

- timeZone - the time zone for the reviews included in the report. The time zone is specified as a UTC offset.

- downTimeThreshold - the expected downtime (in seconds) between audit records. By default, this value is to 900 seconds (15 minutes).

- nonAdmin - indicates whether the report is for non-admin users only.

- additionalActions - indicates whether to include statistics for mass edits and propagation actions. Set this field to one of the following values:

- None - include view and update actions.

- Mass Edit - include view, update, and mass edit actions.

- Propagation - include propagation actions.

- Mass Edit and Propagation - include view, update, mass edit, and propagation actions.

View a sample JSON request for generating a reviewer statistics report Copy

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
{

    "reviewerStatsDataRequest": {

        "startDate": "2019-01-01T00:00:00Z",

        "endDate": "2019-10-05T00:00:00Z",

        "timeZone": "-06.0",

        "downTimeThreshold": "900",

        "nonAdmin": false,

        "additionalActions": "None"

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

In the following descriptions, the term distinct indicates that an action occurred only once per document.

- FullName - the full name for the user.

- UserId - the Artifact ID for a Relativity user.

- TotalUsageTime - calculated as the difference between the time the reviewer first views or edits any document in the workspace, and the time the reviewer last views or edits any document in the workspace per session. A session is the timeframe during which the user is logged in to Relativity. All sessions for the selected date range are then totaled per reviewer.

- Views - the total number of documents that the reviewer looked at during the reporting period.

- DistinctViews - the number of unique documents that the reviewer looked at during the reporting period.

- Edits - the total number of editing or coding decisions made during the reporting period.

- DistinctEdits - the total number of documents edited, excluding repeated edits of the same document.

- EditsPerHour - the number of edits per hour based on the total usage time of the reviewer.

- EditsPerDay - the number of edits performed per day during the reporting period.

- DistinctEditsPerHour - the number of distinct edits per hour based on the total usage time of the reviewer.

- DistinctEditsPerDay - the number of distinct edits performed per day during the reporting period.

- DistinctMassEditsPerHour - the number of distinct mass edits per hour based on the total usage time of the reviewer.

- DistinctMassEditsPerDay - the number of distinct mass edits per day during the reporting period.

- MassEdits - the total number of document edits performed with the mass edit action.

- DistinctMassEdits - the total number of unique document edits performed with the mass edit action.

- MassEditsPerHour - the number of mass edits per hour based on the total usage time of the reviewer.

- MassEditsPerDay - the number of mass edits per day during the reporting period.

- Propagations - the total number of documents that were updated via propagation.

- DistinctPropagations - the total number of unique documents that were updated via propagation.

- DistinctMassPropagationsPerHour - the number of unique documents that had propagations applied per hour based on the total usage time of the reviewer.

- DistinctMassPropagationsPerDay - the number of unique documents that had propagations applied per day based during the reporting period.

- PropagationsPerHour - the number of propagations applied per hour based on the total usage time of the reviewer.

- PropagationsPerDay - the number of propagations applied per day based on the reporting period.

View sample JSON for a statistics report Copy

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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
[

  {

    "FullName": "Service Account, Relativity",

    "UserId": 777,

    "TotalUsageTime": "2:34:08",

    "Views": 0,

    "DistinctViews": 0,

    "Edits": 0,

    "DistinctEdits": 0,

    "EditsPerHour": 0,

    "EditsPerDay": 0,

    "DistinctEditsPerHour": 0,

    "DistinctEditsPerDay": 0,

    "MassEdits": 0,

    "DistinctMassEdits": 0,

    "DistinctMassEditsPerHour": 0,

    "DistinctMassEditsPerDay": 0,

    "MassEditsPerHour": 0,

    "MassEditsPerDay": 0,

    "Propagations": 0,

    "DistinctPropagations": 0,

    "DistinctMassPropagationsPerHour": 0,

    "DistinctMassPropagationsPerDay": 0,

    "PropagationsPerHour": 0,

    "PropagationsPerDay": 0

  },

  {

    "FullName": "Admin, Relativity",

    "UserId": 9,

    "TotalUsageTime": "11:35:28",

    "Views": 37,

    "DistinctViews": 3,

    "Edits": 31,

    "DistinctEdits": 3,

    "EditsPerHour": 2.67,

    "EditsPerDay": 0.11,

    "DistinctEditsPerHour": 0.26,

    "DistinctEditsPerDay": 0.01,

    "MassEdits": 0,

    "DistinctMassEdits": 0,

    "DistinctMassEditsPerHour": 0,

    "DistinctMassEditsPerDay": 0,

    "MassEditsPerHour": 0,

    "MassEditsPerDay": 0,

    "Propagations": 0,

    "DistinctPropagations": 0,

    "DistinctMassPropagationsPerHour": 0,

    "DistinctMassPropagationsPerDay": 0,

    "PropagationsPerHour": 0,

    "PropagationsPerDay": 0

  }

]
```

## Audit Query service

The Audit Query service supports querying for a specific audit record.

### Query for an audit record

To read a single audit record, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/
```

View the descriptions of fields in the request

The request contains the following fields:

- workspaceId - the Artifact ID of the target workspace. To return the instance-level audit records, specify -1. This field is optional in the request. If a mismatch occurs between the ID in this field and the URL, then the ID in the URL is used in the request.

- request - represents a read operation on an audit record:

- Id - the identifier for the audit record generated by Relativity.

- Timestamp - the date and time that the audit record was created.

The request requires the Timestamp and Id fields to uniquely identify the audit record.

View a sample JSON request for a query on an audit record Copy

```text
1
2
3
4
5
6
7
{

    "workspaceId": 1018053,

    "request": {

        "Id": "484127",

        "Timestamp": "2019-04-26T15:56:53.427"

    }

}
```

View the descriptions of fields in the response

The response contains the following fields:

- ID - the ID of the audit record.

- TimeStamp - the date and time of the audit action.

- ArtifactName - the name of the audited artifact, such as the document control number.

- ActionName - the audit action name, such as create, update, query, or others.

- ActionID - the audit action ID.

- ObjectTypeName - the object type of the audited artifact, such as workspace or document.

- ObjectTypeID - the object type ID of the audited artifact.

- ExecutionTime - the length of time in milliseconds used to generate the audit details report.

- ArtifactID - the Artifact ID of the audited artifact.

- UserName - the username associated with the audit record.

- UserID - the Artifact ID of the user associated with the audit record.

- Details - the detailed audit action information.

- OldValues - the values of the fields that have been changed by the action.

- NewValues - the values of the fields that have been set by the action.

- Fields - the fields that have been changed by the action.

- WorkspaceId - the Artifact ID of the workspace associated with the audit record.

- WorkspaceName - the name of the workspace associated with the audit record.

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
38
39
40
41
42
43
44
{

    "ID": "484127",

    "TimeStamp": "2019-04-26T15:56:53.427",

    "ArtifactName": "Audit",

    "ActionName": "Query",

    "ActionID": 29,

    "ObjectTypeName": "Workspace",

    "ObjectTypeID": 8,

    "ExecutionTime": 0,

    "ArtifactID": 1003663,

    "UserName": "Service Account, Relativity",

    "UserID": 777,

    "Details": {

        "auditElement": {

            "OperationID": "|56237733-44595bea4f441873.",

            "QueryText": "SELECT * FROM EveryThing;",

            "QueryParameters": {

                "Parameter": [

                    {

                        "@Name": "@p1",

                        "#text": "1",

                        "@dbType": "Int"

                    },

                    {

                        "@Name": "@p2",

                        "#text": "1000011",

                        "@dbType": "Int"

                    },

                    {

                        "@Name": "@p3",

                        "#text": "1039633",

                        "@dbType": "Int"

                    }

                ]

            },

            "Milliseconds": "0"

        }

    },

    "OldValues": [],

    "NewValues": [],

    "Fields": [],

    "WorkspaceId": 1018053,

    "WorkspaceName": "Audit"

}
```

## Audit Object Manager UI service

The Audit Object Manager UI service supports querying on audit details for display in the Relativity UI. It provides two endpoints for querying:

- query - This endpoint returns detailed information about the field-value pairs returned by the query on the audit, including complete field details. For samples, see Query endpoint .

Copy

```text
1
<host>/Relativity.Rest/API/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/UI/query/
```

- queryslim - This endpoint returns a smaller payload to save bandwidth. It returns only the values of the fields specified in the request without the detailed field information. For samples, see Query on audit fields and return a smaller payload . Copy

```text
1
<host>/Relativity.Rest/API/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/UI/query-slim/
```

Review the following guidelines for Audit Object Manager UI service:

- Sorting is only supported for Timestamp and ExecutionTime fields.

- Use condition and rowCondition properties on the request object for filtering. For more information, see Query conditions .

- Review the following information about paging:

- Query tokens aren't supported for audit record result set paging.

- Check the value of the TotalCount field on the initial response. If it is greater than the specified Length field in the request, adjust the value of the Start field on the subsequent query requests to page through results.

In Relativity instances with a very large number of audit records (1,000,000 or more), paging towards the end of the result set can cause a Deep Paging Exception.

- The Audit record query uses the Relativity Object Manager query pattern. For more information, see Object Manager (REST) .

- Use the endpoint with the auditQueryOptions field if you want to perform additional analysis on the audit data. This endpoint returns the data as an escaped JSON string instead of HTML. For more information, see Query with additional query options .

### Query endpoint

To use the query endpoint, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/UI/query/
```

#### Query on audit fields

You can query for specific fields in an audit as illustrated in the following example.

View the descriptions of fields in the request

The request contains the following fields:

- request - represents a query request for audit information. It contains the following fields:

-

fields - an array of fields used like a SELECT statement in an SQL query. You must specify the field name. This array contains the following:

- Name - the user-friendly name for the field.

- Guids - an array of GUIDs used to identify the field.

- ArtifactID - the Artifact ID for field.

- condition - the search criteria used in the query. For more information, Query conditions . This field is optional.

- rowCondition - the filtering condition criteria for the result set. For more information, Query conditions . This field is optional.

- executingViewId - reserved for future use.

- start - the values in the start and length fields both determine the page number being requested. For example, if you set length to 25 and start to record 17, Relativity interprets these setting as a request for the first page and returns audits 1-25. If you set start to 35, it returns the second page with audits 26-50.

- length - the number of items to return in the query result, beginning with index in the start field. See description for start field.

View a sample JSON request for a query on specific fields Copy

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
{

    "request": {

        "fields": [

            {

                "Name": "User Name",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Details",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Old Value",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "New Value",

                "Guids": [],

                "ArtifactID": 0

            }

        ],

        "condition": "",

        "rowCondition": "",

        "executingViewId": 1039633

    },

    "start": 1,

    "length": 2

}
```

View the descriptions of fields in the response

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array of audit objects. The following fields are listed for each object:

- ParentObject - reserved for future use.

- Name - contains the Artifact ID of the parent object associated with object returned by the query operation.

- FieldValues - an array containing FieldValuePair objects. It contains the following:

- Value - the data assigned to a field.

- Field - a field associated with a specific value. The Field object contains the following:

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- ViewFieldID - a unique identifier used to reference a view field.

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

- ArtifactID - a unique identifier for the object returned by the query.

- Guids - an array of GUIDs used to identify the object returned by the query.

- IDWindow - reserved for future use.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - reserved for future use.

- SampleDetails - reserved for future use.

- RankWindow - reserved for future use.

- RelationalField - name of relational field to expand query results to related objects.

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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
{

  "TotalCount": 1586265,

  "Objects": [

    {

      "ParentObject": null,

      "Name": "1415378",

      "FieldValues": [

        {

          "Value": "1415378",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 0,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Audit ID"

          }

        },

        {

          "Value": "\r\n\t\t\t\t\t\t<div>\r\n\t\t\t\t\t\t\t<a class=\"fluid-item-list-cell-link\" target=\"_top\" onclick=\"relativity.raiseCustomItemListEvent('fil_itemListFUI',1,'audit_modal_view',[1018053,'1415378','2019-05-23T02:22:37.320']);\">\r\n\t\t\t\t\t\t\t\t<img src=\"/Relativity/images/pop_up_icon.png\" alt=\"Show Audit Details\"></img>\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t</div>",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 4,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Details"

          }

        }

      ],

      "ArtifactID": 1003663,

      "Guids": []

    },

    {

      "ParentObject": null,

      "Name": "1415377",

      "FieldValues": [

        {

          "Value": "1415377",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 0,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Audit ID"

          }

        },

        {

          "Value": "\r\n\t\t\t\t\t\t<div>\r\n\t\t\t\t\t\t\t<a class=\"fluid-item-list-cell-link\" target=\"_top\" onclick=\"relativity.raiseCustomItemListEvent('fil_itemListFUI',1,'audit_modal_view',[1018053,'1415377','2019-05-23T02:22:37.290']);\">\r\n\t\t\t\t\t\t\t\t<img src=\"/Relativity/images/pop_up_icon.png\" alt=\"Show Audit Details\"></img>\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t</div>",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 4,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Details"

          }

        }

      ],

      "ArtifactID": 1003663,

      "Guids": []

    }

  ],

  "IDWindow": [

    1,

    2

  ],

  "CurrentStartIndex": 1,

  "ResultCount": 2,

  "ObjectType": {

    "ArtifactID": 0,

    "Name": "",

    "Guids": [],

    "ArtifactTypeID": 0

  },

  "SampleDetails": null,

  "RankWindow": [

    0

  ],

  "RelationalField": null

}
```

#### Query for a specific audit object

You can query on a specific audit object as illustrated in the following example.

View the descriptions of fields in the request

- request - represents a query request for audit information. It contains the following fields:

- objectType - the Audit object type identified by the Artifact Type ID on the Object Type. The values are different for each workspace and the instance-level object types. To programmatically return the Artifact Type ID, query the Relativity object types using the Services API.

- artifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- fields - an array of fields used like a SELECT statement in an SQL query. You must specify the field name. This array contains the following:

- Name - the user-friendly name for the field.

- Guids - an array of GUIDs used to identify the field.

- ArtifactID - the Artifact ID for field.

- condition - the search criteria used in the query. This field is optional.

- rowcondition - the filtering condition criteria for the result set. This field is optional.

- sorts - a collection of Sort objects. This field indicates whether the results are sorted in ascending or descending order, and identifies the field used to sort the results by name. This field is optional. See the Sort class in the kCura.Relativity.Client namespace .

- relationalField - name of relational field to expand query results to related objects. This field is optional.

- searchProviderCondition - specifies a search index other than the default keyword search index. This field is optional.

- includeIdWindow - reserved for future use.

- convertNumberFieldValuesToString - converts the response field values to strings. This field is optional.

- isAdHocQuery - reserved for future use.

- activeArtifactId - reserved for future use.

- queryHint - set a QueryHint field to optimize the view. For example, you can use the hashjoin setting with the value of true or false, or you can use the waitfor setting with a value, such as waitfor:5. This field is optional.

- executingViewId - reserved for future use.

- start - the index of the first artifact in the result set.

- length - the number of items to return in the query result, starting with index in the start field.

- cancel - represents a cancellation token. It contains the following fields:

- RequestId - a GUID.

- TicketId - a GUID.

- progress - represents a progress indicator. It contains the following fields:

- RequestId - a GUID.

- TicketId - a GUID.

The use of progress indicators and cancellation tokens isn't supported, but you must include the cancel and progress fields in the request.

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
34
35
36
37
38
39
40
41
42
43
44
45
{

    "request": {

        "objectType": {

            "artifactTypeID": 1000049

        },

        "fields": [

            {

                "Name": "Field",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Old Value",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "New Value",

                "Guids": [],

                "ArtifactID": 0

            }

        ],

        "condition": "",

        "rowCondition": "",

        "sorts": [],

        "relationalField": null,

        "searchProviderCondition": null,

        "includeIdWindow": true,

        "convertNumberFieldValuesToString": true,

        "isAdHocQuery": false,

        "activeArtifactId": null,

        "queryHint": null,

        "executingViewId": 1039633

    },

    "start": 1,

    "length": 25,

    "cancel": {

        "RequestId": "c8e47286-bbfa-4818-9d8d-175578a6b190",

        "TicketId": "c8e47286-bbfa-4818-9d8d-175578a6b190"

    },

    "progress": {

        "RequestId": "c8e47286-bbfa-4818-9d8d-175578a6b190",

        "TicketId": "c8e47286-bbfa-4818-9d8d-175578a6b190"

    }

}
```

View the descriptions of fields in the response

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array of audit objects. The following fields are listed for each object:

- ParentObject - reserved for future use.

- Name - contains the Artifact ID of the parent object associated with object returned by the query operation.

- FieldValues - an array containing FieldValuePair objects. It contains the following:

- Value - the data assigned to a field.

- Field - a field associated with a specific value. The Field object contains the following:

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- ViewFieldID - a unique identifier used to reference a view field.

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

- ArtifactID - a unique identifier for the object returned by the query.

- Guids - an array of GUIDs used to identify the object returned by the query.

- IDWindow - reserved for future use.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - reserved for future use.

- SampleDetails - reserved for future use.

- RankWindow - reserved for future use.

- RelationalField - name of relational field to expand query results to related objects.

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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
{

  "TotalCount": 1586175,

  "Objects": [

    {

      "ParentObject": null,

      "Name": "1415288",

      "FieldValues": [

        {

          "Value": "1415288",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 0,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Audit ID"

          }

        },

        {

          "Value": "{\"auditElement\":{\"OperationID\":\"9119d82e-abcc-4b0e-931c-9e0415a81c92\",\"QueryText\":\"-- records returned: 1\\r\\n-------------------\\r\\n\",\"QueryParameters\":null,\"Milliseconds\":\"0\"}}",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 4,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Details"

          }

        }

      ],

      "ArtifactID": 1003663,

      "Guids": []

    },

    {

      "ParentObject": null,

      "Name": "1415287",

      "FieldValues": [

        {

          "Value": "1415287",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 0,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Audit ID"

          }

        },

        {

          "Value": "{\"auditElement\":{\"OperationID\":\"9119d82e-abcc-4b0e-931c-9e0415a81c92\",\"QueryText\":\"-- records returned: 1\\r\\n-------------------\\r\\n\",\"QueryParameters\":null,\"Milliseconds\":\"0\"}}",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 4,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Details"

          }

        }

      ],

      "ArtifactID": 1003663,

      "Guids": []

    }

  ],

  "IDWindow": [

    1,

    2

  ],

  "CurrentStartIndex": 1,

  "ResultCount": 2,

  "ObjectType": {

    "ArtifactID": 0,

    "Name": "",

    "Guids": [],

    "ArtifactTypeID": 0

  },

  "SampleDetails": null,

  "RankWindow": [

    0

  ],

  "RelationalField": null

}
```

#### Query with additional query options

You can set additional query options so that the Details field in the Relativity UI contains an escaped JSON string instead of HTML.

View the descriptions of fields in the request

- request - represents a query request for audit information. It contains the following fields:

- objectType - the Audit object type identified by the Artifact Type ID on the Object Type. The values are different for each workspace and the instance-level object types. To programmatically return the Artifact Type ID, query the Relativity object types using the Services API.

- artifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- fields - an array of fields used like a SELECT statement in an SQL query. You must specify the field name. This array contains the following:

- Name - the user-friendly name for the field.

- Guids - an array of GUIDs used to identify the field.

- ArtifactID - the Artifact ID for field.

- condition - the search criteria used in the query. This field is optional.

- rowcondition - the filtering condition criteria for the result set. This field is optional.

- sorts - a collection of Sort objects. This field indicates whether the results are sorted in ascending or descending order, and identifies the field used to sort the results by name. This field is optional. See the Sort class in the kCura.Relativity.Client namespace .

- relationalField - name of relational field to expand query results to related objects. This field is optional.

- searchProviderCondition - specifies a search index other than the default keyword search index. This field is optional.

- includeIdWindow - reserved for future use.

- convertNumberFieldValuesToString - converts the response field values to strings. This field is optional.

- isAdHocQuery - reserved for future use.

- activeArtifactId - reserved for future use.

- queryHint - set a QueryHint field to optimize the view. For example, you can use the hashjoin setting with the value of true or false, or you can use the waitfor setting with a value, such as waitfor:5. This field is optional.

- executingViewId - reserved for future use.

- start - the index of the first artifact in the result set.

- length - the number of items to return in the query result, starting with index in the start field.

- auditQueryOptions - additional query options:

- ReturnRawDetails - a Boolean value indicating whether the Details field should contain an escaped JSON string instead of HTML. Set this field to true if you want to perform further analysis on the audit data. Otherwise, the data is returned as HTML for display on the Audit tab in the Relativity UI. For more information, see Audit in the Relativity Documentation site.

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
34
35
36
37
38
39
40
41
42
{

    "request": {

        "fields": [

            {

                "Name": "Details",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Audit ID",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Timestamp",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Object Name",

                "Guids": [],

                "ArtifactID": 0

            }

        ],

        "condition": "(('Artifact ID' IN VIEW 1039633))",

        "rowCondition": "",

        "sorts": [],

        "relationalField": null,

        "searchProviderCondition": null,

        "includeIdWindow": true,

        "convertNumberFieldValuesToString": true,

        "isAdHocQuery": false,

        "activeArtifactId": null,

        "queryHint": null,

        "executingViewId": 1039633

    },

    "start": 1,

    "length": 2,

    "auditQueryOptions": {

        "returnRawDetails": true

    }

}
```

View the descriptions of fields in the response

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array of audit objects. The following fields are listed for each object:

- ParentObject - reserved for future use.

- Name - contains the Artifact ID of the parent object associated with object returned by the query operation.

- FieldValues - an array containing FieldValuePair objects. It contains the following:

- Value - the data assigned to a field.

- Field - a field associated with a specific value. The Field object contains the following:

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- ViewFieldID - a unique identifier used to reference a view field.

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

- ArtifactID - a unique identifier for the object returned by the query.

- Guids - an array of GUIDs used to identify the object returned by the query.

- IDWindow - reserved for future use.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - reserved for future use.

- SampleDetails - reserved for future use.

- RankWindow - reserved for future use.

- RelationalField - name of relational field to expand query results to related objects.

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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
{

  "TotalCount": 1586175,

  "Objects": [

    {

      "ParentObject": null,

      "Name": "1415288",

      "FieldValues": [

        {

          "Value": "1415288",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 0,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Audit ID"

          }

        },

        {

          "Value": "{\"auditElement\":{\"OperationID\":\"9119d82e-abcc-4b0e-931c-9e0415a81c92\",\"QueryText\":\"-- records returned: 1\\r\\n-------------------\\r\\n\",\"QueryParameters\":null,\"Milliseconds\":\"0\"}}",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 4,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Details"

          }

        }

      ],

      "ArtifactID": 1003663,

      "Guids": []

    },

    {

      "ParentObject": null,

      "Name": "1415287",

      "FieldValues": [

        {

          "Value": "1415287",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 0,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Audit ID"

          }

        },

        {

          "Value": "{\"auditElement\":{\"OperationID\":\"9119d82e-abcc-4b0e-931c-9e0415a81c92\",\"QueryText\":\"-- records returned: 1\\r\\n-------------------\\r\\n\",\"QueryParameters\":null,\"Milliseconds\":\"0\"}}",

          "Field": {

            "FieldCategory": 0,

            "FieldType": 4,

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Details"

          }

        }

      ],

      "ArtifactID": 1003663,

      "Guids": []

    }

  ],

  "IDWindow": [

    1,

    2

  ],

  "CurrentStartIndex": 1,

  "ResultCount": 2,

  "ObjectType": {

    "ArtifactID": 0,

    "Name": "",

    "Guids": [],

    "ArtifactTypeID": 0

  },

  "SampleDetails": null,

  "RankWindow": [

    0

  ],

  "RelationalField": null

}
```

### Query on audit fields and return a smaller payload

To use the queryslim endpoint, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-audit/{versionNumber}/workspaces/{workspaceID}/audits/UI/query-slim/
```

The AuditQueryOptions field isn't available for the queryslim endpoint. For more information, see Query with additional query options .

View the descriptions of fields in the request

- request - represents a query request for audit information. It contains the following fields:

- objectType - the Audit object type identified by the Artifact Type ID on the Object Type. The values are different for each workspace and the instance-level object types. To programmatically return the Artifact Type ID, query the Relativity object types using the Services API.

- artifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- fields - an array of fields used like a SELECT statement in an SQL query. You must specify the field name. This array contains the following:

- Name - the user-friendly name for the field.

- Guids - an array of GUIDs used to identify the field.

- ArtifactID - the Artifact ID for field.

- condition - the search criteria used in the query. This field is optional.

- rowcondition - the filtering condition criteria for the result set. This field is optional.

- sorts - a collection of Sort objects. This field indicates whether the results are sorted in ascending or descending order, and identifies the field used to sort the results by name. This field is optional. See the Sort class in the kCura.Relativity.Client namespace .

- relationalField - name of relational field to expand query results to related objects. This field is optional.

- searchProviderCondition - specifies a search index other than the default keyword search index. This field is optional.

- includeIdWindow - reserved for future use.

- convertNumberFieldValuesToString - converts the response field values to strings. This field is optional.

- isAdHocQuery - reserved for future use.

- activeArtifactId - reserved for future use.

- queryHint - set a QueryHint field to optimize the view. For example, you can use the hashjoin setting with the value of true or false, or you can use the waitfor setting with a value, such as waitfor:5. This field is optional.

- executingViewId - reserved for future use.

- start - the index of the first artifact in the result set.

- length - the number of items to return in the query result, starting with index in the start field.

- cancel - represents a cancellation token. It contains the following fields:

- RequestId - a GUID.

- TicketId - a GUID.

- progress - represents a progress indicator. It contains the following fields:

- RequestId - a GUID.

- TicketId - a GUID.

The use of progress indicators and cancellation tokens isn't supported, but you must include the cancel and progress fields in the request.

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
34
35
36
37
38
39
40
41
42
43
44
45
{

    "request": {

        "objectType": {

            "artifactTypeID": 1000049

        },

        "fields": [

            {

                "Name": "Execution Time (ms)",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "Object ArtifactID",

                "Guids": [],

                "ArtifactID": 0

            },

            {

                "Name": "User Name",

                "Guids": [],

                "ArtifactID": 0

            }

        ],

        "condition": "",

        "rowCondition": "",

        "sorts": [],

        "relationalField": null,

        "searchProviderCondition": null,

        "includeIdWindow": true,

        "convertNumberFieldValuesToString": true,

        "isAdHocQuery": false,

        "activeArtifactId": null,

        "queryHint": null,

        "executingViewId": 1039633

    },

    "start": 1,

    "length": 25,

    "cancel": {

        "RequestId": "c8e47286-bbfa-4818-9d8d-175578a6b190",

        "TicketId": "c8e47286-bbfa-4818-9d8d-175578a6b190"

    },

    "progress": {

        "RequestId": "c8e47286-bbfa-4818-9d8d-175578a6b190",

        "TicketId": "c8e47286-bbfa-4818-9d8d-175578a6b190"

    }

}
```

View the descriptions of fields in the response

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array of audit objects. The following fields are listed for each object:

- ArtifactID - the Artifact ID of the object.

- Values - an array of values for the fields specified in the request.

- IDWindow - reserved for future use.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - reserved for future use.

- SampleDetails - reserved for future use.

- RankWindow - reserved for future use.

- RelationalField - name of relational field to expand query results to related objects.

- Fields - an array of the fields corresponding to the values.

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- ViewFieldID - a unique identifier used to reference a view field.

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

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
38
39
40
41
42
43
44
45
46
47
48
49
{

  "TotalCount": 1586275,

  "Objects": [

    {

      "ArtifactID": 1003663,

      "Values": [

        "1415388",

        "\r\n\t\t\t\t\t\t<div>\r\n\t\t\t\t\t\t\t<a class=\"fluid-item-list-cell-link\" target=\"_top\" onclick=\"relativity.raiseCustomItemListEvent('fil_itemListFUI',1,'audit_modal_view',[1018053,'1415388','2019-05-23T02:23:55.650']);\">\r\n\t\t\t\t\t\t\t\t<img src=\"/Relativity/images/pop_up_icon.png\" alt=\"Show Audit Details\"></img>\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t</div>"

      ]

    },

    {

      "ArtifactID": 1003663,

      "Values": [

        "1415387",

        "\r\n\t\t\t\t\t\t<div>\r\n\t\t\t\t\t\t\t<a class=\"fluid-item-list-cell-link\" target=\"_top\" onclick=\"relativity.raiseCustomItemListEvent('fil_itemListFUI',1,'audit_modal_view',[1018053,'1415387','2019-05-23T02:23:55.603']);\">\r\n\t\t\t\t\t\t\t\t<img src=\"/Relativity/images/pop_up_icon.png\" alt=\"Show Audit Details\"></img>\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t</div>"

      ]

    }

  ],

  "IDWindow": [

    1,

    2

  ],

  "CurrentStartIndex": 1,

  "ResultCount": 2,

  "ObjectType": null,

  "SampleDetails": null,

  "RankWindow": [

    0

  ],

  "RelationalField": null,

  "Fields": [

    {

      "FieldCategory": 0,

      "FieldType": 0,

      "ViewFieldID": 0,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Audit ID"

    },

    {

      "FieldCategory": 0,

      "FieldType": 4,

      "ViewFieldID": 0,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Details"

    }

  ]

}
```
