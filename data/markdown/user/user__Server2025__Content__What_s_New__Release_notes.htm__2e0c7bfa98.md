---
title: "Release Notes - Relativity Server"
url: https://help.relativity.com/Server2025/Content/What_s_New/Release_notes.htm
collection: user
fetched_at: 2026-06-22T06:05:42+00:00
sha256: cac0e05a7c043800db4025939c2364a2444104973ef8815a1a0b03c9a53fabaf
---

Release Notes - Relativity Server Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Server release notes

This page contains release notes for Relativity Server versions 2023 and later, including release notes for Patches and Hot Fixes. For a list of known issues in Relativity, see Known issues .

To view release notes for Relativity Server 2022, Relativity Server 2021, and Relativity Server 10.3, please see the Release Notes page in the Relativity Server 2022 documentation.

Learn more about hot fixes and patches

- Relativity releases hot fixes and patches to remediate select defects and vulnerabilities found in supported Relativity Server versions. Hot fixes are unscheduled update releases to resolve higher impact defects or vulnerabilities. Patches are scheduled update releases that also include fixes for less severe/lower impact issues

- Hot fixes and patches are associated with a specific version of Relativity Server. In other words, Relativity Server 2025 hot fix #1 is built for Relativity Server 2025 and cannot be applied to Relativity Server 2024.

- Hot fixes and patches are cumulative for a base version of Relativity Server. Each hot fix and patch that Relativity Releases includes all previously-released hot fix and patch content for that base version. In other words, hot fix #2 for Relativity Server 2025 includes hot fix #1 for Relativity Server 2025. Patch #2 for Relativity Server 2025 includes patch #1, as well as any hot fixes released between patch #1 and patch #2.

- This means you do not need to separately install previous hot fixes; the latest hot fix/patch will always include all preceding hot fixes and patches for that version of Relativity server.

- The first digit represents the patch number, and the second digit represents the hot fix number relative to the patch. This new versioning attribute is referred to as the update version.

Consider the diagram below, which illustrates how the new update versioning scheme for Server 2025 would be applied during sequential hot fix and patch releases. In this diagram:

- Hot fix #2 (update.0.2) also includes hot fix #1 (update.0.1) changes

- Patch #1 (update.1.0) includes hot fix #1 and #2, as well as additional new fixes for the patch. (Since hot fix #2 includes hot fix #1, patch #1 includes hot fix #1 as well.)

- Hot fix #3 (update.1.1) includes everything in patch #1. (Therefore, hot fix #3 includes hot fixes #1 and #2, as well as the additional fixes included in patch #1.)

- Hot fix #4 (update.1.2) includes everything in hot fix #3. (And since hot fix #3 includes patch #1, everything up to an including hot fix #3 is included in hot fix #4.)

- Patch #2 (update 2.0) includes patch #1 (update 1.0), hot fixes #3 and #4 (updates 1.1 and 1.2), and additional new fixes for the patch.

Using the Release Notes table

In the following table, click on any column heading to sort the column in alphanumeric order. You can also select the drop-down to set filters for certain columns, or use the Search box to search for specific text in the Description column.

For example:

- To see a list of available Hot Fixes for Relativity Server 2024, select Server 2024 from the Version column, and then select Hot fix from the Update Type column. You can click the Original Release Date column to sort the filtered results by release date, descending or ascending.

- To see a list of Hot fixes included in a specific patch for Server 2024, select Server 2024 from the Version column, and then select the desired patch name in the Patch Version column. You can then select Hot fix from the Update Type column, which will show hot fixes that are included in the patch version that you selected.

- To see if a particular fix is included in a patch or hot fix for different versions of Relativity Server, enter the text of the fix in the Search box. This will return all release notes containing the entered text. If a particular item was released for both Server 2024 and Server 2023, you should see at least two rows in the list of Release note items.

Column Expanations

- Product Version : This is the 'base' version of Relativity Server, for example Server 2024 or Server 2023. Remember that Hot Fixes and Patches apply only to specific versions of Relativity Server.

- Update Type : this is the type of installer that the release item was first released in. Some items are first released in Hot Fixes, while others are first released in Patches.

- Base : these items are included in the initial release for that version of Relativity Server.

- Hot fix : these items were first released in a Hot Fix (but may subsequently be included in a Patch; if there is a value in the Patch version column, it means that this item is also available in that Patch)

- Patch : these items were first released in a Patch.

- Hot Fix Version : If the item was first released as a Hot Fix, this column shows the Hot Fix version that the item was first released in. Note that Hot Fixes are cumulative, see Learn more about hot fixes and patches .

- If Hot Fix version is blank, that particular item was not first released as a separate Hot Fox, but was included in the Base release or in a Patch.

- Patch Version : This is the Patch version that the release item is included in. Patches are essentially collections of all preceding Hot Fixes for that version of Relativity Server, but can include additional fixes as well.

- If Patch version is blank, that item was either included in the initial base release, or is only available as a Hot Fix and is not yet included in a Patch.

- Initial Release Date : This is the date when that item was released for the first time.

- Type : This categories the change type of the item, for example a Resolved Defect or an Enhancement.

- Feature : This is the feature/application within Relativity that the item applies to.

- Description : This is the release item description.

Tip: you can search the Description field by entering text into the Search box. If you want to determine if the same fix was released for both Server 2024 and Server 2023 for example, use the Search box to filter rows for the specific item you are looking for, which will then tell you which release that item is included in for Server 2024 and in which release that item is included for Server 2023.

Product version Update type Hot fix version Patch version Initial release date Type Feature Description

Server 2023 Base 2023/09/18 Enhancement .NET Framework .NET Framework 4.8 and 4.8.1 is now supported.

Server 2023 Base 2023/09/21 Enhancement Active Learning We increased document-to-document speed in active learning queues by approximately 30%.

Server 2023 Base 2023/09/20 Enhancement Active Learning You now have the option to turn off index health documents in an Active Learning Prioritized Review Queue. This allows stable projects to substantially reduce review overhead.

Server 2023 Base 2023/09/19 Enhancement Active Learning Active Learning can now use any single-choice field as its designation, not just fields with exactly two choices. During project setup, one choice is selected as positive, another choice as negative, and the rest of the choices are treated as "neutral" and will not train the model.

Server 2025 Base 2025/12/15 Resolved defect ADS Resolved an issue that caused application imports to fail during validation when they included certain valid Object Rule configurations. The problem would occur because Relativity’s validation logic didn’t properly recognize these configurations as valid, which blocked the application from being installed.

Server 2024 Base 2024/11/15 Enhancement ADS Custom tab icons can now be exported and imported as part of a Relativity application.

Server 2024 Base 2024/11/15 Resolved defect ADS An application will now successfully upgrade when a user publishes a new version using the Publish to Relativity tool even if the application is locked and DeveloperMode is turned off in the instance.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect ADS Resolves an issue where global applications were occasionally incorrectly queued for workspace upgrades, resulting in workspace upgrade failures.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect ADS Update to a LogWarning message for IncompleteTemplateException

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Agents dtSearch Search Agent: Implemented measures to prevent the occurrence of extensive log spams when multiple agents are added to a specific server.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Analytics ARM Restore jobs that include Structured Analytics archives now complete successfully. Previously these restores could fail due to a PostgreSQL 17 incompatibility in CAAT 5.1.0.A1; this is addressed in CAAT 5.1.4.A1.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Analytics CAAT upgrades now complete successfully through the PostgreSQL migration step. Previously, CAAT 5.1.0.A1 upgrades could fail due to an incompatible function in the staging schema; this is resolved in CAAT 5.1.4.A1.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Analytics ARM Restore jobs that include Structured Analytics archives now complete successfully. Previously these restores could fail due to a PostgreSQL 17 incompatibility in CAAT 5.1.0.A1; this is addressed in CAAT 5.1.4.A1.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Analytics CAAT upgrades now complete successfully through the PostgreSQL migration step. Previously, CAAT 5.1.0.A1 upgrades could fail due to an incompatible function in the staging schema; this is resolved in CAAT 5.1.4.A1.

Server 2025 Hot fix CAAT Package-5.1.0.A1 1.0 2026/03/24 Change Analytics This hot fix updates CAAT to version 5.1.0.A1 and upgrades core platform dependencies to supported versions, including JDK 17.0.13, Jetty 12.1.6, and PostgreSQL 17.4, improving security, stability, and platform alignment.

Server 2024 Hot fix CAAT Package-5.1.0.A1 3.1 2026/03/24 Change Analytics This hot fix updates CAAT to version 5.1.0.A1 and upgrades core platform dependencies to supported versions, including JDK 17.0.13, Jetty 12.1.6, and PostgreSQL 17.4, improving security, stability, and platform alignment.

Server 2023 Hot fix CAAT Package-4.7.23.A23 2026/03/24 Change Analytics This hot fix updates CAAT to version 4.7.23.A23 and upgrades core platform dependencies to supported versions, including JDK 17.0.13, Jetty 12.1.6, and PostgreSQL 17.4, improving security, stability, and platform alignment.

