---
title: "Stage a production"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_console/Stage_a_production.htm
collection: user
fetched_at: 2026-06-22T06:08:41+00:00
sha256: 5cd811d03304ec7e2c439580709e0ec2a3bb067292f99b55aa2f42bf781813c4
---

Stage a production

# Stage a production

Before you can run a production, you must stage the production. Staging the production takes a snapshot of the data sources to prepare documents. After you assign your data sources, placeholders, and production set, you can stage your production.

## Stage a production

To stage a production, click Stage in the Production console. You can also stage and run a production job in a single step by clicking Stage and Run Production on the Production console. For more information, see Stage and run a production .

The progress bar displays the following:

- Staging - Relativity is staging the production.

- Running Saved Searches - Relativity is running the saved searches associated with the production data sources.

- Cleaning Up Data - Relativity pre-sorts the documents and deletes any Production Information objects that may already exist if the production is being restaged.

- Creating Production Information Records - Relativity is creating the Production Information records associated with the production.

Changes made to any data source after staging completes are not captured when the production is run. Examples of changes include modifying the conditions of a saved search for a data source and adding or deleting a data source from the production. To insure that you capture data source changes, stage or re-stage the production immediately before you run the production.

If you are upgrading productions from Relativity 9.2 to Server 2025 , previously staged or errored productions are set to a status of New and you must restage the production.

If you want to improve staging times, increase the MassCreateBatchSize instance setting. If you want to improve re-staging times, increase the MassDeleteBatchAmount instance setting.

## Staging Summary fields

During staging, a report is available in the Status section. Use this report to quickly identify the number of documents, images, redacted documents, etc.

Staging Summary fields include:

- Total Documents Count - lists the number of documents found during staging.

- Total Images Count - lists the number of images found during staging.

- Documents with Images - lists the number of documents that include images found during staging

- Documents with Natives - lists the number of documents that include native files found during staging.

- Documents with Placeholders - lists the number of documents that include production placeholders found during staging.

- Redacted Documents - lists the number of documents that include redactions found during staging.

## Staging errors

Staging errors occur when

- The same document is found in multiple data sources.

When the same document is found in multiple data sources, you will receive an error message. The error message identifies the data sources that pulled back the same document and which document they pulled back. To resolve the error, modify the saved searches that you selected as your data sources to ensure that they do not pull back any of the same documents.

- There are no documents in the data sources.

When no documents are found in the data sources, you will receive an error message. To resolve the error, make sure that the saved searches that you selected as your data sources are pulling back documents.
