---
title: "Group Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Group_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:26:28+00:00
sha256: 31243d12dd88e08c3575941b7411d2a38390b978fae224790860133de8e6ef3a
---

Group Manager (REST)

# Group Manager (REST)

In Relativity, you can organize users by assigning them to one or more groups. Additionally, you can set permissions for a group. For more information, see Groups in the Relativity Documentation site.

The Group Manager service exposes endpoints that provide the following functionality:

- CRUD and query operations on groups.

- Helper endpoints for adding and removing users.

- Helper endpoints for querying on available users and clients to associate with a group.

- Mass operations for adding and removing multiple users to or from multiple groups.

As a sample use case, you might create an application with a custom interface for adding multiple users with a mass operation.

You can also use the Group Manager service through .NET. For more information, see Group Manager (.NET) .

## Guidelines for the Group Manager service

Review the following guidelines for working with the Group Manager service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}?includeMetadata=true&includeActions=true
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1 .

- {groupArtifactID} to the Artifact ID of the group.

## Client code sample

To use the Group Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Groups/workspace/{workspaceID}/groups/
```

You can use the following C# code as a sample client for creating a group. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Group Manager service.

- Set the required headers for the request. For more information, see HTTP headers .

- Set the URL required for the operation.

- Set the JSON payload required for the operation.

- Use the PostAsync() method to send a POST request.

- Return the artifact ID of the created group.

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
private HttpClient GetHttpClient()

{

    HttpClient httpClient = new HttpClient();

    httpClient.BaseAddress = new Uri("https://localhost/");

    httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    httpClient.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test.user@mydomain.com:Password")));

    return httpClient;

}

public async Task<List<int>> GetEligibleClientIDs()

{

    string url = "/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/query-eligible-clients";

    var payload = new

    {

        request = new

        {

            Fields = new[]

            {

        new { Name = "*" }

    }

        },

        start = 1,

        length = 100

    };

    string payloadString = JsonConvert.SerializeObject(payload);

    var content = new StringContent(payloadString, Encoding.UTF8, "application/json");

    HttpClient httpClient = GetHttpClient();

    HttpResponseMessage response = await httpClient.PostAsync(url, content);

    string resultString = await response.Content.ReadAsStringAsync();

    var clientIDs = new List<int>();

    dynamic result = JObject.Parse(resultString) as JObject;

    foreach (var obj in result.Objects)

    {

        int clientID = obj.ArtifactID;

        clientIDs.Add(clientID);

    }

    return clientIDs;

}

public async Task<int> Create(int clientID)

{

    string url = "Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/";

    var payload = new

    {

        groupRequest = new

        {

            Name = "Sample group name",

            Client = new

            {

                Value = new { ArtifactID = clientID }

            },

            Keywords = "Sample keywords",

            Notes = "Sample notes"

        }

    };

    string payloadString = JsonConvert.SerializeObject(payload);

    var content = new StringContent(payloadString, Encoding.UTF8, "application/json");

    HttpClient httpClient = GetHttpClient();

    HttpResponseMessage message = await httpClient.PostAsync(url, content);

    string resultString = await message.Content.ReadAsStringAsync();

    dynamic result = JObject.Parse(resultString) as JObject;

    int artifactID = result.ArtifactID;

    return artifactID;

}
```

## Create a group

To create a group, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/
```

View field descriptions for a request

The request contains a groupRequest object with the following fields:

- Client - represents a client to associated with the group. It contains the following fields:

- Secured - a Boolean value indicating whether the object is secured. The values for this field are true or false.

- Value - represents a client object associated with the group. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for the client.

- Guids - a list of GUIDs identifying the client.

- Name - the user-friendly name of the group.

- Keywords - optional words or phrases used to describe the group.

- Notes - additional information about the group.

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

    "groupRequest": {

        "Client": {

            "Value": {

                "ArtifactID": 1015644

            }

        },

        "Name": "MyGroup",

        "Keywords": "Keywords",

        "Notes": "Notes"

    }

}
```

View field descriptions for a create response

The response contains the following fields:

- Client - represents a client to associated with the group. It contains the following fields:

- Secured - a Boolean value indicating whether the object is secured. The values for this field are true or false.

- Value - represents a client object associated with the group. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for the client.

- Guids - an array of GUIDs identifying the client.

- GroupType - indicates the type of the group as follows:

Name Value Description

SystemAdmin "SystemAdmin" A group containing system administrators

SystemGroup "SystemGroup" A group containing users

Everyone "Everyone" A group containing all the users in the system

- Keywords - optional words or phrases used to describe the group.

- Notes - additional information about the group.

- CreatedOn - the date and time when the group was created.

- CreatedBy - represents the user who created the group. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for the user.

- Name - the name of the user.

- Guids - a list of GUIDs identifying the user.

- LastModifiedBy - represents the user who recently updated the group. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for the user.

