---
title: "Workspace Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Workspace_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:22:54+00:00
sha256: 5b5fbdd23f391f3f55c3e0206b1816619e66850cb2c6f30dbe804e56aabaa948
---

Workspace Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Workspace Manager (.NET)

In Relativity, a workspace acts as a secure data repository for documents. It supports customized views, layouts, fields, choices, and security settings. For more information, see Workspaces on the Relativity Documentation site.

The Workspace Manager API supports the following functionality:

- CRUD operations on workspaces.

- Helper methods for retrieving lists of available resources, such as matters, clients, and others.

- Helper methods for retrieving information about advanced settings, such as workspace statuses, full text languages for the SQL Server, and others.

- Helper methods for retrieving Azure credentials.

As a sample use case, you can simplify setting up reviews by using the Workspace Manager API to programmatically create multiple workspaces rather than manually adding them through the Relativity UI.

You can also use the Workspace Manager API through REST. For more information, see Workspace Manager service .

## Fundamentals for the Workspace Manager API

The Workspace Manager API contains the following methods and classes as described in this section.

### Methods

The Workspace Manager API exposes the following methods on the IWorkspaceManager interface in the Relativity.Environment.<VersionNumber>.Workspace namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

View methods

- CreateAsync() method - adds a new workspace to Relativity. This method takes a WorkspaceRequest object and returns a WorkspaceResponse object. See Create a workspace .

- DeleteAsync() method - removes a workspace from Relativity. This method takes the Artifact ID of a workspace. See Delete a workspace .

- GetDefaultDownloadHandlerURLAsync() method - retrieves the URL for the default download handler. This method returns a URL. See Retrieve the URL for the default download handler .

- GetEligibleAzureCredentialsAsync() method - retrieves a list of available Azure credentials for the workspace. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available credentials. See Retrieve Azure credentials .

- GetEligibleAzureFileSystemCredentialsAsync() method - retrieves a list of available Azure file system credentials. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available credentials. See Retrieve Azure file system credentials .

- GetEligibleCacheLocationsAsync() method - retrieves a list of available cache locations. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available cache locations. See Retrieve cache location servers .

- GetEligibleFileRepositoriesAsync() method - retrieves a list of available file repository servers. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available servers. See Retrieve file repository servers .

- GetEligibleResourcePoolsAsync() method - retrieves a list of resource pools. This method returns a list of DisplayableObjectIdentifier objects, which identify available resource pools. See Retrieve resource pools .

- GetEligibleSqlFullTextLanguagesAsync() method - retrieve available languages for a workspace. This method returns a list of SqlFullTextLanguageOptions objects, which describe the available and default languages. See Retrieve full text languages for SQL Server .

- GetEligibleSqlServersAsync() method - a list of SQL servers available for the workspace. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available SQL servers. See Retrieve SQL Servers

- GetEligibleStatusesAsync() method - retrieves a list of available statuses for a workspace. This method returns a list of DisplayableObjectIdentifier objects, which contain the Artifact ID, Name, and GUIDs identifying each status. See Retrieve available statuses for a workspace .

- GetMetaAsync() method - retrieves a list of unsupported WorkspaceRequest fields for a create operation. See Retrieve unsupported fields for a create operation .

- GetWorkspaceSummaryAsync() method - retrieves a summary of workspace statistics. This method takes the Artifact ID of the workspace as an argument and returns a WorkspaceSummary object. See Retrieve workspace statistics .

- QueryEligibleClientsAsync() method - retrieves a list of clients available for this workspace. This method takes a QueryRequest object, a start index, and the number of clients to include in the results. It returns a QueryResultSlim object with a list of available clients. See Retrieve clients .

- QueryEligibleGroupsAsync() method - retrieves a list of groups available for workspace membership. This method takes a QueryRequest object, a start index, and the number of groups to include in the results. It returns a QueryResultSlim object with a list of available groups. See Retrieve groups for workspace membership .

- QueryEligibleMattersAsync() method - retrieves a list of matters. This method takes a QueryRequest object, a start index, and the number of matters to include in the results. It returns a QueryResultSlim object with a list of available matters. See Retrieve matters .

- QueryEligibleSavedSearchesAsync() method - saved searches for use with production restrictions. This method takes a QueryRequest object, a start index, and the number of saved searches to include in the results. It returns a QueryResultSlim object with a list of available saved searches. See Retrieve saved searches for production restrictions .

- QueryEligibleTemplatesAsync() method - a list of workspaces for use as templates when creating a new workspace. This method takes a QueryRequest object, a start index, and the number of templates to include in the results. It returns a QueryResultSlim object with a list of available templates. See Retrieve workspaces for use as templates .

- QueryWorkspaceByGroupAsync() method - retrieves workspaces associated with a group. This method takes a QueryRequest object, a start index, the number of groups to include in the results, and the Artifact ID of a group. It returns a QueryResultSlim object. See Retrieve workspaces associated with a group .

