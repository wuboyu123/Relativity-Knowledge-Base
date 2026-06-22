---
title: "Configure logging"
url: https://platform.relativity.com/Server2025/Content/Logging/Configure_logging.htm
collection: developer
fetched_at: 2026-06-22T06:29:37+00:00
sha256: eacc34feae60c24f447603aa084f0882608fc411aaa19e8161dabb14b692b9e6
---

Configure logging Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Configure logging

By default Relativity only logs at the ERROR level to the system database. When troubleshooting application problems, use the EDDSLogging database objects and configuration files to change the default configuration and capture the level of detail that meets your specific needs.

See these related pages:

- Logging

- Log from a Relativity application

- Troubleshoot Relativity using logging

- Logging system-subsystem-application matrix

## Configuration defaults

Relativity logging is centrally configured in the EDDSLogging database. Logging config files provides backup for the database logging configuration.

If both the central database configuration is unavailable (for example, due to connection failure) and the logging config files are missing or cannot be parsed because of invalid or malformed XML, no logging takes place.

When troubleshooting Relativity, you can change logging to meet your particular needs by using logging configurations, sinks, and rules.

Logging changes take effect without an IIS reset.

By default logging is enabled for all Relativity modules.

The following are the default logging level, sink, and log file location settings.

#### Default logging level

By default, Relativity logs at the Error (4) level. For information on changing the logging level, see Rules .

#### Default sink

By default, logs are stored in the EDDSLogging.RelativityLogs database table. For information on changing sinks, see Sinks and Rules .

#### Default log file location

For file logging, the log file location is set by the RELATIVITY_LOGS environment variable.

The Relativity installer does not set RELATIVITY_LOGS . Instead you must set it manually on all machines in the Relativity environment.

You can also change this variable to a direct folder path within the LogConfig.xml file.

#### Restore logging defaults

To restore default logging settings for the database only, execute the ResetToDefault stored procedure in the EDDSLogging database. When this stored procedure runs, it also outputs the results from the PrintCurrentSetup stored procedure. The output is a runnable SQL script of the configuration that was just deleted. If the @WithParamNames bit parameter is set to 1 , the generated script includes the @Param = [Value] notation and additional usage comments.

Copy

```text
1
 EXEC [EDDSLogging].[eddsdbo].[ResetToDefault] @WithParamNames = 1
```

This deletes all custom rules, configurations, and rule-sinks defined for your Relativity environment in the database.

To restore all logging setting back to default and delete all customizations including sinks, run the ResetToDefault_WithSinks stored procedure.

Copy

```text
1
 EXEC [EDDSLogging].[eddsdbo].[ResetToDefault_WithSinks] @WithParamNames = 1
```

You can't remove the default values entirely from the database or assign them a higher order value than any other rule or configuration.

## EDDSLogging database

Relativity uses the EDDSLogging database to store logging configuration and as the default sink for Relativity logs. In a distributed environment, it is hosted on the same SQL Server as the EDDS database.

The database objects include tables, views, and stored procedures.

### Tables

- Configuration – stores available logging configurations. For more information, see Configurations .

- LoggingLevel – defines the Relativity logging level values.

- RelativityLogs – stores the Relativity logs.

- Rule – stores the logging rules defined for the Relativity instance. For more information, see Rules .

- RuleSink – stores the records that associate logging rules with sinks. For more information , see Rules and sinks .

- Sink – stores the sinks defined for the Relativity instance. For more information, see Sinks .

- SinkType – defines the Relativity sink types.

### Views

- Rules – provides quick access to the logging rules information defined in the EDDSLogging tables. Selecting from this view returns RuleID , Order , BestGuessLoggingEnabled , MachineName , System , SubSystem , Application , LoggingLevel , and JSON-formatted sink data.

- BestGuessLoggingEnabled – indicates whether logging is enabled for the rule ( 1 – enabled, 0 – not enabled). It takes into consideration the Configuration table and applies it to the rule.

- This field's value is not always accurate if your Configuration setting's MachineName, System, SubSystem, Application fields have "gaps" and don't match those in the rule.

- If your rules and configuration match ( MachineName , System , Application are specified without gaps in both) this field is more accurate.

- To return the exact rule information for the log in question, use the WhatIsMyRule stored procedure.

