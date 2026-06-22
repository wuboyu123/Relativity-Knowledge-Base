---
title: "Basic concepts for agents"
url: https://platform.relativity.com/Server2025/Content/Background_processing/Basic_concepts_for_agents.htm
collection: developer
fetched_at: 2026-06-22T06:30:59+00:00
sha256: e5e76ebbad765bf44293719ba140a384601cddc79cd925ba467753a0c8a97a68
---

Basic concepts for agents

# Basic concepts for agents

Review these basic concepts to learn more about implementing agents, uploading them to Relativity, logging events, and other agent functionality.

## Common implementation tasks for agents

Complete these common implementation tasks when developing custom agents. You can also use a template to create an agent. For more information, see Visual Studio templates for Relativity .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler, Relativity.Api, and Relativity.Agent packages.

- Inherit from the kCura.Agent.AgentBase class – ensure that your agent extends this base class.

- Set the CustomAttribute.Name attribute – specify a name for the agent that you want displayed in the Relativity UI.

- Add a GUID for the agent – set the System.Runtime.InteropServices.Guid to the GUID identifying your agent. Use the GUID generator in Visual Studio.

- Override the Execute() method – use the override modifier in your method signature, and add your custom code to this method. This method is triggered on the regularly scheduled interval set up in the Relativity UI. This method doesn't return a response.

- Override the Name property – use the override modifier in your property declaration. Specify the value that you want displayed through the Winform debugging application. This name appears when running the agent from the kCura manager executable and when raising and logging messages from the agent in the Event viewer.

## Establish a database connection from an agent

Use Relativity API Helpers to interact with a database through the IDBContext interface. You can access methods on this interface by adding a reference to the Relativity.API.dll when you create new agent classes. In Visual Studio, you can easily reference these methods through IntelliSense.

## Connect to the Services API with the client-side proxy

You can log in to the Services API by with the client-side proxy and authenticate with the System account. Review the following guidelines:

- Use the methods on IEHHelper class in the Relativity API Helpers to return a connection to the Services API.

- Use System on the ExecutionIdentity enumeration when logging in with an agent.

- Reference the Relativity.API.dll when you create new agent classes.

The following code sample illustrates how to log in to the Services API using System account and the Relativity API helper class.

Copy

```text
using (IObjectManager objectManager = Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System)) {

  // Proxy created.

  // Add your custom code for working with the ObjectManager.

}
```

## Upload agents to Relativity

After you complete the development of a custom agent, you can upload the assembly that contains it to Relativity. Next, you can associate the assembly with an application. For more information, see Resource files on the Relativity Documentation site.

To delete an assembly from your environment, you must first delete all agents based on the agent types that it contains. Additionally, if you remove an agent type from an assembly, and upload the updated assembly to Relativity, all agents of that type are deleted from your environment

### Add an assembly containing an agent

Use the following steps to upload your custom agent:

- Open Relativity.

- Select the Resource Files tab. For more information, see Resource files on the Relativity Ddocumentation site.

- Click New Resource File to upload a file.

- Click Choose File in the Resource File field, and select the .dll file that contains your agent code.

- Click in the Application field and select the application that you want associated with .dll file.

Ensure that you select the application that you want associated with the agent when uploading it as a resource file. Don't select the default application if you want to use the agent in your custom application. You can't add agents associated with the default application to a custom application

- Click OK and then click Save .

You can now add your custom agent as a new agent type in Relativity.

- Select the Agents tab.

- Click New Agent .

- In the Agent Type field, click Select to select your custom agent.

- Enter information or select options as appropriate for the remaining fields. For more information, see Adding and editing agents on the Relativity Documentation site.

- Click Save .

The details view of the application in a workspace no longer lists an "Agent Type" section.

## Agents run on scheduled intervals

Implement your custom agents to run at specific time intervals. You can specify a regularly scheduled time interval for the agent service to trigger the Execute() method in your custom agent. In the Relativity UI, you can set intervals on the Agents tab when you add an agent. See Agents on the Relativity Documentation site.

## Agent types versus instances

When you extend the AgentBase class, you create a custom type of agent for your specific application needs. You can create multiple instances of this custom type to perform more work. As the amount of computation increases, you can continue to scale the number of agents running in your environment.

## Logging for agent events

You can capture information about unexpected behavior that occurs when agents are running jobs in Relativity. When you create a custom agent, your new class must inherit from the AgentBase class. The following table lists methods on this class for capturing information about agent behavior. The event type indicates the information logged in the Event Viewer.

Method Logging level Event type

RaiseError() 1 Error

RaiseMessage() Level passed into the method Information

RaiseWarning() 1 Warning

You can also log from agents using the IAPILog interface in the Relativity API Helpers. The interface provides Error, Information, Warning, Verbose, and Debug-level logging. For more information, see Log from a Relativity application and Basic concepts for Relativity API Helpers .

### Logging levels

The integer values for logging levels that you can set programmatically coincide with the options available when you add a new agent through the Relativity UI . The logging level controls only the message types that the system logs in the Event Viewer. In addition, Relativity periodically checks the agent and then displays the last massage that it raised on the Agents tab available from Home. This tab displays this message regardless of its logging level.

Logging level Integer equivalent

Log critical errors only Log level <= 1

Log warnings and errors Log level <= 5

Log all messages Log level <= 10

Currently, errors and warnings are raised as level 1, so they are always logged. If you want to implement an agent that raises only messages as opposed to errors and warning, then you need pass the logging level of 10 as a parameter to the RaiseMessage() method. For example, implement this code as RaiseMessage(“MESSAGE”, 10). For more information, see Agents on the Relativity Documentation site.
