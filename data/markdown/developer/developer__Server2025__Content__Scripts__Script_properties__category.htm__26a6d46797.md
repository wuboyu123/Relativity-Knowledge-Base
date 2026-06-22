---
title: "category"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/category.htm
collection: developer
fetched_at: 2026-06-22T06:32:22+00:00
sha256: f4489f842cb4194dc842b347ad9da3be0c4a501fe0617841ab0e929c1bc0b88d
---

category Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

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

On this page

- category

-

- Hierarchy

- Syntax

- Default categories

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
