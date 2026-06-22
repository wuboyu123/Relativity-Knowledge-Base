---
title: "Workspace Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Workspace_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:22:56+00:00
sha256: 23f4c2ba54fbe7c2a09515d3308d28fe83b06794a5364fc4c3439daba7bb6ae2
---

Workspace Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Workspace Manager (REST)

In Relativity, a workspace acts as a secure data repository for documents. It supports customized views, layouts, fields, choices, and security settings. For more information, see Workspaces on the Relativity Documentation site.

The Workspace Manager service supports the following functionality:

- CRUD operations on workspaces.

- Helper endpoints for retrieving lists of available resources, such as matters, clients, and others.

- Helper endpoints for retrieving information about advanced settings, such as workspace statuses, full text languages for the SQL Server, and others.

- Helper endpoints for retrieving Azure credentials.

As a sample use case, you can simplify setting up reviews by using the Workspace Manager service to programmatically create multiple workspaces rather than manually adding them through the Relativity UI.

You can also use the Workspace Manager service through the .NET. For more information, see Workspace Manager (.NET) .

## Guidelines for the Workspace Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a workspace:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {workspaceID} to the Artifact ID of a specific workspace.

## Client code sample

To use the Workspace Manager service, send requests by making calls with the required HTTP methods. Use the following base URL for this service:

Copy

```text
1
2

<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/
```

The following sample code is simple .NET client that illustrates how to use the Workspace Manager service to make REST calls.

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
private HttpClient GetHttpClient()

{

    HttpClient httpClient = new HttpClient();



    httpClient.BaseAddress = new Uri("https://localhost/");

    httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    httpClient.DefaultRequestHeaders.Add("Authorization", "Basic " +

        Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));



    return httpClient;

}



private string BASE_URL = "Relativity.REST/api/Relativity.Workspaces/workspace";



private async Task<List<int>> GetArtifactIDList(HttpClient httpClient, string url)

{

    HttpResponseMessage response = await httpClient.GetAsync(url);

    string resultString = await response.Content.ReadAsStringAsync();



    var artifactIDs = new List<int>();



    dynamic objects = JArray.Parse(resultString) as JArray;

    foreach (var obj in objects)

    {

        int artifactID = obj.ArtifactID;

        artifactIDs.Add(artifactID);

    }



    return artifactIDs;

}



private async Task<List<int>> QueryArtifactIDList(HttpClient httpClient, string url)

{

    var queryRequest = new

    {

        request = new

        {

            Fields = new[]

            {

                new { Name = "*" }

            },

            Condition = ""

        },

        start = 1,

        length = 1000

    };



    StringContent payload = new StringContent(JsonConvert.SerializeObject(queryRequest), Encoding.UTF8, "application/json");

    HttpResponseMessage response = await httpClient.PostAsync(url, payload);

    string resultString = await response.Content.ReadAsStringAsync();



    var artifactIDs = new List<int>();



    dynamic result = JObject.Parse(resultString) as JObject;

    foreach (var obj in result.Objects)

    {

        int artifactID = obj.ArtifactID;

        artifactIDs.Add(artifactID);

    }



    return artifactIDs;

}



public async Task<List<int>> GetEligibleStatuses(HttpClient httpClient)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-statuses");

}



public async Task<List<int>> GetEligibleResourcePools(HttpClient httpClient)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-resource-pools");

}



public async Task<List<int>> GetEligibleFileRepositories(HttpClient httpClient, int resourcePoolID)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-resource-pools/{resourcePoolID}/eligible-file-repositories");

}



public async Task<List<int>> GetEligibleCacheLocations(HttpClient httpClient, int resourcePoolID)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-resource-pools/{resourcePoolID}/eligible-cache-locations");

}



public async Task<List<int>> GetEligibleSqlServers(HttpClient httpClient, int resourcePoolID)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-resource-pools/{resourcePoolID}/eligible-sql-servers");

}



public async Task<List<int>> GetEligibleAzureCredentials(HttpClient httpClient, int resourcePoolID)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-resource-pools/{resourcePoolID}/eligible-azure-credentials");

}



public async Task<List<int>> GetEligibleAzureFileSystemCredentials(HttpClient httpClient, int resourcePoolID)

{

    return await GetArtifactIDList(httpClient, $"{BASE_URL}/eligible-resource-pools/{resourcePoolID}/eligible-azure-file-system-credentials");

}



public async Task<List<int>> QueryEligibleMatters(HttpClient httpClient)

{

    return await QueryArtifactIDList(httpClient, $"{BASE_URL}/query-eligible-matters");

}



public async Task<List<int>> QueryEligibleTemplates(HttpClient httpClient)

{

    return await QueryArtifactIDList(httpClient, $"{BASE_URL}/query-eligible-templates");

}



public async Task<int> GetDefaultSqlFullTextLanguage(HttpClient httpClient)

{

    HttpResponseMessage response = await httpClient.GetAsync($"{BASE_URL}/eligible-sql-full-text-languages");

    string resultString = await response.Content.ReadAsStringAsync();

    dynamic languages = JObject.Parse(resultString) as JObject;

    int defaultLanguageID = languages.DefaultLanguageLcid;

    return defaultLanguageID;

}



public async Task<string> GetDefaultDownloadHandlerUrl(HttpClient httpClient)

{

    HttpResponseMessage response = await httpClient.GetAsync($"{BASE_URL}/default-download-handler-url");

    string result = await response.Content.ReadAsStringAsync();

    return JsonConvert.DeserializeObject<string>(result);

}



