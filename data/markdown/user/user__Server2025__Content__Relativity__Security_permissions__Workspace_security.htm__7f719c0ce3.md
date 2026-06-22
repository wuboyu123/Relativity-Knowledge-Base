---
title: "Workspace security"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Workspace_security.htm
collection: user
fetched_at: 2026-06-22T06:07:13+00:00
sha256: 67e5c9dd6e67b160f48667ebaf943d4f96738eadabe7162ee786d4cbb7205225
---

Workspace security

# Workspace security

Relativity’s security rights are highly customizable. Each group you add to a workspace can have vastly different permissions than others. You can also copy an existing group’s permissions to save time on configuring them.

You set group permissions when adding a group to workspace, but you can change these permissions at any time from the Workspace Details page.

If you assign admin permissions to a user group by copying permissions from system admins, you must unset and reset the View Workspace permission to allow the user group to edit the workspace.

## Workspace permissions

Relativity divides workspace permissions into five categories:

- Object security

- Tab visibility

- Browsers

- Mass operations

- Admin operations

### Object security

The Object Security tab lists all workspace objects with their related item-level permissions. Item-level rights include:

- None —denies users access to the object.

- View —view the object. This is the lowest level object permission.

- Edit —edit and view the object.

- Delete —delete, edit, and view the object.

- Add —add new objects. This icon turns blue when the setting is unsaved; once you click Save, the blue icon becomes grey. This icon turns green when you give users this permission both when the setting is unsaved and saved.

- Edit Security —grants users the ability to edit the security of objects. This icon turns blue if you click twice indicating a not applicable status.

Not all item-level rights apply to select objects. Some object permissions require corresponding tab visibility or browser permission. For example, a group with all item-level rights assigned for the Field object can only add, edit, delete, or edit security for fields with access to the Fields tab.

Item-level security permissions override Object-level security permissions.

Once a workspace is created, only System Administrators and Client Domain Administrators can make updates to the Matter object. Even users with full permissions for Matters and Clients will not have the ability to modify this object unless they are System Administrators or Client Domain Administrators.

### Object list

The following is a list of common securable objects in a Relativity workspace. Objects with sub-options, related tab visibility permissions, or specific effective rights state the related requirements and rights.

This list contains objects related to core functionality, and additional objects may be described in the documentation for individual features. This list also does not include custom objects you may find in your environment.

- Active Learning —technology assisted review tool that helps you quickly organize your data and predict which documents are most likely to be relevant to reviewers. For more information, see Active Learning Security permissions .

- Agent Type —a category of agent. Agents manage processes in Relativity and run in the background to complete jobs that you or another user scheduled in your environment.

- Alias —a textual representation of an author. Aliases are identified during the Analytics name normalization operation.

- Analytics Categorization Result —an object that displays the results of an Analytics Categorization Set.

- Analytics Categorization Set —a group of parameters used for gathering example documents that Analytics uses as the basis for identifying and grouping other conceptually-similar documents.

- Viewing, editing, deleting, or adding Analytics categorization sets, or editing security of Analytics categorization sets requires access to the Analytics Categorization Set tab.

- Analytics Category —an object in Analytics that define the categories specific to your analytics set.

- Viewing, editing, deleting, or adding Analytics categories for Analytics categorization sets, or editing security of Analytics categories requires access to the Analytics Categorization Set tab.

- Analytics Example —a document that Analytics uses to run the Analytics Set against to set a baseline.

- Analytics Index

- Search index permissions must be kept in sync with permissions on the Analytics Index object.

If a user has view permissions to Search Index, but no permissions to Analytics Index, they can still access Index Search functionality in the item list and in the viewer. If a user has full View/Edit/Add/Delete security permissions to an Analytics Index, but does not have permissions for Search Index, they will not be able to View/Edit/Add/Delete Analytics indexes.

- Analytics Profile —a group of parameters used for specifying an Analytics Index's dimensions, concept noise words, dtSearch noise words, and filter configurations.

- Editing, deleting, or adding Analytics profiles, or editing security of Analytics profiles requires access to the Analytics Profiles tab.

- Batch —a group of documents assembled based on criteria that an admin sets and then assigns to a reviewer for review.

- Edit—group members can view, check out, and edit batches.

- Delete—group members can view, edit, and delete batches.

- Viewing and checking out, editing, available batches requires access to the Review Batches or Batch Sets tab.

