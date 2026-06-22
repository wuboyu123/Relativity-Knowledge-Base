---
title: "Lesson 3 - Create a RESTful API"
url: https://platform.relativity.com/Server2025/Content/Get_started/Lesson_3_-_Create_a_RESTful_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:55+00:00
sha256: 7765a7c0dd375f2592e1e0640a339d966814b59bcf84ed02f52b1afc2a908c87
---

Lesson 3 - Create a RESTful API Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Lesson 3 - Create a RESTful API

Relativity exposes many REST endpoints, which you easily use to make API calls from various coding languages and tools, such as cURL or Postman. You make REST calls over HTTP, which provides language-agnostic programming and a high level of flexibility.

In this lesson, you will learn how to:

- Use the Kepler framework to build RESTful APIs.

- Implement a RESTful API which integrates with Wikipedia's public APIs.

- Retrieve data in the required format.

Estimated completion time - 2 hours

PREVIOUS LESSON

‹‹ Lesson 2 - Build an application without any code

NEXT LESSON

Lesson 4 - Validate object changes ››

## Before you begin

- If you have not done so already, you should Create a nuget.config file so that your solution can target different nuget repositories for Relativity Server or RelativityOne.

## Step 1 - Create an empty Kepler service

Begin by creating an empty Kepler service, which serves as the framework for the final service that you implement. (You will be using the Relativity Visual Studio templates that you installed in Lesson1, Step 1 )

Use the following steps to create an empty Kepler service:

- Open Visual Studio.

- Click Create a new project .

The Create a new project dialog appears.

- Select C# as the language for the project.

- Search for the Relativity Kepler Project Template .

- Click Next . The Configure your new project dialog appears.

- Enter the following information in this dialog:

- Project name - WikipediaKepler

- Solution name - HelloWikipedia

- Framework - .NET Framework 4.6.2

- Click Create . The Template Wizard appears.

- Enter the following information in the wizard:

- Service Module - WikipediaManagement

- Service Name - WikipediaService

- Click Create . The wizard generates the solution and required projects.

If you see an error like the one below, you need to Create a nuget.config file for your solution:

- Verify that solution contains the WikipediaKepler.Interfaces and WikipediaKepler.Services projects, as illustrated in the following screen shot.

The projects are used as follows:

- WikipediaKepler.Interfaces - add your API definitions to this project.

- WikipediaKepler.Services - add your implementation to this project.

- Ensure that the generated API is compliant with REST best practices by navigating to WikipediaKepler.Interfaces > WikipediaManagement > IWikipediaManagementModule.cs in Visual Studio.

- Update the RoutePrefix attribute to wikipedia-management . Copy

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
using Relativity.Kepler.Services;



namespace WikipediaKepler.Interfaces.WikipediaManagement

{

    /// <summary>

    /// WikipediaManagement Module Interface.

    /// </summary>

    [ServiceModule("WikipediaManagement Module")]

    [RoutePrefix("wikipedia-management", VersioningStrategy.Namespace)]

    public interface IWikipediaManagementModule

    {

    }

}
```

- Navigate to WikipediaKepler.Interfaces > WikipediaManagement > v1 > IWikipediaService.cs in Visual Studio.

- Update the RoutePrefix attribute to wikipedia-service . Copy

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
using System;

using System.Collections.Generic;

using System.Threading.Tasks;

using Relativity.Kepler.Services;

using WikipediaKepler.Interfaces.WikipediaManagement.v1.Models;



namespace WikipediaKepler.Interfaces.WikipediaManagement.v1

{

    /// <summary>

    /// MyService Service Interface.

    /// </summary>

    [WebService("WikipediaService Service")]

    [ServiceAudience(Audience.Public)]

    [RoutePrefix("wikipedia-service")]

    public interface IWikipediaService : IDisposable

    {

        /// <summary>

        /// Get workspace name.

        /// </summary>

        /// <param name="workspaceID">Workspace ArtifactID.</param>

        /// <returns><see cref="WikipediaServiceModel"/> with the name of the workspace.</returns>

        /// <remarks>

        /// Example REST request:

        ///   [GET] /Relativity.REST/api/WIkipediaManagement/v1/WikipediaService/workspace/1015024

        /// Example REST response:

        ///   {"Name":"Relativity Starter Template"}

        /// </remarks>

        [HttpGet]

        [Route("workspace/{workspaceID:int}")]

        Task<WikipediaServiceModel> GetWorkspaceNameAsync(int workspaceID);



        /// <summary>

        /// Query for a workspace by name

        /// </summary>

        /// <param name="queryString">Partial name of a workspace to query for.</param>

        /// <param name="limit">Limit the number of results via a query string parameter. (Default 10)</param>

        /// <returns>Collection of <see cref="WikipediaServiceModel"/> containing workspace names that match the query string.</returns>

        /// <remarks>

        /// Example REST request:

        ///   [POST] /Relativity.REST/api/WIkipediaManagement/v1/WikipediaService/workspace?limit=2

        ///   { "queryString":"a" }

        /// Example REST response:

        ///   [{"Name":"New Case Template"},{"Name":"Relativity Starter Template"}]

        /// </remarks>

        [HttpPost]

        [Route("workspace?{limit}")]

        Task<List<WikipediaServiceModel>> QueryWorkspaceByNameAsync(string queryString, int limit = 10);

    }

}
```

The final route is constructed based on the route prefixes that you just added:

Copy

```text
1
Relativity.REST/api/{{IWikipediaManagementModule route prefix}}/{{IWikipediaService namespace version}}/{{IWikipediaService route prefix}}/{{IWikipediaService method route}}
```

- Build the solution.

When the build completes, you have a functional Kepler service that you can deploy.

## Step 2 - Deploy to Relativity

After implementing a functional Kepler service, you can upload it to Relativity and associate it with an application so that users can interact with it.

Use the following steps to deploy your service to Relativity:

- Log in to your Relativity instance.

- Click to display your home page.

- In the Sidebar, click Other Tabs > Applications & Scripts > Resource Files .

The Resource Files tab appears.

- Click New Resource File .

The Resource File Information dialog appears.

- Click Select to display the Select Library Application dialog.

- Select the Hello Wikipedia application that you created in Lesson 2 - Build an application without any code .

- Click Choose File to select your compiled WikipediaKepler.Interfaces.dll to add as a new resource file.

- Click Save and New .

