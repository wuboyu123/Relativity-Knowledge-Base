---
title: "Pre Mass Delete event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Pre_Mass_Delete_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:29:03+00:00
sha256: 2262a38332d304a61414b29e097203de39bbd653106c1b4ae3df1c9b4a01d0ca
---

Pre Mass Delete event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre Mass Delete event handlers

You call a Pre Mass Delete event handler to perform a one-time operation before deleting a large set of objects. Unlike a Pre Cascade Delete event handler, Pre Mass Delete doesn't require the assigned object to have object dependencies. Use the Pre Mass Delete event handler when working with child objects that you must process in some way before deleting all of them at once.

While you could use a Pre Delete event handler to execute a similar operation, it requires calling the Pre Delete event handler to delete each individual child object. In contrast, the Pre Mass Delete event handler provides an efficient way to run an action before deleting a whole set of children objects a the same time. For example, a Pre Mass Delete event handler can change the status of parent objects in a set before deleting their children.

To view items for deletion, use the TempTableNameWithParentArtifactsToDelete string property of the PreMassDeleteEventHandler base class. It holds the name of the scratch table that contains the ArtifactIDs marked for deletion.

## Guidelines for Pre Mass Delete event handlers

Use these guidelines when developing Pre Mass Delete event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PreMassDeleteEventHandler class – extend the PreMassDeleteEventHandler base class.

- Override the RequiredFields property – you must override this property even though a Pre Mass Delete event handler doesn't use it.

- The ActiveArtifact.Fields collection includes the fields returned by the RequiredFields property, and those on the current layout. It also includes the values of these fields.

- Any Field in ActiveArtifact.Fields that is referenced in this event handler must be placed in the RequiredFields property.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Pre Mass Delete event handler

Review the following code sample for a Pre Mass Delete event handler.

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
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
using System;

using System.Collections.Generic;

using System.Data;

using System.Data.Common;

using System.Linq;

using System.Data.SqlClient;

namespace Relativity.Samples.EventHandlers

{

    /// <summary>

    /// This event handler gets a list of the artifactIDs to be deleted from the temp table in the database

    /// and deletes any existing instances from the queue table in the EDDS database

    /// </summary>

    [kCura.EventHandler.CustomAttributes.Description("A description of the event handler.")]

    [System.Runtime.InteropServices.Guid("D18212D7-32F8-4901-A142-6009E0FDDE2E")]

    public class PreMassDeleteEventHandler : kCura.EventHandler.PreMassDeleteEventHandler

    {

        public override kCura.EventHandler.Response Execute()

        {

            //Construct a response object with default values

            kCura.EventHandler.Response eventResponse = new kCura.EventHandler.Response();

            eventResponse.Success = true;

            eventResponse.Message = String.Empty;

            try

            {

                //Get a dbContext for the current workspace

                Int32 currentWorkspaceArtifactID = this.Helper.GetActiveCaseID();

                Relativity.API.IDBContext workspaceContext = this.Helper.GetDBContext(currentWorkspaceArtifactID);

                //Get the temp table name of the artifactIDs to be deleted

                String tempTableName = this.TempTableNameWithParentArtifactsToDelete;



                //Get a list of the artifactIDs to be deleted

                List<Int32> artifactIDsToBeDeleted = GetArtifactsToBeDeleted(workspaceContext, tempTableName);

                //Get a dbContext for the EDDS database

                Relativity.API.IDBContext eddsDBContext = this.Helper.GetDBContext(-1);

                //Delete instances from the queue table

                DeleteInstancesFromQueueTable(eddsDBContext, artifactIDsToBeDeleted, currentWorkspaceArtifactID);

            }

            catch (Exception ex)

            {

                //Event completed with error. Return failure and mention of the error details.

                eventResponse.Success = false;

                eventResponse.Message = string.Format("An error occurred while executing the Pre-Mass-Event handler.  Message: {0}", ex.Message);

            }

            return eventResponse;

        }

        /// <summary>

        /// Queries the temp table in the database containing the collection of artifactIDs that are being deleted

        /// </summary>

        /// <param name="workspaceContext">A properly constructed workspace database context</param>

        /// <param name="tempTableName">The name of the temp table that holds the artifactIDs to be deleted</param>

        /// <returns>A generic list of Int32 with the artifactIDs to be deleted</returns>

        private List<Int32> GetArtifactsToBeDeleted(Relativity.API.IDBContext workspaceContext, String tempTableName)

        {

            //create a sql statement which will select the list of ArtifactIDs from the TempTableNameWithParentArtifactsToDelete scratch table

            string selectSQL = string.Format("SELECT [ArtifactID] FROM [Resource].[{0}]", tempTableName);

            //get the artifact ids from the table and convert to a generic list of Int32

            return workspaceContext.ExecuteSqlStatementAsDataTable(selectSQL).Rows.Cast<System.Data.DataRow>().Select(dr => Convert.ToInt32(dr["ArtifactID"])).ToList();

        }

        /// <summary>

        /// Removes any instances from the queue table in the EDDS database

        /// </summary>

        /// <param name="eddsDBContext">A properly constructed EDDS database context</param>

        /// <param name="artifactIDsToRemoveFromQueue">The list of artifactIDs to be removed from the queue table</param>

        /// <param name="workspaceArtifactID">The workspace artifactID this operation is being performed on</param>

        private void DeleteInstancesFromQueueTable(Relativity.API.IDBContext eddsDBContext, List<Int32> artifactIDsToRemoveFromQueue, Int32 workspaceArtifactID)

        {

            String deleteSQL = String.Format("DELETE FROM [SamplesAppQueue] WHERE [WorkspaceArtifactID] = @workspaceArtifactID AND [InstanceArtifactID] IN ({0})",

                String.Join(", ", artifactIDsToRemoveFromQueue));

            SqlParameter workspaceArtifactIDParam = new SqlParameter("@workspaceArtifactID", SqlDbType.Int);

            workspaceArtifactIDParam.Value = workspaceArtifactIDParam;

            eddsDBContext.ExecuteNonQuerySQLStatement(deleteSQL, new SqlParameter[] { workspaceArtifactIDParam });

        }

        public override void Commit()

        {

            //Clean up for a successful transaction.

        }

        public override void Rollback()

        {

            //Rollback clean up for a failed transaction.

        }

        /// <summary>

        /// Override this required field property and return null since we don't have any required fields

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get { return null; }

        }

    }

}
```

On this page

- Pre Mass Delete event handlers

- Guidelines for Pre Mass Delete event handlers

- Code sample for a Pre Mass Delete event handler


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
