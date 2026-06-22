---
title: "Use scripts in Relativity"
url: https://platform.relativity.com/Server2025/Content/Scripts/Using_scripts_in_Relativity.htm
collection: developer
fetched_at: 2026-06-22T06:32:13+00:00
sha256: 8ca86a16cf8301ebe10205efffc608df9316894b5e58144146ac3e6342614c06
---

Use scripts in Relativity Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Use scripts in Relativity

Relativity Scripts are a tool to access and modify data stored in Relativity SQL databases. Not all data is available in SQL, and data currently in SQL may be migrated to other storage systems. The recommended integration mechanism is to use APIs/Services instead of scripts to avoid future migration or interruption.

You should only use scripts when an appropriate API is not available. Relativity will add new and updated APIs over time - review the available APIs periodically to determine if you can replace a script with an API or REST service call.

In Relativity, scripts are Relativity artifacts. This means they are securable and eligible for auditing, just like fields and views. On the Scripts tab in a workspace, you can select from the following script options:

- Create New Workspace Script – allows a system admin to create and edit their own environment and workspace scripts in the Scripts tab.

- Select from Script Library – allows any user with rights to add scripts to the workspace to choose from the predefined set of scripts in the Relativity Script Library. If you add a script to a workspace from the library, the workspace points to the library script. Any changes to the library script are automatically reflected in the workspace .

For more information on running a library script, see Scripts on the Relativity Documentation site.

- Relativity Applications – associates the script with an application created on the Relativity Applications tab. All existing applications are available when you click . This option is available only to users who have the Manage Relativity Applications permission under Admin Operations. For information about applications, see Build Relativity applications .

On this page

- Use scripts in Relativity


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
