---
title: "Implementing Relativity Forms event handlers"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Implementing_Relativity_Forms_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:51+00:00
sha256: a6d3221b6170aebceff9dd1c5d9f82e5633ebce987a3c1a07d3471d9e3211f9f
---

Implementing Relativity Forms event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Implementing Relativity Forms event handlers

Page Interaction event handlers for object types using Relativity Forms require JavaScript resource files. These JavaScript files contain the handlers for the client-side events which occur in each pipeline. You implement these client-side event handlers by creating JavaScript files with your custom code, and then specify the names of these files in the ScriptFileNames and AdditionalHostedFileNames properties added to the .NET PageInteractionEventHandler class. The JavaScript and any other supporting files are uploaded to Relativity separately from the DLL for the Page Interaction event handler. Additionally, to be rendered by Relativity Forms the Use Relativity Forms Field on the object type must be set to Yes as shown below:

## Guidelines for page interaction event handlers

Use these guidelines when developing page interaction event handlers in Relativity Forms:

- Create event handler JavaScript files - implement one or more JavaScript files that contain the logic to be executed by a Relativity Forms page. In most cases, you may have only one file, but you can specify multiple files. For more information, see Code .

Create JavaScript files separately from the DLL that contains your Page Interaction event handler. You need to upload these files and the DLL as separate files, so the JavaScript files shouldn’t be part of your Visual Studio project.

- Optionally create additional files - you may optionally implement or define one or more additional files required for your Page Interaction event handler. For example, you might want to provide image, CSS, or supporting JavaScript files.

Create these files separately from the DLL that contains your Page Interaction event handler. As you will need to upload these files and the DLL as separately, the files shouldn’t be part of your Visual Studio project.

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.Server.EventHandler.SDK and Relativity.Server.API.SDK packages. See Best practices for building applications .

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PageInteractionEventHandler class - extend the base class for this type of event handler.

- Override the PopulateScriptBlocks() method - Relativity Forms ignores the PopulateScriptBlocks() method, so if you are making a new event handler only to be used in Relativity Forms, return an empty Response. However, if you are converting an existing Page Interaction event handler for use in Relativity Forms, this can be left as-is so that your existing customizations can be used in Classic Forms while you convert to Relativity Forms.

- Override the ScriptFileNames property - return the names of the files containing the JavaScript logic that you want the Relativity Forms page to execute. These files are automatically interpreted and yield an object that contains one or more event handlers to register for the object type within the Relativity Forms API.

- Optionally, override the AdditionalHostedFileNames property - return the names of any additional files that your Page Interaction event handler needs. For example, it might require images or style sheets. These files are available for download and usage, but the Relativity Forms API doesn't attempt to obtain them or interpret them as event handler files.

- Upload your event handler assembly, script files, and additional files to Relativity - in the Relativity UI, use the Resource Files tab to upload your compiled .dll file for the event handler, and any files specified by the ScriptFileNames and AdditionalHostedFileNames properties. You need to upload these items as separate files, so they shouldn't be embedded in your .NET class. See Add event handlers to applications .

As part of the upload process, you need to associate your custom files with an application that Relativity uses to host them. See Resource files on the Relativity Documentation site.

- Associate your event handler with an object type - in your workspace, associate the newly uploaded Page Interaction event handler with the with one or more object types.

- Enable the use of Relativity Forms on the associated object types - ensure that Relativity Forms is enabled by setting the Use Relativity Forms Field on your object type to Yes .

- When you navigate to a forms page for a Relativity Forms - enabled object type associated with the event handler, it should automatically run the JavaScript contained in the files that you specified in the ScriptFileNames property.

## Customizing Relativity Forms pages with the Relativity Forms API

The following code illustrates a sample Page Interaction event handler compatible with Relativity Forms.

Copy

sample Page Interaction event handler

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
using kCura.EventHandler;

namespace EventHandlerExampleApplication {

  public class EventHandlerExample: kCura.EventHandler.PageInteractionEventHandler {

    public override Response PopulateScriptBlocks() {

      return new Response();

    }

