---
title: "Troubleshoot and upgrade integration points"
url: https://platform.relativity.com/Server2025/Content/Relativity_Integration_Points/Troubleshoot_integration_points.htm
collection: developer
fetched_at: 2026-06-22T06:30:12+00:00
sha256: ead373c49435fd365a45c892b389bb98957e6957b18e1a0a5d818ff430c0caed
---

Troubleshoot and upgrade integration points Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Troubleshoot and upgrade integration points

You can use the following information to troubleshoot your custom integration points and resolve common errors that may occur. It also includes instructions about how to upgrade your integration points for use in Relativity 9.4 and above.

## Upgrade integration points for use in Relativity 9.4 and above

Use the following guidelines to upgrade your custom integration points for use in Relativity 9.4 and above.

### Update the .dll references in your projects

Obtain the new versions of the Relativity Integration Points SDK and the Relativity SDK. Update the references in your projects to the new .dll files in these SDKs. For more information, see Download the SDKs and Set up your Visual Studio solution .

### Update the use of dependency injection

If you have implemented your source provider using dependency injection or have a provider factory inheriting from the DefaultProviderFactory class, update your source provider code as described in this section.

In previous versions of the Integration Points API, you needed to implement the CreateInstance() method on the DefaultProviderFactory class, create another class that implemented the IStartUp interface, and then use the PluginBuilder class to set the provider factory.

In Relativity 9.4 and above, you must now create a class that implements the new abstract ProviderFactoryBase class from the kCura.IntegrationPoints.Domain namespace. Use these guidelines when creating this class:

- Ensure that only one class in your code implements the ProviderFactoryBase class.

- Provide a public, empty constructor for your new class.

- If you have an existing class that inherits from the deprecated DefaultProviderFactory class, modify it so that it now inherits from the ProviderFactoryBase class.

### Recompile and upload your integration point

Recompile the source code for your integration point, and upload the .dlls to Relativity. For more information, see Deploy your integration point .

### Upload remaining assemblies to Relativity

Upload the remaining assemblies to Relativity as resource files. You can obtain them from the Relativity Integration Points SDK. Ensure that you upload the .dll files in the correct order. For more information, see Deploy your integration point .

## Troubleshoot integration points

Use the following troubleshooting guidelines to resolve common errors that may occur in integration points.

### Integration point doesn't run

An integration point doesn't run if the required agent wasn't added or the .dll files were uploaded in the wrong order. Complete the following tasks to troubleshoot an application that doesn't run:

- Verify that the Integration Points Agent is currently running.

- Verify that you added the .dll files in the proper order. If your application isn't registered with Relativity, you won't be able to use the provider. For more information, see Best practices for integration point development .

### Integration point exhibits poor performance

To improve the performance of your application, limit the number of providers executing any given time.

## Debug an integration point

To debug an integration point provider, you must point to the local Symbol files (.pdb) in your Visual Studio application. Unlike other Relativity extensibility points, the Integration Point framework doesn't support uploading the .pdb files to the application domain for use in debugging.

These instructions describe how to debug the following methods that an integration points provider supports. These methods execute at different times and places in your code:

- GetFields() method

- GetBatchablelds() method

- GetData() method method

Use the following steps to debug an integration point provider:

- In Visual Studio, click Tools > Options > Debugging > Symbols .

- Locate the Cache symbols in this directory field.

- Click Browse to select the local directory where Visual Studio stores your .pdb files.

- Attach your remote debugger to the w3p processes on your server. You can now step through the GetFields() method that your integration point provides supports. It executes immediately before a user navigates to the Field Mappings option in the Integration Point framework. See the following screenshot of this option in the Relativity UI:

Attach to the debugger to the w3p process as late as possible. The server rapidly spawns these processes, which may prevent them from being caught by the debugger.

When you attach to multiple w3p processes, debugging in Visual Studio may slow down. As an alternative, you attach to a w3p process by using the following command in the command prompt on the machine where the IIS is installed:

Copy

```text
1
C:\Windows\System32\inetsrv\appcmd.exe list wp
```

It takes the process ID with the following GUID:

Copy

```text
1
(applicationPool:dcf6e9d1-22b6-4da3-98f6-41381e93c30c)
```

- Attach your remote debugger to the agent server where your integration points agent is running. After a user starts a job, the agent server executes the GetBatchablelds() and GetData() methods.

On this page

- Troubleshoot and upgrade integration points

- Upgrade integration points for use in Relativity 9.4 and above

- Update the .dll references in your projects

- Update the use of dependency injection

- Recompile and upload your integration point

- Upload remaining assemblies to Relativity

- Troubleshoot integration points

- Integration point doesn't run

- Integration point exhibits poor performance

- Debug an integration point


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
