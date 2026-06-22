---
title: "Processing Filter Manager (.NET v0)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/v0/Processing_Filter_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:35+00:00
sha256: 6c5efbdd3b23db22f6bc02a04aae730159f01d41df195acc416350233ca40865
---

Processing Filter Manager (.NET v0)

# Processing Filter Manager (.NET v0)

This content refers to Version 0 of the Processing APIs. For documentation on the latest version of this API, see Get started with the Processing SDK

Processing filters provide functionality to view and select processed documents before publishing them to Relativity. The Processing Filter Manager API exposes methods for programmatically creating, updating, and deleting filters. It supports applying these filters to data and retrieving the filtered data. Additionally, this service exposes helper methods for retrieving filters associated with a data source or available in a specific workspace. For more general information, see Filtering data .

As a sample use case, you may want to implement a simplified processing workflow by programmatically adding complex criteria to filters applied to processing jobs in Relativity. This approach eliminates the need to manually enter filter criteria through the UI, which may be time consuming and error prone. Similarly, you can also use the Processing Filter Manager service to modify the settings on these or other complex filters implemented in your environment.

The Processing Filter Manager service also supports the same functionality through REST. For more information, see Processing Filter Manager (REST v0) .

## Fundamentals for the Processing Filter Manager API

Review the following information to learn about the methods, classes, and enumerations used by the Processing Filter Manager service.

### Methods

The Relativity.Processing.Services namespace contains the IProcessingFilterManager interface that exposes the following methods:

- ApplyFilterAsync() method - applies a processing filter to the specified data set in a workspace. Its only parameter is an ApplyProcessingFilterRequest object, and it returns the ID of the filtering job. See Apply a processing filter .

- CreateExpressionFilterAsync() method - adds a new processing filter to Relativity. Its only parameter is a CreateProcessingExpressionFilterRequest object, and it returns a ProcessingFilter object. See Create a processing filter .

- DeleteFilterAsync() method - removes a processing filter from Relativity. Its only parameter is a DeleteFilterRequest object, and it returns a Task. See Delete a processing filter .

- GetDocumentMetadataAsync() method - retrieves all metadata fields and values for a specific document. Its only parameter is a ProcessingMetadataRequest object, and it returns a ProcessingMetadataResponse object. See Retrieve document metadata.

- GetDiscoveredDocumentsAsync() method - retrieves discovered documents in a specific workspace. Its only parameter is a GetDiscoveredDocumentsRequest object, and it returns a ProcessingFilterData object. See Retrieve discovered documents .

- GetFilterByDataSourceAsync() method - retrieves processing filters available for a specific data source. Its only parameter is a GetProcessingFiltersByDataSourceRequest object, and it returns a list of ProcessingFilter objects. See Retrieve processing filters for a data source .

- GetFilterResultAsync() method - retrieves data that matches the filter criteria. Its only parameter is a GetProcessingFilterResultRequest object, and it returns a ProcessingFilterData object. See Retrieve filtered data .

- GetFiltersAsync() method - retrieves processing filters available in a specific workspace. Its only parameter is a GetProcessingFiltersRequest object, and it returns a list of ProcessingFilter objects. See Retrieve processing filters .

- PivotOnDiscoveredDocumentsAsync() method - retrieves filtered discovered documents on pivot in a specific workspace. Its only parameter is a GetDiscoveredDocumentsWithPivotOnRequest object, and it returns a list of GetDiscoveredDocumentsWithPivotOnResponse objects. See Pivot on discovered documents .

- UpdateExpressionFilterAsync() method - modifies the properties of a processing filter, such as the expression used for filtering. Its only parameter is anUpdateProcessingExpressionFilterRequest object, and it returns a ProcessingFilter object. See Update a processing filter .

### Classes and enumerations

Relativity.Processing.Services.Interfaces.DTOs namespace contains the following classes and enumerations used by the Processing Filter Manager API. The following list highlights several of the classes and enumerations in this namespace. For a complete list, see Class library reference in the Class library reference .

Classes used for requests and responses

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

Classes and enumerations for building expressions

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

View supported properties

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

- Composite expression View code sample Copy

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
CreateProcessingExpressionFilterRequest processingExpressionFilterRequest = new CreateProcessingExpressionFilterRequest

