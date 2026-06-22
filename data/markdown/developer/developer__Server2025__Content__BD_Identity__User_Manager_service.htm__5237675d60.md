---
title: "User Manager service"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/User_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:28:29+00:00
sha256: 2f2eb4792ccadbbb0e3b0763798e0b460aa64282523d4cf334b9092839bd562a
---

User Manager service Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# User Manager (REST)

You add users to a Relativity environment to provide individuals with access to it. After creating users, you can add them to groups and assign permissions to the groups in various workspaces. For more information, see Users in the Relativity Documentation site.

The User Manager API exposes endpoints that provide the following functionality:

- Supports CRUD operations on users.

- Helper endpoints for retrieving user types and groups to associate with users.

- Helper endpoints for retrieving and querying on lists of users.

As a sample use case, you might use this API to implement a custom tool for importing users into Relativity. You could retrieve user information for display in a custom application.

You can also use the User Manager service through .NET. For more information, see User Manager (.NET) .

## Guidelines for the User Manager service

Review the following guidelines for the User Manager service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to update a user:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1 .

- {userID} to the Artifact ID of the user.

## Client code sample

To use the User Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for creating a user.

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
public async Task<UserResponse> CreateUserAsync()

{

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("http://localhost/");



        string inputJSON = "{\"UserRequest\":{\"AllowSettingsChange\": true,\"Client\": {\"Secured\": false,\"Value\": {\"ArtifactID\": 1015644}},\"DefaultFilterVisibility\": true,\"DocumentViewerProperties\": {\"AllowDocumentSkipPreferenceChange\": true,\"AllowDocumentViewerChange\": true,\"AllowKeyboardShortcuts\": true,\"DefaultSelectedFileType\": \"Default\",\"DocumentViewer\": \"Default\",\"SkipDefaultPreference\": true},\"DisableOnDate\": null,\"EmailAddress\": \"test222@relativity.com\",\"EmailPreference\": \"Default\",\"FirstName\": \"First Name\",\"ItemListPageLength\": 50,\"LastName\": \"Last Name\",\"RelativityAccess\": true,\"SavedSearchDefaultsToPublic\": true,\"TrustedIPs\": \"\",\"Type\": {\"ArtifactID\": 663},\"Keywords\": \"\",\"Notes\": \"\"}}";

        string url = "/Relativity.REST/api/Relativity-Identity/{versionNumber}/users";

        HttpResponseMessage response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        string content = await response.Content.ReadAsStringAsync();

        return JsonConvert.DeserializeObject<UserResponse>(content);

    }

}
```

## Create a user

To create a new user, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users
```

To retrieve a list of available types to assign to a user, see Retrieve available types for users .

View field descriptions for a create request

The body of the request must contain a UserRequest object with the following fields:

- AllowSettingsChange - a Boolean value indicating whether the user can change a limited number of settings.

- Client - the client associated with the user. It contains these fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - contains the Artifact ID for the client.

- DefaultFilterVisibility - a Boolean value indicating whether filters on all columns are visible by default.

- DocumentViewerProperties - user properties that are related to the document viewer.

- AllowDocumentSkipPreferenceChange - a Boolean value indicating whether the user can change the preference to skip documents during review when they do not meet the original conditions of a view due to propagation.

- AllowDocumentViewerChange - a Boolean value indicating whether the user can change the document viewer modes.

- AllowKeyboardShortcuts - a Boolean value indicating whether the user can see the keyboard shortcuts icon in the core reviewer interface.

- DefaultSelectedFileType - the default viewer mode. See the DefaultSelectedFileType enumeration.

- DocumentViewer - the viewer that the user can access for reviewing documents. See the DocumentViewer enumeration .

- SkipDefaultPreference - a Boolean value indicating whether the user advances to the next document in the queue that matches the defined view conditions when the user clicks Save and Next.

- DisableOnDate - the date when Relativity access for the user is auto-disabled.

- EmailAddress - the user's email address in the format name@domain.extension.

- EmailPreference - the user's preference for email notifications when adding or deleting Users or Groups. See the EmailPreference enumeration .

- FirstName - the user's first name.

