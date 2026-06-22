---
title: "Layout Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/Layout_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:38+00:00
sha256: 11c3faeec9e173b7e286227d27743084b6ef58452df7b46997547feea148cb66
---

Layout Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Layout Manager (REST)

In Relativity, a layout is a web-based coding form that you can use to view and edit document and other fields. For general information, see Layouts on the Relativity Documentation site.

The Layout Manager service exposes CRUD endpoints that you can use to programmatically manipulate layouts in your Relativity environment. In addition to the CRUD endpoints, this API includes a helper endpoint used to retrieve a list of users with permissions necessary to own layouts.

Sample use cases for the Layout Manager service include:

- Developing an application that support specific operations, which users can perform on the layouts included in it.

- Programmatically updating properties of layouts in Relativity.

You can also use the Layout Manager service through .NET. For more information, see Layout Manager (.NET) .

## Guidelines for the Layout Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a layout:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts/{Layout Artifact ID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {Workspace ID} to the Artifact ID of the workspace that contains the layout.

- {Layout Artifact ID} to the Artifact ID of a specific layout.

## Client code sample

To use the Layout Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for creating a layout.

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
public async Task<LayoutResponse> CreateLayoutAsync()

{

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("http://localhost/");



        string inputJSON = "{ \"layoutRequest\": { \"ObjectType\": { \"Secured\": false, \"Value\": { \"Name\": \"TestObjectType\", \"ArtifactTypeID\": 10463412, \"ArtifactID\": 1035231, \"Guids\": [] } }, \"Order\": \"1\", \"OverwriteProtection\": true, \"AllowCopyFromPrevious\": false, \"RelativityApplications\": [], \"Keywords\": \"\", \"Notes\": \"\", \"Owner\": { \"Name\": \"Public\", \"ArtifactID\": 0, \"Guids\": [] }, \"Name\": \"Test Layout\" } }";

        string url = "/Relativity.Rest/API/relativity-data-visualization/V1/workspaces/-1/layouts";

        HttpResponseMessage response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        string content = await response.Content.ReadAsStringAsync();

        return JsonConvert.DeserializeObject<LayoutResponse>(content);

    }

}
```

## Create a layout

To create a single layout, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts
```

View field descriptions for a request

The body of the request must contain a layoutRequest field, which represents a request for creating a layout. It contains the following fields:

- ObjectType - contains information about the object type associated with the layout. It includes these fields:

- Secured - indicates whether the current user has permissions to view the setting in the Value field.

- Value - contains the following fields:

- Name - the name of the object type.

- ArtifactTypeID - the ID for the artifact type of the object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs for the object type.

- Order - the numerical value designating the position of the layout in the drop-down list displayed in the Relativity UI.

- Overwrite Protection - indicates whether the layout can be edited while another process is modifying it.

- AllowCopyFromPrevious - indicates whether the layout supports copying from a previous Document object. This field only applies to layouts associated with Document objects at the workspace level.

- RelativityApplications -an array of identifiers representing Relativity applications that contain the current layout.

- Keywords - optional keywords associated with the layout.

- Notes - optional words or phrase used to describe the layout.

- Owner - an object identifier for the user who owns the layout. It contains the following fields:

- Name - the name of the owner

- ArtifactID - the Artifact ID for the owner.

- Guids - an array of GUIDs for the owner.

