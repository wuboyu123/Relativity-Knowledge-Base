---
title: "Structured Analytics Job Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Structured_Analytics/Get_started_with_the_Structured_Analytics_API.htm
collection: developer
fetched_at: 2026-06-22T06:22:30+00:00
sha256: 615ba2d2f829a1e6d187065913fdfccde495f0ce0bc7ac9486ab6357f942e233
---

Structured Analytics Job Manager (.NET)

# Structured Analytics Job Manager (.NET)

The Structured Analytics Job Manager API supports the automation of various structured analytics workflows. It provides functionality for running an analysis of a structured analytics set, checking the status of the analysis, retrieving document and set errors, and performing other tasks. It also supports the use of progress indicators and cancellation tokens by provided overloaded methods with these options.

For example, you may want to use the Structured Analytics Job Manager API to implement a custom workflow for running structured analytics sets. With this API, you can automate the process for the analysis and monitoring of these sets. It provides an alternative to manually performing these tasks through the Relativity UI.

You can also use the Structured Analytics Job Manager service through REST. However, this service doesn't support cancellation tokens or progress indicators through REST. For more information, see Structured Analytics Job Manager (REST) .

## Fundamentals for the Structured Analytics Job Manager API

Review the following information to learn more about structured analytics.

### Structured analytics overview

The Analytics application includes functionality that you can use to run structured analytics operations. These operations identify differences and similarities between documents added to a structured analytics set. You create a structured analytics set by selecting a saved search with the documents for analysis, the operations that you want to execute, the Analytics server used for this process, and other options.

View structured analytics operations available in the Relativity UI

You can select the following structured analytics operations through the Relativity UI:

- Email threading - groups related email messages and performs other tasks.

- Textual near duplicate identification - identifies the level of similarity between documents.

- Language identification - identifies primary and secondary languages in the documents.

- Repeated content identification - identifies content reused in documents, such as footers.

- Name normalization - identifies aliases within email headers, such as a proper name, email address, and other items. It then assigns these aliases to entities that are imported into Relativity and linked to document fields. This process simplifies the identification of senders and recipients of email messages, because multiple aliases are frequently used for them.

For more information, see Structured analytics on the Relativity Documentation site.

### API namespaces

The Structured Analytics Job Manager API includes the following namespaces that contain the methods, classes, and enumerations needed to automate the analysis of structured analytics sets.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

Relativity.StructuredAnalytics.<VersionNumber>.Jobs

This namespace contains the IStructuredAnalyticsManager interface provides you with access to Structured Analytics Job Manager service. The following methods also support progress monitoring and cancellation tokens:

- CancelAsync() method - stops an analysis of a structured analytics set. This method returns control to the caller. See Cancel an analysis .

- CancelCopyToLegacyAsync() method - cancels a job for copying the results of an analysis to legacy document fields. This method returns an OperationResult object. See Cancel copy to legacy fields .

- GetDocumentErrorsAsync() method - retrieves information about an error that occurred during the analysis of a specific document, such as the Artifact ID of the document. It returns a DocumentError object. See Retrieve document errors for an analysis .

- GetErrorsAsync() method - retrieves information about an error at the level of the structured analytics set, such as the name of the agent server where the error occurred. It returns a StructuredAnalyticsSetError object. See Retrieve analysis errors for a structured analytics set .

- GetStatusAsync() method - retrieves the status of an analysis on a structured analytics set. This method returns a Status object. See Check the status of an analysis .

- GetValidTasksAsync() method - retrieves valid operations for a structured analytics set, such as retrying errors, running an analysis, and others. This method returns a ValidTaskResult object. See Retrieve valid operations for a structured analytics set .

- RetryErrorsAsync() method - attempts to resolve transient errors that occurred during an analysis by running the operation again. See Retry errors in an analysis .

- RunAsync() method - executes an analysis of a structured analytics set. This method returns an OperationResult object. See Run an analysis of a structured analytics set .

- RunCopyToLegacyAsync() method - copies the results of an analysis to legacy document fields. This method returns an OperationResult object. See Copy to legacy document fields .

