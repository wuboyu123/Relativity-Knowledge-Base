---
title: "sql"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/sql.htm
collection: developer
fetched_at: 2026-06-22T06:32:41+00:00
sha256: fa87252a5f0592a1a685271301b677660a2ad90e89c0b63f837c83e59953da00
---

sql

# sql

This tag, if used, populates a drop-down menu with the return value of an inline SQL statement.

### Hierarchy

- script

- input

- sql

### Syntax

Copy

```text
1
2
3
4

<sql id = string

     name = string>

</sql>
```

### Attributes

Name Description Data Type Required

id defines how the field is referenced in the SQL action section of the script. string yes

name defines how the field appears to the user when the Relativity script runs. string yes

required the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required. Boolean no

### Input

The inputs are the same ID and name tags consistent with other input types. The contents of the SQL tag should be an SQL statement that returns at least two columns; one has to be named Display and the other has to be named ID.

When this input appears on the run page, a drop-down list type of field is created. The drop-down menu display value is whatever resides in the Display column and the behind-the-scenes value is whatever is populated in the ID column.

### Example

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

<script>

     <name> Example</name>

     <description> </description>

     <category> </category>

     <input>

          <sql id="viewID" name="Views">

               SELECT

               Display = [Name],

               ID = [ArtifactID]

               FROM

               [View]

          </sql>

     </input>

     <display type="report">

          <settings reporttitle="Test Title" />

     </display>

     <action returns="table">

          <![CDATA[

               SELECT * FROM [View]

               WHERE ArtifactID = #viewID#

          ]]>

     </action>

</script>
```

If the SQL input returns a string value, it must be enclosed in quotes when passed to the CDATA action, as in the following example.

Copy

```text
1
2
3

declare @field_value varchar(100) = '#field_value#'

if (@field_value = 'Yes') ..
```
