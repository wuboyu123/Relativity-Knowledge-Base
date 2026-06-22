---
title: "Pre Delete event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Pre_Delete_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:28:59+00:00
sha256: c41b4db1c52493b108651c7752cffaf3af8b0a90c774781f6298e6dcb9ee9e81
---

Pre Delete event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre Delete event handlers

Pre Delete event handlers execute after a user clicks the Delete button or performs a mass delete operation in Relativity. Documents, Relativity Dynamic Objects (RDOs), and mass delete operations support these event handlers.

After Relativity deletes the target object, the event handler commits the delete database transaction. If an error occurs during this process, a rollback method is triggered and its code is called. You can then execute different code in the rollback method. As best practice, execute a Pre Cascade Delete event handler to perform validation on delete. Next, trigger the Pre Delete event handler.

If you need to cancel a delete operation, performing this validation ensures that objects aren't unlinked or removed. Executing only the Pre Delete event handler without this validation causes associated objects to remain unlinked and child objects to be removed even though you canceled the operation. For more information, see Pre Cascade Delete event handlers .

## Guidelines for Pre Delete event handlers

Use these guidelines when developing Pre Delete event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit form the PreDeleteEventHandler class – extend the PreDeleteEventHandler base class.

- Override the Commit() method – executes after the object is deleted from the database.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Override the Rollback() method – executes when an error occurs during deletion.

Pre Delete event handlers don't use the RequiredFields property. In addition, the ActiveArtifact.Fields collection isn't populated for this type of event handler.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Pre Delete event handler

Review the following code sample for a Pre Delete event handler.

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
using System;



namespace ExampleEventHandlers

{

    /// <summary>

    /// Example of a pre-delete event handler.

    /// </summary>

    [kCura.EventHandler.CustomAttributes.Description("Pre-delete event handler")]

    [System.Runtime.InteropServices.Guid("0E072ECF-1D95-4C28-8F2E-092077A5A84F")]

    class ExamplePreDeleteEventHandler : kCura.EventHandler.PreDeleteEventHandler

    {



        private const String DELETE_OLD_ENTRIES_QUERY = "DELETE FROM [MySQLTable] WHERE [WorkspaceArtifactID] = @workspaceArtifactID AND [InstanceArtifactID] = @instanceArtifactID";



        /// <summary>

        /// The Commit method does not commit any action taken by the event handler.  Rather, it is a hook,

        /// called by the Relativity framework immediately before the SQL transaction (in which the

        /// RDO is being deleted) is committed.

        /// </summary>

        public override void Commit()

        {

            //Do nothing

        }



        /// <summary>

        /// Execute is called immediately before the RDO is deleted.

        /// </summary>

        /// <returns></returns>

        public override kCura.EventHandler.Response Execute()

        {

            //Construct a response object with default values.

            kCura.EventHandler.Response eventResponse = new kCura.EventHandler.Response

            {

                // Note that returning a Success value of false does not

                // prevent the RDO deletion from proceeding.

                Success = true,

                Message = String.Empty

            };



            System.Data.SqlClient.SqlParameter workspaceArtifactIDParam = new System.Data.SqlClient.SqlParameter("@workspaceArtifactID", System.Data.SqlDbType.Int);

            workspaceArtifactIDParam.Value = this.Helper.GetActiveCaseID();

            System.Data.SqlClient.SqlParameter instanceArtifactIDParam = new System.Data.SqlClient.SqlParameter("@instanceArtifactID", System.Data.SqlDbType.Int);

            instanceArtifactIDParam.Value = this.ActiveArtifact.ArtifactID;



            this.Helper.GetDBContext(-1).ExecuteNonQuerySQLStatement(DELETE_OLD_ENTRIES_QUERY, new System.Data.SqlClient.SqlParameter[] { workspaceArtifactIDParam, instanceArtifactIDParam });



            return eventResponse;

        }



        /// <summary>

        /// Return a null object because Pre-Delete event handlers don't return any items in the Fields collection.

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get { return null; }

        }



        /// <summary>

        /// The Rollback method does not rollback any action taken by the event handler.  Rather, it is a hook,

        /// called by the Relativity framework immediately after the SQL transaction (in which the

        /// RDO is being deleted) is rolled back.

        /// </summary>

        public override void Rollback()

        {

            //Do nothing

        }

    }

}
```

On this page

- Pre Delete event handlers

- Guidelines for Pre Delete event handlers

- Code sample for a Pre Delete event handler


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
