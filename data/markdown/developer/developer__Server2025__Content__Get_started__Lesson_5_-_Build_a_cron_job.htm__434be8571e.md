---
title: "Lesson 5 - Build a cron job"
url: https://platform.relativity.com/Server2025/Content/Get_started/Lesson_5_-_Build_a_cron_job.htm
collection: developer
fetched_at: 2026-06-22T06:24:58+00:00
sha256: 888d86b4fccf0b1740fb1505c160d34420e849f34793b29d0d42ea89999d024d
---

Lesson 5 - Build a cron job

# Lesson 5 - Build a cron job

Custom agents perform background processing within your application without interfering with user activities performed through the Relativity UI. You can implement agents as managers that monitor tasks or workers that perform specific jobs in your environment.

In this lesson, you will learn how to complete these tasks:

- Create an agent that runs on a set time interval.

- Debug an agent.

- Add an agent to your Relativity instance.

- Implement an agent for creating and updating documents using the Kepler Service constructed in Lesson 3 - Create a RESTful API .

- Test your agent.

Estimated completion time - 1 hour

This lesson describes all the steps necessary to build the agent but you can also download the completed code from WikipediaAgent.zip .

PREVIOUS LESSON

‹‹ Lesson 4 - Validate object changes

NEXT LESSON

Lesson 6 - Create a custom page ››

## Before you begin

- If you have not done so already, you should Create a nuget.config file so that your solution can target different nuget repositories for Relativity Server or RelativityOne.

## Step 1 - Create a basic agent

A cron job is the process of scheduling tasks to be executed at a future time. The agent framework in Relativity follows a similar approach when handling long running tasks.

Use the following steps to create an agent from a template:

- Open Visual Studio.

- Open the HelloWikipedia solution created in Lesson 3 - Create a RESTful API .

- Create a new project in the HelloWikipedia solution and select the Relativity Server Agent template.

- Click Next to display the Configure your new project dialog.

- Enter the following information:

- Project name - WikipediaAgent

- Location - This field is automatically populated with the solution path when you add a new project to the HelloWikipedia solution.

- Click Create .

- Verify that you have a C# project named WikipediaAgent .

- Rename the following items to match the code samples.

- File - rename RelativityAgent to WikipediaAgent .

- Class name - rename RelativityAgent to WikipediaAgent .

- Class name attribute - When you created the agent from the template, the GUID was automatically generated. Copy

```text
1
2
3
4
5
namespace WikipediaAgent

{

    [kCura.Agent.CustomAttributes.Name("Wikipedia Agent")]

    [System.Runtime.InteropServices.Guid("44ae8827-1c7f-422c-849d-197c1c0f5b68")]

    public class WikipediaAgent : AgentBase
```

- Name property Copy

```text
1
2
3
4
5
6
7
public override string Name

{

    get

    {

        return "Wikipedia Agent-";

    }

}
```

- Add the following code to update the Execute() method to display the message Hello World , and current date and time. Modify the Execute() method by updating the RaiseMessage() method call to include the string Hello World before the reporting the current date and time. Copy

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
using kCura.Agent;

using Relativity.API;

using Relativity.ObjectManager.V1.Interfaces;

using System;

using System.Net;

namespace WikipediaAgent {

  [kCura.Agent.CustomAttributes.Name("Wikipedia Agent")]

  [System.Runtime.InteropServices.Guid("7d1c6f96-f59b-4c96-a749-aaf0493b7e61")]

  public class WikipediaAgent: AgentBase {

    /// <summary>

    /// Agent logic goes here

    /// </summary>

    public override void Execute() {

      IAPILog logger = Helper.GetLoggerFactory().GetLogger();

      try {

        // Update Security Protocol

        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;

        //Get the current Agent artifactID

        int agentArtifactId = AgentID;

        //Get a dbContext for the EDDS database

        IDBContext eddsDbContext = Helper.GetDBContext(-1);

        //Get a dbContext for the workspace database

        //int workspaceArtifactId = 01010101; // Update it with the real

        //IDBContext workspaceDbContext = Helper.GetDBContext(workspaceArtifactId);

        //Get GUID for an artifact

        //int testArtifactId = 10101010;

        //Guid guidForTestArtifactId = Helper.GetGuid(workspaceArtifactId, testArtifactId);

        //Display a message in Agents Tab and Windows Event Viewer

        RaiseMessage("Hello World The current time is: " + DateTime.Now.ToLongTimeString(), 1);

        // To interact with Relativity, refer to the APIs documented on platform.relativity.com.

        // The Object Manager is one of the most popular APIs.

        // Relativity Services API (RSAPI) is obsolete and will not work.

        using (IObjectManager objectManager = this.Helper.GetServicesManager().CreateProxy < IObjectManager > (ExecutionIdentity.CurrentUser)) {

        }

        logger.LogVerbose("Log information throughout execution.");

      } catch (Exception ex) {

        //Your Agent caught an exception

        logger.LogError(ex, "There was an exception.");

        RaiseError(ex.Message, ex.Message);

      }

    }

    /// <summary>

    /// Returns the name of agent

    /// </summary>

