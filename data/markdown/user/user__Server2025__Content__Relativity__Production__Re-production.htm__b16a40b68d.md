---
title: "Re-production"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Re-production.htm
collection: user
fetched_at: 2026-06-22T06:08:35+00:00
sha256: 40cc249c428b04d0c2f59e742bd5a61e8fd9413e62b4fa6963422177cc6f9807
---

Re-production Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Re-production

You can use the Re-produce mass operation to re-produce select documents from a produced production without having to run the whole production again. For each production that is modified, Relativity creates a new production job, which is a re-production job. Re-production jobs store the modified documents and reuse the numbering format, bates numbers, and branding options from the original productions.

Once a re-production job finishes running, the modified documents merge into the existing, original production set; they overwrite the documents that were previously produced. The previously produced version of the document will no longer display in the Viewer and will not be available for export.

Re-production jobs are stored as regular productions in the system and are not deleted after they are complete. If you want to export just the documents that were modified, use the RDC to export the re-producion job.

## Special considerations

Special considerations for the re-production feature include:

-

The re-production feature only works with productions that have been run in Relativity. It will not work with outside productions that have been loaded in.

- You can re-produce documents from multiple production sets with a single mass operation. However, you can only apply one re-production type at a time. Relativity recommends using saved searches to group documents that need the same type of re-production. See Re-production types .

-

Re-production checks for documents that have changed images. Changes to native documents will not be reflected.

-

A re-production job is named after the original production that is modified and uses this naming convention: [original production name]_REPROD_[ re-production type]_[date of the re-production job]. The re-production type in the name is abbreviated. Re-production type abbreviations include:

Re-production type Abbreviation

Replace produced images with placeholder I-P

Replace placeholder with images P-I

Re-produce documents (same number of pages) I-I

For example, if on September 30, 2019, you ran a re-production job to replace documents that were produced as placeholders with images from a production set named "Production", the re-production name would be Production_REPROD_P-I_2019-09-30.

-

Every time a production set is modified via the Re-production mass action, a new entry is added to the Completed Re-productions field in the Production Summary section of the original production set. Click on the name of a completed re-production to go to the production set for that re-production job. If you delete a re-production job or do not have access to that re-production set, the name of the set will still appear on the list, but you will not be able to click on it. See Run a production .

## Security configuration

You must configure certain workspace level permissions to use the Re-production mass operation.

To configure the required security permissions:

- Navigate to the Workspace Details tab.

- Click Manage Permissions .

- Click Edit Permissions for a group on the Group Management tab.

-

Enable the following security permissions:

Object security Tab visibility Other settings

-

Production - View/Edit/Add

-

Production Data Source - View/Edit/Add

-

Production Placeholder - View

NA

Mass operations

- Re-produce

## Re-production types

Relativity supported and unsupported re-production types include:

Supported re-production types Unsupported re-production types

- Replace produced images with placeholder (I-P)

- Replace placeholder with images (P-I)

- Re-produce documents (same number of pages) (I-I)

- Replace a document that was produced as a placeholder with another placeholder.

- Replace a document that was produced as native only with produced images or a placeholder.

- Re-produce the same document as images but with a different number of images.

While you can re-produce documents from multiple production sets with a single mass operation, you can only apply one re-production type at a time. For example, if you want to re-produce 100 documents, and you want to replace 60 with produced images and replace 40 with a placeholder, you would need to run two mass operations.

If none of the documents selected meet the re-production type you choose, when you move to the next step you will receive this error: “No productions match the re-production criteria. Please verify all selected documents are included in a production and match the original production type of the re-production options.” For example, you will receive this error if you selected five documents that were produced only as Natives and if you selected "Replace produced images with placeholder" as the Re-production type. To resolve the error, exit the module and remove the documents that do not meet the selected re-production type criteria from the group of documents you selected for re-production. To avoid this error, Relativity recommends using saved searches to group documents that need the same type of re-production.