- Repeat steps 5 - 7 to add the WikipediaKepler.Services.dll , WikipediaKepler.Interfaces.pdb , and WikipediaKepler.Services.pdb as a resource files.

You have now uploaded the .dlls and pdbs, associated them with the Hello Wikipedia application, and deployed them to Relativity.

## Step 3 - Test the deployed service

You can test your new service after you have deployed it to Relativity.

Use the following steps to make a REST call:

- Make a REST request to your newly deployed Kepler service using an HTTP client such as Postman . If you get a 404 error, wait a few minutes and try again.

- Method - POST

- URL - use the following: Copy

```text
1
<host>/Relativity.REST/api/wikipedia-management/v1/wikipedia-service/workspace
```

- In the sample URL, <host> refers to the Relativity instance's base URL. On a test VM, the <host> value may look something like https://p-dv-vm-abc0efg

- Headers - set the headers as follows:

- X-CSRF-Header - set to a dash ( - ).

- Authorization - set to Basic <basic-authorization-token>.

Basic authentication is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the Authorization header that contains the word Basic followed by a space and a base64-encoded string, such as username:password . For example, if you wanted to authorize as user demo with the password p@55w0rd , use base64 to encode the password. Next, update the Authorization header to Basic with encoded password as ZGVtbzpwQDU1dzByZA== . If you are using a Relativity Test VM, use the same credentials that you used to sign into the Relativity Instance on the Test VM.

- Content type - application/json

- Body - add the following JSON: Copy

```text
1
2
3
4
5
{

    "queryString" : "My First Workspace"

}
```

- Verify that you receive a successful response with the following payload: Copy

```text
1
2
3
4
5
[

    {

        "Name": "My First Workspace"

    }

]
```

## Step 4 - Remote debugging

After you have deployed the service in Relativity, you can use remote debugging to inspect the runtime functionality of the service.

### Verify the remote debugger is running

Make sure that you have the Visual Studio Remote Debugger service running on the Relativity instance where you want to debug. In your DevVM, click the VS 2022 debugger in the taskbar to start running it.

### Remotely debug your code

Use the following steps to remotely debug your code:

- Open the HelloWikipedia solution in Visual Studio.

- Navigate to Debug > Attach to Process .

- Enter a Connection Target and click Find .

The Remote Connections dialog appears.

- Select a connection in the Auto Detected section. A prompt appears requesting your credentials.

- Enter the administrator credentials for your Relativity instance and click OK .

- Use the following steps to locate a process for attaching the debugger:

- Log in to the machine where your Relativity instance is running.

- Open the Task Manager .

- Click the Details tab.

- Right-click the Name column header to display the Select columns dialog.

- Select the Command line checkbox.

- Locate the Relativity.Platform.Service.exe process with the name Hello Wikipedia .

This process is hosting your service.

- Copy the PID of the matching process.

- In Visual Studio, go to the Attach to Process window. See steps 2-5.

- Select the Show processes from all users checkbox .

- Enter the PID that you copied from your Relativity instance in the search box and attach to the matching process.

After you attach to the process, you can add breakpoints to begin testing your service.

- Add a breakpoint to the code in the WikipediaService.cs file for the REST call made in Step 3 - Test the deployed service .

- Repeat the REST call made in Step 3 - Test the deployed service . The breakpoint should be triggered in Visual Studio.

The REST call won't complete until you stop debugging or allow the process to continue.

## Step 5 - Update the service

After confirming that your service is working and can be remotely debugged, you can start updating it.

Use the following steps to update the service:

- Add a default value that the QueryWorkspaceByNameAsync() method returns. Update the WikipediaService.cs file with the following code for the QueryWorkspaceByNameAsync() method. Copy

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
public async Task<List<WikipediaServiceModel>> QueryWorkspaceByNameAsync(string queryString, int limit)

