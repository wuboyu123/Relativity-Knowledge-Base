---
title: "Query for resources"
url: https://platform.relativity.com/Server2025/Content/REST_API/Resource_Tasks/Querying_for_resources.htm
collection: developer
fetched_at: 2026-06-22T06:25:06+00:00
sha256: 97250c60aa40e64eacf099a9cda155ce0563f1a92dd5fbeffc54f7ca871ec147
---

Query for resources

# Query for resources

To query data, you can use the POST method and specify a condition in body of the request. The POST method provides you with the option to build complex queries without the restrictions that browsers impose on the number of characters in a URL. You can also run queries with empty bodies that contain no conditions or sort order designation. This type of query is equivalent to the condition where ArtifactID > 0, which the Services API currently supports. For more information, see Query options .

A successful query returns all the results for small data sets or uses paging to return a subset of results for large data sets. When paging is used, the response includes the first page of data, and a token for retrieving subsequent pages as illustrated in the following example.

Copy

```text
1
2
3
{

"__Location":http://localhost/Relativity.REST/Workspace/1015423/Document/QueryResult/1437867?start=1&count=1000

 }
```

You can also query for objects through the Object Manager service. For more information about this service, see Query for Relativity objects .

## Query options

The body of a POST request for a query may include a JSON representation that contains fields specifying a condition, sort order, and other parameters. This JSON representation of a query illustrates the use of fields.

Copy

```text
1
2
3
4
5
{

   "condition":" 'Artifact ID' == 1109807",

   "sorts":["Artifact ID"],

   "fields":[{"*"}]

}
```

You use Field IDs, Field names, or GUIDs in a JSON array of fields.

View query options

Query Field JSON Name Description

CONDITION "condition" Represents a condition string. For syntax examples, see Syntax for query conditions .

FIELDS "fields"

Represents a JSON array of fields.

- The following example returns the Name, Is Required, and Allow HTML fields: Copy

```text
1
"fields":["Name", "Is Required", "Allow HTML"]
```

- Use the "*" operator to return all fields: Copy

```text
1
"fields":["*"]
```

- Use the *NOFIELDS* operator to return only the artifact identifier fields: Copy

```text
1
"fields":["*NOFIELDS*"]
```

Artifact identifier fields include:

- Artifact ID

- Guids

- Artifact Type ID

- Artifact Type Name

- Artifact Type Guids

- Parent Artifact

- Use the *SELECTEDFIELDS* operator to return only the selected fields within a Saved Search or View: Copy

```text
1
"fields": ["*SELECTEDFIELDS*"]
```

This is only allowed if a Saved Search or View condition is used within the query conditions, and compound conditions are not supported.

SORTS "sorts"

Represents a JSON array of fields. You indicate the sort order by specifying ASC or DESC after the field name, such as Relativity Text Identifier ASC . By default, ASC is the sort order on a field.

Certain resource types use a Sorts object with a different structure:

- Client

- dtSearch

- Keyword search

- Message of the day

- Permission

See query code samples for these resource types for more information on sorting.

RELATIONAL FIELD "relational field"

Represents a string identifying a relational field. A query containing a relational field returns any matching fields and all documents that share this field.

## Syntax for query conditions

You can use the syntax examples in the following table as models for defining query conditions. Make sure that your query conditions don't include special characters such as underscore (_).

View syntax examples

Data Type or Operation Syntax Examples

Whole Numbers 'Foo' == 42

'Foo' <> 42

'Foo' > 42

'Foo' >= 42

'Foo' < 42

'Foo' <= 42

'Foo' IN [42, 53]

Dates

ISO8601 format:

'Foo' == 1972-05-22T00:00:00.00Z

'Foo' <> 1972-05-22T00:00:00.00Z

'Foo' > 1972-05-22T00:00:00.00Z

'Foo' >= 1972-05-22T00:00:00.00Z

'Foo' < 1972-05-22T00:00:00.00Z

'Foo' <= 1972-05-22T00:00:00.00Z

