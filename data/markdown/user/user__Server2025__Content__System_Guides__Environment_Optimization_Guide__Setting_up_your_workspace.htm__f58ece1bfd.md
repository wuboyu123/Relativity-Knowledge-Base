---
title: "Setting up your workspace"
url: https://help.relativity.com/Server2025/Content/System_Guides/Environment_Optimization_Guide/Setting_up_your_workspace.htm
collection: user
fetched_at: 2026-06-22T06:17:56+00:00
sha256: 39a27889fa8fef90db25c585659d2c6ee162f7335100ec8e5322b7020985142f
---

Setting up your workspace Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Setting up your workspace

As a system admin, use the following best practices to optimize your Relativity environment.

## Fixed-length vs. long text field types

Use the appropriate field type and length for text fields within Relativity.

Fixed-length text - a text field with a limited character length.

- Maximum technical limitation of 4,999 characters

- Examples: Author, Email From, Email Subject

Long Text - a text field larger than 4,999 characters.

- The technical limitation on a long text field is 2 GB.

- Relativity is typically configured to stream files smaller than 50 MB. You can set the maximum file size in the Instance Setting table.

- Only the first 20,000 characters appear in Layouts and Views.

You can create indexes on particular columns to improve performance for queries against large databases. See Fields for more information.

Consider these SQL limitations when deciding between the two field types: you can't create an index on a column with a type of Long Text, a Unicode-enabled fixed-length text field of more than 450 characters, or a non-Unicode-enabled fixed-length text field of more than 900 characters.

## Fixed-length text field considerations

If there are more than 8,060 characters in a single database row, SQL may experience performance issues. As a result, a best practice is to limit the length of fixed-length text fields.

You can get the total field length usage for any workspace by viewing the document object properties in the Object Type tab for that workspace. This also applies to any dynamic objects.

When you create a fixed-length text field, configure the length of the field to the appropriate size. You can increase the length as necessary throughout the life of the workspace. If you have a field that will never exceed a certain length, set the length of the field to that value.

For example, a Document Extension field should have a small field length value. If there is a field that could eventually grow to a great length—a Unicode-enabled fixed-length text field of more than 450 characters or a non-Unicode-enabled fixed-length text field of more than 900 characters—then set it as a Long Text field initially rather than a Fixed Length Text field.

For more information on limiting the total length of text fields in SQL, see http://msdn.microsoft.com/en-us/library/ms186981.aspx .

After any major cleanup or length reduction of fixed-length text fields in a workspace, run the DBCC CleanTable SQL Script after hours on the database to reclaim free space. For the steps on running this script, see http://msdn.microsoft.com/en-us/library/ms174418.aspx .

## Unicode support

Define the Unicode Enabled property of a field prior to importing data. A database level operation to convert a field’s data from Unicode to non-Unicode (or vice versa) can take a long time, lock tables, and potentially timeout if performed on a large data set in Relativity.

Only the following field types are Unicode-compatible:

- Fixed-Length Text

- Long Text

- Single Choice

- Multiple Choice

Define the Extracted Text field as Unicode if there is a possibility that text in languages other than English will be loaded into the workspace.

## Data imports

Use the Relativity Desktop Client, Relativity Integration Points, or Relativity Processing to import data into Relativity.

There are two methods of importing native/TIFF files when using the Relativity Desktop Client or Relativity Integration Points:

- Copying files from the original location in the selected load file field to the document repository. This copies the files from the original location in the selected load file field to the selected document repository.

- Importing files that already reside in a valid, Relativity-accessible location.

Use this option when native files already have been copied to their final location and are accessible by Relativity. This location should be separate from that of the Relativity document repository. You can set the default option on an environment-wide level. For more information, see Instance setting descriptions .

For either method, the selected native file path field should point to the current location of the native files.

Many customers use the second option to reduce the total time it takes to load files into the Relativity repositories. You can manually copy files to where they should reside and then provide Relativity Desktop Client or Relativity Integration Points with pointers to their locations. This can save significant time when loading large amounts of natives and/or TIFFs.

