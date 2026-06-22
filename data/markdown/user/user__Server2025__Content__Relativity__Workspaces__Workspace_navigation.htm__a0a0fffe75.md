---
title: "Workspace navigation"
url: https://help.relativity.com/Server2025/Content/Relativity/Workspaces/Workspace_navigation.htm
collection: user
fetched_at: 2026-06-22T06:16:54+00:00
sha256: f2778c3fbd1ac671913b878cca9ebbc6a78dfd7739337cd0770b17cb20e59f10
---

Workspace navigation

# Workspace navigation

The workspace has several key areas that are important to understand as a Relativity user.

## Browser panel

The browser is located on the left side of the workspace. Depending on your permissions, you may not see the browser. If you don't have a browser in your workspace, you can skip this section.

If you can see the browser, it may contain the following options for browsing through your documents:

- Folders

- Field Tree

- Saved Searches

- Clusters

No matter which of these options you use, there are several display options you can use to customize your workspace.

The browser opens by default. Hide or show the browser by using the arrow icon in the upper left of the browser. Clicking closes the browser. Reopen the browser by clicking . You can also resize the browser by hovering over the line separating the panel from the other panel or item list until the line is highlighted. You may then click and drag the line to the desired dimensions.

### Browser options

The browser menu is located directly below the browser. Click on one of the menu’s options to display that mode of the browser:

Icon Name Description

Folder browser Navigate the folder hierarchy for your workspace

Field Tree browser Browse your documents according to how they were coded or grouped

Saved Searches browser Create a new search, or browse previously saved searches. See Saved Search .

Clusters browser Browse your workspace clusters, which are groupings of conceptually correlated documents. See Clustering .

You must have Analytics to use the cluster browser and define clusters in your workspace. See Analytics .

#### Folder browser

Click on the folder icon to navigate the folder hierarchy for your workspace. The folder structure is set when documents are imported. It can be based on the document’s source, or according to a folder structure set by your Relativity administrator. Clicking on a folder displays that folder’s documents in the item list.

##### Considerations

-

Please be aware that folder names in Relativity workspaces are subject to a character limit. The maximum allowed length for folder names is 200 characters. While our system allows you to input names up to 255 characters, any name exceeding the 200-character limit will be automatically truncated. We recommend keeping folder names concise and under 200 characters to ensure they remain intact and fully visible in your workspace. If you anticipate the need for longer folder names, consider using abbreviations or adopting a naming convention to convey necessary information within the character limit.

-

To ensure stable performance, we recommend creating no more than 250,000 folders in a workspace and having 15 sub-folders or less within each folder.

A folder often has multiple subfolders. You can view the subfolders with the expand button to the left of the desired folder. Once the subfolders expand, you can use the collapse button to collapse them back into their root folder.

To change the folder scope (Only this folder or This folder and subfolders), click the arrow icon to the left of the Folder browser, and then select either This folder and subfolders or Only this folder from the drop-down list.

#### Field tree browser

Clicking on the field tree icon displays the field tree in the browser. Selected single- and multiple-choice list fields and their choices appear in a tree structure.

Each single and multiple-choice field has its own choice folder in the field tree. The field’s choices appear as subfolders. Each field also has a [Not Set] choice, which displays null values for the field.

You can click on a choice in the field tree to display all the documents in the item list manager that have the selected choice value AND meet the criteria of the active view. In the item list, click this icon to send a link to the documents currently displayed in it.

##### Sending email links to choices

You can send an email message with a link to a choice, a choice folder, or the item list that appears when the field tree browser is open. In the field tree browser, right-click on a choice (or a choice folder) to display the E-mail Link option. Click this option on a choice to open an email message containing a link to it.

The subject line of the email message pre-populates with the following text: "Review - <Workspace Name> - <Choice Name: Value>." When the recipient clicks on the link, the documents associated with the choice appear in the item list manager. Relativity displays a permissions denied message if the recipient clicks the link but doesn't have access rights on the field associated with the choice.

If you send an email link to a choice folder, the subject line displays the folder name instead of the choice name and the value. The item list manager displays all documents associated with the choices in the folder. Recipients must have access rights to fields associated with the choice folder.

## View bar

The view bar consists of the following elements:

- Show/Hide Browser Panel - Click to show or hide the browser panel.

- Show/Hide Search Panel - Click to show or hide the search panel.

- Show/Hide Document Preview Panel - If the EnableDocumentPreview instance setting is set to True, click to display a panel which allows you to view documents before launching the Viewer. For more information, see Document Preview Panel .

- Show current path - view the current folder browser location for the displayed document list.

- Views drop-down menu - select a view.

- Edit view icon - edit a view that displays within the view drop-down menu. This will only be present if you have permission to edit the view. If it's not present, contact your Relativity administrator to edit the current view.

- New view icon - create a new view from within the view drop-down menu. This will only be present if you have permission to add a new view. If it is not present, contact your Relativity administrator to add a view.

- Include Related Items drop-down menu - returns documents related to the documents currently in the view. The options vary by workspace, but may include email family groups, duplicates, or similar documents. Learn more about related items in the Related items card section of this document.

