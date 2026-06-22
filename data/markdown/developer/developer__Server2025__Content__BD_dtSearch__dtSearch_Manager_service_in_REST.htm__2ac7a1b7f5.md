---
title: "dtSearch Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_dtSearch/dtSearch_Manager_service_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:23:52+00:00
sha256: b0a2d35894a0e359cc98fd131142e1959706bc038c0b2fadcd767157e5f9ce6f
---

dtSearch Manager (REST)

# dtSearch Manager (REST)

Relativity's dtSearch engine provides advanced search functionality such as proximity, stemming, fuzzy searches, and Boolean operators. For more information, see dtSearch on the Relativity Documentation site.

In order to perform a dtSearch search, you must build and activate a dtSearch index. The dtSearch Index Manager API exposes these operations, and others, letting you programmatically manage dtSearch Indexes. A sample use case for the dtSearch Manager API is creating a custom application to programmatically run through the stages of index build rather than manually performing these tasks through the Relativity UI.

You can also use the dtSearch Manager API services through the .NET interfaces. These interfaces support the same functionality as available through REST. For more information, see dtSearch Manager API .

## URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to create a dtSearch:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1

- {workspaceID} to the Artifact ID of the workspace where the search should be added.

## CRUD operations

The dtSearch Manager API supports create, read, update, and delete operations on dtSearch indexes.

### Create a dtSearch index

