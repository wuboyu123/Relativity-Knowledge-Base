---
title: "Agent Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Infrastructure/Agent_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:24:30+00:00
sha256: 55de5327857e3a4071cddb6d893fb5ba27ad289d621d4793a0a18df30bf3831c
---

Agent Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Agent Manager (REST)

The Agent Manager service exposes multiple endpoints that you can use to programmatically manage agents in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations on agents.

- Provides helper endpoints used to retrieve agent types and agent servers. Use these endpoints to determine if a server supports the agent type that you want to add to it.

- Validation endpoints used to check whether an operation results in the number of agents exceeding the maximum or falling below the minimum limits. These endpoints are available for create, update, and delete operations. For example, you can check if adding an agent exceeds the maximum number allowed on a server.

Sample use cases for the Agent Manager service include:

- Adding new worker agents when multiple jobs are submitted to the OCR or Branding queues.

- Deleting worker agents that are unresponsive.

- Developing a custom monitoring tool for messages logged by agents.

You can also use the Agent Manager service through .NET. For more information, see Agent Manager (.NET) .

To implement your own custom agents, use the Agents API. For more information, see Agents .

Set the path parameters as follows:

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Agent Manager service. To download the sample file, click Agent Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Agent Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents
```

For the workspace identifier in the URL, use -1 to indicate the admin-level context. This value is required for all URLs in the Agent Manager service. For additional guidelines, see Agent Manager (.NET) .

You can use the following .NET code as a sample client for creating an agent. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Agent Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Initialize variables with the values for type of agent to create, and the server where it should be added.

- Set the url variable to the URL for creating an agent. For more information, see Create an agent .

- Set the JSON input required for the operation.

- Use the PostAsync() method to send a post request.

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
public async Task<int?> RetrieveArtifactViewFieldIdExample()

{

    int? result = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");

        var agentTypeId = 1015253;

        var agentServerId = 1016892;

        string inputJSON = $"{{\"AgentRequest\":{{ \"AgentType\": {{ \"Secured\": false, \"Value\": {{ \"ArtifactID\": \"{agentTypeId}\" }} }}, \"AgentServer\": {{ \"Secured\": false, \"Value\": {{ \"ArtifactID\": \"{agentServerId}\" }} }}, \"Enabled\": true, \"Interval\": 10, \"LoggingLevel\": 1, \"Keywords\": \"keywords\", \"Notes\": \"notes\" }} }}";

        var url = "/Relativity.REST/API/Relativity.Agents/workspace/-1/agents/";

        var response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<int>(content);

    }

    return result;

}
```

## Retrieve a list of agent types

Relativity supports a variety of agent types used for productions, OCR, Analytics, and other purposes. In addition, you can also implement custom agent types to meet the needs of your users. For more information, see Agents on the Relativity Documentation site .

To retrieve a list of agent types available in a Relativity instance, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agenttypes/
```

The request body is empty.

The response contains the following fields for each agent type returned in the array:

- ApplicationName - the name of the application associated with this agent type.

- CompanyName - the name of the company that implemented or provided the agent.

- DefaultInterval - indicates the number of seconds that the agent manager will wait between each agent execution. The default value varies by the agent type, and it is determined by the entity providing the agent.

- DefaultLoggingLevel - an integer value indicating the message type that the system logs in the Event Viewer. See Basic concepts for agents .

- ArtifactID - the Artifact ID of the agent type.

- Name - the user-friendly name for the agent type, such as Case Manager, File Deletion Manager, and so on.

View a partial JSON sample for a response Copy

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
[

    {

        "ApplicationName": "Default",

        "CompanyName": "Relativity ODA LLC",

        "DefaultInterval": 3600,

        "DefaultLoggingLevel": 1,

        "ArtifactID": 1015242,

        "Name": "Case Manager"

    },

    {

        "ApplicationName": "Default",

        "CompanyName": "Relativity ODA LLC",

        "DefaultInterval": 3600,

        "DefaultLoggingLevel": 1,

        "ArtifactID": 1015243,

        "Name": "File Deletion Manager"

    },

    {

        "ApplicationName": "Default",

        "CompanyName": "Relativity ODA LLC",

        "DefaultInterval": 3600,

        "DefaultLoggingLevel": 1,

        "ArtifactID": 1015244,

        "Name": "Case Statistics Manager"

    },

          ...

]
```

## Retrieve a list of agent servers