Server 2024 Base 2024/11/15 Resolved defect Analytics Resolves an issue where documents listed in the Find Similar Documents card were missing a hyperlink after the control number field had been renamed.

Server 2023 Base 2023/09/22 Deprecation Analytics The Conceptual Resource Manager Agent was removed. Indexes that are inactive for seven (or the configured number of days) will no longer be deactivated.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Analytics Index The Document Exceptions section of the Analytics Index pages now displays all pagination options consistent with other lists in Relativity.

Server 2024 Base 2024/11/15 Resolved defect Application Installation Manager An application will now successfully upgrade when a user publishes a new version using the Publish to Relativity tool even if the application is locked and DeveloperMode is turned off in the instance.

Server 2024 Patch 2.0 2025/08/29 Change Application Library Informational banner on upcoming Server SDK requirements for Relativity Server 2026 now starts collapsed and can be permanently dismissed.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Application Library Cancel button is cut off when choosing a long application name.

Server 2025 Base 2025/12/15 Resolved defect ARM Resolved an issue where workspaces could be restored without audits even though audit data existed in the archive. This occurred when the archive contained empty Audit or DataGrid\Audit directories (for example, when all audits were stored in SQL). The restore process now correctly detects and restores audits from all valid sources and raises an error if audit data is missing.

Server 2024 Hot fix 0.2 1.0 2025/02/06 Resolved defect ARM Resolves an issue where linked natives for documents that have a value populated in the ProcessingFileID field may have been excluded from an archive when using ARM to archive a workspace with “Include Linked Files” enabled. For additional information see knowledge base article REL-1014846

Server 2023 Hot fix Hot fix 18 Patch 3 2025/02/06 Resolved defect ARM Resolves an issue where linked natives for documents that have a value populated in the ProcessingFileID field may have been excluded from an archive when using ARM to archive a workspace with “Include Linked Files” enabled. For additional information see knowledge base article REL-1014846

Server 2023 Patch Patch 2 2024/06/10 Resolved defect ARM Resolves an issue with ARM processing jobs stalling during storage table file copying due to non-repository file endings.

Server 2023 Hot fix Hot fix 6 Patch 2 2024/03/06 Resolved defect ARM Resolves issue where ARM move jobs are failing during restore.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect ARM Update Legal Hold Schema to allow different guides for certain fields.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect ARM Resolves an issue where ARM Move jobs were failing during restore.

Server 2025 Base 2025/12/15 Resolved defect Audit Resolved an issue in the Reviewer Statistics report where total usage time could vary depending on the machine’s time zone. The report now correctly calculates reviewer activity regardless of local browser or system time zone settings.

Server 2025 Base 2025/12/15 Change Audit Relativity Server 2025 is compatible with Elasticsearch 8.x and 9.x. The following versions are officially certified for both Data Grid Audit and Environment Watch: Elasticsearch 8.17.3 Elasticsearch 9.1.3

Server 2024 Patch 2.0 2025/08/29 Resolved defect Audit Resolved an issue where documents with the same artifactID as their workspace could have upload/download audits from unrelated custom RDOs attributed to them.

Server 2024 Patch 1.0 2025/03/21 Enhancement Audit For Server customers that use Data Grid Audit, Server 2024 Patch 1 introduces changes that enable you to cut over to a new authentication architecture for the integration between Relativity and Elasticsearch. Prior to Server 2024 Patch 1, Data Grid Audit relied on an Elasticsearch plug-in called Custom Realms for authentication. Starting with Server 2024 Patch 1, authentication no longer requires Custom Realms and is now based on an API key-based OAuth2 authentication method. Customers will use a new tool called the Relativity Server CLI to cut over to API key-based authentication. Cutting over to API key-based authentication is not required for Data Grid Audit to continue functioning after deploying Server 2024 Patch 1, but all Relativity Server customers that use Data Grid Audit will be required to upgrade to at least Server 2024 Patch 1 and cut over to the new API key-based authentication by early 2026 in order for Data Grid Audit to continue working. The Relativity Community Site article linked below outlines the process for cutting over to API key-based authentication. After cutting over to API key-based authentication, Elasticsearch 8.17 and above is supported for Data Grid Audit (only version 7.17 is supported for Server 2024 if you have not cut over to API key auth). https://community.relativity.com/s/article/Server-Audit-Update-to-basic-license-for-elasticsearch *Additional Note*: Once customers have cut over to the new API key-based authentication, the Elastic Platinum license key that Relativity previously provided as part of our Elasticsearch installation package (“DataTron”) is no longer required to use Data Grid Audit. Moving forward, customers will use the free/open Elastic license, or optionally apply a Platinum or Enterprise license key held by their organization if they are interested in utilizing Elasticsearch features that are not supported under the free/open license. No core Data Grid Audit functionality is impacted when you downgrade to the free/open license.

Server 2025 Base 2025/12/15 Resolved defect Authentication Password reset request are limited to 10. Beyond that limit, the system will block further requests and guide users to contact their administrator for support.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Authentication Resolved an issue that was preventing RSA authentication from functioning properly.

Server 2024 Base 2024/11/15 Resolved defect Authentication Resolved an issue preventing RSA authentication from functioning.

Server 2024 Base 2024/11/15 Resolved defect Authentication Resolved an issue preventing RSA authentication from functioning.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Authentication Logging for OAuth2 clients has been added to enable enhanced troubleshooting of OAuth2-related issues.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Authentication This PR is to cleanup identity rap repo. This will include the removal of Required claims references, JIT settings references

Server 2025 Base 2025/12/15 Change Batch Sets Replaced the Remove Documents from Batch Sets application with the new Batch Set Cleanup (BSC) application. The BSC app provides the same functionality as the previous application, with no need to create or configure any agents. See here for more details: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Batch_Set_Cleanup.htm

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Branding Fixed the defect that occurred when using specific font settings for producing images with small dimensions.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Case Dynamics Case Dynamics interview question text associated with Facts is no longer truncated when exporting reports. The full question text is now included in exported output.

Server 2024 Patch 2.0 2025/08/29 Resolved defect Case Dynamics Resolved an issue in Case Dynamics where creating an Entity from an Outline left the Full Name field blank, causing the entity to appear unnamed in dropdowns and item lists. Entities now correctly display First Name, Last Name, and Full Name in both layout and item list views.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Case Dynamics Case Dynamics timelines can now be successfully saved as XLS or CSV files.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Case Dynamics Case Dynamics timelines can now be successfully saved as XLS or CSV files.

Server 2023 Base 2023/09/23 Enhancement Case Dynamics We updated the Add Fact logic from the Viewer and selected text is no longer copied to the Description field.

Server 2024 Patch 2.0 2025/08/29 Resolved defect Case Metrics Resolved a defect where users were unable to generate a Reviewer OverTurn Report for saved searches containing 150,000 documents. The report now supports large datasets with improved performance and full overturn metrics.

Server 2025 Base 2025/12/15 Resolved defect Coding Pane Fixed an issue where the “Copy from Previous” option disappeared after refreshing or selecting Save and Next.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Coding Pane By repositioning the "saveandnext" completion line, we address a potential race condition in coding-card.ts, which has the potential to lead to form errors.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Conversion Cache Manager Resolved an issue which prevented automatic cleanup of the conversion cache for mass PDFs. Now the cache will automatic remove entries older than 7 days.

Server 2024 Base 2024/11/15 Resolved defect Conversion Cache Manager Resolved an issue which prevented automatic cleanup of the conversion cache for mass PDFs. Now the cache will automatic remove entries older than 7 days.

Server 2024 Base 2024/11/15 Resolved defect Conversion Cache Manager Resolved an issue which prevented automatic cleanup of the conversion cache for mass PDFs. Now the cache will automatic remove entries older than 7 days.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Create Update the UI for workspace level application imports to display errors when the instance level install for that application has errors.

Server 2024 Base 2024/11/15 Resolved defect Custom Pages Improved resiliency and success rate for custom page deployments.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Data Grid Audit Manager It was observed that Data Grid Audit Manager was trying to access a workspace when the workspace upgrade was in progress and then it resulted in error. When workspace upgrade is in progress, Data Grid Audit Manager should not access the workspace and should not spam any error. To fix that, a check for workspace upgrade status is added and some informational logs also included.

Server 2023 Hot fix Hot fix 21 2025/11/20 Resolved defect Data Grid Text Migration Resolved an issue where, during sequential Data Grid Text Migration jobs for multiple long-text fields, previously migrated fields appeared empty in documents if the next field being migrated had no value. Each long-text field now migrates independently, ensuring all text values remain visible and accurate across all documents, regardless of whether other fields contain data.

Server 2024 Hot fix 2.2 3.1 2025/11/18 Resolved defect Data Grid Text Migration Resolved an issue where, during sequential Data Grid Text Migration jobs for multiple long-text fields, previously migrated fields appeared empty in documents if the next field being migrated had no value. Each long-text field now migrates independently, ensuring all text values remain visible and accurate across all documents, regardless of whether other fields contain data.