To create a new dtSearch, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes
```

View the descriptions of the fields in the request

The request contains the following fields. For more information, about the dtSearch index fields, see dtSearch on the Relativity documentation site.

- dtSearchIndexRequest

- Name - the user-friendly name of the dtSearch index.

- Order - the numerical value designating the position of the index in the search indexes list.

- SearchSearchID - the Artifact ID of the saved search used to create the dtSearch index.

- RecognizeDates - a Boolean value indicating whether to make the index auto-recognize dates, email address, and credit card numbers. see Using dtSearch syntax options on the Relativity documentation site.

- SkipNumericValues - a Boolean value indicating whether to suppress indexing of numeric values in applications that do not require numeric range searching. By default, dtSearch indexes numbers both as text and as numeric values, which is necessary for numeric range searching.

- AccentSensitive - a Boolean value indicating whether to make the index sensitive to accents and other language-specific characters.

- IndexShareCodeArtifactID - the Artifact ID of the index share.

- EmailAddress - a semi-colon delimited list of email addresses to send a notification to once the index completes.

- NoiseWords - the index's noise words list.

- AlphabetText - the index's alphabet file.

- SubIndexSize - the size of the sub-index created by the dtSearch index. The minimum value is 1000.

- FragmentationThreshold - the fragmentation level at which the system automatically compresses a dtSearch sub-index during an incremental build. The value must be be equal to or greater than one.

- Priority - an integer value that defines the priority of the index build operation in the dtSearch index build queue.

- DirtySettings - see sample below.

View a sample JSON request for creating a dtSearch index Copy

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
{

   "dtSearchIndexRequest":{

      "Name":"dtsearchIndex",

      "Order":10,

      "SearchSearchID":1129095,

      "RecognizeDates":false,

      "SkipNumericValues":false,

      "AccentSensitive":false,

      "IndexShareCodeArtifactID":1016154,

      "EmailAddress":"",

      "NoiseWords":"a\r\nabout\r\nafter\r\nall\r\nalso\r\nan\r\nand\r\nanother\r\nany\r\nare\r\nas\r\nat\r\nbe\r\nbecause\r\nbeen\r\nbefore\r\nbeing\r\nbetween\r\nboth\r\nbut\r\nby\r\ncame\r\ncan\r\ncome\r\ncould\r\ndid\r\ndo\r\neach\r\neven\r\nfor\r\nfrom\r\nfurther\r\nfurthermore\r\nget\r\ngot\r\nhad\r\nhas\r\nhave\r\nhe\r\nher\r\nhere\r\nhi\r\nhim\r\nhimself\r\nhis\r\nhow\r\nhowever\r\ni\r\nif\r\nin\r\nindeed\r\ninto\r\nis\r\nit\r\nits\r\njust\r\nlike\r\nmade\r\nmany\r\nme\r\nmight\r\nmore\r\nmoreover\r\nmost\r\nmuch\r\nmust\r\nmy\r\nnever\r\nnot\r\nnow\r\nof\r\non\r\nonly\r\nor\r\nother\r\nour\r\nout\r\nover\r\nsaid\r\nsame\r\nsee\r\nshe\r\nshould\r\nsince\r\nsome\r\nstill\r\nsuch\r\ntake\r\nthan\r\nthat\r\nthe\r\ntheir\r\nthem\r\nthen\r\nthere\r\ntherefore\r\nthese\r\nthey\r\nthis\r\nthose\r\nthrough\r\nthus\r\nto\r\ntoo\r\nunder\r\nup\r\nvery\r\nwas\r\nway\r\nwe\r\nwell\r\nwere\r\nwhat\r\nwhen\r\nwhere\r\nwhich\r\nwhile\r\nwho\r\nwill\r\nwith\r\nwould\r\nyou\r\nyour\r\n",

      "AlphabetText":"dtSearch Alphabet File\n\n[Letters] // Original letter, lower case, upper case, unaccented\n 0 0 0 0\n 1 1 1 1\n 2 2 2 2\n 3 3 3 3\n 4 4 4 4\n 5 5 5 5\n 6 6 6 6\n 7 7 7 7\n 8 8 8 8\n 9 9 9 9\n A a A A\n B b B B\n C c C C\n D d D D\n E e E E\n F f F F\n G g G G\n H h H H\n I i I I\n J j J J\n K k K K\n L l L L\n M m M M\n N n N N\n O o O O\n P p P P\n Q q Q Q\n R r R R\n S s S S\n T t T T\n U u U U\n V v V V\n W w W W\n X x X X\n Y y Y Y\n Z z Z Z\n _ _ _ _\n a a A a\n b b B b\n c c C c\n d d D d\n e e E e\n f f F f\n g g G g\n h h H h\n i i I i\n j j J j\n k k K k\n l l L l\n m m M m\n n n N n\n o o O o\n p p P p\n q q Q q\n r r R r\n s s S s\n t t T t\n u u U u\n v v V v\n w w W w\n x x X x\n y y Y y\n z z Z z\n\n[Hyphens]\n -\n\n[Spaces]\n \\09\\0a\\0c\\0d !@\"#$&'()*+,./:;<=>?[\\5c]^`{|}~\n\n[Ignore]\n \u0001\u0002\u0003\u0004\u0005\u0006\u0007\\08\u000b\u000e\u000f\u0010\u0011\u0012\u0013\u0014\u0015\u0016\u0017\u0018\u0019\u001a\u001b\u001c\u001d\u001e\u001f%\n\n[End]\nCJKRanges = 2e80-ac00 ac00-d7af f900-faff fe30-fe4f \n",

      "SubIndexSize":250000,

      "FragmentationThreshold":9,

      "Priority":1,

      "DirtySettings":"<dtSearchDirtySetting><Upgraded>False</Upgraded><AccentSensitiveChanged>False</AccentSensitiveChanged><AlphabetChanged>False</AlphabetChanged><AutoRecognizeChanged>False</AutoRecognizeChanged><NoiseWordsChanged>False</NoiseWordsChanged></dtSearchDirtySetting>"

   }

}
```

When the request is successful, the response contains the Artifact ID of the new dtSearch index. It also returns the status code of 200.

### Retrieve index metadata

You can retrieve the metadata for a dtSearch index. Send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}
```

View the descriptions of the fields in the response

The response contains the following fields. It also returns the status code of 200.

- ID - an internal ID for the dtSearch index.

- Name - the user-friendly name of the dtSearch index.

- SearchableSearchID - the Artifact ID of the saved search.

- RelativitySearchProviderID - the Artifact ID of the dtSearch index.

- RecognizeDates - a Boolean value indicating whether to make the index auto-recognize dates, email address, and credit card numbers.

- SkipNumericValues - a Boolean value indicating whether to suppress indexing of numeric values in applications that do not require numeric range searching. By default, dtSearch indexes numbers both as text and as numeric values, which is necessary for numeric range searching.

- AccentSensitive - a Boolean value indicating whether to make the index sensitive to accents and other language-specific characters.

- IndexShareCodeArtifactID - the Artifact ID of the index share.

- EmailAddress - a list of email notification recipients.

- NoiseWords - the index's noise words list.

