---
title: "Legacy dtSearch Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_dtSearch/dtSearch_Manager_service_old.htm
collection: developer
fetched_at: 2026-06-22T06:25:58+00:00
sha256: 0eedd68eafc79f2ae0c47785d7a11aab445f005d370659598cb6e5fa4b8cc864
---

Legacy dtSearch Manager (REST)

# Legacy dtSearch Manager (REST)

The Relativity REST API supports operations with dtSearch saved searches though the dtSearch Manager Service. The operations available through the service are equivalent to the methods for interacting with the dtSearch DTO in the Relativity Services API. For more information, see dtSearch in the Services API documentation.

You can only use the POST method when interacting with the service.

You can programmatically execute dtSearches created with the dtSearch Manager Service using the SavedSearchCondition class of the Relativity Services API or a saved search query in the REST API.

## Client code sample

The following is an example of .NET REST client for creating a dtSearch saved search. The code can be used for all dtSearch Manager Service operations with different endpoint URLs and input JSON values.

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
//Set up the client.

HttpClient httpClient = new HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set the required headers.

httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");

//Call Create for a SavedSearch.

string url = "Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/Create";

StringContent content = new StringContent(CreateInputJSON, Encoding.UTF8, "application/json");

HttpResponseMessage response = httpClient.PostAsync(url, content).Result;

string result = response.Content.ReadAsStringAsync().Result;

bool success = HttpStatusCode.Created == response.StatusCode;

//Parse the result with Json.NET.

JObject resultObject = JObject.Parse(result);
```

## Create

Use this dtSearch Manager Service URL to create a dtSearch:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/CreateSingleAsync
```

The request must include a workspace ID and valid JSON representation of a dtSearch DTO.

Required dtSearch DTO properties include ArtifactTypeID, Name, SearchIndex, and Fields.

Sample JSON request for creating a dtSearch with multiple conditions, including a date condition Copy

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
{

  "workspaceArtifactID": 1275698,

  "searchDTO": {

    "ArtifactTypeID": 10,

    "Name": "Oil and Gas Search",

    "SearchContainer": {

      "ArtifactID": 1038762,

      "Name": "Admin Searches"

    },

    "Owner": {

      "ArtifactID": 1271248,

      "Name": "Doe, Jane"

    },

    "SearchIndex": {

      "ArtifactID": 1038690,

      "Name": "dtSearch"

    },

    "Scope": "EntireCase",

    "SearchFolders": [],

    "RequiresManualRun": false,

    "SearchCriteria": {

      "Conditions": [

        {

          "Condition": {

            "Operator": "IsAfter",

            "Month": "NotSet",

            "FieldIdentifier": {

              "Name": "Date Created"

            },

            "Value": "2014-10-05T00:00:00",

            "NotOperator": false,

            "ConditionType": "CriteriaDate"

          },

          "BooleanOperator": "And"

        },

        {

          "Condition": {

            "Operator": "IsLike",

            "FieldIdentifier": {

              "Name": "Author"

            },

            "Value": "Doe",

            "NotOperator": false,

            "ConditionType": "Criteria"

          },

          "BooleanOperator": "None"

        }

      ],

      "BooleanOperator": "None"

    },

    "Fields": [

      {

        "Name": "Edit"

      },

      {

        "Name": "Doc ID Beg"

      }

    ],

    "Sorts": [

      {

        "FieldIdentifier": {

          "Name": "Artifact ID"

        },

        "Order": 0,

        "Direction": "Ascending"

      },

      {

        "FieldIdentifier": {

          "Name": "Date Created"

        },

        "Order": 1,

        "Direction": "Descending"

      }

    ],

    "SortByRank": true,

    "SearchText": "jane doe oil gas",

    "FuzzinessLevel": 3,

    "EnableStemming": true

  }

}
```

Sample JSON request for creating a dtSearch associated with a Relativity dashboard Copy

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

    "Name": "Sample dtSearch",

    "Fields": [

      {

        "Name": "Extracted Text"

      }

    ]

  }

}
```

