---
title: "Processing to Data Grid"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Processing_to_Data_Grid.htm
collection: user
fetched_at: 2026-06-22T06:13:39+00:00
sha256: 7c21ef58a2235a806d15818ea922f51e9fc8d71b2eb5f9f846ac34d0abd7739b
---

Processing to Data Grid

# Processing to Data Grid

By processing directly into Data Grid TM , you have the opportunity to improve your publishing speeds.

Read if you're studying for the Processing Specialist exam The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

In order to process data to Data Grid, you must first install all the required components, agents, and applications. For information on how to do this, see Installing Data Grid .

## Enabling processing to Data Grid

After you install Data Grid, the only requirement for setting up your workspace to process to Data Grid is enabling both the workspace and the extracted text field in your environment.

To enable your workspace for Data Grid, perform the following steps:

We recommend you only enable Data Grid for fields storing extracted text, OCR text, or translated text.

- Navigate to the Workspace Details tab, and then click Edit .

- Enable the Is Data Grid Enabled field.

- (Optional) Next to Data Grid File Repository , select the path for the physical location of the text files used by Data Grid. If no file repository is specified for this field, and Data Grid is enabled, Data Grid stores text in the default file repository.

If you run out of space in this repository, you can specify a new repository. Data Grid will continue to read from the old repository as well as the new repository.

- Click Save .

To enable the extracted text field for Data Grid, perform the following steps:

- Navigate to the Fields tab.

- Locate the extracted text field and click the Edit link next to it.

- Enable the Store in Data Grid field under the Advanced Settings tab.

If you are storing extracted text in Data Grid, the Include in Text Index field is set to No because there is no SQL text index. If you want to search using dtSearch, you must follow best practice of creating a saved search of fields you want to index.

- Click Save .

Enabling extracted text fields for Data Grid works for new workspaces only. You can't enable Data Grid for fields that already have text in SQL. If you want to migrate fields from SQL to Data Grid, you must use the Data Grid Text Migration application .

Now that you've enabled processing to Data Grid, you can proceed to running a processing set the way you normally would.

The processing engine and Data Grid do not communicate directly with each other when you process data to Data Grid. Because of this, the Write-to-Grid phase of processing has been deprecated. Instead of writing directly to the grid, the processing engine sends data to the Import API. The Import API receives the data and looks to see whether the workspace is enabled for Data Grid. If the workspace is not Data Grid-enabled, then the Import API sends all of the data to SQL. If the workspace is Data Grid-enabled, then the Import API looks at each field to see which fields are Data Grid-enabled. If the field is Data Grid-enabled, then the Import API sends that data to Data Grid. If the field is not Data Grid-enabled, then it sends that data to SQL.
