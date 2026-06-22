---
title: "Installing applications"
url: https://help.relativity.com/Server2025/Content/Relativity/Applications/Installing_applications.htm
collection: user
fetched_at: 2026-06-22T06:08:11+00:00
sha256: a9caa75a772b4860013ee8f6160fd2a14b1f7bf4c0cd804d56d858c4473fab31
---

Installing applications

# Installing applications

Relativity provides you with several different options for installing applications. You can:

- Install an application that exists as an external file to the Application Library. The application becomes available for installation to all workspaces. This is useful for when you need to install an individual application .xml file or .rap file to multiple workspaces that Relativity support provided to you. For more information, see Installing an application from an external file to the Application Library .

- Push an application that exists in a single workspace to the Application Library, so the application is available for installation to other workspaces. This is useful for when you install an individual application .xml file or .rap file to a single workspace, and then decide to install the application to other workspaces. For more information, see Pushing an application from a workspace to the Application Library .

- Push an application from the Application Library to one or more workspaces. For more information, see Pushing an application from the Application Library to a workspace .

- Install an application from the Application Library to a workspace. This is the standard route of adding an application after you install or upgrade to a new version of Relativity and have access to the most up-to-date Application Library. For more information, see Installing applications from the Application Library .

- Install an application that does not exist in the Application Library to a workspace as an external file. This is useful for when you need to install an individual application .xml file or .rap file that was not included in a Relativity upgrade or installation to a single workspace. For more information, see Installing an application from an external file to a workspace .

## Installing applications to the Application Library

You can add applications across multiple workspaces by installing them to the Application Library. You can do this by installing applications as external files or pushing them from a single workspace.

### Installing an application from an external file to the Application Library

You need to upload the external file for the application to the Library Application tab. After you add it to the Application Library, you can install the application to workspaces directly from this tab. You can also use the Relativity Application tab to add it to the current workspace. Confirm you have appropriate system admin permissions for application installation. For more information, see Workspace security .

Use the following procedure to install an application to the Application Library:

- Click the Application Library tab.

- Click Upload Application .

- Click Select File on the required Application File field.

- Click Open , and then click Save to upload the file to the Application Library.

The application appears on the list page.

- Click Install in the Workspaces Installed section to install the application on workspaces.

- In the Workspaces Installed list, select Install to All Workspaces or select the workspaces you want to install the application to through the following steps:

- Click Select .

-

In the column on the left, select the workspaces you want to install the application to.

- Use the single arrow between the columns to move the selected workspaces over to the column on the right.

- Click Apply .

- These workspaces now contain the application. Relativity lists the workspaces in the Workspaces Installed section on the detail view of the application.

- Review the installation status of the application in a specific workspace. One of the following statuses appear in the Status column for the workspace:

Application Installation Status Description

Pending... Relativity flags the workspace for installation, but is not installing. To cancel the installation, select the check box next to the workspace name, and then click Cancel .

Errors The install failed due to one or more errors. Click Errors to try to resolve conflicts within Relativity. See Troubleshooting application installation errors .

Application out of date. May not work properly. The version of the application that's installed to this workspace is lower than what's installed to the Application Library. Select the workspace's checkbox, and then click Install to upgrade the application in the workspace.

Installation in progress The application is currently installing to the workspace; you can no longer cancel the installation.

Installed The application installed successfully. Click the Installed link to view the import status details.

### Pushing an application from a workspace to the Application Library

When you want to add any application in a workspace to the Application Library, you can use Push To Library available on the detail view of an application. You can then install the application to workspaces throughout your Relativity environment. In Relativity, confirm that you have the appropriate system admin permissions to install an application. For more information, see Workspace security .

You override any existing applications with the same GUID when you push an application from a workspace to the library.

- Navigate to a workspace where the application you want to add to the Application Library is installed.

- Click the Relativity Applications tab.

- Click the name of the application to display its detail view.

- Click Push To Library in the Relativity Application console.

## Pushing an application from the Application Library to a workspace

To install an application from the Application Library to one or more workspaces, perform the following steps:

See an animated GIF of the installation steps

- Navigate to the Application Library .

- Open the application you wish to install on at least one workspace.

- In the Workspaces Installed list, select Install to All Workspaces or select the workspaces you want to install the application to through the following steps:

- Click Select .

- In the column on the left, select the workspaces you want to install the application to.

- Use the single arrow between the columns to move the selected workspaces over to the column on the right.

- Click Apply .

- Verify that the workspaces show up in the associated list view below with an initial status of Pending installation and then a status of Installed .

Once installation is complete, navigate to any of the workspaces you selected, select the Relativity Applications tab, and verify that the application was installed.

## Installing applications to workspaces

You can install applications to workspaces from the Application Library tab or by importing an external application file.

When you install an application, all components are public regardless of the permissions that you assign to them in your application. The ADS framework ignores any permissions or security assigned to a component added to an application during deployment in a workspace.