- ItemListPageLength - the default list length for all views in Relativity for the user.

- LastName - the user's last name.

- RelativityAccess - a Boolean value indicating whether the user can log in to Relativity and included in the billing under your Relativity license.

- SavedSearchDefaultsToPublic - a Boolean value indicating whether saved searches are public or private by default.

- TrustedIPs - an IP address or addresses that are valid locations where a user can log in.

- Type - contains the Artifact ID for the user's type. The default values are internal or external, but the Relativity UI supports adding any value. The type is used only for reference.

- Keywords - optional words or phrases used to describe the user.

- Notes - an optional description or other information about the user.

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
27
28
29
30
31
32
33
34
{

    "UserRequest":{

        "AllowSettingsChange": true,

        "Client": {

            "Secured": false,

            "Value": {

                "ArtifactID": 1015644

            }

        },

        "DefaultFilterVisibility": true,

        "DocumentViewerProperties": {

            "AllowDocumentSkipPreferenceChange": true,

            "AllowDocumentViewerChange": true,

            "AllowKeyboardShortcuts": true,

            "DefaultSelectedFileType": "Default",

            "DocumentViewer": "Default",

            "SkipDefaultPreference": true

        },

        "DisableOnDate": null,

        "EmailAddress": "email address",

        "EmailPreference": "Default",

        "FirstName": "First Name",

        "ItemListPageLength": 50,

        "LastName": "Last Name",

        "RelativityAccess": true,

        "SavedSearchDefaultsToPublic": true,

        "TrustedIPs": "",

        "Type": {

            "ArtifactID": 663

        },

        "Keywords": "",

        "Notes": ""

    }

}
```

View field descriptions for a create response

The response contains the following fields:

AllowSettingsChange - a Boolean value indicating whether the user can change a limited number of their settings.

- Client - the client associated with the user.

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name for the client.

- ArtifactID - the Artifact ID for the client.

- Guids - an array of GUIDs used to identify the client.

- DefaultFilterVisibility - a Boolean value indicating whether filters on all columns are visible by default.

- DocumentViewerProperties - user properties that are related to the document viewer.

- AllowDocumentViewerChange - a Boolean value indicating whether the user can change the document viewer modes.

- AllowKeyboardShortcuts - a Boolean value indicating whether the user can see the keyboard shortcuts icon in the core reviewer interface.

- AllowDocumentSkipPreferenceChange - a Boolean value indicating whether the user change the preference to skip documents during review that no longer meet the original conditions of a view due to propagation.

- DefaultSelectedFileType - the default viewer mode. See the DefaultSelectedFileType enumeration.

- DocumentViewer - the viewer that the user can access when reviewing documents. See the DocumentViewer enumeration .

- SkipDefaultPreference - a Boolean value indicating whether the user advances to the next document in the queue that matches the defined view conditions when the user clicks Save and Next.

- EmailAddress - the user's email address in the format name@domain.extension.

- EmailPreference - the user's preference for email notifications when adding or deleting Users or Groups. See the EmailPreference enumeration .

- FirstName - the user's first name.

- ItemListPageLength - the default list length for all views in Relativity for the user.

- LastName - the user's last name.

- RelativityAccess - a Boolean value indicating whether the user can log in to Relativity and bincluded in the billing under your Relativity license.

- SavedSearchDefaultsToPublic - a Boolean value indicating whether saved searches are public or private by default.

- TrustedIPs - an IP address or addresses that are valid locations where the user can log in.

- Type - contains the following fields. The default values are internal or external, but the Relativity UI supports adding any value. The type is used only for reference.

- Name - the user-friendly name for the type.

- ArtifactID - the Artifact ID for the type.

- Guids - an array of GUIDs used to identify the type.

- Keywords - optional words or phrases used to describe the user.

- Notes - an optional description or other information about the user.

- CreatedOn - the date and time when the user was added to Relativity.

- CreatedBy - contains the Artifact ID and name of the user who created the user.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the user.

- LastModifiedOn - the date and time when the user was most recently modified.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - a listed of fields not supported on the current instance of this user.

- ReadOnly - an array of user properties that cannot be modified.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this user. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the user, such as delete, update, and others.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this user.

- Reason - provides an explanation for the unavailability of an action.

- ArtifactID - the Artifact ID of the user.

- Guids - an array of GUIDs used to identify the user.

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
{

   "AllowSettingsChange":true,

   "Client":{

      "Secured":false,

      "Value":{

         "Name":"Relativity",

         "ArtifactID":1015644,

         "Guids":[



         ]

      }

   },

   "DefaultFilterVisibility":true,

   "DocumentViewerProperties":{

      "AllowDocumentViewerChange":true,

      "AllowKeyboardShortcuts":true,

      "AllowDocumentSkipPreferenceChange":true,

      "DefaultSelectedFileType":"Viewer",

      "DocumentViewer":"Default",

      "SkipDefaultPreference":true

   },

   "EmailAddress":"email address",

   "EmailPreference":"All",

   "FirstName":"First Name",

   "ItemListPageLength":50,

   "LastName":"Last Name",

   "RelativityAccess":true,

   "SavedSearchDefaultsToPublic":true,

   "TrustedIPs":"",

   "Type":{

      "Name":"Internal",

      "ArtifactID":663,

      "Guids":[



      ]

   },

   "Keywords":"",

   "Notes":"",

   "CreatedOn":"2020-04-29T20:04:24.617",

   "CreatedBy":{

      "Name":"Doe, Jane",

      "ArtifactID":1023652,

      "Guids":[



      ]

   },

   "LastModifiedBy":{

      "Name":"Doe, Jane",

      "ArtifactID":1023652,

      "Guids":[



      ]

   },

   "LastModifiedOn":"2020-04-29T20:04:24.617",

   "Meta":{

      "Unsupported":[



      ],

      "ReadOnly":[



      ]

   },

   "Actions":[

      {

         "Name":"Delete",

         "Href":"Relativity.Users/workspace/-1/users/1018403",

         "Verb":"DELETE",

         "IsAvailable":true,

         "Reason":[



         ]

      },

      {

         "Name":"Update",

         "Href":"Relativity.Users/workspace/-1/users/1018403",

         "Verb":"PUT",

         "IsAvailable":true,

         "Reason":[



         ]

      }

   ],

   "ArtifactID":1018403,

   "Guids":[



   ]

}
```

