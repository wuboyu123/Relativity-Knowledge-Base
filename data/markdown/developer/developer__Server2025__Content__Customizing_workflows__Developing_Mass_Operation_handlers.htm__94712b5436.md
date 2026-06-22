---
title: "Develop Mass Operation handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Developing_Mass_Operation_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:40+00:00
sha256: dbee41f341771cda9bb804b400c89c168f3e156054ad05c7e87c8297d505750a
---

Develop Mass Operation handlers

# Develop Mass Operation handlers

You can create Mass Operation handlers that perform custom mass operations. For example, you can develop a Mass Operation handler that submits a group of objects to an agent for some type of processing. You can also use a Mass Operation handler to update related items when a group of objects undergoes a mass edit. In Relativity, the drop-down menu in the mass operations bar displays your custom mass operations.

To create a custom mass operation, you develop a class that inherits from the MassOperationHandler class. It resides in the kcura.EventHandler assembly under the kCura.MassOperationHandlers namespace. You can then add your custom Mass Operation handler as a resource file and associate it with an object type or an application in Relativity.

You can also develop custom mass operations that use custom pages rather than Mass Operation handlers. After implementing the custom page, you can associate it with an object type in Relativity. For example, you might want to use custom page for the development of a mass operation that displays a graphical data summary for a group of objects. See Creating and editing Relativity Objects .

## Guidelines for Mass Operation handlers

- Create a new class in Visual Studio

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages. See Best practices for building applications .

- Add a GUID for the Mass Operation handler – set the System.Runtime.InteropServices.Guid to the GUID identifying your Mass Operation handler. Use the GUID generator in Visual Studio.

- Set the Description attribute – provide a description for the Mass Operation that you want to appear in the Relativity UI.

- Inherit from the MassOperationHandler class – extend the base class for the MassOperationHandler event handler.

- Override the required methods – see the following list:

- ValidateSelection() method – implement code that performs a validation step and returns a message to the user if necessary.

- ( Optional) ValidateLayout() method – implement code that runs a Pre Save event handler on the data entered in a layout. You don't need to implement this method if you aren't using a layout.

- PreMassOperation() – implement code that performs a setup action required before the mass operation occurs. For example, you might include code for creating an instance of an object.

- DoBatch() – implement code that you want executed on batches of objects. You can set the batch size in the MassCustomBatchAmount instance setting on the Instance Settings tab. For more information, see Instance settings' descriptions on the Relativity Server 2025 Documentation site.

- PostMassOperation() – implement code that performs any action required after the batching completes.

- Upload your Mass operation handler assembly to Relativity – use the Resource Files tab to upload your compiled .dll file to Relativity. See Resource Files on the Relativity Documentation site.

- Add your mass operation to an object type or an application – perform one of the following tasks in Relativity:

- Click the Object Types tab. Next, click the name of the object type that you want to associate with your Mass Operation handler. You can also create a new object type. Click New on the Mass Operation list to add your handler. For more information, see Creating and editing Relativity Objects .

- Click the Relativity Application tab. Next, click the name of the application that you want to associate with your Mass Operation handler. Click Link on the Mass Operation list to add your handler. For more information, see Create an application in Relativity .

## Code sample for a Mass Operation handler

Review the following code sample for a Mass Operation handler.

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
using System.ComponentModel;

using System.Runtime.InteropServices;

using kCura.MassOperationHandlers;

using kCura.Relativity.Client;

using Relativity.API;

namespace MassOperationsTest

{

    [Guid("1EF284EE-87A9-42EE-BF0A-4C0D9237F1E1")]

    [Description("Sample Mass Operation.")]

    class MassOperationDocExample : MassOperationHandler

    {

        /*Occurs after the user has selected items and pressed go. In this function

          you can validate the items selected and return a warning/error message*/

        public override kCura.EventHandler.Response ValidateSelection()

        {

            kCura.EventHandler.Response response = new kCura.EventHandler.Response()

            {

                Success = true,

                Message = "WARNING: This operation permanantly edits the selected objects. Please be certain you wish to proceed"

            };

            int workspace_id = this.Helper.GetActiveCaseID();

            /*Validate the count of item. Fail validation if not even*/

            string sqlText = "SELECT COUNT(*) FROM [Resource].[" + this.MassActionTableName + "]";

            int count = (int)this.Helper.GetDBContext(workspace_id).ExecuteSqlStatementAsScalar(sqlText);

            if (count % 2 != 0)

            {

                response.Success = false;

                response.Message = "This mass operation requires an even number of items to function";

            }

            return response;

        }

        /*Occurs after the user has inputted data to a layout and pressed Ok. This function runs as a pre-save

         eventhandler. This is NOT called if the mass operation does not have a layout*/

        public override kCura.EventHandler.Response ValidateLayout()

