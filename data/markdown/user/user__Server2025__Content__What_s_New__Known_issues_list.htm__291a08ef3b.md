---
title: "Known issues"
url: https://help.relativity.com/Server2025/Content/What_s_New/Known_issues_list.htm
collection: user
fetched_at: 2026-06-22T06:10:47+00:00
sha256: 0f316d9345c2e28ceda6cc3efdff93401ca9864d4957205f0068ebd372d7c3b1
---

Known issues Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024 Server 2023

☰

# Known issues

The following list provides descriptions of known issues in Relativity for 2021 and later. For a list of Relativity enhancements and more details for resolved issues, see Relativity Server release notes .

- The table below lists known issues for 2021 and later. To view a list of known issues for 2016-2020, see Known issues archive (2016-2020) .

- Relativity uses a number of third-party technologies to ingest, store, search for, and manipulate data. Relativity does not possess a comprehensive list of all issues ever reported in the third-party technologies, and cannot provide fixes when these application-specific issues arise. Relativity will, however, work to alert the third-party vendor if issues are uncovered.

- RelativityOne environment has not been upgraded to the latest release, known issues listed as Fixed may not be resolved in your environment yet.

Learn more about known issues

#### Why we publish known issues

Relativity publishes known issues to provide transparency and to give you the information you need when making upgrade decisions. Relativity Customer Support and Engineering publishes known issues at its own discretion based criteria such as on the number of customer reports, the severity of the issue, and the availability of a workaround. Not all defects are published as known issues.

#### When we publish known issues

The known issues list receives updates when the following occurs:

- Engineering or Support identifies new known issues.

- A monthly update introduces a new known issue.

- A monthly update resolves an existing known issue.

If you're experiencing an issue in Relativity and you don't see it listed on the known issues page, contact Client Services .

#### Known issues details

The Known Issues page contains the following information about each known issue. You can also sort on each column by clicking the column header:

- Date added - lists the date that the known issue was added to this web page.

- Defect number - lists the defect number. This number is helpful in conversations with Client Services or Sales if you think you're experiencing the Known Issue in your environment.

- Feature - lists the feature of Relativity affected by the Known Issue, so you can identify the Known Issue within a workspace.

- Description - provides an overview of the Known Issue.

- Versions affected - lists the versions of Relativity where the Known Issue appears.

- Version resolved in - lists the versions of Relativity where the Known Issue is resolved so you can make decisions on upgrades. If this column is blank, the known issue is still open.

Date added Defect # Feature Description Identified in version Version resolved

Date added Defect # Feature Description Identified in version Version resolved

2026-05-20 REL-1304134 Data Grid > Text Migration When a Data Grid text migration job is running on a Long Text field, any concurrent OCR set writing to that same field will have its output overwritten by the original SQL value. The affected field value may then propagate downstream to dtSearch indexes, Search Terms Reports, and dependent workflows Server 2024

Server 2025

2026-05-04 REL-1274507 Review > Mass Operations Audit logs incorrectly record a "Set" action when a Mass Edit operation includes documents across folders with different permission levels. Documents where the user has view-only access are not modified, but still generate audit entries, creating inconsistency between audit logs and actual system changes. Server 2024 Patch 2

Server 2025

2026-03-13 REL-1209342 Core > Relativity Forms In Relativity Server, the Copy from Previous button in the coding layout may disappear after refreshing the browser while viewing a document. The button should remain visible but disabled; however, it is removed from the UI instead.

Workaround: Refresh the coding pane frame (Right-click \x1a Reload/Refresh Frame) or navigate to another document and return to make the button reappear. Server 2024 Patch 1

Server 2024 Patch 2 Server 2024 Patch 3

2025-11-19 REL-1220278 List The Pivot Profile dropdown displays correctly when creating the first Pivot but may appear blank when creating a second Pivot in the same session. Server 2024 Patch 2

Server 2025 Server 2024 Patch 2

Server 2025

2025-10-17 REL-1175213 Core After refreshing the browser while on the coding layout, the “Copy from Previous” button may temporarily disappear instead of remaining visible in a disabled state. The button reappears only after manually reloading the page or navigating away and back. Server 2024 Patch 1

