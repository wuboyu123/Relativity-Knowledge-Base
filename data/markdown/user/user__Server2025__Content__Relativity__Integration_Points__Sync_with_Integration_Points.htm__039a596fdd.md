---
title: "Promoting data between workspaces through Integration Points"
url: https://help.relativity.com/Server2025/Content/Relativity/Integration_Points/Sync_with_Integration_Points.htm
collection: user
fetched_at: 2026-06-22T06:09:22+00:00
sha256: 5417e76df31774e4f513cb5a9716c8125e446860e4dddfaf67d95850249824fe
---

Promoting data between workspaces through Integration Points Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Promoting data between workspaces through Integration Points

You can use Integration Points to promote (move) data from one Relativity workspace to another Relativity workspace. This can be thought of as a one-way sync process from a source workspace to a destination workspace and not a back and forth syncing process between them.

Once you've tagged documents for inclusion in or exclusion from the data you want to promote for review, you can access Integration Points to start the job or jobs that will send those documents to the review workspace.

For information on how to develop with Integration Points, visit the Developers documentation site .

## Special considerations for large sync workflows

We recommend configuring integration point jobs into batches for large sync workflows. The following are recommendations when creating job batches:

- Document count should be no more than 500,000 documents in a single batch.

- When including extracted text as a mapped field in the integration point job, the sum of the extracted text in the batch should not exceed 25 GBs.

- The recommended number of fields to be mapped should be no greater than 100, but it is best to map as few long text fields as possible.

- When using the append/overlay or overlay only configuration, the batch size recommendations should be half the amount described above, specifically:

- 250,000 document count

- 12.5 GBs extracted text sum

## Integration point agent considerations

When you have one agent enabled, a scheduled integration points job is always queued and is always run. When you have more than one agent, however, the scheduled job may get queued or it may result in an error, after which that job is rescheduled. In other words, there is mixed behavior when you have enabled more than one agent.

The following table provides a breakdown of this behavior:

If Then

- You enable a single agent called Agent 1.

- You schedule a job called IP1 to run at 10:00 AM daily.

- You click Run or Retry Errors on IP1 at 9:59:59 AM.

- Agent 1 picks up the Run or Retry Errors job for IP1 and completes it in one hour.

- Agent 1 picks up the scheduled job for IP1, creates an error, removes the job history from IP1, and reschedules IP1 to run at the next interval.

- You enable Agent 1 and Agent 2.

- You schedule IP1 to run at 10:00 AM daily.

- You click Run or Retry Errors on IP1 at 9:59:59 AM.

- Agent 1 picks up the Run or Retry Errors job for IP1 and begins working on it.

- Agent 2 picks up the scheduled job for IP1, creates an error, removes the job history from IP1, and reschedules IP1 to run at the next interval.

- You enable Agent 1 and Agent 2.

- You schedule IP1 to run at 10:00 AM daily.

- You click Run or Retry Errors on IP1 at 9:59:59 AM.

- All other agents are busy, including Agent 2.

- Agent 1 picks up the Run or Retry Errors job for IP1 and begins working on it.

- Agent 1 completes the Run or Retry Errors job for IP1.

- Agent 1 picks up the scheduled job for IP1 and completes it.

- You enable Agent 1 and Agent 2.

- You click Run or Retry Errors on IP1.

- You click Run or Retry Errors on IP2.

- Agent 1 picks up the Run or Retry Errors job for IP1 and begins working on it.

- Agent 2 picks up the Run or Retry Errors job for IP2 and begins working on it.

## Exporting to a Relativity workspace

In addition to exporting to a CSV and load file, you have the option of exporting data from a source workspace to a destination workspace in Relativity. You can do this by selecting Relativity as the destination for the data that you intend to transfer and then selecting a specific workspace where you want that data to go. This is the most efficient way to move documents from one workspace to another, since it's a one-step process and it doesn't require you to export and re-import your data.

Note the following details about exporting to a workspace:

- When using integration points to transfer data between workspaces, you can move original images and natives and/or metadata. You are not required to have Integration Points installed on the destination workspace.

- When transferring images to a destination workspace, the field mapping section is disabled because only the control number is required and available in this scenario. If you want to transfer other field metadata, you must create a new integration point without choosing to copy images.

