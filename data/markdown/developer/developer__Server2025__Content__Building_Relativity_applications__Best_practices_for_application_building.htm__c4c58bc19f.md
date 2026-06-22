---
title: "Best practices for building applications"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Best_practices_for_application_building.htm
collection: developer
fetched_at: 2026-06-22T06:30:53+00:00
sha256: 1bbb7c9d90fae05280b23138e28cac6af5c6b2651b80a694903ab28e3b77e078
---

Best practices for building applications

# Best practices for building applications

Use these guidelines when developing Relativity applications through the Application Deployment System (ADS).

## Set up a dedicated environment for application development

Set up a dedicated or “golden” environment for developing applications. You can make all your schema changes for an application in this environment, such as adding new object types, event handlers, and other resources. When you release applications to clients, you ensure that they have the same origin signatures, and that changes to the applications import successfully.

For example, two developers may work locally on implementing versions of an application. When they each export their applications, the origin signatures differ. Relativity checks the origin signature during the installation of an application. If the signatures don’t match, it does a new installation. It doesn’t merge applications with different signatures, so features developed in one version of an application may be lost during installation. Always use a dedicate environment for updating the application. For more information about origin signatures, see Advanced functionality for the application framework .

Set up a new dedicated environment for each major version of your application. If you need to fix breaking changes in a new version of the application, you have dedicated environment available. You also have dedicated environments with previous versions of the application.

Additionally set up a new dedicated environment for each version of Relativity that you support. Because functionality differs between Relativity versions, you may want to use new application features. You don’t want to import applications with features available only a specific version of Relativity to other versions.

Custom Applications in the Repository workspace are prohibited

## Use GUIDs to reference object types

Use unique identifiers (GUIDs) in your custom applications to reference Artifacts. Unlike the ArtifactIDs and Names of objects, you can't modify GUIDs referenced in an application. This practice avoids name conflicts. These conflicts occur when Artifacts from a custom application are imported into a Relativity workspace, containing objects with similar names.

You may want to create a class that contains GUID constants for Artifacts, such Fields, Choices, Object Types, and others. You can then reference this class in your custom application. See the following code sample:

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
<![CDATA[

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

namespace Relativity.Samples.Core

{

     public static class ApplicationConstants

     {

          public static readonly Guid OLD_CODING_FIELD_GUID = new Guid("eb174a88-068e-40a9-8835-5f020f80a089");

          public static readonly Guid NAME_FIELD_GUID = new Guid("0761E9D6-F775-48BB-91CC-1DB39B2CE9F0");

          public static readonly Guid RELATED_DOCUMENT_FIELD_GUID = new Guid("513B40E6-1FC5-4E59-9191-1C52D66C89AD");

          public static readonly Guid CONTAINS_EXTRACTEDTEXT_FIELD_GUID = new Guid("181724B3-AB4E-4E9F-82B7-6852D7DBFCBE");

          public static readonly Guid HAS_IMAGES_FIELD_GUID = new Guid("DB80E2CB-CE37-4813-8AAA-45AE54C8AB7B");

     }

}

        ]]>
