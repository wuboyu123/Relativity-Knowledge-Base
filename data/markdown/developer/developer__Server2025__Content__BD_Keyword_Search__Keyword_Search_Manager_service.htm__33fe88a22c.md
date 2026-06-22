---
title: "Keyword Search Manager (REST) for saved searches"
url: https://platform.relativity.com/Server2025/Content/BD_Keyword_Search/Keyword_Search_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:24:26+00:00
sha256: dda47273fff5b84f5a5c2b1d5ead06a986341da5b3fccc38f66741aef9421ed8
---

Keyword Search Manager (REST) for saved searches Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Keyword Search Manager (REST) for saved searches

A keyword search (or SQL index search) is the default search engine in Relativity. You can use a keyword search to query a full text index and to interact with save searches. For more information, see Keyword search on the Relativity Documentation site.

The Keyword Search Manager API supports the create, read, update, delete, and query operations on a KeywordSearch DTO. It also includes helper methods to facilitate returning saved search parameters available to the user in the workspace, such as fields, search owners, search indexes are also provided. You can also generate email links to the search results.

You can also use the Keyword Search Manager service through .NET. For more information, see Keyword Search Manager (.NET) for saved searches .

## Client code sample

The following is an example of .NET REST client for creating a keyword saved search. The code can be used for all Keyword Search Manager Service operations with different endpoint URLs and input JSON values.

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
//Set up the client.



HttpClient httpClient = new HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set the required headers.



httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");

//Call Create for a SavedSearch.



string url = "Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/Create";

StringContent content = new StringContent(CreateInputJSON, Encoding.UTF8, "application/json");

HttpResponseMessage response = httpClient.PostAsync(url, content).Result;

string result = response.Content.ReadAsStringAsync().Result;

bool success = HttpStatusCode.Created == response.StatusCode;

//Parse the result with Json.NET.



JObject resultObject = JObject.Parse(result);
```

## Create

Use this Keyword Search Manager Service URL to create a keyword search:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/CreateSingleAsync
```

The request must include a workspace ID and valid JSON representation of a KeywordSearch DTO.

Required KeywordSearch DTO properties include ArtifactTypeID, Name, and Fields.

The response is an Artifact ID of the created search.

The following are JSON examples for creating keyword saved searches.

