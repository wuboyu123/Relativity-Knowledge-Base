---
title: "Logging Configuration APIs"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Relativity_services/Logging_Configuration_APIs.htm
collection: developer
fetched_at: 2026-06-22T06:26:41+00:00
sha256: b577bf06a1849dc703c90dc07af35c57b7874c4e41b40b022773750abf7f736f
---

Logging Configuration APIs

# Logging Configuration APIs

The logging configuration services provide functionality for programmatically interacting with the Relativity logging framework . The following services update logging information stored on the EDDSLogging database:

- Logging Configuration Manager - use this service to create, retrieve, update, or delete the logging configurations. A configuration includes settings for logging information about your Relativity environment. You define a configuration by setting a combination of values for a specific machine, system, subsystem, and application. For more information, see Configurations .

- Logging Rule Manager - use this service to create, retrieve, update, or delete rules that control the logging levels for a Relativity environment. You define a rule by setting values for the logging level, machine, system, and other properties. For more information, see Rules .

- Logging Sink Manager - use this service to create and retrieve various types of sinks. It supports sink types that write messages to files, Data Grid, SQL databases, or the Logentries website. For more information, see Sinks .

You can use these services to simplify the setup of logging through the Relativity logging framework. For example, you may want to use these services when implementing a custom page or application that provides a UI for configuring logging. Your custom UI may provide users with options for adding configurations, rules, and sinks.

## Fundamentals for logging configuration services

In the Services API, the Relativity.Services.LoggingConfig namespace contains the interfaces and other classes required to configure logging. You can use the following interfaces to access the services that support this functionality:

- ILoggingConfigurationManager interface - use this interface to access the Logging Configuration Manager service. It includes the CreateAsync() method for adding or updating configurations, and the DeleteAsync() method for removing a specific configuration from the EDDSLogging database. It provides the GetAllAsync() method for retrieving a collection of existing configurations from the database.

- ILoggingRuleManager interface - use this interface to access the Logging Rule Manager service. It includes the CreateAsync() method for adding or updating a rule, and the DeleteAsync() method for removing a rule. It also provides the GetAllAsync() method for retrieving a collection of rules from the EDDSLogging database.

- ILoggingSinkManager interface - use this interface to access the Logging Sink Manager services. It includes methods for creating file, Data Grid, SQL, and Logentries sinks. It also provides the GetAllAsync() method for retrieving a collection of existing sinks.

In addition, the Relativity.Services.LoggingConfig namespace contains the following classes used in conjunction with these services:

- Configuration class - represents the properties for a logging configuration, which determines how logging should be applied in your Relativity environment. You can specify properties on this class to collect logging information on a specific machine, system, subsystem, and application combination. The methods on the ILoggingConfigurationManager interface use Configuration objects.

- Rule class - represents the logging level applied to specific machine, system, subsystem, application, and sink combination. You can specify properties for the order, logging level, system, and sink on this object. The methods on the ILoggingRuleManager interface use Rule objects.

- Sink class - represents a sink that writes messages to a file, Data Grid, an SQL database, or the Logentries website. You can specify the name of a sink as a property. The methods on the ILoggingSinkManager interface use Sink objects.

### Guidelines for using logging configuration services

Use the following guidelines when working with the logging configuration services:

- Ensure that the user accessing the services is a system admin. Only system admins have access to the logging configuration services.

- Review the following guidelines for working with rules:

- Don't attempt to delete the default logging rule.

- Don't add a rule that duplicates the settings of an existing rule.

## Logging Configuration Manager

The Logging Configuration Manager service supports creating and deleting logging configurations. It also supports retrieving a list of all configurations currently stored in the EDDSLogging database. For more information, see Configurations .

### Retrieve configurations