- Adding batches requires access to the Batch Sets tab.

- Editing security on batches requires access to the Review Batches or Batch Sets tab.

- Batch Set —the set to which the batch belongs.

- Using any Batch Set permissions requires access to the Batch Sets tab.

- Choice —a value applied to a single or multi-choice list field that is used in coding fields to allow reviewers to record decisions on a document.

- Editing, deleting, or adding choices, or editing the security for choices requires access to the Choices tab.

- Cluster Set (Relativity 9.5.196.102 and above)

- Permissions for Cluster Set and the multiple choice fields that hold cluster data should be kept in sync.

If a group has the None permission set on the Cluster Set object, but View/Edit/Add/Delete permissions to the Multiple Choice fields that hold cluster data, users in that group will still see Analytics clusters in the cluster browser and will be able to visualize clusters. To prevent the group from viewing the clusters in the cluster browser, or visualizing clusters, you must item-level secure the multiple choice fields that hold the cluster data for the group.

- Color Map

- Email Thread Visualization requires View permissions or higher for the Color Map object.

- Custom Page —a custom web page created that enhances the flexibility of application development by supporting the creation of custom layouts and the display of dynamic content, such as unique graphics, dynamic date, and report results.

- Dashboard —a page configuration made up of widgets and item lists.

- Destination Workspace —the Destination Workspaces tab in the Integration Points object, which provides information on the workspaces to which users have exported data through Integration Points. Note that this setting has no impact on the Destination Workspace field on the Connect to Source layout of the Integration Point you are creating or editing; this means that you can still select a workspace from that field drop-down list even if you do not have permission to this object.

- Document —a record within a workspace.

- Upload Image —group members can use the image upload functionality in the viewer to upload a single image.

- Replace Document —group members can replace a single document in the viewer.

- Create PDF —group members can print and save as PDF individual documents from Relativity.

- Local Access (Download; Copy Text)—group members can open the file in its native application or to copy text from the viewer.

- Redact Document —group members can place stamp or text box redactions on a document.

- Highlight Document —group members can place a highlight on a document.

- Add Image —group members can use Relativity’s image-on-the-fly functionality.

- Delete Image —group members can delete images in Relativity.

- New Document —group members can upload a new document.

- Case Dynamics - Coding Pane —group members can use the Case Dynamics coding pane.

Use the document Edit permission to tag documents with workspace coding values using layouts. Do not assign coding users rights to edit fields or edit layouts. Use the Field edit permission, along with access to the Fields tab, to edit field properties such as changing a fixed length text field from 255 to 320 characters.

- Domain —the name of the business or organization on the internet. For example, “@company.com” in the email address “jsmith@company.com” is the domain for that company email address.

- Entity —the individuals or entities who own or facilitate the data found in the data sources.

- Group members can view, add, edit, and delete the entities used for Relativity Processing, Legal Hold, and Collect, and Analytics.

- Event Handler —the name of the assembly that helps facilitate the completion of document review and various other functions in Relativity by applying custom business logic to corresponding user actions.

- Field —the Relativity entity used to store document metadata and coding values within Relativity.

- Add Field Choice By Link —exposes the Manage link option on choice fields, allowing group members to add new choices to a field on a layout.

- Editing, deleting, sorting, or adding fields, or editing the security of fields requires access to the Fields tab.

- Folder —the name of the container of documents in Relativity that are arranged in a hierarchy in the folder browser.

- Using any Folder permissions requires access to the Folder browser.

You can customize permissions for individual child folders. This does not change the permissions of a folder's parent, but it can change the behavior of a folder's children, if you configure the children folders to inherit permissions from their parent.

Changing root folder permissions during import is not a supported workflow.

- Job History —the Job History tab in the Integration Points object, which provides information the history of import and export jobs run through Integration Points.

- Job History Error —the Job History Errors tab in the Integration Points object, which provides information errors that occurred during import and export jobs run through Integration Points.

- Imaging Profile —the name of the profile that controls the settings used to image a group of documents.

- Editing, deleting, or adding imaging profiles, or editing security of imaging profiles requires access to the Imaging Profiles tab.

- Imaging Set —the profile and saved search containing the documents you want to image.

- Editing, deleting, or adding imaging sets, or editing security of imaging sets requires access to the Imaging Sets tab.

- Install Event Handler —the name of the pre or post install event handler, which is an assembly that runs when you install them to configure your Relativity environment to support your applications.

