---
title: "Group Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Group_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:26:26+00:00
sha256: f98eb83ed846a3954d8deefc9a048f481bf6977386c0934c0071a4fb86857e86
---

Group Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Group Manager (.NET)

In Relativity, you can organize users by assigning them to one or more groups. Additionally, you can set permissions for a group. For more information, see Groups in the Relativity Documentation site.

The Group Manager API exposes methods that provide the following functionality:

- CRUD and query operations on groups.

- Helper methods for adding and removing users.

- Helper methods for querying on available users and clients to associate with a group.

- Mass operations for adding and removing multiple users to or from multiple groups.

As a sample use case, you might create an application with a custom interface for adding multiple users with a mass operation.

You can also use the Group Manager API through REST. For more information, see Group Manager (REST) .

## Fundamentals for the Group Manager API

Review the following information to learn about the methods and classes used by the Group Manager API.

### Methods

The Group Manager API exposes the following methods on the IGroupManager interface in the Relativity.Identity.<VersionNumber>.Services namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- AddMembersAsync() method - adds users to the group. Its parameters include the Artifact ID of the group, and a list of user identifiers. See Add users to a group .

- CreateAsync() method - adds a new group to Relativity. This method takes a GroupRequest object and returns a GroupResponse object. See Create a group .

- DeleteAsync() method - removes a group from Relativity. This method takes the Artifact ID of the group. See Delete a group .

- MassAddUsersToGroupsAsync() method - adds multiple users to multiple groups. Its parameters include a list of user identifiers and a list of group identifiers. It returns a list of MassOperationResult objects. See Add multiple users to multiple groups .

- MassRemoveUsersFromGroupsAsync() method - removes multiple users from multiple groups. Its parameters include a list of user identifiers and a list of group identifiers. It returns a list of MassOperationResult objects. See Remove multiple users from multiple groups .

- QueryEligibleClients() method - retrieves a list of clients available for use when creating and updating a group. Its parameters include a QueryRequest object, a start index, and the number of clients to return. It returns a QueryResultSlim object. See Query for clients to associate with a group .

The Object Manager API also uses QueryResultSlim objects. For more information about these objects, see Object Manager (.NET) .

- QueryEligibleUsersToAdd() method - retrieves a list of users that can be added to a group. Its parameters include a QueryRequest object, a start index, the number of users to return, and the Artifact ID of a group. It returns a QueryResultSlim object. See Query for users to add to a group .

- QueryMembersAsync() method - retrieves information about the users assigned to a group. Its parameters are a QueryRequest object, a start index, the number of users to return, and the Artifact ID of a group. It returns a QueryResultSlim object. See Query for group members .

- ReadAsync() method - retrieves metadata for a user group, including its name, associated client, and other properties. Its parameter is the Artifact ID of the group. It returns the GroupResponse object. See Retrieve a group .

- RemoveMembersAsync() method - removes users from a group. Its parameters include the Artifact ID of the group, and a list of user identifiers. See Remove users from a group .

- UpdateAsync() method - modifies properties of a group. Its parameters are the Artifact ID of the group and the GroupRequest object. It returns the GroupResponse object. See Update a group .

### Classes

The Group Manager API includes the following classes available in the Relativity.Identity.<VersionNumber>.GroupModels namespace:

- GroupRequest class - represents the data used to create or update the group. See the following properties:

Field Type Description

Client Securable<ObjectIdentifier> A client identifier associated with a group.

Name string The name of a group.

Keywords string Keywords associated with a group.

Notes string Notes about a group.

- GroupResponse class - represents the existing group. See the following properties:

Field Type Description

Client Securable<DisplayableObjectIdentifier> A client identifier associated with a group.

GroupType GroupType enum The type of the group.

Keywords string Keywords associated with a group.

Notes string Notes about the group.

CreatedOn DateTime The date and time of group creation.

CreatedBy DisplayableObjectIdentifier The identifier for the user who created the group.

LastModifiedBy DisplayableObjectIdentifier The identifier for the user who last modified the group.

LastModifiedOn DateTime The date and time of last modification.

