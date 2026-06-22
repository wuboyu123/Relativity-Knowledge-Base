---
title: "Imaging API (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Imaging/Imaging_API_services_for_REST.htm
collection: developer
fetched_at: 2026-06-22T06:23:15+00:00
sha256: dc8944645c4743f8ccbb7ae803a69eee96317c6920f8124b2745b0aa93d108c5
---

Imaging API (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Imaging API (REST)

Imaging API provides multiple HTTP services used for programmatically interacting with imaging profiles, sets, jobs, and other related components:

- The services for imaging jobs include endpoints for running and canceling jobs, updating priorities on jobs, and retrying jobs with errors.

- The services for imaging profiles, imaging sets, and application field codes support all CRUD operations. The imaging set service provides additional functionality used to hide and release images during a quality control review, while the native type service includes functionality for reading native file types supported by Relativity.

- Additional services provide endpoints for retrieving imaging status information for documents and managing your imaging environment.

Sample use cases for the imaging services include:

- Use the imaging services to automate a workflow for running imaging jobs rather than manually performing these tasks through the Relativity UI.

- Implement an application with a custom UI that displays information about imaging profiles, imaging sets, and jobs based on specific requirements from your organization.

You can also access the Imaging API services through .NET. For more information, see Imaging (.NET) .

The Imaging API is now versioned in the Osier release. The content on this page illustrates how to use this new versioned API. However, you can continue to use the legacy Imaging API with the Osier release although you should consider implementing any new functionality with the versioned Imaging API. For legacy documentation, see Imaging API on the Relativity Server 2021 Developers site.

## Guidelines for the Imaging services

Review the following guidelines for working with these services.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve an imaging profile:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-profiles/{ImagingProfileID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {WorkspaceID} to the Artifact ID of the workspace that contains the imaging profile.

- {ImagingProfile} to the Artifact ID of a specific imaging profile.

## Imaging Profile Manager

An imaging profile defines a set of options that you can use when imaging a group of documents. It may include options for controlling how spreadsheets, emails, or other document types are imaged, such as page orientation, or other specialized settings. For more information, see Imaging profiles on the Relativity Server 2025 Documentation site.

The Imaging Profile Manager service supports create, read, update, and delete operations on imaging profiles.

Create a basic imaging profile

To create a basic imaging profile that uses options available on basic imaging engine, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-profiles/basic
```

The request body must contain a request object with the following fields:

- Name - the user-friendly name for the imaging profile.

- Keywords - words or concise phrase used to describe the imaging profile.

- Notes - a description or other information about the imaging profile.

- BasicOptions - the settings for a basic imaging job include the following:

- ImageOutputDpi - the image output quality (DPI).

- BasicImageFormat - the basic image format, such as JPEG or TIFF.

- ImageSize - the basic image size, such as original setting, letter, A4, or legal.

- MaximumImageHeight - the maximum of height of custom images in inches for the imaging profile.

- MaximumImageWidth - the maximum width of custom images in inches for the imaging profile.

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
{

    "request":

    {

        "Name": "Basic Profile",

        "Keywords": "Basic Imaging Keywords",

        "Notes": "Basic Imaging Notes",

        "BasicOptions": {

            "ImageOutputDpi": 299,

            "BasicImageFormat": 1, //JPEG

            "ImageSize": 4, //Custom,

            "MaximumImageHeight": 2.0, //Optional

            "MaximumImageWidth": 5.5 //Optional

        }

    }

}
```

When an imaging profile is successfully created, the response contains its Artifact ID.

Copy

```text
1
{{ImagingProfileID}}
```

Create a native imaging profile

To create a native imaging profile that uses options available on the native imaging engine, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-profiles/native
```

The request body must contain a request object with the following fields unless specifically identified as optional:

- Name - the user-friendly name for an imaging profile.

- Notes - a description or other information about the imaging profile.

- Keywords - words or concise phrase used to describe the imaging profile.

- BasicOptions - the group of basic image settings for this imaging profile as follows:

- ImageOutputDpi - the image output quality (DPI).

- BasicImageFormat - the basic image format, such as a JPEG or TIFF.

- ImageSize - the basic image size, such as original setting, letter, A4, or legal.

- MaximumImageHeight - the maximum of height of custom images in inches for the imaging profile.

- MaximumImageWidth - the maximum width of custom images in inches for the imaging profile.

- NativeOptions - the group of native image settings for this imaging profile as follows:

- ImageOutputDpi - the resolution and density of an image in dots per inch (DPI). This field is optional.

- NativeImageFormat - the image format for files sent to the native imaging engine. The supported formats include JPEG or TIFF.

- RenderColorPagesToJpeg - a Boolean value indicating whether to automatically render color pages as JPEG files. This property overrides the NativeImageFormat property if it's set to TIFF. This field is optional.

- DitheringAlgorithm - the dithering algorithm used when imaging documents. This field is optional.

- DitheringThreshold - the dithering threshold used to determine how color pixels are converted to black and white. This integer value can range from 0 - 255. This field is optional.

- MaxPagesPerDoc - the maximum number of document pages imaged per file. This field is optional.

- SpreadsheetOptions - the settings used for imaging spreadsheets. The following fields are required only for spreadsheets unless specifically identified as optional:

- PaperSizeOrientation - the paper size and orientation used to render the pages in a spreadsheet.

- PageOrder - the order used to render the pages in a spreadsheet, such as vertical or horizontal overflow.

- PrintArea - the print area in a spreadsheet used for an imaging job.

- HideAndPagebreakAfterConsecutiveBlankRowCol - the option controlling the maximum number of consecutive blank rows or columns.

- ShowTrackChanges - a Boolean value indicating whether to display modifications made through the Track Changes option in Excel.

- IncludeRowAndColumnHeadings - indicates whether to render row headings (1, 2, 3, etc.) and column headings (A, B, C, etc.) in a spreadsheet.

- IncludeHeadersAndFooters - indicates whether to render headers and footers in the spreadsheet.

- IncludeComments - a Boolean value indicating whether to render comments added to a spreadsheet.

- IncludeGridlines - indicates whether to render the grid lines between rows and columns in the spreadsheet.

- IncludeBorders - a Boolean value indicating whether to render the borders in a spreadsheet.

- UnhideHiddenWorksheets - a Boolean value indicating whether to display hidden worksheets.

- LimitToPages - controls the number of pages to render. This field is optional.

- FitToPagesWide - resets the page width for a spreadsheet. This field is optional.

- FitToPagesTall - resets the page height for a spreadsheet. This field is optional.

- Formatting - indicates how to format a spreadsheet, such as auto-fit rows and columns, and clearing empty rows and columns. This field is optional.

- TextVisibility - indicates how to handle text visibility by controlling background and font color.

- EmailOptions - the settings used for imaging email messages. The following fields are required only for email messages:

- Orientation - indicates whether the orientation of email messages is portrait or landscape.

- ResizeImagesToFitPage - a Boolean value indicating whether to modify images to fit the page size.

- ResizeTablesToFitPage - a Boolean value indicating whether to modify tables to fit the page size.

- SplitTablesToFitPageWidth - a Boolean value indicating whether to split oversized tables and re-print them.

- DownloadImagesFromInternet - a Boolean value indicating whether to allow downloading images from the Internet.

- ClearIndentations - a Boolean value indicating whether tabs are removed from the display of email threads.

- DetectCharacterEncoding - a Boolean value indicating whether to override the code page for an email during imaging.

- DisplaySmtpAddresses - a Boolean value indicating whether to display SMTP addresses in the UI.

- ShowMessageTypeInHeader - a Boolean value indicating whether to identify the image as a message, appointment, distribution list, or other entity.

- WordProcessingOptions - the settings used for imaging documents formatted with word processing options, such Microsoft Word. The following fields are required only for word processing files:

- ShowTrackChanges - a Boolean value indicating whether to display any markup added to the document through the Track Changes feature in Microsoft Word.

- PageOrientation - the word processing option for page orientation, such portrait, landscape, or original orientation.

- Include - a list of the word processing options for rendering comments, field codes, and hidden text.

- PresentationOptions - the settings used for imaging documents from presentation software, such as Microsoft PowerPoint. The following fields are required only for presentations:

- ShowSpeakerNotes - a Boolean value indicating whether to display the speaker’s notes at the bottom of presentation slides.

- SlideOrientation - the orientation of presentation slides, such as landscape, portrait, or original setting.

- HtmlOptions - the setting used for imaging HTML documents. This field is required only for HTML documents:

- RemoveNonBreakingSpaceCodes - a Boolean value indicating whether to remove non-breaking spaces (NBSP).

- NativeTypes - an array of native types associated with the imaging profile. This field is optional. If you don't set this field, Relativity uses the default restricted native types. For more information, see Imaging native types on the Relativity Server 2025 Documentation site.

- ApplicationFieldCodes - an array of fields used by Microsoft documents to store data. This field is optional. For more information, see Application Field Codes on the Relativity Server 2025 Documentation site.

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
83
84
85
86
87
88
89
90
91
92
93

{

    "request":

    {

        "Name": "Native Profile from Postman",

        "Keywords": "Native Imaging Keywords",

        "Notes": "Native Imaging Notes",

        "BasicOptions": {

            "ImageOutputDpi": 305,

            "BasicImageFormat": 1, //JPEG

            "ImageSize": 4, //Custom,

            "MaximumImageHeight": 11.5, //Optional

            "MaximumImageWidth": 12.1 //Optional

        },

        "NativeOptions": {

            "ImageOutputDpi": 400,

            "NativeImageFormat": 0, //TIFF

            "RenderColorPagesToJpeg": true,

            "DitheringAlgorithm": 7, //Threshold

            "DitheringThreshold": 100,

            "MaxPagesPerDoc": 1000 //Optional

            //TimeZoneFieldOnDocument

            //LastModifiedDateOnDocument

        },

        "SpreadsheetOptions": {

            "PaperSizeOrientation": 1, //Letter8Point5X11

            "PageOrder": 2, //OverThenDown

            "PrintArea": 1, //IgnorePrintArea

            "HideAndPagebreakAfterConsecutiveBlankRowCol": 56,

            "ShowTrackChanges": true,

            "IncludeRowAndColumnHeadings": 2, //No

            "IncludeHeadersAndFooters": 2, //No

            "IncludeComments": true,

            "IncludeGridlines": 1, //Yes

            "IncludeBorders": true,

            "UnhideHiddenWorksheets": true,

            "LimitToPages": 45, //Optional,

            //"ZoomLevelPercentage": 101, //Optional, ignored when FitTo* is set

            "FitToPagesWide": 200, //Optional

            "FitToPagesTall": 201, //Optional

            "Formatting": [1,2], //[AutoFitColumns, ClearFormattingInEmptyRows] (Optional)

            "TextVisibility": [0,1] //[RemoveBackgroundFillColors, SetTextColorToBlack] (Optional)



        },

        "EmailOptions": {

            "Orientation": 1, //Landscape

            "ResizeImagesToFitPage": true,

            "ResizeTablesToFitPage": true,

            "SplitTablesToFitPageWidth": true,

            "DownloadImagesFromInternet": true,

            "ClearIndentations": true,

            "DetectCharacterEncoding": true,

            "DisplaySmtpAddresses": true,

            "ShowMessageTypeInHeader": false

        },

        "WordProcessingOptions": {

            "ShowTrackChanges": true,

            "PageOrientation": 2, //Landscape

            "Include": [0, 2] //[Comments, HiddenText] (Optional)

        },

        "PresentationOptions": {

            "ShowSpeakerNotes": true,

            "SlideOrientation": 2 //Landscape

        },

        "HtmlOptions": {

            "RemoveNonBreakingSpaceCodes": true

        },

         "NativeTypes": [

            {

                "ArtifactID": 1036955,

                "Name": "DBase III"

            },

            {

                "ArtifactID": 1036956,

                "Name": "DBase IV or V"

            },

            {

                "ArtifactID": 1036957,

                "Name": "Framework III"

            }

        ],

        "ApplicationFieldCodes": [

            {

                "ArtifactID": 1038657,

                "Name": "Word Date"

            },

            {

                "ArtifactID": 1038666,

                "Name": "Excel Page"

            }

        ]

    }

}
```

When an imaging profile is successfully created, the response contains its Artifact ID.

Copy

```text
1
{{ImagingProfileID}}
```

Retrieve an imaging profile

To retrieve an imaging profile, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-profiles/{ImagingProfileID}
```

The request body is empty.

The response for a read operation contains the many of the same fields as a request for a create operation. See the field descriptions in Create a native imaging profile .

The read response also contains these fields:

- ImagingMethod - the imaging method used for running jobs with the profile as follows:

- Basic - uses options available on the basic imaging engine.

- Native - uses options available on the native imaging engine.

For more information, see Imaging profiles on the Relativity Server 2025 Documentation site.

- ArtifactID - the unique identifier for the imaging profile.

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
{

    "ImagingMethod": "Native",

    "BasicOptions": {

        "ImageOutputDpi": 300,

        "BasicImageFormat": "Tiff",

        "ImageSize": "OriginalSetting"

    },

    "NativeOptions": {

        "ImageOutputDpi": 300,

        "NativeImageFormat": "Tiff",

        "RenderColorPagesToJpeg": false,

        "DitheringAlgorithm": "FloydAndSteinberg"

    },

    "SpreadsheetOptions": {

        "PaperSizeOrientation": "OriginalSetting",

        "PageOrder": "OriginalSetting",

        "PrintArea": "IgnorePrintArea",

        "HideAndPageBreakAfterConsecutiveBlankRowCol": 10,

        "ShowTrackChanges": true,

        "IncludeRowAndColumnHeadings": "OriginalSetting",

        "IncludeHeadersAndFooters": "OriginalSetting",

        "IncludeComments": true,

        "IncludeGridlines": "Yes",

        "IncludeBorders": true,

        "UnhideHiddenWorksheets": true

    },

    "EmailOptions": {

        "Orientation": "Portrait",

        "ResizeImagesToFitPage": true,

        "ResizeTablesToFitPage": true,

        "SplitTablesToFitPageWidth": true,

        "DownloadImagesFromInternet": true,

        "ClearIndentations": false,

        "DetectCharacterEncoding": true,

        "DisplaySmtpAddresses": false,

        "ShowMessageTypeInHeader": false

    },

    "WordProcessingOptions": {

        "ShowTrackChanges": true,

        "PageOrientation": "OriginalSetting"

    },

    "PresentationOptions": {

        "ShowSpeakerNotes": true,

        "SlideOrientation": "OriginalSetting"

    },

    "HtmlOptions": {

        "RemoveNonBreakingSpaceCodes": false

    },

    "NativeTypes": [

        {

            "ArtifactID": 1035893,

            "Name": "Smart DataBase"

        },

        {

            "ArtifactID": 1035894,

            "Name": "DBase III"

        }

    ],

    "ArtifactID": 1039439,

    "Name": "Native Profile"

}
```

Update an imaging profile

To update an imaging profile, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-profiles/{ImagingProfileID}
```

The request body must contain a request object with the following fields:

- Name - the user-friendly name for the imaging profile.

- BasicOptions - the settings for a basic imaging job as follows:

- ImageOutputDpi - the image output quality (DPI).

- BasicImageFormat - the basic image format, such as JPEG or TIFF.

- ImageSize - the basic image size, such as original setting, letter, A4, or legal.

- NativeOptions - the settings for a native imaging job as follows:

- ImageOutputDpi - the image output quality (DPI).

- NativeImageFormat - the native image format, such as JPEG or TIFF.

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
{

    "request":

    {

        "Name": "Profile Testing",

        "BasicOptions": {

            "ImageOutputDpi": 300,

            "BasicImageFormat": "Jpeg",

            "ImageSize": "OriginalSetting"

        },

        "NativeOptions": {

            "ImageOutputDpi": 600,

            "NativeImageFormat": "Jpeg"

        }

    }

}
```

When an imaging profile is successfully updated, the response contains its Artifact ID.

Copy

```text
1
{{ImagingProfileID}}
```

Delete an imaging profile

To delete an imaging profile, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-profiles/{ImagingProfileID}
```

The request body is empty.

When the imaging profile is successfully deleted, the response returns the status code of 200.

## Imaging Set Manager

To running an imaging job, you need to create an imaging set, which consists of an imaging profile and a search containing the documents to image. For general information, see Imaging sets and QC Review on the Relativity Server 2025 Documentation site.

The Imaging Sets Manager API supports create, read, update, and delete operations on imaging sets. It also supports the hide and release operations used for a QC Review of imaged documents.

Create an imaging set

To create an imaging set, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets
```

The request must contain the following fields:

- DataSourceID - the Artifact ID of the saved search containing the documents for imaging.

- ImagingProfileID - the Artifact ID of the imaging profile associated with the imaging set.

- Name - the user-friendly name of the imaging set.

- EmailNotificationRecipients - a list of email addresses for users who are notified after the associated imaging job completes. This field must be included in the JSON request, but you can set it to an empty string.

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
{

    "request" : {

        "DataSourceID" : {{DataSourceID}},

        "ImagingProfileID" : {{ImagingProfileID}},

        "Name" : "All documents",

        "EmailNotificationRecipients" : "some_person@test.com;some_other_person@test.com"

    }

}
```

When an imaging set is successfully created, the response contains its Artifact ID.

Copy

```text
1
{{ImagingSetID}}
```

Retrieve an imaging set

To retrieve an imaging set, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}
```

The request body is empty.

The response returns the following fields:

- ImagingProfile - the imaging profile associated with the imaging set. This object contains the following field:

- ArtifactID - the Artifact ID of the imaging profile.

- DataSourceID - the Artifact ID of the saved search containing the documents for imaging.

- Status - contains the following:

- LastRunError - a string indicating an error on the previous job for this imaging set.

- QCEnabledOnLastRun - a Boolean value indicating whether a quality control review was enabled on the last job for this imaging set.

- Status - a string indicating the imaging set status

- ArtifactID - the Artifact ID of the imaging set.

- Name - the user-friendly name of the imaging set.

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
{

    "ImagingProfile": {

        "ArtifactID": {{ImagingProfileID}}

    },

    "DataSourceID": {{DataSourceID}},

    "Status": {

        "LastRunError": "",

        "QCEnabledOnLastRun": false,

        "Status": "Completed with errors"

    },

    "ArtifactID": {{ImagingSetID}},

    "Name": "All documents"

}
```

Update an imaging set

To update an imaging set, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}
```

The request for an update operation must contains the same fields as those for a create request. See the field descriptions for the request in Create an imaging set .

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
{

    "request" : {

        "DataSourceID" : {{DataSourceID}},

        "ImagingProfileID" : {{ImagingProfileID}},

        "Name" : "All documents",

        "EmailNotificationRecipients" : "some_person@test.com;some_other_person@test.com"

    }

}
```

When an imaging set is successfully updated, the response contains its Artifact ID.

Copy

```text
1
{{ImagingSetID}}
```

Delete an imaging set

To delete an imaging set, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}
```

The request body is empty.

The response returns the status code of 200 when the image set is successfully deleted.

Hide an imaging set

You can prevent users from viewing images that need to undergo a quality control review by hiding them. For more information, see QC Review on the Relativity Server 2025 Documentation site.

To hide an imaging set, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}/hide-images
```

The request body is empty.

When the image set is successfully hidden, the response returns the status code of 200.

Release an imaging set

After a quality control review has been completed on hidden images, you can make them available to reviewers by releasing them. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}/release-images
```

The request body is empty.

When the image set is successfully released, the response returns the status code of 200.

Retrieve the status of an imaging set

To retrieve the status of an imaging set, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}/status
```

When you read an imaging set, its status is also returned. See Retrieve an image set .

The request body is empty.

The response contains the following fields:

- Status - a string indicating the imaging set status.

- LastRunError - a string indicating an error on the previous job for this imaging set.

- QcReviewEnabledOnLastRun - a Boolean value indicating whether a quality control review was enabled on the last job for this imaging set.

- JobType - an integer indicating if the job is in progress as follows:

- 0 - no running job.

- 1 - full imaging job.

- 2 - imaging job with retry errors.

- NumberOfDocuments - an integer indicating the total number of documents in the imaging set.

- NumberOfDocumentsHidden - an integer indicating the number of documents hidden for quality control review.

- NumberOfDocumentsViewable - an integer indicating the number of documents visible for quality control review.

- NumberOfDocumentsWithWarnings - an integer indicating the number of documents with warnings.

- JobStatus - indicates the status of the job as follows:

- Invalid - an invalid job.

- Default - the imaging job isn't initialized. This value is returned if the imaging job doesn't exist.

- Created - the imaging job has been created.

- CancelRequested - the Imaging job has been flagged for cancellation.

- PickedUpByAgent - the Imaging Request agent has picked up the job.

- SubmittedToInvariant - the documents in the imaging job have been submitted to Invariant.

- JobExists - a Boolean indicating one of the following:

- True - the imaging job exists.

- False - the imaging job has completed or doesn't exist.

- NumberOfDocumentsCompleted - an integer indicating the number of documents completed. This value is 0 until the job is submitted to Invariant.

- NumberOfDocumentsSkipped - an integer indicating the number of documents skipped. This value is 0 until the job is submitted to Invariant.

- NumberOfDocumentsWaiting - an integer indicating the number of documents waiting to be converted to images.

- NumberOfDocumentsErrored - an integer indicating the number of documents in an errored state. This value is 0 until the job is submitted to Invariant.

- NumberOfDocumentsSubmitted - an integer indicating the number of documents submitted in the job.

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
{

"Status": "Completed with errors",

"LastRunError": "",

"QcReviewEnabledOnLastRun": false,

"JobType": 0,

"NumberOfDocuments": 10,

"NumberOfDocumentsHidden": 0,

"NumberOfDocumentsViewable": 8,

"NumberOfDocumentsWithWarnings": 0,

"JobStatus": "Default",

"JobExists": false,

"NumberOfDocumentsCompleted": 0,

"NumberOfDocumentsSkipped": 8,

"NumberOfDocumentsWaiting": 0,

"NumberOfDocumentsErrored": 2,

"NumberOfDocumentsSubmitted": 0

}
```