-

Integration points uses the following delimiters to configure the Import API for the destination workspace. Other delimiters typically configured with the Import API, for example via the RDC, are not utilized:

-

Multi-value delimiter: ASCII 029

- Nested-value delimiter: ASCII 030

### Setup

To create an integration point specifically for exporting a workspace, perform the following steps:

- Navigate to the Integration Points tab.

- Click New Integration Point .

- Complete the following fields in the Setup category of the Create Integration Point layout:

- Name —the name of your integration for reference purposes.

- Type —select Export to designate this as an export job. Selecting this sets the Source field to be Relativity.

- Source —this is automatically set to Relativity since you're exporting data out of a Relativity workspace.

- Destination —select Relativity . This is because you don't want to export directly to another Relativity workspace, but instead want to leverage the RDC export functionality, which is available on a subsequent layout only if you select Load File here.

- Transferred Object —select the available Document or non-document object meta data you want to promote to the destination workspace. The non-document object must already exist in the destination workspace. The data promotion process will not transfer custom objects created by users in a workspace.

You will need to create a new integration point for each object type that you want to export to the destination workspace.

- Profile —use this to complete the remaining Integration Points settings based on the settings of a saved profile. This includes all of the fields in the Connect to Source layout, as well as field mappings. If no profiles exist in the workspace, you don't have the option of selecting them. To apply a profile that you've already created, select it from the drop-down list. For more information on profiles, see Integration Points profiles .

- Email Notification Recipients —enter the email addresses of those who should receive notifications of whether the integration point export succeeded or failed. Use semi colons to separate email addresses.

- Log Errors —select Yes or No to denote whether Relativity tracks item level errors. If you select Yes , each job also logs any item level errors. If you select No , Relativity doesn't log these item level errors. Regardless of your selection, job-level errors are always recorded in Relativity.

- Enable Scheduler - gives you the option of scheduling additional exports. Selecting Yes makes the following fields available:

- Frequency —the interval at which Relativity syncs this integration point.

- Daily —select this option to sync once every day.

- Weekly —select this option to sync on a weekly basis. You can specify how often in the Reoccur field, in which you'll provide a number value in the Every # week(s) choice. You can then specify on which day of the week the sync will take place by checking any of the days of the week listed.

-

Monthly —select the day of the month that you want this integration point to sync once every month.

- Reoccur —enter the number of month(s) in which this integration point recurrently syncs.

- Send On

- Day __ the month —select the day of the month that you want this integration point to sync.

- The __ of the Month —select this option for this integration point to sync on the chosen day of every month. For example, "The Second Friday of the month."

- Start Date —the date that you want Integration Points to start syncing the data.

- End Date —(Optional) the date that you want Integration Points to stop syncing the data. Leaving the End Date blank causes the Integration Point to run indefinitely at the scheduled interval.

- Scheduled Time —the time at which this integration point syncs. This time is local to your PC, not to the server

- Click Next to advance to the Source Information layout.

### Connect to Source

Continue create your import integration point by connecting Relativity to the data source. Follow the steps below.

- In the Connect to Source layout complete the following fields:

- Source —select a saved search or production from the drop-down list. specify that you want to select a folder, from which you want export the data in your load file. You'll select this folder below from the folder structure in the Folder field. You'll also need to select a View from the Views field.

- Saved Search/Production —select an existing saved search or production set. If your source is a saved search, click the ellipsis button for an alternative way to select a saved search.

- Destination Workspace —select an existing workspace to export your saved search or production to.

- Location —select a folder or production set as the destination location.

- Folder —select the drop-down menu to expand the folder structure, locate the folder from which you want to export the data, and select it. This field is only available if you've selected Folder.

-

Production Set —select a production set to export the data to. Click the plus sign to create a new production set.

- Create Saved Search —select Yes to create a saved search in the destination workspace. This saved search's name will take the name given to the integration point.

- Click Next to advance to the Destination Information layout.

### Map Fields

Map the attributes or fields so that Integration Points imports the targeted data into specific Relativity fields.

- In the Map Fields wizard, you have the following options for mapping fields:

- Use the Shift + click and Ctrl + click method to select multiple fields at a time, similar to field mapping in the Relativity Desktop Client.

