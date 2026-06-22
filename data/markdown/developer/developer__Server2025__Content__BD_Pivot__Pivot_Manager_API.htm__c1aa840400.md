---
title: "Pivot Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Pivot/Pivot_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:23+00:00
sha256: f44a5d12580f9cf28f0c24a437672e436e206220b85a4b94a09a120becc7d1da
---

Pivot Manager (.NET)

# Pivot Manager (.NET)

In Relativity, Pivot helps you analyze and report trends or patterns in workspace data by querying specific sets of data and summarizing the results in a table or chart. To create those tables or charts, you can use predefined settings that are stored in a Pivot profile or custom settings that you define when you create a Pivot query.

Whether you use predefined or custom settings, Relativity provides a range of options for querying, calculating, and displaying the data. By using the Pivot APIs, you can extend those options by running queries based on existing Pivot profiles, creating and running custom Pivot queries, and passing query results to another application—for example, a third-party software application or web-based visualization tool—for deeper analysis and reporting.

For general information about Pivot, see Pivot on the Relativity Documentation site.

## Pivot fundamentals

Before you run a Pivot query, first determine whether you want to use custom settings or predefined settings that are stored in a Pivot profile. The Pivot APIs support both approaches, although you can’t use them to save custom settings as a Pivot profile. If you expect to reuse the same query settings more than once, it’s a good idea to create a Pivot profile with those settings directly in Relativity. You can then use the Pivot APIs to run a query that’s based on the profile and work with the resulting data.

If you prefer to use custom settings, you also need to answer a few key questions:

- Which field do you want to use to group the data? This field, referred to as the “Group By” field, creates the primary list of items to summarize data for and corresponds to what is typically the horizontal (x) axis of a chart.

- Do you want to break down the data further by using an additional field? If so, which field? This field, referred to as the “Pivot On” field, is a secondary field that you can optionally use to further characterize grouped data. It corresponds to what is typically the vertical (y) axis of a chart.

- If the Group By or Pivot On field is a Date field, what time interval do you want to use when calculating and summarizing data for the field? You can summarize date-based data by year, month and year, month only, or a combination of day, month, and year. Note that you can pivot data by using a Date field only if you also use a Date field to group data. In addition, you can pivot data by month only if you group data by year.

Before you can use any type of field to group data in a Pivot query, the field must be enabled for grouping (Field.AllowGroupBy property). Similarly, a field must be enabled for pivot (Field.AllowPivotOn property) before you can use it to pivot data. Later in this topic, we’ll provide examples of how to programmatically get a list of fields that you can use to group and pivot data.

In addition, you must have permission to view a field before you can use it in a Pivot query. Otherwise, an error occurs when you try to run the query because the Pivot APIs use the permission settings of the active user account.

Whether you plan to use a Pivot profile or custom settings, the IPivotManager interface and PivotSettings class in the Relativity Services API contain most of the methods and properties that you need to create and run a Pivot query:

- IPivotManager interface - Defines asynchronous methods for running a custom query or reading a Pivot profile and running a query based on the profile. It also provides optional parameters for implementing cancellation support, a progress indicator, or both.

- PivotSettings class - Defines objects and properties for creating a custom query, and properties that you can optionally set for a query that’s based on a Pivot profile. The various properties control settings such as the maximum number of rows or columns to return and, for custom queries, the Group By and Pivot On fields to use, and the time interval for calculating date-based data.

Both the IPivotManager interface and the PivotSettings class support using the Query class of the Relativity Services API to optionally define a sort order or criteria that documents or objects must meet to be included in a Pivot query and query results. Using the Query class can be helpful if you want to limit the results of a Pivot query by running the query against only a subset of documents or objects in a workspace.

To help you work with query results, the PivotResultSet class provides the results of a Pivot query as a standard .NET System.Data.DataTable object and defines properties for interpreting those results.

Note that the Pivot APIs aren’t designed to create any kind of persistent object that can be stored, read, or manipulated in a Relativity database. By default, custom Pivot queries and query results live only in memory and are dismissed after the response object is returned. However, you can retrieve or pass those results to another application by integrating the Pivot APIs into a larger solution.