{

    WorkspaceArtifactId = workspaceArtifactId,

    FilterName = "NameOfTheFilter",

    DataSourceArtifactIDs = processingDataSourceId,

    Expression = JsonConvert.SerializeObject(new ProcessingFilterCompositeExpression()

        {

            Expressions = new IExpressionModel[]

            {

                new ProcessingFilterConditionalExpression()

                {

                    Property = Property.FileId,

                    Constraint = Constraint.Is,

                    Value = "1"

                },

                new ProcessingFilterConditionalExpression()

                {

                    Property = Property.FileId,

                    Constraint = Constraint.Is,

                    Value = "2"

                }

            },

            Operator = Operator.Or

        }),

    IncludeFamily = true

};
```

- Conditional expression View code sample Copy

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
CreateProcessingExpressionFilterRequest processingExpressionFilterRequest = new CreateProcessingExpressionFilterRequest

{

    WorkspaceArtifactId = workspaceArtifactId,

    FilterName = "NameOfTheFilter",

    DataSourceArtifactIDs = processingDataSourceId,

    Expression = JsonConvert.SerializeObject(new ProcessingFilterConditionalExpression()

    {

        Property = Property.ProcessingFileId,

        Constraint = ProcessingFilterConstraint.Is,

        Value = "1"

    }),

    IncludeFamily = true

};
```

- Empty expression View code sample Copy

```text
1
2
3
4
5
6
7
8
CreateProcessingExpressionFilterRequest processingExpressionFilterRequest = new CreateProcessingExpressionFilterRequest

{

    WorkspaceArtifactId = workspaceArtifactId,

    FilterName = "NameOfTheFilter",

    DataSourceArtifactIDs = processingDataSourceId,

    Expression = JsonConvert.SerializeObject(new ProcessingFilterEmptyExpression())

    IncludeFamily = true

};
```

View complete code sample for creating a filter Copy

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
public async Task<bool> ProcessingFilterManager_Create_Async(IHelper helper, int workspaceArtifactId, int[] processingDataSourceId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            //Build the processingExpressionFilterRequest object.

            CreateProcessingExpressionFilterRequest processingExpressionFilterRequest = new CreateProcessingExpressionFilterRequest

            {

                WorkspaceArtifactId = workspaceArtifactId,

                FilterName = "NameOfTheFilter",

                DataSourceArtifactIDs = processingDataSourceId,

                Expression = JsonConvert.SerializeObject(new ProcessingFilterConditionalExpression()

                {

                    Property = Property.ProcessingFileId,

                    Constraint = ProcessingFilterConstraint.Is,

                    Value = "1"

                }),

                IncludeFamily = true

            };

            //Create the processingFilter object. The service returns the the whole object including the id.

            ProcessingFilter processingFilter = await proxy.CreateExpressionFilterAsync(processingExpressionFilterRequest);

            if (processingFilter.FilterId != 0)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_Create_Async), "Create failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_Create_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```

## Apply a processing filter

Use the ApplyFilterAsync() method to apply a processing filter to a data set. The following code sample illustrates how to instantiate a ApplyProcessingFilterRequest object containing the Artifact ID of the workspace, filter ID, and a job priority. The request object is then passed to the ApplyFilterAsync() method, which returns a job ID.

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

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
public async Task<bool> ProcessingFilterManager_ApplyFilter_Async(IHelper helper, int workspaceArtifactId, long filterId, int priority)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            //Build the processingExpressionFilterRequest object.

            ApplyProcessingFilterRequest processingApplyFilterRequest = new ApplyProcessingFilterRequest

            {

                WorkspaceArtifactId = workspaceArtifactId,

                FilterId = filterId,

                Priority = priority

            };

            //Returns a to which the filter was applied.

            long jobId = await proxy.ApplyFilterAsync(processingApplyFilterRequest);

            if (jobId != 0)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_ApplyFilter_Async), "Apply filter failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_ApplyFilter_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```

## Update a processing filter

To update a processing filter, instantiate an UpdateProcessingExpressionFilterRequest object, and pass it to the UpdateExpressionFilterAsync() method, which returns a a ProcessingFilter object containing the name, identifier, and type of the filter. For more information, see Filter expressions .

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

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
public async Task<bool> ProcessingFilterManager_Update_Async(IHelper helper, int workspaceArtifactId, int[] processingDataSourceId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            //Build the processingExpressionFilterRequest object.

            UpdateProcessingExpressionFilterRequest processingExpressionFilterRequest = new UpdateProcessingExpressionFilterRequest

            {

                WorkspaceArtifactId = workspaceArtifactId,

                FilterName = "NameOfTheFilter",

                DataSourceArtifactIDs = processingDataSourceId,

                Expression = JsonConvert.SerializeObject(new ProcessingFilterConditionalExpression()

                {

                    Property = Property.ProcessingFileId,

                    Constraint = ProcessingFilterConstraint.Is,

                    Value = "1"

                }),

                IncludeFamily = true

            };

            //Create the processingFilter object. The service returns the the whole object including the id.

            ProcessingFilter processingFilter = await proxy.UpdateExpressionFilterAsync(processingExpressionFilterRequest);

            if (processingFilter.FilterId != 0)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_Update_Async), "Update failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_Update_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```

## Delete a processing filter

