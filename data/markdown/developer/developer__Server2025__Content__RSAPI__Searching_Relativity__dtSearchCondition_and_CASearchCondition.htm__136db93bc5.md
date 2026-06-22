---
title: "dtSearchCondition and CASearchCondition"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Searching_Relativity/dtSearchCondition_and_CASearchCondition.htm
collection: developer
fetched_at: 2026-06-22T06:33:26+00:00
sha256: 0bad112e037fbe95b8e62088ac0ebb72928487f2d9e84b82a2e1994f8939a77c
---

dtSearchCondition and CASearchCondition Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# dtSearchCondition and CASearchCondition

The Services API includes functionality for retrieving a list of available search indexes, as well as for querying these indexes. The dtSearchCondition and CASearchCondition classes support key searching options available for dtSearch and Analytics indexes respectively.

## Query for a search index

To retrieve a dtSearch or Analytics index, you need to create a query that uses SearchIndex as the ArtifactType. This code sample illustrates how to create this query, which also uses the index type and name as conditions. The following code samples for the dtSearchCondition and CASearchCondition classes also call this method.

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

/// </summary>

/// <param name="proxy">RSAPIClient</param>

/// <param name="indexType">"dtSearch" or "Analytics"</param>

/// <param name="indexName">The name of the SearchIndex.</param>

/// <returns>Artifact of the SearchIndex.</returns>



private static Artifact FindSearchIndex(IRSAPIClient proxy, string indexType, string indexName)

{

     Artifact artifact = null;



     Query query = new Query();

     query.ArtifactTypeID = (int)ArtifactType.SearchIndex;



     query.Condition = new CompositeCondition(

          new TextCondition("Type", TextConditionEnum.EqualTo, indexType), CompositeConditionEnum.And,

          new TextCondition("Name", TextConditionEnum.EqualTo, indexName));



     try

     {

          QueryResult result = proxy.Query(proxy.APIOptions, query);



          if (result.Success)

          {

               artifact = result.QueryArtifacts.FirstOrDefault();

          }

     }

     catch (Exception err)

     {

          Console.WriteLine(err.Message);

     }

     return artifact;

}
```

## Query for a dtSearch index and execute searches

You can query against a dtSearch index using common syntax options including proximity searches, stemming, and fuzziness. For more information about syntax options, see dtSearch on the Relativity Server 2025 Documentation site.

This code sample illustrates how to use the FindSearchIndex() to retrieve a reference to a dtSearch index. It then calls the dtSearch()method, which takes several parameters that include those for defining the search criteria.

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

public static bool Query_And_Execute_dtSearch(IRSAPIClient proxy)

{

     // STEP 1: Find the artifactID of the SearchIndex to that you want to search.

     // This example shows how to query for the dtSearchIndex "My dtSearch" defined in Relativity.

     Artifact searchArtifact = FindSearchIndex(proxy, "dtSearch", "My dtSearch");



     // STEP 2: Execute the search.

     if (searchArtifact != null)

     {

          // Search for "money" within 5 words of "enron."

          dtSearch(proxy, searchArtifact.ArtifactID, "money w/5 enron", false, false, String.Empty);



          // Search for "money" within 5 words of "enron" and sort by rank.

          dtSearch(proxy, searchArtifact.ArtifactID, "money w/5 enron", true, false, String.Empty);



          // Search for "house" and enable stemming.

          dtSearch(proxy, searchArtifact.ArtifactID, "house", false, true, String.Empty);



          // Search for "house" and set fuzzieness level to 3.

          dtSearch(proxy, searchArtifact.ArtifactID, "house", false, false, "3");

     }

     return true;

}
```

The dtSearch() method illustrates how to set the properties available on a dtSearchCondition object.

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

/// <summary>

/// Example showing how to perform a dtSearch.

/// </summary>

/// <param name="proxy">IRSAPIClient</param>

/// <param name="searchIndexArtifactID">An integer which uniquely identifies a dtSearch index.</param>

/// <param name="searchTerms">The SearchTerms of the dtSearch.</param>

/// <param name="sortByRank">Enable SortByRank of the dtSearch.</param>

/// <param name="enableStemming">EnableStemming of the dtSearch.</param>

/// <param name="fuzzinessLevel">The FuzzinessLevel of the dtSearch. Valid values are 0-10 or String.Empty.</param>



public static void dtSearch(IRSAPIClient proxy, int searchIndexArtifactID, string searchTerms, bool sortByRank, bool enableStemming, string fuzzinessLevel)