## Retrieve metadata for a user

To retrieve basic or extended metadata for a user, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID}?{includeMetadata:bool}&{includeActions:bool}
```

Extended metadata includes operations that you have permissions to perform on the user. Set the query parameters in the URL to true for extended metadata:

- includeMetadata

- includeActions

The request body is empty.

The response for a read operation contains many of the same fields as a response for a create operation. See the descriptions in View field descriptions for a create response .

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

   "AllowSettingsChange":true,

   "Client":{

      "Secured":false,

      "Value":{

         "Name":"Relativity",

         "ArtifactID":1015644,

         "Guids":[



         ]

      }

   },

   "DefaultFilterVisibility":true,

   "DocumentViewerProperties":{

      "AllowDocumentViewerChange":false,

      "AllowKeyboardShortcuts":true,

      "AllowDocumentSkipPreferenceChange":true,

      "DefaultSelectedFileType":"Viewer",

      "DocumentViewer":"Default",

      "SkipDefaultPreference":true

   },

   "EmailAddress":"test@t.com",

   "EmailPreference":"All",

   "FirstName":"1",

   "ItemListPageLength":25,

   "LastName":"1",

   "RelativityAccess":true,

   "SavedSearchDefaultsToPublic":false,

   "TrustedIPs":"",

   "Type":{

      "Name":"External",

      "ArtifactID":672,

      "Guids":[



      ]

   },

   "Keywords":"",

   "Notes":"",

   "CreatedOn":"2021-05-07T13:45:59.61",

   "CreatedBy":{

      "Name":"Allen, Rob",

      "ArtifactID":9,

      "Guids":[



      ]

   },

   "LastModifiedBy":{

      "Name":"Allen, Rob",

      "ArtifactID":9,

      "Guids":[



      ]

   },

   "LastModifiedOn":"2021-05-07T13:45:59.61",

   "Actions":[



   ],

   "ArtifactID":1017952,

   "Guids":[



   ]

}
```

