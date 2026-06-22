---
title: "Folder Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/REST_API/REST_services/Folder_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:26:23+00:00
sha256: a6dafee393f467d817c1b6234225270d5e905d99d1c0ea5b7a02166ab3d8d72b
---

Folder Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Folder Manager (REST)

The Folder Manager service available in the REST API supports multiple operations for manipulating folder structures in the Relativity UI framework. You can use it to create, update, or move a folder, query for folders, retrieve the root or children in a folder tree, and delete empty folders. It also indicates the progress for the deletion operation on folders.

You can also use the Relativity Services API to create, update, delete, and query for folders. For more information, see Folder Manager (.NET) .

## Client code sample

To interact with the Folder Manager service, you send HTTP(S) requests that use the POST method and specify query conditions in the body of the request. See the base URL for this service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/
```

You can use the following .NET code as the REST client for performing any of the operations available on the Folder Manager service. The code currently illustrates how to create a new folder, but you can modify it as follows to perform other operations:

- Set the url variable to the URL for the operation that you want to perform.

- Set the string represented by payload variable to the JSON input required for your operation.

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
public async Task FolderCreate()

{

    using (HttpClient httpClient = new HttpClient())

    {

        httpClient.BaseAddress = new Uri("http://localhost/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/");

        //Set the required headers.

        httpClient.DefaultRequestHeaders.Add("/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/QueryAsync", string.Empty);

        httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");

        string url = "CreateSingleAsync";

        var workspaceArtifactId = 0;

        var payload = @"{

                    workspaceArtifactID:0,

                    model: {

                        name: 'New folder name',

                        parentFolder: {

                            artifactId: 151561

                        }

                    }";

        var result = await httpClient.PostAsJsonAsync(url, payload);

    }

}
```

### HTTP headers and status codes

The Folder Manager Service uses the same HTTP(S) headers and status codes as other services in the Relativity REST API. For more information, see the following:

- HTTP headers

- HTTP status codes

## Create a folder

To create a folder, send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/CreateSingleAsync
```

The request includes the following fields:

- workspaceArtifactID – the Artifact ID of the workspace where you want to create the folder.

- name – the model name, which is the name of the Folder DTO that you want to create.

- parentFolder – this field contains the parent folder where you want to add the new subfolder. If you want to create a folder at the root of a workspace, omit the parentFolder property.

The following request results in the creation of a child folder called MyFolder , which is added under an existing parent folder in a workspace.

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

    "workspaceArtifactID": 1015024,

    "model": {

        "name": "MyFolder",

        "parentFolder": {

            "artifactId": "1003697"

        }

    }

}
```

The response returns the Artifact ID of the folder that was created.

## Update a folder

To rename or move a folder, send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/UpdateSingleAsync
```

The request must contain the following fields:

- workspaceArtifactID – the unique identifier for the workspace where the folder resides.

- model.artifactID – the unique identifier for the Folder DTO.

- model.name – the text for the new folder name.

If the requests contains an Artifact ID that differs from ID for the original parent folder, the folder is moved to the parent folder specified in the request. If a parent folder isn't specified, the folder is moved to the root folder of the workspace.

The following request updates the name of folder to My new folder name . This folder has a parent folder in the workspace.

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

    "workspaceArtifactID": 1015024,

    "model": {

        "artifactID": "1039180",

        "parentFolder": {

            "artifactId": 1003697

        },

        "name": "My new folder name"

    }

}
```

The response returns the Artifact ID of the folder that was updated.

## Delete unused folders

To delete all empty folders in a workspace, send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/DeleteUnusedFoldersAsync
```

The DeleteUnusedFoldersAsync() method removes all unused folders from the workspace.

The request must include the Artifact ID of the workspace, where you want to deleted the unused folders:

Copy

```text
1
2
3
{

    "workspaceArtifactID": 1015024

}
```

The response returns a folder result set that lists the deleted folders.

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
{

    "QueryToken": "",

    "TotalCount": 3,

    "Success": true,

    "Message": "",

    "Results": [{

        "Success": true,

        "Artifact": {

            "ArtifactID": 1039163

        },

        "Message": "",

        "WarningMessages": []

    }, {

        "Success": true,

        "Artifact": {

            "ArtifactID": 1039179

        },

        "Message": "",

        "WarningMessages": []

    }, {

        "Success": true,

        "Artifact": {

            "ArtifactID": 1039180

        },

        "Message": "",

        "WarningMessages": []

    }]

}
```

