---
title: "Text migration checklist"
url: https://help.relativity.com/Server2025/Content/Relativity/Data_Grid/Text_migration_checklist.htm
collection: user
fetched_at: 2026-06-22T06:12:26+00:00
sha256: 3b54176ed8f80b115fd7add62c6a6478d7d1603b37350069f459d0b9e59c59a0
---

Text migration checklist Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Running text migration

To run a text migration job, complete the following steps:

- Identify workspaces to migrate

- Identify long text fields to migrate

- Create a text migration job

- Run the breakage report

- Create and/or activate a dtSearch index

- Resolve saved searches and views

- Run text migration

- Review and resolve migration errors

## Identifying workspaces to migrate

Identify the workspace(s) you want to migrate. Be sure to review the special considerations for text migration as well as the list of supported and unsupported functionality for Data Grid. For more information, see Considerations .

## Identifying long text fields to migrate

Identify which long text field(s) you want to migrate. You can migrate up to three fields per migration job.

## Creating a text migration job

To create a text migration job, complete the following:

- Navigate to the Text Migration Jobs tab underneath the Data Grid tab.

- Click New Text Migration Job.

- Complete the following fields:

- Name - enter a name for the migration job.

- Workspaces - click , and then select the from the list on the left the workspaces you want to migrate. Use the arrows to move your selection(s) to the list on the right. Once you are finished, click Save .

- Fields - click , and then select the from the list on the left the fields you want to migrate. This list contains all long text fields that aren't Data Grid enabled. Use the arrows to move your selection(s) to the list on the right. Once you are finished, click Save .

You can migrate up to three fields per job.

- Email notification Recipients - enter the email address(es) of the recipient(s) you want to send a notification to when your migration job finishes running. Separate entries with a semicolon.

- Click Save . When you first save the job, it has a default status of Pending.

- Once you are ready to start the job, click Start Job on the console.

## Running the Breakage Report

To run the Breakage Report, click Breakage Report from the text migration console. The Breakage Report provides a list of all views, saved searches, indexes, and custom objects that will no longer function once you migrate SQL text to Data Grid. We recommend resolving these issues before running a migration job.

One of the primary functions of the Breakage Report is to identify areas where any of the objects above are tied to a keyword search or using keyword search specific functions like Contains or Does Not Contain. Most of the issues identified can be resolved by modifying the object to use an active dtSearch index.

The Breakage Report contains the following columns:

- Workspace ID - the Artifact ID of the workspace.

- Workspace Name - the name of the workspace.

- Name - the name of the view, saved search, index, or custom object that will break upon migration.

- Object Type - search, view, index, or custom object.

- Owner - the owner of the view, saved search, index, or custom object that will break upon migration.

- Field - the name of the field causing the object to break.

- Operator – the search operator (is, is not, etc.) incompatible with Data Grid.

- Term – the text string used in the broken search.

## Creating and/or activating a dtSearch index

Most of the issues identified by the breakage report can be resolved by modifying the object to use an active dtSearch index. To create or activate a dtSearch index, see Creating a dtSearch index .

Ensure all fields you want to search on are included in the searchable set for the dtSearch index. You can include a combination of Data Grid and SQL fields in your saved search.

The Data Grid Text Migration application includes logical to automatically fix active dtSearch indexes using the <all documents in workspace> searchable set. This logic only applies if the fields being migrated have the Include in Text Index field set to Yes.

The Data Grid Text Migration application creates a saved search called SS_TextMigration_[JobName] which contains all fields where Include in Text Index is set to Yes. It also creates a new dtSearch index called Migration_[existing dtSearch index name] which uses this new saved search. Once text migration completes, navigate to the old dtSearch index and click Swap Index . Select Migration_[existing dtSearch index name] as the replacement index.

## Resolving saved searches and views

Use the results of the breakage report to help you resolve index or field-level search issues that affect saved searches and views

We recommend copying saved searches prior to making edits.

### Resolving index searches

- Navigate to the saved search.

- Right-click on the name, and then click Edit .

- Click the (Index Search) condition.

- Copy the terms in the Search Terms field.

- Change the Index field to an active dtSearch index.

