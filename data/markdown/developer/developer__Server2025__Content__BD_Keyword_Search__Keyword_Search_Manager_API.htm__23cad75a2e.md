---
title: "Keyword Search Manager (.NET) for saved searches"
url: https://platform.relativity.com/Server2025/Content/BD_Keyword_Search/Keyword_Search_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:19+00:00
sha256: 1a20cb4e33a6e03f14592f51e8cb68dfb3448792b48e2b23a8f4b1ce053450d8
---

Keyword Search Manager (.NET) for saved searches

# Keyword Search Manager (.NET) for saved searches

A keyword search (or SQL index search) is the default search engine in Relativity. You can use a keyword search to query a full text index and to interact with save searches. For more information, see Keyword search on the Relativity Documentation site.

The Keyword Search Manager API supports the create, read, update, delete, and query operations on a KeywordSearch DTO. It also includes helper methods to facilitate returning saved search parameters available to the user in the workspace, such as fields, search owners, search indexes are also provided. You can also generate email links to the search results. The operations on KeywordSearch DTOs are performed asynchronously. Note that asynchronous operations return a standard .NET System.Threading.Tasks.Task<TResult> object that can be used to monitor progress and interact with the process.

You can also use the Keyword Search API through REST. For more information, see Keyword Search Manager (REST) for saved searches .

## KeywordSearch properties

The following KeywordSearch object properties correspond to the keyword search properties that can be specified through the Relativity user interface (shown in the images below). For code samples of setting the properties, see Create a KeywordSearch and KeywordSearch helper methods .

- ArtifactID - ArtifactID of the saved search object.

- ArtifactTypeID - Artifact Type ID of the object to be returned by the search. Currently only Document is supported. Use ArtifactType enumeration to set the value. This is a required property when creating and updating saved searches.

- Name - descriptive name of the saved search. This is a required property when creating and updating saved searches.

- Includes - the field for identifying documents related to the documents matching the search criteria. The related documents will be included in the result set alongside with the documents that match the search criteria. Use the GetSearchIncludesAsync helper method to return the property value.

- Scope - The scope of the search (entire repository or selected folders) specified as a ScopeType enumeration.

ScopeType enumeration values

Member name Value Description

EntireCase 0 Search the entire workspace.

Folders 1 Search folders.

Subfolders 2 Search subfolders

- SearchFolders - if folders or subfolders are specified as the Scope value, the folders to be included in the search.

- RequiresManualRun - requires users to rerun a saved search when they return to it to ensure up-to-date search results.

- Dashboard - the dashboard associated with the saved search.

- SearchText - search terms.

- SortByRank – indicates that the search results must be sorted by rank.

- SearchCriteria - search conditions specified as a CriteriaCollection object.

- Fields - the fields to be included in the search result set specified as a collection of Field objects. Use the GetFieldsForSearchResultViewAsync helper method to return the property value. This is a required property when creating and updating saved searches.

- Sorts - sort order for search results specified as a Sorts object.

- Keywords - an optional field where extra group information may be recorded.

- Notes - detailed description of the saved search.

- QueryHint - string parameter used to optimize views. Only use the query hint if instructed by the kCura Client Services team. Currently, you can use Hashjoin:(true/false) or Maxdrop:(x) to populate the field.

- RelativityApplications - Relativity applications that use the saved search.

- Owner - user(s) who can access the saved search. Setting the value to 0 enables all users with permissions to the saved search are able to see it. Use the GetSearchOwnersAsync helper method to return the property value.

- SearchContainer - the saved search folder. If no value is specified, the search will be saved at the logical root of the saved search view.

- SystemCreatedBy - ArtifactID of the user who created the search.

- SystemCreatedOn - date and time in UTC when the search was created.

- SystemLastModifiedBy - ArtifactID of the user who last modified the search.

- SystemLastModifiedOn - date and time in UTC when the search was last modified.

## Create a KeywordSearch

You can create KeywordSearch objects asynchronously by using the CreateAsync() method of the IKeywordSearchManager interface.

The following code sample illustrates how to create a KeywordSearch DTO. Note the use of the GetResultFields() method to return all available workspace fields as the resultFields.FieldsNotIncluded property. This is accomplished by specifying the workspace ID and 0 as the dtSearch ArtifactID as GetResultFields() parameters. For more information, see Helper methods . Subsequently the Edit, File Icon, Doc ID Beg, Email Subject, and Artifact ID are included as the search result fields. The results are sorted by ArtifactID (ascending) and Date Sent (descending). CreateAsync() returns System.Threading.Tasks.Task<TResult>.

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
public static async Task<bool> CreateKeywordSearchAsync(IKeywordSearchManager proxy, int folderID, int workspaceID, string folderName)

