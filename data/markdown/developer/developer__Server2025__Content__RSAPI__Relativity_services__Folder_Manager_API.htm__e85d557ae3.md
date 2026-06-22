---
title: "Folder Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Relativity_services/Folder_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:26:20+00:00
sha256: e86147f91954a30273fc7e56b6ab617d9f623c3699e08d11cc32cbd21698e02f
---

Folder Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Folder Manager (.NET)

You can use the Folder Manager service to perform multiple operations for manipulating folder structures in the Relativity UI framework. You can use it to create, update, or move a folder, query for folders, retrieve the root or children in a folder tree, and delete empty folders. It also supports the progress monitoring for the deletion operation on folders.

You can also use the Folder Manager service to create, update, delete, and query for folders through the REST API. For more information, see Folders .

## Folder Manager service

The Relativity.Services.Folder namespace contains the IFolderManager interface and various classes used to manage folders. You use the IFolderManager interface to access the Folder Manager service, and the methods that it provides for working with folders. The interface contains the following methods:

- CreateSingleAsync() – used to add new folders under a parent or root folder.

- DeleteUnusedFoldersAsync() – This overloaded method allows you to pass the Artifact ID of the workspace where you want to delete all empty folders, or to pass the workspace Artifact ID and an IProgress object.

- GetWorkspaceRootAsync() – used to retrieve the root folder for a workspace.

- GetChildrenAsync() – used to retrieve the subfolders for a given folder.

- GetFolderTreeAsync() – This overloaded method requires you to pass the Artifact IDs of the workspace and the expanded folders, but you also have the option to pass the Artifact ID of a folder currently selected by a user. This method returns a list of folders.

- MoveFolderAsync() – used to move a folder and its children, including subfolders and documents. This method returns FolderMoveResultSet object, which contains status information about the move operation.

- QueryAsync() and QuerySubsetAsync() – The QueryAsync() method requires that you pass a workspace Artifact ID and Query object, but you also have the option of passing an integer for the number of results that you want returned. You can use the QuerySubsetAsync() method to retrieve a subset of folder instances in the results.

- UpdateSingleAsync() – used to update the name of a folder.

In addition, the Relativity.Services.Folder namespace also contains the following classes:

- FolderResultSet class - This class inherits properties from the QueryResultSet<T> class, which provides information about a query such as an error message when the query fails, the total number of Artifacts returned, and other properties.

- FolderMoveResultSet class - This class provides information about a specific move operation on a folder. It includes properties for the total number of operations that need to be execute for a folder move operation, and the number of operations currently completed. It also contains property that indicates the state of the move operation. For example, this property may contain string indicating that documents are currently being moved.

### Accessing the Folder Manager service

You access the IFolderManager interface through a client proxy to the API and by instantiating a FolderManager object. You can instantiate a FolderManager object with the ServiceFactory class as illustrated in the following code sample.

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

Uri keplerEndpoint = new Uri("http://localhost/Relativity.Rest/API");

Services.ServiceProxy.ServiceFactory serviceFactory = new Services.ServiceProxy.ServiceFactory(

    new Services.ServiceProxy.ServiceFactorySettings(

    keplerEndpoint,

    new Services.ServiceProxy.UsernamePasswordCredentials("username", "password")));

Services.Folder.IFolderManager proxy = serviceFactory.CreateProxy<Services.Folder.IFolderManager>();
```

In addition, you can instantiate a FolderManager object using the Relativity API Helpers. Use this approach if you want use the Folder Manager service from a custom page. For more information, see Use Relativity API Helpers .

Copy

```text
1
Relativity.Services.Folder.IFolderManager folderManager = Relativity.CustomPages.ConnectionHelper.Helper().GetServicesManager().CreateProxy<Relativity.Services.Folder.IFolderManager>(Relativity.API.ExecutionIdentity.System);
```

After you create the client proxy and instantiate a FolderManager object, you’re ready to create, update, or perform other operations on folders available through this service.

## Create a folder

To create a new folder, use the CreateSingleAsync() method as illustrated in the following code sample.

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
public static async Task CreateFolder_Async()

{

    int workspaceArtifactId = 1014823;

    string folderName = "New Case Documents";

    Services.Folder.Folder folderToCreate = new Services.Folder.Folder();

    folderToCreate.Name = folderName;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            int newFolderArtifactId = await folderManager.CreateSingleAsync(workspaceArtifactId, folderToCreate);

            string info = string.Format("Created dolder '{0}' with Artifact ID {1}", folderName, newFolderArtifactId);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update a folder

To update the name of a folder, use the UpdateSingleAsync() method as illustrated in the following code sample.

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
public static async Task UpdateFolder_Async()

{

    int workspaceArtifactId = 1014823;

    int folderArtifactId = 1039004;

    string updatedFolderName = "Jones case documents";

    Services.Folder.Folder updatedFolder = new Services.Folder.Folder();

    updatedFolder.ArtifactID = folderArtifactId;

    updatedFolder.Name = updatedFolderName;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            await folderManager.UpdateSingleAsync(workspaceArtifactId, updatedFolder);

            string info = string.Format("Renamed folder with Artifact ID {0} to '{1}'", folderArtifactId, updatedFolderName);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));



        }

    }

}
```

