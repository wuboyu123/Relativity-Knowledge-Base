---
title: "Saved search"
url: https://help.relativity.com/Server2025/Content/Relativity/Saved_search/Saved_search.htm
collection: user
fetched_at: 2026-06-22T06:02:25+00:00
sha256: 882fddd68af4e7c7d8f2bf6a966f092e9d848475ee9f6b40ed8cfc7050a49fd7
---

Saved search Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Saved search

A saved search is a saved set of criteria that returns the latest documents that meet that criteria. For example, if you want to reference documents that contain the terms "confidential" and "property" and are also marked as Relevant, you can create a saved search with that criteria. However, saved searches can be much more complex.

In Relativity, you can create saved searches by defining custom queries and unique views, as well as by selecting public or private security settings, specific folders to query, and nested sort orders. You can also execute a search on the fly, save it for later use, or perform a combination of these tasks.

Since saved searches are executed in real-time, you save the search definition but not the results. Relativity executes the search each time you click on it in the Saved Searches browser and when you return to it after performing other tasks in the workspace. This functionality ensures that only data meeting the search criteria is returned in the result set. (You can set the Requires Manual Rerun option to control this functionality.)

When you execute a saved search, Relativity first applies the conditions then related items (from the search criteria), then the filters (from the item list). The only exception is when you have nested relational searches, for example, Search A which relies on the results of Search B. In this scenario, Relativity applies the innermost search conditions (in this case, Search B), then the family Search B relies on; it then applies the outer search conditions (Search A), then the family Search A relies on. Finally, Relativity applies the filters from the item list.

You can also use saved searches as the building blocks in other Relativity features. For example, you're required to select a saved search when you create batches, build a dtSearch or Analytics index, define an imaging set, and perform other tasks in Relativity.

This page contains the following sections:

- Navigating the saved searches browser

- Controlling the visibility of saved searches

- Organizing saved searches in folders

See these related pages:

- Creating or editing a saved search

- Defining criteria for saved searches

- Saving searches on the Documents tab

- Saved search history

Also see these related recipes:

- Creating secured saved search folders for multiple groups

- Using saved searches to complete conflict checks

- Searching for a document set using control numbers

- Coding the first item in a family group with the skip function

## Permissions

The following security permissions are required to view, edit, delete, and add saved searches and saved search folders:

Object Securit Other Settings

- Search - View, Edit, Delete, Add

- Search Container - Edit, Add

- Browsers - Advanced & Saved Searches

For complete details on workspace permissions, see Setting workspace permissions .

## Navigating the saved searches browser

On the Documents tab, you can click to view the Saved Searches browser. This browser provides you with features used to create, organize, edit, and perform other tasks with saved searches.

The Search Folder Tree displays the following options:

- Create New Search button - click this to display the Saved Search form. To display this form, you can also click any folder, including the root folder.

- Public or Private - the icons display next to the name of a saved search to indicate its visibility.

- Search textbox - enter the name of a search in this field to automatically filter the list as you type to the saved search(es) that you are looking for. See Filtering the list of saved searches .

- Display checkboxes button - click this button to display checkboxes in the list to the left of folders and searches. You can then perform mass operations for items that you check. Click the icon again to toggle them off. See Performing mass operations on saved searches .

- Search Right-click Menu - highlight a search in the folder tree to display a right-click menu with the following options:

- Edit - displays the Saved Search form, where you can modify the current settings for the search.

- Copy - adds a duplicate of the search to the tree.

- Secure - available on public searches, this option displays a security page so that you can override the security inherited from the workspace, or parent folder. See Setting permissions on Relativity objects .

- Delete - permanently removes the search from the database.

- Email Link - opens an email message containing a link to the saved search. The Subject line is pre-populated with the following text: "Review - <Workspace Name> - <Search Name>." When the recipient clicks on the link, the saved search is displayed with the current result set.

Relativity displays a permissions denied message if the recipient clicks the link to display the search but does not have access rights to it.

- Copy Link to Clipboard - copies a URL path to the search to your clipboard.

Relativity displays a permissions denied message if the recipient clicks the link to display the search but does not have access rights to it.

- Folder Right-click Menu - Highlight a folder to display a right-click menu for managing folders. See Organizing saved searches in folders .

The action bar displays the following when a search is selected in the browser:

- Show current path icon ( ) - view the current search browser folder location for the displayed search.

- Edit Search - When you click this icon on the action bar, the Search Builder dialog appears where you can update search criteria.

- Save Search - When you click this icon on the action bar, a pop-up appears where you can select a new owner and modify the search name. See Creating or editing a saved search .

