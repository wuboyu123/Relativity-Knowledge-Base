---
title: "Global script variables"
url: https://platform.relativity.com/Server2025/Content/Scripts/Global_script_variables.htm
collection: developer
fetched_at: 2026-06-22T06:32:17+00:00
sha256: 4ec8e986799fa3677af61dff3dec576d108fa2e6d9142279673c077925647377
---

Global script variables Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Global script variables

The following global script variables go into the content of the action and are replaced with a preset value:

- #CaseArtifactID# – replaced with the artifact ID of the current workspace.

- #LoggedInUserID# – replaced with the ID of the logged in user.

- #MasterDatabasePrepend#

- replaced with "[EDDS].[EDDSDBO]." If the script runs on the same sever as the EDDS database.

- replaced with "[server-name].[EDDS].[EDDSDBO]." If the script runs from a different server.

- #TimeZoneOffset# - populated based on the script runner's time zone.

- #SampleACLID# - acceptable values for #SampleACLID# are from the table AccessControlListID for the current user, and relates to the AccessControlListPermission table for determining the current user's permissions.

On this page

- Global script variables


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
