---
title: "Production data source"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_data_source.htm
collection: user
fetched_at: 2026-06-22T06:06:12+00:00
sha256: 08364a6bf41072651d562494e97a75406d32612977c84628c89733860978ba8f
---

Production data source

# Production data source

The production data source attaches saved searches to your production set. With the production data source you can specify the type of production and select placeholders from your placeholder library to customize your production. By setting the placeholder on the data source you can include multiple placeholders within a single production. The placeholder is based on the saved search attached to the production data source.

You must have view, add, and edit permissions for the Production Data Source object in order to successfully create a data set. We also recommend the delete permission.

## Adding a production data source

To add a production data source to your production:

- Navigate to the Production tab.

- Select the Production Sets tab.

- Click the name of the production where you want to add a data source.

- Scroll down to the Production Data Source card.

- Click New .

The Add Production Data Source window opens.

- Add the following fields as necessary. Required fields are orange.

- Name - the name of the production data source.

- Production Type - select images, natives, or both. If you select Images for Production Type, additional fields are required.

- Document Source - the available saved searches to use as a data source for the production.

You must create public saved searches in order for your searches to populate another Relativity user's Available Items list.

-

Use Image Placeholder - a single-choice field to add image placeholders to the data source. Documents without images receive a placeholder (slip-sheet) in their place. The placeholder receives the same branding as the rest of the produced images. This option is only available if you produce images.

- When No Image Exists - inserts a placeholder only when no image exists for a document.

- Never Use Image Placeholder - this is the default option. Never inserts an image placeholder for any document.

- Placeholder - the placeholder used for the data source. Click to view a list of available placeholders from your placeholder library. Click Add to add a placeholder on-the-fly. This field automatically appears when you select When No Image Exists.

- Burn Redactions - indicates that redactions are applied to the documents when set to Yes . Set this field to No if you do not want redactions applied to the documents.

- Markup Set - indicates which markup set is used to apply redactions to the production images.

- You can't have the same document in more than one production data source.

- The Native Time Zone Offset field controls the date and time displayed on redacted and highlighted images. If necessary, you may want to review and adjust the UTC value to avoid incorrect time designations on documents and inaccurate productions.

- Click Save .
