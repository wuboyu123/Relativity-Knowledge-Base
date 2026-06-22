---
title: "Search Provider (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Search_Provider_API.htm
collection: developer
fetched_at: 2026-06-22T06:28:07+00:00
sha256: 489bb34bd4acf5c15b7f1cfa52e37946ca320f7beb01f86a331fe4d15650fcfa
---

Search Provider (.NET)

# Search Provider (.NET)

In Relativity, search providers let the user to search across documents in the workspace. By default, Relativity supports the following search providers:

- Keyword search provider

- dtSearch provider

- Analytics search provider

The Search Provider API service provides an API for the developers to interact with these Search Providers programmatically.

You can also use the Search Provider API services through REST. These interfaces support the same functionality as available through .NET. For more information, see Search Provider service in REST .

## Fundamentals for managing search providers

Review the following information to learn about the methods used by the Agent Manager service.

### Methods

The Relativity.Services.Interface namespace contains the ISearchProviderManage interface that exposes the following methods:

- CreateAsync() method - adds a new search provider to the specified workspace.

- UpdateAsync() method - updates search provider information.

- ReadAsync() method - retrieves metadata information regarding the specified search provider

- DeleteAsync() method - deletes the specified search provider from a workspace.

- GetDependencyList() method - retrieves a list of all dependencies for an existing search provider in a workspace.

## Create a search provider

You can create a search provider by using the CreateAsync() method of the ISearchProviderManager interface.

The following code sample illustrates how to create a dtSearch:

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
public async Task<int> CreateSearchProviderAsync(int workspaceId, string searhProviderName, string dllName)

{

    var searchProviderRequest = new SearchProviderRequest()

    {

        Active = true,

        AvailableForSearching = true,

        RankCacheMultiplier = 1,

        MinRank = 0,

        MaxRank = 100,

        Order = 10,

        Name = searhProviderName,

        DLL = dllName

    };

    using (var searchProviderService = proxy.GetClient<ISearchProviderManager>())

    {

        return await searchProviderService.CreateAsync(workspaceId, searchProviderRequest);

    }

}
```

## Update a search provider

The following code sample illustrates how to create a dtSearch using the UpdateAsync() method of the ISearchProviderManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task UpdateSearchProviderAsync(int workspaceId, int searchProviderArtifactId, SearchProviderRequest searchProviderReq)

{

    using (var searchProviderService = proxy.GetClient<ISearchProviderManager>())

    {

        await searchProviderService.UpdateAsync(workspaceId, searchProviderArtifactId, searchProviderReq);

    }

}
```

## Retrieve search provider metadata

The following code sample illustrates how to read a search provider using the ReadAsync() method of the ISearchProviderManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task<SearchProviderResponse> ReadSearchProviderAsync(int workspaceId, int searchProviderArtifactId)

{

    using (var searchProviderService = proxy.GetClient<ISearchProviderManager>())

    {

        return await searchProviderservice.ReadAsync(workspaceId, searchProviderArtifactId);

    }

}
```

## Delete a search provider

The following code sample illustrates how to delete a search provider using the DeleteAsync() method of the ISearchProviderManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task DeleteSearchProviderAsync(int workspaceId, int searchProviderArtifactId)

{

    using (var searchProviderService = proxy.GetClient<ISearchProviderManager>())

    {

        await searchProviderservice.DeleteAsync(workspaceId, searchProviderArtifactId);

    }

}
```

## Retrieve a list of dependencies

The following code sample illustrates how to retrieve a list of objects with dependencies to the specified search provider using the GetDependencyList() method of the ISearchProviderManager interface:

Copy

```text
1
2
3
4
5
6
7
public async Task<List<Dependency>> GetDependencyListAsync(int workspaceId, int searchProviderArtifactId)

{

    using (var searchProviderService = proxy.GetClient<ISearchProviderManager>())

    {

        return await searchProviderservice.GetDependencyList(workspaceId, searchProviderArtifactId);

    }

}
```