This section contains the following information:

- Installing applications from the Application Library

- Installing an application from an external file to a workspace

- Installing applications containing saved searches

- Mapping fields

- Viewing Import status

### Installing applications from the Application Library

If you added the application to the Application Library, you can install it to the current workspace without importing an external file to Relativity. In Relativity, confirm that you have the appropriate system admin permissions to install an application. For more information, see Workspace security .

Use the following procedure to install an application from the Application Library:

- Navigate to a workspace where you want to install the application.

- Click the Workspace Admin tab and the Relativity Applications tab.

- Click New Relativity Application to display an application form.

- Click the Select from Application Library radio button in the Application Type section.

Global applications are not listed in the Select from Application Library option when attempting to add an application to a workspace.

- Click in the Choose from Application Library field.

- Select the application that you want to add to your workspace on the Select Library Application dialog. This dialog displays only applications added to the Application Library.

- Click Ok to display the application in the Choose from Application Library field. The application form also displays the following fields:

- Version —displays the version of the application that you are installing.

- User-friendly URL —displays a user-friendly version of the application's URL. This field may be blank.

- Application Artifacts —displays object types and other application components.

- (Optional) Click Clear to remove the application from the form.

- Map fields if necessary to prevent installation errors. If your application does not contain any fields corresponding to those currently in the workspace, the following message displays. Otherwise, the Map Fields section displays a mapping grid. For more information, see Mapping fields .

- Click Import to save your mappings and import the application.

Relativity installs the application into the workspace.

- Review the import status of the application. Verify that the install was successful or resolve errors. See Viewing import status and Troubleshooting application installation errors .

### Installing an application from an external file to a workspace

You can install an application to the current workspace by importing an external file if the application has not been added to the Application Library tab. Relativity automatically stores shared components the application uses in the Application Library and overwrites any lower versions. Shared components may include event handlers, scripts, custom pages, mass operations, or agents. In Relativity, confirm that you have the appropriate system admin permissions to install an application. For more information, see Workspace security .

You can also use the Application Install API to import an application programmatically. For more information, see Application Install (.NET) on the Server 2025 Developers site.

Use the following procedure to install an application from an external file:

- Navigate to a workspace.

- Click the Relativity Applications tab.

- Click New Relativity Application to display an application form.

- Click Import from File in the Application Type section.

- Click in the File field to browse for the application file.

Relativity Applications use .rap files. If you upload the wrong file type, the following error message appears: The uploaded file is not a valid Relativity Application file .

If the application includes a custom page of a restricted file type, you receive an error message and cannot install the application. See Best practices for custom pages on the Server 2025 Developers site.

- Click Open to upload the file to Relativity. The application form displays the following fields:

- Application Name —displays the name of the application.

- Version —displays the version of the application you're installing.

- File Name —displays the name of the application file. To remove the file from the form, click Clear in this field.

- Expand the tree to view the artifacts associated with your application in the Application Artifacts section. This hierarchy tree includes Object Types, External Tabs, Scripts, Custom Pages, Agent Types, as well as Pre and Post Install Event Handlers contained in your application.

- Map fields if necessary to prevent installation errors. If your application does not contain any fields corresponding to those currently in the workspace, the following message displays. Otherwise, the Map Fields section displays a mapping grid. For more information, see Mapping fields .

- Click Import to save your mappings and import the application. Relativity installs the application into the workspace.

- Review the import status of the application. Verify that the install was successful or resolve errors. See Viewing import status and Troubleshooting application installation errors .

### Installing applications containing saved searches

Relativity applications may contain saved searches that use keyword, dtSearch, and Analytics indexes. When you install the application, Relativity creates the folder structure used to organize the searches in the saved search browser of the workspace. It adds the saved search to the correct folder by matching the globally unique identifier (GUID). If it does not find a match, Relativity continues to traverse the folder structure to the root before creating the required folder. Otherwise, it adds any new or updated saved searches to the existing folder with the matching GUID, even if the user has moved the folder to a new location in the saved search browser. For more information, see Customizing locked applications .

While Relativity 9 and above assigns a GUID to any saved search added to an application, older versions of Relativity do not use GUIDs to identify saved searches. You can build an application using a saved search in a template workspace created before upgrading to Relativity 9 or above. However, deploying your application in a workspace created with this template results in duplicate copies of the saved search. Since Relativity identifies saved searches by GUID, it does not recognize that the legacy search in the workspace is the same as the search in the application, so it creates a new one with the matching GUID.

In general, you install these applications following the same steps used for other applications, but you may want to complete the verification steps before you install them in a workspace. If the workspace does not contain a dtSearch or an Analytics index with the same name as the one included in the application, Relativity creates it using the system defaults. The post-installation steps require you to build the index after Relativity completes this process. For information about building applications with saved searches, see the Creating an application in Relativity on the Server 2025 Developers site.