- RunAnalysisPreparationAsync() method - generates fields for storing results before you run an analysis on a new structured analytics set. This method returns an OperationResult object. See Generate result fields before running an analysis .

Relativity.StructuredAnalytics.<VersionNumber>.Jobs.Models

- AnalysisSettings class - represents a configuration used for running an analysis. The RunAsync() method takes an instance of this class as an argument.

- DocumentError class - represents an error at the level of a document. Its properties provide the Artifact ID of the document with errors, a detailed error message, and status information based on the DocumentErrorStatus enumeration. The GetDocumentErrorsAsync() method returns this object type.

- DocumentErrorStatus enumeration - indicates whether a document with errors remains in structured analytics set during an analysis, and whether it is included in the result set. For example, these constants include RemovedFromSet, IncludedInSet, and DataWarning. The DocumentError class has a Status property that references a DocumentErrorStatus constant.

- OperationResult class - indicates whether the analysis was successful and provides a detailed message about the operation. The CancelAsync(), CancelCopyToLegacyAsync(), RetryErrorsAsync(), RunAnalysisPreparationAsync(), RunAsync(), and RunCopyToLegacyAsync() methods return an OperationResult object.

- ValidTaskResult class - represents the operations that are valid to perform on a structured analytics set, such as retrying errors, running an analysis, and others. The GetValidTasksAsync() method returns an object of this type.

- StructuredAnalyticsTask enumeration - contains members used to indicate that an operation is valid for a structured analytics set, such as CANCEL_ANALYSIS, RETRY_ERRORS, RUN_ANALYSIS and others. The ValidTaskResult class has a ValidTasks property, which is a list of StructuredAnalyticsTask enums.

- StructuredAnalyticsSetError class - represents an error at the level of the structured analytics set. Its properties provide a detailed error message, the name of the agent server where the error occurred, and the source of the error. The GetErrorsAsync() returns a StructuredAnalyticsSetError object.

Relativity.StructuredAnalytics.<VersionNumber>.Jobs.Models.Status

- EmailThreadingStatistics class - provides the number of email messages analyzed, and the number of inclusive messages. The JobResults class has the EmailThreadingStatistics property that references this object type.

- JobResults class - provides information about the number of documents analyzed, and statistics for email threading and textual near duplicates. The JobResults class has properties that reference EmailThreadingStatistics, NameNormalizationStatistics, and TextualNearDuplicatesStatistics and objects.

- JobState class - indicates whether the analysis job is completed, canceled, or running, the phase of the job, the time elapsed, and other information. The Status class has a property that references a JobState object.

- NameNormalizationStatistics class - provides information about the number of aliases in a group of email messages. It contains the AliasesIdentified property that represents a count of all aliases in the group, and the NewAliasesImported property that represents the number of new aliases added to Relativity. An alias may be a proper name, email address, or other item.

- Status class - provides information about the state of the job, the operations assigned to it, the operations currently executing on it, and other information. The GetStatusAsync() method returns a Status object.

- TextualNearDuplicatesStatistics class - provides the average similarity of textual near duplicates as a percentage, and the total number of textual near duplicate groups. The JobResults class has the TextualNearDuplicatesStatistics property that is set to this class.

- OperationState class - provides information about an operation, including the time associated with the last activity, the operation such as email threading, and the phase such as exporting or setup.

- JobOperation enumeration - lists specific analysis types that can be performed on a structured analytics set. For example, these types include EmailThreading, TextualNearDuplicateId, and others. The Status class has a SelectedOperations property that is set to a JobOperation constant.

- JobPhase enumeration - lists specific phases in an analysis. For example, phases include Setup, RunningOperations, and others. The JobState class has a Phase property that is set to a JobPhase constant.

## Guidelines for the Structured Analytics Job Manager API

Review the following guidelines for working with this API.

### Custom code implementation

When implementing your custom code, follow these guidelines:

- Execute only valid operations for the state of a structured analytics set - Only certain operations are valid for the current state of your structured analytics set. See the following examples:

- A call to the CancelAsync() method is only valid when an analysis is currently running.

- A call to the RetryErrorsAsync() method is only valid when a structured analytics set is in an errored state.

To get a list of valid operations, make a call with the GetValidTasksAsync() method. The ValidTaskResult object returned from this call contains a valid list of operations. If you attempt to execute an invalid operation, you receive 400 status response.

- Monitor the analysis progress - After making a successful call to the RunAsync() method, make calls to GetStatusAsync() method to monitor the progress of your analysis.

- Use structured analytics set RDOs - The Structured Analytics Job Manager API doesn't expose standard CRUD operations for structured analytics set RDOs. Use the Object Manager service to create RDOs. For more information, see Object Manager (.NET) or Object Manager (REST) .

### Code samples

Use the code samples in the following sections to learn about calling the methods available in the Structured Analytics Job Manager API. These code samples illustrate the following best practices for working with the API:

- Use helper classes to create the proxy and select an appropriate authentication type. See Relativity API Helpers .

- Create the Services API proxy within a using block in your code.

- Call specific methods on the Structured Analytics Job Manager API within a try-catch block.

- Use await/async design pattern.

- Use the logging framework for troubleshooting and debugging purposes. See Log from a Relativity application .

### Relativity environment setup

Use these steps to set up your Relativity environment:

- Obtain access to an instance of Relativity 12.3 used for development purposes.

- Install the Relativity Analytics application on this Relativity instance. Make sure that your Analytics server is configured properly. For more information, see Upgrading or installing your Analytics server on the Relativity Documentation site.

- Add the Relativity Analytics application to your workspace. For more information, see Installing applications on the Relativity Documentation site.

- Enable Developer mode in your development instance of Relativity to simplify troubleshooting.

- Create the structured analytics sets that you want include in the automated analysis. See the following resources:

- To create setsprogrammatically, see Object Manager (.NET) or Object Manager (REST) .

- To create sets through the Relativity UI, see Structured analytics on the Relativity Documentation site.

## Generate result fields before running an analysis

You can optionally call the RunAnalysisPreparationAsync() method when you want to generate fields for storing results before you run an analysis on a new structured analytics set. For example, you might use the following workflow in this case:

- Create a new structured analytics set.

- Call the RunAnalysisPreparationAsync() method to generate fields used to store results from an analysis.

- Use the fields generated by the RunAnalysisPreparationAsync() method to create views and saved searches. You can also use this process to add a structured analytics set to a template workspace.

- Poll the GetValidTasksAsync() method until StructuredAnalyticsTask.RUN_ANALYSIS is reported as a valid task to run.

- Call the RunAsync() method to complete the analysis of the structured analytics set, and store results in the fields that you generated.

To generate these results fields, call the RunAnalysisPreparationAsync() method by passing the Artifact ID for the structured analytics set, and the workspace that contains it. You can also optionally pass ProgressReport or CancellationToken objects to this method.

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
public void RunSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        OperationResult results = sasManager.RunAnalysisPreparationAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        if (results.IsSuccess)

        {

            System.Diagnostics.Debug.WriteLine($"Call to run Analysis Preparation on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

        }

        else

        {

            throw new Exception($"Call to run Analysis Preparation on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Message}");

        }

    }

}
```

## Retrieve valid operations for a structured analytics set

You can use the GetValidTasksAsync() method to retrieve all valid operations that you can run for a specific structured analytics set, such as retrying errors, running an analysis, and others.

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
public void RunSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        ValidTaskResult results = sasManager.GetValidTasksAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        if (results != null)

        {

            System.Diagnostics.Debug.WriteLine($"Call to get valid tasks on SAS {sasArtifactId} on workspace {workspaceId} succeeded. Copy to legacy is legal: {results.CopyToLegacyQualified}, Valid tasks: {string.Join(",", results.ValidTasks.Select(t => t.ToString()))}");

        }

        else

        {

            throw new Exception($"Call to get valid tasks on SAS {sasArtifactId} on workspace {workspaceId} failed.");

        }

    }

}
```

