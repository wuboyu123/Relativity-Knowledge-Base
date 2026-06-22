---
title: "Legacy Search Provider Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Search_Provider_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:33:18+00:00
sha256: 3e60e5e35a332c57e49bb7a320f0eac02b8157ac8af84b1b77e4da6bef7696ef
---

Legacy Search Provider Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Legacy Search Provider Manager (.NET)

You can use the Search Provider Manager service to retrieve a list of active search providers in a workspace, and then display them in the Relativity UI framework. This service returns the following search providers supported by Relativity, as well as custom search providers, when active in a workspace that you query:

- Keyword search provider

- dtSearch provider

- Analytics search provider

- Data Grid search provider

It also returns the HTML markup used to display the search provider in the UI.

You can use this service to provide an index search in a custom HTML page. For example, you could build a custom page that includes a search provider, and then utilize this service to retrieve the markup needed to display it. As illustrated in the following screen shot, the Search Provider Manager service returns the HTML markup outlined in red for an index or keyword search. Each search provider has its own HTML markup that controls how it appears in the new UI framework.

The type of search provider controls the HTML markup used to render it. If you want to customize the markup, you need to build your own search provider.

You can also use the Search Provider Manager service through the REST API, but it doesn't support cancellation tokens or progress indicators. For more information, see Search providers .

## Search provider fundamentals

In the Services API, the Relativity.Services.Search namespace contains the ISearchProviderManager interface and other classes required to query for active search providers in a workspace. You use the ISearchProviderManager interface to access the Search Provider Manager service, and the methods that it provides for retrieving search providers. This interface contains a single overloaded method called GetActiveHtmlSearchProvidersAsync(). When calling this method, you must specify the following arguments:

- Artifact ID – identifier for the workspace that you want to search for the provider.

- Artifact Type ID – indicates the data transfer object (DTO) used in the queries executed by your search provider. For example, an Artifact Type ID of 10 indicates that you want the results set to include only search providers that return Document objects.

- useAdvancedSearch – Set this value to false to return basic search markup or to true to return advanced search markup.

The Keyword, dtSearch, Analytics, and Data Grid search providers don't currently support returning advanced search markup.

If you use an overloaded method, you can also pass the following arguments:

- CancelationToken – used to request the cancellation of a query executed by the Search Provider Manager service. The ISearchProviderManager interface includes overloaded methods that take an object of the type System.Threading.CancellationTokenSource provided by the .NET framework.

- IProgress<ProgressReport> object – used to define a provider for progress updates. The ISearchProviderManager interface includes overloaded methods that take an object of the type System.IProgress provided by the .NET framework.

Each of the overloaded methods that the Search Provider Manager service supports returns a SearchProviderResultSet object that contains a list of active search providers and the markup that they use for display in the Relativity UI framework.

In addition, the Relativity.Services.Search namespace also contains the following classes that you use when querying on search providers:

- SearchProvider class – This class has multiple properties that you use to define a search provider, including its Artifact ID, a unique identifier for its markup set, and the name of the search provider as displayed in the UI.

- SearchProviderMarkup class – This class has properties that define the HTML markup used to display a search provider, including a unique identifier for the markup, and the string containing the markup.

- SearchProviderResultSet class – The GetActiveHtmlSearchProvidersAsync() method returns an object of this type when a query executes successfully. A SearchProviderResultSet object consists of a list of search providers and HTML markup collections. Each search provider has a MarkupId property that contains the unique identifier associated with its respective markup collection. This ID links the search provider to a specific markup collection returned in the SearchProviderResultSet object.

## Retrieve search providers

You can use the following code samples to learn about how the Search Provider Manager service retrieves search providers. It also illustrates how to cancel a search request and how to provide progress information to the users.

To provide users with the ability to cancel a query, instantiate a new CancellationTokenSource object. You can call the Cancel() method on this object when a user clicks the Cancel button in the UI.

Copy

```text
1
private System.Threading.CancellationTokenSource _cancellationTokenSource = new System.Threading.CancellationTokenSource();
```

Next, instantiate a SearchProviderManager object using the ServiceFactory class:

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
//Create a SearchProviderManager instance using the ServiceFactory constructor.

private Relativity.Services.Search.ISearchProviderManager GetSearchProviderManager()

