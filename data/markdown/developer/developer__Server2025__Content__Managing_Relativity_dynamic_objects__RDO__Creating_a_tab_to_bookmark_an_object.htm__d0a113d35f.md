---
title: "Creating a tab to bookmark an object"
url: https://platform.relativity.com/Server2025/Content/Managing_Relativity_dynamic_objects/RDO/Creating_a_tab_to_bookmark_an_object.htm
collection: developer
fetched_at: 2026-06-22T06:29:30+00:00
sha256: b8ea665e6002467758c3cb2e3efc5679d2457a97ab1ee5bb8bfc44d547faf2f9
---

Creating a tab to bookmark an object Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Creating a tab to bookmark an object

You can create new a tab that links directly to any web page or a location within Relativity. This is useful for bypassing list views or for going to specific locations.

## Finding the ArtifactID

If the target is a Relativity page or object, you need the ArtifactID.

To find the ArtifactID:

- Navigate to the page or object from within a workspace. If you are a system admin, you can navigate to pages or objects in the Admin Mode area.

- View the page URL. The ArtifactID follows the string beginning with ArtifactID= .

In the image below, the URL ends with ArtifactID=1035255 . That means the ArtifactID for this object is 1035255.

## Creating the tab

To create a bookmark tab:

- Navigate to the Tabs tab, then click New Tab .

- Complete the following fields:

- Name - the name for the new tab. The name must be between 1 and 50 characters.

- Tab Type - select External from the menu.

- Link - enter one of following options:

- The URL of a non-Relativity target webpage. For example, enter http://www.example.com or http://www.example.com/Instructions .

- The ArtifactID of a Relativity page or object, specified in this format: ObjectArtifactIdentifier= identifier , where identifier is the ArtifactID.

For example, in the dialog below, the Link value is ObjectArtifactIdentifier=1035255 .

- Set as Default Tab - select Yes to set this tab as the default when a reviewer logs in; otherwise, select No .

-

Visible - select Yes to display this tab.

- Relativity Applications - click Select to associate this tab with an application.

- Show in Sidebar - select Yes if you want the tab to appear in the navigation sidebar.

- Parent - optionally specifies the parent workspace tab for this new tab to appear under. Leave as Select... , the default value, for the new tab to appear as a separate tab in the tab strip.

- Order - the numerical position of the tab. The lower the Order value is, the more the new tab appears to the left in the tab strip. Click View Order to display a list of active tabs and their current order.

- Click Save .

The tab appears immediately.

On this page

- Creating a tab to bookmark an object

- Finding the ArtifactID

- Creating the tab


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
