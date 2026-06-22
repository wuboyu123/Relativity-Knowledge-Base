---
title: "Choice Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Choice_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:25:44+00:00
sha256: ea5c545af2b3dd95bdeccd802f2f54d7a4c029d1facff27d19b78332cb2b0645
---

Choice Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Choice Manager (REST)

In Relativity, choices are predetermined values of single and multi-choice list fields. You can perform operations on admin and workspace choices. For more general information, see Choices in the Relativity Documentation site.

The Choice Manager service exposes multiple operations you can use to programmatically manage choices in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations and mass operations on choices.

- Provides helper endpoints used to sort choices, move choices in lists, and retrieve highlight colors and parent choices or fields.

As a sample use case, you could use the Choice Manager API to create choices used to perform specific operations in a custom application.

You can also use the Choice Manager API through .NET. For more information, see Choice Manager (.NET) .

## Guidelines for the Choice Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a choice:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/{ChoiceID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1.

- {workspaceID} to the Artifact ID of the workspace containing the choice.

- {choiceID} to the Artifact ID of the choice.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Choice Manager service. To download the sample file, click Choice Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

You can use the following .NET code as a sample client for creating a choice.

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
public async Task<int> CreateChoiceRestAsync()

{



    int choiceID = 0;

    using (Relativity.ObjectModel.V1.Choice.IChoiceManager choiceManager = _serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Choice.IChoiceManager>())

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("<user login>:<user password>")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("http://localhost/");



        string inputJSON = @"{""choiceRequest"":{""Field"":{""ArtifactID"":1104632,""Guids"":[]},""Name"":""Relevant"",""Color"":3,""Order"":100}}";

        string url = "/Relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/1022092/choices";

        HttpResponseMessage response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        string content = await response.Content.ReadAsStringAsync();

        choiceID = Int32.Parse(content);

    }



    return choiceID;

}
```

## Create a single choice

To create a choice, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices
```

View field descriptions for a request

The request must contain a choiceRequest object with the following fields:

- Field - identifiers for the field to associated with the new choice. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for a field.

- Guids - an array of GUIDs used to identify a field.

- Name - a string representing the user-friendly name of the choice.

- Color - the highlight color for the choice.

- Order - an integer used to determine order in which multiple choices are listed in UI. Lower values are listed first.

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

    "choiceRequest": {

        "Field": {

            "ArtifactID": 1104632,

            "Guids": []

        },

        "Name": "Relevant",

        "Color": 3,

        "Order": 100

    }

}
```

The response contains the Artifact ID of the created choice.

## Mass create choices

To create multiple choices in a mass operation, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices
```

View field descriptions for a request

The request must contain a massCreateChoiceRequest object with the following fields:

- Choices - an array of choice names. This field sets the for the new choices and contains the names of the choices.

- ChoiceTemplateData - contains information used to create the choices as follows:

- Field - the identifiers for a field to be associated with the choices:

- ArtifactID - an integer representing a unique identifier for the field.

- Guids - an array of GUIDs used to identify the field.

View a JSON request Copy

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

    "massCreateChoiceRequest": {

        "Choices": [

            {

                "Name": "Important",

                "Children": [

                    {

                        "Name": "Critical"

                    },

                    {

                        "Name": "Very"

                    },

                    {

                        "Name": "Somewhat"

                    }

                ]

            }

        ],

        "ChoiceTemplateData": {

            "Field": {

                "ArtifactID": 1104635,

                "Guids": []

            }

        }

    }

}
```

View field descriptions for a response

The response contains the following fields:

- ChoicesCreated - an array of choices that were added. It contains the following fields for each choice:

- ObjectIdentifier - containing the following fields:

- Name - a string representing the user-friendly name of the choice.

- ArtifactID - an integer representing a unique identifier for a choice.

- Guids - an array of GUIDs used to identify a choice.

- ParentChoice - containing the following fields:

- ArtifactID - an integer representing a unique identifier for a parent choice.

- Guids - an array of GUIDs used to identify a parent choice.

- Success - a Boolean value indicating whether the move succeeded.

- Message - explanatory information for an error when one occurs.

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
{

    "ChoicesCreated": [

        {

            "ObjectIdentifier": {

                "Name": "Important",

                "ArtifactID": 1104660,

                "Guids": []

            },

            "ParentChoice": {

                "ArtifactID": 0,

                "Guids": []

            }

        },

        {

            "ObjectIdentifier": {

                "Name": "Critical",

                "ArtifactID": 1104661,

                "Guids": []

            },

            "ParentChoice": {

                "ArtifactID": 1104660,

                "Guids": []

            }

        },

        {

            "ObjectIdentifier": {

                "Name": "Very",

                "ArtifactID": 1104662,

                "Guids": []

            },

            "ParentChoice": {

                "ArtifactID": 1104660,

                "Guids": []

            }

        },

        {

            "ObjectIdentifier": {

                "Name": "Somewhat",

                "ArtifactID": 1104663,

                "Guids": []

            },

            "ParentChoice": {

                "ArtifactID": 1104660,

                "Guids": []

            }

        }

    ],

    "Success": true,

    "Message": ""

}
```

