---
title: "Production sets"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_sets.htm
collection: user
fetched_at: 2026-06-22T06:02:53+00:00
sha256: 6e7a0def69ca09642417c9176ba67457945110cd3f2a71a1b6501aef14258108
---

Production sets Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production sets

## Post production

When you want to produce documents in a case workspace, you can create a production set that defines the markup set for redactions, the document numbering, the appearance of the numbering, and other settings that Relativity uses when you run the production.

You can then view the produced images in the Review Interface by selecting Production mode and the production set.

This page contains the following:

- Creating and editing a production set

- Basic Settings

- Numbering

- Branding

- Sorting

- Viewing production set details

See these related pages:

- Production Data Source

- Production Placeholders

- Production console

## Creating and editing a production set

Before you can run a production, you must create a production set, and then add documents to it via a saved search. Use the following steps to create or edit a production set:

- Navigate to the Production tab.

- Click the Production Sets tab.

- Click New Production .

- To edit an existing production set, click the edit link next to the production set name.

The name of a production can be changed at any point in the production process.

- Add or edit the fields in the following sections as necessary. Required fields are orange.

- Basic Settings

- Numbering

- Branding

- Sorting

- Other

- Save the additions or updates.

If you imported a production, the page numbering is set by the imported Opticon file. Any markup set selection, branding, or other settings on the Production Set form are not applied to the imported production. The images produce exactly as they were imported.

## Basic Settings

When you add or edit a production set, you can begin by modifying the settings in the Basic Settings section of the Production Set form.

The Basic Settings section contains the following fields:

- Name - (required) the name of the production set you are creating.

- Date Produced - the date that the documents were produced. You can select any date in this field. If you do not select a date, Relativity automatically sets this value with the date that the Production was completed.

- Email Notification Recipients - sends email notifications when a production fails or completes. To send the email messages to multiple recipients, enter email addresses separated by a semicolon.

- Imported - indicates if the production is open to receive imported production documents.

- Scale Branding Font for Viewer - (required) scales up the branding text size to be consistent with Relativity 7.5 behavior for optimal viewing of images in the Viewer when set to Yes . Set this field to No to use the default font scaling when printing images. This field is read-only after you run a production set.

- Branding Font - (required) the font type that will be use on the branded text. To set a default branding font for productions, adjust the value of DefaultBrandingFont. See DefaultBrandingFont .

- Branding Font Size - (required) the font size for branding added to a page. The font type is Arial. To set a default branding font size for productions, adjust the value of DefaultBrandingFontSize. See DefaultBrandingFontSize .

- Placeholder Image Format - (required) brands the production placeholder image as the file type selected. This field is set to TIFF by default, but users have the option to brand placeholder images as JPEG files too.

Click on the tool tip icon next to Basic Settings for more information on the image file types (see image below).

-

Copy Production on Workspace Create - (required) if the current workspace is used as a template the production is copied into the new workspace when the field is set to Yes . This option copies the production and associated data sources.

- Wraps Branding Text - if the content of two adjacent footers or headers are likely to overlap.

## Numbering

On the Production Set form, you can define multiple options that control how numbering is applied to images in your production.

Relativity provides the following numbering types for productions:

Numbering type Description

Page level numbering Generates a new incremental number (also known as a Bates number) on every page across your production documents. This number is branded on the images in your production.

Document level numbering Generates a new document number for each document, which is branded on the images in your production.

Original image numbering Retains the identifiers originally associated with your images. For example, you may want to retain the Bates or other numbers already assigned to images uploaded to Relativity. Relativity utilizes these values to create the production and attachment numbers.

Existing production numbering Re-uses the Bates numbering fields from a previously-run production set, changes the images of the documents produced, or produces only a subset of documents contained in the existing production.

Document field numbering Uses any fixed-length text field on the Document object for your numbering. Reflective fields are not available for this numbering option.

Page level numbering

Select Page level numbering to generate a new incremental number (also known as a Bates number) on every page across your production documents. This number is branded on the images in your production.

The form fields available when you select Page level numbering include:

- Prefix - (required) the characters added to the beginning of each Bates number. This is limited to 50 characters.

- Suffix - optional characters applied to the end of each Bates number. This is a static, non-incremental text string, limited to 50 characters.

- Start number - (required) the first number used in a sequence of Bates numbers. To select a previous production and continue with its numbering sequence, click Continue from Previous .

Continue from Previous will not work for productions using original image numbering, existing production numbering, or document field numbering.

Relativity automatically populates the Start number field with the value that displays for the Next doc number .

- Number of digits for document numbering - (required) determines how many digits the Bates number contains. The range of available values is between 1 and 10. By default, this option is set to 7 characters.