{

    List<WikipediaServiceModel> models = new List<WikipediaServiceModel>();

    WikipediaServiceModel unrealWorkspace = new WikipediaServiceModel

    {

        Name = "NotARealWorkspace"

    };



    models.Add(unrealWorkspace);



    // Validate queryString and throw a ValidationException (HttpStatusCode 400) if the string does not meet the validation requirements.

    if (string.IsNullOrEmpty(queryString) || queryString.Length > 50)

    {

        // ValidationException is in the namespace Relativity.Services.Exceptions and found in the Relativity.Kepler.dll.

        throw new ValidationException($"{nameof(queryString)} cannot be empty or greater than 50 characters.");

    }



    try

    {

        // Use the dependency injected IHelper to get a database connection.

        // In this example a query is made for all workspaces that are like the query string.

        // Note: async/await and ConfigureAwait(false) is used when making calls external to the service.

        //       See https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/

        //       See also https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.configureawait

        //       See also https://blogs.msdn.microsoft.com/benwilli/2017/02/09/an-alternative-to-configureawaitfalse-everywhere/

        //       See also https://blog.stephencleary.com/2012/07/dont-block-on-async-code.html

        //       Warning: Improper use of the tasks can cause deadlocks and performance issues within an application.

        IEnumerable<int> workspaceIDs = await _helper.GetDBContext(-1).ExecuteEnumerableAsync(

            new ContextQuery

            {

                SqlStatement = @"SELECT TOP (@limit) [ArtifactID] FROM [Case] WHERE [ArtifactID] > 0 AND [Name] LIKE '%'+@workspaceName+'%'",

                Parameters = new[]

                {

                    new SqlParameter("@limit", limit),

                    new SqlParameter("@workspaceName", queryString)

                }

            }, (record, cancel) => Task.FromResult(record.GetInt32(0))).ConfigureAwait(false);



        // Create a Kepler service proxy to interact with other Kepler services.

        // Use the dependency injected IHelper to create a proxy to an external service.

        // This proxy will execute as the currently logged in user. (ExecutionIdentity.CurrentUser)

        // Note: If calling methods within the same service, the proxy is not needed. It is doing so

        //       in this example only as a demonstration of how to call other services.

        using (IWikipediaService proxy = _helper.GetServicesManager().

                   CreateProxy<IWikipediaService>(ExecutionIdentity.CurrentUser))

        {

            foreach (int workspaceID in workspaceIDs)

            {

                // Loop through the results and use the proxy to call another service for more information.

                // Note: async/await and ConfigureAwait(false) is used when making calls external to the service.

                //       See https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/

                //       See also https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.configureawait

                //       See also https://blogs.msdn.microsoft.com/benwilli/2017/02/09/an-alternative-to-configureawaitfalse-everywhere/

                //       See also https://blog.stephencleary.com/2012/07/dont-block-on-async-code.html

                //       Warning: Improper use of the tasks can cause deadlocks and performance issues within an application.

                WikipediaServiceModel wsModel =

                    await proxy.GetWorkspaceNameAsync(workspaceID).ConfigureAwait(false);

                if (wsModel != null)

                {

                    models.Add(wsModel);

                }

            }

        }

    }

    catch (Exception exception)

    {

        // Note: logging templates should never use interpolation! Doing so will cause memory leaks.

        _logger.LogWarning(exception, "An exception occurred during query for workspace(s) containing {QueryString}.", queryString);



        // Throwing a user defined exception with a 404 status code.

        throw new WikipediaServiceException($"An exception occurred during query for workspace(s) containing {queryString}.");

    }



    return models;

}
```

- Save the changes and rebuild the solution.

- Log in to your Relativity instance.

- Click to display your home page.

- In the Sidebar, click Other Tabs > Applications & Scripts > Resource Files .

The Resource Files tab appears.

- In the Name filter, type WikipediaKepler .

You should see the two .dlls and two .pdbs files that you uploaded in Step 2 - Deploy to Relativity .

- To update the implementation code, click WikipediaKepler.Services.dll .

You only need to update these .dll and .pdb files because you didn't modify the interfaces.

- Click Edit .

The Resource File Information dialog appears.

- Click Clear in the Resource File field.

- Select your compiled WikipediaKepler.Services.dll to add as a new resource file.

- Click Save .

The updated .dll is uploaded to Relativity and the service is redeployed. If you want to remote debug this service, repeat steps 9-11 for the WikipediaKepler.Services.pdb file.

- After waiting a few minutes for the service to redeploy, repeat the REST call made in Step 3 - Test the deployed service .

The same results should be returned along with the new default value. Copy

```text
1
2
3
4
5
6
7
8
[

    {

        "Name": "NotARealWorkspace"

    },

    {

        "Name": "Hello Wikipedia Tutorial"

    }

]
```

## Step 6 - Implement methods on an interface

In this step, you implement each of the methods on the IWikipediaService interface in the IWikipediaService.cs file.

Use the following steps to add methods to the IWikipediaService interface:

- In Visual Studio, locate the IWikipediaService.cs file.

- In your IWikipediaService interface, remove the existing Kepler methods, GetWorkspaceNameAsync() and QueryWorkspaceByNameAsync().

- Do not change the WikipediaService constructor.

- Do not change the WikipediaService Dispose() method.

- Add the GetCategoriesByPrefixAsync() method to the IWikipediaService interface. Copy

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
...

/// <summary>

/// Returns a list of Categories in Wikipedia.

/// </summary>

/// <param name="prefix">Category prefix to limit results query of Categories in Wikipedia.</param>

/// <returns><see cref="CategoryResponseModel"/> with the title of the category.</returns>

/// <remarks>

/// Example REST request:

///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/categories?prefix=Star%20Wars

/// Example REST response:

///   [{"Title":"Star Wars: The Rise of Skywalker"},{"Title":"Star Wars: A New Hope"}]

/// </remarks>

[HttpGet]

[Route("categories?{prefix}")]

Task<List<CategoryResponseModel>> GetCategoriesByPrefixAsync(string prefix);

...
```

- Add the CategoryResponseModel to the following file in your project: WikipediaKepler.Interfaces > WIkipediaManagement > v1 > Models > CategoryResponseModel.cs . Copy

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
namespace WikipediaKepler.Interfaces.WikipediaManagement.v1.Models

{

    /// <summary>

    /// CategoryResponseModel Data Model.

    /// </summary>

    public class CategoryResponseModel

    {

        /// <summary>

        /// Title property.

        /// </summary>

        public string Title { get; set; }

    }

}
```

- Add an interface to later inject in our WikipediaService. Add the IRestService to the following file in your project: WikipediaKepler.Interfaces > WIkipediaManagement > v1 > IRestService.cs Copy

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
using System.Net.Http;

using System.Threading.Tasks;

namespace WikipediaKepler.Interfaces.WikipediaManagement.v1

{

    public interface IRestService

    {

        Task<HttpResponseMessage> GetAsync(string requestUri);

    }

}
```

- If System.Net.Http and HttpResponseMessage show up in Red, like in the picture below, you will need to add a reference to System.Net.Http

- Right click the WikipediaKepler.Interfaces project

- Choose Add > Reference

- In the Reference Manager dialog, check Assemblies > Framework > System.Net.Http 4.0.0 .

-

For the WikipediaKepler.Services project, you will have to add a reference to System.Net.Http, the same way we did in Step 6 above

- Add the implementation WikipediaRestService to the following file in your project: WikipediaKepler.Services > WIkipediaManagement > v1 > WikipediaRestService.cs Copy

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
using System;

using System.Net.Http;

using System.Threading.Tasks;

using WikipediaKepler.Interfaces.WikipediaManagement.v1;

namespace WikipediaKepler.Services.WikipediaManagement.v1

{

    public class WikipediaRestService : IRestService

    {

        private static Lazy<HttpClient> _httpClient = new Lazy<HttpClient>(() => new HttpClient()

        {

            BaseAddress = new Uri("https://en.wikipedia.org/w/")

        });

        private HttpClient HttpClient => _httpClient.Value;

        public async Task<HttpResponseMessage> GetAsync(string requestUri)

        {

            return await HttpClient.GetAsync(requestUri);

        }

    }

}
```

- Update the service constructor so that you can inject additional dependencies needed at runtime.

In the WikipediaService() method, add the additional private fields and update the constructor as illustrated in the following code sample.

With this update, you can avoid initializing other classes in the implementation, which increases the flexibility and reusability of the code. It also simplifies testing. The WikipediaService() method is in the WikipediaService.cs file.

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
...

private IRestService _restService;

private const int _CATEGORY_TITLE_INDEX = 9;



// Note: IHelper and ILog are dependency injected automatically into the constructor every time the service is called.

public WikipediaService(IHelper helper, ILog logger, IRestService restService)

{

    // Note: Set the logging context to the current class.

    _logger = logger.ForContext<WikipediaService>();

    _helper = helper;

    _restService = restService;

}

...
```

- Add the dependency injection code that injects IRestService at runtime. The classes extending IWindsorInstaller interface are injected and executed as part of the service deployment.

