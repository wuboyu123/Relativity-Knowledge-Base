---
title: "Set native file size field v4"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Set_native_file_size_field_v4.htm
collection: user
fetched_at: 2026-06-22T06:15:35+00:00
sha256: 7b2df504901b75f43153fc5fd5b57e3da20a11b3d83b6f4f89a81f126cc30559
---

Set native file size field v4

# Set native file size field v4

This Relativity script stores the native file size for each document in the workspace in a decimal field.

This script only populates the size field if it was blank before running the script, and in those cases, it populates that field with a kilobyte (KB) value. If the size field was already set in bytes and not KB, the script does not change that value, and it remains in bytes.

This is a case functionality script to be run at a case level.

## Special considerations

Consider the following when running this script:

- This script cannot be undone.

- The script may run for some time without reporting any progress.

- This script updates the Document table.

- This script will populate the file size field for any files, including third party documents not processed in Relativity, as well as those that were transferred into the workspace as ‘Links only’ Natives via Integration Points.

## Inputs

Before running the script, create a decimal field to store the native file size.

## Results

Once run, this script updates the Native File Size field with the file size for any document in the workspace. Note that there could be a mix of file size values in KB and bytes.