- Name - the user-friendly name of the layout.

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

    "layoutRequest": {

        "ObjectType": {

            "Secured": false,

            "Value": {

                "Name": "TestObjectType",

                "ArtifactTypeID": 1036342,

                "ArtifactID": 1035231,

                "Guids": []

            }

        },

        "Order": "1",

        "OverwriteProtection": true,

        "AllowCopyFromPrevious": false,

        "RelativityApplications": [],

        "Keywords": "",

        "Notes": "",

        "Owner": {

            "Name": "Public",

            "ArtifactID": 0,

            "Guids": []

        },

        "Name": "TestLayout"

    }

}
```

View field descriptions for a response

This endpoint returns a LayoutResponse object that represents the newly created layout. It contains the following fields:

- ObjectType - contains information about the object type associated with the layout. It includes these fields:

- Secured - indicates whether the current user has permissions to view the setting in the Value field.

- Value - contains the following fields:

- Name - the name of the object type.

- ArtifactTypeID - the ID for the artifact type of the object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs for the object type.

- Order - the numerical value designating the position of the layout in the drop-down list displayed in the Relativity UI.

- Overwrite Protection - indicates whether the layout can be edited while another process is modifying it.

- AllowCopyFromPrevious - indicates whether the layout supports copying from a previous Document object. This field only applies to layouts associated with Document objects at the workspace level.

- RelativityApplications - list of identifiers representing Relativity applications that contain the current layout. It includes these fields:

- HasSecuredItems - indicates whether the list contains one or more items that aren't accessible to the current user.

- ViewableItems - an array of items (accessible to the current user) that describe the applications that contain the current layout.

- CreatedOn - the date and time when the layout was added to Relativity.

- CreatedBy - the name and unique identifier for the user who created the layout.

- LastModifiedBy - the name and unique identifier for the user who last updated the layout.

- LastModifiedOn - the date and time when the layout was last updated.

- Keywords - optional keywords associated with the layout.

- Notes - optional words or phrase used to describe the layout.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of fields not supported on the current instance of this layout.

- ReadOnly - an array of layout fields that can't be modified, such its name.

- Actions - an array of Action objects indicating operations that the user has permissions to perform on this layout. For example, the user may not have permissions to modify a layout that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the layout, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether the user has permissions to perform the operation on this layout.

- Reason - an explanation for the unavailability of an action.

- Owner - an object identifier for the user who owns the layout. It contains the following fields:

- Name - the name of the owner.

- ArtifactID - the Artifact ID for the owner.

- Guids - an array of GUIDs for the owner.

- Name - the user-friendly name of the layout.

- ArtifactID - the Artifact ID of the layout.

- Guids - any GUIDs used to identify the layout.

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
{

    "ObjectType": {

        "Secured": false,

        "Value": {

            "Name": "Document",

            "ArtifactTypeID": 10,

            "ArtifactID": 1035231,

            "Guids": []

        }

    },

    "Order": "1",

    "OverwriteProtection": true,

    "AllowCopyFromPrevious": false,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "CreatedOn": "2020-05-07T19:12:41.13",

    "CreatedBy": {

        "Name": "User2, Test",

        "ArtifactID": 777,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "User1, Test",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedOn": "2020-08-05T20:19:08.67",

    "Keywords": "",

    "Notes": "",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Object Type"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-data-visualization/{versionNumber}/workspace/1018025/layouts/1036363",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-data-visualization/{versionNumber}/workspace/1018025/layouts/1036363",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Owner": {

        "Name": "Public",

        "ArtifactID": 0,

        "Guids": []

    },

    "Name": "Document Metadata",

    "ArtifactID": 1036363,

    "Guids": []

}
```

## Read a layout

You can retrieve basic metadata for a layout or extended metadata, which also includes operations that a user has permissions to perform on the layout.

- Basic metadata for a layout - send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts/{Layout Artifact ID}
```

- Extended metadata for a layout - send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts/{Layout Artifact ID}/true/true
```

The response for a read operation contains the same fields as those for a create response. See the field descriptions for the response in Create a layout .

