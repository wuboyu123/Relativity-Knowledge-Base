---
title: "Known issues"
url: https://help.relativity.com/Server2025/Content/What_s_New/KnownIssuesArchive.htm
collection: user
fetched_at: 2026-06-22T06:21:35+00:00
sha256: 902a441debc67230c38812f69672af0668b0e7aef974bafa9459232436ec3458
---

Known issues Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024 Server 2023

☰

# Known issues archive (2016-2020)

The following list provides descriptions of known issues in Relativity , 2016-2020. To view the current list of known issues, see Known Issues .

- Relativity uses a number of third-party technologies to ingest, store, search for, and manipulate data. Relativity does not possess a comprehensive list of all issues ever reported in the third-party technologies, and cannot provide fixes when these application-specific issues arise. Relativity will, however, work to alert the third-party vendor if issues are uncovered.

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

2020-12-18 REL-478772 Assisted Review When a family document is deleted/removed, there is an identified discrepancy with the SQL logic for Family Group / Responsive Family Group columns of statistics. The Summary row counts the children and the round row does NOT count the children. Server 2022, Server 2023 Not Planned

2020-12-15 REL-444606 Case Dynamics From the inline edit list pages in Case Dynamics, creating object entries using a custom multi object field results in errors. 10.3 Not Planned

2020-12-15 REL-424035 Transcripts Transcript files are not fully rendered in the Transcripts viewer when using the Safari browser and the user's Document Viewer setting is set to Relativity Review or Default. As a workaround you can set the Document Viewer setting to HTML and use Safari or switch to the Chrome browser, which does not require adjusting of the Document Viewer setting. Server 2022 Not Planned

2020-12-10 REL-263816 Discovery Text from charts embedded in excel files may not be captured. This issue is limited to clients running Office 2010 on their workers and use native processing. 9.6 Not Planned

2020-12-07 REL-495897 Processing Administration Processing Source Locations ending with a backslash (\) may have an extra one appended to the file path when creating Processing Data Sources. The workaround to this issue is to remove the backslash (\) from the Processing Source Location and create a new Processing Set. Server 2022 Server 2023

2020-12-07 REL-468225 Imaging The Has Images field on the Document object allows for new choices to be added as well as the ability to delete existing choices. Deleting an existing choice will break imaging and potentially break other features. Server 2022 Not Planned

2020-11-10 REL-357133 Transcripts When using the IE browser to navigate to the next transcript in the queue, the viewer does not refresh correctly and so the text of the next transcript is not rendered properly. As a workaround, please use Chrome. 10.2 Not Planned

2020-11-10 REL-493697 Case Dynamics You cannot use the Currency or Decimal field types to set up conditions in the Timeline Builder. 10.3 Not Planned

2020-10-27 REL-475236 Structured Analytics Communication Analysis does not properly cancel, when requested through the Relativity List Page. The List Page will show that the request has been cancelled, but the back-end logic continues to execute. 10.3, Server 2021 Server 2022

2020-10-26 REL-489141 Case Dynamics When undergoing Active Learning document review in HTML viewer, fetching the New Document while the user is on Case Dynamics Coding pane, it sometimes returns a spinner. Workaround is to use Hydro Viewer. Server 2022 Not Planned

2020-10-23 REL-315723 Discovery OneNote files may be occasionally processed without embedded emails within them extracted out as child documents. 10.3 Server 2022

2020-10-23 REL-469001 Authentication User's browser session cache not cleared on logout. This could potentially lead to information leak if the browser is left open. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2020-10-22 REL-478848 Resource Servers There is an issue when a workspace is migrated to a new sql server that the workspace in question is unavailable until services are restarted. 10.3 10.3

2020-10-20 REL-484317 Relativity Web Components (RWC) Google Chrome versions starting with 86.0.4240.75 include a change that "bottom justifies" field labels. The issue is cosmetic, but misleading for many fields. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2022

2020-10-20 REL-487141 Relativity Forms Quickly navigating from the processing document error page to a processing error details page can cause a crash and error. This can be resolved by navigating back to the document error page, and letting that page fully load all event handlers, before clicking on any specific error in the list. This will be fixed in a future release. Server 2022, Server 2023 No

2020-10-09 REL-483677 dtSearch When building a dtSearch index, any field following a SQL Long Text field can potentially have its first term appended to the last term of the SQL Long Text field for larger documents.

Recommended workarounds:

1. If using a Saved Search with only one Long Text field stored in SQL, reorder the fields in the Saved Search to have the Long Text field last in the sequence as only fields immediately following the Long Text field could be impacted.

2. Increase the dtSearchStreamThresholdInBytes instance setting as only documents larger than this size could be impacted.

3. Migrate SQL Long Text fields to Data Grid as Long Text fields stored only in SQL are impacted. 10.2, 10.3 Server 2021

2020-09-21 REL-443693 Discovered Files You are not able to export dashboards from the Discovered Files tab. 10.3 Not Planned

2020-09-15 HYDRO-12550 Reviewer Interface When viewing documents in the Review Interface, if the browser zoom level is configured to a value greater or less than 100% visual issues may occur. This includes components not being visible inside the browser window or resizing in an unexpected way. Please note that browser zoom levels other than 100% are not supported. Server 2022 Not Planned

2020-09-11 REL-470944 Authentication User's whose session has timed out or have been forced logged out end up on the Relativity error page instead of logout 10.3 10.3

2020-09-08 REL-458938 Agents Files that fail to be converted completely can sometimes fail to produce the index.html file. This results in orphaned cache files that will not be properly cleaned up by cache manager. 10.3 10.3

2020-09-08 HYDRO-12395 Reviewer Interface If the document identifier (typically Control Number) is changed for the document being actively viewed, the label in the top-center of the Review Interface will not update to reflect this change until the user re-enters the workspace. Server 2022 Not Planned

2020-09-03 REL-469523 RDO Framework Custom labels applied to fields on the coding layout do not word-wrap and can appear cutoff. When using custom labels on Document object layouts, this typically occurs after several navigations for labels over 40 characters long. 10.3 Not Planned

2020-09-03 REL-450815 Workspace In AOAG environments that are configured with individual servers that have both primary and secondary AG's on the same server, workspace deletion fails. 10.3 Server 2022

2020-08-28 REL-456134 Reviewer Interface When attempting to download native files with names containing commas fails when using Google Chrome. This can be worked around by removing the comma from the Filename column on the File table. 10.3 Server 2021

2020-08-28 REL-423877 List Page When using two search index conditions the second one gets dropped. 10.3 10.3

2020-08-28 REL-435780 Discovery If you have data sources prior to 9.7 they could be publishing duplicate parent files. This is due to the altered attachment hash the defect prompts for, which, ultimately alters the Processing Duplicate hash we dedupe off of. 10.3 10.3

2020-08-28 REL-437396 Relativity Desktop Client RDC imports won't finish due to a query that never finishes running in SQL 10.3 10.3

2020-08-28 REL-410185 Hold Admin Customers who have a large set of unique metadata types may experience slowness and/or error during publish due to memory consumption. 10.3 10.3

2020-08-28 REL-400722 RDO Framework Customers may receive unexpected results for search queries including Is Set criteria on fixed-length text fields 10.3 10.3

2020-08-28 REL-318333 dtSearch Inaccurate search results as dtSearch index silently excludes non-Unicode Long Text fields if they're longer and are streamed 10.1 10.2

2020-08-28 REL-393957 Assisted Review We removed code that was incorrectly deleting unassigned documents before population of the Dynamic Review Queue. By doing so, multiple batches of documents sent back from CAAT will not overwrite one another. 10.3 10.3

2020-08-28 REL-391724 Admin Operations Getting the following error when attempting to delete a legal hold project via mass operations as well as when you try to delete the project from within the project. This appears to be happening when an exception is thrown during the mass delete. Relativity is attempting to save the exception message to the Status field of the MassOperationProcessState table. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2020-08-28 REL-459947 Search Term Reports

Steps to reproduce in 10.3:

1) Create a Report and tag Search Term Report

2) Any Index and any saved search is fine, no hits need to actually come back

3) Add 10 or more long STR terms (15 example terms using the ticket description are in the attached ""STR overlapping term example.csv"" file.

4) Run the STR

5) Open the term report and notice that the terms start overlapping when they are long enough.

Expected Behavior: The terms are spaced properly so they can be read easily.

Actual Behavior: The terms overlap and are difficult to read."

10.3 10.3

2020-08-28 REL-440119 RDO Framework

Steps to reproduce:

1. Create a multiple choice field on the document object.

2. Add 1 choice with 2 child choices via Choices Tab and Save.

3. Open any document.

4. Edit the layout and add this the choice field from step 1 as a check box list to a layout and save.

5. Click Edit and open Choice Editor by clicking the Manage link under the field created in step 1.

6. Click the alphabetize button to reorder the choices.

7. Click Save and Close.

Expected: The layout reflects the changes made to the layout.

Actual: The layout does not reflect the changed made to the layout."

10.3 10.3

2020-08-28 REL-436387 Publish Incredibly expensive query causes publish jobs to get stuck during the PublishBatchOfMasters phase of Export. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2020-08-28 REL-412995 Imaging A non-admin user can be assigned certain administrator-level permissions, such as the ability to view the Worker Manager Queue tab and update job priorities / cancel jobs in the queue. When one of these non-admin users attempts to update the Job Priority of an Imaging job (either mass imaging or imaging sets), an error is thrown and the priority is not updated. Since the user has these admin permissions but is not an administrator, I believe the expected behavior is to allow the user to change the priority. Canceling of Imaging jobs from the Worker Manager Queue works as expected for these non-admin users. 10.2, 10.3 10.3

2020-08-28 REL-417283 Integration Points Currently, event handlers which are updating integration points configuration are attempting to load the entire list of integration points before processing them and later update them one by one. This is causing serious performance issues when there is a significant number of integration points. 10.3 10.3

2020-08-28 REL-426324 Authentication Upgraded JQuery javascript library from 3.4.0 to 3.4.1 10.3 10.3

2020-08-28 REL-417100 Publish The new dedupe stored proc script runs very slow on SQL server versions lower than 2017. This makes the publish job stuck in the dedupe phase. Our assumption was, this only happened because of SQL Server version 2017 and lower (based on incidents from on-prem clients). But recently, we encountered this issue with KPMG New Zealand R1. Hence our assumption that this might be related to SQL Server version 2017 and lower might not be true. 10.3 10.3

2020-08-28 REL-403062 Discovery When ingesting an EML file with line enders that don't conform to spec, it is possible for the 3rd party chilkat library to drop attachments. The problem has been verified to affect individual attachments when the line enders for the MIME boundary marker that precedes them are of differing types. Fix details: The solution to this problem is for us to normalize line enders as we did in the past (make all line enders CRLF) but when doing so we need to not change line ender values when they are with binary encoded MIME parts. 10.3 10.3

2020-08-28 REL-411997 Discovery

Large RSMF Files Lose Attachments - Backport On-prem. Reported issues:

1: Attachments are NOT being extracted for large files. The file gets processed and can be viewed but no attachments.

2: No error is generated to tell me attachments are missing.

Fix details: The issue is tied to a limitation of Chilkat when processing such abnormal file sizes. The engineering team has added better error detection and handling to inform the customer if such limits are reached."

10.3 10.3

2020-08-28 REL-466604 Discovery Text Extraction for complex CAD drawings may fail, due to workers timing out while trying to image the file. If the imaging portion of a text extraction job on a CAD file times out, there is no way to increase the timeout for the retry. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022 Server 2023

2020-08-18 REL-463183 Assisted Review When using Case Dynamics and Active Learning, Save and Next doesn't always serve up the next active learning document in HTML viewer. Workaround is to use the Hydro Viewer or click Save and Next twice. Server 2022 Not Planned

2020-08-14 REL-461741 Publish As part of a successful upgrade or restore, an agent error on invalid jobs may occur for Processing Sets that were part of archives with the "Include Processing" setting not selected. Server 2022 Not Planned

2020-08-14 REL-461912 Assisted Review Reviewers using the Aero Viewer will not be able to review documents in sample based learning. The classic viewer works and all other areas of sample based learning are fully functional. Server 2022 Not Planned

2020-08-13 REL-421822 RDO Framework Newly created RDOs do not appear in recents list when Relativity Forms is enabled. They do appear in subsequent user sessions. Server 2022 Not Planned