public async Task<int> CreateWorkspace(string name)

{

    HttpClient httpClient = GetHttpClient();



    int statusID = (await GetEligibleStatuses(httpClient)).First();

    int matterID = (await QueryEligibleMatters(httpClient)).First();

    string defaultDownloadHandlerUrl = await GetDefaultDownloadHandlerUrl(httpClient);

    int resourcePoolID = (await GetEligibleResourcePools(httpClient)).First();

    int fileRepositoryID = (await GetEligibleFileRepositories(httpClient, resourcePoolID)).First();

    int cacheLocationID = (await GetEligibleCacheLocations(httpClient, resourcePoolID)).First();

    int sqlServerID = (await GetEligibleSqlServers(httpClient, resourcePoolID)).First();

    int sqlFullTextLanguage = await GetDefautlSqlFullTextLanguage(httpClient);

    int templateID = (await QueryEligibleTemplates(httpClient)).First();



    var payloadObject = new

    {

        workspaceRequest = new

        {

            Name = name,

            Status = new { ArtifactID = statusID },

            Matter = new { Secured = false, Value = new { ArtifactID = matterID } },

            DownloadHandlerUrl = defaultDownloadHandlerUrl,

            EnableDataGrid = false,

            ResourcePool = new { Secured = false, Value = new { ArtifactID = resourcePoolID } },

            DefaultFileRepository = new { Secured = false, Value = new { ArtifactID = fileRepositoryID } },

            DefaultCacheLocation = new { Secured = false, Value = new { ArtifactID = cacheLocationID } },

            SqlServer = new { Secured = false, Value = new { ArtifactID = sqlServerID } },

            SqlFullTextLanguage = sqlFullTextLanguage,

            Template = new { Secured = false, Value = new { ArtifactID = templateID } },

            Keywords = "sample keywords for workspace",

            Notes = "sample notes for workspace"

        }

    };



    StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

    HttpResponseMessage response = await httpClient.PostAsync($"{BASE_URL}/", payload);

    string resultString = await response.Content.ReadAsStringAsync();



    dynamic result = JObject.Parse(resultString) as JObject;

    int artifactID = result.ArtifactID;

    return artifactID;

}
```

## Create a workspace

To add a new workspace to Relativity, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace
```

All fields related to the infrastructure details; DownloadHandlerUrl , Resource Pool , DefaultFileRepository , DataGridFileRepositor y, DefaultCacheLocation , and SqlServer are optional. If the infrastructure details are not explicitly specified in the request, they are automatically selected by the algorithm.

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for the workspace set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View field descriptions for a create request

The body of the request must contain a workspaceRequest object with the following fields:

- DownloadHandlerUrl - a string representing the default URL used to make downloaded files available to users. This field is optional. If not specified in the request, the default URL is automatically selected by the algorithm.

- EnableDataGrid - a Boolean value indicating whether the workspace can have fields that save to Data Grid. This field can't be set during create operation.

- Matter - represents a securable matter object. A matter is the case or legal action associated with the workspace. It contains the following fields:

- Secured - a Boolean value indicating whether the current user has permissions to view the settings in the Value field. The user can't view the Value field when this value is true. For a create request, set this value to false .

- Value - contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

- Name - the user-friendly name of the workspace.

- ResourcePool - represents a securable resource pool object associated with the workspace. See descriptions for the Secured and Value fields under Matter. This field is optional. If not specified in the request, the resource pool is automatically selected by the algorithm.

- DefaultFileRepository - represents a securable file repository server object associated with the workspace. See descriptions for the Secured and Value fields under Matter. This field is optional. If not specified in the request, the file repository server is automatically selected by the algorithm.

- DataGridFileRepository - represents a securable file repository server object used for Data Grid. See descriptions for the Secured and Value fields under Matter. This field is optional. If not specified in the request, the file repository server for Data Grid is automatically selected by the algorithm.

- DefaultCacheLocation - represents a securable cache location server object associated with the workspace. See descriptions for the Secured and Value fields under Matter. This field is optional. If not specified in the request, the cache location server is automatically selected by the algorithm.

- SqlServer - represents a securable SQL server object associated with the workspace. See descriptions for the Secured and Value fields under Matter. This field is optional. If not specified in the request, the SQL server is automatically selected by the algorithm.

- AzureCredentials - represents a securable Azure credentials object associated with the workspace.

- AzureFileSystemCredentials - represents a securable Azure file system credentials object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- SqlFullTextLanguage - an integer representing the ID of the language used for determining the word-break characters used in the full text index for the workspace.

- Status - an object representing the status of the workspace used in views to filter on workspaces. It contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

- Template - an object representing an existing workspace structure used to create the workspace. You can only set this field in a create request. See descriptions for the Secured and Value fields under Matter .

- Keywords - optional words or phrases used to describe the workspace.

- Notes - additional information about the workspace.