## Native Type Manager

You can retrieve native file types supported by Relativity for imaging. For more information, see Imaging native types on the Relativity Server 2025 Documentation site.

Retrieving a native type

To retrieve a native type, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/native-types/{NativeTypeID}
```

The request body is empty.

The response returns the following fields:

- BasicCategory - the basic imaging category for this native type, such as spreadsheet, graphic, or others. For more information, see the BasicCategory enumeration in Class library reference on the Relativity API reference page.

- NativeCategory - the native imaging category for this native type, such a spreadsheet, email message, or others. For more information, see the NativeCategory enumeration in Class library reference on the Relativity API reference page.

- UseNativeImaging - a Boolean value indicating whether to use native imaging on this native type.

- RestrictedFromImagingByDefault - a Boolean value indicating whether this native type is restricted from imaging by default.

- FileTypeId - the identifier of the file type used by Invariant.

- PreventNativeDownload - a Boolean value indicating whether the native type is restricted from being downloaded.

- ArtifactID - the Artifact ID of the native type.

- Name - the user-friendly name for the native type.

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
{

    "BasicCategory": "WordProcessor",

    "UseNativeImaging": false,

    "RestrictedFromImagingByDefault": false,

    "FileTypeID": 1000,

    "PreventNativeDownload": false,

    "ArtifactID": 1036768,

    "Name": "Word for DOS 4.x"

}
```

