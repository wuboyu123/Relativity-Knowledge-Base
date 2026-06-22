---
title: "Search Terms Report Services (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Search_Terms_Report/Search_Terms_Report_Services_API.htm
collection: developer
fetched_at: 2026-06-22T06:22:27+00:00
sha256: 66c7dcd7ef36ba852908223fee9d6ee1314b775cb08ae7dd32108df596e51669
---

Search Terms Report Services (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Search Terms Report Services (.NET)

Search terms reports provide the ability to identify documents containing specific keywords or terms. You can enter multiple terms and generate a report listing the number of hits for each term in a document. For more information, see Search terms report in the Relativity Documentation site.

The Search Terms Report Services API provides functionality for generating a search terms report, adding terms to an existing search terms report, retrying any errors, and viewing the build progress of a specific search terms report.

The following sample use cases illustrate how you can use this API:

- Create a new search terms report.

- Add or update terms in a search terms report.

- Run terms against a new search terms report.

- Refresh a search terms report when document results have changed.

- Run additional terms on an existing search terms report.

- Retry any errors from a previous run of this API.

- Get the progress of any running terms in a search terms report.

- Retrieve the report from executing a search terms report.

You can also use the Search Terms Report Services API through REST. For more information, see Search Terms Report Services (REST) .

## Fundamentals for the Search Terms Report Services API

Review the following information to learn about the methods and classes used by the Search Terms Report Services API.

### Methods

The Search Terms Report Services API includes the following methods available on the ISearchTermsReportManager interface in the Relativity.SearchTermsReport.<VersionNumber>.Interfaces namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CancelJob() method - cancels a running job a search terms report. See Cancel a running search terms report job .

- CreateTerms() method - creates terms used in a search terms report. See Create terms for a search terms report .

- GetProgress() method - retrieves the build progress for a search terms report. See View the build progress of a search terms report .

- GetReportTypeIDs() method - retrieves the report type choice IDs for a specific workspace. See Retrieve the report type choice IDs .

- GetReportUrl() method - retrieve the URL used to navigate to a search terms report. See Retrieve the URL for a search terms report .

- GetResultsUrl() method - builds the URL used for navigating to the Search Terms Result tab with the appropriate filter criteria for the search terms report. See Retrieve the URL for the Search Terms Result tab .

- IndexContainsLongTextField() method - checks whether the specified searchable set contains at least one long text field. See Search Terms Report Services (.NET) .

- RetryErrors() method - queues a Retry Errors job for a search terms report. This methods attempts to regenerate the report for search terms that returned error messages. See Retry errors in a search terms report .

- RunAllTerms() method - queues a Run All Terms job for a search terms report. This method generates counts for each term. You can use this method the first time that you generate a report and to regenerate the count for a report already run. See Run all terms in a search terms report .

- RunPendingTerms() method - queues a Run Pending Terms job for a search terms report. You can use this method to add terms to the report by updating any terms that have a pending status. See Run pending terms in a search terms report .

- UpdateTerms() method - updates a list of Search Term Results terms with the text and color changes specified in the update request. See Update terms for a search terms report .

### Classes and enumerations

The following list contains key classes and enums used by the Search Terms Report Services API :

- ApplicationGuids class - contains GUIDs for the search terms report application.

- Enums - contains the search terms report enumerations.

- SearchTermsResultCreateResponse class - contains the following properties:

- TermsAffected - the number of terms successfully created or updated.

- TermsSkippedAsDuplicated - the number of terms that were not created or updated because the term duplicate an existing one.

- TermsSkippedForLength - the number of terms that were not created or updated because the text length of the term exceeded the maximum character count of 450.

- TermsSkippedAsErrors - the number of terms that were not created or updated because errors occurred while executing operations on the them.

- SearchTermsResultCreateRequest class - contains the following properties:

- TermsToAdd - a List of terms to add.

- RelativityHighlightColor - a semicolon delimited string where the first number corresponds to the background color and second number is the text color based on this enumeration.

View enumeration

- Default = 0,

- Black = 1,

- DarkRed = 2,

- DarkGreen = 3,

- DarkYellow = 4,

- DarkBlue = 5,

- DarkMagenta = 6,

- DarkCyan = 7,

- LightGray = 8,

- Gray = 9,

- Red = 10,

- Green = 11,

- Yellow = 12,

- Blue = 13,

- Magenta = 14,

- Cyan = 15,

- White = 16,

- LightGreen = 17,

- LightBlue = 18,

- LightYellow = 19,

- LightPurple = 20,

- LightRed = 21,

- LightOrange = 22,

- Purple = 23,

- Orange = 24,

- DarkPurple = 25,

- DarkOrange = 26

- SearchTermsResultUpdateRequest class - contains the following properties:

- UpdatedTerms - a List of SearchTermsResultsTermUpdatedTerm objects containing the Artifact ID and updated term name.

- RelativityHighlightColor - see SearchTermsResultUpdateRequest class for a description.

- SearchTermsResultsTermUpdatedTerm class - contains the following properties:

- ArtifactID - the ArtifactID of the term to update.

- Newterm - the new name of the term.

## Create a Search Term Report

The following code snippet demonstrates the workflow to create a new Search Terms Report using a combination of Object Manager and Search Terms Report Manager calls.

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
public static async Task Main(string[] args)

{

   int workspaceID = 1017814;  //TODO: specify your workspace ID

   Dictionary<string, int> reportTypes = await GetSTReportTypeIDs(workspaceID).ConfigureAwait(false);

   int reportTypeAndTag = reportTypes["Report and tag"];  //or "Report only"

   int searchableSet = await GetSearchableSet(workspaceID, "Extracted Text Only").ConfigureAwait(false);

   int dtSearchIndexID = await GetDTSearchIndex(workspaceID).ConfigureAwait(false);

   int strID = await CreateSTR(helper, workspaceID, dtSearchIndexID, searchableSet, reportTypeAndTag).ConfigureAwait(false);

}

public static async Task<Dictionary<string,int>> GetSTReportTypeIDs(int workspaceID)

{

   using (var strManager = _proxy.GetClient<ISearchTermsReportManager>())

   {

      return await strManager.GetReportTypeIDs(workspaceID).ConfigureAwait(false);

   }

}

public static async Task<int> CreateSTR(int workspaceID, int dtSearchIndex, int searchableSet, int strType)

{

   using (var objManager = _proxy.GetClient<IObjectManager>())

   {

      Guid strObjectTypeGuid = new Guid("481E9ACF-368B-4341-B6B5-A21153AD9950");  //Guid of STR Object Type

      var createRequest = new CreateRequest();

      createRequest.ObjectType = new ObjectTypeRef { Guid = strObjectTypeGuid };

      createRequest.FieldValues = new List<FieldRefValuePair>()

      {

         new FieldRefValuePair {Field = new FieldRef { Name = "Name"}, Value = "Test STR from API" },

         new FieldRefValuePair {Field = new FieldRef { Name = "Index"}, Value = new RelativityObjectRef{ArtifactID = dtSearchIndex} },

         new FieldRefValuePair {Field = new FieldRef {Name = "Searchable set"},Value = new RelativityObjectRef{ArtifactID = searchableSet}},

         new FieldRefValuePair {Field = new FieldRef { Name = "Include Relational Group"}, Value = null },

         new FieldRefValuePair {Field = new FieldRef { Name = "Type"}, Value = new RelativityObjectRef{ArtifactID = strType} },

         new FieldRefValuePair {Field = new FieldRef { Name = "Calculate Unique Hits"}, Value = false },

         new FieldRefValuePair {Field = new FieldRef { Name = "Email Notification Recipients"}, Value = null },

         new FieldRefValuePair {Field = new FieldRef { Name = "Notes"}, Value = null },

         new FieldRefValuePair {Field = new FieldRef { Name = "Show In Field Tree"}, Value = true },

         new FieldRefValuePair {Field = new FieldRef { Name = "Remove Hidden Characters In Terms"}, Value = true }

      };

      CreateResult result = await objManager.CreateAsync(workspaceID, createRequest, new OperationOptions());

      return result.Object.ArtifactID;

   }

}

public static async Task<int> GetSearchableSet(int workspaceID, string searchName)

{

   using (var searchManager = _proxy.GetClient<IKeywordSearchManager>(

   {

      Condition condition = new TextCondition("Name", TextConditionEnum.EqualTo, searchName);

      Query query = new Query();

      query.Condition = condition.ToQueryString();

      KeywordSearchQueryResultSet queryResultSet = await searchManager.QueryAsync(workspaceID, query).ConfigureAwait(false);

      return queryResultSet.Results[0].Artifact.ArtifactID;

   }

}

public static async Task<int> GetDTSearchIndex(int workspaceID)

{

   int indexID;

   using (var objManager = _proxy.GetClient<IObjectManager>())

   {

      var queryRequest = new QueryRequest()

      {

         ObjectType = new ObjectTypeRef { Name = "Search Index" },

         Condition = "'Name' == 'test index'",

         Fields = new List<FieldRef>() { new FieldRef { Name = "Name" }, new FieldRef {Name = "Type"} }

      };

      QueryResultSlim result = await objManager.QuerySlimAsync(workspaceID, queryRequest, 1, 100).ConfigureAwait(false);

      indexID = Convert.ToInt32(result.Objects[0].ArtifactID);

   }

   return indexID;

}
```

## Create terms for a search terms report

Use the CreateTerms() method to create terms used in a search terms report. Pass the following arguments to this method:

- Artifact ID of a workspace

- Artifact ID of a search terms report

- SearchTermsResultCreateRequest object - for a list of properties, see Classes and enumerations .

The CreateTerms() method returns a SearchTermsResultCreateResponse object. See Classes and enumerations .

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
public async Task<SearchTermsResultResponse> CreateTerms(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

    using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

    {

        SearchTermsResultCreateRequest termsRequest = new SearchTermsResultCreateRequest()

        {

            TermsToAdd = new List<string> { "term1", "term2" },

            RelativityHighlightColor = "5;16"

        };

        Return await searchTermsReportManager.CreateTerms(workspaceID, searchTermsReportID, termsRequest).ConfigureAwait(false);

    }

}
```

## Update terms for a search terms report

Use UpdateTerms() method to modify existing terms used in a search terms report. Pass the following arguments to this method:

- Artifact ID of a workspace

- Artifact ID of a search terms report

- SearchTermsResultUpdateRequest object - for a list of properties, see Classes and enumerations .

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
public async Task<SearchTermsResultResponse> UpdateTerms(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

    using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

    {

        SearchTermsResultUpdateRequest termRequest = new SearchTermsResultUpdateRequest()

        {

            UpdatedTerms = new List<SearchTermsResultsTermUpdatedTerm>()

                    {

            new SearchTermsResultsTermUpdatedTerm()

                           {

                  ArtifactID = 1169116,

               NewTerm = "New Term Name"

                           }

                    },

            RelativityHighlightColor = "5;16"

        };

        Return await searchTermsReportManager.UpdateTerms(workspaceID, searchTermsReportID, termsRequest).ConfigureAwait(false);

    }

}
```

## Run all terms in a search terms report

Use the RunAllTerms() method to queue a Run All Terms job for a search terms report. This method generates counts for each term. You can use this method the first time you generate a report and to regenerate the count for a report already run.

The following code sample illustrates how to call the RunAllTerms() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async System.Threading.Tasks.Task RunAllTerms(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      await searchTermsReportManager.RunAllTerms(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## Run pending terms in a search terms report

Use the RunPendingTerms() method to queue a Run Pending Terms job for a search terms report. You can add terms to the report by updating any terms that have a pending status.

The following code sample illustrates how to call the RunPendingTerms() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async System.Threading.Tasks.Task RunPendingTerms(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      await searchTermsReportManager.RunPendingTerms(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## View the build progress of a search terms report

Use the GetProgress() method to view the build progress of a search terms report and related statistics.

The following code sample illustrates how to call the GetProgress() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async System.Threading.Tasks.Task<Relativity.SearchTermsReport.Interfaces.Models.ProgressResponse> GetProgress(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      return await searchTermsReportManager.GetProgress(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## Retry errors in a search terms report

Use the RetryErrors() method to queue a Retry Errors job for the specified search terms report. This method attempts to regenerate the report for search terms that returned error messages.

The following code sample illustrates how to call the RetryErrors() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async System.Threading.Tasks.Task RunAllTerms(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      await searchTermsReportManager.RunAllTerms(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## Cancel a running search terms report job

Use the CancelJob() method to cancel a running search terms report job. The following code sample illustrates how to call the CancelJob() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async Task CancelJob(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      await searchTermsReportManager.CancelJob(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## Retrieve the URL for the Search Terms Result tab

Use the GetResultsUrl() method to retrieve the URL used for navigating to the Search Terms Result tab with the appropriate filter criteria for this search terms report.

The following code sample illustrates how to call the GetResultsUrl() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async Task<string> GetResultsUrl(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      await searchTermsReportManager.GetResultsURL(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## Retrieve the URL for a search terms report

Use the GetReportURL() method to retrieve the URL used for navigating to a search terms report.

The following code sample illustrates how to call the GetReportURL() method by passing the Artifact IDs of a workspace and search terms report.

Copy

```text
1
2
3
4
5
6
7
public async Task<string> GetResultsUrl(Relativity.API.IHelper helper, int workspaceID, int searchTermsReportID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      await searchTermsReportManager.GetReportURL(workspaceID, searchTermsReportID).ConfigureAwait(false);

   }

}
```

## Check whether an index contains a long text field

Use the IndexContainsLongTextField() method check whether a search index contains at least one long text field.

The following code sample illustrates how to call the IndexContainsLongTextField() method by passing the Artifact IDs of a workspace and search index.

Copy

```text
1
2
3
4
5
6
7
public async Task<bool> IndexContainsLongTextField (Relativity.API.IHelper helper, int workspaceID, int indexID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<Relativity.SearchTermsReports.V1.SearchTermsReportManager.ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      return await searchTermsReportManager. IndexContainsLongTextField (workspaceID, indexID).ConfigureAwait(false);

   }

}
```

## Retrieve the report type choice IDs

Use the GetReportTypeIDs() method to retrieve the report type choice IDs for a workspace.

The following code sample illustrates how to call the GetReportTypeIDs() method by passing the Artifact ID of a workspace.

Copy

```text
1
2
3
4
5
6
7
public async Task<Dictionary<string, int>> GetReportTypeIDs (Relativity.API.IHelper helper, int workspaceID)

{

   using (var searchTermsReportManager = helper.GetServicesManager().CreateProxy<ISearchTermsReportManager>(Relativity.API.ExecutionIdentity.CurrentUser))

   {

      return await searchTermsReportManager.GetReportTypeIDs(workspaceID).ConfigureAwait(false);

   }

}
```

This method returns a Dictionary object containing the report type and Artifact ID. See the following example:

Copy

```text
1
2
"Report only": 1035327,

"Report and tag": 1035328
```

On this page

- Search Terms Report Services (.NET)

- Fundamentals for the Search Terms Report Services API

- Methods

- Classes and enumerations

- Create a Search Term Report

- Create terms for a search terms report

- Update terms for a search terms report

- Run all terms in a search terms report

- Run pending terms in a search terms report

- View the build progress of a search terms report

- Retry errors in a search terms report

- Cancel a running search terms report job

- Retrieve the URL for the Search Terms Result tab

- Retrieve the URL for a search terms report

- Check whether an index contains a long text field

- Retrieve the report type choice IDs


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
