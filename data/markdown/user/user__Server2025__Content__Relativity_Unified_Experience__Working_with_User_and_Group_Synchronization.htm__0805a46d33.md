---
title: "Working with User and Group Synchronization"
url: https://help.relativity.com/Server2025/Content/Relativity_Unified_Experience/Working_with_User_and_Group_Synchronization.htm
collection: user
fetched_at: 2026-06-22T06:17:22+00:00
sha256: 5c1f70713c812a46c78f6f9582f61659ba362d5a74f9b5c99f1bfe65fa9cbf63
---

Working with User and Group Synchronization

# Working with User and Group Synchronization

After installing and configuring the User and Group Synchronization application in your environments, you can sync users from your master instance to your duplicate instance, view user and group synchronization information, and monitor the status of jobs that the User Group Sync agent processes during a sync.

## Special considerations

Special considerations include:

- The user and group synchronization syncs OpenID Connect login methods (not SAML) in addition to groups, users, and clients. However, it does NOT carry over passwords, authentication providers, or permissions to the duplicate instance. Use the Invite users mass operation to send out a mass password reset invitation email and manually set security permissions for the synced groups in your duplicate instance after migration is completed.

- This functionality is only available for customers running at least one RelativityOne instance, as well as a second instance running either RelativityOne or Relativity 9.5.224.9 and above.

## Specifying which users to sync with your duplicate instance

In your master instance, add the users that you want to sync with your duplicate instance to the Synched Users group. See Step 3 - Configure your master instance .

- To successfully synchronize users and groups from the master instance to the duplicate instance, you must have successfully completed all steps to configure the master and duplicate instances.

- You can only synchronize groups between a Relativity Server instance and a RelativityOne instance if both groups have users in them. If a group does not have users in it, add a dummy user to the group.

When you add new users to the Synced Users group or modify groups linked to Synced Users in the master instance, let the agent run, and then validate that the new users and modified groups appear in your duplicate instance.

- The agent runs a sync every 5 minutes after first time users are synced. Keep in mind that it may take some time for the users to be reflected in the duplicate instance, depending on how many users and groups are being synced.

- While the users are being synced to the duplicate instance, ensure that updates are not being made to users in the master instance.

To view the users and groups that are synced, see Viewing User and Group Synchronization information

To exclude certain groups of users or clients (and their associated groups of users) from being synced, see Excluding groups and clients from synchronization .

## User sync data flow

When users are added to the Synced Users group that you created in the master instance, the application will sync the users' information, any groups related to the users, and any clients related to the users or groups to the duplicate instance. The way users are synced to the duplicate instance is controlled by the Group Sync Mode setting. See Step 3 - Configure your master instance .

### Special considerations

Consider the following additional information:

- Users and groups are updated depending the user or group's Last Modified On property in the master instance.

- Users are pushed to the duplicate instance in batches of 100.

- This application synchronizes Login Methods of type OpenID Connect when you configure it for that purpose, but does not sync Passwords, Authentication Providers or permissions.

- Clients and choices are automatically created in the duplicate instance.

- Choices that are part of the synchronization form the following fields: User - User Type, User - DefaultSelectedFileType, User - DocumentSkip, and Client - Status.

If any of the synced users, groups, or clients are removed on the duplicate instance, the master instance will recreate them when the agent syncs the instances again. When any of the synced users, groups, or clients are deleted from master, they won't be deleted on the duplicate instance when the agent syncs with the duplicate instance.

### Object fields that are synced to the duplicate instance

Object fields that are synced to the duplicate instance include:

User object Group object Client object Choice object

- First Name

- Last Name

- Email Address

- Type

- Client

- Relativity Access

- Document Skip

- Change Settings

- Change Document Viewer

- Keyboard Shortcuts

- Item List Page Length

- Default Selected File Type

- Skip Default Preference

- Enforce Viewer Compatibility

- Default Saved Search Owner

- Native Viewer Cache Ahead

- Document Viewer

- Name

- Client

- Users

- Name

- Number

- Status

- Name

- Order

## Viewing User and Group Synchronization information

You can view user and group synchronization information on the User Sync Information tab in both your master and duplicate instances.

The User Sync Information tab displays the Instance Relationship at the top, which shows the master-duplicate relationship. It also contains two sections below that list the users, groups, and clients being synchronized.

- Click View Details for each user to view more detailed information for each user.

- The Sync Status column for both users and groups describes whether or not the user or group was synchronized (only displayed for the master instance). If problems syncing occur for a user or group in the list, the Error link will display in the Sync Status column. You can then click on the Error hyperlink to view a pop-up modal with details of the error.

- Click the link in the # of Users column in the Groups section to view the list of users that are being synced from the selected group.

- Use the JobID for a record to locate the status of any given synchronization job in the Users and Group Sync Job Queue. See Users and Group Sync Job Queue .

## Excluding groups and clients from synchronization

To exclude groups and clients from synchronization:

- On the User Sync Information tab, navigate to one of the following sections and expand it:

- Groups

- Clients

- Select the checkbox in the Exclude column for the groups or clients to exclude from syncing.

A warning notification displays.

- For excluded groups , selecting the checkbox will delete the group on the duplicate instance if it was previously created. Every user belonging to the excluded group and the Synced Users group will be orphaned without a group on the duplicate instance if It doesn’t belong to another group on master that is synced.

- For excluded clients , selecting the checkbox will move all the users and groups associated with the excluded client to the "Default UGS Client" on the duplicate instance.

- Click Exclude to confirm your changes.

A green confirmation message appears letting you know the changes have been made.

To include the group or client that has been excluded, simply uncheck the checkbox in the Exclude column.

## Users and Group Sync Job Queue

The Users and Group Sync Job Queue tab enables you to monitor the status of jobs that the User Group Sync agent processes during a sync. You can use the standard filters and sorting for this table to find the information you need. Use the JobId from the User Sync Information tab to locate a specific job and review it's status.

The following columns are shown:

- FirstArtifactID

- Status

- Last Run

- Message

- Priority

You can use the Export to File mass operation to export the listed job data to a CSV, XLS, or DAT file.