## Application Field Code Manager

Microsoft applications use fields codes as placeholders for data that may be updated or used for other specialized purposes in their documents, such as those created in Word, Excel, or others. In Relativity, application field codes indicate how to handle field codes used in Microsoft documents during imaging. For more information, see Application Field Codes on the Relativity Server 2025 Documentation site.

Use the Application Field Code Manager service to create, read, update, or delete application field codes.

Create an application field code

To create an application field code, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/application-field-codes
```

The request must contain the following fields:

- applicationFieldCode - indicates how to handle field codes used in Microsoft documents during imaging. This object contains the following fields:

- FieldCode - a string indicating that the field code is available in a specific application, such as Microsoft Word, Excel, or Visio.

- Application - an identifier for the application associated with a field code, such as Microsoft Word, Excel, or others. For more information, see the ApplicationType enumeration in Class library reference on the Relativity API reference page.

- Option - the option controlling whether the field code is displayed, replaced with a Relativity application field code, or some other action is taken for rendering the field code in an image. For more information, see ApplicationFieldCodeOption enumeration in the Class library reference reference and Application Field Codes on the Relativity Server 2025 Documentation site.

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

    "ApplicationFieldCode": {

        "FieldCode": "DateTime",

        "Application": "MicrosoftWord",

        "Option": "ShowFieldCode"

    }

}
```

