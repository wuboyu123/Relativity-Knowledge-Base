---
title: "Script Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Script_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:04+00:00
sha256: 87996e901f07bb61dae9ffab7cfee1c33c7adf1eb4b5ba8b303e3e1295dfb00b
---

Script Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Script Manager (.NET)

In Relativity, you can execute SQL scripts through the UI that act on the databases backing an instance. You can implement these scripts to customize and extend Relativity functionality. For more information, see Scripts on the Relativity Documentation site.

If you use a Relativity script in a custom development project, it is recommended to make a copy of the script and use the copied script in your project. Software updates may modify the scripts provided by Relativity, which could cause unintended results if you use the Relativity-provided scripts directly in your custom development projects.

The Relativity Script Manager API exposes methods for interacting with scripts as follows:

- Using CRUD operations on a script

- Retrieving script input parameters

- Previewing a script and its input parameters

- Importing a scripting

- Running jobs on a script, such as retrieving its status, exporting results, and others.

Use this API to create standalone applications that manage scripts across multiple environments or across workspaces in a single environment.

You can also use the Script service through REST. For more information, see Script service .

## Script Manager API fundamentals

### Key concepts

For a script to be run (once queued) a Script Run Manager agent must be running in the environment.

Methods - the following gives a brief list of the methods available in the service

Click here to view methods.

- CreateAsync() - creates a new script in the environment.

- ReadAsync() - reads a single script from the environment.

- UpdateAsync() - modifies a script.

- DeleteAsync() - deletes a script.

- ImportAsync() - pushes a script from the admin script library into workspace script libraries.

- GetScriptParametersAsync() - retrieves a list of all input parameters defined for a given script.

- PreviewScriptAsync() - returns a string representing the SQL that will be executed with specified input values applied to the script.

- EnqueueRunJobAsync () - queues a script for execution by the Script Run Manager agent.

- ReadRunJobAsync () - reads that status of script run job (Queued, Completed, Errored, etc.).

- QueryActionJobResultsAsync () - returns completed script action results that match query filter/sort conditions.

- ExportActionResultsAsync () - returns the completed script action results in .csv format.

- ExportScriptReportAsync () - returns completed script results (all actions) in the specified file format (HTML, CSV, PDF, XLS, XLSX, RTF, PNG).

- CleanupRunJobAsync () - cleans up all temporary tables created as part of a script run job.

Models - the following lists data models used in the Script Manager service.

Click here to view models.

- ScriptImportRequest - identifies an admin script to be imported into a workspace script library.

- ScriptRequest - represents the entirety of the script (in xml) to create.

- ScriptResponse - contains the xml of the script being read including related metadata.

- ScriptParameterDetails - contains information about the defined inputs of a given script, including possible values they can take.

- MultiScriptInput - used to specify values to a multi-value script input.

- SingleScriptInput - used to specify a value for a single-value script input.

- EnqueueRunJobResponse - response from enqueue run job endpoint providing script run identifier (GUID) used to check job status and results.

- RunJob - response from read run job endpoint, contains information about status of script run job.

- ActionQueryRequest - used to specify criteria for action results query.

- ActionResultsQueryResponse - response from query action job results endpoint. Contains action results matching query criteria.

- ExportActionResultsRequest - used in export action results endpoint, to specify query criteria of action results to include in exported CSV formatted file.

- ExportScriptReportRequest - used to specify the file type in which to export the script results.

### Troubleshooting information

For more complicated scripts, it is often easier to implement and debug the script body using SQL Server Management Studio directly.

## Add a script

To add a script to Relativity, call the CreateAsync method by passing in the following parameters:

- workspaceID - the ArtifactID of the workspace where the script should be created. Use -1 to indicate the admin workspace.

- scriptRequest - a request object containing the data used to create the script.

This method returns the Artifact ID of the new script.

Click here to view code sample. Copy

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
public async Task CreateNewScriptAsync()