- ReadAsync() method - retrieves a workspace. This method takes the Artifact ID of a workspace and returns a WorkspaceResponse object. See Retrieve a workspace .

- RetryFailedCreateEventHandlersAsync() method - retries failed create event handlers for a workspace. This method takes the Artifact ID of the workspace as an argument. See Retry failed create event handlers .

- UpdateAsync() method - modifies the properties of a workspace. This method takes the Artifact ID of the workspace and a WorkspaceRequest object. It returns a WorkspaceResponse object. See Update a workspace .

### Classes

The Workspace Manager API exposes the following classes available in the Relativity.Environment.<VersionNumber>.Workspace.Models namespace:

- WorkspaceRequest class - represents a request for creating or updating a workspace. View properties All properties related to the infrastructure details ( DownloadHandlerUrl , Resource Pool , DefaultFileRepository , DataGridFileRepository , DefaultCacheLocation , and SqlServer ) are optional. If the infrastructure details are not explicitly specified in the request, they are automatically selected by the algorithm.

- AzureCredentials - a Securable<ObjectIdentifier> object representing Azure credentials for the workspace. If CredentialEnableAzure setting is true, this field is required.

- AzureFileSystemCredentials - a Securable<ObjectIdentifier> object representing the Azure file system credentials for the workspace. If CredentialEnableAzure setting is true, this field is required.

- DataGridFileRepository - a Securable<ObjectIdentifier> object representing the file repository for the physical location of the text files used by Data Grid. This field is optional. If not specified, the file repository server for Data Grid is automatically selected by the algorithm.

- DefaultCacheLocation - a Securable<ObjectIdentifier> object representing the cache location server where the natives, images, productions and other file types are temporarily stored. This field is optional. If not specified, the cache location server is automatically selected by the algorithm.

- DefaultFileRepository - a Securable<ObjectIdentifier> object representing the file repository for the physical location of the files, including document natives and images. This field is optional. If not specified, the file repository server is automatically selected by the algorithm.

- DownloadHandlerUrl - a string representing the default URL used to make downloaded files available to users. This field is optional. If not specified in the request, the default URL is automatically selected by the algorithm.

- EnableDataGrid - a Boolean value indicating whether the workspace can have fields saved to Data Grid. This field can't be set during a create operation.

- Matter - a Securable<ObjectIdentifier> object representing the case or legal action associated with the workspace. This field is required.

- Name -a string representing the name of the workspace. This field is required.

- ProductionRestrictions - a Securable<ObjectIdentifier> object representing the saved search used to exclude documents from new production sets. This field can't be set during a create operation.

- ResourcePool - a Securable<ObjectIdentifier> object representing the resource pool used by the workspace for the other resource-related fields. This field is optional. If not specified, the resource pool is automatically selected by the algorithm.

- SqlFullTextLanguage - an integer representing the ID of the language used for determining the word-break characters used in the full text index for the workspace. Defaults to 0 if not specified.

- SqlServer - a Securable<ObjectIdentifier> object representing the SQL Server where the workspace database is stored. This field is optional. If not specified, the SQL server is automatically selected by the algorithm.

- Status - an ObjectIdentifier object representing the status of the workspace used in views to filter on workspaces. This field is required.

- Template - a Securable<ObjectIdentifier> object representing an existing workspace structure used to create the workspace. You can only set this field in a create request.

- WorkspaceAdminGroup - a Securable<ObjectIdentifier> object representing the group selected as the admin group for the workspace. A create operation cannot set this field.

- WorkspaceResponse class - represents the results of a read operation on a workspace. View properties

- Actions - a list of Action objects representing RESTful operations that a user has permissions to perform on the artifact.

- AzureCredentials - a Securable<DisplayableObjectIdentifier> object representing Azure credentials for the workspace.

- AzureFileSystemCredentials - a Securable<DisplayableObjectIdentifier> object representing the Azure file system credentials for the workspace.

- Client - a Securable<DisplayableObjectIdentifier> object representing the client associated with the workspace.

- ClientNumber - a Securable<string> representing the number of the clients associated with the workspace.

- CreatedBy - a DisplayableObjectIdentifier object representing the user who created the workspace.

- CreatedOn - a DateTime object representing the date and time when the workspace was added to Relativity.

- DataGridFileRepository - a Securable<DisplayableObjectIdentifier> object representing the file repository for the physical location of the text files used by Data Grid.

- DefaultCacheLocation - a Securable<DisplayableObjectIdentifier> object representing the cache location server where the natives, images, productions and other file types are temporarily stored.

- DefaultFileRepository - a Securable<DisplayableObjectIdentifier> object representing the file repository for the physical location of the files, including document natives and images.