- Attachment relational field - selects a relational field indicating a family group such as group identifier.

- Preview - displays sample text illustrating how the Bates number appears in the images.

Relativity does not support the combined length of the Prefix and Suffix exceeding 255 characters when using Page level numbering.

Document level numbering

Select Document level numbering to generate a new document number for each document, which is branded on the images in your production.

The form fields available when you select Document level numbering include:

- Prefix - (required) lists the characters added to the beginning of each document number. This is limited to 50 characters.

- Suffix - lists optional characters applied to the end of each document number. The suffix is added after the document number but before the page number when the Include page number option is selected. This is a static, non-incremental text string, limited to 50 characters.

- Start number - (required) indicates the first number used in a sequence of document numbers. To select a previous production and continue with its numbering sequence, click Continue from Previous .

Continue from Previous will not work for productions using original image numbering, existing production numbering, or document field numbering.

Relativity automatically populates the Start number field with the value that displays for the Next doc number .

- Number of digits for document numbering - (required) determines how many digits the document number contains. The range of available values is between 1 and 10. By default, this option is set to 7 characters.

- Include page numbers - (required) adds a unique page number after the document number on each page in a document, when it is set to Yes . By default, this option is set to No .

If you export a production with document level numbering as single-page TIFF, and it does not include page numbering, Relativity automatically adds page numbers to identify each page uniquely.

- Document Page Separator - displays when you select the Include page number option. The following separators are available:

- _ (underscore, selected by default)

-

- (hyphen)

-

. (period)

- Number of digits for page numbering - determines how many digits the page number contains. The range of available values is between 1 and 6. By default, this option is set to 4 characters.

- Start numbering on second page - determines where the document level numbering begins.

- Yes - starts numbering on the second page of the production documents.

- No - starts numbering on the first page of the production documents.

- Attachment relational field - selects a relational field indicating a family group such as group identifier.

The combined length of the Prefix and Suffix cannot exceed 255 characters when using Document level numbering.

Original image numbering

Select the Original image numbering to retain the identifiers originally associated with your images. For example, you may want to retain the Bates or other numbers already assigned to images uploaded to Relativity. Relativity utilizes these values to create the production and attachment numbers.

The form fields available when you select Original image numbering include:

- Attachment relational field - selects a relational field indicating a family group such as group identifier.

The following table provides several original image numbering scenarios:

Document has Produced with Generated Bates numbers with

Natives + imported images Images and natives The Image identifiers defined in the Image Load File.

Natives + images Natives only The Document Identifier.

Natives + Oracle images Images only

The Images number created by the TIFF native manager: Document Identifier + <Page

Number> + <Hash Value>.

For example: Stel_Img_0_272ec3bf-9287-4862-be34-bbb230274a86

Images only (imported) Images only The Image identifiers defined in the Image Load File.

Natives only Natives only The Document Identifier.

Natives only Images and natives

The created image place holder, using the Document Identifier field.

For Example: e2f448d6-6e19-4d7c-9e50-7fccbf9c5c6b

Natives only Images only

The created image place holder, using the Document Identifier field.

For Example: e2f448d6-6e19-4d7c-9e50-7fccbf9c5c6b

Existing production numbering

Select the Existing production numbering choice if you'd like to re-use the Bates numbering fields from a previously-run production set, change the images of the documents produced, or produce only a subset of documents contained in the existing production. More specifically, you may want to select this option if, for example, a court order requires that your documents be produced without an already-applied confidential branding or if you need to redact already-produced documents for privilege.

-

When creating a production set with Existing production numbering, you cannot add documents not contained in the existing set, change page counts, or change whether or not a document previously produced as native only is produced with a placeholder. You can, however, replace a document produced as a image with a placeholder as long as it’s a single page document.

- When you choose a production set with more documents than the existing set, Relativity generates a warning to inform you that it auto-removed the extra documents. If the new production set has a subset of documents contain in the existing set, the new production set will generate without any warnings.

The following required fields appear when you select the Existing production numbering choice:

- Production Set - (required) Select the production set containing the numbers you'd like to use for the set you're creating. Only completed production sets are available to select from this drop-down list.

- Merge Existing Set - (required) When you merge a new production with an existing production, the new production images replace the images in the previously existing production. The new production still exists for export. Relativity updates the Has Redaction field in the Production Information record in cases where redactions were added or removed. From the viewer, if you compare the existing production and the new production, the images look the same if the images from the existing production set are not in the cache. If existing production images are in the cache, then you'll still see the original produced version of the image when you click on the existing production set production radio button. For more information on merging, see Numbering merge conflicts .