Server 2024 Hot fix 1.1 2.0 2025/05/14 Resolved defect Data Transfer Users can now specify and retain custom destination paths for load files from the Integration Points frontend.

Server 2023 Base 2023/09/24 Resolved defect Discovery Emails and Calendar items sent using the "On Behalf Of" feature will now correctly display that text in extracted text.

Server 2024 Hot fix 2.7 3.1 2026/03/19 Resolved defect Document List Resolved an issue that could intermittently display an “Unable to get data from server” message on the Document List page during navigation or shortly after field updates. This issue was transient but could disrupt the user experience with unexpected error notifications.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect DropIt An update is done for the setup.bat file to allow all date and time formats, ensuring successful patch installation. This is created to avoid the error that occurred during the creation of sub-folder during extraction. The installation was failing if the date and time format is set to English (United Kingdom) as dd/MM/yyyy or other Formats. The installation is only successful with the English (United States) format. This is addressed as part of update.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Email Files Improved the parsing logic for identifying domains in exchange address.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Email Files Addresses the issue of emails with journaled email attachments, ensuring that their bodies are rendered correctly.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Email Files Resolves an issue where certain Russian and Korean characters were not displayed correctly in extracted text. Please note that this change will alter the deduplication hash of the affected files.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Email Threading Resolved an issue where the "Inclusive Email" field and the "Inclusive" designation in the Email Threading Display field displayed conflicting values.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Email Threading Resolved an issue where email threading thread groups in the Document List and Relational Pane displayed ellipses instead of the correct Inclusive/Non-Inclusive symbols.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Email Threading Resolved an issue where email threading thread groups in the Document List and Relational Pane displayed ellipses instead of the correct Inclusive/Non-Inclusive symbols.

Server 2024 Base 2024/11/15 Resolved defect Email Threading Resolves an issue in email threading where presence of a ">" character in the author/recipient name would result in an incorrect participant merge.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Email Threading Resolves an issue in Email Threading where the presence of unsupported 'When' headers in email 'To' headers resulted in excessive alias merging.

Server 2024 Patch 3.1 2026/06/03 Enhancement Environment Watch Environment Watch continues to expand with a new antivirus dashboard (currently supporting Windows Defender), enhanced file share monitoring for conversion cache and storage health, and deeper visibility into factors that impact review performance. RabbitMQ logs are now centrally available within Environment Watch, simplifying troubleshooting by removing the need to access individual servers. Full details are available on the Environment Watch release page here: https://github.com/relativitydev/server-bundle-release/releases Note: This Environment Watch release is being released in conjunction with Server 2025 Patch 1 but is backward compatible with Relativity Server 2024 Patch 2 and later.

Server 2025 Patch 1.0 2026/05/22 Enhancement Environment Watch Environment Watch continues to expand with a new antivirus dashboard (currently supporting Windows Defender), enhanced file share monitoring for conversion cache and storage health, and deeper visibility into factors that impact review performance. RabbitMQ logs are now centrally available within Environment Watch, simplifying troubleshooting by removing the need to access individual servers. Full details are available on the Environment Watch release page here: https://github.com/relativitydev/server-bundle-release/releases Note: This Environment Watch release is being released in conjunction with Server 2025 Patch 1 but is backward compatible with Relativity Server 2024 Patch 2 and later.

Server 2024 Hot fix 2.6 3.1 2026/03/06 Enhancement Environment Watch This hotfix further reduces telemetry generation in Environment Watch for Server 2024 by an additional 25%, bringing the total reduction to 75% compared to earlier releases.

Server 2025 Base 2025/12/15 Enhancement Environment Watch Environment Watch is now generally available as an optional component for Relativity Server. Learn more about its benefits and capabilities here: https://help.relativity.com/Server2025/Content/Environment_Watch/Environment_Watch_Overview.htm Detailed release notes will be maintained on the Environment Watch GitHub site moving forward, but highlights from our Server 2025 update include: custom JSON configuration enabling users to define monitoring for certificates and Windows services from a central location and enhanced dashboard navigation within Kibana.

Server 2024 Patch 2.0 2025/08/29 Enhancement Environment Watch Environment Watch is now generally available as an optional component for Relativity Server. Detailed release notes will be maintained on the Environment Watch GitHub site moving forward. Learn more about its benefits and capabilities here: https://help.relativity.com/Server2024/Content/Environment_Watch/Environment_Watch_Overview.htm

Server 2024 Patch 1.0 2025/03/21 Resolved defect Errors Timestamp field values on the Errors tab are now displayed in the user's local time zone instead of UTC.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Errors Timestamp field values on the Errors tab are now displayed in the user's local time zone instead of UTC.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Event Handler Framework Resolves an issue of object reference errors occurring during event handler operations. Fields used by event handlers are now required to be declared in the RequireFields property. Only required fields are loaded in event handlers to improve its performance.

Server 2023 Base 2023/09/15 Resolved defect Event Handlers Resolves an issue of object reference errors occurring during event handler operations. Fields used by event handlers are now required to be declared in the RequireFields property. Only required fields are loaded in event handlers to improve its performance.

Server 2025 Base 2025/12/15 Resolved defect Event Handlers Express Creating or editing Event Handler Express automations now works properly in Server 2025—the misleading “You do not have access to view this page” error no longer appears when selecting New Event Handler Express after installing the RAP. The fix removes an incorrect assembly reference that caused this reproducible post-install issue in Server 2024, eliminating the need for IIS restarts or other workarounds.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Extensibility Points Non-temporary Relativity program files are no longer saved in Windows Temp folders. The automatic deletion of files from these folders (e.g. by anti-virus software or Microsoft Storage Sense) would occasionally cause Relativity product functionality issues.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Field Mapping Resolves an issue with Excel Pivot Table Field Mapping enabling seamless Native Extraction

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Field Mapping Resolves an issue where Field Mapping for Excel Pivot Table was not working for Native Extraction

Server 2025 Base 2025/12/15 Resolved defect Fields HTML content in reflected Long Text fields displayed as raw HTML on layouts and views for the associative object type when both 'Enable HTML' and 'Include in Text Index' are enabled.

Server 2024 Patch 2.0 2025/08/29 Resolved defect File Validation Application Resolved an issue where the File Validation Agent application could become nonfunctional and could not be upgraded again after installing version 10.2.7.5

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Find Similar Documents Resolved an issue where documents returned in Find Similar Documents were missing hyperlinks after the Control Number field was renamed.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Find Similar Documents Resolves an issue where viewing of documents beyond the first 1,000 results failed upon clicking Control Number in 'Find Similar Document' Card.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Forms Resolved an issue where removing a value for long text field, resulted in "BLANK" instead of "Null".

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Forms Resolved an issue where removing a value for long text field, resulted in "BLANK" instead of "Null".

Server 2024 Base 2024/11/15 Resolved defect Forms Resolves an issue where the mass edit modal would occasionally appear in the classic forms styling rather than new newer Relativity forms appearance.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Graphical Image Files Arabic, Hebrew, Thai, Vietnamese, and Belarusian unsupported languages show up under 'Default OCR languages' in Processing profile. Processing files with these languages will result in gibberish for OCR extracted text in the viewer.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Image Viewer The Image Viewer now loads correctly when a user has only Redact and Highlight permissions and no markup set is configured.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Image Viewer The Image Viewer now loads correctly when a user has only Redact and Highlight permissions and no markup set is configured.

Server 2023 Hot fix Hot fix 15 Patch 3 2024/10/04 Resolved defect Imaging Fixed an issue where AdminPermissionRepository.IsUserSystemAdminAsync used the workspace UserID instead of the required EDDS UserID, which caused Imaging on the fly to fail. This fix ensures to use correct user id i.e. EDDS UserID

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Include Processing The Processing Migration process will now rely on the Storage table to determine which files to copy, rather than using the Invariant Settings table. This adjustment is made due to the observed inaccuracy in the Settings table, and utilizing the Storage file copy method is expected to provide increased accuracy and speed.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Installation & Deployment Resolved an issue that caused application imports to fail during validation when they included certain valid Object Rule configurations. The problem would occur because Relativity's validation logic didn't properly recognize these configurations as valid, which blocked the application from being installed.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Installation & Deployment You can now use PowerShell 7 to deploy the DropIt package as part of the Server Update Tool exe or legacy DropIt deployment workflow.

Server 2024 Base 2024/11/15 Enhancement Installation & Deployment The About Relativity screen now indicates the hot fix or patch version applied to the instance. Run the Relativity Update Version Check script available in the Relativity Script Library to see the hot fix or patch version applied to each server in an instance.

Server 2023 Patch Patch 1 2024/03/01 Enhancement Instance Details An 'Alerts' indicator in the top right corner of Relativity notifies a user that active alerts are present on the Instance Details tab. Permission to see the Alerts indicator is inherited from Instance Details tab visibility.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Instance Settings Framework Resolves an issue where users occasionally encountered an error when attempting to delete an instance setting immediately after successfully deleting a separate instance setting.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Kepler A potential memory leak in the Kepler Services hosting framework was addressed.

