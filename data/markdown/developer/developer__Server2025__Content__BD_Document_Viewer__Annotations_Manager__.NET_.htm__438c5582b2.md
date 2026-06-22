---
title: "Annotations Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Annotations_Manager__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:22:34+00:00
sha256: 1d324512ee801e0459bed148e72673f31d20e6d3327b9bb598db4f8ec2f89e0a
---

Annotations Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Annotations Manager (.NET)

In Relativity, markups refer to redactions and highlights that you can add to document images as part of the review process in the Image Viewer. A redaction obscures confidential content in an image, while a highlight visually emphasizes content. You can define the colors and styles used to add markups to a document image. For more information, see ImageViewer and Markups in the Relativity Documentation site.

The Annotations Manager API exposes functionality for programmatically redacting and highlighting document images. It contains methods for creating, updating, retrieving, and deleting redactions and highlights.

As a sample use case, you might use this API in application that provides custom functionality for adding redactions or highlights to document images. You might include the ability to delete multiple redactions in a single operation.

You can also use the Annotations Manager API through REST. For more information, see Annotations Manager (REST) .

The following content uses the term annotations to reference redactions or highlights added to document images through the Image Viewer.

## Fundamentals for the Annotations Manager API

Review the following information to learn about the methods and classes used by the Annotations Manager API.

Methods

The Annotations Manager API includes the following methods available on the IAnnotationServiceManager interface in the Relativity.DocumentViewer.Services.Versioned.<VersionNumber> namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- Delete() method - removes annotations from a document image. See Delete annotations from a document .

- Get() method - retrieves annotations on a specific document image. See Retrieve annotations on a document .

- Save() method - adds annotations to a document image or updates them. See Create or update annotations .

Classes

The Annotations Manager API uses the following key classes:

- Annotation class - represents an annotation on a document image. It contains the following properties:

- BorderA - an integer representing the degree of transparency for the border color. This property can be null.

- BorderB - an integer representing blue in the RGB color model for the border. This property can be null.

- BorderG - an integer representing green in the RGB color model for the border. This property can be null.

- BorderR - an integer representing red in the RGB color model for the border. This property can be null.

- BorderSize - an integer representing the width of the border in pixels. This property can be null.

- BorderStyle - an integer representing the style of the border. This property can be null.

- DocumentArtifactID - the Artifact ID of the document.

- DrawCrossLines - a Boolean value indicating whether cross lines should be drawn.

- FillA - an integer representing the degree of transparency for the fill color. This property can be null.

- FillB - an integer representing blue in the RGB color model for the fill. This property can be null.

- FillG - an integer representing green in the RGB color model for the fill. This property can be null.

- FillR - an integer representing red in the RGB color model for the fill. This property can be null.

- FontA - an integer representing the degree of transparency for the font color. This property can be null.

- FontB - an integer representing blue in the RGB color model for the font. This property can be null.

- FontG - an integer representing green in the RGB color model for the font. This property can be null.

- FontR - an integer representing red in the RGB color model for the font. This property can be null.

- FontName - a string representing the name of the font.

- FontStyle - an integer representing the font style. This property can be null.

- FontSize - an integer indicating the font size in points. This property can be null.

- Guid - a string representing a GUID identifying the image.

- Height - an integer representing the height of a redaction in pixels.

- ID - integer IDs representing an annotation.

- ImageHeight - an integer indicating the image height in pixels.

- ImageWidth - an integer indicating the image width in pixels.

- PageHeight - an integer representing the page height in the Image Viewer.

- PageNumber - an integer representing the page number of a specific document image.

- PageWidth -an integer representing the page width in the Image Viewer.

- MarkupSetArtifactID - the Artifact ID of the markup set used to draw the annotations.

- MarkupSubType - an integer representing the subtype of the markup.

- MarkupType - an integer representing the type of markup.

- ModifiedBy - the Artifact ID for the user who last updated the annotation.

- Text - a string representing any text added to the annotation.

- ValuesAreScaledToDB - a Boolean value indicating whether values are scaled to the database.

- Width - an integer representing the width of a redaction in pixels.

- WorkspaceID - the Artifact ID of the workspace containing the image.

- X - a decimal representing the x-coordinate of the annotation.

- Y - a decimal representing the y-coordinate of the annotation.

- ZOrder - an integer representing the order of overlapping two-dimensional objects.

- SaveAnnotationsReturnObject class - represents the object returned by the Save() method used when creating or updating an annotation on a document.

- AnnotationIDs - an array of integer IDs representing the annotations that were added or updated on a document.

- CustomErrorMessage - a string containing an error message returned when the create or update operation for an annotation fails.

- ErrorCode - a string representing the error code returned when the create or update operation for an annotation fails.

- Success - a Boolean value indicating whether the annotation was created or updated without errors.

## Create or update annotations

Use the Save() method to add annotations to a document image or to update existing ones. Pass the following arguments to this method:

- workspaceId - the Artifact ID of the workspace containing the document image with annotations.

- annotation - an array of Annotation objects. For a list of properties, see Classes .

