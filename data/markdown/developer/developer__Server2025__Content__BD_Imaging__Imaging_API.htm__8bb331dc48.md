---
title: "Imaging (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Imaging/Imaging_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:13+00:00
sha256: 8ad7293d3594be8ca32d4e0524bdf7ccecdfe8c8bd93960ec8b5839edae0eeff
---

Imaging (.NET)

# Imaging (.NET)

The Imaging API supports programmatically interacting with imaging profiles, sets, jobs, and other related components:

- The interfaces for imaging jobs include methods for running and canceling jobs, updating priorities on jobs, and retrying jobs with errors.

- The interfaces for imaging profiles, imaging sets, and application field codes support all CRUD operations. The imaging set service provides additional functionality used to hide and release images during a quality control review, while the native type service includes functionality for reading native file types supported by Relativity.

- Additional interfaces provide methods for retrieving imaging status information for documents and managing your imaging environment.

Sample use cases for the imaging services include:

- Use the imaging services to automate a workflow for running imaging jobs rather than manually performing these tasks through the Relativity UI.

- Implement an application with a custom UI that displays information about imaging profiles, imaging sets, and jobs based on specific requirements from your organization.

You can also use the Imaging API through REST. For more information, see Imaging API (REST) .

## Imaging API fundamentals

The Imaging API contains the methods, classes, and enumerations required to run imaging jobs and perform other related tasks.

View Imaging API interfaces

The Imaging API includes the following interfaces available in the Relativity.Imaging.Services.Interfaces.<VersionNumber> namespace:

- IApplicationFieldCodeManager interface - contains the CRUD methods used to work with application field codes. It includes the following methods: CreateAsync(), ReadAsync(), UpdateAsync(), and DeleteAsync(). See Application Field Code Manager .

- IDocumentStatusManager - contains the GetStatusAsync() method, which retrieves status information about the imaging job for a document. See Document Status Manager .

- IImagingEnvironmentManager - contains the CleanupInactiveJobsAsync() method for cleaning up inactive imaging jobs, and the GetMaxMassImagingJobSizeAsync() for retrieving the size of a mass imaging job.

- IImagingJobManager interface - contains the methods used for executing imaging jobs. It includes the following methods: RunImagingSetAsync(), ImageDocumentAsync(), MassImageDocumentsByMassProcessIdAsync(), StopImagingJobAsync(), RetryImagingSetErrorsAsync(), and UpdateJobPriorityAsync(). See Imaging Job Manager .

- IImagingProfileManager interface - contains the CRUD methods used to work with imaging profiles. It includes the following methods: CreateBasicImagingProfileAsync(), CreateNativeImagingProfileAsync(), ReadAsync(), UpdateAsync(), and DeleteAsync(). See Imaging Profile Manager .

- IImagingSetManager interface - contains the CRUD methods used to work with imaging sets. It includes the following methods: CreateAsync(), ReadAsync(), UpdateAsync(), and DeleteAsync(). It also provides the HideImagingSetAsync() method used to hide images from reviewers during a quality control review, and the ReleaseImagingSetAsync() method to make them available to reviewers. See Imaging Set Manager

- INativeTypeManager interface - contains the ReadAsync() method used to retrieve native file types. See Native Type Manager .

View classes and enumerations

The Imaging API includes multiple classes and enumerations. The following list highlights some key classes in the Relativity.Imaging.Services.Interfaces.<VersionNumber>.Models namespace:

- ApplicationFieldCode - contains information about fields used in Microsoft documents to store data.

- BasicImagingEngineOptions - represents the settings for a basic imaging job, including the output quality (DPI), the image format as a JPEG or TIFF, image size settings, and others.

- ImagingProfile - contains the settings specified for an imaging job.

- ImagingSet - represents the imaging profile and saved search used for an imaging job.

- NativeImagingEngineOptions - represents the settings for a native imaging job, including the output quality (DPI), the image format, number of pages imaged, and others.

- NativeType - represents the native files types associated with an imaging profile.

## SDK for Imaging API

The Imaging API is released as a NuGet package that you can reference in your Visual Studio projects. For more information, see Relativity Server APIs .

## Imaging Profile Manager

