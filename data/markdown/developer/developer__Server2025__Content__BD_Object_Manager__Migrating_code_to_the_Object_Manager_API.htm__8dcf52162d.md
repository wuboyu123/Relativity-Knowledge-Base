---
title: "Migrating code to the Object Manager API"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Manager/Migrating_code_to_the_Object_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:20+00:00
sha256: 889caac8262a7c20a24530becc5634fc497d53a6c2cf0523ccad0541f6db20c6
---

Migrating code to the Object Manager API Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Migrating code to the Object Manager API

Due to the deprecation of the Object Query Manager API, you need to update your code to use the query functionality available through the Object Manager API.

You can easily migrate your existing code to the Object Manager API. The following list outlines the differences between the Object Manager and Query Object Manager APIs:

- With the Object Manager API, you can identify the object types and fields by Name, ArtifactID, and GUID. This functionality was unavailable in the Query Object Manager API.

- With the Object Manager API, you can now use ref object types, which offer several optional properties, rather than just string and integer values.

- The Object Manager API also offers different result formats, such as a QueryResultSet object or a QueryResultSlim object, which contains a smaller payload. See Query for Relativity objects .

## Legacy code sample using the Object Query Manager API

The following legacy code queries for the top 25 decimal fields on the Document object type with the Object Query Manager API.

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
using (var objectQueryManager = Helper.GetServicesManager().CreateProxy<Services.ObjectQuery.IObjectQueryManager>())

{

    var query = new Services.ObjectQuery.Query()

    {

        Condition = "(('Object Type' == 'document') AND ('Field Type' == 'Decimal'))",

        Fields = new String[]

        {

            "Name"

        },

        IncludeIdWindow = false,

        Sorts = new String[]

        {

            "Name ASC"

        },

    };

    var includePermissions = new int[] {};

    var queryToken = String.Empty;

    var results = await objectQueryManager.QueryAsync(this.WorkspaceArtifactID, (int) kCura.Relativity.Client.ArtifactType.Field, query, 0, 25, includePermissions, queryToken);

}
```

## Updated code sample using the Object Manager API

The following updated code illustrates how to perform the same query as the legacy sample, but it uses the Object Manager API.

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
using (var objectManager = Helper.GetServicesManager().CreateProxy <Services.Objects.IObjectManager>())

{

    var nameField = new Services.Objects.DataContracts.FieldRef()

    {

        Name = "Name"

    };

    var query = new Services.Objects.DataContracts.QueryRequest()

    {

        ObjectType = new Services.Objects.DataContracts.ObjectTypeRef()

        {

            ArtifactTypeID = (int) kCura.Relativity.Client.ArtifactType.Field

        },

        Condition = "(('Object Type' == 'document') AND ('Field Type' == 'Decimal'))",

        Fields = new []

        {

            nameField

        },

        IncludeIDWindow = false,

        Sorts = new []

        {

            new Services.Objects.DataContracts.Sort()

            {

                FieldIdentifier = nameField,

                Direction = Services.Objects.DataContracts.SortEnum.Ascending

            }

        }

    };

    var results = await objectManager.QuerySlimAsync(this.WorkspaceArtifactID, query, 0, 25);

}
```

On this page

- Migrating code to the Object Manager API

- Legacy code sample using the Object Query Manager API

- Updated code sample using the Object Manager API


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
