---
title: "List Page Interaction event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/List_Page_Interaction_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:30+00:00
sha256: d68f979e572061274aaaa25330b72226f871ac6b83775900fbdbd412524ebbd9
---

List Page Interaction event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# List Page Interaction event handlers

You can use the List Page Interaction event handlers to customize the content and behavior of Relativity list pages. To implement these customizations, you need to use the JavaScript APIs developed specifically for List Page Interaction event handlers. These APIs provide you with the ability to access the internal functionality of a list page, and interact with various features of an application. The following list highlights some of the customizations for list pages supported by the JavaScript APIs:

- Sending and receiving events

- Customizing the new item button

- Opening custom content modal windows

- Adding custom data sources

Unlike other event handlers, List Page Interaction event handlers require external JavaScript files rather than code defined in the PopulateScriptBlocks() method as in Page Interaction event handlers. You implement List Page Interaction event handlers by creating JavaScript files with your custom code, and then specifying the names of these files in the ScriptFileNames and AdditionalHostedFileNames properties added to the .NET code. Your JavaScript code must use the JavaScript APIs developed specifically by Relativity for these event handlers. The JavaScript and any other supporting files are uploaded to Relativity separately from the DLL for the List Page Interaction event handler. Additionally, these event handlers must be associated with a Relativity application.

See these related pages:

- List Page Interaction Event Handler API

- Page Interaction event handlers

## Special considerations for List Page Interaction event handlers

Before you begin implementing your event handler, review the following special considerations:

- Required JavaScript APIs - Relativity list pages expose their own JavaScript APIs that you must to use implement your page customizations. If you don't use these APIs, Relativity reverts your customizations. For more information, see List Page Interaction Event Handler API .

Don't interact with the DOM for the list page from within your JavaScript. This approach may cause unexpected behavior. If the JavaScript APIs don't provide a specific functionality that you want to implement, contact Client Services .

- Support in Relativity UI - Use the List Page Interaction event handler only with list pages used in the following releases:

- Use of HTTP headers - The files that you upload to Relativity are served up by the web server with a Cache-Control: public header and an Expires header set to a date far in the future. These files are listed in the ScriptFileNames and AdditionalHostedFileNames properties for the event handler. See Guidelines for List Page Interaction event handlers .

- Associated Relativity application - List Page Interaction event handlers must be associated with a Relativity application that exists in the Application Library. This association with an application is required because Relativity hosts the assets of List Page Interaction event handlers at the instance level. Review the following pages to learn about Relativity applications, resource files, and the Application Library:

- Create an application in Relativity

- Resource files on the Relativity Server 2025 Documentation site.

- Installing applications on the Relativity Server 2025 Documentation site.

## Guidelines for List Page Interaction event handlers

Use these guidelines when developing List Page Interaction event handlers:

- Create JavaScript files - implement one or more JavaScript files that contain the logic to be executed by a Relativity list page. You must use the JavaScript API developed specifically for List Page Interaction event handlers. See List Page Interaction Event Handler API .

Create JavaScript files separately from the DLL that contains your List Page Interaction event handler. You need to upload these files and the DLL as separate files, so the JavaScript files shouldn’t be part of your Visual Studio project.

- Optionally create additional files - implement or define one or more additional files required for your List Page Interaction event handler. For example, you might want to provide image, CSS, or supporting JavaScript files.

- Create a new class that inherits from ListPageInteractionEventHandler in Visual Studio

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages. See Best practices for building applications .

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Implement the event handler - complete these tasks:

- Override the PopulateScriptBlocks() method to return an empty Response.

- Override the ScriptFileNames property to return the names of the files containing the JavaScript logic that you want the list page to execute. In most cases, you may have only one file but you can specify multiple files.

- Optionally override the AdditionalHostedFileNames property to return any additional files that your List Page Interaction event handler needs. For example, it might require images or style sheets.

- Create or identify a Relativity application - List Page Interaction event handlers must be associated with a Relativity application. You must either create an application or use an existing one for this purpose. Additionally, the application must exist in the Application Library. See Installing applications on the Relativity Server 2025 Documentation site.

- Upload your event handler assembly and JavaScript files to Relativity - In the Relativity UI, use the Resource Files tab to upload your compiled .dll file for the event handler, custom JavaScript files, and any supplementary files specified by the AdditionalHostedFileNames property. You need to upload these items as separate files, so they shouldn't be embedded in your .NET class.

As part of the upload process, you need to associate your custom files with an application that Relativity uses to host them. See Resource Files on the Relativity Documentation site.

- Associate your event handler with an object type - In your workspace, associate the newly uploaded List Page Interaction event handler with the with one or more object types. See Adding an event handler .

When you navigate to a list page for an object type associated with the event handler, it should automatically run the JavaScript contained in the files that you specified in the ScriptFileNames property.

## Code sample for a List Page Interaction event handler