## Create a PivotManager object

The first step in performing operations with a Pivot profile is to create an instance of the PivotManager class. To create an instance of the PivotManager class, use the IPivotManager interface in the Relativity Services API. The interface contains methods and parameters for instantiating a PivotManager object and specifying the operations that you want to perform, such as create, update, or query.

For running queries, the IPivotManager interface defines two fundamental methods, the ExecuteAsync method, which you use to run custom queries, and the ExecutePivotProfileAsync method, which you use to run queries based on Pivot profiles. Both methods are overloaded, which means that how you call the method depends on whether you want to implement a progress indicator, cancellation support, or both for the query.

Like other Services API interfaces, you start by accessing the IPivotManager interface through a client proxy to the Services API and instantiating a PivotManager object. If you plan to use the query with a custom page, event handler, or agent, you can use API Helpers:

Copy

```text
1
2
3
4
private Relativity.Services.Pivot.IPivotManager GetPivotManager(IHelper helper)

{

    return helper.GetServicesManager().CreateProxy<IPivotManager>(ExecutionIdentity.System));

}
```

After you create the client proxy and instantiate a PivotManager object, you’re ready to define the Pivot query or perform other operations that you want to run.

How you define the query to run depends on whether you want to use an existing Pivot profile or custom settings. For more information, see Run a query based on a Pivot profile or Execute a custom Pivot query .

## Create a Pivot profile

You can create a Pivot profile using the CreateProfileAsync() method on the IPivotManager Interface. The following code sample illustrates how to complete these tasks for creating a Pivot profile:

- Instantiate a logger using the ForContext() method on the IAPILog interface. For more information, see Log from a Relativity application.

- Use a try-catch block when instantiating the proxy using the Relativity API Helpers. For more information, see Using Relativity API Helpers.

- Set the required properties on the Pivot profile. For conceptual information about these properties, see Pivot profiles on the Relativity Documentation site.

- Use the CreateProfileAsync() method on the Pivot Manager service to create the Pivot profile.

- Use the logger to report errors that may occur when creating the profile.

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
public async Task<bool> CreateProfileAsync(IHelper helper)