- Paste the search terms if needed.

- Click Apply .

- Click Save & Search .

### Resolving field-level searches

- Navigate to the saved search.

- Right-click on the name, and then click Edit .

- Click the condition using the field being migrated (for example, extracted text).

- Copy the text query, and note the operator (is, is like, contains).

- Click Add Condition , and then select (Index Search).

- Next to Index , select an active dtSearch index.

- Paste the query text you copied in step 4. Depending on the operator that was used, you may need to convert your search. For more information, see Search operator conversion .

- Click Apply .

- Remove the field condition.

- Click Save & Search .

#### Search operator conversion

Data Grid only supports the IS SET and IS NOT SET operators. If your field-level search uses another operator, you need to convert the search as follows:

Operator Example search Conversion

is Jane has a broken search "Jane has a broken search"

is not Jane has a broken search NOT "Jane has a broken search"

is set Supported operator No modification required

is not set Supported operator No modification required

is less than N/A N/A

is greater than N/A N/A

is less than or equal to N/A N/A

is greater than or equal to N/A N/A

is like Jane has a broken search *Jane has a broken search*

is not like Jane has a broken search NOT *Jane has a broken search*

begins with Jane has a broken search Paul*

does not begin with Jane has a broken search NOT Paul*

ends with Jane has a broken search *broken search

does not end with Jane has a broken search NOT *broken search

contains Jane has a broken search *Jane has a broken search*

does not contain Jane has a broken search NOT *Jane has a broken search*

## Running a text migration job

Once you've resolved or taken note of any items in the breakage report, click Start Job to start the text migration job. If another text migration job is already in progress, the new job is added to the queue and begins as soon as any running or pending jobs complete

The job displays one of the following statuses which you can use to monitor the state of your migration:

- Pending

- In Progress

- Complete

- Completed with Errors

The Migration Job Details table shows the progress of each workspace in the migration job. This table refreshes every two seconds. Once the job completes or completes with errors, you can filter the table.

The table contains the following columns:

- Workspace Name - the name of the workspace being migrated.

- Fields - the name of the field being migrated

- Migration Status - the status of the field being migrated. The following lists the field migration statuses:

- Pending

- In Progress

- Not In Workspace

- Already Migrated

- Completed

- Completed with Errors

- Documents Migrated - the count of documents migrated

- Total Documents - the total number of documents migrated.

- Errors - the count of documents with errors.

After a successful migration, the application runs a verification step to ensure all documents migrated from SQL to Data Grid. Then, the application drops the SQL column, permanently deleting the migrated text from SQL.

- If all documents are migrated, but a workspace and field are still marked as In Progress, this mean they are currently being verified.

- Although the application automatically deletes the column in SQL, you are still required to reclaim the space that was taken up by your long text document field in SQL.

## Viewing migration errors

Run the Data Grid Migration Error Report from the Text Migration Reports tab to view migration errors. To run this report, click Run . Click the drop-down to toggle between Field Level Errors and Document Level Errors. Once you've resolved any errors, return to the migration job and click Retry . The job status returns to In Progress and any errors on the fields marked with errors are reset.

### Field Level Errors

The following results populate the bottom of the window:

- Job Name - the name of the migration job where the errors occurred.

- Workspace Id - the artifact ID of the workspace.

- Workspace Name - the name of the workspace.

- Field Id - the Artifact ID of the field with errors.

- Field Name - the name of the field with errors.

- Error Message - the text of the error.

### Document Level Errors

The following results populate the bottom of the window:

- Job Name - the name of the migration job where the errors occurred.

- Workspace Id - the artifact ID of the workspace.

- Workspace Name - the name of the workspace.

- Document ID - the artifact ID of the document.

- Field Name - the name of the field with errors.

- Error Message - the text of the error.

On this page

- Running text migration

- Identifying workspaces to migrate

- Identifying long text fields to migrate

- Creating a text migration job

- Running the Breakage Report

- Creating and/or activating a dtSearch index

- Resolving saved searches and views

- Resolving index searches

- Resolving field-level searches

- Running a text migration job

- Viewing migration errors

- Field Level Errors

- Document Level Errors


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
