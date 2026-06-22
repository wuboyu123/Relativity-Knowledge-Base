---
title: "Application Install (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Application_Install_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:49+00:00
sha256: d8227e4e17c3110948b02bcd64c76f8ae2096999e686c1e2e7a4369cfc8aec37
---

Application Install (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Application Install (REST)

The Application Install service includes endpoints for installing applications into one or more workspaces, cancel pending installations, as well as retrieving the status of application installations. Additionally, it supports conflict resolution for failed application installations.

You can also use the Application Install service through .NET. For more information, see Application Install (.NET) .

## Client code sample

To use the Application Install service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.REST/API/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationID}/install/
```

For the workspace identifier in the URL, use -1 to indicate the admin-level context. This value is required for all URLs in the Application Install service. For additional guidelines, see Application Install API .

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
public async Task<InstallApplicationResponse> InstallApplicationIntoWorkspace(int applicationID, int workspaceID)

{

    InstallApplicationResponse response = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", string.Empty);

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("relativity.admin@kcura.com:Test1234!")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");



        string inputJSON = $"{{ \"request\": {{\"WorkspaceIDs\": [{workspaceID}], \"UnlockApplications\": true}} }}";



        string url = $"/Relativity.REST/API/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationID}/install/";

        System.Net.Http.HttpResponseMessage httpResponse = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        httpResponse.EnsureSuccessStatusCode();

        string content = await httpResponse.Content.ReadAsStringAsync();

        response = JsonConvert.DeserializeObject<InstallApplicationResponse>(content);

    }



    return response;

}
```

## Field descriptions for JSON requests

The Application Install service uses many common fields for JSON requests.

View field descriptions for JSON requests

The requests may contain the following fields for the application:

- WorkspaceIDs - the ID of the workspace.

-

WorkspaceIdentifier - the identifier of the workspace.

- ArtifactID - the Artifact ID of the workspace.

- Guids - an array of GUIDs used to identify the workspace.

- UnlockApplications - setting this flag to true allows the endpoint to automatically unlock any associated applications that have locking conflicts with the application that is being installed. Setting the flag to false instead will force a user to manually resolve any locking conflicts that result from the attempted installation.

-

ConflictResolutions - options to resolve an installation conflict. There are four resolution types supported:

- RenameField - has a numeric value of 1.

- RenameRelationalFriendlyName - has a numeric value of 2.

- MapField - which has a numeric value of 3.

- UnlockAssociatedApplications - unlocking any associated applications that have locking conflicts with the application that is being installed, has a numeric value of 4.

- ConflictCorrelationID - the unique ID that identifies a specific validation conflict found during application installation.

- ConflictArtifactIdentifier - represents the ID, GUID, and name of the artifact that caused the validation conflict.

- Value - if the resolution type is RenameField or RenameRelationalFriendlyName , the artifact that caused the validation conflict will be renamed to the new value that is passed in. If the resolution type is either MapField or UnlockAssociatedApplications , the value should be an empty string.

- ResolutionType - represents the four different types of Resolution Actions supported when dealing with application installation conflicts:

- RenameField - has a numeric value of 1.

- RenameRelationalFriendlyName - has a numeric value of 2.

- MapField - has a numeric value of 3.

- UnlockAssociatedApplications - unlocking any associated applications that have locking conflicts with the application that is being installed, has a numeric value of 4.

- Mode - for the InstallApplicationAllAsync endpoint, users can set the Mode attribute in the request to one of two options:

- ForceInstall - has a numeric value of 1, will install the application in all workspaces where it doesn't already exist and upgrade all workspaces where it is already installed.

- UpgradeOnly - has a numeric value of 2, will only upgrade workspaces where the application is already installed.

- RetryInstallAction - this action queues up another install for the specified application into the specified workspace, though there have been no changes to the application itself. This action is mainly used to resolve installation conflicts.

- RetryInstallRequestTemplate - the RetryInstallRequestTemplate serves as a request for the RetryInstallAction and contains any important details pertaining to conflict resolution, such as the workspace ID, whether or not to auto-unlock any associated applications, the conflict correlation ID, and the conflict artifact identifier.

- Endpoints with pagination - endpoints that include pagination (i.e. those that require a start value and length value), return actions for users to easily navigate through each page of the returned results. The start value represents the index of the first returned result, and the length value represents how many results a user would like returned in a single page.

- FirstPage

- PreviousPage

- NextPage

- LastPage