## Delete unused folders

To delete all empty folders in a workspace, use the DeleteUnusedFoldersAsync() method. This overloaded method provides you with the option to pass only the workspace Artifact ID, or the workspace Artifact ID and an object of the type System.IProgress provided by the .NET framework.

## Query for folders

To query for folders, implement a method that performs the tasks listed in the following sample code:

- Instantiate the Query object and construct the Condition object.

- Call the QueryAsync() method. Pass this method your workspace Artifact ID, the Query object., and optionally the query length value.

- Store the search results in a FolderResultSet object.

- Call the QuerySubsetAsync() method to page to return a subset of folder instances in the results.

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
public static async Task FolderQuery()

{

    /*

    * Possible query condition field names include:

    * ArtifactID

    * Name

    * ParentArtifactID

    * AccessControlListIsInherited

    * SystemCreatedBy

    * SystemCreatedByName

    * SystemCreatedOn

    * LastModifiedBy

    * SystemLastModifiedByName

    * SystemLastModifiedOn

    * SystemLastModifiedOn

    */

    Query query = new Services.Query();

    int length = 5;

    Condition queryCondition = new TextCondition("Name", Services.TextConditionEnum.StartsWith, "Jones Case");

    string queryString = queryCondition.ToQueryString();

    query.Condition = queryString;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            Services.Folder.FolderResultSet queryResults = await folderManager.QueryAsync(1014823, query, length);

            if (queryResults.Success)

            {

                // Loop through the search results and display successful search results.

                foreach (Services.Result<Services.Folder.FolderRef> result in queryResults.Results)

                {

                    // If the result was successful display the ArtifactID and Name, if it is not display the error message.

                    if (result.Success)

                    {

                        string info = string.Format("{0} - {1}", result.Artifact.ArtifactID, result.Artifact.Name);

                        Console.WriteLine(info);

                    }

                    else

                    {

                        string info = string.Format("Error: {0}", result.Message);

                        Console.WriteLine(info);

                    }

                }

                // If a QueryToken exists more results are available.

                int queryStartPosition = 1 + length;

                while (!string.IsNullOrEmpty(queryResults.QueryToken))

                {

                    // Query for the subset of query results.

                    queryResults = await folderManager.QuerySubsetAsync(queryResults.QueryToken, queryStartPosition, length);

                    // Repeat the same process to read results as seen in QueryAsync.

                    // Check to see if the query was successful.

                    if (queryResults.Success)

                    {

                        // Loop through the search results and display successful search results.

                        foreach (Services.Result<Services.Folder.FolderRef> result in queryResults.Results)

                        {

                            // If the result was successful display the ArtifactID and Name, if it is not display the error message.

                            if (result.Success)

                            {

                                string info = string.Format("{0} - {1}", result.Artifact.ArtifactID, result.Artifact.Name);

                                Console.WriteLine(info);

                            }

                            else

                            {

                                string info = string.Format("Error: {0}", result.Message);

                            }

                        }

                        // Shift the starting position.

                        queryStartPosition += length;

                    }

                    else

                    {

                        string info = string.Format("Error: QuerySubsetAsync was not successfull - {0}", queryResults.Message);

                    }

                }

            }

            else

            {

                string info = string.Format("Error: QueryAsync was not successfull - {0}", queryResults.Message);

                Console.WriteLine(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Helper methods

The Folder Manager service provides helper methods that simplify retrieving folders or traversing the folder tree.

### Retrieve the root Folder for a workspace

To retrieve the root folder for a workspace, call the GetWorkspaceRootAsync() on the proxy, and pass the workspace Artifact ID to the method as illustrated in the following code.

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
public static async Task WorkspaceRootFolder()

{

    int workspaceArtifactId = 1014823;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            Services.Folder.Folder rootFolder= await folderManager.GetWorkspaceRootAsync(workspaceArtifactId);

            string info = string.Format("Workspace [{0}] root folder Artifact ID is {1}", rootFolder.Name, rootFolder.ArtifactID);

            Console.Write(info);



        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));



        }

    }

}
```

### Retrieve subfolders

To retrieve subfolders, call the GetChildrenAsync() on the proxy, and pass the Artifact IDs of the workspace and required subfolders to the method as illustrated in the following code.

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
public static async Task FolderChildren()

{

    int workspaceArtifactId = 1014823;

    int folderArtifactId = 1039002;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            System.Collections.Generic.List<Services.Folder.Folder> children = await folderManager.GetChildrenAsync(workspaceArtifactId, folderArtifactId);

            foreach (Services.Folder.Folder subfolder in children)

            {

                string info = string.Format("{0} - {1}", subfolder.Name, subfolder.ArtifactID);

                Console.WriteLine(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Retrieve expanded Folder nodes

You can use the overloaded GetFolderTreeAsync() method to perform these tasks:

- Retrieve a folder structure that contains expanded nodes. The method returns an array of folders that are expanded.

- Retrieve a folder structure that contains expanded nodes and Artifact ID of the folder currently selected by a user. The method returns an array of folders.

You can use the GetFolderTreeAsync() method to retrieve information about specified expanded folders nodes as illustrated in the following code.

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
public async Task FolderTree()

{

    //Artifact ID of active workspace

    var workspaceArtifactId = 1014823;

    //Artifact IDs of selected folders

    var folderArtifactIds = new List<int> { 1039002, 1039003 };

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            List<Services.Folder.Folder> result = await folderManager.GetFolderTreeAsync(workspaceArtifactId, folderArtifactIds);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Retrieve ancestors of a Folder

You can also use the GetFolderTreeAsync() method to retrieve all expanded folder nodes and the currently selected folder node as illustrated in the following code.

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
public async Task FolderTreeWithSelected()

{

    //Artifact ID of active workspace

    var workspaceArtifactId = 1014823;

    //Artifact IDs of selected folders

   var folderArtifactIds = new List<int> { 1039002, 1039003 };

    //Specify the Artifact ID of a selected folder. Next, set the DTO property of the selected folder to retrieve all of its ancestors.

    var selectedFolderArtifactId = 1039003;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            List<Services.Folder.Folder> result = await folderManager.GetFolderTreeAsync(workspaceArtifactId, folderArtifactIds, selectedFolderArtifactId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Get access status for a Folder

The GetAccessStatusAsync() method returns the FolderStatus object that represents the user‘s ability to access a folder. The fields are as follows:

- Exists - indicates whether the folder exist.

- CanView - indicates whether the user has the permissions to view the folder.

This method requires that you pass the following parameters:

- Artifact ID of the workspace that contains the folder.

- Artifact ID of the folder.

This example illustrates how to use GetAccessStatusAsync():

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
public static async Task GetFolderStatus()

{

    int workspaceArtifactId = 1014823;

    int folderArtifactId = 1038002;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            Services.DataContracts.DTOs.Folder.FolderStatus folderAccessStatus = await folderManager.GetAccessStatusAsync(workspaceArtifactId, folderArtifactId);

            string info = string.Format("Folder exists: {0} \nUser has access: {1}", folderAccessStatus.Exists.ToString(), folderAccessStatus.CanView.ToString());

            Console.Write(info);



        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Move Folders

You can use the MoveFolderAsync() method to move a folder and its children, including subfolders and documents. This method requires that you pass the following parameters:

- Artifact ID of the workspace that contains the folder.

- Artifact ID of the folder that you want to move.

- Artifact ID of the destination folder.

You can also optionally pass the cancellation token and progress object as parameters to this method. The use of cancellation and progress reporting with the MoveFolderAsync() method is similar to the processes followed by the QueryAsync() method on the Object Manager (.NET) .

The following code sample illustrates how to the MoveFolderAsync() method on the proxy, and pass the required parameters to it.

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
public static async Task MoveFolder_Async()

{

    int workspaceArtifactId = 1014823;

    int folderArtifactId = 1038002;

    int destinationFolderArtifactId = 1039002;

    using (Services.Folder.IFolderManager folderManager = serviceFactory.CreateProxy<Services.Folder.IFolderManager>())

    {

        try

        {

            Services.Folder.FolderMoveResultSet folderMoveResult = await folderManager.MoveFolderAsync(workspaceArtifactId, folderArtifactId, destinationFolderArtifactId);

            string info = string.Format("Operations completed: {0} \nProcess state: {1}\nTotal operations: {2}", folderMoveResult.OperationsCompleted.ToString(), folderMoveResult.ProcessState.ToString(), folderMoveResult.TotalOperations.ToString());

            Console.Write(info);



        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

On this page

- Folder Manager (.NET)

- Folder Manager service

- Accessing the Folder Manager service

- Create a folder

- Update a folder

- Delete unused folders

- Query for folders

- Helper methods

- Retrieve the root Folder for a workspace

- Retrieve subfolders

- Retrieve expanded Folder nodes

- Retrieve ancestors of a Folder

- Get access status for a Folder

- Move Folders


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