### Replace produced images with placeholder (I-P)

In the Re-produce Documents module, select Replace produced images with placeholder if you need to replace images in a production with a placeholder. With this re-production type, each page of an imaged document is replaced with a placeholder. For example, if an imaged document is 50 pages, each of the 50 pages would be replaced with a placeholder; the re-produced document would contain 50 placeholders. This preserves the original bates numbering.

- Include Natives - a boolean field. Select Yes to include the natives of the documents you selected for re-production. Set this field to No if you only want to include a placeholder for the documents. This option overrides the option on the original production. If the document was originally produced with natives, but the user does not select "Include Natives", the document will be merged to the original production with no natives.

- Select Production Placeholder - select a production placeholder for the documents you selected for re-production.

### Replace placeholder with images (P-I)

In the Re-produce Documents module, select Replace placeholder with images if you need to replace documents that were produced as placeholders with produced images.

The documents must already be imaged before you run the mass operation, or an error will occur with the mass operation.

- Delimiter - given that you are replacing a placeholder (1-page image) with produced images, it is possible that the new document may have more than 1 page. This option allow you to use a character to suffix the original production bates number from the number of pages in re-produced image. The suffix will start on the second page with number #1. The following separators can be used:

-

_ (underscore, selected by default)

-

- (hyphen)

-

. (period)

- Number of Digits - determines how many digits the suffix number contains.. The range of available values is between 1 and 6. By default, this option is set to 4 characters.

- Include Natives - a boolean field. Select Yes to include the natives of the documents you selected for re-production. Set this field to No if you only want to include a placeholder for the documents. This option overrides the option on the original production. If the document was originally produced with natives, but the user does not select "Include Natives", the document will be merged to the original production with no natives.

- Burn Redactions - a boolean field. Select Yes to apply redactions to the documents you selected for re-production. Set this field to No if you do not want redactions applied to the documents.

- Select Markup Set - indicates which markup set is used to apply redactions to the production images.

- Preview - displays what the bates number will look like based on your selections.

### Re-produce documents (same number of pages) (I-I)

In the Re-produce Documents module, select Re-produce documents (same number of pages) if you need to replace documents in a production.

The documents that you are using to replace the documents in the production must be the same number of pages as the documents in the production that you are replacing.

- Include Natives - a boolean field. Select Yes to include the natives of the documents you selected for re-production. Set this field to No if you only want to include a placeholder for the documents. This option overrides the option on the original production. If the document was originally produced with natives, but the user does not select "Include Natives", the document will be merged to the original production with no natives.

- Burn redactions - a boolean field. Select Yes to apply redactions to the documents you selected for re-production. Set this field to No if you do not want redactions applied to the documents.

- Select Markup Set - indicates which markup set is used to apply redactions to the production images.

## Re-production scenarios

Re-production scenarios include:

Documents selected Re-production type selected Productions available for modification Number of documents to be modified in each production Outcome

Doc A was produced as placeholder in Prod_1

Doc B was produced as placeholder in Prod_2

Replace Placeholders with images

Prod_1

Prod_2

Prod_1 | 1 out of the total of 2 documents selected will be modified in this production

Prod_2 | 1 out of the total of 2 documents selected will be modified in this production

Doc A is re-produced in Prod_1

Doc B is re-produced in Prod_2

Doc A was produced as placeholder in Prod_1

Doc B was produced as Images in Prod_1

Replace Placeholders with images Prod_1 Prod_1 | 1 out of the total of 2 documents selected will be modify in this production. Doc A is re-produced in Prod_1

Doc A was produced as placeholder in Prod_1

Doc B was produced as images in Prod_1

Doc A was produced as images in Prod_2

Doc B was produced as placeholder in Prod_2

Replace Placeholders with images

Prod_1

Prod_2

Prod_1 | 1 out of the total of 2 documents selected will be modify in this production.

