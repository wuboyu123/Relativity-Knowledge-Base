---
title: "Page Interaction event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Page_Interaction_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:28:53+00:00
sha256: f99fd8e93cff907a88435507c62d00403cddf37cf2656ee9586e12e1b7e1bd00
---

Page Interaction event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Page Interaction event handlers

Relativity supports event handlers that you can use to inject JavaScript and make other customizations to form and list pages. Page Interaction event handlers support customizations to the behavior of pages containing forms. You can inject your own JavaScript code or load your Cascading Style Sheets (CSS) file on the view or edit page of an object. You can use this event handler to add specialized behavior to these pages, and to control their look and feel.

For example, you can add JavaScript to Page Interaction event handlers that controls the formatting of phone numbers entered in text boxes or validates a user's entry in a form. You can also use this type of event handler to alter the spacing between object types listed on a view page or modify the functionality of a console button.

This following information describes how to develop your own custom Page Interaction event handlers by providing general guidelines and code samples.

List pages expose JavaScript APIs that can be used to change the appearance and behavior of a page. You can interact with these APIs by implementing a ListPageInteractionEventHandler, which inherits from the PageInteractionEventHandler class, and writing separate JavaScript files that contain custom code. For more information, see List Page Interaction event handlers .

Relativity Forms is a new Layout-rendering option, providing the developer with robust JavaScript APIs and a granular front-end page life cycle for easier, more controlled Relativity Object customization. It is enabled by setting the Use Relativity Forms field on your object type to Yes , and customization is supplied via JavaScript resource files specified by the PageInteractionEventHandler-derived class' ScriptFileNames property. For more information, see Relativity Forms API .

See the following related pages:

- List Page Interaction event handlers

- List Page Interaction Event Handler API

- Relativity Forms API

## Guidelines for Page Interaction event handlers

Use these guidelines when developing Page Interaction event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PageInteractionEventHandler class – extend the base class for this type of event handler

- Override the PopulateScriptBlocks() method – injects the JavaScript and loads the .css file.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

- Optionally use event handlers to construct HTTP responses - event handlers can't access the request header, cookies, or session information using the HTTPContext object, although they can assisted in constructing an HTTP response.

## Code sample for a Page Interaction event handler

Review the following code sample for a Page Interaction event handler.

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
using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using kCura.EventHandler;

namespace PIBeginnerSample

{

    [System.Runtime.InteropServices.Guid("250B8988-45BE-45D9-9800-73B19D4F8DB7")]

    [kCura.EventHandler.CustomAttributes.Description("Insert a description for your Page Interaction Event Handler")]

    public class BeginnerPageInteractionEventHandler : kCura.EventHandler.PageInteractionEventHandler

    {

        // This sample page interaction event handler shows how to add inline Javascript functions

        // to the DOM from inside Relativity.

        public override Response PopulateScriptBlocks()

        {

            //Create an empty response object

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            retVal.Message = String.Empty;

            //Write an HTML script tag to hold your functions.

            String htmlToInsert = "<script type=\"text/javascript\"> " +

                "alert(\"a function has been added to this Object's layout\"); " +

                "document.body.setAttribute('new-attribute', 'value')" +

                "</script>";

            //Attach your script tag to the DOM and run the javascript after all elements have loaded.

            //Alternatively, register using this.RegisterClientScriptBlock() to run your function before loading elements.

            this.RegisterStartupScriptBlock(new kCura.EventHandler.ScriptBlock()

            {

                Key = "alertKey",

                Script = htmlToInsert

            });

            return retVal;

        }

    }

}
```

## Helper method for custom page URLs

The following code sample illustrates how to use a helper method to obtain the string path of the custom pages for an application on the web server. The GetRelativePathToCustomPages() method is available on the IUrlHelper interface in the Relativity.API namespace. For more information, see Use API helper classes and Simplify custom page URLs .

You may want to reference the RelativityInstanceURL instance setting if you are creating external links for users to access your application. Your Relativity admin can configure this value for your environment. See Instance setting table and Instance settings' descriptions on the Relativity Server 2025 Documentation site.

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
// This sample page interaction event handler shows how to add external CSS or JavaScript

// to an event handler using a custom page.

// This sample assumes you already have a custom page created.

public override Response PopulateScriptBlocks()

{

    //Create an empty response object.

    kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

    retVal.Success = true;

    retVal.Message = string.Empty;

    //Retrieve the URL to the custom page where your external files are stored.  Use your custom page application's GUID.

    string applicationPath = this.Helper.GetUrlHelper().GetRelativePathToCustomPages(new Guid("439e0ca3-cfbf-4940-a868-c9cd70d0368d"));

    //Append the file paths to the Javascript/CSS in your custom page project. The event now contains a reference to your custom logic.

    this.RegisterLinkedStartupScript(applicationPath + "Javascript/javascriptTest.js");

    this.RegisterLinkedCss(applicationPath + "Css/StyleSheetTest.css");

    return retVal;

}
```

On this page

- Page Interaction event handlers

- Guidelines for Page Interaction event handlers

- Code sample for a Page Interaction event handler

- Helper method for custom page URLs


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