- DownloadHandlerUrl - a string representing the default URL used to make downloaded files available to users.

- EnableDataGrid - a Boolean value indicating whether the workspace can have fields saved to Data Grid.

- Keywords - a string representing keywords associated with the workspace.

- LastModifiedBy - a DisplayableObjectIdentifier object representing the user who recently updated the workspace.

- LastModifiedOn - a DateTime object representing the date and time when the workspace was most recently updated.

- Matter - a Securable<DisplayableObjectIdentifier> object representing the case or legal action associated with the workspace.

- MatterNumber - a Securable<string> representing the number for the matter associated with the workspace.

- Meta - a Meta object representing a list of unsupported and read-only properties on the current workspace.

- Notes - a string representing an optional description or other information about the workspace.

- ProductionRestrictions - a Securable<DisplayableObjectIdentifier> object representing the saved search used to exclude documents from new production sets.

- ResourcePool - a Securable<DisplayableObjectIdentifier> object representing the resource pool used by the workspace for the other resource-related fields.

- SqlFullTextLanguage - a NameIDPair object representing the ID and name of the language used for determining the word-break characters used in the full text index for the workspace.

- SqlServer - a Securable<DisplayableObjectIdentifier> object representing the SQL Server where the workspace database is stored.

- Status - a DisplayableObjectIdentifier object representing the status of the workspace used in views to filter on workspaces.

- WorkspaceAdminGroup - a Securable<DisplayableObjectIdentifier> object representing the group selected as the admin for the workspace.

- SqlFullTextLanguageOptions class - represents the available full text language options for the SQL Server associated with a workspace. View properties

- DefaultLanguageLcid - an integer representing the ID of the default language.

- Languages - a list of NameIDPair objects representing the available languages.

-

WorkspaceSummary class - represents the statistics for a workspace.

View properties

- DocumentCount - a long representing the number of documents in a workspace.

- FileSize - a long representing the total size of the workspace files in bytes.

## Guidelines for the Workspace Manager API

Review the following guidelines for working with the Workspace Manager API.

### NuGet package

The NuGet package called Relativity.Environment.SDK is required to use the endpoints exposed in the Workspace Manager API. For more information, see SDK and Nuget Compatibility .

### Create a proxy

You must use a proxy to interact with the Workspace Manager API. To set up a proxy, call the CreateProxy() method on the object returned by the GetServiceManager() method.

View code sample Copy

```text
1
2
3
4
5
6
7
using Relativity.Environment.V1.Workspace;



Uri keplerEndPoint = new Uri("http://localhost/relativity.rest/api");

Services.ServiceProxy.ServiceFactory serviceFactory = new Services.ServiceProxy.ServiceFactory(new Services.ServiceProxy.ServiceFactorySettings(keplerEndPoint,

       new Services.ServiceProxy.UsernamePasswordCredentials("username", "password")));

Relativity.Environment.V1.Workspace.IWorkspaceManager workspaceManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Workspace.IWorkspaceManager>();<![CDATA[

]]>
```

### Field permissions

Review the following information about how field permissions are used by Workspace Manager API:

-

Secured fields - A user interacting with the Workspace Manager API may be given access to read and write to only select fields in the workspace. You can control this access by using the Securable<T> object types. Objects of this type have the following properties: Secured ( bool ) and Value ( T ). When the Secured property is set to true, the user doesn't have read or write access to the contents of the fields set for the Value property.

View table with field permissions

This table illustrates the permissions set on each field by operation. For general information, see Instance security and Workspace security on the Relativity Documentation site.

Field Create Update Read

Matter View permissions set on the Matter object at the instance level. Same as create. Same as create.

ClientNumber N/A N/A View permissions set on the Client object at the instance level.

ProductionRestrictions N/A View permissions set on the Search object at the workspace level. View permissions set on the Search object at the workspace level.

ResourcePool View permissions set on the Resource Pool object at the instance level. Same as create. Same as create.

DefaultFileRepository View permissions set on the Resource Server object at the instance level. Same as create. Same as create.

DataGridFileRepository View permissions set on the Resource Server object at the instance level. Same as create. Same as create.

DefaultCacheLocation View permissions set on the Resource Server object at the instance level. Same as create. Same as create.

SqlServer View permissions set on the Resource Server object at the instance level. Same as create. Same as create.

AzureCredentials View permissions set on the Credential object at the instance level. Same as create. Same as create.

AzureFileSystemCredentials View permissions set on the Credential object at the instance level. Same as create. Same as create.

Template View permissions set on the Workspace object at the instance level. N/A N/A

WorkspaceAdminGroup View permissions set on the Credential object at the instance level. N/A Same as create.

- Read-only fields - A user may have permission to view a field but not update or delete it. In this case, the field name is included in the read-only list in the metadata. The following fields are examples: client, matter, and workspace admin group.

