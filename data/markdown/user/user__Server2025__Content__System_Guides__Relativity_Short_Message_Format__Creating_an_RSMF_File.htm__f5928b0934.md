---
title: "Creating an RSMF file"
url: https://help.relativity.com/Server2025/Content/System_Guides/Relativity_Short_Message_Format/Creating_an_RSMF_File.htm
collection: user
fetched_at: 2026-06-22T06:16:26+00:00
sha256: 001515b6018f9c57356e073adcb458683be44f12de2d65b04716dc11857d1719
---

Creating an RSMF file

# Creating an RSMF file

To use the Short Message Viewer, you will need to create an RSMF file and Relativity 10.3 or above. RSMF is an agnostic chat platform data format which means that as long as a platform's functionality contains messaging capabilities, it will likely be supported in RSMF. Over 40 different chat platforms’ data have been transformed and reviewed in RSMF. Examples of chat data that have been supported in RSMF include, but are not limited to: Slack, Microsoft Teams, Text messages (MMS, SMS, iMessage, Whatsapp), Google Chat, Bloomberg Chat, Instagram, and more.

There are two methods you can use to create an RSMF file. Each method and some resources that provide additional information are provided below.

- To build an RSMF file, use the following developer resources.

- How to build RSMF files

- How to validate RSMF files

- Example file

-

Don’t have a development resource, or a source that exports RSMF? Find partners that offer tailored conversion to RSMF.

- Relativity App Hub

## RSMF file support in Processing

In addition to being RFC 5322 compliant, an RSMF file must meet the following conditions before you can bring it into Relativity using Processing:

- It must have a .rsmf extension.

- It must have an <X-RSMF-Version> header field that defines the version of the RSMF spec that the file conforms to.

- It must have exactly one attachment with a Content-Transfer-Encoding header type of base64 (RFC 2045) and a Content-Disposition header of type attachment with a parameter filename equal to "rsmf.zip" (RFC 6266). See the rsmf.zip section for more details.

Relativity Short Message Format also supports a number of optional headers that provide roll-up of short message data contained within the file. To view the full list of supported headers, see Relativity's short message format .

To learn more about which fields are processed and mapped into Relativity, visit Processing an RSMF file .

## RSMF file creation process

Before you begin the file creation process, the following resources may be useful to reference:

- Relativity has developed an RSMF library which allows you to optionally validate RSMF files and ensure they will work in Relativity before ingestion. This library is available via nuget . Documentation for the library is part of the nuget package.

- Relativity has also provided sample code demonstrating how to use the library. This code can be found by visiting the Relativity Validator Library GitHub page . The schema for rsmf_manifest.json file is also located in this repository. A tool such as Newtonsoft JSON can be used to generate the rsmf_manifest.json file.

To create an RSMF file, perform the following steps:

- Retrieve short message data from its source. For instance, you can use a mobile collection solution to extract data from a mobile device or an API to retrieve data from a messaging platform.

We recommend that an RSMF file should have no more than 10,000 events to ensure high performance in Relativity.

-

Group by participants and timeframes in the data.

- The most common way we recommend you generate RSMF files is to first group messages by like participants, then group those messages by time period. You will then be able to review one conversation in standard time periods.

- For example, if you have a conversation between two participants over two years and the volume of messages is somewhat low, we recommend grouping all of those messages together, then creating RSMF files each grouped by day. While also respecting the 10,000 message recommended cap per RSMF file.

- Once the data is selected, you will need to create an rsmf_manifest.json file. To learn more about this file type, visit rsmf_manifest.json .

- Ensure that the manifest file includes references to any avatars and/or attachments from the data source to make sure they have full functionality in Relativity. To learn more about attachment and avatar support, visit RSMF-supported Emoji Emoticons and Attachments .

- Once the rsmf_manifest.json file has been created, you should create a new folder and place the manifest file within it. Then, add any avatars and/or attachments that were referenced within manifest.json into that folder.

- Create a zip of the folder (which includes the rsmf_manifest.json and all the avatars/attachments) and name the file rsmf.zip. For additional information about the rsmf.zip file, visit Relativity Short Message Format .

- Create the RSMF file using the zip file created in the previous step. We recommend doing the following when creating the RSMF file:

-

Add text to the Body of the RSMF file. Relativity Processing will extract the Body and automatically map it to the Extracted Text field when you publish.

-

Add one participant to the FROM header of the RSMF file. Relativity Processing will extract the data and make it available to map when you publish. This is a requirement if you want to run name normalization against the RSMF file.

Optionally, if you include information in the Body section of the RSMF file, this will display in the Extracted Text mode of the Short Message Viewer .

Once the RSMF file has been created, you can then import it into Relativity and ingest it into your workspace through Relativity Processing. To learn more, visit Processing an RSMF file .

Relativity provides a validation tool that you can use to validate the RSMF file before importing it into Relativity. To learn more about the validation tool, visit Validation library and rsmf_manifest.json schema availability .