### Stored procedures

- DeleteRule @RuleID

- Removes the rule and associated rule-sinks for the @RuleID passed in. See example in Troubleshoot Relativity using logging

- EnsureConfiguration @ConfigurationID, @Order, @MachineName, @System, @SubSystem, @Application, @LoggingEnabled

- Ensures that a row exists in the Configuration table for the passed in parameters by inserting a new configuration if the MachineName , System , SubSystem , Application combination does not exist, or updating the Order or LoggingEnabled fields if it does. See example in Configurations .

- Ensures that the other rows' order values are updated according to the passed in @Order value. If the value already exists, the existing order values are incremented by 1 where necessary.

- Ensures that the default configuration (the row with null values for MachineName , System , SubSystem , Application ) has the highest Order value in the table.

- EnsureRule @RuleID, @Order, @MachineName, @System, @SubSystem, @Application, @LoggingLevel, @SemicolonDelimitedListOfSinkNames

- Ensures that a row exists in the Rule table for the passed in parameters by inserting a new Rule when the MachineName , System , SubSystem , Application combination does not exist, or updating when the @RuleID exists and the combination doesn't already exist with a different RuleID . See example in Rules .

- Ensures that the RuleSink pairings match the @SemicolonDelimitedListOfSinkNames passed in. The param is taken literally; it deletes existing RuleSinks that were not included, and inserts RuleSinks that did not exist before.

- Ensures that the other rows' order values are updated according to the passed in @Order value. If the value already exists, the existing order values is incremented by 1 where necessary.

- Ensures that the default configuration has the highest Order value in the table.

- EnsureRuleSinks @RuleID, @SemicolonDelimitedListOfSinkNames

- Ensures that the rule-sink pairings match the @SemicolonDelimitedListOfSinkNames passed in for the @RuleID . The parameter is taken literally; it deletes the existing rows in RuleSink table that are not included in @SemicolonDelimitedListOfSinkNames , and inserts the rows that don't exist.

- EnsureSink @Name, @SinkTypeID, @Data

- Ensures that the sink exists for the passed in parameters.

- @Name is the primary key.

- @SinkTypeID is one of the sink types supported by Relativity (defined in the SinkType table). For more information, see Sinks .

- @Data is the JSON-formatted string defining for the sink.

It is recommended that you use the other available stored procedures ( EnsureSink_DataGrid , EnsureSink_EDDS , EnsureSink_File , and EnsureSink_SQLServer ) for creating sinks because they create a JSON-formatted string for you.

- EnsureSink_EDDS @Name

- Ensures the default EDDSLogging sink exists and creates the expected JSON-formatted value. See example in Sinks .

- EnsureSink_File @Name, @LogFileLocation, @MaxFileSizeInMB

- Ensures the file sink exists and creates the expected JSON-formatted value. See example in Sinks .

- EnsureSink_SQLServer @Name, @ConnectionString, @TableName

- Ensures the database sink exists and creates the expected JSON-formatted value. See example in Sinks .

- PrintCurrentSetup @WithParamNames

- The script generates a dynamic representation of the stored procedures needed to recreate all logging configurations, rules, sinks, and rule-sinks defined in the EDDSLogging database.

- If the @WithParamNames bit parameter is set to 1 , the generated script includes the @Param = [Value] notation and additional usage comments.

- ResetToDefault @WithParamNames

- Deletes all configuration, rules, and rule-sinks in the system and restores the original default logging settings at the Error (4) level to the RelativityLogs table. Note that sinks are not deleted.

- Generates a SQL script to restore the deleted logging settings. Copy and save this output just in case.

- ResetToDefault_WithSinks @WithParamNames

- Deletes all configuration, rules, and rule-sinks in the system and restores the original default logging settings at the Error (4) level to the RelativityLogs table.

- Generates a SQL script to restore the deleted logging settings. Copy and save this output just in case.

- WhatIsMyRule @MachineName, @System, @SubSystem, @Application

- Returns the rule view for the matching combination of machine name, system, subsystem, and application.

- Make sure to pass in all parameters. You can find the machine name, system, subsystem, and application using the information on the Errors tab or in the Relativity logs. For more information, see Troubleshoot Relativity using logging

## Configurations

