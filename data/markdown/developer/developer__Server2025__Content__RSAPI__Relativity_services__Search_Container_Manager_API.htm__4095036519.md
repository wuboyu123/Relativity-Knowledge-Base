---
title: "Search Container Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Relativity_services/Search_Container_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:28:03+00:00
sha256: 6c37db4a8d9815a492e1edbee14d0e73ebdfe6dd5f978a9ee507f9c2a8359c69
---

Search Container Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# Search Container Manager (.NET)

You can organize Relativity saved searches by using logical folders. Saved search folders can be secured by permissions. For more information, see Organizing saved searches in folders on the Relativity Documentation site.

The Services API supports creating, reading, updating, deleting, and querying saved search folders as SearchContainer DTOs. A helper method to easily return the content of a SearchContainer (saved searches and subfolders) is also provided. You can perform the operations on SearchContainer DTOs asynchronously.

You can also interact with the SearchContainer objects using the Relativity REST API .

## Create a SearchContainer

You can create a SearchContainer asynchronously using the CreateSingleAsync() method of the ISearchContainerManager interface. The following example illustrates how to create a folder with the Name "My Search Container" in the root saved search folder. The root saved search folder is specified by setting the value of ArtifactID of the ParentSearchContainer property to 0. Note that you can easily find the values of saved search folder's ArtifactIDs for setting the ParentSearchContainer property by using the GetSearchContainerItemsAsync() helper method. For more information, see List SearchContainer content .

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
public async Task<bool> CreateSingleAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        try

        {

            Services.Search.SearchContainer searchContainer =

            new Services.Search.SearchContainer();

            searchContainer.Name = "My Search Container";

            //A parent Artifact ID of 0 specifies the root Search Container

            searchContainer.ParentSearchContainer.ArtifactID = 0;

            //Create the Search Container

            int artifactID = await proxy.CreateSingleAsync(this.SampleWorkspace_ID, searchContainer);

            if (artifactID != 0)

            {

                success = true;

            }

            else

            {

                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, "Create failed", this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, exception.Message, this.GetType().Name);

        }

    }

    return success;

}
```

## Read a SearchContainer

The following code sample illustrates how to read a SearchContainer DTO using the ReadSingleAsync() method of the ISearchContainerManager interface.

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
public async Task<bool> ReadSingleAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        //Set the ForContext for the method.

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            // Create sample data.

            int? searchContainerID;

            Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.SampleWorkspace_ID,

            out searchContainerID);

            Services.Search.SearchContainer searchContainer = await proxy.ReadSingleAsync(this.SampleWorkspace_ID, searchContainerID.Value);

            // Display the search artifact result.

            logger.LogDebug("{SearchContainerID} - {SearchContainerName}", searchContainer.ArtifactID, searchContainer.Name);

            success = true;

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

## Update a SearchContainer

The following code sample illustrates how to update a SearchContainer using the UpdateSingleAsync() method of the ISearchContainerManager interface.

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
public async Task<bool> UpdateSingleAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        int? searchContainerArtifactID;

        if (Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.Logger, this.SampleWorkspace_ID,

                    out searchContainerArtifactID))

        {

            try

            {

                //Get the search container to update

                Services.Search.SearchContainer searchContainer = await proxy.ReadSingleAsync(this.SampleWorkspace_ID, searchContainerArtifactID.Value);

                //Create sample parent

                int? parentSearchContainerArtifactID;

                if (Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.Logger, this.SampleWorkspace_ID,

                            out parentSearchContainerArtifactID))

                {

                    //Set this new sample search Container to be the new parent

                    searchContainer.ParentSearchContainer.ArtifactID = parentSearchContainerArtifactID.Value;

                }

                //Change the name on the search Container

                searchContainer.Name = "My Updated SearchContainer";

                //Update the search container

                await proxy.UpdateSingleAsync(this.SampleWorkspace_ID, searchContainer);

                success = true;

            }

            catch (ServiceException exception)

            {

                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, exception.Message, this.GetType().Name);

            }

        }

    }

    return success;

}
```

