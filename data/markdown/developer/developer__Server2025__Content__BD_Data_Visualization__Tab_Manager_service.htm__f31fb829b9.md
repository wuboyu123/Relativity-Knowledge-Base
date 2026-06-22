---
title: "Tab Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/Tab_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:02+00:00
sha256: cb848f6ecd27808b9c953510e3cfe40cb46e42838b911dea2ddf736d477c1126
---

Tab Manager (REST)

# Tab Manager (REST)

The Tab Manager service exposes endpoints for programmatically managing tabs in the Relativity. It includes the following features:

- Supports create, read, update, and delete operations on tabs.

- Provides helper endpoints that simplify working with tabs. You can use these endpoints to retrieve information about the display order of tabs, parent tabs, and available object types that can be associated with tabs. Additionally, you can also retrieve workspace-level metadata for admin and system tabs.

As a sample use case, you might use the Tab Manager service to add specialized tab functionality to custom pages in a Relativity application developed for your organization.

You can also access the Tab Manager service through .NET. For more information, see Tab Manager (.NET) .

## Guidelines for the Tab Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a tab:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/{tabID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {WorkspaceID} to the Artifact ID of the workspace that contains the tab.

- {tabID} to the Artifact ID of a specific tab.

### JSON payloads for create and update operations

When you create or update a tab, any field not included in the JSON request is automatically set to null or to a default value. For example, if the JSON for a request doesn't include the IsVisible field, then this field is automatically set to the default value of false.

Use the ReadAsync endpoint to retrieve all the properties and values set on a Tab object, and then only modify specific property values when updating the tab. This practice maintains the integrity of the data and avoids any inconsistencies. For more information, see Retrieve tab metadata and Update a tab .

View sample JSON for Tab object Copy

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
{

    "tab": {

        "Name": "Aliases1234",

        "Order": 100,

        "LinkType": 3,

        "ObjectType": {

            "ArtifactTypeID": 10

        },

        "IsVisible": true,

        "Parent": {

            "Secured": false,

            "Value": {

                "ArtifactID": 1003663

            }

        }

    }

}
```

### IconIdentifier field

Some requests contain the IconIdentifier field, which represents a string identifier for the icon displayed when the Tab appears in the sidebar.

View table of IconIdentifier values

The following table lists the available IconIdentifier values:

Icon

String Identifier

Name

sidebar-access

Access

sidebar-analytics

Analytics

sidebar-bar-chart

Bar chart

sidebar-case

Case

sidebar-case-dynamics

Case dynamics

sidebar-configure

Configure

sidebar-data-transfer

Data transfer

sidebar-documents

Documents

sidebar-download

Download

sidebar-export

Export

sidebar-folder

Folder

sidebar-infrastructure

Infrastructure

sidebar-monitor

Monitor

sidebar-page

Page

sidebar-pie-chart

Pie chart

sidebar-processing

Processing

sidebar-production

Production

sidebar-resources

Resources

sidebar-review

Review

sidebar-default-tab

Tag

sidebar-upload

Upload

sidebar-workspaces

Workspaces

## Client code sample

You send a request to the Tab Manager service by making a call to an endpoint with the required HTTP method. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces
```

You can use the following .NET code as a sample client for creating a tab at the admin-level. This code illustrates how to perform the following general tasks:

- Instantiate an HttpClient object for sending requests to the Tab Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Initialize variables with the values for the name and order of the tab that you want to create. The order indicates the position of the tab in relation to other tabs displayed in the Relativity UI.

- Set the JSON input required for the operation.

- Set the url variable to the URL for creating the tab. For more information, see Create a tab .

This code sample illustrates how to create the tab at the admin-level, so the workspace ID is set to -1 in the URL.

- Use the PostAsync() method to send a post request.

- Return the results of the request and deserialize it.

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
public async Task<int?> CreateTabExample()

{

    int? result = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");

        var tabName = "SomeNewTab";

        var order = 100;

        string inputJSON = $"{{\"tab\":{{ \"Name\": \"{tabName}\", \"Order\":  \"{order}\", \"LinkType\": 3, \"IsVisible\": true, \"Parent\": {{\"Value\": {{\"ArtifactID\": 1003663 }} }} }} }}";

        var url = "/Relativity.REST/API/relativity-data-visualization/v1/workspaces/-1/tabs/";

        var response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<int>(content);

    }

    return result;

}
```

## Create a tab

To create a new tab, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs
```

View field descriptions for a request

