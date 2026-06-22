---
title: "Exporting a folder and its subfolders"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Exporting/Exporting_a_folder_and_its_subfolders.htm
collection: user
fetched_at: 2026-06-22T06:14:55+00:00
sha256: d547835482fd638f7fa8546becc83a0b3aea10f6eae5c118df00daf2c9a70a36
---

Exporting a folder and its subfolders

# Exporting a folder and its subfolders

You can export the contents of a folder and its subfolders, as well as an entire workspace, through the RDC.

To preserve the current folder structure of each document in a long text field, you have the option of running the Set Relativity folder path field script when you're exporting a folder through the RDC.

## Exporting RDC Permissions

The following permissions are required to use the exporting feature in Relativity Desktop Client:

Object Security Admin Operations

-

Document: Local Access (Download, Copy Text)

This is required when exporting long-text cells greater than the value defined by the MaximumLongTextSizeForExportInCell instance setting, the default value of which is 1048576.

-

Allow Export

## Exporting a folder and its subfolders

You can also export only the content of the current folder using the Folder option. See Exporting a folder .

To export a folder and its subfolders:

- Open the RDC and select a workspace.

- In the RDC browser, right-click on a specific folder, point to Export and then click Folder and Subfolders .

You can also highlight a folder in the RDC browser. On the Tools menu, point to Export and click Folder and Subfolders .

The Data Source tab in the Export Production window appears.

To export an entire workspace, highlight the root folder.

- (Optional) To use settings in an existing export file, complete these steps:

- Click File and select Load Export Settings .

- Browse for your export settings file (.kwx) in the Open dialog. For technical information on .kwx files, see Technical considerations for .kwx files

- Select a view, and then click OK . Your view is lists on the Data Source tab. This determines the fields listed in the Selected Columns box. Other settings from the file are used to populate the Destination Files tab. You can also modify any settings on the Data Source and Destination Files tab as necessary.

On the Destination Files tab, you may want to select Overwrite Files if you are re-exporting the same group of files to the previously used location.

- Continue with step 7.

- On the Data Source, select a view in the Views box. Update the remaining options as necessary.

The Data Source tab appears when you select the option to export production sets, saved searches, folders, and subfolders. You will see similar options on the tab for each of these actions, but you may want to select different settings for them. The following screen shot uses a production set as an example, but the settings are the same when exporting production sets, saved searches, folders, and subfolders.

On the Data Source tab, you can set the following options for the data that you want to export. Depending on the type of data you want to export, the dropdown updates accordingly. Select from the following:

- Views - Folders and subfolders - select a view for the data that you want to export.

- Searches - Saved Search - select a saved search you want to export.

- Productions - Production set - select a production set you want to export

- Selected Columns - choose the fields that you want to export by moving them to the Selected Columns box. The box on the right displays all available fields. Only the fields in the Selected Columns box are exported.

If a reflected production field is selected for Selected Column, the RDC doesn't narrow down the field to a specific production. The reflected field for all productions is included.

- Start Export at Record # - select a record number that identifies the initial document for export. The RDC exports the document with this record number and continues exporting documents with subsequent record numbers.

- (Available only for Saved Searches, Folders, and Subfolders) Production Precedence - click to display the Pick Production Precedence dialog where you can select a group of produced documents for export instead of the original images.

- Select the images that you want to export:

- Original Images - export only the original, non-produced images.

- Produced Images - export a produced version of the images.

- Include original images… - export original images for the documents that are not in a specified production.

- Move the productions that you want to exported to the Selected Productions box. To move productions between columns, highlight the production and click the Right or Left single or double arrows. Use the Up and Down arrows to order the precedence of the fields.

Any produced native files will be exported as a native instead of an image. Only one produced image is exported based on precedence in the list. If the document is in the topmost production, that version is exported. If not, Relativity checks for the document in the second production and so on. If the document is not a part of any of the selected productions, and Include original images ... is enabled, then the original document is produced.

- Select the Destination Files tab.

On the Destination tab, you can set options that control how the files in folders, searches, and production sets are exported. The Export dialog displays this tab when you select an Export option from the Tools menu, or when you right-click on a folder or workspace in the RDC. The Destination tab displays the same options when you export files in folders, searches, or production sets.

In the Text and Native File Name section, the Named after option is available only for Production Sets.

- Complete the fields on the Destination Files tab. See Fields on the Destination Files tab .

- After you have selected your export settings, select File and then click Run .