2020-08-12 REL-461202 Relativity Forms Customer who set Maximum_length of 1-3 on Fixed-Length Fields cannot use it in an item list, or the item list will not load. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2020-08-10 REL-444080 Relativity Forms Currency, Decimal, and Number fields may have incorrect formats in European markets, and will default to use US number formats. 10.2, 10.3 Server 2022

2020-08-10 REL-339093 Discovery Text encoded PDF files that have HTML tags in its header information prior to PDF declaration may be identified as HTML files. These circumstances are rare as PDF files should always have their PDF declaration prior to the HTML tags in its header information according to Adobe documentation. 10.2 Not Planned

2020-08-10 REL-460007 Errors When navigating through individual errors in the Document Errors tab, an empty webpage may load when a user clicks follows this specific workflow. Click into an individual document error, click their browsers refresh button, and then click the Document Errors tab to go back to the list page. If this happens, refreshing the webpage once more will load the page correctly. Server 2022 Not Planned

2020-08-09 REL-455310 RDO Framework Icons are required for tabs shown in the sidebar, but if a user edits an existing tab and toggles Show in Sidebar to true, the icon field is not being marked as required. Server 2022 Not Planned

2020-08-09 REL-458494 RDO Framework If Tab Sync removes a tab from the sidebar and the user tries to go in and edit that tab afterwards there is a UI issue where the icon control appears when it shouldn't. The workaround is to toggle Show in Sidebar on and off again to resolve the issue. Server 2022 Not Planned

2020-08-09 REL-441262 RDO Framework If a user edits a tab using the pencil icon on the Tabs list page, the parent tab dropdown may not be populated with the most up to date information. After waiting 30-60 seconds the correct information should auto populate. Server 2022 Not Planned

2020-08-07 REL-422390 Discovery If the processing profile setting to exclude embedded objects, the 'Contains Embedded Files' field will return 'No' regardless of the existence of them. Server 2021 Not Planned

2020-08-07 REL-393988 Discovery Some Word documents containing VBA code may be falsely reported as having hidden data. Server 2021 Not Planned

2020-08-07 REL-260727 RPC Documents that had searchable PDFs created will show a -1 page count in the matter inspector. 9.0 Not Planned

2020-08-07 REL-350312 Field Mapping When mapping fields to Invariant fields, environments with an extremely high number of metadata fields discovered may be stuck when loading all Invariant fields when choosing field source. 10.1, 10.2, 10.3 Server 2022

2020-08-07 REL-443697 Processing Administration When using the Scale to Maximum Workers button on the Worker Monitor page, if the scaling fails, the button may be stuck in a "Scaling" state. Server 2022 Not Planned

2020-08-07 REL-211276 Discovery MSG files with a PR_INTERNET_CPID value over 50000 may not have their text extracted. A processing error is created. 9.5 Not Planned

2020-08-07 REL-241812 Discovery Files embedded in emails that don't have valid date metadata may be assigned a date equal to the date and time they were processed. 9.2 Not Planned

2020-08-07 REL-426785 Processing Sets When creating a Processing Data Source, there will be no warning pop-up about unsaved changes when navigating to a different tab. Server 2022 Not Planned

2020-08-07 REL-445089 Search Term Reports Mass Copy of a Search Terms Report fails to copy for Search Terms Reports with more than 30,000 terms. Server 2022 Not Planned

2020-08-07 REL-436910 Errors When navigating through Processing Document Errors quickly, a blank screen may sometimes appear. A refresh can be done to workaround this issue. Server 2022 Not Planned

2020-08-07 REL-443902 Search Term Reports When you click on the searchable set popup to make an edit in an STR but cancel without making a change, if you reopen the popup the option originally set for searchable set is no longer selected by default. Server 2022 Not Planned

2020-08-07 REL-363865 Field Mapping If a Relativity field is named "File Path" is mapped to the Invariant field "Source Path", it will instead be populated by the Invariant field "Native Path Link". 9.4 Not Planned

2020-08-07 REL-366903 Reports When Data Grid is enabled on the Extracted Text field, the Processing Text Extraction report will incorrectly display that no documents had their text extracted. 10.3 Server 2022

2020-08-07 REL-387274 Discovery Users may encounter document errors on certain emails that were encrypted with S/MIME encryption, despite having added the certificate correctly to the password bank. Server 2022 Not Planned

2020-08-07 REL-398618 Processing Sets When a data source has a destination folder set, and then between discovery and publish the destination folder is deleted, a user will not be able to set a new destination folder and the data source will not be able to be published. Server 2021 Not Planned

2020-08-07 REL-418686 Processing Profile On the Processing Profile and Data Source, clicking "Clear" on the Destination Folder does not clear out the current value. Server 2022 Not Planned

2020-08-07 REL-419671 Errors Processing Errors tab must be manually refreshed to show updated error statuses. Server 2022 Not Planned

2020-08-07 REL-424901 Publish When publishing documents from a processing set, the Created By value for the document may be captured as Relativity Service Account instead of the user who initiated the publish. Server 2021 Server 2022

2020-08-07 REL-432211 Processing Administration The Worker Monitor page may not show any information when viewed at low screen resolutions. Setting the web browser's zoom to a lower setting can be used as a work around. Server 2022 Not Planned

2020-08-07 REL-452772 Quick Create Sets When using Quick Create to make processing sets, and there is a high number of folders/files in the source folder, the folder browser may not display the folder tree. It will be stuck on a loading message. 10.3

2020-08-07 REL-455691 Field Mapping When mapping a field, if a user chooses the All Fields view, closes the field mapping modal, and then re-opens the modal, the Field Catalog view will be indicated, but all fields will be displayed. 9.6 Not Planned

2020-08-07 REL-459080 Discovery When processing an RSMF file over 200mb, attachments may not be discovered with no error message reported. 10.0 10.3 Patch 2

2020-08-07 HYDRO-9966 Reviewer Interface The Review Interface may start in the incorrect viewer mode (Native/Image/Production/Text) if accessed by clicking on the Document Identifier at the top of the Document Preview Panel. Server 2022 Not Planned

2020-08-07 HYDRO-10000 Reviewer Interface Filters applied to the Production History card in the Review Interface do not persist after navigating to another document. Server 2022 Not Planned

2020-08-07 HYDRO-11861 Reviewer Interface Document file icons displayed in the Document Quick List in the Review Interface are incorrect and do not match the file icons used in the primary list page on the Documents tab. Server 2022 Not Planned

2020-08-07 HYDRO-11176 Reviewer Interface The order of shortcut icons in the Related Items area of the Review Interface can change after clicking a shortcut icon. This does not occur if the options are instead selected using the dropdown. Server 2022 Not Planned

2020-08-07 HYDRO-11514 Reviewer Interface The Layout Mode dropdown in the Review Interface can sometimes display behind other elements on the page. Server 2022 Not Planned

2020-08-05 REL-428399 RDO Framework Navigation via the back button on multi object pop up forms could cause improper navigation of the main window, while leaving the pop up window open. Server 2022 Not Planned

2020-08-05 REL-428201 RDO Framework Though permissions work as expected, edit icons on associated object lists within forms can incorrectly display an edit pencil icon to users that do not have permission to edit. Once clicked, they would get an error. Server 2022 Not Planned

2020-08-05 REL-442393 Relativity Forms No data is displayed on associated item lists after the last item on the current page is deleted. User's have to navigate back a page to see data. Server 2022 Not Planned

2020-08-05 HYDRO-11852 Markup Sets When multiple redaction text options in a Markup Set begin with the same 25 characters, they may not be displayed as available options in the Image Viewer right-click context menu. This can be worked around by adjusting the redaction text so the first 25 characters are unique for each available option. 10.2, 10.3, Server 2021 Server 2022

2020-07-29 REL-442098 Processing Profile The create/rename dropdown in the Destination Folder selector when creating a Processing Data Source may not display properly when there are many nested folders present. Server 2022 Not Planned

2020-07-20 REL-345686 Transcripts Pagination and Word Index do not respect page/line values with Volume II transcripts. 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-07-20 REL-372969 Transcripts When importing transcript files using the RDC, the Transcripts app does not respect the setting: "Do not copy files to a Relativity document repository." The physical files are removed from the network/client machine and are added to the Relativity document repository. 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-07-20 REL-451470 Conceptual Analytics If an index population fails due to a saved search validation issue (e.g., saved search contains no documents), then no email is sent to the Email notification recipients defined on the Analytics Index RDO. 10.2 Not Planned

2020-07-14 REL-374263 Transcripts Only the first instance of an exhibit's name is hyperlinked when LEF files with pre-hyperlinked exhibits is imported. To correct this problem, use the right-click option "Link All Occurrences" to hyperlink the other exhibit references within the transcript. 10.1, 10.2 10.3

2020-07-14 REL-445360 Reviewer Interface When a relational field name contains spaces, the icon displays incorrectly in the Related Items pane. This issue does not occur for default fields such as Group Identifier. Server 2021 Not Planned

2020-07-13 REL-435885 RPC If the RPCSessionTimeoutDelay (90 seconds by default) instance setting value is greater than or equal to the RPCSessionTimeout (15 minutes by default) instance setting value, Relativity will revert to the default values for both instance settings. This can cause more frequent automatic log outs of the RPC. 10.1 Not Planned

2020-07-13 HYDRO-11151 Reviewer Interface When developing Viewer extensions, referencing relative URLs in iframe cards do not work when the Viewer is popped out. Switching to an absolute URL will resolve this issue. Server 2022 Not Planned

2020-07-06 REL-446907 Assisted Review For the Next Gen viewer, Active Learning will not work with IE 11. If a user must use IE 11 they can use the classic viewer. The Next Gen viewer works with Active Learning in all other supported browsers. Server 2022 Not Planned

2020-06-26 REL-321723 Transcripts Duplicate note icons displayed when user is navigating to the next page of the Transcripts viewer. 10.2 Not Planned

2020-06-26 REL-321726 Transcripts In the Transcripts viewer, when using the search text bar, the highlighted results are shown with incorrect color and placement. For a workaround, we suggest using the Word Index to search for terms. 10.2 Not Planned

2020-06-23 REL-443873 Case Dynamics Case Dynamics Coding Pane does not link items when the viewer is undocked. Workaround is to use the Coding Pane only when the viewer is docked. 10.1, 10.2, 10.3, Server 2021 Server 2022

2020-06-22 REL-443772 RelativityOne Activity Dashboard The Data Utilization tab in the Activity Dashboard incorrectly shows no usage data at certain periods in the day. Server 2021 Patch 1 Server 2022

2020-06-13 REL-433236 Assisted Review When reviewing a document in active learning navigating to related items or email thread visualization, when you exit related items or email thread visualization there may be a new document. This is only an issue with the classic viewer, the next gen viewer will maintain the original document. Server 2021 Not Planned

2020-06-10 REL-411122 Reviewer Interface After rotating all pages on some multi-page documents, some pages may not appear to respect the rotation value in the Image Viewer. This inconsistency does not negatively affect markup location or burned redactions for productions. When this behavior occurs, the correct rotational value is persisted to the workspace database. 10.3 Server 2021

2020-06-10 HYDRO-10724 List Page When the Document Preview Panel is open, navigating between different tabs in a workspace and returning to the Documents tab can result in the viewer tabs within the Document Preview Panel failing to load. This can be worked around by closing and reopening the Document Preview Panel. Server 2021 Server 2022

2020-06-08 REL-415232 Transcripts Clicking on the All Video Clips link in the video player does not work when the transcript viewer is undocked. Server 2022 Not Planned

2020-06-08 REL-414402 Transcripts For the Key Terms transcripts report, the option to "Include Entire Question & Answer" does not return the full pair when used in combination with the "Include additional lines above and Below" option. 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-06-08 REL-404017 Reviewer Interface When loading multi-page documents in the Review Interface, the loading skeleton can intermittently fail to clear after the document content is loaded. This can result in the first page of the document being hidden behind the placeholder skeleton. 10.3 10.3

2020-06-08 REL-388443 Reviewer Interface Native file download through the Review Interface can fail if the native file contains a comma in its name. 10.2, 10.3 Server 2021

2020-06-08 REL-205363 Publish If the default destination folder set on the Processing Profile is deleted from Review prior to publishing a Data Source, an agent error will occur. In order to resolve this error, you can update the default destination folder value on the Profile to an existing folder and retry publish. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-06-08 REL-430837 Imaging Table split will not occur when there is a row that spans across multiple columns. 10.2 Not Planned