The body of the request contains the following fields:

- tabRequest - represents a TabRequest object. This object contains optional fields that aren't required to create a tab, such as RelativityApplications, ObjectType, and IsDefault fields. Any fields on this object not included in the JSON request are automatically set to null or a default value. For more information, see JSON payloads for create and update operations .

- Name - the user-friendly name of the tab.

- Order - the numerical value designating the position of the tab in the Relativity UI. For information about the order of tabs in a workspace, see Retrieve tab orders .

- LinkType - indicates type of link associated with the tab. For example, a parent type indicates that the tab may have sub-tabs.

The following table summarizes the values used to represent link types:

Name Value Description

Unknown 0 Indicates an unknown link type.

Object 1 Indicates that the tab links to a Relativity object.

Link 2 Indicates that the tab links to a URL.

Parent 3 Indicates that the tab may have sub-tabs.

Available link types are included on the TabLinkTypeEnum enumeration.

- IsVisible - a Boolean value indicating whether the tab is displayed in a workspace.

- Parent - contains the following fields for the parent tab:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - an object containing Artifact ID or the GUIDs used to identify the parent tab:

- ArtifactID - the Artifact ID of the parent tab.

- Guids - an array of GUIDs for the parent tab.

- RelativityApplications - a list of items that describe the applications that contain the current tab. Each item contains the following fields:

- ArtifactID - the Artifact ID of the application.

- Guids - an array of GUIDs for the application.

- ObjectType - contains information about the object type that you want associated with the tab. These fields are only required for creating a tab with an object link type:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - an object containing object type identifiers:

- ArtifactTypeID - the ID of the Artifact Type of the object.

- ArtifactID - the Artifact ID of the object type.

- Guids - the GUIDs for the object type.

- Name - the name of the object type.

You can only create one tab per object type. After you create a tab for an object type, you can't reuse the Artifact ID to create another tab. Making a call with the Artifact ID returns an Invalid ObjectType error.

- Link - a link to a URL. This field is only required for a creating a tab with an external type link.

- IsDefault - a Boolean value indicating whether the tab should be the first tab that you access when navigating to the parent tab.

- IsShownInSidebar - a Boolean value indicating whether the tab should be displayed in the sidebar.

- IconIdentifier - the string identifier for the icon displayed when the tab is listed in the sidebar. For valid values, see IconIdentifier field .

View JSON for creating a tab with an object type link Copy

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

  "tabRequest": {

    "Name": "Tab - Object",

    "Order": 100,

    "LinkType": 1,

    "IsVisible": true,

    "Parent": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1436126

      }

    },

    "ObjectType": {

      "Secured": false,

      "Value": {

          "ArtifactTypeID": 1000045

      }

    }

  }

}
```

View JSON for creating a tab with an external type link Copy

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

  "tabRequest": {

    "Name": "Tab - Link",

    "Order": 100,

    "LinkType": 2,

    "IsVisible": true,

    "Parent": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1436126

      }

    },

    "Link": "%ApplicationPath%/Admin/LinkTabExample/Example.aspx?%AppID%"

  }

}
```

