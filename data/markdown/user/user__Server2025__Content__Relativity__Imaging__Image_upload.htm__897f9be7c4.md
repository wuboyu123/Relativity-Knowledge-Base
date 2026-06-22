---
title: "Image upload"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Image_upload.htm
collection: user
fetched_at: 2026-06-22T06:14:08+00:00
sha256: 4f8f35b30afbdcc84133fbb1c79b07d26ffe1aa03c820f40a3e5630610559320
---

Image upload Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Image upload

Use Relativity's image upload feature to open a file in the viewer and upload a single image for that record without having to use the RDC to create a load file to re-import the image.

You can manage review and productions more efficiently by reducing the number of steps involved and avoiding some of the errors that were previously common when importing an image.

With this feature, you're able to upload the following file types:

- GroupIV TIFF

- JPEG

- PDF

## Required security permissions

To use the image upload feature, you must have the following permissions enabled in the Object Security console:

- Upload Image

- Add Image

- Delete Image

You need to install the Imaging Request and Imaging Response agents in order to perform image on the fly, run an imaging set, or execute a mass imaging operation. The maximum recommend amount of Imaging Response agents is 8, any more can cause database issues. The standard configuration is 4, for details on installation and activation of these agents, see Imaging .

## Uploading an image

To upload an image for a file in the viewer, click the file name and select Upload images for this document . In the menu, select the imaging profile you want to upload the image with. For more information see, Imaging profiles .

If an image already exists for a document, you can replace it by clicking the document name and selecting Replace images fore this document . In the menu, select the imaging profile you want to upload the new image with. Replacing the image with a supported image type replaces the entire image not just a single page of an image. For example, if you have a 5 page document, but you upload a JPG or TIFF file, you will have 1 image. If you upload a 5 page PDF file, then 5 images will upload.

Once you choose an image profile after selecting Upload images for this document or Replace images for this document, the upload/replace image window will appear. Select click to select a file to open the folder containing the image you want to upload. You can also drag a single file from your local machine and drop it into the upload window.

Once you select the file in the folder, Relativity automatically begins to upload it. When the upload is successful, the image is visible in the viewer.

If you've redacted or added highlights to an image in the viewer and then you attempt to upload a new image, you'll receive a message informing you that you're about to remove those redactions or highlights when you replace the image. Note that replacing an image with redactions will update the Has Redactions field for that file to No and remove all existing redactions and markup.

If you attempt to upload an unsupported file type, you'll receive an error message.

From here, you can click Upload New Image to select a new image to upload.

## Audits for image upload

The following actions are available in Relativity to assist in identifying how the logged-in user has been using image upload.

- Images - Created - indicates that the logged in user generated an image in the viewer.

- Images - Deleted - indicates that the logged-in user deleted an image from the viewer.

On this page

- Image upload

- Required security permissions

- Uploading an image

- Audits for image upload


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


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