{

    String restServerAddress = "http://localhost/relativity.rest/api";

    String rsapiServerAddress = "http://localhost/relativity.services/api";

    Uri keplerUri = new Uri(restServerAddress);

    Uri servicesUri = new Uri(rsapiServerAddress);

    Relativity.Services.ServiceProxy.ServiceFactorySettings settings = new Relativity.Services.ServiceProxy.ServiceFactorySettings(

             servicesUri, keplerUri, new Relativity.Services.ServiceProxy.UsernamePasswordCredentials("jsmith@example.com", "ExamplePassword1!"));

    var serviceFactory = new Relativity.Services.ServiceProxy.ServiceFactory(settings);

    Relativity.Services.Search.ISearchProviderManager searchProviderManager = serviceFactory.CreateProxy<Relativity.Services.Search.ISearchProviderManager>();

    return searchProviderManager;

}
```

In addition, you can instantiate a SearchProviderManager object using the Relativity API Helpers. Use this approach if you want use the Search Provider Manager service from a custom page. For more information, see Use Relativity API Helpers .

Copy

```text
1
Relativity.Services.Search.ISearchProviderManager searchProviderManager = Relativity.CustomPages.ConnectionHelper.Helper().GetServicesManager().CreateProxy<Relativity.Services.Search.ISearchProviderManager>(Relativity.API.ExecutionIdentity.System);
```

Implement a custom method that takes a ProgressReport object used to capture information about the execution of a service by referencing the Message, CompletedSteps, and TotalSteps properties. You can then define how you want this information displayed for users.

Copy

```text
1
2
3
4
private void SearchProviderManagerProgress(Relativity.Services.DataContracts.DTOs.ProgressReport progressReport)

{

    //Optionally, define how to display the progress messages.

}
```

Implement a handler that calls the Cancel() method on the CancellationTokenSource object when the user clicks a Cancel button.

Copy

```text
1
2
3
4
5
//Define a handler function that is called when the user clicks a Cancel button.

public void CancelButton_Clicked()

{

    _cancellationTokenSource.Cancel();

}
```

To run a query for search providers, implement a method that returns a list of search providers and performs the following tasks:

- Get the SearchProviderManager object that you instantiated using the ServiceFactory class.

- Instantiate a Progress object by passing the constructor the SearchProviderManagerProgress callback function. Each time that the Search Provider Manager service publishes a progress message, it calls this function.

If you want to use the progress functionality, you need to implement this callback function.

- Call the GetActiveHtmlSearchProvidersAsync() method on the ISearchProviderManager interface.

- Run the query in a try-catch block.

- Return a list of search providers or an error message.

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
//Instantiate a SearchProviderManager object and retrieve the active HTML search providers by passing the workspaceId, artifactTypeId, and useAdvancedSearch

//arguments to the GetActiveHtmlSearchProvidersAsync() method.

public List<Relativity.Services.Search.SearchProvider> GetActiveHtmlSearchProvidersAsync(int workspaceId, int artifactTypeId, bool useAdvancedSearch)

{

    Relativity.Services.Search.ISearchProviderManager searchProviderManager = GetSearchProviderManager();

    //Define a progress reporter that provides information about the status of the query.

    System.Progress<Relativity.Services.DataContracts.DTOs.ProgressReport> progressReporter = new Progress<Relativity.Services.DataContracts.DTOs.ProgressReport>(SearchProviderManagerProgress);

    //Make the service call using the instantiated Search Provider Manager object.

    System.Threading.Tasks.Task<Relativity.Services.Search.SearchProviderResultSet> executeTask = searchProviderManager.GetActiveHtmlSearchProvidersAsync(workspaceId, artifactTypeId, useAdvancedSearch, _cancellationTokenSource.Token, progressReporter);

    string errorMessage = string.Empty;

    List<Relativity.Services.Search.SearchProvider> searchProviders = null;

    //Run the query and return the results as a SearchProviderResultSet object. Use a try-catch block to capture and optionally display

    //an error message if the query fails.

    try

    {

        executeTask.Wait();

        Relativity.Services.Search.SearchProviderResultSet results = executeTask.Result;

        if (results.Success)

        {

            //Optionally, define add code to handle the results.

            searchProviders = results.SearchProviders;

        }

        else

        {

            errorMessage = results.Message;

        }

    }

    catch (Exception exception)

    {

        errorMessage = exception.ToString();

    }

    if (!string.IsNullOrWhiteSpace(errorMessage))

    {

        //Optionally, define how to display the error message.

    }

    return searchProviders;

}
```

On this page

- Legacy Search Provider Manager (.NET)

- Search provider fundamentals

- Retrieve search providers


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