Server 2024 Patch 2 Server 2025

2025-09-24 REL-1172420 ARM An issue affecting ARM Restores in Relativity Server and RelativityOne has recently been identified in which the restored ARM archive will complete successfully, but Data Grid Audits will not be restored. When accessing the Audit tab within the workspace, historical Audits from the source instance before the workspace was archived will not be visible.

The issue originates with a conflict in the execution of the Data Grid Audit migrator during the Archive job in Relativity Server; Two audit folders may have been created within the ARM archive (\Audit and \DataGrid\audit). One folder would contain the workspace's historical Audit data (\DataGrid\audit), while the other folder would be empty (\Audit). Upon restore of affected workspaces, the empty folder (\Audit) may have been the Audit source selected for restore.

This conflict was the result of the state of the NewDataGridMigratorToggleOverwrite Instance Setting having been set to 'False' in the Relativity Server environment in which the workspace was archived.

Workspaces archived within RelativityOne will not be impacted. Workspaces restored to RelativityOne after the fix has been applied (ETA: October 2025) will not be impacted. The missing\unrestored Audits will still be available in the affected ARM archives.

2025-08-20 REL-1103353 Processing > Discovery Publisher files issue: Extracted text is not displaying for a few files and metadata values do not match. Support for .pub (Publisher) files ends with the Office 2024 upgrade. Convert Publisher files to PDF for continued use or review them offline Server 2024

2025-08-20 REL-1113126 Imaging CSV (Comma-Separated Values) files are plain-text representations of tabular data. Though they open in Excel and resemble spreadsheets, they lack formatting, cell structure, and metadata needed for accurate imaging. Server 2024

2025-06-27 REL-1001285 Processing Notebooks created in OneNote 2007 may not render/function as expected in Office 2024. Users may experience compatibility issues. User has to convert notebooks using OneNote 2010/2013 which is recommended for Office 2024. Server 2024

2025-06-27 REL-1106910 Processing Digital Image File types: When processing vector-based file formats such as .snp, .emf, .svgz, and .wmf, in Office 2024 the extracted text does not accurately match the text as rendered in the original document. This mismatch may include missing characters, incorrect text order, formatting inconsistencies, or garbled content. Server 2024

2025-06-27 REL-1102761 Processing When creating a processing profile where Tagalog is selected as the native file's language for OCR, some translation results may be mismatched by off by one letter in Office 2024. Server 2024

2025-06-23 REL-1121639 Imaging During Native Imaging of Google Docs, comments in the Google Docs overlap and do not appear aligned. This issue is also observed in Relativity One. Server 2024

2025-03-20 REL-1072629 All products The Help link for Server 2024 incorrectly redirects to Server 2023 documentation instead of Server 2024. This will be fixed in Server 2024 Patch 2. Server 2024

Server 2024 Patch 1 Server 2024 Patch 2

2025-03-05 REL-1069721 Structured Analytics There is an issue where having an apostrophe in the structured set name results in front-end errors when opening the set, which may persist even after switching to a different set. This problem occurs in on-prem deployments and displays the error message: "An error occurred while loading this page." Server 2022

Server 2023

Server 2024 Patch 2 Server 2024 Patch 2

Server 2025

2025-02-04 REL-1050313 Processing In Server 2023, there's a bug where file errors can get stuck in "Resolving" status after error retry jobs complete. When this happens, customers are unable to retry these errors, support teams have to manually fix the issue through running SQL scripts in the SOP. Server 2023

Server 2024 Server 2026

2025-02-03 REL-1052726 Service Bus, RabbitMQ Compatibility of TLS-1.3 with RabbitMQ-3.13.x. The Secret Store does not function with TLS 1.3, which is preventing RDP access to the RabbitMQ server. To ensure RDP access to the server, enable both TLS 1.3 and TLS 1.2. Disabling TLS 1.2 may result in the inability to connect to the server using RDP. Server 2023 Hotfix 12.3.857.3, Server 2024

2025-01-09 REL-997945 Timestamp Timestamp fields in the Errors tab are incorrectly displaying time in UTC instead of the user's local time zone. Server 2023

