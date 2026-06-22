---
title: "Resource File (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Resource_File_service.htm
collection: developer
fetched_at: 2026-06-22T06:27:56+00:00
sha256: ae77a8a5a8eeb885f7fbd5adf0f775f844b25e4e3e69b327e3954fc437031769
---

Resource File (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Resource File (REST)

The Resource File API allows clients to manage resource files for the Relativity applications in their environment. It includes support for the following features:

- Create, read, update, delete, and download of resource files.

- Update and upload of file content and metadata.

- Helper services for the client, including retrieving all available applications.

## Guidelines for the Resource File service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a resource file:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {resourceFileID} to the Artifact ID of a specific resource file.

## Client code sample

To use the Resource File service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.REST/API/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{applicationID}/
```

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
public async Task<ResourceFileResponse> ReadResourceFile(int resourceFileID)

{

    ResourceFileResponse response = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", string.Empty);

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("relativity.admin@kcura.com:Test1234!")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");



        string url = $"/Relativity.REST/API/relativity-environment/v1/workspaces/-1/resource-files/{resourceFileArtifactId}/";

        System.Net.Http.HttpResponseMessage httpResponse = await client.GetAsync(url);

        httpResponse.EnsureSuccessStatusCode();

        string content = await httpResponse.Content.ReadAsStringAsync();

        response = JsonConvert.DeserializeObject<LibraryApplicationResponse>(content);

    }



    return response;

}
```

## Create a resource file

To create a resource file, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files
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
{

  "resourceFileRequest": {

    "Application": {

      "Guids":["3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46"]

    },

    "FileName": "TestEventHandlerFailures.dll"

  }

}
```

The newly created artifact ID of the resource file will be returned in the response.

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
{

    "ObjectIdentifier": {

        "ArtifactID": 1669611,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "TestEventHandlerFailures.dll",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "",

    "Notes": "",

    "CreatedOn": "2020-11-05T20:08:25.717",

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

    "LastModifiedOn": "2020-11-05T20:08:25.717",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "Application"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669611",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669611",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

}
```

## Read a resouce file

To read a resource sile, send a POST request with a URL in one of the following formats:

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}/{includeMetadata}/{IncludeActions}
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
{

    "ObjectIdentifier": {

        "ArtifactID": 1669611,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "TestEventHandlerFailures.dll",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "",

    "Notes": "",

    "CreatedOn": "2020-11-05T20:08:25.717",

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

    "LastModifiedOn": "2020-11-05T20:08:25.717",

    "Actions": []

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
54
55
56
57
58
{

    "ObjectIdentifier": {

        "ArtifactID": 1669611,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "TestEventHandlerFailures.dll",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "",

    "Notes": "",

    "CreatedOn": "2020-11-05T20:08:25.717",

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

    "LastModifiedOn": "2020-11-05T20:08:25.717",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "Application"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669611",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669611",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

}
```

## Update a resource file

To read a resource sile, send a POST request with a URL in one of the following formats:

Copy

```text
1
2
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}

<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}/contents/{contentsKey}
```

View JSON for a sample request

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
{

    "ObjectIdentifier": {

        "ArtifactID": 1669628,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "New1.txt",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "update2",

    "Notes": "update2",

    "CreatedOn": "2020-11-06T14:14:24.603",

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

    "LastModifiedOn": "2020-11-09T06:13:05.973",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "Application"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669628",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669628",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

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

  "resourceFileRequest": {

    "Application": {

      "Guids":["3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46"]

    },

"FileName":"New1.txt",

    "Notes":"update3",

"Keywords":"update3"

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
{

    "ObjectIdentifier": {

        "ArtifactID": 1669628,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "New1.txt",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "update3",

    "Notes": "update3",

    "CreatedOn": "2020-11-06T14:14:24.603",

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

    "LastModifiedOn": "2020-11-09T06:17:33.393",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "Application"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669628",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669628",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

}
```

View JSON for a sample request

To modify properties of a resource file using contents key(Guid).

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

  "resourceFileRequest": {

    "Application": {

      "Guids":["3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46"]

    },

"FileName":"New1.txt",

    "Notes":"update4",

"Keywords":"update4"

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
{

    "ObjectIdentifier": {

        "ArtifactID": 1669628,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "New1.txt",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "update4",

    "Notes": "update4",

    "CreatedOn": "2020-11-06T14:14:24.603",

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

    "LastModifiedOn": "2020-11-09T06:18:41.683",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "Application"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669628",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669628",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

}
```

## Delete a resource file

To delete a resource file, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}
```

View JSON for a sample request

The body of this request should be empty.

View JSON for a sample response

The body of the response will also be empty. If the delete is successful it will just return a 200 status code.

## Download the contents of a resource file

To downloads the contents associated with a resource file, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/{resourceFileID}/contents/
```

View JSON for a sample request

The body of this request should be empty.

View JSON for a sample response

Depending from the file type the raw JSON response might not be human-readable.

## Upload the contents of a resource file

To upload the contents associated with a resource file, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/contents/
```

View JSON for a sample request

View JSON for a sample response Copy

```text
1
2
3
{

    "ContentsKey": "eed948ff-ef0b-4e7d-8ab5-c836e9918071"

}
```

## Create or update a resource file

To create or update a resource file, send a PATCH request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/
```

View JSON for a sample request Copy

```text
1
2
3
4
5
6
{"applicationIdentifier":

    {

        "Guids":["3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46"]

    },

    "fileName":"New.txt"

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
{

    "ObjectIdentifier": {

        "ArtifactID": 1669627,

        "Guids": []

    },

    "Application": {

        "Secured": false,

        "Value": {

            "Name": "Default",

            "ArtifactID": 950,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        }

    },

    "FileName": "New.txt",

    "AgentTypes": [],

    "EventHandlers": [],

    "MassOperations": [],

    "Services": [],

    "Keywords": "",

    "Notes": "",

    "CreatedOn": "2020-11-06T14:04:30.927",

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

    "LastModifiedOn": "2020-11-06T14:04:30.927",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "Application"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669627",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/workspaces/-1/resource-files/1669627",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

}
```

## Retrieve available applications

To retrieve a list of eligible applications, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/resource-files/eligible-applications
```

View JSON for a sample request

The body of this request should be empty.

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
{

    "HasSecuredItems": false,

    "ViewableItems": [

        {

            "ObjectIdentifier": {

                "Name": "Default",

                "ArtifactID": 950,

                "Guids": [

                    "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

                ]

            },

            "IsGlobalApplication": false,

            "Required": "Optional"

        },

        {

            "ObjectIdentifier": {

                "Name": "Imaging",

                "ArtifactID": 1015285,

                "Guids": [

                    "c9e4322e-6bd8-4a37-ae9e-c3c9be31776b"

                ]

            },

            "IsGlobalApplication": false,

            "Version": "12.1.0.0",

            "SchemaVersion": "11.2.199.24",

            "FileName": "Relativity.Conversion.rap",

            "Required": "Required"

        },

        {

            "ObjectIdentifier": {

                "Name": "Search Terms Report",

                "ArtifactID": 1015286,

                "Guids": [

                    "f807ac5a-6f0c-4ef3-9c7d-db2bae51a5f4"

                ]

            },

            "IsGlobalApplication": false,

            "Version": "13.3.1.0",

            "SchemaVersion": "12.0.9.13",

            "FileName": "SearchTermsReport.rap",

            "Required": "Required"

        },

        {

            "ObjectIdentifier": {

                "Name": "Analytics Core",

                "ArtifactID": 1015510,

                "Guids": [

                    "62284add-91f5-4f35-a582-bbcfa439ad8c"

                ]

            },

            "IsGlobalApplication": false,

            "Version": "3003.1.0.3",

            "SchemaVersion": "3000.4.0.9",

            "FileName": "Analytics.Core.rap",

            "Required": "Required"

        },

        {

            "ObjectIdentifier": {

                "Name": "OCR",

                "ArtifactID": 1015511,

                "Guids": [

                    "8354d537-689a-4dde-b057-5ef2fe4dba2b"

                ]

            },

            "IsGlobalApplication": false,

            "Version": "100.0.0.19",

            "SchemaVersion": "11.2.154.4",

            "FileName": "Relativity.OCR.rap",

            "Required": "RequiredIfPresent"

        },

...

    ]

}
```

On this page

- Resource File (REST)

- Guidelines for the Resource File service

- URLs

- Client code sample

- Create a resource file

- Read a resouce file

- Update a resource file

- Delete a resource file

- Download the contents of a resource file

- Upload the contents of a resource file

- Create or update a resource file

- Retrieve available applications


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
