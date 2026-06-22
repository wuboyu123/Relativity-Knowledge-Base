---
title: "Processing Document Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Document_Manager.htm
collection: developer
fetched_at: 2026-06-22T06:27:28+00:00
sha256: 4e1368460b10169c49054e00232fa4c3b79f9c544b33ba30ec3f83877f50c5da
---

Processing Document Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Document Manager

This topic describes the IProcessingDocumentManager interface, which is used to access the Processing Document Manager service. The Processing Document Manager service includes methods for working with documents in a publishing set.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Retrieve metadata fields and values for a document

- Method

- GetDocumentMetadataAsync: Gets all of the metadata fields and values for the requested Document.

- Parameters

- <int>workspaceID: ID of workspace that file belongs to.

- <long> fileID: ID of requested file.

- Returns

- ProcessingMetadataResponse object

- <long>ProcessingFileID

- <int> WorkspaceArtifactID

- <string>MetadataJson: A JSON-serialized dictionary of Metadata and DocMetadata. The dictionary has two keys, "Metadata" and "DocMetdata". For each top-level key, the value is a dictionary of the metadata Name: Value

- <List<string>> Errors: A list of all Metadata fields that represents errors

View Sample C# Copy

```text
1
2
3
4
using (IProcessingDocumentManager proxy = _servicesMgr.CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.CurrentUser))

{

    ProcessingMetadataResponse response = await proxy.GetDocumentMetadataAsync(data.WorkspaceId, fileID).ConfigureAwait(false);

}
```

## Retrieve error history for a document

- Method

- GetDocumentErrorHistoryAsync: Gets error history for the requested document.

- Parameters

- <int>workspaceID: ID of workspace that file belongs to.

- <long>fileID: ID of requested file.

- <int>skip: The starting index to retrieve documents errors.

- <int>top: The number of documents errors to retrieve.

- Returns

- ProcessingDocumentErrorHistoryResponse object

- <int>TotalCount

- <List<ProcessingDocumentErrorInfo>> DocumentErrorHistory

- <DateTime>TimeStamp

- <string> Category

- <string>ErrorMessage

- <string>ErrorPhase

- <string>RetryStatus

View Sample C# Copy

```text
1
2
3
4
using (IProcessingDocumentManager proxy = _servicesMgr.CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.CurrentUser))

{

    ProcessingDocumentErrorHistoryResponse response = await proxy.GetDocumentErrorHistoryAsync(data.WorkspaceId, fileID, 0, 10).ConfigureAwait(false);

}
```

## Retry deleting documents

- Method

- RetryDeleteDocumentAsync: Send a request to retry deleting documents.

- Parameters

- <int>workspaceID: ID of workspace that the files belong to.

- documentsRequest: ProcessingDocumentsRequest object

- <List<long>>ProcessingFileIDs: The FileIDs of the requested documents.

- <string>Expression: Expression that needs to be applied on the FileIDs

View Sample C# Copy

```text
1
2
3
4
5
6
7
8
ProcessingDocumentsRequest request = new ProcessingDocumentsRequest

{

    ProcessingFileIDs = new List<long> {1, 2, 3}

};

using (IProcessingDocumentManager proxy = _servicesMgr.CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.CurrentUser))

{

        await proxy.RetryDeleteDocumentAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

## Retry document errors

- Method

- RetryDocumentErrorsAsync: Send a request to retry document errors.

- Parameters

- <int>workspaceID: ID of workspace that the files belong to.

- documentsRequest: ProcessingDocumentsRequest object

- <List<long>>ProcessingFileIDs: The FileIDs of the requested documents.

- <string>Expression: Expression that needs to be applied on the FileIDs

View Sample C# Copy

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

ProcessingDocumentsRequest request = new ProcessingDocumentsRequest

{

    ProcessingFileIDs = new List<long> {1, 2, 3}

};

using (IProcessingDocumentManager proxy = _servicesMgr.CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.CurrentUser))

{

    await proxy.RetryDocumentErrorsAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

## Publish documents

- Method

- PublishDocumentsAsync: Send a request to publish documents.

The toggle that controlled conditional or filtered publishing is no longer supported. The PublishDocumentsAsync endpoint only supports the republishing of existing documents.

- Parameters

- <int>workspaceID: ID of workspace that the files belong to.

- documentsRequest: ProcessingDocumentsRequest object

- <List<long>>ProcessingFileIDs: The FileIDs of the requested documents.

- <string>Expression: Expression that needs to be applied on the FileIDs

View Sample C# Copy

```text
1
2
3
4
5
6
7
8
ProcessingDocumentsRequest request = new ProcessingDocumentsRequest

{

    ProcessingFileIDs = new List<long> {1, 2, 3}

};

using (IProcessingDocumentManager proxy = _servicesMgr.CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.CurrentUser))

{

    await proxy.PublishDocumentsAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

## Retrieve count of publishable documents

- Method

- RetrievePublishableDocumentCountAsync: Retrieve information regarding the publishing request.

- Parameters

- <int>workspaceID: ID of workspace that the files belong to.

- documentsRequest: ProcessingDocumentsRequest object

- <List<long>>ProcessingFileIDs: The FileIDs of the requested documents.

- <string>Expression: Expression that needs to be applied on the FileIDs

- Returns

-

<long>: representing the number of publishable documents

View Sample C# Copy

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

ProcessingDocumentsRequest request = new ProcessingDocumentsRequest

{

    Expression = "{\"Type\":\"CompositeExpression\",\"Expressions\":[{\"Type\":\"ConditionalExpression\",\"Property\":\"IsDeleted\",\"Constraint\":\"Is\",\"Value\":false},{\"Type\":\"ConditionalExpression\",\"Property\":\"ProcessingFileId\",\"Constraint\":\"Is\",\"Value\":5}],\"Operator\":\"And\"}"

};

using (IProcessingDocumentManager proxy = _servicesMgr.CreateProxy<IProcessingDocumentManager>(ExecutionIdentity.CurrentUser))

{

    await proxy.RetrievePublishableDocumentCountAsync(data.WorkspaceId, request).ConfigureAwait(false);

}
```

On this page

- Processing Document Manager

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