{

     Query query = new Query();

     query.ArtifactTypeID = (int)ArtifactType.Document;



     dtSearchCondition searchCondition = new dtSearchCondition(searchIndexArtifactID, searchTerms);

     searchCondition.SortByRank = sortByRank;

     searchCondition.EnableStemming = enableStemming;

     searchCondition.FuzzinessLevel = fuzzinessLevel;

     query.Condition = searchCondition;



     try

     {

          QueryResult result = proxy.Query(proxy.APIOptions, query);



          if (result.Success)

          {

               foreach (Artifact artifact in result.QueryArtifacts)

               {

                    Console.WriteLine(String.Format("Artifact ID:{0}", artifact.ArtifactID));

               }

          }

          else

          {

               Console.WriteLine(result.Message);

          }

     }

     catch (Exception ex)

     {

          Console.WriteLine(ex.Message);

     }

}
```

## Query for an Analytics index and execute searches

Using the CASearchCondition class, you can query against an Analytics index by performing concept searching. You set the following properties on this class for concept searches:

- SearchTerms – list of words or phrases

- Concepts – block text

- SortByRank – orders result set by relevance

- MinimumConceptRank – ranking for a minimum level of conceptual correlation

You can also set the IsSimilarDocQuery property to perform similar document detection, which identifies groups of highly related documents. For more information, see Analytics on the Relativity Server 2025 Documentation site.

This code sample illustrates how to use the FindSearchIndex() to retrieve a reference to an Analytics index. It then calls the CASearch() method, which takes several parameters that include those for defining the search criteria.

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

public static bool Query_And_Execute_CASearch(IRSAPIClient proxy)

{

     // STEP 1: Find the artifactID of the SearchIndex to search.

     // In the case below the CASearchIndex "My CA Search" would have already been defined in Relativity.

     Artifact searchArtifact = FindSearchIndex(proxy, "Analytics", "My CA Search");



     // STEP 2: Execute the search:

     if (searchArtifact != null)

     {



          // Search for "money" within 5 words of "enron."

          CASearch(proxy, searchArtifact.ArtifactID, "money w/5 enron", String.Empty, false, String.Empty, String.Empty, false, 0);



          // Search for "money" within 5 words of "enron" and sort by rank.

          CASearch(proxy, searchArtifact.ArtifactID, "money w/5 enron", String.Empty, true, String.Empty, String.Empty, false, 0);



          // Search for "house" and set fuzzieness level to 3.

          CASearch(proxy, searchArtifact.ArtifactID, "house", String.Empty, false, "3", String.Empty, false, 0);



          // Search for documents that are like documents with ArtifactID 1037198.

          CASearch(proxy, searchArtifact.ArtifactID, "", String.Empty, false, String.Empty, String.Empty, true, 1037198);



          // Search for concept of "Just thought I'd say hello" and a minimum concept rank of 60%.

          CASearch(proxy, searchArtifact.ArtifactID, String.Empty, "Just thought I'd say hello", false, String.Empty, ".6", false, 0);

     }

     return true;

}
```

The CASearch() method provides illustrates how to set the properties available on a CASearchCondition object.

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

/// <summary>

/// Example showing how to perform a CASearch.

/// </summary>

/// <param name="proxy">IRSAPIClient</param>

/// <param name="searchIndexArtifactID">An integer which uniquely identifies a CASearch index.</param>

/// <param name="searchTerms">The SearchTerms of the CASearch.</param>

/// <param name="concepts">The Concepts of the CASearch.</param>

/// <param name="sortByRank">Enable SortByRank of the CASearch.</param>

/// <param name="fuzzinessLevel">The FuzzinessLevel of the CASearch. Valid values are 0-10 or String.Empty.</param>

/// <param name="minimumConceptRank">The MinimumConceptRank of the CASearch. Valid values are decimal values 0-1.</param>

/// <param name="isSimilarDocQuery">Enable IsSimilarDocQuery of the CASearch.</param>

/// <param name="documentArtifactID">The DocumentArtifactID of a document to be used when IsSimilarDocQuery is true.</param>



public static void CASearch(IRSAPIClient proxy, int searchIndexArtifactID, string searchTerms, string concepts, bool sortByRank, string fuzzinessLevel, string minimumConceptRank, bool isSimilarDocQuery, int documentArtifactID)

{

     Query query = new Query();

     query.ArtifactTypeID = (int)ArtifactType.Document;



     CASearchCondition searchCondition = new CASearchCondition(searchIndexArtifactID, searchTerms);

     searchCondition.Concepts = concepts;

     searchCondition.SortByRank = sortByRank;

     searchCondition.IsSimilarDocQuery = isSimilarDocQuery;

     searchCondition.DocumentArtifactID = documentArtifactID;

     searchCondition.FuzzinessLevel = fuzzinessLevel;

     searchCondition.MinimumConceptRank = minimumConceptRank;

     query.Condition = searchCondition;



     try

     {

          QueryResult result = proxy.Query(proxy.APIOptions, query);



          if (result.Success)

          {

               foreach (Artifact artifact in result.QueryArtifacts)

               {

                    Console.WriteLine(String.Format("Artifact ID:{0}", artifact.ArtifactID));

               }

          }

          else

          {

               Console.WriteLine(result.Message);

          }

     }

     catch (Exception ex)

     {

          Console.WriteLine(ex.Message);

     }

}
```

On this page

- dtSearchCondition and CASearchCondition

- Query for a search index

- Query for a dtSearch index and execute searches

- Query for an Analytics index and execute searches


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
