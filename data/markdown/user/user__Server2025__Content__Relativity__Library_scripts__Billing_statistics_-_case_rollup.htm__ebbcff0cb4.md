---
title: "Billing statistics - case rollup"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Billing_statistics_-_case_rollup.htm
collection: user
fetched_at: 2026-06-22T06:15:10+00:00
sha256: ab6b9f8d4167cf1444361c9370d5a7b766f8116567726c170e551333fbf664f0
---

Billing statistics - case rollup

# Billing statistics - case rollup

To help optimize performance, we don't store all historical data in Case Statistics tables. The Billing Statistics - Case Rollup only stores data for 13 months by default to ensure high performance. If you need to store this data for a longer period of time, edit the BillingDataRetentionPeriodInMonths instance setting to your desired value. Note the minimum value is 13 months.

The Billing Statistics - Case Rollup script is a billing script that reports on peak billable data for all cases in a Relativity environment. The peak billable data is the highest value within the range of a single month. This script can be used in environments where the auto-emailed statistics feature isn't possible. The results of this script will only update after an off-hours agent runs.

You must run this script in Admin mode and not from within a workspace. Otherwise, you will receive a warning and the script won't complete.

## Inputs

After clicking Run on the Script console, enter values for the following fields:

- Usage Period Year (YYYY) - the year you wish to report on.

- Usage Period Month (MM) - the month you wish to report on.

- Replace Case Name With Artifact ID - determines whether the name of the case is replaced by the case artifact ID in the report results.

- Replace Matter Name With Hash Value - obfuscate the matter names in billing metrics.

- Replace Client Name With Hash Value - obfuscate the client names in billing metrics.

## Results

After you run the script, the Billing Statistics – Case Rollup report is displayed for the specified month and year. In this table, the term peak refers to the highest value within the range of a single month.

The linked file sizes in the script do not immediately report as the underlying process to populate the linked data for the script runs on a nightly basis with the Repository Billing Agent.

The report includes the following columns (shown in alphabetical order):

Column Definition

Account The name designated as the account name.

Activity Status

Reflects whether a workspace was Active or Inactive in a specific month. This determination is based solely on a single document view within the workspace during that month. No other actions within the workspace (e.g., adding/deleting documents, user activity) affect its activity status.

Data for the timeframe of a June to August 2023 may be inaccurate due to a field being temporarily disabled.

Archive Status Indicates a status of Archived if an ARM workspace restore is in progress. Otherwise the status is Online.

AuditRecordCount The total number of audit records stored in Data Grid per workspace

AuditSize The total size of audits in GB for that workspace. If the workspace does not have the Audit application installed, this calculation is blank. AuditSize is retrieved from Elasticsearch and represents the combined size across all shards (Primary and Replica). If the original workspace has fewer shards, the reported AuditSize may be lower.

CA Image Documents Number of documents with images and without natives run through a Analytics Index or Structured Analytics Set for the first time during the reported month.

CA Native Documents Number of Native documents that were indexed with Content Analyst for first time, during the reported month.

CA Native Size Size in GB of all Native documents indexed with Content Analyst for first time, during the reported month.

Case Artifact ID Unique artifact ID associated with a workspace in the environment.

Case GUID The case Globally Unique Identifier (GUID) associated with the workspace to that environment.

Case ID Unique identifier for the workspace across all environments which combines Instance and workspace artifact ID.

CA Text Only Documents Number of documents without an image or native that were run through a Analytics Index or Structured Analytics Set for the first time during the reported month.

CA Total Documents Total number of all documents run through a Content Analyst Index for the first time, during the reported month.

Client Artifact ID Unique artifact ID of the client associated with the workspace. If the workspace is deleted, no value is reported.

Client Name The name of the client associated with the workspace. If the workspace is deleted, no value is reported.

Client Status The current status of the workspace. This value is automatically inserted by the system based on a setting in Workspace Details Advanced Settings.

CurrentBillableFileSize Current day's data for BillableFileSize in GB.

CurrentDataGridFileSize Current day's data for DataGridFileSize in GB.

