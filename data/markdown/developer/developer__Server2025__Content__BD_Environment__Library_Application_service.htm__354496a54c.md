---
title: "Library Application (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Library_Application_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:54+00:00
sha256: 070cb07789029f564ab058d7d96e7dfb660eb3b624722518f704812f0a59aea5
---

Library Application (REST)

# Library Application (REST)

Through the REST API, the Library Application API allows clients to read application metadata and RAP files from the library, upload new applications, and update or delete existing applications.

## Guidelines for the Library Application service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve an application:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {artifactID} to the Artifact ID of a specific application.

## Client code sample

To use the Library Application service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.REST/API/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/
```

For the workspace identifier in the URL, use -1 to indicate the admin-level context. This value is required for all URLs in the Library Application service. For additional guidelines, see Library Application API .

Code sample for the base URL Copy

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
public async Task<LibraryApplicationResponse> ReadLibraryApplication(int applicationID)

{

    LibraryApplicationResponse response = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", string.Empty);

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test.com:SomePassword!")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");

        string url = $"/Relativity.REST/API/relativity-environment/v1/workspace/-1/libraryapplications/{applicationID}/";

        System.Net.Http.HttpResponseMessage httpResponse = await client.GetAsync(url);

        httpResponse.EnsureSuccessStatusCode();

        string content = await httpResponse.Content.ReadAsStringAsync();

        response = JsonConvert.DeserializeObject<LibraryApplicationResponse>(content);

    }

    return response;

}
```

## Create a library application

To create a library application, send a POST request using multi-part form data. The first part should contain the request as JSON content type application/json . The second part should contain the file as binary with content type application/octet-stream :

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/libraryapplications

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/libraryapplications/{packageGuid}
```

The alternative version takes a GUID referring to a previously uploaded package, see UploadPackage . The body is empty.

The body of the request is empty.

The response contains the following fields for the library application:

- ApplicationIdentifier - the identifier of the application.

- ArtifactID - the Artifact ID of the library application.

- Guids - an array of GUIDs used to identify the library application.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this library application. For example, you may not have permissions to modify a library application due to your privileges. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the library application, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether the operation is available or not on this library application.

- Reason - provides an explanation for the unavailability of an action.

- ApplicationInstallID - the ID of the application installation.

- InstallStatus - the status of the application installation.

- Code - the status code indicating the state of the application installation.

- Message - a string that returns an informative message about the status of the request.

View JSON for a sample response

The newly created artifact ID of the application will be returned in the response.

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

    "ApplicationIdentifier": {

        "ArtifactID": 1022432,

        "Guids": [

            "74f3c015-f382-476d-838e-275b13919f91"

        ]

    },

    "Actions": [],

    "ApplicationInstallID": 1,

    "InstallStatus": {

        "Code": "Pending"

    },

}
```

## Read a library application

To read a library application, send a GET request for any one of the following URLs:

Copy

```text
1
2
3
4
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}/{includeMetadata}/{IncludeActions}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}/{includeMetadata}/{IncludeActions}
```

The body of the request is empty.

The response contains the following fields for the library application:

- Version - the version of the library application.

- FileName - RAP file name of the library application.

- UserFriendlyURL - a more simple and readable version of the application's URL (i.e. without GUIDs).

- Required - whether an application is required, required if present or optional.

- TreeView - indicates the different components that make up the application in JSON format.

- CreatedBy - contains the Artifact ID and name of the user who created the library application.

- CreatedOn - the date and time when the library application was added to Relativity.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the library application.

- LastModifiedOn - the date and time when the library application was most recently modified.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this library application. For example, you may not have permissions to modify a library application due to your privileges. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the library application, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether the operation is available or not on this library application.

- Reason - provides an explanation for the unavailability of an action.

- Name - the name of the library application.

- ArtifactID - the Artifact ID of the library application.

- Guids - an array of GUIDs used to identify the library application.

