---
title: "Processing Filter Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Filter_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:20+00:00
sha256: a5adce44c2b75a9715c03e3e07b1845eefa7e867a61450530d1054119b85ecdd
---

Processing Filter Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Filter Manager

Processing filters provide functionality to view and select processed documents before publishing them to Relativity. The Processing Filter Manager API exposes methods for programmatically creating, updating, and deleting filters. It supports applying these filters to data and retrieving the filtered data. Additionally, this service exposes helper methods for retrieving filters associated with a data source or available in a specific workspace. For more general information, see Filtering data .

As a sample use case, you may want to implement a simplified processing workflow by programmatically adding complex criteria to filters applied to processing jobs in Relativity. This approach eliminates the need to manually enter filter criteria through the UI, which may be time consuming and error prone. Similarly, you can also use the Processing Filter Manager service to modify the settings on these or other complex filters implemented in your environment.

The Processing Filter Manager service also supports the same functionality through REST. For more information, see Processing Filter Manager (REST) .

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Fundamentals for the Processing Filter Manager API

Review the following information to learn about the methods, classes, and enumerations used by the Processing Filter Manager service.

### Methods

The Relativity.Processing.Services namespace contains the IProcessingFilterManager interface that exposes the following methods:

- ApplyFilterAsync() : applies a processing filter to the specified data set in a workspace. See Apply a processing filter .

- CreateExpressionFilterAsync() : adds a new processing filter to Relativity. See Create a processing filter .

- DeleteFilterAsync() : removes a processing filter from Relativity. See Delete a processing filter .

- GetDiscoveredDocumentsAsync() : retrieves discovered documents in a specific workspace. See Retrieve discovered documents .

- GetDiscoveredDocumentIdsAsync() : retrieve discovered document IDs. See Retrieve discovered document IDs .

- PrepareDiscoveredDocumentListAsync() : retrieve the list of discovered files from invariant as a CSV. See Retrieve the list of discovered files from invariant as a CSV

- PivotOnDiscoveredDocumentsAsync() : retrieves filtered discovered documents on pivot in a specific workspace. See Pivot on discovered documents .

- DownloadDiscoveredDocumentListAsync() : download a csv listing of discovered files. See Download a csv listing of discovered files .

- GetFiltersByDataSourceAsync() : retrieves processing filters available for a specific data source. See Retrieve processing filters for a data source .

- GetFilterResultAsync() : retrieves data that matches the filter criteria. Its only parameter is a GetProcessingFilterResultRequest object, and it returns a ProcessingFilterData object. See Retrieve filtered data .

- GetFiltersAsync() : retrieves processing filters available in a specific workspace. See Retrieve processing filters .

- UpdateExpressionFilterAsync() : modifies the properties of a processing filter, such as the expression used for filtering. See Update a processing filter .

### Classes and enumerations

Relativity.Processing.Services.Interfaces.DTOs namespace contains the following classes and enumerations used by the Processing Filter Manager API. The following list highlights several of the classes and enumerations in this namespace. For a complete list, see Class library reference in the Class library reference .

#### Classes used for requests and responses

- ApplyProcessingFilterRequest class - represents the processing filter used on a data set. The ApplyFilterAsync() method takes an object of this type. Its properties include the filter ID, Artifact ID of the workspace, and the priority for the job.

- CreateProcessingExpressionFilterRequest class - represents the data used to create a processing filter. The CreateExpressionFilterAsync() method takes an object of this type. Its properties include the Artifact IDs of the workspace and data source for the filter, the filter name, and others.

- DeleteFilterRequest class - represents the processing filter to remove from Relativity. The DeleteFilterAsync() method takes an object of this type. Its properties include the Artifact ID of the workspace and the filter ID.

- ProcessingMetadataRequest class - represents a workspace containing the metadata fields and values for a specific document. The GetDocumentMetadataAsync() method takes an object of this type. Its properties include the Artifact ID of the workspace and the Processing file ID of the document.

- GetDiscoveredDocumentsRequest class - represents a workspace containing discovered documents. The GetDiscoveredDocumentsAsync() method takes an object of this type. Its properties include the Artifact ID of the workspace and data source for the filter.

- GetProcessingFiltersByDataSourceRequest class - represents a data source associated with processing filters. The GetFilterByDataSourceAsync() method takes an object of this type. Its properties include the Artifact IDs of the workspace and data source.

- GetProcessingFilterResultRequest class - represents a workspace containing processing filters. The GetFiltersAsync() method takes an object of this type. Its only property is the Artifact ID of the workspace.