View JSON for creating a tab with a parent type link Copy

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
{

   "tabRequest":{

      "Name":"Aliases1234",

      "Order": 100,

      "LinkType":3,

      "IsVisible":true,

      "Parent":{

         "Secured": false,

         "Value": {

            "ArtifactID": 1003663

         }

      }

   }

}
```

View field descriptions for a create response

The response contains a TabResponse object with the following fields:

- ObjectIdentifier - an object containing identifying information for the tab as follows:

- Name - the user-friendly name of the tab.

- ArtifactID - the Artifact ID of the tab.

- Guids - an array of GUIDs used to identify the tab.

- Order - the numerical value designating the position of the tab in the Relativity UI.

- Link - a link to a URL. This field is only required for a tab with an external type link.

- IsDefault - a Boolean value indicating whether this tab is the first one displayed to the users when they access a workspace. For more information, see Tabs on the Relativity Documentation site.

- IsVisible - a Boolean value indicating whether the tab is displayed in a workspace.

- IsShownInSidebar - a Boolean value indicating whether the tab should be displayed in the sidebar.

- RelativityApplications - contains the following fields:

- HasSecuredItems - a Boolean value indicating whether the list contains one or more items that aren't accessible to the current user.

- ViewableItems - a list of items (accessible to the current user) that describe the applications that contain the current tab. Each item contains the following fields:

- ArtifactID - the Artifact ID of the application.

- Name - the name of the application.

- Guids - GUIDs used to identify the application.

- LinkType - indicates type of link associated with the tab. For more information on link types, see Create a tab .

- CreatedOn - the date and time when the tab was added to Relativity.

- CreatedBy - contains the following fields that represent the user who created the Tab:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - contains the following fields:

- ArtifactID - the Artifact ID of the user.

- Name - the name of the user.

- Guids - GUIDs used to identify the user.

- LastModifiedBy - contains the following fields that represent the user who last modified the Tab:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - contains the following fields:

- ArtifactID - the Artifact ID of the user.

- Name - the name of the user.

- Guids - GUIDs used to identify the user.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of fields not supported on the current instance of this tab.

- ReadOnly - an array of tab fields that can't be modified, such its name or link.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this tab. For example, you may not have permissions to modify a tab that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - the name of an operation available through REST for the tab, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this tab.

- Reason - an explanation for the unavailability of an action.

- ObjectType - contains information about the object type that you want associated with the tab. These fields are only required for a tab with an object link type:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - an object containing identifying information for the object type:

- ArtifactTypeID - the ID of the Artifact Type of the object.

-

ArtifactID - the Artifact ID of the object type.

-

Guids - an array of GUIDs used to identify the object type.

-

Name - the user-friendly name of the object type.

- Parent - contains the following fields for the parent tab:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the parent tab.

- ArtifactID - the Artifact ID of the parent tab.

- Guids - an array of GUIDs used to identify the parent tab.

- IconIdentifier - the string identifier for the icon displayed when the tab is listed in the sidebar. For a list of valid values, see IconIdentifier field .

- LastModifiedOn - the date and time when the tab was most recently modified.

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
{

    "ObjectIdentifier": {

        "Name": "Workspaces",

        "ArtifactID": 1015520,

        "Guids": []

    },

    "Order": -1000,

    "IsDefault": true,

    "IsVisible": true,

    "IsShownInSidebar": true,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "LinkType": "Object",

    "CreatedOn": "2014-09-29T15:32:47.187",

    "ObjectType": {

        "Secured": false,

        "Value": {

            "ArtifactTypeID": 8,

            "Name": "Workspace",

            "ArtifactID": 1016187,

            "Guids": []

        }

    },

    "Parent": {

        "Secured": false,

        "Value": {

            "Name": "System",

            "ArtifactID": 62,

            "Guids": [

                "bd10a60d-b8ec-4928-84ee-6fc4f30d9612"

            ]

        }

    },

    "IconIdentifier": "sidebar-workspaces",

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "User1",

            "ArtifactID": 1000987,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "User2",

            "ArtifactID": 1000777,

            "Guids": []

        }

    },

    "Meta": {

        "Unsupported": [

            "RelativityApplications"

        ],

        "ReadOnly": []

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-data-visualization/v1/workspaces/-1/tabs/1015520",

            "Verb": "DELETE",

            "IsAvailable": false,

            "Reason": [

                "This tab cannot be deleted because it is a system tab."

            ]

        },

        {

            "Name": "Update",

            "Href": "relativity-data-visualization/v1/workspaces/-1/tabs/1015520",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "LastModifiedOn": "2020-07-07T19:33:02.72"

}
```

## Retrieve tab metadata

You can retrieve basic or extended metadata for a tab. Extended metadata includes operations that you have permissions to perform on the tab, such as delete or update.

- Retrieve basic metadata for a tab - send a GET request with a URL in the following format: Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/{tabID}
```

- Retrieve extended metadata for a tab -send a GET request with a URL in the following format: Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/{tabID}?includeMetadata={includeMetadata}&includeActions={includeActions}
```

Set both the {includeMetadata} and {includeActions} path parameters to true.

The body of the request is empty.

The response for a read operation contains the same fields as a response for a create operation. See the field descriptions in View field descriptions for a create response .

