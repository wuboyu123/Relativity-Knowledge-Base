---
title: "User counts per workspace"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/User_counts_per_workspace.htm
collection: user
fetched_at: 2026-06-22T06:10:07+00:00
sha256: e5ee2c24e458283e51ea2510bbb2e3ab6968c79d99d950f5f8d3653aef6bf5f1
---

User counts per workspace Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# User counts per workspace

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The User Counts per Workspace solution is an environment-level script. It calculates the distinct number of standard users and system admins with access to a workspace in a Relativity instance. It performs this calculation the selected month and year.

## Before you begin

The User Counts per Workspace solution is an environment-level script. It calculates the distinct number of standard users and system admins with access to a workspace in a Relativity instance. It performs this calculation the selected month and year. It groups the results by workspace name.

### Supported versions

This solution is supported in the versions of Relativity listed in the following table.

Click on this link to download the appropriate version from the Relativity Community:

Solution version Supported Relativity version

1.0.0.1 8.2 +, RelativityOne

### Components

This solution consists of a Relativity script that runs at the environment level.

### Considerations

Review the following considerations for this solution:

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- This solution uses the same user logic as the Billing Statistics - Users script.

- The workspace name displays as EDDS followed by the workspace Artifact ID when both the following conditions occur. For example, it is listed as EDDS1015380

- The workspace has been deleted from Relativity.

- Users had access to the workspace for the selected month and year

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Preparing the workspace

This solution runs at the environment level. It reports data for all the users and workspaces in a Relativity instance. Consequently, you don't need to complete special requirements or steps to prepare workspaces to use the solution.

## Running the solution

You configure and run the User Counts per Workspace script from Home mode for the Relativity instance.

Complete the following steps to configure and run the script:

- Click the Relativity Script Library tab.

- Click the name of the User Counts per Workspace script.

- In the console, click Run Script . The script inputs page appears.

- Complete the following fields:

- Year (yyyy ) - a required text box for the requested year with the format YYYY . Input a value for the year value.

- Month (mm) - a required text box for the requested month with the format MM . Input a value for the month.

## Viewing the results

After you run the solution, the results appear as a report on the scripts page:

The following table describes the columns in the report:

Column Description

Workspace The name of the workspace.

Standard User Count The distinct count of all users who had access to the workspace during the given time period. These users aren't members of the System Admin group.

System Admin Count The distinct count of all users who had access to the workspace during the given time period. These users are members of the System Admin group.

On this page

- User counts per workspace

- Before you begin

- Supported versions

- Components

- Considerations

- Preparing the workspace

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