A warning message displays if you are missing information required to run the export. Update the settings for the required options, and run the export again.

- Review the progress of the export.

You can view the progress of an export through the RDC. Select the following tabs to display specific information:

- Summary - displays general information about the number of records, processing warnings, and errors. The following screen shot displays file progress for an export job.

- Errors - lists any errors encountered during the load. The Errors tab displays any errors that occur when you export content with the RDC.

- Progress - displays a detailed view of the load progress.

- Warnings - displays information about loading or connection issues.

- Report - includes the following files that you can export:

- Export Error Report - exports a .csv file with a summary of errors.

- Export Error File - exports a .dat file, which is a document-level load file containing only records with errors.

- File Transfer Mode - displays the following information:

- Web mode - this mode uses the web server and it is the standard.

- Direct mode - this mode provides faster performance, but requires a connection to the network hosting the data, as well as specific Windows group permissions. For more information, see Direct mode .

- (Optional) To save your export settings, click File > Save Export Settings . Choose a location for the export settings file (.kwx). See Technical considerations for .kwx files .

## Fields on the Destination Files tab

The Destination Files tab contains the following sections with their respective fields:

- Export Location - select a target directory for exporting folders, searches, and production sets. Click to browse for a location. Select Overwrite Files to overwrite any existing files of the same name in the target export directory.

- Physical File Export - select the Copy Files From Repository option. This is the default option and copies files from the file server to the specified export location. If you don't select Copy Files From Repository , Relativity doesn't copy the files to the export location. Instead, the exported load files reference the repository location of the files.

- Volume Information - controls the naming and size of the volume identifier. Set the following options in this section:

- Prefix - enter the alpha prefix for the volume identifier.

- Start # - select the first number used for the numeric section of the volume identifier. Multiple volumes increment numbers during export creating unique volume identifiers.

- # of Digits - select the number of digits attached to the prefix. (For example, if you select 3, the output is VOL001, VOL002, and so on.)

- Max size - select the maximum size allowed for each volume in MBs.

- Subdirectory Information - controls the naming and size of volume subfolders. Set the following options in this section:

- Image Prefix - enter the alpha prefix for the subdirectory that stores exported images.

- Native Prefix - enter the alpha prefix for the subdirectory that stores exported native files.

- Text Prefix - enter the alpha prefix for the subdirectory that stores exported extracted text files.

- Pdf Prefix - enter the alpha prefix for the subdirectory that stores exported extracted PDF files.

- Start # - select the starting number for the subdirectories.

- # of Digits - select the number of digits of the subdirectory prefix (For example, if you select 3, the output is IMG001, IMG002, and so on.)

- Max Files - select the number of files to store in each subdirectory.

- File Path - controls how the export path for the files is referenced. Select one of the following options:

- Use absolute paths - paths to exported files are represented as absolute paths.

C:\ Desktop\VOL001\NATIVE001\AS000001.msg

- Use relative paths - paths to exported files are represented as relative paths.

.\VOL001\NATIVE001\AS000001.msg

- Use prefix - a prefix is added to the relative path, such as a CD drive letter.

D:\VOL001\NATIVE001\AS000001.msg

- Load File Characters - select the delimiters to use in a document-level load file when Data File Format in the Metadata section is set to Custom . Select the following options as necessary:

- Column - this delimiter separates columns in the load file.

- Quote - this delimiter qualifies the text in each field of the load file.

- Newline - this delimiter signifies the end of any extracted text or long text field in the load file.

- Multi-Value - this delimiter separates different choices within a choice field.

- Nested Value - this delimiter indicates the hierarchy of choices within a choice field.

- Text and Native File Names - select the following options for naming exported native and extracted text files:

The following field types are supported by this feature: Date, Decimal, Fixed-Length Text, Single Choice, Whole Number, and Yes/No.

- (Available Only for Production Sets) Named after - select one of the following naming convention for exported files:

- Identifier - select this option to name the files after the identifier for your workspace.

- Beginning production number - select this option to name the files after the production number. (This number may be the Bates number for a production.)

- Custom - select this option to name the native and text files in an export by appending them with either a control number or production begin bates and optionally, a field of your choice.

To select custom naming options for your exported native and text files, do the following:

- Select Custom from the Named after drop-down menu.

- Click to the right of the Named after drop-down menu.

- Select either the control number or production begin bates naming option from the drop-down menu.

- Optionally, to append a field or custom text to the file name, click .

- Select the desired spacing option from the _ (underscore) drop-down menu.