{

    //Set the ForContext for the method.

    ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

    bool success = false;

    try

    {

        //Use the ServiceManager to create an IPivotManager proxy

        using (Services.Pivot.IPivotManager pivotManager = helper.GetServicesManager().CreateProxy<Services.Pivot.IPivotManager>(ExecutionIdentity.System))

        {

            Services.PivotProfile.PivotProfileRef sampleProfile = new Services.PivotProfile.PivotProfileRef()

            {

                ChartOrientation = ChartOrientationOption.Vertical,

                ChartType = ChartTypeOption.Line,

                GroupByDateTimePart = DateTimePartOption.Date,

                GroupByField = new FieldRef() { ArtifactID = this.SampleField_Date_ID },

                GroupByResultLimit = ResultLimitOption.All,

                GroupByResultLimitValue = null,

                ID = 0,

                Name = "sampleProfileName",

                ObjectType = new Services.ObjectTypeReference.ObjectTypeRef()

                {

                    DescriptorArtifactTypeID = this.SampleObjectType_Artifact_Type

                },

                PageSize = 100,

                PivotOnDateTimePart = DateTimePartOption.YearMonth,

                PivotOnField = new FieldRef() { ArtifactID = this.SampleField_Date_ID },

                PivotOnResultLimit = ResultLimitOption.Top,

                PivotOnResultLimitValue = 100,

                SortOn = SortOnOption.GroupByField,

                SortOrder = SortOrderOption.Descending,

                SwitchSeries = false,

                Toggles = new ToggleOptions()

                {

                    RotateLabels = false,

                    ShowBlankValues = false,

                    ShowGrandTotal = true,

                    ShowLabels = false,

                    ShowLegend = true,

                    ShowSubChart = false,

                    StaggerLabels = true

                }

            };

            Services.PivotProfile.PivotProfileRef results = await pivotManager.CreateProfileAsync(this.SampleWorkspace_ID, sampleProfile);

            if (results != null && results.ID > 0)

            {

                logger.LogDebug("Success: PivotManager.CreateProfileAsync was successful. Created profile with ID: {0}", results.ID);

                success = true;

            }

            else

            {

                logger.LogError("Error: PivotManager.CreateProfileAsync failed - Result was null");

            }

        }

    }

    catch (Exception ex)

    {

        logger.LogError(ex, "Error: PivotManager.CreateProfileAsync failed. Exception");

        success = false;

    }

    return success;

}
```

## Update a Pivot profile

To update a Pivot profile, use the UpdateProfileAsync() method on the on the IPivotManager Interface. The following code sample illustrates how to complete these tasks for updating a Pivot profile:

- Instantiate a logger using the ForContext() method on the IAPILog interface. For more information, see Log from a Relativity application.

- Use a try-catch block when instantiating the proxy using the Relativity API Helpers. For more information, see Using Relativity API Helpers.

- Set the required properties on the Pivot profile. For conceptual information about these properties, see Pivot profiles on the Relativity Documentation site.

- Use the UpdateProfileAsync() method on the Pivot Manager service to create the Pivot profile.

- Use the logger to report errors that may occur when updating the profile.

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
public async Task<bool> UpdateProfileAsync(IHelper helper)

{

    bool success = false;

    Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

    try

    {

        using (Services.Pivot.IPivotManager pivotManager = helper.GetServicesManager().CreateProxy<Services.Pivot.IPivotManager>(ExecutionIdentity.System))

        {

            var modifiedProfileName = "RenamedProfile";

            Services.PivotProfile.PivotProfileRef pivotProfileToUpdate;

            if (PivotProfileHelper.TryCreate(pivotManager, this.SampleWorkspace_ID, this.SampleField_Date_ID, this.SampleObjectType_Artifact_Type, out pivotProfileToUpdate))

            {

                pivotProfileToUpdate.Name = modifiedProfileName;

                Services.PivotProfile.PivotProfileRef results = await pivotManager.UpdateProfileAsync(this.SampleWorkspace_ID, pivotProfileToUpdate);

                if (results != null && results.ID == pivotProfileToUpdate.ID)

                {

                    logger.LogDebug("Success: PivotManager.UpdateProfileAsync was successful.");

                    success = true;

                }

                else

                {

                    logger.LogError("Error: PivotManager.UpdateProfileAsync failed - Result was null");

                }

            }

        }

    }

    catch (Exception ex)

    {

        logger.LogError(ex, "Unhandled Exception");

    }

    return success;

}
```

## Run a query based on a Pivot profile

To run a query based on a Pivot Profile, first get the identifier of both the Pivot profile that you want to use and the workspace that contains the profile. To get those identifiers, you can use core Services API members to return the Artifact identifier (ArtifactID property) for each item.

After you get the workspace and profile identifiers, you run the query by calling an ExecutePivotProfileAsync method (IPivotManager interface) and passing those identifiers as arguments. The following code sample demonstrates how. The sample assumes that a PivotManager object named GetPivotManager already exists, as discussed in Create a PivotManager object .

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

/*

Instantiate a PivotManager object and set the Artifact identifiers for the workspace and the Pivot profile. Optionally set a Query object

that defines the set of documents or objects to include in the Pivot query.

*/

public System.Data.DataTable ExecutePivotProfileAsync(int workspaceId, Relativity.Services.Query query, int pivotProfileArtifactId)

