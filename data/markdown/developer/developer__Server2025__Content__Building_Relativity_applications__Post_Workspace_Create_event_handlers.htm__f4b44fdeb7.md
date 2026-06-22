---
title: "Post Workspace Create event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Post_Workspace_Create_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:37+00:00
sha256: 52ba853216359d5b6963182bb2edaf93e6a28fd49d6d97c97baf429191c799f0
---

Post Workspace Create event handlers

# Post Workspace Create event handlers

You can use Post Workspace Create event handlers to update database tables as part of the workspace creation process. You can also use them to make direct SQL calls and to perform other operations on a workspace or EDDS database. This event handler runs as the final task performed during workspace creation.

For example, you might want to use a workspace with a custom application as a template. If the application includes custom tables on the workspace database, you can use a Post Workspace Create event handler to clear obsolete data from these tables when you create your new workspace and its database. You could also use this type of event handler to update tables in the EDDS with entries for a newly installed application in a workspace.

When a Post Workspace Create event handler fails to finish executing, the Workspace Details page displays an error message and the Re-run Post Workspace Create Event Handlers button in the Relativity Utilities console. Click this button to run the event handler again. If the Post Workspace Create event handlers continue to fail, contact Product Support .

## Guidelines for Post Workspace Create event handlers

Use these guidelines when developing Post Workspace Create event handlers:

- Create a new class in Visual Studio .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages. See Best practices for building applications .

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PostWorkspaceCreateEventHandler class – ensure that you extend the PostWorkspaceCreateEventHandler base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

- Add event handler to application included in workspace template – include your Post Workspace Create event handler in an application installed in your workspace template. The Post Workspace Create event handler only executes after creating a workspace from a template that includes an application, which contains it.

## Code sample for a Post Workspace Create event handler

Review the following code sample for a Post Workspace Create event handler.

Copy

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
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
using System;

using System.Data.SqlClient;

namespace Relativity.Samples.EventHandlers

{

      /// <summary>

      /// This event handler cleans up the workspace scratch table of records that were used in the template workspace

      /// </summary>

      [kCura.EventHandler.CustomAttributes.Description("Cleans application tables after workspace is used for a template")]

      [System.Runtime.InteropServices.Guid("AEDA8241-B769-4ACD-9804-F3CD6CDD5D21")]

      class SamplePostWorkspaceCreate : kCura.EventHandler.PostWorkspaceCreateEventHandlerBase

      {

            public override kCura.EventHandler.Response Execute()

            {

                  //Construct a response object with default values

                  kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

                  retVal.Message = String.Empty;

                  retVal.Success = true;

                  try

                  {

                        //Get the current workspace artifact ID

                        Int32 currentWorkspaceID = this.Helper.GetActiveCaseID();

                        //Get the current workspace database context

                        Relativity.API.IDBContext workspaceDBContext = this.Helper.GetDBContext(currentWorkspaceID);

                        //Remove entries from the table that were for objects in the old case

                        TruncateLocalTable(workspaceDBContext);

                  }

                  catch (System.Exception ex)

                  {

                        //Catch an exception if it occurs, log it, and return a response with success = false.

                        retVal.Success = false;

                        retVal.Message = ex.ToString();

                  }

                  return retVal;

            }

            /// <summary>

            /// Removes entries from application tables in the workspace

            /// </summary>

            /// <param name="workspaceDBContext">Context object to the current workspace</param>

            private static void TruncateLocalTable(Relativity.API.IDBContext workspaceDBContext)

            {

                  String deleteWaitingJobsSQL = "TRUNCATE TABLE [SamplesAppScratchTable]";

                  workspaceDBContext.ExecuteNonQuerySQLStatement(deleteWaitingJobsSQL);

            }

      }

}
```
