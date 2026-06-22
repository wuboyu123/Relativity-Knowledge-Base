---
title: "Importing data into a Relativity Dynamic Object"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Importing/Importing_data_into_a_Relativity_Dynamic_Object.htm
collection: user
fetched_at: 2026-06-22T06:14:48+00:00
sha256: c0d80cf73bfbd9c8f6516d509acec2fd4ec39dd0b3e3338561d105c90b5f2c39
---

Importing data into a Relativity Dynamic Object Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Importing data into a Relativity Dynamic Object

You can import data into Relativity Dynamic Objects for use in Relativity applications. Dynamic object data imports follow the same general guidelines as document data imports. Before importing data into a dynamic object:

- Create the application and all necessary objects in Relativity. For an example of a Relativity application, see Building Media Tracker with Relativity Dynamic Objects.

- Create the data file. The file must be properly delimited (for example, a comma-delimited CSV file as shown in the example below) and meet the standards for Relativity data imports. See Load file specifications for more information.

```text
Media Received ID,Received From,Received On,Type,Letter From,Letter Date,Letter Title
LET1,Laura Crowne,12/23/2013,summons,Tuchman,12/31/2013,Regarding the Simpson Case
LET2,Earle Byrd,11/30/2013,brief,Tuchman,12/31/2013,The Simpsons Matter
LET3,Earle Byrd,10/31/2013,summons,Tuchman,12/31/2013,Regarding the Simpson Case
LET4,Earle Byrd,9/29/2013,brief,Tuchman,12/31/2013,The Simpsons Matter
LET5,Earle Byrd,12/31/2013,summons,Tuchman,12/31/2013,Regarding the Simpson Case
LET6,Laura Crowne,12/23/2013,summons,Tuchman ,12/31/2013,The Simpsons Matter
LET7,James Jones,11/30/2013,brief,Marsch,12/31/2013,The Simpsons Matter
LET8,James Jones,10/31/2013,brief,Tuchman,12/31/2013,The Simpsons Matter
LET9,James Jones,9/29/2013,summons,Tuchman,12/31/2013,The Simpsons Matter
```

## Importing RDC Permissions

The following permissions are required to use the importing feature in Relativity Desktop Client:

Object Security Tab Visibility Admin Operations

-

Document: View, Add, Edit

-

Documents

-

Allow Import

## Importing data into the Media Received object

The following example illustrates how to import data into the Media Received object associated with the Media Tracker application:

- Open the RDC and select a workspace.

- Select the Media Received object type.

- On the Tools menu, point to Import and click Media Received Load File . The Import Media Received Load File dialog appears.

- On the Load File tab, click to browse for a document load file. Next, set the other options as necessary.

- Click the Field Map tab. To automatically map fields, click Auto Map Fields . The fields from the load file are mapped to any existing fields of the same name in the workspace.

-

Only fields matched in the center columns are loaded into the workspace. Other fields in the Workspace Fields and Load File Fields lists are ignored. You must always match the identifier field for the load file.

Consider the following when auto-mapping fields:

- Case isn't taken into account for the mapping. For example, a field named "email" in the load file would map to a field named "Email" in the workspace.

- Spacing is taken into account. For example, in a two-word field name, if there is one space between words in the workspace field, and two spaces between words in the load file field, the fields will not be mapped.

- Characters are mapped only to themselves. For example, an underscore is only mapped to another underscore, not to a space.

You can also manually map fields in the load file to existing fields in the workspace.

To manually map fields, highlight a field from the Workspace Fields list and click the right arrow to move the field into the center column. Then, highlight the corresponding field in the Load File Fields list and click the left arrow to move the field into the center column.

You can move all fields in a list into a new column by clicking the double arrow buttons. Use the up and down arrow buttons to reorder the fields.

- In the Overwrite section, select one of these options to indicate the type of load:

- Append Only - loads only new records

- Overlay Only - updates existing records only. You must include a workspace identifier in an overlay load. This field acts as a link indicating to Relativity where to import the data.

- Append/Overlay - adds new records and overlays data on existing records

- (Optional) To view any errors, click Import , and then Check Errors . The preview dialog lists several tabs that may contain information about any errors in your import. See Handling errors .

- On the Import menu, click Import File .

- After the import completes, open the Media Received tab in Relativity and review the data.

On this page

- Importing data into a Relativity Dynamic Object

- Importing RDC Permissions

- Importing data into the Media Received object


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
