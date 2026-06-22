---
title: "Object Type Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Object_Type_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:27:11+00:00
sha256: cbe8c0303738309b0108bea0edbe1931b9bbadf815365d25d3234814c5e6f738
---

Object Type Manager (.NET)

# Object Type Manager (.NET)

You can use the Object Type Manager API to programmatically create custom object types for use in your applications. It includes the following features:

- Support for create, read, update, and delete operations on object types.

- Helper methods for retrieving parent object types and dependent objects.

As a sample use case, you could use the Object Type Manager API to add new object types to support a custom application that you developed. You might want to implement an application that tracks vendor or customer information and decide to add different object types for each of these items. You could also customize these object types with object rules, event handlers, and mass operations.

You can also use the Object Type Manager API through REST. For more information, see Object Type Manager (REST) .

## Fundamentals for managing object types

Review the following information to learn about the methods and classes used by the Object Type Manager API:

Methods

The Object Type Manager API exposes the following methods on the IObjectTypeManager interface in the Relativity.ObjectModel.<VersionNumber>.ObjectType namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new object type to the specified workspace. See Create an object type .

- ReadAsync() method - retrieves information about an object, including its parent object type, whether it is a dynamic object, or its view is enabled, and other properties. See Read an object type .

- UpdateAsync() method - modifies the properties of an object type, such as its user-friendly name, whether pivot or copy instances on workspace creation is enabled, and others. See Update an object type .

- DeleteAsync() method - removes an object type from a specified workspace. See Delete an object type .

- GetAvailableParentObjectTypesAsync() method - retrieves a list of parent object types available in a workspace. See Retrieve parent object types .

The DisplayableObjectTypeIdentifier class contains the Artifact ID, Name, and other identifiers for an object. It is available in the Relativity.Shared.<VersionNumber>.Models namespace.

Classes

The Object Type Manager API includes the following classes available in the Relativity.ObjectModel.<VersionNumber>.ObjectType.Models namespace:

- ObjectTypeRequest class - represents the data used to create or update an object type. The CreateAsync() and UpdateAsync() methods take an object of this type. Its properties include name, parent object type, and others.

- ObjectTypeResponse class - represents the results of a read operation. Its properties include name, parent object type, and others.

Additionally, this API includes the following class in the Relativity.ObjectModel.<VersionNumber>.ObjectType namespace:

- ObjectTypeConstants class - provides routing information about URLs used by the Object Type Manager service.

## CRUD operations for object types

Review the following guidelines for working with the Object Type Manager API:

- Verify that you have the appropriate permissions to access an object type before attempting to modify or delete it.

- Verify that the Relativity application is unlocked before attempting to add an object type to it, or to modify or delete an existing object type. You also need permissions to the application and the object type to perform these tasks.

- Use -1 to indicate the admin-level context when necessary.

See the following subsections for more information:

- Create an object type

- Read an object type

- Update an object type

- Delete an object type

- Retrieve parent object types

### Create an object type

Use the CreateAsync() method to add a new object type to a workspace or the admin-level context. When you call this method, pass the Artifact ID of the workspace or -1 for admin-level context, and an ObjectTypeRequest object. This method returns an ObjectTypeResponse object containing data about the newly-created object type.

View code sample.

Use the CreateAsync() method to add a new object type to a workspace or the admin-level context. When you call this method, pass the Artifact ID of the workspace or -1 for admin-level context, and an ObjectTypeRequest object. This method returns an ObjectTypeResponse object containing data about the newly-created object type.

To set the Artifact ID for the ParentObjectType on the ObjectTypeRequest object, use the GetAvailableParentObjectTypesAsync() method. See Retrieve parent object types .

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
public static async Task Create_Async()

