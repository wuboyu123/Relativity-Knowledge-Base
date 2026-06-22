---
title: "Configuring your environments"
url: https://help.relativity.com/Server2025/Content/Relativity_Unified_Experience/Configuring_your_environments.htm
collection: user
fetched_at: 2026-06-22T06:17:20+00:00
sha256: 9ad05d1f5e93ffed1535f2d6f36dfddd15cf5d1b1d1358d01153ab2293c8a5f1
---

Configuring your environments Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Configuring your environments

After installing the User Group Synchronization applications, you need to configure your environments.

To configure your environment, follow the steps in these sections:

- Step 1 - Provision your environments

- Step 2 - Configure your duplicate instance

- Step 3 - Configure your master instance

- Step 4 - Initialize the User Group Sync agent (master instance)

- Step 5 - (Optional) Set up single sign-on

For User Group Synchronization functionality to work properly, your master instance must be able to communicate with the duplicate instance over port 443.

## Step 1 - Provision your environments

To prepare for configuration:

- Copy and paste the URL of your master and duplicate instances into a text file. You will need this information later.

-

In your duplicate instance, set up and enable a user called Hybrid User with these fields:

- Name - enter Hybrid User .

- Email - enter wp@relativity.one .

- User Group Email Notifications - set to "Do Not Receive".

Do not use an "@relativity.com" email address for Hybrid User .

Hybrid User is the Relativity user account that will be used exclusively by the Relativity User and Group Synchronization and Workspace Portal applications.

-

In your duplicate instance, create a group called Hybrid Group with these instance-level security permissions.

Object Security Tab Visibility Admin Operations

- Choice - View, Add, Edit

- Client - View, Add, Edit

- Field - View, Edit

- Group - View, Add, Edit

- InstanceSetting - View

- Login Method - View, Add, Edit, Delete

- User - View, Add, Edit

- N/A

- View Admin Repository

Hybrid Group is the Relativity group that will be used exclusively by the Relativity User and Group Synchronization and Workspace Portal applications.

- In your duplicate instance, assign the Hybrid User to the Hybrid Group .

## Step 2 - Configure your duplicate instance

To configure your duplicate instance, set up an OAuth2 client to authenticate with the master instance, copy the Client ID and Client Secret strings, and then paste them into a text file for use in Step 3 - Configure your master instance .

If you already set up an OAuth2 Client for Workspace Portal and know the Client ID and Client Secret, you can use the existing OAuth2 client and skip to Step 3 - Configure your master instance .

If you have not installed Workspace Portal, use the following steps to create an OAuth2 client:

- Navigate to the OAuth2 Client tab.

- Click New OAuth2 Client .

- Enter the following fields:

- Name - enter HybridModelAuth .

- Flow Grant Type - select Client Credentials .

- Context User - select Hybrid User . See Step 1 - Provision your environments .

- Enabled - select Yes .

- Access Token Lifetime - enter 60 . While the recommended value is 60 minutes, you can adjust this value based on your needs.

- Click Save . The Client Id and Client Secret fields populate when you click Save.

- Copy the generated Client Id and Client Secret , and then paste this information into a text editor for use when configuring your master instance.

## Step 3 - Configure your master instance

To configure your master instance:

- Create a new group in your master instance called Synced Users . When users are added to this group, they will be synced to the duplicate instance along with any other groups that user belongs to.

The Synced Users group is meant to tag users to be synced to the other instance and does not need any special configuration. It should be assigned zero permissions and can be associated to any client.

- Copy the Artifact ID from the URL displayed after you create your new group. This will be entered for the Sync Group Artifact ID field during configuration.

- Navigate to the User and Group Managment > User Sync Information tab in your master instance.

- Click the Settings ( )icon in the top right corner of the tab to launch the User & Group Sync Settings pop-up window.

- Add the field properties listed in the table below to the User & Group Sync Settings pop-up window.

You must click the Change OAuth Information ( ) button to edit the Client ID and Client Secret properties (these are the values you copied and pasted in a text file during the OAuth2 client configuration in your duplicate instance).

Field Name Description

Instance URL

Enter the URL used to access the duplicate instance. This URL should be in the following format: <protocol>://<hostname>/Relativity

Sample: https://relativity.customer.com/Relativity

Sync Group Artifact ID