- Results - any endpoint that returns a response containing a list of items to return refers to that list as Results . For example, if you want to get the installation status for all workspaces where a specified application is installed, you would call upon the GetAllInstallStatusAsync endpoint, which would return in its response, a list called Results of GetInstallStatusResponse objects, where each object corresponds to a unique workspace.

- ApplicationIdentifier - the identifier of the application.

- IsSuccessful - a Boolean value indicating whether the request succeeded or failed.

- ApplicationInstallID - the ID of the application installation.

- Message - a string that returns an informative message about the status of the request.

-

InstallStatus - the status of the application installation.

- Code - the status code indicating the state of the application installation

- Message - a string that returns an informative message about the status of the request.

-

GetDetailsAction - an array of Action objects indicating operations that you have permissions to perform on this application. For example, you may not have permissions to modify a application due to your privileges. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the application, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this application.

- Reason - provides an explanation for the unavailability of an action.

- ValidationMessages - a list of messages associated with the application installation .

- InstalledBy - the user that initiated the application installation.

- StartedOn - the start time for the job.

- CompletedOn - the date and time when the application installation completed.

- Version - the version of the library application.

Actions and pagination

The Application Install API has several methods that use on an optional parameter called includeActions . These methods include SearchAsync(), SearchApplicationAsync(), and GetAvailableWorkspacesAsync().

The includeActions parameter controls whether the pagination properties are populated, such as FirstPage, NextPage, and others. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request.

Review these guidelines for setting this includeActions parameter:

- True - When the includeActions parameter is set to true, several objects then include additional properties that you can use as follow-up steps to queries. For example, the InstallStatus objects contain the GetDetailsAction property, which provides detailed information about the installation of a single application.

- False - When the API is called without the parameter, the default value of the includeActions parameter is false.

## Install an application library to specific workspaces

To install an application to one or more workspaces, send a POST request with one of the following URLs:

Copy

```text
1
2
3
4
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{IncludeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{IncludeActions}
```

View JSON for a sample request Copy

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

    "request":

    {

        "WorkspaceIDs": [

            1014823,

            1015024

        ],

        "UnlockApplications": true

    }

}
```

View JSON for a sample request Copy

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

    "request":

    {

        "WorkspaceIDs": [

            1014823,

            1015024

        ],

        "UnlockApplications": false

    }

}
```

View JSON for a sample request If there are conflict resolutions to be resolved with a retry Copy

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

    "request":

    {

        "WorkspaceIDs": [

            1014823

        ],

        "UnlockApplications": false,

        "ConflictResolutions": [

            {

                "ConflictCorrelationID": 1000,

                "WorkspaceID": 1014823,

                "ConflictArtifactID": 1038344,

                "ApplicationComponentType": "Field",

                "ResolutionType": "Rename",

                "Value": "NewName"

            },

            {

                "ConflictCorrelationID": 1001,

                "WorkspaceID": 1014823,

                "ConflictArtifactID": 1038343,

                "ApplicationComponentType": "Field",

                "ResolutionType": "MapField",

                "FieldIdentifiers": [

                    "6d7a5661-b193-44b1-a2d5-a880792407df"

                ]

            },

            {

                "ConflictCorrelationID": 1002,

                "WorkspaceID": 1014823,

                "ConflictArtifactID": 1038344,

                "ApplicationComponentType": "Field",

                "ResolutionType": "UnlockAssociatedApplications",

                "ConflictApplicationID": 1038426

            }

        ]

    }

}
```

View JSON sample response if the endpoint is invoked without the includeActions flag Copy

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

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "Messages": [],

    "Results": [

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1014823,

                "Guids": [

                    "6dd7ec30-11eb-4c33-b812-1efd8141a9e9"

                ]

            },

            "ApplicationInstallID": 17731,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace."

            }

        },

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1015024,

                "Guids": [

                    "01bec74e-b382-40f0-8ec5-0060fdb0ded3"

                ]

            },

            "ApplicationInstallID": 18210,

            "Messages": [],

            "InstallStatus": {

                "Code": "Pending"

            }

        }

    ]

}
```