    public override string Name {

      get {

        return "Wikipedia Agent";

      }

    }

  }

}
```

- In the Visual Studio menu, click Build > Build Solution .

## Step 2 - Upload the agent to an application

Use the following steps to upload the agent to a Relativity application:

- Log in your Relativity instance.

- Navigate to the Resource File tab.

- Click New Resource File . The Resource File Information dialog appears.

- In the Resource File field, click Browse to select the .dll file for the agent from the directory where you built the project. See Step 1 - Create a basic agent .

- The Relativity.ObjectManager.dll is required along with WikipediaAgent.dll. Locate the Relativity.ObjectManager.dll file. It should be in the bin folder of your Visual Studio project. Then add the Relativity.ObjectManager.dll file as a Resource File that is associated to your application:

- To assist with remote debugging, repeat step 5 to upload the WikipediaAgent.pdb debug symbols file as a Resource File that is associated to your application. It should be in the bin folder of your Visual Studio project. (This step is only required when you want to be able to perform remote debugging.)

- In the Application field, click to select Hello Wikipedia , which is the application created in Lesson 2 - Build an application without any code .

This action links your agent assembly to the Hello Wikipedia application.

- Click Save and Back .

## Step 3 - Add the agent to a Relativity instance

After associating your agent with an application, you can add this agent to your Relativity instance.

Use the following steps to add your agent:

- Navigate to the Agents tab.

- Click New Agent . The Agent Information dialog appears.

- In the Agent Type field, click Select and then search for your agent by name on the Select Item dialog.

- In the Agent Server field, click Select and then choose a server where you want your agent to run. If you are using a DevVM, then select the RELATIVITYDEVVM with the Type as Agent .

- Use the default values for the Number of Agents and Run Interval fields.

- In the Logging level field, select Log all messages .

With this setting, you can see the message added to the Execute() method. We don't recommend setting Logging level field to Log all messages in a production environment.

- Click Save and Back .

- In the Agent list, search for your agent. After adding your agent, it may take several minutes for the Agent Manager to pick up the agent and start it.

- Verify that the Message column for the agent is populated with the message added to the Execute() method.

## Step 4 - Remotely debug an agent

After deploying your agent in a Relativity instance, you can start remotely debugging it (as long as you have also uploaded the debug symbols file as a resource for your application). The following steps are similar to those for debugging a Kepler service. See Lesson 3 - Create a RESTful API .

Make sure that you have the Visual Studio Remote Debugger service running on the Relativity instance where you want to debug.

Use the following steps to remotely debug an agent:

- Open the HelloWikipedia solution in Visual Studio.

- Navigate to Debug > Attach to Process . The Attach to Process dialog appears.

- Click Find .

Your Relativity instance with the debugging service running should be automatically detected. See the Auto Detected field in the following screen shot.

- Enter the administrator credentials for your Relativity instance when prompted.

- Use the following steps to locate a process for attaching the debugger:

- Log in to the machine where your Relativity instance is running.

- Open the Task Manager .

- Click the Details tab.

- Right-click the Name column header to display the Select columns dialog.

- Select the Command line checkbox.

- Click OK .

- Locate the kCuraAgentManager.exe service in the Details tab of the Task Manager.

It displays two services with differing command line entries as follows:

- C:\Program Files\kCura Corporation\Relativity\Agents\...

- C:\Program Files\kCura Corporation\Relativity\WebProcessing\...

- Select the process for the server where your agent is running. For example, you would choose the kCuraAgentManager process at the command line entry, C:\Program Files\kCura Corporation\Relativity\Agents\ , because it matches the server selected for the agent.

- In Visual Studio, use the process ID (PID) to search for the process and then select it. Click Attach .

- Add a break point in the agent code where you call the RaiseMessage() method.

You should see the breakpoint being triggered immediately because your agent runs at 5 second intervals.

## Step 5 - Update the agent functionality

After creating the IWikipediaArticleManager and implementing all the methods on it, your agent can perform these tasks:

- Find workspaces where the Hello Wikipedia application is installed.

- Retrieve the Article Category objects in workspaces where the application is installed.

- Retrieve the top 10 articles for each category in a workspace.

- Create and update a Document and Reference Article object for each of the articles.

- Link the Article Reference object to the appropriate Article Category object for each of the articles.

Use the following steps to update the functionality of your agent:

- Delete the file named WikipediaAgent.cs from the basic agent created in Step 1 - Create a basic agent . You will create a new agent in the following steps, which contains the code for the Hello Wikipedia application.

- Create a Constants.cs file in the agent project.

- Add the GUIDs for the application artifacts that you created to the Constants class.

Use these steps to view the GUIDs:

- Navigate to the details views of the Hello Wikipedia application created in Lesson 2 - Build an application without any code .

- Click Show Component GUIDs in the Application console.

- Note the GUIDs for the Article Category and the Article Category – Name .

- View the code for the Constants class. The Constants class provides values used in the implementation of the other classes. The GUIDs in this sample code differ from the GUIDs generated by your Relativity instance. Update the GUIDs in the code with those from your instance.

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
using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

namespace WikipediaAgent {

  public static class Constants {

    public

    const int NUMBER_OF_ARTICLES = 10;

    public

    const int NUMBER_OF_ENTRIES_TO_QUERY = 100;

    public

    const int DOCUMENT_ARTIFACT_ID = 10;

    public

    const int CONTROL_NUMBER_FIELD_ID = 1003667;

    #if DEBUG

    // Change this constant to your local instance when using the Relativity Local Debugger, exemplfied by https://RelativityDevVm-12.2.190.4/RelativityWebAPI.

    public

    const string WEB_SERVICE_URL = "http://localhost/RelativityWebAPI";

    #else

    public

    const string WEB_SERVICE_URL = "http://localhost/RelativityWebAPI";

    #endif

    public static readonly Guid HELLO_WIKIPEDIA_APP_GUID = new Guid("E57FA0FE-59FD-49EB-92ED-895F3E592CD1");

    public static readonly Guid CATEGORY_OBJECT_TYPE_GUID = new Guid("6b20f149-1b17-4e9c-8403-439e98e8bfd2");

    public static readonly Guid REFERENCE_OBJECT_TYPE_GUID = new Guid("f5e7f198-9d2e-445f-a42c-9e248ea85c51");

    public static readonly Guid CATEGORY_NAME_FIELD_GUID = new Guid("16D8A362-2923-45B7-8444-7339C57B3AF0");

    public static readonly Guid CATEGORY_OVERWRITE_FIELD_GUID = new Guid("042e0329-1467-4993-8188-66615e103de3");

    public static readonly Guid CATEGORY_UPDATES_FIELD_GUID = new Guid("f365de2e-a641-428f-9188-a3970a7c308f");

    public static readonly Guid REFERENCE_NAME_FIELD_GUID = new Guid("bb4b7fca-7b9a-4ae0-8ac0-7684a1b34d3b");

    public static readonly Guid REFERENCE_URL_FIELD_GUID = new Guid("086D0E22-72B2-42F4-B0F4-A377A5DD6890");

    public static readonly Guid REFERENCE_ARTICLE_CATEGORIES_FIELD_GUID = new Guid("2F9E6B70-B17D-4A1D-8987-EBB70239FD20");

  }

}
```

