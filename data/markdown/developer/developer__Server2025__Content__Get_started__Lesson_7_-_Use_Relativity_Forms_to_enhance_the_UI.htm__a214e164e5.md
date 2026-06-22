---
title: "Lesson 7 - Use Relativity Forms to enhance the UI"
url: https://platform.relativity.com/Server2025/Content/Get_started/Lesson_7_-_Use_Relativity_Forms_to_enhance_the_UI.htm
collection: developer
fetched_at: 2026-06-22T06:25:03+00:00
sha256: 78f02d018257e0e372c11640b96dbd22bdfad9ee219f77e95e0619ae69304dd5
---

Lesson 7 - Use Relativity Forms to enhance the UI

# Lesson 7 - Use Relativity Forms to enhance the UI

Relativity Forms is a layout-rendering option, providing robust JavaScript APIs and a granular front-end page life cycle for easier, more controlled Relativity object customization.

In this lesson, you will learn how to complete these tasks:

- Develop your familiarity with key concepts for Relativity Forms.

- Use Relativity Forms to create customization for layouts in Relativity.

- Customize the UI within Relativity Dynamic Objects (RDOs) using the Relativity Forms APIs.

- Create an event handler to customize the UI for a layout.

- Update a layout by changing the display type for specific fields. In this lesson, you will update the display of the Automatic Updates Enabled and Overwrite Article Text fields from checkboxes to toggles.

Estimated completion time - 2 hours

PREVIOUS LESSON

Lesson 6 - Create a custom page ››

## Step 1 - Pre-work

Use the following steps to prepare your Relativity application for updates:

- Verify the Hello Wikipedia application is installed in your workspace and pushed to the Application Library.

- Navigate to the details view of the Hello Wikipedia application.

- Click Unlock Application .

- Use the following steps to enable the Article Category object for Relativity Forms:

- On the details view of the Hello Wikipedia application, locate the Object Type section and click the Edit link for the Article Category object type.

- Select Yes for the Use Relativity Forms field .

- Click Save .

When the Article Category object is loaded, it renders with Relativity Forms.

## Step 2 - Set up the project folders and create an event handler in Visual Studio

Use the following steps to set up the root folder, WikipediaForms, and create a PageInteractionEventHandler for this lesson:

- Open Visual Studio.

- Open the HelloWikipedia solution created in Lesson 3 - Create a RESTful API .

- Create a new project in the HelloWikipedia solution and select the Class Library (.Net Framework) template.

- Click Next to display the Configure your new project dialog.

- Enter the following information:

- Project name – PageInteractionEventHandlers

- Location - This field is automatically populated with the solution path when you add a new project to the HelloWikipedia solution. Add \WikipediaForms to the end of this path.

- Framework - .NET Framework 4.6.2

- Click Create .

- Verify that the solution contains the PageInteractionEventHandlers project.

- In the PageInteractionEventHandlers project, rename class file from Class1.cs to ArticleCategoryPageInteractionEventHandler.cs and rename the class within the file, if Visual Studio doesn't prompt to rename it for you.

- Add the Relativity.Server.EventHandler.SDK package in Visual Studio.

- Add a GUID for the event handler:

- Set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler.

- Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute to provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PageInteractionEventHandler class by extending the base class for this type of event handler.

- Override the PopulateScriptBlocks() method.

Relativity Forms ignores the PopulateScriptBlocks() method, so you need only return an empty kCura.EventHandler.Response .

- Override the ScriptFileNames property by returning a string array containing articleCategory.js .

This update ensures that Relativity Forms recognizes the JavaScript file as an event handler.

- Compare the following sample code with your implementation of the Article Category Page Interaction event handler: Copy

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
using System;

using kCura.EventHandler;

namespace HelloWikipedia.PageInteractionEventHandlers

{

    [kCura.EventHandler.CustomAttributes.Description("HelloWikipedia ArticleCategory Page Interaction EventHandler")]

    [System.Runtime.InteropServices.Guid("13a13a13-a13a-1313-a241-a241a241a241")]

    public class ArticleCategoryPageInteractionEventHandler : kCura.EventHandler.PageInteractionEventHandler

    {