Server 2024 Server 2023 Patch 3

Server 2024 Patch 1

Server 2025

2024-11-21 REL-975559 Authentication When adding a 'Default Password Provider' Login Method in Chromium-based browsers, the 'Days' field nested under the 'Maximum Password Days' field is sometimes auto-populated with the user's email address that is saved in the browser password manager. Attempting to save the form with an email address in the 'Days' field results in an error. Because the 'Days' field is hidden by default behind the default toggled-off 'Maximum Password Days' field, it is not easily apparent that the save error is caused by the invalid value in the hidden 'Days' field. To mitigate this issue, users can enable incognito mode in their browser or toggle on the 'Maximum Password Days' field and clear the email address from the 'Days' field. Server 2022, Server 2023, Server 2024

2024-09-05 REL-987368 Structured Analytics While performing the 'Assign to entity' operation and merge for Entities operation for the Name Normalization in Relativity Server 2022,2023, and 2024 environment, you may receive the following error *kCura.Data.RowDataGateway.ExecuteSQLStatementFailedException: SQL Statement Failed ---> System.Data.SqlClient.SqlException: Cannot continue the execution because the session is in the kill state*

The fix for this issue is to make sure you are running Microsoft SQL Server 2019, CU 28 or later. Server 2022, Server 2023, Server 2024

2024-09-05 REL-996051 Data Transfer When importing OneNote SOAP files through SFU, an "unsupported file type" error occurs in the viewer. Please use the RDC or Processing to import these files as a workaround. Server 2023 Patch 3

Server 2024 Server 2026

2024-09-04 REL-932589 Structured Analytics Transform set start button is not available in certain scenarios. To resolve the issue please refer to this article: Transform Sets Start Button Not Visible Server 2023 Patch 1

2024-08-19 REL-988748 Processing Set Layout On Processing Set Layout, clicking on the "File Errors" link redirects users to the "Document Errors" tab instead of the intended destination, the "Files" tab. To resolve the issue, see the Community site article, Server 2023 - File errors link re-directs to document errors tab instead of files tab . Server 2023 Server 2023 Patch 3

Server 2024

2024-07-29 REL-973287 ADS When errors are encountered when importing application files to the Application Library, attempting to export the error file using the 'Export Error File' link on the conflict resolution modal does not not work. Server 2022, Server 2023, Server 2024

2024-07-19 REL-977682 Audit * Audit fails to migrate due to differences in the structure of already indexed audits and new audits.

* This is not an issue with XML parser, this is the issue mapping of dynamic fields in Elasticseach.

[SLA 4/30/21] When attempting to view summary report, Relativity redirects to generic error page - Relativity Jira (kcura.com) Server 2022, Server 2023, Server 2024

2024-07-19 REL-977681 Audit * As of now we randomly pick 10 workspaces and only display audits from these 10 workspaces at the Admin level tab.

* If the user doesn't have access to any one of the 10 chosen workpaces then the Audit tab fails to load.

* Instead of picking 10 random workspaces, pick the workspaces that the user has access to while displaying Audits from all the workspaces. Server 2024

2024-05-13 REL-947156 Relativity Forms Long text fields with values that end with an ellipsis cannot be edited (Read Only) in Relativity Forms. Server 2022

Server 2023

Server 2024

Server 2024 Patch 3

Server 2025 Patch 1

Server 2026

2024-04-04 REL-922481 Processing UI On Processing Set layout, clicking on the "File Errors" link redirects users to the "Document Errors" tab instead of the intended destination, the "Files" tab. To resolve the issue please refer to this article: https://community.relativity.com/s/article/Server-2023-File-errors-link-re-directs-to-document-errors-tab-instead-of-files-tab Server 2023 Patch 1 Server 2024

2024-03-13 REL-923461 Discovery When selecting native text extraction for Excel files, certain numbers may be rounded to the nearest whole number in the extracted text. Server 2023, RelativityOne

2024-02-26 REL-909837 List Page A user without the 'Add' Search permission is still able to create and run a saved search from the root level folder if they have access to the Saved Searches browser. Server 2022, Server 2023 Server 2023 Patch 3, Server 2024 Patch 1, Server 2025