View a sample JSON request with all infrastructure details fields specified Copy

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
{

  "workspaceRequest": {

    "DownloadHandlerUrl": "Relativity.Distributed",

    "EnableDataGrid": false,

    "Matter": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1016816

      }

    },

    "Name": "Sample workspace",

    "ResourcePool": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1015040

      }

    },

    "DefaultFileRepository": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1014887

      }

    },

    "DataGridFileRepository": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1015998

      }

    },

    "DefaultCacheLocation": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1015534

      }

    },

    "SqlServer": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1015096

      }

    },

    "AzureCredentials": null,

    "AzureFileSystemCredentials": null,

    "SqlFullTextLanguage": 1033,

    "Status": {

      "ArtifactID": 675

    },

    "Template": {

        "Secured": false,

        "Value": {

            "ArtifactID": 1014823

        }

    },

    "Keywords": "Sample keywords for a workspace",

    "Notes": "Sample notes for a workspace"

  }

}
```

View a sample JSON request with no infrastructure details fields specified: Copy

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

  "workspaceRequest": {

    "EnableDataGrid": false,

    "Matter": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1016816

      }

    },

    "Name": "Sample workspace",

    "AzureCredentials": null,

    "AzureFileSystemCredentials": null,

    "SqlFullTextLanguage": 1033,

    "Status": {

      "ArtifactID": 675

    },

    "Template": {

        "Secured": false,

        "Value": {

            "ArtifactID": 1014823

        }

    },

    "Keywords": "Sample keywords for a workspace",

    "Notes": "Sample notes for a workspace"

  }

}
```

View field descriptions for a response

The response returns an object representing a new workspace. It contains the following fields:

- Client - a securable client object associated with the workspace. It contains the following fields:

- Secured - a Boolean value indicating whether the current user has permissions to view the settings in the Value field. The user can't view the Value field when this value is true.

- Value - contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

- Name - the user-friendly name of the object.

- ClientNumber - a securable object representing the client's number. It contains the following fields:

- Secured - a Boolean value indicating whether the current user has permissions to view the settings in the Value field. The user can't view the Value field when this value is true.

- Value - a string represents the number for the client.

- DownloadHandlerUrl - a string representing the default URL used to make downloaded files available to users.

- EnableDataGrid - a Boolean value indicating whether the workspace can have fields that save to Data Grid. This field can't be set during create operation.

- Matter - represents a securable matter object. A matter is the case or legal action associated with the workspace. See descriptions for the Secured and Value fields under Client .

- MatterNumber - a string representing the number for the matter associated with the workspace.

- Secured - a Boolean value indicating whether the current user has permissions to view the settings in the Value field. The user can't view the Value field when this value is true.

- Value - a string represents the number for the matter.

- ProductionRestrictions - represents a securable saved search object used for production restrictions. See descriptions for the Secured and Value fields under Client .

- ResourcePool - represents a securable resource pool object associated with the workspace. See descriptions for the Secured and Value fields under Client .

- DefaultFileRepository - represents a securable file repository server object associated with the workspace. See descriptions for the Secured and Value fields under Client .

- DefaultCacheLocation - represents a securable cache location server object associated with the workspace. See descriptions for the Secured and Value fields under Client .

- SqlServer - represents a securable SQL server object associated with the workspace. See descriptions for the Secured and Value fields under Client .

- SqlFullTextLanguage - an object representing the full text language used by the SQL Server. It contains the following fields:

- Name - the name of the full text language used by the SQL Server.

- ID - an integer used as a unique identifier for the language.

- Status - represents a workspace status object associated with the workspace. It contains the following fields:

- Name - the user-friendly name of the status.

- ArtifactID - an integer used to identify the status.

- Guids - an array of GUIDs used to identify the status.

- Keywords - optional words or phrases used to describe the workspace.

- Notes - additional information about the workspace.

- CreatedOn - the date and time when the workspace was created.

- CreatedBy - represents the user who created the workspace. It contains the following fields:

- Name - the name of the user.

- ArtifactID - an integer used to identify the user.

- Guids - an array of GUIDs used to identify the user.

- LastModifiedBy - represents the user who recently updated the workspace. See the field descriptions for the CreatedBy field.

- LastModifiedOn - the date and time when the workspace was most recently modified.

- Name - the user-friendly name of the workspace.

- ArtifactID - an integer used as a unique identifier for the workspace.

- Guids - an array of GUIDs used to identify the workspace.

View a sample JSON response Copy

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
{

  "Client": {

    "Secured": false,

    "Value": {

      "Name": "Relativity",

      "ArtifactID": 1015644,

      "Guids": []

    }

  },

  "ClientNumber": {

    "Secured": false,

    "Value": "Relativity"

  },

  "DownloadHandlerUrl": "Relativity.Distributed",

  "EnableDataGrid": false,

  "Matter": {

    "Secured": false,

    "Value": {

      "Name": "Salt vs. Pepper",

      "ArtifactID": 1016816,

      "Guids": []

    }

  },

  "MatterNumber": {

    "Secured": false,

    "Value": "1"

  },

  "ProductionRestrictions": {

    "Secured": false,

    "Value": {

      "Name": "Saved Search 1",

      "ArtifactID": 1117132,

      "Guids": []

    }

  },

  "ResourcePool": {

    "Secured": false,

    "Value": {

      "Name": "Default",

      "ArtifactID": 1015040,

      "Guids": []

    }

  },

  "DefaultFileRepository": {

    "Secured": false,

    "Value": {

      "Name": "\\\\A-BC-DE-FGHIJK\\fileshare\\",

      "ArtifactID": 1014887,

      "Guids": []

    }

  },

  "DefaultCacheLocation": {

    "Secured": false,

    "Value": {

      "Name": "Default Cache Location",

      "ArtifactID": 1015534,

      "Guids": []

    }

  },

  "SqlServer": {

    "Secured": false,

    "Value": {

      "Name": "A-BC-DE-FGHIJK\\EDDSINSTANCE001",

      "ArtifactID": 1015096,

      "Guids": []

    }

  },

  "SqlFullTextLanguage": {

    "Name": "English",

    "ID": 1033

  },

  "Status": {

    "Name": "Active",

    "ArtifactID": 675,

    "Guids": []

  },

  "Keywords": "Sample keywords for a workspace",

  "Notes": "Sample notes for a workspace",

  "CreatedOn": "2018-04-24T15:19:57.677",

  "CreatedBy": {

    "Name": "Admin, Relativity",

    "ArtifactID": 9,

    "Guids": []

  },

  "LastModifiedBy": {

    "Name": "Admin, Relativity",

    "ArtifactID": 9,

    "Guids": []

  },

  "LastModifiedOn": "2020-01-09T15:51:39.13",

  "Name": "Sample workspace",

  "ArtifactID": 1017266,

  "Guids": []

}
```

## Create operation helper methods

The following helper endpoints provide functionality to support the create operation.

### Retrieve unsupported fields for a create operation

To retrieve unsupported fields on a WorkspaceRequest object for a create operation, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/meta
```

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for the workspace set at the instance level. See Instance security on the Relativity Documentation site.