2020-06-01 REL-412624 Case Dynamics Timelines with 8,000 facts or more fail to render. The workaround suggestion is to create multiple timelines. Using conditions can help speed up the process. Server 2021, Server 2022, Server 2023 Not Planned

2020-05-26 REL-375868 Reviewer Interface When running a term search from the Document List that contains a special character, such as an ampersand, the resulting Search Highlights may display an HTML entity character reference rather than the character. This does not impact the accuracy of the highlights within the document. 10.1 Not Planned

2020-05-19 REL-340326 Assisted Review When filtering on Project Reviewers::User and use the condition 'is not set', it returns no documents. All other conditions for the Project Reviewers:: User field (including 'is set') work as expected. The Project Reviewers::User field is a reflected field of Project Reviewers. The Project Reviewers field filters as expected. 10.0 Not Planned

2020-05-13 REL-412191 Case Dynamics Offline Report fails to download when name of report contains comma. 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-05-13 REL-407151 Transcripts Linked exhibits numbered wrong for transcripts with over 10 exhibits. 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-05-13 REL-404200 Transcripts "Relativity Native Type" field gets overwritten for existing Transcripts with the native type of the newly uploaded Transcript. Server 2021, Server 2022, Server 2023 Not Planned

2020-05-08 REL-422360 Case Dynamics When saving data on a custom view, row is not put into view mode; i.e. row remains open. When you refresh, you see that the data is saved but the UI is not updated correctly. 10.3 Server 2021

2020-05-06 REL-320221 Navigation If a document present in a user's review queue is deleted by a different user, navigation in the Review Interface can become unresponsive upon navigating to the deleted document. This can be worked around by reloading the Review Interface. 9.7 Not Planned

2020-05-06 REL-412974 RelativityOne Activity Dashboard The User Performance tab in the Activity Dashboard is not correctly showing which user ran a long running query. The value being shown is not correct. Server 2021 Server 2022

2020-05-05 HYDRO-8217 Reviewer Interface While the Mass Redact operation is in-progress, if the Viewer is changed to a different mode then back to the Image Viewer, the Review Interface buttons can become unresponsive. This can be worked around by refreshing the page or exiting and re-entering the Review Interface. Server 2021 Not Planned

2020-04-30 REL-426221 Publish The All Custodians and All Paths/Locations fields are only populated on primary documents that have duplicates. These fields are not populated on unique documents, even if that document's data source has dedupe enabled. 10.2 10.3

2020-04-29 REL-384383 Reviewer Interface When the name of the field tagged as the Document Identifier begins with an integer, an incorrect syntax error can be thrown when attempting to view documents. 10.2 10.3

2020-02-11 REL-388847 Searching Fixes an issue where search syntax is not being properly set in session when running a saved search against an index. This can result in highlights incorrectly not being found if another syntax (such as dtSearch) should be used. 10.0, 10.2, 10.3, Server 2021 Server 2022

2020-03-30 REL-412398 Extensibility Points Fixes an issue where a previous hotfix caused Kepler services to fail to start and front-end ARM pages to not load. 10.2 10.2

2020-03-25 REL-414456 Field Mapping Fixes issue where a previous hotfix caused Processing field mapping to crash. 10.2 10.2

2019-09-06 REL-132588 Processing Sets Fixes Processing defect where native files that have been published to Relativity are incorrectly deleted. 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2019-05-06 REL-318333 Searching Fixes dtSearch defect where fields that exceed 512 KB are potentially not included in index. 10.1 10.1

2020-02-25 REL-398048 Reviewer Interface Fixes redaction defect where redactions are deleted when navigating to document with conversion error for image or imaging status of error or pending. 10.2 10.2

2020-01-30 REL-391724 Admin Operations Fixes an exception thrown during a failed mass delete when the original failure's exception is too large to fit in the Status column of the MassOperationProcessState table which only allows 900 characters. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2020-01-23 REL-388420 Authentication Changes how Relativity sets authentication-related cookie information for SameSite cookie behavior for Google Chrome 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2020-01-22 REL-375627 Service Bus Conversion becoming periodically unresponsive in RabbitMQ environment 10.1 10.1

2019-10-12 REL-371102 Structured Analytics When Name Normalization is run in Relativity version 10.1, 10.2, or 10.3, pre-existing Entities that could be referenced by Legal Hold, Collect, Processing, Analytics, Case Dynamics, or custom applications within the workspace, may be deleted without any errors or notifications to alert the user. 10.1 10.1

2020-04-22 REL-322205 Case Dynamics When the level on nesting goes beyond 10 levels deep, the Offline Report and the Mass Action export to CSV or XLS, will not returns results in the correct order. The workaround is to keep nesting up to 9 levels. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-04-15 REL-405418 Imaging Foreign language characters may be in different order (left to right, right to left) when using the native imaging profile. The issue happens in environments with Windows 2012 and Office Word 2016 combined. 10.1 Not Planned

2020-04-14 REL-420257 Discovery Microsoft changes the Excel Last Accessed metadata on Excel files when they are opened, leaving that change in place even if the user opening the file makes no edits or does not save the file when closing it. This results in a slightly different file being stored which, when hashed, will not have the same value as it did before being processed. In all other ways the post-processed Excel file is identical to the pre-processed file. Server 2021 Server 2022

2020-04-08 REL-419384 RDO Framework The quick link to the layout information page on the layout builder is not working in the Aero UI. Users can still navigate to the layout information page by going into the layout object directly. Server 2021 Not Planned

2020-04-08 REL-383181 Reviewer Interface In the Review Interface, the Persistent Highlight Pane may start expanded and not collapse until all highlight hits are found in the current document. Server 2021 Not Planned

2020-03-19 REL-406546 Quick Create Sets When using Quick Create Sets to create Processing Sets, there is a potential for a timeout to occur within workspaces with large amounts of Processing Sets. Server 2021 Not Planned

2020-03-10 REL-410640 Publish Deduplication may run slower than expected on SQL server versions lower than 2017, at times causing publish jobs to become stuck. 10.3, Server 2021 Server 2022

2020-02-26 REL-402333 Assisted Review

There is a known issue where Elusion Tests will not complete in a timely fashion due to one (or more) documents being assigned to a reviewer who is no longer active in the review. In the latest Chrome and Edge browsers, an unsaved document is not automatically freed upon closing the browser, clicking browser back button, refreshing browser, or clicking "Return to document list". Freeing a document allows it to be reviewed by another reviewer.

It takes one hour post the user logging out of Relativity for the document to be unassigned. This impacts the elusion test if the user leaves the viewer without saving the document, the elusion test document won't be available for another user until one hour after the user logs out of Relativity. If this document needs to reviewed by a different reviewer before the timeout, customer support can free the document.

Server 2021 Server 2022

2020-02-21 REL-228436 Text Extraction

When using the native text extraction option, header or footer text from Excel documents that have a different header/footer on alternating pages will be missing from the document's extracted text. This is not an issue when using Processing instead.

9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2022

2020-02-17 REL-394911 Case Dynamics When using the dropdowns on the Key Entities field in the Case Dynamics list views, if the entity does not have the Type field set, the entity will not appear as an item you can link. To make the entity appear in the list of items you can select to link, set the Type field to Person or Organization. 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-02-14 REL-400086 Conceptual Analytics The single click filtering should be applied upon selection of a single cluster. The original intent upon selection of a single cluster was that the single cluster would immediately be added as a filter condition, similarly to how Pivot Widgets and Communication Analysis currently works. Changing the filtering interaction on Cluster Visualization makes the user experience across pivot widgets and analytic widgets. 10.3 Server 2021

2020-02-14 REL-399797 Conceptual Analytics

The implementation of the changes:

• “View Nearby Clusters” feature should have the same filtering interactions revisions but this sub-feature wasn’t identified in original requirements

10.3 Server 2021

2020-02-14 REL-368274 Case Dynamics

When a user upgrades Case Dynamics to a Foxglove or above version, they will not see the people that were linked in the Offline Report prior to the upgrade. This issue stems from a problem with our migration code where people listed in the Person object are converted into Key People (on the Entity object) and must be relinked using the Key People (Entities) field on the Report Set object. This second step is not taking place.

There is a workaround for users where they can find the people (now Key People) that were not re-linked to the Offline Report(s) during the migration. The user can create a custom view on the Report Set object where the, Name, Report Set People and Key Entities fields are listed. Once the view is created, the user can go to the Report Set tab, open the new view and see the Key Entities that need to be relinked to the Report. Once the user finds the people that need to be relinked, they can go into the Offline Reports and manually link the Key People (and regenerate the report) or use the RDC to do an overlay

10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-02-10 REL-203741 Discovery For EML files containing attachments encoded in binary format, there is a possibility that the attachment is extracted incorrectly, with binary differences introduced into the extracted file that can render it unable to be opened or processed. 9.5, 9.6, 9.7 10.0

2020-02-05 REL-376129 Mass Operations When designation names include one of the following special characters: single quote, double quote or back slash, the Transcripts Viewer Save as PDF print option fails and a PDF of the transcript is not created. To workaround this issue, remove the special characters by editing the designation name and run the Save as PDF operation. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2020-02-04 REL-398144 Integration Points The Integration Points application on Relativity version 10.1.290.1 does not work properly with Microsoft Edge 41.16299.1480.0. To solve the issue versions 10.2 and higher are recommended for use. 10.1 Not Planned

2020-01-31 REL-233019 Discovery When processing HTML body type emails that include both VML and non-VML formatting, only VML formatting will be respected. This results in any inline images in the non-VML formatting to be extracted as children even if the profile option to not extract inline images option is selected. Additionally, the "Hidden Attachment" metadata will not be properly set. 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2020-01-31 REL-389665 Production Sets

Produced Images with header and footer applied will be blank for the two following image properties:

Tall Skinny Image

Image Width in Pixels < (8.5*dpi)/3

Image Height in Pixels > (11*dpi)/3

or

Short Wide Image Image Width in Pixels > (8.5*dpi)/3

Image Height in Pixels < (11*dpi)/3

10.2, 10.3 10.3

2020-01-29 REL-301569 Integration Points For the import loadfile type jobs in Relativity Integration Points, on third step: 'Preview Options' -> 'File' or 'Errors' or 'Choices & Folders', preview is not generated. The page remains in 'Preparing Preview' status and the error is logged: "Unable to check the progress of the given Preview Job Please check Error tab for more details" 10.2 Not Planned

2020-01-28 REL-378655 Hold Admin When viewing a Communication, clicking the Custodian Open Items report does not display the list of open items. 10.3 Server 2021

2020-01-22 REL-390597 Assisted Review There is an edge case in active learning in which workspace runs out of artifacts ids. To come across the defect, an agent or service bus must be in error, a deadletter failed to retry, or an index population failed. In addition there must be skipped documents removed from the index. 10.0 10.1

2020-01-17 REL-394469 Reviewer Interface If multiple similarly named relational fields exist, a generic error may be thrown in the Review Interface. This occurs when two or more relational fields contain at least one space and have the same string of characters directly before the first space. 9.6 Not Planned

2020-01-16 REL-393524 Reviewer Interface When viewing PowerPoint documents with hidden slides, the Show/Hide Hidden Items button on the toolbar does not toggle the hidden content. This can be worked around by clicking the orange toaster notification in the lower-right of the viewer. 10.3 Server 2021

2020-01-16 REL-393534 Reviewer Interface If the Review Interface is open in multiple browser windows/tabs/pop-ups, users will be unable to navigate between documents in all but the most recently opened window/tab/pop-up. 10.3 Not Planned

2020-01-14 REL-393255 Transcripts When generating an Annotation Digest report, you may see duplicate items listed in the section where the Case Dynamics objects are listed. This issue arises when you use the right-click Link option to link items like facts to your transcript. To generate the Annotation Digest report correctly, select only one of the items that's listed twice. Server 2021, Server 2022 Not Planned

2020-01-13 REL-387720 Searching When modifying the Order or Active field on a Keyword Search index, an error will appear informing you to contact your administrator requiring you to navigate back to the Relativity home page. 10.2 10.3

2020-01-02 REL-389646 Mass Operations When attempting to delete an Active Learning project but an error occurs, the error message will sometimes be displayed as "Error: Running" instead of a more descriptive error message. 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2020-01-02 REL-389646 Audit When exporting approximately 400,000 or more audit records from the Audit tab, the export progress window can result in a 502 error. 10.3 Server 2022