2024-01-31 REL-910519 PageBase Any user that does not have ViewAdminRepository permission and attempts to refresh the Workspace Details page once already there, or to access it from the Password Bank page will be redirected to the permission denied page. In any other case, the Workspace Details page will load correctly. Server 2023

2024-01-11 REL-898243 Infrastructure In Server 2023, Structured Analytics jobs may become stuck toward the end of the Export phase if one or more batches are erroneously marked as orphaned by the Structured Analytics Manager agent's orphaned job check. The workaround to unblock jobs is documented here: https://community.relativity.com/s/article/Relativity-Server-Name-Normalization-Stuck-at-99-Percent Server 2023 Server 2023 Patch 2

2023-11-08 REL-890142 Discovery Arabic, Hebrew, Thai, Vietnamese, and Belarusian unsupported languages show up under 'Default OCR languages' in Processing profile. Processing files with these languages will result in gibberish for OCR extracted text in the viewer. Server 2023 Server 2023 Patch 1

2023-10-27 REL-884580 Reviewer Interface For document history does not load when audit app is not set up with elastic instance configured properly to retrieve the history data. Server 2023 Server 2023 Patch 1

2023-10-17 REL-884170 Processing New and existing Processing jobs are not able to run when upgrading from a pre-Server 2022 version to Server 2023. We intend to resolve the issue with a hotfix soon. Server 2023 Server 2023 Hotfix 4, Server 2023 Patch 1

2023-10-06 REL-877573 Legal Hold There is an issue that prevents workspace upgrades from Server 2021 or Server 2022 Legal Hold to Server 2023 Legal Hold. We plan to remediate this issue with a hot fix for Server 2023 in the coming weeks. Server 2021, Server 2022, Server 2023 Server 2022, Server 2023, Server 2023 Patch 1.1

2023-09-26 REL-877573 ARM There is an issue that prevents Legal Hold archives from Server 2021 or Server 2022 from being restored into RelativityOne. We plan to remediate this issue in the coming weeks, and we do not expect a hot fix for Server being required. Server 2021, Server 2022, Server 2023, RelativityOne Server 2022, Server 2023, Server 2023 Patch 1.1, RelativityOne

2023-08-30 REL-826158 Processing A failure occurs when deleting a Processing Set with document errors from the Processing Set layout. The workaround is to delete the Processing Set using the Mass Delete action from the Processing Set list view. Server 2021

2023-08-04 REL-862446 Processing Processing Set error messages do not display the relevant error messages during new set creation. Instead, a static error message is always displayed. Server 2023, RelativityOne Server 2023 Patch 1

2023-07-13 REL-834578 Files Tab

For Processing Sets that contain large amounts of data sources, clicking the File Errors link from their Processing Set page can fail to navigate to the Files tab, and instead show a 404 error. This problem occurs when a Processing Set contains approximately 140 or more Data Sources.

To work around this issue, navigate directly to the Files tab, select the Current Errored Files view, and add a condition to filter the view by Data Source - selecting the data sources from the current Processing Set.

Server 2022

2023-06-21 REL-809665 Relativity Forms When the 'Save and New' button is clicked in a popup window, the popup disconnects from the parent object and is unable to save again. The initial save successfully completes, however the user will need to close the popup and reopen in order to continue. As a workaround, we recommend using the 'Save' button instead. Server 2022 Patch 3

2023-04-18 REL-604868 Case Dynamics The Fact Modal date picker does not load the correct font for the *Previous* and *Next* buttons on the Calendar popup. However, this does not affect functionality and users can still click on the button area to navigate to Previous or Next month. Server 2023

2023-03-10 REL-827207 Discovery Google has made an update to their GMAIL export format. Due to this change, the automated sidecar metadata ingestion when processing GMAIL data is not functioning. Server 2021, Server 2022, Server 2023 14.3

2023-02-13 REL-815444 Relativity Scripts & Utilities Service account activity from TDFE (Track Document Field Edits) for Updated By fields can show up in the "Reviewer Statistics - No System Administrators" report as a blank user. This happens if user 777 is not a system administrator in the environment, because TDFE is hard coded to use UserID 777 for Service account. Server 2021, Server 2022, Server 2023, Server 2024