Simple keyword search Copy

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
{

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactTypeID": 10,

    "Name": "My New Keyword Search",

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

Keyword search with a fixed length condition Copy

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
{

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactTypeID": 10,

    "Name": "My New Keyword Search With Condition",

    "SearchCriteria": {

      "Conditions": [

        {

          "Condition": {

            "Operator": "Is",

            "FieldIdentifier": { "Name": "FixedLengthField" },

            "Value": "abc",

            "ConditionType": "Criteria"

          }

        }

      ]

    },

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

Keyword search with two conditions Copy

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

 {

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactTypeID": 10,

    "Name": "My New Keyword Search With Two Conditions",

    "SearchCriteria": {

      "Conditions": [

        {

          "Condition": {

            "Operator": "Is",

            "FieldIdentifier": { "Name": "FixedLengthField" },

            "Value": "abc",

            "NotOperator": false,

            "ConditionType": "Criteria"

          },

          "BooleanOperator": "Or"

        },

        {

          "Condition": {

            "Operator": "AnyOfThese",

            "FieldIdentifier": { "Name": "SingleChoiceField" },

            "Value": [

              112233,

              987987

            ],

            "ConditionType": "Criteria"

          }

        }

      ]

    },

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

Keyword search with grouped conditions (A or B) and C Copy

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

 {

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactTypeID": 10,

    "Name": "My New Keyword Search With Nested Conditions",

    "SearchCriteria": {

      "Conditions": [

        {

          "Conditions": [

            {

              "Condition": {

                "Operator": "AnyOfThese",

                "FieldIdentifier": { "Name": "SingleChoiceField" },

                "Value": [

                  112233,

                  987987

                ],

                "ConditionType": "Criteria"

              },

              "BooleanOperator": "Or"

            },

            {

              "Condition": {

                "Operator": "Is",

                "FieldIdentifier": { "Name": "YesNoField" },

                "Value": true,

                "ConditionType": "Criteria"

              },

              "BooleanOperator": "None"

            }

          ],

          "BooleanOperator": "And"

        },

        {

          "Condition": {

            "Operator": "Is",

            "FieldIdentifier": { "Name": "FixedLengthField" },

            "Value": "abc",

            "ConditionType": "Criteria"

          }

        }

      ]

    },

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

Keyword search with a date condition Copy

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
{

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactTypeID": 10,

    "Name": "My New Keyword Search With Date Condition",

    "SearchCriteria": {

      "Conditions": [

        {

          "Condition": {

            "Operator": "Between",

            "Month": "NotSet",

            "FieldIdentifier": { "Name": "Date Field" },

            "Value": [

              "2015-08-01T00:00:00",

              "2015-08-15T00:00:00"

            ],

            "ConditionType": "CriteriaDate"

          }

        }

      ]

    },

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

Keyword search condition referencing a multiple object field Copy

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
{

  "workspaceArtifactID": 1015976,

  "searchDTO": {

    "ArtifactId": "1039032",

    "ArtifactTypeID": 10,

    "Name": "Sample Saved Search",

    "SearchCriteria": {

      "Conditions": [

        {

          "Conditions": [

            {

              "Condition": {

                "Operator": "In",

                "FieldIdentifier": {

                  "Name": "Email Domains"

                },

                "Value": {

                  "Conditions": [

                    {

                      "Condition": {

                        "Operator": "AllOfThese",

                        "FieldIdentifier": {

                          "Name": "Email Domains"

                        },

                        "Value": [

                          1039027,

                          1039028

                        ],

                        "ConditionType": "Criteria"

                      }

                    }

                  ]

                },

                "ConditionType": "Criteria"

              }

            }

          ]

        }

      ]

    },

    "Fields": [

      {

        "Name": "Email Domains"

      }

    ]

  }

}
```

Keyword search with associated Relativity dashboard

Beginning in October 2017, you can associate saved keyword searches with Relativity dashboards using the Dashboard property of the search.

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
{

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactID":1044254,

    "ArtifactTypeID": 10,

    "Dashboard": {

        "ArtifactID":1044273,

        "Name":"Sample Dashboard",

        "Guid":"e5fbf747-fe80-4d26-8821-8a7d0ba00171"

    },

    "Name": "Sample Keyword Search",

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

### Search condition criteria

The CriteriaCondition object represents a condition for a single non-date Relativity field. The following table describes the allowed CriteriaCondition values for each type of field.

Field Type

CriteriaCondtionEnum

Value Type

Notes

Text

AnyOfThese

List<int> or int[]

Text

IsSet

null

Text

Is, IsLike, LessThan, GreaterThan, StartsWith, EndsWith

String

Text

Contains

String

Allowed when Include in Text is true and Open to Associations is false.

Yes/No

IsSet

null

Yes/No

Is

bool

Single Choice

IsSet

null

Single Choice

AnyOfThese

List<int> or int[]

List<Guid> or Guid[]

Multiple Choice

IsSet

null

Multiple Choice

AnyOfThese, AllOfThese

List<int> or int[]

List<Guid> or Guid[]

Single Object

IsSet

null

Single Object

AnyOfThese

List<int> or int[]

List<Guid> or Guid[]

Single Object

IsLike

String

Single Object

LessThan, GreaterThan

String

NotOperator cannot be set to true.

Multiple Object

In

CriteriaCollection

The value is another set of criteria defined by instantiating a new CriteriaCollection.

Batch

In

CriteriaCollection

The value is another set of criteria defined by instantiating a new CriteriaCollection.

Multiple Object, Batch condition value

IsSet

null

NotOperator cannot be set to true

Multiple Object, Batch condition value

AnyOfThese, AllOfThese

List<int> or int[]

List<Guid> or Guid[] (for Multiple Object)

Multiple Object, Batch condition value

IsLIke

String

Multiple Object, Batch

LessThan, GreaterThan

String

NotOperator cannot be set to true

Number (Whole Number, Currency, Decimal)

IsSet

null

Number (Whole Number, Currency, Decimal)

Is, GreaterThan, LessThan

A valid number.

User

IsLoggedInUser

null

NotOperator cannot be set to true

User

IsSet

null

User

AnyOfThese

List<int> or int[]

Extracted Text or Full Text

Contains

String

Saved Search

In

int

The CriteriaDateCondition object represents a condition for a single date-type Relativity field. The following table presents value types corresponding to CriteriaDateCondition.

CriteriaDateConditionEnum

Value Type

Notes

IsSet

null

Is, IsBefore, IsBeforeOrOn, IsAfter, IsAfterOrOn

DateTime

Between

List<DateTime> or DateTime[]

Must contain two DateTime objects.

In

DateTimeRange enumeration

If DateTimeRange = MonthOf then Month must be set from the Month enumeration.

## Read

Use this Keyword Search Manager Service URL to read a keyword search:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/ReadSingleAsync
```

The request must include the workspace ID and the keyword saved search Artifact ID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 1030160,

  "searchArtifactID": 1038891

}
```

The response returns a JSON representation of a KeywordSearch DTO.

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
{

  "ArtifactID": 1039076,

  "ArtifactTypeID": 10,

  "Name": "My New Keyword Search With Two Conditions",

  "SearchContainerID": 1035243,

  "Owner": 0,

  "Includes": 0,

  "Scope": 0,

  "SearchFolders": [],

  "RequiresManualRun": false,

  "SearchCriteria": {

    "Conditions": [

      {

        "Condition": {

          "Operator": "Is",

          "FieldIdentifier": {

            "ArtifactID": 0,

            "ViewFieldID": 1000567,

            "Guids": [],

            "Name": "Email Subject"

          },

          "Value": "abc",

          "NotOperator": false,

          "Identifier": null,

          "ConditionType": "Criteria"

        },

        "Operator": 2

      },

      {

        "Condition": {

          "Operator": "Is",

          "FieldIdentifier": {

            "ArtifactID": 0,

            "ViewFieldID": 1000643,

            "Guids": [],

            "Name": "Conversation Family"

          },

          "Value": "987987",

          "NotOperator": false,

          "Identifier": null,

          "ConditionType": "Criteria"

        },

        "Operator": 0

      }

    ],

    "Operator": 0

  },

  "Fields": [

    {

      "ArtifactID": 1003668,

      "ViewFieldID": 1000187,

      "Guids": [

        "58d35076-1b1d-43b4-bff4-d6c089de51b2"

      ],

      "Name": "Extracted Text"

    }

  ],

  "Sorts": [],

  "QueryHint": "",

  "SortByRank": false,

  "SearchText": "",

  "Keywords": "",

  "Notes": "",

  "SystemCreatedBy": {

    "ArtifactID": 1271248,

    "Name": "Doe, Jane"

  },

  "SystemCreatedOn": "2014-09-25T20:29:53.697",

  "SystemLastModifiedBy": {

    "ArtifactID": 1271248,

    "Name": "Doe, Jane"

  },

  "SystemLastModifiedOn": "2014-09-25T20:29:53.697"

}
```

## Update

Use this Keyword Search Manager Service URL to update a keyword search:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/UpdateSingleAsync
```

The request must include a workspace ID and a valid JSON representation of a KeywordSearch DTO.

You must include all DTO field information in the update. You cannot update individual fields because fields left empty will be cleared on the update. All DTO fields are required except for system/user created by/created on.

The following JSON sample illustrates how to add fields and sort to the keyword search created in a previous example.

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

{

  "workspaceArtifactID": 1030160,

  "searchDTO": {

    "ArtifactID": 1038573,

    "ArtifactTypeID": 10,

    "Name": "My New Keyword Search",

    "Fields": [

      {

        "Name": "Doc ID Beg"

      },

      {

        "Name": "Author"

      },

      {

        "Name": "Extracted Text"

      }

    ],

    "Sorts": [

      {

        "FieldIdentifier": {

          "Name": "Doc ID Beg"

        },

        "Order": 0,

        "Direction": 1

      }

    ]

  }

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Delete

Use this Keyword Search Manager Service URL to update a keyword search:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/DeleteSingleAsync
```

The request must include the workspace ID and the keyword saved search Artifact ID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 1030160,

  "searchArtifactID": 1038661

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Query

The Keyword Search Manager Service URL for querying keyword searches:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/QueryAsync
```

The request must include the workspace ID, the query, and length (the number of results to be returned) specified as an integer.

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

{

  "workspaceArtifactID": 1030160,

  "query": {

    "Condition": "'Name' STARTSWITH 'My'",

    "Sorts": [

      {

        "FieldIdentifier": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

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
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/QuerySubsetAsync
```

Note that the QuerySubsetAsync request can specify the starting index of the result subset and the number of results to be returned.

Copy

```text
1
2
3
4
5
6
{

  "workspaceArtifactID": 1030160,

  "queryToken": "d0aff8bf-321d-4600-8240-dba2f0173b1d",

  "start": 6,

  "length": 5

}
```

## Move

You can move a keyword saved search to a different folder. Send a request to this Keyword Search Manager service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/MoveAsync
```

The request must contain the following fields:

- workspaceArtifactID – the Artifact ID for the workspace where the search resides.

- artifactID – the Artifact ID of the search.

- destinationContainerID - the Artifact ID of the target saved search folder.

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

- ProcessState - a message that indicates the current operation executing on the search being moved. The values can include:

- Moving saved searches.

- Error

- Completed

- TotalOperations - equals the sum of the number of moved objects.

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

Unlike the Services API, the Keyword Search Manager Service doesn’t support use of progress indicators or cancellation tokens.

## Copy

You can create a copy of an existing keyword saved search in the same saved search folder. Send a request to this Keyword Search Manager service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/CopySingleAsync
```

The request must contain the following fields:

- workspaceArtifactID – the Artifact ID for the workspace where the saved search resides.

- artifactID – the Artifact ID of the search

Copy

```text
1
2
3
4
5

{

   "workspaceArtifactID": 1015024,

   "searchArtifactID": 1036361

}
```

This creates a copy of an existing search in the same location. The name of the copy is based on the name of the original with an incremented number in brackets, for example New Case Documents (3) .

The response returns the saved search reference object the with following fields:

- ArtifactID - the Artifact ID of the copy.

- Name - the name of the copy.

Copy

```text
1
2
3
4
{

    "ArtifactID": 1041178,

    "Name": "New Case Documents (3)"

}
```

## Helper operations

The Keyword Search Manager Service provides the following helper operations for retrieving search properties:

- GetEmailToLinkUrlAsync

- GetFieldsForCriteriaConditionAsync

- GetFieldsForObjectCriteriaCollectionAsync

- GetFieldsForSearchResultViewAsync

- GetSearchIncludesAsync

- GetSearchOwnersAsync

- GetAccessStatusAsync

### GetEmailToLinkUrlAsync

The Keyword Search Manager Service URL for retrieving an email link to keyword search results:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/GetEmailToLinkUrlAsync
```

The request must include the workspace ID and the search Artifact ID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 1030160,

  "searchArtifactID": 1039106

}
```

The response is the string value of the email link.

Copy

```text
1
"mailto:?subject=Relativity%20Review%20-%20Integration%20Tests%20-%20My%20New%20Keyword%20Search%20With%20Two%20Conditions&body=http%3a%2f%2fmyhost%2frelativity%2fsearchlink.aspx%3fSelectedSearchArtifactID%3d1039106%26AppID%3d1275015"
```

### GetFieldsForCriteriaConditionAsync

The Keyword Search Manager Service URL for retrieving all workspace fields available to the user that can be included in a saved search conditions criteria:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/GetFieldsForCriteriaConditionAsync
```

The request must include the workspace ID and the search artifact type ID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 1275015,

  "artifactTypeID": 10

}
```

Currently only Document can be specified as the artifact type.

The response is a collection of Field objects.

Click to display the JSON response sample Copy

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
[

  {

    "ArtifactID": 0,

    "ViewFieldID": 1000471,

    "Guids": [],

    "Name": "(Saved Search)"

  },

  {

    "ArtifactID": 1038302,

    "ViewFieldID": 1001175,

    "Guids": [

      "664fa808-6579-425c-929d-eaa2b096b2da"

    ],

    "Name": "Analytics Index"

  },

  {

    "ArtifactID": 1003676,

    "ViewFieldID": 1000195,

    "Guids": [

      "0a51edfc-846b-47c5-8319-08e637c19be3"

    ],

    "Name": "Artifact ID"

  },

  {

    "ArtifactID": 1037988,

    "ViewFieldID": 1001028,

    "Guids": [],

    "Name": "Attachment Document IDs"

  },

  {

    "ArtifactID": 1037987,

    "ViewFieldID": 1001027,

    "Guids": [],

    "Name": "Attachment Name"

  },

  {

    "ArtifactID": 1035344,

    "ViewFieldID": 1000544,

    "Guids": [

      "1c7eb349-929e-467e-8b42-4b7c045e1fa1"

    ],

    "Name": "Author"

  },

  {

    "ArtifactID": 1035250,

    "ViewFieldID": 1000422,

    "Guids": [

      "d7a9d9fd-68fc-4c85-ad44-ba524a0ca872"

    ],

    "Name": "Batch"

  },

  {

    "ArtifactID": 1035345,

    "ViewFieldID": 1000545,

    "Guids": [

      "6e3e65e7-1382-49ea-8960-455bd88655f7"

    ],

    "Name": "Bates Beg"

  },

  {

    "ArtifactID": 1035373,

    "ViewFieldID": 1000572,

    "Guids": [

      "4946a783-90e3-4acb-8171-f915e5b6fe5a"

    ],

    "Name": "Bates Beg Attach"

  },

  {

    "ArtifactID": 1035346,

    "ViewFieldID": 1000546,

    "Guids": [

      "6dcd3bd1-aa7a-478a-897e-b5712e38c409"

    ],

    "Name": "Bates End"

  },

  {

    "ArtifactID": 1035372,

    "ViewFieldID": 1000571,

    "Guids": [

      "cf4232be-5e98-4975-8f9c-323ea8ab87d1"

    ],

    "Name": "Bates End Attach"

  },

  {

    "ArtifactID": 1035347,

    "ViewFieldID": 1000547,

    "Guids": [

      "72893a43-1d4e-4aff-a579-3bf5e734b98f"

    ],

    "Name": "Categories"

  },

  {

    "ArtifactID": 1035348,

    "ViewFieldID": 1000548,

    "Guids": [

      "33b7f3d4-6f95-440a-92d8-3d9c06a9baf5"

    ],

    "Name": "Comments"

  },

  {

    "ArtifactID": 1035349,

    "ViewFieldID": 1000549,

    "Guids": [

      "c1da1863-b420-4bc3-a439-02d72c1794e7"

    ],

    "Name": "Conversation"

  },

  {

    "ArtifactID": 1035456,

    "ViewFieldID": 1000643,

    "Guids": [

      "14ffb8be-42d1-419e-b72c-645484a78a83"

    ],

    "Name": "Conversation Family"

  },

  ...

]
```

### GetFieldsForObjectCriteriaCollectionAsync

The request must include the workspace ID, a multi-object Field, and the search artifact type ID.

Copy

```text
1
2
3
4
5
{

  "workspaceArtifactID": 1275015,

  "field":{"Name": "Batch"},

  "artifactTypeID": 10

}
```

The response is a collection of Field objects.

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
[

  {

    "ArtifactID": 1035250,

    "ViewFieldID": 1000422,

    "Guids": [

      "d7a9d9fd-68fc-4c85-ad44-ba524a0ca872"

    ],

    "Name": "Batch"

  },

  {

    "ArtifactID": 1035251,

    "ViewFieldID": 1000423,

    "Guids": [

      "8c3ea95d-6c72-4463-8696-1b6859c0e00e"

    ],

    "Name": "Batch::Batch Set"

  },

  {

    "ArtifactID": 1035252,

    "ViewFieldID": 1000424,

    "Guids": [

      "3e62303c-b955-4a93-b82a-894ce40b5563"

    ],

    "Name": "Batch::Assigned To"

  },

  {

    "ArtifactID": 1035253,

    "ViewFieldID": 1000425,

    "Guids": [

      "70e1751f-4f6b-4c1d-abd7-8a6328750175"

    ],

    "Name": "Batch::Status"

  }

]
```

### GetFieldsForSearchResultViewAsync

If the request includes the workspace ID and the artifact type ID, the service returns all workspace fields available to the user as a collection of Field objects in the FieldsNotIncluded property.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 1030160,

  "artifactTypeID": 10

}
```

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
{

  "FieldsIncluded": [],

  "FieldsNotIncluded": [

    {

      "ArtifactID": 1038302,

      "ViewFieldID": 1001175,

      "Guids": [

        "664fa808-6579-425c-929d-eaa2b096b2da"

      ],

      "Name": "Analytics Index"

    },

    {

      "ArtifactID": 1003676,

      "ViewFieldID": 1000195,

      "Guids": [

        "0a51edfc-846b-47c5-8319-08e637c19be3"

      ],

      "Name": "Artifact ID"

    },

    {

      "ArtifactID": 1037988,

      "ViewFieldID": 1001028,

      "Guids": [],

      "Name": "Attachment Document IDs"

    },

    {

      "ArtifactID": 1037987,

      "ViewFieldID": 1001027,

      "Guids": [],

      "Name": "Attachment Name"

    },

    {

      "ArtifactID": 1035344,

      "ViewFieldID": 1000544,

      "Guids": [

        "1c7eb349-929e-467e-8b42-4b7c045e1fa1"

      ],

      "Name": "Author"

    },

    {

      "ArtifactID": 1035250,

      "ViewFieldID": 1000422,

      "Guids": [

        "d7a9d9fd-68fc-4c85-ad44-ba524a0ca872"

      ],

      "Name": "Batch"

    },

    {

      "ArtifactID": 1035252,

      "ViewFieldID": 1000424,

      "Guids": [

        "3e62303c-b955-4a93-b82a-894ce40b5563"

      ],

      "Name": "Batch::Assigned To"

    },

    {

      "ArtifactID": 1035251,

      "ViewFieldID": 1000423,

      "Guids": [

        "8c3ea95d-6c72-4463-8696-1b6859c0e00e"

      ],

      "Name": "Batch::Batch Set"

    },

    {

      "ArtifactID": 1035253,

      "ViewFieldID": 1000425,

      "Guids": [

        "70e1751f-4f6b-4c1d-abd7-8a6328750175"

      ],

      "Name": "Batch::Status"

    },

    {

      "ArtifactID": 1035345,

      "ViewFieldID": 1000545,

      "Guids": [

        "6e3e65e7-1382-49ea-8960-455bd88655f7"

      ],

      "Name": "Bates Beg"

    },

    {

      "ArtifactID": 1035373,

      "ViewFieldID": 1000572,

      "Guids": [

        "4946a783-90e3-4acb-8171-f915e5b6fe5a"

      ],

      "Name": "Bates Beg Attach"

    },

    {

      "ArtifactID": 1035346,

      "ViewFieldID": 1000546,

      "Guids": [

        "6dcd3bd1-aa7a-478a-897e-b5712e38c409"

      ],

      "Name": "Bates End"

    },

  ...

  ]

}
```

If the request includes the workspace ID, the artifact type ID, and the Artifact ID of a keyword saved search, the service returns the fields included in the specified search as a collection of Field objects in the FieldsIncluded property. Workspace fields available to be included in the search are returned in the FieldsNotIncluded property.

Copy

```text
1
2
3
4
5
{

  "workspaceArtifactID": 1030160,

  "artifactTypeID": 10,

  "searchArtifactID": 1039076

}
```

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
{

  "FieldsIncluded": [

    {

      "ArtifactID": 0,

      "ViewFieldID": 1000183,

      "Guids": [],

      "Name": "Edit"

    },

    {

      "ArtifactID": 1033806,

      "ViewFieldID": 1000184,

      "Guids": [

        "861295b5-5b1d-4830-89e7-77e0a7ef1c30"

      ],

      "Name": "File Icon"

    },

    {

      "ArtifactID": 1003667,

      "ViewFieldID": 1000186,

      "Guids": [

        "2a3f1212-c8ca-4fa9-ad6b-f76c97f05438"

      ],

      "Name": "Doc ID Beg"

    }

  ],

  "FieldsNotIncluded": [

    {

      "ArtifactID": 1038302,

      "ViewFieldID": 1001175,

      "Guids": [

        "664fa808-6579-425c-929d-eaa2b096b2da"

      ],

      "Name": "Analytics Index"

    },

    {

      "ArtifactID": 1003676,

      "ViewFieldID": 1000195,

      "Guids": [

        "0a51edfc-846b-47c5-8319-08e637c19be3"

      ],

      "Name": "Artifact ID"

    },

    {

      "ArtifactID": 1037988,

      "ViewFieldID": 1001028,

      "Guids": [],

      "Name": "Attachment Document IDs"

    },

    {

      "ArtifactID": 1037987,

      "ViewFieldID": 1001027,

      "Guids": [],

      "Name": "Attachment Name"

    },

    {

      "ArtifactID": 1035344,

      "ViewFieldID": 1000544,

      "Guids": [

        "1c7eb349-929e-467e-8b42-4b7c045e1fa1"

      ],

      "Name": "Author"

    },

    {

      "ArtifactID": 1035250,

      "ViewFieldID": 1000422,

      "Guids": [

        "d7a9d9fd-68fc-4c85-ad44-ba524a0ca872"

      ],

      "Name": "Batch"

    },

    {

      "ArtifactID": 1035252,

      "ViewFieldID": 1000424,

      "Guids": [

        "3e62303c-b955-4a93-b82a-894ce40b5563"

      ],

      "Name": "Batch::Assigned To"

    },

    {

      "ArtifactID": 1035251,

      "ViewFieldID": 1000423,

      "Guids": [

        "8c3ea95d-6c72-4463-8696-1b6859c0e00e"

      ],

      "Name": "Batch::Batch Set"

    },

    {

      "ArtifactID": 1035253,

      "ViewFieldID": 1000425,

      "Guids": [

        "70e1751f-4f6b-4c1d-abd7-8a6328750175"

      ],

      "Name": "Batch::Status"

    },

    {

      "ArtifactID": 1035345,

      "ViewFieldID": 1000545,

      "Guids": [

        "6e3e65e7-1382-49ea-8960-455bd88655f7"

      ],

      "Name": "Bates Beg"

    },

    {

      "ArtifactID": 1035373,

      "ViewFieldID": 1000572,

      "Guids": [

        "4946a783-90e3-4acb-8171-f915e5b6fe5a"

      ],

      "Name": "Bates Beg Attach"

    },

    {

      "ArtifactID": 1035346,

      "ViewFieldID": 1000546,

      "Guids": [

        "6dcd3bd1-aa7a-478a-897e-b5712e38c409"

      ],

      "Name": "Bates End"

    },

  ...

  ]

}
```

### GetSearchIncludesAsync

To return all relational fields available to the user in the workspace, use this Keyword Search Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/GetSearchIncludesAsync
```

The request must include a workspace ID.

Copy

```text
1
2
3
{

  "workspaceArtifactID": 1030160

}
```

The response includes a collection of Field objects.

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
[

  {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [],

    "Name": ""

  },

  {

    "ArtifactID": 1035456,

    "ViewFieldID": 1000643,

    "Guids": [

      "14ffb8be-42d1-419e-b72c-645484a78a83"

    ],

    "Name": "Include Conversation Family"

  },

  {

    "ArtifactID": 1003669,

    "ViewFieldID": 1000188,

    "Guids": [

      "a426bc5e-3420-47b4-a293-4c4848a237d7"

    ],

    "Name": "Include Duplicates"

  },

  {

    "ArtifactID": 1036396,

    "ViewFieldID": 1000671,

    "Guids": [

      "c0aa4323-45d5-4db3-bf00-71094792901b"

    ],

    "Name": "Include Emailset"

  },

  {

    "ArtifactID": 1036394,

    "ViewFieldID": 1000670,

    "Guids": [

      "ff4e3c74-d1e0-4c0c-bb58-b50dd7ee8dfa"

    ],

    "Name": "Include EquiSet"

  },

  {

    "ArtifactID": 1003671,

    "ViewFieldID": 1000190,

    "Guids": [

      "1f036749-a691-4aa8-8cf7-5eeb80c36caf"

    ],

    "Name": "Include Family"

  }

]
```

### GetSearchOwnersAsync

To return all users in the workspace with permissions to view saved searches, use this Keyword Search Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/GetSearchIncludesAsync
```

The request must include a workspace ID.

Copy

```text
1
2
3
{

  "workspaceArtifactID": 1030160

}
```

The response includes a collection of User objects.

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

[

  {

    "ArtifactID": 0,

    "Name": "Public, Joe"

  },

  {

    "ArtifactID": 9,

    "Name": "Admin, Relativity"

  },

  {

    "ArtifactID": 1000000392,

    "Name": "Admin, Relativity"

  },

  {

    "ArtifactID": 1271248,

    "Name": "Doe, Jane"

  }

]
```

### GetAccessStatusAsync

The GetAccessStatusAsync endpoint returns the information about the user‘s ability to access the saved search.

To return the access status, use this Keyword Search Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/Keyword%20Search%20Manager/GetAccessStatusAsync
```

The request must include these fields:

- workspaceArtifactID – the Artifact ID for the workspace where the search resides.

- artifactID – the Artifact ID of the search.

- ancestorArtifactIDs – a collection of Artifact IDs representing the folder path where the search resides.

Copy

```text
1
2
3
4
5
{

    "workspaceArtifactID": 1015024,

    "artifactID": 1038050,

    "ancestorArtifactIDs":[1036361, 1035243]

}
```

The response returns an access status object with the following fields:

- Exists – indicates whether the search exists relative to the specified folder path.

- CanView – indicates whether the user has view permissions to the search.

- CanAccessSearchProvider – indicates whether the user has view permissions to the search provider used in the search.

- CanViewCriteriaFields – indicates whether the user has view permissions to all of the fields used in the search.

Copy

```text
1
2
3
4
5
6
7

{

    "Exists": true,

    "CanView": true,

    "CanAccessSearchProvider": false,

    "CanViewCriteriaFields": false

}
```

On this page

- Keyword Search Manager (REST) for saved searches

- Client code sample

- Create

- Search condition criteria

- Read

- Update

- Delete

- Query

- Move

- Copy

- Helper operations

- GetEmailToLinkUrlAsync

- GetFieldsForCriteriaConditionAsync

- GetFieldsForObjectCriteriaCollectionAsync

- GetFieldsForSearchResultViewAsync

- GetSearchIncludesAsync

- GetSearchOwnersAsync

- GetAccessStatusAsync


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
