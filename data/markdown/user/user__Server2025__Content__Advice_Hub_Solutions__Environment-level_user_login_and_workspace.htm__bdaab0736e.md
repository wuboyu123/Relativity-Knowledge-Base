---
title: "Environment-level user login and workspace"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Environment-level_user_login_and_workspace.htm
collection: user
fetched_at: 2026-06-22T06:10:03+00:00
sha256: 82cd850268f2d000e79fa1e4ea70a7a79663e55341d0186cc1fd1533409c713d
---

Environment-level user login and workspace

# Environment-level user login and workspace access

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Environment-Level User Login and Workspace Access solution reports data about login and access actions that individual users performed in a Relativity instance during a time period that you specify.

This script in RelativityOne is not fully supported, so it might only return partial results based on the selected date range. A wider date range increases the likelihood of receiving partial results. This occurs because the script relies on Audit SQL table records , which are continuously migrated to the Data Grid.

## Before you begin

The Environment-Level User Login and Workspace Access solution queries and reports data about login and access actions that individual users performed in a Relativity instance during a time period that you specify. For each user who logged in during the specified time period, the data includes:

- The action that the user performed, specifically logging in to the Relativity instance or navigating to a document view in a workspace.

- Each date and time when the user logged in to the Relativity instance.

- Each date and time when the user navigated to a document view in a workspace, along with the name and Artifact ID of the workspace.

You can sort and filter the data in the report.

### Supported versions

This solution is supported in the versions of Relativity listed in the following table.

Solution version Supported Relativity version

2.6.0 8.2 and above

### Components

This solution consists of a Relativity script that runs at the environment level.

### Considerations

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- This solution doesn't report user login or access data for the relativity.admin@kcura.com or relativity.serviceaccount@kcura.com accounts.

- Solution performance depends primarily on the number of users and workspaces in the Relativity instance. When tested in an environment with 241 users and 188 workspaces, the solution ran in 1 minute 30 seconds.

- The default timeout value for running the solution is 20 minutes (1,200 seconds). If you receive a timeout error when running the solution, you can increase the timeout value by changing it from 1200 to a higher value directly in the solution script.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Deploying and configuring the solution

To deploy the solution, you first add it to the Application Library as a Relativity application. You can then install it from the Application Library to one or more workspaces.

This script runs from the Admin level, you must install this application into a workspace for it to appear in the Script Library (at the instance level).

To add the solution to the Application Library:

- Log in to Relativity.

- Navigate to the Application Library tab.

- Click New Library Application .

- Either click Select File, or drag and drop the file into the Application.

- Navigate to and select the application file included in the solution, and then click Open .

- Click Save to upload the file to the Application Library.

To add the solution to a workspace:

- In the Workspaces Installed section, click Select to install the application to one or more workspaces.

- Select the workspace(s) where you want to install the application, and then click the Move selected left to right icon.

- Click Apply .

The application is installed to the selected workspace(s). A list of workspace(s) where the application has been installed displays in the Workspaces Installed section.

## Preparing the workspace

Because this solution runs at the environment level and reports data for all the users and workspaces in a Relativity instance, there are no special requirements or steps to prepare any workspaces to use the solution.

## Running the solution

To run the solution, you need to configure and run the Environment Level User Login and Workspace Access script from Home mode for the Relativity instance.

To configure and run the script:

- On the Relativity Script Library tab, click the name of the Environment Level User Login and Workspace Access script.

- In the console, click Run Script . This brings up the script inputs dialog.

- Next to the Start Date field, click , and then select the earliest date for the data that you want to include in the report.

- Next to the End Date field, click , and then select the latest date for the data that you want to include in the report.

- Click Run .

A progress window displays the execution status of the script. After the script finishes running, the script layout displays the results.

## Viewing the results

After you run the Environment Level User Login and Workspace Access script, the results appear as a report on the script layout. The report includes detailed information about actions that users took during the date range that you specified when you configured the script.

In the report, rows are organized first by a specific date, time, and user, and then by the action that the user took. If a user didn't log in to Relativity or access a workspace during the date range that you specified, the report doesn't include any data for the user.

If a user navigated to a workspace but didn't navigate to a document view in the workspace during the specified date range, the report doesn't include any workspace access data for the user. To qualify as workspace access, a user must navigate to a document view in a workspace, as recorded on the History tab under an action of Document Query for an object type of View or Workspace.

The following table lists and describes the columns in the report.

Column Description

Date The date when the action occurred. The display format is "MM/DD/YYYY".

Time The time when the action occurred. The display format is "hh:mm:ss".

User The name of the user who performed the action. The display format is "First Name Last Name".

Action The type of action that the user performed at the specified time:

- Log in - The user logged in to the Relativity instance.

- Workspace Accessed - The user navigated to a document view in the workspace identified in the Workspace Name and Workspace Artifact ID columns.

System The type of resource that the user accessed:

- Relativity - The user logged in to the Relativity instance.

- Blank - The user navigated to a document view in the workspace identified in the Workspace Name and Workspace Artifact ID columns.

Workspace Name The name of the workspace that the user accessed, if the user navigated to a document view in the workspace. If the user only logged in to the Relativity instance, this field is blank.

Workspace Artifact ID The Artifact ID of the workspace that the user accessed, if the user navigated to a document view in the workspace. If the user only logged in to the Relativity instance, this field is blank.
