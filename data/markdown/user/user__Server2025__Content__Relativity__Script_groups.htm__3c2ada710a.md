---
title: "Script groups"
url: https://help.relativity.com/Server2025/Content/Relativity/Script_groups.htm
collection: user
fetched_at: 2026-06-22T06:07:10+00:00
sha256: d681e5c5fd9b9215c5c1b631f66b17b843229a0314ddc357a1f666a0d5ee2597
---

Script groups

# Script groups

You can use script groups in Relativity to create a dashboard view into your scripting activities. Script groups are an extension of the Relativity script page where you can dynamically create script dashboards based on the category specified in the Relativity script XML. These dashboards provide you with a radio button list of all scripts, and they provide a centralized location to run your similar scripts.

Changes to SQL fields executed by Relativity Scripts do not produce Audit logs.

See Scripts for more information.

## Setting up a script group

Follow these steps to set up a script group:

- Create or select a group of Relativity scripts that you would like to add to a script group . They must all share the same Category. You can also create new categories. See Creating a new workspace script .

- Create a new external tab that links to your script group. See Creating and editing tabs .

If the category name contains spaces, replace the spaces with the + sign.

-

Copy the script category’s Report Group URL to your clipboard or Notepad. For example, if you are creating a script group for all scripts whose category is Case Functionality, open any script belonging to this category. Then, copy the entire path listed in Report Group URL.

- Navigate to Workspace admin > Tabs , and then select New Tab .

- Enter the following:

-

Link Type - External

- Link - Paste the entire Report Group URL path. It should look similar to the following:

%ApplicationPath%/ Case/RelativityScript/Run.aspx?%AppID%&%SystemID%&category=Case+Functionality

- Leave all other fields at default settings.

- Navigate to the new tab you created for your script group.

Linked scripts can only be members of a script group as an admin tab. You can't create script groups of linked scripts within a workspace.
