---
title: "Mass operations"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Mass_operations.htm
collection: user
fetched_at: 2026-06-22T06:06:26+00:00
sha256: 9831965398d079d1df80e655f21692c409fa7967d4b13899a0ff014d6e702edc
---

Mass operations

# Mass operations

Using mass operations, you can perform actions on a set of documents at once instead of performing the same action for each individual document. Some mass operations are available to reviewers, while other mass operations will only display in the mass operations bar if you are a system administrator. Access to each mass operation can be granted individually.

- Some mass operations like Edit, Replace, and Delete can temporarily lock down the document table while executing. In a workspace with a large number of records and users, the table may be locked for an extended period of time and prevent users from performing standard edits. In such cases, we recommend carrying out mass operations at night or an off-peak time.

- You can't use mass operations on Data Grid-enabled fields.

See the following mass operations for details:

- Cancel Production Job

- Mass edit

- Mass copy

- Mass move

- Mass delete

- Mass PDF

- Mass replace

- Mass image

- Tally/sum/average

- Send to CaseMap

- Mass export to file

- Mass convert

- Move to folder path

- Mass Save as List

- Mass cluster

- Re-produce

- Set long text field size

- Invite users

## Mass operations permissions

- Assign to Entity —gives group members the rights to select and re-assign an alias to a different entity when using name normalization in Analytics.

- Cluster —gives group members the rights to cluster documents using Analytics clustering.

- Convert —gives group members the ability to convert a large set of documents into HTML5 format for faster document load times within the viewer.

Mass convert is not available in repository workspaces.

- Copy —gives group members the rights to copy securable objects such as views, layouts and summary reports.

- Delete —group members can mass-delete documents. Mass delete also requires the rights to delete documents.

- Edit —gives group members the rights to use their layouts to simultaneously edit document field values for multiple documents.

- Export —gives group members the rights to export audit data via Audit.

This permission only appears if Audit is installed and configured.

- Export to File —gives group members the right to export the contents of a view to a .csv, .xls or .dat file.

- Image —group members can simultaneously send image requests for multiple native files.

- Move —gives group members the right to simultaneously move documents from one or more folders to one target folder. Mass Move also requires add and delete document rights.

- Merge —gives group members the rights to select and merge multiple entities into a single entity when using name normalization in Analytics.

- Print Image —gives group members the right to simultaneously print images from multiple documents.

When you mass print images, you can choose how to print the redactions on those images, normal or transparent. Even if users do not have permission to move or delete redactions, if they mass print images, they can choose to print redactions as normal or transparent.

- Produce —gives group members the right to simultaneously add multiple documents to a production set.

- Replace —group members can perform a replace operation on multiple documents. Examples include:

- Copying the contents of one text field to another.

- Adding a set string to the beginning or end of an existing field.

- Merging the values of a source field with the values of a target field.

- Process Transcript —group members can process imported transcripts for viewing in Relativity.

- Send To Case Map —group members can send multiple documents to CaseMap.

CaseMap is not compatible with Windows 8.

- Tally/Sum/Average —group members can tally, sum and average the values of any numeric fields. This action is recorded under the document history.

- Custom mass operations —may appear in this list. They include mass operations that you added to Relativity or that are available in applications currently installed in your environment.
