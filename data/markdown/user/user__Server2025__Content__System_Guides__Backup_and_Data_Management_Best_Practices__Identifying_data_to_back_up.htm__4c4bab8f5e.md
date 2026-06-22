---
title: "Identifying data to back up"
url: https://help.relativity.com/Server2025/Content/System_Guides/Backup_and_Data_Management_Best_Practices/Identifying_data_to_back_up.htm
collection: user
fetched_at: 2026-06-22T06:17:48+00:00
sha256: 2601c512b85a7d69448ea5a61d15da2bd0a0dffd93a3ab49e110fd54cd50a5f2
---

Identifying data to back up Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Identifying data to back up

The following sections provide a comprehensive list of all possible data locations of relevant Relativity files (there may be other areas that relate to custom applications or ISV products). You should also consider these areas when creating a backup inventory.

## Database files

A backup of a SQL database includes the Data file, the Log file, and any additional data files, such as the full-text index catalog. You should preserve and thoroughly document maintenance plans and other SQL configurations to help restore service after an outage. There are many configuration options available with the SQL backup command—understanding them is critical to properly maintaining backup continuity. Both Relativity workspace and processing databases should be backed up.

## Relativity file repositories

Relativity file repositories are locations that Relativity “owns.” That is, Relativity creates and deletes files from these locations when requested.

Relativity File repositories are represented as Resource Servers with a type of Fileshare, and you can view them on the Servers tab.

## File stores

Natives and images loaded with pointers are treated differently. Relativity reads files from file store locations but never deletes the locations, even if the document is deleted from Relativity.

Non-repository files in a workspace's File table are indicated by a 0 value for the InRepository column. This could be Processing data or data loaded from another workspace or disk location that was not copied to the repository. These paths may exist outside of your Relativity fileshare and should be included in your backup strategy for document data.

## Analytics

The Analytics server contains critical information about some configurations and may also be the default location for Analytics indexes. Take care to ensure that this server can be completely restored.

## Cache location

Cache location servers temporarily store natives, images, productions, and other file types the viewer uses. Backing up the cache location is optional but recommended as rebuilding the cache can take much time and planning.

## Configurations

The following sections provide possible data locations for configuration information in Relativity.

### Agents

Relativity retains agent configurations in the database. Backing up the EDDS database effectively preserves all agent configuration data.

### Web

You can customize certain aspects of the Relativity web application. For this reason, you should back up the website files as needed. You can also customize certain configurations in IIS. IIS provides a way to export and save the IIS configuration.

### Ancillary indexes (dtSearch, Analytics)

The configuration of the index specifies the locations of the dtSearch and Analytics indexes. Capture all folders and subfolders.

### Full-text catalogs

The full-text catalog may reside within either the database .mdf file, a separate .ndf file, or a mixture of both. The distribution location of the full-text catalog may vary depending on the age of the instance as well as the original version of SQL.

On this page

- Identifying data to back up

- Database files

- Relativity file repositories

- File stores

- Analytics

- Cache location

- Configurations

- Agents

- Web

- Ancillary indexes (dtSearch, Analytics)

- Full-text catalogs


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
