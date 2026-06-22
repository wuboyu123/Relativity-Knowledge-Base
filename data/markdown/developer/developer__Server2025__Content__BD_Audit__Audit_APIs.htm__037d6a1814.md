---
title: "Audit (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Audit/Audit_APIs.htm
collection: developer
fetched_at: 2026-06-22T06:22:39+00:00
sha256: 69482667362267bfedf18d26f485ca514d785413344042a589779db48183333e
---

Audit (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Audit (.NET)

The Audit APIs available through .NET include methods that you can use to programmatically revert, retrieve, and search Relativity audit records stored in Elasticsearch. These services support interactions with both instance-level and workspace-level audit records. The following APIs provide methods for this functionality:

- Audit Metrics API - includes a method for retrieving information about the number and size of the audits in a specific workspace.

- Audit Revert API - includes methods for reverting document update actions. It provides methods for reverting a single action or list of actions, and for verifying whether the revert operation can be performed on an action.

- Audit (.NET) - includes methods for running pivot queries on audit data. It supports querying with group by and pivot on operations for object type, action, username, and timestamp fields.

- Reviewer Statistics API - includes methods for retrieving information about reviewer actions, such as the number of actions performed by a reviewer on a document, the usage time per review, a summary report of reviewer actions, and others.

- Audit Query API - includes a method for querying on a specific audit record.

- Audit Object Manager UI API - includes methods for querying on audit details to display in the Relativity UI, including filtering on the returned data.

These APIs don't support working with audit records stored in an SQL Server database.

Sample use cases for the Audit APIs include building custom applications to perform the following tasks:

- Transfer data to other applications and tools for analysis and reporting, such as a third-party software applications or web-based visualization tools.

- Implement an audit record query as part of a larger solution that captures query results and then manipulates the results using a visualization solution.

- Programmatically generate a reviewer statistics report.

- Retrieve or aggregate audit data or execute pivot queries on the data.

Additionally, you can access the Audit API services through REST. These services support the same functionality as the .NET interfaces. For more information, see Audit (REST) .

## Fundamentals for Audit APIs

Click the following drop-down links to learn about the methods and classes used by the Audit APIs.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

### Audit Metrics API

The Audit Metrics API contains the following method and classes.

#### Methods

The Audit Metrics API exposes the following method on the IAuditMetricsService interface in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Metrics namespace:

- GetWorkspaceAuditMetricsAsync() method - retrieves a total count of all audits in a workspace, and the total size of the audits in bytes. It takes the Artifact ID of a workspace as its only parameter. This method returns an AuditMetricsAggregateResponse object. See Retrieve the total number and size of audits .

#### Classes

The Audit Metrics API includes the following class available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Metrics.Models namespace:

- AuditMetricsAggregateResponse class - represents the data for the total count and size of the audits in a workspace. The GetWorkspaceAuditMetricsAsync() method returns this object type.

### Audit Revert API

The Audit Revert API contains the following methods and classes.

#### Methods

The Audit Revert API exposes the following methods on the IAuditRevertService API interface in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Revert namespace:

- MassRevertAuditAsync() method - reverts document updates. Its parameters include the Artifact ID of a workspace and a MassRevertAuditRequest object. This method returns a MassRevertAuditResponse object. See Mass revert a list of audits .

- RevertAuditAsync() method - reverses an audit action. Its parameters include the Artifact ID of a workspace, and a RevertAuditRequest object. This method returns a RevertAuditResponse object. See Revert an audit .

- ValidateRevertAuditAsync() method - indicates whether an audit action can be reversed. Its parameters include the Artifact ID of a workspace and a RevertAuditRequest object. This method returns a ValidateRevertAuditResponse object. See Validate a revert operation for an audit .

#### Classes

The Audit Revert API includes the following classes available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Revert.Models namespace:

- MassRevertAuditResponse class - represents the results of a mass revert operation. Its properties include a list of ValidateRevertAuditResponse objects for each action, a Boolean value indicating whether the operation succeeded, and others. The MassRevertAuditAsync() method returns an object of this type.

- MassRevertAuditRequest class - represents a request to revert multiple document updates. Its properties include a list of RevertAuditRequest objects, and others. The MassRevertAuditAsync() method takes an object of this type.

- RevertAuditRequest class - represents a request to revert a single audit action. Its properties include the identifier and timestamp of an audit action. The RevertAuditAsync() method takes an object of this type.

- RevertAuditResponse class - represents the results of a single revert operation. Its properties include a Boolean value indicating whether the operation succeeded, a message if the operation fails, and others. The RevertAuditAsync() method returns an object of this type.

- ValidateRevertAuditResponse class - represents the results of a validation operation. Its properties include the identifier and timestamp of an audit action, a Boolean value indicating whether the operation can be reverted, and others. The ValidateRevertAuditAsync() method takes an object of this type.

### Audit Pivot API

The Audit Pivot API contains the following method and classes.

#### Methods

The Audit Pivot API exposes the following method on the IAuditPivotService interface in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Pivot namespace:

- PivotAsync() method - runs a pivot query on audit data. Its parameters include the Artifact ID of a workspace, and PivotSettings, CancellationToken, and IProgress<ProgressReport> objects. This method returns a PivotResultSet object. See Query with Pivot on audit data .

The method signature for the PivotAsync() method includes the CancellationToken and IProgress<ProgressReport> objects. However, they aren't supported but must be passed to the method as required.

#### Classes

The Audit Pivot API includes the following classes available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Pivot.Models namespace:

- PivotResultSet class - represents the results of a pivot query on audit data. The PivotAsync() method returns an object of this type.

- PivotSettings class - represents the pivot fields to use for the query and the query conditions. The PivotAsync() method takes an object of this type.

### Reviewer Statistics API

The Reviewer Statistics API contains the following methods and classes.

#### Methods

The Reviewer Statistics API exposes the following methods on the IReviewerStatisticsService interface in the Relativity.Audit.Services.Interfaces.<VersionNumber>.ReviewerStatistics namespace:

- GetDocumentActionCountsAsync() method - retrieves the total action counts for all the updated documents in a workspace for a specified time frame. Its parameters include the Artifact ID of a workspace and a DocumentActionCountCriteria object. This method returns a DocumentActionCountResponse object. See Retrieve action counts for updated documents .

- GetDocumentActionsPerHourOfDayAsync() method - aggregates the total distinct document actions performed by each reviewer, grouped by the hour of the day in which the action was performed. Its parameters include the Artifact ID of a workspace and a DocumentActionPerHourOfDayCriteria object. This method returns a DocumentActionPerHourOfDayResponse object. See Retrieve an aggregate of user actions by hour .

- GetReviewerChoicesAsync() method - retrieve information about choices reviewed by users in a specific workspace. Its parameters include the Artifact ID of a workspace and a ReviewerChoicesCriteria object. This method returns a ReviewedFieldChoicesPerUserResponse object. See Retrieve choices reviewed by users .

- GetReviewerStatsAsync() method - generates a report similar to the reviewer statistics report available through the Relativity UI. Its parameters include the Artifact ID of a workspace and a ReviewerStatsDataRequest object. See Retrieve a summary report of reviewer statistics .

- GetTotalReviewedDocumentSizesAsync() method - retrieves the size of the extracted text for all documents reviewed per reviewer. Its parameters include the Artifact ID of a workspace and a ReviewedDocumentSizeCriteria object. This method returns a ReviewedDocumentSizeResponse object. See Retrieve extracted text size of reviewed documents .

- GetUsageTimesAsync() method - computes the total usage time in seconds per reviewer. Its parameters include the Artifact ID of a workspace and a UsageTimeResponse UsageTimeCriteria object. This method returns a UsageTimeResponse object. See Retrieve the usage time per reviewer .

#### Classes

The Reviewer Statistics API includes the following classes available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.ReviewerStatistics.Models namespace:

- DocumentActionCountResponse class - represents the total actions perform on a document per user based on the specified search criteria. The GetDocumentActionCountsAsync() method returns an object of this type.

- DocumentActionCountCriteria class - represents a request containing the audit actions and related users used for retrieving the total counts for actions performed. The GetDocumentActionCountsAsync() method takes an object of this type.

- DocumentActionPerHourOfDayResponse class - represents an aggregation of the total number of document actions performed hourly based on the specified search criteria. The GetDocumentActionsPerHourOfDayAsync() method returns an object of this type.

- DocumentActionPerHourOfDayCriteria class - represents a request containing the audit actions, related users, and timeframe for retrieving data on document actions performed hourly by reviewers. The GetDocumentActionsPerHourOfDayAsync() method takes an object of this type.

- ReviewedDocumentSizeCriteria class - represents a request containing the audit actions, related users, and field ID used for retrieving the size of the reviewed extracted text. The GetTotalReviewedDocumentSizesAsync() method takes an object of this type.

- ReviewedDocumentSizeResponse class - represents the extracted text size per reviewer based on the specified search criteria. The GetTotalReviewedDocumentSizesAsync() method returns an object of this type.

- ReviewedFieldChoicesPerUserResponse class - represents data on the choices selected by reviewers based on the specified search criteria. The GetReviewerChoicesAsync() method returns an object of this type.

- ReviewerChoicesCriteria - represents the field IDs, user IDs, and timeframe used to retrieve information about choices selected by reviewers. The GetReviewerChoicesAsync() method takes an object of this type.

- ReviewersStats class - represents the data in a reviewer statistics report. The GetReviewerStatsAsync() method returns an object of this type.

- ReviewerStatsDataRequest class - represents a request containing the timeframe, additional actions, and a Boolean value for inclusion or exclusion of admin actions used to generate a reviewer statistics report. The GetReviewerStatsAsync() method takes an object of this type.

- UsageTimeCriteria class - represents a request containing the audit actions, related users, and timeframe for retrieving usage metrics. The GetUsageTimesAsync() method takes an object of this type.

- UsageTimeResponse class - represents the usage time in seconds based on the specified search criteria. The GetUsageTimesAsync() method returns an object of this type.

### Audit Query API

The Audit Query API contains the following method and classes.

#### Methods

The Audit Query API exposes the following method on the IAuditQueryService interface in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Query namespace:

- GetAuditAsync() method - searches for a specific audit record. Its parameters include the Artifact ID of a workspace and a GetAuditRequest object. This method returns a returns AuditLogItem object. See Query for an audit record .

#### Classes

The Audit Query API includes the following classes available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.Query.Models namespace:

- AuditLogItem class - represents the result of a query for an audit log. Its properties include the identifier and timestamp for the audit log, the artifact name, action name, and others. The GetAuditAsync() method returns an object of this type.

- GetAuditRequest class - represents the audit log to query on. Its properties include the identifier and timestamp of an audit record. The GetAuditAsync() method takes an object of this type.

### Audit Object Manager UI API

The Audit Object Manager UI API contains the following methods and classes.

#### Methods

The Audit Object Manager UI API exposes the following methods on the IAuditObjectManagerUIService interface in the Relativity.Audit.Services.Interfaces.<VersionNumber>.UI namespace:

- QueryAsync() method - searches for specific fields on an audit for display in the Relativity UI. It is an overloaded method that takes the Artifact ID of a workspace, a QueryRequest object, the index of the first artifact in the result set, the number of items to return, and an optional AuditQueryOptions object. It also takes CancellationToken and IProgress<ProgressReport> objects. This method returns a QueryResult object. See Query on audit fields .

- QuerySlimAsync() method - searches for specific fields on an audit for display in the Relativity UI but returns a smaller payload then the QueryAsync() method. It is also an overloaded method that takes the same parameters as the QueryAsync() method, except for the AuditQueryOptions object. This method returns a QueryResultSlim object. See Query on audit fields and return a smaller payload .

The method signatures for the overloaded QueryAsync() and QuerySlimAsync() methods include the CancellationToken and IProgress<ProgressReport> objects. However, they aren't supported but must be passed to the methods as required.

#### Classes

The Audit Object Manager UI API includes the following classes available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.UI.Models namespace:

- QueryResult class - represents the results of a search for specific audit fields. Its properties contain information about the result set, including a list of result items, the total number of Artifacts returned, an indicator about the success of the operation, and others. The QueryAsync() method returns an object of this type.

- QueryRequest class - represents the settings for the search that you want to run. The QueryAsync() and the QuerySlimAsync() methods take an object of this type as a parameter.

- QueryResultSlim class - represents the results of a search for specific audit fields returned by the QuerySlimAsync() method. It has the same properties as the QueryResult class.

The Audit Object Manager UI API includes the following class available in the Relativity.Audit.Services.Interfaces.<VersionNumber>.UI.Models namespace:

- AuditQueryOptions class - represents the option to return escaped JSON string instead of HTML. The data is returned as HTML is for display on the Audit tab in the Relativity UI, but you may want to return JSON to perform further analysis on it. For more information, see Audit in the Relativity Documentation site.

## Guidelines for the Audit APIs

Review the following guidelines for working with the Audit APIs.

### Operations supported by the Audit APIs

The following table lists a summary of operations that you can perform using the Audit APIs.

API name Method name Code samples

Audit Metrics GetWorkspaceAuditMetricsAsync() Retrieve the total number and size of audits

Audit Revert ValidateRevertAuditAsync() Validate a revert operation for an audit

RevertAuditAsync() Revert an audit

MassRevertAuditAsync() Mass revert a list of audits

Audit Pivot PivotAsync() Query with Pivot on audit data

Reviewer Statistics GetDocumentActionCountsAsync() Retrieve action counts for updated documents

GetUsageTimesAsync() Retrieve the usage time per reviewer

GetTotalReviewedDocumentSizesAsync() Retrieve extracted text size of reviewed documents

GetDocumentActionsPerHourOfDayAsync() Retrieve an aggregate of user actions by hour

GetReviewerChoicesAsync() Retrieve choices reviewed by users

GetReviewerStatsAsync() Retrieve a summary report of reviewer statistics

Audit Query GetAuditAsync() Query for an audit record

Audit Object Manager UI QueryAsync() Query on audit fields

QuerySlimAsync() Query on audit fields and return a smaller payload

### Admin-level context

To work with audits at the admin-level context, set the workspace ID in a method call -1. For example, the workspaceID the following code could be set to -1 , so this call would retrieve number and size of the audits for a Relativity instance. See Retrieve the total number and size of audits .

Copy

```text
1
AuditMetricsAggregateResponse workspaceMetrics = await auditMetricsService.GetWorkspaceAuditMetricsAsync(workspaceId);
```

### Query conditions

You can specify conditions for an audit query in the Condition or RowCondition properties of a request object. Setting these properties is equivalent to using conditions and list filtering in the Relativity UI. For information about rendering audit details in the Relativity UI, see Audit in the Relativity Documentation site.

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

## Audit Metrics API

The Audit Metrics API supports the retrieval of information about the number and size of the audits in a specific workspace.

### Retrieve the total number and size of audits

To retrieve the total count of all audits in a workspace, and the total size of the audits in bytes, call the GetWorkspaceAuditMetricsAsync() method by passing the Artifact ID of a workspace. This method returns an AuditMetricsAggregateResponse object. See the following code sample:

Copy

```text
1
2
3
using (var auditMetricsService = proxy.GetClient<IAuditMetricsService>()) {

    AuditMetricsAggregateResponse workspaceMetrics = await auditMetricsService.GetWorkspaceAuditMetricsAsync(workspaceId);

}
```

## Audit Revert API

The Audit Revert API supports reverting document update actions. It provides methods for reverting a single action or list of actions, and for verifying whether the revert operation can be performed on an action.

For example, you can use a method on this service as a programmatic shortcut for reverting incorrect coding decisions.

### Validate a revert operation for an audit

To confirm that an audit action can be reverted, call the ValidateRevertAuditAsync() method by passing the Artifact ID of a workspace and an RevertAuditRequest object to it. It returns a ValidateRevertAuditResponse object that contains the IsRevertable property, which indicates whether the operation can be completed. See the following code sample:

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
using (var revertService = proxy.GetClient<IAuditRevertService> ()) {

var request = new RevertAuditRequest

{

    AuditId = "1409184",

    Timestamp = "2019-05-22T15:10:42.877"

};

    ValidateRevertAuditResponse validateResponse = await revertService.ValidateRevertAuditAsync(workspaceId, request);

}
```

### Revert an audit

To revert an audit action, call the RevertAuditAsync() method by passing the Artifact ID of a workspace and an RevertAuditRequest object to it. It returns a RevertAuditResponse object, which contains a Success property indicating the status of the operation.

- Before reverting an action, consider calling the ValidateRevertAuditAsync() method to verify that the revert operation can succeed.

- You must set both the Timestamp and Id properties on the request to uniquely identify the audit record.

See the following code sample:

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
using (var revertService = proxy.GetClient<IAuditRevertService>())

{

    var request = new RevertAuditRequest

    {

        AuditId = "1409184",

        Timestamp = "2019-05-22T15:10:42.877"

    };

    RevertAuditResponse revertResponse = await revertService.RevertAuditAsync(workspaceId, request);

}
```

### Mass revert a list of audits

You can control the maximum number of Audits that can be reverted during a mass operation by updating the RevertMaxAuditCount instance setting. For more information, see Instance settings descriptions on the Relativity Documentation site.

The following code sample illustrates how to instantiate a list of RevertAuditRequest objects, and then call the MassRevertAuditAsync() method by passing the Artifact ID of a workspace and the request object. This method returns a MassRevertAuditResponse object.

- The MassRevertAuditAsync() method validates that each action can be successfully reverted before performing this operation.

- You must set both the Timestamp and Id properties on the request to uniquely identify the audit record.

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
using (var revertService = proxy.GetClient<IAuditRevertService>())

{

    var request = new MassRevertAuditRequest

    {

        RevertAuditRequests = new List<RevertAuditRequest>

        {

            new RevertAuditRequest

            {

                AuditId = "1409184",

                Timestamp = "2019-05-22T15:10:42.877"

            },

            new RevertAuditRequest

            {

                AuditId = "1409411",

                Timestamp = "2019-05-22T15:35:01.947"

            },

        }

    };

    MassRevertAuditResponse massRevertResponse = await revertService.MassRevertAuditAsync(workspaceId, request);

}
```

### Query with Pivot on audit data

The following code sample illustrates how to instantiate a PivotSettings object by setting the pivot and query conditions. Call the PivotAsync() method by passing the Artifact ID of a workspace, and the PivotSettings, CancellationToken, and IProgress objects. This method returns a PivotResultSet. For more information, see Query conditions .

The method signature for the PivotAsync() method includes the CancellationToken and IProgress<ProgressReport> objects. However, they aren't supported but must be passed to the method as required.

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
using (var pivotService = proxy.GetClient<IAuditPivotService>())

{

    var cancellationToken = new CancellationToken(); // required but not supported

    var progressToken = new Progress<string>(); // required but not supported

    var settings = new PivotSettings

    {

        // Field Artifact ID

        GroupBy = new FieldRef(1039619),

        PivotOn = new FieldRef(1039617),

        ObjectSetQuery = new global::Relativity.Services.Query

        {

            // Filter conditions

            Condition = "((('Audit ID' LIKE ['1413541'])))",

            RowCondition = ""

        },

        ConvertNumberFieldValuesToString = true,

        MaximumNumberOfColumns = 10,

        MaximumNumberOfRows = 10,

        Timeout = 10,

        RawDataOnly = false,

        TimeZone = "America/Chicago"

    };

    Console.WriteLine(JsonConvert.SerializeObject(settings));

    PivotResultSet pivotResponse = await pivotService.PivotAsync(workspaceId, settings, cancellationToken, progressToken);

}
```

## Reviewer Statistics API

The Reviewer Statistics API provides methods for returning information about reviewer actions, such as the number of actions performed by a reviewer on a document, the usage time per review, a summary report of reviewer actions, and others.

Review the following guidelines for setting properties on the request objects:

- If you pass an empty array for the UserIDs property on the request object, the report is computed for all the users in the workspace.

- The StartDate and EndDate properties determine the timeframe used to generate a report. Only audits within this timeframe are included in the report.

- The TimeZone property for the reviews included in the summary report is specified as a UTC offset. See Retrieve a summary report of reviewer statistics .

### Retrieve action counts for updated documents

You can retrieve the total action counts for all the updated documents in a workspace for a specified time frame. Additionally, you can list specific actions that you want counted per document.

The following code sample illustrates how to instantiate DocumentActionCountCriteria object, and then call the GetDocumentActionCountsAsync() method by passing the Artifact ID of a workspace and the request object.

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
using (var reviewerStats = proxy.GetClient<IReviewerStatisticsService>())

{

    var request = new DocumentActionCountCriteria

    {

        AuditActionIds = new int[] { 1, 2, 3},

        UserIds = new int[] {9, 777},

        StartDate = new DateTimeOffset(DateTime.Now.AddDays(-5)),

        EndDate = new DateTimeOffset(DateTime.Now),

        TimeZone = "America/Chicago"

    };



    DocumentActionCountResponse actionCounts = await reviewerStats.GetDocumentActionCountsAsync(workspaceId, request);

}
```

### Retrieve the usage time per reviewer

Use the GetUsageTimesAsync() method to compute the total usage time in seconds per reviewer.

In the request, the Downtime property indicates the number of seconds used to determine whether a null session action should be joined to a non-null session action. If the time difference for the performance of a null session action is larger than this maximum duration, the null session is counted as one minute.

The following code sample illustrates how to instantiate UsageTimeCriteria object, and then call the GetUsageTimesAsync() method by passing the Artifact ID of a workspace and the request object.

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
using (var reviewerStats = proxy.GetClient<IReviewerStatisticsService>())

{

    var request = new UsageTimeCriteria

    {

        AuditActionIds = new int[] { 1, 2, 3 },

        UserIds = new int[] { 9, 777 },

        StartDate = new DateTimeOffset(DateTime.Now.AddDays(-5)),

        EndDate = new DateTimeOffset(DateTime.Now),

        TimeZone = "America/Chicago",

        DownTimeThresholdSeconds = 900 // seconds

    };

    UsageTimeResponse usageTime = await reviewerStats.GetUsageTimesAsync(workspaceId, request);

}
```

### Retrieve extracted text size of reviewed documents

Use the GetTotalReviewedDocumentSizesAsync() method to retrieve the size of the extracted text for all documents reviewed per reviewer.

The following code sample illustrates how to instantiate ReviewedDocumentSizeCriteria object, and then call the GetTotalReviewedDocumentSizesAsync() method by passing the Artifact ID of a workspace and the request object.

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
using (var reviewerStats = proxy.GetClient<IReviewerStatisticsService>())

{

    var request = new ReviewedDocumentSizeCriteria

    {

        AuditActionIds = new int[] {1, 2, 3},

        UserIds = new int[] {9, 777},

        StartDate = new DateTimeOffset(DateTime.Now.AddDays(-5)),

        EndDate = new DateTimeOffset(DateTime.Now),

        TimeZone = "America/Chicago",

        ExtractedTextFieldArtifactId = 1003668,

    };



    ReviewedDocumentSizeResponse documentSize = await reviewerStats.GetTotalReviewedDocumentSizesAsync(workspaceId, request);

}
```

### Retrieve an aggregate of user actions by hour

Use the GetDocumentActionsPerHourOfDayAsync() method to aggregate the total distinct document actions performed by each reviewer, grouped by the hour of the day in which the action was performed.

The following code sample illustrates how to instantiate DocumentActionPerHourOfDayCriteria object, and then call the GetDocumentActionsPerHourOfDayAsync() method by passing the Artifact ID of a workspace and the request object.

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
using (var reviewerStats = proxy.GetClient<IReviewerStatisticsService>())

{

    var request = new DocumentActionPerHourOfDayCriteria

    {

        AuditActionIds = new int[] { 1, 2, 3 },

        UserIds = new int[] { 9, 777 },

        StartDate = new DateTimeOffset(DateTime.Now.AddDays(-5)),

        EndDate = new DateTimeOffset(DateTime.Now),

        TimeZone = "America/Chicago",

    };



    DocumentActionPerHourOfDayResponse documentActionPerHourOfDayResponse = await reviewerStats.GetDocumentActionsPerHourOfDayAsync(workspaceId, request);

}
```

### Retrieve choices reviewed by users

Use the GetReviewerChoicesAsync() method to retrieve information about choices reviewed by users in a specific workspace. This method supports retrieving statistics for single choice fields, multiple choice fields, and Yes/No fields. Set the FieldIds property to the Artifact IDs of the fields that you want used to compute the choices selected by reviewers.

If you pass an empty array for the UserIdsToExcludeInReport or the UserIdsToIncludeInReport field, the report is computed for all the users in the workspace.

The following code sample illustrates how to instantiate ReviewerChoicesCriteria object, and then call the GetReviewerChoicesAsync() method by passing the Artifact ID of a workspace and the request object.

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
using (var reviewerStats = proxy.GetClient<IReviewerStatisticsService>())

{

    var request = new ReviewerChoicesCriteria

    {

        FieldIds = new int[] { 1035357 },

        UserIdsToIncludeInReport = new int[]{9},

        UserIdsToExcludeInReport = new int[]{777},

        StartDate = new DateTimeOffset(DateTime.Now.AddDays(-5)),

        EndDate = new DateTimeOffset(DateTime.Now),

        TimeZone = "America/Chicago",

    };



    ReviewedFieldChoicesPerUserResponse reviewerChoice = await reviewerStats.GetReviewerChoicesAsync(workspaceId, request);

}
```

### Retrieve a summary report of reviewer statistics

Use the GetReviewerStatsAsync() method to programmatically generate a report similar to the reviewer statistics report available through the Relativity UI. For more information, see Reviewer statistics on the Relativity Documentation site.

On the ReviewerStatsDataRequest object, set the NonAdmin to false if you want to include system admin statistics in the data. Additionally, set the AdditionalActions property to one of the following values:

- None - include view and update actions.

- Mass Edit - include view, update, and mass edit actions.

- Propagation - include propagation actions.

- Mass Edit and Propagation - include view, update, mass edit, and propagation actions.

The following code sample illustrates how to instantiate ReviewerStatsDataRequest object, and then call the GetReviewerStatsAsync() method by passing the Artifact ID of a workspace and the request object.

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
using (var reviewerStats = proxy.GetClient<IReviewerStatisticsService>())

{

    var request = new ReviewerStatsDataRequest

    {

        StartDate = "2019-01-01T00:00:00Z",

        EndDate = "2019-10-05T00:00:00Z",

        TimeZone = -6.0,

        NonAdmin = false,

        AdditionalActions = "Mass Edits"

    };



    IEnumerable<ReviewersStats> reviewerMetrics = await reviewerStats.GetReviewerStatsAsync(workspaceId, request);

}
```

## Audit Query API

The Audit Query service supports querying for a specific audit record.

You must set both the Timestamp and Id properties on the request to uniquely identify the audit record.

### Query for an audit record

The following code sample illustrates how to instantiate a GetAuditRequest object, and then pass the GetAuditAsync() method the Artifact ID of a workspace and the request object. This method returns an AuditLogItem object. See the following code sample:

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
using (IAuditQueryService auditQueryService = Helper.GetServicesManager().CreateProxy<IAuditQueryService>(Relativity.API.ExecutionIdentity.System))

{

    var request = new GetAuditRequest

    {

        Id = "484127",

        Timestamp = "2019-04-26T15:56:53.427"

    };

    AuditLogItem queryResults = await auditQueryService.GetAuditAsync(workspaceId, request);

}
```

## Audit Object Manager UI API

The Audit Object Manager UI service supports querying on audit details for display in the Relativity UI. It provides two overloaded methods for querying:

- QueryAsync() method - This overloaded method returns detailed information about the field-value pairs returned by the query on the audit, including complete field details. For samples, see Query on audit fields .

- QuerySlimAsync() method - This overloaded method returns a smaller payload to save bandwidth. It returns only the values of the fields specified in the request without the detailed field information. For samples, see Query on audit fields and return a smaller payload .

Review the following guidelines for Audit Object Manager UI API:

- Sorting is only supported for the TimeStamp and ExecutionTime properties.

- Use Condition and RowCondition properties on the request object for filtering. For more information, see Query conditions .

- Review the following information about paging:

- Query tokens aren't supported for audit record result set paging.

- Check the value of the TotalCount field on the initial response. If it is greater than the specified Length field in the request, adjust the value of the Start field on the subsequent query requests to page through results.

In Relativity instances with a very large number of audit records (1,000,000 or more), paging towards the end of the result set can cause a Deep Paging Exception.

- The Audit record query uses the Relativity Object Manager query pattern. For more information, see Object Manager (.NET) .

- Call the overloaded method with the auditQueryOptions argument if you want to perform additional analysis on the audit data. This method returns the data as an escaped JSON string instead of HTML. For more information, see Query for an audit record .

### Query on audit fields

The overloaded QueryAsync() method takes the following arguments:

- workspaceID - an integer representing the Artifact ID of a workspace, or -1 to indicate the admin-level context.

- request - an instance of the QueryRequest class.

- start - an integer representing the index of the first artifact in the result set.

- length - an integer representing the number of items to return in the query result, beginning with index in the start argument.

- auditQueryOptions - an optional AuditQueryOptions object, which contains a Boolean value indicating whether the Details field should contain an escaped JSON string instead of HTML. Set this field to true if you want to perform further analysis on the audit data. Otherwise, the data is returned as HTML for display on the Audit tab in the Relativity UI. For more information, see Audit in the Relativity Documentation site.

View overloaded QueryAsync() methods Copy

```text
1
2
3
4
5
6
Task<QueryResult> QueryAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length

)
```

The following method signature includes the CancellationToken and IProgress<ProgressReport> objects. However, they aren't supported but must be passed to the method as required.

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
Task<QueryResult> QueryAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length,

    CancellationToken cancel,

    IProgress<ProgressReport> progress

)
```

