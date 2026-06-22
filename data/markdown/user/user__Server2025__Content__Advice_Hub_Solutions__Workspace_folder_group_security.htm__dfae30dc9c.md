---
title: "Workspace folder group security"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Workspace_folder_group_security.htm
collection: user
fetched_at: 2026-06-22T06:17:13+00:00
sha256: 1237d1a4fa1d19f8a5991724ca6411fb65d74b702ede11ebd4300d926dbefe95
---

Workspace folder group security Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Workspace folder group security

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Workspace folder group security solution provides a script that reports on the security permissions for each folder in the Document object.

## Before you begin

### Supported versions

Click on this link to download the appropriate version from the Relativity Community. You must be logged into Community to view the information:

Solution version Supported Relativity version

1.1

Server 2021 and above

### Components

This solution consists of a Relativity script that runs at the workspace level. This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

## Deploying and configuring the solution

This solution is available as an application. If you are upgrading from a script version of the solution to an application version, you must delete the original script before adding the new application to your environment and installing it to a workspace.

To deploy the solution, you first add it to the Application Library as a Relativity application. You can then install it from the Application Library to one or more workspaces.

To add the solution to the Application Library:

- Log in to Relativity.

- Navigate to the Application Library tab.

- Click New Library Application .

- Click Select file on the Application File field.

- Navigate to and select the Application File included in the solution, and then click Open .

- Click Save to upload the file to the Application Library.

To add the solution to a workspace:

- Click Select in the Workspaces Installed section to install the application on workspaces.

- Select the desired workspaces in the Select Workspaces dialog and click Apply.

These workspaces now contain the application. Relativity lists the workspaces in the Workspaces Installed section on the detail view of the application.

## Running the solution

After preparing the workspace, you can configure and run the solution.

Complete the following steps to run the solution:

- In the workspace, navigate to the Script tab.

- Click the name of the Workspace Folder Group Security v1.1 script.

- Click Run Script .

- Click Run .

## Viewing the results

After you run the script, the results appear as a report.

The following table describes the columns in the report:

Column Definition

Folder Name The name of the folder.

Folder Path The path to the folder.

Security Inherited or Override.

Groups The user groups the folder belongs to.

On this page

- Workspace folder group security

- Before you begin

- Supported versions

- Components

- Deploying and configuring the solution

- Running the solution

- Viewing the results


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