2020-01-02 REL-389650 Audit When exporting any amount of audit records from the Audit tab, the mass operation pop-up window will appear as normal. Once executed, the progress window will display normally, but once the window closes no other action will occur without any error message available. 10.3, Server 2021 Server 2022

2020-01-02 REL-348743 Processing Administration On the Processing History page, unexpected results occur when filtering on column headers while also making use of the checkbox selectors. Server 2021 Server 2022

2019-12-18 REL-388169 Assisted Review If the browser is refreshed in the viewer, the document will be considered outside coded, not coded in an Active Learning review queue. Server 2021 Not Planned

2019-12-18 REL-317309 Service Bus The Conversion Complete Agent does not respect the logging level designated and can result in a large number of logged messages. 10.1 10.2

2019-12-18 REL-329346 Reviewer Interface When adjusting zoom in the Viewer using CTRL + mouse wheel, sometimes the zoom value in the toolbar does not update as expected. 10.1 10.2

2019-12-18 REL-331864 Entity In workspaces with greater than 200 entities, the document numbering prefix assigned to any given entity will fail to automatically overwrite the document numbering prefix on the data source when the entity is linked. The prefix can still be manually changed via the UI. 10.1 Not Planned

2019-12-17 REL-387896 Reviewer Interface When navigating across multiple documents in the Viewer, the zoom level does not persist between documents. 10.1 Not Planned

2019-12-12 REL-273874 Reviewer Interface When the UseDistributedAuthenticationTokenToggle toggle is True, Relativity Document Compare can fail after selecting the comparison document. 10.1 Not Planned

2019-12-06 REL-372964 Reviewer Interface When launching the Stand-alone Viewer for a document not in the current review queue, such as when opening a document from the Related Items Pane, the Image Viewer mode can sometimes fail to initialize. 10.2 10.3

2019-12-04 REL-383435 Reviewer Interface After undocking and redocking the Viewer in the Review Interface, the Coding Pane does not resize to match the appropriate width after the Viewer is redocked. This can be worked around by manually resizing the Coding Pane. Server 2021 Not Planned

2019-12-02 REL-369004 Hold Admin There is a defect in Chrome browsers version 75 and higher that will not allow printing of Legal Holds reports from Chrome.. As a workaround, you can save the report to a PDF and then print the PDF. You can also choose to use another browser when printing as this is an issue with the Chrome browser only. 10.1 Not Planned

2019-11-21 REL-379786 Imaging An error may occur when importing a native imaging profile with custom application field codes to a workspace. 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2019-11-20 REL-318942 Case Dynamics When using the Case Dynamics Mass Export to CSV operation with a long text field which has two commas in the name, the CSV file will be incorrectly generated. The workaround for this issue is to use the Mass Export to XLS option. From there the XLS can be converted into a CSV, as needed. Alternatively, the commas from the field can be removed and you can use the CSV option for exporting. 10.1 Not Planned

2019-11-18 REL-356643 Case Dynamics

When setting up conditions for the Timeline Builder using the Is Like and Is Not Like operators, no results are rendered.

9.7, 10.0, 10.1 10.2

2019-11-14 REL-352877 Case Dynamics Adding a custom file field to Case Dynamics views is not supported. You can use the attachment tab, which is provided on the Case Dynamics layouts, to upload supporting documents. 10.0 Not Planned

2019-11-11 REL-375616 Case Dynamics When you attempt to generate a primary Report an error is thrown and the report is not created. The workaround for exporting items to XLS or CSV is to use the Mass Action from the ListView tabs of Case Dynamics. 10.3 Server 2021

2019-10-24 REL-185494 Discovery When Discovering CAB archives, any documents located inside nested folders of the archive will not be discovered. The workaround is to manually expand the CAB archive using 7zip prior to processing. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2019-10-24 REL-363603 Assisted Review The relational field used in family based review can be deleted. If the field is deleted the active learning project is not accessible. Server 2021 Not Planned

2019-10-10 REL-366657 Discovered Files On the Discovered Files page, clicking on Export to XLSX from a pivot will not trigger an export. 10.3 Server 2021

2019-10-09 REL-366389 Imaging When imaging excel files with any Native Imaging Profile set to Auto-fit Rows and Auto-fit Columns set to yes, and Print Area set to "Ignore Print Area", long Excel cell text is cut off at the length of the width of the page. 8.2 Not Planned

2019-10-01 REL-361763 Reviewer Interface In Chrome 77 when using a Single Sign On (SSO) provider, the Review Interface may fail to load and display a blank page. This can be worked around by rolling back Chrome to version 76 or below, launching Chrome with web security disabled, using a different web browser, or accessing Relativity without using SSO. 10.0, 10.1 10.2

2019-09-25 REL-350909 Case Dynamics When you are on the last document in the item list and you open the Case Dynamics Coding Pane, you will see a Save and Next button where the Save and Back button should be. Clicking on the Save and Next button will result in a spinner since there is no other document to pull up in the list. To save your Case Dynamics coding decisions, the workaround is to click the Save button on the Case Dynamics Coding Pane. Then if you want to return to the Document item list view, you can click on the Save and Back button on the standard Relativity layout or click on the Return to document list link at the top left hand corner of the Viewer. 10.2 Not Planned

2019-09-25 REL-355132 Case Dynamics When undergoing Active Learning document review and the Save and Next button on the Case Dynamics Coding Pane is clicked, the next document in the Active Learning queue is not served up. 10.1 Not Planned

2019-09-23 REL-357550 List Page Security groups with permissions only to the Advanced and Saved Search browser will land on the browser with a default document view to all non-secured documents instead of an empty saved search screen. This issue has been resolved in 10.1.3 and up. 10.0 10.1

2019-09-17 REL-357442 Processing Sets When a Processing Data Source is re-published, the Last Publish Time Submitted field will no longer be populated. 9.6 Not Planned

2019-09-04 HYDRO-4966 Reviewer Interface When Markup Visibility is set to Hidden in the Review Interface, changing the selected Markup Set will re-enable the redaction and highlight tools which can allow users to draw redactions while hidden. 10.2 Not Planned

2019-09-04 REL-354724 Unified Experience

For customers who are using Workspace Portal, the version packaged in the 10.2 version of Relativity/RelativityOne can break existing integration with prior versions if the context user for the Workspace Portal OAuth client does not have the following email address: wp@relativity.one.

Mitigation requires the following steps:

- Navigate to the OAuth client used for Workspace Portal in the satellite instances and identify the configured user.

- Navigate to the Users tab and search for the user identified in Step

- 1. If the configured user is an active user in the system or not a specific user for the Workspace Portal app (including Relativity Admins or a Relativity Service Accounts), then a new user must be created and added to the group

- 2. For more instructions, see Workspace portal .

- 3. Edit the user and replace its email with the required by Workspace Portal: wp@relativity.one

Resolution steps are also in this KnowledgeBase article.

10.2 10.3

2019-09-03 REL-320642 Imaging Canceling an imaging job from Worker Manager Queue may cause duplicate image errors. You will have to manually delete images from documents that have the duplicate image error. 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2019-08-28 REL-307564 Audit When querying the All Audits view in the instance level Audit tab, an exception is thrown if you do not have access to a particular workspace. A workaround is to create a new View to or create a filter to exclude the workspace(s) you do not have access to. 9.5, 9.6, 9.7, 10.0, 10.1 10.2

2019-08-28 REL-339956 Relativity Scripts & Utilities For large case Text Migrations, you may encounter a timeout during the initial setup preparing a Field for Text Migration. Increasing the timeout limit on DataGridMigrationLongRunningQueryTimeout to 7200 will allow the job to proceed. 9.7, 10.0, 10.1 10.3

2019-08-28 REL-345713 Audit When viewing the History tab, the History tab will not display records and result in an error. 10.1 10.1

2019-08-28 REL-353038 Searching When copying a dtSearch index with the Create Accent Sensitive set to 'Yes', the setting will be set to 'No' on the newly created dtSearch index. After copying the dtSearch index, click Edit and update the Create Accent Sensitive to ensure the setting is correctly applied before index build. 10.2 10.3

2019-08-27 REL-350196 Admin Operations A user not part of a system admin group will not be able to see the message of the day. The fix for this defect will be in Relativity 10.2. Please reach out to Support if you need the fix any sooner. 10.1 10.2

2019-08-26 REL-352363 Case Dynamics When the Case Dynamics - Coding Pane permission is removed for a group and Preview is used to review the permissions setup, the Case Dynamics link will still appear on the coding layout. When you log in as the user, the links is correctly removed. 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2019-08-22 REL-322344 Extensibility Points On the Object Manager API, when a .NET update method is called by passing a MassUpdatePerObjectsRequest object containing objects with Artifact IDs not ordered numerically, the service assigns values to the wrong objects. This same issue occurs when making a RESTful update call with the massRequestPerObject object. 10.0 10.1

2019-08-14 REL-205051 Errors

In certain cases the status of document error instance in set to In-Progress, but should be Ready to Retry.

Steps:

- Run a Discover and Publish job, which will generate 3 errors for the same file ID.

- Resolve the publish problem and Re-Publish the set.

Results:

- The publish error is resolved and is marked as Retried - Expected.

- The document error is marked as In-progress when Republish started, but never got flipped to Ready-to-Retry when the job completed. - Not Expected, should be marked as Ready to Retry, since there are two more errors with the same status.

9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2019-08-09 HYDRO-4507 Reviewer Interface In rare scenarios, markups can render in the thumbnail viewer but not the main Image Viewer. This can be worked around by resizing the Viewer window or browser window. 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2019-08-09 REL-347379 Transcripts In a workspace restored using ARM, previously existing exhibit links will log out the user when clicking on the exhibit link in the Transcripts Viewer. However, the exhibit links in the Transcripts layout will open the documents successfully. Additionally, newly created exhibit links will open successfully when clicking in the Transcripts Viewer as well as the Transcripts layout. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2019-08-06 REL-323389 Case Dynamics When the Case Dynamics coding pane is made small and numerous documents are coded, the pagination arrows can shift to the right slightly. Resizing the pane restores the buttons to their original position. 9.6, 9.7, 10.0, 10.1 10.2

2019-08-01 REL-344863 Assisted Review The Classification Index rank search may error on larger projects if the index is building or populating. The search will try to complete for five minutes, however, if the index hasn't finished building within this time, the search will fail. You can retry running the search once the index build completes. 10.3 Not Planned

2019-08-01 REL-282474 Discovery When discovering Bloomberg XML files, there is a chance of performance degradation and incorrectly extracted content. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2019-07-29 REL-343629 Relativity Desktop Client When exporting with the default settings, each zero byte file contained within the export generates an error message stating "Empty file. ... 0 document(s) exported." 9.7, 10.0, 10.1, 10.2 10.3

2019-07-27 REL-343579 Billing Using the MaxBilling application can result in performance impacts to RelativityOne due to one of its agents locking the audit table, which is critical. 10.2 10.2

2019-07-25 HYDRO-4087 Reviewer Interface The Image Viewer or Production Viewer can fail to fully load if a user undocks the Viewer, opens another document through a link in the Related Items Pane, and re-docks the Viewer. This can be worked around by refreshing the browser window. 10.2 Not Planned

2019-07-25 REL-319139 Custodian Portal The Questionnaire Responses Export (report) will contain no data for workspaces that were previously ARMed. 9.6, 9.7, 10.0, 10.1 10.2

2019-07-25 REL-327820 Hold Admin Changing a custodian's assigned role to a role that has the Place On Preservation Hold system tag enabled may cause the Legal Hold application to become unresponsive. Refreshing the page will bring the application back and the change will have been applied successfully. 10.0, 10.1 10.2

2019-07-25 REL-337048 Searching When indexing a document greater than 2 GBs, your index build will fail with the following error: "Arithmetic operation resulted in an overflow." 9.6, 9.7, 10.0, 10.1 10.2

2019-07-25 REL-161185 Audit Users applying a sort on the Object Artifact ID in the Audit tab will receive an error. 9.5, 9.6, 9.7, 10.0, 10.1 10.2

2019-07-25 REL-339773 All Products Object Manager API read operations of Long Text fields greater than the max length of 100,000 characters will be truncated. When saved, any value that's greater than the truncated 100,000 characters will not be audited. 9.6, 9.7, 10.0 10.1

2019-07-23 REL-272306 Errors If a Document Error is Ignored, an error will be logged under the Errors tab in Home mode. However, the Document Error will still be properly ignored. 9.5 Not Planned

