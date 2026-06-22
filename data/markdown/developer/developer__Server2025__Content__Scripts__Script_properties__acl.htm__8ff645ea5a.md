---
title: "acl"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/acl.htm
collection: developer
fetched_at: 2026-06-22T06:32:48+00:00
sha256: 2d273a038fd2afa1ff5aa4cac332e8eef1dd0eecd2f42a2fcd4367a90dbf0d85
---

acl Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# acl

This tag pulls back a list of ACL IDs for the current user based on the attributes values so they can be referenced inside of a script.

### Hierarchy

- script

- security

- acl

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

<acl

     id = string

     typeartifactid= string

     typeartifactguid= string

     type = string

/>
```

### Attributes

Name Description Data Type Required

id the ID for the field you want to reference inside the Relativity script. string yes

typeartifactid the Artifact ID for the object type that the ACL ID's are referencing. string no

typeartifactguid the Artifact Guid for the object that the ACL ID's are referencing. string no

type the permission type for the ACL ID's. Accepted values:

- View

- Edit

- Delete

string yes

You have to specify either the artifact guide or the artifact ID of the object type in order for the list to return correctly.

### Example

This script shows how to add security, enabling developers to write security-aware scripts.

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

<script>

     <name>Security Example</name>

     <description>Examples of how to use security</description>

     <category></category>

     <input></input>

     <security>

          <acl id="id" type="delete" typeartifactguid="<!--guid of an object type -->" />



     </security>

     <action returns="table"><![CDATA[

          SELECT * FROM [Field] WHERE [AccessControlListID] in (#id#)

     ]]></action>

</script>
```

On this page

- acl

-

- Hierarchy

- Syntax

- Attributes

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
