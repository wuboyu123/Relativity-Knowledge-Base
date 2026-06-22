---
title: "Create an application in Relativity"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Creating_an_application_in_Relativity.htm
collection: developer
fetched_at: 2026-06-22T06:30:54+00:00
sha256: 41da317a14e14b39a4b5cd4e6cca320bff613032ce19fe03b32bcee610490874
---

Create an application in Relativity

# Create an application in Relativity

A Relativity application consists of objects used alone or in conjunction with each other to store and manage information other than document metadata. You can add these customizable and securable objects to workspaces as you build an application. Using the Application Deployment System (ADS), you can package components added to your custom application. You can now easily deploy it to other workspaces or Relativity instances.

In the Relativity UI, you can create Relativity Dynamic Objects (RDOs), views, layouts, choices, tabs, and fields for inclusion in your application. You can also provide advanced functionality in your application by uploading custom code for event handlers, mass operations, and other features to Relativity. After you complete these steps, you can create an application, and then add these components and your custom code to it.

You can build different types of applications using the ADS. For example, you could build an application to structure evidence for a review. You could also build an application to manage a business workflow. It might reside in a workspace created specifically for system admins, so that they can manage their daily administrative tasks.

## Create an application

You can create Relativity applications to perform specialized functions in a workspace. After you create an application, you can customize it by adding new objects to your application or linking to existing ones. See Add components to an application .

To create an application, you need the following permissions:

- Add rights to the Relativity Application object on the Object security tab.

- View rights to the Relativity Applications tab in the Tab visibility list.

For more information, see Workspace security on the Relativity Documentation site.

Use these steps to create an application:

- Open a workspace where you want to create the application.

- Click the Relativity Applications tab.

- Click New Relativity Application to display New Application layout. See New application layout fields .

- Click Save to display the application details view. You can add custom components to your application and perform other tasks from this view. See View or edit application details .

### New application layout fields

The new application layout contains the following fields:

- Application Type – click one of the following options:

- Create new Application – creates a new application without any components in your workspace. You can then add new components to it as necessary. See Add components to an application .

- Select from Application Library – installs an application from the Application Library in your workspace. See Installing applications on the Relativity Documentation site.

- Import from File – installs a RAP application in your workspace. See Installing applications on the Relativity Documentation site.

- New Application Name – the name that you want assigned to the application.

- (Optional) Version – the version number for the application. Use the format X.X.X (Major.Minor.Build), exemplified as 1.0.0.

If you don't enter a version number, Relativity automatically assigns one to the application when you export it. See Application schema versions .

- Tab Display – select Vertical or Horizontal to control how child tabs appear under the parent tab.

- (Optional) User-friendly URL – enter a value that you want displayed in custom page URLs. Relativity displays this value instead of the application GUID and other complex path information. View more information about user-friendly URLs

User-friendly URLs provide you with the option of displaying easy to read and understand URLs. As a suggested use case, you can send an email message to your users that contains a simplified URL. This URL could link to a custom page in an application. For more information, see Basic concepts for custom pages .

If you enter MyCustomApplication in this field, users see custom page URLs that appear as ~/Relativity/apps/MyCustomApplication. However, you can continue to reference custom pages using the user-friendly URL, and the URL that contains the application GUID. For example, you can reference it as ~/Relativity/CustomPages/216ecac1-998b-4b67-980b-ada83b9a0f59.

Use these guidelines when working with user-friendly URLs:

- Don’t include the following invalid characters in your URL.

Ampersand (&) Dollar sign ($) Pipe (|)

Asterisk (*) Equal sign (=) Plus sign (+)

At sign (@) Greater and less signs (< >) Semi-colon (;)

Colon (:) Question mark (?) Tab