## Query for folders

To get an unstructured list of folders, send a request to the following Folder Manager Service URL:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/QueryAsync
```

The request includes the following fields:

- workspaceArtifactId – the Artifact ID of the workspace that you want to query.

- query – may include query conditions or may be an empty query as illustrated in the following sample.

- length – indicates the number of returned results. The default value is 0 for length, and the number of returned results defaults to the Instance setting table value of PDVDefaultQueryCacheSize of 10000.

Copy

```text
1
2
3
4
5
{

    "workspaceArtifactId": 1015024,

    "query": {},

    "length": 2

}
```

The response returns a list of all folders in the workspace that are available to requesting user.

View the JSON response for a query Copy

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
{

    "QueryToken": "a4118970-7d8c-4910-8790-208f2331a716",

    "TotalCount": 11,

    "Success": true,

    "Message": "",

    "Results": [

        {

            "Success": true,

            "Artifact": {

                "ArtifactID": 1003697,

                "Name": "Doc Test"

            },

            "Message": "",

            "WarningMessages": []

        },

        {

            "Success": true,

            "Artifact": {

                "ArtifactID": 1110585,

                "Name": "ZipperAndrew"

            },

            "Message": "",

            "WarningMessages": []

        }

    ]

}
```

If the response contains a token value that isn't null, it indicates that more results are available than initially specified in the length property, or that result count exceeds the default query limit. You can retrieve the additional folders by using the QuerySubsetAsync() method as illustrated in the following URL:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/QuerySubsetAsync
```

The request for this method must include the workspaceArtifactID, queryToken, start, and length as in the following sample query:

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

    "queryToken": "f61f0c4a-a794-4cd0-9407-f8c4b927bdc3",

    "start": 5,

    "length": 4

}
```

The response to this query returns a subset with four elements from the previous query that starts at the fifth element.

## Helper methods

The Folder Manager service provides helper methods that simplify retrieving folders or traversing the folder tree.

### Retrieve workspace root Folder

To retrieve the root folder in a workspace, send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/GetWorkspaceRootAsync
```

The request must include the workspaceArtifactID, which is the Artifact ID of the workspace that you want to query.

Copy

```text
1
2
3
{

    "workspaceArtifactID": 1015024,

}
```

The response returns root folder in the workspace.

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

    "ParentFolder": {

        "ArtifactID": 0

    },

    "AccessControlListIsInherited": true,

    "SystemCreatedOn": "2010-08-08T16:59:49.1",

    "SystemLastModifiedOn": "2010-08-08T16:59:49.1",

    "Permissions": {

        "add": true,

        "delete": true,

        "edit": true,

        "secure": true

    },

    "Selected": false,

    "HasChildren": false,

    "ArtifactID": 1003697,

    "Name": "Test Template"

}
```

### Retrieve subfolders

To retrieve a list of subfolders, send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/GetChildrenAsync
```

The request must include the workspaceArtifactID, which is the Artifact ID of the workspace that you want to query.

Copy

```text
1
2
3
4
{

    "workspaceArtifactID": 1015024,

    "parentId": 1003697

}
```

The response returns an array containing only direct descendants of the specified parent folder.

View JSON response with children of the parent folder Copy

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
[{

    "ParentFolder": {

        "ArtifactID": 1003697,

        "Name": "Relativity Starter Template"

    },

    "AccessControlListIsInherited": true,

    "SystemCreatedOn": "2015-08-19T07:22:37.107",

    "SystemLastModifiedOn": "2015-08-19T07:22:37.107",

    "Permissions": {

        "add": true,

        "delete": true,

        "edit": true,

        "secure": true

    },

    "Selected": false,

    "HasChildren": true,

    "ArtifactID": 1039027,

    "Name": "Folder 1"

}, {

    "ParentFolder": {

        "ArtifactID": 1003697,

        "Name": "Relativity Starter Template"

    },

    "AccessControlListIsInherited": true,

    "SystemCreatedOn": "2015-08-19T07:22:37.037",

    "SystemLastModifiedOn": "2015-08-19T07:22:37.037",

    "Permissions": {

        "add": true,

        "delete": true,

        "edit": true,

        "secure": true

    },

    "Selected": false,

    "HasChildren": true,

    "ArtifactID": 1039014,

    "Name": "Folder 2"

}]
```