To retrieve a list of available configurations, call the GetAllAsync() method on the ILoggingConfigurationManager interface. This method returns a collection of Configuration objects representing data stored on the EDDSLogging database. For more information, see Fundamentals for logging configuration services .

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
11
12
13
14
15
16
public async Task<ICollection<Configuration>> GetAllConfigurationsAsync(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    ICollection<Configuration> configurations = null;

    using (ILoggingConfigurationManager proxy = serviceFactory.CreateProxy<ILoggingConfigurationManager>())

        try

        {

            configurations = await proxy.GetAllAsync();

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingConfigurationManager>();

            _logger.LogError(exception, "GetAllAsync call for logging configurations failed.");

        }

    return configurations;

}
```

### Create or update a configuration

You can use the CreateAsync() method on the Logging Configuration Manager service to add a new configuration or update an existing one. To create a new configuration, instantiate a Configuration object with these properties, and pass it as an argument to the CreateAsync() method:

- Order - indicates the sequence in which this configuration is applied. This property is required.

- LoggingEnabled - indicates whether logging is enabled for this configuration. This property is optional.

- MachineName - the optional name of the machine that you want to collect logging information about.

You can specify a combination of the machine, system, subsystem, and application for the collection of logging information.

- System - the optional name of the system that you want to collect logging information about.

- SubSystem - the optional name of the subsystem that you want to collect logging information about.

- Application - the optional GUID of the application that you want to collect logging information about.

To update an existing configuration, you must include Id property when instantiating the Configuration object that you pass to the CreateAsync() method. This value is available on the record for the configuration in the EDDSLogging database, or by calling the GetAllAsync() method. The other properties are optional when updating a configuration.

If you don't supply an Id field for an update operation, the service checks for a matching machine, system, subsystem, and application combination in order to make the update. If the service doesn't find a matching combination, then it creates a new configuration.

The following code sample illustrates how to create a new configuration. It includes the required Order property, and other optional properties for a configuration.

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
public async Task PostConfigurationAsync(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingConfigurationManager proxy = serviceFactory.CreateProxy<ILoggingConfigurationManager>())

        try

        {

            // To update an existing configuration, set the Id property to the Id on an existing Configuration object.

            var newConfiguration = new Configuration()

            {

                Order = 99,

                LoggingEnabled = true,

                MachineName = "YOUR_MACHINE",

                System = "YOUR_AGENT",

                SubSystem = "YOUR_SUB",

                Application = "YOUR_APPLICATION_GUID"

            };

            await proxy.CreateAsync(newConfiguration);

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingConfigurationManager>();

            _logger.LogError(exception, "CreateAsync call for a logging configuration failed.");

        }

}
```

### Delete a configuration

To delete a configuration, use the DeleteAsync() method. You must pass a Configuration object to this method that includes Id property for the configuration that you want removed. Other properties defined on this Configuration object are optional.

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
public async Task DeleteConfigurationAsync(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingConfigurationManager proxy = serviceFactory.CreateProxy<ILoggingConfigurationManager>())

    {

        try

        {

            var configuration = new Configuration()

            {

                Id = 1026, // rule Id

                Order = 99,

                LoggingEnabled = true,

                MachineName = "YOUR_MACHINE",

                System = "YOUR_AGENT",

                SubSystem = "YOUR_SUB",

                Application = "YOUR_APPLICATION_GUID"

            };

            await proxy.DeleteAsync(configuration);

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingConfigurationManager>();

            _logger.LogError(exception, "DeleteAsync call for a logging configuration failed.");

        }

    }

}
```

## Logging Rule Manager

The Logging Rule Manager service supports creating and deleting rules. It also supports retrieving a list of all configurations currently stored in the EDDSLogging database. For more information, see Rules .

### Retrieve rules

To retrieve a list of available rules, call the GetAllAsync() method on the ILoggingRuleManager interface. This method returns a collection of Rule objects representing data stored on the EDDSLogging database. For more information, see Fundamentals for logging configuration services .

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
11
12
13
14
15
16
17
18
19
20

public async Task<ICollection<Rule>> GetAllRulesAsync(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    ICollection<Rule> rules = null;

    using (ILoggingRuleManager proxy = serviceFactory.CreateProxy<ILoggingRuleManager>())

    {

        try

        {

            var ruleManager = GetLoggingRuleManager();

            rules = await ruleManager.GetAllAsync().Result;

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingRuleManager>();

            _logger.LogError(exception, "GetAllAsync call for logging rules failed.");

        }

    }

    return rules;

}
```

### Create or update a rule

You can use the CreateAsync() method on the Logging Rule Manager service to add or update a rule. To create a new rule, instantiate a Rule object with the following properties, and pass it as an argument to this method:

- Order - indicates the sequence in which this rule is applied. This property is required.

- LoggingLevel - controls the amount of information written to the log. This property is required. For more information, see Reading a log entry

- LoggingEnabled - indicates whether logging is enabled for this rule.

- MachineName - the optional name of the machine that the rule is applied to.

You can specify a combination the machine, system, subsystem, and application for the collection of logging information.

- System - the optional name of the system that the rule is applied to.

- SubSystem - the optional name of the subsystem that the rule is applied to.

- Application - the optional GUID of the application that the rule is applied to.

- Sink - an optional sink that you want associated with this rule. You can associate multiple sinks with a rule. If you don't provide a sink, then this property is set to the default value of SQL sink.

To update an existing rule, you must include Id property when instantiating the Rule object that you pass to the CreateAsync() method. This value is available on the record for the rule in the EDDSLogging database, or by calling the GetAllAsync() method. The other properties are optional when updating a rule.