{

    int workspaceId = 1017660;

    int parentArtifactTypeId = 10;

    int parentArtifactId = 1035231;

    int applicationId = 1042129;

    ObjectTypeRequest request = new ObjectTypeRequest

    {

        Name = "Test Object",

        CopyInstancesOnCaseCreation = false,

        CopyInstancesOnParentCopy = false,

        EnableSnapshotAuditingOnDelete = true,

        PersistentListsEnabled = false,

        PivotEnabled = true,

        SamplingEnabled = false,

        Keywords = "",

        Notes = "",

        ParentObjectType = new Securable<DisplayableObjectTypeIdentifier>

        {

            Secured = false,

            Value = new DisplayableObjectTypeIdentifier { ArtifactID = parentArtifactId, ArtifactTypeID = parentArtifactTypeId }

        },

        RelativityApplications = new List<ObjectIdentifier>()

        {

            new ObjectIdentifier { ArtifactID = applicationId }

        }

    };

    using (IObjectTypeManager objectTypeManager = serviceFactory.CreateProxy<IObjectTypeManager>())

    {

        try

        {

            ObjectTypeResponse newObjectType = await objectTypeManager.CreateAsync(workspaceId, request);

            string info = string.Format("Created object type with Artifact ID {0}", newObjectType.ObjectIdentifier.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Read an object type

You can retrieve basic metadata for an object type, including its name, parent object type, and other properties. You can pass in the following:

- workspaceID - the Artifact ID of the workspace where the object type exists.

- objectTypeID - the Artifact ID of the object type.

- includeMetadata - a Boolean value indicating whether to return extended object type metadata in the response. Defaults to False when not specified.

- includeActions - a Boolean value indicating whether to return a list of operations available to the current user of this object type. Defaults to False when not specified.

View code sample

The following code sample illustrates how to call the ReadAsync() method by passing the Artifact ID of a workspace and an object type. It returns only basic information. This method returns an ObjectTypeResponse object containing data about the requested object type.

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
public static async Task Read_Async()

{

    int workspaceId = 1017660;

    int objectTypeArtifactId = 1042122;

    using (IObjectTypeManager objectTypeManager = serviceFactory.CreateProxy<IObjectTypeManager>())

    {

        try

        {

            ObjectTypeResponse response = await objectTypeManager.ReadAsync(workspaceId, objectTypeArtifactId);

            string info = string.Format("Read object type {0} with Artifact ID {1}", response.ObjectIdentifier.Name, response.ObjectIdentifier.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Update an object type

Use the UpdateAsync() method to modify the properties of an object type. You can pass in the following:

- objectTypeID - the Artifact ID of the object type.

- objectTypeRequest - a request object containing the data used to update the object type

- lastModifiedOn - if specified, prevents the update operation from proceeding if the supplied date and time do not match the existing last-modified-on date and time. You can get the value of this property from an ObjectTypeResponse object, which is returned by the ReadAsync() method.

This method returns an ObjectTypeResponse object containing data about the updated object type.

View code sample.

The following code sample illustrates how to call this method by passing the Artifact ID of a workspace and an object type, and an ObjectTypeRequest object to it.

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
public static async Task Update_Async()

{

    int workspaceId = 1017660;

    int parentArtifactTypeId = 10;

    int parentArtifactId = 1035231;

    int applicationId = 1042129;

    int objectTypeArtifactId = 1042142;

    ObjectTypeRequest request = new ObjectTypeRequest

    {

        Name = "Test Object Update",

        CopyInstancesOnCaseCreation = false,

        CopyInstancesOnParentCopy = false,

        EnableSnapshotAuditingOnDelete = true,

        PersistentListsEnabled = false,

        PivotEnabled = true,

        SamplingEnabled = false,

        Keywords = "updated keywords",

        Notes = "updated notes",

        ParentObjectType = new Securable<DisplayableObjectTypeIdentifier>

        {

            Secured = false,

            Value = new DisplayableObjectTypeIdentifier { ArtifactID = parentArtifactId, ArtifactTypeID = parentArtifactTypeId }

        },

        RelativityApplications = new List<ObjectIdentifier>

        {

            new ObjectIdentifier { ArtifactID = applicationId }

        }

    };

    using (IObjectTypeManager objectTypeManager = serviceFactory.CreateProxy<IObjectTypeManager>())

    {

        try

        {

            await objectTypeManager.UpdateAsync(workspaceId, objectTypeArtifactId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Delete an object type

Use the DeleteAsync() method to delete an object type. You can pass in the following:

- workspaceID - the Artifact ID of the workspace where the object type exists. Use -1 to indicate the admin workspace.

- objectTypeID - the Artifact ID of the object type.

View code sample.

The following code sample illustrates how to call the DeleteAsync() method by passing Artifact IDs of a workspace and an object type.

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

    int workspaceId = 1017660;

    int objectTypeArtifactId = 1042142;

    using (IObjectTypeManager objectTypeManager = serviceFactory.CreateProxy<IObjectTypeManager>())

    {

        try

        {

            await objectTypeManager.DeleteAsync(workspaceId, objectTypeArtifactId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Retrieve parent object types

Use the GetAvailableParentObjectTypesAsync() method to retrieve a list of parent object types for a given workspace by passing in the workspaceID .

You may want to call this method before creating a new object type, because you must specify its parent object type.

This method returns a list of DisplayableObjectIdentifier objects, one for each object type which contains the following properties:

- ArtifactID - the Artifact ID of the object type.

- ArtifactTypeID - the ArtifactTypeID of the object type.

- GUIDs - GUIDs associated with the object type.

- Name - the name of the object type.

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
18
19
20
21
public static async Task GetAvailableParentObjectTypes_Async()

{

    int workspaceId = 1017660;

    using (IObjectTypeManager objectTypeManager = serviceFactory.CreateProxy<IObjectTypeManager>())

    {

        try

        {

            List<DisplayableObjectTypeIdentifier> response = await objectTypeManager.GetAvailableParentObjectTypesAsync(workspaceId);

            foreach (DisplayableObjectTypeIdentifier objectType in response)

            {

                string info = string.Format("Read objectType {0} with Artifact ID {1}", objectType.Name, objectType.ArtifactID);

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
