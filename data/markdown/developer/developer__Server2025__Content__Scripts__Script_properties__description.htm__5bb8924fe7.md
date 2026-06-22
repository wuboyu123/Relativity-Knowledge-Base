---
title: "description"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/description.htm
collection: developer
fetched_at: 2026-06-22T06:32:23+00:00
sha256: fb88b9bc90270162ea829196ba550c5b28980c03ae6bfc2c680abad5e7a6b21c
---

description

# description

The value between these tags is used to populate the description column of the script.

### Hierarchy

- script

- description

### Syntax

Copy

```text
1
2
3
4

<description>

     <!-- string value -->

</description>
```

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

<script>

     <name>Description Example</name>

     <description>This is an example script for using the description element</description>

     <category></category>

     <input orientation="horizontal" />

     <display type="itemlist" />

     <action returns="table">

          <![CDATA[

          ]]>

     </action>

</script>
```