An imaging profile defines a set of options that you can use when imaging a group of documents. It may include options for controlling how spreadsheets, emails, or other document types are imaged, such as page orientation, or other specialized settings. For general information, see Imaging profiles on the Relativity Server 2025 Documentation site.

The Imaging Profile Manager API supports create, read, update, and delete operations on imaging profiles.

Create a basic imaging profile

Use the CreateBasicImagingProfileAsync() method to create a basic imaging profile that uses options available on basic imaging engine. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace where you want to add the imaging profile.

- BasicImagingProfileCreateRequest object - see the code sample for property settings.

You specify only the properties for the basic profile on the BasicImagingProfileCreateRequest object. Like the Relativity UI, the options for the native profile are set to default values.

The method returns the Artifact ID of the new profile.

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
public async Task CreateBasicImagingProfileAsync(Interfaces.V1.IImagingProfileManager profileManager, int workspaceID, List<NativeTypeRef> nativeTypes)

{

    var basicProfileRequest = new BasicImagingProfileCreateRequest()

    {

        BasicOptions = new BasicImagingEngineOptions()

        {

            BasicImageFormat = ImageFormat.Jpeg,

            ImageOutputDpi = 300,

            ImageSize = ImageSize.OriginalSetting,

            MaximumImageHeight = null,

            MaximumImageWidth = null

        },

        Keywords = "",

        Name = "Basic Imaging Profile",

        Notes = "",

        NativeTypes = nativeTypes

    };

    try

    {

        await profileManager.CreateBasicImagingProfileAsync(workspaceID, basicProfileRequest).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when creating basic Imaging Profile: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Create a native imaging profile

Use the CreateNativeImagingProfileAsync() method to create a native imaging profile that uses options available on the native imaging engine. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace where you want to add the imaging profile.

- NativeImagingProfileCreateRequest object - see the code sample for property settings.

The method returns the Artifact ID of the new profile.

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
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
public async Task CreateNativeImagingProfileAsync(Interfaces.V1.IImagingProfileManager profileManager, int workspaceID, List<NativeTypeRef> nativeTypes, List<ApplicationFieldCodeRef> applicationFieldCodes)

{

    var nativeProfileRequest = new NativeImagingProfileCreateRequest()

    {

        NativeOptions = new NativeImagingEngineOptions()

        {

            DitheringAlgorithm = DitheringAlgorithm.Clustered16X16,

            DitheringThreshold = 128,

            ImageOutputDpi = 300,

            MaxPagesPerDoc = null,

            NativeImageFormat = ImageFormat.Tiff,

            RenderColorPagesToJpeg = false,

            TimeZoneFieldOnDocument = null,

            LastModifiedDateOnDocument = null

        },

        BasicOptions = new BasicImagingEngineOptions()

        {

            BasicImageFormat = ImageFormat.Jpeg,

            ImageOutputDpi = 300,

            ImageSize = ImageSize.OriginalSetting,

            MaximumImageHeight = null,

            MaximumImageWidth = null

        },

        Name = "Native Imaging Profile",

        Keywords = "",

        Notes = "",

        NativeTypes = nativeTypes,

        ApplicationFieldCodes = applicationFieldCodes,

        EmailOptions = new EmailOptions()

        {

            ClearIndentations = true,

            DetectCharacterEncoding = true,

            DisplaySmtpAddresses = true,

            DownloadImagesFromInternet = true,

            Orientation = Orientation.Landscape,

            ResizeImagesToFitPage = true,

            ResizeTablesToFitPage = true,

            ShowMessageTypeInHeader = true,

            SplitTablesToFitPageWidth = true

        },

        HtmlOptions = new HtmlOptions()

        {

            RemoveNonBreakingSpaceCodes = true

        },

        PresentationOptions = new PresentationOptions()

        {

            ShowSpeakerNotes = true,

            SlideOrientation = SlideOrientation.OriginalSetting

        },

        SpreadsheetOptions = new SpreadsheetOptions()

        {

            FitToPagesTall = null,

            FitToPagesWide = null,

            Formatting = new HashSet<Formatting>()

            {

                Formatting.AutoFitColumns,

                Formatting.AutoFitRows,

                Formatting.ClearFormattingInEmptyColumns,

                Formatting.ClearFormattingInEmptyRows

            },

            HideAndPageBreakAfterConsecutiveBlankRowCol = 10,

            IncludeBorders = true,

            IncludeComments = true,

            IncludeGridlines = IncludeGridlines.OriginalSetting,

            IncludeHeadersAndFooters = IncludeHeadersAndFooters.OriginalSetting,

            IncludeRowAndColumnHeadings = IncludeRowAndColumnHeadings.OriginalSetting,

            LimitToPages = null,

            PageOrder = PageOrder.OriginalSetting,

            PaperSizeOrientation = PaperSizeOrientation.OriginalSetting,

            PrintArea = PrintArea.OriginalSetting,

            ShowTrackChanges = true,

            TextVisibility = new HashSet<TextVisibility>()

            {

                TextVisibility.RemoveBackgroundFillColors,

                TextVisibility.SetTextColorToBlack

            },

            UnhideHiddenWorksheets = true,

            ZoomLevelPercentage = null,

        },

        WordProcessingOptions = new WordProcessingOptions()

        {

            Include = new HashSet<Include>()

            {

                Include.Comments,

                Include.FieldCodes,

                Include.HiddenText

            },

            PageOrientation = PageOrientation.OriginalSetting,

            ShowTrackChanges = true

        }

    };

    try

    {

        await profileManager.CreateNativeImagingProfileAsync(workspaceID, nativeProfileRequest).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when creating Native Imaging Profile: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Retrieve an imaging profile

Use the ReadAsync() method to retrieve an imaging profile. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging profile.

- imagingProfileID - the Artifact ID of the imaging profile.

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
public async Task<Interfaces.V1.Models.ImagingProfile> ImagingProfileReadAsync(Interfaces.V1.IImagingProfileManager imagingProfileManager, int workspaceID, int imagingProfileID)

{

    Interfaces.V1.Models.ImagingProfile imagingProfile;

    try

    {

        return await imagingProfileManager.ReadAsync(workspaceID, imagingProfileID).ConfigureAwait(false);

    }

    catch(Exception ex)

    {

        string exception = $"An error occurred when reading an Imaging Profile: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Update an imaging profile

Use the UpdateAsync() method to modify an imaging profile. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging profile.

- imagingProfileID - the Artifact ID of the imaging profile.

- ImagingProfileUpdateRequest object - see the code sample for property settings.

The method returns the Artifact ID of the updated profile.

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
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
public async Task<int> ImagingProfileUpdateAsync(Interfaces.V1.IImagingProfileManager imagingProfileManager, int workspaceID, int imagingProfileID, List<NativeTypeRef> nativeTypes, List<ApplicationFieldCodeRef> applicationFieldCodes)

{

    var request = new ImagingProfileUpdateRequest()

    {

        ApplicationFieldCodes = applicationFieldCodes,

        NativeTypes = nativeTypes,

        BasicOptions = new BasicImagingEngineOptions()

        {

            BasicImageFormat = ImageFormat.Jpeg,

            ImageOutputDpi = 300,

            ImageSize = ImageSize.OriginalSetting,

            MaximumImageHeight = null,

            MaximumImageWidth = null

        },

        Name = "Imaging Profile Update",

        Keywords = "",

        Notes = "",

        NativeOptions = new NativeImagingEngineOptions()

        {

            DitheringAlgorithm = DitheringAlgorithm.Clustered16X16,

            DitheringThreshold = 128,

            ImageOutputDpi = 300,

            MaxPagesPerDoc = null,

            NativeImageFormat = ImageFormat.Tiff,

            RenderColorPagesToJpeg = false,

            TimeZoneFieldOnDocument = null,

            LastModifiedDateOnDocument = null

        },

        EmailOptions = new EmailOptions()

        {

            ClearIndentations = true,

            DetectCharacterEncoding = true,

            DisplaySmtpAddresses = true,

            DownloadImagesFromInternet = true,

            Orientation = Orientation.Landscape,

            ResizeImagesToFitPage = true,

            ResizeTablesToFitPage = true,

            ShowMessageTypeInHeader = true,

            SplitTablesToFitPageWidth = true

        },

        HtmlOptions = new HtmlOptions()

        {

            RemoveNonBreakingSpaceCodes = true

        },

        PresentationOptions = new PresentationOptions()

        {

            ShowSpeakerNotes = true,

            SlideOrientation = SlideOrientation.OriginalSetting

        },

        SpreadsheetOptions = new SpreadsheetOptions()

        {

            FitToPagesTall = null,

            FitToPagesWide = null,

            Formatting = new HashSet<Formatting>()

            {

                Formatting.AutoFitColumns,

                Formatting.AutoFitRows,

                Formatting.ClearFormattingInEmptyColumns,

                Formatting.ClearFormattingInEmptyRows

            },

            HideAndPageBreakAfterConsecutiveBlankRowCol = 10,

            IncludeBorders = true,

            IncludeComments = true,

            IncludeGridlines = IncludeGridlines.OriginalSetting,

            IncludeHeadersAndFooters = IncludeHeadersAndFooters.OriginalSetting,

            IncludeRowAndColumnHeadings = IncludeRowAndColumnHeadings.OriginalSetting,

            LimitToPages = null,

            PageOrder = PageOrder.OriginalSetting,

            PaperSizeOrientation = PaperSizeOrientation.OriginalSetting,

            PrintArea = PrintArea.OriginalSetting,

            ShowTrackChanges = true,

            TextVisibility = new HashSet<TextVisibility>()

            {

                TextVisibility.RemoveBackgroundFillColors,

                TextVisibility.SetTextColorToBlack

            },

            UnhideHiddenWorksheets = true,

            ZoomLevelPercentage = null,

        },

        WordProcessingOptions = new WordProcessingOptions()

        {

            Include = new HashSet<Include>()

            {

                Include.Comments,

                Include.FieldCodes,

                Include.HiddenText

            },

            PageOrientation = PageOrientation.OriginalSetting,

            ShowTrackChanges = true

        },

        ImagingMethod = ImagingMethod.Native

    };

    try

    {

        return await imagingProfileManager.UpdateAsync(workspaceID, imagingProfileID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when updating an Imaging Profile: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Delete an imaging profile

Use the DeleteAsync() method to remove an imaging profile from Relativity. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging profile.

- imagingProfileID - the Artifact ID of the imaging profile.

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
public async Task ImagingProfileDeleteAsync(Interfaces.V1.IImagingProfileManager imagingProfileManager, int workspaceID, int imagingProfileID)

{

    try

    {

        await imagingProfileManager.DeleteAsync(workspaceID, imagingProfileID).ConfigureAwait(false);

    }

    catch(Exception ex)

    {

        string exception = $"An error occurred when deleting an Imaging Profile: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Imaging Set Manager

To running an imaging job, you need to create an imaging set, which consists of an imaging profile and a search containing the documents to image. The Imaging Set Manager API provides supports create, read, update, and delete operations on imaging sets. It also supports the hide and release operations used for a QC Review of imaged documents. For general information, see Imaging sets and QC Review on the Relativity Server 2025 Documentation site.

Create an imaging set

Use the CreateAsync() method to add a new imaging set to Relativity. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

- ImagingSetCreateRequest object - see the code sample for property settings.

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
public async Task<int> ImagingSetCreateAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int datasourceID, int imagingProfileID)

{

    try

    {

        var request = new ImagingSetCreateRequest

        {

            Name = "All documents",

            DataSourceID = datasourceID,

            EmailNotificationRecipients = "some_person@test.com;some_other_person@test.com",

            ImagingProfileID = imagingProfileID

        };

        return await imagingSetManager.CreateAsync(workspaceID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when creating imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Retrieve an imaging set

Use the ReadAsync() method to retrieve an imaging set. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

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
public async Task<Interfaces.V1.Models.ImagingSet> ImagingSetReadAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int imagingSetID)

{

    try

    {

        return await imagingSetManager.ReadAsync(workspaceID, imagingSetID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when retrieving imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Update an imaging set

Use the UpdateAsync() method to modify an imaging set. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

- ImagingSetUpdateRequest object - see the code sample for property settings.

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
public async Task<int> ImagingSetUpdateAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int imagingSetID, int datasourceID, int imagingProfileID)

{

    try

    {

        var request = new ImagingSetUpdateRequest

        {

            Name = "All documents",

            DataSourceID = datasourceID,

            EmailNotificationRecipients = "some_person@test.com;some_other_person@test.com",

            ImagingProfileID = imagingProfileID

        };

        return await imagingSetManager.UpdateAsync(workspaceID, imagingSetID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when updating imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Delete an imaging set

Use the DeleteAsync() to remove an imaging set from Relativity. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

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
public async Task ImagingSetDeleteAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int imagingSetID)

{

    try

    {

        await imagingSetManager.DeleteAsync(workspaceID, imagingSetID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when deleting imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Hide an imaging set

You can hide images that need to prevent users from viewing images that need to undergo a quality control review. For more information, see QC Review on the Relativity Server 2025 Documentation site.

Call the HideImagingSetAsync() method by passing the following arguments to it:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

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
public async Task ImagingSetHideImagingSetAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int imagingSetID)

{

    try

    {

        await imagingSetManager.HideImagingSetAsync(workspaceID, imagingSetID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when hiding imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Release an imaging set

After a quality control review has been completed on hidden images, you can make them available to reviewers by releasing them.

Call the ReleaseImagingSetAsync() method by passing the following arguments to it:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

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
public async Task ImagingSetReleaseImagingSetAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int imagingSetID)

{

    try

    {

        await imagingSetManager.ReleaseImagingSetAsync(workspaceID, imagingSetID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when releasing imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Retrieve the status of an imaging set

Use the GetStatusAsync() method to retrieve the status of an imaging set. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

When you read an imaging set, its status is also returned. See Retrieve an imaging set .

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
public async Task<Interfaces.V1.DTOs.ImagingSetStatusResponse> ImagingSetGetStatusAsync(Interfaces.V1.IImagingSetManager imagingSetManager, int workspaceID, int imagingSetID)

{

    try

    {

        return await imagingSetManager.GetStatusAsync(workspaceID, imagingSetID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when getting imaging set status: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Native Type Manager

You can retrieve native file types supported by Relativity for imaging. For general information, see Imaging native types on the Relativity Server 2025 Documentation site.

Retrieve a native type

Use the ReadAsync() method to retrieve a native type. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the native type.

- nativeTypeID - the Artifact ID of the native type.

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
public async Task<Interfaces.V1.Models.NativeType> ReadAsyncNativeType(Interfaces.V1.INativeTypeManager nativeTypeManager, int workspaceID, int nativeTypeID)

{

    Interfaces.V1.Models.NativeType nativeType;

    try

    {

        nativeType = await nativeTypeManager.ReadAsync(workspaceID, nativeTypeID).ConfigureAwait(false);

        return nativeType;

    }

    catch(Exception ex)

    {

        string exception = $"An error occurred when reading Native Type: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Application Field Code Manager

Microsoft applications use fields codes as placeholders for data that may be updated or used for other specialized purposes in their documents, such as those created in Word, Excel, or others. In Relativity, application field codes indicate how to handle field codes used in Microsoft documents during imaging. For general information, see Application Field Codes on the Relativity Documentation site.

Use the Application Field Code Manager API to create, read, update, or delete application field codes.

Create an application field code

Use the CreateAsync() method to add a new application field code to Relativity. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace where you want to add the application field code.

- ApplicationFieldCodeRequest object - see the code sample for property settings.

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
public async Task<int> ApplicationFieldCodeCreateAsync(Interfaces.V1.IApplicationFieldCodeManager applicationFieldCodeManager, int workspaceID)

{

    var request = new ApplicationFieldCodeRequest()

    {

        Application = ApplicationType.MicrosoftExcel,

        FieldCode = "Author",

        ImagingProfiles = null,

        Option = ApplicationFieldCodeOption.DocumentDefault,

        RelativityField = null

    };

    try

    {

        return await applicationFieldCodeManager.CreateAsync(workspaceID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when creating an Application Field Code: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Retrieve an application field code

Use the ReadAsync() method to retrieve an application field code. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the application field code.

- applicationFieldCodeID - the Artifact ID of the application field code.

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
public async Task<Interfaces.V1.Models.ApplicationFieldCode> ApplicationFieldCodeReadAsync(Interfaces.V1.IApplicationFieldCodeManager applicationFieldCodeManager, int workspaceID, int applicationFieldCodeID)

{

    Interfaces.V1.Models.ApplicationFieldCode applicationFieldCode;

    try

    {

        applicationFieldCode = await applicationFieldCodeManager.ReadAsync(workspaceID, applicationFieldCodeID).ConfigureAwait(false);

        return applicationFieldCode;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when reading an Application Field Code: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Update an application field code

Use the UpdateAsync() method to modify an application field code. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the application field code.

- applicationFieldCodeID - the Artifact ID of the application field code.

- ApplicationFieldCodeRequest object - see the code sample for property settings.

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
public async Task<int> ApplicationFieldCodeUpdateAsync(Interfaces.V1.IApplicationFieldCodeManager applicationFieldCodeManager, int workspaceID, int applicationFieldCodeID)

{

    var request = new ApplicationFieldCodeRequest()

    {

        Application = ApplicationType.MicrosoftExcel,

        FieldCode = "Author",

        ImagingProfiles = null,

        Option = ApplicationFieldCodeOption.DocumentDefault,

        RelativityField =null

    };

    try

    {

        return await applicationFieldCodeManager.UpdateAsync(workspaceID, applicationFieldCodeID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when updating an Application Field Code: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Delete an application field code

Use the DeleteAsync() method to remove an application field code from Relativity. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the application field code.

- applicationFieldCodeID - the Artifact ID of the application field code.

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
public async Task ApplicationFieldCodeDeleteAsync(Interfaces.V1.IApplicationFieldCodeManager applicationFieldCodeManager, int workspaceID, int applicationFieldCodeID)

{

    try

    {

        await applicationFieldCodeManager.DeleteAsync(workspaceID, applicationFieldCodeID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when deleting an Application Field Code: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Imaging Job Manager

Use the Imaging Job Manager API to run jobs to image documents, cancel a job currently executing on an imaging set, or retry errors that occurred during a job. For general information, see Running an imaging set and Imaging errors on the Relativity Server 2025 Documentation site.

Run an imaging set job

Use the RunImagingSetAsync() method to schedule an imaging set job. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging set.

- imagingSetID - the Artifact ID of the imaging set.

- ImagingSetRequest object - see the code sample for property settings.

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
public async Task<Interfaces.V1.DTOs.ImagingSetResponse> ImagingJobRunImagingSetAsync(Interfaces.V1.IImagingJobManager imagingJobManager, int workspaceID, int imagingSetID)

{

    try

    {

        var request = new ImagingSetRequest

        {

            OriginationID = Guid.NewGuid(),

            QcEnabled = false

        };

        return await imagingJobManager.RunImagingSetAsync(workspaceID, imagingSetID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when running imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Submit an imaging job for a single document

Use the ImageDocumentAsync() method to submit an imaging job for a single document, specified by an image on the fly request. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging job.

- documentArtifactID - the Artifact ID of the document for imaging.

- ImageOnTheFlyRequest object - see the code sample for property settings. You can image a native file stored in Relativity or you can use the AlternateNativeLocation property to specify an alternative native file by providing a file path for it.

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
public async Task<Interfaces.V1.DTOs.ImageOnTheFlyResponse> ImagingJobImageDocumentAsync(Interfaces.V1.IImagingJobManager imagingJobManager, int workspaceID, int documentArtifactID, int imagingProfileID)

{

    try

    {

        var request = new Interfaces.V1.DTOs.ImageOnTheFlyRequest

        {

            OriginationID = Guid.NewGuid(),

            AlternateNativeLocation = null,

            ProfileID = imagingProfileID,

            RemoveAlternateNativeAfterImaging = false

        };

        return await imagingJobManager.ImageDocumentAsync(workspaceID, documentArtifactID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when imaging a document: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Submit a mass imaging job

Use the MassImageDocumentsByMassProcessIdAsync() method to submit a mass imaging job. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging job.

- MassImageRequest object - see the code sample for property settings.

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
public async Task<Interfaces.V1.DTOs.MassImagingResponse> ImagingJobMassImageAsync(Interfaces.V1.IImagingJobManager imagingJobManager, int workspaceID, string massProcessID, int imagingProfileID)

{

    try

    {

        var request = new Interfaces.V1.DTOs.MassImageRequest

        {

            OriginationID = Guid.NewGuid(),

            MassProcessID = massProcessID,

            ProfileID = imagingProfileID,

            SourceType = SourceType.Native

        };

        return await imagingJobManager.MassImageDocumentsByMassProcessIdAsync(workspaceID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when mass image: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Cancel an imaging job

Use the StopImagingJobAsync() method to stop in-progress imaging jobs, including jobs for imaging sets and image on the fly. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging job.

- imagingJobID - the Artifact ID of the imaging job.

- StopImagingJobRequest object

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
public async Task<Interfaces.V1.DTOs.StopImagingJobResponse> ImagingJobStopImagingJobAsync(Interfaces.V1.IImagingJobManager imagingJobManager, int workspaceID, int imagingJobID)

{

    try

    {

        var request = new Interfaces.V1.DTOs.StopImagingJobRequest();

        return await imagingJobManager.StopImagingJobAsync(workspaceID, imagingJobID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when stopping imaging job: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Retry imaging set errors

Use the RetryImagingSetErrorsAsync() method to retry imaging set errors. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging job.

- imagingSetID - the Artifact ID of the imaging set.

- ImagingSetRequest object - see the code sample for property settings.

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
public async Task<Interfaces.V1.DTOs.ImagingSetResponse> ImagingJobRetryImagingSetErrorsAsync(Interfaces.V1.IImagingJobManager imagingJobManager, int workspaceID, int imagingSetID)

{

    try

    {

        var request = new ImagingSetRequest

        {

            OriginationID = Guid.NewGuid(),

            QcEnabled = false

        };

        return await imagingJobManager.RetryImagingSetErrorsAsync(workspaceID, imagingSetID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when retrying imaging set: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Update the priority of an imaging job

Use the UpdateJobPriorityAsync() method to update an imaging job priority. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the imaging job.

- imagingJobID - the Artifact ID of the imaging job.

- UpdateJobPriorityRequest object - set the Priority property to an integer value representing the new priority to assign to the job.

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
public async Task<Interfaces.V1.DTOs.UpdateJobPriorityResponse> ImagingJobUpdateJobPriorityAsync(Interfaces.V1.IImagingJobManager imagingJobManager, int workspaceID,  int imagingJobID)

{

    try

    {

        var request = new Interfaces.V1.DTOs.UpdateJobPriorityRequest

        {

            OriginationID = Guid.NewGuid(),

            Priority = 99

        };

        return await imagingJobManager.UpdateJobPriorityAsync(workspaceID, imagingJobID, request).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when updating imaging job priority: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Document Status Manager

Use the method on the Document Status Manager API to obtain status information about the imaging job for a document.

Retrieve imaging status of a document

Use the GetStatusAsync() method to retrieve the imaging status of a document. Pass the Artifact ID of the workspace and document to this method. It returns information about whether the document has images, the number of images, and errors or warnings associated with the document.

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
public async Task<DocumentStatusResponse> DocumentGetStatusAsync(Interfaces.V1.IDocumentStatusManager statusManager, int workspaceID, int documentID)

{

    try

    {

        return await statusManager.GetStatusAsync(workspaceID, documentID).ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when getting document Image status: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Imaging Environment Manager

Use the methods on the Imaging Environment Manager API to remove inactive jobs and to obtain the size of mass imaging jobs.

Remove inactive imaging jobs

Use the CleanupInactiveJobsAsync() method to cleans up inactive imaging jobs.

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
public async Task CleanUpInactiveJobAsync(Interfaces.V1.IImagingEnvironmentManager imagingEnvironmentManager)

{

    try

    {

        await imagingEnvironmentManager.CleanupInactiveJobsAsync().ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when cleaning up inactive Imaging jobs: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

Retrieve the size of a mass imaging job

Use the GetMaxMassImagingJobSizeAsync() to retrieve the size of a mass imaging job. It returns an integer indicating the number of documents in the imaging job.

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
public async Task<int> RetrieveMassImagingMaxJobSize(Interfaces.V1.IImagingEnvironmentManager imagingEnvironmentManager)

{

    try

    {

        return await imagingEnvironmentManager.GetMaxMassImagingJobSizeAsync().ConfigureAwait(false);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred when retrieving Mass Imaging max job size: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```
