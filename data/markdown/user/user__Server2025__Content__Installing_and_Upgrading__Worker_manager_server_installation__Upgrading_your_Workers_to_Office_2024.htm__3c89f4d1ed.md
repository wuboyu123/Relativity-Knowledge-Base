---
title: "Upgrading your Workers to Office 2024"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Worker_manager_server_installation/Upgrading_your_Workers_to_Office_2024.htm
collection: user
fetched_at: 2026-06-22T06:04:09+00:00
sha256: 1efa8b09d972a19cf82c3e02194d330f1d0b34271db149a50e56fbedd82d0d78
---

Upgrading your Workers to Office 2024

# Upgrading your Workers to Office 2024

As part of our ongoing commitment to platform compatibility and security, Server 2025 supports the installation of Microsoft Office 2024 on your Relativity Worker servers. Upgrading to Server 2025 and Office 2024 is highly recommended before or shortly after Microsoft’s end of support for Office 2016 on October 14, 2025. To learn more, see Microsoft's website .

This change requires updates to your environment, including the adoption of Server 2025 to your entire instance and the adoption of Windows Server 2022 for Invariant Workers.

You are not required to immediately adopt Office 2024 once Server 2025 is released, but it is highly recommended to ensure the security of your Relativity Server environment. We are only certifying and supporting Office 2024 for Relativity Server 2025 and future major releases.

We do not certify or support Office 2024 for Relativity Server 2023 or earlier Relativity releases.

Before deciding to upgrade, it is important to think about how your organization plans to handle the end of support for Office 2016:

- If your organization must deprecate Office 2016 on or shortly after October 14, 2025, you need to upgrade to Relativity Server 2025 to adopt Office 2024. If you would like to download the Relativity Server 2025, visit Relativity Community . If you have the flexibility to continue using Office 2016 for a little more time, carefully review the Known Issues and the Behavior changes sections below before deciding on your upgrade timeline. To learn more, see Known Issues and Behavior changes and other upgrade considerations below.

- Worker servers that run Office 2024 must be on Windows Server 2022. Other server roles (SQL, Web, Agent and others) may remain on their existing operating systems, provided those versions are still supported and you intend to continue using them in their current configurations.

- We recommend assessing potential risks of delaying adoption of Office 2024, including missing product updates, security patches, or compatibility improvements.

We want you to have the information you need to plan ahead, to understand the impact that moving from Office 2016 and 2024 will have on processing and native imaging, and to help you make informed decisions as Microsoft phases out support for Office 2016 on October 14, 2025.

## Preparing for your upgrade

Please be aware of the following system requirements and considerations as you plan your upgrade to Office 2024:

- Plan your upgrade path to Windows Server 2022, which is required for Office 2024 compatibility with Invariant workers. Windows Server 2022 is already supported for Relativity Server 2024, so you can upgrade to Windows Server 2022 at any time.

- Upgrade to Server 2025 to ensure compatibility with Office 2024 and make use of the latest improvements.

- Review licensing requirements for Office LTSC 2024. To view the licensing requirements, visit Office LTSC 2024 .

- Review the upgrade process. For detailed guidance on performing the upgrade, see the Office 2024 Upgrade Guide . This page provides step-by-step instructions and important considerations to ensure a smooth transition.

## Considerations

- Server Requirements —Office 2024 Worker Servers require Windows Server 2022.

- Relativity Server version —Relativity Server 2025 is the minimum required. All future Invariant updates, including hot fixes or patches, will require you to install the new version of Invariant.

- Office Licensing —The following license types are supported: Office, Project, and Visio LTSC Standard licenses are not supported.

- Office LTSC Professional Plus 2024

- Project Professional 2024

- Visio LTSC Professional 2024

- Older Office Files —Compatibility with legacy files remains, but the behavior may vary. More information is included in release documentation.

- Known Issues and Key Changes —To see a detailed list of known issues, see Known Issues and Behavior changes and other upgrade considerations sections below.

