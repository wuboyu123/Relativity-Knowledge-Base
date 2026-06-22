---
title: "Sample: Converting a Classic Form to a Relativity Form"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Convert_to_Relativity_Forms.htm
collection: developer
fetched_at: 2026-06-22T06:31:50+00:00
sha256: 155b505bbd7b7a7db215104b8e7c000695b8ac363534a6abc1bb3411478da163
---

Sample: Converting a Classic Form to a Relativity Form

# Sample: Converting a Classic Form to a Relativity Form

You may need to make changes to your code or customizations to migrate from Classic Forms to Relativity Forms. This topic is an example scenario where we will migrate a basic classic form with two event handlers ( a console event handler and a page interaction event handler) to a Relativity Form.

- Console Event Handler - adds a button that pops up a window alert message.

- Page Interaction Event Handler - is used to show/hide one field depending on a different field's value.

## Setting up the classic form

Complete the following steps to set up the classic form event handlers:

- Create an object type.

- Add the following fields to the object type:

Field Name Type Required

Display Hidden Field?

Yes/No Yes

Hidden Field Fixed-Length Text No

-

Edit the default layout of the object type:

- Add Display Hidden Field? and Hidden Field to the layout.

- In Display Hidden Field? , select Radio Button in the Display Type dropdown.

- Enter 2 in the Repeat Columns field.

- Create a Console Event Handler:

Copy

Create a Console Event Handler

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

using kCura.EventHandler;

namespace ConsoleEventHandler {

  [kCura.EventHandler.CustomAttributes.Description("Basic Console EventHandler")]

  [System.Runtime.InteropServices.Guid("796805a5-089a-479e-9cec-968e02eab80d")]

  public class BasicConsoleEventHandler: kCura.EventHandler.ConsoleEventHandler {

    private const String CONSOLE_TITLE = "Demo Console";

    private const String BUTTON_NAME = "_DisplayInfo";

    private const String BUTTON_DISPLAY_TEXT = "Display Info";

    private const String MESSAGE = "Display Info console button clicked";

    public override kCura.EventHandler.Console GetConsole(PageEvent pageEvent) {

      // Create a console with a title

      kCura.EventHandler.Console returnConsole = new kCura.EventHandler.Console() {

        Items = new List<IConsoleItem>(), Title = CONSOLE_TITLE

      };

      // Initialize button

      kCura.EventHandler.ConsoleButton getInfoButton = new kCura.EventHandler.ConsoleButton();

      getInfoButton.Name = BUTTON_NAME;

      getInfoButton.DisplayText = BUTTON_DISPLAY_TEXT;

      getInfoButton.Enabled = true;

      getInfoButton.OnClickEvent = $ "window.alert('{MESSAGE}')";

      // Add button to the console

      returnConsole.Items.Add((getInfoButton));

      return returnConsole;

    }

    public override void OnButtonClick(kCura.EventHandler.ConsoleButton consoleButton) {}

    /// <summary>

    /// If you don't need access to any specific field on the parent, you can return an empty list.

    /// </summary>

