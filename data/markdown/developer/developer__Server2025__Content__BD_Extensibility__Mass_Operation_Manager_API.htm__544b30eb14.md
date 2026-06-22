---
title: "Mass Operation Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Mass_Operation_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:22:47+00:00
sha256: ec75a57bd45e62122e0b72824a71a61f2647d21aa7f751650ce3fa1107b06333
---

Mass Operation Manager (.NET)

# Mass Operation Manager (.NET)

You can add mass operations to object types to further customize their behavior. When a user interacts with a mass operation, you can display a custom page or execute an event handler with specialized functionality. For general information about mass operations, see Adding a custom mass operation .

The Mass Operations Manager API includes methods for creating, reading, updating, and deleting mass operations. It also includes helper methods for retrieving information about object types that be associated with a mass operation, and available event handlers and layouts for use with a mass operation.

You can also use the service through the REST API. For more information, see Mass Operation Manager (REST) .

## Fundamentals for managing mass operations

Click the following drop-down links to learn about the methods and classes used by the Object Type Manager and related APIs.

Mass Operation Manager API

The Mass Operation Manager API contains the following methods and classes.

### Methods

The Mass Operation Manager API exposes the following methods on the IMassOperationManager interface in the Relativity.Extensibility.{versionNumber}.MassOperations namespace:

- CreateAsync() method - adds a new mass operation to an object type in a specified workspace. See Create a mass operation .

- ReadMassOperationAsync() method - retrieves information about a mass operation, such as its name, associated object type and applications, and other properties. See Read a mass operation .

- UpdateAsync() method - modifies the properties of a mass operation. See Update a mass operation .

- DeleteAsync() method - removes a mass operation from an object type in the specified workspace. See Delete a mass operation .

- GetAvailableEventHandlersAsync() method - retrieves a list of all event handlers in a specified workspace. See Retrieve available event handlers for a mass operation .

- GetAvailableLayoutsAsync() method - retrieves a list of layouts for an object type available in a given workspace with the specified object type. See Retrieve available layouts for a mass operation .

- GetAvailableObjectTypeAsync() method - retrieves a list of the available object types in the specified workspace. See Retrieve available object types for a mass operation .

### Classes

The Mass Operation Manager API includes the following classes and enumeration available in the Relativity.Extensibility.{versionNumber}.MassOperations.Models namespace:

- CustomPageMassOperationRequest class - represents the data used to create or update a mass operation that displays a custom page as a pop-up window. The CreateAsync() and UpdateAsync() methods take an object of this type. Its properties include the URL for the custom page, the width and height of the window, and others.

- EventHandlerMassOperationRequest class - represents the data used to create or update a mass operation that executes a custom event handler. The CreateAsync() and UpdateAsync() methods take an object of this type. It properties include the ID of the event handler, object type and layout associate with operation, and others.

- MassOperationResponse class - represents information about a mass operation, such its name, object type and application associated with it, and other properties. The ReadMassOperationAsync() method returns an object of this type.

- MassOperationEventHandlerResponse class - contains information about an event handler, such as the class, assembly, and application associated with it, and other properties. The GetAvailableEventHandlersAsync() method returns an object of this type.

- MassOperationLayoutResponse class - contains information about a layout, such as its user-friendly name, Artifact ID, associated object type, and other information. The GetAvailableLayoutsAsync() method returns an object of this type.

## Guidelines for managing mass operations

Review the following guidelines for working with this service:

- Make sure that you set the appropriate field values for the type of mass operation that you want to create.

- Use the helper methods to retrieve object types, event handlers, and layouts available for associating with mass operation.

- Mass operations aren't available in the admin-level context, so you must specify a workspace ID.

This API does not apply to the admin workspace and any attempt to reference the admin workspace (with workspaceID of -1) will result in a response status code of 400 (bad request).

## Create a mass operation

You can a create a mass operation that displays a custom page or that executes a custom event handler when a user interacts with it. For general information about mass operations, see Adding a custom mass operation .

Click the following drop-down links to view sample code for custom page and event handler mass operations.

Create a custom page mass operation

The following code sample illustrates how to instantiate a MassOperationRequest object containing properties used to create the mass operation. Next, it shows how to call the CreateAsync() method by passing the Artifact ID of the workspace and the MassOperationRequest object.

The value returned is the artifact identifier of the newly created mass operation.

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
public async Task CreateCustomPageMassOpAsync()