- GetDiscoveredDocumentsWithPivotOnRequest class - represents a workspace containing discovered documents on pivot. The PivotOnGetDiscoveredDocumentsAsync() method takes an object of this type. Its properties include the Artifact ID of the workspace and pivot on options.

- ProcessingFilter class - represents information used to identify a filter. The CreateExpressionFilterAsync(), GetFilterByDataSourceAsync(), GetFiltersAsync(), and UpdateExpressionFilterAsync() methods return an object of this type. Its properties include the name, identifier, and type of the filter.

- ProcessingFilterData class - represents the result set returned after data is filtered. The ApplyFilterAsync() method takes an object of this type. Its properties include the filter ID, the result set, and the total count of items in the result set.

- UpdateProcessingExpressionFilterRequest class - represents the data used to modify a processing filter. The UpdateExpressionFilterAsync() method takes an object of this type. Its properties include the Artifact IDs of the workspace and data source for the filter, the filter name, and others.

#### Classes and enumerations for building expressions

- ProcessingFilterCompositeExpression class - represents an expression created by combining several shorter expressions using the AND and OR operators.

- ProcessingFilterConditionalExpression class - represents an expression created by using Boolean conditions. See Expression types .

- ProcessingFilterConstraint enumeration - provides operators for use with Boolean conditions, such as Is, IsNot, and others. See Operators .

- ProcessingFilterOperator enumeration - provides operators for combining expressions, including AND and OR. See Operators .

- ProcessingFilterEmptyExpression class - provides an empty object for creating an expression. See Expression types .

- Property enumeration - provides a list of properties for evaluating an expression. See Properties .

## Guidelines for the Processing Filter Manager API

Review the following guidelines for working with the Processing Filter Manager API.

### Access rights

Verify that you have access to the workspace where you want make calls to the Processing Filter Manager service.

### Helper methods

Use the GetFilterByDataSourceAsync() or GetFiltersAsync() helper methods to get the name, identifier, and type for a filter. See Retrieve processing filters or Retrieve processing filters for a data source .

### Filter expressions

To create or update a processing filter, use the expression types, operators, and properties supported by the Processing Filter Manager service for this purpose. For more information about expression classes and enumerations, see the Relativity.Processing.Services.Interfaces.DTOs namespace for the Class library reference .

#### Expression types

You can find examples of expression types in Create a processing filter .

The following types of expressions are supported:

- Composite expression - several shorter expressions that are combined by using the AND and OR operators. To create this expression type, instantiate a ProcessingFilterCompositeExpression object by setting the following properties:

- Expressions - an array of expressions to be combined. See IProcessingFilterExpressionModel interface in the Class library reference .

- Operator - an operator used to combine expressions. See Operators .

- Conditional expression - expressions that use Boolean conditions for evaluation. To create this expression type, instantiate a ProcessingFilterConditionalExpression object by setting the following properties:

- Property - a property used for filtering. See Properties .

- Constraint - an operator used to evaluate a property against a specified value. See Operators .

- Value - a string compared to a property.

- Empty expression - an empty expression object used to create expressions. See the ProcessingFilterEmptyExpression class in the Class library reference .

#### Operators

The Relativity.Processing.Services.Interfaces.DTOs namespace includes the following enumerations for operators supported in expressions:

- Constraint operators - The ProcessingFilterConstraint enumeration supports the following operators: Is, IsNot, IsIn, and IsNotIn.

- Composite operators - The ProcessingFilterOperator enumeration supports the following operators: AND and OR.

#### Properties

The Property enumeration provides a list of properties supported for use in expressions.

- ContainerExtension

- ContainerFileId

- ContainerName

- DocumentError

- FileExtension

- FileName

- FileType

- OriginalPath

- ParentDocumentId

- ProcessingFileId

- ProcessingFolderPath

- SourcePath

- StorageError

- StorageId

- TextExtractionMethod

- VirtualPath

## Create a processing filter

To create or update a processing filter, you need to create an expression object that is referenced by the request object passed to the CreateExpressionFilterAsync() method.

The following code samples illustrate how to create a request object for each type of expression. For more information, see Filter expressions .

- Method

-

CreateExpressionFilterAsync

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- CreateProcessingExpressionFilterRequest object

- <string> FilterName: Name of the expression filter.

- <List<int>>DataSourceIDs: The DataSourceIDs of the jobs where the filters needs to be created on.

- <string>Expression: Specifies the expression use to create the expression filter.

- <bool>IncludeFamily: Specifies if the result of the filter should contain the family.