Complete these steps:

- Install the Castle.Windsor 3.3.0 NuGet package.

- Add the WikipediaServiceInstaller class to the following file in your project: WikipediaKepler.Services > WIkipediaManagement > v1 > WikipediaServiceInstaller.cs .

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
using Castle.MicroKernel.Registration;

using Castle.MicroKernel.SubSystems.Configuration;

using Castle.Windsor;

using WikipediaKepler.Interfaces.WikipediaManagement.v1;

namespace WikipediaKepler.Services.WikipediaManagement.v1

{

    public class WikipediaServiceInstaller : IWindsorInstaller

    {

        public void Install(IWindsorContainer container, IConfigurationStore store)

        {

            container.Register(Component.For<IRestService>().ImplementedBy<WikipediaRestService>().LifestyleTransient());

        }

    }

}
```

- Review API:Allcategories on the MediaWiki site before implementing GetCategoriesByPrefixAsync() method. Notice the request call and response format for retrieving a list of categories that match a specific prefix.

- Install the Newtonsoft.Json 6.0.8 NuGet package to use JSON as the response format.

- Add the following classes as internal models to simplify deserialization in the future implementation. These models are required for the implementation of the GetCategoriesByPrefixAsync() method.

Add the models to the following folder in your project: WikipediaKepler.Services > WikipediaManagement > v1 > Models .

View a list of models to implement

- Add a WikipediaQueryResponse.cs file with this code: Copy

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
namespace WikipediaKepler.Interfaces.WikipediaManagement.v1.Models

{

    /// <summary>

    /// PageForCategoryResponseModel Data Model.

    /// </summary>

    public class PageForCategoryResponseModel

    {

        /// <summary>

        /// Title property.

        /// </summary>

        public string Title { get; set; }

    }

}
```

- Add a Continue.cs file with this code: Copy

```text
1
2
3
4
5
6
7
namespace WikipediaKepler.Services.WikipediaManagement.v1.Models

{

    internal class Continue

    {

        public string CmContinue { get; set; }

    }

}
```

- Add a Query.cs file with this code: Copy

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
using System.Collections.Generic;

namespace WikipediaKepler.Services.WikipediaManagement.v1.Models

{

    internal class Query

    {

        public Dictionary<string, Page> Pages { get; set; }

        public List<Item> CategoryMembers { get; set; }

    }

}
```

- Add a Page.cs file with this code: Copy

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
using System.Collections.Generic;

namespace WikipediaKepler.Services.WikipediaManagement.v1.Models

{

    internal class Page : Item

    {

        public List<Item> Categories { get; set; }

        public string Extract { get; set; }

    }

}
```

- Add a Item.cs file with this code: Copy

```text
1
2
3
4
5
6
7
namespace WikipediaKepler.Services.WikipediaManagement.v1.Models

{

    internal class Item

    {

        public string Title { get; set; }

    }

}
```

- Implement the GetCategoriesByPrefixAsync() method in the WikipediaService.cs file. Copy

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
...

public async Task<List<CategoryResponseModel>> GetCategoriesByPrefixAsync(string prefix)

{

    var categories = new List<CategoryResponseModel>();

    HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&generator=allcategories&gacprefix={prefix}&prop=info&format=json");

    string content = await response.Content.ReadAsStringAsync();

    WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

    if (result.Query != null)

    {

        categories = result.Query.Pages.Values.Select(page => new CategoryResponseModel

        {

            Title = page.Title.Substring(_CATEGORY_TITLE_INDEX) // Substring to drop the 'Category:' prefix

        }

        ).ToList();

    }

    return categories;

}

...
```

- Add the GetPagesForCategoryAsync() method to the IWikipediaService interface in the IWikipediaService.cs file. Copy

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
...

/// <summary>

/// Get a list of pages under the provided Category in Wikipedia.

/// </summary>

/// <param name="categoryName">An existing Category in Wikipedia.</param>

/// <param name="pageSize">Number of results in the page.</param>

/// <param name="continueFrom">Identifier indicating where a paged result should be continued from. If '-', will start from the beginning.</param>

/// <returns><see cref="CategoryResponseModel"/> with the title of the category.</returns>

/// <remarks>

/// Example REST request:

///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/categories/Star%20Wars/pages?pageSize=10&continueFrom=page|123|456&pageSize=2

/// Example REST response:

///   [{"Title":"Star Wars: The Rise of Skywalker"},{"Title":"Star Wars: A New Hope"}]

/// </remarks>

[HttpGet]

[Route("categories/{categoryName}/pages?{pageSize}&{continueFrom}")]

Task<Pageable<PageForCategoryResponseModel>> GetPagesForCategoryAsync(string categoryName, int pageSize = 10, string continueFrom = "-");

...
```

- Add models that are required to support paging for categories to the following folder in your project: WikipediaKepler.Interfaces > WIkipediaManagement > v1 > Models .

- Add the Pageable.cs file with this code: Copy

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
using System.Collections.Generic;



namespace WikipediaKepler.Interfaces.WikipediaManagement.v1.Models

{

    /// <summary>

    /// A generic container for pageable results

    /// </summary>

    /// <typeparam name="T">Type of results</typeparam>

    public class Pageable<T>

    {

        /// <summary>

        /// List of results of type <typeparam name="T"></typeparam>

        /// </summary>

        public List<T> Results { get; set; }



        /// <summary>

        /// Identifier for next page of results, if any. Can be empty.

        /// </summary>

        public string Next { get; set; }

    }

}
```

- Add the PageForCategoryResponseModel.cs file with this code: Copy

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
using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;



namespace WikipediaKepler.Interfaces.WikipediaManagement.v1.Models

{

    /// <summary>

    /// PageForCategoryResponseModel Data Model.

    /// </summary>

    public class PageForCategoryResponseModel

    {

        /// <summary>

        /// Title property.

        /// </summary>

        public string Title { get; set; }

    }

}
```

- Implement the GetPagesForCategoryAsync() method in the WikipediaService.cs file.

It references the API:Categorymembers on the MediaWiki site. Copy

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
...

public async Task<Pageable<PageForCategoryResponseModel>> GetPagesForCategoryAsync(string categoryName, int pageSize = 10, string continueFrom = "-")

