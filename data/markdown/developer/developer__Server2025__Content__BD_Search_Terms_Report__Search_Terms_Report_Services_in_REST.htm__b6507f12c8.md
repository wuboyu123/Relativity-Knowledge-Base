---
title: "Search Terms Report Services (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Search_Terms_Report/Search_Terms_Report_Services_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:22:29+00:00
sha256: c19f11ec4d6062bb43fe4871f6d73c9cedc2edf91afaa05f00b20e78342f0ce4
---

Search Terms Report Services (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Search Terms Report Services (REST)

Search terms reports provide the ability to identify documents containing specific keywords or terms. You can enter multiple terms and generate a report listing the number of hits for each term in a document. For more information, see Search terms report . in the Relativity Documentation site.

The Search Terms Report Services provides functionality for generating a search terms report, adding terms to an existing search terms report, retrying any errors, and viewing the build progress of a specific search terms report.

The following sample use cases illustrate how you can use this service:

- Create a new search terms report.

- Add or update terms in a search terms report.

- Run terms against a new search terms report.

- Refresh a search terms report when document results have changed.

- Run additional terms on an existing search terms report.

- Retry any errors from a previous run of this API.

- Get the progress of any running terms in a search terms report.

- Retrieve the report from executing a search terms report.

You can also use the Search Terms Report Services through .NET. For more information, see Search Terms Report Services (.NET) .

## Guidelines for using the Search Terms Report Services

Review the following guidelines for working with the Search Terms Report Services.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to run a job for a search terms report:

Copy

```text
1
2

<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/run-all-terms
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1 .

- {workspaceID} to the Artifact ID of the workspace containing the search terms report.

- {searchTermsReportID} to the Artifact ID of the search terms report.

## Create a Search Term Report

To create a search term report, use the Object Manager to create a Search Terms Report Object by sending a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.Objects/workspace/<workspaceID>/object/create
```

Fill in the query parameters for:

- workspaceID

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
{

   "request":{

      "FieldValues":[

         {

            "Field":{

               "Name":"Name"

            },

            "Value":"test STR created from REST API"

         },

         {

            "Field":{

               "Name":"Index"

            },

            "Value":{

               "ArtifactID":1041994

            }

         },

         {

            "Field":{

               "Name":"Searchable set"

            },

            "Value":{

               "ArtifactID":1038051

            }

         },

         {

            "Field":{

               "Name":"Include Relational Group"

            },

            "Value":null

         },

         {

            "Field":{

               "Name":"Type"

            },

            "Value":{

               "ArtifactID":1035328

            }

         },

         {

            "Field":{

               "Name":"Calculate Unique Hits"

            },

            "Value":false

         },

         {

            "Field":{

               "Name":"Email Notification Recipients"

            },

            "Value":null

         },

         {

            "Field":{

               "Name":"Notes"

            },

            "Value":null

         },

         {

            "Field":{

               "Name":"Show In Field Tree"

            },

            "Value":true

         },

         {

            "Field":{

               "Name":"Remove Hidden Characters In Terms"

            },

            "Value":true

         }

      ],

      "ObjectType":{

         "Guid":"481E9ACF-368B-4341-B6B5-A21153AD9950"

      }

   }

}
```

This call uses Object Manager to create a Search Terms Report Object. Enter values for these fields as indicated below (you can refer to the Relativity User Documentation on creating a Search Terms Report for a detailed description of each field).

- Name

- Index is the ArtifactID of the dtSearch Index to use for the STR.

- Searchable set is the ArtifactID of a saved search.

- Include Relational Group is the ArtifactID of a relational group to include.

- Type should be set to the ArtifactID that represents “Report only” or “Report and tag”. Lookup these values using Get Report Type IDs

- Calculate Unique Hits - if set to true, includes a Unique hits value for each term in the search terms results.

- Email Notification Recipients specifies recipients to send an email notification to when your search terms report finishes running. Enter the email address(es) of the recipient(s). Separate entries with a semicolon.

- Notes are used to enter notes specific to the search terms report.

- Show in Field Tree - if set to true, automatically adds the terms to the field tree

- Remove Hidden Characters in Terms , if set to true, automatically filters out hidden or non-displayable text control characters when creating or editing terms for the Search Terms Report.

- ObjectType - enter the Guid for the STR Object Type “481E9ACF-368B-4341-B6B5-A21153AD9950”

The response for the create STR operation is the same as for creating an RDO. See the Create an RDO section of the Object Manager for more details on the response.

## Create terms for a search terms report

To create terms used in a search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/create-terms
```

### Request field descriptions

- TermsToAdd - an array of terms to add.

- RelativityHighlightColor - a semicolon delimited string where the first number corresponds to the background color and second number is the text color based on this enumeration.

View enumeration

- Default = 0,

- Black = 1,

- DarkRed = 2,

- DarkGreen = 3,

- DarkYellow = 4,

- DarkBlue = 5,

- DarkMagenta = 6,

- DarkCyan = 7,

- LightGray = 8,

- Gray = 9,

- Red = 10,

- Green = 11,

- Yellow = 12,

- Blue = 13,

- Magenta = 14,

- Cyan = 15,

- White = 16,

- LightGreen = 17,

- LightBlue = 18,

- LightYellow = 19,

- LightPurple = 20,

- LightRed = 21,

- LightOrange = 22,

- Purple = 23,

- Orange = 24,

- DarkPurple = 25,

- DarkOrange = 26

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
{

   "createRequest":{

      "TermsToAdd":[

         "term1",

         "term2"

      ],

      "RelativityHighlightColor":"5;16"

   }

}
```

#### Create response field descriptions

- TermsAffected - the number of terms successfully created or updated.

- TermsSkippedAsDuplicated - the number of terms that were not created or updated because the term would duplicate an existing one.

- TermsSkippedForLength - the number of terms that were not created or updated because the text length of the term exceeded the maximum character count of 450.

- TermsSkippedAsErrors - the number of terms that were not created or updated because errors occurred while executing operations on them.

### Sample JSON response

Copy

```text
1
2
3
4
5
6
{

   "TermsAffected":2,

   "TermsSkippedAsDuplicates":0,

   "TermsSkippedForLength":0,

   "TermsSkippedAsErrors":0

}
```

## Update terms for a search terms report

To modify existing terms used in a search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/update-terms
```

### Request field descriptions

The body of a request must contain an updateRequest object with the following fields:

- UpdatedTerms - an array of SearchTermsResultsTermUpdatedTerm objects containing the following fields:

- ArtifactID - the ArtifactID of the term to update.

- Newterm - the new name of the term.

- RelativityHighlightColor - a semicolon delimited string where the first number corresponds to the background color and second number is the text color based on this enumeration.

View enumeration

- Default = 0,

- Black = 1,

- DarkRed = 2,

- DarkGreen = 3,

- DarkYellow = 4,

- DarkBlue = 5,

- DarkMagenta = 6,

- DarkCyan = 7,

- LightGray = 8,

- Gray = 9,

- Red = 10,

- Green = 11,

- Yellow = 12,

- Blue = 13,

- Magenta = 14,

- Cyan = 15,

- White = 16,

- LightGreen = 17,

- LightBlue = 18,

- LightYellow = 19,

- LightPurple = 20,

- LightRed = 21,

- LightOrange = 22,

- Purple = 23,

- Orange = 24,

- DarkPurple = 25,

- DarkOrange = 26

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
{

   "updateRequest":{

      "UpdatedTerms":[

         {

            "ArtifactID":123123,

            "NewTerm":"termX"

         },

         {

            "ArtifactID":321321,

            "NewTerm":"termY"

         }

      ],

      "RelativityHighlightColor":"5;16"

   }

}
```

The response for an update operation contains the same fields as those for a create response. See the field descriptions and JSON sample for the response in Create response field descriptions .

## Run all terms in a search terms report

To queue a Run All Terms job for a search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/run-all-terms
```

The request body is empty.

The body of the response is empty. The service returns one of the following HTTP status codes:

Status Description

200 Success

404 Invalid Workspace ID

500 Invalid Search Terms Report ID

## Run pending terms in a search terms report

To queue a Run Pending Terms job for a search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/run-pending-terms
```

The request body is empty.

The body of the response is empty. The service returns one of the following HTTP status codes:

Status Description

200 Success

404 Invalid Workspace ID

500 Invalid Search Terms Report ID

## View the build progress of a search terms report

To view the build progress of a search terms report and related statistics, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/get-progress
```

The request body is empty.

### Response field descriptions

- TermsCompleted - the number of terms with a Completed status.

- TermsPending - the number of terms with a Pending status.

- TermsError - the number of terms with an Error status.

- TermsNew - the number of terms added since last run.

- TermsTotal - the total number of terms.

- TotalDocumentsWithHits - the total number of unique documents containing at least one term.

- TotalDocumentsWithHitsIncludingGroup - the total number of unique documents or relational documents containing at least one term.

- DocumentsInSearchableSet - the total number of documents in selected searchable set.

- TimeElapsedInSeconds - the time elapsed in seconds for the current job.

- Status - the status of the search terms report.

- JobType - one of the following type of jobs:

- Run All Terms - the job runs against all available search terms.

- Run Pending Terms - the job runs against terms not yet processed.

- Resolve Alerts - the job runs against all terms with an Error status.

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
{

   "TermsCompleted":17,

   "TermsPending":93,

   "TermsError":0,

   "TermsNew":13,

   "TermsTotal":123,

   "TotalDocumentsWithHits":1337,

   "TotalDocumentsWithHitsIncludingGroup":0,

   "DocumentsInSearchableSet":2000,

   "TimeElapsedInSeconds":234"Status":"Processing""JobType":"Run All Terms"

}
```

## Retry errors in a search terms report

To queue a Retry Errors job for a search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/retry-errors
```

The request body is empty.

The body of the response is empty. The service returns one of the following HTTP status codes:

Status Description

200 Success

404 Invalid Workspace ID

500 Invalid Search Terms Report ID

## Cancel a running search terms report job

To cancel a running search terms report job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/cancel-job
```

The request body is empty.

The body of the response is empty. The service returns one of the following HTTP status codes:

Status Description

200 Success

404 Invalid Workspace ID

500 Invalid Search Terms Report ID

## Retrieve the URL for the Search Terms Result tab

To retrieve the URL used for navigating to the Search Terms Result tab with the appropriate filter criteria for this search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/get-results-url
```

The request body is empty.

The response body contains the URL string.

## Retrieve the URL for a search terms report

To retrieve the URL used to navigate to a search terms report, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/SearchTermsReport/{searchTermsReportID}/get-report-url
```

The request body is empty.

The response body contains the URL string.

## Check whether an index contains a long text field

To check whether a search index contains at least one long text field, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/indexID/{indexID}/index-contains-long-text-field
```

The {indexID} path parameter is the Artifact ID of a search index.

The request body is empty.

The response body contains a Boolean value.

## Retrieve object types for Search Terms Report and Result objects

To retrieve the object types for the Search Terms Report and Result objects, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/get-str-object-types
```

The request body is empty.

### Response field descriptions

The response contains the following fields:

- SearchTermsReportObjectTypeID - the Object Type ID of the Search Terms Report object.

- SearchTermsResultObjectTypeID - the Object Type ID of the Search Terms Report Result object.

### Sample JSON response

Copy

```text
1
2
3
4
{

   "SearchTermsReportObjectTypeID":1000006,

   "SearchTermsResultObjectTypeID":1000007

}
```

## Retrieve the report type choice IDs

To retrieve the report type choice IDs for a workspace, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-search-terms-report/{versionNumber}/workspace/{workspaceID}/get-report-type-ids
```

The request body is empty.

### Response field descriptions

The response contains the following fields:

- Report only - the Artifact ID of the report.

- Report and tag - the Artifact ID of the report and tag.

### Sample JSON response

Copy

```text
1
2
3
4
{

   "Report only":1035327,

   "Report and tag":1035328

}
```

On this page

- Search Terms Report Services (REST)

- Guidelines for using the Search Terms Report Services

- URLs

- Create a Search Term Report

- Sample JSON request

- Create terms for a search terms report

- Request field descriptions

- Sample JSON request

- Sample JSON response

- Update terms for a search terms report

- Request field descriptions

- Sample JSON request

- Run all terms in a search terms report

- Run pending terms in a search terms report

- View the build progress of a search terms report

- Response field descriptions

- Sample JSON response

- Retry errors in a search terms report

- Cancel a running search terms report job

- Retrieve the URL for the Search Terms Result tab

- Retrieve the URL for a search terms report

- Check whether an index contains a long text field

- Retrieve object types for Search Terms Report and Result objects

- Response field descriptions

- Sample JSON response

- Retrieve the report type choice IDs

- Response field descriptions

- Sample JSON response


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
