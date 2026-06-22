---
title: "Creating or editing a saved search"
url: https://help.relativity.com/Server2025/Content/Relativity/Saved_search/Creating_or_editing_a_saved_search.htm
collection: user
fetched_at: 2026-06-22T06:07:30+00:00
sha256: f255d16c7288b68a17937c9d70bec5e7a08803e907c38514a6bf5c55727924ec
---

Creating or editing a saved search Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Creating or editing a saved search

This page contains the following sections:

- Creating or editing a saved search

- Search fields

- Using pop-up pickers

- Using the Search Bar

- Linking a Relativity Application to a saved search

- Rerunning out-of-date saved searches

## Permissions

The following security permissions are required to view, edit, delete, and add saved searches and saved search folders:

Object Securit Other Settings

- Search - View, Edit, Delete, Add

- Search Container - Edit, Add

- Browsers - Advanced & Saved Searches

For complete details on workspace permissions, see Setting workspace permissions .

## Creating or editing a saved search

To create or edit a saved search from the Search browser, follow these steps:

- Click the Saved Searches icon in the Search Panel.

- Click Create New Search . To edit a search, right-click the search name, and click Edit .

If you do not see the Create New Search button, you may have another saved search selected. Click the top-level folder in the Search Panel. In the image below, the top-level folder is named Salt and Pepper .

- Complete the fields in the Information section. For an explanation of the individual field details, see Information .

- Click Add Condition to add a new condition to the search or click Add Logic Group to create a logic group to group conditions together to create the criteria for the search. In the image below, a condition is set where the custodian is Sally Beck. For more information on setting conditions, see Conditions .

The Default Search View controls which fields are returned, by default, on an advanced or saved search. You can always include additional fields from the advanced or saved search field selector. This view also controls the field sort order. The Default Search View is only meant to be used as a way to control the default fields that are brought back when running a saved search in Relativity. Since that is its purpose in Relativity there is no way to make any changes or additions to the Conditions portion of this view.

- Click the Fields tab. Select the fields you want to display in the search results. Note that Edit, File Icon, and Control Number are default fields and are preselected. You can remove them if they are not needed. For more information on setting search results fields, see Search fields .

- Click the Sort tab to specify sorting for the search results. For more information on setting the sort order, see Sort .

- Click the Advanced tab to add additional information such as search keywords and hints. For more information on advanced settings, see Advanced .

- Click Save & Search , Search , Save , or Save As .

Selecting Save As opens a pop-up modal to update the name of the saved search.

## Search fields

#### Information

The Information fields are:

- Name —enter a title for the saved search.

- Owner —select an owner from the drop-down list or click Me to make yourself the owner. The owner is the user that can view the saved search. If you select Me, only you can view the saved search. If you select Public, anyone with view permissions to the workspace can view the saved search.

- Dashboard —select an already created dashboard to link the saved search to it. For more information, see Linking a dashboard to a saved search .

- Requires Manual Rerun —select this option if you want to require users to rerun a saved search when they return to it after navigating to other features in Relativity. Selecting this option only affects the search that the current user is running. It does not affect any parent or nested searches tied to the current search. If you have a search that has Requires Manual Rerun checked and you include it as the criteria for another search, it will rerun.

- Scope —select one of these options to designate the document set for the search:

- Entire Workspace —searches all documents within a workspace.

- Selected Folders —select this option, and then click Select Folders . On the Select Folders pop-up, select the checkboxes for the folders that you want to search. Clear the Include Subfolders checkbox on the pop-up if you don't want to include subfolders. Click Clear All to remove all selections.

The Requires Manual Rerun option is for searches that might take a long time to run, and you don't need them to run automatically when you navigate back to the saved searches. This keeps you from having to manually cancel queries before you can navigate away from that search.

- Notes —any notes you want to add to provide additional information about the search.

#### Advanced

The Advanced fields are:

- Relativity Applications —any Relativity applications you want to associate with a saved search.

- Keywords —any keywords you want to provide additional information about the search.

- Query Hint —used to optimize views. Only use the query hint if instructed by the Relativity Customer Support team. Currently, you can use Hashjoin: (true/false) or Maxdop: (x) to populate the field. You must remove query hints before using a saved search in a Relativity script.

#### Conditions

The Conditions fields define the criteria of the search. Click on a filter card to edit the condition or click the x in the top right corner to remove the condition. The equation box along the top gives you a high-level view of the conditional statement you are creating. There are the following controls on this tab:

- Add Condition —select the field you want to apply a condition to by entering the name of the field or selecting the field from the drop-down list.

If there are previously created field categories, you can select a field category from the drop-down list to conveniently filter the fields list. To learn more, visit Field Categories .

- Index Search —select this to select a Keyword , dtSearch , or Analytics index, and then enter search terms to apply as a search condition.

- Saved Search —select this to select an existing Keyword , dtSearch , or Analytics saved search to apply as a search condition.

- <field name> —select an object field name to create a conditional expression for that field to apply to the overall search criteria.

- Add Logic Group —adds logic groups you can add conditions to by dragging and dropping the conditions into the logic group frames. Use the AND or OR operator to join logic groups.

- Includes drop-down —select an option for returning documents related to hit documents. (Hit documents match the search criteria.) The related documents are included in the result set, but they do not need to match the search criteria. Select No Related Items if you do not wish to include any of these documents.

- Duplicates —use this setting if you want the result set to include documents with the same MD5 Hash values as the hit documents. (The MD5 Hash value is used as a unique file identifier.)

- Family —use this setting if you want the result set to include documents with the same group identifiers as the hit documents.

- <Custom Field> —your organization may use custom related fields. Contact your system admin for additional information.

#### Fields

The Fields (Required) fields represent the field columns that are displayed for your search results:

- Available: these fields are listed in left box.

If there are previously created field categories, you can select a field category from the drop-down list to conveniently filter the fields list. To learn more, visit Field Categories .

- Selected: these fields are listed in the right box, and they will be displayed for your search results. They are ordered based on their position in this box. You can drag and drop them to change their order.

#### Sort

The Sort options define the default sort order used for the search results. Each row in a sort criterion contains the following options:

- Sort Field: select a field from the left drop-down box. The search sorts on the field you select.

- Order: select ascending or descending from the right drop-down box.

## Using pop-up pickers

You may have the option to select values from a pop-up picker when you choose certain fields or operators in the Conditions section. For example, pop-ups are available when you select the following operators:

- Any of these

- None of these

- All of these (only for multiple object fields)

- Not all of these (only for multiple object fields)

See Creating or editing a saved search . For information about setting batch conditions, see Batch fields as search conditions .

### Select items pop-up picker

Use the following general steps to select items in the picker:

- Navigate to the Saved Search form or use the Search Conditions feature.

- Select a Field option for a condition.

- Select one or more items in the Available Items list. A checkmark indicates an item is selected.

- Click Apply .

### System user fields

System user fields include the System Created By and System Last Modified By fields, which you can use in search conditions.

- Navigate to the Save Search form or use the Search Conditions feature.

- Select a system user field in the Field option for a condition.

- Select an operator, and perform one of the following tasks:

- If you selected any of these or none of these , select from the Available fields and move to the Selected fields column, then click Apply .

- Enter the username in the textbox.

- Define any additional search criteria as needed.

### Folder name field

You can select Folder Name as a field in a search condition to create more flexible queries than using the Scope section of the Saved Search form. You can combine conditions containing the Folder Name and other fields with AND or OR operators refining your search criteria.

- Navigate to the Save Search form or use the Search Conditions feature.

- Select Folder Name in the Field option for a condition.

- Select an operator, and perform one of the following tasks:

- If you selected any of these or none of these , select the checkbox next to one or more item, then Apply .

- If you selected another operation, enter the folder name in the text box.

- Define any additional search criteria as needed.

## Using the Search Bar

The Search Bar, a UI controlled feature, exists along the top of item lists that support index search. This replicates the functionality of the Index Search condition in the Search Panel (including Keyword Search and dtSearch). To run the index search, simply enter your search terms in the search bar and hit Enter on your keyboard or click Search .If you would like to list more than one search term on separate lines, click Enter + Shift .

When Index search conditions are disabled/enabled in the condition panel, the Search Bar reflects the condition panel state.

### Recent Searches

The Search Bar can also be used to generate highlights within a document in the Viewer.

To view Recent Searches within a document:

- Navigate to Documents .

- Select the desired index from the Keyword Search drop-down list.

- Enter the desired search terms in the field to the right of the drop-list and click Enter on your keyboard. Keyword, proximity, fuzzy, and stemming searches can work depending on which type of search index you chose.

The list displays documents that match your search criteria.

- Click on the desired document to open it in the Viewer. Terms that match the entered criteria are highlighted as Recent Searches along with any Persistent Highlight Sets that are enabled.

- Optionally, click on Show/Hide Persistent Highlight Pane to display the Recent Searches and Persistent Highlight Sets. Click on the lightbulb icon to turn the Recent Searches and/or Persistent Highlight Sets on or off.

Recent Searches only apply when using the Search Bar or when running a saved search against a keyword index. Recent Searches do not apply when running a saved search against a dtSearch index.

## Linking a Relativity Application to a saved search

To link a Relativity Application to a saved search:

- Navigate to the Search Browser.

- Create a new search or edit an existing search.

- Click Add in the Advanced tab to display the Select Items —Relativity Applications modal. Available applications are in the left box and Selected applications are in the right box.

- Choose one or more applications. Use the arrows to move the applications from the available to selected boxes.

-

Click Set .

You can clear your options by clicking the clear button.

To unlink a Relativity Application from a saved search, click Add and use the arrows to remove the application(s). Please note that you cannot leave the selected applications box empty. A warning in red will appear along the bottom that reads: "Selection cannot be empty." Either leave at least one application linked or clear all using the clear button.

## Linking a dashboard to a saved search

To link a dashboard to a saved search:

- Navigate to the Search Browser.

- Create a new search or edit an existing search.

- Choose a dashboard from the drop-down list.

- Click Save & Search , Search , Save , or Save As .

If you switch to a different dashboard while viewing the saved search, the link breaks. There are two ways to restore this link:

- Log out of your environment, then log back in.

- Edit the search and hit Save and Search again.

If you delete a dashboard, Relativity removes the link in the saved search.

If you delete a dashboard with dependencies, a message appears with a list of dependencies.

## Rerunning out-of-date saved searches

You may need to rerun a saved search when you return to it after navigating to other features in Relativity. Instead of seeing your search results, you see a message indicating that your search is out of date.

To enable the Run saved search feature, select the Requires Manual Rerun option in the Information section of the Saved Search form.

Perform one of these tasks:

- Click Run saved search to reload your search results. You can also click on the saved search in the browser to rerun the search.

- Click Edit Search to display the Saved Search form where you modify the search settings.

If you edit an item returned in your saved search, you need to rerun it. You must rerun the search even when the edited item still meets the search criteria, and the number of documents returned doesn't change.

On this page

- Creating or editing a saved search

- Permissions

- Creating or editing a saved search

- Search fields

- Using pop-up pickers

- Select items pop-up picker

- System user fields

- Folder name field

- Using the Search Bar

- Recent Searches

- Linking a Relativity Application to a saved search

- Linking a dashboard to a saved search

- Rerunning out-of-date saved searches


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
