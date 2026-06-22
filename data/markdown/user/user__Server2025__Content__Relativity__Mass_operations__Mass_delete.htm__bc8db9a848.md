---
title: "Mass delete"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Mass_delete.htm
collection: user
fetched_at: 2026-06-22T06:15:47+00:00
sha256: 29b257f4f40492663f7a1374bb8f949ec669b928bad7cb72d28973bf7f7d8627
---

Mass delete

# Mass delete

You can use the Mass delete operation to remove a group of documents or objects from Relativity in a single operation. When you delete documents, you can also remove their images and natives from the file servers. Mass delete is available from the mass operations bar.

If you have the appropriate permissions, you may also be able to force delete documents and certain objects, which includes unlinking associative objects and deleting child objects. This option is available when you have the Delete Object Dependencies permission listed in the Admin Operations section of the security page.

- You can't undo a mass delete operation

- You can't use mass operations on Data Grid-enabled fields.

This page contains the following content:

- Performing a mass delete on documents

- Performing a mass delete on other objects

- Enabling or disabling snapshot auditing on delete

## Performing a mass delete on documents

Users need the following permissions to successfully mass delete documents:

Object Security Other Settings

Document Mass Operations Admin Operations

- View (Eye icon)

- Edit (Pencil icon)

- Delete (Trash can icon)

- Add Image

- Delete Image

- Delete

- Edit

- Image

- Delete Object Dependencies

If you delete documents that were published via Processing, those files are marked as Yes on the Processing Deletion field on the Discovered Files page. In addition, Relativity recalculates deduplication, and publishes new primary documents, if applicable. See Post-publish delete .

To perform a mass delete on documents, perform the following steps:

- From the mass operations bar on the document list, choose whether to delete Checked items or All items in the current returned set.

- Select Delete . The Delete Details pop-up displays.

- Select the files associated with the documents that you want to delete.

Force a delete even if Redactions, Highlights, Links, or Transcript Tags are present. option can be set to Yes or No if one of the last three list options are selected. It is set to Yes for the first list option automatically and can not be set to No.

- (Optional) To view a report showing affected objects, click View Dependencies . When the current object doesn't have any children or associative objects, the View Dependencies button is disabled.

- Click Delete again to permanently remove the items you selected.

Relativity deletes the documents in batches. If an error occurs in a batch, Relativity doesn't delete documents that haven't been processed, and Relativity continues by processing the next batch.

## Performing a mass delete on other objects

To perform a mass delete operation on other objects, perform the following steps:

- Navigate to the tab for the object that you want to delete.

- Select Checked items or All items in the current returned set.

- Select Delete . The Delete Details form prompts you to confirm the deletion.

Depending on your security permissions, you may see a message on the Delete Details Form indicating that Relativity deletes children and unlinks associative objects when you remove the selected objects. This option is available when you delete Dynamic Objects such as Transform Sets, Analytics Categorization Sets, Search Terms Reports, OCR Sets, Image Sets, and their associated objects.

- Click Delete to delete the object and its children, as well as unlink associative objects. This message displays when you have the security permission Delete Object Dependencies listed in the Admin Operations section of the Security page.

- (Optional) To view a report showing affected objects, click View Dependencies . When the current object doesn't have any children or associative objects, the View Dependencies button is disabled.

To improve mass delete performance when deleting large numbers of documents, disable snapshot auditing. See Enabling or disabling snapshot auditing on delete .

## Enabling or disabling snapshot auditing on delete

When performing a delete, you can optionally create a snapshot of the current field values in the deleted record. Relativity stores this data in the history for the workspace. While you can enable this property to facilitate searching workspace history, it can also significantly increase the size of the audit table for the workspace. Disabling snapshot and removing any PreDeleteHandlers on the document object will improve mass delete performance. For information on PreDeleteHandlers, see Pre Mass Delete event handlers .

To enable or disable this option, navigate to the Object Type tab, and edit the Document object type.

Enabling Snapshot Auditing On Delete increases the database size.