View JSON sample response if the endpoint is invoked with the includeActions flag Copy

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
{

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "Messages": [],

    "Results": [

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1014823,

                "Guids": [

                    "6dd7ec30-11eb-4c33-b812-1efd8141a9e9"

                ]

            },

            "ApplicationInstallID": 19980,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace.",

                "GetDetailsAction": {

                    "Name": "GetInstallDetailsFirst",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/19980/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            }

        },

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1015024,

                "Guids": [

                    "01bec74e-b382-40f0-8ec5-0060fdb0ded3"

                ]

            },

            "ApplicationInstallID": 19996,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace.",

                "GetDetailsAction": {

                    "Name": "GetInstallDetailsFirst",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/19996/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            }

        }

    ]

}
```

## Install an application library to all workspaces

To install an application to all workspaces, send a POST request with one of the following URLs:

Copy

```text
1
2
3
4
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/all

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/all/{IncludeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/all

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/all/{IncludeActions}
```

The client can specify one of two options for Mode :

- ForceInstall

- UpgradeOnly

View JSON for a sample request Copy

```text
1
2
3
4
5
6
7
{

    "request":

    {

        "Mode": 1,

        "UnlockApplications": true

    }

}
```

View JSON for a sample response if the endpoint is invoked without the includeActions flag Copy

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
{

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "Messages": [],

    "Results": [

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1014823,

                "Guids": [

                    "6dd7ec30-11eb-4c33-b812-1efd8141a9e9"

                ]

            },

            "ApplicationInstallID": 17731,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace."

            }

        },

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1015024,

                "Guids": [

                    "01bec74e-b382-40f0-8ec5-0060fdb0ded3"

                ]

            },

            "ApplicationInstallID": 18210,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace."

            }

        }

    ]

}
```

View JSON for a sample response the endpoint is invoked with the includeActions flag Copy

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
{

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "Messages": [],

    "Results": [

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1014823,

                "Guids": [

                    "6dd7ec30-11eb-4c33-b812-1efd8141a9e9"

                ]

            },

            "ApplicationInstallID": 19980,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace.",

                "GetDetailsAction": {

                    "Name": "GetInstallDetailsFirst",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/19980/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            }

        },

        {

            "WorkspaceIdentifier": {

                "ArtifactID": 1015024,

                "Guids": [

                    "01bec74e-b382-40f0-8ec5-0060fdb0ded3"

                ]

            },

            "ApplicationInstallID": 19996,

            "Messages": [],

            "InstallStatus": {

                "Code": "Completed",

                "Message": "Skipped the application installation because the same version of this product is already installed into the target workspace.",

                "GetDetailsAction": {

                    "Name": "GetInstallDetailsFirst",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/19996/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            }

        }

    ]

}
```

## Retrieve the installation status of an application

To get the installation status of an application, send a GET request with one of the following URLs. The request URL can take either the application's ArtifactID or the Guid.

Copy

```text
1
2
3
4
5
6
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{applicationInstallID}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{applicationInstallID}/{IncludeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{applicationInstallID}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{applicationInstallID}/{IncludeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/{workspaceID}/libraryapplications/{artifactID}/install?{IncludeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/{workspaceID}/libraryapplications/{applicationGuid}/install?{IncludeActions}
```

The body of the request is empty.

View JSON sample response if the endpoint is invoked without the includeActions flag Copy

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
{

    "ApplicationInstallID": 1,

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": []

    },

    "WorkspaceIdentifier": {

        "ArtifactID": 1014823,

        "Guids": [

            "6dd7ec30-11eb-4c33-b812-1efd8141a9e9"

        ]

    },

    "WorkspaceName": "Example Workspace",

    "Client": {

        "Name": "Example Client",

        "ArtifactID": 97,

        "Guids": []

    },

    "Matter": {

        "Name": "Example Matter",

        "ArtifactID": 107,

        "Guids": []

    },

    "InstallStatus": {

        "Code": "Completed"

    },

    "Version": "7.5.0.1",

    "IsOutOfDate": false,

    "ValidationMessages": [

        "The supplied installation status identifier is out of date for this application."

    ],

    Errors: [

        {

            CreatedOn: "2019-12-16T15:17:10.457",

            ArtifactTypeName: "Field",

            Message: "The Object Type Other Conflict File Fields already has a file field, File Field 1. Object Types can only have one file field. Unable to import this field.",

            Name: "File Field 2",

            ArtifactID: 1038821,

            Guids: [ ]

        }

    ],

    "InstalledBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "StartedOn": "2012-11-19T23:24:47.82"

}
```

View JSON sample response if the endpoint is invoked with the includeActions flag (the exact actions that are returned are dependent on the installation status) Copy

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

    "ApplicationInstallID": 19980,

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": []

    },

    "WorkspaceIdentifier": {

        "ArtifactID": 1014823,

        "Guids": [

            "6dd7ec30-11eb-4c33-b812-1efd8141a9e9"

        ]

    },

    "WorkspaceName": "Example Workspace",

    "Client": {

        "Name": "Example Client",

        "ArtifactID": 97,

        "Guids": []

    },

    "Matter": {

        "Name": "Example Matter",

        "ArtifactID": 107,

        "Guids": []

    },

    "InstallStatus": {

        "Code": "Completed",

        "GetDetailsAction": {

            "Name": "GetInstallDetailsFirst",

            "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/19980/details/1/10",

            "Verb": "GET",

            "IsAvailable": true,

            "Reason": []

        }

    },

    "Version": "10.3.0.0",

    "IsOutOfDate": false,

    "ValidationMessages": [],

    "InstalledBy": {

        "Name": "Service Account, Relativity",

        "ArtifactID": 777,

        "Guids": []

    },

    Errors: [

        {

            CreatedOn: "2019-12-16T15:17:10.457",

            ArtifactTypeName: "Field",

            Message: "The Object Type Other Conflict File Fields already has a file field, File Field 1. Object Types can only have one file field. Unable to import this field.",

            Name: "File Field 2",

            ArtifactID: 1038821,

            Guids: [ ]

        }

    ],

    "StartedOn": "2019-07-16T19:23:54.873",

    "CompletedOn": "2019-07-16T19:26:25.737"

}
```

If the installation failed due to validation errors (duplicate name or locked app conflicts), the endpoint is invoked with the includeActions flag, then the JSON response will have the conflicts listed and with a sample request to retry the installation.

View JSON sample response Copy

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

    "ApplicationInstallID": 19924,

    "ApplicationIdentifier": {

        "ArtifactID": 1022443,

        "Guids": []

    },

    "WorkspaceIdentifier": {

        "ArtifactID": 1022442,

        "Guids": [

            "46e1cb06-286f-4e75-be49-5098c33a67bb"

        ]

    },

    "WorkspaceName": "Example Workspace",

    "Client": {

        "Name": "Example Client",

        "ArtifactID": 97,

        "Guids": []

    },

    "Matter": {

        "Name": "Example Matter",

        "ArtifactID": 107,

        "Guids": []

    },

    "InstallStatus": {

        "Code": "Failed",

        "Message": ""

    },

    "ValidationResult": {

        "RetryInstallAction": {

            "Name": "RetryApplicationInstall",

            "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1022443/install",

            "Verb": "POST",

            "IsAvailable": true,

            "Reason": []

        },

        "RetryInstallRequestTemplate": {

            "WorkspaceIDs": [

                1018078

            ],

            "UnlockApplications": false,

            "ConflictResolutions": [

            ]

        },

        "InstallConflicts": [

            {

                "ConflictArtifactIdentifier": {

                    "Name": "ConflictingField",

                    "ArtifactID": 1038419,

                    "Guids": []

                },

                "Description": "A field with the name ConflictingField already exists in the target workspace. Unable to import this field.",

                "ApplicationComponentType": "Field",

                "ConflictType": "Name",

                "ResolutionOptions": [

                    {

                        "WorkspaceID": 1018078,

                        "ConflictArtifactID": 1038419,

                        "ApplicationComponentType": "Field",

                        "ResolutionType": "Rename",

                        "FieldIdentifiers": [],

                        "Value": ""

                    },

                    {

                        "WorkspaceID": 1018078,

                        "ConflictArtifactID": 1038419,

                        "ApplicationComponentType": "Field",

                        "ResolutionType": "MapField",

                        "FieldIdentifiers": [

                            "6d7a5661-b193-44b1-a2d5-a880792407df"

                        ]

                    }

                ]

            },

            {

                "ConflictArtifactIdentifier": {

                    "Name": "ConflictingField",

                    "ArtifactID": 1038419,

                    "Guids": []

                },

                "Description": "The ConflictingField field in the target workspace is used by the locked Relativity Application Field_Name_Conflict_X. You can't rename this field unless you unlock the Field_Name_Conflict_X application.",

                "ApplicationComponentType": "Field",

                "ConflictType": "LockedApplication",

                "ConflictApplicationIdentifier": {

                    "Name": "Field_Name_Conflict_X",

                    "ArtifactID": 1038426,

                    "Guids": []

                },

                "ResolutionOptions": [

                    {

                        "WorkspaceID": 1018078,

                        "ConflictArtifactID": 1038419,

                        "ApplicationComponentType": "Field",

                        "ResolutionType": "UnlockAssociatedApplications",

                        "ConflictApplicationID": 1038426,

                        "FieldIdentifiers": []

                    }

                ]

            }

        ]

    },

    "Version": "0.0.0.1",

    "IsOutOfDate": false,

    "ValidationMessages": [],

    "InstalledBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    Errors: [

        {

            CreatedOn: "2019-12-16T15:17:10.457",

            ArtifactTypeName: "Field",

            Message: "The Object Type Other Conflict File Fields already has a file field, File Field 1. Object Types can only have one file field. Unable to import this field.",

            Name: "File Field 2",

            ArtifactID: 1038821,

            Guids: [ ]

        }

    ],

    "StartedOn": "2019-07-11T19:32:11.263",

    "CompletedOn": "2019-07-11T19:32:11.59"

}
```

## Retrieve the number of workspaces with an outdated application

To retrieve the number of outdated workspace installations associated with an application, send a GET request with the following URLs:

Copy

```text
1
2
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/outdated-workspaces-count

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactGuid}/install/outdated-workspaces-count
```

The body of the request should be empty.

If the count of outdated workspace installations is greater than zero, the response will include an action to update all outdated applications to the latest version available in the Application Library, as well as the payload associated with the action. The JSON response would look like this:

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
{

    "ApplicationIdentifier": {

        "ArtifactID": 1017669,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "IsGlobalApplication": false,

    "OutdatedWorkspacesCount": 2,

    "UpdateOutdatedApplications": {

        "Name": "UpdateOutdatedApplications",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1017669/install/all",

        "Verb": "GET",

        "IsAvailable": true,

        "Reason": []

    },

    "UpdateOutdatedApplicationsPayload": {

        "Mode": "UpgradeOnly",

        "UnlockApplications": true

    }

}
```

## Cancel pending application installations

To cancel one or more application installations, send a DELETE request with one of the following URLs:

Copy

```text
1
2
3
4
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{applicationInstallID}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{applicationInstallID}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install
```

If the endpoint is invoked with a single application installation ID, the JSON request should be empty.

View JSON for a sample request if the endpoint is invoked with multiple application installation IDs Copy

```text
1
2
3
4
5
6
{

    "applicationInstallIDs": [

        4825,

        4827

    ]

}
```

View JSON for a sample response if the endpoint is invoked with a single application installation ID Copy

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
{

    "Results": [

        {

            "IsSuccessful": true,

            "WorkspaceID": -1,

            "ApplicationInstallID": 4825

        }

    ],

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    }

}
```

View JSON for a sample response if the endpoint is invoked with multiple application installation IDs Copy

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
{

    "Results": [

        {

            "IsSuccessful": true,

            "WorkspaceID": -1,

            "ApplicationInstallID": 4825

        },

        {

            "IsSuccessful": true,

            "WorkspaceID": -1,

            "ApplicationInstallID": 4827

        },

        {

            "IsSuccessful": false,

            "ApplicationInstallID": 4829,

            "Message": "The application installation record with identifier 4829 was invalid, in progress, completed, or outdated, and therefore could not be canceled."

        }

    ],

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    }

}
```

## Retrieve installation details for an application

To retrieve installation details for an application, use the GetApplicationInstallDetailsAsync() method.

This endpoint has four different implementations:

- With ID but no actions

- With GUID but no actions

- With ID and actions

- With GUID and actions

To get details of an install,, send a GET request with one of the following URLs:

Copy

```text
1
2
3
4
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{applicationInstallID}/details/{start}/{length}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{applicationInstallID}/details/{start}/{length}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{applicationInstallID}/details/{start}/{length}/{includeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{applicationInstallID}/details/{start}/{length}/{includeActions}
```

The body of the request is empty.

View JSON for a sample response if the endpoint is invoked with a single application installation ID Copy

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

    "CurrentStartIndex": 1,

    "ResultCount": 2,

    "TotalCount": 6,

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "SchemaVersion": {

        "Major": 7,

        "Minor": 5,

        "Build": 0,

        "Revision": 1,

        "MajorRevision": 0,

        "MinorRevision": 1

    },

    "ApplicationInstallID": 1,

    "InstallStatus": {

        "Code": "Completed"

    },

    "Messages": [],

    "Details": [

        {

            "CreatedOn": "2012-11-19T23:24:58.737",

            "ArtifactTypeName": "Object",

            "Message": "Updated successfully",

            "Name": "Document",

            "ArtifactID": 1035231,

            "Guids": []

        },

        {

            "CreatedOn": "2012-11-19T23:24:58.787",

            "ArtifactTypeName": "Object",

            "Message": "Updated successfully",

            "Name": "Field",

            "ArtifactID": 1035232,

            "Guids": []

        }

    ],

    "FirstPage": {

        "Name": "GetInstallDetailsFirst",

        "Verb": "GET",

        "IsAvailable": false,

        "Reason": []

    },

    "PreviousPage": {

        "Name": "GetInstallDetailsPrevious",

        "Verb": "GET",

        "IsAvailable": false,

        "Reason": []

    },

    "NextPage": {

        "Name": "GetInstallDetailsNext",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/1/details/3/2",

        "Verb": "GET",

        "IsAvailable": true,

        "Reason": []

    },

    "LastPage": {

        "Name": "GetInstallDetailsLast",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/1/details/5/2",

        "Verb": "GET",

        "IsAvailable": true,

        "Reason": []

    }

}
```

## Generate an installation report

This endpoint has two different implementations. To get a report, send a GET request with one of the following URLs:

Copy

```text
1
2
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/{applicationInstallID}/details/csv

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/{applicationInstallID}/details/csv
```

The response will be an IKeplerStream object. In a browser context, this will be turned into a file download.

## Cancel pending application installations

This endpoint cancels all pending application installs associated with a specified application. To cancel all pending application installations, send a DELETE request with one of the following URLs:

Copy

```text
1
2
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{artifactID}/install/all

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid}/install/all
```

The JSON request should be empty.

View the JSON for a sample response if the endpoint is invoked with an application ID or GUID for an application with one or more pending installs Copy

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

    "Results": [

        {

            "IsSuccessful": true,

            "WorkspaceIdentifier": {

                "ArtifactID": 1014823,

                "Guids": []

            },

            "ApplicationInstallID": 2046

        },

        {

            "IsSuccessful": true,

            "WorkspaceIdentifier": {

                "ArtifactID": 1015024,

                "Guids": []

            },

            "ApplicationInstallID": 2047

        }

    ],

    "ApplicationIdentifier": {

        "ArtifactID": 1018305,

        "Guids": [

            "9c5e0a91-2e66-40cf-b6fe-3a1ecafee8d7"

        ]

    }

}
```

## Retrieve installation status by workspace

This endpoint has one implementation with optional query fields start (default: 1), length (default: 10), and includeActions (default: false). To search application installations, send a POST request the following URL:

Copy

```text
1
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/install/search?start={start}&length={length}&includeActions={includeActions}
```

The includeActions parameter controls whether the pagination properties are populated. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request. For more information, see Actions and pagination .

JSON Request Copy

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
{

    "queryOptions": {

        "Condition": "'Application Artifact ID' == 1015285",

        "Sorts": [

            {

                "FieldName": "Workspace",

                "Direction": "Ascending"

            }

        ]

    }

}
```

JSON Response Copy

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
{

    "Results": [

        {

            "ApplicationInstallID": 53769,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "Admin Case",

                "ArtifactID": -1,

                "Guids": []

            },

            "RootFolderID": 0,

            "InstallStatus": {

                "Code": "Completed",

                "GetDetailsAction": {

                    "Name": "GetInstallDetails-DefaultPage",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/53769/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            },

            "Version": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:01:32.753",

            "CompletedOn": "2019-12-02T17:01:49.923"

        },

        {

            "ApplicationInstallID": 53784,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "New Case Template",

                "ArtifactID": 1014823,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed",

                "GetDetailsAction": {

                    "Name": "GetInstallDetails-DefaultPage",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/53784/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            },

            "Version": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:02:12.11",

            "CompletedOn": "2019-12-02T17:02:55.58"

        },

        {

            "ApplicationInstallID": 53801,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "Relativity Starter Template",

                "ArtifactID": 1015024,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed",

                "GetDetailsAction": {

                    "Name": "GetInstallDetails-DefaultPage",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/53801/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            },

            "Version": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:02:17.017",

            "CompletedOn": "2019-12-02T17:03:00.283"

        }

    ],

    "Summary": {

        "Other": 0,

        "Pending": 0,

        "InProgress": 0,

        "Failed": 0,

        "Completed": 37,

        "Canceled": 0,

        "TotalActiveInstalls": 0,

        "Total": 37

    },

    "CurrentStartIndex": 1,

    "ResultCount": 3,

    "TotalCount": 37,

    "FirstPage": {

        "Name": "SearchStatus-FirstPage",

        "Verb": "POST",

        "IsAvailable": false,

        "Reason": []

    },

    "PreviousPage": {

        "Name": "SearchStatus-PreviousPage",

        "Verb": "POST",

        "IsAvailable": false,

        "Reason": []

    },

    "NextPage": {

        "Name": "SearchStatus-NextPage",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/search?start=4&length=3&includeActions=true",

        "Verb": "POST",

        "IsAvailable": true,

        "Reason": []

    },

    "LastPage": {

        "Name": "SearchStatus-LastPage",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/search?start=37&length=3&includeActions=true",

        "Verb": "POST",

        "IsAvailable": true,

        "Reason": []

    }

}
```

## Query for application installations by identifier

This endpoint has two implementations with optional query fields start (default: 1), length (default: 10), and includeActions (default: false). To search application installations, send a POST request to one of the following URLs:

Copy

```text
1
2
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationID:int}/install/search?start={start}&length={length}&includeActions={includeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid:guid}/install/search?start={start}&length={length}&includeActions={includeActions}
```

The includeActions parameter controls whether the pagination properties are populated. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request. For more information, see Actions and pagination .

JSON Request Copy

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
{

    "queryOptions": {

        "Condition": "(NOT 'Workspace' LIKE ['Admin']) AND ('Status Code' == 4)",

        "Sorts": [

            {

                "FieldName": "Workspace",

                "Direction": "Ascending"

            }

        ]

    }

}
```

