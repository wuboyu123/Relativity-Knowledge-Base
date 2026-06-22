---
title: "Mass image"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Mass_image.htm
collection: user
fetched_at: 2026-06-22T06:15:50+00:00
sha256: 8890542078d1ee5fd8580ccb693d0bd771b3878706245510e6d4e673c43a74e3
---

Mass image Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Mass image

Mass imaging creates TIFF or JPEG images for a document set based on the settings in the imaging profile you select. Relativity also provides a default imaging profile that you can use out-of-the-box. You can customize profiles to create color JPEG images, adjust image size, and leverage other formatting options. Mass image is available from the mass operations bar.

The mass image operation uses the same technology as the Relativity native file viewer.

The mass image operation is disabled if the Imaging application isn't installed.

To perform a mass image operation, perform the following steps:

You can't use mass operations on Data Grid-enabled fields.

- From the mass operations bar on the document list, choose whether to image Checked items or All items in the current returned set.

The maximum number of documents you can select at one time for the mass image action is 10,000 documents. If the number of documents selected exceeds this value, a warning appears and prevents the job from running. If you want to image more than 10,000 documents, create and run an imaging set. See Imaging sets and Running an imaging set .

- Select Image in the drop-down menu.

The Image Documents pop-up displays.

-

Select a Source Type .

- Select an option in the Imaging Profile drop-down menu. Only profiles that you have permissions to use appear. You can also use the Default profile for the imaging job.

-

Click OK to create the images. Depending on the number of documents you submit, this may take some time. Image-on-the-fly jobs take precedence over batch image jobs.

The default priority for all image jobs is determined by the current value of the ImagingJobPriorityDefault entry in the Instance setting table.

If any of the documents you selected to image is of a type that is included in the Restricted Native Types object on the imaging profile you selected for the mass image job, that document can't be imaged and you receive a corresponding error message.

On this page

- Mass image


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
