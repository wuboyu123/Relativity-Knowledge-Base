---
title: "Best Practices"
url: https://platform.relativity.com/Server2025/Content/Relativity_Integration_Points/Best_practices_for_integration_point_development.htm
collection: developer
fetched_at: 2026-06-22T06:30:08+00:00
sha256: 7942101950f678fbc188e59e8f860561c1cfab35f2614fbfa05247bc39db25c6
---

Best Practices

# Best practices for integration point development

Use these guidelines to optimize your development of custom integration points. You can use them as a general outline of the development process that you may want to follow. Additionally, you can use them as a checklist to verify that your source code meets implementation requirements for an integration point.

## Use separate projects for custom page and provider code

Consider setting up your Visual Studio solution with separate projects for your custom page and provider code:

- Add an empty ASP.NET MVC 5 Web Application as the project for your custom page development.

- Add a Class Library project for your provider code.

For sample projects, see Build your first integration point and Build an advanced integration point .

## Reference the required Relativity libraries in your projects

When you set up a Visual Studio solution for an integration point, ensure that you reference the following .dll files:

- In your custom page project, add a reference to the Relativity.CustomPages.dll, which is available in the Relativity SDK. For more information, see Download the SDKs .

- In your provider project, add the following references:

- kCura.EventHandler.dll, which is available in the Relativity SDK.

- Relativity.IntegrationPoints.Contracts.dll, Relativity.IntegrationPoints.SourceProviderInstaller.dll, and Relativity.IntegrationPoints.Services.Interfaces.Private, which are available in the Integration Points SDK. See Download the SDKs and Integration Points SDK files .

## Create a custom application in Relativity

Before you begin developing your source code, add a workspace in a Relativity development environment where you want to build the custom application for your integration point. Create your application and obtain its GUID, which you need to reference in your source code. For sample steps, see Create a Relativity application .

Ensure that you reserve this workspace and application for future development. As you update your integration point, use this environment. For more information, see Build Relativity applications .

## Use GUIDs in your source code

Developing a custom integration point requires that you reference GUIDs when adding the following functionality:

- Custom page – the source code for your custom page requires that you reference the GUID for the application where you want to upload the page.

- Provider – when implementing your provider, you need to set the DataSourceProvider attribute to a GUID.

- Event handlers – you should implement an IntegrationPointSourceProviderInstaller and IntegrationPointSourceProviderUninstaller event handler for your integration point. These event handlers extend the Post Install and Pre Uninstall event handler classes available in the Relativity platform. Each of these classes requires a custom attribute that takes a GUID.

Consider creating global variables for your application and provider GUIDs so that you can conveniently reference them in your source code. For sample code, see Build your first integration point

## Subscribe to required JavaScript events

When Relativity users interact with the custom page in your integration point, they cause several JavaScript events to be raised. Ensure that you include a custom JavaScript file with handlers that subscribe to the following events:

- submit – raised when the user clicks the Next or Save button in the Relativity UI.

- saveState – executes logic that persists the state.

- saveComplete – indicates to the host page that it can continue processing.

- back – raised when a user clicks the Back button in the Relativity UI.

- load – raised when the host page loads the current settings page.

The view in your web project should reference a JavaScript file that includes handlers for these events.

## Reference required JavaScript files in the view

Ensure that the view in your web application project references the following JavaScript files:

- custom JavaScript file – defines handlers for various events. You implement this code for your integration point. See Subscribe to required JavaScript events and Add a custom JavaScript file .

- frame-messaging.js – we developed this proprietary code to support integration point development.

- jquery-postMessage.js – enables communication across iFrames in web pages.

- jquery-3.6.0.js – provides the standard jQuery library.

The Integration Points SDK includes all of these files except the first one so that you easily add them to your web application project. See Relativity Server APIs .

## Include event handlers for your provider

You should include the following event handlers in the project that you create for your provider:

- IntegrationPointSourceProviderInstaller – use this event handler to register your provider with Relativity. It updates the SourceProvider table in the workspace database with information about your integration point, including the GUIDs for the provider and application. It also updates the URL for your custom page. For more information, see Display source provider settings selected by users .