Comma (,) Quotation marks (") White space

- Use 30 characters or less in a user-friendly URL. If you enter more than 30 characters in the User-friendly URL field, Relativity displays an error message.

- To display user-friendly URLs, you must push the application to Application Library. You can also export and then reimport the application to your current or another workspace. The value set for a user-friendly URL is exported as part of the application. Custom page URLs display this user-friendly URL when you import the application to other workspaces or Relativity instances.

## View or edit application details

To view application details, click the name of an application on the Relativity Applications tab. These details also appear immediately after you create a new application. You can use the buttons at the top of the page to edit, delete, or perform other tasks with the application.

- Application Information and History sections – The Application Information section displays the name, version, and orientation of the tab for the application. The History section displays information about the user who created and last modified the application, and the associated dates.

- Relativity Application console – The console includes buttons and links for performing tasks used in administering and developing custom applications. Administrative tasks

You can use the following buttons in the console for completing various administrative tasks. To find additional information about these tasks, click the links listed here to display content in the Relativity Documentation site.

- Upgrade Application – updates the application to the most recent version. See Upgrading applications .

- Export Application – saves the application as a RAP file. See Exporting applications .

- Lock and Unlock Application – prevents or enables the editing of the application and its associative objects. See Locking and unlocking applications .

You need the appropriate system admin permissions to lock or unlock an application. You can't unlock system secured applications.

- Uninstall Application – removes an application and all of its components from a workspace. See Uninstalling and deleting applications .

- Push To Library – adds an application to the Application Library. You override any existing applications with the same GUID when you push an application from a workspace to the library. See Installing applications .

After you add the application to the library, you can upload files to it from the Resource Files tab. See Resource files .

Development tasks

You can use the following buttons in the console for completing these development tasks:

- Show Application Breakdown – creates a concise list of application components and related information. It downloads an HTML page that summarizes the application configuration. The HTML visualization varies by application. For example, it lists custom objects and their associated fields, and field types. See Troubleshoot application errors .

- Show Errors – displays a list of application errors. Relativity disables Export , Push to Library , and Show Application Breakdown when an application contains errors. You must resolve these errors before you can export an application, add it to the Application Library, or view its breakdown. See Troubleshoot application errors .

- Refresh Page – reloads the current page so you can view updates to it.

- Associative lists – You can use the associative lists on the details view to add custom components to your application, such as fields, choices, event handlers, and others. See Add components to an application .

## Add components to an application

You can customize your application by adding new components to it or by modifying its existing components. Before you start adding or modifying components, review these guidelines:

- Pushing application to Application Library – You may want to add your application to the Application Library so that you can associate files uploaded through the Resources file tab with it. See View or edit application details .

- Uploading files – You need to upload the compiled assemblies for event handlers, agents, and mass operation handlers as resource files before you can add them as application components. See Resource files on the Relativity Documentation site.

- Unlocking or locking applications – You need to unlock the application before adding or removing any components. As a best practice, lock the application when you finish your updates to ensure that it isn't inadvertently modified. For more information, see Locking and unlocking applications on the Relativity Documentation site.

Use these steps to add components to an application:

- Locate the associative list for the component that you want to add or modify on the details view of the application. For example, the Object Type list appears in this screen shot.

- Perform one or more of these tasks depending on the component type:

- Create a new object – Click New to display the form for the object that you want to create. Relativity automatically links this object to your application. From the application details view, you can create object types, fields, choices, views, layouts, tabs, Relativity scripts, and application event handlers.

- Add an existing object – Click Link to displays the Select Items dialog. If an object is already linked to your application, it isn't listed on this dialog. This option is available for all components except application event handlers. To add event handlers, click New .

- Dissociate an object from the application – Select the checkbox for an object and click Unlink . When you unlink an object, Relativity dissociates it from the application, but doesn't delete it from your environment. To remove application event handlers from an application, click Delete . This operation also deletes these event handlers from your environment.

- Modify properties of an object – Click the Edit link for an object.

- To ensure that you can export your application, review the requirements for valid components. See Validation requirements for application components .

### Associative lists

Use the following associative lists to add custom functionality to your application:

- Object Type – See Creating and editing Relativity Objects .

- Field – See Fields on the Relativity Documentation site.

- Choice – See Choices on the Relativity Documentation site.

- View – See Views on the Relativity Documentation site.

- Layout – See Layouts on the Relativity Documentation site.

- Tab – See Tabs on the Relativity Documentation site.

- Event Handler – You can add object type event handlers from this associative list. These event handler types include Console, Page Interaction, Pre Cascade Delete, Pre Delete, Pre Load, Pre Mass Delete, Pre Save, and Post Save event handlers. For more information, see Add object type event handlers .

- Object Rule – You can link objects rules defined for specific objects to your application. See Creating and editing Relativity Objects .

- Relativity Script – You can link custom SQL and other scripts to your application. See Develop scripts .

- Custom Page – You can create a new custom page or associate an existing one with an application. See Publish and upload custom pages .

- Application Event Handler – You can associate Pre Install or Post Install event handlers with an application. These event handlers are run prior to or after the installation of an application respectively. View more information about application event handlers

The Application Event Handler list indicates the order used to execute a series of Pre Install or Post Install event handlers, and the execution type of each event handler. You can designate the order used to execute the event handlers of each type, such as run the first Post Install event handler then the second one.

The execution type determines when the event handler is run in the workspace. Event handlers set to run once are executed when you initially install an application. If the installation fails, these event handlers are re-executed until the application is successfully installed, and then no longer run. Other event handlers run every time the application is installed.

Use the New button to add Pre and Post Install event handlers to an application. The Add Install Event Handler pop-up provides you with the ability to select an event handler and to specify the order in which it is run. For more information, see Develop application event handlers .

- Mass Operations – You can associate mass operations with an application. View more information about mass operations

Use these guidelines when working with mass operations:

- Object types – A mass operation is associated with a specific object type that your application must include. If your application doesn’t currently include it, click Link in the Object Type section to add it.

- Layouts – A mass operation maybe associated with a layout. If it uses a layout, you must include this item in your application. Click Link in the Layout section to add it.

- Application domain – A mass operation may require a Mass Operation handler to provide its functionality. The code for this functionality exists in a class that is added to an assembly that is a .dll file. You can load this assembly to one or more application domains. You must select only mass operations tied to a resource file used by your application. Failure to follow these guidelines causes an application error. To view these errors, click Show Errors in the Relativity Application console. See View or edit application details .

A mass operation may also require a custom page tied to a specific application. In this case, you must also select only mass operations in the domain tied to your application. For custom pages, you need to verify that the URL or page works properly, because you won't see an error if you select a mass operation that isn't tied to the domain. See Develop Mass Operation handlers .

- Saved Search – You can link a saved search to an application. When you create or edit a saved search, you can optionally select an application to associate with it. For more information, see Creating or editing a saved search on the Relativity Documentation site. View more information about saved searches

Use these guidelines when working with saved searches:

- Search providers – Add only saved searches referencing keyword, dtSearch, or Analytics indexes to your application. Saved searches referencing other search providers aren’t supported in Relativity applications.

Minimize the number of indexes that you use when adding saved searches. Ensure that any indexes added to the workspace where you are developing saved searches have unique names. Relativity uses the name of the index when mapping the index to a saved search. As a best practice, consider naming the index based on its type, using dtSearch or Analytics to identify it.

- Document object – If you link a saved search to your application, you must also link the document object to it.

- Path for saved search – You can use the Path column on the details view of an application to determine the current location of a saved search. See the following screen shot:

After installing an application in a workspace, you can move the saved searches that it contains to different folders in the saved search browser. The Path column always displays the current location of the saved search.

- Application installation – Relativity uses the settings for the index name and type stored in the saved search to map it to an existing index in the workspace where you installed the application. If the workspace doesn’t contain the dtSearch or Analytics index used by the saved search, Relativity creates a shell for the index, and requires that you build the index. You also need to update certain fields on dtSearch and Analytics indexes.

You may want to provide documentation that describes the optimal set up for the saved searches included in your application. It may include information about the type of indexes needed, and the settings that you want used on these indexes. If your application is installed on a workspace that doesn't contain any indexes, the user needs to set several properties on the created shells. The user may also want to modify the properties of an index mapped to a saved search even when the index already exists on a workspace. Use your application documentation to provide guidelines about these modifications or optimizations to your users. For more information about setting index properties, see Installing applications on the Relativity Documentation site.

During installation, Relativity creates the folder structure that you use to organize saved searches in your application. It identifies a folder by referencing its GUID, which was assigned when the folder was created by a previous installation. Relativity creates the folder if it doesn’t find one with a matching GUID in the workspace. Otherwise, it adds any new or updated saved searches to the folder as necessary, even if the user has moved the folder to a new location in the saved search browser.

- Public permissions on saved searches – When you install an application, all saved searches are public regardless of the permissions that you assigned to them in your application or folder structure. The ADS framework ignores any permissions or security assigned to a saved search added to an application during deployment in a workspace.

- Versioning – You can modify the saved searches in a locked application by moving them to different folders in the saved search browser or by changing their index type. If you modify a saved search in a locked application, Relativity increments the version when you export the application. It also preserves these changes to saved searches during upgrades. For more information, see Locking and unlocking applications on the Relativity Documentation site.

- Dashboard – You can link a dashboard to an application. If the dashboard has other associations, such as to specific objects or fields, you must also include them in your application. See Dashboards on the Relativity Documentation site.

## Validation requirements for application components

You can export only Relativity applications that contain valid and exportable components, such as fields, scripts, layouts, views, object types, object rules, choices, event handlers, and tabs. When an application contains invalid components, you can't export it. The following table lists the requirements for valid application components. You can use them to determine that the application is exportable, and to troubleshoot application errors. See View application errors .

You can always export agent types, custom pages, and Relativity scripts.

View validation requirements for application components

Application component Application must include...

Choice

- Object type and field that own the choice object.

- Parent of a child or nested choice.

Dashboard

- Object type associated with the dashboard.

- Fields associated with the dashboard.

Event handler

- Object type of the event handler.

Field

- Object type that owns the field.

- Associated object type of single or multiple object fields or one of the following: field, search, search index, production, or object type.

- Custom view if used by fields with a pop-up picker filter type. Any view other than All Items is considered a custom view.

- Custom view if used by single or multiple object field with the field tree. Any view other than All Items is considered a custom view.

You can't export document system fields.

Layout

- Object type that owns the layout and all fields in the layout.

- Views referenced by associative or child lists, and pop- up picker fields.

Mass Operations handler

- Correctly associated with an application and reside in the domain for the application.

- Object type of the mass operation handler.

- Layout associated with the mass operation handler.

Object Rule

- Object type of the object rule.

- Layouts associated with the object rule.

- Single choice fields associated with the object rule.

- Choices associated with the object rule.

- Layouts, fields, and choices referenced by the object rule.

Object Type

- Parent object type of any child object type, or the parent must be a document or workspace object.

Saved Search

- Document object

- All Fields in the saved search. However, the application doesn't need to include the fields in saved searches for field, search, search index, production, and object type.

- Any Saved Searches used as conditions

- Choice used in a choice condition. Only these view conditions are supported for exported applications: choice, currency, date, decimal, number, file, and user-is logged in user.

Tab

- Associated object type for an object type tab.

You can't export parent tabs. While you can export external tabs, their associated URLs may become invalid when you import the application.

View

- Object type that owns the view, or the owner must be the document object.

- All fields in the view. However, the application doesn't need to include the fields in views for field, search, search index, production, and object type.

- Any saved searches that the view uses as a condition.

- Choice used in a choice condition. Only these view conditions are supported for exported applications: choice, currency, date, decimal, number, file, and user-is logged in user.

Indented list views are exportable.
