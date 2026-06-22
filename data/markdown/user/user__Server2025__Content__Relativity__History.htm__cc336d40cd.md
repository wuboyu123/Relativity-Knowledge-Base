---
title: "History"
url: https://help.relativity.com/Server2025/Content/Relativity/History.htm
collection: user
fetched_at: 2026-06-22T06:06:39+00:00
sha256: 338223e3c25facf3a040635e1fd8853aa1b4f504314cbd8f516fb66123e1863c
---

History

# History

On the History tab, you can view the actions of users throughout the workspace. Relativity has a comprehensive audit system that logs actions that users perform, object types, timestamps, and other details. This tab also includes views and filters to help you navigate through the audit records.

If the workspace has been restored, ensure that Audits have been migrated properly. Also, ensure you have allowed viewing of audits at the workspace level for the group.

When you view a document in the Review Interface, you can display its history in the related items pane by selecting the Document History icon.

## History view fields

You can customize the views available on the History tab or create new views as necessary. The History tab includes pre-configured views for recently updated documents, long running queries, and imaging history, which you can modify.

The following fields are available in views on this tab:

- Action —the user activity captured in the audit record.

- Artifact ID —the artifact ID of the audit action.

- Details —the detailed description of the audit action.

- Execution time —the length of time in milliseconds for a document query to run.

- ID —the identifier for the audited item; each tracked action has its own unique identifier.

- Name —the name of the object.

- Object type —the type of object.

- Request origination —the connection details for the user that sent the change request.

- Timestamp —the date and time when the audit action occurred.

- User name —the user who initiated the action.

You can export the contents of a view to Excel using at the top of the screen. Only the currently-loaded records are included in the Excel file. For example, in the following workspace, only 1,000 records would be included instead of the full 2,501 records.

Some features' history views are more detailed.

- For more information on saved search history, see Saved search history .

## Filters on the History tab

On the History tab, you can search for specific audit records by using filters just as you would on other tabs. For more information on filtering, see Filters .

You can also search for choice values using the Details Filter . Actions related to field choices are recorded using Artifact ID. To display the Artifact ID for choice values, click the Choice Legend icon in the view bar.

On the Choice Legend pop-up, you can search for choices in the workspace, their artifact IDs, and their associated fields. You can then enter Artifact ID listed for a choice value in the Details Filter and filter the audit records.

You can also use views to filter audit records. See History view fields .

## Audited actions

The following table lists audited actions in Relativity:

If you perform a job while previewing a user's security settings, the audit action will be credited to your user name and not to the user whose security you were previewing when you started the job.

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

No login action exists when you access a workspace. Relativity interprets the login based on any other auditable action in the workspace. For example, if you view a document in Workspace A, Relativity audits that view action on the History tab and indicates that a user accessed Workspace A.

## Exporting the history list

You can export a history list view as a .csv file using the following steps:

When Audit is installed, you can't export from the History tab.

- Navigate to the History tab.

- Select the history objects you would to export.

- Click Export to File .

- A pop-up appears. Select values for the fields:

- Format —select Comma Separated Values, .csv, which creates a comma delimited text file.

- Encoding —select the desired encoding for the output file.

- Escape Formulas —select yes or no. When you select yes, any line starts with the following special characters: =,@,+,-, or if the line starts with any combination of spaces before those characters, Relativity prepends a single quote to the line.

- Click Run to export the file or Cancel to cancel the export.