The request body is empty.

The response contains the following fields

- Unsupported - an array of fields that aren't supported on the WorkspaceRequest object for a create operation.

- ReadOnly - an array of fields that can't be modified on the WorkspaceRequest object for a create operation.

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

    "Unsupported": [

        "AzureCredentials",

        "AzureFileSystemCredentials"

    ],

    "ReadOnly": []

}
```

### Retry failed create event handlers

To retry failed create event handlers, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}/retry-failed-create-event-handlers
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the workspace level. See Workspace security on the Relativity Documentation site.

When the failed create event handlers are successfully retried, the response returns the status code of 200.

## Retrieve a workspace

To retrieve a workspace, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}
```

View required permissions

To use this endpoint, the caller must have the following:

- View Workspace Details permissions for the workspace set at the workspace level. See Workspace security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin. See Instance security on the Relativity Documentation site.

This permission is required for the admin-level context workspace. Use -1 to indicate the admin-level context.

The response for a read operation contains many of the same fields as those for a body of a create request. See View field descriptions for a create request .

View additional field descriptions for a response

- ArtifactID - an integer used as a unique identifier for the workspace.

- Guids - an array of GUIDs used to identify the workspace.

- ProductionRestrictions - represents a securable saved search object used for production restrictions. See descriptions for the Secured and Value fields under Matter.

View sample JSON response Copy

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
{

  "ArtifactID": 245678,

  "Guids": [

    "CE780D86-4217-45D7-83A2-0934F2F66B17"

  ],

  "Name": "New Workspace",

  "Matter": {

    "Secured": false,

    "Value": {

      "ArtifactID": 123456

    }

  },

  "Status": {

    "ArtifactID": 345678

  },

  "ResourcePool": {

    "Secured": false,

    "Value": {

      "ArtifactID": 456789

    }

  },

  "SqlServer": {

    "Secured": false,

    "Value": {

      "ArtifactID": 567890

    }

  },

  "DefaultFileRepository": {

    "Secured": false,

    "Value": {

      "ArtifactID": 567890

    }

  },

  "DefaultCacheLocation": {

    "Secured": false,

    "Value": {

      "ArtifactID": 567890

    }

  },

  "DownloadHandlerUrl": "Relativity.Distributed",

  "EnableDataGrid": false,

  "ProductionRestrictions": {

    "Secured": false,

    "Value": {

      "ArtifactID": 678901

    }

  },

  "DataGridFileRepository": {

    "Secured": false,

    "Value": {

      "ArtifactID": 789012

    }

  },

  "AzureCredentials": {

    "Secured": false,

    "Value": {

      "ArtifactID": 890123

    }

  },

  "AzureFileSystemCredentials": {

    "Secured": false,

    "Value": {

      "ArtifactID": 901234

    }

  },

  "SqlFullTextLanguage": "English",

  "WorkspaceAdminGroup": {

    "Secured": false,

    "Value": {

      "ArtifactID": 134567

    }

  },

  "Keywords": "",

  "Notes": ""

}
```

## Update a workspace

To modify the properties of a workspace, send a PUT request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}
```

View required permissions

To use this endpoint, the caller must have the following:

- Edit permissions for the workspace set at the workspace level. See Workspace security on the Relativity Documentation site.

- View Workspace Details permissions for the workspace set at the workspace level.

To update the WorkspaceAdminGroup or Matter properties, the calling user must be a system admin or client domain admin. The admin workspace can't be updated. It resides in the admin level context indicated by -1.

View field descriptions for an update request

For read-only fields, set their Secured property set to true, and set their Value properties to null. For more information, see Field permissions .

The body of request must contain a workspaceRequest object with the following fields:

- Name - the user-friendly name of the workspace.

- Matter - represents a securable matter object. A matter is the case or legal action associated with the workspace. It contains the following fields:

- Secured - a Boolean value indicating whether the current user has permissions to view the settings in the Value field. The user can't view the Value field when this value is true. For a create request, set this value to false .

- Value - contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

-

Template - an object representing an existing workspace structure used to create the workspace. See descriptions for the Secured and Value fields under Matter .

Leave the Template property blank because you can only set it at workspace creation.

- Status - represents a workspace status object associated with the workspace. It contains the following field:

- ArtifactID - an integer used to identify the status.

- ResourcePool - represents a securable resource pool object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- SqlServer - represents a securable SQL server object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- DefaultFileRepository - represents a securable file repository server object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- DefaultCacheLocation - represents a securable cache location server object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- DownloadHandlerUrl - a string representing the default URL used to make downloaded files available to users.