JSON Response Copy

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
{

    "Results": [

        {

            "ApplicationInstallID": 53784,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "New Case Template",

                "ArtifactID": 1014823,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed",

                "GetDetailsAction": {

                    "Name": "GetInstallDetails-DefaultPage",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/53784/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            },

            "Version": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:02:12.11",

            "CompletedOn": "2019-12-02T17:02:55.58"

        },

        {

            "ApplicationInstallID": 53801,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "Relativity Starter Template",

                "ArtifactID": 1015024,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed",

                "GetDetailsAction": {

                    "Name": "GetInstallDetails-DefaultPage",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/53801/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            },

            "Version": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:02:17.017",

            "CompletedOn": "2019-12-02T17:03:00.283"

        },

        {

            "ApplicationInstallID": 53869,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "Test-0db2cf10-97e7-456f-af89-e8186c720656",

                "ArtifactID": 1020470,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed",

                "GetDetailsAction": {

                    "Name": "GetInstallDetails-DefaultPage",

                    "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/53869/details/1/10",

                    "Verb": "GET",

                    "IsAvailable": true,

                    "Reason": []

                }

            },

            "Version": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:07:06.577",

            "CompletedOn": "2019-12-02T17:07:39.873"

        }

    ],

    "Summary": {

        "Other": 0,

        "Pending": 0,

        "InProgress": 0,

        "Failed": 0,

        "Completed": 36,

        "Canceled": 0,

        "TotalActiveInstalls": 0,

        "Total": 36

    },

    "CurrentStartIndex": 1,

    "ResultCount": 3,

    "TotalCount": 36,

    "FirstPage": {

        "Name": "SearchStatus-FirstPage",

        "Verb": "POST",

        "IsAvailable": false,

        "Reason": []

    },

    "PreviousPage": {

        "Name": "SearchStatus-PreviousPage",

        "Verb": "POST",

        "IsAvailable": false,

        "Reason": []

    },

    "NextPage": {

        "Name": "SearchStatus-NextPage",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/search?start=4&length=3&includeActions=true",

        "Verb": "POST",

        "IsAvailable": true,

        "Reason": []

    },

    "LastPage": {

        "Name": "SearchStatus-LastPage",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/search?start=34&length=3&includeActions=true",

        "Verb": "POST",

        "IsAvailable": true,

        "Reason": []

    }

}
```

## Validate new artifact names

This endpoint has one implementation. To validate one or more name requests, send a POST request with one of the following URLs:

Copy

```text
1
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/install/conflict/validate-names
```

JSON Request Copy

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

    "nameValidationItems": [

        {

            "WorkspaceID": 1014823,

            "ConflictArtifactID": 1035231,

            "ConflictType": "Name",

            "Value": "Document"

        }

    ]

}
```

