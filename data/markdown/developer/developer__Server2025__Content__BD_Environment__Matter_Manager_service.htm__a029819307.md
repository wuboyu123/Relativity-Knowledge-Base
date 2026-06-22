---
title: "Matter Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Matter_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:29+00:00
sha256: 066c23e3c14fcd79f02145ce498977441fd989809c6487dc207c504b990b2b55
---

Matter Manager (REST)

# Matter Manager (REST)

In Relativity, a matter is a legal case, such as a dispute or other action during which a law firm acts as a representative of a client. For general information, see Matters on the Relativity Documentation site.

The Matter Manager service exposes multiple endpoints for programmatically managing matters in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations on matters.

- Provides helper endpoints used to retrieve available clients and statuses. Use these endpoints when creating or updating matters.

You can also use the Matter Manager service through .NET. For more information, see Matter Manager (.NET) .

## Guidelines for the Matter Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a matter:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspaces/-1/matters/{Matter ID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {Matter ID} to the Artifact ID of a specific matter.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Matter Manager service. To download the sample file, click Matter Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

In the following examples, the URLs use -1 to indicate the admin-level context. For example, the URL for creating a matter uses -1 as the workspace ID. See Create a matter .

## Retrieve a list of available clients

To retrieve a list of the available clients in a Relativity environment, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/eligible-clients
```

The request body is empty.

The response contains the following fields for each server returned in the array:

- Name – the name of the client.

- ArtifactID - the Artifact ID of the client.

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
[

    {

        "Name": "Relativity Template",

        "ArtifactID": 1006066

    },

    {

        "Name": "Relativity",

        "ArtifactID": 1015644

    }

]
```

## Retrieve a list of matter statuses

To retrieve a list of available matter statuses in a Relativity environment, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity-environment/{versionNumber}/workspaces/-1/matters/eligible-statuses
```

The request body is empty.

The response contains the following fields for each server returned in the array:

- Name – the name of the status.

- ArtifactID - the Artifact ID of the status.

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
[

    {

        "Name": "Active",

        "ArtifactID": 671

    },

    {

        "Name": "Inactive",

        "ArtifactID": 670

    }

]
```

## Create a matter

Before creating a matter, you need to identify an available client and status to associate with the matter. Use the helper endpoints to obtain this information. See Retrieve a list of available clients and Retrieve a list of matter statuses .

To add a new matter to a Relativity environment, send a POST request to this URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspaces/-1/matters
```

View field descriptions for a request

The body of the request must contain the following fields unless specifically identified as optional:

- MatterRequest - represents a request for creating or updating a matter. It includes the following fields:

- Client - indicates the client to be associated with this matter. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the client.

- Status – indicates the status of the matter:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the status.

- Name – the name of the matter.

- Number – indicates the numbered ordering used to display this matter in a list of matters.

- Keywords - an optional description or other information about the matter.

- Notes - optional words or phrase used to describe the matter.

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

    "MatterRequest" : {

        "Client": {

            "Secured": false,

            "Value": {

                "ArtifactID": "1012273"

            }

        },

        "Status": {

            "Secured": false,

            "Value": {

                "ArtifactID": "1018493"

            }

        },

        "Name": "Example Name",

        "Number": "10",

        "Keywords": "",

        "Notes": ""

    }

}
```

When the matter is successfully created, the response returns the status code of 200.

## Retrieve metadata for a matter

You can retrieve basic information about a matter or extended information, which also includes operations that you have permissions to perform on the matter.

- Retrieve basic metadata for a matter - send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspaces/-1/matters/{Matter ID}
```

- Retrieve extended metadata for a matter -send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspaces/-1/matters/{Matter ID}/true/true
```

The body of the request is empty.

View the descriptions of JSON response fields

- Client - indicates the client associated with this matter. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the client.

- Status – indicates the status of the matter:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the status.

- Name – the name of the matter.

- Number – indicates the numbered ordering used to display this matter in a list of matters.

- CreatedOn - the date and time when the matter was added to Relativity.

- CreatedBy - contains the Artifact ID and name of the user who created the matter.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the matter.

- LastModifiedOn - the date and time when the matter was most recently modified.

- Keywords - an optional description or other information about the matter.

- Notes - optional words or phrase used to describe the matter.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - a listed of fields not supported on the matter.

- ReadOnly - an array of matter properties that can't be modified, such its name or client.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this matter. For example, you may not have permissions to modify a matter due to your privileges. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the matter, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this matter.

- Reason - provides an explanation for the unavailability of an action.

View JSON for a sample response without extended metadata: Copy

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
{

    "Client": {

        "Secured": false,

        "Value": {

            "Name": "Relativity Template",

            "ArtifactID": 1006066

        }

    },

    "Number": "10",

    "Status": {

        "Secured": false,

        "Value": {

            "Name": "Active",

            "ArtifactID": 671

        }

    },

    "Keywords": "",

    "Notes": "",

    "Actions": [],

    "CreatedOn": "2019-05-08T21:36:08.953",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9

    },

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9

    },

    "LastModifiedOn": "2019-05-08T21:36:08.953",

    "Name": "Example Name",

    "ArtifactID": 1019900

}
```

View JSON for a sample response with extended metadata Copy

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
{

    "Client": {

        "Secured": false,

        "Value": {

            "Name": "Relativity Template",

            "ArtifactID": 1006066

        }

    },

    "Number": "10",

    "Status": {

        "Secured": false,

        "Value": {

            "Name": "Active",

            "ArtifactID": 671

        }

    },

    "Keywords": "",

    "Notes": "",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": []

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-environment/v1/workspace/-1/matters/1023963",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-environment/v1/workspace/-1/matters/1023963",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "CreatedOn": "2019-05-08T15:35:33.387",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9

    },

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9

    },

    "LastModifiedOn": "2019-05-08T15:35:33.387",

    "Name": "Example Name",

    "ArtifactID": 1019900

}
```

## Update a matter

You can modify the properties of a matter, such as its name. Additionally, you can also restrict the update of a matter to the date that it was last modified by adding the LastModifiedOn field to the request.

To update the properties of a matter, send a PUT request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspaces/-1/matters/{Matter ID}
```

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

- MatterRequest - represents a request for creating or updating a matter. It includes the following fields:

- Client - indicates the client to be associated with this matter. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the client.

- Status – indicates the status of the matter:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the status.

- Name – the name of the matter.

- Number – indicates the numbered ordering used to display this matter in a list of matters.

- Keywords - an optional description or other information about the matter.

- Notes - optional words or phrase used to describe the matter.

- LastModifiedOn - the date and time when the matter was most recently modified. This field is only required if you want to restrict the update of a matter to the date that it was last modified. The value must match the LastModifiedOn date for the matter stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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

    "MatterRequest":{

        "Client": {

            "Secured": true,

            "Value": {

                "ArtifactID": "1019900"

            }

        },

        "Status": {

            "Secured": true,

            "Value": {

                "ArtifactID": "1100893"

            }

        },

        "Name": "New Name",

        "Number": "5",

        "Keywords": "",

        "Notes": ""

    }

}
```

When the matter is successfully updated, the response returns the status code of 200.

## Delete a matter

You can delete a matter from a Relativity environment if it isn't associated with any workspace.

To delete a matter, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-environment/{versionNumber}/workspaces/-1/matters/{ToDelete}
```

The body of the request is empty.

When the matter is successfully deleted, the response returns the status code of 200.