{

    var pages = new List<PageForCategoryResponseModel>();

    continueFrom = continueFrom == null || continueFrom.Equals("-") ? string.Empty : continueFrom;

    HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&list=categorymembers&cmtitle=Category:{categoryName}&cmlimit={pageSize}&cmcontinue={continueFrom}&format=json");

    string content = await response.Content.ReadAsStringAsync();

    WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

    if (result.Query != null)

    {

        pages = result.Query.CategoryMembers.Select(item => new PageForCategoryResponseModel { Title = item.Title }).ToList();

    }

    string next = result.Continue?.CmContinue ?? string.Empty;



    return new Pageable<PageForCategoryResponseModel>{ Results = pages, Next = next};

}

...
```

- Implement the GetPageByNameAsync() method on the IWikipediaService interface by adding it to the IWikipediaService.cs file. Copy

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
...

/// <summary>

/// Returns an existing page in Wikipedia.

/// </summary>

/// <param name="pageName">Name of the page in Wikipedia.</param>

/// <returns><see cref="PageResponseModel"/> with the Title, Url, and categories of the page.</returns>

/// <remarks>

/// Example REST request:

///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/Star%20Wars

/// Example REST response:

///  {"Title":"Star Wars", "Url":"https://en.wikipedia.org/wiki/Star_Wars", "Categories":[{"Title":"Star Wars: The Rise of Skywalker"}]}

/// </remarks>

[HttpGet]

[Route("pages/{pageName}")]

Task<PageResponseModel> GetPageByNameAsync(string pageName);

...
```

- Implement the PageResponseModel class for use with the GetPageByNameAsync() method.

This method requires a model used to return a standalone Page. Add the PageResponseModel.cs file to the WikipediaKepler.Interfaces > WIkipediaManagement > v1 > Models folder. Copy

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
using System.Collections.Generic;



namespace WikipediaKepler.Interfaces.WikipediaManagement.v1.Models

{

    /// <summary>

    /// PageResponseModel Data Model.

    /// </summary>

    public class PageResponseModel

    {

        /// <summary>

        /// Title property.

        /// </summary>

        public string Title { get; set; }



        /// <summary>

        /// Url property.

        /// </summary>

        public string Url { get; set; }



        /// <summary>

        /// Categories property.

        /// </summary>

        public List<CategoryResponseModel> Categories { get; set; }

    }

}
```

- Implement the GetPageByNameAsync() method in the WikipediaService.cs file.

It references the API:Categories on the MediaWiki site. Copy

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
...

public async Task<PageResponseModel> GetPageByNameAsync(string pageName)

{

    HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&format=json&titles={pageName}&prop=categories");

    string content = await response.Content.ReadAsStringAsync();

    WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

    Page page = result.Query.Pages.First().Value;

    if (page.Categories == null)

    {

        string errorMsg = $"Unable to find a page with name {pageName}.";

        _logger.LogError(errorMsg);

        throw new NotFoundException(errorMsg);

    }



    List<CategoryResponseModel> categories = page.Categories.Select(item => new CategoryResponseModel { Title = item.Title.Substring(_CATEGORY_TITLE_INDEX) }).ToList();

    return new PageResponseModel

    {

        Title = pageName,

        Url = $"https://en.wikipedia.org/wiki/{Uri.EscapeUriString(pageName)}",

        Categories = categories

    };

}

...
```

- Implement the GetPageTextAsync() method on the IWikipediaService interface by adding it to the IWikipediaService.cs file. Copy

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
...

/// <summary>

/// Returns a UTF-8 encoded text stream of an existing page in Wikipedia

/// </summary>

/// <param name="pageName">Name of the page in Wikipedia.</param>

/// <returns>A <see cref="IKeplerStream"/> containing a UTF-8 encoded text stream from the specified page.</returns>

/// <remarks>

/// Example REST request:

///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/Star%20Wars/text

/// Example REST response:

///  Star Wars is an American epic space-opera media franchise created by George Lucas[...]

/// </remarks>

[HttpGet]

[Route("pages/{pageName}/text")]

Task<IKeplerStream> GetPageTextAsync(string pageName);

...
```

- Implement the GetPageTextAsync() method in the WikipediaService.cs file.

It references the API:Get the contents of a page on the MediaWiki site. Copy

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
...

public async Task<IKeplerStream> GetPageTextAsync(string pageName)

{

    HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&prop=extracts&titles={pageName}&format=json");

    string content = await response.Content.ReadAsStringAsync();

    WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

    Page page = result.Query.Pages.First().Value;

    if (page.Extract == null)

    {

        throw new NotFoundException($"Unable to find a page with name {pageName}.");

    }

    var stream = new MemoryStream(Encoding.UTF8.GetBytes(page.Extract));

    return new KeplerStream(stream)

    {

        ContentType = "text/html",

        StatusCode = HttpStatusCode.OK

    };

}

...
```

- Verify that IWikipediaService interface is like the following code.

This code sample lists all the methods on the IWikipediaService interface that following steps describe how to implement.

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
using Relativity.Kepler.Services;

using Relativity.Kepler.Transport;

using System;

using System.Collections.Generic;

using System.Threading.Tasks;

using WikipediaKepler.Interfaces.WikipediaManagement.v1.Models;

namespace WikipediaKepler.Interfaces.WikipediaManagement.v1

{

    /// <summary>

    /// Wikipedia Service Interface.

    /// </summary>

    [WebService("wikipedia-service Service")]

    [ServiceAudience(Audience.Public)]

    [RoutePrefix("wikipedia-service")]

    public interface IWikipediaService : IDisposable

    {

        /// <summary>

        /// Returns a list of Categories in Wikipedia.

        /// </summary>

        /// <param name="prefix">Category prefix to limit results query of Categories in Wikipedia.</param>

        /// <returns><see cref="CategoryResponseModel"/> with the title of the category.</returns>

        /// <remarks>

        /// Example REST request:

        ///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/categories?prefix=Star%20Wars

        /// Example REST response:

        ///   [{"Title":"Star Wars: The Rise of Skywalker"},{"Title":"Star Wars: A New Hope"}]

        /// </remarks>

        [HttpGet]

        [Route("categories?{prefix}")]

        Task<List<CategoryResponseModel>> GetCategoriesByPrefixAsync(string prefix);



        /// <summary>

        /// Get a list of pages under the provided Category in Wikipedia.

        /// </summary>

        /// <param name="categoryName">An existing Category in Wikipedia.</param>

        /// <param name="pageSize">Number of results in the page.</param>