2019-07-15 REL-339926 Reviewer Interface In the legacy Transcript viewer, the word index and tag list will not render for the first transcript viewed. This can be worked around by navigating to another document then back to the transcript. 10.0 Not Planned

2019-07-11 REL-338573 Persistent Highlight Sets In Firefox, when rapidly switching between different Viewer modes the persistent highlight pane can fail to load. 10.2 Not Planned

2019-07-11 REL-338569 Reviewer Interface In Chrome, when rapidly switching between different Viewer modes the document can fail to display. This can be worked around by resizing any component of the Review Interface or refreshing the page. 10.2 Not Planned

2019-07-11 HYDRO-4143 Reviewer Interface In Safari, the coding pane can appear blank after rapidly navigating backwards in the Review Interface multiple times. 10.2, 10.3, Server 2021 Not Planned

2019-07-08 REL-329766 Audit The Artifact ID field cannot be queried on in the List View. As a workaround, use the Object Artifact ID as it contains the same data. 9.4, 9.5, 9.6, 9.7, 10.0 10.1

2019-07-08 REL-165051

When exporting images from workspace to workspace using the options of:

* Append

* Copy Images Yes

* copy files to repository No

Then running a production set with the migrated documents the images lose their extension. The fix is provided in Relativity v.10.0 .

9.5, 9.6 10.0

2019-07-11 REL-336403 Relativity Desktop Client Any export that uses the "production precedence" feature in which any selected production includes natives will cause the RDC to abort with a "Read failed" error. 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2019-07-11 REL-323153 Production Sets When you upgrade a Production from 9.6 to any later version, the Produced Date field will be nulled. 9.7, 10.0, 10.1 10.2

2019-07-01 REL-28798 Publish If one or more errors occur on a container during discovery, some or all of the files in that container may remain undiscovered. If all discovery errors are not resolved prior to publish, unexpected deduplication results can occur due to the discovery of additional duplicate files during the retry/republish of these errors. In addition, Relativity may display a negative value for the unpublished file count. 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023

2019-06-26 HYDRO-3742 Reviewer Interface If a user selects a markup, then clicks a toolbar button, then clicks on the selected markup, then attempts to delete it using the 'Delete' keyboard key, the deletion will not occur. This can be worked around by de-selecting and re-selecting the markup or attempting to delete using the right-click context menu. 10.2 Not Planned

2019-06-26 HYDRO-3358 Reviewer Interface After submitting an image-on-the-fly job and quickly navigating to another document, the page count and zoom levels will not update immediately. The proper information will be populated when an event takes place, such as scrolling to another page or adjusting the zoom level. 10.2 Not Planned

2019-06-26 HYDRO-2711 Reviewer Interface When viewing a document image larger than 10,000 pages long, the conversion streaming status pill will not update to indicate conversion is complete. This can be worked around by exiting and re-entering the Viewer to refresh the conversion status. 10.2 Not Planned

2019-06-26 HYDRO-2636 Reviewer Interface Changes to markup visibility in the undocked or standalone viewers does not reflect in the primary viewer once redocked. 10.2 Not Planned

2019-06-26 HYDRO-2494 Reviewer Interface In Safari, when scrolling through a multi-page document image with a zoom level other than 100%, the top and bottom toolbars can sometimes display as solid black. This can be worked around by changing the zoom level or refreshing the browser page. 10.2 Not Planned

2019-06-26 HYDRO-1568 Reviewer Interface In the Image and Production Viewers, separators in the right-click context menu may not appear at browser zoom levels above 100%. 10.2 Not Planned

2019-06-26 HYDRO-3751 Reviewer Interface In Firefox in the Image Viewer, pressing the Backspace key without a markup selected results in a 'Back' navigation in the browser. 10.2 Not Planned

2019-06-26 REL-324689 Reviewer Interface Navigating to the end of a review queue in the undocked viewer and redocking can sometimes result in the window hanging or temporarily freezing. This can be worked around by refreshing the browser window. 10.2 10.3

2019-06-26 REL-329750 Reviewer Interface In Firefox, when switching layouts with unsaved changes a warning indicating unsaved changes exists does not get thrown. 10.1 Not Planned

2019-06-19 REL-314038 Case Dynamics System Admins and non-admin users with full Case Dynamic permissions (Delete & Add permissions for all the Case Dynamics objects), cannot delete an object from a Layout. Clicking on the Delete button on layouts throws an error and all associate objects are not unlinked. 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023

2019-06-19 REL-304183 Case Dynamics When the user does not have or has limited permission for the Entity object, the UI for the Case Dynamics Coding Pane and Inline Edit lists shows spinners and inconsistent loading behavior. Clients are advised to give users full permissions to the Entity object so that they can have a smooth user experience throughout the Case Dynamics application. 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2019-06-18 REL-330210 Assisted Review In Active Learning, running more than one update ranks operation at the same time in the same workspace can lead to SQL locks. To avoid this, it's recommended to only run Update Ranks on one Active Learning project in the same workspace at a time. 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2019-06-13 REL-327382 Imaging SQL deadlock errors may occur when the Set Native Time Zone Offset with DST agent is running. v6.0.1.6 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2019-06-07 REL-322221 Import API An import error when using the RDC has been seen stating: Error: Bulk load: An unexpected end of file was encountered in the data file. The OLE DB provider "BULK" for linked server "(null)" reported an error. The provider did not give any information about the error." due to a BCP load file issue preventing a successful import. 10.1 10.1

2019-05-31 REL-306465 Transfer API An import error when using the RDC has been seen stating "Error: SQL Statement Failed Error: Cannot bulk load. The file (file name) does not exist." To address this as a workaround set TapiForceBcpHttpClient to False. 10.0, 10.1, 10.2, 10.3, Server 2021 Server 2022

2019-05-30 REL-156962 RDO Framework Using the undo button immediately after a paste operation or addition of a merge field will delete the contents in the editor. 9.5, 9.6, 9.7, 10.0, 10.1 10.2

2019-05-28 REL-324556 Reviewer Interface After submitting an image-on-the-fly job and quickly switching Viewer modes or undocking and redocking the Viewer, the toolbar in the Image Viewer may render behind other elements and not be visible. This can be worked around by resizing the Viewer, or refreshing the page. 10.2 Not Planned

2019-05-27 REL-318958 Hold Admin When creating a Preservation Case if you enter just a Start Date or just a End Date for your date filter criteria, Legal Hold will hang. 10.0 10.1

2019-05-22 REL-319112 Reviewer Interface The Document Identifier in the top-left of the Viewer will incorrectly display the file icon of the previous document for documents without associated native files. 9.7 Not Planned

2019-05-17 REL-321081 Assisted Review If documents are deleted from the active learning project, the prioritized review progress chart may not display. The workaround is to populate the index. 9.5 Not Planned

2019-05-10 REL-314054 Assisted Review Pending document count for an Elusion Test can be incorrect if the time of the last model build erroneously appears to be before the examples were sent to the engine. This can occur if the workspace is moved or restored via ARM, or if the analytics server is restarted, during the Elusion Test. 10.1, 10.2 10.3

2019-05-08 REL-316281 List Page Filtering for document query and the search object will display a clickable link in the Name field which will result in a server error. 9.7 Not Planned

2019-05-07 REL-318761 Reviewer Interface When frame-flipping is enabled in the Viewer, media files may still continue to play in the background after navigating to the next document if there is not another document to preload on the back frame. 9.7 Not Planned

2019-05-06 REL-317651 RDO Framework When you mass move a set of documents from multiple folders into a folder, the documents will appear to have not moved in the folder browser and there is some inconsistency in how Relativity treats these documents' ancestry. The workaround is to create a temporary folder, mass move the documents to the temporary folder, then mass move them to the target folder. 10.1 10.2

2019-05-02 REL-317701 Reviewer Interface When navigating a modal using the tab key in the Image Viewer or Production Viewer in Internet Explorer, the focus is sometimes lost to other background elements on the page. 10.2 Not Planned

2019-05-01 REL-304946 Structured Analytics In rare scenarios, two or more identical emails with different Authors (normalized 'From' values) or Date Sent values are incorrectly marked as duplicate spares. A hotfix is available in certain versions of Relativity. For more information, see this article on the Relativity Community . 9.5, 9.6, 9.7, 10.0 10.1

2019-05-01 REL-301141 Relativity Desktop Client The .kwi and .kwe file settings may not deserialize correctly when using files created from earlier Relativity Desktop Client releases. The workaround is to recreate the settings file. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2019-05-01 REL-301212 Relativity Desktop Client Some imported documents do not appear in the Document list when the workspace/folder artifact identifiers match. The workaround is to view in the Document list through a Saved Search. 9.0, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2019-05-01 REL-315889 Relativity Desktop Client The latest VC++ runtime is a pre-req for Relativity Desktop Client and needs to be downloaded and installed in order to prevent any errors. 10.1, 10.2 10.3

2019-05-01 REL-315286 Relativity Desktop Client When importing production images, the Begin Bates value is set to NA. 9.7 Not Planned

2019-04-30 REL-316000 ARM ARM Archive Location length cannot exceed 260 characters. 10.1, 10.2, 10.3 Server 2021

2019-04-18 REL-310832 Production Sets A production job may fail during Branding when a document contains a redaction created in pre 9.4 version of Relativity. 10.0 10.1

2019-04-18 REL-307531 Mass Operations The Mass Operation "Send to Case Map" will not work if the case map view contains a single/multi-choice field and if the value is not set for a document. 10.0 10.1

2019-04-16 REL-304948 Imaging You cannot use Native imaging on MPX files with Microsoft Project 2013 or later. The latest Microsoft Project that can open it is 2010. You will need to have this installed on the worker or it will not image. You can also use Basic Imaging as a workaround. 10.1 Not Planned

2019-04-16 REL-310964 ARM Archiving a workspace without structured analytics, but with "Include structured analytics" selected fails. 9.7, 10.0, 10.1, 10.2 10.3

2019-04-16 REL-304224 ARM Analytics move jobs between different Analytics servers may fail due to not being able to delete analytics indexes. 9.7 Not Planned

2019-04-08 REL-299528 Relativity Scripts & Utilities When performing a migration of a document larger than 1 GB, an error occurs due to a SQL timeout and cannot migrate the document. A known workaround is to either delete the document from the workspace or overlay the document using the RDC to allow the migration to continue. 9.7 10.0

2019-04-08 REL-310368 Reviewer Interface Conversion may fail due to being unable to successfully parse an accessible path if the Windows temp location on an agent server contains a space character. 9.6 Not Planned

2019-04-02 REL-307639 Mass Operations Initiating a mass operation from the Saved Search list page with an index search applied may result in a higher than expected number of records affected when the underlying saved search is configured to include families. 9.4, 9.5, 9.6, 9.7, 10.0 10.1

2019-04-01 REL-308166 Searching Audits generated for changes to the Alphabet Text field of a dtSearch index will currently be created with empty Old and New value fields. 10.2 10.3

2019-03-28 REL-307530 Integration Points While pushing documents between workspaces instance-to-instance workflow does not work however it is available as an option in Integration Points Destination -> Relativity Instance as a Proof Of Concept feature. Promoting Data with Integration Points between instances is on RIP future enhancements roadmap. 10.1 Not Planned

2019-03-26 REL-304385 Structured Analytics The Communication Analysis widget cannot be added to workspaces where the Analytics application was installed after the 10.1 release. This does not impact workspaces created from a template with the Analytics application or workspaces that had the Analytics application installed prior to the upgrade. 10.1 10.3

2019-03-19 REL-261537 ARM After archiving a workspace some data may be archived twice, in the Invariant folder and in the NonRepository folder of the ARM archive. This issue is fixed in Foxglove. 9.6, 9.7, 10.0, 10.1 10.2

2019-03-12 REL-300711 Imaging Imaging Sets with high a percentage of Project files (in the hundreds) will result in an inconsistent image count. Re-imaging the file will fix the issue. 10.0 Not Planned

2019-03-06 REL-280915 Markup Sets Special characters are not displayed correctly in the Markup Set drop-down of the Markup Navigator in the Viewer. 9.6 Not Planned

2019-03-05 REL-299885 RDO Framework When using Firefox version 65.0.2 and using the Tab keyboard navigation to expand a tree node that is at least 10 levels deep the page may freeze for about 20 seconds. In order to workaround this, clicking the node to expand does not result in this behavior. 10.1, 10.2 10.3