The following code sample illustrates how to create a rule. It includes the required Order and LoggingLevel properties, and other optional properties for a rule.

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
11
12
13
14
15
16
17
18
19
20
21
22
23
public async Task CreateRuleAsync(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingRuleManager proxy = serviceFactory.CreateProxy<ILoggingRuleManager>())

        try

        {

            var newRule = new Rule()

            {

                Order = 99,

                LoggingLevel = "Verbose",

                MachineName = "YOUR_MACHINE",

                System = "YOUR_AGENT",

                SubSystem = "YOUR_SUB",

                Application = "YOUR_APPLICATION_GUID"

            };

            await proxy.CreateAsync(newRule);

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingRuleManager>();

            _logger.LogError(exception, "CreateAsync call for a logging rule failed.");

        }

}
```

### Delete a rule

To delete a rule, use the DeleteAsync() method. You must pass a Rule object to this method that includes Id property for the rule that you want removed. Other properties defined on this Rule object are optional.

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

public async Task DeleteRuleAsyncTask(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingRuleManager proxy = serviceFactory.CreateProxy<ILoggingRuleManager>())

        try

        {

            var rule = new Rule()

            {

                Id = 1097, // rule Id

                Order = 99,

                LoggingLevel = "Verbose",

                MachineName = "YOUR_MACHINE",

                System = "YOUR_AGENT",

                SubSystem = "YOUR_SUB",

                Application = "YOUR_APPLICATION_GUID"

            };

            await proxy.DeleteAsync(rule);

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingRuleManager>();

            _logger.LogError(exception, "DeleteAsync call for a logging rule failed.");

        }

}
```

## Logging Sink Manager

The Logging Sink Manager service supports creating and retrieving sinks. For more information, see Sinks .

### Retrieve sinks

To retrieve a list of available sinks, call the GetAllAsync() method on the ILoggingSinkManager interface. This method returns a collection of Sink objects representing data stored on the EDDSLogging database. For more information, see Fundamentals for logging configuration services .

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
11
12
13
14
15
16
17
18
19

public async Task<ICollection<Sink>> GetAllSinksAsync(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    ICollection<Sink> sinks = null;

    using (ILoggingSinkManager proxy = serviceFactory.CreateProxy<ILoggingSinkManager>())

    {

        try

        {

            sinks = await proxy.GetAllAsync();

        }

        catch (Exception exception)

        {

            // Optionally, define how to display the error message.

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingSinkManager>();

            _logger.LogError(exception, "GetAllAsync call for logging sinks failed.");

        }

    }

    return sinks;

}
```

### Create sinks

Use the methods on the ILoggingSinkManager interface to create a file, Data Grid, SQL database, or Logentries sink.

#### Create file sink

To create a file sink, pass the following arguments to the CreateFileSink() method:

- name - the name of the sink that you want to create.

- logFileLocation - the path to the location where you want to store the log file.

- maxFileSize - indicates the maximum file size (MB) for the log.

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
11
12
13
14
15
public async Task CreateFileSink(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingSinkManager proxy = serviceFactory.CreateProxy<ILoggingSinkManager>())

    {

        try

        {

            await proxy.CreateFileSinkAsync("sink Name", "FILE_LOCATION", 22);

        }

        catch (Exception exception)

        {

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingSinkManager>();

            _logger.LogError(exception, "CreateFileSinkAsync call for a logging sink failed.");

        }

    }

}
```

#### Create a Data Grid sink

To create a Data Grid sink, pass the following arguments to the CreateDataGridSinkAsync() method:

- name - the name of the sink that you want to create.

- dataGridEndPoint - the URL for the Data Grid instance where you want the sink to write messages.

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
11
12
13
14
15
public async Task CreateDataGridSink(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingSinkManager proxy = serviceFactory.CreateProxy<ILoggingSinkManager>())

    {

        try

        {

            await proxy.CreateDataGridSinkAsync("sink Name", "http://localhost/");

        }

        catch (Exception exception)

        {

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingSinkManager>();

            _logger.LogError(exception, "CreateDataGridSinkAsync call for a logging sink failed.");

        }

    }

}
```

#### Create an SQL sink

To create an SQL sink, pass the following arguments to the CreateSqlSinkAsync() method:

- name - the name of the sink that you want to create.

- connectionString - the connection string to the SQL Server where you want the sink to write messages.

- tableName - the name of the database table where you want the messages stored.

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
11
12
13
14
15
16

public async Task CreateSqlSink(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingSinkManager proxy = serviceFactory.CreateProxy<ILoggingSinkManager>())

    {

        try

        {

               await proxy.CreateSqlSinkAsync("sink Name", "connection_string", "table_name");

        }

        catch (Exception exception)

        {

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingSinkManager>();

            _logger.LogError(exception, "CreateSqlSinkAsync call for a logging sink failed.");

        }

    }

}
```

#### Create a Logentries sink

To create a Logentries sink, pass the following arguments to the CreateLogentriesSinkAsync() method:

- name - the name of the sink that you want to create.

- token - the unique identifier for your destination log on the Logentries website. For more information, see Logentries .

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
11
12
13
14
15
16

public async Task CreateLogentriesSink(Relativity.Services.ServiceProxy.ServiceFactory serviceFactory)

{

    using (ILoggingSinkManager proxy = serviceFactory.CreateProxy<ILoggingConfigurationManager>())

    {

        try

        {

            await proxy.CreateLogentriesSinkAsync("sink Name", "token");

        }

        catch (Exception exception)

        {

            ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<ILoggingSinkManager>();

            _logger.LogError(exception, "CreateLogentriesSinkAsync call for a logging sink failed.");

        }

    }

}
```
