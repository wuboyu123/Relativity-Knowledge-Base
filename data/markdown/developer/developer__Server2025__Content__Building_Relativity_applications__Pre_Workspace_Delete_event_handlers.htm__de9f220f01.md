---
title: "Pre Workspace Delete event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Pre_Workspace_Delete_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:39+00:00
sha256: 9ff1ecaef2d4406ab7db8ed5d769170c06c57a99b5fbd0f965942ce189f2733e
---

Pre Workspace Delete event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre Workspace Delete event handlers

Using Pre Workspace Delete event handlers, you can remove unneeded application data from your database when you flag a workspace for deletion. The process of deleting a workspace automatically triggers the Pre Workspace Delete event handlers in all applications that contain them. They execute as the last step in the process used to flag a workspace for deletion. In other words, they execute as the last action that occurs while the progress bar is running in the Relativity UI for a delete operation.

These event handlers remove data that the applications may create or need in order to run in the deleted workspace. For example, they might clear entries from database tables, drop unneeded tables, or perform other clean-up tasks on the EDDS database. Pre Workspace Delete event handlers don’t need to remove tables or values from the workspace itself, because the delete operation performs these tasks.

You might consider using Pre Workspace Delete event handlers when you want to remove queue or other tables used by applications to store jobs associated with a workspace that you are deleting. In addition, these event handlers can clean up external resources created for the deleted workspace, such as another database.

## Guidelines for Pre Workspace Delete event handlers

Use these guidelines when developing Pre Workspace Delete event handlers:

- Create a new class in Visual Studio .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages. See Best practices for building applications .

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PreWorkspaceDeleteEventHandlerBase class – ensure that your event handler extends the PreWorkspaceDeleteEventHandlerBase base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Pre Workspace Delete event handler

Review the following sample code for a Pre Workspace Delete event handler.

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

using System;

namespace Relativity.Samples.EventHandlers {

/// <summary>

/// This event handler runs before the delete process starts on a workspace.

/// </summary>

[kCura.EventHandler.CustomAttributes.Description("Deletes job entries on the GlobalProcessingQueue for the workspace.")]

[System.Runtime.InteropServices.Guid("B3891465-5F2B-482D-9A11-590AB8ADEF5C")]

class ClearGlobalQueuePreWorkspaceDeleteEventHandler: kCura.EventHandler.PreWorkspaceDeleteEventHandlerBase {

  private const String DELETE_OBSOLETE_JOBS_SCRIPT = "DELETE FROM [GlobalProcessingQueue] WHERE [WorkspaceArtifactID] = @workspaceArtifactID";

  public override kCura.EventHandler.Response Execute() {

    //Construct a response object with default values.

    kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

    retVal.Message = String.Empty;

    retVal.Success = true;

    System.Data.SqlClient.SqlParameter workspaceArtifactIDParam = new System.Data.SqlClient.SqlParameter("@workspaceArtifactID", System.Data.SqlDbType.Int);

    workspaceArtifactIDParam.Value = this.Helper.GetActiveCaseID();

    try {

          this.Helper.GetDBContext(-1).ExecuteNonQuerySQLStatement(DELETE_OBSOLETE_JOBS_SCRIPT, new System.Data.SqlClient.SqlParameter[] {

          workspaceArtifactIDParam});

      } catch (Exception ex) {

            //Catch an exception if it occurs and fail the case delete.

            retVal.Success = false;

            retVal.Message = ex.ToString();

            }

          return retVal;

        }

    }

}
```

On this page

- Pre Workspace Delete event handlers

- Guidelines for Pre Workspace Delete event handlers

- Code sample for a Pre Workspace Delete event handler


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