        public override Response PopulateScriptBlocks()

        {

            return new kCura.EventHandler.Response();

        }

        public override string[] ScriptFileNames => new string[] { "articleCategory.js" };

    }

}
```

## Step 3 - Create a JavaScript file for an event handler

Use the following steps to create a file for your event handler:

- In the root folder, WikipediaForms, create a folder called JavaScript .

- Create a file called articleCategory.js in the JavaScript folder.

You can add this file through Visual Studio Code or Windows Explorer.

- Update the stub detail in the following code block: Copy

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
(function (eventNames, convenienceApi, privilegedEnvelope) {

    var vars = privilegedEnvelope || {};

    var eventHandlers = {};

    console.log("Hello From Article Category.js");

    return eventHandlers;

}(eventNames, convenienceApi, privilegedEnvelope));

// eof
```

## Step 4 - Associate the event handler with an object type

Use the following steps to associate an event handler with an object type:

- Build your PageInteractionEventHanders.dll by building the solution in Visual Studio.

- Log in to the Relativity instance on your DevVM.

- Navigate to the Resource File tab and click New Resource File .

The Resource File Information dialog appears. For more information, see Resource files on the Relativity Documentation site.

- In the Application field, click to select the Hello Wikipedia application.

You need to associate your custom files with this application.

- In the Resource File field, click Browse to select the PageInteractionEventHanders.dll .

- Click Save and New .

- Repeat steps 4-6 for the articleCategory.js file.

Because you upload these files separately, they don't need to be embedded in your .NET project. See Add event handlers to applications .

- Complete these steps to associate your event handler with an object type: In your workspace, associate the newly uploaded Page Interaction event handler with the Article Category object types as in Lesson 4 - Validate object changes .

.

- Navigate to the details view of the Hello Wikipedia application.

- Click Push to Library in the Application Console.

This action automatically locks the application.

- Click Unlock Application in the Application Console.

The Hello Wikipedia application is unlocked so you can now update it.

- Navigate to the Article Category form page.

It should automatically run the code in the articleCategory.js file.

- Navigate to the Article Category list page to complete these steps:

- Open developer tools to display the Console tab in your preferred browser.

- Click New Article Category .

- Check the browser console for output from your event handler by pressing F12 while in your browser and navigating to the Console tab.

## Step 5 - Add functionality to the JavaScript event handler

Use the following steps to add functionality to the event handler:

- Complete the following steps to add GUIDs to reference your fields:

- Locate the GUIDs for the Article Category layout and Article Category’s Automatic Updates Enabled and Overwrite Article Text fields in the XML for the application.

To view the GUIDs, navigate to the details view of the Hello Wikipedia application and click Show Component GUIDs in the Application console.

- In the articleCategory.js file, set the GUIDs for Layout and Field as an object properties on vars called GUIDS as in the code for step c.

- Insert the following code in a newline after the code console.log("Hello From Article Category.js"); , and updated the GUIDs with the values for your application. Copy

```text
1
2
3
4
5
vars.GUIDS = {

   SAMPLE_LAYOUT: "9f195c94-30aa-4e9c-9939-e4c5c05f6193",

   FIELD_AUTOMATIC_UPDATES: "f365de2e-a641-428f-9188-a3970a7c308f",

   FIELD_OVERWRITE_TEXT: "042e0329-1467-4993-8188-66615e103de3"

};
```

- Complete these steps to use a TRANSFORM_LAYOUT event handler to update the display types of the Automatic Updates Enabled and Overwrite Article Text fields:

- Get the GUIDS for the active layout via this bindings layoutMetadataCopy.Guids.

- Verify that the current GUIDs for Layouts contain the Layout defined in the object property.

- Get and iterate through all the fields.

- Target and update the display type for the Automatic Updates Enabled and Overwrite Article Text fields.