The response contains Artifact ID of the new field code.

Copy

```text
1
{{applicationFieldCodeID}}
```

Retrieve an application field code

To retrieve an application field code, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/application-field-codes/{applicationFieldCodeID}
```

The request body is empty.

The response returns the following fields:

- FieldCode - a string indicating that the field code is available in a specific application, such as Microsoft Word, Excel, or Visio.

- Application - an identifier for the application associated with a field code, such as Microsoft Word, Excel, or others. For more information, see the ApplicationType enumeration in the Class library reference on the Relativity API reference page.

- Option - the option controlling whether the field code is displayed, replaced with a Relativity application field code, or some other action is taken for rendering the field code in an image. For more information, see the ApplicationFieldCodeOption enumeration in the Class library reference reference and Application Field Codes on the Relativity Server 2025 Documentation site.

- ImagingProfiles - an array of Artifact IDs for the imaging profiles that use this application field code.

- ArtifactID - the Artifact ID of the application field code.

- Name - the user-friendly name for the Relativity application field code.

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
{

    "FieldCode": "Date",

    "Application": "MicrosoftWord",

    "Option": "ShowNothing",

    "ImagingProfiles": [

        {

            "ArtifactID": 1037523

        }

    ],

    "ArtifactID": 1038657,

    "Name": "MicrosoftWord Date ShowNothing"

}
```