    public override kCura.EventHandler.FieldCollection RequiredFields {

      get {

        kCura.EventHandler.FieldCollection retVal = new kCura.EventHandler.FieldCollection();

        return retVal;

      }

    }

  }

}
```

- Create a Page Interaction Event Handler:

Copy

Create a Page Interaction Event Handler

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
using System;

using kCura.EventHandler;

namespace PageInteractionEventHandler {

  [kCura.EventHandler.CustomAttributes.Description("Page Interaction EventHandler")]

  [System.Runtime.InteropServices.Guid("b8f7f065-92f4-4b93-9fcc-fcea596a950f")]

  public class PageInteractionEventhandler: kCura.EventHandler.PageInteractionEventHandler {

    public override Response PopulateScriptBlocks() {

      //Create a response object with default values

      kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

      retVal.Success = true;

      retVal.Message = string.Empty;

      // Creating a common function that be used elsewhere in the page

      String changeFunction = "<script type=\"text/javascript\">" +

        "function hideField(toHide) {" +

        "   document.querySelector(\"[fafriendlyname = 'Hidden Field']\").parentElement.hidden = !toHide;" +

        "}" +

        "</script>";

      this.RegisterClientScriptBlock(new kCura.EventHandler.ScriptBlock() {

        Key = "changeFunc", Script = changeFunction

      });

      // 'Main' block of the page interaction event handler

      String startUp = "<script type=\"text/javascript\"> " +

        "$( document ).ready(function() {" +

        // Since the object type has a Console event handler we can determine

        // when the form is a view form by the existence of the console

        "if(!document.querySelector('.consoleContainer')) {" +

        "   var toHideField = document.querySelector(\"[fafriendlyname='Display Hidden Field?']\").parentElement;" +

        "   var radio = toHideField.childNodes[2];" +

        "    var yesRadio = radio.querySelectorAll(\"[type = 'radio']\")[0];" +

        "   hideField(yesRadio.checked);" +

        //  Adding onClick Event to radio group to trigger when to hide/show field

        "   toHideField.onclick = function() { " +

        "       var yesRadio = radio.querySelectorAll(\"[type = 'radio']\")[0];" +

        "       hideField(yesRadio.checked);" +

        "   };" +

        " } else { " +

        // Show/Hide field in view mode

        "   var toHideField = document.querySelector(\"[fafriendlyname='Display Hidden Field?']\").parentElement;" +

        "   var toHide = toHideField.childNodes[2].textContent === 'Yes';" +

        "   hideField(toHide);" +

        "}});" +

        "</script>";

      this.RegisterStartupScriptBlock(new kCura.EventHandler.ScriptBlock() {

        Key = "startup", Script = startUp

      });

      return retVal;

    }

  }

}
```

- Add the event handlers to the created Object. For more information, see Adding an event handler .

## Migrating to Relativity Forms

Now that you have created the classic form, complete the following steps to transition the event handlers in to the Relativity Forms API.

- Create a JavaScript file that will be used for the new forms event handler:

Copy

forms event handler (JS)

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
(function tutorialjs(eventNames, convenienceApi) {

  ////////////////////////////////////////////////////////////////////

  ////////////////////       tutorial.js       ///////////////////////

  ////////////////////////////////////////////////////////////////////

  var eventHandlers = {};

  ////////////////////////////////////////////////////////////////////

  //////////////////// EVENT HANDLER FORM CODE ///////////////////////

  ////////////////////////////////////////////////////////////////////

  return eventHandlers;

}(eventNames, convenienceApi));
```

- Add a reference to the JavaScript file in the page interaction event handler's ScriptFileNames property:

Copy

reference to the JavaScript file

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
using System;

using kCura.EventHandler;

namespace PageInteractionEventHandler {

  [kCura.EventHandler.CustomAttributes.Description("Page Interaction EventHandler")]

  [System.Runtime.InteropServices.Guid("b8f7f065-92f4-4b93-9fcc-fcea596a950f")]

  public class PageInteractionEventhandler: kCura.EventHandler.PageInteractionEventHandler {

    public override Response PopulateScriptBlocks() {

      kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

      //

      // Existing code can be left alone since the PopulateScriptBlocks gets ignored

      // by Relativity Forms.

      //

      return retVal;

    }

    public override string[] ScriptFileNames {

      get {

        return new string[] {

          "tutorial.js"

        };

      }

    }

  }

}
```

### Converting the console event handler

When converting a classic console event handler to a Relativity Forms event handler there are a couple of key considerations:

- Determine if the console is dynamic and updates due to page interaction. If the console is dynamic an UPDATE_CONSOLE hook will also need to be created.

- Take advantage of functionality the Console API has for creating common console workflows.

Copy

