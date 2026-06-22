---
title: "Logging Configuration Manager services"
url: https://platform.relativity.com/Server2025/Content/REST_API/REST_services/Logging_Configuration_Manager_services.htm
collection: developer
fetched_at: 2026-06-22T06:26:44+00:00
sha256: 1b45efce3712b8b5c995c55d1785723cdd5166ebe6b6a9e2c393db4be640b1a4
---

Logging Configuration Manager services

# Logging Configuration Manager services

The REST API includes services that you can use to interact programmatically with the Relativity logging framework Relativity logging framework . The following services provide endpoints to support this functionality:

- Logging Configuration Manager service - includes endpoints for creating, updating, and deleting configurations. This service also includes an endpoint for retrieving all existing configurations. For more information, see Configure logging .

- Logging Rule Manager service - includes endpoints for creating, updating, and deleting rules. This service also includes an endpoint for retrieving all existing rules. For more information, see Rules .

- Logging Sink Manager service - includes endpoints for creating sinks that write messages to files, Data Grid, SQL databases, or the Logentries website. This service also includes an endpoint for retrieving all existing sinks. For more information, see Sinks .

For example, you may want to use these services when implementing a custom page or application that provides a UI for configuring logging. Your custom UI may provide users with options for adding configurations, rules, and sinks.

The Relativity Services API also provides the same functionality for interacting programmatically with the Relativity logging framework. For more information, see Logging Configuration APIs .

## Client code sample

To interact with an endpoint on one of the logging configuration services, send an HTTP request that makes a POST method call. See the following base URLs for each of the services:

- Logging Configuration Manager service Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Configuration%20Manager/
```

- Logging Rule Manager service Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Rule%20Manager/
```

- Logging Sink Manager service Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Sink%20Manager/
```

You can use the following .NET code as the REST client for interacting with the logging configuration services. The following sample code illustrates how to perform these tasks:

- Instantiate an HttpClient object for sending requests and responses using the URL for an endpoint on one of the logging configuration services. This example uses the Logging Configuration Manager service to retrieve a collection of configurations.

- Set the required headers for the request.

- Set the variable call url to the URL for the retrieval operation.

- Use the PostAsJsonAsync() method to send a post request.

- Return the results of the request.

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
public async Task<ICollection<Rule>> GetAllRules()

{

    ICollection<Rule> rules = null;

    using (HttpClient httpClient = new HttpClient())

    {

        httpClient.BaseAddress =

            new Uri(

                "http://localhost/relativity.rest/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/");

        //Set the required headers.

        httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        httpClient.DefaultRequestHeaders.Add("Authorization",

            "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");

        string url = " Logging Rule Manager/GetAllAsync ";

        rules = await httpClient.PostAsJsonAsync(url, null);

    }

    return rules;

}
```

## Logging Configuration Manager

The Logging Configuration Manager service supports creating and deleting logging configurations. It also supports retrieving a list of all configurations currently stored in the EDDSLogging database. For more information, see Configurations .

### Retrieve configurations

To retrieve a list of all configurations, send a request with this URL on the Logging Configuration Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Configuration%20Manager/GetAllAsync
```

This request doesn't require any input parameters.

The response returns the following fields:

- Id - the Id for the configuration stored on the EDDSLogging database. For more information, see Configure logging .

- Order - indicates the sequence in which this configuration is applied.

- MachineName - the optional name of the machine that you want to collect logging information about.

- System - the optional name of the system that you want to collect logging information about.

- SubSystem - the optional name of the subsystem that you want to collect logging information about.

- Application - the optional GUID for an application that you want to collect logging information about.

- LoggingEnabled - a Boolean flag that indicates whether logging is enabled for this configuration.

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
[

   {

      "Id":3063,

      "Order":2002,

      "MachineName":"",

      "System":"",

      "SubSystem":"",

      "Application":"",

      "LoggingEnabled":true

   }

]
```

### Create or update a configuration