### Retrieve expanded Folder nodes

You can retrieve a folder structure that contains expanded nodes, or you can retrieve a folder structure that contains expanded nodes, and Artifact ID of the folder currently selected by a user.

To retrieve information about expanded folder nodes, send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/GetFolderTreeAsync
```

The request includes the following fields:

- workspaceArtifactId – the Artifact ID of the workspace that you want to query.

- expandedNodes – a list of Artifact IDs of specified folders. You want to retrieve information about these specified folders.

- selectedFolderId – an optional field used to mark a specific folder as selected.

For example, you might want to retrieve information about the children of the expanded root folder called Relativity Starter Template illustrated in the following screen shot:

You would query on Relativity Starter Template, Folder 3, and Folder 3.2 by sending the following request:

For more information about the starter template, see Starter template on the Relativity Server 2025 Documentation site.

Copy

```text
1
2
3
4
5
{

    "workspaceArtifactId": 1015024,

    "expandedNodes": [1003697, 1039001, 1039006],

    "selectedFolderId": "1039008"

}
```

The response returns a list of children for all expanded folders.

View the JSON response for all expanded folders Copy

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
302
303
304
305
306
307
[{

    "ParentFolder": {

        "ArtifactID": 1003663

    },

    "AccessControlListIsInherited": true,

    "SystemCreatedOn": "0001-01-01T00:00:00",

    "SystemLastModifiedOn": "0001-01-01T00:00:00",

    "Permissions": {

        "add": true,

        "delete": true,

        "edit": true,

        "secure": true

    },

    "Children": [{

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": true,

        "ArtifactID": 1039027,

        "Name": "Folder 1"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": true,

        "ArtifactID": 1039014,

        "Name": "Folder 2"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [{

            "ParentFolder": {

                "ArtifactID": 1039001

            },

            "AccessControlListIsInherited": true,

            "SystemCreatedOn": "0001-01-01T00:00:00",

            "SystemLastModifiedOn": "0001-01-01T00:00:00",

            "Permissions": {

                "add": true,

                "delete": true,

                "edit": true,

                "secure": true

            },

            "Children": [],

            "Selected": false,

            "HasChildren": true,

            "ArtifactID": 1039010,

            "Name": "Folder 3.1"

        }, {

            "ParentFolder": {

                "ArtifactID": 1039001

            },

            "AccessControlListIsInherited": true,

            "SystemCreatedOn": "0001-01-01T00:00:00",

            "SystemLastModifiedOn": "0001-01-01T00:00:00",

            "Permissions": {

                "add": true,

                "delete": true,

                "edit": true,

                "secure": true

            },

            "Children": [{

                "ParentFolder": {

                    "ArtifactID": 1039006

                },

                "AccessControlListIsInherited": true,

                "SystemCreatedOn": "0001-01-01T00:00:00",

                "SystemLastModifiedOn": "0001-01-01T00:00:00",

                "Permissions": {

                    "add": true,

                    "delete": true,

                    "edit": true,

                    "secure": true

                },

                "Children": [],

                "Selected": false,

                "HasChildren": false,

                "ArtifactID": 1039009,

                "Name": "Folder 3.2.1"

            }, {

                "ParentFolder": {

                    "ArtifactID": 1039006

                },

                "AccessControlListIsInherited": true,

                "SystemCreatedOn": "0001-01-01T00:00:00",

                "SystemLastModifiedOn": "0001-01-01T00:00:00",

                "Permissions": {

                    "add": true,

                    "delete": true,

                    "edit": true,

                    "secure": true

                },

                "Children": [],

                "Selected": true,

                "HasChildren": false,

                "ArtifactID": 1039008,

                "Name": "Folder 3.2.2"

            }, {

                "ParentFolder": {

                    "ArtifactID": 1039006

                },

                "AccessControlListIsInherited": true,

                "SystemCreatedOn": "0001-01-01T00:00:00",

                "SystemLastModifiedOn": "0001-01-01T00:00:00",

                "Permissions": {

                    "add": true,

                    "delete": true,

                    "edit": true,

                    "secure": true

                },

                "Children": [],

                "Selected": false,

                "HasChildren": false,

                "ArtifactID": 1039007,

                "Name": "Folder 3.2.3"

            }],

            "Selected": false,

            "HasChildren": true,

            "ArtifactID": 1039006,

            "Name": "Folder 3.2"

        }, {

            "ParentFolder": {

                "ArtifactID": 1039001

            },

            "AccessControlListIsInherited": true,

            "SystemCreatedOn": "0001-01-01T00:00:00",

            "SystemLastModifiedOn": "0001-01-01T00:00:00",

            "Permissions": {

                "add": true,

                "delete": true,

                "edit": true,

                "secure": true

            },

            "Children": [],

            "Selected": false,

            "HasChildren": true,

            "ArtifactID": 1039002,

            "Name": "Folder 3.3"

        }],

        "Selected": false,

        "HasChildren": true,

        "ArtifactID": 1039001,

        "Name": "Folder 3"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1044568,

        "Name": "Folder name"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": false,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1039163,

        "Name": "helo"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1039183,

        "Name": "New 555Folder"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1039179,

        "Name": "New Folder"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1039181,

        "Name": "New Folder 3"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1039180,

        "Name": "new folder name"

    }, {

        "ParentFolder": {

            "ArtifactID": 1003697

        },

        "AccessControlListIsInherited": true,

        "SystemCreatedOn": "0001-01-01T00:00:00",

        "SystemLastModifiedOn": "0001-01-01T00:00:00",

        "Permissions": {

            "add": true,

            "delete": true,

            "edit": true,

            "secure": true

        },

        "Children": [],

        "Selected": false,

        "HasChildren": false,

        "ArtifactID": 1039182,

        "Name": "New older"

    }],

    "Selected": false,

    "HasChildren": true,

    "ArtifactID": 1003697,

    "Name": "Relativity Starter Template"

}]
```

