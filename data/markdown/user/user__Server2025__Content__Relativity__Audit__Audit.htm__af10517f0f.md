---
title: "Audit"
url: https://help.relativity.com/Server2025/Content/Relativity/Audit/Audit.htm
collection: user
fetched_at: 2026-06-22T06:06:31+00:00
sha256: 7aed8a2cfae216e122a41e2451e444fd986222e522fa7ad2f09aa42e7b78f399
---

Audit Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Audit

Audit is an application that you can use to monitor and run reports on audited user activity. With Audit, you can use pivots and visualizations to quickly identify audit activity in your Relativity instance.

Some of the benefits of using Audit include:

- Building multiple widgets and lists to create custom dashboards for reporting.

- Viewing audit records that occur at the instance level through the Relativity UI.

- Easily searching through millions of audits to identify actions ranging from reviewer coding decisions to users logging in and out of Relativity for monitoring activity

- Quickly exporting audits to meet stakeholder requests for reporting on user activity in Relativity.

For information about common Audit workflows, see Reporting and Monitoring using Audit .

You must have Elasticsearch configured to use the Audit application. See Elastic Stack system requirements for more information on setting up the preliminary requirements.

## Supported Audit tab functionality

The following lists supported and unsupported functionality on the Audit tab as compared to the history tab.

Supported functionality Currently unsupported functionality

- ARM – Archive & Restore

- Dashboards

- Group By/Pivot On functionality (limited number of fields)

- Item list

- Filtering

- Views

- Widgets

- Reverting/mass revert document edits

- Error reporting

- Exporting data from lists

- Exporting dashboard widgets as image

- Custom scripts

- Export of dashboards

- Exporting from the History tab

## Installing and configuring Audit

In order to use Audit, you must complete the following:

- Install and configure Elasticsearch. For more information, see Installing Elastic Stack .

- Install the Audit application to your workspace(s). For more information on installing applications, see Installing applications .

- Install the Audit agents. See Audit agents .

### Audit agents

The Audit application includes the agents described below:

Agent name Requirement information Function Agent type

Data Grid Audit Migrator Only 1 per core on the agent server. Up to 16 agents per environment. A Data Grid Audit Migrator agent migrates audit data from SQL to Elasticsearch for any workspace that has Audit installed. The frequency with which this agent checks for migrations and runs the migrations is controlled by the agent run interval value. Multiple-installation

Data Grid Audit Deleter 1 per environment required. Up to 4 agents per environment.

The Data Grid Audit Deleter agent is an off-hour agent that deletes all audits from SQL that have been successfully migrated to Elasticsearch. Along with un-migrated audits, it will leave other existing audits in SQL for a configurable number of days for billing purposes.

Single-installation

Data Grid Audit Reporter (Optional) 1 per environment The Data Grid Audit Reporter agent reviews the audit queue for errors that occurred during migration from SQL to Elasticsearch. This agent triggers a Relativity error based on the agent's run interval. This agent is set to an hourly run interval by default. Single-installation

Data Grid Audit Manager Only 1 per environment Populates filters in the Audit application. Single-installation

Data Grid Manager Only 1 per environment

A Data Grid Manager agent is an off-hours agent responsible for Data Grid enabled workspace management, including deleting outdated search results cache tables and monitoring Data Grid index conditions.

If you've already installed this agent with Data Grid installation, you don't need to add another.

Single-installation

For more information on installing agents, see Adding and editing agents .

## Audit tab

You can use the Audit tab to build custom widgets and design dashboards to meet workflow needs by utilizing the same Group By and Pivot On functionality available in Relativity. The default view on the Audit dashboard shows the last 7 days of Audit activity.

You can't add the Security, Edit, Name, System Last Modified On, System Last Modified By, System Created By, or System Created On fields to an Audit list view. In addition, you should not add the Artifact ID field to any views from the Audit tab.

The following functionality is also available:

- Searching on Field, Old Value, and New Value columns in list view.

- Creating and customizing views on the Audit tab.

