---
title: "Exporting OCR and Extracted Text"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Exporting/Exporting_OCR_and_Extracted_Text.htm
collection: user
fetched_at: 2026-06-22T06:14:57+00:00
sha256: 9875700ac306530f93660d230a1825d669601148a0d9216cdbe8357350ffe365
---

Exporting OCR and Extracted Text Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Exporting OCR and Extracted Text

To export OCR text for redacted documents and Extracted Text for non-redacted documents, you must set text precedence during export in the RDC.

When using text precedence, the RDC checks each text field per the order you set. If you set text precedence using the following procedure, the RDC picks up a document to export and then checks whether the OCR Text field is populated.

If OCR Text field is populated, then the RDC exports the text for this document. If OCR Text field is not populated, the RDC moves to the Extracted Text field to check whether that field is populated. If Extracted Text field is populated, then the RDC exports that as text.

## Setting text precedence

To set text precedence, perform the following steps in the RDC:

- Select Tools\Export\Production Set .

- Select the checkbox for Export Text Field as Files on the Destination Files tab.

- Select the text encoding.

- Select the ellipses next to the Text Precedence option. Move the applicable long text fields to the Selected Long Text Fields box. Rank them in the order of your desired precedence. The topmost field is the priority long text field during export.

- Click OK .

On this page

- Exporting OCR and Extracted Text

- Setting text precedence


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