Copy

```text
1
2
3
4
5
6
7
Task<QueryResult> QueryAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length,

    AuditQueryOptions auditQueryOptions

)
```

#### Code sample: querying on specific fields

This code samples illustrates how to instantiate the QueryRequest object to search on specific fields. It also shows how to call the QueryAsync() method by passing the Artifact ID of the workspace, a request object, the index for the first item in the result set, and the number items to returns.

Copy Querying on specific fields

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
using (var auditObjectManager = proxy.GetClient<IAuditObjectManagerUIService>())

{

    var request = new QueryRequest

    {

        Fields = new List<Relativity.Services.Objects.DataContracts.FieldRef>

        {

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Audit ID"},

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Details"}

        },

        Condition = "",

        RowCondition = "",

        Sorts = new List<Sort>

        {

            new Sort

            {

                Direction = SortEnum.Descending,

                FieldIdentifier = new Relativity.Services.Objects.DataContracts.FieldRef {Name = "Timestamp"} // Only support Timestamp and Execution Time (ms)

            }

        },

        ExecutingSavedSearchID = 0,

        ExecutingViewID = 0,

        ActiveArtifactID = 0,

        MaxCharactersForLongTextValues = 0

    };

    QueryResult queryRequest = await auditObjectManager.QueryAsync(workspaceID, request, 1, 2);

}
```

#### Code sample: querying on specific fields with the cancellation and progress arguments

This code samples illustrates how to instantiate the QueryRequest object to search on specific fields. For this method, you must pass both the CancellationToken and IProgress<ProgressReport> objects even though they aren't supported.

Copy Querying on specific fields with the cancellation and progress arguments

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
using (var auditObjectManager = proxy.GetClient<IAuditObjectManagerUIService>())

{

    var cancellation = new CancellationToken(); // Required but not supported.

    var progress = new Progress<ProgressReport>(); // Required but not supported

    var request = new QueryRequest

    {

        Fields = new List<Relativity.Services.Objects.DataContracts.FieldRef>

        {

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Audit ID"},

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Details"}

        },

        Condition = "",

        RowCondition = "",

        Sorts = new List<Sort>

        {

            new Sort

            {

                Direction = SortEnum.Descending,

                FieldIdentifier = new Relativity.Services.Objects.DataContracts.FieldRef {Name = "Timestamp"} // Only support Timestamp and Execution Time (ms)

            }

        },

        ExecutingSavedSearchID = 0,

        ExecutingViewID = 0,

        ActiveArtifactID = 0,

        MaxCharactersForLongTextValues = 0

    };

    QueryResult queryRequest = await auditObjectManager.QueryAsync(workspaceID, request, 1, 2, cancellation, progress);

}
```