## Delete a SearchContainer

You can delete SearchContainer objects asynchronously by using the DeleteSingleAsync() method of the ISearchContainerManager interface. The following code sample illustrates how to delete a SearchContainer.

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
public async Task<bool> DeleteSingleAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        int? SearchContainerArtifactID;

        if (Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.Logger,

                this.SampleClient_ID, out SearchContainerArtifactID))

        {

            try

            {

                await proxy.DeleteSingleAsync(SearchContainerArtifactID.Value);

                success = true;

            }

            catch (ServiceException exception)

            {

                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, exception.Message, this.GetType().Name);

            }

        }

    }

    return success;

}
```

## Query SearchContainers

The following code sample illustrates how to query SearchContainer objects using the QueryAsync() and QuerySubsetAsync() methods of the ISearchContainerManager interface. The query condition checks if the search name starts with the string "API". The results are sorted by ArtifactID in descending order. If the query returns a token value that is not null, more results are available than initially specified in the length property (5 in this example), and they are subsequently retrieved by using the QuerySubsetAsync() method. When the length parameter is not specified, its value defaults to 0, and the number of returned results defaults to the Instance setting table value PDVDefaultQueryCacheSize of 10000. For more information about query conditions and using query tokens, see Search Relativity .

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
116
117
118
119
120
121
122
public async Task<bool> QueryAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        try

        {

            // Create sample data.

            int? searchContainerID;

            for (int i = 0; i < 12; i++)

            {

                Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.Logger, this.SampleWorkspace_ID, out searchContainerID);

            }

            // Create a new instance of a Query.

            Services.Query query = new Services.Query();

            // Define the search length. This is the number of results to be returned.

            // If more results are available the search results will contain a query token that can be used with QuerySubsetAsync

            // to get the additional results from the search query. Setting length to 0 will use the default length defined in Relativity.

            int length = 5;

            // Define the search condition for the query.  Conditions can be created programmatically using Conditions and converted

            // to a query string using the ToQueryString extension method that the query conditions accepts.

            Condition queryCondition = new TextCondition(ClientFieldNames.Name, TextConditionEnum.StartsWith, "API");

            string queryString = queryCondition.ToQueryString();

            query.Condition = queryString;

            // Create an instance of a Sort and define how this query is to be sorted.

            Services.Sort sortBy = new Services.Sort();

            sortBy.FieldIdentifier.Name = "ArtifactID";

            sortBy.Order = 0;

            sortBy.Direction = SortEnum.Descending;

            query.Sorts.Add(sortBy);

            // Query for search objects given the above query condition and sort order.

            SearchContainerQueryResultSet queryResultSet = await proxy.QueryAsync(this.SampleWorkspace_ID, query, length);

            if (queryResultSet.Success)

            {

                // Loop through the search results and display successful search results.

                foreach (Services.Result<Services.Search.SearchContainer> result in queryResultSet.Results)

                {

                    // If the result was successful display the ArtifactID and Name, if it is not display the error message.

                    if (result.Success)

                    {

                        string info = string.Format("{0} - {1}", result.Artifact.ArtifactID, result.Artifact.Name);

                        this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Debug, new StackFrame(0).GetMethod().Name, info,

                        this.GetType().Name);

                    }

                    else

                    {

                        string info = string.Format("Error: {0}", result.Message);

                        this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, info,

                        this.GetType().Name);

                    }

                }

                #region QuerySubsetAsync Example

                // If a QueryToken exists more results are available.

                int queryStartPosition = 1 + length;

                while (!string.IsNullOrEmpty(queryResultSet.QueryToken))

                {

                    // Query for the subset of query results.

                    queryResultSet = await proxy.QuerySubsetAsync(this.SampleWorkspace_ID, queryResultSet.QueryToken, queryStartPosition, length);

                    // Repeat the same process to read results as seen in QueryAsync.

                    // Check to see if the query was successful.

                    if (queryResultSet.Success)

                    {

                        // Loop through the search results and display successful search results.

                        foreach (Services.Result<Services.Search.SearchContainer> result in queryResultSet.Results)

                        {

                            // If the result was successful display the ArtifactID and Name, if it is not display the error message.

                            if (result.Success)

                            {

                                string info = string.Format("{0} - {1}", result.Artifact.ArtifactID, result.Artifact.Name);

                                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Debug, new StackFrame(0).GetMethod().Name, info,

                                this.GetType().Name);

                            }

                            else

                            {

                                string info = string.Format("Error: {0}", result.Message);

                                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, info,

                                this.GetType().Name);

                            }

                        }

                        // Shift the starting position.

                        queryStartPosition += length;

                    }

                    else

                    {

                        string info = string.Format("Error: QuerySubsetAsync was not successful - {0}", queryResultSet.Message);

                        this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, info,

                        this.GetType().Name);

                    }

                }

                #endregion

                success = true;

            }

            else

            {

                string info = string.Format("Error: QueryAsync was not successful - {0}", queryResultSet.Message);

                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, info,

                this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, exception.Message, this.GetType().Name);

        }

    }

    return success;

}
```