The following code sample illustrates how to implement a simple List Page Interaction event handler. It shows how to override the PopulateScriptBlocks() method, and the ScriptFileNames and AdditionalHostedFileNames properties. For more information, see Guidelines for List Page Interaction event handlers .

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
using kCura.EventHandler;

namespace QueryTest

{

     [System.Runtime.InteropServices.Guid("0cae30b4-a591-4029-acf7-ac85302ac83f")]

     [kCura.EventHandler.CustomAttributes.Description("Sample List Page Interaction event handler")]

     public class SampleListPageInteractionEventHandler : ListPageInteractionEventHandler

     {

             public override Response PopulateScriptBlocks()

             {

                      return new Response();

             }

             public override string[] ScriptFileNames => new string[] { "sample.js"};

              public override string[] AdditionalHostedFileNames => new string[] { "cat.jpg", "dog.jpg" };

     }

}
```

### Sample JavaScript file

The following code sample illustrates a simple JavaScript file called sample.js, which is referenced by the ScriptFileNames property in the previous event handler code. It uses the uses the cell formatting event and the Modal API to add custom functionality to a List Page Interaction event handler. The sample.js file is uploaded as a separate file to Relativity. For more information, see Cell Formatter API and Modal API .

View code for sample JavaScript file Copy

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
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
define(function() {

     "use strict";

     function sampleHandle(api) {

          var api = api;

          // FORMATTING TEXT EXAMPLE

          function subjectFormatter(value, options, rowObject, formatterApi) {

               var data, resultHtml;

                data = formatterApi.getCellData(value) || "";

                resultHtml = "<span style='color: #0b3e6f'>File type: "+data+"</span><hr><span>Another Line</span>";

                return resultHtml;

          }

           // OPEN MODAL EXAMPLE

          function authorFormatter(value, options, rowObject, formatterApi) {

               var valueText, resultHtml, modalId, modalContent;

                valueText = formatterApi.getCellData(value) || "";

                modalContent = {

                    title: "Modal for " + valueText,

                    modalClass: "rlh-new-rdo-dialog",

                    modalName: "rlhRdoModalDialog",

                    template: "<span>Some sample text</span>",

                    buttons: [{

                         name: "Apply",

                         eventName: "apply_click",

                    }, {

                         name: "Close",

                         eventName: "close_click"

                    }],

                    init: function (scope, el) {

                         scope.$on("apply_click", function() {

                              alert("OK clicked - " + valueText);

                              api.modalService.hideModal(modalId);

                            });

                          scope.$on("close_click", function() {

                              api.modalService.hideModal(modalId);

                         });

                    }

               }

                var modalId = api.modalService.createModal(modalContent);

                resultHtml = valueText + "<br><a href='#' " + formatterApi.getOnClickForModal(modalId) + ">Open modal (formatterApi)</a>";

                return resultHtml;

          }

         function cellFormattersInit(formatterApi) {

            var fieldSubject, fieldAuthor;

             fieldSubject = formatterApi.fields.find(function (field) {

                return field.displayName === "File Type";

            });

            if (fieldSubject) {

                formatterApi.setFormatter(fieldSubject.columnName, subjectFormatter);

            }

             fieldAuthor = formatterApi.fields.find(function (field) {

                return field.displayName === "File Path";

            });

            if (fieldAuthor) {

                formatterApi.setFormatter(fieldAuthor.columnName, authorFormatter);

            }

        }

         return {

            cellFormattersInit: cellFormattersInit

        };

    }

     return sampleHandle;

});
```

## Identifying the URL for a file

You can use the AdditionalHostedFileNames property to identify supplementary files for use by your event handler. The web server hosts any files that you specify in this property. To determine the appropriate URL for a file, make the following call from within your JavaScript:

Copy

```text
1
window.top.GetRelativityApplicationWebResourceFile(<applicationGuid>,'latest',<fileName>);
```

This call consists of the following parameters:

- <applicationGuid> - the GUID of the Relativity application associated with your event handler.

- 'latest' - a placeholder for any valid value that is part of a generated URL. Currently, the web server ignores this part of the URL, but it is reserved for future development purposes.

- <fileName> - the name of a file. This call returns the URL for this file.

## Updating List Page Interaction event handlers

After you implement a List Page Interaction event handler, you can modify it by uploading new files or replace existing one through the Resource Files tab. Within five seconds of uploading the files, they are available on all web servers in your environment. For more information, see Resource files on the Relativity Server 2025 Documentation site.

To simplify uploading your files, consider setting up a reusable configuration through the Publish to Relativity tool. For more information, see Publish to Relativity tool .

On this page

- List Page Interaction event handlers

- Special considerations for List Page Interaction event handlers

- Guidelines for List Page Interaction event handlers

- Code sample for a List Page Interaction event handler

- Sample JavaScript file

- Identifying the URL for a file

- Updating List Page Interaction event handlers


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