        {

            kCura.EventHandler.Response response = new kCura.EventHandler.Response()

            {

                Success = true,

                Message = "WARNING: This operation permanently edits the selected objects. Please be certain you wish to proceed."

            };

            /*Validate the string input length.*/

            if (this.LayoutMask.Fields["E09387A3-701D-4CAD-AD46-AA1C7476BB15"].Value.Value.ToString().Length < 30)

            {

                response.Success = false;

                response.Message = "This mass operation requires an input text greater than 30 characters.";

            }

            return response;

        }

        /*Occurs before batching begins. A sample use would be to set up an instance of an object*/

        public override kCura.EventHandler.Response PreMassOperation()

        {

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            retVal.Message = "Successful Pre Execute Operation method";

            return retVal;

        }

        /*This function is called in batches based on the size defined in configuration.*/

        public override kCura.EventHandler.Response DoBatch()

        {

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            this.ChangeStatus("Batch is executing");

            return retVal;

        }

        /*Occurs after all batching is completed*/

        public override kCura.EventHandler.Response PostMassOperation()

        {

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            retVal.Message = "Successful Post Execute Operation method";

            return retVal;

        }

    }

}
```

## Convert legacy custom mass operations

Relativity Server 2025 supports the development of custom mass operations that use custom pages or Mass Operation handlers. You can add these entities directly to object types and applications. The following instructions describe how to convert legacy custom mass operations. The describe how to use the custom page option and to refactor your legacy code. For information, see Code sample for a Mass Operation handler .

While Relativity Server 2025 continues to support legacy custom mass operations, we recommend that you develop all new custom mass operations as Mass Operation handlers. Legacy custom mass operations are only supported on Relativity 8.2 and below.

Use the following steps as a workflow for this conversion process:

- In Relativity, navigate to the Object Type tab. For more information, see Creating and editing Relativity Objects .

- Filter for the Document object type and click on it to display the details view.

- In the Mass Operations section, click New .

- Perform these tasks on the Add New Mass Operation dialog:

- Enter the Name of your mass operation.

- Select Custom Page in the Pop-up Directs To field.

- In the Custom Page URL field, enter the URL for your legacy custom page.

- Enter the values for the default height and width of your custom page in pixels.

- Refactor the database connection code in your legacy custom page. To access the select IDs, use the new query string variable called DatabaseToken to obtain the table name. Next, run a query against that table using the DBContext methods in the ConnectionHelper class in the Relativity.CustomPages.dll.

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
//START DATABASE AND MASS OPERATION INFORMATION READING

string databasetoken = "empty";

string artifacttypeid = "empty";

string appid = "empty";

//artifacttypeid

//appid

try

{

    databasetoken = Request.QueryString["DatabaseToken"];

    if (databasetoken == null)

    {

        databasetoken = "Database Token is null";

    }

}

catch

{

    databasetoken = "No Database Token parameter was passed. Are you using this custom page for mass operations?";

}

try

{

    appid = Request.QueryString["appid"];

    if (appid == null)

    {

        appid = "App ID is null";

    }

}

catch

{

    appid = "No App ID was passed";

}

try

{

    artifacttypeid = Request.QueryString["artifacttypeid"];

    if (artifacttypeid == null)

    {

        artifacttypeid = "Artifact Type ID is null";

    }

}

catch

{

    artifacttypeid = "No Artifact Type ID was passed";

}

string query = "SELECT [WorkspaceID]  ,[ServerName]  ,[TableName] ,[ObjectType] FROM [MassOperationTokenInfo] WHERE [TokenID] = @tokenID";

SqlParameter param = new System.Data.SqlClient.SqlParameter("@tokenID", databasetoken);

Relativity.API.IDBContext context = ConnectionHelper.Helper().GetDBContext(-1);

DataTable table = context.ExecuteSqlStatementAsDataTable(query, new List<System.Data.SqlClient.SqlParameter>() { param });

DataRow row = table.Rows[0];

string serverName = row["ServerName"].ToString();

string tableName = row["TableName"].ToString();

string WorkspaceID = row["WorkspaceID"].ToString();

string ObjectType = row["ObjectType"].ToString();

context.ReleaseConnection();

//write new query to get all ids from tableName

string query_ids = string.Format("SELECT [ArtifactID] FROM [Resource].[{0}]", tableName);

Relativity.API.IDBContext caseContext = ConnectionHelper.Helper().GetDBContext(Convert.ToInt32(WorkspaceID));

DataTable guidTable = caseContext.ExecuteSqlStatementAsDataTable(query_ids);

List<string> someNumbers = new List<string>();

foreach (DataRow guidrow in guidTable.Rows)

{

    someNumbers.Add(guidrow["ArtifactID"].ToString());

}

// transfer data to ViewBag

caseContext.ReleaseConnection();

//END DATABASE AND MASS OPERATION INFORMATION
```
