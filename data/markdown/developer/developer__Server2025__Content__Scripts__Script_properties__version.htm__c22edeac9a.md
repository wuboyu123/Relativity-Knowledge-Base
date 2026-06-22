---
title: "version"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/version.htm
collection: developer
fetched_at: 2026-06-22T06:32:50+00:00
sha256: e71d693e3aeb355acefbdbec1c600707c0d741a67a3d1dde04ab5a9173cc8114
---

version

# version

The value between these tags is used to track the internal script version.

### Hierarchy

- script

- version

### Syntax

Copy

```text
1
2
3
4

<version>

     <!-- string value -->

</version>
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
13

<script>

     <name>Version Example</name>

     <description></description>

     <category></category>

     <version>1.2.3.0</version>

     <input orientation="horizontal" />

     <display type="itemlist" />

     <action returns="table">

          <![CDATA[

          ]]>

     </action>

</script>
```