- Returns

- ProcessingFilter object

- <long>FilterID: The filter Id for the filter

- <string> FilterName: The filter name for the filter.

- <string>Type: The filter type for the filter

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
CreateProcessingExpressionFilterRequest request = new CreateProcessingExpressionFilterRequest() {

  FilterName = "Hello World Filter Name",

    DataSourceIDs = new List<int>{

      123

    },

    Expression = "{\"Type\": \"ProcessingFilterConditionalExpression\", \"Property\": \"ProcessingFileID\", \"Constraint\": \"IsNot\", \"Value\": 123}",

    IncludeFamily = true

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy < IProcessingFilterManager > (ExecutionIdentity.CurrentUser)) {

  ProcessingFilter filter = await proxy.CreateExpressionFilterAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

## Apply a processing filter

Use the ApplyFilterAsync() method to apply a processing filter to a data set. The following code sample illustrates how to instantiate a ApplyProcessingFilterRequest object containing the Artifact ID of the workspace, filter ID, and a job priority. The request object is then passed to the ApplyFilterAsync() method, which returns a job ID.

- Method

- ApplyFilterAsync

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <long> filterID: Filter ID of the filter to apply.

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

- ApplyProcessingFilterRequest object

- <int>Priority: priority of the job

- Returns

- <long>: the jobId to which the filter was applied

Copy

```text
1
2
3
4
5
6
ApplyProcessingFilterRequest request = new ApplyProcessingFilterRequest() {

  Priority = 90

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  long jobId = await proxy.ApplyFilterAsync(data.WorkspaceId, filterID, request).ConfigureAwait(false);

}
```

## Update a processing filter

To update a processing filter, instantiate an UpdateProcessingExpressionFilterRequest object, and pass it to the UpdateExpressionFilterAsync() method, which returns a a ProcessingFilter object containing the name, identifier, and type of the filter. For more information, see Filter expressions .

- Method

- UpdateExpressionFilterAsync: Updates an expression filter

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <long> filterID: Filter ID of the filter to update.

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

- UpdateProcessingExpressionFilterRequest object

- <string> FilterName: Name of the expression filter.

- <List<int>>DataSourceIDs: The DataSourceIDs of the jobs where the filters needs to be created on.

- <string>Expression: Specifies the expression use to create the expression filter.

- <bool>IncludeFamily: Specifies if the result of the filter should contain the family

- Returns

- ProcessingFilter object

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
UpdateProcessingExpressionFilterRequest request = new UpdateProcessingExpressionFilterRequest() {

    FilterName = "Hello World Filter Name",

    DataSourceIDs = new List<int>{

      123

    },

    Expression = "{\"Type\": \"ProcessingFilterConditionalExpression\", \"Property\": \"ProcessingFileID\", \"Constraint\": \"IsNot\", \"Value\": 123}",

    IncludeFamily = true

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  ProcessingFilter filter = await proxy.UpdateExpressionFilterAsync(data.WorkspaceId, filterID, request).ConfigureAwait(false);

}
```

## Delete a processing filter

To remove a processing filter, instantiate a DeleteFilterRequest object containing the Artifact ID of the workspace, and the filter ID, and then pass this request to the DeleteFilterAsync() method.

- Method

- DeleteFilterAsync

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <long> filterID: Filter ID from which the result is retrieved.

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

Copy

```text
1
2
3
using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

    await proxy.DeleteFilterAsync(data.WorkspaceId, filterID).ConfigureAwait(false);

}
```

## Retrieve discovered documents

After you apply a processing filter, you can use the GetDiscoveredDocumentsAsync() method to retrieve discovered documents.

- Method

- GetDiscoveredDocumentsAsync: Get discovered documents

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- GetDiscoveredDocumentsRequest object

- <int> StartingPointOfResult: Starting point to return rows from a result set.

- <int>NumberOfResults: Count of rows after startingpoint to get in result set.

- <string>Expression: Specifies the expression use to create the expression filter.

- <int>AuditedSourceID: The view or saved filter ID for auditing.

- <List<SortingOption>> SortingOptions: A list of sorting priority to which get applied upon result retrieval.

- Property: enum of properties to sort on

- Ordering: enum of ordering directions, Ascending or Descending

- <bool>ExcludeTotalCount: Whether or not to calculate the total size of the discovered documents returned

- Returns

- ProcessingFilterData object

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
GetDiscoveredDocumentsRequest request = new GetDiscoveredDocumentsRequest() {

  Expression =

    "{\"Type\":\"ConditionalExpression\",\"Property\":\"FileExtension\",\"Constraint\":\"15\",\"Value\":\"European\"}",

    StartingPointOfResult = 0,

    NumberOfResults = 1,

    SortingOptions = new List<SortOption>{

      new SortOption() {

        Property = Property.FileName,

          Order = Ordering.Ascending

      }

    },

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  ProcessingFilterData response = await proxy.GetDiscoveredDocumentsAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

## Retrieve discovered document IDs

After you apply a processing filter, you can use the GetDiscoveredDocumentIdsAsync() method to retrieve the Ids of discovered documents.

- Method

- GetDiscoveredDocumentIdsAsync: Get discovered document IDs

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- GetDiscoveredDocumentsRequest object

- <int> StartingPointOfResult: Starting point to return rows from a result set.

- <int>NumberOfResults: Count of rows after startingpoint to get in result set.

- <string>Expression: Specifies the expression use to create the expression filter.

- <int>AuditedSourceID: The view or saved filter ID for auditing.

- <List<SortingOption>> SortingOptions: A list of sorting priority to which get applied upon result retrieval.

- Property: enum of properties to sort on

- Ordering: enum of ordering directions, Ascending or Descending

- <bool>ExcludeTotalCount: Whether or not to calculate the total size of the discovered documents returned

- Returns

- ProcessingFileIdResults object

- <long>FilterID

- <int>TotalCount: Total result count for a filter.

- <List<long>>Results: File ids (from the Invariant Matter table)

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
GetDiscoveredDocumentsRequest request = new GetDiscoveredDocumentsRequest() {

  Expression =

    "{\"Type\":\"ConditionalExpression\",\"Property\":\"FileExtension\",\"Constraint\":\"15\",\"Value\":\"European\"}",

    StartingPointOfResult = 0,

    NumberOfResults = 1,

    SortingOptions = new List<SortOption>{

      new SortOption() {

        Property = Property.ContainerName,

          Order = Ordering.Descending

      }

    },

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  ProcessingFileIdResults results = await proxy.GetDiscoveredDocumentIdsAsync(data.WorkspaceId, request).ConfigureAwait(false);

}            }
```