2019-03-04 REL-282446 Audit When adding unsupported Fields to the List View in the Audit application, you will see an error because the fields cannot query the unsupported fields. As a workaround, ensure the following fields are not included in your View settings: Edit, Name, Security, System Created By, System Created On, System Last Modified By, System Last Modified On. 9.5, 9.6, 9.7 10.0

2019-03-04 REL-236894 List Page The pivot widget will display inaccurate results when pivoting on a choice field that has choices with the same exact name. To workaround this, the duplicate choice names will need to be edited to be unique for an accurate pivot. It is worth noting that choosing to Group By with the choice field will yield accurate results. 9.7 Not Planned

2019-03-04 REL-293132 Processing Sets Log files containing EML-like content are incorrectly identified as EML files. 9.2, 9.3, 9.4, 9.5, 9.6, 9.7 10.0

2019-02-22 REL-294713 Admin Operations When creating a Single Choice Field at the administrator level. If the name of the field matches a pre-existing field or the name contains any number between 0-6 you will be unable to use the manage link on the Status field via the Workspace Details page. If you run into this issue deleting or renaming the Single Choice Field will allow you to use the manage link. 10.1, 10.2 10.3

2019-02-20 REL-296563 Workspace You cannot assign a Workspace Admin group to a case during case creation. The Workspace Admin Group can still be assigned post creation via the workspace details page. 9.7 10.0

2019-02-18 REL-287767 Assisted Review If a categorization set associated with a classification index fails during the synchronization process, it may require database cleanup to proceed. This depends on the state of the data and nature of the failure. 9.7 10.0

2019-02-15 REL-295366 Reviewer Interface When attempting to view a document with a file size larger than the value configured for MaximumNativeSizeForViewerInBytes and with the native file missing from the fileshare, the Viewer will display a loading spinner without displaying an error indicating that the file size limit has been exceeded or that the file is missing. 9.6 Not Planned

2019-02-01 REL-281087 Reviewer Interface When multiple Persistent Highlight Sets contain the same term but different source types (terms vs field) only the term in the PHS with the lowest order value is considered for rendering. In certain scenarios this can result in the term incorrectly not being highlighted. 9.6, 9.7 10.0

2019-01-31 REL-248673 Reviewer Interface The Conversion Complete agent will log multiple information events each check in even when the logging level is set to log critical errors only. 9.6 9.7

2019-01-31 REL-283353 Audit When selecting a different Resource Pool, Audit agents cannot update to the new Resource Group selected. As a workaround, you need to delete and recreate or disable and enable the Audit agent to correctly update to the selected Resource Pool. 9.5, 9.6 9.7

2019-01-28 REL-267134 Custodian Portal Custodians are sometimes given a prompt for a username and password while filling out a questionnaire. This results in the custodian losing all of the answers they provided prior to the prompt. 9.5, 9.6, 9.7 10.0

2019-01-28 REL-221325 Custodian Portal Newly created Question Categories are not shown in Category list. 9.6, 9.7 10.0

2019-01-28 REL-272290 Hold Admin Hold notices that contain unicode characters in the subject line do not get emailed to custodians. 9.5, 9.6, 9.7 10.0

2019-01-28 REL-264797 Case Dynamics Tabs with Is Visible set to No are visible when the Tab Strip is displayed while in the Viewer. 9.7 Not Planned

2019-01-28 REL-284132 Reviewer Interface Page navigation buttons for document images are not visible when the Tab Strip is displayed while in the Viewer. 9.7, 10.0, 10.1 10.2

2019-01-24 REL-258848 Reviewer Interface After undocking the Viewer, returning to the document list, then returning again to the Viewer, the user is incorrectly sent to the docked Viewer rather than the undocked Viewer. 10.0 Not Planned

2019-01-17 REL-282185 RDO Framework When viewing user type fields on a layout, any user that has been disabled or removed from all groups assigned to the workspace will show up as a blank value in the layout. 9.6, 9.7 10.0

2019-01-17 REL-279671 List Page Changing to different document browser while saved search is loading causes display of empty Document list. The issue is reproducible on very slow network connection. 9.6, 9.7, 10.0 10.1

2019-01-17 REL-280270 List Page Opened documents are captured twice into the Recents list. 9.7, 10.0 10.1

2019-01-11 REL-272860 Imaging A user will not be able to select the field name option on the pop-up picker for the Mass Operations Saves as PDF. 9.7 10.0

2019-01-10 REL-236647 ARM During workspace restore, when DataGrid import stage runs for more than 24 hours, it will be retried causing the the same stage to be executed twice. The workaround is to change DefaultJobTimeout ARM instance setting to accommodate for additional time needed for this stage to finish and restart ARM agent afterwards. It will be fixed with version 10.0. 9.6, 9.7 10.0

2019-01-08 REL-279319 Imaging When installing Microsoft Office 2013 using the "Click to Run" option, missing images may occur when imaging using the native profile. Instead, install Microsoft Office 2013 using the MSI Installer option. As a workaround, Basic imaging will work as expected. 9.5 Not Planned

2019-01-02 REL-281895 Quick Create Sets Object Security Permissions still references Quick-Create Set(s) as Processing Assistant. 10.0, 10.1 10.2

2018-12-20 REL-263692 Reviewer Interface In rare scenarios the redaction toolbar buttons in the Viewer can be available to users without permissions to create redactions. This allows the user to draw redactions but does not allow those redactions to be saved or persist. 9.6 9.7

2018-12-20 REL-266307 Reviewer Interface When switching between multiple markup sets in the Viewer, redactions will not properly clear if the user does not have permission to create redactions and the second markup set selected does not have any redactions. 9.6 9.7

2018-12-20 REL-176988 Search Term Reports When viewing the Search Term Report, long search terms produced overlapping text making it difficult to view term results. 9.5, 9.6, 9.7 10.0

2018-12-17 REL-274690 Processing Administration The first time you open the Worker Monitoring tab, the "Scale to Maximum Workers" button may take up to 1 minute to be displayed. Refreshing the page will currently make the button appear more quickly. 9.7 10.0

