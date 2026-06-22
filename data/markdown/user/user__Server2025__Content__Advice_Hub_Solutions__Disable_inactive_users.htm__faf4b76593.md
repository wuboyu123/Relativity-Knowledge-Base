---
title: "Disable inactive users"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Disable_inactive_users.htm
collection: user
fetched_at: 2026-06-22T06:10:10+00:00
sha256: bd131379b585463b05fe3f7a6c2ede362337f2d156f7ba65018ddd2ffa394dc4
---

Disable inactive users

# Disable inactive users

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Disable Inactive Users solution generates a report listing report of inactive users. It can also disable inactive users based on selected criteria.

### Supported versions

This solution is supported in the following Relativity Server versions and RelativityOne.

Solution version Supported Relativity version

Disable Inactive Users (Relativity v10.3+) 10.3 - Server 2025, RelativityOne

## Before you begin

The Disable Inactive Users solution disables users considered inactive. You can run the solution in safe mode to view users who would be disabled without actually disabling them. To view these user, select Yes in the Run in Safe Mode field.

Inactive users meet the following criteria:

- The user belongs to the selected user type.

- The user currently has access to workspaces that are associated with a specific client, if one is selected.

Inactive users meet at least one of the following criteria:

- The user has existed for more than the specified number of days. The last login date was more than a specified number of days ago.

- The user has existed for more than the specified number of days. The user has never logged in to Relativity.

The Disable Inactive Users solution won't disable system accounts so that at least one user can always log in to Relativity. In Relativity Server, the Relativity service account and admin accounts won't be disabled.

### Supported versions

This solution is supported in the versions of Relativity listed in the following table.

Solution version Supported Relativity version

8.0 Server 2025

### Components

This solution consists of a Relativity script that works at the environment level.

### Considerations

Review the following considerations for this solution:

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- The script creates an audit record for each user that it disables. The personal items for disabled user remain private.

- The timeout value is currently set to 20 minutes. If a timeout error occurs when executing the script, increase the timeout value by editing the following line: timeout = "1200". The timeout value is in seconds, so 1200 equal 20 minutes.

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

This solution runs at the environment level. It reports data for all the users and workspaces in a Relativity instance. Consequently, you don't need to complete special requirements or steps to prepare workspaces to use the solution.

## Running the Solution

You configure and run the Disable Inactive Users script from Home mode for the Relativity instance.

Complete the following steps to configure and run the script:

- Click the Relativity Script Library tab.

- Click the name of the Disable Inactive Users script.

- In the console, click Run Script . The script inputs page appears.

- Complete the following fields:

- Run in Safe Mode - Required. Select Yes to run the script runs without disabling users. The script displays a report listing the users who meet the input criteria. If you run the script outside Safe mode, it disables these users.

- User Type - Required. When the script executes, it disables this type of users. You can run this script on internal, external, or a custom user type added through the Choice Editor.

- User Created More Than (Days) - Required. The minimum number of days the user must have existed. For example, enter 30 to disable users who were created more than 30 days ago. This data isn't inclusive. The solution returns data for days greater than the input values. For example, return data on users created on the same day that you run the script by entering (0). If you enter (-1), an error occurs.

- Last Login Date More Than (Days) - Required. The minimum number of days the user hasn't logged in to Relativity. For example, enter 30 to disable users whose last login date was over 30 days. This data isn't inclusive. The solution returns data for days greater than the input values.For example, return data on users created on the same day that you run the script by entering (0). If you enter (-1), an error occurs.

- Client - Optional. Select a client to disable inactive users from all groups only in workspaces, which are associated with this client.

- Click Run .

## Viewing the results

After running the Disable Inactive Users script, the results appear as a report on the script page. When you execute the script in Safe mode, the report includes all users who meet the selected criteria. When you execute the script outside Safe mode, the report includes all users who were disabled by the script.

The following table describes the columns in the report:

Column Description

User Artifact ID Artifact ID of the user who will be disabled.

First Name First name of the user who will be disabled.

Last Name Last name of the user who will be disabled.

Email Address Email address of the user who will be disabled.

User Created Date Date that the user was created in Relativity.

Last Login Date Date that the user last logged in to Relativity.

Client The client the user belongs to.

Group A semi-colon delimited list of groups the user belongs to.

Workspace A semi-colon delimited list of workspaces the groups the user belongs to have access to.

Action Displayed only in Safe Mode. Indicates the results of running this script on a specific user.