## List SearchContainer content

The ISearchContainerManager interface provides these methods for listing SearchContainer content:

- GetSearchContainerItemsAsync() – returns the saved searches and subfolders in a specified saved search folder in a workspace. They are returned as the SavedSearchContainerItems (saved searches) and SearchContainerItems (subfolders) properties of the SearchContainerItemCollection object.

- GetChildSearchContainersAsync() – returns the subfolders in a specified saved search folder in a workspace. Subfolders are returned as the SavedSearchContainerItems property of the SearchContainerItemCollection object.

Note that the permissions of the items in the returned collections can be tested using the Personal and Secured Boolean properties of the SavedSearchContainerItem objects.

### GetSearchContainerItemsAsync()

This example illustrates how to use the GetSearchContainerItemsAsync() method to return saved searches and subfolders in a SearchContainer.

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
public async Task<bool> GetSearchContainerItems(Client.SamplesLibrary.Helper.IHelper helper)

{

    //Search Container has a helper method where the user can pass a root search container

    //and they will get back all search containers and search under it, so it will auto-expand and return

    //search containers and searches from multiple levels deep.

    bool success = false;

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        try

        {

            // Create sample data.

            int? searchContainerID;

            for (int i = 0; i < 12; i++)

            {

                Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.Logger, this.SampleWorkspace_ID, out searchContainerID);

            }

            //When the ArtifactID of the passed in search container is 0 it'll retrieve the root search container

            Services.Search.SearchContainer rootSearchContainer = new Services.Search.SearchContainer();

            rootSearchContainer.ArtifactID = 0;

            // Query for search objects given the above query condition and sort order.

            SearchContainerItemCollection itemCollection =

            await proxy.GetSearchContainerItemsAsync(this.SampleWorkspace_ID, rootSearchContainer);

            if (itemCollection.SavedSearchContainerItems != null || itemCollection.SearchContainerItems != null)

            {

                // Loop through the search results and display successful search results.

                foreach (SearchContainerItem item in itemCollection.SearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the search container has item

                    // level security.

                    string info = string.Format("{0} - {1}, Item-Secured: {2}", item.SearchContainer.ArtifactID, item.SearchContainer.Name, item.Secured);

                    this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Debug, new StackFrame(0).GetMethod().Name, info,

                    this.GetType().Name);

                }

                foreach (SavedSearchContainerItem item in itemCollection.SavedSearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the saved search has item

                    // level security and if it belongs to the current user.

                    string info = string.Format("{0} - {1}, Item-Secured: {2}, IsOwner: {3}", item.SavedSearch.ArtifactID, item.SavedSearch.Name, item.Secured, item.Personal);

                    this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Debug, new StackFrame(0).GetMethod().Name, info,

                    this.GetType().Name);

                }

                success = true;

            }

            else

            {

                string info = "Error: Getting Search Container Items was not successfull";

                this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, info,

                this.GetType().Name);

            }

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            this.Logger.LogMessage(Client.SamplesLibrary.Logging.LogLevel.Error, new StackFrame(0).GetMethod().Name, exception.Message, this.GetType().Name);

        }

    }

    return success;

}
```

### GetChildSearchContainersAsync()

This example illustrates how to use the GetChildSearchContainersAsync() method to return the subfoders in a SearchContainer.

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
public async Task<bool> GetChildSearchContainersAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    //Search Container has a helper method where the user can pass a root search contaier

    //and they will get back all search containers and search under it, so it will auto-expand and return

    //search containers and searches from multiple levels deep.

    bool success = false;

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        //Set the ForContext for the method.

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            // Create sample data.

            int? searchContainerID;

            for (int i = 0; i < 12; i++)

            {

                Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.SampleWorkspace_ID, out searchContainerID);

            }

            Services.Search.SearchContainerRef rootSearchContainer = new Services.Search.SearchContainerRef();

            rootSearchContainer.ArtifactID = 0;

            // Query for search objects given the above query condition and sort order.

            SearchContainerItemCollection itemCollection =

            await proxy.GetChildSearchContainersAsync(this.SampleWorkspace_ID, rootSearchContainer);

            if (itemCollection.SavedSearchContainerItems != null || itemCollection.SearchContainerItems != null)

            {

                // Loop through the search results and display successful search results.

                foreach (SearchContainerItem item in itemCollection.SearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the search container has item

                    // level security.

                    logger.LogDebug("{SearchContainerID} - {SearchContainerName}, Item-Secured: {Secured}", item.SearchContainer.ArtifactID, item.SearchContainer.Name, item.Secured);

                }

                foreach (SavedSearchContainerItem item in itemCollection.SavedSearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the saved search has item

                    // level security and if it belongs to the current user.

                    logger.LogDebug("{SavedSearchID} - {SavedSearchName}, Item-Secured: {Secured}, IsOwner: {Personal}", item.SavedSearch.ArtifactID, item.SavedSearch.Name, item.Secured, item.Personal);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting Child Search Containers was not successful");

            }

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

## Retrieve expanded search container nodes

The ISearchContainerManager interface provides these methods for traversing search containers in a tree structure.

- GetSearchContainerTreeAsync() – retrieves information about expanded search container nodes. The method returns a SearchContainerItemCollection object, which provides this information about a given SearchContainer. You can use this method to render an expanded browser tree for a saved search.

- GetFilteredSearchContainerTreeAsync() – retrieves information about search container nodes matching the specified condition. The method returns a SearchContainerItemCollection object. The method has two overloads that allow you to specify the condition as a query string or a SearchContainerTreeFilter object.

### GetSearchContainerTreeAsync()

The following code sample illustrates how to complete these tasks for retrieving information about expanded search container nodes using GetSearchContainerTreeAsync():

- Set the URI and endpoint for the Relativity Services and REST APIs.

- Create a proxy for the Search Container Manager object using the ServiceFactory class.

- Set the Artifact IDs of the workspace where you want to retrieve the search containers.

- Call the GetSearchContainerTreeAsync() method by passing the workspace Artifact ID, and the list of Artifact IDs for the specific expanded container nodes that you want to retrieve.

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
public async Task GetSearchContainerTreeWithExpandedNodes()

{

    Uri keplerEndpoint = new Uri("http://localhost/relativity.rest/api");

    Services.ServiceProxy.ServiceFactory serviceFactory = new Services.ServiceProxy.ServiceFactory(

            new Services.ServiceProxy.ServiceFactorySettings(keplerEndpoint,

            new Services.ServiceProxy.UsernamePasswordCredentials("username", "password")));

    Services.Search.ISearchContainerManager proxy = serviceFactory.CreateProxy<Services.Search.ISearchContainerManager>();

    //Initialize a variable for the Artifact ID of an active workspace.

    var workspaceArtifactId = 0;

    var result = await proxy.GetSearchContainerTreeAsync(

        workspaceArtifactID: workspaceArtifactId, expandedNodes: new[] { 1035243, 1039255 }.ToList()

    );

}
```

