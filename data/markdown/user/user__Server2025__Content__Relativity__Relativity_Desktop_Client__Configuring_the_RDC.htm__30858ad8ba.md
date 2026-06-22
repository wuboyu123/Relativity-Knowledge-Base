---
title: "Configuring the RDC"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Configuring_the_RDC.htm
collection: user
fetched_at: 2026-06-22T06:14:58+00:00
sha256: ed4fc27ea4377da065bdc8fc1de8b860783d4e24e4b7b6fb30da5c53cb897eeb
---

Configuring the RDC Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Configuring the RDC

You can fine-tune the performance of the RDC in your environment by adjusting its configuration settings, for example, for batching, data validation, and retries.

## RDC configuration file

You can use the information in this section to update the configuration settings used by the RDC. The Import API also uses these same settings located in the app.config file. Click here to download this file.

Use the following instructions to locate the config file on your machine, and set custom configuration properties for the RDC:

- Exit the RDC if it is currently open.

- Navigate to the Relativity.Desktop.Client.exe.config file on the machine where the RDC is installed. By default, this configuration file is located in the following directory:

[Installation_Directory]\kCura Corporation\Relativity Desktop Client

Make a backup copy of this file in case you need to rollback any configuration changes made to it.

- Open the Relativity.Desktop.Client.exe.config file in a text or XML editor and modify it as necessary.

### Configuration settings

The Relativity.DataExchange section of the Relativity.Desktop.Client.exe.config contains the configuration properties in the following table.

#### General settings

Name Description Default Value

CreateErrorForInvalidDate When this value is set to True, a zeroed date, such as 0/0/0000, causes an Invalid Date error. When False, the date is treated as a NULL value. True

FileTypeIdentifyTimeoutSeconds Defines the maximum number of seconds to identify a file type before reaching the timeout. 10

HttpExtractedTextTimeoutSeconds Defines the timeout, in seconds, for HTTP/REST-based API web services specifically used for extracted text.

This value doesn't impact WebAPI-based web services, which means that WebAPIOperationTimeout setting is still honored.

900

HttpTimeoutSeconds Defines the timeout, in seconds, for HTTP/REST-based API web services.

This value doesn't impact WebAPI-based web services, which means the WebAPIOperationTimeout setting is still honored.

300

IOErrorNumberOfRetries

Defines the number of times the RDC retries an operation within an import or export process after an IO failure occurs.

20

IOErrorWaitTimeInSeconds

Defines the number of seconds the RDC waits before retrying an operation within an import or export process after an IO failure occurs.

30

LogAllEvents Enables an option to Save Progress Log when job completes. False

LogConfigFile Defines the Relativity Logging configuration file name. LogConfig.xml

SuppressCertificateCheckOnClient When this value is set to True, SSL certificate validation errors are suppressed. When False, SSL certificate validation errors cause job failures. False

TempDirectory Defines a temp directory override where short lived import files are stored. When not defined, the user profile %TEMP% directory is used.

WebAPIOperationTimeout Defines the time in milliseconds, which an XML Web service client waits for the reply to a synchronous XML Web service request to arrive. 600000

#### Transfer settings

Name Description Default Value

BadPathErrorsRetry When this value is set to True, bad path errors are retried during a transfer. When False, permission errors aren't retried and cause job failures. True

PermissionErrorsRetry When this value is set to True, permission errors are retried before and during a transfer. When False, permission errors aren't retried and cause job failures. True

TapiFileNotFoundErrorsDisabled When this value is set to True, missing files aren't treated as errors. When False, missing files are treated as errors. False

TapiFileNotFoundErrorsRetry When this value is set to True, missing files are retried. When False, missing files aren't retried. True

TapiForceBcpHttpClient When this value is set to True, the HTTP transfer client is forced only for BCP operations. When false, the best fit transfer client is chosen at runtime. This functionality is also available as the TapiForceBcpHttpClient instance setting. False

TapiForceClientCandidates Forces an ordered list of transfer clients when probing a workspace and choosing the best client. This value represents a semi-colon delimited list. Native transfer client identifiers must be used, such as FileShare or Http.

TapiForceFileShareClient When this value is set to True, the file share transfer client is forced. When False, the best fit transfer client is chosen at runtime. False

TapiForceHttpClient When this value is set to True, the HTTP transfer client is forced. When false, the best fit transfer client is chosen at runtime.

This setting is the same as web mode.

False

TapiLargeFileProgressEnabled When this value is set to True, large-file progress is used by transfer clients to display "Trip x of y" chunk info within the status area. When False, no chunk info is displayed . False