Logging configurations in the EDDSLogging.Configuration table are used to enable or disable logging for a combination of machine/system/subsystem/application.

Configurations work similarly to logging rules , but they are used to set the LoggingEnabled flag.

By default the table contains only one row:

This enables logging for all systems, subsystems, and applications on all machines in the Relativity environment.

You can define additional configurations as necessary. For example, the following configuration disables logging for all Relativity Agents on the agent-srv1 machine:

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureConfiguration] @ConfigurationID = NULL, @Order = 1, @MachineName = 'agent-srv1', @System = 'Agent', @SubSystem = 'RelativityAgent', @Application = NULL, @LoggingEnabled = 0, @PollingInterval = NULL
```

Output:

The PollingInterval column specifies how quickly changes to this rule are reflected in logging sinks. A NULL value defaults to 30 seconds, and can be optionally overridden. This column must be set to a positive integer. See the following example:

Copy

```text
1
EXEC [eddsdbo].[EnsureConfiguration] @ConfigurationID = 2, @Order = 1, @MachineName = 'agent-srv1', @System = 'Agent', @SubSystem = 'RelativityAgent', @Application = NULL, @LoggingEnabled = 0, @PollingInterval = 300
```

Output:

If you need a logger to update its configuration or rules immediately rather than wait for the polling Interval, you can edit and save the local LogConfig.xml file of the system you want to check.

For example, the polling interval is set to an hour, but the web instance is experiencing errors. You create a new rule for the Relativity web system and increase the logging level to INFORMATION. Instead of waiting an hour for the logger to check in, complete the following steps to manually update the configuration values:

- Log into the machine hosting web instance.

- Navigate to LogConfig.xml file in the C:\Program Files\kCura Corporation\Relativity\EDDS\ folder.

- Open the LogConfig.xml file in a text editor.

- Type a space and then delete the space. You can now save the file. The loggers for this web instance trigger and query the database, and then update their configuration values with your new rule.

The following configuration enables logging for Relativity Services on rel-srv1 :

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureConfiguration] @ConfigurationID = NULL, @Order = 2, @MachineName = 'rel-srv1', @System = 'RelativityServices', @SubSystem = NULL, @Application = NULL, @LoggingEnabled = 1, @PollingInterval = NULL
```

Output:

## Sinks

The EDDSLogging.SinkType table defines the following sink types:

The EDDSLogging.Sink table defines the available sinks. The entries in EDDSLogging.Sink are linked to the EDDSLogging.SinkType table by TypeID. By default, only the EDDSLogging sink is set up in the Sink table:

The data column accepts JSON-formatted strings for the Sink Type used. The easiest way to insert data is to use the stored procedures.

You can add and update sinks by using the stored procedures in the EDDSLogging database. If a sink with the specified name already exists in the table, it is updated.

### File

Run the EnsureSink_File stored procedure.

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureSink_File] @Name = 'File1', @LogFileLocation = 'C:\Temp\Logs\', @MaxFileSizeInMB = 10000
```

The stored procedure attempts to escape any single backslash to make the LogFileLocation JSON serializable.

### SQL Server

Run the EnsureSink_SQLServer stored procedure.

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureSink_SQLServer] @Name = 'SQL1', @ConnectionString = 'data source=localhost;initial catalog=EDDSLogging;persist security info=False;user id=EDDSdbo;password=FAKE123; workstation id=localhost;packet size=4096', @TableName = 'RelativityLogs'
```

Do not use double-quotes in the connection string because that breaks the eddsdbo.PrintCurrentSetup script. The connection string does not need double quotes to work. The TableName does not need the database schema of the targeted table to work.

Output from running all three of the above scripts:

Note that the data field that defines the sink (for example, the database connection string or file path) must be formatted as JSON and the stored procedures automatically do it for you.

## Rules

Rules defined the EDDSLogging.Rule table are used to set the logging level for a combination of machine/system/subsystem/application. For more information on identifying Relativity components in logging, see Logging system-subsystem-application matrix .

By default the table contains only one row:

This sets the logging level to 4 (Error) for all systems, subsystems, and applications on all machines in the Relativity environment.

The Order field defines the order in which Relativity logging parses the rule for a given combination of machine/system/subsystem/application. The rule with the lowest Order value is used once machine/system/subsystem/application are matched.

