---
title: "Best practices for Relativity scripts"
url: https://platform.relativity.com/Server2025/Content/Scripts/Best_practices_for_Relativity_scripts.htm
collection: developer
fetched_at: 2026-06-22T06:32:16+00:00
sha256: 49c4cc9b2e0b900d934549986a652a7da108eacf5ed5feddb20fe5b4a9cfd09c
---

Best practices for Relativity scripts

# Best practices for Relativity scripts

Relativity Scripts are a tool to access and modify data stored in Relativity SQL databases. Not all data is available in SQL, and data currently in SQL may be migrated to other storage systems. The recommended integration mechanism is to use APIs/Services instead of scripts to avoid future migration or interruption.

You should only use scripts when an appropriate API is not available. Relativity will add new and updated APIs over time - review the available APIs periodically to determine if you can replace a script with an API or REST service call.

If you do use Relativity scripts, review the best practices described below to identify potential issues, and how to avoid them.

## Verify your security permissions

We recommend that only Relativity and SQL experts who are familiar with XML be in charge of creating, testing, maintaining, and altering Relativity scripts.

You must have the appropriate system admin permissions to work with scripts. For more information, see Security and Permissions on the Relativity Server 2025 Documentation site.

## Avoid errors and performance issues

Any statement that can be written in SQL can be written into a Relativity script. In theory, you could create a script that completely erases your workspace's document table.

In addition, some scripts can negatively impact system performance if run during peak hours.

You can avoid these problems by:

- Allowing only experts to write scripts

- Allowing only experts to run scripts

- Testing scripts in test workspaces only, not in those being used for an actual case

## Upgrade scripts for database schema changes

If you use a Relativity script in a custom development project, it is recommended to make a copy of the script and use the copied script in your project. Software updates may modify the scripts provided by Relativity, which could cause unintended results if you use the Relativity-provided scripts directly in your custom development projects.

Data stored in SQL may be migrated to different storage solutions in the future. Applications accessing this data via APIs will not be affected, but any scripts or direct SQL queries will need to be rewritten if the underlying storage mechanism changes.

To test whether your script references need updating, run the SQL portion of the script in SQL Server Management Studio. If the script fails, it will throw an error message and attempt to identify the problem. If it succeeds, it will either advise you how many rows were affected or return the rows queried for.

If you have a Relativity test instance, deploy the latest version and test your scripts prior to upgrading the production environment.

## Contact Support when necessary

Relativity Support is available to assist with any questions, comments, or concerns.

If you are writing scripts, we recommend that you attend infrastructure training to learn more about Relativity architecture. For more information, see Relativity Infrastructure Training .