```

## Use GUIDs when developing event handlers

From an event handler, you can reference objects by name, Artifact ID, and GUID. Relativity assigns all the components of your application a GUID. To view these GUIDs, click Show Components GUIDs on the detail view of an application. Additionally, the GUIDs for these components don’t change when you deploy the application in different environments. The use of GUIDs prevents name conflicts, when you install an application to a workspace that contains similarly named objects.

When a name conflict occurs during installation, Relativity asks you to rename the object in order to add the application to the workspace. If you developed your event handlers to use object names, they won’t function properly, and your application breaks. However, event handlers developed to use GUIDs continue to function as expected. For more information about developing event handlers, see Event Handlers .

Develop event handlers to use GUIDs rather than Artifact IDs. Artifact IDs are unique for a specific workspace, but they aren’t unique across environments. An Artifact ID may mean different things across a group of workspaces. Consequently, the system may not correctly port the Artifact IDs during application installation.

## Set the RunTarget attribute on event handlers

To improve performance, set the RunTarget attribute on your custom event handlers. This attribute indicates the database context that your event handler executes against, such as the workspace or instance level. It improves performance of your event handlers by helping them avoid race conditions or possible deadlocks. For example, if your event handler only executes against a workspace database, then set this attribute to Workspace.

The Helper RunTargets enumeration includes the Workspace enum, as well as the Instance and InstanceAndWorkspace enums, which you can use to set the RunTarget attribute. This enumeration is available on the kCura.EventHandler namespace in the Event Handlers API. For reference information, see Class library reference .

Always set the RunTarget attribute on all custom Post Install event handlers as a best practice. For more information, see Post Install event handlers .

The following code sample illustrates how to set the RunTarget attribute for executing at the instance level:

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
using System.Runtime.InteropServices;

using kCura.EventHandler;

using kCura.EventHandler.CustomAttributes;

namespace MyApp.EventHandlers

{

    [Description("My Post Install Event Handler")]

    [Guid("00000000-0000-0000-0000-000000000000")]

    [kCura.EventHandler.CustomAttributes.RunTarget(kCura.EventHandler.Helper.RunTargets.Instance)]

    public class MyPostInstallEventHandler : PostInstallEventHandler

    {

        public override Response Execute()

        {

            // Event Handler Implementation

        }

    }

}
```

## Use Relativity API Helpers for establishing Services API connections

Use the methods on IEHHelper class to return a connection to the Services API. You can access these methods by adding a reference to the Relativity.API.dll when you create new event handler classes. In Visual Studio, you can easily reference these methods through Intellisense. The following code samples illustrate how to log in to Relativity using the helper methods:

- Logging in as a system user: Copy

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

try