- IntegrationPointSourceProviderUninstaller – use this event handler to remove all application information from the workspace database table when a user wants to delete your integration point. It deletes all integration points and scheduled import jobs from your workspace database. It also removes your source provider from the Source Provider drop-down menu in the integration point wizard.

For examples of these event handlers, see Build your first integration point and Build an advanced integration point .

## Display source provider settings selected by users

You can display the settings that users select for a source provider on your custom page. To display this information, complete these tasks:

- In an ApiController class in your MVC project, add a method to return the key-value pairs that you want to appear in your custom page. The key represents the name of a field that users can set on your source provider, and the value represents the setting that the user enters.

- Set the ViewDataURL property on the SourceProvider class to a URL that routes to an API controller in your source provider. Add this code when you implement the IntegrationPointSourceProviderInstaller. See Set the ViewDataUrl property .

### Define a method for returning key-value pairs

Because your custom page development should be part of a ASP.NET MVC 5/WebAPI application, you can implement a custom controller that performs the following tasks:

- Inherits from the ApiController class.

- Accepts the settings entered by the user.

- Returns a list of key-value pairs that appear in the custom page.

The JSON loader code sample includes the following API controller, which returns key-value pairs based on locations that you can set in this source provider. For more information, see Build an advanced integration point .

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
namespace JsonWeb.Controllers.api

{

      public class ViewController : ApiController

      {

            [HttpPost]

            public HttpResponseMessage GetViewFields([FromBody] object data)

            {

                  var result = new List<KeyValuePair<string, string>>();

                  if (data != null)

                  {

                        var helper = new JsonHelper();

                        var settings = helper.GetSettings(data.ToString());

                        result.Add(new KeyValuePair<string, string>("FieldLocation", settings.FieldLocation));

                        result.Add(new KeyValuePair<string, string>("DataLocation", settings.DataLocation));

                  }

                  return Request.CreateResponse(HttpStatusCode.OK, result);

            }

      }

}
```

### Set the ViewDataUrl property

You must set the ViewDataUrl property to a URL that maps to an API-specific route determined by your controller. The format for the URL includes the application path token, the text CustomPages , the application GUID, and routing information for your Web API controller. The following code snippet illustrates the format used for the URL:

Copy

```text
1
2

ViewDataUrl = "/%applicationpath%/CustomPages/f0fd184d-d2ca-4be9-83ec-884955eea8ff/api/view/"
```

The Relativity Integration Points API provides the following tokens for use in your URLs:

- %applicationPath% – represents the application path in Relativity.

- %appId% – represents a workspace ID.

- %artifactID% – represents the ArtifactID of the current integration point.

You can use these tokens to route URLs to a controller. While they have names similar to those used in linking custom pages to tabs in Relativity, these tokens aren't supported for this purpose.

In this code from the JSON loader sample, you can see how the installer for this source provider sets the ViewDataUrl property by using tokens, the application GUID, and the specific API route required by its controller. It also illustrates how to set the Configuration property on the SourceProvider class by instantiating a SourceProviderConfiguration object and setting its properties. For the complete sample code, see Build an advanced integration point .

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
27
28
29
30
31
32
33
34
35
namespace JsonLoader.Installer

{

    [kCura.EventHandler.CustomAttributes.Description("Update Json provider - On Every Install")]

    [kCura.EventHandler.CustomAttributes.RunOnce(false)]

    [Guid("64110733-03F8-4DAC-958D-31E9DFDA6071")]

    public class RunEveryTimeInstaller : IntegrationPointSourceProviderInstaller

    {

        public override IDictionary<System.Guid, SourceProvider> GetSourceProviders()

        {

            return new Dictionary<Guid, SourceProvider>()

            {

                {

                    new Guid(GlobalConst.JSON_SOURCE_PROVIDER_GUID),

                    new SourceProvider()

                    {

                        Name = "JSON",

                        Url = $"/%applicationpath%/CustomPages/{GlobalConst.APPLICATION_GUID}/Home/",

                        ViewDataUrl = $"/%applicationpath%/CustomPages/{GlobalConst.APPLICATION_GUID}/api/view/",

                        Configuration = new SourceProviderConfiguration()

                        {

                            AlwaysImportNativeFiles = false,

                            AlwaysImportNativeFileNames = false,

                            OnlyMapIdentifierToIdentifier = false,

                            CompatibleRdoTypes = new List<Guid>()

                            {

                                new Guid(GlobalConst.DOCUMENT_RDO_GUID),

                                new Guid(GlobalConst.SAMPLE_JSON_OBJECT_GUID)

                            }

                        }

                    }

                }

            };

        }

    }

}
```