To remove a processing filter, instantiate a DeleteFilterRequest object containing the Artifact ID of the workspace, and the filter ID, and then pass this request to the DeleteFilterAsync() method.

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

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
public async Task ProcessingFilterManager_DeleteFilterAsync_Async(IHelper helper, int workspaceArtifactId, long filterId)

{

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        //Build the DeleteFilterRequest Dto.

        DeleteFilterRequest request = new DeleteFilterRequest

        {

            WorkspaceArtifactId = workspaceArtifactId,

            FilterId = filterId

        };

        // Delete filter

        await proxy.DeleteFilterAsync(request);

    }

}
```

## Retrieve document metadata

You can retrieve available metadata for a specific document. The following code sample illustrates how to instantiate a ProcessingMetadataRequest instance with the Artifact ID of a specific workspace and Processing file ID of the document. It shows how to call the GetDocumentMetadataAsync() method by passing the request object to it. This method returns a ProcessingMetadataResponse object. For brief descriptions of the data fields on this object, see Processing Filter Manager (REST v0) in the Processing Filter Manager (REST v0) .

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

                <p>public async Task<bool> GetDocumentMetadataAsync_Async(IHelper helper, int workspaceArtifactId, long processingFileId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingDocumentManager proxy = helper.GetServicesManager().CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.User))

    {

        try

        {

            ProcessingMetadataRequest processingMetadataRequest = new ProcessingMetadataRequest

            {

                WorkspaceArtifactId = workspaceArtifactId,

                ProcessingFileId = processingFileId

            };

            ProcessingMetadataResponse processingMetadataResponse = await proxy.GetDocumentMetadataAsync(processingMetadataRequest);

            if (processingMetadataResponse.ProcessingFileId != 0)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(GetDocumentMetadataAsync_Async), "Get Document Metadata failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(GetDocumentMetadataAsync_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}</p>

```

## Retrieve discovered documents

After you apply a processing filter, you can use the GetDiscoveredDocumentsAsync() method to retrieve discovered documents.

The following code sample illustrates how to instantiate a GetDiscoveredDocumentsRequest instance with the Artifact ID of a specific workspace, the number of rows in the result set to return and the sorting property, order, and starting index for these rows. It shows how to call the GetDiscoveredDocumentsAsync method by passing the request object to it.

This method returns a ProcessingFilterData object. For brief descriptions of the data fields on this object, see Retrieve discovered documents in the Processing Filter Manager (REST v0) .

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

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

                <p>public async Task <bool> ProcessingFilterManager_GetDiscoveredDocuments_Async(IHelper helper, int workspaceId, int dataSourceId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy <IProcessingFilterManager> (ExecutionIdentity.User))

    {

        try

            {

                GetDiscoveredDocumentsRequest request = new GetDiscoveredDocumentsRequest()

                {

                    WorkspaceArtifactId = workspaceId,

                    StartingPointOfResult = 0,

                    NumberOfResults = 100,

                    Expression = JsonConvert.SerializeObject(new ProcessingFilterConditionalExpression()

                    {

                        Property = Property.ProcessingFileId,

                        Constraint = ProcessingFilterConstraint.IsNot,

                        Value = "1"

                    }),

                    SortingOptions = new []

                    {

                        new SortOption()

                        {

                            Property = Property.FileName,

                            Order = Ordering.Ascending

                        }

                    },

                };

                ProcessingFilterData filterData = await proxy.GetDiscoveredDocumentsAsync(request);

                if (filterData.TotalCount >= 1)

                {

                    success = true;

                }

                else

                {

                    Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetDiscoveredDocuments_Async), "Get discovered documents failed", this.GetType().Name);

                }

            }

            catch (ServiceException exception)

            {

                //The service returns exceptions of type ServiceException.

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetDiscoveredDocuments_Async), exception.Message, this.GetType().Name);

                throw;

            }

        }

        return success;

}        </p>

```

## Retrieve filtered data

After you apply a processing filter, you can use the GetFilterResultAsync() method to retrieve the filtered data.

The following code sample illustrates how to instantiate a GetProcessingFilterResultRequest instance with the Artifact ID of a specific workspace, the identifier for a filter, the number of rows in the result set to return, and the starting index for these rows. It shows how to call the GetFilterResultAsync method by passing the request object to it.

This method returns a ProcessingFilterData object. For brief descriptions of the data fields on this object, see Retrieve filtered data in the Processing Filter Manager (REST v0) .

You can obtain the identifier for a filter by calling the GetFilterByDataSourceAsync() or GetFiltersAsync() methods. See Retrieve processing filters or Retrieve processing filters for a data source .

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
public async Task<bool> ProcessingFilterManager_GetFilterResultAsync_Async(IHelper helper, int workspaceArtifactId, long filterId, int startingPoint, int numberOfResults)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            //Build the GetProcessingFilterResultRequest Dto.

            GetProcessingFilterResultRequest getProcessingFilterResultRequest = new GetProcessingFilterResultRequest

            {

                WorkspaceArtifactId = workspaceArtifactId,

                FilterId = filterId,

                StartingPointOfResult = startingPoint,

                NumberOfResults = numberOfResults

            };

            //Returns an object processingFilterData with filter results.

            ProcessingFilterData processingFilterData = await proxy.GetFilterResultAsync(getProcessingFilterResultRequest);

            if (processingFilterData != null)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetFilterResultAsync_Async), "Get filter results failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetFilterResultAsync_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```