- Use the text search boxes above the Source and Destination lists to find a particular field.

- Use the single and double arrows or double-click a field to move selected fields between columns.

- Use the horizontal scroll bar in each column as needed to fully view long field names.

- Each column displays the number of fields available in that column. This allows you to quickly compare the number of mapped fields to make sure they match. If they do not match, an error will display when you attempt to save the Integration Point.

- The field names in the Destination column include the type of each field listed.

- Click the Map Fields button between the Source and Destination columns to automatically map all fields with matching names. If you have Destination fields that are mapped to Fields in the Field Catalog, Relativity tries to find name matches between these Catalog Fields, as well.

If the WebAPIPath instance setting in the kCura.IntegrationPoints section isn't configured correctly after upgrade or installation, the Source field list is empty because it can't return any attributes, and you aren't able to map fields.

You do not need to map all attributes or fields. Only the Unique Identifier and Object Identifier are required. The Unique Identifier should contain a value that no other item in the workspace contains. For example, use the GUID or distinguishedName attribute. The Object Identifier is the specific field on the object that holds the displayed identifier, which might not be unique. For example, the Full Name field is the Object Identifier of the Entity RDO but it might not be unique. These two identifier values can be the same.

- Complete the following Import Settings on the Map Fields layout:

- Overwrite — determines how the system overwrites records once you promote data to the review workspace. This field provides the following choices:

- Append Only —promote only new records into the review workspace.

- Overlay Only —update existing records only in the review workspace. Any documents with the same workspace identifier are overlaid. This field acts as a link indicating to Relativity where to import the data. When you select this or Append/Overlay, you must complete the Multi-Select Field Overlay Behavior field described below.

- Append/Overlay —adds new records to the review workspace and overlays data on existing records. When you select this or Overlay Only, you must complete the Multi-Select Field Overlay Behavior field described below. You are not able to create folders or re-folder documents when you select Append/Overlay.

-

Multi-Select Field Overlay Behavior —determines how the system will overlay records when you push documents to the review workspace. This field is only available if you've selected either Overlay Only or Append/Overlay above. This field provides the following choices:

-

Merge Values —merges all values for multi-choice and multi-object fields in the source data with corresponding multi-choice and multi-option fields in the workspace, regardless of the overlay behavior settings in the environment.

-

Replace Values —replaces all values for multi-choice and multi-object fields in the source data with corresponding multi-choice and multi-option fields in the workspace, regardless of the overlay behavior settings in the environment.

-

Use Field Settings —merges or replaces all values for multi-choice and multi-object fields in the source data with corresponding multi-choice and multi-option fields in the workspace according to the overlay behavior settings in the environment.

- Copy Images —choose to copy, or not copy, images to the destination workspace. Selecting Yes will copy images to your destination workspace. When Yes is selected, an Image Precedence field needs to be completed. Selecting No will not copy images to your destination workspace. When No is selected, a Copy Native Files needs to be completed.

- Image Precedence —select Original Images or Produced Images to copy to the destination workspace.

- Copy Native Files —select Physical Files , Links Only , or No to copy any native files, links to the native files, or nothing while syncing data between the source repository and destination review workspaces.

- Physical files —select to copy any native files from the repository workspace to the review workspace.

- Links only —select to add links to the destination workspace that direct back to the source workspace documents. When choosing this option, be aware that if you delete the native files in the repository workspace or if you delete or archive the repository workspace, the links to the files will be broken in the review workspace. In this situation, if you wanted to maintain the files in the review workspace, you first need to promote the physical files to that workspace before deleting them from the repository workspace or before deleting or archiving the repository workspace.

The Links Only option is enabled for system administrators only by default. Changing the default setting and enabling this option for other users may lead to unauthorized access to another workspace's files.

- No —select to not create additional copies of your natives.

- Doing this maintains a single copy of that data file no matter how many times you use the document in your workspace.

- You have the option of selecting No for an initial run of an integration point and then Yes for a subsequent run. Doing this saves you time on the initial job while then retaining copies of the native files on the final job.

- The benefit of selecting No for this field is that you save on storage and speed, as it tells the system to look for a file path in the source workspace.