- AlphabetText - the index's alphabet file.

- LastBuildError - the error message if the index failed. This field is empty if the index build is successful.

- Status -

- SubIndexSize - the size of the sub-index created by the dtSearch index.

- DirtySettings - see sample below.

- LastBuildStartTime - a timestamp indicating the time of the last index build began.

- LastBuildEndTime - a timestamp indicating the time the last index build ended.

- LastIndexStartTime -

- DtSearchSourceIndexID - a value used during index builds to identify the original dtSearch index build ID.

- FragmentationThreshold - the fragmentation level at which the system automatically compresses a dtSearch sub-index during an incremental build.

View a sample JSON response Copy

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
{

    "ID": 2,

    "Name": "dtsearch-test",

    "SearchableSearchID": 1038051,

    "RelativitySearchProviderID": 1039620,

    "RecognizeDates": false,

    "SkipNumericValues": false,

    "AccentSensitive": false,

    "IndexShareCodeArtifactID": 1016154,

    "EmailAddress": "",

    "NoiseWords": "a\r\nabout\r\nafter\r\nall\r\nalso\r\nan\r\nand\r\nanother\r\nany\r\nare\r\nas\r\nat\r\nbe\r\nbecause\r\nbeen\r\nbefore\r\nbeing\r\nbetween\r\nboth\r\nbut\r\nby\r\ncame\r\ncan\r\ncome\r\ncould\r\ndid\r\ndo\r\neach\r\neven\r\nfor\r\nfrom\r\nfurther\r\nfurthermore\r\nget\r\ngot\r\nhad\r\nhas\r\nhave\r\nhe\r\nher\r\nhere\r\nhi\r\nhim\r\nhimself\r\nhis\r\nhow\r\nhowever\r\ni\r\nif\r\nin\r\nindeed\r\ninto\r\nis\r\nit\r\nits\r\njust\r\nlike\r\nmade\r\nmany\r\nme\r\nmight\r\nmore\r\nmoreover\r\nmost\r\nmuch\r\nmust\r\nmy\r\nnever\r\nnot\r\nnow\r\nof\r\non\r\nonly\r\nor\r\nother\r\nour\r\nout\r\nover\r\nsaid\r\nsame\r\nsee\r\nshe\r\nshould\r\nsince\r\nsome\r\nstill\r\nsuch\r\ntake\r\nthan\r\nthat\r\nthe\r\ntheir\r\nthem\r\nthen\r\nthere\r\ntherefore\r\nthese\r\nthey\r\nthis\r\nthose\r\nthrough\r\nthus\r\nto\r\ntoo\r\nunder\r\nup\r\nvery\r\nwas\r\nway\r\nwe\r\nwell\r\nwere\r\nwhat\r\nwhen\r\nwhere\r\nwhich\r\nwhile\r\nwho\r\nwill\r\nwith\r\nwould\r\nyou\r\nyour\r\n",

    "AlphabetText":"dtSearch Alphabet File\n\n[Letters] // Original letter, lower case, upper case, unaccented\n 0 0 0 0\n 1 1 1 1\n 2 2 2 2\n 3 3 3 3\n 4 4 4 4\n 5 5 5 5\n 6 6 6 6\n 7 7 7 7\n 8 8 8 8\n 9 9 9 9\n A a A A\n B b B B\n C c C C\n D d D D\n E e E E\n F f F F\n G g G G\n H h H H\n I i I I\n J j J J\n K k K K\n L l L L\n M m M M\n N n N N\n O o O O\n P p P P\n Q q Q Q\n R r R R\n S s S S\n T t T T\n U u U U\n V v V V\n W w W W\n X x X X\n Y y Y Y\n Z z Z Z\n _ _ _ _\n a a A a\n b b B b\n c c C c\n d d D d\n e e E e\n f f F f\n g g G g\n h h H h\n i i I i\n j j J j\n k k K k\n l l L l\n m m M m\n n n N n\n o o O o\n p p P p\n q q Q q\n r r R r\n s s S s\n t t T t\n u u U u\n v v V v\n w w W w\n x x X x\n y y Y y\n z z Z z\n\n[Hyphens]\n -\n\n[Spaces]\n \\09\\0a\\0c\\0d !@\"#$&'()*+,./:;<=>?[\\5c]^`{|}~\n\n[Ignore]\n \\08\u000b%\n\n[End]\nCJKRanges = 0e00-0e4e 3040-30ff 4e00-9fff \n",

    "LastBuildError": "",

    "Status": "No documents indexed",

    "SubIndexSize": 250000,

    "DirtySettings": "",

    "LastBuildStartTime": "2020-07-06T20:30:56.623",

    "LastBuildEndTime": "2020-07-06T20:31:15.847",

    "LastIndexStartTime": "2020-07-06T20:31:07.783",

    "FragmentationThreshold": 9

}
```

### Update a dtSearch index

You can update the settings on a dtSearch index such as its name, order, and other fields. To update a dtSearch index, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}
```

