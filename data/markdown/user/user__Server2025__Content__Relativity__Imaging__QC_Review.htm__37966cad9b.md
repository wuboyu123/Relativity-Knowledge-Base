---
title: "QC Review"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/QC_Review.htm
collection: user
fetched_at: 2026-06-22T06:14:17+00:00
sha256: ec8955e4ea6cc38eede10bc2e725dc295cd7f791686b4aba9bb39036bb485713
---

QC Review

# QC Review

Using QC Review you can prevent users from viewing or editing images in an Imaging Set until a QC reviewer has a chance to review the images. The QC reviewer has access to the images, but the images are hidden from other groups until you release them. A permission setting in the Admin Operations section of the Workspace Details tab determines whether or not members of a particular group are able to view images held for QC Review. If a user without sufficient permissions views a document in an Imaging Set that is held for QC Review, the Image radio button is unavailable in the Viewer until you release the Imaging Set.

Sometimes it's necessary to have one team of professionals perform a preliminary review of the images in a particular data set before releasing the images to a larger group of reviewers. With QC Review you can restrict access to a collection of images from one group, while another group performs quality checks. When the QC review process is complete, you can release the images to other groups to view.

QC Review of Imaging Sets that contain large volumes of documents can be optimized with Random Sampling. See Sampling for more information.

## Hiding images for QC

The suggested workflow for the QC Review feature is as follows:

- Click the Imaging Set tab.

- Select an Imaging Set.

- Click Image Documents .

- An option to Hide Images appears. Selecting this checkbox prevents all users without sufficient permissions from viewing the document images in that particular Imaging Set.

- Click OK .

The ImageQCOnByDefault instance setting value makes this checkbox default to checked.

All images in that Imaging Set are only viewable by users whose groups have the permission to View Images Hidden for QC Review . Apply this permission to any group from the Workspace Details tab.

## Releasing images

When the QC review process is complete use the following steps to grant other groups to access the images of all documents associated with that Imaging Set.

- Click the Imaging Set tab.

- Select the Imaging Set.

- Click the Release Images button. A Release Images Confirmation window prompts you to confirm your intention to release all images in this Imaging Set.

- Click OK .

If the documents in the Imaging Set you want held for QC Review already have images:

- Click the Imaging Set tab.

- Select an Imaging Set.

- Click the Hide Images button in the QC Review section of the Imaging Set.

### QC Review fields

If you image a document in more than one Imaging Set, the Imaging Set system field lists the most recent Imaging Set. The following two fields are relevant to QC Review:

- Image QC Status - this choice field defines whether or not the image for the document is Hidden for QC . The value is null if it is not hidden.

- Imaging Set - this field displays the most recent Imaging Set associated with that document. If the document's image originates from outside of Relativity or with Image on the fly functionality, this field is null.

### Image QC Review Status

- Documents set to hidden - displays the number of images hidden during the imaging process.

- Documents viewable - displays the number of documents with viewable images.
