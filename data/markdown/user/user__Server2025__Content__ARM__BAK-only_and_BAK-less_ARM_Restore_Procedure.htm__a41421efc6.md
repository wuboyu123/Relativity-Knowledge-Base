---
title: "BAK-only ARM Restore Procedure"
url: https://help.relativity.com/Server2025/Content/ARM/BAK-only_and_BAK-less_ARM_Restore_Procedure.htm
collection: user
fetched_at: 2026-06-22T06:17:11+00:00
sha256: aaa3746fbbbfc4fb024c0e0c1804c8edec2d6386f4dbe87c6ddcb46280f6c774
---

BAK-only ARM Restore Procedure Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# BAK-only and BAK-less ARM Restore Procedure

- The BAK-only restore process is not available in RelativityOne.

- Analytics, Processing, and Data Grid data is not restorable with BAK-only restore.

## BAK-only ARM Restore Procedure

### Database Restore (BAK-only) job prerequisite

Before performing a Database Restore (BAK-only) job you must first perform the following procedure:

- The user must restore the database to the new environment.

If you are restoring the database manually to SQL the name of the database must be in the EDDSxxxxxxx format, for example EDDS9999999. If the name is not in this format, you will not see it in the Database drop down on the New Restore Job page.

- Resolve orphaned users on the database either manually or through running an ARM stored procedure targeting the new database.

To do this manually, use the following to directly change the SQL code:

Set @databaseName to the restored database's name.

DECLARE @databaseName NVARCHAR(50) = 'databaseName';

DECLARE @defaultSchema NVARCHAR(50) = 'EDDSDBO';

DECLARE @sql NVARCHAR(max) =N'EXEC ' + QUOTENAME(@databaseName) + N'..sp_executesql @tsql;'

DECLARE @params NVARCHAR(MAX) =N'@tsql nvarchar(max)';

DECLARE @tsql NVARCHAR(max);

SET @tsql=N'

IF NOT EXISTS (SELECT * FROM sys.sysusers WHERE sid=SUSER_SID(N''EDDSDBO''))

BEGIN

IF USER_ID(N''EDDSDBO'') IS NULL

BEGIN

CREATE USER EDDSDBO FROM LOGIN EDDSDBO WITH DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ELSE

BEGIN

ALTER USER EDDSDBO WITH LOGIN = EDDSDBO, DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ALTER ROLE [db_owner] ADD MEMBER EDDSDBO;

END

IF EXISTS(SELECT * FROM master.sys.sql_logins WHERE sid=SUSER_SID(N''RelativityScriptLogin''))

BEGIN

IF NOT EXISTS (SELECT * FROM sys.sysusers WHERE sid=SUSER_SID(N''RelativityScriptLogin''))

BEGIN

IF USER_ID(N''RelativityScriptUser'') IS NULL

BEGIN

CREATE USER RelativityScriptUser FROM LOGIN RelativityScriptLogin WITH DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ELSE

BEGIN

ALTER USER RelativityScriptUser WITH LOGIN = RelativityScriptLogin, DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ALTER ROLE [db_owner] ADD MEMBER RelativityScriptUser;

END

END';

EXEC sp_executesql @sql, @params, @tsql;

- See Creating and running a Restore job to complete the Database Restore (BAK-only) job.

Application mapping is not available during a BAK-only restore, the Next button will be grayed out.

### DtSearch migration

Complete the following steps to manually place the dtSearch in the new locations after the Database Restore (BAK-only) job.

- Run the following query against the primary SQL server:

SELECT ArtifactID as indexShareCodeArtifactId, Name as Location FROM [EDDS].[EDDSDBO].[Code] WHERE CodeTypeID =

(SELECT CodeTypeID FROM [EDDS].[EDDSDBO].[CodeType] WHERE Name = 'dtSearchIndexShareLocation')

- Run the following query against the SQL server where the case is located:

UPDATE [EDDS{CaseId}].[EDDSDBO].[dtSearchIndex]

SET [Location] = Replace([Location],'dt_{oldCaseId}','dt_{CaseId}'), IndexShareCodeArtifactID = {indexShareCodeArtifactId}

Set the following:

- {CaseId} —with the current case (workspace) id.

- {oldCaseId} —with the former case id.

- {indexShareCodeArtifactId} —with the desired indexShareCodeArtifactId from the first query.

- Move the dtSearch data into the new dtSearch location associated with the indexShareCodeArtifactId from the first query.

### Repository file migration

Complete the following steps to manually place the repository files in the new locations after the Database Restore (BAK-only) job.

