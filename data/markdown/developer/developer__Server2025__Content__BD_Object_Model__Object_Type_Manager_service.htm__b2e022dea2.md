---
title: "Object Type Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Object_Type_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:27:13+00:00
sha256: c411074a8d4e5e24ff13182ee853b5439aad68e67c471ea5a91d79358ce1f654
---

Object Type Manager (REST)

# Object Type Manager (REST)

The Object Type Manager service exposes endpoints for programmatically creating custom object types for use in your applications. This service includes the following features:

- Support for create, read, update, and delete operations on object types.

- Helper endpoint for retrieving parent object types.

As a sample use case, you could use the Object Type Manager service to add new object types to support a custom application that you developed. You might want to implement an application that tracks vendor or customer information and decide to add different object types for each of these items. These object types could be further customized with object rules, event handlers, and mass operations.

You can also work with the Object Type Manager service through .NET. For more information, see Object Type Manager (.NET) .

## Guidelines for the Object Type Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve an object type:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/{objectTypeArtifactID}
```

Set the path parameter as follows:

- {versionNumber} to the version of the service, such as v2 .

- {workspaceID} to the Artifact ID of the workspace containing the object type to retrieve.

- {objectTypeArtifactID} to the Artifact ID of the object type.

## Postman sample files

You can use the Postman sample files to become familiar with making calls to endpoints on the services for object types. To download the sample files, click Object Type Postman File .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Object Type Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/<workspaceID>/object-types
```

You can use the following .NET code as a sample client for creating an object type.

View code sample.

This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Object Type Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Initialize variables with the values for the object type to create, and the workspace where it should be added.

- Set the url variable to the URL for the workspace where the object type is to be added. For more information, see Create an object type .

- Set the JSON input required for the operation.

- Use the PostAsync() method to send a POST request.

- Return the results of the request and deserialize it.

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
public static async Task<ObjectTypeResponse> Create()

{

    ObjectTypeResponse result;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");

        int workspaceId = 1017660;

        int parentObjectArtifactId = 1035231;

        int applicationId = 1042129;

        string inputJSON = $"{{\"ObjectTypeRequest\": {{\"ParentObjectType\": {{\"Value\": {{\"ArtifactID\": \"{parentObjectArtifactId}\"}}}},\"RelativityApplications\": [{{\"ArtifactID\": \"{applicationId}\"}}],\"Name\": \"Object Test 1\",\"CopyInstancesOnCaseCreation\": false,\"CopyInstancesOnParentCopy\": false,\"EnableSnapshotAuditingOnDelete\": true,\"PersistentListsEnabled\": false,\"PivotEnabled\": true,\"SamplingEnabled\": false,\"Keywords\": \"\",\"Notes\": \"\"}}}}";

        var url = $@"/Relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/";

        var response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<ObjectTypeResponse>(content);

    }

    return result;

}
```

## CRUD operations for object types

The Object Type Manager service supports create, read, update, and delete operations on object types. It also includes helper endpoints used to retrieve information about parent object types, and dependent objects.

Review the following guidelines for working with this service:

- Verify that you have the appropriate permissions to access an object type before attempting to modify or delete it.

- Verify that the Relativity application is unlocked before attempting to add an object type to it, or to modify or delete an existing object type. You also need permissions to the application and the object type to perform these tasks.

See the following subsections for more information:

- Create an object type

- Read an object type

- Update an object type

- Delete an object type

- Retrieve a parent object types

### Create an object type

When creating a new object type, you need to identify its parent object type. For more information, see Retrieve a parent object types .

To create an object type, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/
```

View field descriptions for a request

The JSON request contains the following fields:

- ObjectTypeRequest - represents a request to create or update an object type. It contains the following fields:

- ParentObjectType - indicates the parent object type of the object type. For example, an object type may be a child of the Document object. This field contains the following subfields:

- Value - contains an ArtifactTypeID, which is an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10. The Value field also contains the Artifact ID of the object type.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object type is linked to the applications in this array. If the array is empty, then the object type is not linked to any application.

- Name - the user-friendly name of the object type.

- CopyInstancesOnCaseCreation - a Boolean value indicating whether instances of this object type are copied when you create a new workspace. For more information, see Fields for an object type .

- CopyInstancesOnParentCopy - a Boolean value indicating whether the child objects are copied when the parent object is copied. For more information, see Fields for an object type .

- EnableSnapshotAuditingOnDelete - a Boolean value indicating whether to capture audit information about the current field values for an object. For more information, see Fields for an object type .

- PersistentListsEnabled - a Boolean value indicating whether users can save lists of these object instances.

