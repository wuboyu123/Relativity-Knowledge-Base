---
title: "searchprovider"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/searchprovider.htm
collection: developer
fetched_at: 2026-06-22T06:32:39+00:00
sha256: 92c8c166bbad38df3a05ea033199439b7f47ada8e8070d066180caf518942b27
---

searchprovider

# searchprovider

This tag, if used, populates a drop-down list of search providers in the case. The selected value is converted into the selected search provider's ID.

### Hierarchy

- script

- input

- searchprovider

### Syntax

Copy

```text
1
2
3
4

<searchprovider id = string

     name = string>

</searchprovider>
```

### Attributes

Name Description Data Type Required

id determines how the field is referenced in the SQL action section of the script. string yes

name determines how the field appears to the user when the Relativity script runs. string yes

required the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required. Boolean no

### Input

The search provider input allows you to enter a drop-down list of search providers in the workspace. Each search provider input must be assigned a search provider ID and name.

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

<script>

     <name>Example</name>

     <description> </description>

     <category></category>

     <input>

          <searchprovider id="SearchProvider" name="Search Index:" />

     </input>

     <action returns="table">

               <![CDATA[

               select [ArtifactID],[Name] from [SearchProvider] where [ArtifactID] = #SearchProvider#

               ]]>

     </action>

</script>
```
