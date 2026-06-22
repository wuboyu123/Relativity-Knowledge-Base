---
title: "Structured Analytics Job Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Structured_Analytics/Structured_Analytics_Manager_service_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:22:32+00:00
sha256: bc99f5e7ccb0f886f8097241723e1d095c126134e8b4f5f5b281588f6d115b2d
---

Structured Analytics Job Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Structured Analytics Job Manager (REST)

The Structured Analytics Job Manager service is an HTTP service, which you can use to automate operations on structured analytics sets through Representational State Transfer (REST). You can use the endpoints on this service to run an analysis of a structured analytics set, check the status of the analysis, retrieve document and other errors, and perform additional tasks. For general information about REST, see the REST API .

You can implement custom workflows for programmatically running structured analytic sets using the REST endpoints. For example, you can automate an analysis of a structured analytics set after performing only minor setup tasks in the Relativity UI. You could also implement a custom page that uses these endpoints to display the status of an analysis or errors that may have occurred.

You can also use the Structured Analytics Job Manager service API through .NET. The API supports the use of progress indicators and cancellation tokens in .NET. For more information, see Structured Analytics Job Manager (.NET) .

You must install the Analytics application in your Relativity environment to automate workflows with the Structured Analytics Job Manager service. For more information, see Upgrading or installing your Analytics server on the Relativity Documentation site.

## Guidelines for the Structured Analytics Job Manager service

Review the following guidelines for working with this service.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set {versionNumber} to the version of the API, using the format lowercase v and the version number , such as v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, such as {workspaceID} to the Artifact ID of a workspace.

For example, you can use the following URL to retrieve valid operations for a structured analytics set:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/valid-tasks?
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {workspaceId} - the Artifact ID of the workspace that contains the structured analytics set.

- {sasArtifactId} - the Artifact ID of the structured analytics set.

### Custom code

When implementing your custom code, follow these guidelines:

- Execute only valid operations for the state of a structured analytics set - Only certain operations are valid for the current state of your structured analytics set. See the following examples:

- A call to the CancelAsync endpoint is only valid when an analysis is currently running.

- A call to the RetryErrorsAsync endpoint is only valid when a structured analytics set is in an errored state.

To get a list of valid operations, make a call with the GetValidTasksAsync() endpoint. The ValidTaskResult object returned from this call contains a valid list of operations. If you attempt to execute an invalid operation, you receive 400 status response.

- Monitor the analysis progress - After making a successful call to the RunAsync endpoint, make calls to the GetStatusAsync endpoint to monitor the progress of your analysis.

- Use structured analytics set RDOs - The Structured Analytics Job Manager service doesn't expose standard CRUD operations for structured analytics set RDOs. Use the Object Manager service to create RDOs. For more information, see Object Manager (.NET) or Object Manager (REST) .

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Error Manager service. To download the sample file, click Structured Analytics Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Structured Analytics Job Manager service, send an HTTP request that makes a POST method call. See the following base URL for this service:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/v1/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs
```

You can use the following .NET code as a sample REST client for performing any of the operations available in the Structured Analytics Job Manager service. This code sample illustrates how to perform the following tasks:

- Instantiate an HttpWebRequest object for sending requests and responses using the URL for the Structured Analytics Job Manager service.

- Set the required headers for the request.

- Initialize the parameters for the workspace and structured analytics set.

- Set the url variable to the URL for the RunAsync operation.

- Use the GetResponse() method to send a POST request.

- Return the results of the request and parse it.

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
public bool ExecuteRunAsync(int workspaceId, int sasArtifactId, bool analyzeAllDocs, bool repopulateAllDocuments)

{

    string url = "http://localhost/relativity.rest/api/relativity-structured-analytics/ + "v1/workspaces/" + workspaceId + "/sets/" + sasArtifactId + "/jobs";

    var HttpWebRequest request = HttpWebRequest.CreateHttp(url)

    request.Method = "POST";

    request.ContentType = "application/json";

    request.KeepAlive = false;

    request.Headers.Add("Authorization", GetBase64AuthHeader());

    request.Headers.Add("X-CSRF-Header", "-");

    request.Headers.Add("X-Kepler-Version", "2.0");



    //Initialize the parameters for the structured analytics set.

    string requestPayload= Newtonsoft.Json.JsonConvert.SerializeObject(new

    {

        settings = new

        {

            AnalyzeAll = analyzeAllDocs,

            PopulateAll = repopulateAllDocuments

        }

    });

    using (var requestContent = new System.IO.StreamWriter(request.GetRequestStream()))

    {

        //write request payload to stream

        requestContent.Write(requestPayload);

        requestContent.Flush();

    }

    var response = request.GetResponse();

    string responsePayload = null;

    using (var streamReader = new System.IO.StreamReader(response.GetResponseStream()))

    {

        responsePayload = streamReader.ReadToEnd();

    }

    JObject results = JObject.Parse(responsePayload);

    if (results.Value<bool>("IsSuccess") == true)

    {

        System.Diagnostics.Debug.WriteLine($"Call to Run on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

    }

    else

    {

        throw new Exception($"Call to Run on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Value<string>("Message")}");

    }

}
```

