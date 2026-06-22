---
title: "Name normalization results"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Name_normalization_results.htm
collection: user
fetched_at: 2026-06-22T06:05:05+00:00
sha256: 514efb9a56e3c7aa720d617bb0a2ec8aa7e5de5f3ab882ded690fb54f10db2fc
---

Name normalization results

# Name normalization results

After you run the name normalization operation, the structured analytics set displays the number of aliases identified and the number of new aliases imported. If an alias already exists in Relativity, it isn't created again so as not to create duplicates.

## Aliases

Analytics adds aliases into Relativity under the Alias RDO. You can view these aliases from the Aliases tab under the Entities parent tab. For more information, see Alias object .

The following fields are created for each alias:

Only the Name and Type fields are required for each alias.

- Name - the name of the alias. This field must be unique.

Don't adjust the name field even if it's incorrect as the field is used in subsequent runs of name normalization.

- Domain - the full domain of the alias (everything after the @ sign).

- us.relativity.com

- Primary Domain - the domain of the organization.

- relativity.com

- Type - the type can be one of the following:

- Proper Name - an alias that contains only letters or letters and a comma.

- Jane Smith

- Smith, Jane

- Email Address - a standard email address with no display name.

- jane.smith@relativity.com

- Extended Email Address - an email address that contains other characters. A typical case is an email address with a display name.

- Jane Smith [Jane.Smith@relativity.com]

- Exchange - X500 and X400 formats.

- Smith, Jane </O=RELATIVITY/OU=NA/CN=RECIPIENTS/CN=JSMITH>

- Phone Number - an alias that contains only numbers and punctuation.

- 123-456-7890

- Undefined - an alias that doesn't fall into any of the categories above.

- Jane Smith/RELATIVITY@relativityXgat

- Entity - the entity the alias belongs to. This field links to the Entity object.

The Entity field is locked from editing. Use the Assign to Entity mass action on the Aliases tab to assign an alias to a different entity.

The following multiple-object fields link aliases to the documents they appear in.

These fields are locked from editing.

- Alias From - the documents where the given alias was identified in the From section of the document's top-most segment header.

- Alias To - the documents where the given alias was identified in the To section of the document's top-most segment header.

- Alias CC - the documents where the given alias was identified in the CC section of the document's top-most segment header.

- Alias BCC - the documents where the given alias was identified in the BCC section of the document's top-most segment header.

- Alias Recipient - the documents where the given alias was identified in the To, CC, or BCC section of the document's top-most segment header.

- Alias Participant - the documents where the given alias was identified in the From, To, CC, or BCC section of any segment header within a document.

Click the name of the alias to view details including the documents where that alias appears in the Alias From, Alias To, Alias CC, Alias BCC, Alias Recipient, or Alias Participant field.

## Entities

Analytics uses logic to automatically group multiple aliases into a single entity. Entities with the same first name and last name values are automatically merged with each other. Also, entities identified by name normalization are automatically merged with those created by Legal Hold, Processing, or Case Dynamics when their first and last name values match.

The following fields are created for each entity:

Only the Name and Type fields are required for each entity. If Legal Hold is installed in the workspace, the Email field is also required.

- Full Name - the full name of the entity.

- Smith, Jane

- First Name - the first name of the entity.

- Jane

- Last Name - the last name of the entity.

- Smith

- Classification - all entities created or impacted by name normalization receive the classification value Communicator - Analytics . You can add new Classification choices, such as Custodian, to help keep track of groups of entities.

- Aliases - any aliases linked to the entity. This field links to the Alias object.

The Aliases field is locked from editing. Use the Merge mass action on the Entities tab to merge entities.

The following multiple-object fields link entities to the documents that their aliases appear in:

These fields are locked from editing.

- Entity From - the documents where any of the given entity's linked aliases were identified in the From section of the document's top-most segment header.

- Entity To - the documents where any of the given entity's linked aliases were identified in the To section of the document's top-most segment header.

- Entity CC - the documents where any of the given entity's linked aliases were identified in the CC section of the document's top-most segment header.

- Entity BCC - the documents where any of the given entity's linked aliases were identified in the BCC section of the document's top-most segment header.

- Entity Recipient - the documents where any of the given entity's linked aliases were identified in the To, CC, or BCC section of the document's top-most segment header.

- Entity Participant - the documents where any of the given entity's linked aliases were identified in the From, To, CC, or BCC section of any segment header within a document.

## Documents

After running the name normalization operation, Analytics automatically creates and populates the following fields on the Document object. These fields are linked to the Entity and Alias objects. These fields can be beneficial in creating searches, views, pivots, and privilege logs.

These fields are locked from editing.

- Alias From - the alias that was identified in the From section of a document's top-most segment header.

- Alias To - the aliases that were identified in the To section of a document's top-most segment header.

- Alias CC - the aliases that were identified in the CC section of a document's top-most segment header.

- Alias BCC - the aliases that were identified in the BCC section of a document's top-most segment headers.

- Alias Recipient - the aliases that were identified in the To, CC, or BCC sections of a document's top-most segment header.

- Alias Participant - the aliases that were identified in the From, To, CC, or BCC section of any segment header within a document.

- Entity From - the entity linked to the alias that was identified in the From section of a document's top-most segment header.

- Entity To - the entities that were linked to the aliases identified in the To section of a document's top-most segment header.

- Entity CC - the entities that were linked to the aliases that were identified in the CC section of a document's top-most segment header.

- Entity BCC - the entities that were linked to the aliases that were identified in the BCC section of a document's top-most segment header.

- Entity Recipient - the entities that were linked to the aliases that were identified in the To, CC, or BCC section of a document's top-most segment header.

- Entity Participant - the entities that were linked to the aliases that were identified in the From, To, CC, or BCC section of any segment header within a document.