Meta Meta Metadata for the group, including a list of read-only and unsupported fields.

Actions List<Action> A list of available actions that can be performed on a group.

ArtifactID int The Artifact ID of the group.

Guids List<Guid> A list of Guids associated with the group.

Name string The name of the group.

- GroupType enum - represent the type of a group. See the following enums:

Name Value Description

SystemAdmin 1 A group containing system administrators

SystemGroup 2 A group containing users

Everyone 3 A group containing all the users in the system

## Create a group

When creating a group, you can use the QueryEligibleClients() method to retrieve a list of available clients to associate with it. See Query for clients to associate with a group .

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
int clientArtifactID = 1015644;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    GroupRequest request = new GroupRequest()

    {

        Client = new Securable<ObjectIdentifier>()

        {

            Value = new ObjectIdentifier()

            {

                ArtifactID = clientArtifactID

            }

        },

        Name = "My Group",

        Keywords = "Group keywords",

        Notes = "Group notes"

    };



    GroupResponse response = await mgr.CreateAsync(request);



    Console.WriteLine($"Created group with ArtifactID {response.ArtifactID}");
```

## Retrieve a group

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
int groupArtifactID = 1029453;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    GroupResponse response = await mgr.ReadAsync(groupArtifactID);



    Console.WriteLine($"Read group with ArtifactID {response.ArtifactID}");

}
```

## Update a group

You can pass optional CancellationToken and IProgress<ProgressReport> objects to this overloaded method.

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
int groupArtifactID = 1029453;

int clientArtifactID = 1015644;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    GroupRequest request = new GroupRequest()

    {

        Client = new Securable<ObjectIdentifier>()

        {

            Value = new ObjectIdentifier()

            {

                ArtifactID = clientArtifactID

            }

        },

        Name = "My Group",

        Keywords = "Updated group keywords",

        Notes = "Updated group notes"

    };



    GroupResponse response = await mgr.UpdateAsync(groupArtifactID, request);



    Console.WriteLine($"Updated group with ArtifactID {response.ArtifactID}");

}
```

## Delete a group

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
int groupArtifactID = 1029455;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    await mgr.DeleteAsync(groupArtifactID);



    Console.WriteLine($"Delete group with ArtifactID {groupArtifactID}");

}
```

## Query for group members

You can pass optional CancellationToken and IProgress<ProgressReport> objects to this overloaded method.

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
int groupArtifactID = 1029453;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    QueryRequest request = new QueryRequest()

    {

        Fields = new List<FieldRef>

        {

            new FieldRef { Name = "Full Name" },

            new FieldRef { Name = "E-mail Address" }

        },

        Condition = "'E-mail Address' == 'testuser@mydomain.com'"

    };



    QueryResultSlim result = await mgr.QueryMembersAsync(request, 1, 1000, groupArtifactID);



    string emailAddress = result.Objects[0].Values[1].ToString();



    Console.WriteLine($"Queried user with email address {emailAddress}");

}
```

## Add users to a group

When adding users to a group, you can use the QueryEligibleUsersToAdd() method to retrieve a list of available users. See Query for users to add to a group .

You can pass optional CancellationToken and IProgress<ProgressReport> objects to this overloaded method.

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
int groupArtifactID = 1029453;

int userArtifactID = 1029457;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    ObjectIdentifier objIdentifier = new ObjectIdentifier()

    {

        ArtifactID = userArtifactID

    };



    await mgr.AddMembersAsync(groupArtifactID, objIdentifier);



    Console.WriteLine($"Added user with ArtifactID {userArtifactID}");

}
```

## Remove users from a group

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
int groupArtifactID = 1029453;

