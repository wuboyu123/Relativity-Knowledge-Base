---
title: "Persistent Highlight Service (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Persistent_Highlight_Service__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:27:18+00:00
sha256: 90f0496a927dd89d279d60a296a3ab99451cb2c9d12e5117de9a1e13b507494e
---

Persistent Highlight Service (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Persistent Highlight Service (.NET)

In Relativity, you use persistent highlight sets to configure and apply term highlighting as part of the document review process in the viewer. You can identity terms in a document to highlight and then configure the color used to highlight them. You can also apply multiple highlights set to a single document. For more information, see Persistent highlight sets .

The Persistent Highlight Service API provides the following functionality for programmatically working with these sets:

- Retrieve information about the persistent highlight sets and terms used in a specific document or workspace.

- Set terms or highlight sets as active or inactive.

- Add new terms to a persistent highlight set.

As a sample use case, you might create a custom viewer that displays and reads persistent highlight sets and terms.

In addition, you can use the Persistent Highlight Service API through the REST API. For more information, see Persistent Highlight Service (REST) .

## Fundamentals for the Persistent Highlight Service API

Review the following information to learn about the methods, classes, and enumerations used by the Persistent Highlight Service API.

Methods

The Persistent Highlight Service API includes the following methods available on the IPersistentHighlightServiceManager interface in the Relativity.DocumentViewer.Services.Versioned.<VersionNumber> namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- AddPersistentHighlightTermsToSet() method - adds new terms to a persistent highlight set. See Add new terms to a persistent highlight set .

- GetPersistentHighlightSets() method - retrieves persistent highlight sets. This overloaded method retrieves highlight sets in a specific workspace or for a specific document. See Retrieve persistent highlight sets .

- SavePersistentHighlightState() method - changes the default persistent highlight set or terms. It also can set terms or sets as inactive. See Change the state of a persistent highlight set .

Classes and enumerations

The Persistent Highlight Service API uses the following classes and enumerations:

- AddHighlightTermsToSetRequest class - represents a request to add new highlight terms to a set.

- PersistentHighlightSetDTO class - represents a persistent highlight set. Its properties include the identifier, name, initial state, and other information about the highlight set.

- PersistentHighlightStateAction enumeration - represents the actions used when storing the persistent highlight state, such as enabled, disabled, expanded, and others.

## Retrieve persistent highlight sets

Use the GetPersistentHighlightSets() method to retrieve persistent highlight sets. This overloaded method retrieves highlight sets in a specific workspace or for a specific document based on the arguments that you pass to it:

- Highlights for a specific workspace: GetPersistentHighlightSets(int workspaceID).

- Highlights for a specific document: GetPersistentHighlightSets(int workspaceID, int documentID).

View code sample Copy

```text
1
2
3
4
5
6
public async Task<IEnumerable<PersistentHighlightSetDTO>> GetPersistentHighlightSets(int workspaceID, int documentID)

{

    var persistentHighlightSetRepository = helper.GetServicesManager().CreateProxy<IPersistentHighlightServiceManager>(ExecutionIdentity.CurrentUser);

    IEnumerable<PersistentHighlightSetDTO> sets = await persistentHighlightSetRepository.GetPersistentHighlightSets(workspaceID, documentID);

    return sets;

}
```

## Change the state of a persistent highlight set

Use the SavePersistentHighlightSetState() method to change the state of a persistent highlight set or make the terms or set inactive.

View code sample Copy

```text
1
2
3
4
5
6
public async Task SavePersistentHighlightState(int workspaceID, int persistentHighlightSetID, IEnumerable<int> termIDs)

{

    PersistentHighlightStateAction action = PersistentHighlightStateAction.Collapsed;

    var persistentHighlightSetRepository = helper.GetServicesManager().CreateProxy<IPersistentHighlightServiceManager>(ExecutionIdentity.CurrentUser);

    await persistentHighlightSetRepository.SavePersistentHighlightSetState(workspaceID, persistentHighlightSetID, termIDs, action);

}
```

## Add new terms to a persistent highlight set

Use the AddPersistentHighlightTermsToSet() method to add new terms to a persistent highlight set.

View code sample Copy

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
public async Task AddPersistentHighlightTermsToSet(int workspaceID, int persistentHighlightSetID)

{

    string backgroundColor = "#336600";

    string foregroundColor = "#ffffff";

    string term = "Lorem";

    List<AddHighlightTermsToSetRequest> requests = new List<AddHighlightTermsToSetRequest>()

    {

        new AddHighlightTermsToSetRequest(backgroundColor, foregroundColor, term)

    };

    var persistentHighlightSetRepository = helper.GetServicesManager().CreateProxy<IPersistentHighlightServiceManager>(ExecutionIdentity.CurrentUser);

    await persistentHighlightSetRepository.AddPersistentHighlightTermsToSet(workspaceID, persistentHighlightSetID, requests);

}
```

On this page

- Persistent Highlight Service (.NET)

- Fundamentals for the Persistent Highlight Service API

- Retrieve persistent highlight sets

- Change the state of a persistent highlight set

- Add new terms to a persistent highlight set


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