## Run an analysis of a structured analytics set

To analyze documents in a structured analytics set, call the RunAsync() method by passing the Artifact ID for the structured analytics set, the Artifact ID for the workspace that contains it, and an AnalysisSettings object. This object has properties that you can use to specify whether all documents are updated with the analysis results and repopulated or just new ones undergo these processes. You can also optionally pass ProgressReport or CancellationToken objects to this method.

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
public void RunSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        AnalysisSettings runAnalysisSettings = new AnalysisSettings();

        //This AnalysisSettings configuration will run the equivalent of a Pre-Smart Ingestion Full Analysis

        runAnalysisSettings.AnalyzeAll = true;

        runAnalysisSettings.PopulateAll = true;

        //This AnalysisSettings configuration will run the equivalent of a Pre-Smart Ingestion Incremental Analysis

        //runAnalysisSettings.AnalyzeAll = false;

        //runAnalysisSettings.PopulateAll = false;

        //This AnalysisSettings configuration will add new documents to staging area, remove documents from staging area

        //that no longer exist in the target saved search, and run a full analysis.

        //runAnalysisSettings.AnalyzeAll = true;

        //runAnalysisSettings.PopulateAll = false;

       //This AnalysisSettings configuration is illegal and will throw a validation error

       //runAnalysisSettings.AnalyzeAll = false;

        //runAnalysisSettings.PopulateAll = true;

        OperationResult results = sasManager.RunAsync(workspaceId, sasArtifactId, runAnalysisSettings).GetAwaiter().GetResult();

        if (results.IsSuccess)

        {

            System.Diagnostics.Debug.WriteLine($"Call to run analysis on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

        }

        else

        {

            throw new Exception($"Call to run analysis on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Message}");

        }

    }

}
```

## Cancel an analysis

The CancelAsync() method makes a request to cancel the analysis of the structured analytics set that is currently running. It then returns control immediately to the caller. This request only initiates an asynchronous cancel request. The job for the structured analytics set job run isn't guaranteed to be canceled on the response of this request. Poll the GetStatusAsync() method after completing this request to monitor the progress of your cancel request.

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
public void CancelSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        OperationResult results = sasManager.CancelAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        if (results.IsSuccess)

        {

            System.Diagnostics.Debug.WriteLine($"Call to run Cancel Analysis on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

        }

        else

        {

            throw new Exception($"Call to run Cancel Analysis on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Message}");

        }

    }

}
```

## Check the status of an analysis

Use the GetStatusAsync() method to return a Status object. This object contains information about the state of job and current operations. For more information, see Fundamentals for the Structured Analytics Job Manager API

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
public void GetStatusSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        SASModels.Status.Status results = sasManager.GetStatusAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        System.Diagnostics.Debug.WriteLine($"SAS Name: {results.JobName}");

        System.Diagnostics.Debug.WriteLine($"SAS Status: {results.JobState.Status}");

        if (results.JobState.IsCompleted)

        {

            System.Diagnostics.Debug.WriteLine($"SAS Docs Analyzed: {results.JobResults.DocumentsAnalyzed}");

        }

    }

}
```

## Retry errors in an analysis

Use the RetryErrorsAsync() method to resolve transient errors that occurred during an analysis.

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
public void RetryErrorsSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        OperationResult results = sasManager.RetryErrorsAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        if (results.IsSuccess)

        {

            System.Diagnostics.Debug.WriteLine($"Call to run Retry Errors on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

        }

        else

        {

            throw new Exception($"Call to run Retry Errors on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Message}");

        }

    }

}
```

## Retrieve analysis errors for a structured analytics set