{

     Relativity.Services.Pivot.IPivotManager pivotManager = GetPivotManager();

     System.Threading.Tasks.Task<Relativity.Services.Pivot.PivotResultSet> executeTask = pivotManager.ExecutePivotProfileAsync(

          workspaceId, pivotProfileArtifactId, query);

     string errorMessage = null;

     System.Data.DataTable resultsTable = null;

     /*

     Run the query and return the results as a PivotResultSet object. Use a try/catch block to capture and optionally display

     an error message in case the query fails.

     */

     try

     {

          executeTask.Wait();

          Relativity.Services.Pivot.PivotResultSet results = executeTask.Result;

          if (results.Success)

          {

               resultsTable = results.Results;

          }

          else

          {

               errorMessage = results.Message;

          }

     }

     catch (Exception executionError)

     {

          errorMessage = executionError.ToString();

     }

     if (!string.IsNullOrEmpty(errorMessage))

     {

          //Optionally define how to display the error message

     }

     return resultsTable;

}
```

Note that the preceding sample represents a simple Pivot query and provides a container for reporting errors that might occur. You can customize the query in other ways by using additional parameters of the ExecutePivotProfileAsync method to implement a progress indicator, cancellation support, or both.

## Execute a custom Pivot query

Before you execute a custom Pivot query, it’s important to gather a few key pieces of information:

- The Artifact identifier of the workspace that you want to query.

- The Artifact identifier, name, or GUID of the field that you want to use to group data.

- The time interval to use when calculating and summarizing data, if you want to use a Date field to group or pivot data.

- The Artifact identifier, name, or GUID of the field that you want to use to pivot data, if you want to pivot data.

- A Query object that defines the set of documents or objects to include in the Pivot query, if you want to limit the query and query results to only a subset of documents or objects in the workspace.

To get the Artifact identifier (ArtifactID property) for the workspace or a field, you can use core Services API members.

To determine which field you want to use to group data, you can use the GetFieldsForGroupByAsync method (IPivotManager interface) to get a list of workspace fields that you have permission to access and are enabled for grouping:

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

/*

Set the Artifact identifier of the workspace and the Artifact Type identifier of the DTO that the fields apply

to. The applicable DTO is typically the Document object, which has an ArtifactTypeID value of “10”.

*/

public List<Relativity.Services.Field.FieldRef> GetAllowedGroupByFields(int workspaceId, pivotTargetArtifactTypeId)

{

     Relativity.Services.Pivot.IPivotManager pivotManager = GetPivotManager();

     System.Threading.Tasks.Task<List<FieldRef>> getFieldsTask = pivotManager.GetFieldsForGroupByAsync(

          workspaceId, pivotTargetArtifactTypeId);

     getFieldsTask.Wait();

     List<FieldRef> groupByFields = getFieldsTask.Result;

     return groupByFields;

}
```

Similarly, you can get a list of workspace fields that you have permission to access and are enabled for pivot by using the GetFieldsForPivotOnAsync method (IPivotManager interface):

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

/*

Set the Artifact identifier of the workspace and the Artifact Type identifier of the DTO that the fields apply

to. The applicable DTO is typically the Document object, which has an ArtifactTypeID value of “10”.

*/

public List<Relativity.Services.Field.FieldRef> GetAllowedPivotOnFields(int workspaceId, pivotTargetArtifactTypeId)

