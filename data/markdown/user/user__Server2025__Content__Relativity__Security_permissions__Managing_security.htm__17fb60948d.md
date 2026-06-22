---
title: "Security and Permissions"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Managing_security.htm
collection: user
fetched_at: 2026-06-22T06:04:15+00:00
sha256: b4602c828fe292b61fc597430578f14ffb030dabf074c6ae9b824a22285ab6c2
---

Security and Permissions Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Security and permissions

You can manage varying levels of security for users, system admins, and individual objects such as views, tabs, and fields, across your instance of Relativity and in each workspace. You can quickly edit security for a number of users simultaneously by assigning permissions at group level. After configuring a group's access permissions, you can preview the effective security rights by impersonating a general member of the group or a specific user in your environment.

If a user is a member of multiple security groups, they receive the highest permissions from the combination of groups.

## Levels of Security in Relativity

In Relativity there are two levels of security when assigning permissions, Object-level security, and Item-level security. Depending on how permissions are configured, the two levels of security can be used to grant or exclude access to either a full set of Objects, or a specified set of Items. In Relativity, Object-level security permissions define access for all items belonging to an Object type. Item-level security permissions, on the other hand, define access to a specific item or set of items, regardless of the permissions that have been set for the Object type at large. Item-level security can be used to override or offset the Object-level permissions.

Object-level permissions – an “umbrella” setting for all items belonging to an Object type. Object-level permissions are divided into two groups:

-

Instance permissions - permissions for system admin groups to limit or grant access to specified system admin objects

-

Workspace permissions - permissions for user groups added to the selected workspace. If a user group is not added to the workspace, it means users in that group do not have any access to that workspace.

Item-level permissions - permissions for a specific individual object instance and its children. By default, individual items inherit their objects rights (from workspace or instance permissions). Item-level security can override instance and workspace permissions for a specific object instance.

For most object types it is possible to grant to one of six permissions on the Item or Object level.

-

None - user does not have any access to the object.

-

View - user has access to view the object. This is the lowest object permission.

-

Edit - user has access to edit and view the object.

-

Delete - user has access to delete, edit, and view the object.

-

Add - user has access to add new objects.

-

Edit Security - grants users the ability to edit the security of objects.

For some object types, options will be missing from the above list of permissions. For example, administrators cannot set permissions to 'None' for the 'Users' or 'Views' objects, because it will make Relativity unusable.

On this page

- Security and permissions

- Levels of Security in Relativity


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


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
