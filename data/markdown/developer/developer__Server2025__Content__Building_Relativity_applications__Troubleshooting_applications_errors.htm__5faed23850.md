---
title: "Troubleshoot application errors"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Troubleshooting_applications_errors.htm
collection: developer
fetched_at: 2026-06-22T06:30:57+00:00
sha256: 6084a6301836fa2256b3aa9e376067d6260b6976854b194745715293119e7b4a
---

Troubleshoot application errors Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Troubleshoot application errors

You can use the information to view application errors and to resolve specific types of errors.

## View application errors

To view application errors, open the detail view of an application. Click Show Errors on the Relativity Application console. Relativity enables this link only when an application has errors.

The Export Application and Show Application Breakdown buttons are disabled when an application contains errors.

After you click Show Errors , the Error dialog displays a list of messages that describe the application errors. These errors messages are based on application validation requirements. You can't export an application that contains validation errors. For more information, see Maintain application validation requirements .

## Stack traces for install event handler failures

When the installation of application fails in an exception, you can find the exception in the EDDS database. You can use the stack trace to determine the cause of an install event handler failure, when you have difficulty debugging or can't easily reproduce the error.

Follow these steps to locate the stack trace for an install event handler failure:

- Open SQL Server Management Studio on your Relativity database server.

- Connect to the EDDS database.

- To return the last failed installation of your application, run the following query: Copy

```text
1
2
3
4
5
6
7
8
9
SELECT TOP 1 ApplicationInstall.[Message], ApplicationInstall.[Details]

FROM LibraryApplication

INNER JOIN CaseApplication

ON LibraryApplication.ArtifactID = CaseApplication.ApplicationID

INNER JOIN ApplicationInstall

ON CaseApplication.CurrentApplicationInstallID = ApplicationInstall.ApplicationInstallID

WHERE LibraryApplication.[GUID] = 'Application GUID'

AND [Status] = 1

ORDER BY ApplicationInstallID DESC
```

In this query, the Message is the error displayed for users in the Relativity UI, while the Details are the full stack trace that you can use to debug the failed installation.

When developing install event handlers, ensure that you return helpful information to users in the event handler response message. Providing this information may help users resolve errors themselves.

## Rerun RunOnce install event handlers

During troubleshooting and development, you may need to run Pre and Post Install event handlers with the RunOnce execution type multiple times for testing purposes. These event handlers usually run only during the initial installation of an application. For convenience, you can use the following steps to rerun these event handlers within the same workspace:

- Open SQL Server Management Studio on your Relativity database server.

- Connect to the workspace where you want to rerun the event handlers.

- To identify the install event handlers in your application, run the following query: Copy

```text
1
2
3
4
5
6
7
8
9

SELECT Name, [Order], AG.ArtifactGuid, ARO.InstalledOn

FROM InstallEventHandler IEH

INNER JOIN ArtifactGuid AG

ON IEH.ArtifactID = AG.ArtifactID

LEFT JOIN ApplicationInstallEventHandlerRunOnce ARO

ON ARO.InstallEventHandlerGuid = AG.ArtifactGuid

WHERE IEH.ExecutionType IN (9,10)

AND IEH.ApplicationGuid = 'Your Application GUID'
```

The SELECT statement includes the following parameters:

- Name – the name of the event handler class.

- Order – the execution order assigned to the event handler.

- ArtifactGuid – the GUID for this instance of your event handler. The system tracks the GUID when you run the event handler.

- InstalledOn – the date of the last successful run. If your event handler has already run, the system populates the field with this date.

Use the Name and Order to find the event handler that you want to rerun. If you use the same event handler more than once, then it appears multiple times in the query results.

- To enable your event handler to rerun, use the following query to delete the date of its last successful run: Copy

```text
1
2
DELETE FROM ApplicationInstallEventHandlerRunOnce

WHERE InstallEventHandlerGuid IN ('GUID FROM STEP 3')
```

- Install the application in the workspace. If the application is up-to-date, you may need to unlock it before you can reinstall it.

## Can't export due to unassigned event handlers or agents

When you attempt to export your application, you receive the following error message:

Copy

```text
1
2
3
Event Handler XXXX is not assigned to the correct application domain.

Agent YYYY is not assigned to the correct application domain.

Install Event Handler ZZZZ is not assigned to the correct application domain.
```

This error occurs when the assemblies referencing these objects are loaded for the wrong application in ResourceFile table.

Complete the following steps to resolve this issue:

- On the Relativity Applications tab in your workspace, click the application name.

- Complete the following tasks on the detail view of the application:

- Install Event Handler section - delete the event handler from application.

- Agent Type section - unlink the agent from the application.

- Event Handler section - unlink the event handler from the application.

- Object Type section - click the Edit link for the object associated with event handler. Navigate to the detail view of the object type, select the event handler, and click Delete .

- Click the Resource Files tab.

- Complete these steps for the agent and each event handler:

- Click the Edit link for the .dll that contains that contains the event handler, install event handler, or agent that you want in your application.

- On the detail view, click the file name to download the .dll file.

- On the Resource Files tab, click New Resource File .

- Click to select your application. (If you don't see your application listed, click Push to Library on the detail view of the application to add it to Application Library.)

- Click Choose File to select the .dll that you downloaded.

- On the Relativity Application tab in your workspace, click on the name of your application.

- Add the event handler, install event handler, or agent to your application. Verify that the your application name is associated with the .dll that you selected.

## Can’t find assembly for event handler on an object type

Your application runs but it throws an error when attempting to access an object that is attached to an event handler. The stack trace indicates that the assembly for the event handler can’t be found. This error occurs when the assembly associated with an event handler isn’t linked to the application.

Complete the following steps to resolve this issue:

- In your workspace, click the Object Type tab.

- Click the name of the object type associated with the event handler in error.

- On the details view, note the name of the .dll file.

- Select the Relativity Applications tab.

- Click the name of your application.

- On the details view, scroll down to the Event Handler section.

- Verify that the Application Name column displays the correct information. Perform one of the following tasks:

- Application name matches – unlink the event handler. Next, select the correct event handler for your application. The assembly is available in this case, but it points to the wrong application. If you don't see the event handler listed for your application listed, you may need to add the application to the Application Library. See View or edit application details . Your application should now run without errors.

- Missing assembly – continue with step 8.

- Click the Resource Files tab.

- Filter on the application name to locate the correct assembly. Perform one of the following tasks:

- Missing assembly – add the assembly as a resource file. Click New Resource File to select the .dll and application that you want to associate with it. For more information, see Resource files on the Relativity Documentation site. Your application should now run without errors.

- Correct assembly and application – The database reference to the assembly may be incorrect. Continue with step 10.

- Run the following script on the case database to identify event handlers that you may need to relink: Copy

```text
1
2
3
4
5

SELECT DISTINCT AssemblyArtifactID, ResourceFile.ApplicationGuid

FROM ActiveSyncs INNER JOIN EDDS.eddsdbo.ResourceFile

     ON ActiveSyncs.AssemblyArtifactID = ResourceFile.ArtifactID

WHERE ActiveSyncs.ApplicationGuid <> ResourceFile.ApplicationGuid
```

- To relink event handlers, run the following statement on the query results from step 10: Copy

```text
1
2
3
4

UPDATE ActiveSyncs

SET ApplicationGuid = # ApplicationGuid #

WHERE AssemblyArtifactID = # AssemblyArtifactID #
```

On this page

- Troubleshoot application errors

- View application errors

- Stack traces for install event handler failures

- Rerun RunOnce install event handlers

- Can't export due to unassigned event handlers or agents

- Can’t find assembly for event handler on an object type


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
