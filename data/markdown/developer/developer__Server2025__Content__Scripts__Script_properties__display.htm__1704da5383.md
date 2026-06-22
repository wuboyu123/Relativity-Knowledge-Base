---
title: "display"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/display.htm
collection: developer
fetched_at: 2026-06-22T06:32:25+00:00
sha256: dee6933baafe840ff0a5752ec772a3782e8dca5f58e2fbf0ad4715022da75821
---

display Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# display

The display element allows you to control how the script output will be rendered when the script is run.

### Hierarchy

- script

- display

### Syntax

Copy

```text
1
2
3
4

<display type = string>

     <!-- children –->

</display>
```

### Attributes

Name Description Data Type Required

type declares what data type the output should be when the script is executed. Valid values:

- Report - outputs data as a PDF report

- Table - outputs data as a standard item list

string yes

### Children

Name Description

settings defines certain attributes about your report. Currently you can define the report title.

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

     <name>Display Element</name>

     <description></description>

     <category> </category>

     <input orientation="horizontal" />

     <display type="report"></display>

     <action returns="table">

          <![CDATA[

               Select top 10 [ArtifactID] from [View]

          ]]>

     </action>

</script>
```

On this page

- display

-

- Hierarchy

- Syntax

- Attributes

- Children

- Example


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