## Read a choice

To retrieve the metadata for a choice, send a GET request with a URL in the following format (to list the choices for a field, see Object Rule Manager service ):

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/{ChoiceID}
```

The request body is empty.

View field descriptions for a response

The request contains the following fields:

- ObjectIdentifier - containing the following fields:

- Name - a string representing the user-friendly name of the choice.

- ArtifactID - an integer representing a unique identifier for a choice.

- Guids - an array of GUIDs used to identify a choice.

- Field - identifiers for the field to associated with the choice. It contains the following fields:

- Name - a string representing the user-friendly name of the field.

- ArtifactID - an integer representing a unique identifier for a field.

- Guids - an array of GUIDs used to identify a field.

- Order - an integer used to determine order in which multiple choices are listed in UI. Lower values are listed first.

- Color - contains the following field:

- ID - an integer representing the highlight color for the choice.

- Parent - identifiers for the parent associated with the choice. It contains the following fields:

- ArtifactID - an integer representing a unique identifier for the parent.

- Guids - an array of GUIDs used to identify the parent.

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
{

    "ObjectIdentifier": {

        "Name": "Critical",

        "ArtifactID": 1104661,

        "Guids": []

    },

    "Field": {

        "Name": "Multi choice test field",

        "ArtifactID": 1104635,

        "Guids": []

    },

    "Order": 1000,

    "Color": {

        "ID": 3

    },

    "Parent": {

        "ArtifactID": 1104660,

        "Guids": []

    }

}
```

## Update a choice without a version check

To update a choice without a version check, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/{ChoiceID}
```

View field descriptions for a request

The request contains choiceRequest object with the following fields:

- Name - a string representing the user-friendly name of the choice.

- Color - the highlight color for the choice.

- Parent - identifiers for the parent associated with the choice. It contains the following fields:

- Name - a string representing the user-friendly name of the parent.

- ArtifactID - an integer representing a unique identifier for the parent.

- Guids - an array of GUIDs used to identify the parent.

- Order - an integer used to determine order in which multiple choices are listed in UI. Lower values are listed first.

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

    "choiceRequest": {

        "Name": "Critical - 2",

        "Color": 3,

        "Parent": {

            "Name": "Important",

            "ArtifactID": 1104636,

            "Guids": []

        },

        "Order": 1000

    }

}
```

When the choice is update successfully, the response contains a status code of 200.

## Update a choice with a version check

To update a choice with a version check, send a PUT request with a URL in the following format::

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/{ChoiceID}
```

View field descriptions for a request

The request contains a choiceRequest object with the following fields:

- Name - a string representing the user-friendly name of the choice.

- Color - the highlight color for the choice.

- Parent - identifiers for the parent associated with the choice. It contains the following fields:

- Name - a string representing the user-friendly name of the parent.

- ArtifactID - an integer representing a unique identifier for the parent.

- Guids - an array of GUIDs used to identify the parent.

- Order - an integer used to determine order in which multiple choices are listed in UI. Lower values are listed first.

- objectVersionToken - the version token of the choice being updated.

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

    "choiceRequest": {

        "Name": "Critical - 3",

        "Color": 3,

        "Parent": {

            "Name": "Important",

            "ArtifactID": 1104636,

            "Guids": []

        },

        "Order": 400

    },

    "objectVersionToken": "637499580733130000"

}
```

