---
title: "settings"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/settings.htm
collection: developer
fetched_at: 2026-06-22T06:32:26+00:00
sha256: caf90d1f2f942677fdc285bf7be25d1c3611a66a4b8ed45a068a19f727ef1721
---

settings

# settings

This tag defines certain attributes about your report. Currently you can define the report title.

### Hierarchy

- script

- display

- settings

### Syntax

Copy

```text
1
2
3

<settings reporttitle= string>

</settings>
```

### Attributes

Name Description

reporttitle defines the title of the report that appears in the report header when the script is rendered as a report. If nothing is defined, Relativity uses the script name instead.

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

     <name>Settings Element</name>

     <description> </description>

     <category> </category>

     <input orientation="horizontal" />

     <display type="report">

          <settings reporttitle="Test Title" />

     </display>

     <action returns="table">

          <![CDATA[

               Select top 10 [ArtifactID] from [View]

          ]]>

     </action>

</script>
```