To change the logging level, update the LoggingLevel value. For example, this statement turns logging level up to DEBUG for everything:

Copy

```text
1
update [EDDSLogging].[eddsdbo].[Rule] set LoggingLevel = 1
```

You can define additional rules as necessary. For example, the following rules set logging for all Relativity core agents ('Default' application) on the agent-srv1 machine to INFORMATION and to the Default sink:

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureRule] @RuleID = NULL, @Order = 1, @MachineName = 'agent-srv1', @System = 'Agent', @SubSystem = 'RelativityAgent', @Application = NULL, @LoggingLevel = 2,@SemicolonDelimitedListOfSinkNames = 'Default'
```

- @MachineName is 'agent-srv1'

- @System is set to 'Agent'

- @Subsystem is set to 'RelativityAgent' for core Relativity agents

- @Application is set to null

- @LoggingLevel is set to 2 ( INFORMATION )

- @SemicolonDelimitedListOfSinkNames is set to 'Default'

Output:

The rules also add a row to the eddsdbo.RuleSink table to link the sink to the rule.

The following rule turns up logging to INFORMATION only for Relativity telemetry agents (Telemetry Host, Telemetry Metrics Transmission, and APM Transmission agent):

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureRule] @RuleID = NULL, @Order = 1, @MachineName = null, @System = 'Agent', @SubSystem = 'CustomAgent', @Application = '3d20c75d-e2a8-468d-86c3-7544c035a11d', @LoggingLevel = 2, @SemicolonDelimitedListOfSinkNames = 'Default'
```

- @MachineName is null because telemetry agents run on a single server in the Relativity environment

- @System is set to 'Agent'

- @Subsystem is set to 'CustomAgent' because the agents are part of the telemetry application

- @Application is set to the GUID of the telemetry application ('3d20c75d-e2a8-468d-86c3-7544c035a11d')

- @LoggingLevel is set to 2 ( INFORMATION )

- @SemicolonDelimitedListOfSinkNames is set to 'Default'

Output:

The following configuration enables logging for all Relativity services on rel-srv1 to WARNING and to both the Default sink and a File sink:

Copy

```text
1
EXEC [EDDSLogging].[eddsdbo].[EnsureRule] @RuleID = NULL, @Order = 2, @MachineName = 'rel-srv1', @System = 'RelativityServices', @SubSystem = NULL, @Application = NULL, @LoggingLevel = 4, @SemicolonDelimitedListOfSinkNames = 'Default;File1'
```

- @MachineName is 'rel-srv1'

- @System is set to 'RelativityServices'

- @Subsystem is null

- @Application is null

- @LoggingLevel is set to 4 ( WARNING )

- @SemicolonDelimitedListOfSinkNames is set to 'Default;File1'

Output:

The configuration also adds two rows to eddsdbo.RuleSink to link the sink to the rule.

Using the eddsdbo.EnsureRule stored procedure, you can remove or add sinks linked to our rule by simply adding or removing them to the @SemicolonDelimitedListOfSinkNames parameter. The stored procedure ensures that only the sink names that exists in the value are linked to the rule.

When making changes to logging rules, make sure to select an appropriate logging level to avoid flooding the logs.

### Rules and sinks

The entries in EDDSLogging.RuleSink table associate rules with sinks. You can use the table to set up logging to multiple sinks from a single rule.

By default the table contains only one row:

This instructs the system to log everything to the EDDSLogging.RelativityLogs table. The entries in EDDSLogging.RuleSink are linked to the EDDSLogging.Sink table by name.

## Config files

The logging config files provide a fallback in case of a database connection failure. The files are named LogConfig.xml and are located next to the main configuration file for each Relativity system. The following example shows LogConfig.xml in a production environment, right next to web.config .

#### Default config file

The following is the LogConfig.xml file installed by default for all modules.

Copy

```text
1
2
3
4
5
6
7
8
9
10
<?xml version="1.0" encoding="utf-8" ?>

    <!--Information on how to use this file can be found here https://help.relativity.com/Server2025/Content/Logging/Configure_logging.htm#Config -->

    <kCuraLogging masterLoggingConfiguration="EDDS">

    <rules enabled="true">

         <rule system="*" loggingLevel="Error" sink="File1"/>

    </rules>

    <sinks>

         <fileSink name="File1" logFileLocation="%RELATIVITY_LOGS%" maxFileSizeInMB ="10000" />

    </sinks>

</kCuraLogging>
```