- Name - the name of the user.

- Guids - a list of GUIDs identifying the user.

- LastModifiedOn - the date and time when the group was most recently modified.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of fields not supported on the current instance of this object.

- ReadOnly - an array of fields that cannot be modified.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this object. For example, you may not have permissions to modify a tab that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - the name of an operation available through REST for the tab, such as delete, update, and others.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this object.

- Reason - an explanation for the unavailability of an action.

- Name - the user-friendly name of the group.

- ArtifactID - an integer representing a unique identifier for the group.

- Guids - an array of GUIDs identifying the group.

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
{

    "Client": {

        "Secured": false,

        "Value": {

            "Name": "Relativity",

            "ArtifactID": 1015644,

            "Guids": []

        }

    },

    "GroupType": "SystemGroup",

    "Keywords": "Keywords",

    "Notes": "Notes",

    "CreatedOn": "2021-05-21T18:38:39.313",

    "CreatedBy": {

        "Name": "user, demo",

        "ArtifactID": 1029460,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "user, demo",

        "ArtifactID": 1029460,

        "Guids": []

    },

    "LastModifiedOn": "2021-05-21T18:38:39.313",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "GroupType"

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

        },

        {

            "Name": "AddMembers",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "RemoveMembers",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Name": "MyGroup",

    "ArtifactID": 1029462,

    "Guids": []

}
```

## Retrieve a group

To retrieve a group, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}?includeMetadata=true&includeActions=true
```

The request body is empty.

The response for a read operation contains the same fields as a response for a create operation. See the descriptions in View field descriptions for a create response .

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
{

    "Client": {

        "Secured": false,

        "Value": {

            "Name": "Relativity",

            "ArtifactID": 1015644,

            "Guids": []

        }

    },

    "GroupType": "SystemGroup",

    "Keywords": "Keywords",

    "Notes": "Notes",

    "CreatedOn": "2021-05-21T18:38:39.313",

    "CreatedBy": {

        "Name": "user, demo",

        "ArtifactID": 1029460,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "user, demo",

        "ArtifactID": 1029460,

        "Guids": []

    },

    "LastModifiedOn": "2021-05-21T18:38:39.313",

    "Name": "MyGroup",

    "ArtifactID": 1029462,

    "Guids": []

}
```

## Update a group

To update a group, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}
```

View field descriptions for a request

The request contains a groupRequest object with the following fields:

- Client - represents a client to associated with the group. It contains the following fields:

- Value - represents a client object associated with the group. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for the client.

- Name - the user-friendly name of the group.

- Keywords - optional words or phrases used to describe the group.

- Notes - additional information about the group.

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

    "groupRequest": {

        "Client": {

            "Value": {

                "ArtifactID": 1015644

            }

        },

        "Name": "MyGroup",

        "Keywords": "Updated Keywords",

        "Notes": "Updated Notes"

    }

}
```

The response for an update operation contains the same fields as a response for a create operation. See the descriptions in View field descriptions for a create response .

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
{

    "Client": {

        "Secured": false,

        "Value": {

            "Name": "Relativity",

            "ArtifactID": 1015644,

            "Guids": []

        }

    },

    "GroupType": "SystemGroup",

    "Keywords": "Updated Keywords",

    "Notes": "Updated Notes",

    "CreatedOn": "2021-05-21T18:38:39.313",

    "CreatedBy": {

        "Name": "user, demo",

        "ArtifactID": 1029460,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "user, demo",

        "ArtifactID": 1029460,

        "Guids": []

    },

    "LastModifiedOn": "2021-05-21T18:46:33.13",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "GroupType"

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

        },

        {

            "Name": "AddMembers",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "RemoveMembers",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "Name": "MyGroup",

    "ArtifactID": 1029462,

    "Guids": []

}
```

## Delete a group

To delete a group, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}
```

The request body is empty.

When the group is successfully deleted, the response returns the status code of 200.

## Add users to a group

To add users to a group, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}/members
```

View field descriptions for a request

The body of a request contains the following fields:

- Users - an array of objects describing the users to add. Each object contains the following fields:

- ArtifactID - an integer representing a unique identifier for the user

- Guids - a list of GUIDs identifying the user.

View a sample JSON request Copy

```text
1
2
3
4
5
6
{

    "users": [

        { "ArtifactID": 1029457 },

        { "ArtifactID": 1029460 }

    ]

}
```

When the users are successfully added, the response returns the status code of 200.

## Remove users from a group