{

    bool success = false;

    try

    {

        SearchContainerRef searchFolder = new SearchContainerRef();

        searchFolder.Name = folderName;

        searchFolder.ArtifactID = folderID;

        KeywordSearch search = new KeywordSearch();

        search.Name = "My KeywordSearch";

        search.SearchContainer = searchFolder;

        int artifactType = 10;

        // Get all the query fields available to the current user.

        SearchResultViewFields resultFields = await proxy.GetFieldsForSearchResultViewAsync(workspaceID, artifactType);

        FieldRef field;

        // Set the owner to the current user, in this case "Admin, Relativity," or "0" for public.

        List<UserRef> searchOwners = await proxy.GetSearchOwnersAsync(workspaceID);

        search.Owner = searchOwners.First(o => o.Name == "Public");

        // Add the fields to the Fields collection.

        // If a field Name, ArtifactID, Guid, or ViewFieldID is known, a field can be set with that information as well.

        field = resultFields.FieldsNotIncluded.First(f => f.Name == "Edit");

        search.Fields.Add(field);

        field = resultFields.FieldsNotIncluded.First(f => f.Name == "File Icon");

        search.Fields.Add(field);

        field = resultFields.FieldsNotIncluded.First(f => f.Name == "Control Number");

        search.Fields.Add(field);

        // Create a Criteria for the field named "Extracted Text" where the value is set

        Criteria criteria = new Criteria();

        criteria.Condition = new CriteriaCondition(new FieldRef()

        {

            Name = "Control Number"

        }, CriteriaConditionEnum.IsSet);

        // Add the search condition criteria to the collection.

        search.SearchCriteria.Conditions.Add(criteria);

        // Search for the text string "John" with a fuzziness level of 5 and stemming enabled.

        search.SearchText = "John";

        search.Notes = "Generated by API";

        // Add a note.

        search.Notes = "This is my new KeywordSearch";

        search.ArtifactTypeID = 10;

        // Create the search.

        int createSuccess = await proxy.CreateSingleAsync(workspaceID, search);

        if (createSuccess != 0)

        {

            success = true;

            Console.WriteLine("Successfully created KeywordSearch with ArtifactID: " + createSuccess);

        }

        else

        {

            Console.WriteLine("Failed to create the search!");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine("Failure " + ex.ToString());

        return false;

    }

    return success;

}
```

To associate a keyword search with a Relativity dashboard, use the Dashboard property of the search object:

Copy

```text
1
2
//Associate with dashboard.

search.Dashboard = new Services.DashboardObject.DashboardRef(this.SampleDashboardArtifact_ID);
```

## Read KeywordSearch

The following code sample illustrates how to read a KeywordSearch DTO using the ReadSingleAsync() method of the IKeywordSearchManager interface.

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
public static async Task<bool> ReadKeywordSearchAsync(IKeywordSearchManager proxy, int searchID, int workspaceID)

{

    bool success = false;

    try

    {

        KeywordSearch readSuccess = await proxy.ReadSingleAsync(workspaceID, searchID);

        if (readSuccess.ArtifactID != 0)

        {

            success = true;

            Console.WriteLine("Details for: {0}", readSuccess.Name);

            Console.WriteLine("Artifact ID: {0}", readSuccess.ArtifactID);

            Console.WriteLine("Parent Folder Name: {0}", readSuccess.SearchContainer.Name);

        }

        else

        {

            Console.WriteLine("Failed to read");

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine(ex);

    }

    return success;

}
```

## Update KeywordSearch

The following code sample illustrates how to update a KeywordSearch using the UpdateSingleAsync() method of the IKeywordSearchManager interface.

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
public async Task<bool> UpdateSingleKeywordSearchAsync(IKeywordSearchManager proxy, int searchID, int workspaceID)

{

    bool success = false;

    try

    {

        // Read the search object.

        KeywordSearch search = await proxy.ReadSingleAsync(workspaceID, searchID);

        // Modify search properties.

        search.Name = "My KeywordSearch Updated";

        // Add a search criteria to the search.

        search.SearchCriteria.Conditions.Add(new Criteria()

        {

            Condition = new CriteriaCondition(new FieldRef("Control Number"),

            CriteriaConditionEnum.IsLike,

            "ABC")

        });

        // Add a result field to the search.

        search.Fields.Add(new FieldRef("Responsive"));

        // Update the search.

        await proxy.UpdateSingleAsync(workspaceID, search);

        success = true;

    }

    catch (Exception ex)

    {

        Console.WriteLine(ex);

    }

    return success;

}
```

## Delete KeywordSearch

You can delete KeywordSearch DTOs using the DeleteSingleAsync() method of the IKeywordSearchManager interface.

The following code sample illustrates how to delete a keyword search.

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
public static async Task<bool> DeleteSingleKeywordSearchAsync(IKeywordSearchManager proxy, int searchID, int workspaceID)

{

    bool success = false;

    try

    {

        await proxy.DeleteSingleAsync(workspaceID, searchID);

        success = true;

    }

    catch (Exception ex)

    {

        Console.WriteLine(ex);

    }

    return success;

}
```

## Query KeywordSearches

The following code sample illustrates how to query KeywordSearch DTOs using the QueryAsync() and QuerySubset() methods of the of the IKeywordSearchManager interface. The query condition checks if the search name starts with the string "My". If the query returns a token value that is not null, more results are available than initially specified in the length property, and they are subsequently retrieved by using the QuerySubsetAsync() method. When the length parameter is not specified, its value defaults to 0, and the number of returned results defaults to the Instance setting table value of PDVDefaultQueryCacheSize of 10000.

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
public static async Task<bool> QueryKeywordSearchAsync(IKeywordSearchManager proxy, int searchID, int workspaceID)

{

    bool success = false;

    try

    {

        // Create a new instance of a Query.

        Query query = new Query();

        // Define the search length. This is the number of results to be returned.

        // If more results are available the search results will contain a query key that can be used with QuerySubsetAsync

        int length = 5;

        // Define the search condition for the query.  Conditions can be created programmatically using Conditions and converted

        // to a query string using the ToQueryString extension method that the query conditions accepts.

        Condition queryCondition = new TextCondition("Name", TextConditionEnum.StartsWith, "My");

        string queryString = queryCondition.ToQueryString();

        query.Condition = queryString;

        // Create an instance of a Sort and define how this query is to be sorted.

        Sort sortBy = new Sort();

        sortBy.FieldIdentifier.Name = "ArtifactID";

        sortBy.Order = 0;

        sortBy.Direction = SortEnum.Descending;

        query.Sorts.Add(sortBy);

        // Query for search objects given the above query condition and sort order.

        KeywordSearchQueryResultSet queryResultSet = await proxy.QueryAsync(workspaceID, query, length);

        // Check to see if the query was successful.

        if (queryResultSet.Success)

        {

            // Loop through the search results and display successful search results.

            foreach (Result<KeywordSearch> result in queryResultSet.Results)

            {

                // If the result was successful display the ArtifactID and Name, if it is not display the error message.

                if (result.Success)

                {

                    Console.WriteLine("{0} - {1}", result.Artifact.ArtifactID, result.Artifact.Name);

                }

                else

                {

                    Console.WriteLine("Error: {0}", result.Message);

                }

            }

            // If a QueryToken exists more results are available.

            int queryStartPosition = 1 + length;

            while (!string.IsNullOrEmpty(queryResultSet.QueryToken))

            {

                // Query for the subset of query results.

                queryResultSet = await proxy.QuerySubsetAsync(workspaceID, queryResultSet.QueryToken, queryStartPosition, length);

                // Repeat the same process to read results as seen in QueryAsync.

                // Check to see if the query was successful.

                if (queryResultSet.Success)

                {

                    // Loop through the search results and display successful search results.

                    foreach (Result<KeywordSearch> result in queryResultSet.Results)

                    {

                        // If the result was successful display the ArtifactID and Name, if it is not display the error message.

                        if (result.Success)

                        {

                            Console.WriteLine("{0} - {1}", result.Artifact.ArtifactID, result.Artifact.Name);

                        }

                        else

                        {

                            Console.WriteLine("Error: {0}", result.Message);

                        }

                    }

                    // Shift the starting position.

                    queryStartPosition += length;

                }

                else

                {

                    Console.WriteLine("Error: QuerySubsetAsync was not successfull - {0}", queryResultSet.Message);

                }

            }

        }

        else

        {

            Console.WriteLine("Failed to Query " + queryResultSet.Message);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine("Failed to Query " + ex);

    }

    return success;

}
```

## Helper methods

The IKeywordSearchManager interface provides the following asynchronous helper methods to return workspace parameters for populating keyword saved search properties:

- GetFieldsForSearchResultViewAsync - returns the SearchResultViewFields object. If an ArtifactID of an existing search is specified as an input parameter, the fields included in the saved search are returned as the SearchResultViewFields.FieldsIncluded property. If no search Artifact ID is specified, then all workspace fields available to the user are returned as SearchResultViewFields.FieldsNotIncluded property. Use to populate the Fields property.

- GetSearchIncludesAsync - returns all relational fields available to the user in the workspace. Use to populate the Includes property.

- GetSearchOwnersAsync - returns all users in the workspace with permissions to view saved searches. Use to populate the Owners property.

- GetFieldsForCriteriaConditionAsync - returns all workspace fields available to the user that can be included in a saved search condition as a list of Field objects.

- GetFieldsForObjectCriteriaCollectionAsync - returns all workspace fields available to the user that can be specified as a subcondition for a given field in a saved search condition. Use to populate field values for batch and multi-object conditions.

- GetAccessStatusAsync - returns the SearchAccessStatus object with the information about the user‘s ability to access the saved search. The fields include:

- Exists – indicates whether the search exists relative to the specified folder path.

- CanView – indicates whether the user has view permissions to the search.

- CanAccessSearchProvider – indicates whether the user has view permissions to the search provider used in the saved search.

- CanViewCriteriaFields – indicates whether the user has view permissions to all of the fields used in the saved search.

The following example illustrates how to use the helper methods to return the fields, indexes, search owners, and relational fields available in the workspace.

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
public static async Task<bool> KeywordSearchHelpersAsync(IKeywordSearchManager proxy, int workspaceID)

{

    bool success = false;

    // Sets the artifact type to Document.

    int artifactType = 10;

    try

    {

        // Make calls to get information, then display it.

        List<UserRef> searchOwners = await proxy.GetSearchOwnersAsync(workspaceID);

        List<FieldRef> searchIncludes = await proxy.GetSearchIncludesAsync(workspaceID);

        SearchResultViewFields resultFields = await proxy.GetFieldsForSearchResultViewAsync(workspaceID, artifactType);

        List<FieldRef> searchConditionFields = await proxy.GetFieldsForCriteriaConditionAsync(workspaceID, artifactType);

        foreach (UserRef owner in searchOwners)

        {

            Console.WriteLine("Owner: {0} - {1}", owner.ArtifactID, owner.Name);

        }

        foreach (FieldRef include in searchIncludes)

        {

            Console.WriteLine("Include: {0} - {1}", include.ArtifactID, include.Name);

        }

        foreach (FieldRef fieldNotIncluded in resultFields.FieldsNotIncluded)

        {

            Console.WriteLine("Field: {0} - {1}", fieldNotIncluded.ArtifactID, fieldNotIncluded.Name);

        }

        foreach (FieldRef searchConditionField in searchConditionFields)

        {

            Console.WriteLine("SearchConditionField: {0} - {1}", searchConditionField.ArtifactID, searchConditionField.Name);

        }

        // Find a SearchConditionField that contains sub conditions. ("Batch" contains sub conditions) then display results.

        FieldRef batchField = searchConditionFields.Where(x => x.Name == "Batch").FirstOrDefault();

        List<FieldRef> subConditionFieldsForConditionField = await proxy.GetFieldsForObjectCriteriaCollectionAsync(workspaceID, batchField, artifactType);

        foreach (FieldRef subConditionField in subConditionFieldsForConditionField)

        {

            Console.WriteLine("SubConditionField: {0} - {1}", subConditionField.ArtifactID, subConditionField.Name);

        }

        success = true;

    }

    catch (Exception ex)

    {

        Console.WriteLine(ex);

    }

    return success;

}
```

The following example illustrates how to use GetAccessStatusAsync(). When calling the method, specify the workspace Artifact ID, the saved search Artifact ID, and a collection of Artifact ID representing the folder path where the search resides.

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
public static async Task<bool> GetKeywordSearchAccessStatusAsync(IKeywordSearchManager proxy, int workspaceID, int searchID)

{

    bool success = false;

    try

    {

        List<int> searchAncestorsIDs = new List<int>();

        SearchAccessStatus accessStatus = await proxy.GetAccessStatusAsync(workspaceID, searchID, searchAncestorsIDs);

        Console.WriteLine("Access information for: {0}\r\nCan Access: {1}\r\nCan view: {2}", searchID, accessStatus.CanAccessSearchProvider, accessStatus.CanView);

        success = true;

    }

    catch (Exception ex)

    {

        Console.WriteLine(ex);

    }

    return success;

}
```

With GetAccessStatusAsync(), you can also specify an empty collection of ancestor Artifact IDs to test the existence of the search not relative of any folder structure.

## Email a link to KeywordSearch

Relativity allows you to generate an email link to saved search results. IKeywordSearchManager interface provides the GetEmailToLinkUrlAsync() method to return an email link to the search results.

In order for GetEmailToLinkUrlAsync() to return results, the EmailLinkURLOverride configuration option must be enabled. For more information, see Instance settings' descriptions on the Relativity Server 2025 Documentation site.

This example illustrates how to use the GetEmailToLinkUrlAsync method to return the email link to a KeywordSearch.

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
public static async Task<bool> GetEmailToKeywordSearchLinkUrlAsync(IKeywordSearchManager proxy, int workspaceID, int searchID)

{

    bool success = false;

    // Try to get the email link for the specified saved search.

    try

    {

        string emailToLinkUrl = await proxy.GetEmailToLinkUrlAsync(workspaceID, searchID);

        string unescapeDataString = Uri.UnescapeDataString(emailToLinkUrl);

        Console.WriteLine(unescapeDataString);

        success = true;

    }

    catch (Exception ex)

    {

        Console.WriteLine(ex);

    }

    return success;

}
```

## Move KeywordSearch

You can use the MoveAsync() method to move a KeywordSearch to a different folder. This method requires that you pass the following parameters:

- Artifact ID of the workspace that contains the search.

- Artifact ID of the search that you want to move.

- Artifact ID of the destination folder.

You must have delete permission for saved search and search folder on the source search folder and add permissions for saved search and search folder on destination folder. If any of those is not met then a validation error is returned.

The SavedSearchMoveResultSet.ProcessState object returned by the operation can have these values:

- Creating destination container hierarchy

- Creating search batches

- Moving saved searches

- Error

- Completed

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
public static async Task<bool> MoveKeywordSearchAsync(IKeywordSearchManager proxy, int workspaceID, int searchToMoveID, int targetFolderID)

{

    bool success = false;

    try

    {

        SavedSearchMoveResultSet result = await proxy.MoveAsync(workspaceID, searchToMoveID, targetFolderID);

        if (!result.ProcessState.ToLowerInvariant().Contains("error"))

        {

            success = true;

            Console.WriteLine("ServiceHost call to KeywordSearchManager.MoveAsync was successful. Returned ProcessState {0}", result.ProcessState);

        }

        else

        {

            Console.WriteLine("Error: ServiceHost call to KeywordSearchManager.MoveAsync was not successful - {Message}", result);

        }

    }

    catch (Exception ex)

    {

        Console.WriteLine("Error: ServiceHost call to KeywordSearchManager.MoveAsync was not successful\r\n{0}", ex);

        success = false;

    }

    return success;

}
```

## Copy KeywordSearch

You can use the CopySingleAsync() method to make of a copy of an existing . The copy is created in the same saved search folder location as the original. The method returns a SavedSearchRef object with the Artifact ID and the name of the copy. The name of the copy is based on the name of the original with an incremented number in brackets, for example Jones Case Documents (1) .

This method requires that you pass the following parameters:

- Artifact ID of the workspace that contains the .

- Artifact ID of the .

The following code sample illustrates how to call the CopySingleAsync() method on the proxy:

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
public static async Task<bool> CopySingleKeywordSearchAsync(IKeywordSearchManager proxy, int workspaceID, int searchID)

{

    bool success = false;

    try

    {

        SavedSearchRef savedSearchCopy = await proxy.CopySingleAsync(workspaceID, searchID);

        Console.WriteLine("ServiceHost call to KeywordSearchManager was successful - Created {0}", savedSearchCopy.Name);

        success = true;

    }

    catch (Exception ex)

    {

        Console.WriteLine("ServiceHost call to KeywordSearchManager was not successful - {0}", ex);

        success = false;

    }

    return success;

}
```

## Exception handling

Use kCura.Kepler.Exceptions.ServiceException and kCura.Kepler.Exceptions.ValidationException when interacting with saved search.

### ServiceException

When a saved search operation results in an error, it throws a kCura.Kepler.Exceptions.ServiceException, which inherits from the System.Exception class. This Kepler exception class has a Message property, which contains the error that the save search operation threw. It uses the Data property to populate the ResultSet<T> or the WriteResultSet<T> objects with information about the error returned from the underlying CRUD operation. Since the Data object is a dictionary, Relativity retrieves the information from this object using the index of the result set.

The code samples on this page illustrate how to use the kCura.Kepler.Exceptions.ServiceException.

### ValidationException

kCura.Kepler.Exceptions.ValidationException is thrown when invalid input (for example, a query condition) cannot be serialized or deserialized.
