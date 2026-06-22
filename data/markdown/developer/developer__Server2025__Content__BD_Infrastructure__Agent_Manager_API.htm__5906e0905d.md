---
title: "Agent Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Infrastructure/Agent_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:31+00:00
sha256: e0fe0c636dceb3d7bf80b7ca95119be067e5c1a09cdbe21670752c3d7a057410
---

Agent Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Agent Manager (.NET)

In Relativity, agents are process managers and workers that run in the background to complete jobs scheduled in your environment. For general information, see Agents on the Relativity Documentation site.

The Agent Manager API exposes multiple operations that you can use to programmatically manage agents in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations on agents.

- Provides helper methods used to retrieve agent types and agent servers. Use these methods to determine if a server supports the agent type that you want to add to it.

- Validation methods used to check whether an operation results in the number of agents exceeding the maximum or falling below the minimum limits. These methods are available for create, update, and delete operations. For example, you can check if adding an agent exceeds the maximum number allowed on a server.

Sample use cases for the Agent Manager service include:

- Adding new worker agents when multiple jobs are submitted to the OCR or Branding queues.

- Deleting worker agents that are unresponsive.

- Developing a custom monitoring tool for messages logged by agents.

You can also use the Agent Manager service through the REST API. For more information, see Agent Manager (REST) .

To implement your own custom agents, use the Agents API. For more information, see Agents .

## Fundamentals for managing agents

Review the following information to learn about the methods, classes, and other entities used by the Agent Manager service.

### Methods

In the Relativity Services API, the Relativity.Services.Interfaces.Agent namespace contains the IAgentManager interface that exposes the following methods:

- CreateAsync() method - adds a new agent to a Relativity environment. It returns the Artifact ID of the new agent. See Create an agent .

- CreateAsync() method - adds a new agent to a Relativity environment. This overloaded method also supports adding multiple agents in a single call by passing integer specifying the number of agents to create. It returns the Artifact ID of the new agent, or a list of Artifact IDs when you add multiple agents. See Create an agent .

- DeleteAsync() method - removes an agent from Relativity. This overloaded method supports deleting an agent after it finishes executing or deleting it immediately. See Delete an agent .

- GetAgentServersAsync() method - retrieves a list of all agent servers in a Relativity environment. It returns a list of AgentServerResponse objects. See Retrieve a list of agent servers .

- GetAgentTypesAsync() method - retrieves a list of agent types. It returns a list of AgentTypeResponse objects. See Retrieve a list of agent types .

- GetAvailableAgentServersAsync() method - retrieves a list of agent servers compatible with a specific agent type. This overloaded method takes the Artifact ID of a workspace, and the Artifact ID or GUID of an agent type. It returns a list of AgentServerResponse objects. See Retrieve servers compatible with a specific agent type .

- ReadAsync() method - retrieves information about an agent, including its type, logging level, enabled property, and others. You can also use this overloaded method to return extended metadata, including information about the operations that you have permissions to perform on the agent, such as update or delete. See Retrieve metadata for an agent .

- UpdateAsync() method - modifies the properties of an agent, such as its run intervals, enabled property, and others. You can use also this overloaded method to restrict the update of an agent based on the date that it was last modified. See Update the properties of an agent .

- ValidateCreateInstanceLimitAsync() method - indicates whether adding a new agent exceeds the limits for the agent type in a Relativity environment or server. It returns an AgentInstanceLimitResult object if a limit is exceeded. See Validate a create, update, or delete operation .

- ValidateDeleteInstanceLimitAsync() method - indicates whether deleting an agent violates the lower limit for an agent type in a Relativity environment, resource pool, or server. It returns an AgentInstanceLimitResult object if the number is outside the limit. See Validate a create, update, or delete operation .

- ValidateUpdateInstanceLimitAsync() method - indicates whether modifying an agent exceeds the limits for the agent type in a Relativity environment, resource pool, or server. It returns an AgentInstanceLimitResult object if a limit is exceeded. See Validate a create, update, or delete operation .

### Classes and enumerations

The Relativity.Services.Interfaces.Agent.Models namespace contains the following classes and enumerations used by the Agent Manager API:

- AgentInstanceLimitResult class - represents information about an agent type limit that has been violated.

- AgentRequest class - represents the data used to create or update an agent. The CreateAsync() and UpdateAsync() methods take an object of this type. Its properties include the agent type, agent server, enabled setting, and others.

- AgentResponse class - represents the results of a read operation. Its properties include the agent type, agent server, enabled setting, and others.