## Retrieve the list of discovered files from invariant as a CSV

- Method

- PrepareDiscoveredDocumentListAsync: Creates a request to get the list of discovered files from invariant as a CSV

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- • GetDiscoveredDocumentListRequest object

- <string>Expression

- <long[]>FileIDs

- <List<ExportColumn>> Columns: Column to be included in an exported CSV file

- <enum>Property: The property value to include in this column of exported CSV data

- <string>Header: The column header to include in the CSV for this property

- <List<SortingOption>> SortingOptions: A list of sorting priority to which get applied upon result retrieval.

- Property: enum of properties to sort on

- Ordering: enum of ordering directions, Ascending or Descending

- Returns

- PrepareDiscoveredDocumentListResponse object

- <Guid>Guid - The Guid used to retrieve the Discovered File List

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
GetDiscoveredDocumentListRequest request = new GetDiscoveredDocumentListRequest {

  Columns = new List<ExportColumn>{

      new ExportColumn {

        Header = "Id",

          Property = Property.ProcessingFileId

      }

    },

    Expression = string.Empty,

    FileIDs = new long[] {

      1

    }

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  PrepareDiscoveredDocumentListResponse response = await proxy.PrepareDiscoveredDocumentListAsync(data.WorkspaceId, request).ConfigureAwait(false);

}        }
```

## Retrieve filtered data

After you apply a processing filter, you can use the GetFilterResultAsync() method to retrieve the filtered data.

- Method

- GetFilterResultAsync: Get Filter Result

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <long>filterID: Filter ID from which the result is retrieved.

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

- <int>skip: Starting point to return rows from a result set.

- <int>top: Count of rows after starting point to get in result set

- Returns

- ProcessingFilterData object

- <long>FilterID.

- <int>TotalCount: Total result count for a filter.

- Results – list of ProcessingFilterResult objects with multiple properties including ContainerName, CustodianName, DiscoverGroupId, and more

Copy

```text
1
2
3
using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  ProcessingFilterData response = await proxy.GetFilterResultAsync(data.WorkspaceId, filterID, 0, 10).ConfigureAwait(false);

}
```

## Retrieve processing filters

You can retrieve all available processing filters for a specific workspace. The following code sample illustrates how to instantiate a GetProcessingFiltersRequest instance with the Artifact ID of a specific workspace. It shows how to call the GetFiltersAsync() method by passing the request object to it. This method returns a ProcessingFilter object, which has properties for the name, identifier, and type of the filter.

- Method

- GetFiltersAsync: Get Filters from invariant

- Parameters

- <int>workspaceID: The workspace artifact identifier

- Returns

-

List of ProcessingFilter objects

Copy

```text
1
2
3
using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  List<ProcessingFilter> filters = await proxy.GetFiltersAsync(data.WorkspaceId).ConfigureAwait(false);

}
```

## Retrieve processing filters for a data source

You can retrieve processing filters for a specific data source. This method returns a list of ProcessingFilter object, which has properties for the name, identifier, and type of the filter.

- Method

- GetFiltersByDataSourceAsync: Get Filter Result

- Parameters

- <int>workspaceID : The workspace artifact identifier.

- <int> dataSourceID: The Artifact ID of the processing data source to get filters from

- Returns

- List of ProcessingFilter objects

Copy

```text
1
2
3
4
using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser))