        /// <param name="continueFrom">Identifier indicating where a paged result should be continued from. If '-', will start from the beginning.</param>

        /// <returns><see cref="CategoryResponseModel"/> with the title of the category.</returns>

        /// <remarks>

        /// Example REST request:

        ///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/categories/Star%20Wars/pages?pageSize=10&continueFrom=page|123|456&pageSize=2

        /// Example REST response:

        ///   [{"Title":"Star Wars: The Rise of Skywalker"},{"Title":"Star Wars: A New Hope"}]

        /// </remarks>

        [HttpGet]

        [Route("categories/{categoryName}/pages?{pageSize}&{continueFrom}")]

        Task<Pageable<PageForCategoryResponseModel>> GetPagesForCategoryAsync(string categoryName, int pageSize = 10, string continueFrom = "-");



        /// <summary>

        /// Returns an existing page in Wikipedia.

        /// </summary>

        /// <param name="pageName">Name of the page in Wikipedia.</param>

        /// <returns><see cref="PageResponseModel"/> with the Title, Url, and categories of the page.</returns>

        /// <remarks>

        /// Example REST request:

        ///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/Star%20Wars

        /// Example REST response:

        ///  {"Title":"Star Wars", "Url":"https://en.wikipedia.org/wiki/Star_Wars", "Categories":[{"Title":"Star Wars: The Rise of Skywalker"}]}

        /// </remarks>

        [HttpGet]

        [Route("pages/{pageName}")]

        Task<PageResponseModel> GetPageByNameAsync(string pageName);



        /// <summary>

        /// Returns a UTF-8 encoded text stream of an existing page in Wikipedia

        /// </summary>

        /// <param name="pageName">Name of the page in Wikipedia.</param>

        /// <returns>A <see cref="IKeplerStream"/> containing a UTF-8 encoded text stream from the specified page.</returns>

        /// <remarks>

        /// Example REST request:

        ///   [GET] /Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/Star%20Wars/text

        /// Example REST response:

        ///  Star Wars is an American epic space-opera media franchise created by George Lucas[...]

        /// </remarks>

        [HttpGet]

        [Route("pages/{pageName}/text")]

        Task<IKeplerStream> GetPageTextAsync(string pageName);

    }

}
```

- Verify that your final WikipediaService implementation class is like the following code. Copy

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
using Relativity.API;

using Relativity.Kepler.Logging;

using Relativity.Services.Exceptions;

using System;

using System.Collections.Generic;

using System.Linq;

using System.Net.Http;

using System.Threading.Tasks;

using Newtonsoft.Json;

using WikipediaKepler.Interfaces.WikipediaManagement.v1;

using WikipediaKepler.Interfaces.WikipediaManagement.v1.Models;

using WikipediaKepler.Services.WikipediaManagement.v1.Models;

using Relativity.Kepler.Transport;

using System.IO;

using System.Net;

using System.Text;



namespace WikipediaKepler.Services.WikipediaManagement.v1

{

    public class WikipediaService : IWikipediaService

    {

        private IHelper _helper;

        private ILog _logger;

        private IRestService _restService;

        private const int _CATEGORY_TITLE_INDEX = 9;



        // Note: IHelper and ILog are dependency injected into the constructor every time the service is called.

        public WikipediaService(IHelper helper, ILog logger, IRestService restService)

        {

            // Note: Set the logging context to the current class.

            _logger = logger.ForContext<WikipediaService>();

            _helper = helper;

            _restService = restService;

        }



        public async Task<List<CategoryResponseModel>> GetCategoriesByPrefixAsync(string prefix)

        {

            var categories = new List<CategoryResponseModel>();

            HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&generator=allcategories&gacprefix={prefix}&prop=info&format=json");

            string content = await response.Content.ReadAsStringAsync();

            WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

            if (result.Query != null)

            {

                categories = result.Query.Pages.Values.Select(page => new CategoryResponseModel

                    {

                        Title = page.Title.Substring(_CATEGORY_TITLE_INDEX) // Substring to drop the 'Category:' prefix

                    }

                ).ToList();

            }

            return categories;

        }



        public async Task<Pageable<PageForCategoryResponseModel>> GetPagesForCategoryAsync(string categoryName, int pageSize = 10, string continueFrom = "-")

        {

            var pages = new List<PageForCategoryResponseModel>();

            continueFrom = continueFrom == null || continueFrom.Equals("-") ? string.Empty : continueFrom;

            HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&list=categorymembers&cmtitle=Category:{categoryName}&cmlimit={pageSize}&cmcontinue={continueFrom}&format=json");

            string content = await response.Content.ReadAsStringAsync();

            WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

            if (result.Query != null)

            {

                pages = result.Query.CategoryMembers.Select(item => new PageForCategoryResponseModel { Title = item.Title }).ToList();

            }

            string next = result.Continue?.CmContinue ?? string.Empty;



            return new Pageable<PageForCategoryResponseModel> { Results = pages, Next = next };

        }



        public async Task<PageResponseModel> GetPageByNameAsync(string pageName)

        {

            HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&format=json&titles={pageName}&prop=categories");

            string content = await response.Content.ReadAsStringAsync();

            WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

            Page page = result.Query.Pages.First().Value;

            if (page.Categories == null)

            {

                string errorMsg = $"Unable to find a page with name {pageName}.";

                _logger.LogError(errorMsg);

                throw new NotFoundException(errorMsg);

            }



            List<CategoryResponseModel> categories = page.Categories.Select(item => new CategoryResponseModel { Title = item.Title.Substring(_CATEGORY_TITLE_INDEX) }).ToList();

            return new PageResponseModel

            {

                Title = pageName,

                Url = $"https://en.wikipedia.org/wiki/{Uri.EscapeUriString(pageName)}",

                Categories = categories

            };

        }



        public async Task<IKeplerStream> GetPageTextAsync(string pageName)

        {

            HttpResponseMessage response = await _restService.GetAsync($"api.php?action=query&prop=extracts&titles={pageName}&format=json");

            string content = await response.Content.ReadAsStringAsync();

            WikipediaQueryResponse result = JsonConvert.DeserializeObject<WikipediaQueryResponse>(content);

            Page page = result.Query.Pages.First().Value;

            if (page.Extract == null)

            {

                throw new NotFoundException($"Unable to find a page with name {pageName}.");

            }

            var stream = new MemoryStream(Encoding.UTF8.GetBytes(page.Extract));

            return new KeplerStream(stream)

            {

                ContentType = "text/html",

                StatusCode = HttpStatusCode.OK

            };

        }



        /// <summary>

        /// All Kepler services must inherit from IDisposable.

        /// Use this dispose method to dispose of any unmanaged memory at this point.

        /// See https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose for examples of how to properly use the dispose pattern.

        /// </summary>

        public void Dispose()

        { }

    }

}
```

