---
title: "Mass export to file"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Mass_export_to_file.htm
collection: user
fetched_at: 2026-06-22T06:15:57+00:00
sha256: 1a937a9c9a9292dd15a99dac69c1054fced6bce902539c22d063ed1f8fe8f19e
---

Mass export to file

# Mass export to file

Use the Export to file option from the Mass Operations bar to export the current View to a file (e.g., .xls, .cvs, .dat). If no individual records are selected, Relativity will export all records in the current view, regardless of how many records are displayed per page. For example, if a saved search returns 1,000 records and you ‘Export to File’ the view without selecting individual records, Relativity will export 1,000 records.

All fields in the current view and its content are exported, including unicode characters. Mass export to file is available from the mass operations bar.

### Considerations

-

Mass exports do not guarantee any sort order in the exported data, nor does mass export to file necessarily save data in the same order as it is displayed in the interface.

-

The Mass export to file option displays in the mass operations bar on the Views, Tabs, and Relativity Scripts Library tabs.

-

You can't use mass operations on Data Grid-enabled fields.

To perform the Export to file mass operation, perform the following steps:

- Select the records you want to export from the view. Do not select any records if you would like to export all of them.

- Select Export to File in the drop-down menu.

The Exporting form displays.

- Select values for the fields on the Exporting Documents form. See Fields .

- Click Run to export the file or Cancel to cancel the export.

## Fields

- Format

- Excel spreadsheet via HTML (.xls) creates an Excel file.

- Comma Separated Values (.csv) creates a comma delimited text file.

- Concordance DAT format (.dat) creates a DAT text file with the standard concordance delimiters.

The names of exported files include the word export , the date (YYYYMMDD), the time (HHMMSS in UTC), and a file extension. For example, the name of an exported file might be export_20131119_16073.xls.

- Encoding - Select the desired encoding for the output file.

- Escape Formulas - select yes or no. When you select yes, any line starts with the following special characters: =,@,+,-, or if the line starts with any combination of spaces before those characters, Relativity prepends a single quote to the beginning of the line.
