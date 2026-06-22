---
title: "Short Message Viewer Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Short_Message_Viewer_Manager__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:22:38+00:00
sha256: 509a9aef4ed693598ea57f725546369fd5fa3b3ab282056cf3c2e18df756027b
---

Short Message Viewer Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Short Message Viewer Manager (REST)

In Relativity, the Short Message Viewer displays messages sent through SMS such as iMessage and instant messenger services such as Skype Messenger, Slack, and others. For more information, see Short Message Viewer on the Relativity Documentation site.

The Short Message Viewer API exposes endpoints for retrieving the JSON, attachments, and participant information for short messages. It also provides endpoints for validating the Relativity Short Message Format (RSMF).

You can also use the Short Message Viewer Manager service through .NET. For more information, see Short Message Viewer Manager (.NET) .

## Guidelines for using the Short Message Viewer Manager service

Review the following guidelines for working with the Short Message Viewer service.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set {versionNumber} to the version of the API, using the format lowercase v and the version number , such as v2 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, such as {workspaceID} to the Artifact ID of a workspace.

For example, you can use the following URL to retrieve the JSON representation for a short message document:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspace/{workspaceID}/short-message/{documentID}/message-json
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v2 .

- {workspaceID} to the Artifact ID of the workspace containing the short message conversation.

- {documentID} to the Artifact ID of the short message document.

## Retrieve the JSON for a short message

To retrieve the JSON representation for a short message document, send a GET request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspace/{workspaceID}/short-message/{documentID}/message-json
```

The fields in the JSON response correspond to those in the rsmf_manifest.json file. For field definitions, see rsmf_manifest.json file on the Relativity Documentation site.

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
{

    "version": "1.00",

    "participants": [

        {

            "display": "Jane Doe",

            "id": "001"

        },

        {

            "display": "John Doe",

            "id": "002"

        }

    ],

    "conversations": [

        {

            "display": "Slack conversation with three replies",

            "id": "1234",

            "platform": "slack",

            "type": "channel",

            "participants": [

                "001",

                "002"

            ]

        }

    ],

    "events": [

        {

            "id": "007",

            "participant": "001",

            "timestamp": "2004-03-11T17:04:19",

            "type": "message",

            "body": "I am a parent event :alien:",

            "conversation": "1234",

            "importance": "normal"

        },

        {

            "id": "008",

            "participant": "002",

            "timestamp": "2004-03-12T17:33:56",

            "type": "message",

            "deleted": false,

            "body": "First reply",

            "conversation": "1234",

            "parent": "007"

        }

    ]

}
```

## Retrieve attachment information for a short message

To retrieve attachment information associated with a short message document, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspace/{workspaceID}/short-message/{documentID}/attachment-info
```

View field descriptions for a request

The request includes the following field:

- attachmentIDs - a string array containing IDs for attachments to return information about. The ID corresponds to the attachment object in the RSMF manifest file. See rsmf_manifest.json file on the Relativity Documentation site.

View a sample JSON request Copy

```text
1
2
3
4
5
6
{

    "attachmentIDs": [

        "1040812.jpg",

        "Powerpoint2016.pptx"

    ]

}
```

View field descriptions for a response

The response is an array of AttachmentInfo objects. These objects contain the following fields:

- AttachmentID - the ID field for the attachment in the RSMF manifest file.

- DocumentArtifactID - the ArtifactID of the attachment document.

- FileGuid - the GUID for the attachment file.

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
[

    {

        "AttachmentID": "1040812.jpg",

        "DocumentArtifactID": 1439830,

        "FileGuid": "2746d6da-5a12-445c-9b53-51204697dd53"

    },

    {

        "AttachmentID": "Powerpoint2016.pptx",

        "DocumentArtifactID": 1439831,

        "FileGuid": "355a63ab-2266-49c9-a7aa-e8efcaab4cfb"

    }

]
```

## Retrieve entity information for a participant in a short message document

You can retrieve entity information for a participant in a short message conversation. An Entity object links people, companies, organizational groups, and their metadata. For more information, see Entity object on the Relativity Documentation site.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/short-message/participant-info
```

View field descriptions for a request

The response contains the following fields:

- participantRequests - an array containing ParticipantRequestInfo objects. A ParticipantRequestInfo object contains the following fields:

- Id - the ID for the participant in the RSMF manifest file. For more information, see rsmf_manifest.json file on the Relativity Documentation site.

- Name - the display field for the participant in the RSMF manifest file.

- Email - an optional email field for the participant in the RSMF manifest file.

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
{

    "participantRequests": [

        {

            "Id":"001",

            "Name":"Jane Doe",

            "Email":"Jane.Doe@relativity.com"

        },

        {

            "Id":"002",

            "Name":"John Doe"

        }

    ]

}
```

