---
title: "dtSearch"
url: https://help.relativity.com/Server2025/Content/Relativity/dtSearch/dtSearch.htm
collection: user
fetched_at: 2026-06-22T06:02:22+00:00
sha256: 12c08d0578dbd31289f99632534a80c044d54702471bce313f6af3cdc8687baf
---

dtSearch Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# dtSearch

Relativity's dtSearch engine provides advanced search functionality such as proximity, stemming, and fuzzy searches across any field type. It also supports the use of Boolean operators and custom noise word lists and the basic searching features available in keyword searches. After building your dtSearch index, the Dictionary search option becomes available.

Relativity partitions a single index into multiple smaller indexes (called sub-indexes), which multiple workers build simultaneously. This increases performance by spreading out the work over a configurable number of agents. When you perform a search, Relativity runs your query on the smaller indexes in parallel. The application then federates and returns your results. For more details, see the Ask The Expert Training content: Searching: Best Practices for dtSearch Builds .

See these related pages:

- Running a dtSearch

- Running a Dictionary search

- Using dtSearch syntax options

- Search Grid for dtSearch

- dtSearch grid best practices

- Moving dtSearch indexes

- Using regular expressions with dtSearch

Also see these related recipes:

- Regular expression searching - SSN and EIN

- Searching for a document set using control numbers

- Searching for terms while excluding email footers

## Creating a dtSearch index

You can build custom dtSearch indexes for a subset of documents or for certain document fields in a workspace. You must have the appropriate permissions to complete this task. See Workspace security .

Before you begin, you need to create a saved search that includes the fields that you want to include in the index. You can then name the index based on the document search set used to create it.

Within a field, dtSearch truncates any string longer than 32 characters that does not contain a space character. It indexes only the first 32 characters of the string. For more information, see Searching for words longer than 32 characters .

To create a new dtSearch index:

- Use the search feature to navigate to the Search Indexes tab.

- Click New Search Index .

The dtSearch Index Information form appears with required fields having an orange asterisks.

- Complete the fields on the dtSearch index form. See more details, see Fields .

- Click Save to display the index details page. The index details page now displays three additional read-only fields and the dtSearch index console. See Fields and dtSearch console .

- Click Build Index: Full . A dialog box asks you to verify that you want to run a full build. You can also select Activate this index upon completion . Indexes must be active to search them.

-

Click OK to build your index.

Network problems can slow down your dtSearch builds. If a dtSearch manager or worker agent encounters a network-related error during the build process, it executes up to three retry attempts at 30-second intervals.

- If you did not select Activate this index upon completion in the dialog box, click Activate Index on the console. The index will not activate if there are errors. Activating an index makes it available in the Search menu.

- (Optional) Click Refresh Page at any point in the build to see the index's current build status. If errors occur during the build, the Retry Errors button enables on the console under the Errors and Status heading. Click this button to try to resolve any errors.

Once the index builds, the console enables additional options. See dtSearch console .

## Accent-insensitive indexes

By default, Relativity builds an accent-insensitive index. In an accent-sensitive index, some characters translate to the base character, which causes those characters and any terms containing those characters to be treated the same in a Search Terms Report.

dtSearch uses .ABC files, but only for characters in the range from 33 to 127. Relativity handles all other characters according to the definitions in the Unicode character tables.

Example: Relativity converts accented characters like á or ñ to the unaccented versions, a or n.

Example: If you search for the term fröhlich, searching that term as fröhlich or frohlich would both return the hit. However, highlighting in the Viewer may not display both variations.

## Case-insensitive indexes

Relativity does not support case-sensitive dtSearch indexes for Unicode text. While dtSearch provides an option to modify the letters section of the alphabet file for case-sensitive indexing, this functionality only applies to the standard ASCII range, not Unicode text. See Build a Case Sensitive dtSearch Index in Community and dtSearch alphabet file for more information.

Due to how text is processed in dtSearch, case sensitivity will only work for characters in the standard ASCII range (decimal values 0–127). This includes unaccented English letters, digits, and common punctuation. The behavior is controlled by modifying the alphabet file, which applies only to characters in this ASCII range. Unicode characters, including extended or “double-wide” variants of standard ASCII characters, are not supported for case-sensitive indexing.