{

     Relativity.Services.Pivot.IPivotManager pivotManager = GetPivotManager();

     System.Threading.Tasks.Task<List<FieldRef>> getFieldsTask = pivotManager.GetFieldsForPivotOnAsync(

          workspaceId, pivotTargetArtifactTypeId);

     getFieldsTask.Wait();

     List<FieldRef> pivotOnFields = getFieldsTask.Result;

     return pivotOnFields;

}
```

After you determine which fields to use for grouping and pivoting the data and you have the Artifact identifier of the workspace that you want to query, you’re ready to build and run the query by using members of the IPivotManager interface and PivotSettings class.

The following code sample shows how to create and run a Pivot query that does the following:

- Queries all documents in a workspace.

- Calculates and groups document data by calendar year and pivots on that data by using another field.

- Provides a progress indicator that reports the status of the query while the query is running.

- Returns the results as a PivotResultSet object. To determine how many results to return, the example uses the instance settings for the Relativity database that hosts the workspace.

The sample assumes that a PivotManager object named GetPivotManager already exists, as discussed in Create a PivotManager object .

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
//Declare the workspace, Query object, and fields for grouping and pivoting data.

public System.Data.DataTable ExecutePivotQuery(

     int workspaceId, Relativity.Services.Query query, Relativity.Services.Field.FieldRef groupByField, Relativity.Services.Field.FieldRef pivotOnField)

/*

Create the query as a PivotSettings object with the required properties.

ArtifactTypeID – An integer that indicates which type of DTO to query. This example uses “10”,

which is the identifier for the Document object.

ObjectSetQuery – The Query object that defines the base set of documents to run the Pivot query against.

GroupBy - The Artifact identifier, name, or GUID of the field to use for grouping data.

GroupByDateGrouping – An enum that specifies the time interval for calculating grouped results. This

example uses “2” to calculate and group data by calendar year.

PivotOn – The Artifact identifier, name, or GUID of the field to use for pivoting data.

*/

{

     PivotSettings pivotQuerySettings = new Relativity.Services.Pivot.PivotSettings()

     {

          ArtifactTypeID = 10,

          ObjectSetQuery = query,

          GroupBy = groupByField,

          GroupByDateGrouping = 2,

          PivotOn = pivotOnField

     };

     //Define a progress indicator that reports the status of the query.

     System.Progress<string> progressReporter = new Progress<string>(PivotExecutionProgress);

     /*

     Run the query and return the results as PivotResultSet object. Use a try/catch

     block to capture and optionally display an error message in case the query fails.

     */

     Relativity.Services.Pivot.IPivotManager pivotManager = GetPivotManager();

     System.Threading.Tasks.Task<Relativity.Services.Pivot.PivotResultSet> executeTask = pivotManager.ExecuteAsync(

          workspaceId, pivotQuerySettings, progressReporter);

     string errorMessage = null;

     System.Data.DataTable resultsTable = null;

     try

     {

          executeTask.Wait();

          Relativity.Services.Pivot.PivotResultSet results = executeTask.Result;

          if (results.Success)

          {

               resultsTable = results.Results;

          }

          else

          {

               errorMessage = results.Message;

          }

     }

     catch (Exception executionError)

     {

          errorMessage = executionError.ToString();

     }

     if (!string.IsNullOrEmpty(errorMessage))

     {

          //Optionally define how to display the error message

     }

     return resultsTable;

}
```

Although the preceding sample demonstrates a few ways to customize a Pivot query—for example, implementing a progress indicator and providing a container for reporting errors—you can customize a query in other ways by using additional properties of the PivotSettings class. For example, you can define custom settings that specify the maximum number of columns and rows to return, the maximum amount of time to run the query before timing out, and whether to return only raw data or apply a Pivot view to the data. By using an additional parameter of the ExecuteAsync method, you can also implement cancellation support.

## Display query progress

The IPivotManager interface supports use of the .NET System.IProgress interface for implementing a progress indicator that reports the status of a Pivot query while the query is running. This means that you can report progress by passing an IProgress object as an argument for the progress parameter of a Pivot execution method. The Pivot execution method then captures progress messages that are sent by the Pivot execution code on the Relativity server, which you can display to a user. In a custom query for example:

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

//Define a progress indicator to report the status of the query.

System.Progress<string> progressReporter = new Progress<string>(PivotExecutionProgress);

//Pass the progress indicator as an argument for the Progress<String> object in the Pivot ExecuteAsync method.

var task = pivotManager.ExecuteAsync(workspaceId, pivotQuerySettings, progressReporter);

public void PivotExecutionProgress(string progressMessage)

{

     //Define a function to display progress messages while the query is running.

}
```

## Cancel a query

The IPivotManager interface also defines methods that help you implement cancellation support for a Pivot query, primarily through support for the .NET System.Threading.CancellationTokenSource class. To implement cancellation support, pass a CancellationTokenSource object as an argument for the cancellationToken parameter of a Pivot execution method, for example:

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

//Define the cancellation token.

_cancelQueryTokenSource = new System.Threading.CancellationTokenSource();

//Pass the token as an argument in the Pivot ExecuteAsync method.

var task = pivotManager.ExecuteAsync(workspaceId, pivotQuerySettings, _cancelQueryTokenSource.Token);

//Define a handler function to call when the user clicks a Cancel button.

public void CancelButton_Clicked()

{

     _cancelQueryTokenSource.Cancel();

}
```

## Work with query results

