---
title: "Event Handler Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Event_Handler_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:26:02+00:00
sha256: 83bc897ff3778b24ce00acceff353a970cf32b2654fc2aeb9d9ff5dd6f14fa86
---

Event Handler Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Event Handler Manager (.NET)

You can add custom behavior to an object type by attaching event handlers to it. For example, you might attach an event handler that performs a specific action when a user makes an update to an object and then attempts to save it. For more information, see Develop object type event handlers .

The Event Handler Manager service contains methods for programmatically attaching event handlers to an object type, and for detaching them. It also provides helper methods that you can use for the following purposes:

- To retrieve a list of event handlers in a workspace, which could be attached to a specific object type.

- To retrieve a list of event handlers currently attached to an object type.

You can also use the Event Handler Manager through the REST API. For more information, see Event Handler Manager (REST) .

## Fundamentals for managing object event handlers

Click the following drop-down links to learn about the methods and classes used by the Event Handler Manager.

Event Handler Manager API

The Event Handler Manager API contains the following methods and classes.

#### Methods

The Event Handler Manager API exposes the following methods on the IEventHandlerManager interface in the Relativity.Extensibility.{versionNumber}.EventHandler namespace:

- AttachAsync() method - adds an event handler to the specified object type. This method takes the Artifact IDs of the workspace, the object type to attach the event handler to, and the event handler. It returns a Task. See Attach an event handler to an object type .

- DetachAsync() method - removes an event handler from the specified object type. This method takes the Artifact IDs of the workspace, the object type to detached the event handler from, and the event handler. It returns a Task. See Detach an event handler to an object type .

- GetAttachedAsync() method - retrieves a list of event handlers attached to the specified object type. This method takes the Artifact IDs of the workspace and object type, and returns a list of EventHandlerResponse objects. See Retrieve event handlers attached to an object type .

- GetAvailableEventHandlersAsync() method - retrieves a list of event handlers available in a workspace for association with a specific object type. This method takes the Artifact IDs of the workspace and object type, and returns a list of EventHandlerResponse objects. See Retrieve available event handlers for an object type .

#### Classes and enumerations

The Event Handler Manager API includes the following classes and enumeration available in theRelativity.Extensibility.{versionNumber}.EventHandler.Models namespace:

- EventHandlerExecution enumeration - provides a list of execution types for event handlers, such as Console, PageInteraction, and others. See Develop object type event handlers for general information about these event handler types.

- EventHandlerResponse class - represents the results of a get operation for attached or available event handlers in a workspace. The GetAttachedAsync() and GetAvailableEventHandlersAsync() methods return an object of this type. Its properties include class name, assembly name, and others.

## Attach an event handler to an object type

To attach an event handler to an object type, call the AttachAsync() method by passing the Artifact IDs of a workspace and an object type, and the ID of the event handler.

In the following code sample, the eventHandlerId parameter is an identifier assigned by Relativity to the event handler. This identifier isn't the artifact ID for the event handler. The GetAttachedAsync() and GetAvailableEventHandlersAsync() methods return an EventHandlerResponse object, which has this ID property.

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
public static async Task Attach_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1035231;

    int eventHandlerId = 1982384;

    using (Services.Interfaces.EventHandler.IEventHandlerManager eventHandlerManager = serviceFactory.CreateProxy<Services.Interfaces.EventHandler.IEventHandlerManager>())

    {

        try

        {

            await eventHandlerManager.AttachAsync(workspaceId, objectTypeArtifactId, eventHandlerId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Detach an event handler to an object type

To detach an event handler from an object type, call the DetachAsync() method by passing the Artifact IDs of a workspace and an object type, and the ID of the event handler.

In the following code sample, the eventHandlerId parameter is an identifier assigned by Relativity to the event handler. This identifier isn't the Artifact ID for the event handler. The GetAttachedAsync() and GetAvailableEventHandlersAsync() methods return an EventHandlerResponse object, which has this ID property.

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
public static async Task Detach_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1035231;

    int eventHandlerId = 1982384;



    using (Services.Interfaces.EventHandler.IEventHandlerManager eventHandlerManager = serviceFactory.CreateProxy<Services.Interfaces.EventHandler.IEventHandlerManager>())

    {

        try

        {

            await eventHandlerManager.DetachAsync(workspaceId, objectTypeArtifactId, eventHandlerId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve event handlers attached to an object type

To retrieve the event handlers attached to an object type, call the GetAttachedAsync() method by passing the Artifact IDs of a workspace and an object type. If no event handlers are available for the object type, this method returns an empty list.

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
public static async Task GetAttached_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1035231;

    using (Services.Interfaces.EventHandler.IEventHandlerManager eventHandlerManager = serviceFactory.CreateProxy<Services.Interfaces.EventHandler.IEventHandlerManager>())

    {

         try

        {

            List<EventHandlerResponse> response = await eventHandlerManager.GetAttachedAsync(workspaceId, objectTypeArtifactId);

            foreach (EventHandlerResponse eventHandler in response)

            {

                string info = string.Format("Read Event Handler {0} with Artifact ID {1}", eventHandler.ClassName, eventHandler.ArtifactID);

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

## Retrieve available event handlers for an object type

You can retrieve a list of event handlers in a workspace that are compatible with a specific object type.

The following code sample illustrates how to call the GetAvailableEventHandlersAsync() method by passing the Artifact IDs of a workspace and an object type. If no event handlers are available for the object type, this method returns an empty list.

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
public static async Task GetAvailableEventHandlers_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1035231;

    using (Services.Interfaces.EventHandler.IEventHandlerManager eventHandlerManager = serviceFactory.CreateProxy<Services.Interfaces.EventHandler.IEventHandlerManager>())

    {

        try

        {

            List<EventHandlerResponse> response = await eventHandlerManager.GetAvailableEventHandlersAsync(workspaceId, objectTypeArtifactId);

            foreach (EventHandlerResponse eventHandler in response)

            {

                string info = string.Format("Read Event Handler {0} with Artifact ID {1}", eventHandler.ClassName, eventHandler.ArtifactID);

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

On this page

- Event Handler Manager (.NET)

- Fundamentals for managing object event handlers

- Attach an event handler to an object type

- Detach an event handler to an object type

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