- EnableDataGrid - a Boolean value indicating whether the workspace can have fields that save to Data Grid.

- ProductionRestrictions - represents a securable saved search object used for production restrictions. See descriptions for the Secured and Value fields under Matter .

- DataGridFileRepository - represents a securable file repository server object used for Data Grid. See descriptions for the Secured and Value fields under Matter .

- AzureCredentials - represents a securable Azure credentials object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- AzureFileSystemCredentials - represents a securable Azure file system credentials object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- SqlFullTextLanguage - an integer representing the ID of the language used for determining the word-break characters used in the full text index for the workspace.

- WorkspaceAdminGroup - a securable group object associated with the workspace. See descriptions for the Secured and Value fields under Matter .

- Keywords - optional words or phrases used to describe the workspace.

- Notes - additional information about the workspace.

View sample JSON request Copy

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
{

  "workspaceRequest": {

    "Name": "New Workspace",

    "Matter": {

      "Secured": false,

      "Value": {

        "ArtifactID": 123456

      }

    },

    "Template": {

      "Secured": false,

      "Value": {

        "ArtifactID": 234567

      }

    },

    "Status": {

      "ArtifactID": 345678

    },

    "ResourcePool": {

      "Secured": false,

      "Value": {

        "ArtifactID": 456789

      }

    },

    "SqlServer": {

      "Secured": false,

      "Value": {

        "ArtifactID": 567890

      }

    },

    "DefaultFileRepository": {

      "Secured": false,

      "Value": {

        "ArtifactID": 567890

      }

    },

    "DefaultCacheLocation": {

      "Secured": false,

      "Value": {

        "ArtifactID": 567890

      }

    },

    "DownloadHandlerUrl": "Relativity.Distributed",

    "EnableDataGrid": false,

    "ProductionRestrictions": {

      "Secured": false,

      "Value": {

        "ArtifactID": 678901

      }

    },

    "DataGridFileRepository": {

      "Secured": false,

      "Value": {

        "ArtifactID": 789012

      }

    },

    "AzureCredentials": {

      "Secured": false,

      "Value": {

        "ArtifactID": 890123

      }

    },

    "AzureFileSystemCredentials": {

      "Secured": false,

      "Value": {

        "ArtifactID": 901234

      }

    },

    "SqlFullTextLanguage": 1033,

    "WorkspaceAdminGroup": {

      "Secured": false,

      "Value": {

        "ArtifactID": 134567

      }

    },

    "Keywords": "",

    "Notes": ""

  }

}
```

The response for an update operation contains the same fields as those for a request. See the field descriptions for View field descriptions for an update request .

View sample JSON response Copy

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

  "ArtifactID": 245678,

  "Guids": [

    "CE780D86-4217-45D7-83A2-0934F2F66B17"

  ],

  "Name": "New Workspace",

  "Matter": {

    "Secured": false,

    "Value": {

      "ArtifactID": 123456

    }

  },

  "Template": {

    "Secured": false,

    "Value": {

      "ArtifactID": 234567

    }

  },

  "Status": {

    "ArtifactID": 345678

  },

  "ResourcePool": {

    "Secured": false,

    "Value": {

      "ArtifactID": 456789

    }

  },

  "SqlServer": {

    "Secured": false,

    "Value": {

      "ArtifactID": 567890

    }

  },

  "DefaultFileRepository": {

    "Secured": false,

    "Value": {

      "ArtifactID": 567890

    }

  },

  "DefaultCacheLocation": {

    "Secured": false,

    "Value": {

      "ArtifactID": 567890

    }

  },

  "DownloadHandlerUrl": "Relativity.Distributed",

  "EnableDataGrid": false,

  "ProductionRestrictions": {

    "Secured": false,

    "Value": {

      "ArtifactID": 678901

    }

  },

  "DataGridFileRepository": {

    "Secured": false,

    "Value": {

      "ArtifactID": 789012

    }

  },

  "AzureCredentials": {

    "Secured": false,

    "Value": {

      "ArtifactID": 890123

    }

  },

  "AzureFileSystemCredentials": {

    "Secured": false,

    "Value": {

      "ArtifactID": 901234

    }

  },

  "SqlFullTextLanguage": 1033,

  "WorkspaceAdminGroup": {

    "Secured": false,

    "Value": {

      "ArtifactID": 134567

    }

  },

  "Keywords": "",

  "Notes": ""

}
```

## Delete a workspace

To remove a workspace from Relativity, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}
```

The request body is empty.

View required permissions

To use this endpoint, the caller must have the following:

- View and Delete permissions for the workspace set at the workspace level. See Workspace security on the Relativity Documentation site.

When the workspace is successfully deleted, the response returns the status code of 200.

## Retrieve workspace statistics

To retrieve a summary of workspace statistics, send a GET request to a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}/summary
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the workspace level. See Workspace security on the Relativity Documentation site.

The request body is empty.

The response contains the following fields:

- DocumentCount - a long representing the number of documents in a workspace.

- FileSize - a long representing the total size of the workspace files in bytes.

Copy

```text
1
2
3
4
{

  "DocumentCount": 73973,

  "FileSize": 0

}
```

## Retrieve workspaces associated with a group

To retrieve workspaces associated with a group, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/query-by-group/{groupID}
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for the group set at the instance level. See Instance security on the Relativity Documentation site.

View field descriptions for a request

The body of a request contains the following fields:

- request - represents the request object. It contains the following fields:

- Fields - an array of objects describing the fields to query. Each object contains the following fields:

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guid - a GUID used to identify the field.

- Name - the user-friendly name of a field.

- Condition - the search criteria used for the query.

- Sorts - a list of objects describing the sort rules for the results. Each object contains the following fields:

- Field - an object describing the field. It contains the following fields:

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guid - a GUID used to identify the field.

- Name - the user-friendly name of the field.

- Direction - a string specifying whether to sort the query results in ascending or descending order. Set this field to Ascending or Descending .

- RowCondition - the search criteria used for the query.

- start - an integer indicating the index of the first item in the query.

- length - an integer indicating the number of items to query.

View a sample JSON request Copy

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

  "request": {

    "Fields": [

      {

        "Name": "*"

      }

    ],

    "Condition": null

  },

"start": 1,

"length": 1000

}
```