The GetErrorsAsync() method retrieves set errors. These are errors aren't document specific and they cause an analysis to stop. For example, a set error may be a validation error for a structured analytics set, or it may occur when the Analytics server is disabled or goes down. This method returns a StructuredAnalyticsSetError object. For more information, see Fundamentals for the Structured Analytics Job Manager API .

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
public void GetErrorsSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    int indexOfFirstError = 0;

    int maxNumberOfErrorsToReturn = 1000;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        List<StructuredAnalyticsSetError> results = sasManager.GetErrorsAsync(workspaceId, sasArtifactId, indexOfFirstError, maxNumberOfErrorsToReturn).GetAwaiter().GetResult();

        System.Diagnostics.Debug.WriteLine($"Call to GetErrors (Get Set Errors) on {sasArtifactId} on workspace {workspaceId} returned {results.Count} record(s).");

        if (results.Any())

        {

            System.Diagnostics.Debug.WriteLine("Errors:");

            foreach (var error in results)

            {

                System.Diagnostics.Debug.WriteLine(error.Message);

                System.Diagnostics.Debug.WriteLine("-----");

            }

        }

    }

}
```

## Retrieve document errors for an analysis

The GetDocumentErrorsAsync() method retrieves errors that are associated with the processing of a specific document. For example, this type of error occurs when a document is too large to be extracted or ingested in the Analytics engine, or when Analytics engine fails to process a document due to corruption. This method returns a list of DocumentError objects.

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
public void GetDocumentErrorsSample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    int indexOfFirstError = 0;

    int maxNumberOfErrorsToReturn = 1000;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        List<DocumentError> results = sasManager.GetDocumentErrorsAsync(workspaceId, sasArtifactId, indexOfFirstError, maxNumberOfErrorsToReturn).GetAwaiter().GetResult();

        System.Diagnostics.Debug.WriteLine($"Call to GetDocumentErrors on {sasArtifactId} on workspace {workspaceId} returned {results.Count} record(s).");

        if (results.Any())

        {

            System.Diagnostics.Debug.WriteLine("Errors:");

            foreach (var error in results)

            {

                System.Diagnostics.Debug.WriteLine(error.Message);

                System.Diagnostics.Debug.WriteLine("-----");

            }

        }

    }

}
```

## Work with legacy document fields

As of Relativity 9.5.196.102, structured analytics stopped writing results for email threading and textual near duplicate identification to Document fields. Instead, it writes results to fields on the Structured Analytics Results object. However, you can copy these results to the legacy document result fields by calling the RunCopyToLegacyAsync() method. It copies the results from the newly created fields to the legacy document fields from pre 9.5.196 versions of Relativity. For more information, see Copy to Legacy Document Fields on the Relativity Documentation site.

### Copy to legacy document fields

To copy analysis results to legacy document fields, call the RunCopyToLegacyAsync() method by passing the Artifact ID for the structured analytics set and the workspace that contains it. You can also optionally pass ProgressReport or CancellationToken objects to this method.

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
public void CopyToLegacySample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        OperationResult results = sasManager.RunCopyToLegacyAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        if (results.IsSuccess)

        {

            System.Diagnostics.Debug.WriteLine($"Call to run CopyToLegacy on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

        }

        else

        {

            throw new Exception($"Call to run CopyToLegacy on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Message}");

        }

    }

}
```

### Cancel copy to legacy fields

To cancel a copy operation, call the CancelCopyToLegacyAsync() method by passing the Artifact ID for the structured analytics set and the workspace that contains it. You can also optionally pass ProgressReport or CancellationToken objects to this method.

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
public void CancelCopyToLegacySample()

{

    int workspaceId = Constants.WORKSPACE_ID;

    int sasArtifactId = Constants.SAS_ARTIFACT_ID;

    using (IJobManager sasManager = ServiceProxyHelper.CreateProxy<IJobManager>())

    {

        OperationResult results = sasManager.CancelCopyToLegacyAsync(workspaceId, sasArtifactId).GetAwaiter().GetResult();

        if (results.IsSuccess)

        {

            System.Diagnostics.Debug.WriteLine($"Call to cancel CopyToLegacy on SAS {sasArtifactId} on workspace {workspaceId} succeeded");

        }

        else

        {

            throw new Exception($"Call to cancel CopyToLegacy on SAS {sasArtifactId} on workspace {workspaceId} failed. Error message: {results.Message}");

        }

    }

}
```
