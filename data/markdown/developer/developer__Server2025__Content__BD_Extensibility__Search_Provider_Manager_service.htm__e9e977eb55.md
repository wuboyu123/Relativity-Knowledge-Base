---
title: "Legacy Search Provider Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Search_Provider_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:33:19+00:00
sha256: 5c22100eaf266ba1b921fadd954eebbfbd561bfcf513bb20b005c56b3d6d0dcc
---

Legacy Search Provider Manager (REST)

# Legacy Search Provider Manager (REST)

The Search Provider Manager service available in the REST API retrieves a list of active search providers in a workspace. It also retrieves the HTML markup used to display the search provider in the Relativity UI. This service returns the following search providers supported by Relativity, as well as custom search providers, when active in a workspace that you query:

- Keyword search provider

- dtSearch provider

- Analytics search provider

- Data Grid search provider

The service returns search providers for a given workspace based on the Artifact Type for a Relativity object that you define in the query. For example, you might specify the value for Artifact Type identifier associated with Document or Field objects.

You can use this service to provide an index search in a custom HTML page. For example, you could build a custom page where you include a search provider, and then utilize this service to retrieve the markup needed to display it.

You can also use the Relativity Services API to retrieve SearchProvider objects. Through the Services API, this service supports the use of progress indicators or cancelation tokens. For more information, see Retrieve search providers.

## Client code sample

To interact with the Search Provider Manager service, you send HTTP(S) requests that use the POST method and specify query conditions in the body of the request. See the base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Provider%20Manager/
```

You can use the following .NET code as the REST client for retrieving search providers. The code illustrates how to instantiate an HttpClient object for sending requests and responses by the URL for the Search Provider Manager service.

It also illustrates how to deserialize the response into a SearchProviderResultSet object available in the Services API. The SearchProviderResultSet object consists of a list of search providers and HTML markup collections. Each search provider has a MarkupId property that contains the unique identifier associated with its respective markup collection. This ID links the search provider to a specific markup collection returned in the SearchProviderResultSet object.

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
public List<Relativity.Services.Search.SearchProvider> GetActiveHtmlSearchProvidersAsync(int workspaceId, int artifactTypeId, bool useAdvancedSearch)

{

    using (var httpClient = new System.Net.Http.HttpClient())

    {

        List<Relativity.Services.Search.SearchProvider> searchProviders = null;

        httpClient.BaseAddress = new Uri("http://localhost/Relativity.REST/API/");

        httpClient.DefaultRequestHeaders.Add("Accept", "application/json");

        httpClient.DefaultRequestHeaders.Add("X-CSFRF-Header", string.Empty);

        httpClient.DefaultRequestHeaders.Add("Authorization", "Basic bXkudXNlckBrY3VyYS5jb206Q250VGNoVGhzMTIzNCE=");

        //Initialize the parameters that you want to use to identify the workspace, object type, and type of markup that you want to use for the query.

        var parameters = new

        {

            workspaceId = workspaceId,

            artifactTypeId = artifactTypeId,

            useAdvancedSearch = useAdvancedSearch

        };

        System.Net.Http.StringContent parametersJson = new System.Net.Http.StringContent(Newtonsoft.Json.JsonConvert.SerializeObject(parameters), System.Text.Encoding.UTF8, "application/json");

        //Define the REST endpoint for the Search Provider Manager service.

        String searchProviderUrl = "Relativity.Services.Search.ISearchModule/Search%20Provider%20Manager/GetActiveHtmlSearchProvidersAsync";

        //Make the HTTP request against the endpoint of the Search Provider Manager service.

        System.Net.Http.HttpResponseMessage response = httpClient.PostAsync(searchProviderUrl, parametersJson).Result;

        bool success = response.StatusCode == System.Net.HttpStatusCode.OK;

        String result = response.Content.ReadAsStringAsync().Result;

        if (success)

        {

            //Deserialize the response string into a SearchProviderResultSet object.

            Relativity.Services.Search.SearchProviderResultSet resultSet = Newtonsoft.Json.JsonConvert.DeserializeObject<Relativity.Services.Search.SearchProviderResultSet>(result);

            //Retrieve the search providers.

            searchProviders = resultSet.SearchProviders;

        }

        return searchProviders;

    }

}
```

## Read a SearchProvider

