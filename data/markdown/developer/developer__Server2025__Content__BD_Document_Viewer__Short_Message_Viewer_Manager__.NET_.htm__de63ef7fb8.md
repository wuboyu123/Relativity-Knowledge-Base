---
title: "Short Message Viewer Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Short_Message_Viewer_Manager__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:22:24+00:00
sha256: ec1a8c74fe4a7f6b827b8778b8dcbb188773d949ddb248861ff8e2f98d33cdf2
---

Short Message Viewer Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Short Message Viewer Manager (.NET)

In Relativity, the Short Message Viewer displays messages sent through SMS such as iMessage and instant messenger services such as Skype Messenger, Slack, and others. For more information, see Short Message Viewer on the Relativity Documentation site.

The Short Message Viewer Manager API exposes methods for retrieving the JSON, attachments, and participant information for short messages. It also provides methods for validating the Relativity Short Message Format (RSMF) and creating new documents based on a subset of messages.

You can also use the Short Message Viewer Manager API through REST. For more information, see Short Message Viewer Manager (REST) .

## Fundamentals for the Short Message Viewer Manager API

Review the following information to learn about the methods and classes used by the Short Message Viewer Manager API.

### Methods

The Short Message Viewer Manager API includes the following methods available on the IShortMessageViewerManager interface in the Relativity.DocumentViewer.Services.<VersionNumber> namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- GetAttachmentInfo() method - retrieves information about the attachments contained in a short message document. See Retrieve attachment information for a short message .

- GetMessageJson() method - retrieves the JSON representation for a short message document. See Retrieve the JSON for a short message .

- GetParticipantInfo() method - retrieves entity information for the requested participants in a short message document. See Retrieve entity information for a participant in a short message document .

- SliceRSMF() method - creates a new document based on a subset of events in a short message document. See Use slicing to create a new document with short message events .

- ValidateRSMF() method - verifies whether a specific file or document has a valid RSMF. It returns information explaining why a document or file is invalid. See Validate the RSMF for a file or document .

### Classes

The Short Message Viewer Manager API uses the following key classes:

- AttachmentInfo - represents an attachment on a short message conversation and is returned by the GetAttachmentInfo method(). It contains the following properties:

- AttachmentID - the ID field for the attachment in the RSMF manifest file. For more information, see rsmf_manifest.json file on the Relativity Documentation site.

- DocumentArtifactID - the ArtifactID of the attachment document.

- FileGuid - the GUID for the attachment file.

- ParticipantRequestInfo - represents a request for entity information and is passed to the GetParticipantInfo() method. It contains the following properties:

- ParticipantID - the ID field for the participant in the RSMF manifest file. For more information, see rsmf_manifest.json file on the Relativity Documentation site.

- Name - the display field for the participant in the RSMF manifest file.

- Email - the email field for the participant in the RSMF manifest file.

- ParticipantResponseInfo - represents the entities of the requested participants and is returned by the GetParticipantInfo() method. It contains the following properties:

- ParticipantID - the ID field for the participant in the RSMF manifest file. For more information, see rsmf_manifest.json file on the Relativity Documentation site.

- EntityName - the name of the corresponding entity object for the participant.

- Aliases - a list of alias names associated with the entity object for the participant.

- Url - a URL that links to the entity object corresponding to the participant.

- RSMFValidationResponse - provides information about validity of RSMF for a file or document and is returned by the overloaded ValidateRSMF() method. It contains the following properties:

- Status - indicates whether the RSMF is valid. Its value may be Passed, Failed, or PassedWithWarnings.

- Errors - a list of validation errors for the RSMF. Each object contains these properties: LineNumber, LinePosition, Message, and list of Submessages.

- Warnings - a list of validation warnings for the RSMF. Each object contains these properties: LineNumber, LinePosition, Message, and list of Submessages.

- SliceRequest - contains request information about the creation of a new document based on a subset of events and is passed to the SliceRSMF() method. It contains the following properties:

- EventIndexes - a list of events to slice or extract from the original RSMF. This list corresponds to the indexes in the events array of the manifest file. For more information, see rsmf_manifest.json file on the Relativity Documentation site.

- SliceRequestOptions - a set of options that define the behavior of the slice operation:

- CreateAttachments - indicates whether to create and import new documents for the attachments in the new file. The default value is false.

- SourceLayoutID - an optional Artifact ID for the document layout containing fields that are copied from the parent document to the new document.

- PreserveAllParticipants - indicates whether to include all participants from the original RSMF in the new RSMF. The default value is true. If this option is false, only active participants are included in the new RSMF.

- EmailConfirmation - indicates whether an email is sent to initiating user on completion of the slice. The default value is true, indicating an email should be sent.

## Retrieve the JSON for a short message