## Generate result fields before running an analysis

You can optionally call the RunAnalysisPreparationAsync endpoint when you want to generate fields for storing results before you run an analysis on a new structured analytics set. For example, you might use the following workflow in this case:

- Create a new structured analytics set.

- Call the RunAnalysisPreparationAsync endpoint to generate fields used to store results from an analysis.

- Use the fields generated by the RunAnalysisPreparationAsync endpoint to create views and saved searches. You can also use this process to add a structured analytics set to a template workspace.

- Call the RunAsync endpoint to complete the analysis of the structured analytics set, and store results in the fields that you generated.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/prep
```

The response contains the following fields:

- IsSuccess - a Boolean value indicating whether the request succeeded or failed.

- Message - a string that returns an informative message about the status of the request.

Copy

```text
1
2
3
4
{

   "IsSuccess":true,

   "Message":"Analysis Preparation has been successfully started for Structured Analytics Set 7654321 in Workspace 1234567"

}
```

## Retrieve valid operations for a structured analytics set

Use the valid-tasks endpoint to retrieve an array of valid operations for a structured analytics set, such as retrying errors, running an analysis, and others.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/valid-tasks?
```

The response contains the following fields:

- ValidTasks - an array of valid jobs that can be run on the specified analytics set.

- CopyToLegacyQualified - a Boolean value indicating whether the results of an analysis are copied to existing document fields. For more information, see Work with legacy document fields .

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
{

   "ValidTasks":[

      "RUN_ANALYSIS",

      "COPY_TO_LEGACY",

      "PREPARE_ANALYSIS"

   ],

   "CopyToLegacyQualified":true

}
```

## Run an analysis of a structured analytics set

Use the jobs endpoint to run analysis on documents in a structured analytics set.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs
```

The request body must contain the following fields:

- settings - represents a configuration used for an analysis run. This field represents an AnalysisSettings object, which contains the following fields:

- AnalyzeAll - a Boolean value indicating whether all documents are updated with the analysis results. When this field is set to false, only new documents are updated with the results.

- PopulateAll - a Boolean value indicating whether all documents are repopulated. When the PopulateAll field is set to false, only new documents are added to the existing population. Otherwise, all documents are repopulated.

Copy

```text
1
2
3
4
5
6
{

   "settings":{

      "AnalyzeAll":true,

      "PopulateAll":true

   }

}
```

The response contains the following fields:

- IsSuccess - a Boolean value indicating whether the request succeeded or failed.

- Message - a string that returns an informative message about the status of the request.

Copy

```text
1
2
3
4
{

   "IsSuccess":true,

   "Message":"Analysis has been successfully started for structured analytics set 7654321 in Workspace 1234567"

}
```

## Cancel an analysis

You can make a request to cancel the analysis of a structured analytics set that is currently running. After this request, control immediately returns to the caller.

To cancel an analysis of a structured analytics set, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs
```

The response contains the following fields.

- IsSuccess - a Boolean value indicating whether the request succeeded or failed.

- Message - a string that returns an informative message about the status of the request.

Copy

```text
1
2
3
4
{

   "IsSuccess":true,

   "Message":"The cancel analysis request has successfully started for structured analytics set 134890 in workspace 123456."

}
```

## Check the status of an analysis

To retrieve the status of an analysis for a structured analytics set, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs
```

View field descriptions for a response

The response contains the following JSON objects with their related fields:

- JobName - contains a field that specifies the name of the structured analytics set.