When the choice is update successfully, the response contains a status code of 200.

## Mass update choices

To update multiple choices in a mass operation, send a PUT request with a URL in the following format

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices
```

All choices in a mass update request must be associated with the same field.

View field descriptions for a request

The request contains a massUpdateChoices object with an array of the following fields:

- ObjectIdentifier - containing the following fields:

- ArtifactID - an integer representing a unique identifier for a choice.

- Name - a string representing the user-friendly name of the choice.

- Color - an integer representing the highlight color for the choice.

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
{

    "massUpdateChoices": [

        {

            "ObjectIdentifier": {

                "ArtifactID": 1104662,

            },

            "Name": "Relevant",

            "Color": 3

        },

        {

            "ObjectIdentifier": {

                "ArtifactID": 1104663,

            },

            "Name": "Confidential",

            "Color": 3

        }

    ]

}
```

View field descriptions for a response

The response contains the following fields:

- TotalChoices - an integer indicating the number of choices affected.

- Success - a Boolean value indicating whether the operation succeeded.

- Message - explanatory information for an error when one occurs.

View a sample JSON response Copy

```text
1
2
3
4
5
{

    "TotalChoices":2,

    "Success":true,

    "Message":""

}
```

## Delete a choice

To remove a choice from Relativity, send a DELETE request with a URL in the following format::

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/{ChoiceID}
```

When the choice is deleted successfully, the response contains a status code of 200.

## Mass delete choices

To remove multiple choices in a mass operation, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices
```

View field descriptions for a request

The request contains the following fields:

- massDeleteRequest - a request object with the following field:

- ChoiceIDs - an array of Artifact IDs for the choices to delete.

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

    "massDeleteRequest": {

        "ChoiceIDs": [

            {

                "ArtifactID": 1104661,

            },

            {

                "ArtifactID": 1104662,

            },

            {

                "ArtifactID": 1104663,

            }

        ]

    }

}
```

View field descriptions for a response

The request contains the following fields:

- TotalChoices - an integer indicating the number of choices affected.

- Success - a Boolean value indicating whether the operation succeeded.

- Message - explanatory information for an error when one occurs.

View a sample JSON response Copy

```text
1
2
3
4
5
{

    "TotalChoices":3,

    "Success":true,

    "Message":""

}
```

When the choices are deleted successfully, the response contains a status code of 200.

## Sort choices

To sort choices, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/sort
```

View field descriptions for a request

The request contains the following fields:

- fieldID - the Artifact ID of the field associated with the choices being sorted.

- sortType - a SortDirection enum indicating how to sort the choices:

- Ascending

- Descending

View a sample JSON request for alphabetically sorting choices Copy

```text
1
2
3
4
{

    "fieldID": 1104635,

    "sortType": "Ascending"

}
```

View field descriptions for a response

The response contains the following fields:

- TotalChoices - an integer indicating the number of choices sorted.

- Success - a Boolean value indicating whether the move succeeded.

View a sample JSON response Copy

```text
1
2
3
4
{

    "TotalChoices": 16,

    "Success": true

}
```

## Move choices to the beginning or end of a list

To move choices to the beginning or end of a list, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/move
```

View field descriptions for a request

The request contains the following fields:

- fieldID - the Artifact ID of the field associated with the choices being moved.

- choiceObjectIdentifiers - contains the following fields:

- ArtifactID - an integer representing a unique identifier for a choice.

- Guids - an array of GUIDs used to identify a choice.

- moveListTo - a ChoiceMoveType enum indicating where to move the choice in the list:

- Beginning

- End

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
{

    "fieldID": 1104635,

    "choiceObjectIdentifiers": [

        {

            "ArtifactID": 1104638,

            "Guids": []

        },

        {

            "ArtifactID": 1104637,

            "Guids": []

        }

    ],

    "moveListTo": "End"

}
```

View field descriptions for a response

The response contains the following fields:

- TotalChoices - an integer indicating the number of choices affected.

- Success - a Boolean value indicating whether the operation succeeded.

- Message - explanatory information for an error when one occurs.

View a sample JSON response Copy

```text
1
2
3
4
5
{

    "TotalChoices":0,

    "Success":true,

    "Message":""

}
```

## Move choices after a specific choice in a list