View field descriptions for a response

The response contains the following fields:

- TotalCount - an integer indicating the total number of items returned by the query.

- Objects - a list of objects containing the results of a query. Each object contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Values - an array of values for the requested fields.

- CurrentStartIndex - an integer indicating the index of the first item in the result set.

- ResultCount - an integer indicating the number of items in the result set.

- Fields - an array of objects describing fields. Each object contains the following fields:

- FieldType - a string indicating the type of the field, such as FixedLengthText, Date, or others.

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guids - an array of GUIDs used to identify the field.

View a sample JSON response Copy

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
{

  "TotalCount": 3,

  "Objects": [

    {

      "ArtifactID": 1000002,

      "Values": [

        "Relativity Template",

        "Edit",

        "0001",

        "Relativity Template 2",

        "Active",

        "0001",

        "Admin, Relativity",

        "Admin, Relativity",

        "2007-01-01T00:00:00",

        "2008-08-05T00:36:05.54",

        "kk",

        "nn",

        1000002,

        {

          "OverwriteInheritedSecurity": false,

          "UserCanEditSecurity": false

        },

        {

          "ArtifactID": 1006066,

          "Guids": [],

          "Name": "Relativity Template 2",

          "ItemSecured": false

        },

        "Relativity Template"

      ]

    },

    {

      "ArtifactID": 1016816,

      "Values": [

        "Salt vs. Pepper",

        "Edit",

        "1",

        "Relativity",

        "Active",

        "Relativity",

        "Admin, Relativity",

        "Admin, Relativity",

        "2018-04-24T13:57:34.92",

        "2019-08-08T13:59:16.733",

        "keywords",

        "notes",

        1016816,

        {

          "OverwriteInheritedSecurity": false,

          "UserCanEditSecurity": false

        },

        {

          "ArtifactID": 1015644,

          "Guids": [],

          "Name": "Relativity",

          "ItemSecured": false

        },

        "Salt vs. Pepper"

      ]

    },

    {

      "ArtifactID": 1027403,

      "Values": [

        "Sample matter",

        "Edit",

        "12345",

        "Changed name",

        "Active",

        "Updated client number",

        "Admin, Relativity",

        "Admin, Relativity",

        "2019-11-20T15:21:51.247",

        "2019-11-20T15:21:51.247",

        "",

        "",

        1027403,

        {

          "OverwriteInheritedSecurity": false,

          "UserCanEditSecurity": false

        },

        {

          "ArtifactID": 1022225,

          "Guids": [],

          "Name": "Changed name",

          "ItemSecured": false

        },

        "Sample matter"

      ]

    }

  ],

  "IDWindow": [],

  "CurrentStartIndex": 1,

  "ResultCount": 3,

  "ObjectType": {

    "ArtifactID": 1016187,

    "Name": "Matter",

    "Guids": [],

    "ArtifactTypeID": 6

  },

  "RankWindow": [],

  "Fields": [

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 28,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Name"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "Empty",

      "ViewFieldID": 31,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Edit"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 32,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Number"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 33,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Client Name"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 35,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Status"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 45,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Client Number"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 136,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Created By"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 137,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Last Modified By"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "Date",

      "ViewFieldID": 138,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Created On"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "Date",

      "ViewFieldID": 139,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Last Modified On"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 140,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Keywords"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 141,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Notes"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "WholeNumber",

      "ViewFieldID": 1000098,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Artifact ID"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 0,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Security"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "SingleObject",

      "ViewFieldID": 1000486,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Client"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 0,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Text Identifier"

    }

  ]

}
```

## Resource information helper methods

The following helper methods correspond to the fields that you can set in the Resource Information section of the Workspace form in the Relativity UI. For more information, see Workspaces on the Relativity Documentation site.

### Retrieve matters

To retrieve a list of matters, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/query-eligible-matters
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for matters set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View field descriptions for a request

The body of a request contains the following fields:

- request - represents the request object. It contains the following fields:

- Fields - an array of objects describing the fields to query. Each object contains the following fields:

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guid - a GUID used to identify the field.

- Name - the user-friendly name of a field.

- Condition - the search criteria used for the query.

- Sorts - a list of objects describing the sort rules for the results. Each object contains the following fields:

- Field - an object describing the field. It contains the following fields:

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guid - a GUID used to identify the field.

- Name - the user-friendly name of the field.

- Direction - a string specifying whether to sort the query results in ascending or descending order. Set this field to Ascending or Descending .

- RowCondition - the search criteria used for the query.

- start - an integer indicating the index of the first item in the query.

- length - an integer indicating the number of items to query.

View a sample JSON request Copy

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

  "request": {

    "Fields": [

      {

        "Name": "*"

      }

    ],

    "Condition": null

  },

"start": 1,

"length": 1000

}
```

