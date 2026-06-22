---
title: "Configure logging"
url: https://help.relativity.com/Server2025/Content/Logging/Configure_logging.htm
collection: user
fetched_at: 2026-06-22T06:03:45+00:00
sha256: f82437045ad215f8ddd6e10a16b0b5394bc7ab196b524551df247065fa0494e4
---

Configure logging Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Configure logging

By default, Relativity logs Errors and Health Checks. (Health Checks log at the Information log level - this is the only subsystem that has a default rule that logs below the Error level). With the default configuration, Error and Health Checks logs are persisted to the system database without requiring the overall log level to be set to Information.

When troubleshooting application problems, use the EDDSLogging database objects and configuration files to change the default configuration and capture the level of detail that meets your needs.

## Configuration defaults

Relativity logging is centrally configured in the EDDSLogging database. Logging config files provides backup for the database logging configuration.

If both the central database configuration is unavailable (for example, due to connection failure) and the logging config files are missing or cannot be parsed because of invalid or malformed XML, no logging takes place.

When troubleshooting Relativity, you can change logging to meet your particular needs by using logging configurations, sinks, and rules.

Logging changes take effect without an IIS reset.

By default logging is enabled for all Relativity modules. See Configurations for more information.

The following are the default logging level, sink, and log file location settings.

#### Default logging level

By default, Relativity logs at the Error (4) level for all machines, systems, subsystems, and applications (except for the Health Check subsystem which by default logs at the Information (2) level to ensure that important health check logs are captured without defaulting all logging to the Information level). For information on changing the logging level, see Rules .

#### Default sink

By default, logs are stored in the EDDSLogging.RelativityLogs database table. For information on changing sinks, see Sinks and Rules .

#### Default log file location

For file logging, the log file location is set by the RELATIVITY_LOGS environment variable.

The Relativity installer does not set RELATIVITY_LOGS . Instead you must set it manually on all machines in the Relativity environment.

You can also change this variable to a direct folder path within the LogConfig.xml file.

#### Restore logging defaults

To restore default logging settings for the database only, execute the ResetToDefault stored procedure in the EDDSLogging database. When this stored procedure runs, it also outputs the results from the PrintCurrentSetup stored procedure. The output is a runnable SQL script of the configuration that was just deleted. If the @WithParamNames bit parameter is set to 1 , the generated script includes the @Param = [Value] notation and additional usage comments.

```text
 EXEC [EDDSLogging].[eddsdbo].[ResetToDefault] @WithParamNames = 1
```

This deletes all custom rules, configurations, and rule-sinks defined for your Relativity environment in the database.

To restore all logging setting back to default and delete all customizations including sinks, run the ResetToDefault_WithSinks stored procedure.

```text
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

## Sinks

The EDDSLogging.SinkType table defines the following sink types:

The EDDSLogging.Sink table defines the available sinks. The entries in EDDSLogging.Sink are linked to the EDDSLogging.SinkType table by TypeID. By default, only the EDDSLogging sink is set up in the Sink table:

The data column accepts JSON-formatted strings for the Sink Type used. The easiest way to insert data is to use the stored procedures.

You can add and update sinks by using the stored procedures in the EDDSLogging database. If a sink with the specified name already exists in the table, it is updated.

### File

Run the EnsureSink_File stored procedure.

```text
EXEC [EDDSLogging].[eddsdbo].[EnsureSink_File] @Name = 'File1', @LogFileLocation = 'C:\Temp\Logs\', @MaxFileSizeInMB = 10000
```

The stored procedure attempts to escape any single backslash to make the LogFileLocation JSON serializable.

### SQL Server

Run the EnsureSink_SQLServer stored procedure.

```text
EXEC [EDDSLogging].[eddsdbo].[EnsureSink_SQLServer] @Name = 'SQL1', @ConnectionString = 'data source=localhost;initial catalog=EDDSLogging;persist security info=False;user id=EDDSdbo;password=FAKE123; workstation id=localhost;packet size=4096', @TableName = 'RelativityLogs'

```

Do not use double-quotes in the connection string because that breaks the eddsdbo.PrintCurrentSetup script. The connection string does not need double quotes to work. The TableName does not need the database schema of the targeted table to work.

Output from running all three of the above scripts:

Note that the data field that defines the sink (for example, the database connection string or file path) must be formatted as JSON and the stored procedures automatically do it for you.

## Rules

Rules defined in the EDDSLogging.Rule table are used to set the logging level for a combination of machine/system/subsystem/application. For more information on identifying Relativity components in logging, see Logging system-subsystem-application matrix .

By default the table contains two rules:

- LoggingLevel 4 (Error) for all machines, systems, subsystems, and applications

- LoggingLevel 2 (Information) for all Health Check subsystem logs. This new default rule was introduced in Server 2024. For a standard server, you can expect to see about 2,000 Health Check Information level log entries per day.

The Order field defines the order in which Relativity logging parses the rule for a given combination of machine/system/subsystem/application. The rule with the lowest Order value is used once machine/system/subsystem/application are matched.

To change the logging level, update the LoggingLevel value. For example, this statement turns logging level up to DEBUG for everything:

```text
update [EDDSLogging].[eddsdbo].[Rule] set LoggingLevel = 1
```

You can define additional rules as necessary. For example, the following rules set logging for all Relativity core agents ('Default' application) on the agent-srv1 machine to INFORMATION and to the Default sink:

- @MachineName is 'agent-srv1'

- @System is set to 'Agent'

- @Subsystem is set to 'RelativityAgent' for core Relativity agents

- @Application is set to null

- @LoggingLevel is set to 2 ( INFORMATION )

- is set to 'Default'

Output:

The rules also add a row to the eddsdbo.RuleSink table to link the sink to the rule.

The following rule turns up logging to INFORMATION only for Relativity telemetry agents (Telemetry Host and Telemetry Metrics Transmission):

- @MachineName is null because telemetry agents run on a single server in the Relativity environment

- @System is set to 'Agent'

- @Subsystem is set to 'CustomAgent' because the agents are part of the telemetry application

- @Application is set to the GUID of the telemetry application ('3d20c75d-e2a8-468d-86c3-7544c035a11d')

- @LoggingLevel is set to 2 ( INFORMATION )

- is set to 'Default'

Output:

The following configuration enables logging for all Relativity services on rel-srv1 to WARNING and to both the Default sink and a File sink:

- @MachineName is 'rel-srv1'

- @System is set to 'RelativityServices'

- @Subsystem is null

- @Application is null

- @LoggingLevel is set to 4 ( WARNING )

- is set to 'Default;File1'

Output:

The configuration also adds two rows to eddsdbo.RuleSink to link the sink to the rule.

Using the eddsdbo.EnsureRule stored procedure, you can remove or add sinks linked to our rule by simply adding or removing them to the parameter. The stored procedure ensures that only the sink names that exists in the value are linked to the rule.

When making changes to logging rules, make sure to select an appropriate logging level to avoid flooding the logs.

### Rules and sinks

The entries in EDDSLogging.RuleSink table associate rules with sinks. You can use the table to set up logging to multiple sinks from a single rule.

By default the table contains only one row:

This instructs the system to log everything to the EDDSLogging.RelativityLogs table. The entries in EDDSLogging.RuleSink are linked to the EDDSLogging.Sink table by name.

## Config files

The logging config files provide a fallback in case of a database connection failure. The files are named LogConfig.xml and are located next to the main configuration file for each Relativity system. The following example shows LogConfig.xml in a production environment, right next to web.config .

#### Default config file

The following is the LogConfig.xml file installed by default for all modules.

```text
<?xml version="1.0" encoding="utf-8" ?>
    <!--Information on how to use this file can be found here https://platform.relativity.com/9.3/Content/Logging/Local_config_files.htm -->
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

<rules enabled>

- Required attributes:

- enabled="true" – if the settings in the file are used and not the database, logging is turned on and the rules in this file apply.

- enabled="false" – if the settings in the file are used and not the database, logging is turned off and the rules in this file are ignored.

<rule system subSystem application loggingLevel sink>

- General information:

- Each rule is read in a top-down manner. Once a logger has found a matching rule, it stops and uses the logging level and sink specified in that rule.

- Required attributes (If these are not specified, the rule fails to initialize):

- loggingLevel – values are Verbose , Debug , Information , Warning , Error , and Fatal .

- sink – value is the exact name of the sink that is defined in the sinks element. Multiple sinks can be included and are semicolon (;) delimited, for example:

```text
sink="MyFileSink" or sink="MyFileSink;MySQLSink;..."
```

If multiple sinks are specified, the same information logged to each sink.

- Optional attributes (If these are not specified or their value="*" , then the rule applies to all items of that type).

- system – values are predefined names of the System this rule applies to.

- subSystem – values are predefined names of the SubSystem this rule applies to.

- application – values are the GUID of the Application this rule applies to.

If you have multiple <rule> elements in the <rules> section, the <rule> elements are evaluated in the order they are found, so you must put more specific rules first. For example, this is how you set logging level to Verbose for the Processing application (specified by GUID) while logging is set to Error for the rest of Relativity:

```text
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

## Example: Increasing logging level for agents

Problems related to Data Grid might require you to increase the logging level for the Data Grid core agents on the appropriate machine to capture additional information. To do that, you must define a new logging rule. The rule can be defined in the database or the logging configuration file.

- Examine the masterLoggingConfiguration property in the C:\Program Files\kCura Corporation\Relativity\Agents\LogConfig.xml file on rel-dg-srv-1 to determine what logging configuration is used.

- If masterLoggingConfiguration="EDDS" , execute the EDDSLogging.eddsdbo.EnsureRule database procedure with the following parameters:

- @MachineName 'rel-dg-srv-1', the name of the agent server where Data Grid Core agents are running

- @System is set to 'Agent'

- @Subsystem is set to 'CustomAgent' because the agents are part of the Data Grid Core application

- @Application is set to the GUID of the Data Grid Core application ('6a8c2341-6888-44da-b1a4-5bdce0d1a383')

- @LoggingLevel is set to 2 ( INFORMATION )

- is set to 'Default' to write to the default sink

- If masterLoggingConfiguration="Local" , define an additional logging rule in the LogConfig.xml file:

```text
<rule system="Agent" subsystem="CustomAgent" application="6a8c2341-6888-44da-b1a4-5bdce0d1a383" loggingLevel="Information" sink="EDDS"/>
```

This sets logging level for Data Grid Core application agents on the rel-dg-srv-1 server to INFORMATION .

## Troubleshoot logging

Logging failures can occur when logging configuration is missing or cannot be processed due the central database connection failure or malformed XML in the config files. If logging for a Relativity component fails to initialize, Windows records error messages in the Event Viewer. Look for the messages in Server Manager > Diagnostics > Event Viewer > Applications and Services Logs > kCura .

On this page

- Configure logging

- Configuration defaults

- EDDSLogging database

- Tables

- Views

- Sinks

- File

- SQL Server

- Rules

- Rules and sinks

- Config files

- Example: Increasing logging level for agents

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