The request contains the following fields:

- Name - the user-friendly name of the dtSearch index.

- Order - the numerical value designating the position of the index in the search indexes list.

- SearchSearchID - the Artifact ID of the saved search used to create the dtSearch index.

- RecognizeDates - a Boolean value indicating whether to make the index auto-recognize dates, email address, and credit card numbers. see Using dtSearch syntax options on the Relativity documentation site.

- SkipNumericValues - a Boolean value indicating whether to suppress indexing of numeric values in applications that do not require numeric range searching. By default, dtSearch indexes numbers both as text and as numeric values, which is necessary for numeric range searching.

- AccentSensitive - a Boolean value indicating whether to make the index sensitive to accents and other language-specific characters.

- IndexShareCodeArtifactID - the Artifact ID of the index share.

- EmailAddress - a semi-colon delimited list of email addresses to send a notification to once the index completes.

- NoiseWords - the index's noise words list.

- AlphabetText - the index's alphabet file.

- SubIndexSize - the size of the sub-index created by the dtSearch index. The minimum value is 1000.

- FragmentationThreshold - the fragmentation level at which the system automatically compresses a dtSearch sub-index during an incremental build. The value must be be equal to or greater than one.

- Priority - an integer value

- DirtySettings -

View a sample JSON request for updating a dtSearch index Copy

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
{

    "ID": 2,

    "Name": "IndexName-2",

    "SearchableSearchID": 1038051,

    "RelativitySearchProviderID": 1039620,

    "RecognizeDates": false,

    "SkipNumericValues": false,

    "AccentSensitive": false,

    "IndexShareCodeArtifactID": 1016154,

    "EmailAddress": "",

    "NoiseWords": "a\r\nabout\r\nafter\r\nall\r\nalso\r\nan\r\nand\r\nanother\r\nany\r\nare\r\nas\r\nat\r\nbe\r\nbecause\r\nbeen\r\nbefore\r\nbeing\r\nbetween\r\nboth\r\nbut\r\nby\r\ncame\r\ncan\r\ncome\r\ncould\r\ndid\r\ndo\r\neach\r\neven\r\nfor\r\nfrom\r\nfurther\r\nfurthermore\r\nget\r\ngot\r\nhad\r\nhas\r\nhave\r\nhe\r\nher\r\nhere\r\nhi\r\nhim\r\nhimself\r\nhis\r\nhow\r\nhowever\r\ni\r\nif\r\nin\r\nindeed\r\ninto\r\nis\r\nit\r\nits\r\njust\r\nlike\r\nmade\r\nmany\r\nme\r\nmight\r\nmore\r\nmoreover\r\nmost\r\nmuch\r\nmust\r\nmy\r\nnever\r\nnot\r\nnow\r\nof\r\non\r\nonly\r\nor\r\nother\r\nour\r\nout\r\nover\r\nsaid\r\nsame\r\nsee\r\nshe\r\nshould\r\nsince\r\nsome\r\nstill\r\nsuch\r\ntake\r\nthan\r\nthat\r\nthe\r\ntheir\r\nthem\r\nthen\r\nthere\r\ntherefore\r\nthese\r\nthey\r\nthis\r\nthose\r\nthrough\r\nthus\r\nto\r\ntoo\r\nunder\r\nup\r\nvery\r\nwas\r\nway\r\nwe\r\nwell\r\nwere\r\nwhat\r\nwhen\r\nwhere\r\nwhich\r\nwhile\r\nwho\r\nwill\r\nwith\r\nwould\r\nyou\r\nyour\r\n",

    "AlphabetText":"dtSearch Alphabet File\n\n[Letters] // Original letter, lower case, upper case, unaccented\n 0 0 0 0\n 1 1 1 1\n 2 2 2 2\n 3 3 3 3\n 4 4 4 4\n 5 5 5 5\n 6 6 6 6\n 7 7 7 7\n 8 8 8 8\n 9 9 9 9\n A a A A\n B b B B\n C c C C\n D d D D\n E e E E\n F f F F\n G g G G\n H h H H\n I i I I\n J j J J\n K k K K\n L l L L\n M m M M\n N n N N\n O o O O\n P p P P\n Q q Q Q\n R r R R\n S s S S\n T t T T\n U u U U\n V v V V\n W w W W\n X x X X\n Y y Y Y\n Z z Z Z\n _ _ _ _\n a a A a\n b b B b\n c c C c\n d d D d\n e e E e\n f f F f\n g g G g\n h h H h\n i i I i\n j j J j\n k k K k\n l l L l\n m m M m\n n n N n\n o o O o\n p p P p\n q q Q q\n r r R r\n s s S s\n t t T t\n u u U u\n v v V v\n w w W w\n x x X x\n y y Y y\n z z Z z\n\n[Hyphens]\n -\n\n[Spaces]\n \\09\\0a\\0c\\0d !@\"#$&'()*+,./:;<=>?[\\5c]^`{|}~\n\n[Ignore]\n \\08\u000b%\n\n[End]\nCJKRanges = 0e00-0e4e 3040-30ff 4e00-9fff \n",

    "LastBuildError": "",

    "Status": "No documents indexed",

    "SubIndexSize": 250000,

    "DirtySettings": "",

    "LastBuildStartTime": "2020-07-06T20:30:56.623",

    "LastBuildEndTime": "2020-07-06T20:31:15.847",

    "LastIndexStartTime": "2020-07-06T20:31:07.783",

    "FragmentationThreshold": 9

}
```

When the request is successful, it returns the status code of 200.

### Delete a dtSearch index

To delete a dtSearch index, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/delete-index
```