int userArtifactID = 1029457;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    ObjectIdentifier objIdentifier = new ObjectIdentifier()

    {

        ArtifactID = userArtifactID

    };



    await mgr.RemoveMembersAsync(groupArtifactID, objIdentifier);



    Console.WriteLine($"Removed user with ArtifactID {userArtifactID}");

}
```

## Helper methods for users and clients

The Group Manager API exposes multiple helper methods that you can use to query for information about users and clients.

### Query for clients to associate with a group

You can pass optional CancellationToken and IProgress<ProgressReport> objects to this overloaded method.

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
using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    QueryRequest request = new QueryRequest

    {

        Fields = new List<FieldRef> { new FieldRef { Name = "Name" } },

        Condition = ""

    };

    QueryResultSlim result = await mgr.QueryEligibleClients(request, 1, 1000);



    for (int i = 0; i < result.ResultCount; i++)

    {

        Console.WriteLine($"Client {result.Objects[i].Values[0]} with Artifact ID {result.Objects[i].ArtifactID}");

    }

}
```

### Query for users to add to a group

You can pass optional CancellationToken and IProgress<ProgressReport> objects to this overloaded method.

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
int groupArtifactID = 1029453;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    QueryRequest request = new QueryRequest

    {

        Fields = new List<FieldRef> { new FieldRef { Name = "Full Name" } },

        Condition = ""

    };

    QueryResultSlim result = await mgr.QueryEligibleUsersToAdd(request, 1, 1000, groupArtifactID);

    for (int i = 0; i < result.ResultCount; i++)

    {

        Console.WriteLine($"User {result.Objects[i].Values[0]} with Artifact ID {result.Objects[i].ArtifactID} is can be added to a group with Artifact ID {groupArtifactID}");

    }

}
```

### Query for groups assigned to a user

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
using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    QueryRequest request = new QueryRequest

    {

        Fields = new List<FieldRef> { new FieldRef { Name = "Name" } },

        Condition = ""

    };

    QueryResultSlim result = await mgr.QueryMembersAsync(request, 1, 1000, groupArtifactID);



    for (int i = 0; i < result.ResultCount; i++)

    {

        Console.WriteLine($"Client {result.Objects[i].Values[0]} with Artifact ID {result.Objects[i].ArtifactID}");

    }

}
```

## Mass operations on groups

You can use mass operations to add or remove multiple users to or from multiple groups in a single API call.

### Add multiple users to multiple groups

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
int groupArtifactID = 1029453;

int userArtifactID = 1029457;



using (IGroupManager mgr = new ServiceFactory(settings).CreateProxy<IGroupManager>())

{

    List<ObjectIdentifier> groups = new List<ObjectIdentifier>()

    {

        new ObjectIdentifier() { ArtifactID = groupArtifactID }

    };



    List<ObjectIdentifier> users = new List<ObjectIdentifier>()

    {

        new ObjectIdentifier() { ArtifactID = userArtifactID }

    };



    List<MassOperationResult> result = await mgr.MassAddUsersToGroupsAsync(users, groups);

}
```

### Remove multiple users from multiple groups

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
public static async Task MassRemoveUsersFromGroups()

{

    int groups = new List<ObjectIdentifier>

    {

        new ObjectIdentifier { ArtifactID = 1015005 },

        new ObjectIdentifier { ArtifactID = 1015028 }

    };

    int users = new List<ObjectIdentifier>

    {

        new ObjectIdentifier { ArtifactID = 1026730 },

        new ObjectIdentifier { ArtifactID = 1026732 }

    };



    using (IGroupManager mgr = ServiceFactory.CreateProxy<IGroupManager>())

    {

        List<MassOperationResult> results = await groupManager.MassRemoveUsersFromGroupsAsync(users, groups);

        for each (MassOperationResult result in results)

        {

            if (result.Succeeded)

            {

                Console.WriteLine($"Users removed from a group with Artifact ID {result.ArtifactID}");

            }

            else

            {

                Console.WriteLine($"Failed to remove users from a group with Artifact ID {result.ArtifactID}: {result.Exception.Message}");

            }

        }

    }

}
```

On this page

- Group Manager (.NET)

- Fundamentals for the Group Manager API

- Methods

- Classes

- Create a group

- Retrieve a group

- Update a group

- Delete a group

- Query for group members

- Add users to a group

- Remove users from a group

- Helper methods for users and clients

- Query for clients to associate with a group

- Query for users to add to a group

- Query for groups assigned to a user

- Mass operations on groups

- Add multiple users to multiple groups

- Remove multiple users from multiple groups


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