- AgentServerResponse class - represents information about an agent server, including its Artifact ID, name, number of agents running on the server, number of cores, and other properties. The GetAgentServersAsync() and GetAvailableAgentServersAsync() methods return objects of this type.

- AgentTypeResponse class - represents information about an agent type, including Artifact ID, name, logging level, and other properties. The GetAgentTypesAsync() method returns an object of this type.

- AgentEventLevel enumeration - indicates the minimum level of detail for agent messages logged to the Event Viewer.

- AgentInstanceLimit enumeration - Indicates when a minimum or maximum limit for agents allowed in an Relativity environment, server, or resource pool has been violated. See Failed validation responses .

## Guidelines for the Agent Manager service

Review the following guidelines for working with the Agent Manager service.

### Admin-level context

The methods on the Agent Manager API require that you pass an integer representing a workspace ID. You must pass -1 to indicate the admin-level context. This value is required as an argument for all methods on the Agent Manager API.

### Validation and compatibility checks

Relativity has minimum and maximum limits on the number of agents in an environment, server, or resource pool. These limits vary by agent type. For general information, see Managing and setting Relativity agent quantity limitations on the Relativity Documentation site.

You can use the validation methods on the Agent Manager service to verify that a create, update, or delete operation doesn't violate these limits. Validation checks have the following behavior:

- A check for a minimum limit is a warning. The action can be completed.

- A check for a maximum limit results in error. The attempted action is denied.

For more information, see Validate a create, update, or delete operation .

Additionally, an agent server may host only specific agent types. The Agent Manager service provides the GetAvailableAgentServersAsync() method that you can use to retrieve a list of servers compatible with an agent type. See Retrieve servers compatible with a specific agent type .

### Sample workflow for adding agents

You can use the following sample workflow to add agents to your Relativity environment.

- Retrieve a list of agent types available in a Relativity environment. See Retrieve a list of agent types .

- Retrieve a list of agent servers that support the agent type to add. You can only create some types of agent on specific agent server types. See Retrieve servers compatible with a specific agent type

- Perform a validation check to verify that you can add the agent without breaking any limits set for it. Call the ValidateCreateInstanceLimitAsync() method before attempting to add the new agent. See Validate a create operation .

- Review the response from the validation check:

- If no error occurs, add the agent. See Create an agent .

- If an error occurs, review Failed validation responses .

### Monitor enabled agents

The following code sample illustrates how to monitor enabled agents. You call the AgentRestart() method by passing an instance of the IAgentManager proxy, and the Artifact ID of the agent that you want to monitor.

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
public async Task AgentRestart(Relativity.Services.Interfaces.Agent.IAgentManager manager, int agentArtifactID)