See the following code that you need to insert on a newline after the previous snippet using the GUIDs from step a: Copy

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
    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function (layoutData) {

            // 1. Ensure we are only transforming the correct layout

        var layoutGuids = this.layoutMetadataCopy.Guids;

        if(layoutGuids.indexOf(vars.GUIDS.SAMPLE_LAYOUT.toLowerCase()) >= 0) {

            // 2. Get and iterate the Fields (for the layout)

            var fields = convenienceApi.layout.getFields(layoutData);

            fields.forEach(function (field) {

                // 3. Is the Field one of the Fields for which we're looking?

                if (field.Guids.indexOf(vars.GUIDS.FIELD_AUTOMATIC_UPDATES.toLowerCase()) >= 0 ||

                    field.Guids.indexOf(vars.GUIDS.FIELD_OVERWRITE_TEXT.toLowerCase()) >= 0) {

                    // 4. If so, change the DisplayType to "Toggle"

                    field.DisplayType = "Toggle";

                }

            });

        }

    };
```

- Verify that the final code in articleCategory.js file is like the following sample code. Copy

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
(function (eventNames, convenienceApi, privilegedEnvelope) {

    var vars = privilegedEnvelope || {};

    var eventHandlers = {};

    console.log("Hello From Article Category.js");

    vars.GUIDS = {

       SAMPLE_LAYOUT: "ACF6E4CA-3074-4261-AD4B-1362B4D970AD",

       FIELD_AUTOMATIC_UPDATES: "448DB41B-7A15-4428-A3F6-3E83E9DAA96F",

       FIELD_OVERWRITE_TEXT: "A1D203B4-2A52-46B9-9077-F2EA8DB6C0FC"

    };

    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function (layoutData) {

        // 1. Ensure we are only transforming the correct layout

        var layoutGuids = this.layoutMetadataCopy.Guids;

        if(layoutGuids.indexOf(vars.GUIDS.SAMPLE_LAYOUT.toLowerCase()) >= 0) {

            // 2. Get and iterate the Fields (for the layout)

            var fields = convenienceApi.layout.getFields(layoutData);

            fields.forEach(function (field) {

                // 3. Is the Field one of the Fields for which we're looking?

                if (field.Guids.indexOf(vars.GUIDS.FIELD_AUTOMATIC_UPDATES.toLowerCase()) >= 0 ||

                    field.Guids.indexOf(vars.GUIDS.FIELD_OVERWRITE_TEXT.toLowerCase()) >= 0) {

                    // 4. If so, change the DisplayType to "Toggle"

                    field.DisplayType = "Toggle";

                }

            });

        }

    };

    return eventHandlers;

}(eventNames, convenienceApi, privilegedEnvelope));

// eof
```

- Update your articleCategory.js file in your Relativity instance by uploading it through the Resource Files tab.

- Click Clear in the Resource File field.

- Select your updated articleCategory.js to add as a new resource file.

- Click Save .

- Verify that the Automatic Updates Enabled and Overwrite Article Text fields now appear as toggle components.

View troubleshooting steps

If the layout didn't update, the browser may be caching the page. To correct this issue, use the development tools in the browser to clear the cache. In Chrome, use the following steps:

- Open the developer tools for the browser.

- Select the Network tab.

- Select Disable Cache .

- From the Network tab in the developer tools, right-click the Reload button near the URL bar.

- Click Empty Cache and Hard Reload .

- Navigate to the details view for the Hello Wikipedia application.

- Click Push to Library .

## Step 6 - Test your JavaScript

This step contains the following subsections describing how to set up your testing environment and run unit tests:

- Configure your development machine

- Configure your project

- Add files for unit testing

- Add a unit test

- Run the unit test

### Configure your development machine

To run the JavaScript tests, download and install Node.js from nodejs.org . This lesson uses version 8 or higher.

### Configure your project

Use the following steps to configure your project for unit testing:

- Navigate to the root directory.

This directory is the parent folder of the JavaScript folder called WikipediaForms . See Step 2 - Set up the project folders and create an event handler in Visual Studio .

- Use the following commands to initialize npm and the dependencies for this project. Copy

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
// Create the package.json file in your project

npm init -y

// install karma test runner and plugins, including the testing framework, Jasmine

npm install karma karma-jasmine karma-chrome-launcher jasmine-core --save-dev

// Create karma.conf.js

node ./node_modules/karma/bin/karma init

// Provide the following answers.  ">  " means to leave it blank, simply pressing enter to skip the question.