{

     using (IObjectManager proxy =

          Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

     {

          // Proxy created.

          // Add your custom code for working with the Object Manager client.

     }

}

catch (Exception e)

{

     // Proxy failure: e.Message

}
```

- Logging in as the current user: Copy

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
try

{

     using (IObjectManager proxy =

          Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

     {

          // Proxy created.

          // Add your custom code for working with the Object Manager client.

     }

}

catch (Exception e)

{

     // Proxy failure: e.Message

}
```

## Use the Relativity UI to edit applications

Don't manually edit the RAP file for an application that you export from Relativity. Update the application through application details page available from the Relativity Application tab. This practice ensures that your modifications are appropriately incorporated in the application. See View or edit application details .

A RAP file is a compressed file contains an application.xml file. This file provides information about your application’s schema. You should avoid unzipping this file, or making manual edits to it. Exporting the application from Relativity overwrites any manual edits. In addition, modifying the RAP may cause an application import failure.

## Don't downgrade application versions

Don't downgrade your application version. You shouldn't change the version of your application to one that is lower than the currently installed version. When you downgrade an application version, you must delete the application from the application library. This process causes the application to be in an unknown or "dirty" state. It may also prevent the resource files for your application from being cleaned up properly. Your application now has an unknown state. For more information about application versions, see Advanced functionality for the application framework .

## Keep applications locked unless you're editing them

Keep applications locked when you aren't making modifications to them. You can inadvertently modify an unlocked application. For more information, see Locking and unlocking applications on the Relativity Documentation site.

## Maintain application validation requirements

Ensure that the components added to your application are valid. You can only export applications that contain valid and exportable components. They include Choices, Event Handlers, Fields, Layouts, Mass Operation Handlers, Object Types, Object Rules, Scripts, Saved Searches, Tabs, and Views. For information, see Validation requirements for application components .

You can always export agent types, custom pages, and Relativity scripts.

## Implement your own application components

Your application should include only components that you implement specifically for it. Adding components from other applications creates dependencies on them. Your application may break if you aren't aware of changes made to these other applications. For example, your application depends on another application, and a developers deletes an object type from it. You also need to delete this object type from your application to prevent it from breaking.

## Add an About page

Include an About page in your custom application that contains your contact information. This page is usually a custom page. For more information, see Custom pages .

## Open and close connections

Open and close your connections properly. Don't create and destroy your SQL connections. Use the Relativity helper classes to create and destroy the connections automatically. For more information, see Relativity API Helpers .

## Batch data

Batch your interactions with large amounts of data, especially during production hours. Avoid locking the database table, such as the Document table. For example, a recommend batch size is 5000 documents.

## Test various file types

Test all file types used by applications that interface with multiple document types to ensure proper functionality.

Use automated tests. This approach is a best practice for all custom application development.

## Do not include assemblies in RAP files for assemblies provided by Relativity

Applications most not include assemblies in their RAP files for assemblies that are provided by Relativity. Relativity automatically deploys some assemblies with each ADS component. While you may safely reference these assemblies within your .NET code, they should not be added as resource files to your application. If they are included, Relativity will overwrite them with its own copy even if they are on different versions. The following are the current list of assemblies that will get overridden:

- HtmlAgilityPack.dll

- IdentityModel.dll

- kCura.Agent.dll

- kCura.dll

- kCura.EventHandler.dll

- kCura.HTMLSanitizer.dll

- kCura.Injection.dll

- kCura.Relativity.Client.dll

- Microsoft.Owin.dll

- Microsoft.Owin.Security.Cookies.dll

- Microsoft.Owin.Security.dll

- Newtonsoft.Json.dll

- Ocr.Engine.Interfaces.dll

- Relativity.AmbientData.dll

- Relativity.API.dll

- Relativity.APIHelper.dll

- Relativity.Audit.Ingestion.Interface.dll

- Relativity.Audit.SDK.dll

- Relativity.Configuration.Core.dll

- Relativity.Configuration.dll

- Relativity.CustomPages.dll

- Relativity.DataGrid.dll

- Relativity.Kepler.dll

- Relativity.OAuth2Client.dll

- Relativity.OAuth2Client.IdentityModel.dll

- Relativity.OAuth2Client.IdentityModel.Interfaces.dll

- Relativity.OAuth2Client.Interfaces.dll

- Relativity.Runtime.Container.dll

- Relativity.Runtime.Interfaces.dll

- Relativity.SecretCatalog.dll

- Relativity.SecretCatalog.SQL.SQLCatalog.dll

- Relativity.SecretStore.Client.Config.Windows.AzureSupported.dll

- Relativity.SecretStore.Client.dll

- Relativity.SecretStore.Interfaces.dll

- Relativity.ServiceBus.AzureProvider.dll

- Relativity.ServiceBus.Bridge.dll

- Relativity.ServiceBus.Contracts.dll

- Relativity.ServiceBus.dll

- Relativity.ServiceBus.Patterns.dll

- Relativity.ServiceBus.Provider.Azure.dll

- Relativity.ServiceBus.Provider.Windows1_1.dll

- Relativity.ServiceBus.Providers.Configuration.dll

- Relativity.ServiceBus.RabbitMQProvider.dll

- Relativity.ServiceBus.WindowsProvider.dll

- Relativity.Services.DataContracts.dll

- Relativity.Services.Interfaces.dll

- Relativity.Services.Interfaces.Helpers.dll

- Relativity.Services.Interfaces.Private.dll

- Relativity.Services.ServiceProxy.dll

- Relativity.Telemetry.APM.dll

- Relativity.Telemetry.APM.ServiceBus.dll

- Relativity.Telemetry.DataContracts.Shared.dll

- Relativity.Telemetry.MetricsCollection.dll

- Relativity.Telemetry.MetricsCollection.Factory.dll

- StructureMap.dll

- System.Collections.Immutable.dll

- System.IdentityModel.Tokens.Jwt.dll

- System.Reactive.Core.dll

- System.Reactive.Interfaces.dll

- System.Reactive.Linq.dll

- System.Reactive.PlatformServices.dll

- System.Reactive.Windows.Threading.dll

- System.Reflection.Metadata.dll

- System.Threading.Tasks.Dataflow.dll

- SystemWrapper.dll