### Cancellation and progress

The Workspace Manager API provides overloaded methods for create, update, and query operations, which support cancellation and progress functionality. For more information, see Cancellation and progress .

## Create a workspace

Use the CreateAsync() method to add a new workspace to Relativity. This method takes a WorkspaceRequest object and returns a WorkspaceResponse object. All WorkspaceRequest properties related to the infrastructure details ( DownloadHandlerUrl , Resource Pool , DefaultFileRepository , DataGridFileRepository , DefaultCacheLocation , SqlServer ) are optional. If the infrastructure details are not explicitly specified in the request, they are automatically selected by the algorithm.

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for the workspace set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View code sample with all infrastructure details fields specified Copy

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
public async Task CreateWorkspaceAsync(

     string name,

     int matterID,

     int templateID,

     int statusID,

     int resourcePoolID,

     int sqlServerID,

     int defaultFileRepositoryID,

     int dataGridFileRepositoryID,

     int defaultCacheLocationId)

{

    try

    {

        string downloadHandlerUrl = await _workspaceManager.GetDefaultDownloadHandlerURLAsync();

        WorkspaceRequest request = new WorkspaceRequest()

        {

            Name = name,

            Matter = new Securable<ObjectIdentifier>(new ObjectIdentifier() {ArtifactID = matterID}),

            Template = new Securable<ObjectIdentifier>(new ObjectIdentifier() {ArtifactID = templateID}),

            Status = new ObjectIdentifier() {ArtifactID = statusID},

            ResourcePool =

                new Securable<ObjectIdentifier>(new ObjectIdentifier() {ArtifactID = resourcePoolID}),

            SqlServer = new Securable<ObjectIdentifier>(new ObjectIdentifier() {ArtifactID = sqlServerID}),

            DefaultFileRepository = new Securable<ObjectIdentifier>(new ObjectIdentifier()

                {ArtifactID = defaultFileRepositoryID}),

            DataGridFileRepository = new Securable<ObjectIdentifier>(new ObjectIdentifier()

                {ArtifactID = dataGridFileRepositoryID}),

            DefaultCacheLocation = new Securable<ObjectIdentifier>(new ObjectIdentifier()

                {ArtifactID = defaultCacheLocationId}),

            DownloadHandlerUrl = downloadHandlerUrl

        };



        WorkspaceResponse response = await _workspaceManager.CreateAsync(request);

        Console.WriteLine($"Created workspace with artifact ID {response.ArtifactID} on {response.CreatedOn}");

    }

    catch (InvalidInputException ex)

    {

        Console.WriteLine("The following validation errors were found:");

        foreach (ValidationError error in ex.Errors)

        {

            Console.WriteLine($"\t{error.PropertyName}: {error.ErrorMessage}");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to create workspace: {ex.Message}");

        throw;

    }

}
```

View a code sample with no infrastructure details fields specified Copy

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
public async Task CreateWorkspaceAsync(string name, int matterID, int templateID, int statusID)

{

    try

    {

        WorkspaceRequest request = new WorkspaceRequest()

        {

            Name = name,

            Matter = new Securable<ObjectIdentifier>(new ObjectIdentifier() {ArtifactID = matterID}),

            Template = new Securable<ObjectIdentifier>(new ObjectIdentifier() {ArtifactID = templateID}),

            Status = new ObjectIdentifier() {ArtifactID = statusID}

        };



        WorkspaceResponse response = await _workspaceManager.CreateAsync(request);

        Console.WriteLine($"Created workspace with artifact ID {response.ArtifactID} on {response.CreatedOn}");

    }

    catch (InvalidInputException ex)

    {

        Console.WriteLine("The following validation errors were found:");

        foreach (ValidationError error in ex.Errors)

        {

            Console.WriteLine($"\t{error.PropertyName}: {error.ErrorMessage}");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to create workspace: {ex.Message}");

        throw;

    }

}
```

## Create operation helper methods

The following helper methods provide functionality to support the create operation.

### Retrieve unsupported fields for a create operation

Use the GetMetaAsync() method to retrieve a list of unsupported WorkspaceRequest fields for a create operation.

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for the workspace set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task GetMetaAsync()

{

    try

    {

        Meta meta = await _workspaceManager.GetMetaAsync();



        if (meta.ReadOnly.Any())

        {

            Console.WriteLine($"The following fields are read-only: {string.Join(", ", meta.ReadOnly)}");

        }

        else

        {

            Console.WriteLine("No fields are read-only.");

        }



        if (meta.Unsupported.Any())

        {

            Console.WriteLine($"The following fields are unsupported: {string.Join(", ", meta.Unsupported)}");

        }

        else

        {

            Console.WriteLine("No fields are unsupported.");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to get meta: {ex.Message}");

        throw;

    }

}
```

### Retry failed create event handlers

Use the RetryFailedCreateEventHandlersAsync() method to retry failed create event handlers for a workspace. This method takes the Artifact ID of the workspace as an argument.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the workspace level. See Workspace security on the Relativity Documentation site.

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
public async Task RetryFailedCreateEventHandlersAsync(int workspaceID)

{

    try

    {

        await _workspaceManager.RetryFailedCreateEventHandlersAsync(workspaceID);

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to retry failed create event handlers: {ex.Message}");

        throw;

    }

}
```

## Retrieve a workspace

Use the ReadAsync() method to retrieve a workspace. This method takes the Artifact ID of a workspace and returns a WorkspaceResponse object.

View required permissions

To use this endpoint, the caller must have the following:

- View Workspace Details permissions for the workspace set at the workspace level. See Workspace security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin. See Instance security on the Relativity Documentation site.

This permission is required for the admin-level context workspace. Use -1 to indicate the admin-level context.

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
public async Task ReadWorkspaceAsync(int workspaceID, bool includeMetadata, bool includeActions)

{

    try

    {

        WorkspaceResponse response = await _workspaceManager.ReadAsync(workspaceID, includeMetadata, includeActions);

        Console.WriteLine($"Workspace {workspaceID} has the name {response.Name}");

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to read workspace {workspaceID}: {ex.Message}");

        throw;

    }

}
```

## Update a workspace

Use the UpdateAsync() method to modify the properties of a workspace. This method takes the Artifact ID of the workspace and a WorkspaceRequest object. It returns a WorkspaceResponse object.

View required permissions

To use this endpoint, the caller must have the following:

- Edit permissions for the workspace set at the workspace level. See Workspace security on the Relativity Documentation site.

- View Workspace Details permissions for the workspace set at the workspace level.

To update the WorkspaceAdminGroup or Matter properties, the calling user must be a system admin or client domain admin. The admin workspace can't be updated. It resides in the admin level context indicated by -1.

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
public async Task UpdateWorkspaceAsync(int workspaceID)

{

    try

    {

        WorkspaceResponse originalWorkspace = await _workspaceManager.ReadAsync(workspaceID, true, true);



        WorkspaceRequest request = new WorkspaceRequest()

        {

            Name = "Updated Workspace",

            Matter = new Securable<ObjectIdentifier>() { Value = originalWorkspace.Matter.Value },

            Status = originalWorkspace.Status,

            ResourcePool = new Securable<ObjectIdentifier>() { Value = originalWorkspace.ResourcePool.Value },

            SqlServer = new Securable<ObjectIdentifier>() { Value = originalWorkspace.SqlServer.Value },

            DefaultFileRepository = new Securable<ObjectIdentifier>() { Value = originalWorkspace.DefaultFileRepository.Value },

            DefaultCacheLocation = new Securable<ObjectIdentifier>() { Value = originalWorkspace.DefaultCacheLocation.Value },

            DownloadHandlerUrl = originalWorkspace.DownloadHandlerUrl

        };



        WorkspaceResponse response = await _workspaceManager.UpdateAsync(workspaceID, request);

        Console.WriteLine($"Updated workspace with artifact ID {workspaceID} on {response.LastModifiedOn}");

    }

    catch (InvalidInputException ex)

    {

        Console.WriteLine("The following validation errors were found:");

        foreach (ValidationError error in ex.Errors)

        {

            Console.WriteLine($"\t{error.PropertyName}: {error.ErrorMessage}");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to update workspace: {ex.Message}");

        throw;

    }

}
```

## Delete a workspace

Use the DeleteAsync() method to remove a workspace from Relativity. This method takes the Artifact ID of the workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View and Delete permissions for the workspace set at the workspace level. See Workspace security on the Relativity Documentation site.

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
public async Task DeleteWorkspaceAsync(int workspaceId)

{

    try

    {

        await _workspaceManager.DeleteAsync(workspaceId);

    }

    catch (InvalidInputException ex)

    {

        Console.WriteLine("The following validation errors were found:");

        foreach (ValidationError error in ex.Errors)

        {

            Console.WriteLine($"\t{error.PropertyName}: {error.ErrorMessage}");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to update workspace: {ex.Message}");

        throw;

    }

}
```

## Retrieve workspace statistics

Use the GetWorkspaceSummaryAsync() method to retrieve a summary of workspace statistics. This method takes the Artifact ID of the workspace as an argument and returns a WorkspaceSummary object.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the workspace level. See Workspace security on the Relativity Documentation site.

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
public async Task GetWorkspaceSummaryAsync(int workspaceID)

{

    try

    {

        WorkspaceSummary workspaceSummary = await _workspaceManager.GetWorkspaceSummaryAsync(workspaceID);

        Console.WriteLine($"Document Count: {workspaceSummary.DocumentCount}");

        Console.WriteLine($"File Size: {workspaceSummary.FileSize}");

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to get workspace summary: {ex.Message}");

        throw;

    }

}
```

## Retrieve workspaces associated with a group

Use the QueryWorkspaceByGroupAsync() method to retrieve workspaces associated with a group. This method takes a QueryRequest object, a start index, the number of groups to include in the results, and the Artifact ID of a group. It returns a QueryResultSlim object. For more information about QueryResultSlim objects, see Query for Relativity objects .

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for the group set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task QueryWorkspaceByGroupAsync(int groupID)

{

    try

    {

        QueryRequest workspacesRequest = new QueryRequest();

        QueryResultSlim workspacesResponse = await _workspaceManager.QueryWorkspaceByGroupAsync(workspacesRequest, 1, _QUERY_LENGTH, groupID);



        foreach (int workspaceID in workspacesResponse.Objects.Select(x => x.ArtifactID))

        {

            Console.WriteLine($"Workspace {workspaceID} is part of group {groupID}");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query workspaces: {ex.Message}");

        throw;

    }

}
```

## Resource information helper methods

The following helper methods correspond to the fields that you can set in the Resource Information section of the Workspace form in the Relativity UI. For more information, see Workspaces on the Relativity Documentation site.

### Retrieve matters

Use the QueryEligibleMattersAsync() method to retrieve a list of matters. This method takes a QueryRequest object, a start index, and the number of matters to include in the results. It returns a QueryResultSlim object with a list of available matters. Use this method when setting the Matter property on a workspace. For more information about QueryResultSlim objects, see Query for Relativity objects .

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for matters set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task QueryEligibleMattersAsync()

{

    try

    {

        QueryRequest mattersRequest = new QueryRequest();

        QueryResultSlim mattersResponse = await _workspaceManager.QueryEligibleMattersAsync(mattersRequest, 1, _QUERY_LENGTH);



        Console.WriteLine("Eligible Matters:");

        foreach (int matterID in mattersResponse.Objects.Select(x => x.ArtifactID))

        {

            Console.WriteLine(matterID);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible matters: {ex.Message}");

        throw;

    }

}
```

### Retrieve clients

Use the QueryEligibleClientsAsync() method to retrieve a list of clients available for this workspace. This method takes a QueryRequest object, a start index, and the number of clients to include in the results. It returns a QueryResultSlim object with a list of available clients. Use this method when setting the Client property on a workspace. For more information about QueryResultSlim objects, see Query for Relativity objects .

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task QueryEligibleClientsAsync()

{

    try

    {

        QueryRequest clientsRequest = new QueryRequest();

        QueryResultSlim clientsResponse = await _workspaceManager.QueryEligibleClientsAsync(clientsRequest, 1, _QUERY_LENGTH);



        Console.WriteLine("Eligible Clients:");

        foreach (int clientID in clientsResponse.Objects.Select(x => x.ArtifactID))

        {

            Console.WriteLine(clientID);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible clients: {ex.Message}");

        throw;

    }

}
```

### Retrieve workspaces for use as templates

Use the QueryEligibleTemplatesAsync() method to retrieve a list of workspaces for use as templates when creating a new workspace. This method takes a QueryRequest object, a start index, and the number of templates to include in the results. It returns a QueryResultSlim object with a list of available templates. Use this method when setting the Template property on a workspace. For more information about QueryResultSlim objects, see Query for Relativity objects .

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task QueryEligibleTemplatesAsync()

{

    try

    {

        QueryRequest templatesRequest = new QueryRequest();

        QueryResultSlim templatesResponse = await _workspaceManager.QueryEligibleTemplatesAsync(templatesRequest, 1, _QUERY_LENGTH);



        Console.WriteLine("Eligible Templates:");

        foreach (int templateID in templatesResponse.Objects.Select(x => x.ArtifactID))

        {

            Console.WriteLine(templateID);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible templates: {ex.Message}");

        throw;

    }

}
```

### Retrieve resource pools

Use the GetEligibleResourcePoolsAsync() method to retrieve a list of resource pools. This method returns a list of DisplayableObjectIdentifier objects, which identify available resource pools. Use this method when setting the ResourcePool property for a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task GetEligibleResourcePoolsAsync()

{

    try

    {

        List<DisplayableObjectIdentifier> resourcePools = await _workspaceManager.GetEligibleResourcePoolsAsync();

        Console.WriteLine("Eligible Resource Pools:");

        foreach (DisplayableObjectIdentifier resourcePool in resourcePools)

        {

            Console.WriteLine($"\t{resourcePool.Name} ({resourcePool.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible resource pools: {ex.Message}");

        throw;

    }

}
```

### Retrieve SQL Servers

Use the GetEligibleSqlServersAsync() method to retrieve a list of SQL servers available for the workspace. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available SQL servers. Use this method when setting the SqlServer property for a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task GetEligibleSqlServersAsync(int resourcePoolID)

{

    try

    {

        List<DisplayableObjectIdentifier> sqlServers = await _workspaceManager.GetEligibleSqlServersAsync(resourcePoolID);

        Console.WriteLine("Eligible SQL Servers:");

        foreach (DisplayableObjectIdentifier sqlServer in sqlServers)

        {

            Console.WriteLine($"\t{sqlServer.Name} ({sqlServer.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible SQL servers: {ex.Message}");

        throw;

    }

}
```

### Retrieve file repository servers

Use the GetEligibleFileRepositoriesAsync() method to retrieve a list of available file repository servers. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available servers. Use this method when setting the DefaultFileRepository and DataGridRepository properties for a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task GetEligibleFileRepositoriesAsync(int resourcePoolID)

{

    try

    {

        List<DisplayableObjectIdentifier> fileRepositories = await _workspaceManager.GetEligibleFileRepositoriesAsync(resourcePoolID);

        Console.WriteLine("Eligible File Repositories:");

        foreach (DisplayableObjectIdentifier fileRepository in fileRepositories)

        {

            Console.WriteLine($"\t{fileRepository.Name} ({fileRepository.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible file repositories: {ex.Message}");

        throw;

    }

}
```

### Retrieve cache location servers

Use the GetEligibleCacheLocationsAsync() method to retrieve a list of available cache location servers. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available cache locations. Use this method when setting the DefaultCacheLocation property for a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task GetEligibleCacheLocationsAsync(int resourcePoolID)

{

    try

    {

        List<DisplayableObjectIdentifier> cacheLocations = await _workspaceManager.GetEligibleCacheLocationsAsync(resourcePoolID);

        Console.WriteLine("Eligible Cache Locations:");

        foreach (DisplayableObjectIdentifier cacheLocation in cacheLocations)

        {

            Console.WriteLine($"\t{cacheLocation.Name} ({cacheLocation.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible cache locations: {ex.Message}");

        throw;

    }

}
```

### Retrieve the URL for the default download handler

Use the GetDefaultDownloadHandlerURLAsync() method to retrieve the URL for the default download handler. This method returns a URL.

This endpoint doesn't require any specific permissions.

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
public async Task GetDefaultDownloadHandlerURLAsync()

{

    try

    {

        string downloadHandlerUrl = await _workspaceManager.GetDefaultDownloadHandlerURLAsync();

        Console.WriteLine($"The default download handler URL is {downloadHandlerUrl}");

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to get download handler URL: {ex.Message}");

        throw;

    }

}
```

## Advanced settings helper methods

The following helper methods correspond to the fields that you can set in the Advanced settings section of the Workspace form in the Relativity UI. For more information, see Workspaces on the Relativity Documentation site.

### Retrieve available statuses for a workspace

Use the GetEligibleStatusesAsync() method to retrieve a list of available statuses for a workspace. This method returns a list of DisplayableObjectIdentifier objects, which contain the Artifact ID, Name, and GUIDs identifying each status. Use this method when setting the Status property on a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for the resource server set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task GetEligibleStatusesAsync()

{

    try

    {

        List<DisplayableObjectIdentifier> statuses = await _workspaceManager.GetEligibleStatusesAsync();



        Console.WriteLine("Eligible Statuses:");

        foreach (DisplayableObjectIdentifier status in statuses)

        {

            Console.WriteLine($"{status.Name} ({status.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to get eligible statuses: {ex.Message}");

        throw;

    }

}
```

### Retrieve full text languages for SQL Server

Use the GetEligibleSqlFullTextLanguagesAsync() method to retrieve a list of available full text languages for the SQL Server assigned to a workspace. This method returns a list of SqlFullTextLanguageOptions objects, which describe the available and default languages. Use this method when setting the SqlFullTextLanguage property on a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for the resource server set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task GetEligibleSqlFullTextLanguagesAsync()

{

    try

    {

        SqlFullTextLanguageOptions sqlFullTextLanguageOptions = await _workspaceManager.GetEligibleSqlFullTextLanguagesAsync();



        Console.WriteLine("Eligible SQL Full Text Languages:");

        foreach (NameIDPair language in sqlFullTextLanguageOptions.Languages)

        {

            Console.WriteLine($"{language.Name} ({language.ID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to get eligible SQL full text languages: {ex.Message}");

        throw;

    }

}
```

### Retrieve groups for workspace membership

Use the QueryEligibleGroupsAsync() method to retrieve a list of groups available for workspace membership. This method takes a QueryRequest object, a start index, and the number of groups to include in the results. It returns a QueryResultSlim object with a list of available groups. For more information about QueryResultSlim objects, see Query for Relativity objects .

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public async Task QueryEligibleGroupsAsync()

{

    try

    {

        QueryRequest groupsRequest = new QueryRequest();

        QueryResultSlim groupsResponse = await _workspaceManager.QueryEligibleGroupsAsync(groupsRequest, 1, _QUERY_LENGTH);



        Console.WriteLine("Eligible Groups:");

        foreach (int groupID in groupsResponse.Objects.Select(x => x.ArtifactID))

        {

            Console.WriteLine(groupID);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible groups: {ex.Message}");

        throw;

    }

}
```

### Retrieve saved searches for production restrictions

Use the QueryEligibleSavedSearchesAsync() method to retrieve saved searches for use with production restrictions. For more information, see Adding and editing production restrictions on the Relativity Documentation site.

This method takes a QueryRequest object, a start index, and the number of saved searches to include in the results. It returns a QueryResultSlim object with a list of available saved searches. Use this method when setting the ProductionRestrictions property on a workspace. For more information about QueryResultSlim objects, see Query for Relativity objects .

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the workspace level. See Workspace security on the Relativity Documentation site.

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
public async Task QueryEligibleSavedSearchesAsync(int workspaceID)

{

    try

    {

        QueryRequest savedSearchRequest = new QueryRequest();

        QueryResultSlim savedSearchResponse = await _workspaceManager.QueryEligibleSavedSearchesAsync(savedSearchRequest, 1, _QUERY_LENGTH, workspaceID);



        Console.WriteLine("Eligible Saved Searches:");

        foreach (int savedSearchID in savedSearchResponse.Objects.Select(x => x.ArtifactID))

        {

            Console.WriteLine(savedSearchID);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible saved searches: {ex.Message}");

        throw;

    }

}
```

## Azure credentials helper methods

Use the following methods to retrieve Azure credentials associated with a resource pool. For more information, see Workspaces on the Relativity Documentation site.

### Retrieve Azure credentials

Use the GetEligibleAzureCredentialsAsync() method to retrieve a list of available Azure credentials for the workspace. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available credentials. Use this method when setting the AzureCredentials property on a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task GetEligibleAzureCredentialsAsync(int resourcePoolID)

{

    try

    {

        List<DisplayableObjectIdentifier> azureCredentials = await _workspaceManager.GetEligibleAzureCredentialsAsync(resourcePoolID);

        Console.WriteLine("Eligible Azure Credentials:");

        foreach (DisplayableObjectIdentifier azureCredential in azureCredentials)

        {

            Console.WriteLine($"\t{azureCredential.Name} ({azureCredential.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible Azure credentials: {ex.Message}");

        throw;

    }

}
```

### Retrieve Azure file system credentials

Use the GetEligibleAzureFileSystemCredentialsAsync() method to retrieve a list of available Azure file system credentials. This method takes the Artifact ID of a resource pool and returns a list of DisplayableObjectIdentifier objects, which identify available credentials. Use this method when setting the AzureFileSystemCredentials property on a workspace.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

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
public async Task GetEligibleAzureFileSystemCredentialsAsync(int resourcePoolID)

{

    try

    {

        List<DisplayableObjectIdentifier> azureFileSystemCredentials = await _workspaceManager.GetEligibleAzureFileSystemCredentialsAsync(resourcePoolID);

        Console.WriteLine("Eligible Azure File System Credentials:");

        foreach (DisplayableObjectIdentifier azureFileSystemCredential in azureFileSystemCredentials)

        {

            Console.WriteLine($"\t{azureFileSystemCredential.Name} ({azureFileSystemCredential.ArtifactID})");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine($"Failed to query eligible Azure file system credentials: {ex.Message}");

        throw;

    }

}
```

On this page

- Workspace Manager (.NET)

- Fundamentals for the Workspace Manager API

- Methods

- Classes

- Guidelines for the Workspace Manager API

- NuGet package

- Create a proxy

- Field permissions

- Cancellation and progress

- Create a workspace

- Create operation helper methods

- Retrieve unsupported fields for a create operation

- Retry failed create event handlers

- Retrieve a workspace

- Update a workspace

- Delete a workspace

- Retrieve workspace statistics

- Retrieve workspaces associated with a group

- Resource information helper methods

- Retrieve matters

- Retrieve clients

- Retrieve workspaces for use as templates

- Retrieve resource pools

- Retrieve SQL Servers

- Retrieve file repository servers

- Retrieve cache location servers

- Retrieve the URL for the default download handler

- Advanced settings helper methods

- Retrieve available statuses for a workspace

- Retrieve full text languages for SQL Server

- Retrieve groups for workspace membership

- Retrieve saved searches for production restrictions

- Azure credentials helper methods

- Retrieve Azure credentials

- Retrieve Azure file system credentials


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