Update an application field code

To update an application field code, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/application-field-codes/{applicationFieldCodeID}
```

The request for an update operation must contains the same fields as those for a create request. See the field descriptions for the request in Create an application field code .

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

    "ApplicationFieldCode": {

        "FieldCode": "DateTime",

        "Application": "MicrosoftExcel",

        "Option": "ShowFieldCode"

    }

}
```

The response contains Artifact ID of the updated field code.

Copy

```text
1
{{applicationFieldCodeID}}
```

Delete an application field code

To delete an application field code, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/application-field-codes/{applicationFieldCodeID}
```

The request body is empty.

When the application field code is successfully deleted, the response returns true.

Copy

```text
1
true
```

## Imaging Job Manager

Use the Imaging Job Manager service to run jobs to image documents, cancel a job currently executing on an imaging set, or retry errors that occurred during a job. For general information, see Running an imaging set and Imaging errors on the Relativity Server 2025 Documentation site.

Run an imaging set job

To schedule an imaging set job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}/run
```

The request body may contain the following field:

- QCEnabled - an optional Boolean set to one of these values:

- True - indicates that the images are hidden until the QC review process is completed.

- False - indicates that the images aren't hidden during the QC review process.

Copy

```text
1
2
3
4
5
{

   "imagingSetRequest":{

      "QcEnabled":true

   }

}
```