- PivotEnabled - a Boolean value indicating whether pivot functionality is available on objects of this type. Pivot provides the functionality to analyze and report trends or patterns by querying specific sets of data and summarizing the results. For more information, see Pivot .

- SamplingEnabled - a Boolean value indicating whether the sampling functionality is enabled on the object. You can use sampling to create a group of documents for quality control or other purposes. For more information, see Sampling .

- Keywords - optional words or phrases used to describe the object type.

- Notes - an optional description or other information about the object type.

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

   "ObjectTypeRequest" : {

       "ParentObjectType": {

           "Secured": false,

           "Value": {

               "ArtifactTypeID": 10,

               "ArtifactID": 1035231

           }

        },

        "RelativityApplications":[

           {

            "ArtifactID": 1045231

           }

         ],

        "Name": "My Custom Object Type",

        "CopyInstancesOnCaseCreation": false,

        "CopyInstancesOnParentCopy": false,

        "EnableSnapshotAuditingOnDelete": true,

        "PersistentListsEnabled": false,

        "PivotEnabled": true,

        "SamplingEnabled": false,

        "Keywords": "",

        "Notes": ""

   }

}
```

View field descriptions for a response

The response contains the following fields:

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ParentObjectType - contains information about the parent object type, as follows:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name for the parent object type.

- ArtifactTypeID - an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of the parent object type.

- Guids - an array of GUIDs used to identify the parent object type.

- CopyInstancesOnCaseCreation - a Boolean value indicating whether instances of this object type are copied when you create a new workspace. For more information, see Fields for an object type .

- CopyInstancesOnParentCopy - a Boolean value indicating whether the child objects are copied when the parent object is copied. For more information, see Fields for an object type .

- EnableSnapshotAuditingOnDelete - a Boolean value indicating whether to capture audit information about the current field values for an object. For more information, see .

- IsDynamic - a Boolean value indicating whether this object type is a custom type that is user-created.

- IsSystem - a Boolean value indicating whether this object type is available as an out-of-the-box type provided with Relativity.

- IsExtensible - a Boolean value indicating whether the object type can have new event handlers, mass operations and object rules.

- IsViewEnabled - a Boolean value indicating whether the view for the object type is enabled.

- PersistentListsEnabled - a Boolean value indicating whether users can save lists of these object instances.

- PivotEnabled - a Boolean value indicating whether pivot functionality is available on objects of this type. Pivot provides the functionality to analyze and report trends or patterns by querying specific sets of data and summarizing the results. For more information, see Pivot .

- SamplingEnabled - a Boolean value indicating whether the sampling functionality is enabled on the object. You can use sampling to create a group of documents for quality control or other purposes. For more information, see Sampling .

- FieldByteUsage - an integer value indicating the number of bytes used by the fields on the object type.

- RelativityApplications - contains the following fields:

- HasSecuredItems - a Boolean value indicating whether the application contains items that the current user does not have permission to access.

- ViewableItems - an array of identifier objects for items that are accessible to the current user. For example, an object in this array would contain the name, Artifact IDs, and GUIDs for an application.

- CreatedOn - the date and time when the object type was added to Relativity.

- CreatedBy - contains the Artifact ID and name of the user who created the object type. It also contains an array of GUIDs used to identify the user.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the object type. It also contains an array of GUIDs used to identify the user.

- LastModifiedOn - the date and time when the object type was most recently modified.

- Keywords - optional words or phrases used to describe the object type.

- Notes - an optional description or other information about the object type.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of properties that indicate functionality not available on the current instance of this object type. For example, if a user could not persist objects of this type in a list, then array would include PersistentListsEnabled.

- ReadOnly - an array of object type properties that cannot be modified, such its name or parent object type.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this object type. For example, you may not have permissions to modify an object type that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the object type, such as delete, update, and others.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this object type.

- Reason - provides an explanation for the unavailability of an action.

- Name - the user-friendly name for the object type.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type

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
{

    "ObjectIdentifier": {

        "Name": "Object Test 1",

        "ArtifactID": 1042195,

        "Guids": []

    },

    "ArtifactTypeID": 1000070,

    "ParentObjectType": {

        "Secured": false,

        "Value": {

            "ArtifactTypeID": 10,

            "Name": "Document",

            "ArtifactID": 1035231,

            "Guids": [

                "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

            ]

        }

    },

    "CopyInstancesOnCaseCreation": false,

    "CopyInstancesOnParentCopy": false,

    "EnableSnapshotAuditingOnDelete": true,

    "IsDynamic": true,

    "IsSystem": false,

    "IsExtensible": true,

    "IsViewEnabled": true,

    "PersistentListsEnabled": false,

    "PivotEnabled": true,

    "SamplingEnabled": false,

    "FieldByteUsage": 514,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": [

            {

                "Name": "SampleApplication",

                "ArtifactID": 1042129,

                "Guids": [

                    "3952dc53-a00e-47f7-b33c-e6b4d04e66d2"

                ]

            }

        ]

    },

    "CreatedOn": "2021-02-24T22:28:43.247",

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "LastModifiedOn": "2021-02-24T22:28:43.247",

    "Keywords": "",

    "Notes": "",

    "Actions": []

}
```

