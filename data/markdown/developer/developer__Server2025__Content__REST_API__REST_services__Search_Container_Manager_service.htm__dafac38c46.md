---
title: "Search Container Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/REST_API/REST_services/Search_Container_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:28:05+00:00
sha256: 06b3d087e5e32616f5f2fb1fe1aa57ab639db8e01a9b9341163ee403819338cc
---

Search Container Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# Search Container Manager (REST)

The Relativity REST API supports operations with saved search folders through SearchContainer objects of the SearchContainer Manager service. The operations available through the service are equivalent to the asynchronous methods for interacting with the saved search folders in the Relativity Services API. For more information, see SearchContainer in the Services API documentation.

You can only use the POST method when interacting with the service.

## Client code sample

The following is an example of .NET REST code for creating a SearchContainer. The code can be used for all SearchContainer Manager service operations with different endpoint URLs and input JSON values.

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
//Set up the REST client.



HttpClient httpClient = new HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set the required headers.



httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");

//Call Create for a SearchContainer.



string url = "/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/CreateSingleAsync";

StringContent content = new StringContent(CreateInputJSON, Encoding.UTF8, "application/json");

HttpResponseMessage response = httpClient.PostAsync(url, content).Result;

string result = response.Content.ReadAsStringAsync().Result;

bool success = HttpStatusCode.Created == response.StatusCode;

//Parse the result with Json.NET.



JObject resultObject = JObject.Parse(result);
```

## Create

Use this SearchContainer Manager service URL to create a SearchContainer:

Copy

```text
1
/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/CreateSingleAsync
```

The request must include a workspace ArtifactID and a valid JSON representation of a SearchContainer DTO. The required properties include Name and ParentArtifactID (parent folder ID). The root saved search folder is specified by setting the value of ParentArtifactID to 0.

You can only use the ArtifactID of the Choice to set the SearchContainer status value.

Sample JSON request for creating a SearchContainer Copy

```text
1
2
3
4
5
6
7
{

  "workspaceArtifactID": 13758822,

  "searchContainer": {

    "Name": "Privileged documents",

    "parentSearchContainer":{"ArtifactID":0}

  }

}
```

The response is an ArtifactID of the created SearchContainer.

## Read

Use this SearchContainer Manager service URL to read a SearchContainer:

Copy

```text
1
/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/ReadSingleAsync
```

The request must include the workspace ArtifactID and the SearchContainer ArtifactID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 13759995,

  "searchContainerArtifactID": 1038661

}
```

The response returns a JSON representation of a SearchContainer DTO.

Click to display JSON response Copy

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
{

  "ParentSearchContainer": {

    "ArtifactID": 1035243,

    "Name": "Tuchman vs Marsh case documents"

  },

  "SystemCreatedBy": {

    "ArtifactID": 9,

    "Name": "Admin, Relativity"

  },

  "SystemCreatedOn": "2015-01-08T23:53:20.58",

  "SystemLastModifiedBy": {

    "ArtifactID": 9,

    "Name": "Admin, Relativity"

  },

  "SystemLastModifiedOn": "2015-01-08T23:53:46.59",

  "ArtifactID": 1038661,

  "Name": "Marsh documents"

}
```

## Update

Use this SearchContainer Manager service URL to update a SearchContainer:

Copy

```text
1
/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/UpdateSingleAsync
```

The request must include a workspace ArtifactID and a valid JSON representation of a SearchContainer DTO.

You must include all DTO field information in the update. You cannot update individual fields because fields left empty will be cleared on the update. All DTO fields are required except for system/user created by/created on.

The following JSON sample illustrates how to change the Name of the folder created in a previous example and move it to a different folder.

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
{

  "workspaceArtifactID": 13759995,

  "searchContainer": {

    "ParentSearchContainer": {

      "ArtifactID": 1038661

    },

    "ArtifactID": 1038661,

    "Name": "Tuchman and Marsh documents"

  }

}
```

The response does not contain any data. Success for failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Delete

Use this SearchContainer Manager service URL to delete a SearchContainer:

Copy

```text
1
/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/DeleteSingleAsync
```

The request must include the workspace ID and the SearchContainer ArtifactID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 13759995,

  "searchContainerArtifactID": 1038661

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Query

The SearchContainer Manager service URL for querying SearchContainer:

Copy

```text
1
/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/QueryAsync
```

