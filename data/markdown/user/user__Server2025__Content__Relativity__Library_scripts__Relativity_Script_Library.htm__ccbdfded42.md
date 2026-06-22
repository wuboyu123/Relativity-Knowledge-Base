---
title: "Relativity Script Library"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Relativity_Script_Library.htm
collection: user
fetched_at: 2026-06-22T06:07:03+00:00
sha256: d20df2676f730c52ddf95c1453131151463501dd84dad43f046aeccf6697b561
---

Relativity Script Library Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Script Library

The following is a list of standard scripts available in Relativity. This list may vary per version of Relativity.

These scripts are available in the Relativity Script Library. To access the script library:

- Navigate to Home .

- Click the Relativity Script Library tab.

To add library scripts to your Script tab in a workspace for your users to run, see Scripts .

Changes to SQL fields executed by Relativity Scripts do not produce Audit logs.

Script Description

Analytics billable estimate

Allows a partner to assess the billable size of a potential Analytics index submission.

Billing statistics - case rollup

Reports on peak billable data for all cases in a Relativity environment; this can be used in environments where the auto-emailed statistics feature is not possible.

Billing statistics - users

Reports on all users who have had access to the case at any time during the month.

Case permission audit report

Reports on all users, workspaces, groups, and each group's permissions in a Relativity environment.

Choice field stratified sampling Selects a specified number of sample documents across categories chosen by the user, ensuring that each category is represented equally.

Create Cluster Upgrade Jobs

Creates job entries in the EDDS database to upgrade Analytics clusters for CAAT 3.17.2. This was introduced in Relativity 9.2.271.9.

Create sample set

Randomly samples documents from a saved search to create a sample set

dtSearch index auto incremental build Incrementally builds all dtSearch indexes in all cases.

Forgotten password reset audit

This Relativity script provides audit records for user password reset requests generated using the Forgot your password? link on the login screen.

Globally administer keyboard shortcuts

Forcibly assigns a keyboard shortcut to a specific system function; this script runs against all workspaces.

Monitor Cluster Upgrade Jobs

Checks and reports the status of all Analytics cluster upgrade jobs recorded in the EDDS database.

Populate parent ID to child

Populate parent to child is a workspace-level script propagates the Document ID of the parent document to any children of that document.

Processing statistics

Provides a report of processed data sizes per processing set and user in all workspaces in the environment and a summary of all processed data in all workspaces in the environment.

Propagate sent date to family documents Sets all email families' documents to the same sent date as their parent documents in a case.

Relativity SMTP configuration

Sets up the available SMTP fields in the kCura.Notification section of the Instance setting table.

Report sample-based statistics Generates reports for the deprecated sample-based learning feature.

Reviewer statistics

Reports on the efficiency of reviewers over the specified date range; the returned statistics provide a count on how many documents were reviewed over a certain period of time.

Saved search gap and overlap check Identifies documents with gaps in Bates numbers or overlapping Bates numbers in a workspace.

Set duplicate flag field

Identifies and sets a Yes/No field on all case documents to indicate it as a duplicate or master.

Set extracted text size field Stores a document's extracted text data length (in Kilobytes) in a decimal field for all documents in a case.

Set native file size field Stores the native file size (in KB), for each case document in a decimal field.

Set production beg/end attach fields

Populates the production beginning and end attachment range fields for each case document included in a production.

Set Relativity folder path field

Stores the current Relativity folder path of each document in a long text field.

Upgrade legacy applications

Upgrades a legacy application (v 6.8 and earlier) to a Relativity Application object

Workspace status report

Reports on the last action performed by a non-system admin in each workspace in a Relativity instance.

The Relativity Script Library includes all scripts installed with your version of Relativity. To request additional scripts, contact Customer Support .

The following scripts are available outside the script library:

Script Description

Australian Document ID

Renumbers your Relativity documents and Host/Family fields into a standard Prefix, Box, and Document format.

Case Dynamics Pre-Entity Integration Script

Aims to detect possible upgrade conflicts, data truncation, and customization on the Person and Organization objects that may need to be re-created on the Entity object during a Case Dynamics upgrade.

Moving dtSearch indexes Moves a dtSearch index from one location to another

Moving Analytics indexes and structured analytics sets Moves an Analytics index from one location to another

Get database size

Displays size and location information for all database files in a specific workspace. Use the following SQL command to run this script:

exec sp_helpdb <databaseName>

On this page

- Relativity Script Library


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