- Since the BETWEEN operator is not supported, use a combination of > and < to specify date ranges.

- Only the date portion of the expression is evaluated. Time is not considered.

MonthOf operator:

'Foo' in MonthOf 5

'Foo' in MonthOf May

Valid MonthOf values include:

- 1 or January

- 2 or February

- 3 or March

- 4 or April

- 5 or May

- 6 or June

- 7 or July

- 8 or August

- 9 or September

- 10 or October

- 11 or November

- 12 or December

Booleans 'Foo' == true

'Foo' <> true

'Foo' == false

Decimals 'Foo' == 3.14

'Foo' == 3.14

'Foo' <> 3.14

'Foo' > 3.14

'Foo' >= 3.14

'Foo' < 3.14

'Foo' <= 3.14

'Foo' IN [3.14,7.50]

Files None

Text 'Foo' == 'Bar'

'Foo' <> 'Bar'

'Foo' STARTSWITH 'Bar'

'Foo' ENDSWITH 'Bar'

'Foo' LIKE 'Bar'

'Foo' IN ['Foo','Bar']

'Foo' CONTAINS 'Bar'

'Foo' > 'Bar'

'Foo' < 'Bar'

'Foo' <= 'Bar'

'Foo' >= 'Bar'

Saved Searches and Views Use the keyword SAVEDSEARCH or VIEW followed by the ArtifactID for a saved search or view:

- 'ArtifactID' IN SAVEDSEARCH <ArtifactID>

- 'ArtifactID' IN VIEW <ArtifactID>

See the following examples:

- 'ArtifactID' IN SAVEDSEARCH 1234567

- 'ArtifactID' IN VIEW 1234567

- ArtifactID is the only valid field for use in saved search and view conditions.

- Saved searches and views can't be used in composite query conditions.

Object Use the keyword OBJECT followed by the ArtifactID for an object:

- 'Foo' == OBJECT <ArtifactID>

- 'Foo' <> OBJECT <ArtifactID>

- 'Foo' IN OBJECT [ <ArtifactID>, <ArtifactID>, <ArtifactID>]

See the following examples:

- 'Foo' == OBJECT 1234567

- 'Foo' IN OBJECT [1234567, 4567123, 6712345]

Multiobject Use the keyword MULTIOBJECT followed by the ArtifactIDs for multiple objects:

- 'Foo' CONTAINS MULTIOBJECT [ <ArtifactID>, <ArtifactID>, <ArtifactID>]

- 'Foo' INTERSECTS MULTIOBJECT [ <ArtifactID>, <ArtifactID>,<ArtifactID>]

See the following examples:

- 'Foo' CONTAINS MULTIOBJECT [1234567, 4567123, 6712345]

- 'Foo' INTERSECTS MULTIOBJECT [1234567, 4567123, 6712345]

Also, see Queries on multiple object fields .

Choice Use the keyword CHOICE followed by either the ArtifactID or GUID for a choice:

- 'Foo' == CHOICE <ArtifactID or GUID>

- 'Foo' <> CHOICE <ArtifactID or GUID>

- 'Foo' IN CHOICE [<ArtifactID or GUID>, <ArtifactID or GUID>, <ArtifactID or GUID>]

See the following examples:

- 'Foo' == CHOICE 1234567

- 'Foo' <> CHOICE 32942BAB-AFD9-4684-8B0D-68EF277F4DC5

- 'Foo' IN CHOICE [3F2504E0-1F89-13D3-9A0C-0305E82C3301, 0657AD6D-A4AB-4344-84E5-0933C84B4F4F]

Multichoice Use the keyword MULTICHOICE followed by either the ArtifactIDs or GUIDs for multiple choices:

- 'Foo' CONTAINS MULTICHOICE [<ArtifactID or GUID>, <ArtifactID orGUID>, <ArtifactID or GUID>]

- 'Foo' INTERSECTS MULTICHOICE [<ArtifactID or GUID>, <ArtifactID orGUID>, <ArtifactID or GUID>]

See the following examples:

