---
title: "security"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/security.htm
collection: developer
fetched_at: 2026-06-22T06:32:46+00:00
sha256: 2846ea10e07ff143e21e65932841757ff6cc7d77b2189926f1115315b73151a3
---

security

# security

This element enables you to reference the current user ACL lists in your scripts.

### Hierarchy

- script

- security

### Syntax

Copy

```text
1
2
3
4

<security>

     <!--child elements -->

</security>
```

### Child elements

Name Description

acl represents a single list of ACL ID's that are able to be referenced in a script.

### Example

Copy

```text
1
2
3
4

<security>

     <acl id="" typeartifactid="" type="" />

</security>
```
