---
title: "Add event handlers to applications"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Adding_event_handlers_to_applications_or_objects.htm
collection: developer
fetched_at: 2026-06-22T06:31:27+00:00
sha256: 7e4b352a15e8e3c424868db59d0b4ec00d11bacdb4d5890c2257efd0f6dca3d2
---

Add event handlers to applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Add event handlers to applications

After your event handler assembly builds successfully, you can upload it to an application or object in the Relativity UI.

Use the following procedure to add your event handler assembly to an application:

- Open a Relativity instance used for development.

- Create an application in a workspace that you want to use for development. See Create an application in Relativity .

For information about linking your event handler to a custom object, see Creating and editing Relativity Objects .

- Navigate to the Resource File tab, and click New Resource File . For more details, see Resource Files on the Relativity Documentation site.

- In the Resource File field, click Browse to select the .dll file for your event handler from the directory where you built your project.

If you want to debug your event handler, you should also upload your Symbol files (.pdb) and associate it with the same application as you did for your event handler. See Troubleshoot event handlers .

- In the Application field, click to select your custom application. In general, you don't want to link to event handler assembly to the default application.

- Click Save . You can now link your event handler to a custom object in Relativity.

Add the event handler to a custom object before adding it to an application, If you don't first add it to a custom object, the event handler won't be displayed in the list used for adding it to an application. For more information, see Creating and editing Relativity Objects .

- Navigate to the workspace containing your application.

- Click the Relativity Applications tab and then click on your application name.

- On the details view of the application, scroll down to the associative list for your event handler type:

- Event Handler – Add object type event handlers. For a list of these event handler types, see Develop object type event handlers .

- Application Event Handler – Add application event handlers. For a list of these event handler types, see Develop application event handlers .

- Mass Operations – Add mass operation handlers. See Develop Mass Operation handlers .

- To attach the event handler to your application, click the New or the Link button on the associative list.

- Select the your event handler in the dialog box. After you attach your event handler, it executes in Relativity as part of your application.

On this page

- Add event handlers to applications


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