The request must include the query and optionally the number of results to return as the length property. The following is an example of a query for SearchContainer objects with the name starting with "P". The result set is sorted by ArtifactID in descending order.

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
{

  "workspaceArtifactID": 13759995,

  "query": {

    "Condition": "'Name' STARTSWITH 'P'",

    "Sorts": [

      {

        "FieldIdentifier": {

          "Name": "ArtifactID"

        },

        "Order": 0,

        "Direction": 1

      }

    ]

  },

  "length": 5

}
```

If more results are available than initially specified in the length property, the query returns a token value that is not null. The results can subsequently be retrieved by a call to the QuerySubsetAsync operation.

Copy

```text
1
/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/QuerySubsetAsync
```

Note that the QuerySubsetAsync request can specify the starting index of the result subset and the number of results to be returned.

Copy

```text
1
2
3
4
5
{

  "queryToken": "a5079c32-e080-473d-846e-941ef6a5f086",

  "start": 6,

  "length": 5

}
```

To return all Clients in a Relativity instance, specify an empty Condition as shown in the JSON example below. When the length parameter is not specified, its value defaults to 0, and the number of returned results defaults to the Instance setting table value PDVDefaultQueryCacheSize of 10000. For more information, see Search Relativity .

Copy

```text
1
2
3
4
{

 "workspaceArtifactID": 13758822,

 "query": {}

}
```

The response returns a collection of SearchContainer objects as a ClientQueryResultSet object.

Click to display JSON response Copy

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
{

  "QueryToken": "a5079c32-e080-473d-846e-941ef6a5f086",

  "TotalCount": 7,

  "Success": true,

  "Message": "",

  "Results": [

    {

      "Success": true,

      "Artifact": {

        "ParentSearchContainer": {

          "ArtifactID": 1035243,

          "Name": "Tuchman vs Marsh Case"

        },

        "SystemCreatedBy": {

          "ArtifactID": 9,

          "Name": "Admin, Relativity"

        },

        "SystemCreatedOn": "2015-01-09T01:17:21.117",

        "SystemLastModifiedBy": {

          "ArtifactID": 9,

          "Name": "Admin, Relativity"

        },

        "SystemLastModifiedOn": "2015-01-09T01:17:25.903",

        "ArtifactID": 1038664,

        "Name": "Pro bono"

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "ParentSearchContainer": {

          "ArtifactID": 1035243,

          "Name": "Tuchman vs Marsh Case"

        },

        "SystemCreatedBy": {

          "ArtifactID": 9,

          "Name": "Admin, Relativity"

        },

        "SystemCreatedOn": "2015-01-09T00:37:58.697",

        "SystemLastModifiedBy": {

          "ArtifactID": 9,

          "Name": "Admin, Relativity"

        },

        "SystemLastModifiedOn": "2015-01-09T00:37:58.697",

        "ArtifactID": 1038663,

        "Name": "Privileged documents"

      },

      "Message": "",

      "WarningMessages": []

    }

  ] ...

}
```

## Move

You can move a saved search folder and all of its content, including saved searches and subfolders, to a different folder. Send a request to this Search Container Manager service URL:

Copy

```text
1
/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/MoveAsync
```

The request must contain the following fields:

- workspaceArtifactID – the Artifact ID for the workspace where the saved search folder resides.

- artifactID – the Artifact ID of the folder.

- destinationContainerID – the Artifact ID of the target saved search folder.

You must have delete permission for saved search and search folder on the source search folder and add permissions for saved search and search folder on destination folder. If any of those is not met then a validation error is returned.

Copy

```text
1
2
3
4
5
6

{

   "workspaceArtifactID": 1015024,

   "artifactID": 1039180,

   "destinationContainerID": 1039178

}
```

The response returns the following fields:

- ProcessState - a message that indicates the current operation executing on the folder being moved. The values can include:

- Creating destination container hierarchy.

- Creating search batches.

- Moving saved searches.

- Error

- Completed

- TotalOperations - equals the sum of the number of searches to be moved and the number of folder references to be updated.

- OperationsCompleted - indicates the number of operations that have been executed.

Copy

```text
1
2
3
4
5
6

{

   "TotalOperations": 1,

   "ProcessState": "Completed",

   "OperationsCompleted": 1

}
```

Unlike the Services API, the Search Container Manager Service doesn’t support use of progress indicators or cancellation tokens.

## Get folder content

The SearchContainer Manager Service provides these helper operations for retrieving the content of a saved search folder.

- GetSearchContainerItemsAsync – returns the saved searches and subfolders in a specified saved search folder.

- GetChildSearchContainersAsync – returns the subfolders in a specified saved search folder.