- To either add custom text to the name or to add a field to the name, do the following:

- To include custom text as part of the name, choose the Custom Text... option in the drop-down menu and enter the desired custom text in the textbox underneath the Custom Text... drop-down menu.

- To include a field as part of the file names, select the desired field option from the Custom Text... drop-down menu. If a field is empty in a workspace it will not display as part of the file name even if selected from the Custom Text... drop-down menu.

If a boolean field is selected, the name of the field will be displayed and not the value. For example: JWOLFE_009_confidential-HAS IMAGES.

- Optionally, to add an additional field or custom text after the previously selected options, click .

- Select the desired spacing option from the _ (underscore) drop-down menu.

- To either add additional custom text to the name or to add an additional field to the name, do the following:

- To include additional custom text as part of the name before a field, choose the Custom Text... option in the drop-down menu and enter the desired custom text in the textbox underneath the Custom Text... drop-down menu.

- To include an additional field as part of the name, select the desired field option from the Custom Text... drop-down menu. If a field is empty in a workspace it will not display as part of the file name even if selected from the Custom Text... drop-down menu.

If a boolean field is selected, the name of the field will be displayed and not the value. For example: JWOLFE_009_confidential-HAS IMAGES.

- Click Apply to save the current naming options.

If a file is not found in any of the production sets, the name will revert to the control number or production begin bates regardless of which naming options you have selected.

- Append original file - Select this option to append the original file name which is defined as the file name as it was on disk to the end of the exported file name.

- Image - determines whether to include images in an export and sets the format of the load file. Set the following options:

- Check Export Images - select this option to include images in the export. (You must set the Data File Format and the File Type when you export images.)

- Data File Format - select one of these formats for image-level load file:

- Opticon

- IPRO

- File Type - select one of these file types:

- Single-page TIF/JPG

- Multi-page TIF

- PDF

- Native - controls which files are exported by Relativity Desktop Client.

- Export Native Files - select to export native files.

- Export rendered PDF's - select to export PDF files. This option is not available when exporting a Production set.

- Metadata - use the following options to control the export of the document-level load file and extracted text:

- Data File Format - select a the format for the document-level load file you're exporting:

- Comma separated (.csv)

- Concordance (.dat) - load file exports with the standard Concordance delimiters.

- Custom (.txt) - load file exports with the custom delimiters that you select in the Load File Characters section.

- HTML (.html) - load file is in HTML and contains hyperlinks to launch any exported files.

- Data File Encoding - select an encoding for the document-level load file from the drop-down box. Click for additional options.

- Export Text Field as Files - determines the export of the extracted text or OCR. Select this option if you want to export files as individual document-level text files, with one file per document. The RDC includes text as part of your load file if you deselect this option.

- Text File Encoding - select the encoding for the document-level text files. Click for additional options.

- Text Precedence - select and assign an order to long text fields that Relativity checks for text when performing an export. You must select one or more long text fields to use this functionality. Click to display the Pick Text Precedence pop-up. To move fields between columns, highlight them and click the Right or Left single or double arrows. Use the Up and Down arrows to order the precedence of the fields.

If you add any fields to the Selected Long Text Fields column, Relativity adds the Text Precedence column as the last column in the load file. During an export, Relativity checks the topmost field in the Selected Long Text Fields column for text, and if the field is null, it checks the next field in order of precedence for text. When it finds a field that contains text, Relativity adds the contents of that field to the Text Precedence column in the document load file, and then continues checking the fields for the next document.

For example, you want the Text Precedence column in the load file to contain the contents of the OCR Text field when it is available for a document and the contents of the Extracted Text field when the OCR Text for a document is null. In the Pick Text Precedence pop-up, you add the OCR Text as the first field in the Selected Long Text Fields column followed by the Extracted Text field.

If you want to improve export performance, you don't need to add all of the long text fields you select in the Pick Text Precedence pop-up to the Selected Columns option on the Data Source tab. When you don't select these fields on the Data Source tab, but you add them to Selected Long Text Fields column, the RDC adds the content of these fields to the Text Precedence column as described above. When you add the long text fields on the Data Source tab, Relativity adds these columns to the document level load file.

The Precedence Text column displays the file path to the exported files if you select the Export Text Field as Files checkbox.

- Export Multiple-Choice Fields as Nested - select this option to maintain the hierarchy of Relativity multiple-choice lists, when applicable. The nested value delimiter, a backslash, separates child choices.