You can retrieve a list of all agent servers in a Relativity environment. However, if you want information about servers where you can add a specific agent type, see Retrieve servers compatible with a specific agent type .

To retrieve a list of agent servers, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agentservers
```

The request body is empty.

The response contains the following fields for each server returned in the array:

- Type - the particular function of a server in your Relativity environment, such as hosting agents.

- ProcessorCores - the number of cores that the server has.

- NumberOfAgents - the number of agents currently added to the server.

- ArtifactID - the Artifact ID of the server.

- Name - the user-friendly name of the server.

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
[

    {

        "Type": "Agent",

        "ProcessorCores": 4,

        "NumberOfAgents": 46,

        "ArtifactID": 1016922,

        "Name": "Agent Server One"

    },

    {

        "Type": "Agent",

        "ProcessorCores": 4,

        "NumberOfAgents": 34,

        "ArtifactID": 1016923,

        "Name": "Agent Server Two"

    },

    {

        "Type": "Agent",

        "ProcessorCores": 4,

        "NumberOfAgents": 37,

        "ArtifactID": 1016924,

        "Name": "Agent Server Three"

    },

    {

        "Type": "Web Background Processing",

        "ProcessorCores": 8,

        "NumberOfAgents": 3,

        "ArtifactID": 1016925,

        "Name": "Web Background One"

    },

    {

        "Type": "Web Background Processing",

        "ProcessorCores": 8,

        "NumberOfAgents": 3,

        "ArtifactID": 1016926,

        "Name": "Web Background Two"

    }

]
```

## Retrieve servers compatible with a specific agent type

You can retrieve a list of servers compatible with a specific agent type that you want to add to Relativity. However, if you want a list of all agent servers in your environment, see Retrieve a list of agent servers .

To retrieve a list of agent servers compatible with an agent type, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agenttypes/{AgentTypeID}/availableagentservers
```

Set {AgentTypeID} to the Artifact ID of the agent type.

The body of the request is empty.

The response contains the following fields for each server returned in the array:

- Type - the particular function of a server in your Relativity environment, such as hosting agents.

- ProcessorCores - the number of cores that the server has.

- NumberOfAgents - the number of agents currently added to the server.

- ArtifactID - the Artifact ID of the server.

- Name - the user-friendly name of the server.

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
[

    {

        "Type": "Agent",

        "ProcessorCores": 4,

        "NumberOfAgents": 46,

        "ArtifactID": 1016922,

        "Name": "Agent Server One"

    },

    {

        "Type": "Agent",

        "ProcessorCores": 4,

        "NumberOfAgents": 34,

        "ArtifactID": 1016923,

        "Name": "Agent Server Two"

    },

    {

        "Type": "Agent",

        "ProcessorCores": 4,

        "NumberOfAgents": 38,

        "ArtifactID": 1016924,

        "Name": "Agent Server Three"

    }

]
```

## Create an agent

Before creating an agent, you need to identify the agent type and a compatible server, and perform a validation check. For more information, see Sample workflow for adding agents .

To add a new agent to a Relativity environment, send a POST request to this URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/
```

The body of the request must contain the following fields unless specifically identified as optional:

- AgentRequest - represents a request for creating or updating an agent. It includes the following fields:

- AgentType - indicates the kind of job that the agent executes. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the agent type, such as a Branding Manager or Production Manager agent.

- AgentServer - the server where the agent is to be added. It has the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the server.

- Enabled - a Boolean value indicating whether the agent is running.

- Interval - indicates the number of seconds that the agent should wait before checking the database for available jobs. The default value varies by the agent type.

- LoggingLevel - an integer value indicating the message type that the system logs in the Event Viewer. See Basic concepts for agents .

- Keywords - optional words or phrases used to describe the agent.

- Notes - an optional description or other information about the agent.

- count - the number of agents to create. This field only required when you want to create more that one agent.

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
{

   "AgentRequest":{

      "AgentType":{

         "Secured":false,

         "Value":{

            "ArtifactID":"1015277"

         }

      },

      "AgentServer":{

         "Secured":false,

         "Value":{

            "ArtifactID":"1016924"

         }

      },

      "Enabled":true,

      "Interval":3600,

      "LoggingLevel":1,

      "Keywords":"",

      "Notes":""

   },

   "count":5

}
```

