---
title: "Advanced Formatting for Branding"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Advanced_Formatting_for_Branding.htm
collection: user
fetched_at: 2026-06-22T06:08:36+00:00
sha256: 53869d9551d454ae303a58ea71ca8cceba28688fe235c6ef734cd5e01f3488fd
---

Advanced Formatting for Branding

# Advanced Formatting for Branding

Advanced Formatting is a type of branding available on the Production Set form. See Branding .

With Advanced Formatting, you can brand headers and footers with a combination of fields from the Advanced Formatting drop-down list, free-form text, and carriage returns. The Advanced Formatting option also supports a scripting language that you can use to create conditional branding based on production, document, and page fields.

For conditional statements, the root context objects are

- Production object

- Document object

- Page object

If you add a field to a conditional statement incorrectly, you can still save and run the production set, but the branding will not generate an error and will produce incorrect results.

## Production object

The production object stores information about the production. It is the same for every item branded in the production.

Name Data type Description Name in Advanced Formatting drop-down list

Document DocumentDrop The current document being branded. N/A

ProductionId int The ID of the workspace. Production Id

ProductionName string The name of the production. Production Name

TotalDocuments int The total number of documents in the production. Total Documents

TotalImages int The total number of images in the production. Total Images

WorkspaceId int The ID of the production.

Workspace Id

Example of Advanced Formatting with the production object

### Example of Advanced Formatting with the production object

The example in this section does not demonstrate everything that you can do with the production object.

As shown in the screen shot below, you can combine free-form text with productions objects.

```text
Number of documents in {{context.ProductionName}}: {{context.TotalDocuments}}
```

The screen shot below shows a document that was branded per the command in the screen shot above. In this example, the ProductionName is Production object conditional statement, and the TotalDocuments is 15.

## Document object

This object stores information about the document and will change for each document.

Name Data type Description Name in Advanced Formatting drop-down list

ArtifactId int The ArtifactId of the document in the production. Artifact Id

HasRedactions bool If set, the current document contains redactions on at least one page. Document Has Redactions

HasPlaceholder bool If set, the current document is a placeholder. Has Placeholder

BeginBates string The first bates number in this document. Begin Bates

EndBates string The last bates number in this document. End Bates

BeginBatesAttachment string The first attachment bates number in this document. Begin Bates Attachment

EndBatesAttachment string The last attachment bates number in this document. End Bates Attachment

Page PageDrop The current page being branded. N/A

["Field Name"] FieldDrop

Returns the field value of the specified document field. This will return null if the field does not exist or is not supported.

e.g. context.Document["Control Number"].Value

Only the following field types are supported:

- These values are in string format as done in object manager.

- Custom Placeholders also supports these field types.

- Reflected fields are not supported.

-

case FieldType.Date

- case FieldType.Decimal

- case FieldType.FixedLengthText

- case FieldType.WholeNumber

-

case FieldType.YesNo

-

case FieldType.SingleChoice

-

case FieldType.MultipleChoice

N/A

Example of Advanced Formatting with the document object

### Example of Advanced Formatting with the document object

The example in this section does not demonstrate everything that you can do with the document object.

As shown in the screen shot below, you can create conditional statements with the document object.

```text
{% if context.Document.HasRedactions %}
THIS DOCUMENT HAS REDACTIONS
{% endif %}
```

The document in the screen shot below is branded per the command in the screen shot above. Since the document has a redaction, it meets the requirements of the conditional statement, so the free-form text is branded on this document.

## Page object

The page object stores information about the page and will change for each page.

Name Data type Description Name in Advanced Formatting drop-down list

BatesNumber string The bates number of the current page. Bates Number

FileName string The name of the file. File Name

HasRedactions bool If set, this page has redactions. Page Has Redactions

IsPlaceholder bool If true, this page is a placeholder page. Is Placeholder

PageNumber int The current page. Page Number

Example of Advanced Formatting with the page object

### Example of Advanced Formatting with the page object

The example in this section does not demonstrate everything that you can do with the page object.

As shown in the screen shot below, you can use page objects in conditional statements.

```text
{% if context.Document.Page.PageNumber == 1 %}
Only brand this text on page 1.
{% endif %}

{% if context.Document.Page.PageNumber > 1 %}
Brand Bates number on every page after page 1:
{{context.Document.Page.BatesNumber}}
{% endif %}
```

The document in the screen shot below is branded per the commands in the screen shot above. The free-form text from the first conditional statement is only printed on the first page. The free-form text from the second conditional statement is only printed on the second page.

## Script examples

Below are Advanced Formatting script examples:

- Brand the free-text, Production Name, and Page Number on every page.

```text
Production Name: {{context.ProductionName}}
Page # {{context.Document.Page.PageNumber}}
```

- Brand the free-text on pages that have redactions.

```text
{% if context.Document.Page.HasRedactions%}
THIS PAGE CONTAINS REDACTIONS
{% endif %}
```

- Brand the free-text on pages that have a specific page number.

```text
{% if context.Document.Page.PageNumber == 1 %}
This text will be branded only on page 1
{% endif %}
```

- Brand the Bates Number on every page after page number 1.

```text
{% if context.Document.Page.PageNumber > 1 %}
{{context.Document.Page.BatesNumber}}
{% endif %}
```

- Brand the free-text on the pages that fall between a page range.

```text
{% if context.Document.Page.PageNumber  > 1 and context.Document.Page.PageNumber  < 11%}
Confidential
{% endif %}
```

```text
{% if context.Document.Page.PageNumber  > 11 and context.Document.Page.PageNumber  < 21%}
Attorneys’ Eyes Only
{% endif %}
```

-

Brand the document that has a document field with specific value.

```text
{% if context.Document["Confidentiality"].Value == "Attorneys’ Eyes Only" %}
```

```text
Confidential - Attorneys’ Eyes Only
```

```text
{% endif %}
```
