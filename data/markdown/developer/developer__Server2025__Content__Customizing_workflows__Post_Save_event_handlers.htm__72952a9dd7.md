---
title: "Post Save event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Post_Save_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:28:56+00:00
sha256: e73a347c467ec55d1c30b80f4639dc790ca0973e08de7611eaece3264adc0764
---

Post Save event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Post Save event handlers

A Post Save event handler executes after a user clicks the Save or Save & Next button on a layout for a document or Relativity Dynamic Object (RDO) in the Relativity UI. It executes after the values entered by the user are written to the database as object properties. To modify the object properties after the event handler writes to the database, use the Relativity Services API to update the artifact. Because the user has clicked the Save or Save & Next button, the you can't cancel the save operation from an Post Save event handler. Post Save event handlers are supported only on documents and RDOs.

Use a Post Save event handler when you need to write the properties of one object to the database before you can instantiate a second object. For example, you may want to create an audit object after the event handler successfully saves another custom object. You can also use Post Save event handlers to send email notifications after a specific action is completed.

## Guidelines for Post Save event handlers

Use these guidelines when developing Post Save event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PostSaveEventHandler class – extend the PostSaveEventHandler base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Override the RequiredFields property – represents fields required on object creation.

- The ActiveArtifact.Fields collection includes the fields returned by the RequiredFields property, and those on the current layout. It also includes the values of these fields.

- Any Field in ActiveArtifact.Fields that is referenced in this event handler must be placed in the RequiredFields property.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Post Save event handler

Review the following code sample for a Post Save event handler.

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
using System;

using System.Data;

using System.Data.SqlClient;



namespace ExampleEventHandlers

{

    /// <summary>

    /// This event handler examines a single choice field on the RDO being saved

    /// to determine if the object has been marked as "Relevant".  If so the artifactID

    /// of the RDO is stored in an SQL table for further, say, examination by an agent.

    /// </summary>

    [kCura.EventHandler.CustomAttributes.Description("Example Post Save Event Handler")]

    [System.Runtime.InteropServices.Guid("E99A4D1A-5157-4481-8AF7-40E634C06F4A")]

    class ExamplePostSaveEventHandler : kCura.EventHandler.PostSaveEventHandler

    {



        private readonly Guid RELEVANT_FIELD_GUID = new Guid("5702F31B-48AC-4E2A-9000-A48B3E3ABDBF");



        public override kCura.EventHandler.Response Execute()

        {

            //Construct a default response object.

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response

            {

                Success = true,

                Message = String.Empty

            };



            try

            {

                // Get field by GUID

                kCura.EventHandler.Field relevantField = this.ActiveArtifact.Fields[RELEVANT_FIELD_GUID.ToString()];

                kCura.EventHandler.ChoiceCollection fieldValue = (kCura.EventHandler.ChoiceCollection)relevantField.Value?.Value;



                if (fieldValue != null)

                {

                    // Get field value using choice name

                    const string choiceName = "Relevant";

                    kCura.EventHandler.Choice choice = fieldValue[choiceName];



                    // If the field value is set to the "Relevant" choice

                    if (choice != null)

                    {

                        // Insert artifactID of "relevant" RDO into the table in the EDDS database

                        Relativity.API.IDBContext eddsDbContext = Helper.GetDBContext(-1);

                        int workspaceArtifactID = Helper.GetActiveCaseID();

                        int artifactID = ActiveArtifact.ArtifactID;

                        AddToSqlTable(eddsDbContext, workspaceArtifactID, artifactID);

                    }

                }

            }

            catch (System.Exception ex)

            {

                retVal.Success = false;

                retVal.Message = ex.ToString();

            }

            return retVal;

        }



        /// <summary>

        /// Ensure that you always have access to the fields in the ActiveArtifact.Fields collection even if they aren't on the current layout.

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get

            {

                kCura.EventHandler.FieldCollection retVal = new kCura.EventHandler.FieldCollection();

                retVal.Add(new kCura.EventHandler.Field(RELEVANT_FIELD_GUID));

                return retVal;

            }

        }



        /// <summary>

        /// Inserts the RDO identifier into a table in the EDDS database if it doesn't already exist.

        /// </summary>

        /// <param name="dbContext">A database context for the EDDS database</param>

        /// <param name="workspaceArtifactID">The workspace ArtifactID to insert</param>

        /// <param name="artifactID">The workspace ArtifactID of the RDO in question marked "relevant".</param>

        private void AddToSqlTable(Relativity.API.IDBContext dbContext, int workspaceArtifactID, int artifactID)

        {



            String sql = "IF NOT EXISTS(SELECT TOP 1 * FROM [MySQLTable] WHERE [WorkspaceArtifactID] = @workspaceArtifactID AND [ArtifactID] = @artifactID)"

                        + " BEGIN"

                        + " INSERT INTO [MySQLTable] (WorkspaceArtifactID, ArtifactID)"

                        + " Values (@WorkspaceArtifactID, @artifactID)"

                        + " END";

            SqlParameter workspaceArtifactIDParam = new SqlParameter("@WorkspaceArtifactID", SqlDbType.Int);

            workspaceArtifactIDParam.Value = workspaceArtifactID;

            SqlParameter artifactIDParam = new SqlParameter("@artifactID", SqlDbType.Int);

            artifactIDParam.Value = artifactID;

            dbContext.ExecuteNonQuerySQLStatement(sql, new SqlParameter[] { workspaceArtifactIDParam, artifactIDParam });

        }



    }

}
```

On this page

- Post Save event handlers

- Guidelines for Post Save event handlers

- Code sample for a Post Save event handler


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