Which testing framework do you want to use ?

Press tab to list possible options. Enter to move to the next question.

> jasmine

Do you want to use Require.js ?

This will add Require.js plugin.

Press tab to list possible options. Enter to move to the next question.

> no

Do you want to capture any browsers automatically ?

Press tab to list possible options. Enter empty string to move to the next question.

> ChromeHeadless

>

What is the location of your source and test files ?

You can use glob patterns, eg. "js/*.js" or "test/**/*Spec.js".

Enter empty string to move to the next question.

>

Should any of the files included by the previous patterns be excluded ?

You can use glob patterns, eg. "**/*.swp".

Enter empty string to move to the next question.

>

Do you want Karma to watch all the files and run the tests on change ?

Press tab to list possible options.

> no
```

- Update the package.json file as follows:

- Set the "name" property to "hellowikipedia-forms" .

- After the "descriptions" property, add the property called "private" , and set its value to true .

- Under the "scripts" property, Set the "test" property as follows:

- For Node 14, set it as "test": "karma start" .

- For Node 12 and earlier, set it as "test": "karma start --experimental-modules" .

- Verify that your file is like this package.json example.

Your versions for the devDependencies may differ from this example. Copy

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
{

  "name": "hellowikipedia-forms",

  "version": "1.0.0",

  "description": "",

  "private": true,

  "scripts": {

    "test": "karma start --experimental-modules"

  },

  "keywords": [],

  "author": "",

  "license": "ISC",

  "devDependencies": {

    "jasmine-core": "^3.6.0",

    "karma": "^5.2.0",

    "karma-chrome-launcher": "^3.1.0",

    "karma-jasmine": "^4.0.1"

  }

}
```

- Update the karma.conf.js file as follows:

- Set the "singleRun" property to true .

- Updates the "files" property as follows:

With this update, Karma serves all your JavaScript files and immediately includes any test files as ES6 modules. The event handlers must be written in ES5.1 and earlier code, but the tests are in ES6 to eliminate dependency management in testing.

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
// change this:

files: [

],

// to this:

files: [

    { pattern: 'JavaScript/**/!(*.spec).js', watched: true, included: false, served: true }, // non-test regular js files

    { pattern: 'JavaScript/**/*.spec.js', watched: true, included: true, served: true , type: "module" } // test files

],
```

### Add files for unit testing

Use the following steps to add files for unit testing:

- In the JavaScript folder, create the following files:

- articleCategory.spec.js - Write the unit tests for articleCategory.js in this file. The spec.js is the file extension that you have configured Karma to use when looking for files containing unit tests.

- testHelper.js - Add operations for use across any test files for Relativity Forms event handlers that you write. For example, you might also write Relativity Forms event handlers for the Article Reference object. The code added to this file mimics how Relativity Forms binds the Relativity Forms API entities, such as the convenienceApi, to your event handlers.

- Add the following code to the testHelper.js file.

This file uses ES6 for the JavaScript modules syntax. It exports its contents individually, but the getEventHandlers() function is the default export and handles most of the work. Copy

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
export const EVENT_NAMES = {

   EVENT_HANDLERS_REGISTERED: "eventHandlersRegistered",

   VALIDATION: "validation",

   TRANSFORM_LAYOUT: "transformLayout",

   HYDRATE_LAYOUT: "hydrateLayout",

   HYDRATE_LAYOUT_COMPLETE: "hydrateLayoutComplete",

   REPLACE_OBTAIN_ADDITIONAL_DATA: "replaceObtainAdditionalData",

   POST_OBTAIN_ADDITIONAL_DATA: "postObtainAdditionalData",

   PAGE_LOAD_COMPLETE: "pageLoadComplete",

   PAGE_UNLOAD: "pageUnload",

   CREATE_ACTION_BAR: "createActionBar",

   CREATE_CONSOLE: "createConsole",

   OVERRIDE_PICKER_DATASOURCE: "overridePickerDataSource",

   PAGE_INTERACTION: "pageInteraction",

   PRE_SAVE: "preSave",

   POST_SAVE: "postSave",

   REPLACE_READ: "replaceRead",

   REPLACE_SAVE: "replaceSave",

   REPLACE_GET_NEW_OBJECT_INSTANCE: "replaceGetNewObjectInstance",

   UPDATE_ACTION_BAR: "updateActionBar",

   UPDATE_CONSOLE: "updateConsole",

   VALIDATE_SAVE: "validateSave",

   ITEM_LIST_RELOADED: "itemListReloaded",

   PRE_DELETE: "preDelete",

   REPLACE_DELETE: "replaceDelete",

   POST_DELETE: "postDelete",

   ITEM_LIST_MODIFY_COLUMNS: "itemListModifyColumns",

   ITEM_LIST_MODIFY_ACTIONS: "itemListModifyActions",

   REPLACE_READ_DELETE_DEPENDENCY_LIST: "replaceReadDeleteDependencyList",

   REPLACE_FILE_ACTIONS: "replaceFileActions"

};

export function getFileTextContent(fileUrl) {

   if (!fileUrl) { throw new Error("fileUrl must not be empty"); }

   const fileTextContentPromise = fetch(`base/JavaScript/${fileUrl}`, { method: "GET" }).then((response) => {

      if (!response.ok) {

         throw new Error(`request for ${fileUrl} failed. Reason: ${response.statusText} (${response.status})`);

      }

      const fileTextContent = response.text();

      return fileTextContent;

   });

   return fileTextContentPromise;

};

export function createEventHandlersFromTextFileContent(fileTextContent, settings = {}) {

   const { convenienceApi, privilegedEnvelope } = settings;

   const eventHandlers = new Function(

      "eventNames",

      "convenienceApi",

      "privilegedEnvelope",

      `"use strict"; return ${fileTextContent}`

   )(EVENT_NAMES, convenienceApi, privilegedEnvelope);

   return eventHandlers;

}

export function getEventHandlers(sourceFileUrl, settings) {

   const contentPromise = getFileTextContent(sourceFileUrl);

   const eventHandlersPromise = contentPromise.then(

      (fileTextContent) => {

         return createEventHandlersFromTextFileContent(

         fileTextContent,

         settings);

      }

   );

   return eventHandlersPromise;

}

export default getEventHandlers;

// eof
```

View information about the getEventHandlers() function

The getEventHandlers() function contains the following functionality:

- Takes the sourceFileUrl and settings parameters.

- Fetches the content of sourceFileUrl as text and executes it as a function.

- Supplies EVENT_NAMES as eventNames and the settings from the convenienceApi to the sourceFileUrl as part of the Relativity Forms API during the tests.

- Optionally, supplies privilegedEnvelope to the sourceFileUrl as part of the Relativity Forms API during the tests.

- Supports the following settings for parameters:

Parameter Description

sourceFileUrl: String The path and file name of your file. In this lesson, the path is relative to the JavaScript folder.

settings: Object

The following the properties on the settings object provide these advantages:

- Control within the tests to ensure that they are atomic.

- Ability to mock or spy on convenienceApi functions.

- When using convenienceApi with the vars object as in the code in this lesson, these properties offer fine-grained control of setup before the execution of event handlers. They also offer shared data checking afterward, and unit testing for your helper functions, which might otherwise be private and inaccessible for testing.

Use these properties on the settings object during the tests:

Property Type Description

convenienceApi Object

The object used as the convenienceApi during your tests. It should be kept slim based on the needs of a given test. Only provide as much surface area as used in the operations under test.

privilegedEnvelope Object (optional, defaults to null) An object used to expose otherwise private data or functions from within your event handler file to the unit tests. Relativity Forms always sends null for this value. Nothing assigned to privilegedEnvelope is externally supplied to the production code. Its purpose is only to provide greater ease and control while testing.

- Returns a Promise<Object>. This Promise resolves into your eventHandlers Object with settings-supplied items bound to it.

### Add a unit test

In this step, you use a JavaScript testing framework called Jasmine . Review the Getting Started page on the Jasmine website for more information.

- Add the following code to the articleCategory.spec.js file.The code for this test contains the following functionality:

- Line 1 - Pulls the default export of testHelper.js and names that function getEventHandlers.

- Line 3 - Creates a group of tests called articleCategory.js event handlers . This test group is called a suite .