View field descriptions for a response

The response is an array of ParticipantResponseInfo objects. A ParticipantResponseInfo object contains the following fields:

- ParticipantID - the ID field for the participant in the RSMF manifest file. For more information, see rsmf_manifest.json file on the Relativity Documentation site.

- EntityName - the name of the corresponding entity object for the participant.

- Aliases - a list of alias names associated with the entity object for the participant.

- Url - a URL that links to the entity object corresponding to the participant.

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
[

    {

        "ParticipantID": "001",

        "EntityName": "Jane Doe",

        "Aliases": [

            "Doe, Jane"

        ],

        "Url": "exampleentityforjane.com"

    },

    {

        "ParticipantID ": "002",

        "EntityName": "John Doe",

        "Aliases": [

            "Doe, John",

            "John.Doe@relativity.com"

        ],

        "Url": "exampleentityforjohn.com"

    }

]
```

## Validate the RSMF for a file or document

You can verify whether a specific file or document has a valid RSMF. For more information, see Relativity Short Message Format on the Relativity Documentation site.

### Validate the RSMF for a file

To validate the RSMF for a file, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/short-message/validate
```

View field descriptions for a request

The request contains the following fields:

- fileName - a string representing the file name of a specific short message document for validation.

- file - a IKeplerStream object representing the file being validated.

View a JavaScript code sample used to make a stream request

The following code sample illustrates how to upload a file for validation using JavaScript:

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
const fileinput = document.getElementById("file_input");

fileinput.onchange = event => {

    currentFile = event.target.files[0];

};



const metaData = {

    fileName: currentFile.name

};



const formData = new FormData();

formData.append("file", currentFile);

formData.append("", new Blob([JSON.stringify(metaData)], { type: "application/json" }));



const xhr = new XMLHttpRequest();



xhr.onreadystatechange = () => {

    if (xhr.readyState === 4) {

        const response = JSON.parse(xhr.response);

    }

}



xhr.open('post', url);

xhr.setRequestHeader("X-CSRF-Header", csrfToken);

xhr.send(formData);
```

View field descriptions for a response

The response is an RSMFValidationResponse containing the following fields:

- Status - indicates whether the RSMF is valid. Its value may be Passed, Failed, or PassedWithWarnings.

- Errors - a list of validation errors for the RSMF. Each object contains these properties: LineNumber, LinePosition, Message, and list of Submessages.

- Warnings - a list of validation warnings for the RSMF. Each object contains these properties: LineNumber, LinePosition, Message, and list of Submessages.

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
22
{

    "Status": "Failed",

    "Errors": [

        {

            "LineNumber": 46,

            "LinePosition": 3,

            "Message": "Invalid conversation at line 46 position 3",

            "Submessages": [

                "Missing Required Property: \"id\""

            ]

        },

        {

            "LineNumber": 66,

            "LinePosition": 3,

            "Message": "Invalid conversation at line 66 position 3",

            "Submessages": [

                "Property \"type\" must have one of the following values: {direct, channel}"

            ]

        }

    ],

    "Warnings": []

}
```

### Validate the RSMF for a document

To validate the RSMF for a document, send a GET request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/short-message/{documentID}/validate
```

The request body is empty.

View field descriptions for a response

The response is an RSMFValidationResponse containing the following fields:

- Status - indicates whether the RSMF is valid. Its value may be Passed, Failed, or PassedWithWarnings.

- Errors - a list of validation errors for the RSMF. Each object contains these properties: LineNumber, LinePosition, Message, and list of Submessages.

- Warnings - a list of validation warnings for the RSMF. Each object contains these properties: LineNumber, LinePosition, Message, and list of Submessages.

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
22
{

    "Status": "Failed",

    "Errors": [

        {

            "LineNumber": 46,

            "LinePosition": 3,

            "Message": "Invalid conversation at line 46 position 3",

            "Submessages": [

                "Missing Required Property: \"id\""

            ]

        },

        {

            "LineNumber": 66,

            "LinePosition": 3,

            "Message": "Invalid conversation at line 66 position 3",

            "Submessages": [

                "Property \"type\" must have one of the following values: {direct, channel}"

            ]

        }

    ],

    "Warnings": []

}
```

On this page

- Short Message Viewer Manager (REST)

- Guidelines for using the Short Message Viewer Manager service

- URLs

- Retrieve the JSON for a short message

- Retrieve attachment information for a short message

- Retrieve entity information for a participant in a short message document

- Validate the RSMF for a file or document

- Validate the RSMF for a file

- Validate the RSMF for a document


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
