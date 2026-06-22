---
title: "object"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/object.htm
collection: developer
fetched_at: 2026-06-22T06:32:36+00:00
sha256: a53941fd7888caa70e68ca8e19397fe15f4ab3d369e72551997ec1b97cd2f87e
---

object

# object

This tag, if used, populates the specified display type with the current instances of the specified object type.

### Hierarchy

- script

- input

- object

### Syntax

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

<object id = string

     name = string

     required = bool

     typeartifactid = integer

     rdoviewartifactid = integer

     displaytype = string

     typeartifactguid = string

     rdoviewartifactguid = string />
```

### Attributes

Name Description Data Type Required

id determines how the field is referenced in the SQL action section of the script. string yes

name determines how the field appears to the user when the Relativity script runs. string yes

required controls whether or not the object field is required for the script to run. boolean no

typeartifactid the Artifact ID of the object field that you want to use inside of the Relativity script integer no

rdoviewartifactid the Artifact ID of the view for the object field that you want to appear inside the Relativity script. integer no

displaytype controls how the object renders inside the Relativity script:

- singlepicker

- multipicker

string yes

typeartifactguid specifies the object type's Artifact GUID. string no

rdoviewartifactguid specifies the view's Artifact GUID. string no

You have to specify either the Artifact GUID or the Artifact ID of the view and object type for the field to render successfully.

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

     <name>Object Test Script</name>

     <description></description>

     <category>Smoke Test 4</category>

     <input orientation="horizontal">

          <object id="Tab" name="Tab" displaytype="multipicker" typeartifactid="1035238" rdoviewartifactid="1034262" />

     </input>

     <action returns="table">

          <![CDATA[

               select top 10 * from [Tab]

               where [ArtifactID] in (#Tab#)

          ]]>

     </action>

</script>
```
