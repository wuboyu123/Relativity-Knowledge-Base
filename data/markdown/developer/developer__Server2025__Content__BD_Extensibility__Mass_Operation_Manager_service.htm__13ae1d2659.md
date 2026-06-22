---
title: "Mass Operation Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Mass_Operation_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:22:49+00:00
sha256: b1a8d74465f50c060413dc9196b1d370d684f6182c8f44f5a2a55fc19baa9fb3
---

Mass Operation Manager (REST)

# Mass Operation Manager (REST)

You can add mass operations to object types to further customize their behavior. When a user interacts with a mass operation, you can display a custom page or execute an event handler with specialized functionality. For general information about mass operations, see Adding a custom mass operation .

The Mass Operation Manager service includes endpoints for creating, reading, updating, and deleting mass operations. It also includes helper endpoints for retrieving information about object types that be associated with a mass operation, and available event handlers and layouts for use with mass operations.

You can also work with this service through .NET. For more information, see Mass Operation Manager (.NET) .

## Postman sample files

You can use the Postman sample files to become familiar with making calls to endpoints on the services. To download the sample files, click {versionNumber}MassOperationsPostmanFiles.zip .

View postman steps.

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Mass Operations Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations
```

View client code sample.

The following code sample demonstrates how to make REST calls against the Mass Operation service. In this example we create a custom page mass operation.

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
using (HttpClient client = new HttpClient())

{

    client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword!")));

    client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

    client.BaseAddress = new Uri("https://localhost/");

    int workspaceID = 1022092;

    string url = $"/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/custom-page-mass-operations";

    string inputJSON = @"{""MassOperationRequest"": {""Name"": ""My Mass Op"",""ObjectType"": { ""Name"": ""My RDO"" },""Url"": ""www.custompagemassop.net"",""PopupHeight"": 500,""PopupWidth"": 500}}";

    using (HttpResponseMessage response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json")))

    {

        response.EnsureSuccessStatusCode();

    }

}
```

## Fundamentals for Mass Operation Manager

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

Review the following guidelines for working with this service:

- Make sure that you set the appropriate field values for the type of mass operation that you want to create. See Create an object type and Update an object type .

- Use the helper endpoints to retrieve object types , event handlers , and layouts available for associating with mass operation.

Mass operations aren't available in the admin-level context, so you must specify a workspace ID.

## Create a mass operation

You can a create a mass operation that displays a custom page or that executes a custom event handler when a user interacts with it. For general information about mass operations, see Adding a custom mass operation .

Click the following drop-down links to view URLs and sample requests for mass operations that use a custom page or an event handler. For the URLs in these examples, set the {WorkspaceID} variable to the Artifact ID of a workspace.

View a JSON request for a custom page mass operation

To create a mass operations that displays a custom page for a user, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/custom-page-mass-operations
```

The body of the request must contain the following fields unless specifically identified as optional:

- MassOperationRequest - represents a request to create a mass operation. It contains the following fields:

- Name - the user-friendly name of the mass operation.

- ObjectType - contains information about the object type to associate with this mass operation. Only the Artifact ID of the object type is required.

- Url - the URL for the custom page that you want displayed as a pop-up window for the mass operation.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The mass operation is linked to the applications in this array. If the array is empty, then the mass operation isn't linked to any application.

- PopupHeight - the height of the pop-up window displayed for this mass operation in pixels. This value must be greater than 0.

- PopupWidth - the width of the pop-up window displayed for this mass operation in pixels. This value must be greater than 0.

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
{

    "MassOperationRequest": {

        "Name": "My Mass Op",

        "ObjectType": {

            "Name": "My RDO"

        },

        "Url": "www.custompagemassop.net",

        "RelativityApplications": []

        "PopupHeight": 500,

        "PopupWidth": 500

    }

}
```

View a JSON request for an event handler mass operation

