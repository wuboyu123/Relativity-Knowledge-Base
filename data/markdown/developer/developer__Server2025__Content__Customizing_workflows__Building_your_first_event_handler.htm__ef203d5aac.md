---
title: "Build your first event handler"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Building_your_first_event_handler.htm
collection: developer
fetched_at: 2026-06-22T06:24:48+00:00
sha256: a6f94cc6e8cfc8f73f5654fbe94ec3d473177bb18a1f3956838a1958197a518a
---

Build your first event handler Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Build your first event handler

This tutorial illustrates how to create a simple event handler that updates the Name field on a Relativity Dynamic Object (RDO). It describes how to complete the following tasks:

- Write the source code for this event handler.

- Inherit from the event handler base class.

- Override the Execute() method with your business logic.

- Add the compiled .dlls for the event handler to Relativity.

- Execute the event handler on an RDO.

For information about different types of event handlers, see Develop object type event handlers and Develop application event handlers .

## Before you begin

Complete the following tasks to before you implement an event handler:

- Set up your development environment.

- Install the Relativity Visual Studio templates. For more information, see Visual Studio templates for Relativity .

- Obtain access to an instance of Relativity used for development purposes. In Relativity, confirm that you have system admin permissions. For more information, see Security and Permissions on the Relativity Documentation site.

- If you have not done so already, you should Create a nuget.config file so that your solution can target different nuget repositories for Relativity Server or RelativityOne.

## Build an event handler

Use the following steps to build a simple event handler:

- Open Visual Studio.

- Click File > New > Project .

- In the New Project dialog, search for Relativity and then scroll down to Relativity Server PreSaveEventHandler .

- In the next dialog, configure the location for your project.

- To view the references in the project, right-click on References in the Solution Explorer. The references are added to the project as part of the template.

- In the Solution Explorer, open the PreSaveEventHandler.cs file. This file displays the template code for an event handler.

- Update the kCura.EventHandler.CustomAttributes.Description to Basic Pre Save . This attribute determines the name of the event handler that appears in Relativity.

Review the additional features of this code:

- The GUID attribute added above the class name in the code.

- The class is derived from the kCura.EventHandler.PreSaveEventHandler class.

- Override the RequiredFields property and return a new FieldCollection, which includes the Name field. This step ensures that the Name field is always available in the ActiveArtifact.Fields collection even when it isn't on the layout.

- Normally, you would add code to the using clause which uses Object Manager, but for this basic tutorial you can add the follow simplified code shown below: Copy

```text
1
2
3
4
5
string yourName = this.Helper.GetAuthenticationManager().UserInfo.FullName;

string currentTimeStr = DateTime.Now.ToLongTimeString();

string helloString = $"Hello {yourName}! The time is: {currentTimeStr}";

kCura.EventHandler.Field nameField = this.ActiveArtifact.Fields["Name"];

nameField.Value.Value = helloString;
```

You must override the Execute() method inherited from the base class. It contains the code with your business logic. In this example, the Execute() method works as follows:

- Instantiates a new Response object with the Success property set to true, and the Message property set to an empty string.

- Retrieves the name of the current user who is logged in and the time.

- Creates a string containing the user and time data.

- Sets the Value property of the Name field in the ActiveArtifact.Fields collection equal to this string.

Your code in the using statement in the Execute() method should be like the following sample:

- To compile your event handler source code, click Build > Build Solution . After your event handler assembly builds successfully, you can upload it to Relativity.

- Open the Relativity instance used for development.

- In this step, we will cover how to satisfy the pre-requisites for adding your event handler to an Application. The prerequisites are:

- The application must be a Relativity Application within a Workspace

- The application must also exist in the Application Library tab

Depending on which previous tutorials/lessons you may have completed, there are multiple scenarios you may be in at this point:

- You completed the previous Basic tutorials, so you already have a Relativity Application in a Workspace, which you pushed to the Application Library. See Step 12.a

- You have a Relativity Application in a Workspace, but it does not appear in the Application Library tab. See Step 12.b

- You created a Relativity Application on a different instance of Relativity, and have not installed it on this instance of Relativity. See Step 12.c

- You want to create a new Application. See Step 12.d

- If you completed the previous basic tutorials, you will already have a Relativity Application in a Workspace, which you pushed to the Application Library. In this case, no further changes are needed. You can skip to Step 13 below.

- If you created an Application on this Relativity instance in a previous lesson/tutorial, but you don't see it in the Application Library, then follow these steps: Expand Steps for 12.b