- JobState - contains fields related to the status of an analysis, including information about the percent completed, the duration of the job, and others. The following list provides additional information about selected fields on the JobState object:

- Phase - the phases for analysis include setup, importing, running operations, and others.

- JobTimeElapsed - the number of seconds since the analysis has started.

- OperationTimeElapsed - the number of seconds since the current operation has started.

- SelectedOperations - lists the structured analytics operations performed on the documents added to the set. These operations include email threading, textual near duplicate identification, language identification, and repeated content identification. For more information, see Run Structured Analytics in Running structured analytics on the Relativity Documentation site.

- ValidOperations - a list of valid operations for a structured analytics set, such as running a full analysis, canceling an analysis, getting document errors, and others.

- JobResults - lists the number of documents analyzed in a job. It also includes a breakdown of email threading statistics as follows:

- EmailsAnalyzed - lists the total number of emails analyzed by the email threading operation.

- InclusiveEmails - lists the total count and percentage of all emails in the set that require review.

- TextualNearDuplicatesStatistics - includes the information in the following fields:

- TextualNearDuplicateGroupsCount - the total number of textual near duplicate groups.

- AverageSimilarityPercentage - a percent that indicates how similar a document must be to a principal document to be grouped with it. For more information, see Textual near duplicate identification on the Relativity Documentation site.

- NameNormalizationStatistics - includes the information in the following fields:

- AliasesIdentified - a total count of all aliases in a group of email messages.

- NewAliasesImported - the number of new aliases added to Relativity.

View a sample JSON response

The NameNormalizationStatistics field isn't listed in the following sample.

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
{

   "JobName":"Sample Analytics",

   "JobState":{

      "IsRunning":false,

      "IsCompleted":true,

      "Status":"Completed analysis with errors",

      "Phase":"Completed",

      "PhaseProgressPercentage":0,

      "JobTimeElapsed":0,

      "OperationTimeElapsed":0

   },

   "SelectedOperations":[

      "EmailThreading",

      "TextualNearDuplicateId",

      "LanguageId",

      "RepeatedContentId"

   ],

   "ValidOperations":[

      "RUN_FULL_ANALYSIS",

      "RUN_INCREMENTAL_ANALYSIS",

      "GET_DOCUMENT_ERRORS"

   ],

   "JobResults":{

      "DocumentsAnalyzed":4798,

      "EmailThreadingStatistics":{

         "EmailsAnalyzed":4698,

         "InclusiveEmails":4645

      },

      "TextualNearDuplicatesStatistics":{

         "AverageSimilarityPercentage":98,

         "TextualNearDuplicateGroupsCount":12

      }

   }

}
```

## Retry errors in an analysis

You can attempt to resolve errors that occurred during an analysis of a structured analytics set by rerunning the failed items with the retry endpoint.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/retry
```

The response contains the following fields:

- IsSuccess - a Boolean value indicating whether the request succeeded or failed.

- Message - a string that returns an informative message about the status of the request.

Copy

```text
1
2
3
4
{

   "IsSuccess":true,

   "Message":"The retry errors request has successfully started for structured analytics set 134890 in workspace 123456."

}
```

## Retrieve analysis errors for a structured analytics set

You can retrieve errors for a structured analytics set. These are errors aren't document specific and they cause an analysis to stop. For example, a set error may be a validation error for a structured analytics set, or it may occur when the Analytics server is disabled or goes down.

To retrieve set errors, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/errors?{start}&{length}
```

The request URL can optionally include the following query parameters:

- start - indicates the index of the first error that you want to return.

- length - the number of subsequent errors to return.

View field descriptions for a response

The response contains the following fields for each error:

- Fulltext - a verbose description of the error that occurred.

- Message - a short summary of the error that occurred.

- Server - the location of the Relativity server that hosts the agent where the error occurred.

- Source - detailed information about where the error originated, such as the agent or web server.

View a sample JSON response

This JSON sample illustrates an array of errors retrieved by the endpoint.

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
[

   {

      "Fulltext":"This is the full text of the error message",

      "Message":"This is a shortened version of the error message...",

      "Server":"SERVER_LOCATION",

      "Source":"ERROR_SOURCE"

   },

   {

      "Fulltext":"This is the full text of the error message",

      "Message":"This is a shortened version of the error message...",

      "Server":"SERVER_LOCATION",

      "Source":"ERROR_SOURCE"

   }

]
```

