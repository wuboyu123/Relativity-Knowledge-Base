---
title: "Batches"
url: https://help.relativity.com/Server2025/Content/Relativity/Batches/Batches.htm
collection: user
fetched_at: 2026-06-22T06:06:23+00:00
sha256: 74e673249f63beca23e4dd30d84c3a43834fc214d2cf998ed8c4948d44dc5f35
---

Batches Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Batches

You can create batches in Relativity by splitting a static set of documents into multiple document sets based on criteria set by a system admin. With the appropriate permissions, users can then check out these batches and assign themselves documents.

A member of the workspace’s admin group will only be able to check out or be assigned batches if that user is also part of another group (non system- admin) in the workspace that has the View Batches permission. Being a workspace admin alone is not sufficient to receive batch assignments.

Batching can bring structure to managing a large-scale document review with multiple reviewers. You can generate batches automatically or manually. Automatic document assignment reduces the chances of accidental redundancy in the review process.

Also see the following pages:

- Building views for checked-out documents

- Assigning batches and checking batches in and out

## Batch fields in Relativity

The fields in Relativity that store batch-related values are:

- Batch Set - the batch set to which the batch belongs.

- Batch - the name of the batch.

- Batch Status - the status of the batch. A batch may be:

- Blank

- In progress, meaning the batch is checked out

- Completed, meaning the batch is checked in as completed

- Batch Unit - the optional grouping condition on the batch.

- Assigned To - the reviewer to whom the batch is checked out.

- Reviewed - specifies whether the batch is reviewed.

- Batch Size - the number of records in the batch.

## Creating and editing batch sets

Documents are pre-converted for viewing upon the checkout of a batch set based on the NumberOfDocumentsToAutoPreconvert instance setting. This setting is set to 1000 by default and can be adjusted to suit your needs. Please note that if the value is set to 0, pre-conversion will be disabled.

To create or edit a batch set, perform the following steps:

- Click the Batch Sets sub-tab from the Case Admin tab.

- Click New Batch Set to create a new batch set, or click Edit next to the batch you want to edit.

If you select a value in the Family Field , then the batch set will include family documents from that related group that are also included in the data source.

The Batch Set Information form appears with required fields in orange.

Complete the fields to create or edit the batch set. See Fields .

- Click Save .

### Batch Sets for Reviewers

Once you've created the batches, navigate to the Batch Sets tab using the quick search (CTRL + /) function. Here you'll see a reviewer's view of the newly created batches.

### Fields

The following fields display on the New Batch Set information form:

- Name - the name of the batch set.

If you're performing a multi-stage review with multiple batch sets per phase, be sure to include the phase name in the batch set name. We also do not recommend using the space bar before or after the name. This makes it easier to search for information within a specific phase.

- Maximum Batch Size - the maximum number of documents in one batch.

Your batch may contain fewer documents than this value if there are no more documents to batch or no more documents with the current Batch Unit value.

- Batch Prefix - sets the prefix for the batch numbering.

- Batch Data Source - the saved search containing documents that you want to batch. If the saved search references a dtSearch or an Analytics index, that index must be active. The sort order of the data source carries over to the batch.

- Batch Unit Field - an optional grouping mechanism, enabling you to group similar documents in the same batch. Documents with different values in a batch unit field are not included in the same batch unless the Family Field would override this.

-

A common batch unit field is custodian. However, you can use any single choice, multi-choice, single object or non-relational and non-system fixed length text field.

If you select a Batch Unit Field option and a Family Field option, batches will assign documents up to the Maximum Batch Size for the Batch Unit Field using only parent documents. Once the parent documents have been included, the family documents are then added to the batch. For example, if you have a Max Batch Size of 100 , and choose Record Type for the Batch Unit field, up to 100 documents with unique family identifiers are added to the batch first, and then the respective family documents are added afterward. This can cause larger batches than using the Family Field alone.

When using multiple choice fields for the Batch Unit Field, the choice values must be the same in order for them to be grouped in a batch. If the combination of choices is unique enough for the choice values, the documents are batched in separate batch groups.

- Family Field - you can select your workspace group identifier. Documents in a family group are not split across batches, even if their batch unit field differs. If you select a Family Field option and do not select sort order option for Batch Data Source, the documents are sorted by their Artifact ID. Otherwise, the documents are sorted based on the sort order option that you select for Batch Data Source.