Selecting this option fully replaces the original production's produced image inside Relativity. You cannot export the original produced image if you merge the sets.

If you have an existing production set with document level numbering, no page-level markers, and the existing production is migrated into the environment, you cannot merge the productions together with existing production numbering.

If one production references an already produced production in the Production Set field, you cannot delete the referenced production. You can resolve the error by referencing an existing production or modifying the parameters of the production to eliminate the reference to the deleted production.

#### Numbering merge conflicts

When electing to use an existing production's numbering and then merging that numbering, consider the following conflict scenarios. These scenarios result in errors when you attempt to run a new production set:

- There are any documents in the production set you're creating that weren't included in the existing production set. You must remove these documents from the new production in order to run it.

- The page counts of the documents in the production set you're creating differs from the page counts in the existing production set.

- If documents in a production set are also in the production restriction for that production, you must remove the documents from either the production set or the production restriction.

- You attempt to perform any action on a production set while it is merging with another.

Document field numbering

Select the Document field numbering choice if you'd like to use any fixed-length text field on the Document object for your numbering. Reflective fields are not available for this numbering option.

You may want to select this option if, for example, if you import a set of documents into Relativity and want to maintain the original numbering of the documents. For example, you could choose control number as the field and produce documents using the control number as the bates field.

The following required fields appear when you select the Document field numbering choice:

- Numbering Field - (required) select the field you'd like to use for numbering from this drop-down list. Only fixed-length text fields are available to select from this drop-down list.

The content of the numbering field, prefix, and suffix cannot exceed 255 characters.

- Include page numbers - (required) adds a unique page number after the document number on each page in a document, when it is set to Yes . By default, this option is set to No .

If you export a production with document level numbering as single-page TIFF, and it does not include page numbering, Relativity automatically adds page numbers to identify each page uniquely.

- Document Page Separator - (required) displays when you select the Include page number option. The following separators are available:

- _ (underscore, selected by default)

-

- (hyphen)

-

. (period)

- Number of digits for page numbering - (required) determines how many digits the page number contains. The range of available values is between 1 and 6. By default, this option is set to 4 characters.

- Start numbering on second page - (required) determines where the document level numbering begins.

- Yes - starts numbering on the second page of the production documents.

- No - starts numbering on the first page of the production documents.

- Attachment relational field - selects a relational field indicating a family group such as group identifier.

## Branding

In the Branding section of the production set form, you can set branding options for headers and footers. You can position headers and footers to the left, center, and right on the images in your production.

If you experience slowness viewing this page, reduce the instance setting ChoiceLimitForUI until the drop-downs become popup pickers. Changing this instance setting affects all workspaces in an environment.

Select a Type for each header or footer position where you want information branded in the image.

The following Types are available:

- Production Bates Number - displays the Bates number associated with each document page.

- Production Number - displays the document number associated with each page. (Available for Document level numbering and Original image numbering only)

- Field - uses the value in the selected document field for branding on each image created for a document.

Relativity restricts the following field types from branding for document images in a production: user, multiple object, and reflective field types.

- Free Text - uses any combination of text, tokens, and carriage returns that you define. However, Relativity doesn't support multi-reflected, multi-object, relational, file, user, and system fields for branding. You can use carriage returns to position the header or the footer closer to the top and bottom margins respectively. Use tokens to include field data as follows:

If you enter a field ID that represents a field that doesn't exist or is not a document field you cannot produce the production.

- Production Number: {!PRODNUM!}

- Any Data Field: {!FIELD:ARTIFACTID!} as in the example {!FIELD:1040549!}. You can brand multiple fields by separating the entries with carriage returns.

- Original Image Number - uses the original page ID assigned by Relativity as follows:

- Numbering used in load file is applied when an image load file was used to import the data. If you run a production with image placeholders, the original image number is replaced with the Document Identifier field.

- Document ID, page ID, and a hash value are applied in combination when images were created using the Image-on-the-fly functionality.

In the above example, SSHACKLET_0000112 is the Document ID, 0 is the page ID, and 5b419b77-abe4-4ed6-a68a-197f99390895 is the hash value.

- Document Identifier + Page Number - uses the document identifier with the page number appended to it. This option sets the first page number to 1 even when the document contains only a single page. The following pages are numbered incrementally. In addition, the page number is padded with up to four digits as illustrated below.

Depending on the settings for the header and footer, Relativity prevents the image from being cut off by adding approximately five extra pixels to its edges.

- Advanced Formatting - uses any combination of fields from the Advanced Formatting drop-down list, free-form text, and carriage returns. The Advanced Formatting option also supports a scripting language that you can use to create conditional branding based on production, document, and page fields. See Advanced Formatting for Branding .