View the JSON response with extended metadata Copy

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
{

    "ObjectIdentifier": {

        "Name": "Workspaces",

        "ArtifactID": 1015520,

        "Guids": []

    },

    "Order": -1000,

    "IsDefault": true,

    "IsVisible": true,

    "IsShownInSidebar": true,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "LinkType": "Object",

    "CreatedOn": "2014-09-29T15:32:47.187",

    "ObjectType": {

        "Secured": false,

        "Value": {

            "ArtifactTypeID": 8,

            "Name": "Workspace",

            "ArtifactID": 1016187,

            "Guids": []

        }

    },

    "Parent": {

        "Secured": false,

        "Value": {

            "Name": "System",

            "ArtifactID": 62,

            "Guids": [

                "bd10a60d-b8ec-4928-84ee-6fc4f30d9612"

            ]

        }

    },

    "IconIdentifier": "sidebar-workspaces",

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "User1",

            "ArtifactID": 1000987,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "User2",

            "ArtifactID": 1000777,

            "Guids": []

        }

    },

    "Meta": {

        "Unsupported": [

            "RelativityApplications"

        ],

        "ReadOnly": []

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-data-visualization/v1/workspaces/-1/tabs/1015520",

            "Verb": "DELETE",

            "IsAvailable": false,

            "Reason": [

                "This tab cannot be deleted because it is a system tab."

            ]

        },

        {

            "Name": "Update",

            "Href": "relativity-data-visualization/v1/workspaces/-1/tabs/1015520",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "LastModifiedOn": "2020-07-07T19:33:02.72"

}
```

## Update a tab

You can modify the properties of a tab, such as its name, order, and others. Additionally, you can restrict the update of a tab to the date that it was last modified by adding the LastModifiedOn field to the request.

You need to unlock an application before making updates to the tabs that it contains. See Add components to an application .

Send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/{tabID}
```

View the descriptions of fields in the request

The body of the request depends on the type of link used for the tab. The sample JSON requests contain the various fields from the following list:

- tabRequest - represents a TabRequest object. This object has some fields that aren't required to update a tab, such as RelativityApplications field, ObjectType, and IsDefault fields. Any field on this object not included in the JSON request are automatically set to null or a default value. For more information, see JSON payloads for create and update operations .

- Name - the user-friendly name of the tab.

- Order - the numerical value designating the position of the tab in the Relativity UI.

- IsDefault - a Boolean value indicating whether the tab should be the first tab that you access when navigating to the parent tab.

- IsVisible - a Boolean value indicating whether the tab is displayed in a workspace.

- IsShownInSidebar - a Boolean value indicating whether the tab should be displayed in the sidebar.

- LinkType - indicates type of link associated with the tab. For more information on link types, see Create a tab .

- Link - a link to a URL. This field is only required for a creating a tab with an external type link.

-

Parent - contains the following fields for the parent tab:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- ArtifactID - the Artifact ID of the parent tab.

- Guids - the GUIDs used to identify the parent tab.

- ObjectType - contains information about the object type that you want associated with the tab. These fields are only required for a tab with an object link type:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - an object containing identifying information for the object type:

- ArtifactTypeID - the ID of the Artifact Type of the object.

-

ArtifactID - the Artifact ID of the object type.

-

Guids - an array of GUIDs used to identify the object type.

-

Name - the user-friendly name of the object type.

You can only create one tab per object type. After you create a tab for an object type, you can't reuse the Artifact ID to create another tab. Making a call with the Artifact ID returns an Invalid ObjectType error.

- IconIdentifier - the string identifier for the icon displayed when the tab is listed in the sidebar. For a list of valid values, see IconIdentifier field .

View JSON for updating a tab with an object type link Copy

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

  "tabRequest": {

    "Name": "Updated Tab - Object",

    "Order": 100,

    "LinkType": 1,

    "IsVisible": true,

    "Parent": {

      "Secured": false,

      "Value": {

        "ArtifactID": 1436126

      }

    },

    "ObjectType": {

      "Secured": false,

      "Value": {

          "ArtifactTypeID": 1000045

      }

    }

  }

}
```

View JSON for updating a tab with an external type link Copy

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

  "tabRequest": {

    "Name": " Updated Tab - Link",

    "Order": 3,

    "LinkType": 2,

    "Link": "%ApplicationPath%/Admin/LinkTabExample/Example.aspx?%AppID%",

    "IsVisible": true,

    "Parent": {

      "Secured": false,

      "Value": {

        "ArtifactID":1003663

      }

    }

  }

}
```