Server 2025 Base 2025/12/15 Resolved defect Layout Manager API Admins who followed the previous QueryCacheMode instance setting guidance may have selected an unsupported value (“SqlDependency”), causing the Document Tab to fail to load. We’ve corrected the description and behavior so that only supported values (TimeBased or None) are used, and any invalid setting now defaults safely to TimeBased.

Server 2024 Patch 2.0 2025/08/29 Resolved defect Layouts Resolved an issue where the Action Bar failed to appear when navigating from a restricted default layout to a non-restricted layout, and where it incorrectly remained visible when moving in the opposite direction. Navigation now properly shows or hides the Action Bar without requiring a page refresh

Server 2024 Patch 2.0 2025/08/29 Resolved defect Legal Hold Legal Hold Portal URL is now correctly populated from the RelativityInstanceURL instance setting by default.

Server 2024 Patch 2.0 2025/08/29 Resolved defect Legal Hold The Insert Link feature is now available in Legal Hold communications to anyone with permission to view and edit communications, without requiring membership in the Legal Hold Admin group.

Server 2023 Base 2023/10/02 Enhancement Legal Hold You can now use modern authentication, certificate based, for setting up Preservation Hold Settings. Basic authentication, username and password, is no longer available for Preservation Hold Settings.

Server 2023 Base 2023/10/01 Resolved defect Legal Hold You can now close projects that have custodians on active Microsoft 365 preservation holds. The holds will automatically be closed as part of closing the project.

Server 2023 Base 2023/09/30 Enhancement Legal Hold You are no longer required to include a portal link for hold notice communications that do not require acknowledgement and do not have an associated questionnaire.

Server 2023 Base 2023/09/29 Enhancement Legal Hold Using an apostrophe in a preservation case name is no longer prohibited.

Server 2023 Base 2023/09/28 Enhancement Legal Hold We added timezone labeling in the legal hold confirmation emails.

Server 2023 Base 2023/09/27 Enhancement Legal Hold We added timezone labeling throughout a variety of lists within the Legal Hold application including within the Mailbox tab.

Server 2023 Base 2023/09/26 Enhancement Legal Hold You can now send legal hold emails using the values set in the instance settings, without having to enter email credentials into a workspace.

Server 2023 Base 2023/09/25 Enhancement Legal Hold You now have increased flexibility to configure escalations, including the number of recurrences, the email subject line, and the email recipient. This offers a customizable experience when including escalations in your legal hold communications.

Server 2023 Base 2023/09/15 Resolved defect Legal Hold Updated the Legal Hold application to save time stamps in UTC going forward. This will decrease discrepancies for customers who have Server time zones set to something other than UTC

Server 2024 Base 2024/11/15 Resolved defect List Page Resolves latency with initial Workspaces list page loads in instances that have a fresh install of Server 2024 or were upgraded to Server 2024 from a version prior to Server 2022

Server 2023 Hot fix Hot fix 10 Patch 2 2024/04/15 Resolved defect List Page Corrects an issue with how the Active Learning "[project name] Reviewed On" field was formatted that could have resulted in incorrect results for saved searches using 'is' conditions on the field.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect List Page When testing a new provisioning pipeline that starts with an environment without any workspaces, Home Page installation failures were observed. Backported the changes for Post Install Event Handler.

Server 2023 Hot fix Hot fix 5 Patch 1 2023/12/04 Resolved defect List Page Updating List Page to disregard carriage returns at the beginning and end of text conditions in saved searches.

Server 2023 Base 2023/10/03 Resolved defect List Page Fixed a responsive UI issue with the Only link in the list filter so that it is now fully visible.

Server 2024 Base 2024/11/15 Enhancement Logging In Server 2024, system health checks are recorded in EDDSLogging as Information level logs. A new rule on the EDDSLogging.Rule table called 'HealthCheck' enables Information level health check logs to be persisted without requiring the overall log level to be set to Information. This rule is enabled by default (set to 2 - Information). For a standard server you can expect to see about 2,000 health check Information level log entries per day

Server 2024 Patch 3.1 2026/06/03 Resolved defect Markup Sets Text redaction values are now isolated per workspace. Resolved an issue where redaction text values could leak across workspaces or continue to appear after the redaction was removed.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Markup Sets Text redaction values are now isolated per workspace. Resolved an issue where redaction text values could leak across workspaces or continue to appear after the redaction was removed.

Server 2025 Base 2026/03/27 Enhancement Migrate Migrate now uses TransferSDK 4.2.0, replacing the legacy TAPI integration. Previous versions of Migrate prior to this update may stop functioning after April 30th as the legacy TAPI integration starts to be decommissioned.

Server 2024 Base 3.1 2026/03/27 Enhancement Migrate Migrate now uses TransferSDK 4.2.0, replacing the legacy TAPI integration. Previous versions of Migrate prior to this update may stop functioning after April 30th as the legacy TAPI integration starts to be decommissioned.

Server 2024 Base 2024/11/15 Enhancement Name Normalization We’ve enhanced Name Normalization with options to analyze only the latest email in a chain and to assign up to 500 aliases to an entity in a single operation.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Network DNS health checks now exclude on-prem server clients reliant on VPNs for communication. This change enhances efficiency and also resolves issues for clients in regions with domain restrictions, like China's inability to resolve some of domains for e.g. google.com.

Server 2025 Base 2025/12/15 Resolved defect Object Manager API The Object Manager export now correctly resumes from the specified start point after a failed run. Previously, when using the {{start}} parameter to restart an export, the API sometimes returned duplicate document batches before continuing normally, preventing reliable data exports via API.

Server 2023 Hot fix Hot fix 4 Patch 1 2023/11/15 Resolved defect Object Manager API The change was to modify the query used, when the condition involved a reflected field for a Choice condition.

Server 2024 Base 2024/11/15 Resolved defect Object Rules If a user is restricted from accessing a layout defined in a 'Default Layout' type Object Rule and the rule condition is met on an object, the user will be shown a message indicating that the layout is not accessible and they will be restricted from accessing any other layout for the object where the rule condition is met. Prior to this change, the user would be presented with another layout that they have access to.

Server 2023 Hot fix Hot fix 14 Patch 3 2024/09/06 Resolved defect Object Rules If a user is restricted from accessing a layout defined in a 'Default Layout' type Object Rule and the rule condition is met on an object, the user will be shown a message indicating that the layout is not accessible and they will be restricted from accessing any other layout for the object where the rule condition is met. Prior to this change, the user would be presented with another layout that they have access to.

Server 2025 Base 2025/12/15 Change OCR For Server 2025, the PDF application is now bundled with the Relativity Server installer. Customers no longer need to deploy this application separately from the main Relativity installation/upgrade.

Server 2023 Base 2023/10/04 Enhancement OCR The OCR engine now provides faster throughput and better text recognition results. These improvements impact non-Latin-based alphabet languages as well.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Permissions In some cases, POST requests were being made as GET requests when called using jQuery Ajax methods with the "type" property used to identify the request type instead of the currently recommended "method" property. In this change, we updated all uses of jQuery Ajax methods to use "method" instead of "type."

Server 2024 Patch 3.1 2026/06/03 Resolved defect Pivot Pivot configuration options now consistently include supported Sort On values and Display Types, including Stacked Bar Chart, for both new and existing Pivot widgets. Previously, some options could be unavailable after upgrading, preventing expected Pivot configurations.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Pivot Pivot XLSX exports now work consistently with corrected sorting enabled. The Export XLSX option no longer becomes disabled when corrected sort is applied to a Pivot.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Pivot Resolved an issue where the Pivot Profile dropdown appeared correctly during the first Pivot creation but disappeared when creating a second Pivot in the same session. This behavior occurred in Server 2024 Patch 2 and Server 2025. The dropdown now loads consistently across all Pivot creation attempts.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Pivot Pivot configuration options now consistently include supported Sort On values and Display Types, including Stacked Bar Chart, for both new and existing Pivot widgets. Previously, some options could be unavailable after upgrading, preventing expected Pivot configurations.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Pivot Pivot XLSX exports now work consistently with corrected sorting enabled. The Export XLSX option no longer becomes disabled when corrected sort is applied to a Pivot.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Pivot Resolved an issue where the Pivot Profile dropdown appeared correctly during the first Pivot creation but disappeared when creating a second Pivot in the same session. This behavior occurred in Server 2024 Patch 2 and Server 2025. The dropdown now loads consistently across all Pivot creation attempts.

Server 2024 Hot fix 2.3 3.1 2025/12/17 Resolved defect Pivot Resolved an issue where the Pivot Profile dropdown appeared correctly during the first Pivot creation but disappeared when creating a second Pivot in the same session. This behavior occurred in Server 2024 Patch 2. The dropdown now loads consistently across all Pivot creation attempts.