Branding text wraps by default if the content of two adjacent footers or headers are likely to overlap with each other. If you copy some older productions, the branding on the new production may look different than the original production, especially if the original production had additional spacing or new lines to prevent the stamps from overlapping.

To keep text from wrapping by default across your entire Relativity instance, add the Relativity.Productions.Domain.Toggles.BrandingOverlayToggle to the Toggle table in the Admin (EDDS) database with the values listed below.

- Name = Relativity.Productions.Domain.Toggles.BrandingOverlayToggle

- IsEnabled = 0

## Sorting

In Sorting, you can select a field that determines how your production is sorted. Note that you can sort a production set by more than one field at a time. You can also use a descending or ascending sort order. By default, the sort order is Artifact ID, which is the load order of the documents. When you perform a sort, family groups are not kept together. The sorting applies to all data sources added to the production set. Sorting is only applicable when Production Numbering is set to the following:

- Page level numbering

- Document level numbering

If you experience slowness viewing this page, reduce the instance setting ChoiceLimitForUI until the drop-downs become popup pickers. Changing this instance setting affects all workspaces in an environment.

If no sort order is specified, the documents will be stamped in order of Artifact ID ascending. The production numbering sort order doesn't determine the order of documents in the document list view.

If you would like to keep family group together in sort order, you must set Field 1/5 to Family Group following with other sorting criteria.

## Post Production

Post Production is an alternative workflow to running scripts after production. In Post Production, you can select additional actions to run automatically once production has completed. Post Production allows for better progress tracking, runs automatically, and provides visibility on the Production Set Console.

The Copy Bates to Document Fields action is supported in Post Production.

Once a production is completed, information stored from the production is copied to the following fields as configured.

- Begin Bates Field — choose the field that you want to copy from Production:BeginBates

- End Bates Field — choose the field that you want to copy from Production:EndBates

- Begin Bates Attachment Field — enabled only when Attachment Relational Field has been selected. Choose the field that you want to copy from Production:BegAttach

- End Bates Attachment Field — enabled only when Attachment Relational Field has been selected. Choose the field that you want to copy from Production:EndAttach

Create dedicated Fixed-Length Text fields for this operation or select fields with the purpose of having bates populated. Selecting one of the template fields may result in production failure.

## Other

The Other section displays additional fields added to the form after the production set was saved:

- Restriction override by - displays the name of the user who clicked the Override and Continue button when running the production without removing conflicts. This user must have the Override Production Restrictions permission.

- Restriction override on - lists the date and time when the production restrictions were overridden.

## Viewing production set details

### Production set details options

You can use the options available on the detail view for production sets to edit permissions, view audit information, preview the production, and perform other tasks. You can access these options through the buttons at the top of the page.

Use the following buttons to complete tasks as necessary:

- Edit - re-displays the production set form so you can update values in the fields. See Creating and editing a production set .

-

Delete - removes the production set from Relativity. When you delete a production, the production is immediately removed from the Production sets tab. However, you may still see the Bates numbers from the production in the Documents tab. Relativity deletes the Bates numbers, the production data source, and any other remaining production information during off hours.

If you don't want to lose the previously recorded Bates numbers, run the Assign Legacy Document Bates Fields script. After you click Delete , a confirmation message displays with the Dependencies button. See Displaying and interpreting the dependencies report for more information.

When deleting a production the production images are deleted, not the original images.

- Back - redirects you to the item list on the Production Sets tab

- Edit Permissions - displays a security page where you can set user permissions on a production set. You can edit rights only on the current production set. By default, the Production Set tab is secured according to the workspace-level rights. See Relativity object security for more information.

- View Audit - displays the history for the production.

The Production Set details options view also shows Production Status Information, Basic Settings, Numbering, Branding, Sorting, Other, and the Production Data Source. Once the production is run, you can also view the First and Last Bates Values associated with the production.

### Previewing a production

In the Production console, click the Preview Production button to preview the newly saved production before running the production. Preview the production to confirm that all basic settings, numbering, branding, sorting, and other options are correct. For more information, see Production console .

## Tracking multiple redaction sets

If you need to track multiple redaction sets on the same document, you can use the following workflow:

- Create multiple redaction sets by defining different markups. See Markups .

- Use each markup to redact the same document.

- Create a production and select a specific markup.

When you select the markup, it controls the redactions branded during production, so you can track multiple redaction sets on the same document, and generate different productions.

On this page

- Production sets

- Post production

- Creating and editing a production set

- Basic Settings

- Numbering

- Branding

- Sorting

- Post Production

- Other

- Viewing production set details

- Production set details options

- Previewing a production

- Tracking multiple redaction sets


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
