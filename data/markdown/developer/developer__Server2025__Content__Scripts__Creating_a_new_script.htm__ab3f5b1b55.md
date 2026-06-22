---
title: "Create a new Relativity Script"
url: https://platform.relativity.com/Server2025/Content/Scripts/Creating_a_new_script.htm
collection: developer
fetched_at: 2026-06-22T06:32:15+00:00
sha256: a6fa93d0a771bfa0567113a7bb64dff386d105e13e6a6df8b20719da83d8e14e
---

Create a new Relativity Script

# Create a new Relativity Script

If you are a system admin, you can create and edit scripts in Relativity. Before creating a script, it's important to read the script formatting section. Due to the complexity and impact a script can have, only expert users of Relativity and SQL should create scripts.

You can create a script in either the Relativity Script Library or a single workspace.

You must enable the AllowAddOrEditScripts instance setting to enable users to create or edit scripts. For more information, see the Relativity Documentation site .

## Relativity Script Library

The script is stored in the Relativity Script Library and can be deployed to all workspaces. Any changes made to the library script are reflected in every workspace that points to the script.

To create a new Relativity Script Library script, perform the following steps:

- In Relativity Home, select the Relativity Script Library tab.

- Click the New Relativity Script button.

- Enter your script into the Script Body box.

- Click Save .

The script will now be available under the Relativity Script Library tab. To run the script, click the script's name. In the script information screen, click the Run Script button in the Script console.

## Workspace scripts

When adding the script code directly to a workspace, a copy of the script exists only in the workspace.

To create a new script in a single a workspace, perform the following steps:

- Select the Script tab.

- Choose the Create New Workspace Script option (default).

- Enter your script into the Script Body box.

- Click Save .

The script will now be available under the Scripts tab. To run the script from the Scripts tab, click the Run link next to the script name.

The script information is populated by the properties entered within the body of the XML. See Script properties for more details.