- Use Folder Path Information —use a metadata field to build the folder structure for the documents that you promote to the review workspace.

- Select Read From Field or Read From Folder Tree to use a metadata field to build the folder structure for the documents that you promote to the review workspace. Selecting either makes the Folder Path Information field required below.

- Select No if you don't want to build a folder structure based on metadata. In this case, Relativity loads all documents directly into the folder indicated by the promote destination, and you create no new folders in the destination workspace.

- You have the option of creating folders or re-foldering documents when you select Append/Overlay for the Overwrite field.

- You have the option of re-foldering documents for the Overwrite field through the Move Existing Documents field below.

- Folder Path Information —specify a metadata field to build the folder structure for the documents that you promote to the review workspace.

- Move Existing Documents —re-folder documents that were previously imported into the destination workspace, but were only placed in the root case folder and not to any subfolders. This field is useful for situations in which you want to add new data to the destination workspace while overlaying existing data.

- Select Yes to move existing documents into the folders provided in the Folder Path Information field. For example, you previously imported custodian Sally Smith's files into the destination workspace's root folder; now, in addition to placing the documents from the saved search specified in this integration point in their subfolder, you also want to move those previously migrated documents into Sally Smith's subfolder, you'd select Yes.

- Select No if you don’t want to re-folder existing documents.

- Copy Files to Repository —determines whether or not Relativity will copy files from the location in the image load file field to a selected document repository.

- Yes —select this to copy files to a document repository that you select in the File Repository field below.

- No —select this if the native files already reside in their final location, which is accessible by Relativity.

- Click Save to save this integration point with these export settings.

Sync improves the field mapping process by validating fields in both the final step in the wizard. When fields can't be mapped from the Source to the Destination, a pop-up modal displays and states the fields that cannot be mapped.

You can either choose to keep the fields in the Source column or skip them and remove them.

Another solution that Integration Points Sync is providing is automatically remapping fields when the destination workspace is changed. When a user changes the destination workspace in either the integration point or integration point profile, fields can vary between the source and destination workspace. When the destination workspace is changed, the new fields in the workspace are automatically mapped.

The artifacts are mapped based on their names only if the ArtifactIDs are different in the new destination workspace. They are mapped so they the integration points job won't fail. This means that if the source workspace fields can't match to the new destination workspace fields, those unmatched are presented at the end of the mappings list for easy identification. Relativity also informs the user that the original source fields from the profile were mapped with corresponding fields from the destination workspace.

Once they are, a pop-up modal displays "We restored the fields mapping as destination workspace has changed.

Once Relativity saves the integration point, you'll be able to run it and export the data based on the settings you specified. See Running the export job for details.

## Working with promoted documents

To view the documents you promoted to the review workspace, perform the following steps:

- Navigate to the destination workspace.

- Select the Saved Search browser and select the search you created to bring back documents that were promoted from the source workspace.

- Note the following fields on the saved search view:

- Relativity Source Case - the name of the workspace in which you tagged documents for inclusion and exclusion and from which you promoted your tagged documents to the review workspace.

- Relativity Source Job - the name of the Integration Point that you used to promote tagged documents to the review workspace.

You can now review these documents and apply coding decisions for responsiveness and/or issues designation.

### Reusing coding decisions

You can re-use the coding decisions you made on reviewed documents and promote them back into the source workspace through another Integration Point. For example, you could run another promote job to conduct a privilege overlay on documents in the source workspace.

To do this, perform the following steps:

- Select the saved search you created to promote documents back to the source workspace.

- Navigate to the Integration Points tab.

- Create a new integration point that specifies the following values, which differ from those you entered for the promote job you ran previously:

- Destination Workspace —select the original source workspace, specifically the workspace from which you previously promoted documents to the review workspace.

- Saved Search —select the saved search you created to promote documents back to the source workspace.

- Field Mappings —map only Control Number (Object Identifier) and Privilege Designation .

- Overwrite —select Overlay Only .

- Click Run .

On this page

- Promoting data between workspaces through Integration Points

- Special considerations for large sync workflows

- Integration point agent considerations

- Exporting to a Relativity workspace

- Setup

- Connect to Source

- Map Fields

- Working with promoted documents

- Reusing coding decisions


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