### GetSearchContainerItemsAsync

Use this SearchContainer Manager service URL to return the content of a SearchContainer including saved searches and subfolders:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetSearchContainerItemsAsync
```

The request must include the workspace ID and the folder object identified by the ArtifactID. The root saved search folder is specified by setting the value of ArtifactID to 0.

Copy

```text
1
2
3
4
5
6
{

  "workspaceArtifactID": 13759995,

  "searchContainer": {

  "ArtifactID": 0

  }

}
```

The response includes the SearchContainerItems (subfolders) and SavedSearchContainerItems (saved searches) collections.

Click to display JSON response Copy

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
{

  "SearchContainerItems": [

    {

      "SearchContainer": {

        "ArtifactID": 1038661,

        "Name": "Marsh case documents"

      },

      "Secured": false

    },

    {

      "SearchContainer": {

        "ArtifactID": 1038659,

        "Name": "Tuchman case documents"

      },

      "Secured": false

    }

  ],

  "SavedSearchContainerItems": [

    {

      "SavedSearch": {

        "ArtifactID": 1036361,

        "Name": "Produced Documents",

        "SearchType": "KeywordSearch"

      },

      "Secured": true,

      "Personal": true

    }

  ]

}
```

### GetChildSearchContainersAsync

Use this SearchContainer Manager service URL to return the only subfolders in a SearchContainer:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetChildSearchContainersAsync
```

The request must include the workspace ID and the folder object identified by the ArtifactID.

Copy

```text
1
2
3
4
5
6
{

  "workspaceArtifactID": 13759995,

  "searchContainer": {

  "ArtifactID": 1039018

  }

}
```

The response includes the SearchContainerItems (subfolders) and SavedSearchContainerItems (saved searches) collections. The SavedSearchContainerItems collection is always empty.

Click to display JSON response Copy

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
{

  "SearchContainerItems": [

    {

      "SearchContainer": {

        "ArtifactID": 1039031,

        "Name": "Marsh case documents"

      },

      "Secured": false,

      "Permissions": {

        "AddSearch": true,

        "EditSearch": true,

        "AddSearchFolder": true,

        "EditSearchFolder": true,

        "SecureSearchFolder": true,

        "DeleteSearchFolder": true

      },

      "HasChildren": false

    },

    {

      "SearchContainer": {

        "ArtifactID": 1039019,

        "Name": "Tuchman documents"

      },

      "Secured": false,

      "Permissions": {

        "AddSearch": true,

        "EditSearch": true,

        "AddSearchFolder": true,

        "EditSearchFolder": true,

        "SecureSearchFolder": true,

        "DeleteSearchFolder": true

      },

      "HasChildren": true

    }

  ],

  "SavedSearchContainerItems": []

}
```

## Retrieve expanded search container nodes

The Search Container Manager service provides these helper operations that simplify traversing search containers in a tree structure:

- GetSearchContainerTreeAsync – retrieves information about a list of expanded search container nodes as a SearchContainerItemCollection object. For example, you can use this method to render an expanded browser tree for a saved search.

- GetFilteredSearchContainerTreeAsync – retrieves information about search container nodes where the name matches the specified condition. The method returns a SearchContainerItemCollection object.

### GetSearchContainerTreeAsync

To retrieve information about expanded search containers, send a POST request to this URL for the Search Container Manager service:

Copy

```text
1
/relativity.rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetSearchContainerTreeAsync
```

The request includes the following fields:

- workspaceArtifactId – the Artifact ID of the workspace that you want to query.

- expandedNodes – a list of Artifact IDs of specified containers. You want to retrieve information about these expanded search containers.

For example, you might want to retrieve information about the children of the expanded root folder called Relativity Starter Template and another folder called Folder 1 as illustrated in the following screen shot:

You would query for this information by sending the following request, where the expandedNodes property contains a list of Artifact IDs, which includes those for the Relativity Starter Template and Folder 1:

For more information about the starter template, see Starter template on the Relativity Server 2025 Documentation site.

Copy

```text
1
2
3
4
{

    "workspaceArtifactID": 1015024,

    "expandedNodes": [1035243, 1039255]

}
```

This response returns a list of children of all expanded saved search containers and saved searches for each expanded container.