## Retrieve settings for the current user

To retrieve settings or extended metadata for the current user, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/me/settings?{includeMetadata:bool}&{includeActions:bool}
```

Extended metadata includes operations that you have permissions to perform on the user. Set the query parameters in the URL to true for extended metadata:

- includeMetadata

- includeActions

The request body is empty..

View field descriptions for a response

The response contains the following fields:

- Actions - an array of Action objects indicating operations that you have permissions to perform on this user. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the user, such as delete, update, and others.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this user.

- Reason - provides an explanation for the unavailability of an action.

- DefaultFilterVisibility - a Boolean value indicating whether filters on all columns are visible by default.

- DefaultSelectedFileType - the default viewer mode. See the DefaultSelectedFileType enumeration.

- EmailAddress - the user's email address in the format name@domain.extension.

- EmailPreference - the user's preference for email notifications when adding or deleting Users or Groups. See the EmailPreference enumeration .

- FirstName - the user's first name.

- ItemListPageLength - the default list length for all views in Relativity for the user.

- LastName - the user's last name.

- SavedSearchDefaultsToPublic - a Boolean value indicating whether saved searches are public or private by default.

- SkipDefaultPreference - a Boolean value indicating whether the user advances to the next document in the queue that matches the defined view conditions when the user clicks Save and Next.

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
{

   "Actions":[



   ],

   "DefaultFilterVisibility":true,

   "DefaultSelectedFileType":"Default",

   "EmailAddress":"rob.allen@example.com",

   "EmailPreference":"All",

   "FirstName":"Rob",

   "ItemListPageLength":25,

   "LastName":"Allen",

   "SavedSearchDefaultsToPublic":false,

   "SkipDefaultPreference":false

}
```

## Update properties for a user

To update the properties of a user, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID}
```

You can restrict the update of a user to the date that it was last modified by adding the LastModifiedOn field to the request.

The request for an update operation contains the same fields as a request for a create operation. See the descriptions in View field descriptions for a create request .

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
27
28
29
30
31
32
33
34
{

   "UserRequest":{

      "AllowSettingsChange":true,

      "Client":{

         "Secured":false,

         "Value":{

            "ArtifactID":1015644

         }

      },

      "DefaultFilterVisibility":true,

      "DocumentViewerProperties":{

         "AllowDocumentSkipPreferenceChange":true,

         "AllowDocumentViewerChange":true,

         "AllowKeyboardShortcuts":true,

         "DefaultSelectedFileType":"Default",

         "DocumentViewer":"Default",

         "SkipDefaultPreference":true

      },

      "DisableOnDate":null,

      "EmailAddress":"email address",

      "EmailPreference":"Default",

      "FirstName":"First Name",

      "ItemListPageLength":50,

      "LastName":"Last Name",

      "RelativityAccess":true,

      "SavedSearchDefaultsToPublic":true,

      "TrustedIPs":"",

      "Type":{

         "ArtifactID":663

      },

      "Keywords":"",

      "Notes":""

   }

}
```

The response for an update operation contains many of the same fields as a response for a create operation. See the descriptions in View field descriptions for a create response .

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

   "AllowSettingsChange":true,

   "Client":{

      "Secured":false,

      "Value":{

         "Name":"Relativity",

         "ArtifactID":1015644,

         "Guids":[



         ]

      }

   },

   "DefaultFilterVisibility":true,

   "DocumentViewerProperties":{

      "AllowDocumentViewerChange":false,

      "AllowKeyboardShortcuts":true,

      "AllowDocumentSkipPreferenceChange":true,

      "DefaultSelectedFileType":"Viewer",

      "DocumentViewer":"Default",

      "SkipDefaultPreference":true

   },

   "EmailAddress":"test@t.com",

   "EmailPreference":"All",

   "FirstName":"1",

   "ItemListPageLength":25,

   "LastName":"1",

   "RelativityAccess":true,

   "SavedSearchDefaultsToPublic":false,

   "TrustedIPs":"",

   "Type":{

      "Name":"External",

      "ArtifactID":672,

      "Guids":[



      ]

   },

   "Keywords":"",

   "Notes":"",

   "CreatedOn":"2021-05-07T13:45:59.61",

   "CreatedBy":{

      "Name":"Allen, Rob",

      "ArtifactID":9,

      "Guids":[



      ]

   },

   "LastModifiedBy":{

      "Name":"Allen, Rob",

      "ArtifactID":9,

      "Guids":[



      ]

   },

   "LastModifiedOn":"2021-05-07T13:45:59.61",

   "Actions":[



   ],

   "ArtifactID":1017952,

   "Guids":[



   ]

}
```

## Update settings for the current user

To update the settings for the current user, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/me/settings
```

