---
title: "Troubleshoot REST API errors"
url: https://platform.relativity.com/Server2025/Content/REST_API/Troubleshooting/Troubleshooting_the_REST_API.htm
collection: developer
fetched_at: 2026-06-22T06:29:49+00:00
sha256: d30ba90ca53c9b072c8707756eeb28d5a60703a281223d7979eab8ea8ddba545
---

Troubleshoot REST API errors Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Troubleshoot REST API errors

Use the information in the following sections to troubleshoot operations performed through the REST API.

## HTTP method fails

The REST API returns a message in the JSON response when an error occurs during an operation. For example, you execute a GET request which does not support the start parameter as illustrated here:

Copy

```text
1
2

GET http://localhost/Relativity.REST/Workspace/1017955/Document/QueryResult?start=12
```

The operation returns a status code of 400, and the response contains the message:

Copy

```text
1
2
3
4

{

     "Message":"There is an invalid parameter in the query string: start"

}
```

If you perform a GET for a Document that doesn't exist, as illustrated here:

Copy

```text
1
2

GET http://localhost/Relativity.REST/Workspace/1017955/Document/1234567
```

The operation returns a status code of 404, and the response contains the message:

Copy

```text
1
2
3
4

{

     "Message":"Artifact cannot be found."

}
```

### Incorrect maxRequestLength parameter

If a Relativity.REST API operation contains a very large payload, for example, a saved search with long search string or a complex set of set of conditions, the operation may fail with a status code of 400 and the following message:

Copy

```text
1
"Maximum request length exceeded. Request content length:{0} > Max request length:{1}"
```

This issue occur if the maximum request length for the service is set to a low value. The error may be resolved by increasing the value of the maxRequestLength parameter in the httpRuntime section of the Relativity.REST web.config file. For more information about the option, see MSDN documentation .The default value is 4096 (4 MB).

On a developer test VM, you can correct this issue by editing the maxRequestLength parameter in the Relativity.Services.ServiceHost.exe.config file. This file is available in the following locations:

- C:\Program Files\kCura Corporation\Relativity\ServiceHost\bin directory

- C:\Program Files\kCura Corporation\Relativity\ServiceHost directory

Set the maxRequestLength parameter as follows:

Copy

```text
1
2
3
<system.web>

     <httpRuntime maxRequestLength="32768"/>

</system.web>
```

View the code for the updated appSettings node Copy

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
<?xml version="1.0" encoding="utf-8"?>

<configuration>

   <configSections>

      <section name="kCura.Config" type="System.Configuration.DictionarySectionHandler, System, Version=1.0.3300.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />

      <section name="kCura.Service.ServiceHost" type="System.Configuration.DictionarySectionHandler, System, Version=1.0.3300.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />

   </configSections>

   <kCura.Config>

      <add key="connectionString" value="Data Source=RELATIVITYDEVVM;Initial Catalog=EDDS;Persist Security Info=False;Packet Size=4096;Workstation ID=localhost" />

   </kCura.Config>

   <startup>

      <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6.2" />

   </startup>

   <appSettings>

      <add key="LogConfigurationFilePath" value="LogConfig.xml" />

   </appSettings>

   <system.web>

      <httpRuntime maxRequestLength="32768"/>

   </system.web>

   <runtime>
```

For more information, see HTTP status codes in Relativity REST APIs .

## Unable to update or delete resources

The inability to update or delete a resource through the REST API may be caused by an incorrect setting for WebDAVModule in the Relativity.REST web.config file. Complete these steps to resolve this issue:

- Open the web.config file in a text editor.

- Locate the <modules> section in the file.

- Verify that the file settings explicitly remove the WebDAVModule. If necessary, update your file to match the following code sample: Copy

```text
1
2
3
4

<modules runAllManagedModulesForAllRequests="true">

     <remove name="WebDAVModule" />

</modules>
```

On this page

- Troubleshoot REST API errors

- HTTP method fails

- Incorrect maxRequestLength parameter

- Unable to update or delete resources


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