common console workflows

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
(function tutorialjs(eventNames, convenienceApi) {

  ////////////////////////////////////////////////////////////////////

  ////////////////////       tutorial.js       ///////////////////////

  ////////////////////////////////////////////////////////////////////

  var eventHandlers = {};

  /////////////////////////////////////////

  /* Console Event Handler Code Follows: */

  /////////////////////////////////////////

  var MESSAGE = "Display Info console button clicked";

  function createAlert() {

    window.alert(MESSAGE);

  };

  eventHandlers[eventNames.CREATE_CONSOLE] = function() {

    var BUTTON_DISPLAY_TEXT = "Display Info";

    var CONSOLE_TITLE = "Demo Console";

    // Construct the html element that is needed for the console title

    var titleElement = convenienceApi.console.generate.title({

      innerText: CONSOLE_TITLE

    });

    // Construct the html element that is needed for the console title

    // Adding the button to a section to make the console nicely formatted

    var sectionElement = convenienceApi.console.generate.section({},

      [

        convenienceApi.console.generate.button({

          innerText: BUTTON_DISPLAY_TEXT,

          onclick: function(e) {

            createAlert();

          },

          disabled: false

        })

      ]);

    // retrieve the console html element and append the title and section elements.

    return convenienceApi.console.containersPromise.then(function(containers) {

      var rootElement = containers.rootElement;

      rootElement.innerHTML = "";

      rootElement.appendChild(titleElement);

      rootElement.appendChild(sectionElement);

    });

  }

  return eventHandlers;

}(eventNames, convenienceApi));
```

### Converting the page interaction event handler

When converting a page interaction event handler to a Relativity Forms event handler there are a couple of key considerations:

- Determine what new lifecycle hooks should be used to cover the functionality of the classic page interaction event handler. Classic functionality may span multiple pipelines (Load, Change, Submit, Delete).

Copy

lifecycle hooks

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
(function tutorialjs(eventNames, convenienceApi) {

  ////////////////////////////////////////////////////////////////////

  ////////////////////       tutorial.js       ///////////////////////

  ////////////////////////////////////////////////////////////////////

  var eventHandlers = {};

  //

  // Console Event Handler Code

  //

  //////////////////////////////////////////////////

  /* Page Interaction Event Handler Code Follows: */

  //////////////////////////////////////////////////

  // Sets the hidden field to show/hide on initial load

  eventHandlers[eventNames.HYDRATE_LAYOUT_COMPLETE] = function() {

    var displayHiddenId = this.fieldNameToFieldIdMap.get("Display Hidden Field?");

    var hiddenFieldId = this.fieldNameToFieldIdMap.get("Hidden Field");

    convenienceApi.fieldHelper.getValue(displayHiddenId).then(function(value) {

      convenienceApi.fieldHelper.setIsHidden(hiddenFieldId, !value);

    });

  };

  // Modifies the hidden field to show/hide during page interactions

  eventHandlers[eventNames.PAGE_INTERACTION] = function(modelData, event) {

    var payload = event.payload;

    var type = event.type;

    // The hidden field show/hide is driven by when the "Display Hidden Field?" is changes value

    if (type === "change") {

      var displayHiddenId = this.fieldNameToFieldIdMap.get("Display Hidden Field?");

      var hiddenFieldId = this.fieldNameToFieldIdMap.get("Hidden Field");

      switch (payload.fieldId) {

        case displayHiddenId:

          //modelData contains the updated values from the change event

          convenienceApi.fieldHelper.setIsHidden(hiddenFieldId, !modelData[displayHiddenId]);

          break;

        default:

          break;

      }

    }

  };

  return eventHandlers;

}(eventNames, convenienceApi));
```

### Updating Relativity assets

Complete the following steps to update the Relativity Assets for the new event handlers:

- Update the Page Interaction Event Handler DLL to the final version that contains the ScriptFileNames Override.

- Add the JavaScript file you created to the Relativity instance. For more information, see Updating Custom Event Handler Scripts

- Enable the object type to use Relativity Forms. (For more information, see Creating and editing Relativity Objects )

Once you have applied your changes, you should see your form rendered using Relativity Forms:
