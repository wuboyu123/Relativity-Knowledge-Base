---
title: "Persistent Highlight Service (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Persistent_Highlight_Service__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:27:20+00:00
sha256: 6f0a2001b2d172ab0e69f03a368622efa74f170ffe1029b6c7d19d45826cec6e
---

Persistent Highlight Service (REST)

# Persistent Highlight Service (REST)

In Relativity, you use persistent highlight sets to configure and apply term highlighting as part of the document review process in the viewer. You can identity terms in a document to highlight and then configure the color used to highlight them. You can also apply multiple highlights set to a single document. For more information, see Persistent highlight sets .

The Persistent Highlight Service provides the following functionality for programmatically working with these sets:

- Retrieve information about the persistent highlight sets and terms used in a specific document or workspace.

- Set terms or highlight sets as active or inactive.

- Add new terms to a persistent highlight set

As a sample use case, you might create a custom viewer that displays and reads persistent highlight sets and terms.

You can also use the Persistent Highlight Service through .NET. For more information, see Persistent Highlight Service (.NET) .

## Guidelines for using the Persistent Highlight Service

Review the following guidelines for working with the Persistent Highlight Service.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set {versionNumber} to the version of the API, using the format lowercase v and the version number , such as v2 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, such as {workspaceID} to the Artifact ID of a workspace.

For example, you can use the following URL to retrieve persistent highlight sets for a specific workspace:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/highlight-sets
```

Set the path parameter as follows:

- {versionNumber} to the version of the service, such as v2 .

- {workspaceID} to the Artifact ID of the workspace containing the persistent highlight sets to retrieve.

## Retrieve persistent highlight sets

To retrieve persistent highlight sets, send a GET request to one of the following URLs:

- Retrieve persistent highlight sets and terms in a specific workspace:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/highlight-sets
```

- Retrieve persistent highlight sets and terms for a specific document:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/documents/{documentID}/highlight-sets
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- ID - a unique identifier for the persistent highlight set or terms.

- SetName - name of the persistent highlight set.

- Expanded - set this field to true if you want the highlight set expanded on loading in the viewer or set this field to false if you want it minimized on loading in the viewer.

- Selected - set this field to true if you want the highlight set enabled on loading in the viewer or set this field to false if you want it disabled on loading the viewer.

- PersistentHighlightSetID - the Artifact ID of the persistent highlight set.

- PersistentHighlightTerms - the Artifact ID of the persistent highlight term.

- ID - a unique identifier for the term.

- Term - the term that is being highlighted.

- Syntax - displays either phsTerms or dtSearch depending on which syntax option is used in a persistent highlight set or term.

- phsTerms - In the viewer, searches for an exact match of the entered term, taking word-boundaries into account. Word boundaries include white space and special characters and help reduce false positives by excluding hits that are a subset of a full word. In long text mode, searches for an exact match of the entered term. It doesn't take word boundaries into account.

- dtSearch - In the viewer, searches for an exact match of the entered term, taking word-boundaries and dtSearch syntax operators into account. dtSearch isn't supported in long text mode.

- BackgroundColor - the hex value of the color of the background of the highlight.

- ForegroundColor - the hex value of the color of the foreground of the highlight.

- PersistentHighlightTermID - the Artifact ID of the persistent highlight term.

- PersistentHighlightSetID - the Artifact ID of the persistent highlight set.

- Selected -Set this field to true if you want the term highlighted on loading the viewer or set this field to false displays if you don't want the term highlighted on loading the viewer.

View a sample JSON response for read exportable View Fields in a workspace Copy

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
[

   {

      "Id":"PHS_TERM_SEARCH_HIGHLIGHTS_0",

      "SetName":"Primary",

      "Expanded":true,

      "Selected":false,

      "PersistentHighlightSetId":1036494,

      "PersistentHighlightTerms":[

         {

            "Id":"PHS_TERM_1036494_0",

            "Term":"the",

            "Syntax":"phsTerms",

            "BackgroundColor":"#ff0000",

            "ForegroundColor":"#ffffff",

            "PersistentHighlightTermId":0,

            "PersistentHighlightSetId":1036494,

            "Selected":false

         }

      ],

      "Order":0

   },

   {

      "Id":"PHS_TERM_SEARCH_HIGHLIGHTS_1",

      "SetName":"Secondary",

      "Expanded":true,

      "Selected":true,

      "PersistentHighlightSetId":1038535,

      "PersistentHighlightTerms":[

         {

            "Id":"PHS_TERM_1038535_0",

            "Term":"the",

            "Syntax":"phsTerms",

            "BackgroundColor":"#ff33ff",

            "ForegroundColor":"#000000",

            "PersistentHighlightTermId":0,

            "PersistentHighlightSetId":1038535,

            "Selected":true

         },

         {

            "Id":"PHS_TERM_1038535_1",

            "Term":"anD",

            "Syntax":"phsTerms",

            "BackgroundColor":"#ff33ff",

            "ForegroundColor":"#000000",

            "PersistentHighlightTermId":1,

            "PersistentHighlightSetId":1038535,

            "Selected":true

         }

      ],

      "Order":20

   },

   {

      "Id":"PHS_TERM_SEARCH_HIGHLIGHTS_2",

      "SetName":"Lorem",

      "Expanded":true,

      "Selected":true,

      "PersistentHighlightSetId":1038601,

      "PersistentHighlightTerms":[

         {

            "Id":"PHS_TERM_1038601_0",

            "Term":"Lorem",

            "Syntax":"phsTerms",

            "BackgroundColor":"#336600",

            "ForegroundColor":"#ffffff",

            "PersistentHighlightTermId":0,

            "PersistentHighlightSetId":1038601,

            "Selected":true

         },

         {

            "Id":"PHS_TERM_1038601_1",

            "Term":"ipsum",

            "Syntax":"phsTerms",

            "BackgroundColor":"#336600",

            "ForegroundColor":"#ffffff",

            "PersistentHighlightTermId":1,

            "PersistentHighlightSetId":1038601,

            "Selected":true

         }

      ],

      "Order":30

   }

]
```

## Change the state of a persistent highlight set

To change the state of a persistent highlight set or make the terms or set inactive, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/highlights/{persistentHighlightSetID}/state
```

View field descriptions for a response

The response contains the following fields:

- WorkspaceID - the Artifact ID of the workspace that contains the persistent highlight set.

- PersistentHighlightSetID - the Artifact ID of the persistent highlight set or terms.

- TermIDs - the terms that are affected by the action.

- Action - the state of the terms included in TermIDs.

View a sample JSON response for read exportable View Fields in a workspace Copy

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
For Terms

{

 "workspaceId": 1051820,

 "persistentHighlightSetId": 1036494,

 "termIds": [1,2,3,4,5,6,7],

 "action": "Disabled"

}

For Sets

{

 "workspaceId": 1051820,

 "persistentHighlightSetId": 1036494,

 "termIds": [],

 "action": "Disabled"

}
```

## Add new terms to a persistent highlight set

To add new terms to a persistent highlight set, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/highlights/{persistentHighlightSetID}/add-terms
```

View field descriptions for a request

The request contains the following fields:

- workspaceID - the Artifact ID of the workspace that contains the persistent highlight set.

- persistentHighlightSetID - the Artifact ID of the persistent highlight set.

- terms - the Terms added to the persistent highlight set as follows:

- Term - the term that is being highlighted.

- BackgroundColor - the hex value of the color of the background for the highlight.

- ForegroundColor - the hex value of the color of the foreground for the highlight.

View a sample JSON request Copy

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
{

   "workspaceID": 1051820,

   "persistentHighlightSetID": 1036494,

   "terms": [

      {

         "Term": "lorem",

         "BackgroundColor": "#336600",

         "ForegroundColor": "#ffffff"

      },

      {

         "Term": "ipsum",

         "BackgroundColor": "#0390fc",

         "ForegroundColor": "#f2f4f5"

      }

   ]

}
```

View a sample JSON response

When the terms are successfully added, the number of terms now present in the persistent highlight set is returned. If the operation failed without throwing an exception, then -1 is returned.

Copy

```text
1
2
3
{

   "d": 10

}
```