Use the GetMessageJson() method to retrieve a JSON manifest representation of a short message document.

Pass the following arguments to this method:

- workspaceID - the Artifact ID of a workspace containing a short message document.

- documentID - the Artifact ID of a short message document.

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
public Task<IKeplerStream> GetMessageJson(int workspaceID, int documentID)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IShortMessageViewerManager shortMessageViewerManager = serviceFactory.CreateProxy<IShortMessageViewerManager >())

    {

        return shortMessageViewerManager.GetMessageJson(workspaceId, documentId);

    }

}
```

## Retrieve attachment information for a short message

Use the GetAttachmentInfo() method to retrieve information about the attachments contained in a short message document.

Pass the following arguments to this method:

- workspaceID - the Artifact ID of a workspace containing a short message document.

- documentID - the Artifact ID of a short message document.

- attachmentIDs - a string array containing the IDs for attachments.

This method returns a AttachmentInfo object.

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
public async Task<List<AttachmentInfo>> GetAttachmentInfo(int workspaceID, int documentID, string[] attachmentIDs)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IShortMessageViewerManager shortMessageViewerManager = serviceFactory.CreateProxy<IShortMessageViewerManager >())

    {

        return await shortMessageViewerManager.GetAttachmentInfo(workspaceId, documentId, attachmentIDs);

    }

}
```

## Retrieve entity information for a participant in a short message document

Use the GetParticipantInfo() method to retrieve entity information for a participant in a short message document. An Entity object links people, companies, organizational groups, and their metadata. For more information, see Entity object on the Relativity Documentation site.

Pass the following arguments to this method:

- workspaceID - the Artifact ID of a workspace containing a short message document.

- participantRequests - an array of ParticipantRequestInfo objects. A ParticipantRequest object contains the name, email address and ID of a participant in Short Message Viewer conversation.

This method returns a ParticipantResponseInfo object, which contains the name of the Entity object associated with the participant, any aliases for this object, and other information.

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
public async Task<List<ParticipantResponseInfo>> GetParticipantInfo(int workspaceID, ParticipantRequestInfo[] participants)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IShortMessageViewerManager shortMessageViewerManager = serviceFactory.CreateProxy<IShortMessageViewerManager >())

    {

        return await shortMessageViewerManager.GetParticipantInfo(workspaceId, documentId, participants);

    }

}
```

## Validate the RSMF for a file or document

Use the overloaded ValidateRSMF() method to verify whether a specific file or document has a valid RSMF. For more information, see Relativity Short Message Format on the Relativity Documentation site.

### Validate the RSMF for a file

To validate the RSMF for a file, pass the following arguments to the ValidateRSMF() method:

- fileName - a string representing the file name of a specific short message document for validation.

- file - a IKeplerStream object representing the file being validated.

This method returns a RSMFValidationResponse object.

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
public async Task<RSMFValidationResponse> ValidateRSMF(string fileName, IKeplerStream file)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IShortMessageViewerManager shortMessageViewerManager = serviceFactory.CreateProxy<IShortMessageViewerManager >())

    {

        return await shortMessageViewerManager.ValidateRSMF(fileName, file);

    }

}
```

### Validate the RSMF for a document

To validate the RSMF for a document, pass the following arguments to the ValidateRSMF() method:

- workspaceID - the Artifact ID of a workspace containing a short message document.

- documentID - the Artifact ID of a short message document.

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
public async Task<RSMFValidationResponse> ValidateRSMF(int workspaceID, int documentID)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IShortMessageViewerManager shortMessageViewerManager = serviceFactory.CreateProxy<IShortMessageViewerManager >())

    {

        return await shortMessageViewerManager.ValidateRSMF(workspaceID, documentID);

    }

}
```

## Use slicing to create a new document with short message events

Use the SliceRSMF() method to create a new document based on a subset of events in a short message document.

Pass the following arguments to this method:

- workspaceID - the Artifact ID of a workspace containing a short message document.

- documentID - the Artifact ID of a short message document.

- sliceRequest - contains details about the messages to include in the new short message document.

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
public Task SliceRSMF(int workspaceID, int documentID, SliceRequest sliceRequest)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IShortMessageViewerManager shortMessageViewerManager = serviceFactory.CreateProxy<IShortMessageViewerManager >())

    {

        return await shortMessageViewerManager.SliceRSMF(workspaceID, documentID, sliceRequest);

    }

}
```

On this page

- Short Message Viewer Manager (.NET)

- Fundamentals for the Short Message Viewer Manager API

- Methods

- Classes

- Retrieve the JSON for a short message

- Retrieve attachment information for a short message

- Retrieve entity information for a participant in a short message document

- Validate the RSMF for a file or document

- Validate the RSMF for a file

- Validate the RSMF for a document

- Use slicing to create a new document with short message events


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