- Go to the workspace where you created the Application.

- Go to the Relativity Applications tab at the workspace level.

- Click on your application.

- Press Push to Library .

- If you created a Relativity Application on a different instance of Relativity, and have not installed it on this instance of Relativity, follow these steps:

Expand Steps for 12.c

- If you don't already have a RAP file for your application, export your application. This will create a RAP file you can use to install to this Relativity instance

- On the Application Library tab, click the Upload Application button

- Click on the Select file button

- Pick your application. After your RAP is selected, the dialog will look like this

- Click on the Save button. Wait until Relativity tells you that the installation is Complete

- On the bottom part of the screen, in the Workspaces Installed section, click on the Select button. You should see the Workspace where you want to do your development work on the application. If you haven't yet created a workspace to do your development work on, you should create a workspace, then go to the Application Library tab, click on your Application. You will see a similar page with a Workspaces Installed section, where you can click on the Select button

- Select/check a workspace, press the button, and then click Apply

- If you want to create a new Application, follow these steps:

Expand Steps for 12.d

- Go to an existing workspace, or create a new workspace.

- Go to the Relativity Applications tab at the workspace level.

- Click New Relativity Application .

- In the Application Type field, click Create new Application .

- Enter a name for your application.

- Click Save

- Press Push to Library .

- Search for the Resource Files tab at the instance level.

- Click New Resource File .

- In the Application field, click Select and select your application.

- In the Resource File field, click Select File to choose BasicPreSaveEventHandler.dll from the directory where you built the project.

- Click Save .

You now have a new event handler type available for use in Relativity. In this example, you attach your event handler to an RDO so that you can execute it.

- In the Resource Files tab, repeat steps 14-17 to add Relativity.ObjectManager.dll. (Steps summarized below for convenience)

- Click New Resource File

- In the Application field, click Select and select your application.

- In the Resource File field, click Select File to choose Relativity.ObjectManager.dll from the directory where you built the project.

- Click Save

- Create a new Object Type called Basic Samples RDO in the workspace you are using for Application development.

- Click Save to display the Event Handlers on Object Type associative list.

- To attach the event handler to your new object type, click New on the Event Handlers associative list.

- Select the BasicPreSaveEventHandler in the dialog box. After you attach your event handler, you can execute it in Relativity.

-

You need to add the new Object Type and the new Event Handler to your application

- Click on your application, within the Relativity Applications tab in your workspace

- Press Unlock Application .

- In the Object Type section, click Link , and add your Object Type, Basic Samples RDO .

- In the Event Handler section, click Link and select your BasicPreSaveEventHandler.

- Click Push to Library .

- To view your event handler execution, create a new instance of the Basic Samples RDO.

- In the Name field, enter Test RDO Instance .

- Click Save to trigger your Pre Save event handler. Your event handler updates the Name field to display the text: Hello <your name>! The time is: <time> .

### Troubleshooting errors with RelativityLogs

- If you forgot to add ObjectManager.dll as a resource file as described in Step 18, it will cause an error when you click the Save button for Basic Samples RDO. If that happens, you will see a failure message on the web page, like this

- To see the cause of this error, you can view the error logging in SQL; the errors are in the table [EDDSLogging].[eddsdbo].[RelativityLogs] . You can use a query like this to find the error messages:

Copy

```text
SELECT TOP 1000 *

FROM [EDDSLogging].[eddsdbo].[RelativityLogs]

ORDER BY ID DESC
```

- You should see a few errors, each with the [Exception] column populated. the first exception should have a message like this

Copy

```text
Expected Message

"BasicPreSaveEventHandler.PreSaveEventHandler" event handler for e118540f-634e-43c9-9dea-da2c207ae761 failed "Save Execute"
```

- If you look in the [Exception] column, you will see an exception which starts with this text:

Copy

```text
Expected Exception

System.IO.FileNotFoundException: Could not load file or assembly 'Relativity.ObjectManager, Version=1.1.2.0, Culture=neutral, PublicKeyToken=null' or one of its dependencies. The system cannot find the file specified.  File name: 'Relativity.ObjectManager, Version=1.1.2.0, Culture=neutral, PublicKeyToken=null'...
```

- To fix this error:

- Add Relativity.ObjectManager.dll as a Resource File, associated with your application.

- Go to the Relativity Application view of your application, and click Push to Library .

On this page

- Build your first event handler

- Before you begin

- Build an event handler

- Troubleshooting errors with RelativityLogs


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