Server 2025 Base 2025/12/15 Resolved defect Pivot Resolved an issue where the Pivot Profile dropdown appeared correctly during the first Pivot creation but disappeared when creating a second Pivot in the same session. The dropdown now loads consistently across all Pivot creation attempts.

Server 2025 Hot fix 1.1 2026/06/05 Change Platform This hot fix includes a collection of platform-level security hardening updates and related assembly changes that address and resolve several platform-level security items across key areas of the platform. Impacted components include Workspace Portal, Processing, Analytics, Mass Operations, Legal Hold, dtSearch, and Tab Sync. While there is no known threat or impact to customers at this time, Relativity strongly recommends applying this hot fix to remain aligned with current security best practices. The hot fix includes a Relativity Server Update Tool package, a new version of CAAT (5.1.5.A1), and optional packages for Case Dynamics and Transcripts (both included outside of the Relativity Server Update Tool package).

Server 2023 Hot fix Hot fix 25 2026/05/12 Change Platform This hot fix includes a collection of platform-level security hardening updates and related assembly changes that address and resolve several platform-level security items across key areas of the platform. Impacted components include ARM, dtSearch, Search Term Reports, Imaging, core Relativity UI components, Case Dynamics, and Review. This release also includes the remaining planned security updates for the Server 2023 release line. Although Server 2023 reached end of support on March 31, these updates are being delivered to ensure all in-scope items are addressed in alignment with standard service commitments. While there is no known threat or impact to customers at this time, Relativity strongly recommends applying this hot fix to remain aligned with current security best practices. The hot fix includes a Relativity Server Update Tool package, a new version of CAAT (5.1.4.A1), and new versions of the ARM and Case Dynamics RAPs (both included outside of the Relativity Server Update Tool package).

Server 2025 Hot fix 0.1 1.0 2026/01/23 Change Platform This hot fix includes a collection of platform-level security hardening updates and related assembly changes that address and resolve several platform-level security items. While there is no threat or impact to customers at this time, Relativity strongly recommends applying this hot fix to remain aligned with current security best practices.

Server 2024 Hot fix 2.4 3.1 2026/01/23 Change Platform This hot fix includes a collection of platform-level security hardening updates and related assembly changes that address and resolve several platform-level security items. While there is no threat or impact to customers at this time, Relativity strongly recommends applying this hot fix to remain aligned with current security best practices.

Server 2023 Hot fix Hot fix 22 2026/01/23 Change Platform This hot fix includes a collection of platform-level security hardening updates and related assembly changes that address and resolve several platform-level security items. While there is no threat or impact to customers at this time, Relativity strongly recommends applying this hot fix to remain aligned with current security best practices.

Server 2023 Hot fix Hot fix 13 Patch 3 2024/07/03 Resolved defect Platform Addresses a security vulnerability

Server 2023 Hot fix Hot fix 12 Patch 2 2024/04/24 Resolved defect Platform Addresses a security vulnerability

Server 2023 Hot fix Hot fix 7 Patch 2 2024/03/06 Resolved defect Platform Addresses a security vulnerability

Server 2025 Base 2025/12/15 Resolved defect Processing Resolved an issue that caused the Invariant Queue Manager Service to start with incorrect settings, leading to missing logs and inaccurate reporting.

Server 2025 Base 2025/12/15 Change Processing Relativity Server 2025 supports Microsoft Office 2024, building on the initial availability introduced in Server 2024 Patch 2. Worker servers that run Office 2024 must be on Windows Server 2022. Other server roles (SQL, Web, Agent and others) may remain on their existing operating systems, provided those versions are still supported and you intend to continue using them in their current configurations. Microsoft ended support for Office 2016 on October 14, 2025; upgrading to Office 2024 is recommended to maintain a secure and supported environment. Office 2016 is not officially supported on Server 2025. You may continue using Office 2016 at your own risk, but Relativity does not support Invariant/Processing troubleshooting or provide fixes for Server 2025 environments running Office 2016. For detailed upgrade steps, including removing legacy Office versions and installing Office 2024, see the Upgrading your Workers to Office 2024 page.

Server 2024 Hot fix 2.1 3.1 2025/11/06 Resolved defect Processing Upgraded the third-party json5 package to mitigate a security vulnerability in older versions of the package.

Server 2024 Patch 2.0 2025/08/29 Enhancement Processing The installation of Office 2024 on Worker servers is now supported. Additional details on Office 2024 support including known issues, system requirements, and upgrade considerations are available here: https://help.relativity.com/Server2024/Content/Installing_and_Upgrading/Worker_manager_server_installation/Upgrading_your_Workers_to_Office_2024.htm

Server 2023 Hot fix Hot fix 19 2025/04/18 Resolved defect Processing Resolves an issue where Outlook emails from PST files would sometimes be published with incorrect parent-child relationships when duplicates of those files had previously been deleted post-publish.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Processing Resolved an issue where Scalable Vector Graphs (SVG) files were incorrectly classified as generic TXT files during Processing. This issue was intermittent, affecting only specific versions or types of SVG files due to format differences.

Server 2024 Patch 1.0 2025/03/21 Enhancement Processing Invariant hot fix and patch updates can now be deployed using the Server Update Tool exe which offers a more automated and streamlined deployment experience.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Processing Resolves an issue causing Processing jobs to time out on corrupt OneNote files after 30 minutes. An error will now be shown after 5 minutes of Processing.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Processing Resolved an issue with the "Discovered Files By Custodian" and "Discovered Files By File Type" reports that caused failures for Job IDs exceeding 32 bits.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Processing Resolved an issue where Scalable Vector Graphs (SVG) files were incorrectly classified as generic TXT files during Processing. This issue was intermittent, affecting only specific versions or types of SVG files due to format differences.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Processing Resolves an issue where clicking the "File Errors" link occasionally redirected users to the "Document Errors" tab instead of the intended "Files" tab.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Processing Resolves an issue causing Processing jobs to time out on corrupt OneNote files after 30 minutes. An error will now be shown after 5 minutes of Processing.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Processing Resolved an issue with the "Discovered Files By Custodian" and "Discovered Files By File Type" reports that caused failures for Job IDs exceeding 32 bits.

Server 2024 Base 2024/11/15 Enhancement Processing OCR during Processing now supports Arabic, Hebrew, Thai, and Vietnamese

Server 2024 Base 2024/11/15 Enhancement Processing When processing RSMF files you can now extract files up to 2 GB, map all RSMF 2.0 header metadata, and introduce your own custom X-RSMF headers.

Server 2024 Base 2024/11/15 Resolved defect Processing The relevant error message is now displayed when errors are encountered during new Processing Set creation, rather than a static error message.

Server 2024 Base 2024/11/15 Enhancement Processing For default and new processing profile 'Relativity' is set as default option for office files.

Server 2024 Base 2024/11/15 Resolved defect Processing Improved handling of MHT emails to ensure that the time zone displayed in the viewer matches the metadata settings, resulting in more accurate timestamp.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Processing The Files processed allows all the Errored-out file messages and displays it under the Files section.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Processing Add support for missing reports such as Document Exception report

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Processing Resolves an issue related to broken parent child relationships

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Processing Resolved an issue with the 'Other Fields' filter not functioning correctly for Field Mapping.

Server 2023 Hot fix Hot fix 3 Patch 1 2023/11/13 Resolved defect Processing New and existing Processing jobs are not able to run when upgrading from a pre-Server 2022 version to Server 2023. While processing backfill jobs to populate a new field 'Is Published', Processing set manager throws errors and becomes unresponsive. The issue is happening due to concurrent SQL connection requests which were failing. The fix removes the concurrent calls and resolves the issue.

Server 2023 Base 2023/10/07 Enhancement Processing Removed UvmSqlUser check for Logging.

Server 2023 Base 2023/10/06 Enhancement Processing Fix native imaging issue for Japanese PDF file without embedded fonts.

Server 2023 Base 2023/10/05 Enhancement Processing The Copy mass operation is now available on the Processing Profiles tab.

Server 2023 Base 2023/10/08 Resolved defect Processing Administration Processing Source Locations will function as expected regardless of if the UNC path provided has a trailing slash or not.

Server 2024 Base 2024/11/15 Resolved defect Processing Compressed Files Resolves a Processing issue that occasionally caused unexpected file extrication behavior from zip files encrypted via ZipCrypto.

Server 2024 Base 2024/11/15 Resolved defect Processing Jobs Resolves an issue where clicking on the 'File Errors' link occasionally incorrectly redirected a user to the 'Document Errors' tab instead of the 'Files' tab.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Processing Migration Address the issue to ensure accurate setting of the RetryStatus column.

Server 2023 Hot fix Hot fix 23 2026/02/25 Processing Reports Fixed a security vulnerability in Processing Reports by enforcing anti-CSRF (Cross-Site Request Forgery) protections.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Processing Sets The relevant error message is now displayed when errors are encountered during new Processing Set creation, rather than a static error message.

Server 2023 Base 2023/09/17 Enhancement Product Documentation You can now mouse-over section headings in product documentation to get (and copy) a hyperlink directly to that heading.