- Once you upgrade to Office 2024, Microsoft Publisher files are no longer supported as Microsoft deprecated the file type in Office 2024. For more information, see Deprecated functionality below.

## .eml file handling

- Outlook 2024 introduces changes to how .eml files, particularly those related to appointments, are structured. This change impacts metadata extraction and hash generation in Relativity Server 2024. It also impacts deduplication behavior.

- These changes are not limited to .ics files. They affect a range of .eml formats, especially those .eml appointments generated from non-Outlook mail clients and web-based mail platforms such as Gmail, Yahoo Mail, and Mozilla Thunderbird.

- As a result, .eml files processed in earlier versions like Relativity Server 2016 may produce different hash values compared to files processed under the new version. This is due to structural differences introduced in Outlook 2024.

- Performance may be degraded for processing jobs with a high volume or large composition of .eml files. We are continuing to test and evaluate the impact internally.

- For any processing projects that are ongoing when you upgrade from Office 2016 to 2024, we strongly recommend reprocessing all .eml files to ensure consistent deduplication and avoid review or production discrepancies.

- These changes align with Outlook 2024’s behavior and are considered the updated standard.

## Support for Server 2023 and 2024 environments running Office 2016 after Oct. 14, 2025

Relativity will continue to fully support deployments of Relativity Server 2023 and Relativity Server 2024 where Office 2016 is installed after Oct. 14, 2025 until the respective support expiration dates for those Relativity versions. To learn more about the support expiration dates, see our Server Support Policy .

However, Microsoft will no longer provide any security updates to Office 2016 after Oct. 14, 2025 and Server 2025 will require you to deploy the new version of Invariant.

## Known Issues

Upgrading to Office 2024 introduces the following known issues for processing and native imaging. The table includes guidance on when Relativity intends to address these known issues, but resolution timeframes are subject to change.

Each Known issue is also available on the Known Issues page where you can track their resolution. To learn more, see Known Issues . You can also view information about the issue resolution on the Release notes page. To learn more, see Relativity Server release notes .

Known Issue Description and Impact Target Resolution Timeframe

Vector Based Digital Image files: .snp, .emf, .wmf When processing vector-based digital image formats such as .snp, .emf, and .wmf in Relativity Server using Office 2024, we have observed that the extracted text occasionally contains minor discrepancies compared to the native file during testing. Not planned

Truncated data or cutoff in Images

Comma-Separated Values (.csv) files are plain-text files used to represent tabular data. While they open in Excel and appear similar to spreadsheets, they lack the formatting, cell structure, and metadata that are critical for accurate rendering during imaging.

There are no observed issues with processing .csv files using Office 2024. Metadata and text are extracted as expected.

To be determined

Microsoft project file: .mpp In internal testing, a small subset of .mpp files showed text extraction or metadata errors during processing and imaging. The issue appears environment-specific and was not observed across all files. As a temporary workaround, you can retry processing or imaging multiple times. This typically resolves these errors. We are continuing to investigate to ensure this does not recur across Relativity environments. Server 2025

## Behavior changes and other upgrade considerations

Feature/File Type Description Implications

Metrics: Discovered, Processed, and Published Slight variations in these metrics may occur when handling a high volume of files. We are continuing to evaluate this behavior internally to assess the impact. Differences are most observed in comparison with Office 2016. You may notice inconsistencies during processing and imaging workflows.

.eml files: Sender field uses Meeting Organizer in .eml appointments

The From field in .eml appointment files is populated using the Meeting Organizer instead of the Sender in Header. This change impacts On Behalf Of scenarios where the Sender and Meeting Organizer are not the same.

.eml calendar appointments where Sender is not the same as Meeting Organizer.

Affects Header Hash and deduplication results.

There is no impact if Sender and Meeting Organizer are the same.

.eml files: Additional recipient added for canceled events

When a calendar event is canceled, the Meeting Organizer is automatically added as an additional recipient in the .eml file.