To create or update a new configuration, use the following URL on the Logging Configuration Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Configuration%20Manager/CreateAsync
```

To create a new configuration, the request must include the Order field. The request can optionally include other fields, such as MachineName, System, and others. However, the only required field is the Order field.

To update a configuration, you must provide the Id field. This value is available on the record for the configuration in the EDDSLogging database, or by calling the GetAllAsync() method.

If you don't supply an Id field for an update operation, then the service checks for a matching machine, system, subsystem, and application combination in order to make the update. If the service doesn't find a matching combination, then it creates a new configuration.

The following JSON illustrates how to update an existing configuration. It includes the required Id field, and optional fields for the configuration. For descriptions of these fields, see Retrieve configurations .

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
{

   "configuration":{

      "Id":1153,

      "Order":"20",

      "MachineName":"My Machine",

      "System":"RelativityDistributed",

      "SubSystem":"Container",

      "Application":"3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46",

      "LoggingEnabled":"TRUE"

   }

}
```

The response returns a status code of 200 when the service successfully updates or creates a configuration.

### Delete a configuration

To delete a configuration, use the the following URL on the Logging Configuration Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging Configuration Manager/DeleteAsync
```

The request must include Id field for the configuration that you want to delete. This value is available on the record for the configuration in the EDDSLogging database, or by calling the GetAllAsync() method. The request can optionally include other fields, such as Order, MachineName, and others. However, the only required field is the Id. For descriptions of these fields, see Retrieve configurations .

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
{

   "configuration":{

      "Id":1053,

      "Order":20,

      "MachineName":"My Machine",

      "System":"RelativityDistributed",

      "SubSystem":"Container",

      "Application":"3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46",

      "LoggingEnabled":true

   }

}
```

The response returns a status code of 200 when the service successfully deletes a configuration.

## Logging Rule Manager

The Logging Rule Manager service supports creating and deleting rules. It also supports retrieving a list of all configurations currently stored in the EDDSLogging database. For more information, see Rules .

### Retrieve rules

To retrieve a list of all rules, send a request with this URL on the Logging Rule Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Rule%20Manager/GetAllAsync
```

This request doesn't require any input parameters.

The response returns the following fields:

- Id - the Id for the rule stored on the EDDSLogging database. For more information, see Rules .

- Order - indicates the sequence in which this rule is applied.

- MachineName - the optional name of the machine that the rule is applied to.

- System - the optional name of the system that the rule is applied to.

- SubSystem - the optional name of the subsystem that the rule is applied to.

- Application - the optional GUID of the application that the rule is applied to.

- LoggingLevel - controls the amount of information written to the log. For more information, see Reading a log entry

- Sink - an optional sink that you want associated with this rule. You can associate multiple sinks with a rule. If you don't provide a sink, then this property is set to the default value of SQL sink.

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
[

   {

      "Id":97,

      "Order":10001,

      "MachineName":"",

      "System":"",

      "SubSystem":"",

      "Application":"",

      "LoggingLevel":"Error",

      "Sinks":[

         "default"

      ]

   }

]
```

### Create or update a rule

To create or update a rule, use the following URL on the Logging Rule Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Rule%20Manager/CreateAsync
```

To create a new rule, the request must include the Order and LoggingLevel fields. Set the Id field to null or to -1 to indicate that you want to create a rule. Optionally, include other fields, such as MachineName, System, and others, but only the Order and LoggingLevel fields are required.

To update a rule, you must provide the Id field. This value is available on the record for the configuration in the EDDSLogging database, or by calling the GetAllAsync() method. The request can optionally include other fields, such as MachineName, System, and others. However, only the Id field is required. If you don't supply an Id field, then the service creates a new rule.

The following JSON illustrates how to create a rule. It includes the required Order and LoggingLevel fields set to 1000 and Verbose respectively. The Id field is set to -1 , which indicates a rule should be created. Additionally, the request includes other optional fields. For descriptions of these fields, see Retrieve rules .

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
{

   "rule":{

      "Id":"-1",

      "Order":"1000",

      "MachineName":"My Machine",

      "System":"Relativity",

      "SubSystem":"Container",

      "Application":"3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46",

      "LoggingLevel":"Verbose",

      "Sinks":[

         "default"

      ]

   }

}
```