When a value for Family Field is selected, the resulting number of documents within each batch may be larger than the value for the Maximum Batch Size field. For example, if your maximum batch size is set to 100, the first 100 documents that the batch source returns puts into the first batch. After this is done, any family members to the documents in the first batch are then included in that batch. This may result in the batch being larger than 100. Depending on the size of your family groupings, the size of your batches may vary significantly.

- Reviewed Field - an optional field that you can select from any yes/no, single-choice, or multi-choice field from the drop-down menu. Based on your selection, a tally is kept of how many documents in the batch have been reviewed. The batch set monitors the field you specify as the Reviewed Field. It also increments a count for each document in the batch that has been coded with a value for that field.

- Auto Batch - enables the system to automatically generate batches.

- Disabled - the default, which enables standard manual batch processing.

- Enabled - automatically generates batches according to the settings below.

- Minimum Batch Size - only available if Auto Batch is enabled. This is the smallest possible number of documents in a batch.

- Auto Create Rate - only available if Auto Batch is enabled. This represents how often (in minutes) the system attempts to create batches.

Newly created batches appear on the Review Batches tab. Any users with access to the Review Batches tab will be able to see any batches that they have permissions for.

With auto batching enabled, the Relativity service account runs the saved search specified as your batch data source. The Relativity Service account is a system admin account.

### Batch Set console

Once you save your batch set, the Batch Set console displays the following options:

- Create Batches - creates the batches based on the entered settings. Created batches display on the bottom half of the batch set details page.

- Purge Batches - deletes any batches associated with the entire batch set.

- View Batch Summary Report - displays the Batch Summary report. This field is only enabled after you've created batches.

- Refresh Page - refreshes the page.

- Auto Batching Status:

- Status - displays the current status of the batch: Pending, Processing, Error or Finished

- Documents to be Batched - displays the remaining documents that don't meet the minimum batch size. You must manually create a batch for these remaining documents.

- Last Successful Run - the date and time stamp of the last successful batch run.

- Last Error Reported - the date and time stamp of the last error that occurred.

Previously created batches do not update to include new properties. For example, if you create batches with a batch size of 500 and then need to lower the size, you should purge the existing batches. You can then make any changes and recreate the batches. Any existing data in the original batch set is lost when those batches are purged.

## Deleting an individual batch

The following permissions are required to delete an individual batch:

Object Security Tab Visibility Other Settings

- Batch Set: View, Edit

- Batch: View, Edit, Delete

- Review Batches

- Mass Operations: Delete

To delete an individual batch using the Delete mass operation, do the following:

- Navigate to the Review Batches tab.

- Select the individual batch you'd like to delete.

- Select Delete from the mass operations drop-down menu in the bottom-left.

A pop-up window displays.

- Click Delete in the pop-up.

The selected batch is removed.

## Deleting a batch set

The following permissions are required to delete a batch set:

Object Security Tab Visibility Other Settings

- Batch Set: View, Edit, Delete

- Batch: View, Edit, Delete

- Case Admin

- Batch Sets

- Mass Operations: Delete

Use the following procedure to delete a batch set.

- Navigate to the Batch Set tab.

- Select the checkbox next to the batch you want to delete.

- Select Delete in the mass operations drop-down menu, and click Go .

A confirmation message appears.

- Click OK .

For more information, see Mass delete .

## Searching for documents not included in existing batch sets

In some cases, you may need to search for all documents not included in a batch set. To properly search for documents not included in a batch set, use the following search criteria:

- Field: Batch

- Operator: not these conditions

- Value:

- Field: Batch::Batch Set

- Operator: any of these

- Value: select all existing batch sets

Documents included in the batch set(s) you select for the Batch::Batch Set field value are excluded from your search results.

If you want to run a search that excludes only certain batch sets select these conditions as the first operator. Select none of these as the second operator. Documents belonging to more than one batch set may return in your search results. Using this combination of search operators returns documents that belong to any batch set you don't specify in the Batch::Batch Set value.

On this page

- Batches

- Batch fields in Relativity

- Creating and editing batch sets

- Batch Sets for Reviewers

- Fields

- Batch Set console

- Deleting an individual batch

- Deleting a batch set

- Searching for documents not included in existing batch sets


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
