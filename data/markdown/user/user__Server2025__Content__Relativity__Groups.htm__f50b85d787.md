---
title: "Groups"
url: https://help.relativity.com/Server2025/Content/Relativity/Groups.htm
collection: user
fetched_at: 2026-06-22T06:06:37+00:00
sha256: 97e864d17461c5e29ad8019d4e7fe87b2b08d48746789e6c92da54c49d66c677
---

Groups Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Groups

With groups you can organize users in Relativity. A user can be a member of one or more groups. You can grant groups permission to view admin tabs from Home. You can also add groups to workspaces and set permissions per group on a workspace-by-workspace basis.

This page contains the following:

- System groups

- Creating and editing groups

- Adding users to groups

- Adding or removing groups from a client domain

## System groups

Relativity workspaces include the following default system groups:

- Everyone - All users are members of the Everyone group. System admins can manage the permissions all users have on system level views and scripts. You are unable to revoke certain permissions for the Everyone group. See Instance security for a complete list of unrevokable permissions.

- System Administrators - Relativity system admins have rights to see every item in a Relativity environment. System admins have full access to all admin tabs. System admins can then create and edit new clients, matters, users, groups and views, among other capabilities. System admins also have the following script and applications-related permissions: view, run, preview, create/write, edit (unlocked scripts only), link, and import applications. See Relativity applications .

Regardless of permissions, system admins can't edit locked scripts.

The following table shows script permissions for each group.

View Run Edit

(locked scripts) Edit

(unlocked scripts) Preview Write Link

System Admin √ √ √ √ √ √

Standard User √ √ √

## Creating and editing groups

To create a new group or edit an existing group:

- Click your name in the upper right corner of Relativity, and then click Home .

- Click the Groups tab.

- Click New Group . To edit group information, click the Edit link next to an existing group name.

If your groups list doesn't show Edit links, edit the All Groups view to display the Edit link. See Views .

- Add or edit the fields on the group details page. See Fields for details.

- Click Save to save the group information.

The group details page displays a list of users added to the group as well as group-accessible workspaces. For more information, see Adding users to groups and Security and permissions .

See the learning course Case Administration Foundations: Creating the Workspace Framework for more information.

## Fields

The groups object contains the following fields:

Group Information

- Name - the group’s name, which is a required field for creating a group.

As your Relativity environment grows, arbitrary group names like "Group 1" can produce a confusing administrative workflow. Name each group according to their purpose and permission level, such as "ACME Co. Reviewer" and "ABC Corp. Administrators."

- Client - a required field that makes the group a child object of the chosen client.

- Group Type - an uneditable field that displays one of the following categories:

- System Admin

- System Group

- Personal

- Everyone

- Workspace Admin

- Keywords - an optional field where extra group information may be recorded.

- Notes - an optional field where extra group information may be recorded.

## Adding users to groups

You can add and/or remove users from groups from either the group details page or the user details page. The procedure is the same for both.

A job is executed when you add users to a group or when you remove them from one. If your Relativity environment is configured with an SMTP server, you receive an email message when the job is completed. To use the notification feature, set the RelativityInstanceURL instance setting. Ensure that the value for this setting is the URL for your Relativity instance. For example, the URL would have the format: https://example.relativity.com/Relativity. The user receiving the notification must have access to this URL. For more information, see the Instance settings .By default, user and group operations are disabled. Contact Customer Support for information about enabling user and group operations in your Relativity environment.

To add or remove users:

- Click your name in the upper right corner of Relativity, and click Home .

- Click the Groups tab. You can complete the following steps from either the Users or Groups tabs:

- From the Users tab, click the name of a user and scroll down to the Groups section on the form.

- From the Groups tab, click the name of a group and scroll down to the Users section on the form.

- To add a user to the group, click Add in the Users or Groups section depending on the tab.

- Choose an item on the selection dialog, and click OK .

- Click Close on the message indicating that you have submitted a job.

Relativity sends an email message notifying you when the job is completed. If an error occurs, the email message contains a link that you can use to retry the job. You must be logged into Relativity before you click the retry link. The Errors tab also displays the retry link. For more information, see Errors .

- To remove a user from a group, click Remove . Click OK on the confirmation message, and then click Close .

You can preview the security of a group to determine whether or not the appropriate permissions are granted to that group over particular workspaces. For more information about previewing group security see Preview security .

## Adding or removing groups from a client domain

You can add or remove objects from client domains if you activate the client domains feature. See Client domains for more information.

Moving a group into a client domains may cause the group to lose previously configured permissions.

Relativity displays a warning message when a sys admin attempts to edit or copy permissions for any group in a client domain. This warning makes the sys admin aware that modifying permissions may have significant consequences. For example, changing permissions may allow client domain users to modify items outside their tenancy. The sys admin can click Manage Permissions to proceed with the update or Cancel to exit the pop-up window.

Use the following steps to add a group to a client domain:

- Navigate to the Groups tab.

- Select the group you want to add to the client domain from the list.

- Click Edit .

- Click Select next to the Client field in Group Information section.

- Select the client with client domains enabled from the list.

- A warning message requires you to confirm your decision by clicking Save .

- Click Save .

Use the following steps to remove a group from a client domain:

- Navigate to the Groups tab.

- Select the group you want to remove from the client domains from the list.

- Click Edit .

- Click Select next to the Client field in Group Information section.

- Select a client not associated with a client domain from the list.

- Click Save .

On this page

- Groups

- System groups

- Creating and editing groups

- Fields

- Adding users to groups

- Adding or removing groups from a client domain


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
