---
title: "Search Relativity"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Searching_Relativity/Searching_Relativity.htm
collection: developer
fetched_at: 2026-06-22T06:33:16+00:00
sha256: 08aceab981a753fb78e8c3e52fd7657595f99d54d064f3e88e38e324672e1a74
---

Search Relativity

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# Search Relativity

With the Services API, you can perform searches using Query objects and the Query() method on the RSAPIClient class. The Query() method takes a Query object, which has Conditions that contain information about the search that you want to execute. In addition, you can combine Conditions with an operator to create compound queries.

See these related pages:

- dtSearchCondition and CASearchCondition

- SavedSearchCondition

- Specialized queries with Conditions

- ViewCondition

- MonthOfCondition

## Use of Query objects

You can use the Query object to describe a search that you want execute. You must indicate the ArtifactType for the search by using the ArtifactTypeID, ArtifactTypeName, or ArtifactTypeGuid. You can use the Condition property on a Query to provide an expression that describes the search criteria. A Condition specifies the name of a Field, a comparison operator (such as EqualTo or GreaterThan), and a value. The list of supported comparison operators varies by Field data type. You can use the Fields collection on the Query object to specify Fields that you want returned for each item matching the search criteria.

The Query() method returns a QueryResult object with those items that match the search Condition. The QueryResult object has the following properties:

- QueryArtifacts – a collection of Artifacts that were found by the query.

- QueryToken – when this property has a value, it indicates that the query returned more Artifacts than number of results specified by the length parameter. See Paging .

The QueryToken expires after a period specified by the PDVCacheLifetime property value in the Services API configuration file. If the property value is not set in the file, it defaults to 1000 minutes.

You can sort query results by specifying one or more Fields in the Sorts property on the Query object. This property is a collection of Sort objects, which takes a Field name, a sort direction (ascending/descending), and a sort precedence order. (The sort order gives a high precedence to lower numbers.)

A query on multi-reflected Fields returns a list of the requested data type. For example, the value of a multi-reflected integer field returns a list of integers.

## Available Conditions for Querying

You can combine Conditions with the AND or OR operator to create complex queries. The Services API provides the following classes as condition types:

- BooleanCondition

- CASearchCondition

- CompositeCondition

- DateTimeCondition

- DecimalCondition

- dtSearchCondition

- FileCondition

- MonthOfCondition

- MultiChoiceCondition

- NotCondition

- ObjectCondition

- ObjectsCondition

- SavedSearchCondition

- SingleChoiceCondition

- TextCondition

- UserCondition

- ViewCondition

- WholeNumberCondition

### Supported data grid query operators

Use these operators to query Data Grid-enabled fields:

- IS SET

- IS NOT SET

- The IS SET condition operator excludes the Data Grid records where the field is null or has an empty string value.

- IS LIKE operator is not supported.

## System types supported by the Query() method

The Query() method provides the following functionality:

- Searches for all Workspaces in Relativity, and all Fields in a specific Workspace. It supports queries for Documents and Dynamic Objects based on specified search criteria.

- Searches on any Field in the Available Fields or the Selected Fields list available in the view for a system type. (The view is available through the Relativity web UI.)

This table summarizes the Relativity system types that the Services API supports.

System Types Query Support

Application Yes

Batch Yes

Batch Sets Yes

Choice Yes

Client Yes

Group Yes

Markup Sets Yes

User Yes

Object Type

Yes (Artifact Type)

Tab Yes (Only Workspace tab)

Folder Yes

Layout

View Yes

Workspace Yes

Error

Field Yes

Relativity Scripts Yes

Saved Searches Yes

## NotCondition

You can use the NotCondition class to construct NOT-conditional expressions. The following code samples illustrate how to negate TextCondition using NotCondition.

##### NOT LIKE

Copy

```text
1
2
TextCondition criteria = new TextCondition("Extracted Text", TextConditionEnum.Like, "Jones");

NotCondition NotCriteria = new NotCondition(criteria);
```

##### IS NOT SET

Copy

```text
1
2
TextCondition criteria = new TextCondition("Extracted Text", TextConditionEnum.IsSet);

NotCondition NotCriteria = new NotCondition(criteria);
```

## Paging

In the Services API, you can perform paging on query results that include Documents or Relativity Dynamic Objects (RDOs). Paging provides the functionality used to return query results in small subsets.

You can use paging in searches for Documents or RDOs by calling the Query() method and passing a length parameter, which determines the number of Artifacts returned by the initial page of results. You can set the length parameter on the QuerySubset() method to return Artifacts on subsequent pages. When the length parameter is set to 0, the Services API uses the default value defined for the PDVDefaultQueryCacheSize setting on the Instance setting table. This value is set to 10000, but you can update it as necessary.

The following sample code illustrates how to use paging.

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
using (IRSAPIClient proxy = this.Helper.GetServicesManager().CreateProxy<IRSAPIClient>(Relativity.API.ExecutionIdentity.System))

{

    var qry = new DTOs.Query<DTOs.Document>();

    qry.Fields = DTOs.FieldValue.AllFields;

    var resultsFirst100 = proxy.Repositories.Document.Query(qry, 100);

    string queryToken = resultsFirst100.QueryToken;

    var resultsSecond100 = proxy.Repositories.Document.QuerySubset(queryToken, 101, 100);

}
```

### Paging support for system objects

In a Relativity workspace, all objects created by users are RDOs, so paging is supported for these objects. It is also supported for Batch and Relativity Application, which are workspace system objects that are also RDOs.

You can check the Boolean value assigned to the Dynamic property on an object to determine whether it is a RDO.

## Constraints on the Query() method

The Query() method is subject to the following constraints:

- Queries are limited to only a single object type.

- Conditions (that is search criteria) only support comparison against literal values, such as True/False, "Hello World”, or 10.5. You can't compare one Field’s value against another.

- The NOT Condition returns the set of all items that don't meet the negated criteria. This operator uses set-based logic. For example, you might query for Documents using a numeric relational comparison operator, such as X < 5 . The query for NOT X < 5 returns documents where X is Greater Than or Equal To 5 , and it also returns all documents where X is NULL (that isn't set).

- Search criteria are only applied against Fields of the object type being returned. For example, when you search for Documents, you can only query on Fields that are associated with the Document object type. You can't query against Fields on Dynamic Objects.

- The list of available comparison operators is limited and varies by Field type. This list will be expanded in future releases.