View JSON sample response if the endpoint is invoked without flags, includeMetadata and includeActions Copy

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
{

    "Version": "10.3.0.1",

    "SchemaVersion": "10.3.0.0",

    "IsGlobalApplication": false,

    "FileName": "Relativity.Conversion.rap",

    "Required": "Required",

    "TreeView": "{}",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "CreatedOn": "2012-10-12T20:49:18.59",

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedOn": "2019-06-25T22:49:59.633",

    "License": "NotApplicable",

    "Actions": [],

    "Name": "Imaging",

    "ArtifactID": 1015285,

    "Guids": [

        "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

    ]

}
```

View JSON sample response if the endpoint is invoked with flags, includeMetadata and includeActions Copy

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
{

    "Version": "10.3.0.0",

    "SchemaVersion": "10.3.0.0",

    "IsGlobalApplication": false,

    "FileName": "Relativity.Conversion.rap",

    "Required": "Required",

    "TreeView": "{}",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "CreatedOn": "2012-10-12T20:49:18.59",

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedOn": "2019-06-25T22:49:59.633",

    "License": "NotApplicable",

    "Actions": [

        {

            "Name": "DownloadRAPFile",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285/contents",

            "Verb": "GET",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Delete",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "InstallToWorkspace",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285/install",

            "Verb": "POST",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Name": "Imaging",

    "ArtifactID": 1015285,

    "Guids": [

        "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

    ]

}
```

## Read all library applications

To read all library applications, send a GET request for one of the following URLs:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{includeMetadata}/{includeActions}
```

The body of the request is empty.

The response contains the following fields for the library application:

- Version - the version of the library application.

- FileName - RAP file name of the library application.

- UserFriendlyURL - a more simple and readable version of the application's URL (i.e. without GUIDs).

- Required - whether an application is required, required if present or optional.

- TreeView - indicates the different components that make up the application in JSON format.

- CreatedBy - contains the Artifact ID and name of the user who created the library application.

- CreatedOn - the date and time when the library application was added to Relativity.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the library application.

- LastModifiedOn - the date and time when the library application was most recently modified.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this library application. For example, you may not have permissions to modify a library application due to your privileges. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the library application, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether the operation is available or not on this library application.

- Reason - provides an explanation for the unavailability of an action.

- Name - the name of the library application.

- ArtifactID - the Artifact ID of the library application.

- Guids - an array of GUIDs used to identify the library application.

View JSON sample response if the endpoint is invoked without flags, includeMetadata and includeActions Copy

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
{

    "Version": "1.0.0.1",

    "SchemaVersion": "1.0.0.0",

    "IsGlobalApplication": false,

    "FileName": "ExampleApplication1.rap",

    "Required": "Required",

    "TreeView": "{}",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "CreatedOn": "0001-01-01T00:00:00.00",

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "LastModifiedOn": "0001-01-01T00:00:00.00",

    "License": "NotApplicable",

    "Actions": [],

    "Name": "Example Application 1",

    "ArtifactID": 1234567,

    "Guids": [

        "5c0cd817-c131-4da2-bd0f-94037956de57"

    ]

},

{

    "Version": "2.0.0.1",

    "SchemaVersion": "2.0.0.0",

    "IsGlobalApplication": false,

    "FileName": "ExampleApplication2.rap",

    "Required": "Required",

    "TreeView": "{}",

    "CreatedBy": "Admin, Relativity",

    "CreatedOn": "0001-01-01T00:00:00.00",

    "ModifiedBy"CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "CreatedOn": "0001-01-01T00:00:00.00",

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "LastModifiedOn": "0001-01-01T00:00:00.00",

    "License": "NotApplicable",

    "Actions": [],

    "Name": "Example Application 2",

    "ArtifactID": 2345678,

    "Guids": [

        "7dba737b-70fa-4995-a7ca-be21739b9623"

    ]

}
```