The response is an Artifact ID of the created search.

## Read

Use this dtSearch Manager Service URL to read a dtSearch:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/ReadSingleAsync
```

The request must include the workspace ID and the dtSearch saved search Artifact ID.

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

The response returns a JSON representation of a dtSearch DTO.

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
{

  "ArtifactID": 1030160,

  "ArtifactTypeID": 10,

  "Name": "My New dtSearch",

  "SearchContainer": {

    "ArtifactID": 1038762,

    "Name": "Admin Searches"

  },

  "Owner": {

    "ArtifactID": 1271248,

    "Name": "Doe, Jane"

  },

  "SearchIndex": {

    "ArtifactID": 1038690,

    "Name": "dtSearch"

  },

  "Includes": null,

  "Scope": "EntireCase",

  "SearchFolders": [],

  "RequiresManualRun": false,

  "SearchCriteria": {

    "Conditions": [],

    "BooleanOperator": "None"

  },

  "Fields": [

    {

      "ArtifactID": -1,

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

      "Name": "FileIcon"

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

  "Sorts": [],

  "QueryHint": "",

  "SortByRank": false,

  "SearchText": "jane doe oil gas",

  "FuzzinessLevel": 3,

  "EnableStemming": false,

  "Keywords": "",

  "Notes": "",

  "RelativityApplications": [],

  "SystemCreatedBy": {

    "ArtifactID": 1271248,

    "Name": "Doe, Jane"

  },

  "SystemCreatedOn": "2014-10-02T23:50:52.333",

  "SystemLastModifiedBy": {

    "ArtifactID": 1271248,

    "Name": "Doe, Jane"

  },

  "SystemLastModifiedOn": "2014-10-06T23:25:58.45"

}
```

## Update

Use this dtSearch Manager Service URL to update a dtSearch:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/UpdateSingleAsync
```

The request must include a workspace ID and a valid JSON representation of a dtSearch DTO.

You must include all DTO field information in the update. You cannot update individual fields because fields left empty will be cleared on the update. All DTO fields are required except for system/user created by/created on.

The following JSON sample illustrates how to change fields and sort order of the dtSearch created in a previous example.

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
{

  "workspaceArtifactID": 1275698,

  "searchDTO": {

    "ArtifactID": 1038769,

    "ArtifactTypeID": 10,

    "Name": "Oil and Gas Search",

    "SearchContainer": {

      "ArtifactID": 1038762,

      "Name": "Admin Searches"

    },

    "Owner": {

      "ArtifactID": 1271248,

      "Name": "Doe, Jane"

    },

    "SearchIndex": {

      "ArtifactID": 1038690,

      "Name": "dtSearch"

    },

    "Scope": "EntireCase",

    "SearchFolders": [],

    "RequiresManualRun": false,

    "SearchCriteria": {

      "Conditions": [

        {

          "Condition": {

            "Operator": "IsAfter",

            "Month": "NotSet",

            "FieldIdentifier": {

              "Name": "Date Created"

            },

            "Value": "2014-10-05T00:00:00",

            "NotOperator": false,

            "ConditionType": "CriteriaDate"

          },

          "BooleanOperator": "And"

        },

        {

          "Condition": {

            "Operator": "IsLike",

            "FieldIdentifier": {

              "Name": "Author"

            },

            "Value": "Doe",

            "NotOperator": false,

            "ConditionType": "Criteria"

          },

          "BooleanOperator": "None"

        }

      ],

      "BooleanOperator": "None"

    },

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

    ],

    "SortByRank": true,

    "SearchText": "jane doe oil gas",

    "FuzzinessLevel": 3,

    "EnableStemming": true

  }

}
```

The response does not contain any data. Success or failure is indicated by the HTTP status code. For more information, see HTTP status codes .

## Delete

Use this dtSearch Manager Service URL to update a dtSearch:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/DeleteSingleAsync
```

The request must include the workspace ID and the dtSearch saved search Artifact ID.

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

The response does not contain any data. Success or failure is indicated by the HTTP status code. For more information, see HTTP status codes .

## Query

The dtSearch Manager Service URL for querying dtSearch:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/QueryAsync
```

