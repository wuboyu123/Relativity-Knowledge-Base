---
title: "Client Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Client_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:25:49+00:00
sha256: 5c942f0a8590920de4f54c7eb9f359fd3f1fb4ffeb19ccd639b716b0cb606ad6
---

Client Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Client Manager (REST)

In Relativity, a client is a company or organization, which is associated with users, matters, groups, and workspaces. For general information, see Clients on the Relativity Server 2025 Documentation site.

The Client Manager service exposes endpoints that provide the following functionality:

- CRUD operations on clients.

- Helper endpoints for retrieving lists of available groups, matters, users, and statuses.

- Endpoints for creating, submitting, and retrying client domain activation keys.

As a sample use case, you can programmatically create multiple clients by using the Client Manager service eliminating the need to manually add them through the Relativity UI.

You can also use the Client Manager service through .NET. For more information, see Client Manager (.NET) .

## Guidelines for the Client Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a client:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {clientID} to the Artifact ID of a specific client.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Client Manager service. To download the sample file, click Client Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Client Manager service, send requests by making calls with the required HTTP methods. The following code sample illustrates how to make calls to the Client Manager service from a .NET client.

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
private HttpClient GetHttpClient()

{

    HttpClient httpClient = new HttpClient();



    httpClient.BaseAddress = new Uri("https://localhost/");

    httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    httpClient.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));



    return httpClient;

}



public async Task<List<int>> GetEligibleStatuses()

{

    string url = "/Relativity.rest/api/relativity-identity/v1/workspaces/-1/clients/eligible-statuses";



    HttpClient httpClient = GetHttpClient();

    HttpResponseMessage response = await httpClient.GetAsync(url);

    string resultString = await response.Content.ReadAsStringAsync();



    var statusIDs = new List<int>();



    dynamic result = JObject.Parse(resultString) as JObject;

    foreach (var obj in result.Objects)

    {

        int statusID = obj.ArtifactID;

        statusIDs.Add(statusID);

    }



    return statusIDs;

}



public async Task<int> Create(int statusID)

{

    string url = "/Relativity.rest/api/relativity-identity/v1/workspaces/-1/clients/";

    var payload = new

    {

        clientRequest = new

        {

            Name = "Sample client name",

            Number = "Sample client number",

            Status = new

            {

                ArtifactID = statusID

            },

            Keywords = "Sample keywords",

            Notes = "Sample notes"

        }

    };



    string payloadString = JsonConvert.SerializeObject(payload);

    var content = new StringContent(payloadString, Encoding.UTF8, "application/json");



    HttpClient httpClient = GetHttpClient();

    HttpResponseMessage message = await httpClient.PostAsync(url, content);

    string resultString = await response.Content.ReadAsStringAsync();



    dynamic result = JObject.Parse(resultString) as JObject;

    int artifactID = result.ArtifactID;



    return artifactID;

}
```

## Create a client

To add a new client to Relativity, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/
```

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View field descriptions for a request

The body of the request must contain the following fields unless specifically identified as optional:

- clientRequest - represents the data used to create or update a client. It contains the following fields:

- Name - the user-friendly name of the client.

- Number - a string representing the number assigned to the client.

- Status - an object representing the status of the client. It contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

- Keywords - optional words or phrase used to describe the client.

- Notes - additional information about the client.

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

    "ClientRequest" : {

        "Name": "Example Name",

        "Number": "50",

        "Status": {

            "ArtifactID": "662",

            "Guids": []

        },

        "Keywords": "",

        "Notes": ""

    }

}
```

View field descriptions for a create response

The response contains a ClientResponse object with the following fields:

- Name - the user-friendly name of the client.

- Number - a string representing the number assigned to the client.

- Status - an object representing the status of the client. It contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

- Name - the user-friendly name of the status.

- IsClientDomain - a Boolean value indicating whether the client domain is activated for this client.

- Keywords - optional words or phrase used to describe the client.

- Notes - additional information about the client.

- CreatedOnDate - the date and time when the client was created.

- CreatedBy - an object representing the user who created the client. It contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Name - the user-friendly name of the user.

- Guids - an array of GUIDs used to identify the user.

- LastModifiedBy - an object representing the user who recently updated the client. See descriptions for the related fields under CreatedBy.

- LastModifiedOnDate - the date and time when the client was most recently modified.

- Meta - an object representing metadata for the client. It contains the following fields:

- Unsupported - an array of fields not supported on the client.

- ReadOnly - an array of client properties that can't be modified.

- Actions -an array of Action objects representing actions that can be performed on the client. Each object contains the following fields:

- Name - the name of an operation available through REST for the client.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this client.

- Reason - an explanation for the unavailability of an action.

- ArtifactID - an integer used as a unique identifier for the new client.

- Guids - an array of GUIDs identifying the client.

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
{

    "Name": "Example Name",

    "Number": "50",

    "Status": {

        "Name": "Active",

        "ArtifactID": 662,

        "Guids": []

    },

    "IsClientDomain": false,

    "Keywords": "",

    "Notes": "",

    "CreatedOnDate": "2020-10-22T00:00:00",

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

    "LastModifiedOnDate": "2020-10-22T00:00:00",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "IsClientDomain"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "ArtifactID": 1040161,

    "Guids": []

}
```

