---
title: "Console event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Console_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:28:52+00:00
sha256: c42da20e283fae8f678bc5cb32b419e2738efbc7eb071fe88a34375d77c02a3b
---

Console event handlers

# Console event handlers

Console event handlers are ignored when your object type is using Relativity Forms, but the same functionality can achieved within Relativity Forms. For more information, see Relativity Forms API .

Console event handlers execute when a user clicks a console button in Relativity. The details view of an object may display a console, which contains header text and a button collection. When a user clicks a button, a call is made to a method in the event handler that contains the business logic for a specific task. In Relativity, the console has a GetConsole() method that returns a Console event handler. Console event handlers support custom HTML elements. You can use them on Relativity Dynamic Objects.

You can use a console event handler to control the workflow of a job or project. For example, you may expose buttons to insert a job into a queue table for background processing by an agent. Next, you may also want to track the progress of the job. You can display a link in the console so users can review errors if they occur. After resolving the errors, users can resubmit the job.

## Guidelines for Console event handlers

Use these guidelines when developing Console event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the ConsoleEventHandler class – extend the ConsoleEventHandler base class.

- Override the GetConsole() method – returns a console containing buttons and header text.

- Override the OnButtonClick() method – executes when a button click is detected.

- Override the RequiredFields property – returns a collection of fields that you need to access. The current layout doesn't need to include the fields.

- The ActiveArtifact.Fields collection includes the fields returned by the RequiredFields property, and those on the current layout. It also includes the values of these fields.

- Any Field in ActiveArtifact.Fields that is referenced in this event handler must be placed in the RequiredFields property.

- Optionally set the CssClass property on the ConsoleButton class – controls the styling used for a console button. If you don't set this property, the default Relativity styles used in console buttons are applied to your new button.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

- Optionally use event handlers to construct HTTP responses - event handlers can't access the request header, cookies, or session information using the HTTPContext object, although they can assisted in constructing an HTTP response.

## Code sample for a Console event handler

Review the following code samples for a Console event handler.

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
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
using System;

using System.Collections.Generic;

namespace ExampleEventHandlers

{

    /// <summary>

    /// This event handler creates a console with a button that could be used for

    /// initiating an action related to the RDO being viewed in the UI.

    /// </summary>

    [kCura.EventHandler.CustomAttributes.Description("Example Console Event Handler")]

    [System.Runtime.InteropServices.Guid("86ACD15E-2E9D-4988-85A7-357216E89170")]

    class ExampleConsoleEventHandler : kCura.EventHandler.ConsoleEventHandler

    {

        private readonly Guid NAME_FIELD_GUID = new Guid("716DDBA3-405B-48B8-AE9F-695511F7C4BB");

        private const String CONSOLE_TITLE = "Example Console";

        private const String BUTTON_ONE_NAME = "_button1";

        private const String BUTTON_ONE_DISPLAY_TEXT = "Button One";

        private const String BUTTON_ONE_TOOL_TIP = "Performs an action pertaining to this RDO.";

        private const String BUTTON_TWO_BUTTON_NAME = "_button2";

        private const String BUTTON_TWO_DISPLAY_TEXT = "Button Two";

        private const String BUTTON_TWO_TOOL_TIP = "Launches pop-up window.";

        public override kCura.EventHandler.Console GetConsole(kCura.EventHandler.ConsoleEventHandler.PageEvent pageEvent)

        {

            // Construct a console object to build the console appearing in the UI.

            kCura.EventHandler.Console returnConsole = new kCura.EventHandler.Console();

            returnConsole.Items = new List<kCura.EventHandler.IConsoleItem>();

            returnConsole.Title = CONSOLE_TITLE;

            // Construct button to raise post backs.

            kCura.EventHandler.ConsoleButton buttonOne = new kCura.EventHandler.ConsoleButton();

            buttonOne.Name = BUTTON_ONE_NAME;

            buttonOne.DisplayText = BUTTON_ONE_DISPLAY_TEXT;

            buttonOne.ToolTip = BUTTON_ONE_TOOL_TIP;

            buttonOne.Enabled = true;

            buttonOne.RaisesPostBack = true;

            // Construct button to open a new window.

            kCura.EventHandler.ConsoleButton buttonTwo = new kCura.EventHandler.ConsoleButton();

            buttonTwo.Name = BUTTON_TWO_BUTTON_NAME;

            buttonTwo.DisplayText = BUTTON_TWO_DISPLAY_TEXT;

            buttonTwo.ToolTip = BUTTON_TWO_TOOL_TIP;

            buttonTwo.RaisesPostBack = false;

            buttonTwo.Enabled = true;

            // Get the name of the artifact.

            kCura.EventHandler.Field nameField = ActiveArtifact.Fields[NAME_FIELD_GUID.ToString()];

            string rdoName = nameField.Value.Value.ToString();

            // Create the JavaScript for the button and set the button property.

            string pageUrl = $"https://www.google.com/search?q={rdoName}";

            string windowOpenJavaScript = $"window.open('{pageUrl}', '', 'location=no,scrollbars=yes,menubar=no,toolbar=no,status=no,resizable=yes,width=300,height=400');";

            buttonTwo.OnClickEvent = windowOpenJavaScript;

            // Add the buttons to the console.

            returnConsole.Items.Add(buttonOne);

            returnConsole.Items.Add(buttonTwo);

            return returnConsole;

        }

        public override void OnButtonClick(kCura.EventHandler.ConsoleButton consoleButton)

        {

            // Determine which button was clicked.

            if (consoleButton.Name == BUTTON_ONE_NAME)

            {

                // Take action...

            }

        }

        /// <summary>

        /// Specify any fields that need to be populated on the

        /// ActiveArtifact when GetConsole() is invoked.

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get

            {

                kCura.EventHandler.FieldCollection retVal = new kCura.EventHandler.FieldCollection();

                retVal.Add(new kCura.EventHandler.Field(NAME_FIELD_GUID.ToString()));

                return retVal;

            }

        }

    }

}
```