View JSON for updating a tab with a parent type link Copy

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
{

  "tabRequest": {

    "Name": "Alias",

    "Order": 20,

    "IsDefault": false,

    "IsVisible": true,

    "IsShownInSidebar": true,

    "LinkType": "Parent",

    "Parent": {

      "Secured": false,

      "Value": {

        "ArtifactID": 62

      }

    },

    "IconIdentifier": "sidebar-access"

  }

}
```

The response for an update operation contains the same fields as a response for a create operation. See the field descriptions in View field descriptions for a create response .

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
{

    "ObjectIdentifier": {

        "Name": "Aliases12345",

        "ArtifactID": 1018257,

        "Guids": []

    },

    "Order": 100,

    "IsDefault": false,

    "IsVisible": true,

    "IsShownInSidebar": false,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "LinkType": "Parent",

    "CreatedOn": "2020-10-27T12:04:35.087",

    "ObjectType": {

        "Secured": false

    },

    "Parent": {

        "Secured": false,

        "Value": {

            "Name": "User and Group Management",

            "ArtifactID": 1015494,

            "Guids": []

        }

    },

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "User1",

            "ArtifactID": 1000987,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "User1",

            "ArtifactID": 1000987,

            "Guids": []

        }

    },

    "LastModifiedOn": "2020-10-27T12:06:47.947"

}
```

## Delete a tab

You can remove a tab from Relativity if you have the appropriate permissions. For more information, see Security and permissions in the Relativity Documentation site.

Before you delete a tab, consider checking for other dependent tabs. See Object Manager (REST) .

Send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspace/{workspaceID}/tabs/{tabID}
```

The body of the request is empty.

When the tab is successfully deleted, the response returns the status code of 200.

## Retrieve object types for a tab

You can retrieving a list of all object types in a workspace available for creating or updating a tab. A tab must be associated it with an object.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/eligible-object-types
```

The body of the request is empty.

View the field descriptions for a response

The response contains the following fields:

- ArtifactTypeID - the Artifact Type ID of the object type.

- Name - the user-friendly name of the object type.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

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
[

    {

        "ArtifactTypeID": 1000008,

        "Name": "Scope",

        "ArtifactID": 1016340,

        "Guids": []

    },

    {

        "ArtifactTypeID": 1000012,

        "Name": "Sanitizer",

        "ArtifactID": 1016493,

        "Guids": []

    }

]
```

## Retrieve eligible parent tabs

You can retrieve a list of parent tabs, which you can associate with a tab when you add or edit it. In the Relativity UI, a parent tab displays a drop-down list containing child tabs.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/eligible-parents
```

The body of the request is empty.

View the field descriptions for a response

The response contains the following fields:

- ObjectIdentifier - an object containing identifying information for the parent tab as follows:

- ArtifactID - the Artifact ID of the parent tab.

- Name - the user-friendly name of the parent tab.

- Guids - an array of GUIDs used to identify the parent tab.

-

SupportedChildTypeLinkTypes - an array of link types that a child tab can have.

Name Value Description

Object 1 Indicates that the tab links to a Relativity object.

Link 2 Indicates that the tab links to a URL.

Parent 3 Indicates that the tab may have sub-tabs.

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
[

    {

        "ObjectIdentifier": {

            "Name": "Other Tabs",

            "ArtifactID": 1018230,

            "Guids": []

        },

        "SupportedChildTypeLinkTypes": [

            "Object",

            "Link",

            "Parent"

        ]

    }

]
```

## Retrieve workspace-level metadata for admin and system tabs

You can retrieve workspace-level metadata about admin and system tabs. This metadata includes fields that can't be updated and those that aren't supported for a specific tab. In general, the following guidelines apply to this metadata:

- Admin tabs - Because these tabs are supported only for workspaces, the RelativityApplications field is always returned as an unsupported field by the meta endpoint.

- System tabs - Because these tabs are part of the core Relativity application, most of their fields can't be updated, and are returned by the meta endpoint as read-only fields, such the Name, Link, and RelativityApplications fields. For example, the fields on the Errors tab are read-only.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/meta
```

Set {workspaceID} to -1 to indicate the admin-level context for system and admin tabs.

The body of the request is empty.

The response contains the following fields:

- Unsupported - an array of fields not supported on the current instance of this tab.

- ReadOnly - an array of tab fields that can't be modified, such its name or link.

Copy

```text
1
2
3
4
5
6
{

    "Unsupported": [

        "RelativityApplications"

    ],

    "ReadOnly": []

}
```

## Retrieve tab orders