- Install the Relativity.Server.Import.SDK NuGet package in the agent project:

- Right-click on the References in the WikipediaAgent project.

- Click Manage NuGet Packages .

- Search for the Relativity.Server.Import.SDK version 2.9.2 package, and click Install .

- Install the Relativity.Server.Services.Interfaces.SDK NuGet package in the agent project:

- Right-click on the References in the WikipediaAgent project.

- Click Manage NuGet Packages .

- Search for the Relativity.Server.Services.Interfaces.SDK version 13.6.1 package, and click Install .

-

Add a reference to the WikipediaKepler.Interfaces project:

- Right click References in the agent project and click Add Reference .

- Select the WikipediaKepler.Interfaces project and click OK .

- Create a new file named Article.cs in the agent project with the following code. Copy

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
namespace WikipediaAgent {

  public class Article {

    private

    const int _HASH_MULTIPLIER_INT = 397;

    public string Category {

      get;

      set;

    }

    public string Title {

      get;

      set;

    }

    public string Url {

      get;

      set;

    }

    public bool OverwriteExisting {

      get;

      set;

    }

    protected bool Equals(Article other) {

      return Category == other.Category && Title == other.Title && Url == other.Url;

    }

    public override bool Equals(object obj) {

      if (ReferenceEquals(null, obj)) {

        return false;

      }

      if (ReferenceEquals(this, obj)) {

        return true;

      }

      if (obj.GetType() != this.GetType()) {

        return false;

      }

      return Equals((Article) obj);

    }

    public override int GetHashCode() {

      unchecked {

        int hashCode = (Category != null ? Category.GetHashCode() : 0);

        hashCode = (hashCode * _HASH_MULTIPLIER_INT) ^ (Title != null ? Title.GetHashCode() : 0);

        hashCode = (hashCode * _HASH_MULTIPLIER_INT) ^ (Url != null ? Url.GetHashCode() : 0);

        return hashCode;

      }

    }

  }

}
```

- Create a new file named ArticleCategory.cs in the Agent project with the following code. Copy

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
namespace WikipediaAgent {

  public class ArticleCategory {

    private

    const int _HASH_MULTIPLIER_INT = 397;

    public string Name {

      get;

      set;

    }

    public bool OverwriteArticleText {

      get;

      set;

    }

    protected bool Equals(ArticleCategory other) {

      return Name == other.Name && OverwriteArticleText == other.OverwriteArticleText;

    }

    public override bool Equals(object obj) {

      if (ReferenceEquals(null, obj)) {

        return false;

      }

      if (ReferenceEquals(this, obj)) {

        return true;

      }

      if (obj.GetType() != this.GetType()) {

        return false;

      }

      return Equals((ArticleCategory) obj);

    }

    public override int GetHashCode() {

      unchecked {

        return ((Name != null ? Name.GetHashCode() : 0) * _HASH_MULTIPLIER_INT) ^ OverwriteArticleText.GetHashCode();

      }

    }

  }

}
```

- Create a new file named IWikipediaArticleManager.cs in the agent project with the following code. Copy

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
using System.CodeDom.Compiler;

using System.Collections.Generic;

using System.Threading.Tasks;

using kCura.Relativity.DataReaderClient;

namespace WikipediaAgent {

    public interface IWikipediaArticleManager {

        Task<IEnumerable<int>> GetHelloWikipediaWorkspaceIDs();

        Task<IEnumerable<ArticleCategory>> GetArticleCategories(int workspaceID);

        Task<IEnumerable<Article>> GetArticles(IEnumerable<ArticleCategory> articleCategories, int numArticlesPerCategory);

        Task<ImportBulkArtifactJob> BuildArticleImportJob(int workspaceID, IEnumerable<Article> articles, TempFileCollection tempFileCollection);

        Task AddOrUpdateArticleReferences(int workspaceID, IEnumerable<Article> articles);

    }

}
```

- Create a new file named WikipediaArticleManager.cs in the agent project with the following code. This class implements the IWikipediaArticleManager interface created in the previous step. Copy

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
using System;

using System.CodeDom.Compiler;

using System.Collections.Generic;

using System.Data;

using System.IO;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using kCura.Relativity.DataReaderClient;

using kCura.Relativity.ImportAPI;

using Relativity.API;

using Relativity.ObjectManager.V1.Interfaces;

using Relativity.ObjectManager.V1.Models;

using Relativity.Services.Interfaces.LibraryApplication;

using Relativity.Services.Interfaces.LibraryApplication.Models;

using Relativity.Services.Interfaces.LibraryApplication.Models.Query;

using WikipediaKepler.Interfaces.WikipediaManagement.v1;

using WikipediaKepler.Interfaces.WikipediaManagement.v1.Models;

using Sort = Relativity.Services.Interfaces.LibraryApplication.Models.Query.Sort;

namespace WikipediaAgent {

  public class WikipediaArticleManager: IWikipediaArticleManager {

    private readonly IApplicationInstallManager _applicationInstallManager;

    private readonly IObjectManager _objectManager;

    private readonly IWikipediaService _wikipediaService;

    private readonly IImportAPI _importApi;

    private readonly IAPILog _logger;

    public WikipediaArticleManager(IApplicationInstallManager applicationInstallManager, IObjectManager objectManager, IWikipediaService wikipediaService, IImportAPI importApi, IAPILog logger) {

      _applicationInstallManager = applicationInstallManager;

      _objectManager = objectManager;

      _wikipediaService = wikipediaService;

      _importApi = importApi;

      _logger = logger;

    }

    public async Task < IEnumerable < int >> GetHelloWikipediaWorkspaceIDs() {

      throw new NotImplementedException();

    }

    public async Task < IEnumerable < ArticleCategory >> GetArticleCategories(int workspaceID) {

      throw new NotImplementedException();

    }

    public async Task < IEnumerable < Article >> GetArticles(IEnumerable < ArticleCategory > articleCategories, int numArticlesPerCategory) {

      throw new NotImplementedException();

    }

    public async Task < ImportBulkArtifactJob > BuildArticleImportJob(int workspaceID, IEnumerable < Article > articles, TempFileCollection tempFileCollection) {

      throw new NotImplementedException();

    }

    public async Task AddOrUpdateArticleReferences(int workspaceID, IEnumerable < Article > articles) {

      throw new NotImplementedException();

    }

  }

}
```