To remove users from a group, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}/members
```

View field descriptions for a request

The body of a request contains the following fields:

- Users - a list of objects describing the users to remove. Each object contains the following fields:

- ArtifactID - an integer representing a unique identifier for the user.

- Guids - an array of GUIDs identifying the user.

View a sample JSON request Copy

```text
1
2
3
4
5
6
{

    "users": [

        { "ArtifactID": 1029457 },

        { "ArtifactID": 1029460 }

    ]

}
```

When the users are successfully deleted, the response returns the status code of 200.

## Helper methods for users and clients

The Group Manager service exposes multiple helper methods that you can use to query for information about users and clients.

### Query for clients to associate with a group

To query the clients that can be assigned to a group, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/eligible-clients/query
```

View field descriptions for a request

The request contains the following fields:

- request - a request object with the following fields:

- Fields - an array containing the following fields:

- Name - the names or email addresses of users to query on.

- Condition - the search criteria used in the query. For more information, Query for resources . This field is optional.

- start - the values in the start and length fields both determine the page number being requested. For example, if you set length to 25 and start to record 17, Relativity interprets these setting as a request for the first page and returns audits 1-25. If you set start to 35, it returns the second page with audits 26-50.

- length - the number of items to return in the query result, beginning with index in the start field. See description for start field.

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
{

    "request": {

        "Fields": [

            {"Name": "Name"}

        ],

        "Condition": ""

    },

    "start": 1,

    "length": 1000

}
```

View field descriptions for a query response

The response contains the following fields:

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array contains objects with the following fields:

- ArtifactID - an integer representing a unique identifier for the object.

- Values - an array containing strings representing usernames and email addresses.

- IDWindow - reserved for future use.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - an object containing the following fields:

- ArtifactID - an integer representing a unique identifier for the object.

- Name - the user-friendly name of the object type.

- Guids - an array of GUIDs identifying the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- RankWindow - reserved for future use.

- Fields - an array of fields with the following properties:

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- ViewFieldID - a unique identifier used to reference a field. You can omit this field if you specify the ArtifactID or Name.

- ArtifactID - an integer representing a unique identifier for the field.

- Guids - an array of GUIDs identifying the field.

- Name - the user-friendly name of the field.

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
{

    "TotalCount": 3,

    "Objects": [

        {

            "ArtifactID": 1006066,

            "Values": [

                "Relativity Template"

            ]

        },

        {

            "ArtifactID": 1015644,

            "Values": [

                "Relativity"

            ]

        },

        {

            "ArtifactID": 1017451,

            "Values": [

                "Sample Client"

            ]

        }

    ],

    "IDWindow": [],

    "CurrentStartIndex": 1,

    "ResultCount": 3,

    "ObjectType": {

        "ArtifactID": 1016169,

        "Name": "Client",

        "Guids": [],

        "ArtifactTypeID": 5

    },

    "RankWindow": [],

    "Fields": [

        {

            "FieldCategory": "Generic",

            "FieldType": "FixedLengthText",

            "ViewFieldID": 21,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Name"

        }

    ]

}
```

### Query for users to add to a group

To query the users that can be added to a group, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}/eligible-members/query
```

View field descriptions for a request

The request contains the following fields:

- request - a request object with the following fields:

- Fields - an array containing the following fields:

- Name - the names or email addresses of users to query on.

- Condition - the search criteria used in the query. For more information, Query for resources . This field is optional.

- start - the values in the start and length fields both determine the page number being requested. For example, if you set length to 25 and start to record 17, Relativity interprets these setting as a request for the first page and returns audits 1-25. If you set start to 35, it returns the second page with audits 26-50.

- length - the number of items to return in the query result, beginning with index in the start field. See description for start field.

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
{

    "request": {

        "Fields": [

            {"Name": "Name"}

        ],

        "Condition": ""

    },

    "start": 1,

    "length": 1000

}
```

The response for this query contains the same fields as a response for a query on clients. See the descriptions in View field descriptions for a query response .

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
{

    "TotalCount": 2,

    "Objects": [

        {

            "ArtifactID": 1029457,

            "Values": [

                "user, test",

                "testuser@mydomain.com"

            ]

        },

        {

            "ArtifactID": 1029460,

            "Values": [

                "user, demo",

                "user@mydomain.com"

            ]

        }

    ],

    "IDWindow": [],

    "CurrentStartIndex": 1,

    "ResultCount": 2,

    "ObjectType": {

        "ArtifactID": 1016184,

        "Name": "User",

        "Guids": [],

        "ArtifactTypeID": 2

    },

    "RankWindow": [],

    "Fields": [

        {

            "FieldCategory": "Generic",

            "FieldType": "FixedLengthText",

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Full Name"

        },

        {

            "FieldCategory": "Generic",

            "FieldType": "FixedLengthText",

            "ViewFieldID": 37,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "E-mail Address"

        }

    ]

}
```

### Query for group members

To query for users that belong to a group, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/{groupArtifactID}/query-members
```

View field descriptions for a request

The request contains the following fields:

- request - a request object with the following fields:

- Fields - an array containing the following fields:

- Name - the names or email addresses of users to query on.