Server 2024 Hot fix 0.1 1.0 2024/12/06 Resolved defect Production Addresses a security vulnerability in the Productions application.

Server 2023 Hot fix Hot fix 17 Patch 3 2024/11/27 Resolved defect Production Addresses a security vulnerability in the Productions application.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Production Resolved the issue where Soft-deleted Productions were not appearing in the available list for the Assign Legacy Documents Bates Field script.

Server 2025 Hot fix 0.3 1.0 2026/03/06 Production Placeholder Fixed a security vulnerability (stored cross-site scripting (XSS)) in the Production Placeholder feature.

Server 2024 Hot fix 2.6 3.1 2026/03/06 Production Placeholder Fixed a security vulnerability (stored cross-site scripting (XSS)) in the Production Placeholder feature.

Server 2023 Hot fix Hot fix 24 2026/03/06 Production Placeholder Fixed a security vulnerability (stored cross-site scripting (XSS)) in the Production Placeholder feature.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Production Sets Resolved an intermittent issue where accessing a produced production set sometimes incorrectly showed the option to add or delete a Production Data Source.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Production Sets Resolved an issue that prevented running a production with a copied placeholder.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Production Sets Resolved an intermittent issue where accessing a produced production set sometimes incorrectly showed the option to add or delete a Production Data Source.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Production Sets Resolved an issue that prevented running a production with a copied placeholder.

Server 2023 Hot fix Hot fix 1 Patch 1 2023/11/13 Resolved defect Query There was an error in code path for multi-object when querying with "all of these" condition. Instead of using table-value parameter, we will use CSV in query as default to fix the issue

Server 2024 Patch 3.1 2026/06/03 Change RabbitMQ RabbitMQ 4.2.5 is now supported on Relativity Server 2024 Patch 3 and Server 2025 Patch 1. Relativity has also published a new RabbitMQ Testing, Certification, and Support Policy that clarifies how RabbitMQ versions are selected, tested, and supported across Server major and patch releases. For the current version support matrix and full policy details, see https://help.relativity.com/Server2025/Content/System_Guides/RabbitMQ/RabbitMQ.htm

Server 2025 Patch 1.0 2026/05/22 Change RabbitMQ RabbitMQ 4.2.5 is now supported on Relativity Server 2024 Patch 3 and Server 2025 Patch 1. Relativity has also published a new RabbitMQ Testing, Certification, and Support Policy that clarifies how RabbitMQ versions are selected, tested, and supported across Server major and patch releases. For the current version support matrix and full policy details, see https://help.relativity.com/Server2025/Content/System_Guides/RabbitMQ/RabbitMQ.htm

Server 2025 Base 2025/12/15 Change RabbitMQ RabbitMQ 4.1.4 is now supported. RabbitMQ 4.1.4 requires Erlang 26.2–27.x.

Server 2023 Hot fix Hot fix 8 Patch 2 2024/04/02 Resolved defect RabbitMQ For customers that have previously applied Server 2023 Patch 1, the Conversion Cache Manager is now able to successfully auto-delete expired conversion cache files during the instance off-hours window. If you have not applied Server 2023 Patch 1, this issue will not impact your instance.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect RabbitMQ Code changes for REL-859181-Missing RabbitMQ Bindings are not restored by restarting and version update of ServiceBus

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Redactions & Highlights The API has been enhanced to eliminate the requirement for converting Redaction to RedactionData array and generating additional array copies, effectively resolving the problem of high memory usage on webserver.

Server 2024 Base 2024/11/15 Resolved defect Relational Pane When coding documents using the relational items card in the Viewer, if the user applies an item list filter and selects the ‘All’ mass-coding option in order to make a coding decision, that coding decision is applied to the top (X) documents in the unfiltered document list where (X) is the number of documents that satisfy the filter. This issue has been resolved so that only the filtered documents are mass-coded when the user selects the ‘All’ mass-coding option.

Server 2023 Hot fix Hot fix 15 Patch 3 2024/10/04 Resolved defect Relational Pane When coding documents using the relational items card in the Viewer, if the user applies an item list filter and selects the ‘All’ mass-coding option in order to make a coding decision, that coding decision is applied to the top (X) documents in the unfiltered document list where (X) is the number of documents that satisfy the filter. This issue has been resolved so that only the filtered documents are mass-coded when the user selects the ‘All’ mass-coding option.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Compare Relativity Compare now correctly renders document text when the Extracted Text field is not Unicode-enabled, instead of displaying unsupported characters.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Relativity Compare Resolved an issue where Document Compare would fail if the document system identifier was hardcoded. The true document system identifier will now be automatically detected and used when attempting to run Document Compare.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Relativity Compare Resolved an issue where Document Compare would fail if the document system identifier was hardcoded. The true document system identifier will now be automatically detected and used when attempting to run Document Compare.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Relativity Compare Resolved the issue of missing custom formatting in Document Comparison

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Relativity Compare Doc compare re encoding wrong streaming for other language.

Server 2025 Base 2025/12/15 Resolved defect Relativity Desktop Client Native import via Web/Direct which was showing 0 documents is resolved to show the actual import count accurately.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Relativity Desktop Client RDC installer defaults to a Relativity Server configuration

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Forms Long Text fields with values ending in an ellipsis ("...") now remain fully editable after saving. Previously, these fields were incorrectly set to read-only in Relativity Forms.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Forms The Copy from Previous button in the coding layout now remains visible after a page refresh, instead of being removed from the UI.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Forms The Saved Search field selector now consistently displays the All Fields option alongside any custom Field Categories. Previously, creating a new Field Category could hide the All Fields option from the selector.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Forms Resolved an issue where coding layouts could fail to load with a "The given key was not present in the dictionary" error originating from LayoutRenderHelper. Affected layouts now render correctly without requiring intervention.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Forms Long Text fields with values ending in an ellipsis ("...") now remain fully editable after saving. Previously, these fields were incorrectly set to read-only in Relativity Forms.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Relativity Forms As a consumer of object manager, I want ObjectManager to allow saves to pass on user fields when the value has not changed, even when the user is not in the workspace.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Relativity Forms Exit viewer navigation occasionally fails when navigating to viewer from Forms

Server 2023 Hot fix Hot fix 11 Patch 2 2024/04/24 Resolved defect Relativity Integration Points DNS health checks now exclude on-prem server clients reliant on VPNs for communication. This change enhances efficiency and also resolves issues for clients in regions with domain restrictions, like China's inability to resolve google.com.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Integration Points (RIP) Image import jobs that target a production set with the Auto Number Page option selected no longer fail unexpectedly during overlay-only execution.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Integration Points (RIP) Relativity Integration Points Export jobs using "Folder and Subfolder" as the source now correctly display available views in Step 2 of the wizard and can be submitted successfully.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Integration Points (RIP) The Next Scheduled Runtime column for Relativity Integration Points Export jobs now displays the correct upcoming runtime for both weekly and monthly schedules, instead of showing today's time.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Integration Points (RIP) Image import jobs that target a production set with the Auto Number Page option selected no longer fail unexpectedly during overlay-only execution.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Integration Points (RIP) Relativity Integration Points Export jobs using "Folder and Subfolder" as the source now correctly display available views in Step 2 of the wizard and can be submitted successfully.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Integration Points (RIP) The Next Scheduled Runtime column for Relativity Integration Points Export jobs now displays the correct upcoming runtime for both weekly and monthly schedules, instead of showing today's time.

Server 2024 Patch 2.0 2025/08/29 Resolved defect Relativity Integration Points (RIP) Resolved an issue where the Total of Images field in Integration Points could incorrectly display a byte size of zero; the field now consistently shows the correct image size.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Relativity Integration Points (RIP) When transferring items between workspaces using Integration Points, 'Items Read' is now being correctly calculated as the sum of 'Items Transferred' + 'Items with Errors'. 'Items Read' was previously being calculated as only 'Items Transferred', which resulted in discrepancies in reporting and metrics.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Relativity Integration Points (RIP) Resolved an issue with data field mapping during Integration Points profile migration from Server 2022 to Server 2023. The fix eliminates the need for manual re-update/mapping, which now works automatically.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Relativity Integration Points (RIP) When transferring items between workspaces using Integration Points, 'Items Read' is now being correctly calculated as the sum of 'Items Transferred' + 'Items with Errors'. 'Items Read' was previously being calculated as only 'Items Transferred', which resulted in discrepancies in reporting and metrics.{color}

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Relativity Integration Points (RIP) When a "timeout" occurs for reading data from the snapshot, pressing the "Stop" button on the UI should immediately terminate the process with the status "Stopped." Currently, the process incorrectly returns a status of "Error - Job Failed" instead. This behavior is being adjusted to ensure that the "Stop" action triggers the correct termination status and process terminates immediately.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Relativity Integration Points (RIP) Resolved an issue with data field mapping during Integration Points profile migration from Server 2022 to Server 2023. The fix eliminates the need for manual re-update/mapping, which now works automatically.