2018-12-12 REL-267794 Hold Admin If the Portal Link merge field is included in the body of an Escalation message, the result will be that blanks are presented in the received email in place of the Portal Link. The reason for this is that we do not want the Portal Link to be forwarded to the escalation recipient (custodian's manager). 9.7 Not Planned

2018-12-11 REL-198561 Infrastructure The message column of the agents tab displays incomplete information. The message does not display any information about which processing set is in progress. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 10.3

2018-12-11 REL-189870 Infrastructure The error returned when processing encounters a corrupt file within an ALZ archive is incorrect. Currently the error reads, "Error occurred when attempting to open the ZIP file. Failed." when it should read, "Error occurred when attempting to extract a file from the ALZIP archive." 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2018-12-11 REL-189831 Infrastructure Password protected ALZ files can't be decrypted even with the proper password entered into the password bank. Processing users will need to decrypt these files manually. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2018-12-11 REL-179199 Processing Sets In some instances, EML files with Japanese text may not have their text extracted properly; the Japanese characters may be replaced with non-readable characters. Native imaging will also render these emails with the non-readable characters. These EML files can still be properly imaged using Basic Imaging, viewed using the viewer, or opened natively. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2018-12-10 REL-277638 List Page Clicking on any folder in Document folder browser ends up in Document List error if Folder Name field is secured in a given Workspace. 9.6 9.7

2018-12-10 REL-276991 List Page Clicking on any folder in Document folder browser in the New UI ends up in Document List error if Folder Name field is secured in a given Workspace. 9.3, 9.4, 9.5, 9.6 9.7

2018-12-07 REL-268850 Import API Note that in the current release of Bluestem 2, any document or object import using the RDC, RIP sync jobs, or Import API where multi-object artifact types contain duplicate records will not throw an error as expected and will link to the associated object. This will be addressed in the next release of RelativityOne in Bluestem 3. 9.7, 10.0 10.1

2018-12-07 REL-270591 Reviewer Interface Documents with an Unknown Native Type submit for pre-conversion multiple times instead of logging a single incompatible document alert. 9.6, 9.7 10.0

2018-12-07 REL-214689 ADS When clicking the Show Application Breakdown link on an application, an error stating "Relativity visualization script files could not be loaded." is displayed instead of the expected HTML file with associated item information. 9.6, 9.7 10.0

2018-12-07 REL-244652 Reviewer Interface After navigating between pages of an Associative List or Child List, or changing the page size of an Associative List or Child List in the Viewer, information for the next queued document may display in the Associative List or Child List. 9.6 9.7

2018-12-06 REL-277173 Assisted Review When population occurs in a Classification Index we automatically cancel the Elusion Test if it is in progress. The Elusion Test will appear in the 'Canceled' state but this action does not give you a notification that this cancellation has occurred. 10.0, 10.1 10.2

2018-11-30 REL-259530 Search Term Reports Search Term Reports can be created and run on an inactive dtSearch index. 9.6, 9.7 10.0

2018-11-30 REL-234236 OCR A long hyphen in a file share path will cause an OCR job to fail. 9.6, 9.7, 10.0 10.1

2018-11-30 REL-232087 Reviewer Interface When viewing the Document List while in the Reviewer Interface, HTML enabled fields display as plain text. 9.6, 9.7 10.0

2018-12-10 REL-266384 Production Sets SQL timeouts may occur when a large Production Set is deleted during active review hours. 9.7 10.2

2018-11-26 REL-267772 ARM A fix and a workflow for the potentially affected application installs while restoring ARM'd workspaces are now available. Please visit the Relativity Community site for information. 9.7 10.0

2018-11-23 REL-264836 Searching Filtering in a nested saved search selection popup might get unresponsive when the action is repeated in different workspaces within same user session. Page should be reloaded using Ctrl+F5 to workaround the issue. 9.6 9.7

2018-11-22 REL-243394 RDO Framework Drop-down field values cannot be selected using keyboard only in a Batch Set form when drop-down contains no type-ahead filter. 9.6, 9.7, 10.0 10.1

2018-11-21 REL-271670 List Page Fixed length text field values that contain leading white spaces cannot be filtered in ingrid filter when filter type is list. 9.7 10.0

2018-11-21 REL-267183 List Page Is some cases view loading via Favorites/Recents list results in a display of previously loaded view instead of one that is captured in a Recent link caption. 9.7 10.0

2018-11-21 REL-246630 Summary Reports Execution of Summary Reports times out after 5 minutes. 9.6 9.7

2018-11-21 REL-213349 List Page Dashboard object permissions are ignored when Relativity is used i a user group preview mode. 9.6 9.7

2018-11-20 REL-261787 RPC When attempting to create a searchable PDF from any document with a mix of extracted text and OCR text, the resultant PDF that is supposed to be searchable will not include the text derived from the OCR. 9.6, 9.7 10.0

2018-11-20 REL-270091 Assisted Review When Full Population in a Classification index occurs while a Prioritized or Coverage Review is in progress it is possible for reviewers to run out of documents to review until Population completes. 10.1 Not Planned

2018-11-20 REL-270096 Assisted Review If you perform a Full Population and then Update Ranks right after an Active Learning Project is complete (meaning an Elusion Test results are accepted/rejected) you will not receive any ranks. The CSR-rank fields will be empty. 10.1 Not Planned

2018-11-16 REL-266381 Markup Sets 9.6 9.7

2018-11-16 REL-269786 Audit When exporting audit data from the History tab, the selected rows from the History tab returns a empty file in Excel. 9.6 9.7

2018-11-13 REL-271291 Relativity Desktop Client Exporting a production to PDF that is over 9 pages with no 0 padding results in incorrect sorting in the PDF. If zero padding is used then it is sorted correctly. 9.5, 9.6, 9.7, 10.0 10.1

2018-11-09 REL-270225 Resource Servers In rare circumstances web server CPU usage can increase while converting document images with an extremely large number of pages. 9.6 9.7

2018-11-07 REL-120269 Processing Sets If the time zone on a Processing Data Source does not match the time zone on the Worker server, a job level error may occur during Publish. The workaround to this issue is to change the Worker's time zone to match the Processing Data Source, usually UTC for both. 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2018-11-05 REL-268388 Reviewer Interface When the HideDownloadNativeFileRadioButton instance setting is True the Prevent Native Download value is not respected and native file download can still occur when clicking the file icon. 9.5, 9.6 9.7

2018-11-02 REL-240268 Processing Sets When an empty container or an empty folder is submitted for Inventory, the set will be placed into an Agent Error state. 9.7, 10.0, 10.1, 10.2 10.3

2018-11-02 REL-266587 Production Sets Exporting a production through the Relativity Desktop Client will fail when more than one Multi-Object field is associated with the Production Information Object. 9.6 9.7

2018-10-25 REL-258459 ARM When performing an ARM Archive job on a workspace with a Lucene Search index, high memory consumption from the Archive of the index can cause the job to fail. 9.5, 9.6 9.7

2018-10-24 REL-250369 Imaging The Print/Save As PDF mass action will fail when used inside of a workspace containing a thousand or more productions. 9.6, 9.7 10.0

2018-10-24 REL-253312

Hold Admin

Legal Hold does not delete an associated project reminder when a Project is deleted. 9.6 9.7

2018-10-24 REL-237760 Infrastructure Legal Hold pulls over all existing projects when creating a new workspace from a template. 9.6 9.7

2018-10-23 REL-249915 Audit Audits migrating to Elasticsearch can fail migration due to differences in the XML formatting between new audits migrating and records that already exist in your Elasticsearch cluster. 9.6 9.7

2018-10-23 REL-266035 Active Learning Copying a classification categorization set causes jobs on the original categorization set to fail with the message "An analytics index can be associated to only one categorization set in SVM." 9.5, 9.6, 9.7, 10.0 10.1

2018-10-23 REL-254702 Searching Running a Saved Search on a dtSearch index that was re-built within 10 minutes of the original dtSearch index will result in an error being thrown for your Saved Search. A workaround for this scenario is to wait 10 minutes for the cache to clear and your Saved Search will return the correct results. 9.6, 9.7 10.0

2018-10-23 REL-266194 Infrastructure When Processing Excel files, some negative numbers, fractions, scientific numbers, currency, date times, and phone numbers can be incorrect if formatted in certain ways. 9.5 Not Planned

2018-10-22 REL-255988 RDO Framework Object Types with File Fields cannot be deleted. 9.6 9.7

2018-10-15 REL-262375 Infrastructure The Change Priority prompt on the Processing Administration and the Worker Manager Queue pages contains inaccurate verbiage. 9.5, 9.6 10.0

2018-10-11 REL-262545 Relativity Desktop Client Exporting a production with the RDC in version 9.6.202.10 results in blank values for the Production::ProductionSet field in the load file. As a workaround, you can populate the set name in a different field and then export that field in the production dat. 9.6 9.7

2018-10-03 REL-255420 List Page Navigation out of Documents tab while saved search is loading causes subsequent Documents tab loads to fail. You must re-login to get Documents tab working. 9.6 9.7

2018-07-26 REL-243169 Production Sets Unicode is not supported in the Custom Production Placeholder. 9.5, 9.6 9.7

2018-07-17 REL-240224 Mass Operations Export to File will fail on Processing Errors when the ArtifactID is in the view. 9.5, 9.6, 10.0 10.1

2018-01-15 REL-193127 Integration Points RIP job status is not updating for cases when first job fails with the status "Error - job failed" and user retries errors with the option "Retry Errors". Despite job continues and finishes successfully. 9.5, 9.6 9.7

2018-01-16 REL-193400 Mass Operations A user must have the Edit Mass Operation Permission to use Save as PDF from the Related Items Pane 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2018-11-16 REL-182349 Relativity Desktop Client The RDC doesn't recognize the "DefaultDocumentLimit" instance setting, which means it can import documents above the set limit. 9.5, 9.6 9.7

2017-11-14 REL-181586 Mass Operations Save as PDF removes non-alphanumeric characters from the resulting PDF file name. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2017-07-28 REL-156298 Mass Operations Navigating away from the list page after Save as PDF request has started may cause the status indicator to fail. 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3 Server 2021

2018-09-27 REL-259121 Active Learning When all documents in Elusion Test have been reviewed, the button is labeled "Complete Review" where it should say "View Results". Clicking the Complete Review button will bring up Elusion Test modal. 9.7 9.7

2018-09-25 REL-195849 Imaging If a user sets the maximum pages imaged per file value to 5 (for example), and image a 10-page document, the document will error out with a message. 9.5, 9.6 9.7

2018-09-25 REL-254667 Active Learning If the Active Learning project is in a completed state (i.e., it has an accepted elusion test) and you are on the Review Statistics tab, clicking the link to re-open the project won't open the accept/complete modal. You need to click the link from Project 9.7 10.0

2018-09-25 REL-258117 List Page Top 10 choices are displayed in the item list multi-choice column. Remaining choices (if any) are replaced with ellipsis. Filtering is not affected by this issue. 9.5, 9.6 9.7

2018-09-17 REL-250870 Installation A workspace upgrade will fail if an apostrophe is in the Production name. The workaround for this issue is to rename the Production and the Save Search view criteria that has the apostrophe in the name. 9.6, 9.7 10.0

2018-09-12 REL-254344 List Page Item list remains at the same scroll level instead of scrolling to the top after page navigation actions. 9.5, 9.6 9.7

2018-09-07 REL-254011 Admin Operations Environment Level user login and workspace script does not output users who access workspaces which are ARM'd into the environment. 9.5 Not Planned

2018-09-07 REL-253576 Active Learning In Active Learning, if the Elusion Test is paused and started again, the 'Start Date' column will display a new Start Date. The Start Date will be the date and time when Elusion Test was restarted instead of the original Start Date. 9.7 10.0

2018-09-07 REL-195921 List Page Navigation within document browsers (folders, saved searches, fields, clusters trees) is not stored in recent links list and it cannot be favorited. Direct links to specific tree nodes are not supported. 9.5, 9.6, 9.7 10.0

2018-09-06 REL-252956 Assisted Review (RAR) "Assisted Review upgraded" Assisted Review Audits are not created on Sample Based Assisted Review projects when workspaces with Assisted Review installed are upgraded. When these workspaces are upgraded an error is created in the errors tab per workspace. 9.5, 9.6, 9.7 10.0

2018-08-28 REL-250005 Active Learning When upgrading an Active Learning project from Relativity 9.5 to the Relativity 9.6.205.1 June update the upgrade will fail with: "The given key was not present in the dictionary". Please visit the Relativity Community site for workaround steps to resolve. 9.6 9.7

2018-08-28 REL-248353 Active Learning When upgrading an Active Learning Project with a paused Prioritized Review Queue from Relativity 9.5 to 9.6 the project will display all documents as manually coded until the Prioritized Review is started again. 9.6, 9.7 10.0

2018-04-20 REL-218439 List Page The clear folder selection possibility is missing in the Saved Search Select Folder modal in the new UI. 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2018-06-21 REL-117234 Production Sets Long free text headers or footers may overlap. 9.4, 9.5, 9.6, 9.7 10.0

2018-08-10 REL-245399 Persistent Highlight Sets Complex Searches with DT & Regular Expressions return document hits, but the terms are not showing & highlighting on document. 10.0 10.1

2018-08-20 REL-244129 Reviewer Interface The Conversion Complete Agent is disabled after tenant provisioning because Conversion Service topics don't exist until the Configure Conversion job is run. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 10.0

2016-03-16 REL-34685 Processing The extracted text from Microsoft Project files is formatted differently depending on whether Microsoft Office 2010 or Microsoft Office 2013 is installed on the worker. 9.3 Not Planned

2018-06-21 REL-25992 Viewer - HTML Oracle viewer adding black boxes on document. 9.0 Not Planned

2018-08-10 REL-245224 List Page Dashboard and widgets cannot be exported when dashboard contains widgets based on Pivot Profile. 9.6 9.7

2018-08-08 REL-208845 Imaging You will not be able to edit the Native Default Imaging Profile 9.5, 9.6 9.7

2018-08-08 REL-245202 Searching Saved search displays documents and families after refresh if +Family is set in the Documents browser, even when saved search was not created to pull back families. 9.6 9.6

2018-08-08 REL-233977 Batching The batch data source dropdown in the Batch Set form can display up to 10,000 saved searches. 9.6, 9.7, 10.0 10.1

2018-08-06 REL-239660 List Page Long words do not break into multiple lines in the Item List cells. You need to widen column to get full content visible. 9.6 9.7

2018-08-02 REL-239180 Persistent Highlight Sets When having multiple Persistent Highlights Sets with the same term and clicking the check/uncheck on that term, it makes the term in the viewer unhighlight even when the other Set has the term still checked. 9.7 Not Planned

2018-07-18 REL-230100 Search Ad-hoc searches may return different results than Saved Searches on relative date fields (e.g. Last 7 Days) when you are not in the same timezone as your Relativity instance. 9.6 9.7

2018-07-17 REL-239971 Mass Operations Save as PDF documents are left in the cache unless the email download link is clicked. 9.6 Not Planned

2018-07-17 REL-226087 Mass Operations A user cannot perform a mass operation "export to file" when the Client column is part of the Users view. 9.6 9.7

2018-07-10 REL-236404 Active Learning Any mass process that exceeds 10 minutes will trigger an error message on the UI only, back-end process continues unaffected. 9.7 Not Planned

2018-06-28 REL-235825 Active Learning The data on the Manually-Selected statistics list page in an Active Learning Project is not ordered by Date Submitted. 9.5, 9.6 9.7

2018-06-25 REL-207970 Search Term Reports When selecting 'Include Relational Group' to build a Search Term Report, relational groups with more than 20 characters can cause the Search Term Report display to overlap over the count of results. 9.6 9.7

2018-06-25 REL-227581 Audit Sampling is not supported functionality with the Audit application. While the icon is available, applying sampling does not return any results. 9.5, 9.6 9.7

2018-06-21 REL-116966 Audit The Audit Details page doesn't specify the conversion type when the action name is Conversion Complete. 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023

2018-06-18 REL-232855 Integration Points 9.6 9.7

2018-06-14 REL-164689 Processing Sets When processing emails with image attachments using the "When extracting children, do not extract: Email inline images" option selected, Relativity was incorrectly reading the email properties to determine if an image was inline or attached. This can affect the number of children processed and published into Relativity. 9.4, 9.5, 9.6 9.7

2018-06-01 REL-163305 Field Mapping When processing Word, Excel, or PowerPoint documents saved in post-2007 format (e.g., .docx, .xlsx, etc.), extended/application-specific metadata is not extracted. This type of metadata includes fields such as "HiddenSlides," "Company," and "Notes," as well as others. 9.3, 9.4, 9.5, 9.6 9.7

2018-05-31 REL-227138 Conceptual Analytics When performing keyword expansion from the document viewer, selecting too much text will result in an error. 9.5 Not Planned

2018-05-30 REL-34896 Processing Sets When processing Lotus/IBM Notes messages, the UNID metadata was improperly populated. 9.3, 9.4, 9.5, 9.6 9.7

2018-05-30 REL-225711 Processing Sets When dtSearch is selected as the text extraction method for DRM-protected Word, Excel, or PowerPoint files, extracted text will contain an error message rather than the actual extracted text. This applies only to files saved in pre-2007 format (e.g., .doc, .xls, etc.). 9.4, 9.5, 9.6, 9.7, 10.0, 10.1 10.2

2018-05-24 REL-200462 Security When using Preview Security, if you exit preview mode while in the Document Viewer Relativity will throw an error. You must return to the Document List before you exit in order to exit without an error being thrown. 9.5, 9.6 9.7

2018-05-22 REL-225998 Reviewer Interface Applying Item Level Security at the folder level then the document inside that folder will disable the ability to utilize the "Replace Document Native" and "Upload Images" feature. 9.6, 9.7 10.0

2018-05-17 REL-220433 Resource Pools Copying a Resource Pool multiples times does not consistently create the resource pool-specific topics in Service Bus Explorer. This causes documents in the copied resource pool to not complete conversion, resulting in a spinner when trying to view the document. 9.6, 9.7 10.0

2018-05-16 REL-222050 Extensibility Points When a customer is running Relativity with Windows Server 2016 and IIS10, some browsers (Firefox and Safari as of now) will try to use HTTP2. This causes errors with switching workspaces and filtering. The workaround is to disable HTTP2 on the Windows 2016 Servers 9.5 9.6

2018-05-15 REL-223553 Production Sets The saved search created when a production set is run is not deleted when the production set is deleted. 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2018-05-10 REL-209241 Production Sets When a Production Delete job fails there is no way to retry the job. The job remains in the production set queue in an error status. 9.6, 9.7, 10.0, 10.1 10.2

2018-05-07 REL-206591 Reviewer Interface Messages that get stuck in the Conversion Complete agent can cause a delay in viewing files that have not been converted yet. 9.6 9.7

2018-05-02 REL-221230 Conceptual Analytics It could be the case that when retrying failed Active Learning jobs, extraneous SVM Categorization Set can be submitted to the cat. set job queue (EDDS.EDDSDBO.[AnalyticsCategorizationSetQueue] RunType = 0). This can cause other cat. sets to become starved for agents. The fix is to clear out all but one extraneous sync jobs for the cat. set in question. 9.5, 9.6 9.7

2018-05-02 REL-221161 Active Learning When an Active Learning Update Ranks job fails mid batch, it could be the case that Retry will fail with a foreign key exception. The resolution for this is to clear the failed job from the queue (EDDS.EDDSDBO.AnalyticsCategorizationSetQueue RunType=3) and submit a new update ranks job through the Active Learning front end. 9.5, 9.6 9.7

2018-05-01 REL-219231 Active Learning The remaining documents count on a elusion test review will display the incorrect number of documents remaining if reviewers are currently reviewing documents. It counts documents in the 'Reviewing' status incorrectly . However the green button to view elusion test results will still perform correctly and only be shown when there are truly are no documents remaining for review. 9.6 9.7

2018-04-24 REL-219255 Extensibility Points Background processes for active learning projects may be delayed due to long running API calls. This can impact impact, refreshing review queue, tagging docs, and syncing reviewers. Restarting services will fix delays. 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023 Not Planned

2018-04-18 REL-217602 Integration Points During RIP job processing state "items transferred" count displayed on the job status page may fluctuate and show a number that do not match actual records transferred. Same when the job finishes with statuses other than "Complete" i.e. "Stopped", "Error - job failed" RIP may present the wrong calculation of the "items transferred". 9.6, 9.7 10.0

2018-04-17 REL-212635 Integration Points RIP is failing when Resource Pool is changed for the workspace. RIP has no proper folder structure under that new location to import/export documents (it is created with RIP installation only). Workaround: Go to that new fileshare location and create necessary folder structure \Data Transfer\Export and \Data Transfer\Import. 9.6 9.7

2018-04-17 REL-215676 Active Learning When viewing the elusion test results for an Active Learning project, if the document ranks were recently updated, the user will not have the option to update ranks when clicking the Complete Project button, even if the responsive cutoff of the elusion test differs from the existing ranks. Workaround: Manually update the document ranks after completing the project. 9.6 9.7

2018-04-12 REL-112126 Processing Sets Relativity Processing may run into memory issues during Inventory and Discovery due to EnCase files that contain a significant number of files. As a workaround, the files will have to be extracted and processed individually. 9.4, 9.5, 9.6, 9.7, 10.0 10.1

2018-04-12 REL-213799 Integration Points In RIP exporting to a Load File with renaming of the column names in the Load File does not have an effect. To correct that issue there is a need to enable a following code toggle: kCura.IntegrationPoints.Core.Toggles. UseOldExportVolumeManagerToggle That change has no effect on other functionalities. Please contact support for details. 9.6 9.7

2018-04-11 REL-181133 Relativity Desktop Client RDC has issue with importing to the Custom Object with Append option. The workaround is to use the Append/Overlay option instead. 9.5, 9.6 9.7

2018-04-09 REL-211930 Persistent Highlight Sets The viewer does not support highlighting of number formatted cells in spreadsheets. 9.6, 9.7 10.0

2018-03-26 REL-207577 RelativityOne Staging Explorer (ROSE) Using custom folder installation for RDC will break ROSE functionality. 9.6, 9.7, Server 2021 10.0

2018-03-16 REL-206325 Active Learning If a manually selected document is coded, subsequently the coding decision is removed from the document, the Document Rank Distribution counts the manually selected document as ‘Skipped’. This is a defect, these documents should be ‘Not Reviewed’ documents. 9.5, 9.6 9.7

2018-02-13 REL-200589 Active Learning Active Learning Projects statistics do not update when coded documents are removed from the search used by the project's Analytics Index. 9.5, 9.6, 9.7 10.0

2018-02-13 REL-200587 Active Learning Documents that have been coded by reviewers and then deleted from Active Learning projects are marked as skipped documents in the Project Statistics. 9.5, 9.6, 9.7 10.0

2018-02-07 REL-197313 Infrastructure When attempting to process Office files created in older versions of Office, a potential error can occur due to File Blocker on the processing worker of Office programs. As a workaround, you can disable File Blocker in the Office Trust Center for all Office applications. Refer this Microsoft Support Page for more information. 9.3, 9.4, 9.5, 9.6 9.7

2018-01-31 REL-191108 Audit When uninstalling the Audit application from a workspace, an exception is thrown due to a dependency on the Audit object type. This exception causes the uninstall to fail. 9.5, 9.6, 9.7, 10.0, 10.1 10.2

2018-01-31 REL-188289 Infrastructure The DryRun validation will not work when going from a version below 9.5.292.12 to a version after 9.5.292.12. The validation will not work and certain folders and files in processing databases may be deleted.

9.5

Not Planned

2018-01-17 REL-194160 RDO Framework

After you activate the User & Group Operations feature, Relativity continues to use the legacy functionality to delete users and groups rather than the new optimized distributed job process. As a workaround, you can use the following steps to delete users or groups when you many workspaces in your Relativity instance:

To delete a group, remove the group from all the workspaces and then delete the group.

To delete a user, remove the user from all the groups it is in and then delete the user.

9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2017-12-21 REL-18179 Search Term Reports Applying a Search Term Report as a condition on a search will allow the individual terms to be used as a condition for that search. When the Available in Field Tree option is set to 'No', terms used for all Search Term Reports will be displayed. This can be problematic when selecting the conditions for workspaces with multiple Search Term Reports with many terms applied. As a workaround, update the Filter Type to 'Popup' and select the STR for the Popup Picker View option. To find this option, navigate to the Fields tab in your workspace and Edit the STR in the List Properties section. Selecting the Popup Picker filter will resolve the issue when trying to select a specific term associated with the STR. 9.3 Not Planned

2017-12-21 REL-141836 Audit When clicking on the search condition applied in the List Condition section of Relativity, Filter Card modals will not show the search condition that is already applied. To keep the same condition and add/remove new conditions, apply the same filters as before and make any changes to reflect the new search condition. 9.5, 9.6, 9.7, 10.0 10.2

2017-12-18 REL-184302 Conceptual Analytics A categorization set associated with an Active Learning project can be deleted without a dependency warning which will leave the project in an usable state. 9.5, 9.6 9.7

2017-12-18 REL-184140 Conceptual Analytics A Classification Index associated with an Active Learning project can be deleted which will leave the project in a not usable state. 9.5, 9.6 9.7

2017-12-18 REL-180798 Conceptual Analytics When filtering the Project Reviewers field on the Document object, reviewers from other Active Learning projects will appear in the filtering options. 9.5, 9.6, 9.7 10.0

2017-12-15 REL-185456 Reviewer Interface If you access any document with the show/hide document list currently showing the coded field in the view and you click Save and Next, the field showing in the document list does not reflect the coding value that was applied until you refresh the page (F5). 9.5 Not Planned

2017-11-03 REL-173557 Processing Sets When processing Binary formatted Excel and Word files (e.g. .XLS or .DOC), inline images will not be extracted as children when the Processing Profile option, Extract Children, is set to Yes. 9.3 Not Planned

2017-11-03 REL-171633 Field Mapping When processing XML formatted Office documents from Excel, PowerPoint, Word, and Visio (e.g. .XLSX, .DOCX, .PPTX, .VSDX), extended metadata is not detected. 9.3, 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2 10.3

2017-10-26 REL-175439 Audit Name field is not supported. 9.5 Not Planned

2017-10-26 REL-174686 Structured Analytics Running a Retry Errors on a Structured Analytics Set that had failed during Export, prior to an upgrade could result in a state where the job is unable to progress. This can be remedied by forcefully deleting the CAAT Ingestion connectors for correlating staging area through the CAAT Rest API. 9.5 9.6

2017-08-21 REL-157940 Reviewer Interface When you first open a document from the document list, you may run into an issue where there is an endless spinner over the viewer content. This is sporadic and will not happen every time. 9.5 9.6

2017-08-18 REL-160531 Pivot In every pivot chart type, dates in exported .xlsx files are displayed in US format, even when the UK format is selected. 9.5 Not Planned

2017-07-05 REL-149959 Hold Admin IE for fonts isn't supported. This is due to the non-standard way IE handles certain HTML tags that are used by the HTML Editor. 9.5 Not Planned

2017-06-28 REL-148608 Conceptual Analytics If a cluster set only has one cluster, it doesn't display in the beta Dial visualization. 9.5 Not Planned

2017-06-26 REL-149029 Integration Points An Integration Points job fails when exporting any Data Grid-enabled text fields, which are usually extracted text, to another workspace. If you encounter this issue, contact Client Service for a workaround. 9.5 9.6

2017-06-20 REL-112218 Relativity Desktop Client When overlaying new production images with the Relativity Desktop Client, old production images are not deleted. The new images are appended as new pages to the end of the document. 9.4 9.5

2017-05-31 REL-139271 New UI Framework In the new UI framework, a filter applied in a Pivot widget slightly differs from a Pivot filter available in the classic UI framework. The new UI framework utilizes filter panel functionality. If data in a Pivot is based on search conditions that include relational fields, the filter applied in the Pivot first filters documents that are directly responsive to filter, and then adds relational documents. In the classic UI framework, it filters out relational documents that don't meet the filter criteria. In other words, the new UI framework filters and then applies relations, while the classic UI framework applies relations and then filters documents. 9.4 Not Planned

2017-05-26 REL-116966 Audit The Audit Details page doesn't specify the conversion type when the action name is Conversion Complete. 9.4, 9.5, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3, Server 2021, Server 2022, Server 2023

2017-05-24 REL-136727 Reviewer Interface The conversion of a document with a large number of images may result in an error. 9.5 Not Planned

2017-05-23 REL-142345 Reviewer Interface In some cases, you may experience Conversion Agent connectivity issues. If you restart the kCura Agent Manager service on each server, the agents pick up jobs that are queued. 9.4 9.5

2017-06-03 REL-140220 Mass Operations An error occurs when you execute a mass Save as PDF operation with produced images, and the Save as Single PDF since the job never finishes. The Save as Individual PDFs In A Zip functions correctly. 9.5 9.6

2017-04-11 REL-134653 Relativity Desktop Client When you choose the Append Original filename option for natives and images, the RDC exports files that have the control number as their filename. 9.4, 9.5, 9.6, 9.7, 10.0 10.1

2017-03-27 REL-131076 Conceptual Analytics Due to a caching issue in the Analytics engine, replacing an existing cluster can take longer than expected to propagate to the cluster visualization widget. 9.5, 9.6 9.7

2017-03-15 REL-129104 Relativity Scripts & Utilities Due to the limitations of the Relativity script framework, we recommend running the Populate Parent ID to Child ID script on productions with a maximum of 20,000-30,000 documents. You can split up the data source of the productions if the script hasn't completed within the default timeout of 20 minutes. Additionally, setting the Force Inclusion of Related Documents drop-down to Yes can cause the script to take significantly longer to complete. 9.5 9.6

2017-03-14 REL-125808 Processing Sets When you run processing on certain PDF files with form fields, the information in the fields is intermittently excluded from the extracted text. 9.5, 9.6 9.7

2017-03-14 REL-125807 Imaging When you run native imaging on certain PDF files with form fields, the information in the form fields is intermittently excluded. 9.5, 9.6, 9.7, 10.0, 10.1 10.2

2017-02-15 REL-125114 Conceptual Analytics For CAAT 3.25.0, cluster visualization may display cached cluster results for a temporary duration. This issue occurs when visualizing a cluster that was used with the Replace Existing Cluster mode. 9.4, 9.5 9.6

2017-01-10 REL-118269 Structured Analytics Misleading information appears in the Structured Analytics Set layout tooltip in the Repeated Content section. The ability to set Minimum product was removed from the layout. 8.2 9.6

2016-12-21 REL-112040 Analytics In some cases, an Assisted Review round displays error information even after the error has been resolved. 9.4 Not Planned

2016-11-30 REL-104908 Reviewer Interface The Conversion Agent sometimes sits at 100% CPU usage indefinitely until the kCura Agent Manager service is manually restarted. 9.4, 9.5 9.6

2016-08-15 REL-28292 Searching When searching on the Folder Name field using the 'IS' condition, an error will be displayed if any text is entered. 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7 10.0

- Known issues archive (2016-2020)


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