The results of any type of Pivot query are returned as a PivotResultSet object, which is fundamentally a .NET System.Data.DataTable object. This means that you can leverage a broad set of standard .NET methods to read, manipulate, and store the results of a Pivot query. For example, you might serialize the data to XML or send it to a SQL Server database by using ADO.NET. Note that Pivot queries don’t create or store any kind of persistent objects that can be read or manipulated in a Relativity database. Instead, they were designed to facilitate data transfer to other applications and tools. Although the query results live only in memory and are dismissed after the response object is returned, you can implement a Pivot query as part of a larger solution that captures query results, writes the results to a specified table, object, or other location, and then manipulates the results in that location.

## Export a Pivot query

To export a Pivot query, use the ExecuteExportAsync() method on the IPivotManager Interface. This method returns an Excel file.

The following code sample illustrates how to complete these tasks for exporting a Pivot query:

- Instantiate a logger using the ForContext() method on the IAPILog interface. For more information, see Log from a Relativity application.

- Use a try-catch block when instantiating the proxy using the Relativity API Helpers. For more information, see Using Relativity API Helpers.

- Set the required properties on a dashboard Pivot chart.

- Set the conditions on a query.

- Use theExecuteExportAsync() method on the Pivot Manager service to export the Pivot query.

- Use the logger to report errors that may occur during export.

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
public async Task<bool> ExecuteExportAsync(IHelper helper)

{

    bool success = false;

    Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

    try

    {

        using (Services.Pivot.IPivotManager pivotManager = helper.GetServicesManager().CreateProxy<Services.Pivot.IPivotManager>(ExecutionIdentity.System))

        {

            PivotProfileRef pivotProfileToUpdate;

            Dashboard sampleDashboard = null;

            Services.Query sampleObjectSetQuery = null;

            if (PivotProfileHelper.TryCreate(pivotManager, this.SampleWorkspace_ID, this.SampleField_Date_ID, this.SampleObjectType_Artifact_Type, out pivotProfileToUpdate))

            {

                sampleDashboard = new Dashboard() {

                    Pivots = new DashboardPivot[] {

                        new DashboardPivot() {

                            PivotProfileID = (int)pivotProfileToUpdate.ID,

                            PivotSettings = new PivotBase() {

                                ChartOrientation = pivotProfileToUpdate.ChartOrientation,

                                ChartType = pivotProfileToUpdate.ChartType,

                                GroupByDateTimePart = pivotProfileToUpdate.GroupByDateTimePart,

                                GroupByField = pivotProfileToUpdate.GroupByField,

                                GroupByResultLimit = pivotProfileToUpdate.GroupByResultLimit,

                                GroupByResultLimitValue = pivotProfileToUpdate.GroupByResultLimitValue,

                                Name = pivotProfileToUpdate.Name,

                                ObjectType = pivotProfileToUpdate.ObjectType,

                                PageSize = pivotProfileToUpdate.PageSize,

                                PivotOnDateTimePart = pivotProfileToUpdate.PivotOnDateTimePart,

                                PivotOnField = pivotProfileToUpdate.PivotOnField,

                                PivotOnResultLimit = pivotProfileToUpdate.PivotOnResultLimit,

                                PivotOnResultLimitValue = pivotProfileToUpdate.PivotOnResultLimitValue,

                                SortOn = pivotProfileToUpdate.SortOn,

                                SortOrder = pivotProfileToUpdate.SortOrder,

                                SwitchSeries = pivotProfileToUpdate.SwitchSeries,

                                Toggles = pivotProfileToUpdate.Toggles

                            }

                        }

                    },

                    CellRatio = 1

                };

                sampleObjectSetQuery = new Services.Query() {

                    Condition = "(('Artifact ID' ISSET))",

                    RowCondition = "",

                    SearchProviderCondition = null,

                    SampleParameters = null

                };

                PivotExportResult results = await pivotManager.ExecuteExportAsync(this.SampleWorkspace_ID, sampleDashboard, sampleObjectSetQuery);

                if (results != null)

                {

                    logger.LogDebug("Success: PivotManager.ExecuteExportAsync was successful.");

                    success = true;

                }

                else

                {

                    logger.LogError("Error: PivotManager.ExecuteExportAsync failed - Result was null");

                }

            }

        }

    }

    catch (Exception ex)

    {

        logger.LogError(ex, "Unhandled Exception");

    }

    return success;

}
```
