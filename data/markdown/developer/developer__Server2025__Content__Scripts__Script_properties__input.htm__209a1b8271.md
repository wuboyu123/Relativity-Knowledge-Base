---
title: "input"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/input.htm
collection: developer
fetched_at: 2026-06-22T06:32:28+00:00
sha256: 3f69bbeaf08d9eaf56eccd481a59e3500cdefc4ffc6bae40ad0f60858b97fdf1
---

input Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# input

This tag allows you to define the orientation of your report as well as define various attributes about your report.

### Hierarchy

- script

- input

### Syntax

Copy

```text
1
2
3
4

<input>

     <!-- children -->

</input>
```

### Attributes

Name Description Data Type Required

orientation allows you to determine how the Relativity script's run page's layout renders. Valid values:

- vertical

- horizontal

string no

### Children

Name Description

constant values (either static or user input) that get passed into the SQL action section.

sql if used, populates a drop-down menu with the return value of an inline SQL statement.

field allows you to reference Relativity case fields.

search if used, populates a drop-down list of saved searches in the inputs section. The selected search is then converted into the FROM clause of its respective saved search.

searchprovider if used, populates a drop-down list of search providers in the case. The selected value is converted into the selected search provider's ID.

object if used, populates the specified display type with the current instances of the specified object type.

On this page

- input

-

- Hierarchy

- Syntax

- Attributes

- Children


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