#### Code sample: using the query options

The following code sample illustrates how to call the QueryAsync() method by passing an AuditQueryOptions object in addition to the other required arguments. The ReturnRawDetails property is set to true, which indicates that the method should return a JSON string.

Copy Using the query options

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
using (var auditObjectManager = proxy.GetClient<IAuditObjectManagerUIService>())

{

    var queryOptions = new AuditQueryOptions

    {

        ReturnRawDetails = true

    };

    var request = new QueryRequest

    {

        Fields = new List<Relativity.Services.Objects.DataContracts.FieldRef>

        {

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Audit ID"},

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Details"}

        },

        Condition = "",

        RowCondition = "",

        Sorts = new List<Sort>

        {

            new Sort

            {

                Direction = SortEnum.Descending,

                FieldIdentifier = new Relativity.Services.Objects.DataContracts.FieldRef {Name = "Timestamp"} // Only support Timestamp and Execution Time (ms)

            }

        },

        ExecutingSavedSearchID = 0,

        ExecutingViewID = 0,

        ActiveArtifactID = 0,

        MaxCharactersForLongTextValues = 0

    };

    QueryResult queryRequest = await auditObjectManager.QueryAsync(workspaceID, request, 1, 2, queryOptions);

}
```

### Query on audit fields and return a smaller payload

The overloaded QuerySlimAsync() method takes the following arguments:

- workspaceID - an integer representing the Artifact ID of a workspace, or -1 to indicate the admin-level context.

- request - an instance of the QueryRequest class.

- start - an integer representing the index of the first artifact in the result set.

- length - an integer representing the number of items to return in the query result, beginning with index in the start argument.

The method signatures for the overloaded QuerySlimAsync() method include the CancellationToken and IProgress<ProgressReport> objects. However, they aren't supported but must be passed to the methods as required.

View overloaded QuerySlimAsync() methods Copy

```text
1
2
3
4
5
6
Task<QueryResultSlim> QuerySlimAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length

)
```

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
Task<QueryResultSlim> QuerySlimAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length,

    CancellationToken cancel,

    IProgress<ProgressReport> progress

)
```

