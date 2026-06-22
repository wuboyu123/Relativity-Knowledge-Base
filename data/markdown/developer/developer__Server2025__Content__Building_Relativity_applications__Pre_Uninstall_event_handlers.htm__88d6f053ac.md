---
title: "Pre Uninstall event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Pre_Uninstall_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:29:06+00:00
sha256: 950fb4df476d44329508954718f4d330c878f223f61557c0c1114be2a4e03089
---

Pre Uninstall event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre Uninstall event handlers

You can use Pre Uninstall event handlers to perform cleanup tasks associated with removing an application from workspaces or from your Relativity environment, such as deleting choices, fields, objects, and other items. It executes immediately after an agent starts running an uninstall job. For example, you can add functionality to clear entries from database tables or to drop unneeded tables.

## Guidelines for Pre Uninstall event handlers

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PreUninstallEventHandler class – ensure that you extend the PreUninstallEventHandler base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Pre Uninstall event handler

Review the following sample code for the SamplePreUninstallEventHandler class. This code sample illustrates how to verify that an application is installed in a workspace. It also illustrates how to use the workspace ArtifactID to delete rows from a queue table, and how to drop a local workspace table.

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
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
using System;

using System.Data.SqlClient;

using System.Runtime.InteropServices;

using kCura.EventHandler;

using kCura.EventHandler.CustomAttributes;

using Relativity.API;

namespace Examples.EventHandlers.Install

{

    /// <summary>

    /// This event handler runs when the application is uninstalled and deletes a queue table from the EDDS database.

    /// </summary>

    [Description("Example uninstall event handler")]

    [Guid("B25E0A6D-57B5-416B-9110-69DD86A07B5A")]

    public class ExamplePreUninstallEventHandler : PreUninstallEventHandler

    {

        private static Guid EXAMPLE_APPLICATION_GUID = new Guid("B4F52C6C-F55C-488F-BA71-E8EE8B5C74F4");

        public override Response Execute()

        {

            //Construct a response object with default values.

            Response retVal = new Response();

            try

            {

                //Get the EDDS database context.

                IDBContext eddsDBContext = this.Helper.GetDBContext(-1);

                //Get the current workspace artifactID.

                int currentWorkspaceID = this.Helper.GetActiveCaseID();

                //Get the current workspace database context.

                IDBContext workspaceDBContext = this.Helper.GetDBContext(currentWorkspaceID);

                //Determine how many workspaces have this application installed.

                if (!IsLastApplicationInEnvironment(eddsDBContext, currentWorkspaceID))

                {

                    //If this application is installed on other workspaces, leave the table and delete entries for this workspace only.

                    RemoveWorkspaceEntriesFromQueueTable(eddsDBContext, currentWorkspaceID);

                }

                else

                {

                    //If this application isn't installed on any other workspaces, drop the queue table.

                    DropEDDSWorkspaceTablesIfExists(eddsDBContext);

                }

                retVal.Message = string.Empty;

                retVal.Success = true;

            }

            catch (Exception ex)

            {

                //Catch an exception if it occurs and fail the uninstall.

                retVal.Success = false;

                retVal.Message = ex.ToString();

            }

            return retVal;

        }

        /// <summary>

        /// Check to see if the application is installed in any other cases, or if this the last one.

        /// </summary>

        /// <param name="eddsDBContext">A properly constructed EDDS database context</param>

        /// <param name="currentWorkspaceID">Current workspace ArtifactID</param>

        /// <returns>True if no other workspaces have this application installed. False if other workspaces have this application installed.</returns>

        private static bool IsLastApplicationInEnvironment(IDBContext eddsDBContext, int currentWorkspaceID)

        {

            string applicationCountSQL = @"

DECLARE @applicationID INT = (SELECT [ArtifactID] FROM [LibraryApplication] WHERE [GUID] = @applicationGUID)

SELECT

    COUNT([CaseApplicationID])

FROM

    [CaseApplication]

WHERE

    [ApplicationID] IN (SELECT [ArtifactID] FROM [LibraryApplication] WHERE [GUID] = @applicationGUID)

    AND

    [CaseID] <> @workspaceArtifactID

";

            SqlParameter applicationGUIDParam = new SqlParameter("@applicationGUID", System.Data.SqlDbType.UniqueIdentifier)

            {

                Value = EXAMPLE_APPLICATION_GUID

            };

            SqlParameter workspaceArtifactIDParam1 = new SqlParameter("@workspaceArtifactID", System.Data.SqlDbType.Int)

            {

                Value = currentWorkspaceID

            };

            int installCount = eddsDBContext.ExecuteSqlStatementAsScalar<int>(applicationCountSQL, applicationGUIDParam, workspaceArtifactIDParam1);

            return installCount == 0;

        }

        /// <summary>

        /// Remove all workspace entries from queue table in the EDDS database.

        /// </summary>

        /// <param name="eddsDBContext">A properly constructed EDDS database context</param>

        /// <param name="currentWorkspaceID">Current workspace ArtifactID</param>

        private static void RemoveWorkspaceEntriesFromQueueTable(IDBContext eddsDBContext, int currentWorkspaceID)

        {

            string deleteWaitingJobsSQL = "DELETE FROM [ExampleMessageQueue] WHERE [WorkspaceArtifactID] = @workspaceArtifactID";

            SqlParameter workspaceArtifactIDParam = new SqlParameter("@workspaceArtifactID", System.Data.SqlDbType.Int)

            {

                Value = currentWorkspaceID

            };

            eddsDBContext.ExecuteNonQuerySQLStatement(deleteWaitingJobsSQL, new[] { workspaceArtifactIDParam });

        }

        /// <summary>

        /// Drop the EDDS tables from the environment when they are no longer needed.

        /// </summary>

        /// <param name="eddsDBContext">A properly constructed EDDS database context</param>

        private static void DropEDDSWorkspaceTablesIfExists(IDBContext eddsDBContext)

        {

            string sql = FormatDropTableSQL("ExampleMessageQueue");

            eddsDBContext.ExecuteNonQuerySQLStatement(sql);

        }

        /// <summary>

        /// Create a SQL statement to check if a table exists and drop the table if it does.

        /// </summary>

        /// <param name="tableName">Name of the table to look for</param>

        /// <returns></returns>

        private static string FormatDropTableSQL(string tableName)

        {

            return $"DROP TABLE IF EXISTS [{tableName}]";

        }

    }

}
```

On this page

- Pre Uninstall event handlers

- Guidelines for Pre Uninstall event handlers

- Code sample for a Pre Uninstall event handler


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