JSON Response Copy

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
[

    {

        "WorkspaceID": 1014823,

        "ConflictArtifactID": 1035231,

        "ConflictType": "Name",

        "IsAvailable": false,

        "Messages": [

            "An Object Type with the same name already exists or the name is reserved by the system."

        ]

    }

]
```

## Query for application installations with additional fields

This endpoint has two implementations with optional query fields start (default: 1), length (default: 10), and includeActions (default: false). To search application installations, send a POST request to one of the following URLs:

Copy

```text
1
2
https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationID:int}/install/available-workspaces?start={start}&length={length}&includeActions={includeActions}

https://{host}/relativity.rest/api/Relativity.LibraryApplications/workspace/-1/libraryapplications/{applicationGuid:guid}/install/available-workspaces?start={start}&length={length}&includeActions={includeActions}
```

The includeActions parameter controls whether the pagination properties are populated. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request. For more information, see Actions and pagination .

JSON Request Copy

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
{

    "queryOptions": {

        "Condition": "(NOT ('Case Artifact ID' == -1)) AND ('Is Installed' == 0)",

        "Sorts": [

            {

                "FieldName": "Workspace",

                "Direction": "Ascending"

            }

        ]

    }

}
```

JSON Response Copy

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
{

    "Results": [

        {

            "ApplicationInstallID": 53784,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "New Case Template",

                "ArtifactID": 1014823,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed"

            },

            "SchemaVersion": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:02:12.11",

            "CompletedOn": "2019-12-02T17:02:55.58"

        },

        {

            "ApplicationInstallID": 53801,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "Relativity Starter Template",

                "ArtifactID": 1015024,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed"

            },

            "SchemaVersion": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:02:17.017",

            "CompletedOn": "2019-12-02T17:03:00.283"

        },

        {

            "ApplicationInstallID": 53869,

            "ApplicationIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "WorkspaceIdentifier": {

                "Name": "Test-0db2cf10-97e7-456f-af89-e8186c720656",

                "ArtifactID": 1020470,

                "Guids": []

            },

            "ClientIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1006066,

                "Guids": []

            },

            "MatterIdentifier": {

                "Name": "Relativity Template",

                "ArtifactID": 1000002,

                "Guids": []

            },

            "RootFolderID": 1003697,

            "InstallStatus": {

                "Code": "Completed"

            },

            "SchemaVersion": "11.1.0.0",

            "IsOutOfDate": false,

            "InstalledBy": {

                "Name": "Service Account, Relativity",

                "ArtifactID": 777,

                "Guids": []

            },

            "StartedOn": "2019-12-02T17:07:06.577",

            "CompletedOn": "2019-12-02T17:07:39.873"

        }

    ],

    "Summary": {

        "Other": 0,

        "Pending": 0,

        "InProgress": 0,

        "Failed": 0,

        "Completed": 36,

        "Canceled": 0,

        "TotalActiveInstalls": 0,

        "Total": 36

    },

    "CurrentStartIndex": 1,

    "ResultCount": 3,

    "TotalCount": 36,

    "FirstPage": {

        "Name": "GetWorkspacesAvailableForInstall-FirstPage",

        "Verb": "POST",

        "IsAvailable": false,

        "Reason": []

    },

    "PreviousPage": {

        "Name": "GetWorkspacesAvailableForInstall-PreviousPage",

        "Verb": "POST",

        "IsAvailable": false,

        "Reason": []

    },

    "NextPage": {

        "Name": "GetWorkspacesAvailableForInstall-NextPage",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/available-workspaces?start=4&length=3&includeActions=true",

        "Verb": "POST",

        "IsAvailable": true,

        "Reason": []

    },

    "LastPage": {

        "Name": "GetWorkspacesAvailableForInstall-LastPage",

        "Href": "Relativity.LibraryApplications/workspace/-1/libraryapplications/1015285/install/available-workspaces?start=34&length=3&includeActions=true",

        "Verb": "POST",

        "IsAvailable": true,

        "Reason": []

    }

}
```

On this page

- Application Install (REST)

- Client code sample

- Field descriptions for JSON requests

- Install an application library to specific workspaces

- Install an application library to all workspaces

- Retrieve the installation status of an application

- Retrieve the number of workspaces with an outdated application

- Cancel pending application installations

- Retrieve installation details for an application

- Generate an installation report

- Cancel pending application installations

- Retrieve installation status by workspace

- Query for application installations by identifier

- Validate new artifact names

- Query for application installations with additional fields


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