TapiMaxInactivitySeconds The maximum number of seconds that elapse with no data movement occurring before the transfer is treated as inactive. When this occurs, the import or export job continues but performance may be degraded. 180

TapiMaxJobParallelism Defines the maximum degree of parallelism for a transfer client job. This value isn't guaranteed to be honored by all clients. 10

TapiMinDataRateMbps Defines the minimum data rate in Mbps units. If set to zero, the best value is chosen. This value isn't guaranteed to be honored by all clients. 0

TapiPreserveFileTimestamps When this value is set to True, the RDC preserves the import and export file timestamps. Only direct modes support this functionality.

By default, this value is set to False, because preserving file timestamps may degrade performance between 10-20%.

False

TapiTargetDataRateMbps Defines the target data rate in Mbps units. This value isn't guaranteed to be honored by all clients. 100

TapiTransferLogDirectory Defines the directory where Relativity Logging and transfer client logs are stored. %temp%\RDC_log\

#### Import settings

Name Description Default Value

AuditLevel

Controls the details collected in an audit:

- FullAudit - includes create, update, and delete messages. Snapshot is also enabled so all current field values (Audit Details) are captured for updates. This is the default setting.

- NoSnapshot - Includes create, update, and delete messages. Snapshot is disabled so current field values (Audit Details) aren't captured for updates.

- NoAudit - Auditing is disabled.

FullAudit

CreateErrorForInvalidDate When this value is set to True, a zeroed date, such as 0/0/0000, causes an Invalid Date error. When False, the date is treated as a NULL value. True

DisableImageLocationValidation Disables the validation of the image file locations for all jobs when set to True. See Additional guidelines for disabling file validation . False

DisableImageTypeValidation Disables the validation of image file types for all jobs when set to True. Image type validation is dependent upon image location validation. See Additional guidelines for disabling file validation . False

DisableNativeLocationValidation Disables the validation of the native file locations for all jobs when set to True. See Additional guidelines for disabling file validation .

Don't use the DisableNativeLocationValidation flag when copying files to a repository. File locations are validated regardless of the flag before they are copied.

False

DisableNativeValidation Disable the validation of native file types for all jobs. Native type validation is dependent upon native location validation. See Additional guidelines for disabling file validation . False

DynamicBatchResizingOn When this value is set to True, the batch size is automatically decreased by 100 when a large import job is in progress, and it causes a timeout. True

ImportBatchMaxVolume Defines the maximum number of bytes before the metadata is imported. 10485760

ImportBatchSize Defines the maximum number of documents or objects before the metadata is imported. 1000

JobCompleteBatchSize Defines the file count threshold at which the RDC completes and recreates the transfer job used to transfer files. 50000

MinimumBatchSize When AutoBatch is set to True, this value represents the lower bound on the batch size. Batch sizes can't be smaller than this value. 100

##### Additional guidelines for disabling file validation

You can disable file validation by setting these configuration settings to true:

- DisableImageLocationValidation

- DisableImageTypeValidation

- DisableNativeLocationValidation

- DisableNativeValidation

Review the following guidelines before disabling file validation:

- When you disable file type validation, you do not receive any warnings regarding unsupported file types. It's therefore possible for files to be imaged and result in errors.

- Disabling the file type validation also causes the application to set the Relativity Native Types field to Unknown Format.

- Setting a native type to unknown has no effect on productions or OCR.

- Setting a native type to unknown has no effect on how the viewer or imaging engine handles the file. This means that a native type of unknown can't be the sole cause of an error in the viewer or the imaging engine. If a file is designated unknown and it actually has an unsupported file type, the Viewer or imaging engine throws an error based on the fact that it has an unsupported file type.

#### Export settings

Name Description Default Value

ExportBatchSize Defines the maximum number of export documents per batch. 1000

ExportErrorNumberOfRetries Defines the number of times the RDC retries an operation within an export process after a non-IO failure. This value should be greater than or equal to the IOErrorNumberOfRetries value. 20

ExportErrorWaitTimeInSeconds

Defines the number of seconds the RDC waits before retrying an operation within an export process after a non-IO failure. This value should be greater than or equal to the IOErrorWaitTimeInSeconds value.

30

ExportThreadCount Defines the number of threads that get created during export.

This configuration setting is only used when the UseOldExport setting is true.

2

UseOldExport When this value is set to True, the legacy export method is used. When False, the new export method is used. The old export should only be used when encountering compatibility issues. False

On this page

- Configuring the RDC

- RDC configuration file

- Configuration settings


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