- Line 9 - Creates a single test, called a spec , with the name has the expected surface area . This test is async because it contains a done parameter. All your Relativity Forms unit tests should be async, which requires you to invoke done() upon the completion of your test's assertions.

- Line 10 - The spec creates event handlers from articleCategory.js, omitting the settings object. The testHelper.js file substitutes an empty object for settings. As a result, when the event handlers are created, no value is bound for convenienceApi. This practice is acceptable only for this specific type of test, and only when the articleCategory.js file doesn't make use of the convenienceApi in the immediately invoked sections.

- Lines 11-18 - At Promise resolution, the eventHandlers object is supplied to the main portion of this test.

The test itself iterates over the names of each expected event handler function in lines 4-6, asserting that the eventHandlers object has such a property, defined as a function. After all expected functions are checked, the properties on the eventHandlers object are checked for existence in the expected handlers array. This step ensures that only the required handlers are included.

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
import getEventHandlers from "./testHelper.js";

describe("articleCategory.js event handlers", () => {

   const EXPECTED_SURFACE_AREA = [

      "transformLayout"

   ];

   const FILE_NAME = "articleCategory.js";

   it("has the expected surface area", (done) => {

      getEventHandlers(FILE_NAME).then((eventHandlers) => {

         expect(typeof eventHandlers).toBe("object", "Event handlers object not returned.\nIs this file a well-formed immediately invoked function expression (iife)?\nBe sure the file's first line is the beginning of the iife, and not a comment or empty line.");

         EXPECTED_SURFACE_AREA.forEach((eventName) => {

            expect(typeof eventHandlers[eventName]).toBe("function",`Expected event handler function '${eventName} expected' is missing.`);

         });

         for(let memberName in eventHandlers) {

            expect(EXPECTED_SURFACE_AREA.indexOf(memberName)).toBeGreaterThanOrEqual(0, `Unexpected ${typeof eventHandlers[memberName]} property on event handlers: '${memberName}'`);

         }

         done();

      }).catch(done.fail);

   });

});
```

- Save the file.

### Run the unit test

In this section, you run a command that starts Karma and executes all tests from each file with the .spec.js extension in the JavaScript folder.

Use the following steps to run the code:

- Enter the following at the command line: Copy

```text
1
npm test
```

- Verify that your output looks like the following code: Copy

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
PS S:\SourceCode\platform\ads\Source\WikipediaForms> npm test

> hellowikipedia-forms@1.0.0 test S:\SourceCode\platform\ads\Source\WikipediaForms

> karma start --experimental-modules

03 09 2020 14:19:14.872:INFO [karma-server]: Karma v5.2.0 server started at http://localhost:9876/

03 09 2020 14:19:14.879:INFO [launcher]: Launching browsers ChromeHeadless with concurrency unlimited

03 09 2020 14:19:14.884:INFO [launcher]: Starting browser ChromeHeadless

03 09 2020 14:19:18.029:INFO [Chrome Headless 84.0.4147.135 (Windows 10)]: Connected on socket UW5f9zaRceX8BSwEAAAA with id 53968789

Chrome Headless 84.0.4147.135 (Windows 10): Executed 1 of 1 SUCCESS (0.026 secs / 0.016 secs)

TOTAL: 1 SUCCESS

PS S:\SourceCode\platform\ads\Source\WikipediaForms>
```

## Step 7 - Additional activities with Relativity Forms

You can find additional examples of how to use Relativity Forms to modify the UI in the following workshops and other content:

- relativity-forms-workshop-fest-2019 - a GitHub repository for the Fest 2019 workshop.

- Fest 2019 Workshop - Relativity Forms API - documentation for the Fest 2019 workshop. In section 5 on page 24, you can find information about how to show or hide a field based on the values of another field during change events for page interaction, and for values on load.

- relativity-forms-workshop-fest-2019 source code - a GitHub repository with the starting code for the workshop.

- relativity-forms-workshop-fest-2019 workshop solutions - a GitHub repository with the solution for each exercise.

- relativity-forms-workshop-fest-2019 field manipulation exercise - a GitHub repository containing the relativityFormsConversion.js file.
