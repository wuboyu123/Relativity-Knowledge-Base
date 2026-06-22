---
title: "constant"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/constant.htm
collection: developer
fetched_at: 2026-06-22T06:32:29+00:00
sha256: b7653a498bf74d9a9412fb61887fb303bef8f997b03df9419a25fdeab155b54e
---

constant Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# constant

Constants are values (either static or user input, with a maximum of length of 255 characters) that get passed into the SQL action section. Each constant in the input is entered using XML.

### Hierarchy

- script

- input

- constant

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

<constant id = string

          name = string

          type = string

          required = bool>

          <!-- children – >

</constant>
```

### Attributes

Name Description Data Type Required

id defines how the field or constant is referenced in the script's SQL action section. string yes

name defines how the field or constant appears to the user when the Relativity script runs. string yes

type determines what sorts of input field(s) render on the script run screen. The available types are:

- date

- datetime

- text

- user

- number

- precision - the digit count of a number

- scale - the digit count of the numbers to the right of a decimal

- timezone

The input is rendered as a dropdown for selecting the time zone offset. The value is a decimal. For example, for Central Standard Time the value is -6.

string yes

required the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required. Boolean no

### Children

Name Description

option limits the available inputs of the constant to the list of options specified. Its entry in the input section is rendered as a drop-down list.

value defines the display value (label) for the option if it is different from the actual value.

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
17
18
19
<script>

    <name>Query Artifact ID</name>

    <description>Queries for an Artifact ID</description>

    <category>Example</category>

    <input orientation="horizontal">

        <constant id="TextIdentifier" name="TextIdentifier" type="text" required="true" />

        <constant id="VersionListNoLabel" name="Version List without Label" type="text">

            <option>1</option>

            <option>2</option>

        </constant>

    </input>

    <display type="itemlist" />

    <action returns="table"><![CDATA[

        SELECT TOP (1) [ArtifactID]

        FROM [Artifact]

        where TextIdentifier = '#TextIdentifier#'

        ]]>

    </action>

</script>
```

On this page

- constant

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