- 'Foo' CONTAINS MULTICHOICE [1234567, 4567123, 6712345]

- 'Foo' INTERSECTS MULTICHOICE [3F2504E0-1F89-13D3-9A0C-0305E82C3301, 0657AD6D-A4AB-4344-84E5-0933C84B4F4F]

Users 'Foo' == USER 'Ralph'

'Foo' <> USER 'Ralph'

'Foo' LIKE USER 'Ralph'

'Foo' LIKE USER '%Ralph'

'Foo' LIKE USER 'Ralph%'

'Foo' LIKE USER '%Ralph%'

Any Field Type 'Foo' ISSET

NOT 'Foo' ISSET

Combinations or Negation 'Foo' == 1 AND 'Bar' == 2

'Foo' == 1 AND 'Bar' == 2 OR 'Baz' <> 'Towel'

'Foo' == 1 AND ('Bar' == 2 OR 'Baz' <> 'Towel') AND NOT ('Foo' == 1)

You can use the AND, OR, and NOT operators with this condition. Parenthesis are optional.

### Wildcard characters

There are two types of wildcard searches supported: single-character and variable-length. The percentage symbol "%" is a variable-length wildcard and will match one or more characters of any type. The underscore symbol "_" is a single-character wildcard and will match only one character of any type.

If you query text that contains one of these two wild card characters, the default behavior will treat the text content as wild cards and you may get over-inclusive results. To avoid this, you can escape "%" and "_" in LIKE, STARTSWITH, and ENDSWITH operators by surrounding with square brackets. For example:

- "FOO LIKE 'yearly [%] increase'": matches text like " yearly % increase "

- "FOO LIKE 'NAME[_]REDACTED": matches text like " NAME_REDACTED "

### Special characters

Your query conditions may require the use of special characters that need to be escaped in your code.

The following table lists special characters that need to be escaped when used in query conditions:

Character

Description

\' Single quotation mark - used for character literals.

\" Double quotation marks - used for string literals.

\\ Backslash

\b Backspace (ASCII character 8)

\f Form feed (ASCII character 12)

\n New line (ASCII character 10)

\r Carriage return (ASCII character 13)

\t Horizontal tab (character 9)

\uxxxx Unicode escape sequence for a character with hexadecimal value of xxxx.

% Percent sign - used as a wildcard . This usage is specific to Relativity.

~ Tilde - used for handling a GUID or Integer as a field name.

Additionally, note that the compiler or interpreter for the programming language that you are using may pre-process strings in your code. For example, the following conditions produce the same result in C# and JavaScript:

- Example 1 : Copy

```text
1
" 'Name' == 'chicago\u00A9land' "
```

In this example, the compiler or interpreter evaluates the string as chicago©land , which is fed directly into condition parser used by Relativity. Since no escape characters are present, the parser proceeds as normal.

- Example 2 : Copy

```text
1
" 'Name' == 'chicago\\u00A9land' "
```

In this second example, the extra backslash instructs the compiler or interpreter to escape the Unicode sequence, so it is evaluated as chicago\u00A9land . The Relativity condition parser then further interprets the Unicode escape sequence and evaluate this string to chicago©land .

### Supported data grid query operators

Use these operators to query Data Grid-enabled fields:

- IS SET

- IS NOT SET

- The IS SET condition operator excludes the Data Grid records where the field is null or has an empty string value.

- IS LIKE operator is not supported.

### Queries on multiple object fields

When querying on multiple object fields, consider the use of INTERSECTS and CONTAINS in the following examples. The numbers 1 and 2 represent the Artifact IDs of the associated object in the multiple object field.

- Determine whether a multiple object field contains at least one of the associated objects in your condition by using this syntax:

Copy

```text
1
Condition = "('Test Multi Object' INTERSECTS MULTIOBJECT [1,2])"
```

- Determine whether a multiple object field contains all the associated objects in your condition by using this syntax:

Copy

```text
1
Condition = "('Test Multi Object' CONTAINS MULTIOBJECT [1,2])"
```