### Filtering the list of saved searches

To filter the list in the saved search browser:

- Enter text matching the search or search folder you want to see in the Filter textbox at the top of the browser.

Matching searches and search folders display as you type in their respective folders.

- Select the search you want to view.

You can also expand the Filter text box and filter on advanced searching fields, including:

- Created By - choose which user created the saved search.

- Created On - select from four different date ranges, including: Past Hour, Today, Past 7 days, and Past 30 days.

- Last Modified By - choose which user last modified the saved search.

- Last Modified On - select from four different date ranges, including: Past Hour, Today, Past 7 days, and Past 30 days.

- Owner - select a specific user or public.

- Keywords - enter keywords.

- Notes - enter notes.

To remove your filtering from the list, delete the text that's there or click the X to the right. The list of searches will automatically update.

To access Advanced Search Filtering:

- Navigate to the Views tab.

- Locate the Advanced Search Browser View.

- Make sure at least one of the following fields is added to the view: Created By, Created On, Last Modified By, Last Modified On, Owner, Keywords, or Notes. We recommend you add them all at once.

- Click Save .

### Performing mass operations on saved searches

The following mass operations are currently available:

- Copy

- Delete

- Move

- Export to file

To perform mass operations on saved searches in the saved search browser:

- Click the checkboxes button to the right of the Filter textbox to turn checkboxes in the list of searches on. The Add or Delete permissions must be selected on the Search object for check boxes to display to the right of the Filter text box for the user. See Permissions for more information.

- Select the checkbox for an individual search or select the checkbox for a search folder to select searches inside that folder.

You must expand the search folders before you can check the checkbox for the folder to allow you to examine the searches you will perform a mass operation for.

The number of selected searches appears in the drop-down list to the left of the mass operations multi-select button below. Alternatively, you can select All from the drop-down list to select all searches.

- Once you've selected the desired searches, choose the desired mass operation (copy, delete, move, or export to file) from the mass operations multi-select button.

- A pop-up modal appears, where you edit and confirm the details of the mass operation you are performing.

- Click Ok to complete the operation.

## Controlling the visibility of saved searches

On the saved search form, you can control the visibility of a search by setting the Owner option. New searches are private by default, making them visible only to you and Relativity administrators. In addition to owner access, users must have permissions to the Saved Searches Browser and at least view permissions for Search on the security page. See Setting workspace permissions .

You can change the visibility of a search by selecting one of these options in the Owner drop-down menu:

- Public - Makes the search available to all users with the appropriate permissions.

You can configure Relativity to make your saved searches public by default. When you create a search, the Owner box will display Public. In My Settings , select Public in the option Default Saved Search Owner .

- User Name - Select a specific user from the drop-down menu. The search will be visible only to that user and Relativity administrators.

- Me - Click this button to reset the visibility on the search to private. Your name appears in the Owner box.

You define the criteria used for saved searches in the Conditions section of the Saved Search form. You can build complex queries using a combination of fields and operators that are set to required values. For information about the operators available for building these queries, as well as specific options for searching batches and developing combined searches, see Defining criteria for saved searches .

## Organizing saved searches in folders

You can organize saved searches by adding them to securable folders that you create and manage in the Saved Searches browser. To work with search folders, you must have the appropriate permissions for Search Folder , Search , and the Saved Searches Browser on the security page. See Setting workspace permissions .

### Adding sub-folders to the root

In the Search Folder Tree, right-click on the root folder to add sub-folders to the browser. Click Create to add a new folder, and name it something descriptive of its contents. To update the folder name, right-click on the folder, and click Rename .

### Managing subfolders

Right-click on a folder under the root to display the following menu options:

- Create - Adds a subfolder to the highlighted folder.

- Rename - Makes the folder name editable. Enter new text for the name.

- Secure - Displays a security page so that you can override the security inherited from the workspace, or parent folder. See Relativity object security .

- Delete - Permanently removes all the searches and subfolders that folder contains from the database.

- New Search - Displays the Saved Search form. See Creating or editing a saved search .

### Adding existing searches to folders

To add existing searches to a folder, left click the search and then drag and drop it into the folder. Click OK on the confirmation message.

When you move a search, it inherits the security from the parent folder. You may want to check the security on a folder before moving a search into it.

On this page

- Saved search

- Permissions

- Navigating the saved searches browser

- Filtering the list of saved searches

- Performing mass operations on saved searches

- Controlling the visibility of saved searches

- Organizing saved searches in folders

- Adding sub-folders to the root

- Managing subfolders

- Adding existing searches to folders


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