{

    //Read in agent.

    Relativity.Services.Interfaces.Agent.Models.AgentResponse agentResponse = await manager.ReadAsync(-1, agentArtifactID);



    if (!agentResponse.Enabled)

    {

        Relativity.Services.Interfaces.Agent.Models.AgentRequest enabledAgentRequest = new AgentRequest(agentResponse);



        enabledAgentRequest.Enabled = true;



        await manager.UpdateAsync(-1, agentArtifactID, enabledAgentRequest);

    }

}
```

## Retrieve a list of agent types

Relativity supports a variety of agent types used for productions, OCR, Analytics, and other purposes. In addition, you can also implement custom agent types to meet the needs of your users. For more information, see Agents on the Relativity Documentation site.

The following code sample illustrates how to call the GetAgentTypesAsync() method by passing -1 to indicate the admin-level context.

The AgentTypeResponse object contains a Guids property, which contains the GUIDs associated with the agent type. This information isn't available through REST.

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
public static async Task GetAgentTypes_Async()

{

    int workspaceId = -1;

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            List<AgentTypeResponse> response = await agentManager.GetAgentTypesAsync(workspaceId);

            foreach (AgentTypeResponse agentType in response)

            {

                string info = string.Format("Read agent type {0} with Artifact ID {1}", agentType.Name, agentType.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve a list of agent servers

You can retrieve a list of all agent servers in a Relativity environment. However, if you want information about servers where you can add a specific agent type, see Retrieve servers compatible with a specific agent type .

The following code sample illustrates how to call the GetAgentServersAsync() method by passing -1 to indicate the admin-level context.

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
public static async Task GetAgentServers_Async()

{

    int workspaceId = -1;

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            List<AgentServerResponse> response = await agentManager.GetAgentServersAsync(workspaceId);

            foreach (AgentServerResponse agentServer in response)

            {

                string info = string.Format("Read agent server {0} with Artifact ID {1}", agentServer.Name, agentServer.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve servers compatible with a specific agent type

You can retrieve a list of servers compatible with a specific agent type that you want to add to Relativity. However, if you want a list of all agent servers in your environment, see Retrieve a list of agent servers .

The following code sample illustrates how to call the GetAvailableAgentServersAsync() method by passing -1 to indicate the admin-level context.

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
public static async Task GetAvailableAgentServers_Async()

{

    int workspaceId = -1;

    int agentTypeId = 1015253;

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            List<AgentServerResponse> response = await agentManager.GetAgentServersAsync(workspaceId, agentTypeId);

            foreach (AgentServerResponse agentServer in response)

            {

                string info = string.Format("Read agent server {0} with Artifact ID {1}", agentServer.Name, agentServer.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Create an agent

Before creating an agent, you need to identify the agent type and a compatible server, and perform a validation check. For more information, see Sample workflow for adding agents .

The following code sample illustrates how to use the CreateAsync() method to add a single agent. It passes -1 to indicate the admin-level context, and the Artifact ID of the agent type and the server.

The CreateAsync() method is overloaded, so you can also use it to add multiple agents in a single call by passing integer specifying the number of agents to create.

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
public static async Task Create_Async()

{

    int workspaceId = -1;

    int agentTypeId = 1015253;

    int agentServerId = 1016892;

    AgentRequest request = new AgentRequest

    {

        Enabled = true,

        Interval = 10,

        Keywords = "keywords",

        Notes = "notes",

        LoggingLevel = 1,

        AgentType = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentTypeId }),

        AgentServer = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentServerId })

    };

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            int newAgentArtifactId = await agentManager.CreateAsync(workspaceId, request);

            string info = string.Format("Created agent with Artifact ID {0}", newAgentArtifactId);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve metadata for an agent

Use the overloaded ReadAsync() method to retrieve basic metadata for an agent or extended metadata, which includes information about the operations that you have permissions to perform on this agent.

The following code sample illustrates how to call the ReadAsync() method by passing -1 to indicate the admin-level context, and the Artifact ID of the agent. If you want to return additional information, use the overloaded method by passing Boolean values set to true for additional metadata and permissions.

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
public static async Task Read_Async()

{

    int workspaceId = -1;

    int agentArtifactId = 1016911;

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            AgentResponse response = await agentManager.ReadAsync(workspaceId, agentArtifactId);

            string info = string.Format("Read agent {0} with Artifact ID {1}", response.Name, response.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update the properties of an agent

Use the UpdateAsync() method to modify the properties of an agent. The following code samples illustrates how to call this method by passing -1 to indicate the admin-level context, the Artifact ID of the agent, and an AgentRequest object.

Additionally, you can also restrict the update of an agent to the date that it was last modified by passing the value of LastModifiedOn property as an argument to the overloaded UpdateAsync() method.

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
public static async Task Update_Async()

{

    int workspaceId = -1;

    int agentArtifactId = 1016911;

    int agentTypeId = 1015253;

    int agentServerId = 1016892;

    AgentRequest request = new AgentRequest

    {

        Enabled = true,

        Interval = 5,

        Keywords = "updated keywords",

        Notes = "updated notes",

        LoggingLevel = 5,

        AgentType = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentTypeId }),

        AgentServer = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentServerId })

    };

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            await agentManager.UpdateAsync(workspaceId, agentArtifactId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete an agent

You can programmatically remove an agent from Relativity after it has finished executing, or you can remove it immediately by forcefully deleting it. When you forcefully delete an agent, the system doesn't wait for it to finish executing. In general, use a force delete when an agent has become unresponsive.

Pass the Artifact IDs of the workspace and agent to the overloaded DeleteAsync() when you want to remove the agent after it finishes executing as illustrated in the following code sample. To remove the agent immediately, pass the Artifact IDs of the workspace and agent, and a Boolean value of true to the method.

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
public static async Task Delete_Async()

{

    int workspaceId = -1;

    int agentArtifactId = 1016911;

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            await agentManager.DeleteAsync(workspaceId, agentArtifactId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Validate a create, update, or delete operation

Before you attempt to add, update, or delete an agent, you can perform a check to verify the success of the operation. For general information, see Validation and compatibility checks .

Review the following information about agent validation:

- In Relativity, each agent type has a maximum or minimum number of required agents for an instance, server, or resource pool. The Agent Manager API provides validation methods that help you answer questions about whether the operation that you want to perform may result in exceeding the required number of agents. For example, Relativity permits only a single Case Manager agent. If you try to create a second agent, the API returns an error indicating that you have exceeded the limit.

- The validation methods on the Agent Manager API indicate whether the number of a specific agent type exceeds maximum limit or falls short of the minimum limit. It doesn't indicate the required limit for an agent type. To obtain this information, see Managing and setting Relativity agent quantity limitations on the Relativity Documentation site.

- Use the Object Manager API if you want to know the number of agents of a specific type that exist in your Relativity instance. For more information, see Object Manager (.NET) .

### Validate a create operation

Use the ValidateCreateInstanceLimitAsync() method to check whether the addition of a new agent exceeds the maximum number allowed.

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
public static async Task ValidateCreateInstanceLimit_Async()

{

    int workspaceId = -1;

    int agentTypeId = 1015253;

    int agentServerId = 1016892;

    int agentsToCreate = 2;

    AgentRequest request = new AgentRequest

    {

        Enabled = true,

        Interval = 10,

        Keywords = "keywords",

        Notes = "notes",

        LoggingLevel = 1,

        AgentType = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentTypeId }),

        AgentServer = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentServerId })

    };

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            List<AgentInstanceLimitResult> result = await agentManager.ValidateCreateInstanceLimitAsync(workspaceId, request, agentsToCreate);

            foreach (AgentInstanceLimitResult instanceLimit in result)

            {

                string info = string.Format("Create limit broken: {0}", instanceLimit.Limit.ToString());

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Validate an update operation

Use the ValidateUpdateInstanceLimitAsync() method to check whether the updating the number of agents exceeds the maximum number allowed.

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
public static async Task ValidateUpdateInstanceLimit_Async()

{

    int workspaceId = -1;

    int agentArtifactId = 1016911;

    int agentTypeId = 1015253;

    int agentServerId = 1016892;

    AgentRequest request = new AgentRequest

    {

        Enabled = true,

        Interval = 5,

        Keywords = "updated keywords",

        Notes = "updated notes",

        LoggingLevel = 5,

        AgentType = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentTypeId }),

        AgentServer = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = agentServerId })

    };

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            List<AgentInstanceLimitResult> result = await agentManager.ValidateUpdateInstanceLimitAsync(workspaceId, agentArtifactId, request);

            foreach (AgentInstanceLimitResult instanceLimit in result)

            {

                string info = string.Format("Update limit broken: {0}", instanceLimit.Limit.ToString());

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Validate a delete operation

Use the ValidateDeleteInstanceLimitAsync method to check whether the removal of an agent violates the minimum number of agents required.

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
public static async Task ValidateDeleteInstanceLimit_Async()

{

    int workspaceId = -1;

    int agentArtifactId = 1016911;

    using (Services.Interfaces.Agent.IAgentManager agentManager = serviceFactory.CreateProxy<Services.Interfaces.Agent.IAgentManager>())

    {

        try

        {

            List<AgentInstanceLimitResult> result = await agentManager.ValidateDeleteInstanceLimitAsync(workspaceId, agentArtifactId);

            foreach (AgentInstanceLimitResult instanceLimit in result)

            {

                string info = string.Format("Delete limit broken: {0}", instanceLimit.Limit.ToString());

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Failed validation responses

When a validation check fails, the response varies depending on the reason for the failure. The AgentInstanceLimit enumeration contains constants that identify the reason for a failed validation check:

- MinPerEnvironment - the environment has the recommended minimum number of agent instances.

- MaxPerEnvironment - the environment has the maximum number of agent instances allowed.

- MinPerResourcePool - the resource pool has the recommended minimum number of agent instances.

- MinPerServer - the agent server has the recommended minimum number of agent instances.

- MaxPerServer - the agent server has the maximum number of agent instances allowed.

- LastPerEnvironment - the last instance of the agent type in the environment is being disabled or deleted.

For more information, see the AgentInstanceLimit enumeration in the Relativity.Services.Interfaces.Agent.Models namespace in the Class library reference .

On this page

- Agent Manager (.NET)

- Fundamentals for managing agents

- Methods

- Classes and enumerations

- Guidelines for the Agent Manager service

- Admin-level context

- Validation and compatibility checks

- Sample workflow for adding agents

- Monitor enabled agents

- Retrieve a list of agent types

- Retrieve a list of agent servers

- Retrieve servers compatible with a specific agent type

- Create an agent

- Retrieve metadata for an agent

- Update the properties of an agent

- Delete an agent

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