View the JSON response for all expanded containers Copy

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
{

    "SearchContainerItems": [{

        "SearchContainer": {

            "ArtifactID": 1035243,

            "Name": "Relativity Starter Template"

        },

        "Secured": false,

        "HasChildren": true,

        "ParentContainer": {

            "ArtifactID": 1003663

        }

    }, {

        "SearchContainer": {

            "ArtifactID": 1038050,

            "Name": "Admin Searches"

        },

        "Secured": false,

        "HasChildren": true,

        "ParentContainer": {

            "ArtifactID": 1035243

        }

    }, {

        "SearchContainer": {

            "ArtifactID": 1039255,

            "Name": "Folder 1"

        },

        "Secured": false,

        "HasChildren": true,

        "ParentContainer": {

            "ArtifactID": 1035243

        }

    }, {

        "SearchContainer": {

            "ArtifactID": 1039259,

            "Name": "Folder 2"

        },

        "Secured": false,

        "HasChildren": true,

        "ParentContainer": {

            "ArtifactID": 1035243

        }

    }, {

        "SearchContainer": {

            "ArtifactID": 1044569,

            "Name": "Folder 1.1"

        },

        "Secured": false,

        "HasChildren": false,

        "ParentContainer": {

            "ArtifactID": 1039255

        }

    }],

    "SavedSearchContainerItems": [

        {

        "SavedSearch": {

            "ArtifactID": 1039240,

            "Name": "Search",

            "SearchType": "KeywordSearch"

        },

        "Secured": true,

        "Personal": true,

        "ParentContainer": {

            "ArtifactID": 1035243

        }

    }]

}
```

### GetFilteredSearchContainerTreeAsync

To return the tree items where the name matches the specified string, send a POST request to this URL for the Search Container Manager service:

Copy

```text
1
/relativity.rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetFilteredSearchContainerTreeAsync
```

The request includes the following fields:

- workspaceArtifactId – the Artifact ID of the workspace that you want to query.

- searchCondition – the search string to be matched.

Copy

```text
1
2
3
4
{

    "workspaceArtifactID": 1015024,

    "searchCondition": "Tuchman"

}
```

You can also specify the condition as a filter object with properties to be matched, such as created by user, created date, and matching the text in the search and folder names:

- searchText – search string for matching the saved search and search folder names.

- CreatedById – the user that created the saved search or saved search folder.

- OwnerId – the user(s) who can access the saved search. Setting the ArtifactID value to 0 enables all users with permissions to the saved search are able to see it.

- CreatedFrom – the date of the creation from which to search.

- LastModifiedById – the last user to modify the saved search or saved search folder.

- LastModifiedFrom – the date of the last modification from which to search.

- Keywords – the text for matching the saved search or search folder keywords.

- Notes – the text for matching the saved search or search folder notes.

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
{

  "workspaceArtifactID": 1180604,

  "filter": {

    "SearchText": "Tuchman",

    "CreatedById": 1031220,

    "OwnerId": 1031220,

    "CreatedFrom": "2017-06-01T10:59:17.2957462Z",

    "LastModifiedById": 1031220,

    "LastModifiedFrom": "2017-06-01T10:59:17.2957462Z",

    "Keywords": "keywords",

    "Notes": "notes"

  }

}
```

This response returns a list of children of all expanded saved search containers and saved searches for each expanded container.

Click to display JSON response Copy

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