The response contains Artifact ID for the job.

Copy

```text
1
2
3
{

    "ImagingJobID": {{ImagingJobID}}

}
```

Submit an imaging job for a single document

You can submit an imaging job for a single document, such as an image on the fly request. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/documents/{DocumentArtifactID}/image
```

The request body must contain the following fields:

- ProfileID - the Artifact ID of a specific imaging profile.

- OriginationId - a GUID that is a unique identifier for the imaging job.

Copy

```text
1
2
3
4
5
{

   "imageOnTheFlyRequest":{

      "ProfileID":1036462

   }

}
```

The response contains Artifact ID for the job.

Copy

```text
1
2
3
{

   "ImagingJobID": {{ImagingJobID}}

}
```

Submit a mass imaging job

To submit a mass imaging job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/documents/mass-image
```

The request body must contain the following fields:

- ProfileId - the Artifact ID of a specific imaging profile.

- MassProcessId - the mass process ID for the modal.

- sourceType - this field set to one of the following values:

- 0 - indicates that a native document is the source file to be imaged.

- 1 - indicates that a rendered PDF is the source file to be imaged.

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

   "MassImageRequest":{

      "ProfileId":"1036462",

      "MassProcessId":5,

      "sourceType":"0"

   }

}
```

The response contains Artifact ID for the job.

Copy

```text
1
2
3
{

    "ImagingJobID": {{ImagingJobID}}

}
```

Cancel an imaging job

You can stop an in-progress imaging job, including jobs for imaging sets and image on the fly. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/jobs/{ImagingJobID}/stop
```