To avoid issues with extended encoding of standard characters, Relativity strongly recommends using fields with Unicode turned off when attempting to configure case sensitivity via the alphabet file. This ensures all characters are stored as ASCII and prevents unpredictable behavior. Attempting to search on an index with Unicode-enabled text and a modified alphabet file could result in false positives or negatives and should be used at your own risk.

## Fields

The dtSearch index page includes the following fields:

dtSearch Index Information

- Name —the dtSearch index name. This name appears within the search with menu in the Documents tab.

- Order —the integer value, positive or negative, representing the position of the index in the search indexes list. Indexes sort from lowest, top, to highest, bottom, order number. Those with the same order number sort alphanumerically.

- Searchable set —the saved search of documents for indexing. Relativity indexes the documents returned by the search as well as the returned documents' fields. It may use a dtSearch or an Analytics index. Make sure the index is active.

When creating a saved search for a dtSearch index, the best practice is to use long text fields. You will see a warning message, when creating a dtSearch index, if you select a saved search that does not contain at least one long text field.

- Email notification recipients —enter the email addresses of those who should receive notifications of whether the dtSearch index build succeeded or failed.

Advanced Settings

- Auto recognize date, email, and credit card numbers —a yes/no field. See Auto-recognition for details.

- Create accent sensitive —a yes/no field. When set to Yes, dtSearch indexes are sensitive to accents and other language-specific characters.

- Sub-index size —determines the maximum size of each sub-index created when you generate a dtSearch index. The minimum value is 1000.

- Skip malicious files —a yes/no field. Select Yes to skip potentially malicious quarantined files and continue processing the index. The final index breakdown includes the number of skipped documents.

- Index share —populated by default by a system administrator.

Noise Words

- Edit the list of words that Relativity ignores during indexing.

Alphabet

- Edit the index’s alphabet file. See Making a character searchable .

If you search for long, uninterrupted strings that have no spaces or word breaks, such as when you have made a character searchable, dtSearch truncates the string after 32 characters and inserts a wildcard. For more information, see Searching for words longer than 32 characters .

## dtSearch console

The dtSearch index console includes the following options:

- Build Index: Full —creates a full build of the index. During the build, the button toggles to Cancel Build . If you add an additional field to your index or change the auto-recognize or accent sensitive settings, you must perform a full build.

Canceling the build stops the indexing thread, leaving the index in an unstable state. Relativity deletes these indexes from the population table and gives them an inactive status. You cannot search on an index with an inactive status until you run a full build. Canceling also deletes the index files in the index share.

- Build Index: Incremental —updates an index after adding or removing documents. During an incremental build the existing index remains available for searching, but changes to the index are not reflected in search results until the incremental build completes. Canceling an incremental build returns the index to its previous state.

The incremental build process copies each sub-index that requires modification, updates the copy, then replaces existing sub-indexes with the updated copies. When run, the Workspace Delete/Housekeeping agent removes duplicate sub-indexes. The system automatically compresses a sub-index during an incremental build only if the sub-index fragmentation level is equal to or greater than the sub-index fragmentation threshold value.

- Compress Index —compresses the dtSearch index returning all sub-indexes with a fragmentation level greater than zero to a fragmentation level of zero. You can search on the original, uncompressed, dtSearch index while compression is in progress. Once compression completes, the system automatically replaces the old sub-indexes with the defragmented sub-indexes. When run, the Workspace Delete/Housekeeping agent removes duplicate sub-indexes.

The Compress Index button only runs compression on sub-indexes that have a fragmentation level greater than zero. Canceling compression returns the index to its original fragmented state before compression began.

- Deactivate Index —deactivates the index and removes it from the search with menu in the Documents tab, but not from the database.

- Swap Index —swaps your index with a replacement index in order to use its resources while your index builds or is inactive or disabled for any reason. This enables you to keep searching while your primary index experiences downtime. You can only select indexes in the Replacement Index with an Active status. This index you swap to does not automatically run an incremental update.

Selecting the index from the drop-down list and clicking OK completes the index swap. You cannot reverse the swap results in the current dialog box. You must close this swap and run it again to swap back or swap another time. This functionality is useful in limited cases, for example, if you are performing a full rebuild on a very large index. Since dtSearch incremental builds are online, you can search documents once indexed.

The Swap Index function updates anything in the Views table, which affects batches, saved searches, nested searches, and more.

- Retry Errors —enables only if errors occur, you can use this button to resolve errors.