{

  "SearchContainerItems": [

    {

      "SearchContainer": {

        "ArtifactID": 1035243,

        "Name": "Tuchman Case Doc Workspace"

      },

      "Secured": false,

      "Permissions": {

        "AddSearch": true,

        "EditSearch": true,

        "AddSearchFolder": true,

        "EditSearchFolder": true,

        "SecureSearchFolder": true,

        "DeleteSearchFolder": true

      },

      "HasChildren": true,

      "ParentContainer": {

        "ArtifactID": 1003663

      }

    },

    {

      "SearchContainer": {

        "ArtifactID": 1141190,

        "Name": "Tuchman Case Docs"

      },

      "Secured": false,

      "Permissions": {

        "AddSearch": true,

        "EditSearch": true,

        "AddSearchFolder": true,

        "EditSearchFolder": true,

        "SecureSearchFolder": true,

        "DeleteSearchFolder": true

      },

      "HasChildren": true,

      "ParentContainer": {

        "ArtifactID": 1035243

      }

    }

  ],

  "SavedSearchContainerItems": [

    {

      "SavedSearch": {

        "ArtifactID": 1141187,

        "Name": "Tuchman Case - New",

        "SearchType": "DataGridSearch"

      },

      "Secured": true,

      "Permissions": {

        "AddSearch": true,

        "EditSearch": true,

        "SecureSearch": false,

        "DeleteSearch": true

      },

      "Personal": true,

      "ParentContainer": {

        "ArtifactID": 1141190

      }

    },

    {

      "SavedSearch": {

        "ArtifactID": 1141189,

        "Name": "Tuchman Case - Old",

        "SearchType": "DataGridSearch"

      },

      "Secured": true,

      "Permissions": {

        "AddSearch": true,

        "EditSearch": true,

        "SecureSearch": false,

        "DeleteSearch": true

      },

      "Personal": true,

      "ParentContainer": {

        "ArtifactID": 1141190

      }

    }

  ]

}
```

## Retrieve Advanced Search View fields

The Search Container Manager service provides these helper operations for working with the Advanced Search View fields:

- GetAdvancedSearchViewInfoAsync - returns the available fields for advanced search filtering in the specified workspace.

- GetAdvancedSearchViewUniqueCreatedByAsync - returns the users that have created at least one saved search in the workspace.

- GetAdvancedSearchViewUniqueModifiedByAsync - returns the users that have modified at least one saved search in the workspace.

- GetAdvancedSearchViewUniqueOwnersAsync - return the users that are owners of at least one saved search in the workspace.

### GetAdvancedSearchViewInfoAsync

To return the available fields for advanced search filtering in the specified workspace, send a POST request to this URL for the Search Container Manager service:

Copy

```text
1
/relativity.rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetAdvancedSearchViewInfoAsync
```

The request must include the workspace Artifact ID:

Copy

```text
1
2
3
{

    "workspaceArtifactID": 1015024

}
```

This response contains a list of field names and a flag indicating whether the user has the permissions to the view.

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
{

  "HasViewPermission": true,

  "FieldNames": [

    "Edit",

    "TextIdentifier",

    "FullPath",

    "EmailTo"

  ]

}
```

### GetAdvancedSearchViewUniqueCreatedByAsync

To return a list of users that have created at least one saved search in the workspace, send a POST request to this URL for the Search Container Manager service:

Copy

```text
1
/relativity.rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetAdvancedSearchViewUniqueCreatedByAsync
```

The request must include the workspace Artifact ID:

Copy

```text
1
2
3
{

    "workspaceArtifactID": 1015024

}
```

This response contains a collection of user reference objects:

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
[

  {

    "ArtifactID": 1088397,

    "Name": "Doe, Jane"

  },

  {

    "ArtifactID": 1088398,

    "Name": "Doe, John"

  },

  {

    "ArtifactID": 777,

    "Name": "Service Account, Relativity"

  }

]
```

### GetAdvancedSearchViewUniqueModifiedByAsync

To return a list of users that have modified at least one saved search in the workspace, send a POST request to this URL for the Search Container Manager service:

Copy

```text
1
/relativity.rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetAdvancedSearchViewUniqueModifiedByAsync
```

The request must include the workspace Artifact ID:

Copy

```text
1
2
3
{

    "workspaceArtifactID": 1015024

}
```

This response contains a collection of user reference objects:

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
[

  {

    "ArtifactID": 1088398,

    "Name": "Doe, John"

  },

  {

    "ArtifactID": 777,

    "Name": "Service Account, Relativity"

  }

]
```

### GetAdvancedSearchViewUniqueOwnersAsync

To return a list of users that are owners of at least one saved search in the workspace, send a POST request to this URL for the Search Container Manager service:

Copy

```text
1
/relativity.rest/api/Relativity.Services.Search.ISearchModule/Search%20Container%20Manager/GetAdvancedSearchViewUniqueOwnersAsync
```

The request must include the workspace Artifact ID:

Copy

```text
1
2
3
{

    "workspaceArtifactID": 1015024

}
```

This response contains a collection of user reference objects:

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
[

  {

    "ArtifactID": 1088397,

    "Name": "Doe, Jane"

  },

  {

    "ArtifactID": 1088398,

    "Name": "Doe, John"

  }

]
```

On this page

- Search Container Manager (REST)

- Client code sample

- Create

- Read

- Update

- Delete

- Query

- Move

- Get folder content

- GetSearchContainerItemsAsync

- GetChildSearchContainersAsync

- Retrieve expanded search container nodes

- GetSearchContainerTreeAsync

- GetFilteredSearchContainerTreeAsync

- Retrieve Advanced Search View fields

- GetAdvancedSearchViewInfoAsync

- GetAdvancedSearchViewUniqueCreatedByAsync

- GetAdvancedSearchViewUniqueModifiedByAsync

- GetAdvancedSearchViewUniqueOwnersAsync


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