- Query for workspaces containing the Hello Wikipedia application by adding the following code for the GetHelloWikipediaWorkspaceIDs() method in the WikipediaArticleManager class. This code uses the Application Install API to query for all workspaces where the Hello Wikipedia application is successfully installed. See Application Install (.NET) . Copy

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
public async Task <IEnumerable<int>> GetHelloWikipediaWorkspaceIDs() {

  var matchingWorkspaceIDs = new List < int > ();

  var queryOptions = new QueryOptions {

    Condition = "'Status Code' == 4" // Successful install.

  };

  const int pageSize = 50;

  int currentStart = 1;

  ApplicationInstallSearchResponse response;

  do {

    response = await _applicationInstallManager.SearchApplicationAsync(-1, Constants.HELLO_WIKIPEDIA_APP_GUID, queryOptions, currentStart, pageSize, true);

    matchingWorkspaceIDs.AddRange(response.Results.Select(x => x.WorkspaceIdentifier.ArtifactID));

    currentStart = response.CurrentStartIndex + pageSize;

  }

  while (response.NextPage != null && response.NextPage.IsAvailable);

  return matchingWorkspaceIDs.Where(id => id != -1);

}
```

- Create a new file for an agent named WikipediaArticleManagerJob.cs with the Relativity Agent template and add the following code. Copy

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
using System;

using System.CodeDom.Compiler;

using System.Collections.Generic;

using System.Data;

using System.IO;

using System.Linq;

using System.Runtime.InteropServices;

using System.Text;

using kCura.Agent;

using kCura.Agent.CustomAttributes;

using kCura.Relativity.DataReaderClient;

using kCura.Relativity.ImportAPI;

using Relativity.API;

using Relativity.ObjectManager.V1.Interfaces;

using Relativity.Services.Interfaces.LibraryApplication;

using WikipediaKepler.Interfaces.WikipediaManagement.v1;

using WikipediaKepler.Interfaces.WikipediaManagement.v1.Models;

using Sort = Relativity.Services.Interfaces.LibraryApplication.Models.Query.Sort;

namespace WikipediaAgent {

  [Name("Wikipedia Article Manager Agent")]

  [Guid("44ae8827-1c7f-422c-849d-197c1c0f5b68")]

  public class WikipediaArticleManagerJob: AgentBase {

    private IAPILog _logger;

    /// <summary>

    /// Returns the name of agent

    /// </summary>

    public override string Name => "Wikipedia Article Manager Agent";

    /// <summary>

    /// Agent logic goes here

    /// </summary>

    public override void Execute() {

      _logger = Helper.GetLoggerFactory().GetLogger();

      try {

      } catch (Exception ex) {

        _logger.LogError(ex, "Failed to process Wikipedia pages.");

        RaiseError(ex.Message, ex.Message);

      }

    }

  }

}
```

- Set up the APIs used to retrieve Article Category objects by adding the following code to the Execute() method in the WikipediaArticleManagerJob class.This code includes the following functionality:

- Sets up connections to the APIs.

- Uses the Import API to be to upload documents. See Import documents with native files .

- Uses the Object Manager API to perform CRUD operations on Relativity objects. See Object Manager Fundamentals

- Uses the Wikipedia API created in Lesson 3 - Create a RESTful API .