To move choices after a specific choice in a list, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/move
```

View field descriptions for a request

The request contains the following fields:

- fieldID - the Artifact ID of the field associated with the choices being moved.

- choiceObjectIdentifiers - contains the following fields:

- ArtifactID - an integer representing a unique identifier for a choice.

- Guids - an array of GUIDs used to identify a choice.

- choiceID - contains the following fields:

- ArtifactID - an integer representing a unique identifier for a choice.

- Guids - an array of GUIDs used to identify a choice.

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
{

    "fieldID": 1104635,

    "choiceObjectIdentifiers": [

        {

            "ArtifactID": 1104638,

            "Guids": []

        },

        {

            "ArtifactID": 1104637,

            "Guids": []

        }

    ],

    "choiceID": {

        "ArtifactID": 1104651,

        "Guids": []

    }

}
```

View field descriptions for a response

The response contains the following fields:

- TotalChoices - an integer indicating the number of choices affected.

- Success - a Boolean value indicating whether the operation succeeded.

- Message - explanatory information for an error when one occurs.

View a sample JSON response Copy

```text
1
2
3
4
5
{

    "TotalChoices":0,

    "Success":true,

    "Message":""

}
```

## Retrieve a list of available parents

You can retrieve a list of parents for a choice or a field.

### Retrieve a list of parents for a choice

To retrieve a list of available parents for a choice, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/{ChoiceID}/parents
```

The request body is empty.

View field descriptions for a response

The response contains an array of identifier objects with the following fields:

- Name - the user-friendly name for the parent.

- ArtifactID - an integer representing a unique identifier for a parent.

- Guids - an array of GUIDs used to identify a parent.

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
[

    {

        "Name": "Important",

        "ArtifactID": 1104636,

        "Guids": []

    },

    {

        "Name": "Very",

        "ArtifactID": 1104637,

        "Guids": []

    },

    {

        "Name": "Somewhat",

        "ArtifactID": 1104638,

        "Guids": []

    },

    ...

    {

        "Name": "Privileged",

        "ArtifactID": 1104640,

        "Guids": []

    },

]
```

### Retrieve a list of parents for a field

To retrieve a list of available parents for a specific field, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/parents
```

View field descriptions for a request

The request contains a field identifier object with the following fields:

- ArtifactID - an integer representing a unique identifier for the field.

- Guids - an array of GUIDs used to identify the field.

View a sample JSON request Copy

```text
1
2
3
4
5
6
{

    "fieldIdentifier": {

        "ArtifactID":1104635,

        "Guids":[]

    }

}
```

View field descriptions for a response

The response contains an array of identifier objects with the following fields:

- Name - the user-friendly name for the parent.

- ArtifactID - an integer representing a unique identifier for a parent.

- Guids - an array of GUIDs used to identify a parent.

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
[

    {

        "Name": "Important",

        "ArtifactID": 1104636,

        "Guids": []

    },

    {

        "Name": "Very",

        "ArtifactID": 1104637,

        "Guids": []

    },

    {

        "Name": "Somewhat",

        "ArtifactID": 1104638,

        "Guids": []

    },

    ...

    {

        "Name": "Privileged",

        "ArtifactID": 1104640,

        "Guids": []

    },

]
```

## Retrieve a list of available colors

To retrieve a list of available colors for highlighting a choice, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/choices/colors
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- Name - a user-friendly name for the color.

- ID - the identifier for the color.

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
[

    {

        "Name": "Green",

        "ID": 3

    },

    {

        "Name": "Gray",

        "ID": 12

    },

    {

        "Name": "Blue",

        "ID": 13

    },

    {

        "Name": "Orange",

        "ID": 14

    },

    {

        "Name": "Tan",

        "ID": 15

    }

]
```

On this page

- Choice Manager (REST)

- Guidelines for the Choice Manager service

- URLs

- Postman sample file

- Client code sample

- Create a single choice

- Mass create choices

- Read a choice

- Update a choice without a version check

- Update a choice with a version check

- Mass update choices

- Delete a choice

- Mass delete choices

- Sort choices

- Move choices to the beginning or end of a list

- Move choices after a specific choice in a list

- Retrieve a list of available parents

- Retrieve a list of parents for a choice

- Retrieve a list of parents for a field

- Retrieve a list of available colors


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