- Try out the methods on your IWikipediaService interface.

They communicate with the Wikipedia API to retrieve information. If you want to test them, upload your .dll and .pdb files again as in Step 2 - Deploy to Relativity .

## Step 7 - Logging

During the implementation of the Wikipedia Service, the ILog logger was used to log any errors that occurred. These logs are available in the EDDSLogging database in your Relativity instance. To view these logs, you can connect to the SQL database of your Relativity instance using Microsoft SQL Server Management Studio. Next, you need to execute a query against the EDDSLogging database.

Use the following steps to view logs:

- Open Microsoft SQL Server Management Studio.

- Connect to the IP address of your instance.

To obtain your SQL credentials, see in Additional information about DevVMs .

- Navigate to the databases on the instance now. They should look like the following screen shot:

-

Make a request that causes logging to occur.

For example, use the HTTP client and configuration from Step 1 - Create an empty Kepler service to make the following GET request:

Copy

```text
1
http://<your-host>/Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/non-existent-page-name
```

- Create a new query and execute it by pressing F5 or Execute in the menu.

The following query retrieves the most recent 1000 logs sorted by descending timestamp.

Update the query with your application GUID.

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

USE EDDSLogging;

SELECT TOP (1000) [ID]

      ,[Message]

      ,[MessageTemplate]

      ,[Level]

      ,[TimeStamp]

      ,[Exception]

      ,[Properties]

  FROM [EDDSLogging].[eddsdbo].[RelativityLogs]

  WHERE [Properties].value('(/properties/property[@key = "Application"]/text())[1]', 'varchar(100)') = 'YOUR APP GUID HERE'

  ORDER BY [TimeStamp] DESC
```

## Step 8 - Write a unit test

To shorten your development cycles, you can write unit tests that validate the functionality of a service. The following example includes only a single unit test, but you can write more unit tests to cover the functionality of your service.

Review these guidelines for writing unit tests:

- Test a single scenario per test.

- Mock any dependencies to ensure that the test is limited to only the behavior that you want to test.

- Follow testing best practices for naming conventions.

Use the following steps to write a unit test:

- Open the HelloWikipedia solution in Visual Studio.

- Right-click on the solution and click Add > New Project . The Add a new project dialog appears.

- Select Unit Test Project (.NET Framework) and click Next .

- Enter the following information in the Configure your new project dialog:

- Project name - WikipediaKepler.Tests

- Location - Location - set this field to the same root folder as your other projects, namely the WikipediaKepler folder.

- Framework - verify that this field is set to .NET Framework 4.6.2 .

- Click Create .

- To set up the required dependencies, right-click on the WikipediaKepler.Tests project, and click Add > Reference > Projects . The Reference Manager dialog appears.

- Select the checkboxes for the following projects:

- WikipediaKepler.Interfaces

- WikipediaKepler.Services

- Install the following NuGet packages:

- NUnit 3

- NUnit3TestAdapter

- Moq 4.5.3

- Newtonsoft.Json 6.0.8 Use Newtonsoft.Json 6.0.8 across all your projects for this tutorial. The matching versions prevent the tests from failing with IO exceptions.

- Relativity.Server.API.SDK 17.4.2

- Relativity.Server.Kepler.SDK 2.15.6

- Add a reference to System.Net.Http, just as you did for WikipediaKepler.Interfaces and WikipediaKepler.Services earlier

- Implement the WikipediaServiceTests class.

As a best practice, mirror the directory structure of the class under test. Add it to the following file in your project: WikipediaKepler.Tests > WikipediaManagement > v1 > WikipediaServiceTests.cs . Copy

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
using System;

using System.Collections.Generic;

using System.IO;

using System.Linq;

using System.Net;

using System.Net.Http;

using System.Text;

using System.Threading;

using System.Threading.Tasks;

using Moq;

using Moq.Protected;

using Newtonsoft.Json.Linq;

using NUnit.Framework;

using Relativity.API;

using Relativity.Kepler.Logging;

using Relativity.Services.Exceptions;

using WikipediaKepler.Interfaces.WikipediaManagement.v1;

using WikipediaKepler.Interfaces.WikipediaManagement.v1.Models;

using WikipediaKepler.Services.WikipediaManagement.v1;

namespace WikipediaKepler.Tests.WikipediaManagement.v1

{

    [TestFixture]

    public class WikipediaServiceTests

    {

        private Mock<IHelper> _helperMock;

        private Mock<ILog> _loggerMock;

        private Mock<IRestService> _restService;

        private const int _ONE_THOUSAND = 1000;

        private const string _WIDGETS = "Widgets";

        private readonly Random _rnd = new Random();

        [SetUp]

        public void SetUp()

        {

            _helperMock = new Mock<IHelper>();

            _loggerMock = new Mock<ILog>();

            _restService = new Mock<IRestService>();

        }

        [TearDown]

        public void TearDown()

        {

            _helperMock = null;

            _loggerMock = null;

            _restService = null;

        }

    }

}
```

- Implement a unit test for the GetCategoriesByPrefixAsync() method.

The following code illustrates a basic unit test for the GetCategoriesByPrefixAsync() method in the WikipediaServiceTests.cs file. Copy

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
...

private readonly Random _rnd = new Random();



[Test]

[Description("Verifies that when GetCategoriesByPrefixAsync is called a call is made to the Wikipedia API and matching categories are returned.")]

public async Task GetCategoriesByPrefixAsync_MatchingPrefix_ReturnsMatchingCategories()