### Read an object type

You can retrieve basic information about an object type or extended information, which also includes operations that you have permissions to perform on the object type.

- Retrieve basic metadata for an object type - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/{objectTypeArtifactID}
```

- Retrieve extended metadata for an object type - send a GET request with a URL in the following general format:

- includeMetadata - an optional query parameter which specifies whether to return extended metadata for the object type.

- includeActions - an optional query parameter which, if set to true, will return an array of Action objects indicating operations you have permissions to perform on the object type.

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/{ArtifactID}?includeMetadata=true&includeActions=true
```

View field descriptions for a response

The response contains the following fields:

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ParentObjectType - contains information about the parent object type, as follows:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name for the parent object type.

- ArtifactTypeID - an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of the parent object type.

- Guids - an array of GUIDs used to identify the parent object type.

- CopyInstancesOnCaseCreation - a Boolean value indicating whether instances of this object type are copied when you create a new workspace. For more information, see Fields for an object type .

- CopyInstancesOnParentCopy - a Boolean value indicating whether the child objects are copied when the parent object is copied. For more information, see Fields for an object type .

- EnableSnapshotAuditingOnDelete - a Boolean value indicating whether to capture audit information about the current field values for an object. For more information, see .

- IsDynamic - a Boolean value indicating whether this object type is a custom type that is user-created.

- IsSystem - a Boolean value indicating whether this object type is available as an out-of-the-box type provided with Relativity.

- IsExtensible - a Boolean value indicating whether the object type can have new event handlers, mass operations and object rules.

- IsViewEnabled - a Boolean value indicating whether the view for the object type is enabled.

- PersistentListsEnabled - a Boolean value indicating whether users can save lists of these object instances.

- PivotEnabled - a Boolean value indicating whether pivot functionality is available on objects of this type. Pivot provides the functionality to analyze and report trends or patterns by querying specific sets of data and summarizing the results. For more information, see Pivot .

- SamplingEnabled - a Boolean value indicating whether the sampling functionality is enabled on the object. You can use sampling to create a group of documents for quality control or other purposes. For more information, see Sampling .

- FieldByteUsage - an integer value indicating the number of bytes used by the fields on the object type.

- RelativityApplications - contains the following fields:

- HasSecuredItems - a Boolean value indicating whether the application contains items that the current user does not have permission to access.

- ViewableItems - an array of identifier objects for items that are accessible to the current user. For example, an object in this array would contain the name, Artifact IDs, and GUIDs for an application.

- CreatedOn - the date and time when the object type was added to Relativity.

- CreatedBy - contains the Artifact ID and name of the user who created the object type. It also contains an array of GUIDs used to identify the user.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the object type. It also contains an array of GUIDs used to identify the user.

- LastModifiedOn - the date and time when the object type was most recently modified.

- Keywords - optional words or phrases used to describe the object type.

- Notes - an optional description or other information about the object type.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this object type. For example, you may not have permissions to modify an object type that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the object type, such as delete, update, and others.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this object type.

- Reason - provides an explanation for the unavailability of an action.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of properties that indicate functionality not available on the current instance of this object type. For example, if a user could not persist objects of this type in a list, then array would include PersistentListsEnabled.

- ReadOnly - an array of object type properties that cannot be modified, such its name or parent object type.

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
{

    "ObjectIdentifier": {

        "Name": "Object Test 1",

        "ArtifactID": 1042195,

        "Guids": []

    },

    "ArtifactTypeID": 1000070,

    "ParentObjectType": {

        "Secured": false,

        "Value": {

            "ArtifactTypeID": 10,

            "Name": "Document",

            "ArtifactID": 1035231,

            "Guids": [

                "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

            ]

        }

    },

    "CopyInstancesOnCaseCreation": false,

    "CopyInstancesOnParentCopy": false,

    "EnableSnapshotAuditingOnDelete": true,

    "IsDynamic": true,

    "IsSystem": false,

    "IsExtensible": true,

    "IsViewEnabled": true,

    "PersistentListsEnabled": false,

    "PivotEnabled": true,

    "SamplingEnabled": false,

    "FieldByteUsage": 514,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": [

            {

                "Name": "TestApp",

                "ArtifactID": 1042129,

                "Guids": [

                    "3952dc53-a00e-47f7-b33c-e6b4d04e66d2"

                ]

            }

        ]

    },

    "CreatedOn": "2021-02-24T22:28:43.247",

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "LastModifiedOn": "2021-02-24T22:28:43.247",

    "Keywords": "",

    "Notes": "",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "ParentObjectType",

            "IsDynamic"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-object-model/{versionNumber}/workspaces/1017660/object-types/1042195",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-object-model/{versionNumber}/workspaces/1017660/object-types/1042195",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

}
```

### Update an object type

To modify an object type, send a PUT request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/{ArtifactID}
```

