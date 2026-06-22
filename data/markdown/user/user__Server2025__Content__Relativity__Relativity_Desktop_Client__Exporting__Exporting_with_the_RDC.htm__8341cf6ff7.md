---
title: "Exporting"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Exporting/Exporting_with_the_RDC.htm
collection: user
fetched_at: 2026-06-22T06:08:49+00:00
sha256: bcb2ecd9afdfff9dd6be74a49c7be8091ff913dda87d972f8cb7c708c0b93e99
---

Exporting

# Exporting with the RDC

You can use the Relativity Desktop Client (RDC) to export production sets, saved search results, and folders. When you perform an export, the RDC automatically creates top-level folders for images, text, and natives. The RDC exports all documents included in the production set, search result, or folder.

You need to install the RDC on your computer before you can perform an export.

See the following related pages:

- Exporting a production set

- Exporting a saved search

- Exporting a folder

- Exporting a folder and its subfolders

## Exporting RDC Permissions

The following permissions are required to use the exporting feature in Relativity Desktop Client:

Object Security Admin Operations

-

Document: Local Access (Download, Copy Text)

This is required when exporting long-text cells greater than the value defined by the MaximumLongTextSizeForExportInCell instance setting, the default value of which is 1048576.

-

Allow Export

## Technical considerations for .kwx files

Note the following:

- .kwx stands for kCura Win edds eXport.

- The .kwx file you call on when you load export settings is a SOAP-serialized file used to run the export.

- SOAP is a protocol based on XML. It's designed specifically to transport or store procedure calls using XML. It does this by converting fields and properties of an object into the serial format of an XML stream.

- When you run an export, the RDC collects all the inputs from the form into an object in memory. The RDC also passes the object on to the export process.

- When you save an export settings object, Relativity passes that object in memory to a SOAP serializer. The SOAP serializer writes that object’s settings to XML.

- When you load export settings, Relativity takes a serialized object and deserializes it to an in-memory settings object. Then it loops over all the properties and sets the actual form values to reflect those settings.