## Use methods for batching in your provider code

Your provider code returns DataReader objects with batches of identifiers for your data, and then batches of metadata associated with a specific identifier. Your provider code should implement the following methods on the IDataSourceProvider interface with the required import logic:

- GetData() – returns a DataReader object that contains the entire data set for import into Relativity.

- GetBatchableIds() – returns a DataReader object with a batch of identifiers.

- GetFields() – returns a list of fields that are available for import in the data source and that can be mapped to workspace fields.

## Upload .dll files to Relativity in the correct order

Your new integration point must be registered with Relativity before you can use it to ingest data. For this process to occur, you must first upload the following .dll files as resource files in Relativity:

- Relativity.IntegrationPoints.Contracts.dll

- Relativity.IntegrationPoints.SourceProviderInstaller.dll

- Relativity.IntegrationPoints.Services.Interfaces.Private.dll

- Your custom source provider .dll file

- Any additional assemblies located in the Provider folder of the Integration Points SDK - see Integration Points SDK files .

You must upload these .dll files in the required order for your integration point application to work properly.

After uploading the required .dll files, you can add the event handlers used by your provider to the application for your integration point. For sample steps, see Deploy your integration point .

## Use unique identifiers and display names in your data

When users import data into Relativity with your integration point, they must map data ingested by your provider to fields in the workspace. You can facilitate this process by using unique identifiers for data entry and unique display names for fields that require mapping. Reusing the same identifiers or display names may cause unexpected results.

## Verify your IIS configuration

In IIS, you should configure the web service called Relativity WebAPI to use Windows authentication. The Integration Point API uses the Relativity Import API, which requires authentication.

## Use secured configurations for sensitive information

When implementing a data source provider, you can use secured configurations to store encrypted user credentials or other sensitive information in the Relativity Secret Store. For more information, see Relativity Secret Store on the Relativity Documentation site.

This section provides general guidelines for implementing a secured configuration. You also find an additional example of this implementation in the JSON Loader application. For more information, see Build an advanced integration point .

Use the following steps as a guide for implementing a secured configuration:

- Review the custom page that you are using as the client interface for your provider to determine which parameters should be secured. In the following example, the username and password fields are secured.

- Add a new function to your source provider that returns your secured model as a string: Copy

```text
1
2
3
4
5
6
function createSecuredConfiguration(model) {

   return JSON.stringify({

      userName: model.userName,

      password: model.password

   });

}
```

- Update the event handler code for 'submit' as follows: Copy

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
message.subscribe('submit', function () {

    var localModel = JSON.stringify(ko.toJS(pageModel));

    this.publish("saveState", localModel); //Save the model in case of error.

    this.publish('saveComplete', localModel);

    var destinationModel = IP.frameMessaging().dFrame.IP.points.steps.steps[1].model;

    destinationModel.SecuredConfiguration = createSecuredConfiguration(localModel);

});
```

- Update the function used to create your view model, so that it retrieves the secured configuration when the custom page is loaded. See the following example: Copy

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
var viewModel = function (model) {

    var self = this;

    //…

    var securedConfiguration = JSON.parse(model.SecuredConfiguration);

    this.userName = ko.observable(securedConfiguration.userName);

    this.password = ko.observable(securedConfiguration.password);

};
```
