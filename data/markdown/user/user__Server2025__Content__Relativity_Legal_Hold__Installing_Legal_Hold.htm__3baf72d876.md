---
title: "Installing Relativity Legal Hold"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Installing_Legal_Hold.htm
collection: user
fetched_at: 2026-06-22T06:04:04+00:00
sha256: 9664e6b52f7d503c3a0368426e4beff05c3beb91bebc4420d485e362b357484c
---

Installing Relativity Legal Hold

# Installing Legal Hold

To use Relativity Legal Hold, you need to install the Relativity Legal Hold application to one or more workspaces.

For more information on prerequisites, technical requirements, and other considerations, see the links below.

-

Collecting required email settings information

-

Adding preservation hold settings using Modern Authentication

-

Relativity Legal Hold

For customers who are using Relativity Legal Hold to manage their own legal holds, it is recommended to install the program to one workspace. This allows for the consolidation of reporting and monitoring custodian interactions across all the organization’s legal holds. If you are installing Relativity Legal Hold to take advantage of the communications and acknowledgments feature, it is recommended to put this in a workspace separate from your legal hold workspace. If you offer Relativity Legal Hold as a service for you clients, it is recommended to separate the workspaces per client.

Use the following procedures to install Legal Hold:

- Install the Relativity Legal Hold application from either the Application Library or an external file. See Installing Legal Hold .

- Add the Legal Hold Agent. See Adding the Legal Hold agent .

- Configure Legal Hold. See Installing Legal Hold .

## Installing Legal Hold

Relativity Legal Hold is only compatible with Relativity. See the Relativity Pre-installation overview for requirements. For a Relativity Legal Hold-only installation, the Relativity Base Template is recommended as the following features are not required:

- Analytics server setup

- Database server for processing or native imaging

- Worker server for processing or native imaging

- Obtaining applications for native imaging and processing

Since Relativity Legal Hold uses the ADS framework, you have the following options available for installing Relativity Legal Hold in your environment:

### Install Legal Hold from the Application Library

If you add the Relativity Legal Hold application to the Application Library, you can install it to the current workspace from the Application Library. See Relativity applications .

- Navigate to the workspace where you want to install the application.

- Navigate to the Relativity Applications tab.

- Click New Relativity Application to display an application form.

- Click the Select from Application Library radio button in the Application Type section.

- Click in the Choose from Application Library field.

- Select Relativity Legal Hold on the Select Library Application dialog. This dialog only displays applications added to the Application Library. If Relativity Legal Hold is not included in the list, see Installing applications .

- Click Ok to display the application in the Choose from Application Library field. The application form also displays the following fields:

- Version —displays the version of the application that you are installing.

- User-friendly URL —displays a user-friendly version of the application's URL. This field may be blank.

- Application Artifacts —displays object types and other application components.

- Map Fields —there are no fields available in Relativity Legal Hold for mapping.

- Click Import to install Legal Hold into the workspace.

- Review the import status of the application. Verify that the install was successful or resolve errors. See Viewing import status and Troubleshooting application installation errors .

## Adding the Legal Hold agent

After you install Relativity Legal Hold, add the Relativity Legal Hold Agent by going to the Agents tab in the Admin level and clicking New Agent . Add at least one Legal Hold agent and one Legal Hold Preservation agent, if using preservation holds, per environment. Add more as needed.

Verify the Enable column displays Yes for the Relativity Legal Hold Agent. See Adding and editing agents .

Agent name Requirement information Function Agent type

Relativity Legal Hold Agent

At least one per environment.

You can add more agents to allow simultaneous jobs to run, and batch large email jobs, after exceeding the default 1,000 email threshold. You may also need more agents if you frequently multitask several Legal Hold actions at once. For example, project deletions and send emails.

Sends emails (including reminder and escalation), pulls emails in from custodian responses and purges custodians from a project. Multiple-installation

Relativity Legal Hold Preservation Agent

At least one per environment.

If multiple preservations are to be created, create more than one preservation agent.

Performs all Microsoft 365 Preservation-related work.

The agent creates an Microsoft 365 eDiscovery Case, holds and assigns mailboxes and OneDrive URLs of corresponding Custodians. The agent job removes corresponding Custodians from Micsofot 365 Hold.

Agent job deletes corresponding Microsoft 365 Case when Project is closed.

Agent job collects information about existing legal hold and Microsoft 365 holds and updates state and property information in Legal Hold.

Agent job sends alert per settings if any modifications found on Microsoft 365 site which does not correspond to Relativity Legal Hold settings.

Agent job sends emails per settings if Custodian is placed/removed on/off Hold.

Agent job for preservation in place manager is created on application install or upgrade and refreshed when Preservation Case Environment RDO is saved to update Agent run interval.

Multiple-installation

### Configuring Legal Hold

Before configuring Legal Hold, gather your SMTP information. For more information, see Legal Hold SMTP information .

To configure Legal Hold, access the Legal Hold Settings tab. For more information, see Adding legal hold settings .

## Post-installation verification test

As a best practice, you should confirm that your Legal Hold application is functioning properly after an initial installation or an upgrade. We provide step-by-step instructions in the following Word document for performing a post-installation verification test in your Relativity environment.

Click here or the following image to download the Relativity Legal Hold Post-Installation Verification Test document.