View the JSON response for an extended metadata request Copy

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
{

    "ObjectType": {

        "Secured": false,

        "Value": {

            "Name": "Document",

            "ArtifactTypeID": 10,

            "ArtifactID": 1035231,

            "Guids": []

        }

    },

    "Order": "1",

    "OverwriteProtection": true,

    "AllowCopyFromPrevious": false,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "CreatedOn": "2020-05-07T19:12:41.13",

    "CreatedBy": {

        "Name": "User1, Test",

        "ArtifactID": 777,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "User2, Test",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedOn": "2020-08-05T20:19:08.67",

    "Keywords": "",

    "Notes": "",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Object Type"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-data-visualization/V1/workspace/1018025/layouts/1036363",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-data-visualization/V1/workspace/1018025/layouts/1036363",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Owner": {

        "Name": "Public",

        "ArtifactID": 0,

        "Guids": []

    },

    "Name": "Document Metadata",

    "ArtifactID": 1036363,

    "Guids": []

}
```

## Update a layout

To update properties of a layout, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts/{Layout Artifact ID}
```

View descriptions of fields in a request

The body of the request must contain a layoutRequest field, which represents a request for updating a layout. It contains the following fields:

- ObjectType - contains information about the object type associated with the layout. It includes these fields:

- Secured - indicates whether the current user has permissions to view the setting in the Value field.

- Value - contains the following fields:

- Name - the name of the object type.

- ArtifactTypeID - the ID of the artifact type of the object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs for the object type.

- Order - the numerical value designating the position of the layout in the drop-down list displayed in the Relativity UI.

- Overwrite Protection - indicates whether the layout can be edited while another process is modifying it.

- AllowCopyFromPrevious - indicates whether the layout supports copying from a previous Document object. This field only applies to layouts associate with Document objects at the workspace level.

- RelativityApplications - list of identifiers representing Relativity applications that contain the current layout.

- Keywords - optional keywords associated with the layout.

- Notes - optional words or phrase used to describe the layout.

- Owner - an object identifier for the user who owns the layout. It contains the following fields:

- Name - the name of the owner

- ArtifactID - the Artifact ID for the owner.

- Guids - an array of GUIDs for the owner.

- Name - the user-friendly name of the layout.

- lastModifiedOn - an optional argument that restricts an update of the layout to the date when it was last modified.

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

    "layoutRequest": {

        "ObjectType": {

            "Secured": false,

            "Value": {

                "Name": "TestObjectType",

                "ArtifactTypeID": 1036342,

                "ArtifactID": 1035231,

                "Guids": []

            }

        },

        "Order": "1",

        "OverwriteProtection": true,

        "AllowCopyFromPrevious": false,

        "RelativityApplications": [],

        "Keywords": "",

        "Notes": "",

        "Owner": {

            "Name": "Public",

            "ArtifactID": 0,

            "Guids": []

        },

        "Name": "TestLayout"

    },

    "lastModifiedOn": "2020-05-07T19:30:41.13"

}
```

The response for an update operation contains the same fields as those for a create response. See the field descriptions for the response in Create a layout .

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
{

    "ObjectType": {

        "Secured": false,

        "Value": {

            "Name": "Document",

            "ArtifactTypeID": 10,

            "ArtifactID": 1035231,

            "Guids": []

        }

    },

    "Order": "1",

    "OverwriteProtection": true,

    "AllowCopyFromPrevious": false,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "CreatedOn": "2020-05-07T19:12:41.13",

    "CreatedBy": {

        "Name": "User2, Test",

        "ArtifactID": 777,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "User1, Test",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedOn": "2020-08-05T20:19:08.67",

    "Keywords": "",

    "Notes": "",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Object Type"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-data-visualization/V1/workspace/1018025/layouts/1036363",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-data-visualization/V1/workspace/1018025/layouts/1036363",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Owner": {

        "Name": "Public",

        "ArtifactID": 0,

        "Guids": []

    },

    "Name": "Document Metadata",

    "ArtifactID": 1036363,

    "Guids": []

}
```

## Delete a layout

To remove a layout from Relativity, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts/{Layout Artifact ID}
```

The body of the request is empty. When the layout is successfully deleted, the response returns the status code of 200.

## Retrieve users for layout ownership

To retrieve a list of users eligible to be layout owners, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{Workspace ID}/layouts/eligible-owners
```

The body for the JSON request is empty.

The response is an array of DisplayableObjectIdentifier objects that represent the users. It contains the following fields:

- Name - the user-friendly name of a user.

- ArtifactID - the Artifact ID of the user.

- Guids - an array of GUIDs used to identify the user.

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
[

    {

        "Name": "Public",

        "ArtifactID": 0,

        "Guids": []

    },

    {

        "Name": "Doe, John",

        "ArtifactID": 1046231,

        "Guids": []

    },

    {

        "Name": "Doe, Jane",

        "ArtifactID": 1057131,

        "Guids": []

    }

]
```

On this page

- Layout Manager (REST)

- Guidelines for the Layout Manager service

- URLs

- Client code sample

- Create a layout

- Read a layout

- Update a layout

- Delete a layout

- Retrieve users for layout ownership


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
