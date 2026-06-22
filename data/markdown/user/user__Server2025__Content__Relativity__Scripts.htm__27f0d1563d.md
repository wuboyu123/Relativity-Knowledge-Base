---
title: "Scripts"
url: https://help.relativity.com/Server2025/Content/Relativity/Scripts.htm
collection: user
fetched_at: 2026-06-22T06:07:09+00:00
sha256: e53c625d5110146e5786ac447967291972afc98696d1ca06f8b1ca5f93b3c4bd
---

Scripts Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Scripts

Scripts are Relativity artifacts. This means they have the same features as standard Relativity objects, allowing them to be secured and audited.

Relativity Scripts are a tool to access and modify data stored in Relativity SQL databases. Not all data is available in SQL, and data currently in SQL may be migrated to other storage systems. The recommended integration mechanism is to use APIs/Services instead of scripts to avoid future migration or interruption.

You should only use scripts when an appropriate API is not available. Relativity will add new and updated APIs over time - review the available APIs periodically to determine if you can replace a script with an API or REST service call.

Changes to SQL fields executed by Relativity Scripts do not produce Audit logs.

Only users who are members of groups with the appropriate permissions can write scripts. System admins have permissions to preview, edit, and create scripts. See Security and permissions .

If a script is locked, it appears as read only, and you can't edit it. If a script is unlocked it's available for editing.

The following table represents the script permissions allowed for each group.

Locked Script Unlocked Script

View Run Edit Preview Edit Preview Write Link

System Admin x x x x x x x

Standard User x* x* x**

* With view rights

** With add rights

## Script compatibility and updates

To improve system performance, architecture improvements are often applied to Relativity’s SQL tables for new versions.

When upgrading, your personally-created scripts must be tested and revalidated before you run them. Remember that the recommended integration mechanism is to use APIs instead of scripts to avoid potential disruption if the data schema or storage mechanism changes.

If you use a Relativity script in a custom development project, it is recommended to make a copy of the script and use the copied script in your project. Software updates may modify the scripts provided by Relativity, which could cause unintended results if you use the Relativity-provided scripts directly in your custom development projects.

When upgrading your environment, the unique script key is referenced to determine if an update is required. If so, this is performed automatically.

## Creating a new library script

You can create a new library script in Admin to then be available for selection from the Scripts tab in any workspace in which the Scripts tab is visible.

To do this:

- Navigate to the Relativity Library Scripts tab in Admin.

- Click New Relativity Script .

- In the Script Body field, enter values for each script component and click Save .

If any errors occurred in the script body, you will see an error message identifying the line and position of the problematic text. Relativity will not save the new script until you address the errors.

If no errors occur, Relativity saves the new script, and it is available for selection from the Scripts tab.

## Selecting a library script

Due to the complexity and impact a script can have, only Relativity, SQL, and XML expert users should create and run them.

To select a library script and add it to your workspace, perform the following steps:

- Navigate to and select the Scripts tab.

- Click New Relativity Script . If you want to edit an existing script, click the Edit link next to the script name.

- Complete the following fields:

- Script Type - select Select from Script Library to choose from a list of predefined Relativity scripts. The Script Library tab is created when Relativity is deployed. Note that this is the only option available for the Script Type field if the AllowAddOrEditScripts instance setting is set to its default value of False.

- Relativity Script - select the script from the script library.

- Relativity Applications - associates the script with an application created on the Relativity Applications tab. All existing applications are available when you click the ellipsis. This is only available for those who have the Manage Relativity Applications permission under Admin Operations. For information on applications, see the Applications Guide For information on applications, see the Applications Guide

- Click Save .

## Creating a new workspace script

You must set the AllowAddOrEditScripts instance setting to True to make the Create New Workspace Script option available. For more information, see AllowAddOrEditScripts .

Due to the complexity and impact a script can have, only Relativity, SQL, and XML expert users should create and run them.

To create a new workspace script, follow these steps:

- Navigate to and select the Scripts tab.

- Click New Relativity Script . If you want to edit an existing script, click the Edit link next to the script name.

- Complete the following fields:

(Click to edit)

- Script Type - select Create New Workspace Script .

- Relativity Applications - associates the script with an application created on the Relativity Applications tab. All existing applications are available when you click the ellipsis. This is only available for those who have the Manage Relativity Applications permission under Admin Operations. For information on applications, see the Applications Guide For information on applications, see the Applications Guide

- Script Body - enter the script code into this area. For information on how to format a Relativity script, see Script properties on our Relativity Developers site ..

- Click Save .

## Adding a library script to the script tab

In order for scripts to appear in your Script tab for your users to run, you must add them. To add a library script to the Script tab, follow these steps:

- Navigate to and select the Scripts tab.

- Click New Relativity Script .

- Choose Select from Script Library on the Script Type field.

- In the Relativity Script field, click Select , and choose the library script you want to add.

- Click Save .

The script information screen appears.

- In the Script console, click Run Script .

The script appears in your Script tab. In addition, Relativity adds the Is Link column to the view and sets it to Yes. When you add a library script to a workspace, it remains linked to the Script Library as indicated in the Is Link column. This column displays No if you add your own custom script to the workspace.

## Running a library script

To run a script, follow these steps:

- Navigate to and select the Scripts tab.

- Click Run next to the script you want to run or open the script and click Run Script on the Actions console.

- Configure the required fields on the script layout.

- Click Preview to display a pop-up of the SQL script, or click Run to execute the script.

On this page

- Scripts

- Script compatibility and updates

- Creating a new library script

- Selecting a library script

- Creating a new workspace script

- Adding a library script to the script tab

- Running a library script


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