## Retrieve a client

You can retrieve basic information about a client or extended information, which also includes operations that you have permissions to perform on the client.

- Retrieve basic metadata for a client - send a GET request to with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}
```

- Retrieve extended metadata for a client - send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}?includeMetadata=true&includeActions=true
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

The request body is empty.

The response for a read operation contains the same fields as a response for a create operation. See the field descriptions in View field descriptions for a create response .

View a sample JSON response for basic metadata Copy

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

    "Name": "Example Name",

    "Number": "50",

    "Status": {

        "Name": "Active",

        "ArtifactID": 662,

        "Guids": []

    },

    "IsClientDomain": false,

    "Keywords": "",

    "Notes": "",

    "CreatedOnDate": "2020-10-22T00:00:00",

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

    "LastModifiedOnDate": "2020-10-22T00:00:00",

    "ArtifactID": 1040161,

    "Guids": []

}
```

View a sample JSON response for extended metadata Copy

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
{

    "Name": "Example Name",

    "Number": "50",

    "Status": {

        "Name": "Active",

        "ArtifactID": 662,

        "Guids": []

    },

    "IsClientDomain": false,

    "Keywords": "",

    "Notes": "",

    "CreatedOnDate": "2020-10-22T00:00:00",

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

    "LastModifiedOnDate": "2020-10-22T00:00:00",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "IsClientDomain"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "ArtifactID": 1040161,

    "Guids": []

}
```

## Update a client

You can modify the properties of a client. Additionally, you can also restrict the update of a client to the date that it was last modified by adding the LastModifiedOn field to the request body.

Send a PUT request to with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}
```

View required permissions

To use this endpoint, the caller must have the following:

- Edit permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

- clientRequest - represents the data used to create or update a client. It contains the following fields:

- Name - the user-friendly name of the client.

- Number - a string representing the number assigned to the client.

- Status - an object representing the status of the client. It contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Guids - an array of GUIDs used to identify the object.

- Keywords - optional words or phrase used to describe the client.

- Notes - additional information about the client.

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

    "ClientRequest" : {

        "Name": "New example name",

        "Number": 100,

        "Status": {

            "ArtifactID": 662,

            "Guids": []

        },

        "Keywords": "",

        "Notes": ""

    }

}
```

When the client is successfully updated, the response returns the status code of 200.

## Delete a client

To remove a client from Relativity, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}
```

Before deleting a client, consider checking for dependent clients using Object Manager service. See Object Manager (REST) .

View required permissions

To use this endpoint, the caller must have the following:

- Delete permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

When the client is successfully deleted, the response returns the status code of 200.

## Helper endpoints for CRUD operations

The following helper endpoints retrieve lists of available groups, matters, users, and statuses, which may be helpful when creating or updating clients. For general information, see Clients on the Relativity Server 2025 Documentation site.

### Retrieve associated groups

To retrieve information about groups associated with a client, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}/query-groups
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and groups set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

View field descriptions for a request

The body of a request contains the following fields:

- Request - represents a request object. It contains the following fields:

- Condition - the search criteria used for the query.

- Sorts - a list of objects describing the sort rules for the results. Each object contains the following fields:

- Field - an object describing the field. It contains the following fields:

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guid - a GUID identifying the field.

- Name - the user-friendly name of the field.

- Direction - a string specifying whether to sort the query results in ascending or descending order. Set this field to Ascending or Descending .

- Order - an integer representing the order of a sort.

- RowCondition - the search criteria used for the query.

- Fields - a list of objects describing the fields to query. Each object contains the following fields:

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guid - a GUID identifying the field.

- Name - the user-friendly name of the field.

- Start - an integer indicating the index of the first item in the query.