View field descriptions for a response

The response contains the following fields:

- TotalCount - an integer indicating the total number of items returned by the query.

- Objects - a list of objects containing the results of a query. Each object contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Values - an array of values for the requested fields.

- CurrentStartIndex - an integer indicating the index of the first item in the result set.

- ResultCount - an integer indicating the number of items in the result set.

- Fields - an array of objects describing fields. Each object contains the following fields:

- FieldType - a string indicating the type of the field, such as FixedLengthText, Date, or others.

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guids - an array of GUIDs used to identify the field.

View a sample JSON response Copy

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
{

  "TotalCount": 3,

  "Objects": [

    {

      "ArtifactID": 1000002,

      "Values": [

        "Relativity Template",

        "Edit",

        "0001",

        "Relativity Template 2",

        "Active",

        "0001",

        "Admin, Relativity",

        "Admin, Relativity",

        "2007-01-01T00:00:00",

        "2008-08-05T00:36:05.54",

        "kk",

        "nn",

        1000002,

        {

          "OverwriteInheritedSecurity": false,

          "UserCanEditSecurity": false

        },

        {

          "ArtifactID": 1006066,

          "Guids": [],

          "Name": "Relativity Template 2",

          "ItemSecured": false

        },

        "Relativity Template"

      ]

    },

    {

      "ArtifactID": 1016816,

      "Values": [

        "Salt vs. Pepper",

        "Edit",

        "1",

        "Relativity",

        "Active",

        "Relativity",

        "Admin, Relativity",

        "Admin, Relativity",

        "2018-04-24T13:57:34.92",

        "2019-08-08T13:59:16.733",

        "keywords",

        "notes",

        1016816,

        {

          "OverwriteInheritedSecurity": false,

          "UserCanEditSecurity": false

        },

        {

          "ArtifactID": 1015644,

          "Guids": [],

          "Name": "Relativity",

          "ItemSecured": false

        },

        "Salt vs. Pepper"

      ]

    },

    {

      "ArtifactID": 1027403,

      "Values": [

        "Sample matter",

        "Edit",

        "12345",

        "Changed name",

        "Active",

        "Updated client number",

        "Admin, Relativity",

        "Admin, Relativity",

        "2019-11-20T15:21:51.247",

        "2019-11-20T15:21:51.247",

        "",

        "",

        1027403,

        {

          "OverwriteInheritedSecurity": false,

          "UserCanEditSecurity": false

        },

        {

          "ArtifactID": 1022225,

          "Guids": [],

          "Name": "Changed name",

          "ItemSecured": false

        },

        "Sample matter"

      ]

    }

  ],

  "IDWindow": [],

  "CurrentStartIndex": 1,

  "ResultCount": 3,

  "ObjectType": {

    "ArtifactID": 1016187,

    "Name": "Matter",

    "Guids": [],

    "ArtifactTypeID": 6

  },

  "RankWindow": [],

  "Fields": [

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 28,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Name"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "Empty",

      "ViewFieldID": 31,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Edit"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 32,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Number"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 33,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Client Name"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 35,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Status"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 45,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Client Number"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 136,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Created By"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 137,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Last Modified By"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "Date",

      "ViewFieldID": 138,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Created On"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "Date",

      "ViewFieldID": 139,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Last Modified On"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 140,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Keywords"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 141,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Notes"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "WholeNumber",

      "ViewFieldID": 1000098,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Artifact ID"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 0,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Security"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "SingleObject",

      "ViewFieldID": 1000486,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Client"

    },

    {

      "FieldCategory": "Generic",

      "FieldType": "FixedLengthText",

      "ViewFieldID": 0,

      "ArtifactID": 0,

      "Guids": [],

      "Name": "Text Identifier"

    }

  ]

}
```

### Retrieve clients

To retrieve a list of clients available for this workspace, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/query-eligible-clients
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

This endpoint uses the same format for requests and responses as the query for matters. For field descriptions and sample JSON, see Retrieve matters .

### Retrieve workspaces for use as templates

To retrieve a list of workspaces for use as templates when creating a new workspace, send a POST request with URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/query-eligible-templates
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

This endpoint uses the same format for requests and responses as the query for matters. For field descriptions and sample JSON, see Retrieve matters .

### Retrieve resource pools

To retrieve a list of resource pools, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-resource-pools
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

The request body is empty.

View field descriptions for a response

The response contains an array of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the resource pool.

- Guids - an array of GUIDs used to identify the resource pool.

- Name - the user-friendly name of the resource pool.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
[

  {

    "Name": "Default",

    "ArtifactID": 1015040,

    "Guids": []

  }

]
```

### Retrieve SQL Servers

To retrieve a list of available SQL Servers, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-resource-pools/{resourcePoolID}/eligible-sql-servers
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

The request body is empty.

View field descriptions for a response

The response contains an array of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the server.

- Guids - an array of GUIDs used to identify the server.

- Name - the user-friendly name of the server.

View sample JSON response Copy

```text
1
2
3
4
5
6
7
[

  {

    "Name": "A-BC-DE-FGHIJK\\EDDSINSTANCE001",

    "ArtifactID": 1015096,

    "Guids": []

  }

]
```

### Retrieve file repository servers

To retrieve a list of available file repository servers, send a GET with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-resource-pools/{resourcePoolID}/eligible-file-repositories
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