- Show Document Errors —enables only if document errors occur. This button creates an exportable list of document-level errors.

- Show Detailed Status —shows you statistical data for the index, including:

- Doc Count —the total number of documents in the index.

- Index Size —the size of the index in bytes.

- Created Date —the date you created the index.

- Updated Date —the date you updated the index.

- Last Build Duration —how long the last build took to complete in hours, minutes, and seconds.

- Refresh Page —shows the index's current build status.

## dtSearch index page

After you create and build a dtSearch index, the dtSearch page has several sections where you can view details about your index.

### Index Status

You can view the state of your dtSearch index from the Index Status section. The name of the Index Status section populates with the name of your dtSearch index. When you are building an index, this section changes to a progress bar where you can track your index's progress in real-time. When the index is no longer in progress, this section changes to a static field that displays the below fields.

- Status —the status of the index. For example, Active - Indexed or Inactive - Indexed.

- Document Breakdown —the number of indexed documents.

### dtSearch Index Information

The dtSearch Index Information section provides general details about the settings applied to your dtSearch index. This section has the following information:

- Name —the name of your index.

- Order —the integer value, positive or negative, representing the position of the index in the search indexes list. Indexes sort from lowest, top, to highest, bottom, order number. Those with the same order number sort alphanumerically.

- Searchable set —the set of documents to be indexed. You can choose from any saved search in the workspace.

- Index share —populated by default by a system administrator.

- Auto-recognize date, email, and credit card numbers —a yes/no field.

- Email notification recipients —the emails that receive an email notification when your index population fails or completes.

### Advanced Settings

The Advanced Settings section provides sub-index details about your dtSearch index. This section has the following information:

- Sub-index size —determines the size of each sub-index created when you generate a dtSearch index. The minimum value is 1000.

- Sub-index fragmentation threshold —the fragmentation level at which the system automatically compresses a dtSearch sub-index during an incremental build.

- Sub-indexes scheduled for compression —the number of sub-indexes at or greater than the sub-index fragmentation threshold. If one or more sub-indexes is equal to or greater than the sub-index fragmentation level, the system automatically compresses those sub-indexes during the next incremental build.

- Rebuild Selected Sub-Indexes —manually rebuilds selected sub-indexes. Do not use this option unless directed by the Support team.

### Temporary Index Details

The Temporary Index Details section only appears during an incremental build. This table displays sub-indexes that copy from your original index and are in the process of modification during the incremental build. Once the sub-indexes in this table update, they replace the original sub-indexes from which they were copied. This section has the following information:

- Population Table —the name of the table that a sub-index is populating.

- Build Status —the state that the sub-index is currently in.

- Worker Agent —the name of the agent that is handling the sub-index.

- Worker Agent Status —the current state of the worker agent.

- Index File Share —the location where you store your sub-index.

- Document count —the number of documents assigned to the sub-index.

- Error(s) —any errors encountered by the sub-index.

- Fragmentation Level —the fragmentation level of the sub-index. Any index equal to or greater than the sub-index fragmentation threshold appears in red.

### Current Index Details

The Current Index Details section displays the sub-indexes that make up your dtSearch index. This section has the following information:

- Population Table —the name of the table that a sub-index is populating.

- Build Status —the current state of the sub-index.

- Worker Agent —the name of the agent that is handling the sub-index.

- Worker Agent Status —the current state of the worker agent.

- Index File Share —the location where you store your sub-index.

- Document count —the number of documents assigned to the sub-index.

- Error(s) —any errors encountered by the sub-index.

- Fragmentation Level —the fragmentation level of the sub-index. Any index equal to or greater than the sub-index fragmentation threshold appears in red.

### View Audit

Using the View Audit button, you can see when a user modified dtSearch index settings. The View Audit layout has the following fields:

- Action

- Field

- Old Value

- New Value

- User Name

- Timestamp

- Details

## Temporary storage

If you specify a temporary storage location, dtSearch builds the index in this directory and then copies the index over to the final index share when the build completes. Using a temporary storage location could speed up the build time and reduce network contention . See Servers .

On this page

- dtSearch

- Creating a dtSearch index

- Accent-insensitive indexes

- Case-insensitive indexes

- Fields

- dtSearch console

- dtSearch index page

- Index Status

- dtSearch Index Information

- Advanced Settings

- Temporary Index Details

- Current Index Details

- View Audit

- Temporary storage


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
