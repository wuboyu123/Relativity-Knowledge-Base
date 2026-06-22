---
title: "Import API best practices"
url: https://platform.relativity.com/Server2025/Content/Import_API/Developer_Guide/Import_API_best_practices.htm
collection: developer
fetched_at: 2026-06-22T06:29:56+00:00
sha256: 120d5f0bd18396f45f1d021395ceab6404b0273f64061d4fffd2f12c9f23e535
---

Import API best practices

# Best practices for the Import API

Review the following guidelines to optimize your application development with the Import API.

## Use the Name field for Dynamic Objects

Use the Name field with a unique identifier to reference Dynamic Objects.

## Use required identifiers in OverwriteMode

Use the following identifiers for documents and Dynamic Objects when setting OverwriteMode to Overlay:

- Documents – use control number

- Dynamic objects – use name

## Specify a field as an identifier for document imports

Use the SelectedIdentifierFieldName() property to specify a field as an identifier when you are importing new documents. During document import, the control number is used when the specified identifier can't be resolved, while an error is generated when the control number can't be resolved.

## Use the kCuraMarkerFilename field when copying files

You can optionally use the kCuraMarkerFilename field when NativeFileCopyMode is set to CopyFiles. Set this field to the filename that you want displayed in Relativity. If you want to use the filename on disk, don't set this field.

## Set NativeFilePathSourceFieldName when copying native files

When the NativeFileCopyMode property is set to any value other than DoNotImportNativeFiles, you must set the NativeFilePathSourceFieldName.

## Use a unique identifier when importing child records

Set the ParentObjectIdSourceFieldName property when importing records that are the children in a parent/child relationship. ParentObjectIdSourceFieldName property indicates the name of the field that contains a unique identifier for the record of the parent object associated with the current record.

## Set appropriate fields when importing extracted text

Set the ExtractedTextEncoding and ExtractedTextFieldContainsFilePath fields when you import extracted text.

## Follow guidelines when importing extracted text with images or productions

Make sure that the extracted text files meet these requirements:

- They have .txt extensions.

- They are stored in the same directory as TIFF files.

- They are named in the same way as the TIFF files.

If you are importing extracted text along with images, you need to set the ExtractedTextFieldContainsFilePath property when you return a ImageImportBulkArtifactJob from the NewProductionImportJob() or NewImageImportJob() method. In addition, the extracted text files must reside in the same directory as the images and use an identical naming scheme as the images, but they must have a.txt as their extension. For example, an image file resides in this directory and using this name:

Copy

```text
1
2

C:\\VOL01\SHAP0001.tif
```

The associated extracted text file must be located in same directory and follow a similar naming convention except for the .txt extension:

Copy

```text
1
2

C:\\VOL01\SHAP0001.txt
```

## Improve performance by using Import API settings

You can improve performance by using settings that control how the Import API handles metadata associated with objects.

### Skip Outside In file identification

Use the OIFileIdMapped property to skip file identification through the Import API. When setting OIFileIdMapped to true, you must process and identify the files yourself. The OIFileIdColumnName and OIFileTypeColumnName properties must be set to values that indicate the columns in the SourceData property, which contain the OutsideInFileId and the OutsideInFileType properties. You can set arbitrary names for those columns. During the actual file import you must then populate those fields for each file.

Copy

```text
1
2
3
importJob.Settings.OIFileIdMapped = true;

importJob.Settings.OIFileIdColumnName = "OIFileId";

importJob.Settings.OIFileTypeColumnName = "OIFileType";
```

### Skip file size checking

Use FileSizeMapped property to skip file size checking through the Import API. The FileSizeColumn property must be set to the value that indicates the column in the SourceData property which contains the FileSize.

Copy

```text
1
2
importJob.Settings.FileSizeMapped = true;

importJob.Settings.FileSizeColumn = "FileSize";
```

### Disable checks on extracted text files

Use the DisableExtractedTextEncodingCheck setting to bypass the process of directly detecting the encoding of each file in an import job. When setting DisableExtractedTextEncodingCheck to true, you must also define the encoding used for all files during your import by setting ExtractedTextEncoding. In addition, use the DisableExtractedTextFileLocationValidation to skip the validation of the location for native files.

Copy

```text
1
2
importJob.Settings.DisableExtractedTextEncodingCheck = true;

importJob.Settings.ExtractedTextEncoding = Encoding.ASCII;
```

Files in an import job must have the same encoding.

### Map objects by ArtifactID

Use the ObjectFieldIdListContainsArtifactId setting to identify fields that should be mapped by ArtifactID instead of by name.

You can map fields by name through both the Relativity Desktop Client (RDC) and the Import API. This functionality requires loading a large metadata table of fields into memory. Since the RDC loads this table and the workspace at the same time, users don’t often notice any delay during an import job. The Import API loads these fields as they are created with a constructor, which may cause a performance delay.

## Use a single Import API instance per workspace

You can improve performance by using a single Import API instance per workspace. In addition, minimize the number of times the Import API instance is created or destroyed. (The Import API loads field metadata at creation, which may cause a performance delay.)

- The ImportAPI class isn't thread-safe. Attempting to use this object from multiple threads or tasks can lead to intermittent fatal exceptions.

- Minimize the number of times that you reusing the Import API objects because they do expire.

- Consider the expiration timing determined by the authentication method that you are using. For more information, see Authentication .

## Determine optimum batch size for your environment

You may want to use import batch sizes of 1000 files initially. After further testing, you can customize the batch size for your environment needs.

## Avoid index fragmentation

When running large jobs through the Import API, you may experience decreased performance due to index fragmentation. Avoid this issue by rebuilding all of your indexes before starting a large import job. Additional steps that you can take to minimize fragmentation include:

- Rebuilding indexes on the fly.

- Upgrading to the latest version of Relativity.

## Miscellaneous ways to improve performance

Additional best practices to improve performance include:

- If you are only adding new items, use Append rather than Append/Overlay. Append mode is much faster. See the OverwriteModeEnum Enumeration in the Import API class library.

- Use ArtifactIDs when creating multiple object and single object fields to facilitate performance.

## Deploy Import API specific assemblies

After implementing a custom Import API application, you need to build your assemblies and then upload them to Relativity as resource files. You must also upload any Import API specific assemblies, including required Transfer API assemblies in the Relativity.Server.Transfer.SDK package as resource files. For more information, see Resource files on the Relativity Documentation site.

Relativity doesn't automatically deploy Import API specific assemblies and dependencies. You must manually add these assemblies in order for your custom application to function properly.

## Path lengths

The Import API doesn't support long paths. For information about path support on Windows operating systems, see Maximum Path Length Limitation on the Microsoft website.
