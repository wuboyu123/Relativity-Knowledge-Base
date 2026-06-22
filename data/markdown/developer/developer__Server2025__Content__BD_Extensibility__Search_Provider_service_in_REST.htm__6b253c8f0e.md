---
title: "Search Provider (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Search_Provider_service_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:28:09+00:00
sha256: e3c1bba0cc73514e92a0020405ed0d64a3b8d642799f56c94eb1829e938716cc
---

Search Provider (REST)

# Search Provider (REST)

In Relativity, search providers let the user to search across documents in the workspace. By default, Relativity supports the following search providers:

- Keyword search provider

- dtSearch provider

- Analytics search provider

The Search Provider API service provides an API for the developers to interact with these Search Providers programmatically.

You can also use the Search Provider API services through the .NET interfaces. These interfaces support the same functionality as available through REST. For more information, see Search Provider API .

## Create a search provider

To create a new search provider, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/{workspaceID}/searchproviders
```

Set {workspaceID} to the Artifact ID of the workspace where you want to add a new search provider. See the following sample URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/1018294/searchproviders
```

View the descriptions of the fields in the request

The request contains the following fields:

- Active - a Boolean field indicating whether the search provider is active.

- AvailableForSearching - a Boolean field indicating whether the search provider is available for searching.

- RankCacheMultiplier - the rank multiplier for the search provider.

- MinRank - the minimum rank for the search provider.

- MaxRank - the maximum rank for the search provider.

- Order - the order for the search provider.

- Name - the user-friendly name of the search provider.

- DLL - the DLL name for the search provider.

- Parameters - the parameters for the search provider.

View a sample JSON request for creating a search provider Copy

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
{

   "Active":false,

   "AvailableForSearching":true,

   "RankCacheMultiplier":1,

   "MinRank":0,

   "MaxRank":100,

   "Order":10,

   "Name":"DtSearchIndex - Incremental-updated",

   "DLL":"kCura.EDDS.dtSearchProvider.dll",

   "Parameters":""

}
```

When the request is successful, the response contains the Artifact ID of the new search provider. It also returns the status code of 200.

## Update a search provider

To update a search provider, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/{workspaceID}/searchproviders/{RelativitySearchProviderID}
```

Set {workspaceID} to the Artifact ID of the workspace containing the search provider. Set {RelativitySearchProviderID} to the Artifact ID of the search provider. See the following sample URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/1018294/searchproviders/1113513
```

View the descriptions of the fields in the request

The request contains the following fields:

- Active - a Boolean field indicating whether the search provider is active.

- AvailableForSearching - a Boolean field indicating whether the search provider is available for searching.

- RankCacheMultiplier - the rank multiplier for the search provider.

- MinRank - the minimum rank for the search provider.

- MaxRank - the maximum rank for the search provider.

- Order - the order for the search provider.

- Name - the user-friendly name of the search provider.

- DLL - the DLL name for the search provider.

- Parameters - the parameters for the search provider.

View a sample JSON request for updating a search provider Copy

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
{

    "searchProvider": {

        "Active": true,

        "AvailableForSearching": true,

        "RankCacheMultiplier": 1,

        "MinRank": 0,

        "MaxRank": 100,

        "Order": 10,

        "Name": "dtsearch index",

        "DLL": "kCura.EDDS.dtSearchProvider.dll",

        "Parameters": ""

    }

}
```

When the request is successful, it returns the status code of 200.

## Retrieve search provider metadata

To retrieve search provider metadata, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/{workspaceID}/searchproviders/{RelativitySearchProviderID}
```

Set {workspaceID} to the Artifact ID of the workspace containing the search provider. Set {RelativitySearchProviderID} to the Artifact ID of the search provider. See the following sample URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/1018294/searchproviders/1113513
```

View the descriptions of the fields in the response

- Active - a Boolean field indicating whether the search provider is active.

- AvailableForSearching - a Boolean field indicating whether the search provider is available for searching.

- ArtifactID - the Artifact ID of the search provider.

- RankCacheMultiplier - the rank multiplier for the search provider.

- MinRank - the minimum rank for the search provider

- MaxRank - the maximum rank for the search provider.

- Order - the order for the search provider.

- Name - the user-friendly name of the search provider.

- DLL - the DLL name for the search provider.

- Parameters - the parameters for the search provider.

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
{

  "Active": true,

  "AvailableForSearching": true,

  "ArtifactID": 1113513,

  "RankCacheMultiplier": 1,

  "MinRank": 0,

  "MaxRank": 100,

  "Order": 1,

  "Name": "DtSearchIndex - Incremental",

  "DLL": "kCura.EDDS.dtSearchProvider.dll",

  "Parameters": ""

}
```

## Delete a search provider

To delete a search provider, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/{workspaceID}/searchproviders/{RelativitySearchProviderID}
```

Set {workspaceID} to the Artifact ID of the workspace containing the search provider. Set {RelativitySearchProviderID} to the Artifact ID of the search provider. See the following sample URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/1018294/searchproviders/1113513
```

When the request is successful, it returns the status code of 200.

## Retrieve a list of dependencies

To retrieve a list of objects with dependencies to the specified search provider, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/{workspaceID}/{RelativitySearchProviderID}/dependencyList
```

Set {workspaceID} to the Artifact ID of the workspace containing the search provider. Set {RelativitySearchProviderID} to the Artifact ID of the search provider. See the following sample URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.SearchProviders/workspace/1018294/searchproviders/1113513/dependencyList
```

View the descriptions of the fields in the response

- ObjectType - the type of Relativity object dependent on the search provider.

- Action - indicates whether a dependent objects is deleted or unlinked when the search provider is deleted.

- Count - the number of objects with a dependency on the search provider.

- Connection - indicates whether a dependency is a parent or a field on a single or multiple object field.

- HierarchicLevel - the degree of dependency between object types.

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

      "ObjectType":{

         "Secured":false,

         "Value":"Search Index"

      },

      "Action":"Delete",

      "Count":{

         "Secured":false,

         "Value":1

      },

      "Connection":{

         "Secured":false,

         "Value":"Parent"

      },

      "HierarchicLevel":0

   },

   {

      "ObjectType":{

         "Secured":false,

         "Value":"Search Terms Report"

      },

      "Action":"Unlink",

      "Count":{

         "Secured":false,

         "Value":1

      },

      "Connection":{

         "Secured":false,

         "Value":"Field: Index"

      },

      "HierarchicLevel":0

   },

   {

      "ObjectType":{

         "Secured":false,

         "Value":"Search / View"

      },

      "Action":"Unlink",

      "Count":{

         "Secured":false,

         "Value":1

      },

      "Connection":{

         "Secured":false,

         "Value":"Field: SearchProviderID"

      },

      "HierarchicLevel":0

   }

]
```