{

    using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            int workspaceID = 1022092;

            // use helper method to find available object types in workspace

            List<DisplayableObjectTypeIdentifier> objectTypes = await massOperationManager.GetAvailableObjectTypeAsync(workspaceID);

            CustomPageMassOperationRequest request = new CustomPageMassOperationRequest()

            {

                Name = "My custom page mass operation",

                ObjectType = objectTypes.Find(ot => ot.Name == "My RDO"),

                OpenInModa = true,

                PopupHeight = 250,

                PopupWidth = 250,

                Url = "www.mycustompage.com"

            };

            int massOpID = await massOperationManager.CreateAsync(workspaceID, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine($"An error occurred: {ex.Message}");

            throw;

        }

    }

}<![CDATA[

]]>
```

Create an event handler mass operation

The following code sample illustrates how to instantiate a MassOperationRequest object containing properties used to create the mass operation. Next, it shows how to call the CreateAsync() method by passing the Artifact ID of the workspace and the MassOperationRequest object.

The value returned is the artifact identifier of the newly created mass operation.

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
public async Task CreateEventHandlerMassOpAsync()

{

    using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            int workspaceID = 1022092;

            // Use helper method to find mass operation event handler previously loaded into environment via a resource file.

            List<MassOperationEventHandlerResponse> availableEventHandlers = await massOperationManager.GetAvailableEventHandlersAsync(workspaceID);

            MassOperationEventHandlerResponse eventHandler = availableEventHandlers.Find(eh => eh.ClassName.Contains("MyCustomEventHandler"));

            EventHandlerMassOperationRequest request = new EventHandlerMassOperationRequest()

            {

                Name = "My event handler mass operation",

                EventHandlerID = eventHandler.EventHandlerID,

                ObjectType = new DisplayableObjectTypeIdentifier() {Name = "My RDO"}

            };

            int massOpID = await massOperationManager.CreateAsync(workspaceID, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine($"An error occurred: {ex.Message}");

            throw;

        }

    }

}
```

## Read a mass operation

You can retrieve basic information about a mass operation or extended information, which also includes operations that you have permissions to perform on the mass operation. If you want to return extended information, use the overloaded method by passing Boolean values set to true for additional metadata and permissions as follows:

Copy

```text
1
MassOperationResponse response = await massOperationManager.ReadAsync(workspaceId, massOperationId, true, true);
```

View code sample.

The following code sample illustrates how to call the ReadAsync() method by passing the Artifact IDs of the workspace and the mass operation.

It returns an object containing information about the specified mass operation.

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
public async Task ReadMassOperationAsync()

{

    using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            int workspaceID = 1022092;

            int massOpID = 1104614;

            MassOperationResponse massOperation = await massOperationManager.ReadMassOperationAsync(workspaceID, massOpID);

        }

        catch (Exception ex)

        {

            Console.WriteLine($"An error occurred: {ex.Message}");

            throw;

        }

    }

}
```

## Update a mass operation

You can update the properties of custom page and event handler mass operations by using the overloaded UpdateAsync() method.

You can also restrict the update of a mass operation to the date that it was last modified by passing the value of LastModifiedOn property as an argument to the overloaded UpdateAsync() method. You can get the value of this property from an MassOperationResponse object, which is returned by the ReadMassOperationAsync() method.

Update a custom page mass operation

You can use these overloaded UpdateAsync() methods to modify custom page mass operations:

- Update the mass operation without any date restrictions Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int massOpID,

    CustomPageMassOperationRequest massOperationRequest

)
```

- Restrict the update of the mass operation to the last modified date: Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int massOperationID,

    CustomPageMassOperationRequest massOperationRequest,

    DateTime lastModifiedOn

)
```

The following code sample illustrates how to instantiate a MassOperationRequest object containing the updates to the mass operation. Next, it shows how to call the UpdateAsync() method by passing the Artifact IDs of the workspace and mass operation, and the MassOperationRequest object.

It returns a status code.

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
public async Task UpdateCustomPageMassOperationAsync()

{

    using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            int workspaceID = 1022092;

            int massOpID = 1104615;

            // read existing mass operation

            MassOperationResponse massOperation = await massOperationManager.ReadMassOperationAsync(workspaceID, massOpID);

            // create update request from read response

            CustomPageMassOperationRequest request = new CustomPageMassOperationRequest(massOperation);

            // update property and send request

            request.Name = "Updated name";

            await massOperationManager.UpdateAsync(workspaceID, massOpID, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine($"An error occurred: {ex.Message}");

            throw;

        }

    }

}
```

Update an event handler mass operation

You can use these overloaded UpdateAsync() methods to modify event handler mass operations:

- Update the mass operation without any date restrictions Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int massOpID,

    EventHandlerMassOperationRequest massOperationRequest

)
```

- Restrict the update of the mass operation to the last modified date: Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int massOpID,

    EventHandlerMassOperationRequest massOperationRequest,

    DateTime lastModifiedOn

)
```

The following code sample illustrates how to instantiate a MassOperationRequest object containing the updates to the mass operation. Next, it shows how to call the UpdateAsync() method by passing the Artifact IDs of the workspace and mass operation, and the MassOperationRequest object.

It returns a status code.

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
public async Task UpdateEventHandlerMassOperationAsync()

{

    using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            int workspaceID = 1022092;

            int massOpID = 1104614;

            // read existing mass operation

            MassOperationResponse massOperation = await massOperationManager.ReadMassOperationAsync(workspaceID, massOpID);

            // create update request from read response

            EventHandlerMassOperationRequest request = new EventHandlerMassOperationRequest(massOperation);

            // use helper method to find a specific layout

            DisplayableObjectTypeIdentifier objectTypeIdentifier = new DisplayableObjectTypeIdentifier() {Name = "My RDO"};

            List<MassOperationLayoutResponse> layouts = await massOperationManager.GetAvailableLayoutsAsync(workspaceID, objectTypeIdentifier);

            // update mass operation to use this layout

            request.Layout = layouts.Find(layout => layout.Name == "Specific Layout");

            await massOperationManager.UpdateAsync(workspaceID, massOpID, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine($"An error occurred: {ex.Message}");

            throw;

        }

    }

}<![CDATA[

]]>
```

## Delete a mass operation

You can remove a mass operation from object types by calling the DeleteAsync() method, and passing Artifact IDs of a workspace and a mass operation to it.

View code sample. Copy

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
public async Task DeleteMassOperationAsync()

{

    using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            int workspaceID = 1022092;

            int massOpID = 1104615;

            await massOperationManager.DeleteAsync(workspaceID, massOpID);

        }

        catch (Exception ex)

        {

            Console.WriteLine($"An error occurred: {ex.Message}");

            throw;

        }

    }

}
```

## Retrieve available object types for a mass operation

You can customize object types with additional functionality by creating mass operations for them. To retrieve a list of available object types in a specific workspace, call the GetAvailableObjectTypeAsync() method.

See Create a custom page mass operation for more information on how to use this function.

## Retrieve available event handlers for a mass operation

You can add an event handler for a mass operation to an object type. This event handler executes when the user executes the mass operation through the Relativity UI. You can retrieve a list of available event handlers by calling the GetAvailableEventHandlersAsync() method.

View code sample.

The following code sample illustrates how to call the GetAvailableEventHandlersAsync() method by passing the passing the Artifact ID of the workspace containing the event handlers to retrieve.

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
public static async Task GetAvailableEventHandlersAsync()

{

    int workspaceId = 1018486;

     using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            List<MassOperationLayoutResponse > response = await massOperationManager.GetAvailableEventHandlersAsync(workspaceId);

            foreach (MassOperationEventHandlerResponse eventHandler in response)

            {

                string info = string.Format("Read event handler {0} with Artifact ID {1}", eventHandler.Name, eventHandler.ArtifactID);

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

## Retrieve available layouts for a mass operation

When you add a mass operation that uses an event handler to an object type, you must select a layout that displays after the user initiates the operation in the Relativity UI. You can retrieve a list of layouts available for the object type by calling the GetAvailableLayoutsAsync() method.

View code sample.

The following code sample illustrates how to call the GetAvailableLayoutsAsync() by passing the Artifact ID of the workspace containing the layouts to retrieve, and the Artifact ID of the object type associated with the layouts.

The ObjectTypeIdentifier class contains the Artifact ID, Name, and other identifiers for an object.

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
public static async Task GetAvailableLayoutsAsync()

{

    int workspaceId = 1018486;

    ObjectTypeIdentifier objectType = new ObjectTypeIdentifier{ ArtifactID = 1246375 }

     using (IMassOperationManager massOperationManager = _serviceFactory.CreateProxy<IMassOperationManager>())

    {

        try

        {

            List<MassOperationLayoutResponse > response = await massOperationManager.GetAvailableLayoutsAsync(workspaceId, objectType);

            foreach (MassOperationLayoutResponse layout in response)

            {

                string info = string.Format("Read layout {0} with Artifact ID {1}", eventHandler.Name, eventHandler.ArtifactID);

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