You can retrieve current order of the tabs in a workspace. The order assigned to a tab determines its position in the Relativity UI. Tabs with a lower order number are displayed on the left, while those with higher order numbers are displayed on the right. For more information, see Tabs on the Relativity Documentation site.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/view-order-list
```

The body of the request is empty.

View the field descriptions for a response

The response contains the following fields:

- ObjectIdentifier - an object containing identifying information for the tab as follows:

- ArtifactID - the Artifact ID of the tab.

- Name - the user-friendly name of the tab.

- Guids - an array of GUIDs used to identify the tab.

- Parent - contains the following fields for the parent tab:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- ArtifactID - the Artifact ID of the parent tab.

- Guids - the GUIDs used to identify the parent tab.

- Order - the numerical value designating the position of the tab in the Relativity UI.

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
[

    {

        "ObjectIdentifier": {

            "Name": "Workspaces",

            "ArtifactID": 1015520,

            "Guids": []

        },

        "Parent": {

            "Secured": false,

            "Value": {

                "ArtifactID": 62,

                "Guids": []

            }

        },

        "Order": -1000

    },

    {

        "ObjectIdentifier": {

            "Name": "User Status",

            "ArtifactID": 1014996,

            "Guids": []

        },

        "Parent": {

            "Secured": false,

            "Value": {

                "ArtifactID": 62,

                "Guids": []

            }

        },

        "Order": -10

    }]
```

## Retrieve all tabs for navigation

You can retrieve information about each tab that the calling user can navigate to in a specific workspace. This endpoint returns a URL for navigating to each tab and tab metadata.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/tabs/navigation
```

The body of the request is empty.

View the field descriptions for a response

- ObjectIdentifier - an object containing identifying information for the tab as follows:

- Name - the user-friendly name of the tab.

- ArtifactID - the Artifact ID of the tab.

- Guids - an array of GUIDs used to identify the tab.

- ObjectType - contains information about the object type that you want associated with the tab. These fields are only required for a tab with an object link type:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - an object containing identifying information for the object type:

- ArtifactTypeID - the ID of the Artifact Type of the object.

- Name - the user-friendly name of the object type.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

- ObjectTypeIdentifier - contains the following fields for the object type associated with the tab. If an exception occurs when populating this value, the Tab is returned but this property is omitted. See the following fields:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the object type.

- ArtifactTypeID - the ID of the Artifact Type of the object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

- LinkType - indicates type of link associated with the tab. For more information on link types, see Create a tab .

- Order - the numerical value designating the position of the tab in the Relativity UI.

- IsDefault - a Boolean value indicating whether this tab is the first one displayed to the users when they access a workspace. For more information, see Tabs on the Relativity Documentation site.

- IsVisible - a Boolean value indicating whether the tab is displayed in a workspace.

- IsShownInSidebar - a Boolean value indicating whether the tab should be displayed in the sidebar.

- Url - the relative path URL for navigating to the tab. The URL begins with /Relativity . If an exception occurs when populating this value, the Tab is returned but this property is omitted.

- IconIdentifier - the string identifier for the icon displayed when the tab is listed in the sidebar. For a list of valid values, see IconIdentifier field .

- Parent - contains the following fields for the parent tab:

- Secured - a Boolean value indicating whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- ArtifactID - the Artifact ID of the parent tab.

- Guids - the GUIDs used to identify the parent tab.

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
[

    {

        "ObjectIdentifier": {

            "Name": "Workspaces",

            "ArtifactID": 1015520,

            "Guids": []

        },

        "ObjectTypeIdentifier": {

            "Secured": false,

            "Value": {

                "ArtifactTypeID": 8,

                "Name": "Workspace",

                "ArtifactID": 1016187,

                "Guids": []

            }

        },

        "LinkType": "Object",

        "Order": -1000,

        "IsDefault": true,

        "IsVisible": true,

        "IsShownInSidebar": true,

        "Url": "/Relativity/RelativityInternal.aspx?AppID=-1&ArtifactTypeID=8&ArtifactID=62&Mode=ListPage",

        "IconIdentifier": "sidebar-workspaces"

    },

    {

        "ObjectIdentifier": {

            "Name": "User Status",

            "ArtifactID": 1014996,

            "Guids": []

        },

        "LinkType": "Link",

        "Order": -10,

        "IsDefault": false,

        "IsVisible": true,

        "IsShownInSidebar": true,

        "Url": "/Relativity/External.aspx?AppID=-1&ArtifactID=-1&DirectTo=%25ApplicationPath%25%2fCustomPages%2f2ff16b11-a4ca-4f02-8bbb-1f07f23fe713%2fstaticObjects.html%23%2fstaticObjects%2fuserstatus",

        "IconIdentifier": "sidebar-access"

    }

]
```