- Length - an integer indicating the number of items to query.

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
{

    "Request":{

        "Condition": "",

        "Sorts": "",

        "Fields":[ ]

    },

    "start": 1,

    "length": 10

}
```

View field descriptions for a response

The response contains the following fields:

- TotalCount - an integer representing the total number of items returned by the query.

- Objects - a list of objects containing the results of a query. Each object contains the following fields:

- ArtifactID - an integer used as a unique identifier for the object.

- Values -- an array of values for the requested fields.

- IDWindow - an array of Window objects containing the IDs of the objects included in the current results set.

- CurrentStartIndex - an integer indicating the index of the first item in the result set.

- ResultCount - an integer indicating the number of items in the result set.

- ObjectType - the type of object the query runs against.

- RankWindow - an array of doubles representing the ranks used to prime the review tool's session.

- Fields - an array of objects describing fields. Each object contains the following fields:

- FieldType - a string indicating the type of the field, such as FixedLengthText, Date, or others.

- ViewFieldID - an integer used as a unique identifier for the view field.

- ArtifactID - an integer used as a unique identifier for the field.

- Guids - an array of GUIDs used to identify the field.

- Name - the user-friendly name of a field.

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
{

    "TotalCount": 9,

    "Objects": [

        {

            "ArtifactID": 20,

            "Values": []

        },

        {

            "ArtifactID": 762,

            "Values": []

        },

        {

            "ArtifactID": 1015005,

            "Values": []

        },

        {

            "ArtifactID": 1015025,

            "Values": []

        },

        {

            "ArtifactID": 1015026,

            "Values": []

        },

        {

            "ArtifactID": 1015027,

            "Values": []

        },

        {

            "ArtifactID": 1015028,

            "Values": []

        },

        {

            "ArtifactID": 1015029,

            "Values": []

        },

        {

            "ArtifactID": 1015030,

            "Values": []

        }

    ],

    "IDWindow": [],

    "CurrentStartIndex": 1,

    "ResultCount": 9,

    "ObjectType": {

        "ArtifactID": 1016185,

        "Name": "Group",

        "Guids": [],

        "ArtifactTypeID": 3

    },

    "RankWindow": [],

    "Fields": []

}
```

### Retrieve associated matters

To retrieve information about the matters associated with a client, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}/query-matters
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and matters set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

This endpoint uses the same format for requests and responses as the query for groups. For field descriptions and sample JSON, see Retrieve associated groups .

### Retrieve associated users

To retrieve information about the users associated with a client, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}/query-users
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and users set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

This endpoint uses the same format for requests and responses as the query for groups. For field descriptions and sample JSON, see Retrieve associated groups .

### Retrieve available statuses

To retrieve a list of available statuses for a client, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/eligible-statuses
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and choices set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

The request body is empty.

View field descriptions for a response

The body of response contains the list of objects with the following fields:

- ArtifactID - an integer used as a unique identifier for the status.

- Name - the user-friendly name of the status.

- Guid - an array of GUIDs used to identify the status.

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
[

  {

    "Name": "Active",

    "ArtifactID": 662,

    "Guids": []

  },

  {

    "Name": "Inactive",

    "ArtifactID": 669,

    "Guids": []

  }

]
```

## Endpoints for client domain activation keys

The following endpoints support creating, submitting, and retrying client domain activation keys. For general information, see Client domains on the Relativity Documentation site.

### Create client domain activation key

To create and return the client domain activation key required to initiate the activation process, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}/client-domain/request-key
```

The request body is empty.

The response is a string containing the client domain activation key.

### Submit a client domain activation key

To submit a client domain activation key and initiate the activation process, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}/client-domain/activation-key
```

The body of a request contains the following field:

- activationKey - a string containing the client domain activation key.

Copy

```text
1
2
3
{

  "activationKey": "ABCD1234"

}
```

When the client domain is successfully activated, the response returns the status code of 200.

### Retry activating a client domain

To rerun a previously failed activation process, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-identity/{versionNumber}/workspaces/-1/clients/{clientID}/client-domain/activate
```

The request body is empty.

When the client domain is successfully activated, the response returns the status code of 200.

On this page

- Client Manager (REST)

- Guidelines for the Client Manager service

- URLs

- Postman sample file

- Client code sample

- Create a client

- Retrieve a client

- Update a client

- Delete a client

- Helper endpoints for CRUD operations

- Retrieve associated groups

- Retrieve associated matters

- Retrieve associated users

- Retrieve available statuses

- Endpoints for client domain activation keys

- Create client domain activation key

- Submit a client domain activation key

- Retry activating a client domain


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