- Condition - the search criteria used in the query. For more information, Query for resources . This field is optional.

- start - the values in the start and length fields both determine the page number being requested. For example, if you set length to 25 and start to record 17, Relativity interprets these setting as a request for the first page and returns audits 1-25. If you set start to 35, it returns the second page with audits 26-50.

- length - the number of items to return in the query result, beginning with index in the start field. See description for start field.

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
{

    "request": {

        "Fields": [

            {"Name": "Full Name"},

            {"Name": "E-mail Address"}

        ],

        "Condition": ""

    },

    "start": 1,

    "length": 1000

}
```

View field descriptions for a response

The response contains the following fields:

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array contains objects with the following fields:

- ArtifactID - an integer representing a unique identifier for the object.

- Values - an array containing strings representing usernames and email addresses.

- IDWindow - reserved for future use.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - an object containing the following fields:

- ArtifactID - an integer representing a unique identifier for the object.

- Name - the user-friendly name of the object type.

- Guids - an array of GUIDs identifying the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- RankWindow - reserved for future use.

- Fields - an array of fields with the following properties:

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- ViewFieldID - a unique identifier used to reference a field. You can omit this field if you specify the ArtifactID or Name.

- ArtifactID - an integer representing a unique identifier for the field.

- Guids - an array of GUIDs identifying the field.

- Name - the user-friendly name of the field.

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
{

    "TotalCount": 2,

    "Objects": [

        {

            "ArtifactID": 1029457,

            "Values": [

                "user, test",

                "testuser@mydomain.com"

            ]

        },

        {

            "ArtifactID": 1029460,

            "Values": [

                "user, demo",

                "user@mydomain.com"

            ]

        }

    ],

    "IDWindow": [],

    "CurrentStartIndex": 1,

    "ResultCount": 2,

    "ObjectType": {

        "ArtifactID": 1016184,

        "Name": "User",

        "Guids": [],

        "ArtifactTypeID": 2

    },

    "RankWindow": [],

    "Fields": [

        {

            "FieldCategory": "Generic",

            "FieldType": "FixedLengthText",

            "ViewFieldID": 0,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "Full Name"

        },

        {

            "FieldCategory": "Generic",

            "FieldType": "FixedLengthText",

            "ViewFieldID": 37,

            "ArtifactID": 0,

            "Guids": [],

            "Name": "E-mail Address"

        }

    ]

}
```

### Query groups assigned to a user

To query the groups that are assigned to a user, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/query-by-user/{userID}
```

This query uses the same request and response fields as Query for group members .

## Mass operations on groups

You can use mass operations to add or remove multiple users to or from multiple groups in a single API call.

### Add multiple users to multiple groups

To add multiple users to multiple groups, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/members
```

View field descriptions for a request

The body of a request contains the following fields:

- Users - a list of objects describing the users to add. Each object contains the following field:

- ArtifactID - an integer representing a unique identifier for a user.

- Groups - a list of objects describing the groups. Each object contains the following field:

- ArtifactID - an integer representing a unique identifier for a group.

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

    "users": [

        { "ArtifactID": 1029457 },

        { "ArtifactID": 1029460 }

    ],

    "groups": [

        { "ArtifactID": 1029462 }

    ]

}
```

View field descriptions for a response

The response contains an array of objects with the following fields:

- Succeeded - a Boolean value indicating whether the operation was successful. The values for this field are true or false.

- Name - the user- friendly name of the group.

- ArtifactID - an integer representing a unique identifier for a group.

- Guids - an array of GUIDs identifying the group.

- Exception - describes an error encountered during this operation.

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
[

    {

        "Succeeded": true,

        "Name": "MyGroup",

        "ArtifactID": 1029462,

        "Guids": []

    }

]
```

### Remove multiple users from multiple groups

To remove multiple users from multiple groups, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/groups/members
```

View field descriptions for a request

The body of a request contains the following fields:

- Users - a list of objects describing the users to add. Each object contains the following field:

- ArtifactID - an integer representing a unique identifier for a user.

- Groups - a list of objects describing the groups. Each object contains the following field:

- ArtifactID - an integer representing a unique identifier for a group.

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

    "users": [

        { "ArtifactID": 1029457 },

        { "ArtifactID": 1029460 }

    ],

    "groups": [

        { "ArtifactID": 1029462 }

    ]

}
```

View field descriptions for a response

The response contains an array of objects with the following fields:

- Succeeded - a Boolean value indicating whether the operation was successful. The values for this field are true or false.

- Name - the user- friendly name of the group.

- ArtifactID - an integer representing a unique identifier for a group.

- Guids - an array of GUIDs identifying the group.

- Exception - describes an error encountered during this operation.

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
[

    {

        "Succeeded": true,

        "Name": "MyGroup",

        "ArtifactID": 1029462,

        "Guids": []

    }

]
```