- Viewing, adding, or deleting event handlers requires access to the Object Type tab.

- Inventory Filter —the filter applied when inventorying files to view how inventories data affects data in your processing set using the Processing application.

- Integration Point — the entity that you create to configure data integrations from third-party systems to Relativity objects using the Integration Points application.

- Integration Point Profile —the profile that you create and save for future use when running future data import or export jobs through the Integration Points application.

- Integration Point Type —the integration point type, import or export, that you specify when you create an integration point to configure data integrations from third-party systems to Relativity objects using the Integration Points application.

- Layout —the name of the web-based coding form that gives reviewers access to view and edit document fields and complete specific review tasks.

- Editing, deleting, or adding layouts, or editing security of layouts requires access to the Layouts tab.

- Lists —an option for saving a group of items without having to specify the types of conditions required for a saved search, which means they remain constant unless someone replaces them with an existing list.

- Editing, deleting, or adding lists, or editing security of lists requires access to the Lists tab.

- Markup Set —a securable sets of annotations and redactions available to reviewers for applying text redactions to documents in the viewer.

- Editing, deleting, or adding lists, or editing security of markup sets requires access to the Markup Sets tab.

The only proper way to secure the text behind a redaction is to the produce the document that contains the redacted text. If a group has View rights only to a markup set, not Edit or Delete rights, and a reviewer in that group loads a document in the Viewer because they have no other way to view that document, they can actually see the text behind the redaction, in which case that text is not totally secured.

- Mass Operation —single actions performed on multiple documents or objects at the same time, such as mass edit, move delete, produce, replace, image, print image, send to CaseMap export file, cluster, and process transcripts.

- Viewing, adding, or deleting mass operations requires access to the Object Type tab.

- Native Type —a Relativity-supported file type that an admin can import and image; Native Type pertains to the Native Types tab and list, which an admin references when selecting file types to restrict from imaging.

- Edit —group members to edit the Restricted From Imaging By Default checkbox for native types.

- Delete —group members to remove native types from the restricted list.

- Add —group members to add existing native types to the restricted list.

Even with all Native Type permissions assigned, a user cannot add new native file types. Relativity is already configured with the native file types that it recognizes. For more information, see Restricted native types .

- Object Rule —permits special or additional functions with user-configurable options. For example, a New Button Override that redirects an object's New button action to another Relativity page or other URL as directed by the user.

- Viewing, adding, or deleting object rules requires access to the Object Type tab.

- Object Type —the type of object specified when creating a Relativity Dynamic Object. For example, Document and Workspace are object types.

- Editing, deleting, or adding object types, or editing security of object types requires access to the Object Type tab.

- OCR Language —determines what language is used to OCR files where text extraction is not possible, such as for image files containing text.

- Viewing, editing, deleting, or adding OCR languages, or editing security of OCR languages requires access to the Processing tab.

- OCR Profile —a saved, reusable set of parameters that you use when creating an OCR set.

- Viewing, editing, deleting, or adding OCR profiles, or editing security of OCR profiles requires access to the OCR Profiles tab.

- OCR Set —a group of documents defined by a saved search or production to be OCRed based on the settings defined by the OCR profile.

- Viewing, editing, deleting, or adding OCR sets, or editing security of OCR sets requires access to the OCR Sets tab.

- Password Bank —a password repository used to decrypt certain password-protected files during inventory, discovery, and native imaging.

- Password Entry —a password you enter into the password bank to decrypt password-protected files.

- Viewing, editing, deleting, or adding password entries in the Password Bank, or editing security of password entries requires access to the Password Bank tab.

- Persistent Highlight Set —a reusable, transferable set of persistent highlight specifications a reviewer can select in the Viewer to assist in document review.

- Pivot Profile —a saved, reusable group of pivot setting that you apply to pivots to quickly analyze case data.

- Quick Create Sets —the Quick Create Sets tab, formerly Processing Assistant, lets you create multiple data sources, entities, and processing sets based on a specific file structure from a single object.

- Processing Data Source —all data sources associated with all processing sets in the workspace.

- Processing Error —a list of errors related to your processing job.

- Download and Upload files with processing sets —group members can download error files and upload replacements for them through the Error Actions console on the error details layout.

- Processing Set —an object to which you attach a processing profile and at least one data source and then use as the basis for a processing job.

- Production —an application that prepares relevant and non-privileged documents to turn over to opposing counsel after review.