{

    string prefix = "pre";

    string expectedCategory = $"{prefix}determined";

    var responseJson = new JObject

    {

        ["batchcomplete"] = "",

        ["query"] = new JObject

        {

            ["pages"] = new JObject

            {

                ["123456"] = new JObject

                {

                    ["pageid"] = _rnd.Next(0,_ONE_THOUSAND),

                    ["ns"] = _rnd.Next(0,_ONE_THOUSAND),

                    ["title"] = $"Category:{expectedCategory}"

                }

            }

        }

    };

    var response = new HttpResponseMessage

    {

        StatusCode = HttpStatusCode.OK,

        Content = new StringContent(responseJson.ToString())

    };

    _restService.Setup(_ => _.GetAsync(It.IsAny<string>())).ReturnsAsync(response);

    var service = new WikipediaService(_helperMock.Object, _loggerMock.Object, _restService.Object);

    List<CategoryResponseModel> actual = await service.GetCategoriesByPrefixAsync(prefix);

    Assert.That(actual.Count, Is.EqualTo(1));

    Assert.That(actual.First().Title, Is.EqualTo(expectedCategory));

}

...
```

- Run the test and verify that it passes.

Use this test as a model for adding coverage for edge cases, such as the behavior of your method when it receives an error from the Wikipedia API.

To quickly run all the tests, open the Test Explorer window in Visual Studio and click Run All Tests , or in the toolbar, click Tests > Run All Tests .

## Step 9 - Deploy and verify

After confirming that the interface successfully retrieves information from the Wikipedia API, and passes your local tests, you can add it to an application.

Use the following steps to add the interface to an application:

- Log in to your Relativity instance.

- Click to display your home page.

- In the Sidebar, click Other Tabs > Applications & Scripts > Resource Files .

The Resource Files tab appears.

- Click New Resource File .

The Resource File Information dialog appears.

- In the Name filter, type WikipediaKepler .

You should see the two .dlls and the 2 pds files that you uploaded in Step 2 - Deploy to Relativity .

- Click WikipediaKepler.Services.dll to update the implementation code.

- Click Edit .

The Resource File Information dialog appears.

- Click Clear in the Resource File field.

- Click to select your compiled WikipediaKepler.Services.dll to add as a new resource file.

- Click Save .

The updated .dll is uploaded to Relativity and the service is redeployed.

- Repeat steps 5 - 10 for the WikipediaKepler.Interfaces.dll , WikipediaKepler.Services.pdb , and the WikipediaKepler.Interfaces.pdb files.

- Use the following sample REST calls to see how your service functions in a Relativity environment after waiting a few minutes for the service to redeploy.

Your results might not exactly match the JSON in the expected results for these examples, because they execute against the live Wikipedia API and may change. Sample 1 - REST Call

- Method - GET

- URL - use the following URL: Copy

```text
1
<host>/Relativity.REST/api/wikipedia-management/v1/wikipedia-service/categories?prefix=Star%20Wars
```

- Headers - set the headers as follows. For more information, see Step 3 - Test the deployed service .

- X-CSRF-Header - set to a dash ( - ).

- Authorization - set to Basic <basic-authorization-token>.

- Expected results Copy

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
[

    {

        "Title": "Star Wars"

    },

    {

        "Title": "Star Wars: Battlefront"

    },

    {

        "Title": "Star Wars: Episode III – Revenge of the Sith"

    },

    {

        "Title": "Star Wars: Episode III – Revenge of the Sith video games"

    },

    {

        "Title": "Star Wars: Episode II – Attack of the Clones"

    },

    {

        "Title": "Star Wars: Episode II – Attack of the Clones video games"

    },

    {

        "Title": "Star Wars: Episode I – The Phantom Menace"

    },

    {

        "Title": "Star Wars: Episode I – The Phantom Menace video games"

    },

    {

        "Title": "Star Wars: Galaxy's Edge"

    },

    {

        "Title": "Star Wars: Jedi Apprentice"

    }

]
```

Sample 2 - REST Call

- Method - GET

- URL - use the following URL: Copy

```text
1
<host>/Relativity.REST/api/wikipedia-management/v1/wikipedia-service/categories/Star%20Wars/pages?pageSize=5
```

- Headers - set the headers as follows. For more information, see Step 3 - Test the deployed service .

- X-CSRF-Header - set to a dash ( - ).

- Authorization - set to Basic <basic-authorization-token>.

- Expected results Copy

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
{

    "Results": [

        {

            "Title": "Charley Lippincott"

        },

        {

            "Title": "Star Wars"

        },

        {

            "Title": "Clone Wars (Star Wars)"

        },

        {

            "Title": "Comparison of Star Trek and Star Wars"

        },

        {

            "Title": "Death Star (business)"

        }

    ],

    "Next": "page|313f4d4f4b3131044d4f512f39454d011301dcbfdc0a|594188"

}
```

Sample 3 - REST Call

- Method - GET

- URL - use the following URL: Copy

```text
1
<host>/Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/Star%20Wars
```

- Headers - set the headers as follows. For more information, see Step 3 - Test the deployed service .

- X-CSRF-Header - set to a dash ( - ).

- Authorization - set to Basic <basic-authorization-token>.

- Expected results Copy

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
{

    "Title": "Star Wars",

    "Url": "https://en.wikipedia.org/wiki/Star%20Wars",

    "Categories": [

        {

            "Title": "20th Century Fox films"

        },

        {

            "Title": "Action film franchises"

        },

        {

            "Title": "Adventure film series"

        },

        {

            "Title": "All Wikipedia articles written in American English"

        },

        {

            "Title": "All articles needing additional references"

        },

        {

            "Title": "All articles with unsourced statements"

        },

        {

            "Title": "American epic films"

        },

        {

            "Title": "American science fantasy films"

        },

        {

            "Title": "Articles needing additional references from January 2020"

        },

        {

            "Title": "Articles with short description"

        }

    ]

}
```

Sample 4 - REST Call

- Method - GET

- URL - use the following URL: Copy

```text
1
<host>/Relativity.REST/api/wikipedia-management/v1/wikipedia-service/pages/Star%20Wars/text
```

- Headers - set the headers as follows. For more information, see Step 3 - Test the deployed service .

- X-CSRF-Header - set to a dash ( - ).

- Authorization - set to Basic <basic-authorization-token>.

- Expected results Copy

```text
1
<Displays the plain text content of the Star Wars Wikipedia entry.>
```

- Try out other API calls with your Kepler service.

On this page

- Lesson 3 - Create a RESTful API

- Before you begin

- Step 1 - Create an empty Kepler service

- Step 2 - Deploy to Relativity

- Step 3 - Test the deployed service

- Step 4 - Remote debugging

- Verify the remote debugger is running

- Remotely debug your code

- Step 5 - Update the service

- Step 6 - Implement methods on an interface

- Step 7 - Logging

- Step 8 - Write a unit test

- Step 9 - Deploy and verify


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
