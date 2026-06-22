---
title: "category"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/filters_category.htm
collection: developer
fetched_at: 2026-06-22T06:32:33+00:00
sha256: 1a1d9e1cbc11bc6b00541f4952a8e374cdb33f0aaa40e13761304c40e65dd7b9
---

category

# category

This element allows you to narrow the field type to a sub-set based on a specific attribute.

### Hierarchy

- script

- input

- field

- filters

- category

### Syntax

Copy

```text
1
2
3
4

<category>

     <!-- integer value -->

</category>
```

### Category values

Filter ID Field Category

0 Generic

1 FullText

2 Identifier

3 Associative

4 Comments

5 Relational

6 ProductionMarker

7 AutoCreate

8 <not in use>

9 FolderName

10 FileInfo

11 ParentArtifact

12 MarkupSetMarker

13 GenericSystem

14 MultiReflected

15 Batch

### Example

The following example demonstrates the use of field ID filter codes.

Copy

```text
1
2
3
4
5
6
7

<field id="DuplicateIndicator" name="Duplicate Indicator">

     <filters>

          <category>0</category>

          <type>3</type>

     </filters>

</field>
```