The value is the Artifact ID of the Synced Users group you created that can be linked to users you want synchronized. See Step 2 for Step 3 - Configure your master instance . This determines what users get synced. Additional groups linked to those users also will be synced. However, groups tied to users that don't belong to this Synced Users group will not be synced.

Group Sync Mode

Group Sync Mode affects behavior when the application encounters a group with the same name in master and duplicate. Make one of the following selections to specify group sync behavior:

-

Merge - merge the users into the existing group in the duplicate instance.

For migrations, use the Merge option.

- Use Master - remove users from the existing group in the duplicate instance and add the users which are part of this group in the master instance.

- New Group - do not modify the existing group and add a new group with “_remote” as suffix in the duplicate instance. Users which are part of this group on the master instance are added to the new group with the suffix in the duplicate instance.

- Keep Current - only synchronizes new elements from the master instance to the duplicate instance if the new element did not previously exist in either the master or duplicate instance. For example, if a user created in the master instance already exists in the duplicate, the Relativity User and Group Synchronization application will not synchronize or modify this user in the duplicate instance.

Client ID

Paste in the Client ID generated from the OAuth2 Client you created in your duplicate instance. See Step 1 under Step 2 - Configure your duplicate instance .

Client Secret

Paste the Client Secret generated from the OAuth2 Client you created in your duplicate instance. See Step 1 under Step 2 - Configure your duplicate instance .

## Step 4 - Initialize the User Group Sync agent (master instance)

To create a User Group Sync agent in your master instance:

- In your master instance, navigate to the Agents tab.

- Click Create a New Agent .

- Set the agent type to User Group Sync Agent and leave the rest of the settings as default. This agent is responsible for the synchronization from master to duplicate.

- Save the new agent. Your User and Group Synchronization configuration is now complete.

For every 350 users that you will be syncing, we recommend adding an additional User Group Sync agent (e.g., add a second agent when you have 350+ users or a third agent when you have 700+ users).

See .

## Step 5 - (Optional) Set up single sign-on

Setting up single sign-on is an optional step. You do not need single sign-on to use User and Group Synchronization.

Single sign-on (SSO) considerations include:

- OpenID Connect Authentication Provider Name (master instance) - this is the authentication provider you set up for single sign-on. This is only required if you want to sync login methods.

- OpenID Connect Authentication Provider Name (duplicate instance) - this is the authentication provider you set up for single sign-on. This is only required if you want to sync login methods.

- SSO setup on both master and duplicate (recommended) - set up single sign-on (SSO) in both your master and duplicate instance to allow you to navigate between these instances without having to use two sets of credentials. See

-

Sync login methods - add the OpenIDLoginMethodsMatch instance setting to your master instance.

If you do not have proper permissions to add instance settings (e.g., RelativityOne is your master), contact ﻿ Relativity Support .

To add the instance setting:

- Navigate to the Instance Setting tab.

- Add and save the following instance setting. Leave Machine Name blank.

Section Name Value

kCura.UGS OpenIDLoginMethodsMatch

You must now match the OpenID Connect Authentication Provider Name on the master instance with the corresponding OpenID Connect Authentication Provider Name on the duplicate instance for each login method you want to sync:

The authentication provider name values should be entered on separate lines for each matched up login method:

{OpenID Connect authentication provider name on master instance}::{OpenID Connect authentication provider name on duplicate instance}

{Additional OpenID Connect authentication provider name on master instance}::{Additional OpenID Connect authentication provider name on duplicate instance}

Sample:

OIDLogin1::OIDLoginOktaLogin

OIDLogin2::GoogleLogin

- The instance setting name and values are case sensitive, and the values must match exactly to their corresponding authentication provider.

- The authentication provider name specified for the duplicate instance must already exist in the duplicate instance for this to sync login method information. If an authentication provider is configured but doesn't exist or its type is not OpenID Connect (master or duplicate), synchronization won't occur and an error in the Errors tab will appear. For Relativity 9.7.229.5 and below, perform an IIS Reset on all web servers, so that proper configuration changes can take place for setting up your provider. For RelativityOne , and Relativity 10.0.318.5 and above , your changes take effect immediately, and you don't need to reset the IIS.

On this page

- Configuring your environments

- Step 1 - Provision your environments

- Step 2 - Configure your duplicate instance

- Step 3 - Configure your master instance

- Step 4 - Initialize the User Group Sync agent (master instance)

- Step 5 - (Optional) Set up single sign-on


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
