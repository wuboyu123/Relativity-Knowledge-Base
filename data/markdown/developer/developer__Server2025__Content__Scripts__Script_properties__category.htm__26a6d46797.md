---
title: "category"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/category.htm
collection: developer
fetched_at: 2026-06-22T06:32:22+00:00
sha256: f4489f842cb4194dc842b347ad9da3be0c4a501fe0617841ab0e929c1bc0b88d
---

category

# category

Categories are text fields on the Relativity script object that can help you define the script type. You can also create your own categories.

### Hierarchy

- script

- category

### Syntax

Copy

```text
1
2
3
4

<category>

     <!-- string value -->

</category>
```

### Default categories

By default, all Relativity library scripts have one of the following:

- Environment Optimization scripts allow you to monitor and maintain the performance of your environment.

- Case Optimization scripts allow you to monitor and maintain the performance of your workspace.

- Case Functionality scripts perform functions against a specific workspace. For example, flag or populate a new field.

- Billing scripts perform administrative tasks providing statistics on your Relativity environment.

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

     <name>Category Example</name>

     <description></description>

     <category>test</category>

     <input></input>

     <version></version>

     <action returns="table">

          <![CDATA[

               Select Top 10 * from artifact

          ]]>

     </action>

</script>
```