- Applying filters and conditions to sort through audit records.

- Exporting audit data from list views and widgets.

If the Audit tab does not load any data and instead displays a query error, you may need to manually add the AdditionalSortBy instance setting and set its value to ID.Keyword.

### Searching on the Details column

To display the query text of an audit record, click in the Details column for that record. You can toggle between a table view and JSON view of audit details.

### Exporting workspace audits

Exporting audits is not available at the instance level.

You can export audit data from list views and widgets. The export respects the data made on the filters in the list view, and the results are filterable.

When you export audit data, the Field, Old Value, and New Value are not included in the output.

To export audit data, complete the following:

- From the mass operations bar, click Export .

- Select the format you want to export your audits in (either .csv or .xlsx).

- Click Run .

Currently, when you sort on the Audit table and then export it, the sort order you specified is not retained. Only filter conditions are retained when you export.

## Instance audits

The Audit tab is available at the instance level upon upgrade. You must have Elasticsearch installed and configured to use the Audit tab. If you don't have Elasticsearch installed, you can hide this tab. For information about hiding tabs, see Tabs .

You must be a system admin to view audits at the instance level.

The Audit tab functions the same at the instance level. You can build custom widgets and design dashboards by utilizing the same Group By and Pivot On functionality available in workspace audits. However, exporting audits is not available. For a list of admin-level audited actions, see Audited actions .

### Filtering on multi-workspace audits

System admins can view workspace audits at the instance level.

You can filter on the Workspace Name column to view audits for specific workspaces. By default, the Audit application displays audit information for the first 10 workspaces, sorted by Artifact ID. You can configure this number using the MaxAggregatedWorkspaces instance setting.

### Mass reverting

System admins can also mass revert audits. Mass reverting is only available at the workspace level.

You can only mass revert the Document Update, Mass Update, or Propagate action, and it only applies to the latest action on the Document object. You can only mass revert on the following field types:

- Currency

- Decimal

- Single choice

- Single object

- Whole number

To mass revert:

- From the mass operations bar, select Revert in the drop-down menu.

By default, the maximum number of audits you can run the mass revert operation on at one time is 5000. If you attempt to run mass revert on more than 5000 audits, you'll receive a warning message. You can decrease the maximum number of audits using the RevertMaxAuditCount instance setting. Do not increase this instance setting value past 5000.

- Audit scans the list of audits to determine how many are revertible. Once it finishes, click Run .

- Click Close to close the pop-up window.

As when you revert a single audit, a new audit record is created for each reverted audit.

## Audit Migration Reports tab

The Audit Migration Reports tab provides you with the option of generating a migration error and migration status report for you to monitor the status of audit data as you migrate it into Elasticsearch. You also have the option of running a migration error retry script.

### Migration Error Report

The Migration Error Report generates a report that provides information on all errors that have occurred while migrating audit data into Elasticsearch, including batch and document errors.

You can also run this script on all environments in your workspace from the Relativity Script Library tab. Click the user drop-down menu in the upper-right corner of Relativity, and then click Home. Navigate to the Applications & Scripts > Relativity Script Library tab, and then search for the name of the script.

To preview the script, select the radio button for this script and click Preview . To run this report, click Run . The following results populate the bottom of the window.

Audit automatically retries certain audit migration errors, like SQL timeouts, invalid XML, and inability to connect to Elasticsearch. With this improvement, the migration error report may display a total of 0 errors because the system automatically retried and resolved those common errors. In this situation, there is no need to run the Migration Error Retry Script.

- Total Error Counts - this section provides a summary of all errors that occurred during migration.

- Batch Errors - lists the total number of batch errors that occurred during migration.

- Document Errors - lists the total number of document errors that occurred during migration.

- Batch Errors - this section provides a summary of all batch errors that occurred during migration.

- Batch ID - lists the batch ID number of the batch that received an error.

- Audit ID Range - lists the first and last Audit ID numbers contained in the batch that received an error.

- Time Stamp - lists the time at which the error occurred.