You can restrict the settings update to the date that it was last modified by adding the LastModifiedOn field to the request.

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

- UserSettingRequest - represents a request updating the settings of the current user. It includes the following fields:

- DefaultFilterVisibility - a Boolean value indicating whether filters on all columns are visible by default.

- DefaultSelectedFileType - the default viewer mode. See the DefaultSelectedFileType enumeration.

- EmailAddress - the user's email address in the format name@domain.extension.

- EmailPreference - the user's preference for email notifications when adding or deleting Users or Groups. See the EmailPreference enumeration .

- FirstName - the user's first name.

- ItemListPageLength - the default list length for all views in Relativity for the user.

- LastName - the user's last name

- SavedSearchDefaultsToPublic - a Boolean value indicating whether saved searches are public or private by default.

- SkipDefaultPreference - a Boolean value indicating whether the user advances to the next document in the queue that matches the defined view conditions when the user clicks Save and Next.

- LastModifiedOn - the date and time when the user was most recently modified. This field is only required if you want to restrict the update of a user to the date that it was last modified. The value must match the LastModifiedOn date for the user stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

   "UserSettingRequest":{

      "DefaultFilterVisibility":true,

      "DefaultSelectedFileType":"Default",

      "EmailAddress":"rob.allen@example.com",

      "EmailPreference":"All",

      "FirstName":"Rob",

      "ItemListPageLength":25,

      "LastName":"Allen",

      "SavedSearchDefaultsToPublic":false,

      "SkipDefaultPreference":false

   }

}
```

View field descriptions for a response

The response contains the following fields:

- Actions - an array of Action objects indicating operations that you have permissions to perform on this user. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the user, such as delete, update, and others.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this user.

- Reason - provides an explanation for the unavailability of an action.

- DefaultFilterVisibility - a Boolean value indicating whether filters on all columns are visible by default.

- DefaultSelectedFileType - the default viewer mode. See the DefaultSelectedFileType enumeration.

- EmailAddress - the user's email address in the format name@domain.extension.

- EmailPreference - the user's preference for email notifications when adding or deleting Users or Groups. See the EmailPreference enumeration .

- FirstName - the user's first name.

- ItemListPageLength - the default list length for all views in Relativity for the user.

- LastName - the user's last name.

- SavedSearchDefaultsToPublic - a Boolean value indicating whether saved searches are public or private by default.

- SkipDefaultPreference - a Boolean value indicating whether the user advances to the next document in the queue that matches the defined view conditions when the user clicks Save and Next.

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
{

    "Actions": [

        {

            "Name": "Delete",

            "Href": "Relativity.Users/workspace/-1/users/1018403",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "Relativity.Users/workspace/-1/users/1018403",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "DefaultFilterVisibility": true,

    "DefaultSelectedFileType": "LongText",

    "EmailAddress": "email address",

    "EmailPreference": "All",

    "FirstName": "Updated First Name",

    "ItemListPageLength": 10,

    "LastName": "Updated Last Name",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Client",

            "Email Address"

        ]

    },

    "SavedSearchDefaultsToPublic": false,

    "SkipDefaultPreference": false

}
```

## Delete a user

To remove a user from Relativity, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID}
```

The request body is empty.

When the user is successfully deleted, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

## Helper endpoints for querying on users

The User Manager service exposes multiple helper endpoints that you can use to query for information about users. See the following sections:

- Retrieve available types for users

- Query for groups to associate with users

- Retrieve information about the current user

- Retrieve all users in a workspace

- Retrieve active users in a workspace

- Retrieve users in workspace with Relativity access

- Query for users in a workspace

### Retrieve available types for users

To retrieve available types for users, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/available-types
```