- Run the following query against the primary SQL server:

SELECT Name as Location FROM [EDDS].[EDDSDBO].[ResourceServer]

WHERE ArtifactID = (SELECT DefaultFileLocationCodeArtifactID FROM [EDDS].[EDDSDBO].[Case] WHERE ArtifactId = {CaseId})

Set {CaseId} with the current case (workspace) id.

- For each former file repository in the old workspace, run the following query:

UPDATE [EDDS{CaseId}].[EDDSDBO].[File]

SET [Location] = Replace([Location], '{oldFileRepository}\EDDS{oldCaseId}', '{fileRepository}\EDDS{CaseId}')

WHERE InRepository = 1

Set the following:

- {CaseId} —with the current case (workspace) id.

- {oldCaseId} —with the former case id.

- {oldFileRepository} —with the former file repository* and case that should be replaced.

- {fileRepository} —with the Location returned from the first query.

*Former File repositories are not easily discernable through a generic query. The best way to determine these post Restore is to look at values from the [EDDS{CaseId}].[EDDSDBO].[File] table and look at non-unique parts of the locations. For example, \\SomeRelativityServer\Repository from the file \\SomeRelativityServer\Repository\EDDS1017866\RV_bc550609-d773-40c2-b9ca-69797b7a2e8c\5c12c2d1-22f7-4908-af56-136189cc5d4a .

- Move the files from the case into the new {fileRepository}\{CaseId} location.

## BAK-less ARM Restore Procedures

ARM allows you to exclude the database backup from the archive. To restore the workspace without a backup file in the archive location, create the backup in the source SQL server and restore BAK in the designated SQL server by completing the following steps:

- Create a Archive Job without a database backup. For more information, see Creating and running an Archive job .

The folder database in an archive should not have a BAK file.

- Manually create the database back-up of the workspace on the source SQL server.

- Manually restore the database on the target SQL server before running a new Restore Job.

If you are restoring the database manually to SQL the name of the database must be in the EDDSxxxxxxx format, for example EDDS9999999. If the name is not in this format, you will not see it in the Database drop down on the New Restore Job page.

- Resolve orphaned users on the database either manually or through running an ARM stored procedure targeting the new database.

To do this manually, use the following to directly change the SQL code:

Set @databaseName to the restored database's name.

DECLARE @databaseName NVARCHAR(50) = 'databaseName';

DECLARE @defaultSchema NVARCHAR(50) = 'EDDSDBO';

DECLARE @sql NVARCHAR(max) =N'EXEC ' + QUOTENAME(@databaseName) + N'..sp_executesql @tsql;'

DECLARE @params NVARCHAR(MAX) =N'@tsql nvarchar(max)';

DECLARE @tsql NVARCHAR(max);

SET @tsql=N'

IF NOT EXISTS (SELECT * FROM sys.sysusers WHERE sid=SUSER_SID(N''EDDSDBO''))

BEGIN

IF USER_ID(N''EDDSDBO'') IS NULL

BEGIN

CREATE USER EDDSDBO FROM LOGIN EDDSDBO WITH DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ELSE

BEGIN

ALTER USER EDDSDBO WITH LOGIN = EDDSDBO, DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ALTER ROLE [db_owner] ADD MEMBER EDDSDBO;

END

IF EXISTS(SELECT * FROM master.sys.sql_logins WHERE sid=SUSER_SID(N''RelativityScriptLogin''))

BEGIN

IF NOT EXISTS (SELECT * FROM sys.sysusers WHERE sid=SUSER_SID(N''RelativityScriptLogin''))

BEGIN

IF USER_ID(N''RelativityScriptUser'') IS NULL

BEGIN

CREATE USER RelativityScriptUser FROM LOGIN RelativityScriptLogin WITH DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ELSE

BEGIN

ALTER USER RelativityScriptUser WITH LOGIN = RelativityScriptLogin, DEFAULT_SCHEMA=' + QUOTENAME(@defaultSchema) + N';

END

ALTER ROLE [db_owner] ADD MEMBER RelativityScriptUser;

END

END';

EXEC sp_executesql @sql, @params, @tsql;

- Create a new Restore Job, under Archive file select Archive without database backup . For more information, see Creating and running a Restore job .

- Under Existing Target Database in the Restore Job, select the previously restored database.

On this page

- BAK-only and BAK-less ARM Restore Procedure

- BAK-only ARM Restore Procedure

- Database Restore (BAK-only) job prerequisite

- DtSearch migration

- Repository file migration

- BAK-less ARM Restore Procedures


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