- Error Message - lists the text of the batch error.

- Document Errors - this section provides a summary of all document errors that occurred during migration.

- Audit ID - lists the audit ID number of the document that received an error.

- Batch ID - lists the batch ID number of the batch in which the document that received an error was contained.

- Time Stamp - lists the time at which the error occurred.

- Error Message - lists the text of the document error.

### Migration Error Retry Script

After identifying errors with the Migration Error Report, an admin can investigate and fix specific audit issues. Once the issues have been fixed, this script will resubmit audit records with errors to be migrated into Elasticsearch.

You can also run this script on all environments in your workspace from the Relativity Script Library tab. Click the user drop-down menu in the upper-right corner of Relativity, and then click Home. Navigate to the Applications & Scripts > Relativity Script Library tab, and then search for the name of the script.

In the Error type to retry drop-down list, select from the following options:

- Batch Errors - retries all batches with errors as reported in the Migration Error Report.

- Document Errors - retries all documents with errors as reported in the Migration Error Report

- All Errors - retries all batch errors and document errors as reported in the Migration Error Report.

Click Preview to see a sample of the report, or select the appropriate option and click Run to execute the script.

### Migration Status Report

The Migration Status Report generates a report that shows the progress of the migration of audit data into Elasticsearch. This includes audits in SQL, audits pending migrations, and migration errors. To preview the script, select the radio button for this script and click Preview .

Click Run to generate this report and display the following information:

- Audits in SQL - lists the number of audits in the SQL database.

- Audits Pending Migration - lists the number of audits in queue for migration into Data Grid.

- Migration Errors - lists the number of errors that occurred during migration.

## Audit Workspace Settings tab

Use the Audit Workspace Setting tab to configure settings specific to the Audit application. The Audit Workspace Setting tab contains two settings, DisplayAuditDataSource and HistoryTabVisibleOnUpgrade.

You must have permission to view this tab in order to configure the setting.

### DisplayAuditDataSource

The DisplayAuditDataSource setting configures whether Relativity displays audits from SQL or Data Grid on the document history pane in the viewer and the View Audit button on object layout pages.

If you set audits to display from Data Grid, there may be a slight delay in viewing the most recent audits. A "Last Updated" value next to audits indicates the last time all audits were verified as migrated for that object. This let's you know that several of a document's most recent audits might not be migrated yet.

You can configure the DisplayAuditDataSource setting with one of three values:

- 0 - displays audits from SQL until the first point that the audit migration has no more audits to migrate. At this point, the system automatically updates this value to "1," and audits are displayed from Data Grid going forward.

- 1 - displays audits from Data Grid only.

- 2 - displays audits from SQL only.

By default, DisplayAuditDataSource is set to display audits from SQL only. To configure DisplayAuditDataSource ,click the Edit link and modify the Value field in the subsequent layout.

### HistoryTabVisibleOnUpgrade

The HistoryTabVisibleOnUpgrade tab configures whether the History tab is visible when upgrading the Audit application.

You can configure the HistoryTabVisibleOnUpgrade setting with one of two values:

- True - displays the History tab upon upgrade.

- False - hides the History tab upon upgrade.

By default, the HistoryTabVisibleOnUpgrade setting is set to hide the History tab when upgrading the Audit application. To configure HistoryTabVisibleOnUpgrade, click the Edit link and modify the Value field in the subsequent layout.

## Audited actions

The following table lists audited actions in Relativity:

If you perform a job while previewing a user's security settings, the audit action will be credited to your username and not to the user whose security you were previewing when you started the job.

Action name Description of activity

CaseMap - Add Document A document was sent to CaseMap.

CaseMap - Add Fact A selection of text from the viewer was sent to CaseMap as a fact.

Conversion Complete A file was converted by way of a user clicking on a file link in the document list, running an imaging set, imaging on the fly, running a mass image operation, or switching to text or production mode in the viewer.

Create An item was created.

Delete An item was deleted.