The request body is empty.

View field descriptions for a response

The response contains an array of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the server.

- Guids - an array of GUIDs used to identify the server.

- Name - the user-friendly name of the server.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
[

  {

    "Name": "\\\\A-BC-DE-FGHIJK\\fileshare\\",

    "ArtifactID": 1014887,

    "Guids": []

  }

]
```

### Retrieve cache location servers

To retrieve a list of available cache location servers, send a GET with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-resource-pools/{resourcePoolID}/eligible-cache-locations
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

View field descriptions for a response

The response contains an array of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the server.

- Guids - an array of GUIDs used to identify the server.

- Name - the user-friendly name of the server.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
[

  {

    "Name": "Default Cache Location",

    "ArtifactID": 1015534,

    "Guids": []

  }

]
```

### Retrieve the URL for the default download handler

To retrieve the URL for the default download handler, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/default-download-handler-url
```

This endpoint doesn't require any specific permissions.

The request body is empty.

The response contains a string representation of the default download handler URL.

Copy

```text
1
"Relativity.Distributed"
```

## Advanced settings helper methods

The following helper methods correspond to the fields that you can set in the Advanced settings section of the Workspace form in the Relativity UI. For more information, see Workspaces on the Relativity Documentation site.

### Retrieve available statuses for a workspace

To retrieve available statuses for a workspace, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-statuses
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for the resource server set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

The request body is empty.

View field descriptions for a response

The response contains an array of objects with the following fields:

- Name - the user-friendly name for the status.

- ArtifactID - an integer used as a unique identifier for the status.

- Guids - an array of GUIDs used to identify the status.

View a sample Json response Copy

```text
1
2
3
4
5
6
7
[

    {

        "Name": "Active",

        "ArtifactID": 675,

        "Guids": []

    }

]
```

### Retrieve full text languages for SQL Server

To retrieve a list of available full text languages for the SQL Server assigned to a workspace, send a GET request to a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-sql-full-text-languages
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for the resource server set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View field descriptions for a response

The response contains the following fields:

- DefaultLanguageLcid - an integer used as a unique identifier for the default language.

- Languages - an array of objects describing the supported languages. Each object contains the following fields:

- ID - an integer used as a unique identifier for the language.

- Name - a string representing the name of the language.

View a sample Json response Copy

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

  "DefaultLanguageLcid": 1033,

  "Languages": [

    {

      "Name": "Arabic",

      "ID": 1025

    },

    {

      "Name": "Bengali (India)",

      "ID": 1093

    },

    {

      "Name": "Bokmål",

      "ID": 1044

    },

    {

      "Name": "Vietnamese",

      "ID": 1066

    }

  ]

}
```

### Retrieve groups for workspace membership

To retrieve a list of groups available for workspace membership, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/query-eligible-groups
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

This endpoint uses the same format for requests and responses as the query for matters. For field descriptions and sample JSON, see Retrieve matters .

### Retrieve saved searches for production restrictions

You can retrieve saved searches for use with production restrictions. For more information, see Adding and editing production restrictions on the Relativity Documentation site.

Send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/{workspaceID}/query-eligible-saved-searches
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for workspaces set at the workspace level. See Workspace security on the Relativity Documentation site.

This endpoint uses the same format for requests and responses as the query for matters. For field descriptions and sample JSON, see Retrieve matters .

## Azure credentials helper methods

Use the following methods to retrieve Azure credentials associated with a resource pool or file system. For more information, see Workspaces on the Relativity Documentation site.

### Retrieve Azure credentials

To retrieve a list of available Azure credentials associated with a resource pool, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-resource-pools/{resourcePoolID}/eligible-azure-credentials
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

View field descriptions for a response

The response contains an array of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the Azure credentials.

- Guids - an array of GUIDs used to identify the Azure credentials.

- Name - the user-friendly name for the Azure credentials.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
[

  {

    "Name": "Example",

    "ArtifactID": 1015096,

    "Guids": []

  }

]
```

### Retrieve Azure file system credentials

To retrieve a list of available Azure file system credentials, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspace/eligible-resource-pools/{resourcePoolID}/eligible-azure-file-system-credentials
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for resource pools set at the instance level. See Instance security on the Relativity Documentation site.

View field descriptions for a response

The response contains an array of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the Azure credentials.

- Guids - an array of GUIDs used to identify the Azure credentials.

- Name - the user-friendly name for the Azure credentials.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
[

  {

    "Name": "Example",

    "ArtifactID": 1015096,

    "Guids": []

  }

]
```

On this page

- Workspace Manager (REST)

- Guidelines for the Workspace Manager service

- URLs

- Client code sample

- Create a workspace

- Create operation helper methods

- Retrieve unsupported fields for a create operation

- Retry failed create event handlers

- Retrieve a workspace

- Update a workspace

- Delete a workspace

- Retrieve workspace statistics

- Retrieve workspaces associated with a group

- Resource information helper methods

- Retrieve matters

- Retrieve clients

- Retrieve workspaces for use as templates

- Retrieve resource pools

- Retrieve SQL Servers

- Retrieve file repository servers

- Retrieve cache location servers

- Retrieve the URL for the default download handler

- Advanced settings helper methods

- Retrieve available statuses for a workspace

- Retrieve full text languages for SQL Server

- Retrieve groups for workspace membership

- Retrieve saved searches for production restrictions

- Azure credentials helper methods

- Retrieve Azure credentials

- Retrieve Azure file system credentials


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
