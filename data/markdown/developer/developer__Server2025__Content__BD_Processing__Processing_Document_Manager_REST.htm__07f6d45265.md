---
title: "Processing Document Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Document_Manager_REST.htm
collection: developer
fetched_at: 2026-06-22T06:27:29+00:00
sha256: e4631a188a10dd723ba37d412f7e711f929d5015240c0747f4e31cbc4c4263ac
---

Processing Document Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Document Manager (REST)

This topic describes the documents endpoint, which is used to access the Processing Document Manager service. The Processing Document Manager service includes methods for working with documents in a publishing set.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

See the section on Filter expressions for more details on building an Expression value, which may be used in the Request Body for certain endpoints.

## Retrieve metadata fields and values for a document

To retrieve metadata fields and values for a document, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/documents/{your file ID}/metadata
```

## Retrieve error history for a document

To retrieve the error history for a document, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/documents/{your file ID}/errors?skip={skip}&top={top}
```

## Retry deleting documents

To retry deleting documents, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/documents/retry
```

Request Body Example

Copy

```text
1
2
3
4
5
6
7
{

    "documentsRequest":

    {

        "ProcessingFileIDs":[1,2,3],

        “Expression”:{expression to apply on file IDs}

    }

}
```

## Retry document errors

The Retry Document Errors ( retry-errors ) endpoint is not currently supported. Support for this endpoint will be added in a future release of Relativity Server

To retry document errors, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/documents/retry-errors
```

Request Body Example

Copy

```text
1
2
3
4
5
6
7
{

    "documentsRequest":

    {

        "ProcessingFileIDs":[1,2,3],

        “Expression”:{expression to apply on file IDs}

    }

}
```

## Publish documents

To publish documents, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/documents/publish
```

Request Body Example

Copy

```text
1
2
3
4
5
6
7
{

    "documentsRequest":

    {

        "ProcessingFileIDs":[1,2,3],

        “Expression”:{expression to apply on file IDs}

    }

}
```

In Relativity Server environments, the PublishDocumentsAsync endpoint no longer supports the toggle or conditional publish functionality. The Expression field in the request body is not supported and will be ignored if provided.

## Retrieve count of publishable documents

To retrieve a count of publishable documents, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/documents/count
```

Request Body Example

Copy

```text
1
2
3
4
5
6
7
{

    "documentsRequest":

    {

        "ProcessingFileIDs":[1,2,3],

        “Expression”:{expression to apply on file IDs}

    }

}
```

On this page

- Processing Document Manager (REST)

- Retrieve metadata fields and values for a document

- Retrieve error history for a document

- Retry deleting documents

- Retry document errors

- Publish documents

- Retrieve count of publishable documents


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