This behavior affects the recipient's metadata extracted during processing. It potentially alters the Recipient Hash, which may impact deduplication.

Updated rendering behavior in Excel & Word

Microsoft has introduced several changes in the rendering engine of Word and Excel which impact how documents display in the Image Viewer and how they are processed by Relativity Server for text extraction.

For example, these changes can alter table alignment in Word, shift cell borders in Excel, or affect font rendering leading to differences between the native application view and the processed output.

May change how comments, hidden text, page numbers, and headers are rendered in images and extracted text.

One Note 2007: Processing and imaging

OneNote 2007 files have compatibility issues with processing and imaging because it uses older .one file structure that may not render correctly with New Office versions.

Microsoft typically recommends converting older OneNote 2007 files to newer formats using an intermediate version.

.tiff or .pdf output may differ in layout compared to Office 2016.

Page breaks, charts, or filters might not render as expected.

.xls 97-2003 Excel files that are created in the 97–2003 format (.xls) are considered legacy by Microsoft. While Office 2024 may still open these files, the specific formatting, formulas, macros, and embedded content may not render or extract correctly. Validate processing and imaging behavior for legacy Excel files before production use or convert them to modern .xlsx format.

Text extraction may produce inconsistent results.

Legacy formulas and embedded objects may not be fully supported.

In imaging, rendering may occasionally result in minor formatting inconsistencies.

Word 97-2003 Word 97–2003 is a legacy format with limited support in Office 2024. While Office 2024 can still open .doc files, certain features, formatting, or embedded content may not render.

In processing, incomplete or mis-formatted extracted text due to outdated structures.

Track changes, comments, or section breaks may not be fully preserved.

Rendered images may show layout issues.

.ppt 97 - 2003 Legacy PowerPoint files use an older file format that Office 2024 does not fully support. Some animations and embedded media might not work correctly. When these files are processed or imaged in Relativity Server, parts of the content may be missing or display incorrectly.

Text may be extracted partially or with formatting inconsistencies.

Embedded content may not be accessible.

In imaging, slides may appear on altered backgrounds, or font rendering may degrade.

In some cases, imaging may fail completely, especially with non-standard fonts or legacy media type.

.rtf .rtf files are partially supported by Office 2024 and formatting compatibility is limited.

In processing, basic text may be extracted, but complex formatting, embedded items, or tables might be lost or appear broken.

In imaging, rendered output may display incomplete content or layout inconsistencies compared to how the file appears in Word.

.pub

Support for Publisher files has been deprecated by Microsoft. Relativity Server 2025, with Office 2024 installed, will inherit this limitation, and users will no longer be able to process or image .pub files using Office 2024.

This limitation applies only when the Office 2024 toggle is enabled. If Office 2016 is installed and selected, Publisher files can still be imaged as before.

## Deprecated functionality

### Publisher files

Since Publisher is not included in Office 2024, this upgrade means .pub files will no longer be supported in Relativity Server after you upgrade to Office 2024. Support for Publisher files is also being deprecated in RelativityOne in early September 2025. While this should have minimal impact to your workflows, if you need to continue working with Publisher files after support has ended, you can do the following:

- Convert Publisher files to a supported format such as .pdf using an older version of Microsoft Publisher or a third-party tool.

- Send the converted files to Relativity for normal processing and imaging.

- Alternatively, you can review Publisher files offline, outside of Relativity Server.

#### Additional considerations

- If you attempt to process or image a Publisher file after this upgrade takes place, the system will indicate that the file format is not supported. When processing, the file will be flagged as an exception with the category Unsupported File Type.

- As with all unsupported formats, processing is unable to obtain metadata and text, but you are still able to publish the files to your workspace.

- Also note, unsupported file types are not included in the Retry File Exceptions workflow, since retrying will not yield a different result.

- There is no change in the level of support for Publisher files using the Native Viewer. These files will continue to be supported for file-ID only.
