---
title: "Event Handler Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Event_Handler_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:26:05+00:00
sha256: 4056ae11d0eb8563ea88c2bab27ca263ff5185beb1ef52c88418b2267f976b48
---

Event Handler Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Event Handler Manager (REST)

You can add custom behavior to an object type by attaching event handlers to it. For example, you might attach an event handler that performs a specific action when a user makes an update to an object and then attempts to save it. For more information, see Develop object type event handlers .

The Event Handler Manager service contains an endpoints for programmatically attaching event handlers to an object type, and for detaching them. It also provides helper endpoints that you can use for the following purposes:

- To retrieve a list of event handlers in a workspace, which could be attached to a specific object type.

- To retrieve a list of event handlers currently attached to an object type.

This API supports the same functionality through .NET. For more information, see Event Handler Manager (.NET) .

## Postman sample files

You can use the Postman sample files to become familiar with making calls to endpoints. To download the sample files, click EventHandlerPostmanFile .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Event Handler Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/relativity.rest/api/Relativity.objectTypes/workspace/{{WorkspaceID}}/objectTypes/
```

You can use the following .NET code as a sample client for creating an object type. This code illustrates how to perform the following tasks:

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
public async Task<int?> Create()

{

    int? result = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");

        int workspaceId = 1018486;

        int parentArtifactTypeId= 10;

        int parentArtifactId = 1035231;

        int applicationId = 1035699;

        string inputJSON = $"{{ \"ObjectTypeRequest\" : {{ \"ParentObjectType\": {{ \"Secured\": false, \"Value\": {{ \"ArtifactTypeID\": \"{parentArtifactTypeId}\", \"ArtifactID\": \"{parentArtifactId}\" }} }}, \"RelativityApplications\":[ {{ \"Secured\": false, \"Value\":{{ \"ArtifactID\": \"{applicationId}\" }} }} ], \"Name\": \"Object Test 1\", \"CopyInstancesOnCaseCreation\": false, \"CopyInstancesOnParentCopy\": false, \"EnableSnapshotAuditingOnDelete\": true, \"PersistentListsEnabled\": false, \"PivotEnabled\": true, \"SamplingEnabled\": false, \"Keywords\": \"\", \"Notes\": \"\" }} }}";

        var url = $@"/Relativity.rest/api/relativity.objectTypes/workspace/{workspaceId}/objectTypes/";

        var response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<int>(content);

    }



    return result;

}
```

## Attach an event handler to an object type

To attach an event handler to an object type, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity.objectTypes/workspace/{{WorkspaceArtifactID}}/objectTypes/{{ObjectTypeArtifactID}}/eventhandlers/{{EventHandlerID}}
```

Set the variables in the URL as follows:

- {{WorkspaceArtifactID}} - the Artifact ID of the workspace that contains the object type.

- {{ObjectTypeArtifactID}} - the Artifact ID of the object type that you want to attach the event handler to.

- {{EventHandlerID}} - the ID of the event handler.

The {{EventHandlerID}} is an identifier assigned by Relativity to the event handler. This identifier isn't the Artifact ID for the event handler. The endpoints for retrieving attached or available event handlers return a field that contains this ID. See Retrieve event handlers attached to an object type or Retrieve available event handlers for an object type .

The body of the request is empty. When the request is successful, the response returns the status code of 200.

## Detach an event handler from an object type

To detach an event handler from an object type, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity.objectTypes/workspace/{{WorkspaceArtifactID}}/objectTypes/{{ObjectTypeArtifactID}}/eventhandlers/{{EventHandlerID}}
```

Set the variables in the URL as follows:

- {{WorkspaceArtifactID}} - the Artifact ID of the workspace that contains the object type.

- {{ObjectTypeArtifactID}} - the Artifact ID of the object type that you want to detach the event handler from.

- {{EventHandlerID}} - the ID of the event handler.

The {{EventHandlerID}} is an identifier assigned by Relativity to the event handler. This identifier isn't the Artifact ID for the event handler. The endpoints for retrieving attached or available event handlers return a field that contains this ID. See Retrieve event handlers attached to an object type or Retrieve available event handlers for an object type .

The body of the request is empty. When the request is successful, the response returns the status code of 200.

## Retrieve event handlers attached to an object type