When the request is successful, the response contains the Artifact ID of the new agent, such as 2017104, or it contains a list of Artifacts for multiple agents. It also returns the status code of 200.

## Retrieve metadata for an agent

You can retrieve basic information about an agent or extended information, which also includes operations that you have permissions to perform on the agent.

- Retrieve basic metadata for an agent - send a GET request with a URL in the following general format: Copy

```text
1
<host>/relativity.rest/api/relativity.agents/workspace/-1/agents/{Agent ID}
```

- Retrieve extended metadata for an agent -send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/{Agent ID}/true/true
```

For both requests, set {Agent ID} to the Artifact ID of the agent that you want to read, and leave the bodies of the requests empty.

View the descriptions of the fields in the response

- AgentType - indicates the kind of job that the agent executes. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the agent type and its user-friendly name, such as a Branding Manager or Production Manager agent.

- AgentServer - the server where the agent is to be added. It has the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the server and its user-friendly name.

- Enabled - a Boolean value indicating whether the agent is running.

- Interval - indicates the number of seconds that the agent manager will wait between each agent execution. The default value varies by the agent type.

- LastUpdate - the date and time immediately before the most recent call to the execution method on the agent.

- LoggingLevel - an integer value indicating the minimum level of detail for agent messages logged to the Event Viewer. See Basic concepts for agents .

- Message - minimal information logged by an agent to Relativity. For more information, see Logging .

- DetailMessage - a comprehensive version of the message that the agent logged to Relativity.

- EventLevel - the event type of the last message that the agent logged to Relativity. For more information, see the AgentEventLevel enumeration in the Relativity.Services.Interfaces.Agent.Models namespace in the Class library reference .

- CreatedOn - the date and time when the agent was added to Relativity.

- CreatedBy - contains the Artifact ID and name of the user who created the agent.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the agent.

- LastModifiedOn - the date and time when the agent was most recently modified.

- Keywords - optional words or phrases used to describe the agent.

- Notes - an optional description or other information about the agent.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - a listed of fields not supported on the current instance of this agent type.

- ReadOnly - an array of agent properties that can't be modified, such its name or agent type.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this agent. For example, you may not have permissions to modify an agent that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the agent, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this agent.

- Reason - provides an explanation for the unavailability of an action.

- ArtifactID - the Artifact ID of the agent.

- Name - the user-friendly name for the agent.

View the JSON response for a basic metadata request Copy

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
{

    "AgentType": {

        "Secured": false,

        "Value": {

            "ArtifactID": 1015277,

            "Name": "Application Installation Manager"

        }

    },

    "AgentServer": {

        "Secured": false,

        "Value": {

            "ArtifactID": 1016924,

            "Name": "SS010AGT000001"

        }

    },

    "Enabled": true,

    "Interval": 3600,

    "LastUpdate": "2018-09-14T21:52:32.753",

    "LoggingLevel": 1,

    "Message": "Completed.",

    "DetailMessage": "",

    "EventLevel": "Informational",

    "CreatedOn": "2018-09-14T21:28:11.947",

    "CreatedBy": {

        "ArtifactID": 1023652,

        "Name": "Doe, Jane"

    },

    "LastModifiedBy": {

        "ArtifactID": 1023652,

        "Name": "Doe, Jane"

    },

    "LastModifiedOn": "2018-09-14T21:28:11.947",

    "Keywords": "",

    "Notes": "",

    "Actions": [],

    "ArtifactID": 2017104,

    "Name": "Application Installation Manager (7)"

}
```

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
{

    "AgentType": {

        "Secured": false,

        "Value": {

            "ArtifactID": 1015277,

            "Name": "Application Installation Manager"

        }

    },

    "AgentServer": {

        "Secured": false,

        "Value": {

            "ArtifactID": 1016924,

            "Name": "SS010AGT000001"

        }

    },

    "Enabled": true,

    "Interval": 3600,

    "LastUpdate": "2018-09-14T21:59:04.42",

    "LoggingLevel": 1,

    "Message": "Completed.",

    "DetailMessage": "",

    "EventLevel": "Informational",

    "CreatedOn": "2018-09-14T21:28:11.947",

    "CreatedBy": {

        "ArtifactID": 1023652,

        "Name": "Doe, Jane"

    },

    "LastModifiedBy": {

        "ArtifactID": 1023652,

        "Name": "Doe, Jane"

    },

    "LastModifiedOn": "2018-09-14T21:28:11.947",

    "Keywords": "",

    "Notes": "",

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "Name",

            "AgentType"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "Relativity.Agents/workspace/-1/agents/2017104",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "Relativity.Agents/workspace/-1/agents/2017104",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "ArtifactID": 2017104,

    "Name": "Application Installation Manager (7)"

}
```

## Update the properties of an agent

You can modify the properties of an agent, such as its run intervals, enabled property, and others. Additionally, you can also restrict the update of an agent to the date that it was last modified by adding the LastModifiedOn field to the request.

To update the properties of an agent, send a PUT request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/{Agent ID}
```

