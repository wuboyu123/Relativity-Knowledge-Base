---
title: "Best practices for event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Best_practices_for_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:26+00:00
sha256: f53cfc674dcfe40e3ea58bed50fe4845020567f378e5579e056b9f63e9394163
---

Best practices for event handlers

We recommend that you set the RunTarget attribute on all custom Post Install event handlers as a new best practice.

# Best practices for event handlers

Use these guidelines to optimize your application development with event handlers.

## Use event handler coding conventions

Use these conventions when developing event handlers:

- Inherit from the appropriate event handler base class and return a response object. See Develop object type event handlers and Develop application event handlers .

- Access only fields on a layout or fields specified in the RequiredFields property.

- Cast field values to their appropriate classes.

- Develop event handler assemblies that contain one or more classes.

## Use helper classes to create the client-side proxy

Use the helper classes so that you program to interface. These classes provide functionality for returning a database context, and connecting to the Services API with the client-side proxy. They reside in Relativity API Helpers available when you reference the Relativity.API.dll in your projects. The following code samples illustrate how to log in to the Services API using the helper methods:

- Logging in as a system user: Copy

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

try

{

     using (IObjectManager proxy =

          Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

     {

          // Proxy created.

          // Add your custom code for working with the Object Manager client.

     }

}

catch (Exception e)

{

     // Proxy failure: e.Message

}
```

- Logging in as the current user: Copy

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
try

{

     using (IObjectManager proxy =

          Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

     {

          // Proxy created.

          // Add your custom code for working with the Object Manager client.

     }

}

catch (Exception e)

{

     // Proxy failure: e.Message

}
```

In addition, codes samples for specific event handler types illustrate how to establish Services API or database connections using the helper classes. See Develop object type event handlers .

## Reference GUIDs

When building event handlers, identify fields with a unique GUIDs. See Use GUIDs to reference object types .

## Avoid using Choices with the same name

An event handler throws an error if it is attached to a multi-choice field that has two choices of the same name, and both choices are selected when the field is saved. See Work with Choice field types .

## Set the RunTarget attribute on event handlers

To improve performance, set the RunTarget attribute on your custom event handlers. This attribute indicates the database context that your event handler executes against, such as the workspace or instance level. It improves performance of your event handlers by helping them avoid race conditions or possible deadlocks. For example, if your event handler only executes against a workspace database, then set this attribute to Workspace.

The Helper RunTargets enumeration includes the Workspace enum, as well as the Instance and InstanceAndWorkspace enums, which you can use to set the RunTarget attribute. This enumeration is available on the kCura.EventHandler namespace in the Event Handlers API. For reference information, see Class library reference .

Always set the RunTarget attribute on all custom Post Install event handlers as a best practice. For more information, see Post Install event handlers .

The following code sample illustrates how to set the RunTarget attribute for executing at the instance level:

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
using System.Runtime.InteropServices;

using kCura.EventHandler;

using kCura.EventHandler.CustomAttributes;

namespace MyApp.EventHandlers

{

    [Description("My Post Install Event Handler")]

    [Guid("00000000-0000-0000-0000-000000000000")]

    [kCura.EventHandler.CustomAttributes.RunTarget(kCura.EventHandler.Helper.RunTargets.Instance)]

    public class MyPostInstallEventHandler : PostInstallEventHandler

    {

        public override Response Execute()

        {

            // Event Handler Implementation

        }

    }

}
```

## Convert long running event handlers to agents

Don't add long running code to Pre Save, Post Save, or Pre Load event handlers. If the code takes longer than 0.5 or 1.0 second to execute, add it to an agent. For additional information about event handlers and agents, see the following pages:

- Lesson 4 - Validate object changes

- Lesson 5 - Build a cron job