To create a mass operation that executes an event handler, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/event-handler-mass-operations
```

The body of the request must contain the following fields unless specifically identified as optional:

- MassOperationRequest - represents a request to create a mass operation. It contains the following fields:

- Name - the user-friendly name of the mass operation.

- ObjectType - contains information about the object type to associate with this mass operation. Only the Artifact ID of the object type is required.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The mass operation is linked to the applications in this array. If the array is empty, then the mass operation isn't linked to any application.

- EventHandlerID - identifier of event handler to invoke for this mass operation.

- Layout - represents identification information for a layout. It contains the following field:

- Value - contains the Artifact ID and GUIDs used to identify a specific layout for the mass operation. The array containing GUIDs can be empty.

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
{

    "MassOperationRequest": {

        "Name": "Mass Op Name",

        "ObjectType": {

            "Name": "My RDO"

        },

        "RelativityApplications": [],

        "EventHandlerID": 8675309,

        "Layout": {

            "Value": {

                "ArtifactID": 3456789,

            }

        }

    }

}
```

When a custom page or event handler mass operation is successfully created, the response contains the Artifact ID of the mass operation, such as 1042616. It also returns a status code of 200.

## Read a mass operation

You can retrieve basic information about a mass operation or extended information, which also includes operations that you have permissions to perform on the mass operation.

- Retrieve basic metadata for a mass operation - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/{massOperationID}
```

- Retrieve extended metadata for a mass operation - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/{massOperationID}/true/true
```

For both requests, set the {WorkspaceID} variable to the Artifact ID of a workspace. Set the {massOperationId} variable to the Artifact ID of the mass operation that you want to read, and leave the body of the request empty.

A successful request will return information about the specified mass operation.

View a JSON response for a custom page mass operation Copy

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

    "Type": "CustomPageMassOperation",

    "Name": "My custom page mass operation",

    "ObjectType": {

        "ArtifactTypeID": 25,

        "Name": "My RDO",

        "ArtifactID": 1104607,

        "Guids": []

    },

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "Url": "www.mycustompage.net",

    "PopupHeight": 500,

    "PopupWidth": 500,

    "EventHandlerID": 0,

    "ArtifactID": 1104616,

    "Guids": []

}
```

## Update a mass operation

You can update a mass operation by sending a PUT request to the endpoint for a custom page or event handler mass operation.

Click the following drop-down links to view URLs and sample requests for custom page and event handler mass operations.

For the URLs in these examples, set the {WorkspaceID} variable to the Artifact ID of a workspace. Set the {massOperationId} variable to the Artifact ID of the mass operation.

View a JSON request for updating a custom page mass operation

To update a custom page mass operation, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/custom-page-mass-operations/{massOperationID}
```

The body of the request must contain the following fields unless specifically identified as optional:

- MassOperationRequest - represents a request to update a mass operation. It can contain the following fields:

- Name - the user-friendly name of the mass operation.

- Url - the URL for the custom page that you want displayed as a pop-up window for the mass operation.

- PopupHeight - the height of the pop-up window displayed for this mass operation in pixels. This value must be greater than 0.

- PopupWidth - the width of the pop-up window displayed for this mass operation in pixels. This value must be greater than 0.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The mass operation is linked to the applications in this array. If the array is empty, then the mass operation isn't linked to any application.

- LastModifiedOn - the date and time when the object rule was most recently modified. This field is only required if you want to restrict the update of a mass operation to the date that it was last modified. The value must match the LastModifiedOn date for the mass operation stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

    "MassOperationRequest": {

        "Name": "My custom page mass operation",

        "ObjectType": {

            "Name": "My RDO"

        },

        "Url": "www.mycustompage.net",

        "PopupHeight": 500,

        "PopupWidth": 500

    }

}
```

View a JSON request for updating an event handler mass operation

To update an event handler mass operation, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/event-handler-mass-operations/{massOperationID}
```

The body of the request must contain the following fields unless specifically identified as optional:

- MassOperationRequest - represents a request to update a mass operation. It contains the following fields:

- Name - the user- friendly name of the mass operation.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The mass operation is linked to the applications in this array. If the array is empty, then the mass operation isn't linked to any application.

- EventHandlerID - identifier of event handler to invoke for this mass operation.

- Layout - represents identification information for a layout. It contains the following field:

- Value - contains the Artifact ID and GUIDs used to identify a specific layout for the mass operation.