Set {Agent ID} to the Artifact ID of the agent that you want to update.

The request must contain the following fields unless specifically identified as optional:

- AgentRequest - represents a request for creating or updating an agent. It includes the following fields:

- AgentType - indicates the kind of job that the agent executes. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the agent type, such as a Branding Manager or Production Manager agent.

- AgentServer - the server where the agent is to be added. It has the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the server.

- Enabled - a Boolean value indicating whether the agent is running.

- Interval - indicates the number of seconds that the agent should wait before checking the database for available jobs. The default value varies by the agent type.

- LoggingLevel - an integer value indicating the message type that the system logs in the Event Viewer. See Basic concepts for agents .

- Keywords - optional words or phrases used to describe the agent.

- Notes - an optional description or other information about the agent.

- LastModifiedOn - the date and time when the agent was most recently modified. This field is only required if you want to restrict the update of an agent to the date that it was last modified. The value must match the LastModifiedOn date for the agent stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

   "AgentRequest":{

      "AgentType":{

         "Secured":true,

         "Value":{

         }

      },

      "AgentServer":{

         "Secured":true,

         "Value":{

         }

      },

      "Enabled":false,

      "Interval":3600,

      "LoggingLevel":1,

      "Keywords":"",

      "Notes":""

   },

   "LastModifiedOn":"2018-10-19T18:41:20.54"

}
```

When the agent is successfully updated, the response returns the status code of 200.

## Delete an agent

You can programmatically remove an agent from Relativity after it has finished executing, or you can remove it immediately by forcefully deleting it. When you forcefully delete an agent, the system doesn't wait for it to finish executing. In general, use a force delete when an agent has become unresponsive.

### Delete an agent

To remove an agent from Relativity after it has finished executing, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/{ToDelete}
```

Set {ToDelete} to the Artifact ID of the agent that you want to delete.

The body of the request is empty. When the agent is successfully deleted, the response returns the status code of 200.

### Forcefully delete an agent

To remove an agent from Relativity immediately, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/{ToDelete}
```

Set {ToDelete} to the Artifact ID of the agent. In the body of the request, set the force field to true.

Copy

```text
1
2
3
{

    "force" : true

}
```

When the agent is successfully deleted, the response returns the status code of 200.

## Validate a create, update, or delete operation

Before you attempt to add, update, or delete an agent, you can perform a check to verify the success of the operation. For detailed information, see Validation and compatibility checks .

Review the following information about agent validation:

- In Relativity, each agent type has a maximum or minimum number of required agents for an instance, server, or resource pool. The Agent Manager service provides validation endpoints that help you answer questions about whether the operation that you want to perform may result in exceeding the required number of agents. For example, Relativity permits only a single Case Manager agent. If you try to create a second agent, the API returns an error indicating that you have exceeded the limit.

- The validation methods on the Agent Manager service indicate whether the number of a specific agent type exceeds maximum limit or falls short of the minimum limit. It doesn't indicate the required limit for an agent type. To obtain this information, see Managing and setting Relativity agent quantity limitations on the Relativity Documentation site.

- Use the Object Manager service if you want to know the number of agents of a specific type that exist in your Relativity instance. For more information, see Object Manager (REST) .

### Validate a create operation

To verify that you can add an agent to a Relativity environment or server, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/validateinstancelimits
```

The request must contain the following fields unless specifically identified as optional:

- AgentRequest - represents a request for creating or updating an agent. It includes the following fields:

- AgentType - indicates the kind of job that the agent executes. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the agent type, such as a Branding Manager or Production Manager agent.

- AgentServer - the server where the agent is to be added. It has the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the server.

- Enabled - a Boolean value indicating whether the agent is running.

- Interval - indicates the number of seconds that the agent should wait before checking the database for available jobs. The default value varies by the agent type.

