---
title: "Installing the User and Group Synchronization applications"
url: https://help.relativity.com/Server2025/Content/Relativity_Unified_Experience/Installing_the_User_and_Group_Synchronization_applications.htm
collection: user
fetched_at: 2026-06-22T06:17:19+00:00
sha256: 633d0e65892a4eb0dcb26c0f535e42696ab47f1daa9eac9b86398899c3277862
---

Installing the User and Group Synchronization applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Installing the User and Group Synchronization applications

The User Group Synchronization application has two different RAP files. One version is for the master instance, and one version for the duplicate instance.

- kCura.UserGroupSync.Master.rap - this application contains an Agent Type (User Group Sync Agent) which is responsible for the synchronization from master to duplicate.

- kCura.UserGroupSync.Duplicate.rap - this application contains a Kepler service (/Relativity.REST/api/kCura.UserGroupSync.Services.Interfaces.IuserGroupSyncModule/DuplicateManager) that is used to synchronize users and groups.

## Install both applications

To install User and Group Synchronization, follow the steps below:

You are responsible for deciding which Relativity instance is your master instance and which instance is your duplicate instance.

-

In the duplicate instance, install the Users & Groups Synchronization (Duplicate) application in a workspace (required to deploy the service). The Users & Groups Synchronization (Duplicate) application file name is kCura.UserGroupSync.Duplicate.rap .

- In the master instance, install the Users & Groups Synchronization (Master) application in a workspace (required to deploy the new agent and custom page). The Users & Groups Synchronization (Master) application file name is kCura.UserGroupSync.Master.rap .

See .

On this page

- Installing the User and Group Synchronization applications

- Install both applications


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