2023-01-19 REL-704035 Errors When top level container files are replaced using Download / Replace, the replaced record will still reside in the Processing Source Location, rather than the workspaces file repository. Server 2022 Patch 1, Server 2023

2022-11-09 REL-757714 Case Dynamics Document viewer navigation doesn't work as expected when using layouts to review documents tied to facts or other objects. The easiest way to review the documents tied to facts or other objects is by using the standalone viewer. Server 2021 Patch 4, Server 2022, Server 2023

2022-10-10 REL-716071 Imaging Imaging PDFs using the Native Imaging profile with a specific type of native redaction can sometimes result in a full page redaction. The Basic Imaging profile does not have this issue. If you encounter a full page redaction, use the Basic Imaging profile instead. 10.3

2022-09-19 REL-744493 RDO Framework There is a limitation of 50 characters in the Name field. Server 2022

2022-08-10 REL-596209 Audit Running a Reviewer Statistics Report in a workspace with audit installed may not generate the results in time if the workspace has a large number of audit records in DataGrid/ElasticSearch. 10.3, Server 2021, Server 2022, Server 2023

2022-08-04 REL-719440 Reviewer Interface Searching Excel files will find hits, but will not advance to a new tab if the hit is in a different sheet. Server 2022, Server 2023 Server 2022 Patch 1

2022-07-13 REL-702489 Workspace Upgrades Server customers upgrading from 10.3 to Server 2021 or Server 2022 who have customized the Custom Page RDO with fields that are marked "Open for Association" may encounter an error. As a workaround, remove any custom fields on the Custom Page object type and retry the workspace upgrade. 10.3, Server 2021, Server 2022 Server 2023

2022-06-07 REL-525326 Relativity Forms Long text fields with values that end with an ellipsis cannot be edited (they become Read Only) in Relativity Forms. 10.3, Server 2021, Server 2022, Server 2023 13.3

2022-06-03 REL-680999 Searching Carriage returns are interpreted literally rather than replaced with OR operators when performing an ad hoc search with the operators "Begins With", "Does Not Begin With", "Ends With", and "Does Not End With". 10.3, Server 2021, Server 2022 10.3 Hotfix 10.3.287.3, Server 2021 Hotfix 11.1.514.7, Server 2022 Hotfix 12.1.537.3

2022-05-26 REL-669307 Publish The Processing Set publish status will remain Incomplete when using the Republish action on newly discovered content from resolved errors on the Files tab. Server 2022

2022-05-19 REL-31122 Reviewer Interface Very small redaction text does not show up in production images. 9.2, 9.3, 9.4

2022-05-17 REL-664963 Processing Dedupe fields will be propagated to child documents when the Processing Profile setting is set to 'No' for the first Data Source in the first Processing Set published in the workspace. 10.3

2022-04-20 REL-663128 Discovery When processing an RSMF file with Unicode characters in the header, attachments may not be discovered. This will be identified with the error "Unable to extract an attachment from RSMF file". 10.3, Server 2021, Server 2022, Server 2023 14.3

2022-03-09 REL-655940 ADS Pagination in the "Workspaces Installed" of the Application Library view form may not work. The workaround is to use a large page size, filters and/or sorts to narrow into specific workspaces. Server 2021 Patch 2

2022-02-07 REL-641177 Discovery If a large number of Entities exist in a workspace, custom document number prefixes attached to Entities do not properly load when creating a Data Source. Server 2021

2021-12-03 REL-621434 Discovery Processing OneNote files may result in additional discovery time. 10.3, Server 2021, Server 2022, Server 2023

2021-11-18 REL-617588 Processing The PowerPoint Hidden Slides metadata field is not accurately indicating the "yes" value for files that meet the criteria of containing hidden slide(s). Please note, the extracted text field does contain the text of the hidden content. 10.3 Server 2022

2021-11-15 REL-507525 Discovery When corrupted Microsoft Outlook Personal Folders (.pst files) are processed, there is a chance that the order of entries in the PST might be corrupt. If such PSTs are partially published, and then the original PST is retried to fix the corruption, run through discovery, and published, the relationships between the parent and child items can become corrupted. This results in parent and child elements appearing in an incorrect order. 10.3, Server 2021, Server 2022, Server 2023 13.0

