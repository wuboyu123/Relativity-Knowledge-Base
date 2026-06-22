---
title: "Post Install event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Post_Install_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:28:54+00:00
sha256: 554f081f3eb298e5af105ea6e7a8cbbeaa1c96eab2ad29f6665eccd7f6471fcd
---

Post Install event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Post Install event handlers

You can develop Post Install event handlers that execute immediately after the user installs an application. You can identify the execution type of these event handlers and the order in which you want them to run. The following examples illustrate how you can use Post Install event handlers:

- Set default values on fields immediately after an application is installed. You could use a Post Install event handler to set a Choice field on an RDO.

You can use Post Install event handlers that run only once to avoid resetting the default values on object type instances during the upgrade of an application. The use of these event handlers prevents any updates to these instances from being overwritten. See Upgrading applications on the Relativity Documentation site.

- Run a Post Install event handler to create new instances of RDOs in a newly installed application. For more information, see Pre and Post Install event handlers .

## Guidelines for Post Install event handlers

Use these guidelines when developing Post Install event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Set the RunTarget attribute - indicate the context that your event handler executes against by specifying an enum from the Helper RunTargets enumeration. The options include Workspace, Instance, and InstanceAndWorkspace. For more information, see Set the RunTarget attribute on event handlers .

- Inherit from the PostInstallEventHandler class – ensure that you extend the PostInstallEventHandler base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

Post Install Event Handlers are not triggered when a workspace is created from a template. If you want to specify events after workspace creation, use a Post Workspace Create Event Handler. For more information, see Post Workspace Create event handlers .

## Code sample for a Post Install event handler

Review the following sample code for the SampleRunOncePostInstallEventHandler class. It illustrates how to set the RunOnce attribute, which allows the event handler to execute only a single time. When the event handler executes, it creates a queue table in the EDDS database.

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
using System;

using System.Runtime.InteropServices;

using kCura.EventHandler;

using kCura.EventHandler.CustomAttributes;

using Relativity.API;

namespace Examples.EventHandlers.Install

{

    /// <summary>

    /// This event handler runs once when the application is installed and creates a queue table in the EDDS database.

    /// </summary>

    [RunOnce(true)]

    [Description("Example create queue table event handler")]

    [RunTarget(kCura.EventHandler.Helper.RunTargets.Instance)]

    [Guid("c9df616d-d51b-48ae-b9f4-3ce4135c59c5")]

    public class ExamplePostInstallEventHandler : PostInstallEventHandler

    {

        public override Response Execute()

        {

            //Construct a response object with default values.

            Response retVal = new Response();

            try

            {

                //Get the EDDS database context.

                IDBContext eddsDBContext = Helper.GetDBContext(-1);

                //Run the SQL statement to create the table.

                CreateEDDSTablesIfNotExists(eddsDBContext);

                //Write message that appears on application details for installation.

                retVal.Message = "Successfully created ExampleMessageQueue table in the EDDS database";

                retVal.Success = true;

            }

            catch (Exception ex)

            {

                //Catch an exception if it occurs and fail the install if the tables aren't created successfully.

                retVal.Success = false;

                retVal.Message = ex.Message;

            }

            return retVal;

        }

        /// <summary>

        /// Create a MyMessageQueue table in EDDS to act as a queue.

        /// </summary>

        /// <param name="eddsDBContext">A properly constructed EDDS database context</param>

        private static void CreateEDDSTablesIfNotExists(IDBContext eddsDBContext)

        {

            string sql = @"

IF NOT EXISTS(SELECT 'true' FROM [INFORMATION_SCHEMA].[TABLES] WHERE [TABLE_NAME] = 'ExampleMessageQueue')

BEGIN

    CREATE TABLE [ExampleMessageQueue] (

        [ID] INT NOT NULL IDENTITY(1,1),

        [WorkspaceArtifactID] INT NOT NULL,

        [Message] NVARCHAR(MAX),

        [Status] INT NOT NULL,

        [ErrorMessage] NVARCHAR(MAX) NULL

    )

END

";

            eddsDBContext.BeginTransaction();

            try

            {

                eddsDBContext.ExecuteNonQuerySQLStatement(sql);

                eddsDBContext.CommitTransaction();

            }

            catch

            {

                eddsDBContext.RollbackTransaction();

                throw;

            }

        }

    }

}
```

On this page

- Post Install event handlers

- Guidelines for Post Install event handlers

- Code sample for a Post Install event handler


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