### Get folder access status

The GetAccessStatusAsync endpoint returns an object that contains information the user‘s ability to access the folder. Like the other endpoints in this API, use a POST request when making this call.

To return the access status, use this Folder Manager Service URL:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/GetAccessStatusAsync
```

The request must contain the following fields:

- workspaceArtifactID – the Artifact ID for the workspace where the folder resides.

- artifactID – the Artifact ID for the folder.

Copy

```text
1
2
3
4
{

    "workspaceArtifactID": 1015024,

    "artifactID": 1038050

}
```

The response returns the following fields:

- Exists - indicates whether the folder exists.

- CanView - indicates whether the user has access to the folder.

Copy

```text
1
2
3
4
5

{

    "Exists": true,

    "CanView": true

}
```

## Move folders

You can move a folder and its children, including subfolders and documents. Send a request to this URL for the Folder Manager service:

Copy

```text
1
/Relativity.Rest/API/Relativity.Services.Folder.IFolderModule/Folder%20Manager/MoveFolderAsync
```

The request must contain the following fields:

- workspaceArtifactID – the Artifact ID for the workspace where the folder resides.

- artifactID – the Artifact ID for the folder that you want to move.

- destinationFolderID - the Artifact ID for the target folder, where you want to move the current folder.

Copy

```text
1
2
3
4
5
6

{

   "workspaceArtifactID":1015024,

   "artifactID":1039180,

   "destinationFolderID":1039178

}
```

The response returns the following fields:

- ProcessState - a message that indicates the current operation executing on the folder being moved. The process state messages include:

- Creating destination folder hierarchy.

- Creating document batches.

- Creating folder reference update batches.

- Moving documents.

- Updating folder references.

- Cleaning up.

- TotalOperations - equals the sum of the number of documents to be moved and the number of folder references to be updated.

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

   "ProcessState":"Moving documents.",

   "TotalOperations":15,

   "OperationsCompleted":2

}
```

On this page

- Folder Manager (REST)

- Client code sample

- HTTP headers and status codes

- Create a folder

- Update a folder

- Delete unused folders

- Query for folders

- Helper methods

- Retrieve workspace root Folder

- Retrieve subfolders

- Retrieve expanded Folder nodes

- Get folder access status

- Move folders


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