View JSON sample response if the endpoint is invoked with flags, includeMetadata and includeActions Copy

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
{

    "Version": "1.0.0.1",

    "SchemaVersion": "1.0.0.0",

    "IsGlobalApplication": false,

    "FileName": "ExampleApplication1.rap",

    "Required": "Required",

    "TreeView": "{}",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "CreatedOn": "0001-01-01T00:00:00.00",

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "LastModifiedOn": "0001-01-01T00:00:00.00",

    "License": "NotApplicable",

    "Actions": [

        {

            "Name": "DownloadRAPFile",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1234567/contents",

            "Verb": "GET",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Delete",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1234567",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1234567",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "InstallToWorkspace",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1234567/install",

            "Verb": "POST",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Name": "Example Application 1",

    "ArtifactID": 1234567,

    "Guids": [

        "5c0cd817-c131-4da2-bd0f-94037956de57"

    ]

},

{

    "Version": "2.0.0.1",

    "SchemaVersion": "2.0.0.0",

    "IsGlobalApplication": false,

    "FileName": "ExampleApplication2.rap",

    "Required": "Required",

    "TreeView": "{}",

    "CreatedBy": "Admin, Relativity",

    "CreatedOn": "0001-01-01T00:00:00.00",

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 123456,

        "Guids": []

    },

    "LastModifiedOn": "0001-01-01T00:00:00.00",

    "License": "NotApplicable",

    "Actions": [

        {

            "Name": "DownloadRAPFile",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/2345678/contents",

            "Verb": "GET",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Delete",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/2345678",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/2345678",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "InstallToWorkspace",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/2345678/install",

            "Verb": "POST",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Name": "Example Application 2",

    "ArtifactID": 2345678,

    "Guids": [

        "7dba737b-70fa-4995-a7ca-be21739b9623"

    ]

}
```

## Retrieve a library application as a RAP file

To retrieve a library application as a RAP file, send a GET request for one of the following URLs:

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}/contents

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}/contents
```

The body of the request is empty.

The response will not be human-readable.

## Update a library application

To update an application, send a PUT request using multi-part form data. The first part should contain the request as JSON content type application/json . The second part should contain the file as binary with content type application/octet-stream :

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{packageGUID}
```

The alternative version takes a GUID referring to a previously uploaded package, see UploadPackage . The body is empty.

The request includes the following fields:

- IgnoreVersion - indicates whether or not the version should be validated before updating the library application. By default only upgrades with a higher application version are allowed.

- RefreshCustomPages - when set to true, the custom pages will be deployed immediately instead of as a task during the application install.

- FileName - RAP file name of the library application.

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
{

    "request":

    {

        "IgnoreVersion":false,

        "CreateIfMissing": false,

        "RefreshCustomPages":false,

    }

}
```

View JSON for a sample response Copy

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

    "ApplicationIdentifier": {

        "ArtifactID": 1019081,

        "Guids": [

            "f6cbe8e2-1ff8-4e39-9aa4-1b0c08c8b22e"

        ]

    },

    "Actions": [

        {

            "Name": "GetLibraryApplicationInstall",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1020261/libraryinstall",

            "Verb": "GET",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "ApplicationInstallID": 1,

    "InstallStatus": {

        "Code": "Pending",

        "CancelInstallAction": {

            "Name": "CancelLibraryApplicationInstall",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1019081/libraryinstall",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        }

    },

    "Messages": []

}
```

## Delete a library application

To delete an application, send a DELETE request. The request URL can take either the application's ArtifactID or the Guid.

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactId}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}
```

The body of this request should be empty.

The body of the response will also be empty. If the delete is successful it will just return a 200 status code.

## Retrieve the installation status of an application

To get the most recent library install status of an application, send a GET request to the following URL. The request URL can take either the application's ArtifactID or the Guid.

Copy

```text
1
2
3
4
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}/libraryinstall

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}/libraryinstall/{IncludeActions}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}/libraryinstall

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}/libraryinstall/{IncludeActions}
```

The body of this request should be empty.

The response includes the following fields:

- ApplicationInstallID - the ID of the application installation.

- ApplicationIdentifier - the identifier of the application.

- WorkspaceIdentifier - the identifier of the workspace.

- InstallStatus - the status of the application installation.

- ValidationResult - if there are any validation failures that require user intervention, the ValidationResult property will hold the options for resolving the failures and retrying the installation.

- Version - the version of the library application.

- ValidationMessages - a list of messages associated with the application installation.

- InstalledBy - the user that initiated the application installation.

- StartedOn - the start time for the job.

- CompletedOn - the date and time when the application installation completed.

- GetCurrentInstallStatus - the action to retrieve the status of the most recent install for the specified application and workspace.

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
{

    "ApplicationInstallID": 18211,

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": []

    },

    "WorkspaceIdentifier": {

        "ArtifactID": -1,

        "Guids": []

    },

    "InstallStatus": {

        "Code": "Completed"

    },

    "ValidationResult": {

        "RetryInstallAction": {

            "Name": "RetryApplicationInstall",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285/install",

            "Verb": "POST",

            "IsAvailable": true,

            "Reason": []

        },

        "RetryInstallRequestTemplate": {

            "WorkspaceIDs": [

                -1

            ],

            "UnlockApplications": false,

            "ConflictResolutions": []

        },

        "InstallConflicts": []

    },

    "Version": "10.3.0.0",

    "ValidationMessages": [],

    "InstalledBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "StartedOn": "2019-06-24T14:52:36.35",

    "CompletedOn": "2019-06-24T14:52:42.087"

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
{

    "ApplicationInstallID": 19964,

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": []

    },

    "WorkspaceIdentifier": {

        "ArtifactID": -1,

        "Guids": []

    },

    "InstallStatus": {

        "Code": "Completed",

        "GetDetailsAction": {

            "Name": "GetInstallDetailsFirst",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285/install/19964/details/1/10",

            "Verb": "GET",

            "IsAvailable": true,

            "Reason": []

        }

    },

    "ValidationResult": {

        "RetryInstallAction": {

            "Name": "RetryApplicationInstall",

            "Href": "relativity-environment/v1/workspace/-1/libraryapplications/1015285/install",

            "Verb": "POST",

            "IsAvailable": true,

            "Reason": []

        },

        "RetryInstallRequestTemplate": {

            "WorkspaceIDs": [

                -1

            ],

            "UnlockApplications": false,

            "ConflictResolutions": []

        },

        "InstallConflicts": []

    },

    "Version": "10.3.0.0",

    "ValidationMessages": [],

    "InstalledBy": {

        "Name": "Service Account, Relativity",

        "ArtifactID": 777,

        "Guids": []

    },

    "StartedOn": "2019-07-16T19:23:00.217",

    "CompletedOn": "2019-07-16T19:23:21.373"

}
```

## Retry installing an application

To queue or retry an install of an existing application into the Application Library, send a PUT request.

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}/libraryinstall

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}/libraryinstall
```

The body of the request should be empty.

The response includes the following fields:

- ApplicationIdentifier - the identifier of the application.

- ApplicationInstallID - the ID of the application installation.

- InstallStatus - the status of the application installation.

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
{

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "ApplicationInstallID": 18211,

    "InstallStatus": {

        "Code": "Pending"

    }

}
```

## Cancel an application installation

To cancel a library application installation, send a DELETE request with one of the following URLs:

Copy

```text
1
2
3
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{artifactID}/libraryinstall

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGuid}/libraryinstall
```

If the endpoint is invoked with a single application install ID, the JSON request should be empty.

The response includes the following fields:

- ApplicationIdentifier - the identifier of the application.

- IsSuccessful - a Boolean value indicating whether the request succeeded or failed.

- ApplicationInstallID - the ID of the application installation.

- Message - a string that returns an informative message about the status of the request.

View JSON sample response if the endpoint is invoked with a single application install ID Copy

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

    "ApplicationIdentifier": {

        "ArtifactID": 1015285,

        "Guids": [

            "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

        ]

    },

    "IsSuccessful": true,

    "ApplicationInstallID": 5655

}
```

## Upload a RAP or XML file

This endpoint uploads a RAP or XML file to a temporary location in Relativity and returns a unique file identifier along with the meta data for the application. If the file is not in a valid format, a validation exception is thrown. This endpoint is used in conjunction with CreateAsync and UpdateAsync to implement workflows where the application's details need to be displayed for final confirmation before installing the application. To create an application, send a POST request using multi-part form data. The first part should contain the request as JSON content type application/json . The second part should contain the file as binary with content type application/octet-stream :

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/package
```

The body of the request should be empty.

View a sample PowerShell script for uploading a RAP file Copy

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

$FilePath = "C:\apps\example.rap"

$HostName = "example.relativity.one"

$HttpClientTimeOut = 30

$Uri = "https://${HostName}/relativity.rest/api/relativity-environment/v1/workspace/-1/libraryapplications"

$pair = "$($username):$($password)"

$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))

#create http client

Add-Type -AssemblyName System.Net.Http

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$httpClient = New-Object System.Net.Http.Httpclient

$httpClient.DefaultRequestHeaders.Authorization = New-Object System.Net.Http.Headers.AuthenticationHeaderValue ("Basic", $encodedCreds)

$httpClient.DefaultRequestHeaders.Add("x-csrf-header","-")

$httpClient.Timeout = New-TimeSpan -Seconds $HttpClientTimeOut

#create payload

$content = New-Object System.Net.Http.MultipartFormDataContent

#payload part - other parameters

$fileName = Split-Path $FilePath -leaf

$jsonPayload =

@{

    "request" = @{

        "IgnoreVersion" = $EnsureVersionCheck

        "RefreshCustomPages" = $RefreshCustomPages

        "CreateIfMissing" = $true

    }

}

$jsonContent = New-Object System.Net.Http.StringContent(ConvertTo-Json $jsonPayload)

$contentDispositionHeaderValue = New-Object System.Net.Http.Headers.ContentDispositionHeaderValue "form-data"

$contentDispositionHeaderValue.Name = "json"

$jsonContent.Headers.ContentDisposition = $contentDispositionHeaderValue

$jsonContent.Headers.ContentType = New-Object System.Net.Http.Headers.MediaTypeHeaderValue "application/json"

$content.Add($jsonContent)

#payload part - file

$packageFileStream = New-Object System.IO.FileStream @($FilePath, [System.IO.FileMode]::Open)

$contentDispositionHeaderValue = New-Object System.Net.Http.Headers.ContentDispositionHeaderValue "form-data"

$contentDispositionHeaderValue.Name = "rapStream"

$contentDispositionHeaderValue.FileName = $fileName

$streamContent = New-Object System.Net.Http.StreamContent $packageFileStream

$streamContent.Headers.ContentDisposition = $contentDispositionHeaderValue

$streamContent.Headers.ContentType = New-Object System.Net.Http.Headers.MediaTypeHeaderValue "application/octet-stream"

$content.Add($streamContent)

$response = $null

try

{

    $response = $httpClient.PostAsync($Uri, $content).GetAwaiter().GetResult()

    if (!$response.IsSuccessStatusCode)

    {

        $responseBody = $response.Content.ReadAsStringAsync().GetAwaiter().GetResult()

        $responseBody

        $errorMessage = "Status code $($response.StatusCode). Reason $($response.ReasonPhrase). Server reported the following message: $($responseBody)."

        throw [System.Net.Http.HttpRequestException] $errorMessage

    }

}

finally

{

    $packageFileStream.Dispose()

    $streamContent.Dispose()

    $httpClient.Dispose()

}
```

View JSON sample response

The response includes application metadata, such as the GUID and version.

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
{

    "Name": "Example Application",

    "PackageGUID": "65f9fc30-2f34-4330-96d6-cfa0bba1cc20",

    "Version": "1.2.3.4",

    "FileName": "ExampleApp.rap",

    "UserFriendlyURL": "ExampleApp",

    "TreeView": "{\"text\":\"ExampleApp\",\"children\":[{\"text\":\"Pre Install Event Handlers\",\"children\":[]},{\"text\":\"Object Types\",\"children\":[]},{\"text\":\"External Tabs\",\"children\":[{\"text\":\"MVC Custom Page\",\"children\":[]}]},{\"text\":\"Scripts\",\"children\":[]},{\"text\":\"Saved Searches\",\"children\":[]},{\"text\":\"Custom Pages\",\"children\":[{\"text\":\"Custom page with authentication tests\",\"children\":[]}]},{\"text\":\"Agent Types\",\"children\":[]},{\"text\":\"Post Install Event Handlers\",\"children\":[]},{\"text\":\"Pre Uninstall Event Handlers\",\"children\":[]},{\"text\":\"Post Workspace Create Event Handlers\",\"children\":[]},{\"text\":\"Pre Workspace Delete Event Handlers\",\"children\":[]}]}"

}
```

## Download a RAP or XML file

This endpoint downloads a RAP or XML file previously uploaded using the UploadPackageAsync endpoint. It takes the unique file identifier as an argument in the URL path and returns a stream of bytes. To create an application, send a GET request with the file's unique identifier in the URL:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/package/{packageIdentifier}/contents
```

The raw JSON response will not be human-readable.

## Delete a RAP file

This endpoint allows clients to delete an RAP file that has been uploaded to a temporary storage location. To delete a package, send a DELETE request with the package identifier in the URL:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/package/{packageIdentifier}
```

The body of this request should be empty.

The body of the response will also be empty. If the delete is successful it will just return a 200 status code.

## Retrieve hosting status of an application

This endpoint retrieves the hosting status of a specified application and indicates the status of the application's hosted components, such as custom pages. An example use case of this endpoint is determining if the application's custom page has been redeployed and is healthy. To retrieve the hosting status of an application, send a GET request with the one of the following URLs:

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationGUID}/hostingStatus

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspace/-1/libraryapplications/{applicationID}/hostingStatus
```

The body of this request should be empty.

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
{

    "CustomPages": [

        {

            "CustomPage": {

                "Secured": false,

                "Value": {

                    "Name": "Conversion API",

                    "ArtifactID": 1019193,

                    "Guids": []

                }

            },

            "StatusCode": "OK",

            "State": "Ready",

            "Message": "",

            "Actions": []

        }

    ],

    "State": "Ready",

    "Message": "",

    "Actions": []

}
```
