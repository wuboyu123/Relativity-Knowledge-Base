---
title: "Specialized queries with Conditions"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Searching_Relativity/Specialized_queries_with_Conditions.htm
collection: developer
fetched_at: 2026-06-22T06:33:27+00:00
sha256: c455f8f30f28c0333006d278930afb5f8d1ca90fb030bdb8f3e437c98b2982d9
---

Specialized queries with Conditions

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# Specialized queries with Conditions

You can use Conditions when you want to perform specialized queries on Groups, Users, and Choices, as well as to create compound queries.

## Query for Groups and Users

You can query for Users by building a Condition against the Groups field that takes a list of Group ArtifactIDs. This Condition returns Users associated with those Groups. In addition, you can query for Groups by building a Condition against the Users field that takes a list of User ArtifactIDs. This Condition returns Groups associated with those Users.

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
44
45
46
47
48
49
50
51
52
53
54
55
56
57
public static List<kCura.Relativity.Client.DTOs.User> QueryUsersByGroupIds(IRSAPIClient proxy, List<int> groupIds)

{

    var users = new List<kCura.Relativity.Client.DTOs.User>();

    List<FieldValue> fields = FieldValue.AllFields;

    var condition = new ObjectsCondition("Groups", ObjectsConditionEnum.AnyOfThese, groupIds);

    var query = new Query<kCura.Relativity.Client.DTOs.User>

    {

        Condition = condition,

        Fields = fields

    };

    try

    {

        QueryResultSet<User> queryResultSet = proxy.Repositories.User.Query(query);

        if (queryResultSet.Success && queryResultSet.TotalCount > 0)

        {

            users.AddRange(queryResultSet.Results.Select(result => result.Artifact));

        }

    }

    catch (Exception e)

    {

        Console.WriteLine(e);

        throw;

    }

    return users;

}

public static List<Group> QueryGroupsByUserIds(IRSAPIClient proxy, List<int> userIds)

{

    var groups = new List<Group>();

    List<FieldValue> fields = FieldValue.AllFields;

    var condition = new ObjectsCondition("Users", ObjectsConditionEnum.AnyOfThese, userIds);

    var query = new Query<Group>

    {

        Condition = condition,

        Fields = fields

    };

    try

    {

        QueryResultSet<Group> queryResultSet = proxy.Repositories.Group.Query(query);

        if (queryResultSet.Success && queryResultSet.TotalCount > 0)

        {

            groups.AddRange(queryResultSet.Results.Select(result => result.Artifact));

        }

    }

    catch (Exception e)

    {

        Console.WriteLine(e);

        throw;

    }

    return groups;
```

## Query for Admin Choices by Choice Type

You can use the Query() method to retrieve the Artifact IDs and Names of the Choices associated with a specific Choice Type. The following Choice type field values are supported when querying by Choice, but they aren't visible on the front end:

- Case Tab

- Default Selected File Type

- Document Skip

- Group Status

- Password

- Resource Server Status

- Resource Server Type

- Send new password to

- Skip Default Preference

Only text condition is supported on Choice Type field.

### Sample code

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

//STEP 1: Create a Query to describe the search you want to run.

     Query q = new Query();

//STEP 2: Set the ArtifactTypeName to tell Relativity the type of item you want to search for.

     q.ArtifactTypeID = 7;

     q.ArtifactTypeName = "Choice";

//STEP 3: Create a Fields list to indicate which fields you want returned.

     q.Fields.Add(new Field("Name"));

     q.Fields.Add(new Field("Artifact ID"));

     q.Condition = new TextCondition("Choice Type", TextConditionEnum.EqualTo, "Password");
```

## Query for Fields associated with an Object Type

You can use the Query() method to retrieve ArtifactIDs and the Names of all Fields associated with a specific Object Type. The search returns only Fields that the logged in user has permissions to view.

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
///STEP 1: Create a Query to describe the search you want to run.

     Query<Field> q = new Query<Field>();

//STEP 2: Create a Fields list to indicate which fields you want returned.

     q.Fields.Add(new FieldValue("Name"));

     q.Fields.Add(new FieldValue("Artifact ID"));

     q.Condition = null;

     q.RelationalField = null;

     q.Condition = new WholeNumberCondition("Object Type", NumericConditionEnum.EqualTo, 10);
```

## Query with complex compound conditional expressions

Conditions may be combined into logical expressions using a CompositeCondition object. A CompositeCondition object can be initialized with two Conditions and an Operator (using And or Or ). In addition, multiple CompositeConditions can be nested to create complex expressions, resulting in binary tree expressions. Since the structure of the tree drives the precedence of operator evaluation, it may significantly influence the outcome of the query. The following illustration shows how expression C1 AND C2 OR C3 may be evaluated.

In the first example, the AND composite condition is the root of the Condition tree, while the OR condition between C2 and C3 is given precedence. In the second example, the AND condition is given precedence and is evaluated before the OR condition at the root of the Condition tree. The following code sample illustrates how to use a CompositeCondition in a query.

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

//Create a TextCondition to specify the search criteria.

     TextCondition criteria1 = new TextCondition();

     criteria1.Field = "Control Number";

     criteria1.Operator = TextConditionEnum.In;

     TextCondition criteria2 = new TextCondition();

     criteria2.Field = "Group Identifier";

     criteria2.Operator = TextConditionEnum.EqualTo;

     criteria2.Value = "999";

     CompositeCondition composite = new CompositeCondition();

     composite.Operator = CompositeConditionEnum.And;

     composite.Condition1 = criteria1;

     composite.Condition2 = criteria2;

//Set the composite criteria as the Query's Condition.

     q.Condition = composite;
```

You can use CompositeCondition to combine ViewCondition and SavedSearchCondition with other query conditions. The following example demonstrates how to use the ViewCondition in a CompositeCondition to search for responsive documents in a view:

Copy

```text
1
2
3
4
SingleChoiceCondition designationCondition = new SingleChoiceCondition("Designation", SingleChoiceConditionEnum.AnyOfThese, new List<int>{responsiveChoiceId});

ViewCondition documentViewCondition = new ViewCondition(documentViewId);

CompositeCondition compositeCondition = new CompositeCondition(designationCondition, CompositeConditionEnum.And, documentViewCondition);

QueryResult queryResult = proxy.Repositories.Document.Query(query);
```