- Add Widget - add a custom widget to your document list dashboard (e.g., pivot chart, list, grid, or cluster visualization).

- Dashboard drop-down - select a custom dashboard to view in your document list. See Dashboards .

- Export drop-down button - you can select export your dashboard widgets to an editable Excel document. See Dashboards .

- Sampling button - If you have proper permissions, clicking the Sampling button lets you create random sample sets from the document list using three different methodologies from the pop-up menu that appears.

For more information, see Views .

The drop-down menu that determined the folder scope has been removed from the view bar and repositioned in the folder browser. To use this new control, see Changing folder scope .

## Document preview panel

The Document preview panel allows you to view documents in the document list before launching the Viewer. It also allows you to filter the list and quickly view documents in the results which makes the process of finding documents more efficient. You can view the native, images, production images, and text of documents in the Document preview panel, as well as view and navigate through highlight hits for any previously created persistent highlight sets. Unlike the Viewer, you cannot search or create ad hoc search terms in the Document preview panel however. Additionally, searching for terms in the document list will not create highlights in a document you are viewing in the Document preview panel.

To access the Document preview panel, the EnableDocumentPreview instance setting should be set to True. The Show Document Preview Panel icon will then display in the View bar. Additionally, users will need to have the Document Preview permission in Other Settings provided to a group they are in.

The Document preview panel does not support viewing hidden content, creating or modifying markups, or editing coding decisions. Please open the document in the Viewer to perform these tasks.

### Navigating the Document Preview Panel

The Document preview panel can be re-sized at any time by clicking and on the edge of the panel and dragging your cursor to the desired sizing.

The Document preview panel can be moved from the right or left side of the document list to the other side as well. To move the preview panel, click in the upper-left corner and drag the window to the blue strip on the other side of the screen.

The following options are available in the Document preview panel:

- Show/Hide Persistent Highlight Pane - displays or hides a panel containing any persistent highlight sets in the workspace. See Persistent highlight sets for more information. Only terms in the sets that are in the current document will display in the pane.

Additionally, you can control which highlights display in the current document by clicking on either the persistent set to only display highlights from that set or you can click on a specific term to only see that term highlighted in the document.

- Document Preview Panel Mode - click the name of the mode in which you would like to view the document. Mode names that are displayed in light blue indicate that the document is available for viewing in that mode. If a name appears in a black font and italics, that mode is not available for viewing in the current document.

The mode that is currently open will display in a darker blue with an underline underneath the name.

- Markup set - displays the active markup set in a drop-down menu. Choose a markup set from the drop-down menu to make a different set active. This menu only appears when viewing a document in Image mode of the Document preview panel.

- Page navigator - use any of the following options to help you navigate the pages in the document you are previewing:

Option Description

Click to move to the first page in the document.

Click to move to the previous page in the document.

Click to move to the next page in the document.

Click to move the last page in the document.

## Item list

The item list manager consists of the item list as well as navigational and other controls for working with the list of items.

Icon Description

Show / Hide Filters Click the blue icon to show filters for columns in the item list. Click the orange icon to hide them.

Clear Filters Click this icon to clear any filters that have been applied to the item list.

Reset column sizes To return to the original settings for the columns, click the Reset Column Sizes icon.

Turn Grid Style On / Off Click the blue icon to turn grid style on. This shrinks the row padding and alternates row shading to make your data more compact and easier to read. Click the orange icon to turn grid style off.

Use these navigational controls to navigate the pages in the item list.

The fields that appear in the item list are based on the selected view, which is editable. A view can also be edited to re-arrange the order that the columns display. Contact your Relativity administrator to change the fields in your view. For more information on how to edit the fields and their order in a view, visit Views .

To change a column’s size, hover over the white line at the edge of the column header. A double arrow appears, indicating that you can move the column. Drag it in either direction to adjust the column width. The other columns on the page automatically adjust to fill the rest of the window. Column data can be cut off. If you wish to return to the original settings click the Reset Column Sizes icon .

### Saving a search from the Documents tab

You can save the conditions you've currently set up for the item list as a new search using the icon located next to the mass operations bar at the bottom of the item list. See Saving searches on the Documents tab .

### Previewing a document

Note that if you hover your mouse pointer over a record’s file icon, you can click to open a pop-up viewer showing the record.

If your item list doesn’t contain the file icon, contact your Relativity administrator to add it.

### Sorting

You can use any field in the view to sort the entire searching set – the number of documents indicated in the bottom right.

Click any field heading once to sort the documents in that field in ascending order, alphabetically. A down arrow appears next to the heading name, as in the Responsive field below. Click a second time to sort the documents in descending order, alphabetically. An up arrow appears. Clicking the field name a third time clears the sort and returns the field to its original order.

If you're not able to sort a particular field, contact your administrator to make sure the field has the Sort option set to Yes.

## Document set information bar

If you are using the new UI, the document set information bar no longer displays the bottom of your screen. In the new user interface, you can now browse your entire returned document set using the item list or the Review Interface without having to incrementally add more documents. The maximum number of documents you can load in the Review Interface can be changed using the FluidReviewQueueSize instance setting.
