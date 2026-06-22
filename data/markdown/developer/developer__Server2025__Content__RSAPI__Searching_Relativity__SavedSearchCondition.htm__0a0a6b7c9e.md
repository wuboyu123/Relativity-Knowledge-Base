---
title: "SavedSearchCondition"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Searching_Relativity/SavedSearchCondition.htm
collection: developer
fetched_at: 2026-06-22T06:33:15+00:00
sha256: f728cac04293a8bf11928d12edabd6e13a604c0c2930b1def4664030c3ad7ed8
---

SavedSearchCondition Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# SavedSearchCondition

You can use the SavedSearchCondition to execute a saved search so that you can review its results. To execute this query, you need the ArtifactID of the saved search stored in Relativity. You can then execute the query by using the SavedSearchCondition on the Query() method.

This page only describes how to use the SavedSearchCondition in a query. If you want to create, read, update, or delete a saved search, see Keyword Search Manager (.NET) for saved searches .

## SelectedFields directive

You can set the SelectedFields directive when you perform a query with SavedSearchCondition or a ViewCondition. The SelectedFields directive returns only the Fields displayed on a saved search or view in Relativity. The following sample code illustrates how to use this directive.

Copy

```text
1
2

query.Fields = Field.SelectedFields;
```

You aren't limited to the Fields defined by the saved search or view when using a SavedSearchCondition or a ViewCondition. Instead, you can specify particular Fields that you want to retrieve, or you can use the AllFields directive to retrieve all Fields for an ArtifactType, such as View, User, or Document.

## Query for the ArtifactID of a Saved Search

You can query for the ArtifactID of a Saved Search. After the ArtifactID is returned, you can use it to run the Saved Search.

## Query for a Document with a SavedSearchCondition

You can use the SavedSearchCondition to query for a Document with a saved search ID. A SavedSearchCondition can't be combined with any other Condition types.

On this page

- SavedSearchCondition

- SelectedFields directive

- Query for the ArtifactID of a Saved Search

- Query for a Document with a SavedSearchCondition


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
