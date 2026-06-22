---
title: "script"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/script.htm
collection: developer
fetched_at: 2026-06-22T06:32:45+00:00
sha256: 891d6fa08a1da9092bef597b1daf592c6ec8074491af0bbbf1432f8685a20616
---

script Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# script

The top XML element in the Relativity script body.

### Hierarchy

- script

### Syntax

Copy

```text
1
2
3
4

<script>

     <!-- children -->

</script>
```

### Child elements

These child elements are the metadata XML tags used to populate the script information, such as name, version, category, etc. Enter any required properties directly into your XML script. If you don't give a value to the property, it displays blank.

Name Description

action the parent of all the attributes listed below. You can use this multiple times to pull back more than one data table from SQL.

category the is used to populate the description column of the script.

description the value is used to populate the description column of the script.

input defines the constants and fields, which are then submitted to the SQL action.

key a mechanism used to lock a script within Relativity.

name the value is used to name (and populate the Name column of) the script

display allows you to control how the script output will be rendered when the script is run.

version the value is used to track the internal script version.

security sets up the acl values that are pulled to be used as tokens in scripts.

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
16

<script>

     <name></name>

     <description></description>

     <category></category>

     <input></input>

     <display></display>

     <version></version>

     <key></key>

     <security></security>

     <action returns="table">

          <![CDATA[

            <p>

          ]]>

     </action>

</script>
```

On this page

- script

-

- Hierarchy

- Syntax

- Child elements

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