Server 2024 Base 2024/11/15 Resolved defect Relativity Integration Points Sync Resolved issue where non-admin users encountered failures during Sync job in newly created Destination Workspace due to missing Tag creation permissions. Implemented solution ensures system objects are now created by Service Account, ensuring seamless job execution.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Relativity Lists Beginning in 2017, if you edited a saved search or view that included a date condition when Daylight Saving Time began or ended, the time component of the search or view would shift back or forward one hour. This only impacted existing saved searches and views and was able to be remediated manually if you corrected the time component change before saving. We developed a SQL script to identify impacted saved searches and a list of Daylight Saving Time dates from 2017 - 2023 by region. Both links along with detailed steps are available in the Community Article. Please review those dates and re-run any saved searches or views with those date conditions.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Relativity Lists The defect has been identified during regression testing of SQL PaaS automatic failover as a solution updated MultiSubnetFailover property set to 'True' in SQL connection string.

Server 2025 Patch 1.0 2026/05/22 Enhancement Relativity Server CLI Automated Elastic Stack installation is now available using the Relativity Server CLI to simplify setup and apply recommended configuration defaults for new installations. This feature is currently in beta, supports single-node deployments only, and will be expanded to include multi-node deployments in a future release. For more details, see here: https://help.relativity.com/topic.html?t=2HC3H

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Server Update Tool Patch and hot fix installations no longer fail on servers configured with multiple roles (for example, combined Agent and Web). The version comparison check now handles multi-role server configurations correctly.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Relativity Update Script The Relativity Update Version Check script now runs reliably. This patch includes an updated version of the script that resolves an intermittent failure preventing it from completing.

Server 2025 Patch 1.0 2026/05/22 Resolved defect Relativity Update Script The Relativity Update Version Check script now runs reliably. This patch includes an updated version of the script that resolves an intermittent failure preventing it from completing.

Server 2024 Base 2024/11/15 Resolved defect Relativity Upgrade Tool Improved resiliency and error reporting for Procuro

Server 2023 Hot fix Hot fix 9 Patch 2 2024/04/08 Resolved defect Reset Password The 'Send Password Reset Email' button on the User object page now successfully sends a password reset email to the respective end user.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Resource Servers Admin Resolves an issue where the 'Delete' button was occasionally displayed on a web server object page despite 'delete' not being a supported action on web servers.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Resource Servers Admin When deleting a Cache Location Server, File Share Server getting an unhelpful error message, fixed the issue by updating proper error message

Server 2023 Base 2023/10/09 Enhancement Review The Edit mass operation is available for Similar Documents and Concept Search cards in the Viewer.

Server 2024 Patch 1.0 2025/03/21 Enhancement Review Interface The Native Viewer now leverages new PDF rendering capabilities, which will support rendering more formatting elements of PDFs, including XFA PDFs. This will provide you with a more stable experience when working with PDFs in Relativity Server. Note: Relativity Processing support for XFA PDFs is not added as part of this update.

Server 2023 Base 2023/10/11 Enhancement Review Interface The Replace Native and Image feature will be implemented in the new Viewer as a drop-down selection from the document name. When clicking on the document name in the Viewer, the option to either Replace document native or Replace images for this document are available. Following this selection, you can select a file to upload.

Server 2023 Base 2023/10/10 Enhancement Review Interface When a coding decision is made, updates to coding layout values visible in the Related Items card will automatically refresh to display those new values. Additionally, any information in the Related Items card can be refreshed whenever the user manually clicks on the Refresh icon in the Related Items card.

Server 2025 Hot fix 0.2 1.0 2026/02/24 Review Interface and Processing Fixed security vulnerabilities in the Review Interface and Processing applications.

Server 2024 Hot fix 2.5 3.1 2026/02/24 Review Interface and Processing Fixed security vulnerabilities in the Review Interface and Processing applications.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Review Service Resolves an issue where Workspace upgrade was throwing an error if the workspace had 0 documents

Server 2023 Hot fix Hot fix 2 Patch 1 2023/11/13 Resolved defect Review Service Backported change to resolve the issue with document history pane not working for clients who do not have Audit app installed/configured

Server 2023 Base 2023/10/14 Enhancement Review-AI Dynamic columns option is now available for Find Similar Documents and Concept Search AI cards in the Viewer.

Server 2023 Base 2023/10/13 Enhancement Review-AI The Copy Selected Keywords option is now available for Keyword Expansion AI card in the Viewer.

Server 2023 Base 2023/10/12 Enhancement Review-AI The Filtering & sorting option is now available for Find Similar Documents, Concept Search and Keyword Expansion AI cards in the Viewer.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Reviewer Interface Resolved an issue preventing non-admin users from selecting cells in Excel in Native viewer.

Server 2023 Base 2023/10/28 Deprecation RSAPI RSAPI endpoints are no longer available for consumption. All applications must use Kepler endpoints instead.

Server 2023 Base 2023/10/15 Deprecation RSAPI RSAPI endpoints are no longer available for consumption. All applications must use Kepler endpoints instead.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect RSMF Files Resolves an issue where the RSMF "MessageHeader" field value was being incorrectly displayed as "Invalid Date"

Server 2024 Base 2024/11/15 Enhancement RSMF Slicing RSMF Slicing will allow customers to create a new RSMF from the original that contains only the relevant messages. This will allow customers to code and produce certain message / portion of the conversation that is relevant. All RSMF slices will be traceable back to the original.

Server 2024 Hot fix 1.1 2.0 2025/05/14 Resolved defect Saved Search Resolved an issue with the 'create search' permission and corrected the improper additional check for Relativity application admin access when creating saved searches.

Server 2023 Hot fix Hot fix 20 2025/05/14 Resolved defect Saved Search Resolved an issue with the 'create search' permission and corrected the improper additional check for Relativity application admin access when creating saved searches.

Server 2024 Base 2024/11/15 Resolved defect Scripts The Case Permission Audit Report will run successfully even when a workspace is marked for deletion.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Scripts Enhanced the error message for cases where failure occurs due to field length issues in the Assign Legacy Document Bates Script.

Server 2024 Patch 1.0 2025/03/21 Resolved defect Search Resolved an issue where users without the 'Add' Search permission could create and run a saved search from the root-level folder in the Saved Searches browser.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect Search Resolved an issue where users without the 'Add' Search permission could create and run a saved search from the root-level folder in the Saved Searches browser.

Server 2024 Hot fix 0.1 1.0 2024/12/06 Resolved defect Search Term Report REL-984271 included in the Server 2024 base release resolved an issue in the population phase of Search Term Reports (STR) where timeouts during the SQL copy of document IDs to a temporary job table could lead to under-inclusive results. The fix also included a detection tool within the dtSearch-Search application that helps users identify impacted STRs. With this hot fix, the detection tool will now work in workspaces where the EDDSDBO.AuditRecord_PrimaryPartition table ID column datatype is set to int. The previous version of the detection tool was only working when the ID column datatype was set to bigint.

Server 2023 Hot fix Hot fix 17 Patch 3 2024/11/27 Resolved defect Search Term Report Server 2023 Hot fix 15 resolved an issue in the population phase of Search Term Reports (STR) where timeouts during the SQL copy of document IDs to a temporary job table could lead to under-inclusive results. The fix also included a detection tool within the dtSearch-Search application that helps users identify impacted STRs. With this hot fix, the detection tool will now work in workspaces where the EDDSDBO.AuditRecord_PrimaryPartition table ID column datatype is set to int. The previous version of the detection tool was only working when the ID column datatype was set to bigint. Note: this hot fix was initially released as a standalone RAP file on 11/15. As of 11/27, the fix is now included as part of a standard cumulative update package.

Server 2024 Base 2024/11/15 Resolved defect Search Term Report Resolved an issue in the population phase of Search Term Reports (STR) where timeouts during the SQL copy of document IDs to a temporary job table could lead to under-inclusive results. This fix ensures accurate and comprehensive reporting, particularly for STRs with document volumes exceeding 20 million. Detection Tool: A detection tool is also included in the new dtSearch-Search application that helps users identify impacted STRs. The detection tool does not currently work in workspaces that do not have the Audit application installed. We will be releasing an updated version of the dtSearch-Search application that resolves the detection tool issue in workspaces where Audit is not installed in the coming days. For workspaces that do not have Audit installed, the STR fix will still be addressed by this hot fix package, but you will need to deploy the new dtSearch-Search application when it becomes available in order to use the detection tool.

Server 2023 Hot fix Hot fix 16 Patch 3 2024/10/09 Resolved defect Search Term Report In Server 2023 Hotfix 15, an issue was resolved in the population phase of Search Term Reports (STR). Specifically, the fix addressed timeouts during the SQL copy of document IDs to a temporary job table, which could lead to under-inclusive results. This fix ensures accurate and comprehensive reporting, particularly for STRs with document volumes exceeding 20 million. It also included a detection tool within the dtSearch-Search application designed to help users identify impacted STRs. However, detection tool was not functional in workspaces where Audit application was not installed. With this release, the detection tool in the dtSearch-Search application has been fixed and is now functional in workspaces without the Audit application.