#### Config file reference

<kCuraLogging masterLoggingConfiguration>

- Required attributes:

- masterLoggingConfiguration="Local" – use the settings in this file.

- masterLoggingConfiguration="EDDS" – connect to the primary SQL Server in your Relativity environment to access the EDDSLogging database. If the connection fails, use the settings in this file.

- Optional attributes:

- pollingInterval=”##” - the number of seconds indicating how often to retry connecting to the database after a connection attempt fails. The value for the pollingInterval attribute must be a positive integer.

<rules enabled>

- Required attributes:

- enabled="true" – if the settings in the file are used and not the database, logging is turned on and the rules in this file apply.

- enabled="false" – if the settings in the file are used and not the database, logging is turned off and the rules in this file are ignored.

<rule system subSystem application loggingLevel sink>

- General information:

- Each rule is read in a top-down manner. Once a logger has found a matching rule, it stops and uses the logging level and sink specified in that rule.

- Required attributes (If these are not specified, the rule fails to initialize):

- loggingLevel – values are Verbose , Debug , Information , Warning , Error , and Fatal .

- sink – value is the exact name of the sink that is defined in the sinks element. Multiple sinks can be included and are semicolon (;) delimited, for example: Copy

```text
1
sink="MyFileSink" or sink="MyFileSink;MySQLSink;..."
```

If multiple sinks are specified, the same information logged to each sink.

- Optional attributes (If these are not specified or their value="*" , then the rule applies to all items of that type).

- system – values are predefined names of the System this rule applies to.

- subSystem – values are predefined names of the SubSystem this rule applies to.

- application – values are the GUID of the Application this rule applies to.

If you have multiple <rule> elements in the <rules> section, the <rule> elements are evaluated in the order they are found, so you must put more specific rules first. For example, this is how you set logging level to Verbose for the Processing application (specified by GUID) while logging is set to Error for the rest of Relativity:

Copy

```text
1
2
3
4
<rules enabled="true">

    <rule application="ed0e23f9-da60-4298-af9a-ae6a9b6a9319" loggingLevel="Verbose" sink="File1"/>

    <rule system="*" loggingLevel="Error" sink="File1"/>

</rules>
```

<sinks>

- General information:

- Each sink type can be included more than once.

- If a name is not unique the first sink found with that name is used.

<fileSink name logFileLocation maxFileSixeInMB>

- Required attributes:

- name – user defined string that links to a rule's sink attribute.

- logFileLocation – absolute path to the location where the log files are saved. You can use the RELATIVITY_LOGS environment variable to specify the default directory portion of log file path.

If you use a relative path for logFileLocation , the output is relative to the location where you are running your application and not to the path of the executable or the bin directory. It is strongly recommended to only use an absolute path.

- maxFileSizeInMB – the max size for a log file can be. Once the max is reached, a new file is created, and the name is suffixed with a number.

<eddsLogSink name>

- General information:

- This sink attempts to find primary Relativity SQL Server with the EDDSLogging database using the connection string that is typically provided in web or app config files of the application.

- Writes the logs into the RelativityLogs table on the EDDSLogging database.

- Required attributes:

- name – user-defined string that links to a rule's sink attribute.

<sqlSink name connectionString tableName>

- Required attributes:

- name – user-defined string that links to a rule's sink attribute.

- connectionString – full connection string of the database that contains the table to log to.

- tableName – name of the table to log to. Table name does not need the schema name.

## Troubleshoot logging

Logging failures can occur when logging configuration is missing or cannot be processed due the central database connection failure or malformed XML in the config files. If logging for a Relativity component fails to initialize, Windows records error messages in the Event Viewer. Look for the messages in Server Manager > Diagnostics > Event Viewer > Applications and Services Logs > kCura .

On this page

- Configure logging

- Configuration defaults

- EDDSLogging database

- Tables

- Views

- Stored procedures

- Configurations

- Sinks

- File

- SQL Server

- Rules

- Rules and sinks

- Config files

- Troubleshoot logging


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