Never run the Relativity Desktop Client on a Relativity production server (Web, Agents, SQL, or Search). Launch the tool on a different server or workstation to prevent resource contention.

## Analytics

Use the following guidelines when setting up an Analytics index in your workspace.

- When populating an Analytics index, exclude non-conceptual files such as XLS, EXE, or RAR from the index. Make sure that the training data source is limited to documents with less than 2 MB of Extracted Text.

- Disable queries on indexes that are no longer being actively used.

- When queries are enabled on an Analytics index, the index is loaded into RAM. Unused indexes shouldn't consume resources on the CAAT server.

- To setup a structured analytics set in your workspace, see Running structured data analytics .

## Views and searching

Follow these best practices for views and searching:

- Avoid Is Like and Is Not Like statements on un-indexed queries. Full table scans on large databases using Is Like statements severely load the server. A full table scan occurs when a query reads every row in a table in order to locate the required information.

If possible, use a Contains condition instead. In order to use Contains, you must add the field to the Full Text Index.

Is Set and Is Not Set criteria also triggers a full table scan. A full table scan operation can be very IO-intensive and can take a while to complete on slower storage units.

- Prevent users from filtering and/or sorting on Long Text fields within the document list in large workspaces. To do this, make sure the field's Allow Sort/Tally property is set to No .

## Tally/Sum/Average mass operation

In the Tally/Sum/Average mass operation, the Tally option is audited. For the set of requested documents, it lists each unique value found in that field along with the frequency of each occurrence. The process can run on Fixed Length Text, Choice, User, and Number fields.

Tallying on un-indexed columns in large workspaces can take a while to complete and slow down database/system performance. Be sure to place indexes on columns in SQL that are regularly tallied in large workspaces.

You can disable the ability to Tally in a workspace by setting each field's Allow Sort/Tally property to No .

## Group by for Pivot

When performing Pivot operations in large workspaces, you can improve Pivot performance by placing a non-clustered index on the field being grouped on. Use SQL Server Management Studio to place the index.

## User notifications

There are several notifications available to help system admins better manage their Relativity environments.

### Disclaimer Message

When you want users to agree to a disclaimer message when using Relativity, you can create a custom message and an agreement button for users when they first log in to the Relativity environment. This type of message is useful to ensure that users acknowledge Relativity terms of use or the confidential nature of Relativity content.

To customize a disclaimer on a Relativity login page, use the following steps:

- Navigate to the web server(s) at C:\Program Files\ Relativity Corporation\Relativity\EDDS.

- Locate the text file, Disclaimer.txt, and update it with your disclaimer text. You must use plain text only; HTML will not display here.

- Update the DisplayDisclaimer instance setting value to true to display the disclaimer message.

For information, see Instance Settings descriptions .

### Message of the Day (MotD)

The Message of the Day (MotD) is a message displayed to all users when they log in to Relativity. MotD is most commonly used to inform users of planned system maintenance.

To activate or change the message of the day, navigate to the Instance Details tab from Home.

### User status

The user status page displays a list of users currently logged into the system. To access the user status page, navigate to the User Status tab from Home.

You can also send messages to any logged in users. This is helpful if you require emergency downtime during a review. System admins can also force log out users from the system on this page.

### Default workspace tabs

When a user enters a workspace within Relativity, they are usually taken to the Documents tab. You can change this default setting in the Tabs tab of any workspace.

Set the Is Default property to Yes for the tab that you want to designate the default tab in a workspace. If a user doesn't have access to the Default tab, he or she will be directed to the Documents tab.

Modifying the default tab may be helpful in informing users of any upcoming workspace-level maintenance. Additionally, system admins can direct users to custom pages that contain links to instructional items, important information about the matter, or an overview of workspace review progress.

On this page

- Setting up your workspace

- Fixed-length vs. long text field types

- Fixed-length text field considerations

- Unicode support

- Data imports

- Analytics

- Views and searching

- Tally/Sum/Average mass operation

- Group by for Pivot

- User notifications

- Disclaimer Message

- Message of the Day (MotD)

- User status

- Default workspace tabs


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