When you install an application, all saved searches are public regardless of the permissions that you assigned to them in your application or folder structure. The ADS framework ignores any permissions or security assigned to a saved search added to an application during deployment in a workspace.

#### Before you begin

You may want to complete the following verification steps before you install an application containing saved searches using dtSearch and Analytics indexes to avoid possible errors:

- Saved searches using dtSearches —confirm that a file share for this index type exists in your environment. The Relativity installer requires you to create this file share during the installation of the primary SQL Server. For more information, see Relativity installation .

- Saved searches using Analytics indexes —confirm that an Analytics server is installed in your Relativity environment. For more information, see Upgrading or installing your Analytics server .

#### Installation steps

To install the application, follow the instructions in Installing applications from the Application Library or Installing an application from an external file to a workspace .

#### Post-installation steps

If your workspace already contains a dtSearch or Analytics index, Relativity automatically maps it to the saved search using the index name and type. It ignores any spaces or case differences in the index name.

If your workspace does not contain an index with a matching name or type, Relativity creates a shell for a dtSearch or Analytics index. You need to complete one of the following steps to build the index:

- dtSearch index —navigate to the Search Indexes tab in Relativity, and click the Edit link for your dtSearch index. Select settings for the Order , Searchable set , Index share , or other fields as necessary, and save your changes. Next, build the index by using Build Index: Full option on the index details page. For more information, see dtSearch .

- Analytics index —navigate to the Search Indexes tab in Relativity, and click the Edit link for your Analytics index. Select settings for Analytics profile , Analytics server , Data source , Training data source , and fields as necessary. Next, build the index. For more information, see Analytics indexes .

### Mapping fields

When you import an application, you can optionally map the fields that are similar to those in an application currently installed on the workspace. You can use mapping to avoid having multiple copies of a field that stores similar information in your workspace.

For example, you might import a new application that contains a long text field on a Document object called Email Cc , but your workspace already contains another application with a similar field on the Document object called Email Cc Addresses . Instead of two fields storing similar information, you might want all applications to use the same field for this metadata. By mapping these fields, you can avoid renaming the new field and using two different fields to store this metadata in your workspace.

Use these guidelines when mapping an application to workspace fields:

- Fixed length text fields —you can map application fields of this type only to workspace fields of equal or lesser length. Workspace fixed text fields that have a length longer than the application fields are not displayed in the Workspace Fields column of the mapping interface.

- Renaming fields —you can rename a field after you map it without impacting future application upgrades.

- Renaming fields and exporting —if you rename a field in an application installed on Workspace A, and then export the application, this field is still renamed when you import the application to Workspace B. This practice does not apply to Document System Fields.

- Target workspace fields renamed —when you map an application field to a workspace field, the application renames the workspace field to match the application field. The application now owns the field.

- Handling of removed components —if you remove a component from an application installed in Workspace A, and the export the application, this component is still part of the application when you import it to Workspace B. In other words, the component that you removed from Workspace A imports to Workspace B. Application components include choices, fields, object rules, and others.

Use the following procedure to map application fields to workspace fields:

- Complete the steps for installing an application described in the previous sections.

-

Locate the Map Fields section on the application form. The Map Fields section displays the mapping interface if the application contains fields corresponding to those in the workspace.

- Complete these steps to map the available application fields of your choice through the Field Mapping interface:

- Highlight a field in the Application Fields box, and then click the arrow to move it to the center box. The Workspace Fields box displays the fields in the target workspace that may match the application field. The Workspace Fields box does not display any fields when no matches exist.

-

Highlight a field in the Workspace Fields box, and then click the left arrow to move it to the center box.

You can also double-click a field name to move it to a mapping box. To remove a field from the mapping box, use the left arrow for the application fields, and right arrow for the workspace fields.

### Including fields in text index

Including imported fields in text index requires the index to be rebuilt and can impact Relativity performance. By default, the fields imported with Relativity applications are not included in text index even if the Include In Text Index property is set to Yes. You can use the UpdateIncludeInTextIndexOnRapImport instance setting to override this behavior and use the value of Include In Text Index from the application.

The UpdateIncludeInTextIndexOnRapImport must be used only when existing fields conflict with imported application fields, and by default existing field settings take precedence.

### Viewing import status

After you install an application through the Relativity Application tab, you can view the status page, which appears immediately after this process completes. The Import Status section indicates whether your installation was successful.

The Artifact Name section displays a list of all the artifacts in your application, which includes its Artifact Type, Artifact ID, and installation status. For artifacts installed without errors, the Status column displays the message Updated successfully .

For unsuccessful installations, the Import Status section indicates that your application installation failed as illustrated in the following message. The message lists the number of errors encountered during the installation. In addition, the Status column describes each error that occurred during a failed installation. For more information, see Troubleshooting application installation errors .

To export the Status section report to a .csv file, you can click the Export Status Details . You can also view status information for the installation of an application from the Application Library tab. Click on an application to display a detail view, and then click its Installed link to display the status page.