    public override string[] ScriptFileNames {

      get {

        return new string[] {

          "eventHandlerExampleResourceFile.js"

        };

      }

    }

  }

}
```

The following code illustrates a simple event handler script file "eventHandlerExampleResourceFile.js":

Copy

event handler script file

```text
1
2
3
4
5
6
7
(function(eventNames, convenienceApi) {

  var eventHandlers = {};

  eventHandlers[eventNames.PAGE_LOAD_COMPLETE] = function() {

    var fileUrl = convenienceApi.utilities.getRelativityPageBaseWindow().GetRelativityApplicationWebResourceFile(<applicationGuid>,'latest',<fileName>);

  }

  return eventHandlers

}(eventNames, convenienceApi));
```

### Identifying the URL for a file

You can use the AdditionalHostedFileNames property to identify supplementary files for use by your event handler. The web server hosts any files that you specify in this property. To determine the appropriate URL for a file, call the GetRelativityApplicationWebResourceFile method on the Relativity page base window. See the following code sample:

Copy

Identifying the URL for a file

```text
1
2
3
4
5
6
7
(function(eventNames, convenienceApi) {

  var eventHandlers = {};

  eventHandlers[eventNames.PAGE_LOAD_COMPLETE] = function() {

    var fileUrl = convenienceApi.utilities.getRelativityPageBaseWindow().GetRelativityApplicationWebResourceFile(<applicationGuid>,'latest',<fileName>);

  }

  return eventHandlers

}(eventNames, convenienceApi));
```

This call consists of the following parameters:

- <applicationGuid> - the GUID of the Relativity application associated with your event handler.

- 'latest' - a placeholder for any valid value that is part of a generated URL. Currently, the web server ignores this part of the URL, but it is reserved for future development purposes.

- <fileName> - the name of a file. This call returns the URL for this file.

The use of the GetRelativityApplicationWebResourceFile on window.top within a pop-up window is deprecated. We recommend accessing the Relativity window in a Forms event handler through the getRelativityPageBaseWindow() method.

## Updating custom event handler script files

After you implement your event handler's script files, you can modify a file without needing to update the associated Relativity Application. To do this, you will replace the existing file through the Resource Files tab. Within five seconds of uploading the files, they are available on all web servers in your environment. Use the following steps:

-

Alter the event handler JavaScript file locally, and save it.

-

Open the Relativity instance that contains your application.

- Navigate to the Resource Files tab and find the JS file you want to update. In this example, look for the eventHandlerExampleResourceFile.js associated with the application.

- Edit the entry and click Clear , in order to clear the exiting entry for the file.

- Click Select File and select your updated JS file. The name of the script must remain the same, click Save .

Your changes should now appear in the associated object type's Relativity Forms pages. If you do not see your changes taking effect, try clearing your browser cache and reloading the page. Some browsers (including Chrome) allow you to disable the cache while your developer tools are open - this will prove helpful during development.

Once you have finished development of the script files, you can update the version number of your Relativity Application by pushing it to the library, in order to fix any lingering cache issues for users.

## Considerations

- Single or multiple files - you can have one or more event handler JavaScript files. When the user first loads the application, the object type may spend less time downloading resources and start marginally more quickly if you provide fewer files. After the first load, the scripts are cached. While generally, a single script file per object type may suffice, you do have the option to define multiple scripts per object type. You can do this to aid in code organization; however, it's important to note that variables defined in one file will not be accessible within another. It is also possible that an object type may be customized with event handlers from multiple Relativity Applications, which would result in multiple files.

- ECMAScript requirements - write your event handler scripts in ECMAScript 5.1 or earlier for best compatibility. Neither Relativity nor the Relativity Forms API transpile event handlers written in ECMAScript 6, TypeScript, or ES.Next. To avoid breaking code, or incompatibility in browsers such as Internet Explorer, avoid using features which are not part of ECMAScript 5.1. For more information, see:

- Relativity compatibility matrix

- ECMAScript Language Specification (5.1 Edition / June 2011)

- ECMAScript 5 Objects and Properties

- Kangax table on browser support for es5 features

- Kangax table on browser support for es6 features

- Script file structure - each event handler script file must meet the following general requirements:

- It should be an immediately-invoked function expression (IIFE). For more information, see IIFE on the MDN web docs site.

- It must return an object where:

- each of its keys is the name of the event to handle.

- each value is the function to be invoked for handling the given event.

- The eventNames object provides access to a list of constants used to reference event handler names.

- The convenienceApi object provides access to methods designed to simplify event handler development.

- Use of HTTP headers - the files that you upload to Relativity are served up by the web server with a Cache-Control public header and an Expires header set to a date far in the future. These files are listed in the ScriptFileNames and AdditionalHostedFileNames properties for the event handler. See Guidelines for Page Interaction event handlers to be used in Relativity Forms .

- Associated Relativity application - page Interaction event handlers must be associated with a Relativity application that exists in the Application Library. This association with an application is required because Relativity hosts the assets of Page Interaction event handlers at the instance level. Review the following pages to learn about Relativity Applications, resource files, and the Application Library:

- Create an application in Relativity

- Resource files on the Relativity Documentation site.

- Installing applications on the Documentation site.

- Impacts on (non-Page Interaction) object type event handlers - your object type may have associated to it, or you may still desire to use, the other object type event handlers . Most of these are still supported by default in Relativity Forms, but have some caveats:

Object type event handler(s)

Brief description

Console event handler

The existence of a Console event handler associated to an object type will not prevent the type from using Relativity Forms, but Relativity Forms ignores them. To achieve Console behavior in Relativity Forms, implement a handler for the load pipeline's createConsole event .

List Page Interaction event handler

(This does not apply to Classic Forms pages or Relativity Forms pages)

Pre Cascade Delete event handler

Pre Delete event handler

Pre Mass Delete event handler

The Object Manager API executes these handlers during its deletions, and by default, Relativity Forms uses Object Manager API for its deletions. So by default, Relativity Forms will respect the existence of these Event Handlers, with the following caveat:

- After the delete pipeline finishes preDelete , the deletion is executed. By default that deletion is a call to the Object Manager API . If a handler is implemented for replaceDelete , and something other than the Object Manager API is used for the deletion, these object type event handlers will not be executed.

Pre Load event handler

The Object Manager API executes these handlers during its reads, and by default, Relativity Forms uses Object Manager API for its object instance reads. So by default, Relativity Forms will respect the existence of these Event Handlers, with the following caveats:

- Pre Load event handlers fire on the server during the read for an object, this only occurs for view and edit forms, and so the Pre Load event handler will not fire on the form for creating a new object. In order to pre-populate values into a new object's form in Relativity Forms, implement a handler for the load pipeline's replaceGetNewObjectInsance .

- If a handler is implemented for the load pipeline's replaceRead, and something other than the Object Manager API is used for this read, the Pre Load event handlers will not be executed.

- Pre Load event handlers are sometimes used to inject script into Classic Forms via Response.Message, but Relativity Forms only supports execution of script which written as part of the Page Interaction event handler JavaScript files. Any scripts within Response.Message will not be executed, and should be moved into a JavaScript file listed in the PageInteractionEventHandler-derived class's ScriptFileNames or AdditionalHostedFileNames.

Pre Save event handler

Post Save event handler

The Object Manager API executes these handlers during its saves, (before and after the object is saved, respectively) and by default, Relativity Forms uses Object Manager API for its saves. So by default, Relativity Forms will respect the existence of these Event Handlers. They fire on the server, after the submit pipeline finishes its validation (on submit) . If a handler is implemented for the submit pipeline's replaceSave , and something other than the Object Manager API is used for the save, these object type event handlers will not be executed.

On this page

- Implementing Relativity Forms event handlers

- Guidelines for page interaction event handlers

- Customizing Relativity Forms pages with the Relativity Forms API

- Identifying the URL for a file

- Updating custom event handler script files

- Considerations


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