Server 2023 Hot fix Hot fix 15 Patch 3 2024/10/04 Resolved defect Search Term Report Resolved an issue in the population phase of Search Term Reports (STR) where timeouts during the SQL copy of document IDs to a temporary job table could lead to under-inclusive results. This fix ensures accurate and comprehensive reporting, particularly for STRs with document volumes exceeding 20 million. Detection Tool: A detection tool is also included in the new dtSearch-Search application that helps users identify impacted STRs. The detection tool does not currently work in workspaces that do not have the Audit application installed. We will be releasing an updated version of the dtSearch-Search application that resolves the detection tool issue in workspaces where Audit is not installed in the coming days. For workspaces that do not have Audit installed, the STR fix will still be addressed by this hot fix package, but you will need to deploy the new dtSearch-Search application when it becomes available in order to use the detection tool.

Server 2024 Hot fix 0.1 1.0 2024/12/06 Enhancement Server Update Tool Enhanced the automated Hotfix/Patch installation process to support custom Relativity installation paths, ensuring missing DLLs are addressed when installed in custom locations.

Server 2023 Hot fix Hot fix 17 Patch 3 2024/11/27 Enhancement Server Update Tool Enhanced the automated Hotfix/Patch installation process to support custom Relativity installation paths, ensuring missing DLLs are addressed when installed in custom locations.

Server 2023 Base 2023/10/16 Deprecation Service Bus Service Bus for Windows is no longer supported. You need to convert Service Bus to RabbitMQ before upgrading to Server 2023. Server 2023 supports RabbitMQ version 3.10.x, 3.11.x, and 3.12.x

Server 2023 Base 2023/10/17 Enhancement SQL Server SQL Server 2022 is now supported.

Server 2024 Base 2024/11/15 Resolved defect Structured Analytics Improves resiliency for large, complex email threading jobs.

Server 2024 Base 2024/11/15 Resolved defect Structured Analytics Addresses an issue where Structured Analytics jobs become stuck during the Export phase due to erroneous batch orphaning by the Structured Analytics Manager agent.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Structured Analytics Addresses an issue where Structured Analytics jobs become stuck during the Export phase due to erroneous batch orphaning by the Structured Analytics Manager agent.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Structured Analytics Spamming of logs issue has been fixed.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Structured Analytics When running the "Merge" mass operation from the Entities tab or the "Assign to Entity" mass operation from the Aliases tab, the mass operation progress bar shows the following error message "Failed to check progress of the mass operation". These operations will complete successfully despite the error message.

Server 2023 Base 2023/10/20 Enhancement Structured Analytics You can now copy the results of the domains identified by Name Normalization into new multi-object fields. These new fields remove empty entries, remove duplicated domains, and support expanded filter options. You can also create a tab in your workspace that includes all the domains identified by the Name Normalization to export your results.

Server 2023 Base 2023/10/19 Enhancement Structured Analytics Structured Analytics now appears in Aero styling.

Server 2023 Base 2023/10/18 Enhancement Structured Analytics Signature blocks are no longer considered part of segment bodies when it comes to email threading analysis. This improves how email signature blocks impact the inclusiveness designation of an email are reduces over-inclusiveness based on signature blocks.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Sync Resolved issue where non-admin users encountered failures during Sync job in newly created Destination Workspace due to missing Tag creation permissions. Implemented solution ensures system objects are now created by Service Account, ensuring seamless job execution.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Text Files Resolved an issue where certain RTF content was not processed correctly through our Text Handler, preventing the extraction of text.

Server 2023 Patch Patch 1 2024/03/01 Resolved defect Transcripts In some cases, POST requests were being made as GET requests when called using jQuery Ajax methods with the "type" property used to identify the request type instead of the currently recommended "method" property. In this change, we updated all uses of jQuery Ajax methods to use "method" instead of "type."

Server 2025 Base 2025/12/15 Resolved defect User Group Sync Syncing groups from the master instance to the duplicate instance no longer requires modifying the users in the master instance.

Server 2024 Patch 1.0 2025/03/21 Resolved defect User Group Sync Export functionality for Users, Groups, and Client sections in the User Group Sync Tab has been fixed in this release.

Server 2024 Patch 1.0 2025/03/21 Resolved defect User Group Sync On the 'User Sync Information' tab, clicking on any cell in the '# of Groups' column will now successfully launch the list of groups that the respective user belongs to in the master instance.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect User Group Sync Export functionality for Users, Groups, and Client sections in the User Group Sync Tab has been fixed in this release.

Server 2023 Patch Patch 3 2025/03/21 Resolved defect User Group Sync On the 'User Sync Information' tab, clicking on any cell in the '# of Groups' column will now successfully launch the list of groups that the respective user belongs to in the master instance.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Viewer Resolved an issue where the Extracted Text viewer did not display the full content when the Extracted Text Field was not Unicode-enabled.

Server 2024 Patch 3.1 2026/06/03 Resolved defect Viewer Resolved an issue where large documents intermittently failed to load in the viewer. Instead of consistently showing the file size error, the viewer sometimes displayed a generic “Failed to load content” message. This occurred because the 'MaximumNativeSizeForViewerInBytes' instance setting cache occasionally did not load the configured file size limit.

Server 2025 Base 2025/12/15 Resolved defect Viewer Resolved an issue where the Extracted Text viewer did not display the full content when the Extracted Field was not Unicode-enabled. The viewer now correctly loads and displays the complete text for non-Unicode long text fields.

Server 2025 Base 2025/12/15 Resolved defect Viewer Resolved an issue where large documents intermittently failed to load in the viewer. Instead of consistently showing the file size error, the viewer sometimes displayed a generic “Failed to load content” message. This occurred because the 'MaximumNativeSizeForViewerInBytes' instance setting cache occasionally did not load the configured file size limit. The viewer now reliably displays the appropriate file size error when documents exceed the supported limit.

Server 2024 Base 2024/11/15 Enhancement Viewer When viewing a supported audio/video file, you can toggle on/off the waveform visualization to track the intensity of the sound and skip through silence.

Server 2024 Base 2024/11/15 Enhancement Viewer The Viewer is now able to render Excel comments formatted as Modern Comments.

Server 2024 Base 2024/11/15 Enhancement Viewer Improved navigation experience in the Viewer for PowerPoint comments formatted as Modern Comments

Server 2024 Base 2024/11/15 Enhancement Viewer Microsoft OneNote SOAP/HTTP File is now supported in the native viewer. This enhancement is only available in the GA release starting on 9/6. It is not available in the EA release

Server 2023 Base 2023/10/25 Enhancement Viewer The Export to CSV option is now available for Find Similar Documents, Concept Search, and Keyword Expansion AI cards in the Viewer.

Server 2023 Base 2023/10/24 Enhancement Viewer Save as Search functionality is available for documents in Concept Search and View Similar documents cards in Viewer.

Server 2023 Base 2023/10/23 Enhancement Viewer The Export to CSV option is now available for Find Similar Documents, Concept Search, and Keyword Expansion AI cards in the Viewer.

Server 2023 Base 2023/10/22 Enhancement Viewer Reviewers now have the ability to rotate native documents.

Server 2023 Base 2023/10/21 Deprecation Viewer The Classic Viewer has been removed in Server 2023. Users will no longer have the option to revert to the Classic Viewer. All review functionality is now standardized on the new Viewer introduced with Aero UI. We’re making this change to enable your teams with a faster, more consistent review experience across native, image, and text documents.

Server 2025 Base 2025/12/15 Change Windows Server Windows Server 2025 is now supported.

Server 2023 Base 2023/10/27 Enhancement Windows Server Windows Server 2012 R2 is no longer supported.

Server 2023 Base 2023/10/26 Enhancement Windows Server Windows Server 2022 is now supported.

Server 2023 Patch Patch 2 2024/06/10 Resolved defect Workspace A result column (HttpResponseCode/Message) is added to the WorkspaceCreateRequestGuid table that can indicate whether the request has completed and return the appropriate code. This is done to resolve an issue where workspace creation requests were occasionally duplicated. This ensures proper handling of duplicate requests and provides better visibility into the request outcomes.

Server 2024 Base 2024/11/15 Resolved defect Workspace Creation Resolves an issue where workspace creation requests were occasionally duplicated. This ensures proper handling of duplicate requests and provides better visibility into the request outcomes.

Server 2024 Patch 2.0 2025/08/29 Resolved defect Workspace Details Tab Resolved an issue where editing a workspace via the pencil icon could cause the Status field under Advanced Settings to fail loading, displaying an “Unable to load content” error. This defect no longer occurs and the Status field now loads correctly in all edit scenarios..

Server 2023 Hot fix Hot fix 14 Patch 3 2024/09/06 Resolved defect Workspace Portal Resolves latency with initial Workspaces list page loads in instances that have a fresh install of Server 2023 or were upgraded to Server 2023 from a version prior to Server 2022.

On this page

- Relativity Server release notes


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
