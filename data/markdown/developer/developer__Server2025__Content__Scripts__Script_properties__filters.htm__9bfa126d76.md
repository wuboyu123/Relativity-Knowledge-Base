---
title: "filters"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/filters.htm
collection: developer
fetched_at: 2026-06-22T06:32:32+00:00
sha256: 15319b4e6d94da88ff265df5afb80f059003437b9973d6b174237140dc5394e5
---

filters

# filters

In addition to the id and name, each field input has a filters sub-section, and each filter is defined by a code. When a script is run, Relativity presents the input fields as drop-down menus. The types of fields in the drop-down menu are designated by a filter. This allows the user to easily select the correct case field. If a value is not specified, the tag automatically defaults to zero.

### Hierarchy

- script

- input

- field

- filters

### Syntax

Copy

```text
1
2
3
4

<filters>

     <!-- children –->

</filters>
```

### Children

Name Description

type defines which Relativity field types appear in the drop-down menu.

category allows you to narrow the field type to a sub-set, based on a specific attribute.

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

<field id="ProductionName" name="ProductionName">

     <filters>

          <category>6</category>

          <type>5</type>

     </filters>

</field>
```