2021-10-14 REL-604605 Publish The republish action from the Files tab will not be performant on larger data sets (~2,000,000+ documents.) Server 2023

2021-10-07 REL-591699 Errors Clicking the Publish button to resolve publish errors on the Processing Set page will only resolve the File Level errors that are outstanding. If Job Errors are present, they will have to be retried through the Job Errors tab. Server 2023

2021-10-07 HYDRO-15023 Reviewer Interface Duplicate View audits are created when documents are viewed in the Image Viewer. Server 2021 Server 2022

2021-09-21 REL-591658 Reviewer Interface In the Classic Reviewer Interface, when a relational field contains non-alphanumeric characters, such as '%', the field's icon fails to load on the page. Server 2021 Server 2021 Patch 2

2021-09-21 REL-596156 Short Messages When a user images an RSMF that contains a file attachment (such as Word, Excel, PPT, etc.), the imaged RSMF says the attachment is missing when it is not true. This doesn't happen for attachments that can be displayed in the Viewer, such as pictures. Server 2022 Server 2023

2021-09-09 REL-569071 ADS

When a user clicks the "Install" button in the Application Library to install an application to specific workspaces, a dialog displays the error message "There are no views." The workaround is to go to the workspace to select that application from the library.

Server 2021 Server 2021 Patch 2

2021-08-19 REL-527723 Hold Admin Rare critical defect that causes a large volume of unintended reminder emails to be sent. 10.3 10.3 Patch 5

2021-08-19 REL-414261 Structured Analytics If name normalization produces two entities that look the same, but one has an invisible character, the Entity results import phase will fail with a duplicate key exception. 10.3, Server 2021 10.3 Patch 5, Server 2021 Patch 1

2021-08-19 REL-416488 Structured Analytics Structured Analytics email threading jobs fail to complete when preparing Email Threading Display data during import phase, if the content to be parsed into XML contains surrogate block characters. Server 2021 Server 2022

2021-08-19 REL-586162 Production Sets The dates are shown in wrong formats for clients in different regions. For example, clients in Australia would expect to see the date in DD/MM/YYYY format, but the bug renders the date in MM/DD/YYYY format. 10.3, Server 2021 10.3 Patch 5, Server 2021 Patch 1

2021-08-10 REL-482867 Publish When deleting documents with Post Publish Delete, the associated Processing Sets will have incorrect unpublished file counts. Server 2022

2021-08-09 REL-569985 Discovery Microsoft Forms are not supported in Pre-2007 Microsoft Office Word, PowerPoint and Excel files, as they are detected as bin files and currently are not flagged with an exception. For an interim workaround, please convert to Post-2007 format. This affects all supported versions. 10.3

2021-07-16 REL-574981 Summary Reports When deleting a Summary Report from the Summary Report page, the delete button will not function and perform the delete. As a workaround, you can delete the desired Summary Report by navigating back to the main list of Summary Reports using the delete mass operation. Server 2022 Not Planned

2021-06-30 REL-571089 Relativity Forms Custom Form Objects do not reflect filter view conditions set on Child or Associative Objects. Results display all field values. Server 2022 Server 2023

2021-06-29 REL-520434 Relativity Forms On a Relativity Forms enabled page, while opening an associated object in a modal which is displayed in the non-Aero older forms rendering engine, any delete action taken for a record will not appear on the initial forms page until after the page is refreshed. Server 2022 Not Planned

2021-06-29 REL-550994 Infrastructure GovCloud Only: Pre-2007 Word, PowerPoint and Excel files will experience errors if Native option is used for text extraction. The errors may result in missing extracted text for these files. The recommended workaround is to use the Relativity text extraction option. Server 2022 Not Planned

2021-06-22 REL-568555 Installation The RelativityScriptLogin SQL user uses the same password as the EDDSDBO SQL user. They should be able to have different passwords. 10.2, 10.3 Server 2021

2021-05-20 REL-546542 RDO Framework RSAPI endpoints can fail to read documents in unassigned batches. 10.3, Server 2021 10.3 Patch 5, Server 2021 Patch 1