## Retrieve document errors for an analysis

You can retrieve errors that are associated with the processing of a specific document. For example, this type of error occurs when a document is too large to be extracted or ingested in the Analytics engine, or when Analytics engine fails to process a document due to corruption.

To retrieve document errors for a structured analytics set, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/doc-errors?{start}&{length}
```

The request URL can optionally include the following query parameters:

- start - indicates the index of the first error that you want to return.

- length - the number of subsequent errors to return.

View field descriptions for a response

The response contains the following fields for each document error:

- DocumentArtifactId - the Artifact ID of the document associated with an error.

- DocumentIdentifier - the control number of the document associated with an error. Relativity uses the control number as a unique identifier for a document. For information, see Analytics profile on the Relativity Documentation site.

- Message - a string that returns an informative message about the status of the request.

- Status - the status of the document. The following statuses may appear in this field:

- IncludedInSet - the document remains in the analysis of the structured analytics set.

- RemovedFromSet - the document is automatically removed from the analysis of the structured analytics set.

- DataWarning - a problem with the document was identified during analysis and the document was removed from the results.

- DateErrored - the date and time when the document error was logged.

View a sample JSON response

This JSON sample illustrates an array of the document errors retrieved by the endpoint.

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
[

   {

      "DocumentArtifactId":1383924,

      "DocumentIdentifier":"Document_1",

      "Message":"An error occurred during processing of email",

      "Status":"DataWarning",

      "DateErrored":"2017-01-06T11:33:00.357"

   },

   {

      "DocumentArtifactId":1383925,

      "DocumentIdentifier":"Document_2",

      "Message":"Processing failed for the given document",

      "Status":"RemovedFromSet",

      "DateErrored":"2017-01-06T11:33:00.357"

   },

   {

      "DocumentArtifactId":1383926,

      "DocumentIdentifier":"EmailThreadingTaskProblemDoc5",

      "Message":"A network error occurred.",

      "Status":"IncludedInSet",

      "DateErrored":"2017-01-06T11:33:00.357"

   }

]
```

## Work with legacy document fields

As of Relativity 9.5.196, structured analytics stopped writing results for email threading and textual near duplicate identification to Document fields. Instead, it writes results to fields on the Structured Analytics Results object. However, you can copy these results to the legacy document result fields by calling the RunCopyToLegacyAsync endpoint. It copies the results from the newly created fields to the legacy document fields from pre 9.5.196 versions of Relativity. For more information, see Copy to Legacy Document Fields on the Relativity Documentation site.

### Copy results to legacy document fields

Use the RunCopyToLegacyAsync endpoint to copy the results of an analysis to existing document fields.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/copy-to-legacy
```

The response contains the following fields:

- IsSuccess - a Boolean value indicating whether the request succeeded or failed.

- Message - a string that returns an informative message about the status of the request.

Copy

```text
1
2
3
4
{

   "IsSuccess":true,

   "Message":"Copy To Legacy Fields has been successfully started for structured analytics set 7654321 in Workspace 1234567"

}
```

### Cancel a job for copying content to legacy fields

To cancel a job for copying the results of an analysis to existing document fields, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-structured-analytics/{versionNumber}/workspaces/{workspaceId}/sets/{sasArtifactId}/jobs/copy-to-legacy
```

The response contains the following fields:

- IsSuccess - a Boolean value indicating whether the request succeeded or failed.

- Message - a string that returns an informative message about the status of the request.

Copy

```text
1
2
3
4
{

   "IsSuccess":true,

   "Message":"Cancel Copy to Legacy Fields has been successfully started for structured analytics set 7654321 in Workspace 1234567"

}
```

On this page

- Structured Analytics Job Manager (REST)

- Guidelines for the Structured Analytics Job Manager service

- URLs

- Custom code

- Postman sample file

- Client code sample

- Generate result fields before running an analysis

- Retrieve valid operations for a structured analytics set

- Run an analysis of a structured analytics set

- Cancel an analysis

- Check the status of an analysis

- Retry errors in an analysis

- Retrieve analysis errors for a structured analytics set

- Retrieve document errors for an analysis

- Work with legacy document fields

- Copy results to legacy document fields

- Cancel a job for copying content to legacy fields


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