The request body must contain an empty JSON object as follows:

Copy

```text
1
2
3
4
5
{

   "stopImagingJobRequest":{



   }

}
```

The response contains the following fields:

- Success -a Boolean value indicating whether the job is canceled without errors.

- ErrorMessage - a string containing information about any errors that occurred when canceling the job.

Copy

```text
1
2
3
4
{

    "Success": true,

    "ErrorMessage": ""

}
```

Retry imaging set errors

To retry imaging set errors, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/imaging-sets/{ImagingSetID}/retry-errors
```

The request body must contain an empty JSON object as follows:

Copy

```text
1
2
3
4
5
{

   "imagingSetRequest":{



   }

}
```

The response contains Artifact ID for the job.

Copy

```text
1
2
3
{

    "ImagingJobID": {{ImagingJobID}}

}
```

Update the priority of an imaging job

To update the priority of an imaging job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/jobs/{ImagingJobID}/priority
```

The request body must contain the following field:

- Priority - an integer indicating the updated priority value.

Copy

```text
1
2
3
4
5
{

   "updateJobPriorityRequest":{

      "Priority":1

   }

}
```

The response contains the following fields:

- Success - a Boolean value indicating whether the priority was updated.

- ErrorMessage - a string containing information about any errors that occurred when updating the priority.