The default values are internal or external, but the Relativity UI supports adding any value. The type is used only for reference.

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- Name - the name of the user type.

- ArtifactID - the Artifact ID of the user type.

- Guids - an array of GUIDs used to identify the user type.

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
[

   {

      "Name":"Internal",

      "ArtifactID":663,

      "Guids":[



      ]

   },

   {

      "Name":"External",

      "ArtifactID":672,

      "Guids":[



      ]

   }

]
```

### Query for groups to associate with users

Use this endpoint to query for groups to which you can add one or more of the specified users. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/query-eligible-groups
```

View field descriptions for a request

The JSON request should contain the following information:

- Users - a list of users by ArtifactID.

- Request - a query request object containing conditions, sorting order, and other information for the query.

- Condition - conditional query statement.

- Sorts - result sorting statement.

- Start - index of the first artifact in the returned result set.

- Length - number of items to return in the result, starting with index in the start parameter.

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
{

   "Users":[

      {

         "ArtifactID":9

      }

   ],

   "Request":{

      "Condition":"",

      "Sorts":[

         {

            "FieldIdentifier":{

               "Name":"Name"

            },

            "Direction":"Ascending"

         }

      ]

   },

   "Start":0,

   "Length":25

}
```

View field descriptions for a response

The response contains the following fields:

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array of groups containing these fields:

- ArtifactID - the Artifact ID of a group.

- IDWindow - reserved for future use.

- CurrentStartIndex - index of the first artifact in the returned result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount field.

- ObjectType - contains the following fields:

- ArtifactID - the Artifact ID of the object type.

- Name - the user-friendly name of the object type.

- Guids - an array of GUIDs used to identify the object type.

- RankWindow - reserved for future use.

- Fields - an array of fields associated with the results.

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
{

   "TotalCount":6,

   "Objects":[

      {

         "ArtifactID":1015025,

         "Values":[



         ]

      },

      {

         "ArtifactID":1015028,

         "Values":[



         ]

      },

      {

         "ArtifactID":1015029,

         "Values":[



         ]

      },

      {

         "ArtifactID":1015030,

         "Values":[



         ]

      },

      {

         "ArtifactID":1015026,

         "Values":[



         ]

      },

      {

         "ArtifactID":1015027,

         "Values":[



         ]

      }

   ],

   "IDWindow":[



   ],

   "CurrentStartIndex":0,

   "ResultCount":6,

   "ObjectType":{

      "ArtifactID":1016185,

      "Name":"Group",

      "Guids":[



      ],

      "ArtifactTypeID":3

   },

   "RankWindow":[



   ],

   "Fields":[



   ]

}
```

### Retrieve information about the current user

To retrieve information about the current user, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/workspaces/{workspaceID}/users/me
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- FirstName - the first name of the user.

- LastName - the last name of the user.

- ItemListPageLength - an integer indicating the length of the item list page for the user.

- ShowFilters - a Boolean value indicating whether the filters should be displayed for the user.

- CreatedOn - the date and time when the user was created.

- AclUserID - an integer representing the AclUserID that determines user permissions.

- ArtifactID - the Artifact ID for the user.

- Name - the full name of user.

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
{

    "FirstName": "Rob",

    "LastName": "Allen",

    "ItemListPageLength": 25,

    "ShowFilters": true,

    "CreatedOn": "2007-01-01T00:00:00",

    "AclUserID": 9,

    "ArtifactID": 9,

    "Name": "Allen, Rob"

}
```

### Retrieve all users in a workspace

To retrieve a list of all users in a workspace, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/workspaces/{workspaceID}/all-users?{includeDeleted:bool}
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- LoggedInUserID - the ID of the current logged in user.

- ActiveUsers - an array of user identifier objects containing these fields:

- ArtifactID - the Artifact ID of a user.

- Name - the full name of a user.

- Email - the email of a user.

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
{

   "LoggedInUserID":9,

   "ActiveUsers":[

      {

         "ArtifactID":1017952,

         "Name":"1, 1"

      },

      {

         "ArtifactID":9,

         "Name":"Allen, Rob"

      },

      {

         "ArtifactID":777,

         "Name":"Sidney, Robin"

      }

   ]

}
```

