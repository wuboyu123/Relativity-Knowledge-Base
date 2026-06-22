---
title: "Troubleshoot Relativity using logging"
url: https://help.relativity.com/Server2025/Content/Logging/Troubleshoot_Relativity_using_logging.htm
collection: user
fetched_at: 2026-06-22T06:21:06+00:00
sha256: 76117a79ca0dd73f08f09d73fdb5264fe10adb545509a4ac8859e49a59acdff3
---

Troubleshoot Relativity using logging

# Troubleshoot Relativity using logging

When troubleshooting Relativity, use logging to capture the details to identify the root cause of a problem. Rules allow you to drill down to the root cause by increasing the logging level in the affected area of the application and avoid capturing unnecessary information.

## Set up a logging rule

Logging uses rules to determine how to treat Relativity events. We recommend that you target your logging rule to filter out unrelated events.

Logging applies rules based on the machine name, system, subsystem, and application , in order of the Order field, to determine the logging level and the sinks to log to.

### Order

Rules are processed in order. Logging uses the first valid rule it finds that meets all conditions. If there are two valid rules for a given log message, the first rule is used and the second is ignored.

Example

Rules A and B are both valid for a log event. Rule A has an order value of 1 while Rule B has an order value of 4. Rule A has a Logging Level of Error (4) while Rule B has a logging level of Verbose (0) .

Because A has a lower order, it is processed first, and thus only Error or above is logged.

### Machine name

The Machine column filters the rule to only apply to logging on a specific machine name. A NULL value indicates that there is no filter for machine name so the rule applies to all machines in the Relativity environment.

Example

Rule A has a MachineName of Server1 and is valid only on Server1 . Logging on Server2 ignores Rule A.

### System

System column filters the rule to only apply to logging for that system. A NULL value indicates that there is no filter for system, so the rule applies to all systems.

Example

Rule A has a System value of Relativity.Rest and is valid only for Relativity.Rest . Logging for the Relativity.Services system ignores processing Rule A.

### Subsystem

The SubSystem column filters the rule to only apply to logging for that subsystem. A NULL value indicates that there is no filter for subsystem, so the rule applies to all subsystems.

Example

Rule A has a subsystem value of EventHandler and is valid only for event handlers. Logging for the CustomPage subsystem ignores processing Rule A.

### Application

The Application column filters the rule to only apply to logging for that application. A NULL value indicates that there is no filter for the application.

Example

Rule A has an Application value of 51b4e374-ef1b-43a0-b5a8-e2841ac3efe1 and is valid only for Analytics ( 51b4e374-ef1b-43a0-b5a8-e2841ac3efe1 ). Logging for Imaging ( c9e4322e-6bd8-4a37-ae9e-c3c9be31776b ) ignores processing Rule A.

### LoggingLevel

The LoggingLevel column contains the level at which the rule applies filtering for log events. The logger writes a log event only when it is equal to or higher than the logging level of the rule.

Example

Rule A has a LoggingLevel of Error (4) and logs error- and fatal-level events (4 and 5). Log events that are Warning (3) , Information (2) , Debug (1 ) , and Verbose (0) are ignored.

### Rule sinks

A rule is not complete without a sink. A sink is a destination to which log messages are written. Logging ignores rules without any sinks. The RuleSink table associates rules with sinks. Rules can share a sink and have multiple sinks.

## Troubleshooting example

By default, Relativity logging is set to the Error level (capturing the same details as the Errors tab). The logging database settings are as follows:

EDDSLogging.Rule Table

EDDSLogging.RuleSink Table

This means that if an error occurs anywhere in Relativity, it is logged to the EDDSLogging.RelativityLogs table (the default sink).

Note that the error in the example below initially doesn't provide a lot of troubleshooting information:

```text
<properties>
    <property key="ErrorMessage">The save could not be completed because an error occurred during a Relativity Event Handler save action. Please contact your system administrator</property>
    <property key="StackTrace">SomeApplication.Eventhandler.PreSaveMyObject.Execute().....</property>
    <property key="CastArtifactID">1234567</property>
    <property key="CaseName">Important Case</property>
    <property key="ErrorArtifactID">1068612</property>
    <property key="SourceContext">Relativity.Core.Service.ErrorManager</property>
    <property key="MachineName">Server1</property> <property key="AppDomain">4</property>
    <property key="Application" /> <property key="SubSystem" />
    <property key="System">Relativity</property>
    <property key="ProcessId">29336</property>
</properties>
```

But the MachineName property does tell you that the error occurred on Server1 , and the System property indicates that it occurred in the Relativity system. Use the information to set up a rule to capture additional details.

The ErrorMessage property tells you that the error happened during an event handler save action, so you know you can add subsystem of EventHandler to the new rule. The StackTrace property mentions SomeApplication , and you can add this application's identifier to the rule to make it even more specific.

Use the EnsureRule stored procedure to add the rule:

```text
EXEC [EDDSLogging].[eddsdbo].[EnsureRule] @RuleID = NULL, @Order = 1, @MachineName = 'Server1', @System = 'Relativity', @SubSystem = 'EventHandler', @Application = '99999999-9999-9999-9999-999999999999', @LoggingLevel = 2, @SemiColonDelimetedListOfSinkNames = 'Default'
```

The logging database settings are now:

EDDSLogging.Rule Table

EDDSLogging.RuleSink Table

You have created a new rule using the information from the initial error message to increase our logging level for the component you believe to be causing to the problem to Information (2) . This rule provides more information for troubleshooting. If you aren't getting enough information, you can continue to drill down and increase the logging level to Debug (1) or Verbose (0) .

After you identify the root cause of the problem, remove the new rules you created. This ensures that unnecessary information is not collected and no system performance degradation occurs through additional use of the CPU, disk, database, and network resources. Use the DeleteRule stored procedure to delete the rule:

```text
EXEC [EDDSLogging].[eddsdbo].[DeleteRule] @RuleID = 2
```