- LastModifiedOn - the date and time when the object rule was most recently modified. This field is only required if you want to restrict the update of a mass operation to the date that it was last modified. The value must match the LastModifiedOn date for the mass operation stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

    "MassOperationRequest": {

        "Name": "Mass Op Name",

        "ObjectType": {

            "Name": "My RDO"

        },

        "RelativityApplications": [],

        "EventHandlerID": 8675309,

        "Layout": {

            "Value": {

                "ArtifactID": 4444445,

            }

        }

    }

}
```

When a mass operation is successfully updated, the response returns a status code of 200.

## Delete a mass operation

To remove a mass operation, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/{massOperationID}
```

Set the {WorkspaceID} variable to the Artifact ID of a workspace. Set the {massOperationId} variable to the Artifact ID of the mass operation. The body of the request is empty. When the mass operation is successfully deleted, the response is a status code of 200.

## Retrieve available object types for a mass operation

You can customize your object types with additional functionality by creating mass operations for them.

To retrieve a list of object types available in a workspace, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/available-object-types
```

Set the {WorkspaceID} variable to the Artifact ID of a workspace.

The body of the request is empty.

View a JSON response for available object types Copy

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
[

    {

        "ArtifactTypeID": 10,

        "Name": "Document",

        "ArtifactID": 1035231,

        "Guids": []

    },

    {

        "ArtifactTypeID": 1000004,

        "Name": "Transform Set",

        "ArtifactID": 1035285,

        "Guids": []

    },

    ...

    {

        "ArtifactTypeID": 1000084,

        "Name": "My RDO",

        "ArtifactID": 1104607,

        "Guids": []

    }

]
```

## Retrieve available event handlers for a mass operation

You can add an event handler for a mass operation to an object type. This event handler executes when the user executes the mass operation through the Relativity UI.

To retrieve a list of available event handlers, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/available-event-handlers
```

Set the {WorkspaceID} variable to the Artifact ID of a workspace.

The body of the request is empty.

View a JSON response for available event handlers Copy

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
[

    {

        "Application": {

            "Secured": false,

            "Value": {

                "Name": "Tab Sync",

                "ArtifactID": 0,

                "Guids": [

                    "2aa5c8bd-f7e7-4e5a-a0db-f085a2b34278"

                ]

            }

        },

        "EventHandlerID": 7137,

        "AssemblyName": "TabSync.MassOperations.dll",

        "ClassName": "TabSync.MassOperations.TabSyncMassOperationHandler",

        "CompanyName": "Relativity ODA LLC",

        "Description": "Executes a mass tab sync."

    },

    {

        "Application": {

            "Secured": false,

            "Value": {

                "Name": "MyMassOperationApplication",

                "ArtifactID": 0,

                "Guids": [

                    "28b730b2-bcb5-4f66-9d3c-707b650494ce"

                ]

            }

        },

        "EventHandlerID": 8137,

        "AssemblyName": "MassOperationHandler.dll",

        "ClassName": "MassOperationHandler.MassiveOperation",

        "CompanyName": "MassOperationHandler",

        "Description": ""

    }

]
```

## Retrieve available layouts for a mass operation

When you add a mass operation that uses an event handler to an object type, you must select a layout that displays after the user initiates the operation in the Relativity UI.

To retrieve a list of available layouts, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/mass-operations/get-available-layouts
```

Set the {WorkspaceID} variable to the Artifact ID of a workspace.

View a JSON request for retrieving available layouts Copy

```text
1
2
3
4
5
{

    "ObjectType": {

        "Name": "My RDO"

    }

}
```

View a JSON response for available layouts Copy

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
[

    {

        "ObjectTypeName": "Analytics Categorization Result",

        "Name": "Analytics Categorization Result Layout",

        "ArtifactID": 1037450,

        "Guids": []

    },

    {

        "ObjectTypeName": "Analytics Categorization Set",

        "Name": "Analytics Categorization Set Layout",

        "ArtifactID": 1037459,

        "Guids": []

    },

    ...

    {

        "ObjectTypeName": "Workspace Processing Settings",

        "Name": "Workspace Processing Settings Layout",

        "ArtifactID": 1103324,

        "Guids": []

    }

]
```