{

    List<ProcessingFilter> filters = await proxy.GetFiltersByDataSourceAsync(data.WorkspaceId, dataSourceId).ConfigureAwait(false);

}
```

## Pivot on discovered documents

After you apply a processing filter, you can use the PivotOnDiscoveredDocumentsAsync() method to retrieve filtered discovered documents on pivot.

- Method

- PivotOnDiscoveredDocumentsAsync: Get discovered documents with pivot on

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- GetDiscoveredDocumentsWithPivotOnRequest object

- <string>Expression

- PivotOnOption object: Group by options use to set group by conditions.

- <Property enum> GroupByProperty: Name of the property to perform group by on.

- <Ordering enum> GroupByOrdering: Sort order of group by condition.

- <int>GroupByCount: Group by count used to select number of top or bottom rows of the condition. Default value 0

- <Property enum> PivotOnProperty: Name of the property to perform pivot.

- <Ordering enum> PivotOnOrdering: Sort order of pivot on ordering condition.

- <int>PivotOnCount: Pivot On count used to select number of top or bottom rows of the condition. Default value 0

- Returns

- List of GetDiscoveredDocumentsWithPivotOnResponse objects

- <string>GroupByIdentifier: Value of the property that is group by.

- <string>PivotOnIdentifier: Value of the property that is pivot on identifier.

- <int>ResultCount: Count of each property

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
GetDiscoveredDocumentsWithPivotOnRequest request = new GetDiscoveredDocumentsWithPivotOnRequest() {

  Expression = "{\"Type\" : \"ConditionalExpression\", \"Property\" : \"FileId\", \"Constraint\" : \"IsNot\", \"Value\" : 123}",

    PivotOnOption = new PivotOnOption() {

      GroupByProperty = Property.ProcessingFileId,

        GroupByOrdering = Ordering.Descending,

        GroupByCount = 10

    }

};

using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser)) {

  List < GetDiscoveredDocumentsWithPivotOnResponse > response = await proxy.PivotOnDiscoveredDocumentsAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

## Download a csv listing of discovered files

- Method

- DownloadDiscoveredDocumentListAsync: Downloads a csv listing of discovered files based on a request submitted earlier

- Parameters

- <int>workspaceID: Id of the workspace for which the request was defined.

- <Guid>requestGuid: Guid of a request as defined by PrepareDiscoveredDocumentListAsync

- Returns

- IKeplerStream object for downloaded file(s)

Copy

```text
1
2
3
4
5
6
using (IProcessingFilterManager proxy = _servicesMgr.CreateProxy<IProcessingFilterManager>(ExecutionIdentity.CurrentUser))

using (IKeplerStream download = await proxy.DownloadDiscoveredDocumentListAsync(data.WorkspaceId, downloadGuid).ConfigureAwait(false))

using (Stream stream = await download.GetStreamAsync().ConfigureAwait(false))

using (var localStream = new MemoryStream()) {

  await stream.CopyToAsync(localStream).ConfigureAwait(false);

}        }
```

On this page

- Processing Filter Manager

- Fundamentals for the Processing Filter Manager API

- Methods

- Classes and enumerations

- Guidelines for the Processing Filter Manager API

- Access rights

- Helper methods

- Filter expressions

- Create a processing filter

- Apply a processing filter

- Update a processing filter

- Delete a processing filter

- Retrieve discovered documents

- Retrieve discovered document IDs

- Retrieve the list of discovered files from invariant as a CSV

- Retrieve filtered data

- Retrieve processing filters

- Retrieve processing filters for a data source

- Pivot on discovered documents

- Download a csv listing of discovered files


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