The response returns a status code of 200 when the service successfully updates or creates a rule.

### Delete a rule

To delete a rule, send a request with this URL on the Logging Rule Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Rule%20Manager/DeleteAsync
```

The request must include Id field for the rule that you want to delete. This value is available on the record for the configuration in the EDDSLogging database, or by calling the GetAllAsync() method. The request can optionally include other fields, such as Order, MachineName, and others. However, the only required field is the Id. For descriptions of these fields, see Retrieve rules .

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
{

   "rule":{

      "Id":1153,

      "Order":1000,

      "MachineName":"My Machine",

      "System":"Relativity",

      "SubSystem":"Container",

      "Application":"3E86B18F-8B55-45C4-9A57-9E0CBD7BAF46",

      "LoggingLevel":"Verbose",

      "Sinks":[

         "default"

      ]

   }

}
```

The response returns a status code of 200 when the service successfully deletes a rule.

## Logging Sink Manager

The Logging Sink Manager service supports creating and retrieving sinks. For more information, see Sinks .

### Retrieve sinks

To retrieve a list of all sinks, send a request with this URL on the Logging Sink Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Sink%20Manager/GetAllAsync
```

This request doesn't require any input parameters.

The response returns the names of the sinks currently stored on the EDDSLogging database.

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
[

   {

      "Name":"datagrid"

   },

   {

      "Name":"default"

   },

   {

      "Name":"file1"

   },

   {

      "Name":"logentries 1"

   },

   {

      "Name":"sqlsource"

   }

]
```

### Create sinks

Use the methods on the Logging Sink Manager service to create a file, Data Grid, SQL database, or Logentries sink.

#### File sinks

To create a file sink, use the following URL on the Logging Sink Manager service:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Sink%20Manager/CreateFileSink
```

The request must include the following fields:

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
{

   "name":"file_sink_name",

   "logFileLocation":"log_file_location",

   "maxFileSize":"200"

}
```

The response returns a status code of 200 when the service successfully creates a sink.

#### Create Data Grid sink

To create a Data Grid sink, use the following URL on the Logging Sink Manager service:

Copy

```text
1
<host>/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Sink%20Manager/CreateDataGridSink
```

The request must include the following fields:

- name - the name of the sink that you want to create.

- dataGridEndPoint - the URL for the Data Grid instance where you want the sink to write messages.

Copy

```text
1
2
3
4
{

   "name":"sink_name",

   "dataGridEndPoint":"http://localhost/"

}
```

The response returns a status code of 200 when the service successfully creates a sink.

#### Create SQL sink

To create an SQL sink, use the following URL on the Logging Sink Manager service:

Copy

```text
1
<host>/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Sink%20Manager/CreateSqlSink
```

The request must include the following fields:

- name - the name of the sink that you want to create.

- connectionString - the connection string to SQL Server where you want the sink to write messages.

- tableName - the name of the database table where you want the messages stored.

Copy

```text
1
2
3
4
5
{

   "name":"sink_name",

   "connectionString":"connection_string",

   "tableName":"sample_table_name"

}
```

The response returns a status code of 200 when the service successfully creates a sink.

#### Create a Logentries sink

To create a Logentries sink, use the following URL on the Logging Sink Manager service:

Copy

```text
1
<host>/Relativity.Services.LoggingConfig.ILoggingConfigModule/Logging%20Sink%20Manager/CreateLogentriesSink
```

The request must include the following fields:

- name - the name of the sink that you want to create.

- token - the unique identifier for your destination log on the Logentries website. For more information, see Logentries .

Copy

```text
1
2
3
4
{

   "name":"sink_name",

   "token":"sample_token"

}
```

The response returns a status code of 200 when the service successfully creates a sink.