Copy

```text
1
2
3
4
5
6
7
Task<QueryResultSlim> QuerySlimAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length,

     CancellationToken cancel

)
```

Copy

```text
1
2
3
4
5
6
7
Task<QueryResultSlim> QuerySlimAsync(

    int workspaceID,

    QueryRequest request,

    int start,

    int length,

    IProgress<ProgressReport> progress

)
```

#### Code sample: querying on specific fields

This code samples illustrates how to instantiate the QueryRequest object to search on specific fields. It also shows how to call the QueryAsync() method by passing the Artifact ID of the workspace, a request object, the index for the first item in the result set, and the number items to returns.

Copy Querying on specific fields

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
using (var auditObjectManager = proxy.GetClient<IAuditObjectManagerUIService>())

{

    var request = new QueryRequest

    {

        Fields = new List<Relativity.Services.Objects.DataContracts.FieldRef>

        {

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Audit ID"},

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Details"}

        },

        Condition = "",

        RowCondition = "",

        Sorts = new List<Sort>

        {

            new Sort

            {

                Direction = SortEnum.Descending,

                FieldIdentifier = new Relativity.Services.Objects.DataContracts.FieldRef {Name = "Timestamp"} // Only support Timestamp and Execution Time (ms)

            }

        },

        ExecutingSavedSearchID = 0,

        ExecutingViewID = 0,

        ActiveArtifactID = 0,

        MaxCharactersForLongTextValues = 0

    };

    QueryResultSlim queryRequest = await auditObjectManager.QuerySlimAsync(workspaceID, request, 1, 2);

}
```

Code sample: using the cancellation and progress options

This code samples illustrates how to instantiate the QueryRequest object to search on specific fields. To use this method, you must pass both the CancellationToken and IProgress<ProgressReport> objects even though they aren't supported.

Copy using the cancellation and progress options

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
using (var auditObjectManager = proxy.GetClient<IAuditObjectManagerUIService>())

{

    var cancellation = new CancellationToken(); // required but not supported

    var progress = new Progress<ProgressReport>(); // required but not supported

    var request = new QueryRequest

    {

        Fields = new List<Relativity.Services.Objects.DataContracts.FieldRef>

        {

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Audit ID"},

            new Relativity.Services.Objects.DataContracts.FieldRef{Name = "Details"}

        },

        Condition = "",

        RowCondition = "",

        Sorts = new List<Sort>

        {

            new Sort

            {

                Direction = SortEnum.Descending,

                FieldIdentifier = new Relativity.Services.Objects.DataContracts.FieldRef {Name = "Timestamp"} // Only support Timestamp and Execution Time (ms)

            }

        },

        ExecutingSavedSearchID = 0,

        ExecutingViewID = 0,

        ActiveArtifactID = 0,

        MaxCharactersForLongTextValues = 0

    };

    QueryResultSlim queryRequest = await auditObjectManager.QuerySlimAsync(workspaceID, request, 1, 2, cancellation, progress);

}
```

On this page

- Audit (.NET)

- Fundamentals for Audit APIs

- Audit Metrics API

- Audit Revert API

- Audit Pivot API

- Reviewer Statistics API

- Audit Query API

- Audit Object Manager UI API

- Guidelines for the Audit APIs

- Operations supported by the Audit APIs

- Admin-level context

- Query conditions

- Audit Metrics API

- Retrieve the total number and size of audits

- Audit Revert API

- Validate a revert operation for an audit

- Revert an audit

- Mass revert a list of audits

- Query with Pivot on audit data

- Reviewer Statistics API

- Retrieve action counts for updated documents

- Retrieve the usage time per reviewer

- Retrieve extracted text size of reviewed documents

- Retrieve an aggregate of user actions by hour

- Retrieve choices reviewed by users

- Retrieve a summary report of reviewer statistics

- Audit Query API

- Query for an audit record

- Audit Object Manager UI API

- Query on audit fields

- Query on audit fields and return a smaller payload


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