- Viewing, editing, deleting, or adding production sets, or editing security of production sets requires access to the Production Sets tab.

Productions appear in the viewer by default. There are no permissions for specific viewer options. To restrict productions from appearing in the viewer for a certain group, set the Production permission to None .

- Production Data Source —saved set of parameters that Relativity uses when running a production.

- Production Information —information records associated with a production during the Staging process of running a production.

- Production Placeholder —text or images you can include in a production as a placeholder for removed or forthcoming information.

-

Queue Refresh Trigger —a mechanism within Relativity's Review Center that initiates a process to update the review queue with the latest information.

- Relativity Application —a customizable collection of Relativity objects that provides improved case and matter management.

- Viewing, editing, deleting, or adding Relativity applications , or editing security of applications requires access to the Relativity Applications tab.

- Relativity Script —a SQL-based command that admins can use to customize and augment Relativity functionality. Scripts are deployed with Relativity and reside in the Relativity script library.

- Viewing, editing, deleting, or adding Relativity scripts, or editing security of scripts requires access to the Scripts tab.

- Relativity Time Zone —the Time Zone for which the Relativity environment adheres to.

- Repeated Content Filter —a filter that finds the text in each document that matches your configuration parameters and suppresses it from the Analytics index.

- Viewing, editing, deleting, or adding repeated content filters, or editing security of repeated content filters requires access to the Repeated Content Filters tab.

- Report —flexible reporting features designed to facilitate roll-ups of information about your case review.

- Viewing, editing, deleting, or adding summary reports, or editing security of summary reports requires access to the Summary Reports tab.

- Review Center Queue —a collection of documents within Relativity's Review Center functionality that serve as a central location for reviewers to access and analyze documents relevant to a specific case or investigation.

- Search —flexible search features designed to facilitate document review process.

- Security settings for the Search object apply to saved searches.

- Editing, deleting, or adding saved searches, or editing security of saved searches requires access to the Saved Searches browser.

- Search Container —the search folder object, which applies to all saved search folders.

- Security settings for the Search Folder object apply to saved search folders.

- Editing, deleting, or adding saved search folders, or editing security of saved search folders requires access to the Saved Searches browser.

- Search Index —access to searching features, such as dtSearch and other searches available from the Documents tab.

- Search index permissions must be kept in sync with permissions on the Analytics Index object.

If a user has view permissions to Search Index, but no permissions to Analytics Index, they can still access Index Search functionality in the item list and in the viewer. If a user has full View/Edit/Add/Delete security permissions to an Analytics Index, but does not have permissions for Search Index, they will not be able to View/Edit/Add/Delete Analytics indexes.

- Dictionary Access —group member can see the dictionary function when searching with a dtSearch index.

- Using available search indexes with dictionary search requires access to the Documents tab.

- Selecting and using available search indexes requires access to the Documents tab.

- Editing, deleting, or adding search indexes, or editing security of search indexes requires access to the Search Indexes tab.

- Search Terms Report —a tool an admin can use to enter a list of terms or phrases and generate a report listing those words’ frequencies in a set of documents.

- Viewing, editing, deleting, or adding search terms reports, or editing security of search terms reports requires access to the Search Terms Reports tab.

- Search Terms Result —a list of results from the search terms report.

- Source Provider —group members can see all available source providers when creating an integration point; for example LDAP, FTP, Import Load file, and Relativity.

- Structured Analytics Errors —a list of errors related to your Structured Analytics job.

- Structured Analytics Set —a saved, reusable group of settings that Structured Analytics uses to shorten your review time, improve coding consistency, optimize batch set creation, and improve your Analytics indexes.

- Tab —an interface component that gives the admin or reviewer access to an assortment of Relativity functionality.

- Editing, deleting, or adding tabs, or editing security of tabs requires access to the Tabs tab.

- Transform —access to the transform functionality in Relativity.

- Viewing, editing, deleting, or adding transforms, or editing security of transforms requires access to the Transform Sets tab.

- Transform Set —a feature that uses handlers to analyze and extract the contents of one field and copy them to another.

- Viewing, editing, deleting, or adding transform sets, or editing security of transform sets requires access to the Transform Sets tab.

- View —a customizable list of items in Relativity from which a user can sort and filter to locate specific items.

- Editing, deleting, or adding views, or editing security of views requires access to the Views tab.