## Adjusting results

You can use the Assign to Entity or Merge mass operations to adjust alias and entity relationships.

### Assign to Entity

The Assign to Entity mass operation is a mass operation on the Aliases tab. This operation lets you select and re-assign an alias to a different entity. An entity must exist for you to merge into it; you can't create a new entity on-the-fly.

You can only use the Assign to Entity mass operation if you have Analytics installed.

To assign aliases to entities:

- From the Aliases list, select the checkbox(es) next to the alias(es) that you want to assign to an entity.

No more than 500 aliases can be included in the Assign to Entity operation.

- From the actions menu at the bottom, select Assign to Entity from the second drop-down.

The Assign to Entity form appears.

- Select the Entity you want to assign the alias(es) to, and then click Assign to Entity .

### Merge

The Merge mass operation is a mass operation on the Entities tab that only appears if you have Analytics installed. This operation lets you select and merge multiple entities into a single entity.

You need the following object security permissions to merge entities:

-

Alias —View, Edit

-

Entity —View, Edit, Delete

-

Field —View, Edit

To limit the impact on Processing and Legal Hold workflows, do not merge entities if two or more of those entities are associated with a Processing data source or Legal Hold project. Doing so can cause downstream errors with publish jobs.

To merge entities:

- From the Entities list, select the checkboxes next to the entities that you want to merge.

No more than 50 entities can be merged at one time.

- From the actions menu at the bottom, select Merge from the second drop-down menu.

- Click Merge Entities .

If a conflict occurs when merging entity fields, the value of the entity associated with either a Processing data source or Legal Hold project takes priority followed by the value of the entity with the lowest Artifact ID.

#### Merging logic

The Merge operation doesn't give you the ability to select which entity fields are merged into and which are deleted. This is all decided by the logic below.

The Merge operation creates both an Update and Delete audit.

Click to expand details about merging logic

- All entities are sorted by Artifact ID, with the lowest Artifact ID at the top.

Artifact ID

Name

(Fixed-length)

Processing Data Source Company Name

Aliases

Internal

001 Smith, Jane M. Relativity ODA LLC

- Jane M. Smith

- janemsmith@example.com

Yes

002 jsmith kCura

- jsmith@kcura.com

No

003 Smith, Jane Processing Source 1

- jane.smith@relativity.com

004 Smith

- Smith

005 Smith, Jane (1) Acme

- jane.smith@acme.com

- Smith, Jane

No

- If an entity is associated with either a Processing data source or Legal Hold project, that entity is moved to the top.

Artifact ID

Name

(Fixed-length text)

Processing Data Source

(Multiple object)

Company Name

(Fixed-length text)

Aliases

(Multiple object)

Internal

(Yes/No)

003 Smith, Jane Processing Source 1

- jane.smith@relativity.com

001 Smith, Jane M. Relativity ODA LLC

- Jane M. Smith

- janemsmith@example.com

Yes

002 jsmith kCura

- jsmith@kcura.com

No

004 Smith

- Smith

005 Smith, Jane (1) Acme

- jane.smith@acme.com

- Smith, Jane

No

- Relativity goes through each multiple object and multiple choice fields and assigns all values to the first entity in the list.

Artifact ID

Name

(Fixed-length text)

Processing Data Source

(Multiple object)

Company Name

(Fixed-length text)

Aliases

(Multiple object)

Internal

(Yes/No)

003 Smith, Jane Processing Source 1

- jane.smith@relativity.com

001 Smith, Jane M. Relativity ODA LLC

- Jane M. Smith

- janemsmith@example.com

Yes

002 jsmith kCura

- jsmith@kcura.com

No

004 Smith

- Smith

005 Smith, Jane (1) Acme

- jane.smith@acme.com

- Smith, Jane

No

- It then goes through each Fixed-length Text, Date, Whole Number, Decimal, Currency, Yes/No, Single Choice, User, File, and Single Object field and assigns the first value for each field to the first entity in the list, as indicated by the bold text.

Artifact ID

Name

(Fixed-length text)

Processing Data Source

(Multiple object)

Company Name

(Fixed-length text)

Aliases

(Multiple object)

Internal

(Yes/No)

003 Smith, Jane Processing Source 1

- jane.smith@relativity.com

001 Smith, Jane M. Relativity ODA LLC

- Jane M. Smith

- janemsmith@example.com

Yes

002 jsmith kCura

- jsmith@kcura.com

No

004 Smith

- Smith

005 Smith, Jane (1) Acme

- jane.smith@acme.com

- Smith, Jane

No

- Finally, Relativity goes through each Long Text field and assigns the first value under 500 characters to the first entity in the list.

Resulting Entity:

Artifact ID

Name

(Fixed-length text)

Processing Data Source

(Multiple object)

Company Name

(Fixed-length text)

Aliases

(Multiple object)

Internal

(Yes/No)

003 Smith, Jane Processing Source 1 Relativity ODA LLC

- jane.smith@relativity.com

- Jane M. Smith

- janemsmith@example.com

- jsmith@kcura.com

- Smith

- jane.smith@acme.com

- Smith, Jane

Yes

Entity data that isn't merged is deleted from the workspace. Any information linked to those entities that can't be merged, such as single object field, are also deleted from the workspace.

## Deleting all data to re-run

If you determine that you need to completely redo your name normalization, you will need to delete the data first. Unlike other structured analytics operations, name normalization results are not purged on subsequent runs. In order to remove all results and completely re-run name normalization, you must complete the following:

- Mass delete all aliases from the Aliases tab.

- Mass delete all entities that are Communicators from the Entities tab.

Do not delete custodians. If you have entities that are both Custodians and Communicators, mass-edit them to remove the Communicator classification.

- Re-run the name normalization operation with the Repopulate Text option enabled.