View field descriptions for a request

The body of the request must contain the following fields unless specifically identified as optional:

- ObjectTypeRequest - represents a request to create or update an object type. It contains the following fields:

- ParentObjectType - indicates the parent object type of the object type. For example, an object type may be a child of the Document object. This field contains the following subfields:

- Value - contains an ArtifactTypeID, which is an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10. The Value field also contains the Artifact ID of the object type.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object type is linked to the applications in this array. If the array is empty, then the object type is not linked to any application.

- Name - the user-friendly name of the object type.

- CopyInstancesOnCaseCreation - a Boolean value indicating whether instances of this object type are copied when you create a new workspace. For more information, see Fields for an object type .

- CopyInstancesOnParentCopy - a Boolean value indicating whether the child objects are copied when the parent object is copied. For more information, see Fields for an object type .

- EnableSnapshotAuditingOnDelete - a Boolean value indicating whether to capture audit information about the current field values for an object. For more information, see Fields for an object type .

- PersistentListsEnabled - a Boolean value indicating whether users can save lists of these object instances.

- PivotEnabled - a Boolean value indicating whether pivot functionality is available on objects of this type. Pivot provides the functionality to analyze and report trends or patterns by querying specific sets of data and summarizing the results. For more information, see Pivot .

- SamplingEnabled - a Boolean value indicating whether the sampling functionality is enabled on the object. You can use sampling to create a group of documents for quality control or other purposes. For more information, see Sampling .

- Keywords - optional words or phrases used to describe the object type.

- Notes - an optional description or other information about the object type.

- LastModifiedOn - the date and time when the object type was most recently modified. This field is only required if you want to restrict the update of an object type to the date that it was last modified. The value must match the LastModifiedOn date for the object type stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

    "objectTypeRequest":{

        "Name":"Custom Object Type",

        "ParentObjectType":{

            "Value":{

                "ArtifactTypeID":10

            }

        },

        "UseRelativityForms":true,

        "CopyInstancesOnCaseCreation":false,

        "CopyInstancesOnParentCopy":false,

        "EnableSnapshotAuditingOnDelete":true,

        "PersistentListsEnabled":true,

        "PivotEnabled":true,

        "SamplingEnabled":false,

        "RelativityApplications":[],

        "Keywords":"",

        "Notes":""

    },

    "LastModifiedOn":"2021-02-25T15:06:14.48"

}
```

When the object type is successfully updated, the response contains the status code of 200.

### Delete an object type

To remove an object type from Relativity, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/{ArtifactID}
```

The request body is empty.

When the object type is successfully deleted, the response returns the status code of 200.

### Retrieve a parent object types

Use this endpoint to retrieve a list of parent object types. You may want to call this endpoint before creating a new object type, because you must specify its parent object type. For more information, see Create an object type .

To call this endpoint, send a GET request to the URL with the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/object-types/available-parent-object-types
```

The request body is empty.

View field descriptions for a response

The response contains the following fields for each parent object type:

- Name - the user-friendly name of the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

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
[

    {

        "ArtifactTypeID": 1000017,

        "Name": "Analytics Categorization Result",

        "ArtifactID": 1036390,

        "Guids": []

    },

    {

        "ArtifactTypeID": 1000018,

        "Name": "Analytics Categorization Set",

        "ArtifactID": 1036399,

        "Guids": []

    },

    {

        "ArtifactTypeID": 1000045,

        "Name": "Analytics Categorization Set Build History",

        "ArtifactID": 1039799,

        "Guids": []

    },

    {

        "ArtifactTypeID": 1000019,

        "Name": "Analytics Category",

        "ArtifactID": 1036408,

        "Guids": []

    },

    {

        "ArtifactTypeID": 8,

        "Name": "Workspace",

        "ArtifactID": 1035229,

        "Guids": []

    }

]
```