When the request is successful, it returns the status code of 200.

## Index build operations

The dtSearch Manager API supports programmatically managing index builds, activation, and other operations performed in Relativity on the dtSearch index console. For more information, see dtSearch on the Relativity Documentation site.

### Build Index: Full

You must run a full build after initially creating a dtSearch index. To run a full build of a dtSearch index, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/full-build-index
```

The body of the request contains the following:

Copy

```text
1
{"isActive":true}
```

When the request is successful, it returns the status code of 200.

### Build Index: Incremental

You can run an incremental build after adding or removing documents from your search. To run an incremental build of a dtSearch index, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/incremental-build-index
```

The body of the request contains the following:

Copy

```text
1
{"isActive":true}
```

When the request is successful, it returns the status code of 200.

### Build Index

You can run the following to first initiate an incremental dtSearch index build operation, if possible, or else run a full dtSearch index build operation. Send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.Compute.DtSearchIndexes/workspace/{workspaceID}/dtSearchIndexes/{RelativitySearchProviderID}/buildIndex
```

The body of the request contains the following:

Copy

```text
1
{"isActive":true}
```

When the request is successful, it returns the status code of 200.

### Cancel a dtSearch index build

To cancel an index build, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/cancel-build
```

When the request is successful, it returns the status code of 200.

### Activate a dtSearch index

To activate a dtSearch index for searching, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/activate-index
```

When the request is successful, it returns the status code of 200.

### Compress a dtSearch index

You can compress a dtSearch index returning all sub-indexes with a fragmentation level greater than zero to a fragmentation level of zero. To compress an index, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/compress-index
```

The body of the request contains the following:

Copy

```text
1
{"isActive":true}
```

When the request is successful, it returns the status code of 200.

### Deactivate index

To deactivate an index, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/deactivate-index
```

When the request is successful, it returns the status code of 200.

### Swap index

You can swap your index with a replacement index in order to use its resources while your index builds or is inactive or disabled for any reason. To swap indexes, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/swap-index
```

The body of the request contains the following:

- oldSearchProviderID - the ArtifactID of the dtSearch index whose resources you want to swap.

- newSearchProviderID - the ArtifactID of the replacement dtSearch index.

Copy

```text
1
2
3
4
{

"oldSearchProviderID":1130118,

"newSearchProviderID":1128030

}
```

