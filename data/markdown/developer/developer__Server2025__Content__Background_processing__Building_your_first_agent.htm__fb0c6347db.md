---
title: "Build your first agent"
url: https://platform.relativity.com/Server2025/Content/Background_processing/Building_your_first_agent.htm
collection: developer
fetched_at: 2026-06-22T06:24:49+00:00
sha256: 3ef9eddfb278e5a5288b05617c507180b2ddde80af3ad7166b8fbf610aa10039
---

Build your first agent Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Build your first agent

This tutorial illustrates how to create a simple agent that raises the message: Hello World! The current time is: <time> . It describes how to write the source code for this agent by completing these tasks:

- Adding references to your Visual Studio project.

- Inheriting from the agent base class.

- Overriding the Execute() method with your business logic and performing other key development tasks.

- Adding the compiled .dll files for the agent to Relativity and view the messages that the agent raises.

## Before you begin

Complete the following tasks to before you begin implementing an agent:

- Set up your development environment. This tutorial uses Visual Studio to illustrate development tasks.

- Install the Relativity Visual Studio templates. For more information, see Visual Studio templates for Relativity .

- Obtain access to an instance of Relativity used for development purposes. In Relativity, confirm that you have the appropriate system admin permissions. For more information, see Security and Permissions on the Relativity Documentation site.

- If you have not done so already, you should Create a nuget.config file so that your solution can target different nuget repositories for Relativity Server or RelativityOne.

## Build an agent

Follow these steps to build a simple agent in Visual Studio:

- Open Visual Studio.

- Click File > New > Project .

- In the New Project dialog, expand Relativity and select Relativity Server Agent .

- Enter BasicSampleAgent in the Name field and click OK .

- To view the references in the project, right-click on References in the Solution Explorer. The references are added to the project as part of the template.

- In the Solution Explorer, open the RelativityAgent.cs file. This file displays the template code for an agent.

- Update the kCura.Agent.CustomAttributes.Name to Basic Sample Agent . The class attribute which determines the name of the agent displayed in Relativity.

Review the additional features of this code:

- The GUID attribute added above the class name in the code.

- The class is derived from the AgentBase class.

- Override the Name property and enter Basic Sample Agent as the name that you want returned for the agent. Only the WinForm debugging tool uses this property to identify the agent.

- Update the time message in the Execute() method. You must override the Execute() method inherited from the base class. The current method raises the message: Hello World! The time is: <time> . In the Relativity UI, you set an interval that specifies when this method is called. See step 22.

- To compile your agent source code, click Build > Build Solution . After your agent assembly builds successfully, you can upload it to Relativity.

- Open the Relativity instance used for development.

- In this step, we will cover how to satisfy the pre-requisites for adding your agent to an Application. The prerequisites are:

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

- In the Resource File field, click Select File to choose the BasicSampleAgent.dll from the directory where you built the project.

- Click Save . You now have a new agent type available for use as an agent in Relativity. To run the agent, you need to add it to an agent server.

- Search for the Agents tab at the instance level.

- Click the New Agent button.

- In the Agent Type field, click Select to choose the Basic Sample Agent that you created.

- In the Agent Server field, click Select to choose the agent server. Your agent runs on this server.

- Set the Run Interval to 5 .

- Click Log All Messages to view all messages that the agent raises in Relativity. Click Save

. Because you created your agent in Relativity, the agent server detects that you have assigned a new agent to it. It loads the necessary assemblies required to trigger the Execute() method on your agent.

- To view your agent execution, click the Agents tab and locate your new agent. You should see the agent has executed:

Hello World! The current time is: <time>

If you agent has not executed and is reporting an error that Relativity can't find the file or assembly Relativity.Objectmanager , the cause of the error is the code below which creates a proxy object for the Relativity.ObjectManager API. Even though we did not actually call the ObjectManager API, C# still requires Relativity.ObjectManager.dll to be present in order to execute this section of code:

As a result of this missing dependency, you will see the following error in the Agents tab:

To address this error, locate the Relativity.ObjectManager.dll file. It should be in the bin folder of your Visual Studio BasicSampleAgent project. Then add the Relativity.ObjectManager.dll file as a Resource File that is associated to your application:

After you have fixed the missing reference error, you should start to see your agent executing:

Hello World! The current time is: <time>

On this page

- Build your first agent

- Before you begin

- Build an agent


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
