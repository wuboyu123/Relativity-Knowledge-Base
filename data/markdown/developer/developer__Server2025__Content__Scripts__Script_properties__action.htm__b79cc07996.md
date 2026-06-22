---
title: "action"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/action.htm
collection: developer
fetched_at: 2026-06-22T06:32:20+00:00
sha256: 98af5499c27ea5bdf9e1aadec467554998a66a894bd905647236e98a5cf31d1c
---

action Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# action

You can use this tag multiple times to pull back more than one data table from SQL.

### Hierarchy

- script

- action

### Syntax

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

<action timeout = string

     returns = string

     displaywarning = bool

     allowhtmltagsinoutput = bool

     name = string>

     <!-- children -->

</action>
```

### Attributes

Name Description Data Type Required

timeout defines how long the script can run.

- The value is in seconds

- It's possible to enter "indefinite", which allows the script to run for an indefinite period of time.

- If there is no value, the timeout defaults to 30 seconds.

string no

returns defines how query results are returned.

- status returns the number of rows affected by the query.

- table returns the output of the query in tabular form.

string yes

displaywarning If set to "true", allows a pop-up warning message to appear when running the script. By default, this is set to "true" if not included. boolean no

allowhtmltagsinoutput if set to "true", allows HTML tags to be interpreted by the browser instead of rendered as markup. boolean no

name the name used to reference the scripts in the item list drop-down menu as well as to populate the subreport header when displayed as a report. string no

### Reference inputs

The body of an action is a SQL script that allows you to pass in inputs. Inputs are referenced in the body of the action by wrapping their ID values in # symbols.

### Example

When the following script runs, it replaces #dateReviewedField# with the actual column name of the field picked in the "Date Reviewed Field" drop-down menu. In addition, #dateReviewed# is replaced with the contents of the "Date Reviewed" field in the run page. Relativity inserts a CDATA tag. A CDATA tag is a token in XML that indicates anything following it up to the ]]> token is to be interpreted as unformatted text. This is important because, in SQL, the inequality operator is <>, which is an empty entity in an XML document. If you use <>, the resulting script would be invalid. This also means that you don't have to escape characters in that text block such as &.

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
17
18
19
20
21

<script>

     <name>Update Script</name>

     <input>

     <constant id="dateReviewed" name="Date Reviewed" type="date"/>

     <field id="dateReviewedField" name="Date Reviewed Field">

          <filters>

               <category>0</category>

                    <type>2</type>

               </filters>

          </field>

     </input>

     <action returns="status" name="Update Script" >

          <![CDATA[

          UPDATE

          [Document]

          SET

          [#dateReviewedField#] = '#dateReviewed#'

          ]]>

     </action>

</script>
```

On this page

- action

-

- Hierarchy

- Syntax

- Attributes

- Reference inputs

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