To retrieve the active HTML supported search providers and their respective markup, send a request to this URL for the Search Provider service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.Search.ISearchModule/Search%20Provider%20Manager/GetActiveHtmlSearchProvidersAsync
```

The request must include the following fields:

- workspaceId – the Artifact ID of the workspace where you want to run queries with the search provider.

- artifactTypeId – the Artifact Type identifier of the data transfer object (DTO) used in the queries executed by your search provider. In the following request, the artifactTypeId is set to 10, which indicates documents. The response returns only search providers for documents.

- useAdvancedSearch – Set this value to false to return basic search markup or to true to return advanced search markup.

The Keyword, dtSearch, Analytics, and Data Grid search providers don't currently support returning advanced search markup.

Copy

```text
1
2
3
4
5
{

    workspaceId: 1020741,

    artifactTypeId: 10,

    useAdvancedSearch: false

}
```

The response returns a list of SearchProvider objects that you requested. It contains the following information about each object:

- Artifact ID for each the search provider

- Name of each search provider, which displays in the Relativity UI.

- MarkupID used to identify the HTML markup required to display a specific search provider.

It also includes the MarkupCollection, which contains the HTML markup used to display the search providers in the UI.

All search providers must register themselves by calling relativity.registerSearchProviderCallbacks. To consume these search providers in a custom HTML page, define relativity.registerSearchProviderCallbacks as a function in the JavaScript of your custom page.

View a JSON response for the retrieval of a SearchProvider Copy

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
{

  "Success": true,

  "Message": "",

  "SearchProviders": [

    {

      "ArtifactId": 1035269,

      "Name": "Keyword Search",

      "MarkupId": "markup_0"

    }

  ],

  "MarkupCollection": [

    {

      "Id": "markup_0",

      "Markup": "<script type='text/javascript'>

        (function registerCallbacks($, relativity) {

          function generateXMLString(searchText, sortByRank) {

            var inputString = '<? xml version = \"1.0\" encoding=\"utf-16\"?>';

            inputString += '<InputData xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">';

            inputString += '<SortByRank xmlns=\"kCura.EDDS.SQLServer2005SearchProvider\">';

            inputString += sortByRank;

            inputString += '</SortByRank>';

            inputString += '<SearchText xmlns=\"kCura.EDDS.SQLServer2005SearchProvider\">';

            inputString += $('<div />').text(searchText).html();

            inputString += '</SearchText>';

            inputString += '</InputData>';

            return inputString;

          }

          function getInput() {

            var $checkbox = $('#keywordSearchRank_markup_0'),

            $textArea = $('#keywordSearchText_markup_0'),

            isChecked = $checkbox.prop('checked'),

            searchText = $textArea.val();

            return {

              input: generateXMLString(searchText, isChecked),

              filterDisplay: searchText

            };

          }

          function clear() {

            var $checkbox = $('#keywordSearchRank_markup_0'),

            $textArea = $('#keywordSearchText_markup_0');

            $checkbox.prop('checked', false);

            $textArea.val('');

          }

          function rehydrate(inputString) {

            var $checkbox = $('#keywordSearchRank_markup_0'),

            $textArea = $('#keywordSearchText_markup_0'),

            parsedXml = $.parseXML(inputString),

            $xmlDoc = $(parsedXml),

            sortByRank = $xmlDoc.find('SortByRank').text(),

            searchText = $xmlDoc.find('SearchText').text();

            if (sortByRank === true || sortByRank === 'true') {

              $checkbox.prop('checked', true);

            }

            if (typeof searchText === 'string') {

              $textArea.val(searchText);

            }

          }

          var registrationSettings = {

            idSuffix: 'markup_0',

            getInputCallback: getInput,

            clearFormCallback: clear,

            hydrateFormCallback: rehydrate

          };

          relativity.registerSearchProviderCallbacks(registrationSettings);

        }(jQuery, relativity));

      </script>

      <section class='searchprovider-search-container'>

        <div class='searchprovider-text-label-container'>

          <span class='searchprovider-text-label'>Search Terms:</span>

        </div>

        <div class='searchprovider-text-container'>

          <textarea id='keywordSearchText_markup_0' class='searchprovider-search-text'></textarea>

        </div>

        <div class='searchprovider-rank-container'>

          <input id='keywordSearchRank_markup_0' class='searchprovider-rank-checkbox' type='checkbox' name='keywordSearchRank_markup_0'></input>

          <label class='searchprovider-rank-label' for='keywordSearchRank_markup_0'>Sort by rank</label>

        </div>

      </section>"

    }

  ]

}
```
