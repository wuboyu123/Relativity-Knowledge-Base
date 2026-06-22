---
title: "ViewCondition"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Searching_Relativity/ViewCondition.htm
collection: developer
fetched_at: 2026-06-22T06:33:28+00:00
sha256: e2a2a00a94c158d0f84a0991a29b98c5f44ef76e8420ceb225f25f77482865de
---

ViewCondition

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# ViewCondition

You can use the ViewCondition to execute a view so that you can review its contents. To execute this query, you need the ArtifactID of the view stored in Relativity. You can then execute the query by using the ViewCondition on the Query() method.

## Supported objects for ViewCondition

You can use ViewCondition when querying all Relativity objects types except these workspace and admin objects.

Workspace:

- Choice

- BatchSet

- RelativityScript

Admin:

- Choice

- RelativityScript

- Workspace

## SelectedFields directive

You can set the SelectedFields directive when you perform a query with SavedSearchCondition or a ViewCondition. The SelectedFields directive returns only the Fields displayed on a saved search or view in Relativity. The following sample code illustrates how to use this directive.

Copy

```text
1
2

query.Fields = Field.SelectedFields;
```

You aren't limited to the Fields defined by the saved search or view when using a SavedSearchCondition or a ViewCondition. Instead, you can specify particular Fields that you want to retrieve, or you can use the AllFields directive to retrieve all Fields for an ArtifactType, such as View, User, or Document.

## Search with a ViewCondition

You can query for the ArtifactID of a View and then set a the ViewCondition to it. When the query executes, it retrieves the objects in the view. The following sample illustrates how to retrieve documents in a view with all fields available on a Document objects:

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

public static bool Query_And_Execute_By_ViewID(IRSAPIClient proxy)

{

     //STEP 1: If you don't have the ArtifactID of a View, you can query to find it.

     var query = new DTOs.Query<View>();

    query.Condition = new TextCondition(ViewFieldNames.Name, TextConditionEnum.EqualTo, "Documents");

    DTOs.QueryResultSet<View> result = null;

    try

    {

        result = client.Repositories.View.Query(query);

    }

    catch (Exception ex)

    {

        Console.WriteLine($"An error occurred: {ex.Message}");

        return;

    }

    //Save the ArtifactID of the returned view.

    var viewID = result.Results[0].Artifact.ArtifactID;

    //STEP 2: Create a new Query to execute the View.

    var executeViewQuery = new Query<DTOs.Document>();

    //STEP 3: Set a ViewCondition used to pass the ArtifactID of the View.

    executeViewQuery.Condition = new ViewCondition(viewID);

    executeViewQuery.Fields = FieldValue.AllFields;

    //STEP 4: Call the Query method on the Document Repository.

    // - See the Object Type column in Views for the repository that aligns to your View.

    DTOs.QueryResultSet<DTOs.Document> executeViewResult = null;

    try

    {

        executeViewResult = client.Repositories.Document.Query(executeViewQuery, 5);

    }

    catch (Exception ex)

    {

        Console.WriteLine($"An error occurred: {ex.Message}");

        return;

    }

    //Check for success.

    if (executeViewResult.Success)

    {

        Console.WriteLine("Retrieved first 5 documents from View 'Documents':");

        foreach (Result<DTOs.Document> document in executeViewResult.Results)

        {

            Console.WriteLine("Document Text Identifier: {0}", document.Artifact.TextIdentifier);

        }

    }

    else

    {

        Console.WriteLine("Error retrieving documents.");

    }

}
```

This is another example of ViewCondition-based query for documents. The result set includes only the fields selected by the view:

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

using System;

using kCura.Relativity.Client;

using kCura.Relativity.Client.DTOs;

public class A

{

     public static void Query_Documents_By_Document_View_ID_Using_Repository(IRSAPIClient proxy)

     {

          //STEP 1: Create a Query to describe the search you want to run.

          DTOs.Query<DTOs.Document> query = new DTOs.Query<DTOs.Document>();

          //STEP 2: Set Condition. For this example, Relativity contains a view with an ArtifactID of 1003689.

          query.Condition = new ViewCondition(1003689);

          //STEP 3: Set the SelectedFields directive to retrieve the fields defined by the view.

          query.Fields = DTOs.FieldValue.SelectedFields;

          //STEP 4: Perform the query.

          DTOs.ResultSet<DTOs.Document> docResults = proxy.Repositories.Document.Query(query);

     }

}
```