- Workspace —a securable document repository used to facilitate productions, witness testimony, and other documents in which admins and reviewers conduct searches for relevant materials and set up views to organize that material.

- Editing or deleting a workspace, or editing security of a workspace requires access to the Workspace Details tab. When the edit security permission is selected, it grants the group the ability to manage permission and the Add/Remove Groups button will display.

### Tab visibility

Tab Visibility lists all parent and child tabs to which you can grant groups access. Combine object security permissions and tab visibility access to give users the tools they need to complete their tasks. Select a tab to make it visible for a group.

The following is a list of common Relativity parent and child tabs in alphabetical order by parent tab name:

- Case Admin

- Batch Sets

- Markup Sets

- Persistent Highlight Sets

- Production Sets

- Scripts

- Transform Sets

- Case Metrics

- Reports

- Reviewer Metrics

- Dashboard

- Documents

-

Entities

- Entities

- Aliases

- Indexing & Analytics

- Structured Analytics Set

- Analytics Profiles

- Repeated Content Filters

- Search Indexes

- Analytics Categorization Set

- Imaging

- Imaging Profiles

- Imaging Sets

- Native Types

- Password Bank

- Lists

- OCR

- OCR Profiles

- OCR Sets

- Processing

- Processing Sets

- Quick Create Sets

- Processing Data Sources

- Processing Profile

- Password Bank

- Inventory

- Errors

- Reports

- Job Errors

- Document Errors

- Processing Administration

- Worker Monitoring

- Processing History

- Reporting

- Search Terms Reports

- Summary Reports

- Pivot Profiles

- Domain

- Search Terms Results

- Review Batches

- Workspace Admin

- Workspace Details

If a user has view access or greater, such as edit, delete rights, to the workspace object and has view access to the Workspace Details tab, but does not have permission to View Workspace Details, the admin operation, the user cannot view the Workspace Details tab.

- Search Indexes

- Object Type

- Fields

- Choices

- Layouts

- Views

- Tabs

- Relativity Applications

- Custom Pages

- History

If a user has view access or greater to the History tab, but does not have permission to View All Audits , the user cannot view the History tab.

- User Status

- Worker Status

This list does not reflect custom tabs or customized parent tab configurations that may vary by environment.

### Browsers

In the Browsers section, you control which browsers are visible to a group. Select a browser type to make it visible for the group.

The following is a list of Relativity browsers:

- Folders

For more information on securing folders, see Relativity object security .

- Field Tree

- Advanced & Saved Searches

- Clusters

See the Browser panel section for complete details regarding each browser type.

Groups not granted access to any of the available browsers in a workspace see their document list spanning the whole screen.

### Mass operations

In the Mass Operations section, you control which types of mass action rights the group can access. This section also lists any custom mass operations that you have added to Relativity or that are available in applications currently installed in your environment.

Select the check mark next to the mass action you want group members to have access to.

You can select the following mass actions:

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

For more information about mass operations, see Mass operations .

### Admin operations

You can secure several admin operations separately. To assign permissions to a group, select check boxes for any combination of these operations.

The options available in the Admin Operations section include:

- Allow dtSearch Index Swap —grants group members the ability to execute the Index Swap function from the dtSearch console. For more information, see dtSearch.

- Allow Export —grants group members the ability to export files using the Relativity Desktop Client and the export functionality found in Integration Points.

- Allow Import —grants group members the ability to import load files using the Relativity Desktop Client and the import functionality found in Integration Points.

- Assign Batches —grants group members permissions to check out batches to other reviewers.

- Communication Analysis Widget —grants group members permission to add the Communication Analysis widget to a dashboard via the Add Widget drop-down menu.

Groups without this permission can still view and interact with the Communication Analysis widget assuming they have access to the dashboard the widget is part of.

- Delete Object Dependencies —grants group members permission to force the deletion of an object, which includes unlinking associative objects and deleting child objects. The group members must also have permissions to delete any dependent child or modify associated objects.

- Download Relativity Desktop Client —grants group members permission to the Download Relativity Desktop Client 32-bit and Download Relativity Desktop Client 64-bit buttons. These buttons are located in the Relativity Utilities console on the Workspace Details page. See Using the utilities console .

- Email Thread Visualization —grants group members permissions to access email thread visualization.

- Export Dashboard —grants group members permission to download a saved dashboard.

- Manage Object Types —permission that grants group members the ability to:

-