When updating an annotation, set the ID property on each Annotation object in the array.

View code sample for creating annotations Copy

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
public async Task<SaveAnnotationsReturnObject> Create(int workspaceId, int documentId, int markupsetId, string imageFileName)

{

    // Arrange

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IDocumentFileManager documentFileManager = serviceFactory.CreateProxy<IDocumentFileManager>())

    {

        List<DocumentFile> documentFiles = await documentFileManager.GetFileInfoAsync(workspaceId, documentId);

        string imageFileGuid = documentFiles.First(x => x.Filename.Equals(imageFileName)).Guid.ToString();

        var annotation = new Annotation

        {

            X= 502.9745m,

            Y= 212.0057m,

            Width= 150.00000000000006m,

            Height= 208,

            MarkupType= 2,

            MarkupSubType= 9,

            DrawCrossLines= false,

            FillA= 0,

            FillR= 255,

            FillG= 165,

            FillB= 0,

            BorderStyle= 1,

            BorderSize= 1,

            Guid= imageFileGuid,

            PageNumber= 0,

            PageHeight= 1056,

            PageWidth= 816,

            ImageHeight= 3300,

            ImageWidth= 2550,

            WorkspaceID= workspaceId,

            DocumentArtifactID= documentId,

            MarkupSetArtifactID= markupsetId

        };

        using (IAnnotationServiceManager annotationService = serviceFactory.CreateProxy<IAnnotationServiceManager>())

        {

            SaveAnnotationsReturnObject retVal = await annotationService.Save(workspaceId, new Annotation[] { annotation });

            return retVal;

        }

    }

}
```

View code sample for updating annotations

Make sure that you set the ID property on each Annotation object when performing an update operation.

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
public async Task<SaveAnnotationsReturnObject> Update(int workspaceId, int documentId, int markupsetId, string imageFileName)

{

    // Arrange

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IDocumentFileManager documentFileManager = serviceFactory.CreateProxy<IDocumentFileManager>())

    {

        List<DocumentFile> documentFiles = await documentFileManager.GetFileInfoAsync(workspaceId, documentId);

        string imageFileGuid = documentFiles.First(x => x.Filename.Equals(imageFileName)).Guid.ToString();

        var annotation = new Annotation

        {

            ID = 1,

            X= 502.9745m,

            Y= 212.0057m,

            Width= 150.00000000000006m,

            Height= 208,

            MarkupType= 2,

            MarkupSubType= 9,

            DrawCrossLines= false,

            FillA= 0,

            FillR= 255,

            FillG= 165,

            FillB= 0,

            BorderStyle= 1,

            BorderSize= 1,

            Guid= imageFileGuid,

            PageNumber= 0,

            PageHeight= 1056,

            PageWidth= 816,

            ImageHeight= 3300,

            ImageWidth= 2550,

            WorkspaceID= workspaceId,

            DocumentArtifactID= documentId,

            MarkupSetArtifactID= markupsetId

        };

        using (IAnnotationServiceManager annotationService = serviceFactory.CreateProxy<IAnnotationServiceManager>())

        {

            SaveAnnotationsReturnObject retVal = await annotationService.Save(workspaceId, new Annotation[] { annotation });

            return retVal;

        }

    }

}
```

## Retrieve annotations on a document

Use the Get() method to retrieve a list of annotations on a document image. Pass the following arguments to this method:

- workspaceId - the Artifact ID of the workspace containing the document image with annotations.

- documentId - the Artifact ID of the document image with annotations.

- markupSetId - the Artifact ID of the markup set used to add the annotations.

View code sample Copy

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
public async Task<Dictionary<string, AnnotationList>> Get(int workspaceId, int documentId, int markupSetId)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IAnnotationServiceManager annotationService = serviceFactory.CreateProxy<IAnnotationServiceManager>())

    {

        Dictionary<string, AnnotationList> docAnnotations = await annotationService.Get(workspaceId, documentId, markupSetId);

        return docAnnotations;

    }

}
```

## Delete annotations from a document

Use the Delete() method to remove annotations on a document. Pass the following arguments to this method:

- workspaceId - the Artifact ID of the workspace containing the document image with annotations.

- annotationIds - an array of integer IDs representing the annotations on the document image.

- documentId - the Artifact ID of the document image with annotations.

- markupSetId - the Artifact ID of the markup set used to add the annotations.

View code sample Copy

```text
1
2
3
4
5
6
7
8
public async Task Delete(int workspaceId, int documentId, int markupSetId, int[] annotationIds)

{

    ServiceFactory serviceFactory = GetServiceFactorySettings();

    using (IAnnotationServiceManager annotationService = serviceFactory.CreateProxy<IAnnotationServiceManager>())

    {

        await annotationService.Delete(workspaceId, annotationIds, documentId, markupSetId);

    }

}
```

On this page

- Annotations Manager (.NET)

- Fundamentals for the Annotations Manager API

- Create or update annotations

- Retrieve annotations on a document

- Delete annotations from a document


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