Prod_2 | 1 out of the total of 2 documents selected will be modify in this production.

Doc A is re-produced in Prod_1

Doc B is re-produced in Prod_2

Doc A was produced as placeholder in Prod_1

Doc A was produced as images in Prod_2

Doc B was produced as images in Prod_2

Replace Placeholders with images

Prod_1

Prod_2 is not displayed because Doc A and Doc B were not produced as placeholder in Prod_2.

Prod_1 | 1 out of the total of 2 documents selected will be modify in this production. Doc A is re-produced in Prod_1

Doc A was produced as placeholder in Prod_1

Doc B was produced as placeholder in Prod_1

Doc A was produced as placeholder in Prod_2

Doc B was produced as images in Prod_2

Replace Placeholders with images

Prod_1

Prod_2

Prod_1 | 2 out of the total of 2 documents selected will be modify in this production.

Prod_2 | 1 out of the total of 2 documents selected will be modify in this production.

Doc A is re-produced in Prod_1

Doc B is re-produced in Prod_1

Doc A is re-produced in Prod_2

Doc A was produced as placeholder in Prod_1

Doc B was produced as placeholder in Prod_1

Doc A was produced as placeholder in Prod_2

Doc B was produced as placeholder in Prod_2

Replace Placeholders with images

Need to replace Doc A and Doc B in Prod_1.

Need to replace Doc A only in Prod_2.

Doc B should not be replaced in Prod_2.

Prod_1

Prod_2

Prod_1 | 2 out of the total of 2 documents selected will be modify in this production.

Prod_2 | 2 out of the total of 2 documents selected will be modify in this production.

Doc A and Doc B are both modified in Prod_1 and Prod_2.

## Re-produce documents

To re-produce documents:

- Navigate to the Documents tab in a workspace.

-

Select the documents that you want to re-produce from a document view, folder, field tree, saved search, or dashboard.

- Click Re-produce from the mass operations menu. The Re-produce Documents module opens.

-

Select a Re-production Type, and complete the required fields. See Re-production types .

If you are modifying multiple productions at the time, the options that you select on this step will apply to all the productions you are modifying, including the placeholder selected in this step, burn redactions, and the options of whether the documents will be produced with natives.

- Click Next .

-

Select the productions that you want modify.

Only productions associated with the selected documents and options display. Productions with a status different to “Produced” or Productions that used Existing numbering will not be available here.

-

Click Re-produce .

Do not close the Re-produce Documents module until the Confirmation checkmark appears. Once the Confirmation checkmark appears, the re-production sets have been created and added to the Production queue.

## Re-production job status

To see the status of a re-production job:

-

Click Click here in the Re-produce Documents module. This will take you to the Re-production view. See Re-production views .

- Navigate to the Production Sets tab, and select the Re-production view. See Re-production views .

## Re-production views

Two views on the Production Sets tab display information regarding re-productions:

- Re-productions - a view that lists every re-production jobs. Fields in the view include:

- Name - the name of the re-production job.

- Status - the status of the re-production job.

- First Bates Value - the first bates number in the production.

- Last Bates Value - the last bates number in the production.

- Prefix - the characters added to the beginning of each Bates number.

- Production Set - the name of and link to the original production set.

- Original Productions - a view that lists every production set that have been modified by a re-production job. Fields in the view include:

- Name - the name of the original production.

- Status - the status of the production job.

- First Bates Value - the first bates number in the production.

- Last Bates Value - the last bates number in the production.

- Prefix - the characters added to the beginning of each Bates number.

- Start Number - the first number used in a sequence of Bates numbers.

On this page

- Re-production

- Special considerations

- Security configuration

- Re-production types

- Replace produced images with placeholder (I-P)

- Replace placeholder with images (P-I)

- Re-produce documents (same number of pages) (I-I)

- Re-production scenarios

- Re-produce documents

- Re-production job status

- Re-production views


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