Create a new tab for a new object type when adding the new object type.

-

Automatically gain view, add, edit, delete, and secure permissions for all newly created object types.

-

Automatically gain tab visibility for newly created tabs.

- Manage Relativity Applications —group members can associate objects with applications by making the Relativity Applications field available on create and edit pages for Field, Layout, View, Script, Object Types, and all other objects compatible with applications. Users with this and Edit permissions for applications are allowed to lock and unlock an application from editing.

- Modify System Keyboard Shortcuts —grants group members permission to the Manage System Keyboard Shortcuts button. User groups must also have permissions to see the Workspace Admin and Workspace Details tab along with the View Workspace Details permissions. This button is located in the Relativity Utilities console on the Workspace Details page. See Keyboard shortcuts

If a user group is given this permission they can modify and delete keyboard shortcuts for their group within a workspace.

- Override Production Restrictions —grants group members permissions to override the setting in the Production Restrictions option on the Workspace Details page. The group members will be able to produce documents that contain conflicts based on these restrictions. See Adding and editing production restrictions .

- Use Pivot/Chart —grants group members permissions to use the Pivot grid and chart functions.

- Use Quick Nav —grants group members the ability to search tabs in a workspace using the quick navigation feature. See Quick nav .

- Use Sampling —grants group members permission to the sampling menu on any object that has the Sampling field set to Enabled. The sampling menu users can create sample sets of items using a sampling methodology of their choice. For example, a user can make a sample set of documents to review for QC purposes. For more information, see Sampling .

- View All Audits —grants group members permission to view the history of a document in the Viewer through the Document History icon, as well as workspace objects, such as markup sets, Dynamic Objects, fields, etc., through the View Audit option on those objects’ layouts.

If a user has view access or greater to the History tab , but doesn't have permission to View All Audits, the user can't view the History tab.

- View Batch Pane —grants group members permission to view the batches associated with a document in the related items pane.

- View Images Hidden for QC Review —grants group members permission to view all images in an imaging set with a QC status set to hide images. For more information, see QC Review .

- View User Status —grants group members permissions to access the User Status tab.

- View User's Personal Items —grants group members permission to click the View Another User's Personal Items link on the Workspace Details page and modify the View Other's Personal Items console.

- View Workspace Details —grants group members permissions to access the Workspace Details page and the Relativity Utilities console.

If a user has view access or greater to the Workspace Details tab , but doesn't have permission to View Workspace Details, the user cannot view the Workspace Details tab.

If you are using RelativityOne, the following admin operations are secured by default and should not be modified. Please contact Relativity Support if you think you need to access this functionality.

- Download RelativityDesktop Client —grants group members permission to the Download RelativityDesktop Client 32-bit and Download RelativityDesktop Client 64-bit buttons. These buttons are located in the Relativity Utilities console on the Workspace Details page. See Using the utilities console .

## Workspace admin group

A system admin can assign any group in Relativity to have full admin rights over a particular workspace. A workspace admin has full control over all objects within the workspace, but members of the group do not have the script permissions available only to system admins.

Use the following steps to set a designate a workspace admin group:

- Click Edit on the Workspace Details tab.

- Click in the Workspace Admin Group field.

- Click the radio button next to the group you want to set as the workspace admin group.

- Click Ok .

You can only designate one group per workspace as a workspace admin group.

Being in a workspace’s Admin Group alone does not permit a user to be assigned review batches. The user must also belong to at least one other group in that workspace (not the System Administrators group or the Workspace Admin group) that has access to the workspace and the View Batches permission. In other words, a Workspace Administrator with no additional group memberships will not appear as an available reviewer for batch check-out.

You can also grant workspace admins permission to alter the security settings of any group.

To grant workspace admins permission to alter the security settings of any group:

- Click Manage Workspace Permissions from the Workspace Details tab.

The Workspace Security window opens.

- Select Object Security .

- Select the desired group from the Select a Group drop-down menu.

- Click the Edit Security padlock for the Workspace object permission.

- Click Save .

## Features in workspaces available only to system admins

System admins are the only users capable of performing the following operations:

- Script Details

- Edit Permissions

- View Audit button

- Preview Script option

- New Script page

- Script Body Editor

- Create New Workspace script

- Relativity Applications select box link

- Select from Script Library radio buttons

- Edit Script page

- Script Body Editor

- New Library Application

- Import from file radio button

- Select from Library radio button