To retrieve a list of event handlers attached to an object type, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity.objectTypes/workspace/{{WorkspaceArtifactID}}/objectTypes/{{ObjectTypeArtifactID}}/eventhandlers
```

Set the variables in the URL as follows:

- {{WorkspaceArtifactID}} - the Artifact ID of the workspace that contains the object type.

- {{ObjectTypeArtifactID}} - the Artifact ID of the object type that has attached event handlers to retrieve.

The body of the request is empty.

The response contains multiple fields, such as the Artifact ID of the event handler, name, and others. If no event handlers are available for the object type, this endpoint returns an empty array.

View the descriptions of fields in the response

- ID - the reference ID of the event handler assigned by Relativity.

- ArtifactID - the artifact ID of the object type.

- Execution - the type of event handler, such as Console, Post Save, and others. For more information, see the EventHandlerExecution enumeration in the Class library reference , and Develop object type event handlers .

- Application - an application that contains the event handler. This field contains the following:

- Name - the user-friendly name for the application.

- ArtifactID - the Artifact ID of the application.

- Guids - an array of GUIDs used to identify the application.

- AssemblyName - the name of the .NET assembly containing the event handler code.

- ClassName - the name of the class that defines the event handler.

- CompanyName - the name of the company that implemented or provided the event handler.

- Description - general information about the event handler.

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
[

    {

        "ID": 20565,

        "ArtifactID": 1042543,

        "Execution": "PreSave",

        "Application": {

            "Name": "Default",

            "ArtifactID": 0,

            "Guids": [

                "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

            ]

        },

        "AssemblyName": "myassembly.dll",

        "ClassName": "myassembly.MyPreSave",

        "CompanyName": "",

        "Description": ""

    }

]
```

## Retrieve available event handlers for an object type

To retrieve a list of event handlers available in a workspace to attach to a specific object type, send a GET request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity.objectTypes/workspace/{{WorkspaceArtifactID}}/objectTypes/{{ObjectTypeArtifactID}}/availableeventhandlers
```

Set the variables in the URL as follows:

- {{WorkspaceArtifactID}} - the Artifact ID of the workspace that contains the object type.

- {{ObjectTypeArtifactID}} - the Artifact ID of the object type that you want to retrieve a list of available event handlers for.

The body of the request is empty.

The response contains multiple fields, such as the Artifact ID of the event handler, name, and others. If no event handlers are available for the object type, this endpoint returns an empty array.

View the descriptions of fields in the response

- ID - the reference ID of the event handler assigned by Relativity.

- ArtifactID - the artifact ID of the object type.

- Execution - the type of event handler, such as Console, Post Save, and others. For more information, see the EventHandlerExecution enumeration in the Class library reference , and Develop object type event handlers .

- Application - an application that contains the event handler. This field contains the following:

- Name - the user-friendly name for the application.

- ArtifactID - the Artifact ID of the application.

- Guids - an array of GUIDs used to identify the application.

- AssemblyName - the name of the .NET assembly containing the event handler code.

- ClassName - the name of the class that defines the event handler.

- CompanyName - the name of the company that implemented or provided the event handler.

- Description - general information about the event handler.

View a JSON sample listing available event handlers Copy

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
[

   {

      "ID":20564,

      "ArtifactID":0,

      "Execution":"PreSave",

      "Application":{

         "Name":"Default",

         "ArtifactID":0,

         "Guids":[

            "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

         ]

      },

      "AssemblyName":"testEH.dll",

      "ClassName":"testEH.REHEPreSave",

      "CompanyName":"",

      "Description":""

   },

   {

      "ID":20566,

      "ArtifactID":0,

      "Execution":"PreSave",

      "Application":{

         "Name":"Default",

         "ArtifactID":0,

         "Guids":[

            "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

         ]

      },

      "AssemblyName":"testEHg.dll",

      "ClassName":"testEHg.REHEPreSave",

      "CompanyName":"",

      "Description":""

   },

   {

      "ID":20565,

      "ArtifactID":0,

      "Execution":"PreSave",

      "Application":{

         "Name":"Default",

         "ArtifactID":0,

         "Guids":[

            "3e86b18f-8b55-45c4-9a57-9e0cbd7baf46"

         ]

      },

      "AssemblyName":"myassembly.dll",

      "ClassName":"myassembly.MyPreSave",

      "CompanyName":"",

      "Description":""

   }

]
```

On this page

- Event Handler Manager (REST)

- Postman sample files

- Client code sample

- Attach an event handler to an object type

- Detach an event handler from an object type

- Retrieve event handlers attached to an object type

- Retrieve available event handlers for an object type


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