### GetFilteredSearchContainerTreeAsync()

The following code sample illustrates how to use the GetFilteredSearchContainerTreeAsync() method to return the items where the name matches the specified string condition - "API" .

You can specify a partial string.

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
public async Task<bool> GetFilteredSearchContainerTreeAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    //Search Container has a helper method where the user can pass a root search contaier

    //and they will get back all search containers and search under it, so it will auto-expand and return

    //search containers and searches from multiple levels deep.

    bool success = false;

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            // Create sample data.

            int? searchContainerID;

            for (int i = 0; i < 6; i++)

            {

                Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.SampleWorkspace_ID, out searchContainerID);

            }

            //Search Condition

            string searchCondition = "API";

            SearchContainerItemCollection treeCollection =

            await proxy.GetFilteredSearchContainerTreeAsync(this.SampleWorkspace_ID, searchCondition);

            if (treeCollection.SavedSearchContainerItems != null || treeCollection.SearchContainerItems != null)

            {

                foreach (SearchContainerItem item in treeCollection.SearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the search container has item

                    // level security.

                    logger.LogDebug("{SearchContainerID} - {SearchContainerName}, Item-Secured: {Secured}",

                    item.SearchContainer.ArtifactID, item.SearchContainer.Name, item.Secured);

                }

                foreach (SavedSearchContainerItem item in treeCollection.SavedSearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the saved search has item

                    // level security and if it belongs to the current user.

                    logger.LogDebug(

                    "{SavedSearchID} - {SavedSearchName}, Item-Secured: {Secured}, IsOwner: {Personal}",

                    item.SavedSearch.ArtifactID, item.SavedSearch.Name, item.Secured, item.Personal);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting Filtered Search Container Tree was not successful");

            }

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

This code sample illustrates how to use the overload of the GetFilteredSearchContainerTreeAsync() method to return the items where the name matches the condition specified as the SearchContainerTreeFilter object. The condition is specified by setting the object properties, such as created by user, created date, and matching the text in the search and folder names.

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
public async Task<bool> GetFilteredSearchContainerTreeAsync_Advanced__SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    //Search Container has a helper method where a user can pass filter(by string, by created/modified user and date, owner and etc.)

    //and will get back all search containers and searches that match the passed filter.

    bool success = false;

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            // Create sample data.

            int? searchContainerID;

            for (int i = 0; i < 6; i++)

            {

                Client.SamplesLibrary.Data.SearchContainerHelper.TryCreate(proxy, this.SampleWorkspace_ID, this.SampleUser_ID, out searchContainerID);

            }

            //Search filter

            var searchCondition = new SearchContainerTreeFilter() {

                SearchText = "API",

                CreatedById = SampleUser_ID,

                LastModifiedById = SampleUser_ID,

                OwnerId = SampleUser_ID,

                CreatedFrom = DateTime.UtcNow.AddDays(-1),

                LastModifiedFrom = DateTime.UtcNow.AddDays(-1),

                Keywords = "keyword",

                Notes = "notes"

            };

            SearchContainerItemCollection treeCollection =

            await proxy.GetFilteredSearchContainerTreeAsync(this.SampleWorkspace_ID, searchCondition);

            if (treeCollection.SavedSearchContainerItems != null || treeCollection.SearchContainerItems != null)

            {

                foreach (SearchContainerItem item in treeCollection.SearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the search container has item

                    // level security.

                    logger.LogDebug("{SearchContainerID} - {SearchContainerName}, Item-Secured: {Secured}",

                    item.SearchContainer.ArtifactID, item.SearchContainer.Name, item.Secured);

                }

                foreach (SavedSearchContainerItem item in treeCollection.SavedSearchContainerItems)

                {

                    // Display the ArtifactID and Name, if it is not display the error message, you can also check if the saved search has item

                    // level security and if it belongs to the current user.

                    logger.LogDebug(

                    "{SavedSearchID} - {SavedSearchName}, Item-Secured: {Secured}, IsOwner: {Personal}",

                    item.SavedSearch.ArtifactID, item.SavedSearch.Name, item.Secured, item.Personal);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting Filtered Search Container Tree was not successful");

            }

        }

        catch (ServiceException exception)

        {

            //Exceptions are returned as an ServiceException

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

## Retrieve Advanced Search View fields

The ISearchContainerManager interface provides these methods for working with the Advanced Search View fields:

- GetAdvancedSearchViewInfoAsync() - returns the available fields for advanced search filtering in the specified workspace. The fields information is returned as the AdvancedSearchViewInfo object. The object contains a list of field names and a flag indicating whether the user has the permissions to the view.

- GetAdvancedSearchViewUniqueCreatedByAsync() - returns the users that have created at least one saved search in the workspace.

- GetAdvancedSearchViewUniqueModifiedByAsync() - returns the users that have modified at least one saved search in the workspace.

- GetAdvancedSearchViewUniqueOwnersAsync() - return the users that are owners of at least one saved search in the workspace.

### GetAdvancedSearchViewInfoAsync()

The following code sample illustrates how to use the GetAdvancedSearchViewInfoAsync() method to return the available fields for advanced search filtering:

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

public async Task<bool> GetAdvancedSearchViewInfoAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            AdvancedSearchViewInfo result = await proxy.GetAdvancedSearchViewInfoAsync(SampleWorkspace_ID);

            if (result != null)

            {

                logger.LogDebug("HasViewPermission - {HasViewPermission}", result.HasViewPermission);

                foreach (string fieldName in result.FieldNames)

                {

                    logger.LogDebug("FieldName - {fieldName}", fieldName);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting advanced search view info was not successful");

            }

        }

        catch (ServiceException exception)

        {

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

### GetAdvancedSearchViewUniqueCreatedByAsync

The following code sample illustrates how to use the GetAdvancedSearchViewUniqueCreatedByAsync() method to return all users that have created at least one of saved searches in the workspace.

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

public async Task<bool> GetAdvancedSearchViewUniqueCreatedByAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            List<UserRef> result = await proxy.GetAdvancedSearchViewUniqueCreatedByAsync(SampleWorkspace_ID);

            if (result != null)

            {

                foreach (UserRef user in result)

                {

                    logger.LogDebug("{Name} - {ArtifactId}", user.Name, user.ArtifactID);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting the users that has created at least one of saved searches in workspace was not successful");

            }

        }

        catch (ServiceException exception)

        {

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

### GetAdvancedSearchViewUniqueModifiedByAsync()

The following code sample illustrates how to use the GetAdvancedSearchViewUniqueModifiedByAsync() method to return all users that have modified at least one of saved searches in the workspace.

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

   public async Task<bool> GetAdvancedSearchViewUniqueModifiedByAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            List<UserRef> result = await proxy.GetAdvancedSearchViewUniqueModifiedByAsync(SampleWorkspace_ID);

            if (result != null)

            {

                foreach (UserRef user in result)

                {

                    logger.LogDebug("{Name} - {ArtifactId}", user.Name, user.ArtifactID);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting the users that has modified at least one of saved searches in workspace was not successful");

            }

        }

        catch (ServiceException exception)

        {

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

### GetAdvancedSearchViewUniqueOwnersAsync()

The following code sample illustrates how to use the GetAdvancedSearchViewUniqueOwnersAsync() method to return all users that are owners of at least one saved search in the workspace.

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

public async Task<bool> GetAdvancedSearchViewUniqueOwnersAsync_SearchContainer(Client.SamplesLibrary.Helper.IHelper helper)

{

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            List<UserRef> result = await proxy.GetAdvancedSearchViewUniqueOwnersAsync(SampleWorkspace_ID);

            if (result != null)

            {

                foreach (UserRef user in result)

                {

                    logger.LogDebug("{Name} - {ArtifactId}", user.Name, user.ArtifactID);

                }

                success = true;

            }

            else

            {

                logger.LogError("Error: Getting the users that is an owners of at least one of saved searches in workspace was not successful");

            }

        }

        catch (ServiceException exception)

        {

            logger.LogError(exception, "Unhandled ServiceException");

        }

    }

    return success;

}
```

## Move SearchContainer

You can use the MoveAsync() method to move a saved search folder and all of its contents (subfolders and saved searches) to a different folder. This method requires that you pass the following parameters:

- Artifact ID of the workspace that contains the folder.

- Artifact ID of the folder that you want to move.

- Artifact ID of the destination folder.

You must have delete permission for saved search and search folder on the source search folder and add permissions for saved search and search folder on destination folder. If any of those is not met then a validation error is returned.

You can also use the overloaded constructors of MoveAsync() to pass the cancellation token and progress object as parameters to this method. The use of cancellation and progress reporting with the MoveAsync() method is similar to the processes followed by the ExecuteAsync() method on the Pivot Manager service.

The following code sample illustrates how to call the MoveAsync() method on the proxy, and pass the required parameters to it.

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
public bool SearchContainerMove(Client.SamplesLibrary.Helper.IHelper helper)

{

    kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

    bool success = false;

    using (ISearchContainerManager proxy = helper.GetServicesManager().CreateProxy<ISearchContainerManager>(ExecutionIdentity.User))

    {

        int? searchContainerIdToMove;

        bool searchContainerSuccess = SearchContainerHelper.TryCreate(proxy, SampleWorkspace_ID, out searchContainerIdToMove);

        if (!searchContainerSuccess)

        {

            logger.LogError("Could not create search container to move");

        }

        try

        {

            //Artifact ID of active workspace

            int workspaceArtifactId = SampleWorkspace_ID;

            int searchContainerToMoveArtifactID = searchContainerIdToMove.Value;

            int destinationContainerArtifactID = SampleSearchContainer_ID;

            SearchContainerMoveResultSet result = proxy.MoveAsync(workspaceArtifactId, searchContainerToMoveArtifactID, destinationContainerArtifactID).Result;

            if (!result.ProcessState.ToLowerInvariant().Contains("error"))

            {

                success = true;

                logger.LogInformation("ServiceHost call to SearchContainerManager.MoveAsync was successful. Returned ProcessState {ProcessState}", result.ProcessState);

            }

            else

            {

                logger.LogError("Error: ServiceHost call to SearchContainerManager.MoveAsync was not successful - {Message}", result);

            }

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Error: ServiceHost call to SearchContainerManager.MoveAsync was not successful");

            success = false;

        }

        return success;

    }

}
```

On this page

- Search Container Manager (.NET)

- Create a SearchContainer

- Read a SearchContainer

- Update a SearchContainer

- Delete a SearchContainer

- Query SearchContainers

- List SearchContainer content

- GetSearchContainerItemsAsync()

- GetChildSearchContainersAsync()

- Retrieve expanded search container nodes

- GetSearchContainerTreeAsync()

- GetFilteredSearchContainerTreeAsync()

- Retrieve Advanced Search View fields

- GetAdvancedSearchViewInfoAsync()

- GetAdvancedSearchViewUniqueCreatedByAsync

- GetAdvancedSearchViewUniqueModifiedByAsync()

- GetAdvancedSearchViewUniqueOwnersAsync()

- Move SearchContainer


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
