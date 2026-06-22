---
title: "User workspace access and last login"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/User_workspace_access_and_last_login.htm
collection: user
fetched_at: 2026-06-22T06:10:08+00:00
sha256: f5c4b03f1c6c75f3cbe8a6b1f7d1e21334fbc7ab2aec38eb4483bfcbe9f1556f
---

User workspace access and last login Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# User workspace access and last login

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The User Workspace Access and Last Login solution generates a report of enabled users, during a listed month, that had access to Relativity at the listed time. The report lists those specific users along with the associated groups and workspaces, the time of their last login, and their current Relativity Access flag value.

Use the links in the Supported versions section to download the solution from the Relativity Community.

## Before you begin

The User Workspace Access and Last Login solution generates a report by looking up all users that accessed Relativity during the month and year added to the Inputs pop-up modal. The solution then lists the following information for each of those users:

- Current workspace access

- Last login date

- Current Relativity Access flag value

### Supported versions

You can find all versions of this solution on the Community via this User workspace access and last login search string . You must be logged in to the Community for that string to return results.

### Category

This solution consists of a Relativity script that runs in Home mode for the Relativity instance.

### Considerations

Review the following considerations for this solution:

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- The solution reports on users listed in the Billing Agent table. This table is updated once a day during agent off hours. If you add users today, the report won't include them until the next time the Billing Agent runs.

- If a user doesn't belong to any workspaces, report won't include the user.

- The solution doesn't record historical workspace access. It reports only on workspaces that users can access on the date and time when the script runs.

- This solution can't be run by client domain admins (multi-tenancy) and Data Grid features of Relativity .

- The report doesn’t include any workspaces that have been deleted. Any information about deleted workspaces won’t be included in the report.

- The report doesn’t include any users that have been deleted. The report won’t include any information about workspaces accessed by these users.

- The report doesn't include users in the System Administrator group.

- The report includes only users who log in during the month selected.

## Deploying and configuring the solution

This script runs from the Admin level, you must install this application into a workspace for it to appear in the Script Library (at the instance level).

## Running the solution

You configure and run the User Workspace Access and Last Login script from Home mode for the Relativity instance.

Complete the following steps to configure and run the script:

- Click the Relativity Script Library tab.

- Click the name of the User Workspace Access and Last Login script.

- In the console, click Run Script . The script input page appears.

- Complete the following fields:

- Month (mm) - Enter a two-digit numerical value for the month.

- Year (yyyy) - Enter a four-digit numerical value for the year.

- Display Active Users Only - Select 'Yes' or 'No' to hide inactive users.

- Click Run .

## Viewing the results

After running the User Workspace Access and Last Login script, the results appear as a report on the script page.

The following table describes the columns in the report:

Column Description

Workspace Name The display of the workspace depends on the input selections:

- If you select User in the Group By field, this column displays a semi-colon delimited list of all workspaces that the user can currently access.

Client Name The name of the client associated with the user.

Matter Name The name of the matter associated with the user.

User Name The name of the user. It use the format Last name, First name .

User Artifact ID The Artifact ID of the user.

Email Address The email address of the user.

Group Name A semi-colon delimited list of groups the user is associated with in the workspace.

User Type The choice value of the user in the Type field.

Relativity Access The user’s current Relativity Access. It displays as Enabled or Disabled.

Date of Last Login The most recent date that the user logged in to Relativity. For a single user, this field is the same across all workspaces.

Relativity Access Last Updated The most recent date and time when the Relativity Access field was changed for each user.

User Status When the script runs, it populates this column with the word Duplicate if same email address is associated with more than one workspaces.

On this page

- User workspace access and last login

- Before you begin

- Supported versions

- Category

- Considerations

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