## Retrieve processing filters

You can retrieve all available processing filters for a specific workspace. The following code sample illustrates how to instantiate a GetProcessingFiltersRequest instance with the Artifact ID of a specific workspace. It shows how to call the GetFiltersAsync() method by passing the request object to it. This method returns a ProcessingFilter object, which has properties for the name, identifier, and type of the filter.

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
public async Task<bool> ProcessingFilterManager_GetFilters_Async(IHelper helper, int workspaceId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (

        IProcessingFilterManager proxy =

        helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            GetProcessingFiltersRequest request = new GetProcessingFiltersRequest()

            {

                WorkspaceArtifactId = workspaceId

            };

            List<ProcessingFilter> filters = await proxy.GetFiltersAsync(request);

            if (filters.Count >= 1)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetFilters_Async), "Get failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetFilters_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```

## Retrieve processing filters for a data source

You can retrieve processing filters for a specific data source. The following code sample illustrates how to instantiate a GetProcessingFiltersByDataSourceRequest instance with the Artifact IDs of the workspace and the data source. It shows how to call the GetFilterByDataSourceAsync() method by passing it this request object. This method returns a ProcessingFilter object, which has properties for the name, identifier, and type of the filter.

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
public async Task<bool> ProcessingFilterManager_GetFilterByDataSource_Async(IHelper helper, int workspaceId, int dataSourceId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (

        IProcessingFilterManager proxy =

            helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            GetProcessingFiltersByDataSourceRequest request = new GetProcessingFiltersByDataSourceRequest()

            {

                WorkspaceArtifactId = workspaceId,

                DataSourceArtifactId = dataSourceId

            };

            List<ProcessingFilter> filters = await proxy.GetFilterByDataSourceAsync(request);

            if (filters.Count >= 1)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetFilterByDataSource_Async), "Get filters by datasource failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_GetFilterByDataSource_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```

## Pivot on discovered documents

After you apply a processing filter, you can use the PivotOnDiscoveredDocumentsAsync() method to retrieve filtered discovered documents on pivot.

The following code sample illustrates how to instantiate a GetDiscoveredDocumentsWithPivotOnRequest instance with the Artifact ID of a specific workspace, group by options, and pivot on options. It shows how to call the PivotOnDiscoveredDocumentsAsync method by passing the request object to it.

This method returns a list of GetDiscoveredDocumentsWithPivotOnResponse objects. For brief descriptions of the data fields on this object, see Pivot on discovered documents in the Processing Filter Manager (REST v0) .

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
public async Task<bool> ProcessingFilterManager_PivotOnGetDiscoveredDocuments_Async(IHelper helper, int workspaceId)

{

    bool success = false;

    //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

    //agents, and custom Pages. They are mocked in these samples.

    //This sample code executes under the context of the current user.

    using (IProcessingFilterManager proxy = helper.GetServicesManager().CreateProxy<IProcessingFilterManager>(ExecutionIdentity.User))

    {

        try

        {

            GetDiscoveredDocumentsWithPivotOnRequest getDiscoveredDocumentsRequest = new GetDiscoveredDocumentsWithPivotOnRequest

            {

                WorkspaceArtifactId = workspaceId,

                Expression = JsonConvert.SerializeObject(new ProcessingFilterConditionalExpression()

                {

                    Property = Property.FileSize,

                    Constraint = ProcessingFilterConstraint.IsGreaterThanOrEqualTo,

                    Value = "1"

                }),

                PivotOnOption = new PivotOnOption()

                {

                    GroupByProperty = Property.FileExtension,

                    GroupByCount = 0,

                    GroupByOrdering = Ordering.Descending,

                    PivotOnProperty = Property.FileType,

                    PivotOnCount = 100,

                    PivotOnOrdering = Ordering.Ascending

                }

            };

            List<GetDiscoveredDocumentsWithPivotOnResponse> response = await proxy.PivotOnDiscoveredDocumentsAsync(getDiscoveredDocumentsRequest);

            if (response.Count >= 1)

            {

                success = true;

            }

            else

            {

                Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_PivotOnGetDiscoveredDocuments_Async), "Get discovered documents on pivot failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //The service returns exceptions of type ServiceException.

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingFilterManager_PivotOnGetDiscoveredDocuments_Async), exception.Message, this.GetType().Name);

            throw;

        }

    }

    return success;

}
```