{

    string scriptBody =

@"<script>

    <name>My script Name</name>

    <description>About my script</description>

    <category></category>

    <input>

        <constant id=""count"" name=""Rows"" type=""number"" />

    </input>

    <display type=""itemlist"" />

    <action returns=""table"">

    <![CDATA[

        SELECT TOP(CAST(#count# AS INT)) * FROM [eddsdbo].[Artifact]

    ]]></action>

</script>";



    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            Relativity.Extensibility.V1.Scripts.Models.ScriptRequest scriptRequest = new Relativity.Services.Interfaces.Scripts.Models.ScriptRequest

            {

                ScriptBody = scriptBody,

                RelativityApplications = null

            };

            int workspaceID = 1015024;

            int scriptID = await scriptManager.CreateAsync(workspaceID, scriptRequest);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve script metadata

Method is overloaded for optional metadata and action data.

The ReadAsync method retrieves basic metadata for a script, including its name, body and other parameters.

- workspaceID - the ArtifactID of the workspace where the script should be created. Use -1 to indicate the admin workspace.

- scriptID - the Artifact ID of the script to retrieve.

Click here to view code sample. Copy

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
public async Task ReadScriptAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            int scriptID = 1021467;

            ScriptResponse response = await scriptManager.ReadAsync(workspaceID, scriptID);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Modify a script

The UpdateAsync () method modifies a script by passing the following parameters to it:

- workspaceID - the ArtifactID of the workspace where the script should be updated. Use -1 to indicate the admin workspace.

- scriptID - the Artifact ID of the script.

- scriptRequest - a request object containing the data used to update the script.

Click here to view a code sample Copy

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
public async Task UpdateScriptAsync()

{

    string scriptBody =

@"<script>

    <name>My script Name</name>

    <description>About my script</description>

    <category></category>

    <input>

        <constant id=""count"" name=""Rows"" type=""number"" />

    </input>

    <display type=""itemlist"" />

    <action returns=""table"">

    <![CDATA[

        SELECT TOP(CAST(#count# AS INT)) * FROM [eddsdbo].[Field]

    ]]></action>

</script>";;



    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            Relativity.Extensibility.V1.Scripts.Models.ScriptRequest scriptRequest = new Relativity.Extensibility.V1.Scripts.Models.ScriptRequest

            {

                ScriptBody = scriptBody,

                RelativityApplications = null

            };

            int workspaceID = -1;

            int scriptID = 1021467;

            await scriptManager.UpdateAsync(workspaceID, scriptID, scriptRequest);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete a script

The DeleteAsync method deletes a script by passing it the following parameters:

- workspaceID - the ArtifactID of the workspace where the script should be deleted. Use -1 to indicate the admin workspace.

- scriptID - the Artifact ID of the script.

Click here to view a code sample. Copy

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
public async Task DeleteScriptAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            int scriptID = 123456;

            await scriptManager.DeleteAsync(workspaceID, scriptID);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Import a script

The ImportAsync method imports a script from the admin library to the workspace script library when you pass it the following parameters:

- workspaceID - the ArtifactID of the workspace where the script should be imported to. Use -1 to indicate the admin workspace.

- scriptID - the Artifact ID of the script.

- scriptImportRequest - a request object containing the data used to import the script from the script library.

The method returns the Artifact ID of the imported script in the workspace.

Click here to view a code sample. Copy

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
public async Task ImportScriptAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = 1015024;

            ScriptImportRequest importRequest = new ScriptImportRequest

            {

                LibraryScript = new ObjectIdentifier

                {

                    // artifact ID of script in admin script library

                    // to import into workspace script library.

                    ArtifactID = 1021467

                }

            };

            int workspaceScriptID = await scriptManager.ImportAsync(workspaceID, importRequest);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve script input parameters

The GetScriptParametersAsync method retrieves a list of the input parameters defined in a given script when you pass it the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- scriptID - the Artifact ID of the script.

The method returns a list of ScriptParameterDetail objects containing information about the inputs for the script.

Click here to view a code sample. Copy

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
public async Task GetScriptParametersAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            int scriptID = 123456;

            List<ScriptParameterDetails> response = await scriptManager.GetScriptParametersAsync(workspaceID, scriptID);



            // Construct script inputs based on parameter detail response.

            // See PreviewScriptAsync and EnqueueRunJobAsync methods that take ScriptInput objects as parameters.

            List<ScriptInput> scriptInputs = new List<ScriptInput>();

            foreach (var scriptParameter in response)

            {

                ScriptInput input = new SingleScriptInput()

                {

                    ID = scriptParameter.Id,

                    Value = GetScriptInputValueByName(scriptParameter.Name) // <-- Hypothetical method providing valid input value.

                };

                scriptInputs.Add(input);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Preview a script

The PreviewScriptAsync method is used to examine a script body (with input values applied) before running it, by passing it the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- inputs - a list of values for all defined inputs of the script.

The method returns a string representing the SQL query that will be executed when the script is run (with input values applied).

Click here to view a code sample. Copy

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
public async Task GetScriptPreviewAsync()

{

    using (Relativity.Services.Interfaces.Script.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Services.Interfaces.Script.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            int scriptID = 1022818;

            List<ScriptInput> inputs = new List<ScriptInput>()

            {

                new SingleScriptInput()

                {

                    ID = "count",

                    Value = "7"

                }

            };

            string scriptBody = await scriptManager.PreviewScriptAsync(workspaceID, scriptID, inputs);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Queue a script to run

The EnqueueRunJobAsync method queues a script to be run when you pass it the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- inputs - a list of inputs required by the script.

- timeZoneOffet - specifies a time zone offset value (referenced in the script body with #TimeZoneOffset#).

- Return value - an EnqueueRunJobResponse object containing a script run job unique identifier used to obtain run job status and script results.

Click here to view a code sample. Copy

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
public async Task RunScriptAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            int scriptID = 1022744;

            List<ScriptInput> inputs = new List<ScriptInput>()

            {

                new SingleScriptInput()

                {

                    ID = "count",

                    Value = "7"

                }

            };

            EnqueueRunJobResponse enqueueResponse = await scriptManager.EnqueueRunJobAsync(workspaceID, scriptID, inputs, 0);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

You should call the CleanupRunJobAsync method once querying the results of your script job has finished.

## Retrieve status of a script run job

The ReadRunJobAsync method returns the status of the script run job and each action contained in the script when you pass it the following parameters.

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- runJobID - run job identifier contained in the EnqueueRunJobResponse object.

The method returns the status of each action in the queued script.

Run Job Status:

- Queued - the job has been successfully submitted and is queued to be run.

- InProgress - the job is actively being run.

- Completed - all actions have been run and completed without error.

- CompletedWithErrors - all actions have been run and one or more have errored.

- FailedToComplete - the job failed to complete.

- AgentHasNotCheckedIn - the Agent has missed multiple consecutive check-ins.

Action Job Status:

- Queued - the job has been successfully submitted and is queued to be run.

- InProgress - the job is actively being run.

- Completed - the job has successfully completed without error.

- Errored - the job has been run and has errored.

Click here to view a code sample. Copy

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
public async Task ScriptRunStatusAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            Guid runJobID = new Guid("0d2d724b-999e-47dc-a206-2dcf17f910b3");

            RunJob statusResponse = await scriptManager.ReadRunJobAsync(workspaceID, runJobID);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Query action results

The QueryActionJobResultsAsync method returns completed script action results that match query filter and sort criteria when you pass in the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- runJobID - run job identifier contained in the EnqueueRunJobResponse object.

- actionIndex - zero-based index of script action to query. Scripts can have multiple action sections, which are executed in sequence. The actionIndex parameter refers to these actions. A value of 0 refers to the first action in the script, 1 refers to the second action, etc. All scripts have at least one action section; 0 will always work. If 1 is entered for a script with only a single action section, an error will be returned.

- actionQueryRequest - query condition criteria. See Object Manager query syntax for details.

- start - used for pagination. Zero-index of first row in the response.

- length - used for pagination. Number of rows in response. If this value is 0 (or not set) it will default to 10,000. Values larger than 10,000 results will be respected if specified.

The method returns results from script actions matching query criteria and pagination values.

For performance reasons, use paging in the result set by specifying the 'start' and 'length' parameters for large result sets.

Click here to view a code sample. Copy

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
public async Task QueryScriptActionResultsAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            Guid runJobID = new Guid("0d2d724b-999e-47dc-a206-2dcf17f910b3");

            ActionQueryRequest queryRequest = new ActionQueryRequest()

            {

                ColumnNames = new List<string>() { "Name", "ArtifactID" },

                Condition = "'Name' LIKE 'important'",

                Sorts = new List<ActionColumnSort>() { new ActionColumnSort() {ColumnName = "Name"}}

            };

            ActionResultsQueryResponse actionQueryResponse = await scriptManager.QueryActionJobResultsAsync(workspaceID, runJobID, 0, queryRequest, 0, 20);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Export action results

The ExportActionResultsAsync method returns completed script action results that match query filter/sort conditions when you pass in the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- runJobID - run job identifier contained in the EnqueueRunJobResponse object.

- actionIndex - zero-based index of script action to query.

- actionExportRequest - contains an ActionQueryRequest parameter to provide filter and sort criteria to be applied to returned results.

The method exports a stream containing results from script action matching query criteria and pagination values to a CSV formatted text file.

ExportActionResults does not provide 'start' and 'length' parameters, and it will always return all rows returned by the SQL script. For performance reasons, you may want to use QueryActionJobResults instead and use paging by specifying the 'start' and 'length' parameters in QueryActionJobResults.

Click here to view a code sample. Copy

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
public async Task ExportScriptActionResultsAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            Guid runJobID = new Guid("0d2d724b-999e-47dc-a206-2dcf17f910b3");

            ExportActionResultsRequest actionExportRequest = new ExportActionResultsRequest() {

            QueryRequest = new ActionQueryRequest()

                {

                    ColumnNames = new List<string>() { "Name", "ArtifactID" },

                    Sorts = new List<ActionColumnSort>() { new ActionColumnSort() { ColumnName = "Name" } }

                }

            };

            IKeplerStream exportStream = await scriptManager.ExportActionResultsAsync(workspaceID, runJobID, 0, actionExportRequest);

            using (FileStream file = File.Create(@"C:\ScriptActionResults.csv"))

            {

                await exportStream.GetStreamAsync().Result.CopyToAsync(file);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Export script report

The ExportScriptReportAsync method returns completed script results (for all actions) that match query filter/sort conditions when you pass in the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- runJobID - run job identifier contained in the EnqueueRunJobResponse object.

- scriptExportRequest - used to specify the file type of the exported script results (HTML, CSV, PDF, XLS, XLSX, RTF, PNG).

The method returns a stream containing script results in the specified file format.

Click here to view a code sample. Copy

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
public async Task ExportScriptResultsAsync()

{

    using (Relativity.Extensibility.V1.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.V1.Scripts.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            Guid runJobID = new Guid("0d2d724b-999e-47dc-a206-2dcf17f910b3");

            ExportScriptReportRequest exportRequest  = new ExportScriptReportRequest()

            {

                FileType = ExportFileType.PDF

            };

            IKeplerStream exportStream = await scriptManager.ExportScriptReportAsync(workspaceID, runJobID, exportRequest);

            using (FileStream file = File.Create(@"C:\ScriptResults.pdf"))

            {

                await exportStream.GetStreamAsync().Result.CopyToAsync(file);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Clean up script results

The CleanupRunJobAsync method cleans up all temporary tables created as part of a script run job when you pass in the following parameters:

- workspaceID - the ArtifactID of the workspace containing the script. Use -1 to indicate the admin workspace.

- runJobID - run job identifier contained in the EnqueueRunJobResponse object.

Once this method has been called the script results are no longer available for querying or export.

Click here to view a code sample. Copy

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
public async Task CleanUpScriptAsync()

{

    using (Relativity.Services.Interfaces.Script.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Services.Interfaces.Script.IScriptManager>())

    {

        try

        {

            int workspaceID = -1;

            Guid runJobID = new Guid("0d2d724b-999e-47dc-a206-2dcf17f910b3");

            await scriptManager.CleanupRunJobAsync(workspaceID, runJobID);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

On this page

- Script Manager (.NET)

- Script Manager API fundamentals

- Key concepts

- Troubleshooting information

- Add a script

- Retrieve script metadata

- Modify a script

- Delete a script

- Import a script

- Retrieve script input parameters

- Preview a script

- Queue a script to run

- Retrieve status of a script run job

- Query action results

- Export action results

- Export script report

- Clean up script results


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