- LoggingLevel - an integer value indicating the message type that the system logs in the Event Viewer. See Basic concepts for agents .

- Keywords - optional words or phrases used to describe the agent.

- Notes - an optional description or other information about the agent.

- count - the number of agents that you want to add to the server.

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
{

    "AgentRequest" : {

        "AgentType": {

            "Secured": false,

            "Value": {

                "ArtifactID": "1015277"

        }

        },

        "AgentServer": {

            "Secured": false,

            "Value": {

                "ArtifactID": "1016924"

            }

        },

        "Enabled": true,

        "Interval": 3600,

        "LoggingLevel": 1,

        "Keywords": "",

        "Notes": ""

    },

    "count" : 1

}
```

If you can successfully add the agent, the response returns the status code of 200. Also, see Failed validation responses .

### Validate an update operation

To confirm that you can update the properties of an agent, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/{Agent ID}/validateinstancelimits
```

Set {Agent ID} to the Artifact ID of the agent.

The request must contain the following fields unless specifically identified as optional:

- AgentRequest - represents a request for creating or updating an agent. It includes the following fields:

- AgentType - indicates the kind of job that the agent executes. It includes the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID for the agent type, such as a Branding Manager or Production Manager agent.

- AgentServer - the server where the agent is to be added. It has the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID of the server.

- Enabled - a Boolean value indicating whether the agent is running.

- Interval - indicates the number of seconds that the agent should wait before checking the database for available jobs. The default value varies by the agent type.

- LoggingLevel - an integer value indicating the message type that the system logs in the Event Viewer. See Basic concepts for agents .

- Keywords - optional words or phrases used to describe the agent.

- Notes - an optional description or other information about the agent.

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
{

    "AgentRequest" : {

        "AgentType": {

            "Secured": true,

            "Value": {

            }

        },

        "AgentServer": {

            "Secured": true,

            "Value": {

            }

        },

        "Enabled": false,

        "Interval": 3600,

        "LoggingLevel": 1,

        "Keywords": "",

        "Notes": ""

    }

}
```

If you can successfully update the agent, the response returns the status code of 200. Also, see Failed validation responses .

### Validate a delete operation

To verify that you can delete an agent, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity.agents/workspace/-1/agents/{Agent ID}/validateinstancelimits
```

Set {Agent ID} to the Artifact ID of the agent.

The body of the request is empty. If you can successfully delete the agent, the response returns the status code of 200. Also, see Failed validation responses .

### Failed validation responses

When a validation check fails, the response varies depending on the reason for the failure. The AgentInstanceLimit enumeration contains constants that identify the reason for a failed validation check:

- MinPerEnvironment - the environment has the recommended minimum number of agent instances.

- MaxPerEnvironment - the environment has the maximum number of agent instances allowed.

- MinPerResourcePool - the resource pool has the recommended minimum number of agent instances.

- MinPerServer - the agent server has the recommended minimum number of agent instances.

- MaxPerServer - the agent server has the maximum number of agent instances allowed.

- LastPerEnvironment - the last instance of the agent type in the environment is being disabled or deleted.

The following examples illustrate possible JSON responses for validation checks:

- You perform a validation check for creating agent in an environment. The following response indicates that the environment already has the maximum number of agent instances allowed. Copy

```text
1
2
3
{

   "Limit":"MaxPerEnvironment"

}
```

- You perform a validation check for deleting an agent from a server. The following response indicates that the agent server has the minimum number of agent instances. In addition, it includes the Artifact ID and name of the server. Copy

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

   "Limit":"MinPerServer",

   "AgentServer":{

      "Secured":false,

      "Value":{

         "ArtifactID":"1016892",

         "Name":"Agent Server One"

      }

   }

}
```

For more information, see the AgentInstanceLimit enumeration in the Relativity.Services.Interfaces.Agent.Models namespace in the Class library reference .

On this page

- Agent Manager (REST)

- Postman sample file

- Client code sample

- Retrieve a list of agent types

- Retrieve a list of agent servers

- Retrieve servers compatible with a specific agent type

- Create an agent

- Retrieve metadata for an agent

- Update the properties of an agent

- Delete an agent

- Delete an agent

- Forcefully delete an agent

- Validate a create, update, or delete operation

- Validate a create operation

- Validate an update operation

- Validate a delete operation

- Failed validation responses


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