### Retrieve active users in a workspace

To retrieve a list of active users in a workspace, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/workspaces/{workspaceID}/active-users?{includeCurrentUser:int}&{enforceChoiceLimitForUI:bool}
```

If the number of returned users exceeds the ChoiceLimitForUI setting, no users are returned.

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- LoggedInUserID - the ID of the current logged in user.

- ActiveUsers - an array of user identifier objects containing these fields:

- ArtifactID - the Artifact ID of a user.

- Name - the full name of a user.

- Email - the email of a user.

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
{

   "LoggedInUserID":9,

   "ActiveUsers":[

      {

         "ArtifactID":1017952,

         "Name":"1, 1"

      },

      {

         "ArtifactID":9,

         "Name":"Allen, Rob"

      },

      {

         "ArtifactID":777,

         "Name":"Sidney, Robin"

      }

   ]

}
```

### Retrieve users in workspace with Relativity access

To retrieve users in a workspace with Relativity access, send a GET request to the following service URL:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/workspaces/{workspaceID}/users-with-access
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- LoggedInUserID - the ID of the current logged in user.

- ActiveUsers - an array of user identifier objects containing these fields:

- ArtifactID - the Artifact ID of a user.

- Name - the full name of a user.

- Email - the email of a user.

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
{

    "LoggedInUserID": 9,

    "ActiveUsers": [

        {

            "ArtifactID": 9,

            "Name": "Allen, Rob"

        },

        {

            "ArtifactID": 777,

            "Name": "Sidney, Robin"

        },

        {

            "ArtifactID": 1017952,

            "Name": "1, 1"

        }

    ]

}
```

### Query for users in a workspace

To query for users in a workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/workspaces/{workspaceID}/query-users
```

View field descriptions for a request

The JSON request should contain the following information:

- Query - a query request object containing conditions, sorting order, and other information for the query. For more information, see Query for resources .

- Condition - conditional query statement.

- Sort - result sorting statement.

- Start - the index of the first item return in the result set.

- Length - the number of items to return in the result, starting with index in the start parameter.

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
{

    "Query":{

        "Condition":"'FullName' LIKE ['John']",

        "Sort":[

            {

                "FieldIdentifier":{

                    "Name":"FullName"

                },

                "Direction":"Ascending"

            }

            ]

    },

    "Start":0,

    "Length":25

}
```

View field descriptions for a response

The response contains the following fields unless specifically identified as optional:

- DataResults - a list of objects containing user information.

- ArtifactID - the Artifact ID of the user.

- FullName - the full name of the user.

- Email - the email of the user.

- ResultCount - the number of objects returned by the current query.

- TotalResultCount - the total number of objects in Relativity that meet the criteria of the query. Due to paging, this count may be larger than the number of objects returned in the ResultCount property.

- CurrentStartIndex - the index of the first artifact in the result set.

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
{

    "DataResults": [

        {

            "ArtifactID": 102125,

            "FullName": "Doe, John",

            "Email": "jdoe@gmail.com"

        },

        {

            "ArtifactID": 102123,

            "FullName": "Lee, John",

            "Email": "john email 2"

        },

        {

            "ArtifactID": 103123,

            "FullName": "Johnson, John",

            "Email": "john email 3"

        }

    ],

    "ResultCount": 3,

    "TotalResultCount": 3,

    "CurrentStartIndex": 0

}
```

On this page

- User Manager (REST)

- Guidelines for the User Manager service

- URLs

- Client code sample

- Create a user

- Retrieve metadata for a user

- Retrieve settings for the current user

- Update properties for a user

- Update settings for the current user

- Delete a user

- Helper endpoints for querying on users

- Retrieve available types for users

- Query for groups to associate with users

- Retrieve information about the current user

- Retrieve all users in a workspace

- Retrieve active users in a workspace

- Retrieve users in workspace with Relativity access

- Query for users in a workspace


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
