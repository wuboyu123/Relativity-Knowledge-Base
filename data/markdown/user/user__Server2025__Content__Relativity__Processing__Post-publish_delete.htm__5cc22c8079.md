---
title: "Post-publish delete"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Post-publish_delete.htm
collection: user
fetched_at: 2026-06-22T06:13:35+00:00
sha256: e5c88eefe4ef9cfd746e422fdb1dbd8ab555eb6ed8349bdea1b74803a8ea7c5c
---

Post-publish delete

# Post-publish delete

Post-publish delete ensures that Processing stays updated when documents are deleted from review. This topic provides real-world examples of how you can integrate post-publish delete functionality into your processing workflow.

## Post-publish delete overview

If you discover and publish files into review and then Mass Delete them from the Documents tab, the Files tab updates to reflect this deletion, and post-publish delete occurs.

Any files associated with a deleted document are indicated with a Yes value on the Processing Deletion field. All deleted documents can be seen in the Files tab . Note that post-publish delete occurs only if you select the Document and all associated files on the delete confirmation modal.

In addition, Processing updates deduplication. Specifically, once the modal closes and the mass delete operation is complete in review, Processing recalculates deduplication. At this point, the deleted files are removed, and any newly-designated primary documents are automatically published into review.

If a document has duplicates within a single custodian, the document will need to be deleted per occurrence. Duplicate documents are not automatically deleted within a single custodian.

Deleting a file also precludes it from being factored into any future deduplication calculations, including any newly processed data. This occurs regardless of whether the deleted document was a master or unique.

For information on reporting what was deleted, see Master Document Replacement Summary .

## Publishing a new master document

In this example, a user has deleted a primary custodian's document, and Processing automatically publishes the next deduped custodian's document.

To recreate this example, perform the following steps:

- In the Documents list select a primary custodian's document.

- Select the Delete mass operation.

- Click Delete on the warning message. Once you do this, Relativity deletes the selected document from review, and Processing flags it for deletion. When this deletion is complete, the deduplication recalculation will begin.

- Navigate to the Files tab and select the Deleted Documents view.

- To confirm that deduplication has been recalculated and a new master identified, locate the document you deleted and note that the following values are displayed:

- Custodian - the deduped custodian listed for the document before you deleted it.

- Processing Deletion? - Yes

Processing determines the next document in line to be published based on the order in which data sources were originally published in the workspace. If there are multiple copies of the same record in a single data source, Processing will choose the one with the lowest File ID, which means it was discovered first.

## Deleting documents within a family

It's recommended when deleting documents in a family that you delete the entire family at once; however, with post-publish delete you have the ability to delete documents regardless of family status.

In this example, a user accidentally selects only the parent document to delete, which means Processing also flags all of its children for deletion in the Files tab. The user then needs to identify the child documents that were deleted.

To recreate this example, perform the following steps:

- Locate a family group of documents in the Document list and select only the parent.

- Select the Delete mass operation.

- Click Delete on the confirmation message. Since this parent document originated from Processing, it and all of its children will be marked as Yes for the Processing Deletion? field in the Deleted Documents view on the Files tab. The parent will be marked as No for the Is Published? field, and the children will be marked as Yes. In addition, the children will remain visible in the Documents list.

- Navigate to the Files tab and select the Deleted Documents view. Confirm that the parent document and its children are present with the expected values for the Processing Deletion? and Is Published? fields.

## Retrying delete errors

Navigate to the Deleted Documents view to see a record of all deleted documents. The Processing Deletion? field is the yes/no indicator for deleted documents. You can filter by Error Message to see the errors that occurred during deletion. These errors can be retried using the Retry Errors mass operations option. Once deleted, these documents will be excluded from further processing operations (e.g., deduplication, retry, and republish) and the next duplicate will be published as the new master document, if available.

To see a summary of master documents that have been replaced, see the Master Document Replacement Summary report in Processing Reports . See Mass Delete for more information on deleting documents.
