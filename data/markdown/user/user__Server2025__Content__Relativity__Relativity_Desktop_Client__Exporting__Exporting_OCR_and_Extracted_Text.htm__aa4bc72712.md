---
title: "Exporting OCR and Extracted Text"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Exporting/Exporting_OCR_and_Extracted_Text.htm
collection: user
fetched_at: 2026-06-22T06:14:57+00:00
sha256: 9875700ac306530f93660d230a1825d669601148a0d9216cdbe8357350ffe365
---

Exporting OCR and Extracted Text

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