The request must include the workspace ID and the query. You can also specify the number of results to return as the optional length property.

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

To return all analytics saved searches in a workspace, specify an empty Condition as shown in the JSON example below. When the length parameter is not specified, its value defaults to 0, and the number of returned results defaults to the Instance setting value of PDVDefaultQueryCacheSize of 10000. For more information, see Search Relativity .

Copy

```text
1
2
3
4
5

{

  "workspaceArtifactID": 1030160,

  "query":{}

}
```

The response returns a collection of dtSearch objects as a dtSearchQueryResultSet object.

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
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
{

  "QueryToken": "146e1e5f-9de6-446f-8842-7a0de1237aaf",

  "TotalCount": 3,

  "Success": true,

  "Message": "",

  "Results": [

    {

      "Success": true,

      "Artifact": {

        "ArtifactID": 1038758,

        "ArtifactTypeID": 10,

        "Name": "My New dtSearch",

        "SearchContainer": {

          "ArtifactID": 1038762,

          "Name": "Admin Searches"

        },

        "Owner": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SearchIndex": {

          "ArtifactID": 1038690,

          "Name": "dtSearch"

        },

        "Includes": null,

        "Scope": "EntireCase",

        "SearchFolders": [],

        "RequiresManualRun": false,

        "SearchCriteria": {

          "Conditions": [],

          "BooleanOperator": "None"

        },

        "Fields": [

          {

            "ArtifactID": -1,

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

            "Name": "FileIcon"

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

        "Sorts": [],

        "QueryHint": "",

        "SortByRank": false,

        "SearchText": "jane doe oil gas",

        "FuzzinessLevel": 3,

        "EnableStemming": false,

        "Keywords": "",

        "Notes": "",

        "RelativityApplications": [],

        "SystemCreatedBy": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SystemCreatedOn": "2014-10-02T23:50:52.333",

        "SystemLastModifiedBy": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SystemLastModifiedOn": "2014-10-06T23:25:58.45"

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "ArtifactID": 1038764,

        "ArtifactTypeID": 10,

        "Name": "My New dtSearch (1)",

        "SearchContainer": {

          "ArtifactID": 1035243,

          "Name": "Documentation Workspace"

        },

        "Owner": {

          "ArtifactID": 0,

          "Name": "Public"

        },

        "SearchIndex": {

          "ArtifactID": 1038690,

          "Name": "dtSearch"

        },

        "Includes": null,

        "Scope": "EntireCase",

        "SearchFolders": [],

        "RequiresManualRun": false,

        "SearchCriteria": {

          "Conditions": [],

          "BooleanOperator": "None"

        },

        "Fields": [

          {

            "ArtifactID": -1,

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

            "Name": "FileIcon"

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

        "Sorts": [],

        "QueryHint": "",

        "SortByRank": false,

        "SearchText": "jane doe oil gas",

        "FuzzinessLevel": 0,

        "EnableStemming": false,

        "Keywords": "",

        "Notes": "",

        "RelativityApplications": [],

        "SystemCreatedBy": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SystemCreatedOn": "2014-10-03T00:38:00.033",

        "SystemLastModifiedBy": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SystemLastModifiedOn": "2014-10-03T00:38:00.033"

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "ArtifactID": 1038765,

        "ArtifactTypeID": 10,

        "Name": "Oil and gas search",

        "SearchContainer": {

          "ArtifactID": 1035243,

          "Name": "Documentation Workspace"

        },

        "Owner": {

          "ArtifactID": 0,

          "Name": "Public"

        },

        "SearchIndex": {

          "ArtifactID": 1038690,

          "Name": "dtSearch"

        },

        "Includes": null,

        "Scope": "EntireCase",

        "SearchFolders": [],

        "RequiresManualRun": false,

        "SearchCriteria": {

          "Conditions": [

            {

              "Condition": {

                "Operator": "Is",

                "FieldIdentifier": {

                  "ArtifactID": 1035366,

                  "ViewFieldID": 1000566,

                  "Guids": [

                    "12d841e2-d026-4e57-901a-0678b4b44d64"

                  ],

                  "Name": "Email From"

                },

                "Value": "JoneDoe@mycompany.com",

                "NotOperator": false,

                "ConditionType": "Criteria"

              },

              "BooleanOperator": "And"

            },

            {

              "Condition": {

                "Operator": "AnyOfThese",

                "FieldIdentifier": {

                  "ArtifactID": 1035357,

                  "ViewFieldID": 1000557,

                  "Guids": [

                    "8a6747ed-713a-4f2d-b441-c4cd91c3bba9"

                  ],

                  "Name": "Designation"

                },

                "Value": [

                  1035850

                ],

                "NotOperator": false,

                "ConditionType": "Criteria"

              },

              "BooleanOperator": "And"

            },

            {

              "Condition": {

                "Operator": "IsBefore",

                "Month": "NotSet",

                "FieldIdentifier": {

                  "ArtifactID": 1035352,

                  "ViewFieldID": 1000552,

                  "Guids": [

                    "408a5856-f777-40e9-a30b-7c43a9bf28c1"

                  ],

                  "Name": "Date Created"

                },

                "Value": "2014-10-09T00:00:00",

                "NotOperator": false,

                "ConditionType": "CriteriaDate"

              },

              "BooleanOperator": "None"

            }

          ],

          "BooleanOperator": "None"

        },

        "Fields": [

          {

            "ArtifactID": 1003668,

            "ViewFieldID": 1000187,

            "Guids": [

              "58d35076-1b1d-43b4-bff4-d6c089de51b2"

            ],

            "Name": "Extracted Text"

          },

          {

            "ArtifactID": 1035344,

            "ViewFieldID": 1000544,

            "Guids": [

              "1c7eb349-929e-467e-8b42-4b7c045e1fa1"

            ],

            "Name": "Author"

          }

        ],

        "Sorts": [

          {

            "FieldIdentifier": {

              "ArtifactID": 1003676,

              "ViewFieldID": 1000195,

              "Guids": [

                "0a51edfc-846b-47c5-8319-08e637c19be3"

              ],

              "Name": "Artifact ID"

            },

            "Order": 0,

            "Direction": "Ascending"

          },

          {

            "FieldIdentifier": {

              "ArtifactID": 1035352,

              "ViewFieldID": 1000552,

              "Guids": [

                "408a5856-f777-40e9-a30b-7c43a9bf28c1"

              ],

              "Name": "Date Created"

            },

            "Order": 1,

            "Direction": "Descending"

          }

        ],

        "QueryHint": "",

        "SortByRank": false,

        "SearchText": "",

        "FuzzinessLevel": 0,

        "EnableStemming": false,

        "Keywords": "",

        "Notes": "",

        "RelativityApplications": [],

        "SystemCreatedBy": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SystemCreatedOn": "2014-10-03T00:38:00.103",

        "SystemLastModifiedBy": {

          "ArtifactID": 1271248,

          "Name": "Doe, Jane"

        },

        "SystemLastModifiedOn": "2014-10-03T20:30:08.16"

      },

      "Message": "",

      "WarningMessages": []

    }

  ]

}
```

## Move

You can move an saved dtSearch to a different folder. Send a request to this dtSearch Manager service URL:

Copy

```text
1
/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/MoveAsync
```

The request must contain the following fields:

- workspaceArtifactID – the Artifact ID for the workspace where the saved search resides.

- artifactID – the Artifact ID of the search.

- destinationContainerID – the Artifact ID of the target saved search folder.

You must have delete permission for saved search and search folder on the source search folder and add permissions for saved search and search folder on destination folder. If any of those is not met then a validation error is returned.

Copy

```text
1
2
3
4
5
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
{

   "TotalOperations": 1,

   "ProcessState": "Completed",

   "OperationsCompleted": 1

}
```

Unlike the Services API, the dtSearch Manager Service doesn’t support use of progress indicators or cancellation tokens.

## Copy

You can create a copy of an existing dtSearch saved search in the same saved search folder. Send a request to this dtSearch Manager service URL:

Copy

```text
1
/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/CopySingleAsync
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
{

   "workspaceArtifactID": 1015024,

   "searchArtifactID": 1036361

}
```

This creates a copy of an existing search in the same location. The name of the copy is based on the name of the original with an incremented number in brackets, for example Smith Case Documents (2) .

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

    "Name": "Smith Case Documents (2)"

}
```

## Helper operations

The dtSearch Manager Service provides the following helper operations for retrieving search properties:

- GetEmailToLinkUrlAsync

- GetFieldsForCriteriaConditionAsync

- GetFieldsForObjectCriteriaCollectionAsync

- GetFieldsForSearchResultViewAsync

- GetSearchIncludesAsync

- GetSearchIndexesAsync

- GetSearchOwnersAsync

- GetAccessStatusAsync

### GetEmailToLinkUrlAsync

The dtSearch Manager Service URL for retrieving an email link to dtSearch results:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetEmailToLinkUrlAsync
```

In order for GetEmailToLinkUrlAsync to return results, the EmailLinkURLOverride instance setting option must be enabled. For more information, see Instance settings' descriptions on the Relativity Documentation site.

The request must include the workspace ID and the search artifact ID.

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
"mailto:?subject=Relativity%20Review%20-%20Integration%20Tests%20-%20My%20New%20dtSearch%20With%20Two%20Conditions&body=http%3a%2f%2fmyhost%2frelativity%2fsearchlink.aspx%3fSelectedSearchArtifactID%3d1039106%26AppID%3d1275015"
```

### GetFieldsForCriteriaConditionAsync

The dtSearch Manager Service URL for retrieving all workspace fields available to the user that can be included in a saved search conditions criteria:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetFieldsForCriteriaConditionAsync
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

    "Name": "dtSearch Index"

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

The dtSearch Manager Service URL for retrieving all workspace fields available to the user that can be specified as a subcondition for a given field in batch and multi-object field conditions .

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetFieldsForObjectCriteriaCollectionAsync
```

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

The dtSearch Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetFieldsForSearchResultViewAsync
```

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

      "Name": "dtSearch Index"

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

If the request includes the workspace ID, the artifact type ID, and the Artifact ID of a dtSearch saved search, the service returns the fields included in the specified search as a collection of Field objects in the FieldsIncluded property. Workspace fields available to be included in the search are returned in the FieldsNotIncluded property.

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

      "Name": "dtSearch Index"

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

To return all relational fields available to the user in the workspace, use this dtSearch Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetSearchIncludesAsync
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

### GetSearchIndexesAsync

To return all dtSearch indexes available to the user for a given workspace, use this dtSearch Manager Service URL:

Copy

```text
1
//Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetSearchIndexesAsync
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

The response includes a collection of index objects.

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

    "ArtifactID": 1038684,

    "Name": "Salt vs Pepper case index"

  },

  {

    "ArtifactID": 1039332,

    "Name": "Oil and gas correspondence index"

  }

]
```

### GetSearchOwnersAsync

To return all users in the workspace with permissions to view saved searches, use this dtSearch Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetSearchIncludesAsync
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

To return the access status, use this dtSearch Manager Service URL:

Copy

```text
1
/Relativity.REST/api/Relativity.Services.Search.ISearchModule/dtSearch%20Manager/GetAccessStatusAsync
```

The request must include these fields:

- workspaceArtifactID – the Artifact ID for the workspace where the folder resides.

- artifactID – the Artifact ID of the keyword search.

- ancestorArtifactIDs – a an empty of Artifact IDs representing the folder path where the search resides.

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

- Exists – indicates whether the folder exists relative to the specified folder path.

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
{

    "Exists": true,

    "CanView": true,

    "CanAccessSearchProvider": false,

    "CanViewCriteriaFields": false

}
```