CurrentDocumentCountTextOnly Current day's data for DocumentCountTextOnly.

CurrentFileCount Current day's data for FileCount.

CurrentFileSize Current day's data for FileSize in GB.

CurrentImageFileSize Current day's data for ImageFileSize in GB.

CurrentNativeFileSize Current day's data for NativeFileSize in GB.

CurrentProductionFileSize Current day's data for ProductionFileSize in GB.

Data Generated UTC The time when the Billing Agent ran to generate the metrics used by the Case Statistics report.

Data Grid File Size The sum in GB of all files stored in Data Grid per workspace.

Document Count The peak total document count in the workspace.

Document Count Text Only The number of documents that do not have any images, natives, or productions per workspace. This value is calculated as the number of documents that are in the document table but not the file table, aggregated per workspace, and reported as the maximum found for the month (similarly to the Document Count column).

DtSearch Index Size Column currently not used.

ECA Application Installed True/False value indicates if the ECA application is installed to a workspace.

File Count The peak count of the total number of files in the workspace.

File Size

The peak total file size of files in the workspace in GB. This value only counts items in the file table and doesn't include container files in the repository. Therefore, not everything in the file repository is necessarily included in this value. For example, the file size total doesn't take into account working files/copies generated by a processing job. This value also doesn't count the SQL database.

Image File Size The peak size in GB of images files in the workspace that haven't been imported using Integration Points with file pointers. This value is taken from the peak of Total Billable File Size field.

Instance The name designated as the instance name.

LDF Size The peak database log data file (LDF) size of the workspace in GB.

Matter Artifact ID Unique artifact ID of the matter (through client) associated with the workspace. If the workspace is deleted, no value is reported.

Matter Name The name of the matter associated with the workspace. If the workspace is deleted, no value is reported.

MDF Size

The peak database master data file (MDF) size of the workspace in GB.

If your MDF is split into multiple NDFs, the sum of all NDF sizes is returned.

Name The instance name and the workspace name; if the workspace name is obfuscated, it is replaced by the workspace identifier.

Native File Size The peak size in GB of native files in the workspace that haven't been imported using Integration Points with file pointers. This value is taken from the peak of Total Billable File Size field in GB.

Peak Status The peak status of any workspace in the environment. If any workspace was active during the reported month, the status is Active; otherwise, it is Inactive.

Prior CA Image Documents Number of documents with images and without natives run through a Analytics Index or Structured Analytics Set for the first time during the prior month.

Prior CA Native Documents Number of Native documents that were indexed with Content Analyst for first time, during the prior month.

Prior CA Native Size GB Size of all Native documents indexed with Content Analyst for first time, during the prior month.

Prior CA Text Only Documents Number of documents without an image or native that were run through a Analytics Index or Structured Analytics Set for the first time during the prior month.

Prior CA Total Documents Total number of all documents run through a Content Analyst Index for the first time, during the prior month.

Prior CA Year Month The prior month for the Analytics data. For example if the report is running in October, the metrics are from September.

Production File Size The peak size of production files in the workspace that haven't been imported using Integration Points with file pointers in GB. This value is taken from the peak of Total Billable File Size field.

Relativity Case Name The name given to the workspace in Relativity.

Relativity Integration Point Pushed Documents True/False value indicates if documents were pushed from a workspace using Integration Points.

SQL FT Size The peak size of the disk space that is allocated to the index (the file group) in GB. This will be within 5-10% of the actual size of the index. To estimate the actual size of the Full Text index, reduce the value reported by 5-10%.

Status Column currently not used.

Time Executed Date on which the report was generated.

Time Executed UTC The UTC time when the report is generated.

Total Billable File Size

The peak billable size of all files in the workspace in GB (this does not include files that have been imported using Integration Points with file pointers).

Total Billable File Size and the size of SQL database files are not directly related. Total Billable File Size is reporting on the size of natives, images, productions in the file repository. No SQL database files are included in this calculation.

Usage ID The usage ID given to the workspace. This is a unique identifier which combines instance, workspace artifact ID, year, and month.

Year & Month The year and month of the reported data.
