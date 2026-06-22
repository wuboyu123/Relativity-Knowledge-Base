---
title: "Set Relativity folder path field"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Set_Relativity_folder_path_field.htm
collection: user
fetched_at: 2026-06-22T06:15:39+00:00
sha256: a4fc6668944c11c26bc52ca326f3a39d933f22e3cea4902a5a0bd13df7516d45
---

Set Relativity folder path field

# Set Relativity folder path field

This Relativity case script stores the current Relativity folder path of each document in a long text field. A document cannot be in more than one folder path. See the full path structure of a folder for example, Custodian / J Smith / Inbox.

This script populates the new long text field with the current case folder structure.

This is a case functionality script to be run at a case level.

The script will not work on long text fields stored in data grid. You must disable the Stored in Data Grid option when creating the long text field.

## Special considerations

The risks outlined below must be considered when running this script:

- This script cannot be undone.

- The script may run for some time without reporting any progress.

- This script updates the Document table.

- If, at any time, a folder is renamed or a document is moved, the folder path value is inaccurate.

## Inputs

By default, this script will only update documents that do not have an existing folder path. To update the folder path of documents with existing folder paths, ensure the following are in place before running the script:

- Create a long text field to store the folder path.

- Ensure the Folder Path field is not populated. Otherwise, the script won’t return results.

If you want to able to search the original folder path after running the script, save the original folder path in a separate field before you clear the existing folder path.

## Results

Once the script has run, it reports on each distinct folder path in the case, returning the number of documents per path, and the execution time of the script. It also updates the Folder Path field with the Relativity folder path of that document.

A table with the following is returned:

Column

Definition

Timestamp An indication of when the step or path finished processing.

Message The name of a distinct Relativity folder path or an execution step in the script.

DocCount The count of documents for a folder path or, if -1, the execution step of the script.