Copy

```text
1
2
3
4
{

    "Success": true,

    "ErrorMessage": ""

}
```

## Document Status Manager

Use the Document Status Manager service to obtain status information about the imaging job for a document.

Retrieve imaging status of a document

To retrieve the imaging status of a document, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/workspaces/{WorkspaceID}/documents/{DocumentArtifactID}/status
```

The request body is empty.

The response is a Document Image Status Response object that contains the following fields:

- ImageCount - the number images for the document.

- Error - this field contains the following:

- Message - a string containing information about the error.

- Status - a string indicating the error status.

- Warnings - an array of document warning objects. Each object contains the following:

- Message - a string containing information about the warning.

- Type - a string indicating the indicating the type of warning.

- HasImages - indicates the status of images for the document. The values for this field include Yes, No, Pending, or Error.

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
{

    "ImageCount": 0,

    "Error": {

        "Message": "OI EXOpenExport failed - 11: file is password protected or encrypted [11]",

        "Status": "ReadyToRetry"

    },

    "Warnings": [],

    "HasImages": "Error"

}
```

## Imaging Environment Manager

Use the endpoints on the Imaging Environment Manager service to remove inactive jobs and to obtain the size of mass imaging jobs.

Remove inactive imaging jobs

To remove inactive imaging jobs, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/environment/jobs/inactive-jobs
```

The request body is empty.

When the inactive jobs are successfully deleted, the response returns the status code of 200.

Retrieve the size of a mass imaging job

To retrieve the size of a mass imaging job, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-imaging/{versionNumber}/environment/jobs/mass-imaging-max-size
```

The request body is empty.

The response contains an integer indicating the number of documents in the imaging job.

Copy

```text
1
10000
```

On this page

- Imaging API (REST)

- Guidelines for the Imaging services

- URLs

- Imaging Profile Manager

- Imaging Set Manager

- Native Type Manager

- Application Field Code Manager

- Imaging Job Manager

- Document Status Manager

- Imaging Environment Manager


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