When the request is successful, it returns the status code of 200.

### Retry index build errors

To retry errors that occurred during the index build, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/retry-errors
```

When the request is successful, it returns the status code of 200.

### Track index build progress

To get the progress on an index build, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/index-job-progress
```

View the descriptions of the fields in the response

The response contains the following fields:

- IndexName - the user-friendly name of the dtSearch index.

- JobType - the type of index build operation (full build, incremental, compress).

- JobStatus - the current state of the job (indexing, populating, finalizing, error).

- JobStage - the current stage of the job (initializing, creating population table, indexing, complete).

- IsStageInError - a Boolean value indicating whether the stage is in an error state.

- TotalIndexed - the total number of documents indexed.

- TotalErrored - the total number of documents errored.

- ProgressPercentage - the percentage of the job completed.

- JobdurationString - a timestamp indicating the total time spent on the job.

- IndexBuildDurationString - a timestamp indicating the time spent by the index workers indexing the saved search.

- CanActivate - a Boolean value indicating whether the index is ready to be activated.

View a sample JSON response Copy

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
{

    "IndexName": "IndexName-2",

    "JobType": "No Active Job",

    "JobStatus": "No documents indexed",

    "JobStage": -999,

    "IsStageInError": false,

    "TotalIndexed": 0,

    "TotalErrored": 0,

    "ProgressPercentage": 0.0,

    "JobDurationString": "01:33:30",

    "IndexBuildDurationString": "01:33:19",

    "ErrorMessage": "",

    "CanActivate": false

}
```

## Helper methods

The dtSearch Manager API provides the following helper methods for returning workspace parameters for populating dtSearch saved search properties.

### Get active indexes

To get a list of active indexes for a given workspace, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/index-shares
```

View a sample JSON response Copy

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
[

 {

   "Name":"\\\\fileshareuncpath\\directoryname\\dtSearchPath\\",

   "ID":1016154

 }

 {

   "Name":"\\\\fileshareuncpath2\\directoryname2\\dtSearchPath2\\",

   "ID":1016155

 }

]
```

### Get saved searches

To get a list of saved searches for a given workspace, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/saved-search
```

The response contains the following fields:

- Name - the name of the saved search.

- ID - the Artifact ID of the saved search.

View a sample JSON response Copy

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
[

{

    "Name":"All Documents",

    "ID":1038052

},

{

    "Name":"Extracted Text Only",

    "ID":1038051

},

{

    "Name":"Produced Documents",

    "ID":1036361

}

]
```

### Get index share locations

To get a list of index share locations for a given workspace, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/Relativity.Compute.DtSearchIndexes/workspace/{workspaceID}/dtSearchIndexes/indexshares
```

View a sample JSON response Copy

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
[

 {

   "Name":"\\\\fileshareuncpath\\directoryname\\dtSearchPath\\",

   "ID":1016154

 }

 {

   "Name":"\\\\fileshareuncpath2\\directoryname2\\dtSearchPath2\\",

   "ID":1016155

 }

]
```

### Get index statistics

To get statistical data for a given index, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/index-statistics
```

View the descriptions of the fields in the response

The response contains the following fields:

- DocumentCount - the total number of documents in the index.

- IndexSize - the size of the index in bytes.

- LastBuiltOn - a timestamp indicating when the index was last built.

- LastModifiedOn - a timestamp indicating when the index was last modified.

- BuildTime - how long the last build took to complete in hours, minutes, and seconds.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
{

   "DocumentCount":300,

   "IndexSize":29952863,

   "LastBuiltOn":"2019-06-13T16:38:02",

   "LastModifiedOn":"2019-06-13T16:38:02",

   "BuildTime":"00:00:16"

}
```

### Get document-level errors

To get a list of document-level errors that occurred during the index build, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-dtsearch/{versionNumber}/workspaces/{workspaceID}/dtsearch-indexes/{RelativitySearchProviderID}/document-errors
```

View a sample JSON response Copy

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
[

    {

        "ArtifactID": 1054057,

        "ErrorMessage": "Error during read -> Invalid URI: The format of the URI could not be determined."

    },

    {

        "ArtifactID" : 1054058,

        "ErrorMessage: "Error during read -> Unable to locate file"

    }

]
```
