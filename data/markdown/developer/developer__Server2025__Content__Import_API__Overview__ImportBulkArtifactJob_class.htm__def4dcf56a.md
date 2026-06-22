---
title: "ImportBulkArtifactJob class"
url: https://platform.relativity.com/Server2025/Content/Import_API/Overview/ImportBulkArtifactJob_class.htm
collection: developer
fetched_at: 2026-06-22T06:29:59+00:00
sha256: ca60089e7cc0699cd39ca8a6a31290be10778b32ca25f15a9a3219d01d3e916c
---

ImportBulkArtifactJob class Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# ImportBulkArtifactJob class

The ImportBulkArtifactJob class provides the functionality for adding a large number of Artifact objects to a Workspace. It includes a Settings property for setting import parameters, as well as an Execute() method for loading data and retrieving messages from the OnMessage event.

## Map fields

The Import API performs field mapping during the first stage of execution for an import job that uses the ImportBulkArtifactJob class. After the Execute() method is called on the ImportBulkArtifactJob instance, the OnMessage event is raised multiple times, and passes Status objects that each have a Message property. This Message property contains information about the progress of the Import job, including these actions taken before the execution begins:

- Message – Getting source data from database

- Message – Updating settings

- Message – Executing

Field mapping occurs after the OnMessage event passes the following execution message: [Timestamp: DATE_TIME] [Record Info: X] message . The next OnMessage event passes the detailed information about the mapping process in the Message property. The content of this Message is a single string that includes the following information:

- Mapping is indicated with the Message: Source field [SRC_FIELD_NAME] --> Destination field [DEST_FIELD_NAME] . Each source to destination message contains one field per line, and it is separated from other messages by a new line.

- SRC_FIELD_NAME is identical to DEST_FIELD_NAME under normal conditions. In general, a named column in the data source matches the display name of a field in a destination workspace.

- DEST_FIELD_NAME may be replaced with the following text:

- Filename – a special indicator related to KCURAMARKERFILENAME. Before the import, files are copied to a local directory using the filename in kCuraMarkerFilename field except when links point to them, or when this field doesn’t exist. The Import API copies the files from their current location in this case. The values in the _KCURAMARKERFILENAME column are used for filenames when this column is in the table. Otherwise, the original filenames are used.

- NativeFilePath – indicates the SRC_FIELD_NAME used as the NativeFilePathColumn.

- NOT MAPPED (Target field not found) – indicates that a source field does not have a matching destination field in Relativity. During Import, Relativity ignores this field unless the SRC_FIELD_NAME is used as the FolderPathSourceFieldName.

After field mapping completes, the OnMessage events pass the messages Progress Info and Record Info .

## Map single- or multiple-object fields by ArtifactID

You can map instances of single- or multiple-object fields by name or ArtifactID. When multiple instances of an object share the same name, you can uniquely identify them by mapping them with their ArtifactIDs. For example, you can assign unique ArtifactIDs to custodians who have the same name.

To map a field, assign the ArtifactID for the field to the Settings.ObjectFieldIdListContainsArtifactId property of a ImportBulkArtifactJob instance. A document is flagged with an error when an instance of a single- or multiple-object field is linked to an ArtifactID that doesn't exist in the workspace. This document is not imported into the workspace.

On this page

- ImportBulkArtifactJob class

- Map fields

- Map single- or multiple-object fields by ArtifactID


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