Add the Execute() method to set up the APIs: Copy

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
public override void Execute() {

  _logger = Helper.GetLoggerFactory().GetLogger();

  try {

    using (var applicationInstallManager = Helper.GetServicesManager().CreateProxy<IApplicationInstallManager>(ExecutionIdentity.System))

    using (var objectManager = Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

    using (var wikipediaService = Helper.GetServicesManager().CreateProxy<IWikipediaService>(ExecutionIdentity.System))

    using (var tempFileCollection = new TempFileCollection()) {

      ImportAPI importApi = ImportAPI.CreateByRsaBearerToken(Constants.WEB_SERVICE_URL);

      var manager = new WikipediaArticleManager(applicationInstallManager, objectManager, wikipediaService, importApi, _logger);

      List<int> matchingWorkspaceIDs = manager.GetHelloWikipediaWorkspaceIDs().ConfigureAwait(false).GetAwaiter().GetResult().ToList();

      RaiseMessage($"Found Hello Wikipedia in {matchingWorkspaceIDs.Count} workspaces", (int) AgentMessage.AgentMessageType.Informational);

      foreach (int workspaceID in matchingWorkspaceIDs) {

        IEnumerable<ArticleCategory> articleCategories = manager.GetArticleCategories(workspaceID).ConfigureAwait(false).GetAwaiter().GetResult();

        List<Article> articles = manager.GetArticles(articleCategories, Constants.NUMBER_OF_ARTICLES).ConfigureAwait(false).GetAwaiter().GetResult().ToList();

        ImportBulkArtifactJob job = manager.BuildArticleImportJob(workspaceID, articles, tempFileCollection).ConfigureAwait(false).GetAwaiter().GetResult();

        job.Execute();

        job.SourceData.SourceData.Close();

        manager.AddOrUpdateArticleReferences(workspaceID, articles).ConfigureAwait(false).GetAwaiter().GetResult();

        RaiseMessage($"Processed {articles.Count}", (int) AgentMessage.AgentMessageType.Informational);

      }

    }

  } catch (Exception ex) {

    _logger.LogError(ex, "Failed to process Wikipedia pages.");

    RaiseError(ex.Message, ex.Message);

  }

}
```

- Retrieve Article Category objects for the matching workspaces by adding the code for the GetArticleCategories() method in the WikipediaArticleManager class. After setting up the API clients, you can access each workspace to retrieve its Article Category objects.This code includes creates the GetArticleCategories() method, which uses the Object Manager API to query for all categories in a workspace. Copy

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
public async Task<IEnumerable<ArticleCategory>> GetArticleCategories(int workspaceID) {

  var categories = new List<ArticleCategory>();

  var queryRequest = new QueryRequest {

    ObjectType = new ObjectTypeRef {

        Guid = Constants.CATEGORY_OBJECT_TYPE_GUID

      },

      Fields = new List<FieldRef> {

        new FieldRef {

          Guid = Constants.CATEGORY_NAME_FIELD_GUID

        },

        new FieldRef {

          Guid = Constants.CATEGORY_OVERWRITE_FIELD_GUID

        }

      },

      Condition = $ "(('{Constants.CATEGORY_UPDATES_FIELD_GUID}' == true))"

  };

  try {

    QueryResult results = await _objectManager.QueryAsync(workspaceID, queryRequest, 1, Constants.NUMBER_OF_ENTRIES_TO_QUERY);

    categories.AddRange(results.Objects.Select(obj => new ArticleCategory {

      Name = obj[Constants.CATEGORY_NAME_FIELD_GUID]?.Value.ToString(),

        OverwriteArticleText = obj[Constants.CATEGORY_OVERWRITE_FIELD_GUID]?.Value as bool ? ?? false

    }));

  } catch {

    _logger.LogWarning("Failed to retrieve article categories for workspace {0}", workspaceID);

  }

  return categories;

}
```

- Retrieve the top 10 articles for a category by adding code for the GetArticles() method.After retrieving the categories in a workspace, you can use the Wikipedia API to get the top 10 articles for each category and return them as list of CategoryPage objects. The CategoryPage objects are later used to create Document and Article Reference objects. Copy

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
public async Task<IEnumerable<Article>> GetArticles(IEnumerable<ArticleCategory> articleCategories, int numArticlesPerCategory) {

  var articles = new List<Article>();

  foreach(var category in articleCategories) {

    Pageable<PageForCategoryResponseModel> pageablePages = await _wikipediaService.GetPagesForCategoryAsync(category.Name, numArticlesPerCategory);

    foreach (PageForCategoryResponseModel page in pageablePages.Results) {

      try {

        PageResponseModel pageResponseModel = await _wikipediaService.GetPageByNameAsync(page.Title);

        articles.Add(new Article {

          Category = category.Name, Title = page.Title, Url = pageResponseModel.Url, OverwriteExisting = category.OverwriteArticleText

        });

      } catch (Exception ex) {

        _logger.LogWarning("Failed to retrieve page by name for {0}: ", page.Title);

      }

    }

  }

  return articles;

}
```

- Create or update the web pages as Document objects after retrieving all the web pages for your list by using the Import API to add them to Relativity.

- Configure a job for uploading documents by adding the following code for the BuildArticleImportJob() , GetImportableArticles() , and InitializeImportJob() methods in the WikipediaArticleManager class. You need to configure a job in the BuildArticleImportJob() method to upload documents with the Import API.This code includes the following functionality:

- Creates a job object

- Sets up a data source with a control number and file path.

- Creates a temporary file from each of the web pages in the article list.

- Adds the temporary file to the data source.

- Returns the job for execution with all the files that need to be uploaded as documents.

Add the following code for these methods:

- BuildArticleImportJob() method Copy

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
public async Task<ImportBulkArtifactJob> BuildArticleImportJob(int workspaceID, IEnumerable<Article> articles, TempFileCollection tempFileCollection) {

  List<Article> importableArticles = await GetImportableArticles(_objectManager, workspaceID, articles);

  ImportBulkArtifactJob job = InitializeImportJob(_importApi, workspaceID);

  var dataTable = new DataTable("Wikipedia Agent Import Data") {

    Columns = {

      new DataColumn("Control Number", typeof (string)),

      new DataColumn("Native File", typeof (string))

    }

  };

  foreach (var article in importableArticles) {

    string tempArticlePath = Path.ChangeExtension(Path.GetTempFileName(), "html");

    tempFileCollection.AddFile(tempArticlePath, keepFile: false);

    string pageText = "";

    using (var keplerStream = await _wikipediaService.GetPageTextAsync(article.Title)) {

      Stream stream = await keplerStream.GetStreamAsync();

      var reader = new StreamReader(stream, Encoding.UTF8);

      pageText = await reader.ReadToEndAsync();

    }

    File.WriteAllText(tempArticlePath, pageText);

    dataTable.Rows.Add(article.Title, tempArticlePath);

  }

  job.SourceData.SourceData = dataTable.CreateDataReader();

  return job;

}
```

- EscapeConditionString() method - add the following code for this method. It escapes strings as required to build conditions for Object Manager query conditions: Copy

```text
1
2
3
4
5
6
private string EscapeConditionString(string title) {

    string articleTitle = title.Replace("\'", "\\\'"); // Escape ''' Character

    articleTitle = articleTitle.Replace("\"", "\\\""); // Escape '"' Character

    articleTitle = articleTitle.Replace("\\", "\\\\"); // Escape '\' Character

    return articleTitle;

}
```

- GetImportableArticles() method Copy

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
private async Task<List<Article>> GetImportableArticles(IObjectManager objectManager, int workspaceID, IEnumerable<Article> articles) {

  Dictionary<bool, List<Article>> overwritableToArticles = articles.GroupBy(article => article.OverwriteExisting).ToDictionary(g => g.Key, g => g.ToList());

  List<Article> importableArticles = overwritableToArticles.TryGetValue(true, out

    var overwritable) ? overwritable : new List<Article>();

  List<Article> nonOverwritableArticles = overwritableToArticles.TryGetValue(false, out

    var nonOverwritable) ? nonOverwritable : new List<Article>();

  if (nonOverwritableArticles.Any()) {

    List<string> conditionElements = new List<string>();

    foreach (Article nonOverwriteableArticle in nonOverwritableArticles) {

      string articleTitle = EscapeConditionString(nonOverwriteableArticle.Title);

      conditionElements.Add($"'{Constants.CONTROL_NUMBER_FIELD_ID}' == '{articleTitle}'");

    }

    var results = new QueryResult();

    var queryRequest = new QueryRequest {

      ObjectType = new ObjectTypeRef {

          ArtifactTypeID = Constants.DOCUMENT_ARTIFACT_ID

        },

        Fields = new List<FieldRef> {

          new FieldRef {

            ArtifactID = Constants.CONTROL_NUMBER_FIELD_ID

          }

        },

        Condition = $ "(({string.Join("

      OR ", conditionElements)}))"

    };

    try {

      results = await objectManager.QueryAsync(workspaceID, queryRequest, 1, 1);

    } catch {

      _logger.LogWarning("Failed to retrieve articles for workspace {1}", workspaceID);

    }

    foreach (var nonOverwritableArticle in nonOverwritableArticles) {

      if (!results.Objects.Any(obj => obj.FieldValues.Any(pair => pair.Value.Equals(nonOverwritableArticle.Title)))) {

        importableArticles.Add(nonOverwritableArticle);

      }

    }

  }

  return importableArticles;

}
```

- InitializeImportJob() method Copy

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
private static ImportBulkArtifactJob InitializeImportJob(IImportAPI importApi, int workspaceID) {

    ImportBulkArtifactJob importJob = importApi.NewNativeDocumentImportJob();

    importJob.Settings.ArtifactTypeId = Constants.DOCUMENT_ARTIFACT_ID;

    importJob.Settings.Billable = false;

    importJob.Settings.BulkLoadFileFieldDelimiter = ";";

    importJob.Settings.CaseArtifactId = workspaceID;

    importJob.Settings.CopyFilesToDocumentRepository = true;

    importJob.Settings.DisableControlNumberCompatibilityMode = true;

    importJob.Settings.DisableExtractedTextFileLocationValidation = false;

    importJob.Settings.DisableNativeLocationValidation = false;

    importJob.Settings.DisableNativeValidation = false;

    importJob.Settings.ExtractedTextEncoding = Encoding.Unicode;

    importJob.Settings.ExtractedTextFieldContainsFilePath = false;

    importJob.Settings.FileSizeColumn = "NativeFileSize";

    importJob.Settings.FileSizeMapped = true;

    importJob.Settings.FolderPathSourceFieldName = null;

    importJob.Settings.IdentityFieldId = Constants.CONTROL_NUMBER_FIELD_ID;

    importJob.Settings.LoadImportedFullTextFromServer = false;

    importJob.Settings.MaximumErrorCount = int.MaxValue - 1;

    importJob.Settings.MoveDocumentsInAppendOverlayMode = false;

    importJob.Settings.NativeFileCopyMode = NativeFileCopyModeEnum.CopyFiles;

    importJob.Settings.NativeFilePathSourceFieldName = "Native File";

    importJob.Settings.OIFileIdColumnName = "OutsideInFileId";

    importJob.Settings.OIFileIdMapped = true;

    importJob.Settings.OIFileTypeColumnName = "OutsideInFileType";

    importJob.Settings.OverwriteMode = OverwriteModeEnum.AppendOverlay;

    importJob.Settings.SelectedIdentifierFieldName = "Control Number";

    importJob.Settings.StartRecordNumber = 0;

    return importJob;

}
```

- Create an Article Reference object for each article by adding the following code for the AddOrUpdateArticleReferences() method in the WikipediaArticleManager class. Copy

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
public async Task AddOrUpdateArticleReferences(int workspaceID, IEnumerable<Article> articles) {

    foreach (var article in articles) {

        RelativityObject maybeArticleReference = await FindExistingArticleReference(_objectManager, workspaceID, article.Title);

        if (maybeArticleReference == null) {

            await CreateArticleReference(_objectManager, workspaceID, article);

        }

        else {

            await UpdateArticleReference(_objectManager, workspaceID, article, maybeArticleReference);

        }

    }

}
```

- Query for existing Article Reference objects and avoid duplicates by adding the following code for the FindExistingArticleReference() method in the WikipediaArticleManager class.You query for existing Article Reference objects before adding new ones to prevent duplicates. If an object already exists, then you can update it. This code uses the querying methods from the Object Manager API. See Object Manager Fundamentals .

Add the following code for the FindExistingArticleReference() method: Copy

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
private async Task<RelativityObject> FindExistingArticleReference(IObjectManager objectManager, int workspaceID, string title) {

    var results = new QueryResult();

    string articleTitle = EscapeConditionString(title);

    var queryRequest = new QueryRequest {

        ObjectType = new ObjectTypeRef { Guid = Constants.REFERENCE_OBJECT_TYPE_GUID },

        Fields = new List<FieldRef> { new FieldRef { Guid = Constants.REFERENCE_NAME_FIELD_GUID } },

        Condition = $"(('{Constants.REFERENCE_NAME_FIELD_GUID}' == '{articleTitle}'))"

    };

    try {

        results = await objectManager.QueryAsync(workspaceID, queryRequest, 1, 1);

    }

    catch {

        _logger.LogWarning("Failed to retrieve article references {0} for workspace {1}", title, workspaceID);

    }

    return results.Objects.FirstOrDefault();

}
```

- Create or update an Article Reference object for a document by adding the following code for the CreateArticleReference() and UpdateArticleReference() methods in the WikipediaArticleManager class. When the query for an Article Reference object return doesn't return an object, the code uses the Object Manager API to create it. When the query finds an existing object, the code uses this API to update it.

- CreateArticleReference() method Copy

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
private async Task CreateArticleReference(IObjectManager objectManager, int workspaceID, Article article) {

  RelativityObject articleCategory = await GetArticleCategory(objectManager, workspaceID, article);

  var fieldValuePairs = new List<FieldRefValuePair> {

    new FieldRefValuePair {

      Field = new FieldRef {

          Guid = Constants.REFERENCE_NAME_FIELD_GUID

        },

        Value = article.Title

    },

    new FieldRefValuePair {

      Field = new FieldRef {

          Guid = Constants.REFERENCE_URL_FIELD_GUID

        },

        Value = article.Url

    },

    new FieldRefValuePair {

      Field = new FieldRef {

          Guid = Constants.REFERENCE_ARTICLE_CATEGORIES_FIELD_GUID

        },

        Value = new List<RelativityObject> {

          articleCategory

        }

    }

  };

  var createRequest = new CreateRequest {

    FieldValues = fieldValuePairs,

      ObjectType = new ObjectTypeRef {

        Guid = Constants.REFERENCE_OBJECT_TYPE_GUID

      }

  };

  await objectManager.CreateAsync(workspaceID, createRequest);

}
```

- UpdateArticleReference() method Copy

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
private async Task UpdateArticleReference(IObjectManager objectManager, int workspaceID, Article article, RelativityObject articleReference) {

  RelativityObject articleCategory = await GetArticleCategory(objectManager, workspaceID, article);

  var fieldValuePairs = new List<FieldRefValuePair> {

    new FieldRefValuePair {

      Field = new FieldRef {

          Guid = Constants.REFERENCE_NAME_FIELD_GUID

        },

        Value = article.Title

    },

    new FieldRefValuePair {

      Field = new FieldRef {

          Guid = Constants.REFERENCE_URL_FIELD_GUID

        },

        Value = article.Url

    },

    new FieldRefValuePair {

      Field = new FieldRef {

          Guid = Constants.REFERENCE_ARTICLE_CATEGORIES_FIELD_GUID

        },

        Value = new List<RelativityObject> {

          articleCategory

        }

    }

  };

  var updateRequest = new UpdateRequest {

    FieldValues = fieldValuePairs,

      Object = new RelativityObjectRef {

        ArtifactID = articleReference.ArtifactID

      }

  };

  await objectManager.UpdateAsync(workspaceID, updateRequest);

}
```

- Retrieve the Article Category object for an Article Reference object by adding the following code for the GetArticleCategory() method in the WikipediaArticleManager class. When creating or updating an Article Reference object, you need to retrieve the Article Category object for it. You use this object to add or update the multiple object field for the Article Reference. The GetArticleCategory() method returns a QueryResult object that you can use to obtain the Article Category object.Add the following code for this method: Copy

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
private async Task<RelativityObject> GetArticleCategory(IObjectManager objectManager, int workspaceID, Article article) {

    var results = new QueryResult();

    var queryRequest = new QueryRequest {

        ObjectType = new ObjectTypeRef { Guid = Constants.CATEGORY_OBJECT_TYPE_GUID },

        Fields = new List<FieldRef> { new FieldRef { Guid = Constants.CATEGORY_NAME_FIELD_GUID } },

        Condition = $"(('{Constants.CATEGORY_NAME_FIELD_GUID}' == '{article.Category}'))"

    };

    try {

        results = await objectManager.QueryAsync(workspaceID, queryRequest, 1, 1);

    }

    catch (Exception e) {

        _logger.LogWarning(e, "Failed to retrieve article category {0} for workspace {1}", article.Category, workspaceID);

    }

    return results.Objects.First();

}
```

- Use the following steps to include additional assemblies from the Relativity.Server.Import.SDK package required by the Import API as part of the RAP file:

- Build the solution in the bin folder for the WikipediaAgent.

- Upload the following assemblies as Resource files associated with the Hello Wikipedia RAP file:

- Relativity.DataExchange.Client.SDK.dll

- Relativity.DataExchange.Legacy.SDK.dll

- Relativity.Telemetry.Services.Interfaces.dll

- Relativity.Transfer.Client.Core.dll

- Relativity.Transfer.Client.Aspera.dll

- Relativity.Transfer.Client.dll

- Relativity.Transfer.Client.FileShare.dll

- Relativity.Transfer.Client.Http.dll

- Renci.SshNet.dll

- Polly.dll

- FaspManager.dll

-

In Step 7 - Verify that the agent runs , you will check that your agent retrieves the top 10 articles for article categories in a workspace. They should be retrieved as documents and article references in Relativity.

## Step 6 - Write a unit test

In this section, you learn how to write a unit test for your new agent.

Review these guidelines for writing unit tests:

- Test a single scenario per test. For example, when calling the GetHelloWikipediaWorkspaceIDs() method, the Application Install Manager is called and only workspaces that aren't administrator workspaces are returned.

- Mock any dependencies to ensure that the test is limited to only the behavior that you want to test. For example, mock the dependencies of IApplicationInstallManager interface.

- Follow testing best practices for naming conventions. The test should explain what is being tested. For example, when testing the GetHelloWikipedia() method, the test should indicate that the application is installed in a non-administrative workspace, and that any matching workspace IDs are returned.

Use the following steps to write a unit test:

- Open Visual Studio.

- Create a unit test project for your solution.

- Select Unit Test Project (.NET Framework) template for your project and name it as WikipediaAgent.Tests .

- Add the project to the same root directory as your other projects.

- Use .NET Framework 4.6.2 as the project framework.

-

Rename the UnitTest1.cs file and class name to WikipediaArticleManagerTests.cs and WikipediaArticleManagerTests .

- Install the following NuGet packages:

- NUnit 3.12.0

- NUnit3TestAdapter 3.16.1

- Moq 4.5.30

- Relativity.Server.ObjectManager.SDK 1.1.2

- Relativity.Server.Import.SDK 2.9.2

- Relativity.Server.API.SDK 17.4.2

- Relativity.Server.Services.Interfaces.SDK 13.6.1

- Add a reference to the following projects:

- Wikipedia Agent

- WikipediaKepler.Interfaces

- Update the WikipediaArticleManagerTests class to test the GetHelloWikipediaWorkspaceIDs() method.

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
using System;

using System.Collections.Generic;

using System.Linq;

using System.Threading.Tasks;

using Moq;

using NUnit.Framework;

using Relativity.Services.Interfaces.LibraryApplication;

using Relativity.Services.Interfaces.LibraryApplication.Models;

using Relativity.Services.Interfaces.LibraryApplication.Models.Query;

using Relativity.Services.Interfaces.Shared.Models;

namespace WikipediaAgent.Tests {

  [TestFixture]

  public class WikipediaArticleManagerTests {

    private readonly Random _random = new Random();

    [Test]

    [Description("Verifies that when GetHelloWikipediaWorkspaceIDs is called, a call is made to the Application Install Manager and matching non-admin workspaces are returned.")]

    public async Task GetHelloWikipediaWorkspaceIDs_InstalledInNonAdminWorkspaces_ReturnsMatchingWorkspaceIDs() {

      // Arrange

      var expectedWorkspaceIDs = new List<int> {

        _random.Next()

      };

      var responseIds = new List<int> {

        -1

      };

      responseIds.AddRange(expectedWorkspaceIDs);

      var response = new ApplicationInstallSearchResponse {

        Results = responseIds.Select(id => new ApplicationInstallSearchItem {

          WorkspaceIdentifier = new DisplayableObjectIdentifier {

            ArtifactID = id

          }

        }).ToList()

      };

      var applicationInstallManagerMock = new Mock<IApplicationInstallManager> ();

      applicationInstallManagerMock.Setup(manager => manager.SearchApplicationAsync(-1, Constants.HELLO_WIKIPEDIA_APP_GUID,

          It.Is<QueryOptions> (q => q.Condition.Equals("'Status Code' == 4")), // A status code of 4 indicates a successful installation

          It.IsAny<int>(), It.IsAny<int>(), true))

        .ReturnsAsync(response);

      var articleManager = new WikipediaArticleManager(applicationInstallManagerMock.Object, null, null, null, null);

      // Act

      IEnumerable<int> actualWorkspaceIDs = await articleManager.GetHelloWikipediaWorkspaceIDs();

      // Assert

      CollectionAssert.AreEquivalent(expectedWorkspaceIDs, actualWorkspaceIDs);

    }

  }

}
```

- Run the test and verify that it passes. Use this test as a model for adding coverage for edge cases. For additional practice, implement unit tests for the other methods used by this agent.

## Step 7 - Verify that the agent runs

After confirming that the agent passes the unit tests, you can add the updated agent to your Relativity instance.

Use the following steps to add the updated agent to Relativity:

- Log in to Relativity.

- Navigate to the Agents tab.

- Delete any instances of the Wikipedia Agent by completing the following steps:

- Select the checkbox for each the instance of the agent to delete.

- Select Delete in the drop-down menu at the bottom of the page.

- Click Delete Agents .

- Navigate to the Resource Files tab.

- Delete the resource file for the previous version of the agent from the Hello Wikipedia application.

You can use the delete mass operation to remove the file:

- Repeat the steps in Step 2 - Upload the agent to an application and Step 3 - Add the agent to a Relativity instance to deploy your new WikipediaAgent.dll .The WikipediaAgent.dll consists of one agent as shown in the following screen shot:

When adding your new agent, make sure your set the Run Interval to a reasonable setting, such as a minimum of 60 seconds. In this tutorial, the code uses Wikipedia API calls. When deploying your agent, follow the usage guidelines at API:Etiquette on the MediaWiki website.

- Navigate to the details view of the application, and click Push to Library in the Application console.

- Create a new workspace.

- Navigate to the Relativity Application tab of the new workspace and click New Relativity Application .

- In the Application Type field, choose Select from Application LIbrary and select Hello Wikipedia in the Choose from Application Library field.

- Click Import .

- Navigate to the Article Category tab in the new workspace.

- Create a new Article Category named Fish , and select the Automatic Updates Enabled field.

- Verify that the document list displays the top 10 articles of the category created from Wikipedia, and corresponding article reference. View sample results

The following screen shot illustrates for top 10 articles for a category.

Go to the Documents tab in the new workspace. The following screen shot displays the Fish document in the viewer.

The following screen shot illustrates an article reference.

- As an alternative to testing an agent running live in the environment, use the Local Debugger to test the agent logic locally as follows:

- Because you are mimicking agent behavior, disable or delete the current agent so the actions don't overlap. See step 3 in Step 7 - Verify that the agent runs .

- Navigate to Article Category tab in the new workspace.

- Create a new Article Category named Birds , and select the Automatic Updates Enabled field.

- In Visual Studio, locate the Constants.cs file in the WikipediaAgent project.

- Verify that the WEB_SERVICE_URL between the #if debug pragma is set to your instance. For example, a setting would be https://relativitydevvm-12.2.190.4/RelativityWebAPI .

- Add a breakpoint at the call ImportBulkArtifactJob job = manager.BuildArticleImportJob in the Execute() method of the WikipediaArticleManagerJob class.

- If your setup from Lesson 5 - Build a cron job is in place, press F5 . You should see the following results:

- Step through the job.Execute() code by pressing F10. The program adds article references to the Birds category as the agent did on the when running live on the instance. See the following sample output:
