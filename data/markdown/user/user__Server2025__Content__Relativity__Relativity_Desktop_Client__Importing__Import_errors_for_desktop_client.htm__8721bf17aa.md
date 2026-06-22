---
title: "Import errors for Desktop Client"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Importing/Import_errors_for_desktop_client.htm
collection: user
fetched_at: 2026-06-22T06:14:50+00:00
sha256: fee6bf64363b90468343a7adccbb0f62fa3d533d0f5d65d6317ae6d29d51215f
---

Import errors for Desktop Client Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Import errors for Desktop Client

When an item-level error occurs in a load file, Relativity Desktop Client uses the proper delimiter automatically so that when users access the load file, they will not experience the error.

The following table lists the most common import errors found in the Relativity Desktop Client, including their messages and fixes.

Message Fix

Invalid date. Change the date information to one of the standard date formats.

Invalid boolean. Change data to a YES or NO format.

Invalid decimal. Change the data to a valid number.

Invalid integer. Change the data to an integer.

Input length exceeds maximum set length of <max length> for this VarChar field. Increase the character restriction on the field.

Input length exceeds maximum set length of <max length> for the associated object field <name>. Increase the character size of associated object.

Error uploading file. Skipping line. Verify and correct line information.

File upload failed. Either the access to the path is denied or there is no disk space available. Verify disk space is available and check permissions on data server.

File '<file name>' not found.

Verify the file is available in path provided.

File '<file name>' contains 0 bytes. No data exists in the file.

Identifier Value not set. The Overlay Identifier field has not been mapped. Map the Overlay Identifier field.

Choice name specified twice for this record. Two choice name fields are titled identically. Each choice name should be unique from all others in the load file.

Proposed choice name exceeds 200 characters. Rename the specified choice to something less than 200 characters.

User does not exist in the system or is not available for assignment. Email used in the entity file is not associated with any entity in the system.

Document has been previously processed in this file Same ID trying to load twice.

Error: full text file specified does not exist. Verify the path of extracted text file.

There are an invalid number of cells in this row - expecting:<expected>, actual:<actual>. Remove the extra column delimiter from load file.

- This document identifier does not exist in the system - no document to overwrite Overlay unavailable. You must append the data.

A document with identifier <document identifier> already exists in the system The identifier field already exists in the system. You need to do an overlay to overwrite the existing data.

This file identifier exists attached to another document with selected key field {0} Same ID trying to load twice.

This file identifier exists attached to another document with selected ArtifactID {0} Same ID trying to load twice.

This file identifier exists attached to another document Duplicate page ID in a different document.

Document is already in the selected production

The Bates number is already loaded.

Because you can't overlay into an existing production, you must create a new production or replace the images manually on the back end.

This document contains redactions or highlights that can't be overwritten Delete the markups.

There is no image specified on this line Make sure image id is present in load file.

One of the files specified for this document does not exist Make sure image files are present for represented path.

The image file specified is not a supported format in Relativity This can't be loaded without conversion to an approved format.

The file being uploaded is empty No data exists in the file so it can't be loaded.

The identifier field for this row is either empty or unmapped Verify that an identifier exists.

The identifier specified on this line has been previously specified in the file Make sure the identifier field is unique or overlay data.

The document specified has been secured for editing. Change security permissions to allow document edit rights.

Your account does not have rights to add a document or object to this case Change security permissions to allow document add rights.

A non-unique associated object is specified for this new object. Two objects with the same name exist in the workspace. Identify the duplicates and change one of their names.

Your account does not have rights to add an associated object to the current object. Change security permissions to allow updates to object.

An object field references a child object which does not exist. Add a child object.

This record's Overlay Identifier is shared by multiple documents in the case, and cannot be imported. Use a unique ID to overlay the data

On this page

- Import errors for Desktop Client


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