2021-05-14 REL-554383 Errors You are unable to use any of the Error Action buttons of Retry, Ignore, Edit Notes, Download File, and Upload Replacement File when viewing individual Document Errors. The recommended workaround is to use the error actions provided in the Files tab to complete error remediation. Server 2022 Server 2023

2021-05-07 REL-483620 RDO Framework After a choice hierarchy gets re-parented the order of multi-choice values displayed in the item list appears in an un-intuitive order. The order no longer corresponds to the hierarchy. There is a work around which is to manually update the order of each choice in the hierarchy. 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022 Not Planned

2021-05-06 REL-554397 RelativityOne Redact The user-experience around reverting a spreadsheet chart redaction using Relativity Redact is not intuitive. After redacting a chart, the user must reject the chart redaction in the Redact QC card and refresh the document view after being prompted by the Redact toast notification to do so. The user might intuit that they could right-click on the redacted chart and revert the markup using the 'Revert' option like other cell redactions but they cannot because the user is actually clicking on the cell underneath the chart rather than the chart itself. Server 2022 Server 2023

2021-04-26 REL-509474 Errors The Error Category field may display 'Unknown' for some Discover or Publish errors. Server 2022 Not Planned

2021-04-26 REL-527800 Errors Specific FileIDs included in processing retry jobs no longer appear in the general data source audit table. The information can be found by selecting the JSON tab in the audit window. Server 2022 Not Planned

2021-04-20 REL-518133 Summary Reports When navigating to the Summary Reports page and selecting the report to navigate to, a general error can appear when trying to load the page. After receiving the first error, clicking to navigate to the same report will allow you to navigate to the desired page. Server 2022 Not Planned

2021-04-07 REL-513517 Imaging Some older versions of a password protected Microsoft Note may not image using native imaging. Server 2022 Not Planned

2021-04-07 REL-532570 Imaging Some PDF file may render incorrectly when using the native imaging profile. 10.3 Server 2021

2021-04-01 REL-541867 RDO Framework

If someone tries to save a document that was previously coded with a user that has since been removed from the workspace, the save fails. This can also happen if the user was not mapped to a system user during an ARM restore. In either case, this works fine in classic.

This only happens if the user field is on the layout and editable. These are a few potential workarounds, in order of feasibility:

* Set the user field to read only.

* Remove the user field from the layout

* *Scenario 1 only (see below):* Add the user back to the workspace

* *Scenario 2 only*: Re-create the deleted user, add them to the workspace, then manually re-code the affected documents with that user. Mass Edit can be used to make this process easier

* *Scenario 3a only*: Create the missing user, then manually re-code the affected documents with the same user. Mass Edit can be used to make this process easier

* *Scenario 3b and 3c only*: Manually re-code the affected documents with the same user. Mass Edit can be used to make this process easier

* Code the documents with another user.

Server 2022 Not Planned

2021-03-17 REL-453550 Discovery Word documents that utilize the Native text extraction method during Processing may not have the Has Hidden Data metadata field properly set. This issue is not present when processing the Word documents in dtSearch or Relativity extraction methods. Using the Relativity extraction method is the recommended workaround. 10.3, Server 2021, Server 2022, Server 2023

2021-03-04 REL-469855 Assisted Review For an Active Learning project, on the Prioritized Review card, the box containing the values for the Family Field can look cut off. This issue isn't consistently reproducible, even when using different browsers, so there isn't a planned resolution. Server 2022 Not Planned

2021-02-10 REL-497226 Imaging Imaging PDFs in color may have a light hue rather than a true color match of the PDF native. 10.3 Not Planned

2021-01-13 REL-511187 Layout The Object Type column on the Choices list in admin is incorrectly specified as "Case" rather than "Resource Pool" for choices belonging to the "dtSearch Index Share Location" and "Processing Source Location" fields. Server 2021 Server 2022

2021-01-07 REL-509917 Discovery OneNote 2003 documents can't be processed on workers with Office 2016 installed as Microsoft did not make their software backwards compatible with that version. Server 2022 Not Planned

- Known issues


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