Document Query A query was run on a list of documents, or a document query was canceled. (A message indicating that a query was canceled is displayed in the details and on the Query Text pop-up.)

Export The contents of a production set, saved search, folder, or subfolder were exported.

Images - Created Images were created.

File Download A file was downloaded through the Single Simple File Upload application. For example, a user clicked Download File on the Error Actions console of an individual processing error layout.

File Upload A file was uploaded through the Single SimpleFile Upload application. For example, a user clicked Upload Replacement File on the Error Actions console of an individual processing error layout.

Images - Created for Production Images corresponding to a production outside of Relativity were imported into the system.

Images - Deleted Images were deleted.

Import Content associated with a load, production, or image file was imported.

Markup - Image - Created Redactions or highlights were added to an image.

Markup - Image - Deleted Redactions or highlights were removed from an image.

Markup - Image - Modified Redactions or highlights were moved, resized or edited on an image.

Markup - Native - Created Redactions or highlights were added. This audit entry applies to transcripts only.

Markup - Native - Deleted Redactions or highlights were removed. This audit entry applies to transcripts only.

Markup - Native - Updated Redactions or highlights were moved, resized or edited. This audit entry applies to transcripts only.

Move A document was moved from one folder to another.

Native - Created A native file was loaded into Relativity.

Native - Deleted A native file was removed from Relativity.

Pivot Query A Pivot report was run, or a Pivot report was canceled. (A message indicating that a query was canceled is displayed in the details and on the Query Text pop-up.)

Production - Add Document A document was added to a production.

Production - Remove Document A document was removed from a production.

Query A process ran a query (such as categorization), or a query was canceled. (A message indicating that a query was canceled is displayed in the details and on the Query Text pop-up.)

RelativityScriptExecution A Relativity script was run.

ReportQuery A summary report was run.

Run A file was imaged, saved as a PDF, or otherwise converted for viewing

Search Cache Table Creation A search cache table was created. (Search cache tables are created the first time you search for a term or phrase using dtSearch or Relativity Analytics.)

Security Security rights were assigned or changed

Tally/Sum/Average The mass operation Tally/Sum/Average was run in the workspace.

Update Document metadata was updated on a single-document basis. In addition, filters on information related to applications installed through the workspace or by an agent.

Update - Mass Edit Document metadata was updated on a mass basis.

Update - Mass Replace Document metadata was edited using a text mass replacement.

Update - Propagation Document metadata was edited according to a propagation rule.

View A document was viewed.

Workspace Upgrade Details about scripts run on a workspace during an upgrade.

The following actions are audited at the admin-level. These admin-level actions are recorded against the Admin Case (workspace name). If you filter on the actual workspace name when searching for the Login action, you will not see any results.

Action name Description of activity

Create An item was created.

Update An item was updated

Delete An item was deleted.

Security An owner of a saved search was set during creation or edit.

Login A user logged in to Relativity.

Logout A user logged out of Relativity.

Export Data was exported from a tab at the instance level. For example, a workspace list, list of users, list of groups, etc.

RelativityScriptExecution A Relativity script was executed.

Password Reset Request - Submitted A password reset request was submitted.

Password Reset Request - Opened A password reset request was opened.

Password Reset Request - Successful A password reset request was successful.

Security Preview Started A security preview started on a user or group.

Security Preview Ended A security preview ended on a user or group.

Workspace Upgrade Upgrade script run on the workspace (details can be viewed in the JSON tab of the Details).

Login - Failed A login attempt to Relativity failed.

On this page

- Audit

- Supported Audit tab functionality

- Installing and configuring Audit

- Audit agents

- Audit tab

- Searching on the Details column

- Exporting workspace audits

- Instance audits

- Filtering on multi-workspace audits

- Mass reverting

- Audit Migration Reports tab

- Migration Error Report

- Migration Error Retry Script

- Migration Status Report

- Audit Workspace Settings tab

- DisplayAuditDataSource

- HistoryTabVisibleOnUpgrade

- Audited actions


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
