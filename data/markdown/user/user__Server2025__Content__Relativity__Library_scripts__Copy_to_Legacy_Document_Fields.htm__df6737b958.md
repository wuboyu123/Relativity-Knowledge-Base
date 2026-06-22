---
title: "Copy To Legacy Document Fields"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Copy_to_Legacy_Document_Fields.htm
collection: user
fetched_at: 2026-06-22T06:08:38+00:00
sha256: b6b3feacdf96636fa8e43b39d787fed9ddd834667953082cfa4a39080dd1cf59
---

Copy To Legacy Document Fields

# Copy To Legacy Document Fields

This script updates Bates fields you create on the Document table with the Bates numbering information stored in the Production Information RDO of a production you select.

This script is available as a feature in Post Production. Using Post Production has several benefits over using script. It is run automatically, improves performance, provides information about progress and gives an indication on the Production Set console that something has been run. See Production sets for more information.

## Special considerations

Consider the following risks before running this script:

- You can't undo this script after you run it.

- This script updates the Document table and may impact performance. Run this script during off-hours.

- Users must have View Script permissions to run this script.

## Inputs

Before running the script, perform the following tasks:

- Run and produce a production. For more information, see Production console .

Before running the script, ensure you create the following Document fields in the workspace:

- Begin Bates

- End Bates

- (Optional) Begin Bates Attachment

- (Optional) End Bates Attachment

- (Optional) Batch Size (Default 10000)

Running the script populates these fields on the Document table.

## Results

This script updates and stores the Bates fields you create on the Document table so you may continue using previous production workflows.
