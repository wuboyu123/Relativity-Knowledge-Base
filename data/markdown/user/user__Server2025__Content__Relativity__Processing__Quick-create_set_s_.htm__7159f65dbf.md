---
title: "Quick-create set(s)"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Quick-create_set_s_.htm
collection: user
fetched_at: 2026-06-22T06:13:31+00:00
sha256: 9b3132893450260ac35ad23909cdbf9ab4e94929715b15611128f674bed3a142
---

Quick-create set(s)

# Quick-create set(s)

With the quick-create set(s) feature, you can streamline the creation of data sources, custodians, and processing sets based on a specific file structure or PST from a single object. For example, if you need to create 73 data sources with a single custodian per data source, quick-create set(s) eliminates the need for you to do so on an individual basis.

You can also elect to create a single or multiple processing sets based on those custodians and data sources and specify what action you want Relativity to take, such as starting inventory or discovery, for each processing set created.

Read if you're studying for the Processing Specialist exam The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

## Required security permissions

In addition to the permissions required to use Processing, you need the following permissions enabled in the Workspace Security console in order to use quick-create set(s).

- The Quick-Create Set(s) entry checked in the Tab Visibility section.

- The Edit permission on the corresponding Quick-Create Set(s) entry in the Object Security section.

## Using quick-create set(s)

To use quick-create set(s), perform the following steps:

- Navigate to the Processing Sets sub-tab, click the New Processing Set drop-down menu, and select the Quick-Create Set(s) option.

- Complete the following fields on the Quick-Create Set(s) layout:

- Name - enter the name you want to appear on the processing set(s) created by this quick-create set. If you're creating a single processing set, it will display only the name you enter here. If you're creating multiple sets, they will display the name you enter here appended with - <Custodian Name> . The following are examples of processing set names:

- Processing Set A - Doe, John

- Processing Set A - Jones, Dan

- Processing Profile - select the profile you'd like to use to create the processing sets or click Add to create a new profile. These options are the same as you'd find in the Processing Profile field on the Processing Set layout. The Default, Fast Processing Profile, and Standard Processing Profile are available by default.

- Action on Save - select what you'd like to occur when you save this quick-create instance. The options are:

- Create processing set(s) - creates the processing set without starting an inventory or discovery job. This means you'll navigate to the processing set layout and manually start inventory or discovery.

- Create processing set(s) and inventory files - creates the processing set and automatically starts the inventory job, which you can monitor on the processing set layout. Once inventory is complete, you can then manually start the discovery job.

- Create processing set(s) and discover files - creates the processing set and starts a discovery job without first running inventory on the set.

- Number of Processing Sets - determine the number of processing sets you wish to create through this quick-create instance. The options are:

- Create single processing set - creates a single processing set.

- Create processing set per data source - creates a processing set for every data source you selected for the source path field.

- Entity Type - select either Person or Other .

- Person - Relativity matches the FirstName and LastName fields, including the Delimiter value entered and the Naming Convention selected. The matching process excludes the FullName field.

- Other - Relativity matches the folder selected as the Source Path to the FullName field of the Entity object. The matching process excludes the FirstName, LastName, Delimeter, and Naming Convention values.

- Naming Convention - select the naming convention you like to use for the custodians in the folder structure. This field is only available if you selected Person as the custodian type above. The options are:

- <Last Name><delimiter><First Name> - specifies that the folder names are formatted to contain the custodians last name, followed by the delimiter entered above, followed by the custodian's first name.

- <First Name><delimiter><Last Name> - specifies that the folder names are formatted to contain the custodians first name, followed by the delimiter entered above, followed by the custodian's last name.

- Delimiter - enter the character you'd like to act as the delimiter between custodians in the folder structure. This field is only available if you selected Person as the custodian type above. If you enter something different than the delimiter contained in the folder path you selected for the Source Path field, you will encounter an error when you attempt to save. The following are examples of delimiters you could enter here:

- - (hyphen)

- . (period)

- _(underscore)

- Relativity treats a delimiter of <> as a space.

- Source path - the location of the data you want to process. Click the ellipsis to see the list of folders. The source path you select determines the folder tree below, and the folder tree displays an icon for each folder within the source path. You can specify source paths in the resource pool under the Processing Source Location object. Each folder you select here will act as a data source on the Processing Set.

You can select up to 100 folders.

Each data source will have a corresponding Custodian, with the folder name serving as the Custodian name. Click OK after you select the desired folders; ensure that the folder corresponds to the person or entity you select for the Entity Type field described below.

- You can select any single folder by clicking on it once. Clicking it again clears that selection.

- When you right-click a folder, you see the following options:

'

- Expand - expands all the sub-folders under the folder you've right-clicked.

- Collapse all - collapses all the expanded folders under the folder you've right-clicked.

- Set Children as Entities - marks the folder's children as custodians. When you select this option, each child folder is marked as [Selected] in the folder tree. These folder names then appear as data sources in the Preview window in the Quick-Create Set(s) layout. They also show up as data sources on the processing set layout once you save the quick set.

- Clear - clears any selections you made.

- Email notification recipients - enter the email addresses of those who should receive notifications of whether the processing set creation succeeded or failed. Use semi colons between addresses.

- (Optional) View the number of data sources you're about to create in the Preview window. If this window is empty, it's most likely a sign that you've selected an invalid source path and/or that you've entered an invalid delimiter; in this case, you'll most likely receive an error when you click Save and Create.

- Click Save and Create .

- If your Action on Save selection above was to either inventory or discover files, then you must click Discover or Inventory on the subsequent confirmation message to proceed with saving the quick-create instance.

Once you save and create the quick-create instance, the layout displays a success message and directs you to the Processing Sets tab.

### Validations and errors

Note the following details about validations and errors:

- Relativity performs the same validations for quick-create set creation as it does for processing profile and set creation. This means that, for example, if the queue manager happens to go down while you're creating the quick -create instance, you'll see an error message at the top of layout and you won't be able to save and create it.

- If the quick-create instance fails to create a set, custodian, or data source, the resulting error will go to the Errors tab in Home, and if the error occurs after the creation of any of those objects, it will be considered a processing error and will go to either the Document Errors or Job Errors tab in the processing object.

- If your entity type is set to Person, Relativity validates that the names of the selected folders adhere to the selected delimiter and naming convention values.

- If you enter , (comma) as your delimiter, and you have one or more folder names that don't contain a comma, you will receive an invalid source path error after clicking Save and Create. In this case, the Preview window would also not list any entity names.
