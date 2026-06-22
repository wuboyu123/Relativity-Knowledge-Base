---
title: "convenienceAPI object"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/convenienceApi_object.htm
collection: developer
fetched_at: 2026-06-22T06:32:01+00:00
sha256: a230d4456740a09240b6eeca154d3a79fc7942a66a2ae3fbabcaad84928af648
---

convenienceAPI object

# convenienceAPI object

As part of the Relativity Forms API, the convenienceApi object provides methods designed to simplify event handler development. You can use these methods to make service calls, localize content, and perform other tasks. Additionally, you can inject the convenienceApi object into an immediately invoked function expression (IIFE) event handler as a second parameter.

## Summary of APIs for convenienceApi object

The following table lists each of the APIs available for use with the convenienceApi object.

API or object

Description

actionBar

Includes methods for creating and updating the contents of an action bar.

additionalData

Provides a method for getting additional data.

applicationPaths

Represents an object used to supply application paths specific to Relativity.

console

Provides property and methods for creating a console on a page.

constants

Provides access to certain constants used globally in an application.

dateTime

Represents a date-time value formatter.

fieldHelper

Includes methods for quickly accessing and modifying fields.

formSettings

Represents an object that contains general settings related to the user viewing a form and the artifact displayed in it.

ItemListDataProviderFactory

Factory that can be used to create ItemListDataProviders which can be used in single and multi-list picker modals

itemListHelper

Includes methods for quickly accessing and modifying item lists.

i18n

Represents an i18n object that contains methods used for application internationalization.

layout

Modifies layouts.

logFactory

Returns an instance of Aurelia logger.

modalService

Provides a service that can be used to open various modals in an application.

permission

Represents a permission object exposed as a part of the Event Handler API. It is used to check actions allowed for an object of a specific object type in a given workspace.

popupService

Provides a service used to open pop-up windows.

previewSecurity

Provides a collection of methods for utilizing Preview Security mode.

promiseFactory

Provides a factory containing methods for returning promises.

relativityFormsPopup

Includes methods for creating pop-up windows through the Relativity Forms API.

relativityHttpClient

Provides methods for making requests to Relativity REST services hosted by a Relativity instance.

reviewQueueBrowser

Provides methods for programmatically navigating through the review queue.

user

Provides properties and methods related to a user.

utilities

Includes various utility functions.

validation

Represents an object used to aid form validation process.

## actionBar

Provides methods for creating and updating the contents of an action bar.

### Properties

Property

Type

Description

containersPromise

Promise<{ rootElement: HTMLElement,

leftSlotElement: HTMLElement,

centerSlotElement: HTMLElement, rightSlotElement: HTMLElement }>

An object that contains references to the

rwc-action-bar element and the left, center, or right slots on the action bar.

isVisible

Boolean

Determines whether the action bar container is visible. The value of this property can be updated in the event handlers.

### Methods

See the following subsections for information about these methods:

- createDefaultActionBar()

- destroy()

- generate.button(props: Object)

- generate.dropdown(props: Object)

- generate.massEditTitle()

- generateDefault.actionButtons()

- generateDefault.actionButtonsForAddPopup(popupControlApi: Object; objectTypeName: String)

- generateDefault.actionButtonsForPopup(popupControlApi: Object)

- generateDefault.layoutDropdown()

- generateDefault.objectPager()

#### createDefaultActionBar()

Creates a default action bar provided by the application, including these components:

- A default layout drop-down element in the left slot.

- Default action buttons in the center slot.

- A default object pager in the right slot.

##### Parameters

None

##### Return type

Promise

##### Example

The following code sample adds a single button to the center slot of the action bar:

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
eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

      convenienceApi.actionBar.createDefaultActionBar().then(function() {

          return convenienceApi.actionBar.containersPromise;

      }).then(function(containers) {

          const button = convenienceApi.actionBar.generate.button({

              innerText:  "Say Hello" ,

              onclick: function() {

                  alert( "Hello!" );

              }

          });

          containers.centerSlotElement.appendChild(button);

      });

 }
```

#### destroy()

Removes all action bar contents.

##### Parameters

None

##### Return type

Promise

##### Example

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
function populateCustomActionBar(containers) {

      const actionBar = convenienceApi.actionBar;

      const button = actionBar.generate.button({

          innerText:  "Say Hello" ,

          onclick: function() {

              alert( "Hello!" );

          }

      });

      const pager = actionBar.generateDefault.objectPager();

      containers.centerSlotElement.appendChild(button);

      containers.rightSlotElement.appendChild(pager);

 }

 function populateDefaultActionBar() {

      convenienceApi.actionBar.createDefaultActionBar();

 }

 function createActionBar() {

      const actionBar = convenienceApi.actionBar;

      const formViewModel =  this ;

      // Change to an artifact ID of an instance of the

      // given object type that exists in your workspace.

      const ARTIFACT_ID_THAT_NEEDS_CUSTOM_ACTION_BAR = 1050081;

      return actionBar.destroy().then(function() {

          return actionBar.containersPromise;

      }).then(function(containers) {

          if (formViewModel.artifactId === ARTIFACT_ID_THAT_NEEDS_CUSTOM_ACTION_BAR) {

              populateCustomActionBar(containers);

          }  else {

              populateDefaultActionBar();

          }

      });

 }

 const eventHandlers = {};

 eventHandlers[eventNames.CREATE_ACTION_BAR] = createActionBar;

 eventHandlers[eventNames.UPDATE_ACTION_BAR] = createActionBar;
```

The following code sample destroys the action bar when a specific artifact ID is encountered during the object switching process:

#### generate.button(props: Object)

Creates a button styled to fit inside an action bar.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the HTML button element accepts. For more information, see <button>: The Button element on the MDN web docs site.

##### Return type

HTMLElement - For more information, see HTMLElement on the MDN web docs site.

##### Example

The following code sample adds a single button to the center slot of the action bar:

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
eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

      const actionBar = convenienceApi.actionBar;

      const button = actionBar.generate.button({

          innerText:  "Test button" ,

          onclick: function(e) { console.log( "Button clicked!" ); }

      });

      actionBar.containersPromise.then(function(containers) {

          containers.centerSlotElement.appendChild(button);

      });

 };
```

#### generate.dropdown(props: Object)

Creates a drop-down element that fits inside the action bar.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the rwc-drop-down-input-field element accepts.

##### Return type

HTMLElement - For more information, see HTMLElement on the MDN web docs site.

##### Example

The following code sample adds a drop-down element with two choices in the right slot of the action bar:

Copy

```text
eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

    const actionBar = convenienceApi.actionBar;

    const choices = [{

        label: "Choice 1",

        value: "1"

    }, {

        label: "Choice 2",

        value: "2"

    }];

    const selectedValue = choices[0].value;

    const dropdown = actionBar.generate.dropdown({

        id: "ChoiceID",

        label: "Choices",

        removeNoValueChoice: true

    });

    dropdown.setChoices(choices);

    dropdown.value = selectedValue;

    dropdown.onchange = function(e) {

        console.log(e.target.value + " was selected!");

    };

    actionBar.containersPromise.then(function(containers) {

        containers.rightSlotElement.appendChild(dropdown);

    });

};
```

#### generate.massEditTitle()

Generate mass edit title element

##### Parameters

Parameter

Description

FormViewModel

formViewModel view-model of the form

##### Return type

HTMLElement - generated mass edit title element. For more information, see HTMLElement on the MDN web docs site.

#### generateDefault.actionButtons()

Creates a list that contains default action buttons populated by the application.

##### Parameters

None

##### Return type

Array<HTMLElement> - For more information, see HTMLElement on the MDN web docs site.

##### Example

The following code sample adds default buttons to the right slot of the action bar:

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
eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

      const actionBar = convenienceApi.actionBar;

      const buttons = actionBar.generateDefault.actionButtons();

      actionBar.containersPromise.then(function(containers) {

          // optional, adds spacing between buttons

          containers.rootElement.className =  "rwa-button-group" ;

          buttons.forEach(function(button) {

              containers.rightSlotElement.appendChild(button);

          });

      });

 };

```

#### generateDefault.actionButtonsForAddPopup(popupControlApi: Object; objectTypeName: String)

Creates a list of default action buttons for the Add RDO pop-up window. This method is for use with the relativityFormsPopup API. For more information, see relativityFormsPopup .

##### Parameters

Parameter

Description

popupControlApi: Object

Returned by any relativityFormsPopup.open call. For more information, see popupControlApi object .

objectTypeName: String

Specifies name of the RDO object type.

##### Return type

Array<HTMLElement> - For more information, see HTMLElement on the MDN web docs site.

##### Example

The following code sample adds a list of action buttons to a pop-up window:

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
eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

      const actionBar = convenienceApi.actionBar;

      const formSettings = convenienceApi.formSettings;

      const buttons = actionBar.generateDefault.actionButtonsForAddPopup(

          popupControlApi,

          formSettings.ObjectTypeName);

      actionBar.containersPromise.then(function(containers) {

          containers.rootElement.className =  "rwa-button-group" ;

          buttons.forEach(function(button) {

              containers.centerSlotElement.appendChild(button);

          });

      });

 };
```

#### generateDefault.actionButtonsForPopup(popupControlApi: Object)

Generate a default layout dropdown element. This method is for use with the relativityFormsPopup API. For more information, see relativityFormsPopup .

##### Parameters

Parameter

Description

popupControlApi: Object

Returned by any relativityFormsPopup.open call. For more information, see popupControlApi object .

##### Return type

HTMLElement - For more information, see HTMLElement on the MDN web docs site.

#### generateDefault.layoutDropdown()

Obtains a default layout drop-down element populated by the application.

##### Parameters

None

##### Return type

HTMLElement - For more information, see HTMLElement on the MDN web docs site.

##### Example

The following code sample adds a default layout drop-down element to the right slot of the action bar:

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
eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

      const actionBar = convenienceApi.actionBar;

      const layoutDropdown = actionBar.generateDefault.layoutDropdown();

      actionBar.containersPromise.then(function(containers) {

          containers.rightSlotElement.appendChild(layoutDropdown);

      });

 };
```

#### generateDefault.objectPager()

Obtains a default object pager. See reviewQueueBrowser .

##### Parameters

None

##### Return type

HTMLElement - For more information, see HTMLElement on the MDN web docs site.

##### Example

For sample code, see generateDefault.layoutDropdown() .

## additionalData

Provides a method for retrieving additional data.

### Methods

#### getDefaultFactoriesForAdditionalData()

Created specifically for use in a replaceObtainAdditionalData event handler. Creates an array of objects containing the default promise factories for obtaining additional data for fields. If the return value of this method is returned inside replaceObtainAdditionalData, the default behavior will be maintained as if the event handler had not been defined at all. This is useful as you can use it to get the default factories for all fields, then override the behavior for just one field instead of having to replace the process of obtaining additional data for either all fields or just one field.

##### Parameters

Parameter Type Description

fieldsRequiringAdditionalData Array<Field> An array of Fields requiring additional data.

workspaceId Number The integer identifier of the workspace where the object type displayed in this form exists.

##### Return type

Array<{field: Field, createAdditionalDataPromise: Function: Promise<AdditionalData>}>

See replaceObtainAdditionalData for more detailed information.

##### Example

This is normally used in the replaceObtainAdditionalData event handler. See replaceObtainAdditionalData for more detailed information.

## applicationPaths

Represents an object used to supply application paths specific to Relativity.

Property

Type

Description

relativity

String

Contains the base path to Relativity application: "/Relativity".

kepler

String

Contains the base path for the Kepler services: "/Relativity.Rest/API".

relativityRest

String

Contains the path to Relativity REST services:"/Relativity.Rest".

## console

Creates a console on the page. This API exposes the console parent element root container and provides methods that can be used to generate various console elements.

### Properties

Property

Type

Description

containersPromise

Promise<{ rootElement: HTMLElement }>

Contains a reference to the console root element container.

isVisible

Boolean

Determines whether the console container is visible. The value of this property can be updated in the event handlers.

### Methods

See the following subsections for information about these methods:

- destroy()

- generate.button(props: Object)

- generate.buttonStyledAsLink(props: Object)

- generate.section(props: Object, children: Array<HTMLElement>)

- generate.sectionTitle(props: Object)

- generate.title(props: Object)

#### destroy()

Removes all console contents.

##### Parameters

None

##### Return type

Promise

##### Example

The following code sample removes all console contents and adds a single title when a specific artifact layout ID is encountered after a layout switch:

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
function generateDefaultConsoleContent() {

      const consoleApi = convenienceApi.console;

      const button = consoleApi.generate.button({

          innerText:  "Test button" ,

          onclick: function(e) { console.log( "Button clicked!" ); }

      });

      const section = consoleApi.generate.section({}, [

          button

      ]);

      return section;

 }

 function generateCustomConsoleContent() {

      const consoleApi = convenienceApi.console;

      const title = consoleApi.generate.title({

          innerText:  "Title"

      });

      return title;

 }

 function createConsole() {

      const consoleApi = convenienceApi.console;

      // Change to a layout ID for the given object type that exists in your workspace.

      const LAYOUT_ID_THAT_NEEDS_CUSTOM_CONSOLE = 1043519;

      let consoleContent;

      // Determine the content that should be added to the console

      // based on the current layout ID of the form.

      if ( this .layoutId === LAYOUT_ID_THAT_NEEDS_CUSTOM_CONSOLE) {

          consoleContent = generateCustomConsoleContent();

      }  else {

          consoleContent = generateDefaultConsoleContent();

      }

      return consoleApi.destroy().then(function() {

          return consoleApi.containersPromise;

      }).then(function(containers) {

          containers.rootElement.appendChild(consoleContent);

      });

 }

 const eventHandlers = {};

 eventHandlers[eventNames.CREATE_CONSOLE] = createConsole;

 eventHandlers[eventNames.UPDATE_CONSOLE] = createConsole;
```

#### generate.button(props: Object)

Creates a button styled to fit inside the console.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the HTML button element accepts. For more information, see <button>: The Button element on the MDN web docs site.

##### Return type

HTMLElement - For more information, see HTMLElement on the MDN web docs site.

##### Example

We require you to add a tooltip to your button in case your button text is truncated. See the following code sample.

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
const consoleApi = convenienceApi.console;

const button = consoleApi.generate.button({

    innerText:  "Do Something",

    title: "Do Something", // Tooltip to show if full button text cannot be displayed

    onclick: function(e) { console.log( "Button clicked!" ); }

});

consoleApi.containersPromise.then(function(containers) {

    containers.rootElement.appendChild(button);

});
```

#### generate.buttonStyledAsLink(props: Object)

Creates a button styled as a link that fits inside the console.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the HTML button element accepts. For more information, see <button>: The Button element on the MDN web docs site.

##### Return type

HTMLElement

##### Example

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
const consoleApi = convenienceApi.console;

 const buttonAsLink = consoleApi.generate.buttonStyledAsLink({

      innerText:  "Test button" ,

      onclick: function(e) { console.log( "Button clicked!" ); }

 });

 consoleApi.containersPromise.then(function(containers) {

      containers.rootElement.appendChild(buttonAsLink);

 });
```

#### generate.section(props: Object, children: Array<HTMLElement>)

Creates a console section. Use sections to break large consoles into logical groups.

A section or section title isn't always necessary, especially if your console has only one button. See the following examples:

- Do streamline the interface.

- Don't add unnecessary sections.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the HTML div element accepts.

children: Array<HTMLElement>

Attached as children of the section based on the order in which they are supplied. For more information, see <div>: The Content Division element on the MDN web docs site.

##### Return type

HTMLElement

##### Example

The following code sample creates a section that contains a button:

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
const consoleApi = convenienceApi.console;

 const button = consoleApi.generate.button({

      innerText:  "Test button" ,

      onclick: function(e) { console.log( "Button clicked!" ); }

 });

 const section = consoleApi.generate.section({}, [

      button

 ]);

 consoleApi.containersPromise.then(function(containers) {

      containers.rootElement.appendChild(section);

 });
```

#### generate.sectionTitle(props: Object)

Creates an HTML h3 section title that fits inside the console.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the HTML h3 element accepts. For more information, see <h1>–<h6>: The HTML Section Heading elements on the MDN web docs site.

##### Return type

HTMLElement

##### Example

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
const consoleApi = convenienceApi.console;

 const sectionTitle = consoleApi.generate.sectionTitle({

      innerText:  "Test section title"

 });

 const section = consoleApi.generate.section({}, [

      sectionTitle

 ]);

 consoleApi.containersPromise.then(function(containers) {

      containers.rootElement.appendChild(section);

 });
```

#### generate.title(props: Object)

Creates a HTML h2 section title that fits inside the console.

Use the generate.sectionTitle() function unless multiple levels are needed in a console. See the following examples:

- Do use section titles when there's only one level of hierarchy.

- Don't use regular titles when there's only one level of hierarchy.

A top-level console title is rarely necessary. Don't use a console title if it doesn't provide useful information to the user. For example, a console title that restates the name of an RDO is redundant. See the following examples:

- Do use the minimum number of titles.

- Don't add unneeded titles.

##### Parameters

Parameter

Description

props: Object

Translates on a one-to-one basis into the entities that the HTML h2 element accepts. For more information, see <h1>–<h6>: The HTML Section Heading elements on the MDN web docs site.

##### Return type

HTMLElement

##### Example

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
const consoleApi = convenienceApi.console;

 const title = consoleApi.generate.title({

      innerText:  "Test section title"

 });

 consoleApi.containersPromise.then(function(containers) {

      containers.rootElement.appendChild(title);

 });
```

## constants

Provides access to certain constants used globally in an application.

### Properties

Property

Type

Description

FORM_VIEW_MODEL_TYPE

Object

Copy

```text
1
2
3
4
5
FORM_VIEW_MODEL_TYPE = {

    VIEW: 0,

    ADD: 1,

    EDIT: 2

}
```

VIEW_MODEL_NAME

Object

Copy

```text
1
2
3
4
5
VIEW_MODEL_NAME = {

    ADD: "add",

    VIEW: "view",

    EDIT: "edit"

};
```

ACTIONS

Object

Copy

```text
1
2
3
4
ACTIONS = {

    SAVE: "save",

    DELETE: "delete"

};
```

ACTION_TYPES

Object

Copy

```text
1
2
3
4
5
6
ACTION_TYPES = {

    NEW: "New",

    DELETE: "Delete",

    LINK: "Link",

    UNLINK: "Unlink"

};
```

MODAL_THEMES

Object

Copy

```text
1
2
3
4
MODAL_THEMES = {

    CONFIRMATION: "confirmation",

    NO_CONTAINER: "no-container"

};
```

ARTIFACT_TYPE

Object

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

ARTIFACT_TYPE = {

    BATCH_SET: 24,

    CLIENT: 5,

    DOCUMENT: 10,

    FIELD: 14,

    TAB: 23,

    USER: 2

};
```

## dateTime

Represents a date-time value formatter. This API is part of the data-management modules within the Relativity web components library, which is made directly available via the convenienceApi.

### Methods

#### getFormatter(options: <Object>)

Returns a formatter object that can be used to format date-time strings to a given locale

##### Parameters

Parameter

Type

Description

options

Object

Provides DateTime formatting options and configuration. Contains the following:

- errorText - a <string> that provides parsed error text.

- includeSeconds - a <boolean> that indicates whether the formatter includes seconds in the output string.

- includeTime - a <boolean> that indicates whether the formatter includes time in the output string.

- isUTC - a<boolean> that indicates whether the date-time string given to the formatter is a UTC time. When true, the output will be converted to the local timezone of the user's browser.

- locale - a <string> that indicates the BCP 47 language tag, such as "en-US", or "de-DE", to which the output string will be localized.

##### Return type

Object

##### Example

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
var unformattedDateTimeString = "2009-04-27T18:44:50.217";

var myDateTimeFormatter = convenienceApi.dateTime.getFormatter({

      isUTC:  true ,

      includeSeconds:  true ,

      includeTime:  true

 });

var formattedDateTimeString = myDateTime.format(unformattedDateTimeString);

console.log(formattedDateTimeString); // "4/27/2009, 1:44:50 PM CDT"
```

## fieldHelper

Includes methods for quickly accessing and modifying fields. The fieldHelper API will not work properly until the hydrateLayoutComplete stage or later.

### Parameters

The identifier parameter is used to find a field. Each fieldHelper API method takes an identifier parameter. The following table lists supported identifier types:

Parameter

Description

Object

If the identifier is an object, it must include one key-value pair, representing the field property to match. Supported properties include:

- guid

- displayName

- fieldId

The following are valid object shapes:

{ guid: String }{ displayName: String }{ fieldId: Number }

If the object does match one of the valid shapes, a TypeError is thrown. For example, use the following object to retrieve the value of a field with a displayName of Artifact ID :

Copy

```text
1
convenienceApi.fieldHelper.getValue({ displayName: "Artifact ID" })
```

String | Number

If the identifier is a string or number, perform the following steps:

- If a field with a fieldId the matches the identifier, use this field.

- If no field is found, look for a field with a guid that matches the identifier. Use this field.

- If no field is found, look for a field with a displayName that matches the identifier and use this field.

For example, use the string Artifact ID to retrieve the value of a field with a displayName of Artifact ID :

Copy

```text
1
convenienceApi.fieldHelper.getValue("Artifact ID")
```

### Methods

See the following subsections for information about these methods:

- getValue(identifier: String|Number|Object)

- setValue(identifier: String|Number|Object, valueToSet: Any)

- getHtmlElement(identifier: String|Number|Object)

- setIsEditMode(identifier: String|Number|Object, isEditMode: Boolean)

- setIsDisabled(identifier: String|Number|Object, isDisabled: Boolean)

- setIsLoading(identifier: String|Number|Object, isLoading: Boolean)

- addAdditionalData(identifier: String|Number|Object, additionalData: List<Object>)

- setIsHidden(identifier: String|Number|Object, isHidden: Boolean)

- setIsRequired(identifier: String|Number|Object, isRequired: Boolean)

- setAriaDescribedBy(fieldId, ariaDescribedby)

- setContextualHelpText(identifier: String|Number|Object, contextualHelpText: String)

#### getValue(identifier: String|Number|Object)

Retrieves the value of a given field from the view-model. It returns a promise that resolves to the value. The promise resolves to null if the action does not succeed. Choice fields, Object fields and User fields will have a value of a Relativity Object.

##### Parameters

Parameter

Description

identifier: String|Number

The identifier to use to look up the field.

##### Return type

Promise<FieldValue> - If the field exists, the promise resolves to the value of the field. For more information about possible values of fields, see the Field Value section of the Additional Forms API Object page.

Promise<null> - If field does not exist, the promise resolves to null .

##### Example

Copy

```text
1
2
3
convenienceApi.fieldHelper.getValue(identifier).then(function (value) {

      console.log( "The field has a value of " + value);

});
```

#### setValue(identifier: String|Number|Object, valueToSet: Any)

Sets the value of a given field. It returns a promise that resolves to the value and resolves to null if the set operation does not succeed.

Choice fields and Object fields will have to be set to a value of a Relativity Object.

##### Parameters

Parameter

Description

identifier: String|Number

The identifier to use to look up the field.

valueToSet: FieldValue

The value that should be assigned to the field. See the Field Value section of the Additional Forms API Object page for more information.

##### Return type

Promise<Object|Primitive Type> - If the set operation succeeds , the promise resolves to the value that was set.

Promise<null> - If the set operation fails , the promise resolves to null .

##### Example

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
var relativityObject1 = {

    ArtifactID: 10010,

    Name: "Object1"

};

var relativityObject2 = {

    ArtifactID: 10011,

    Name: "Object2"

};

convenienceApi.fieldHelper.setValue( singleChoiceOrObjectFieldId, relativityObject1||null );

convenienceApi.fieldHelper.setValue( TrueOrFalseFieldId, true);

convenienceApi.fieldHelper.setValue( textFieldId, "string" );

// To clear out the value of a mutli choice.object field, set the value to an empty array

convenienceApi.fieldHelper.setValue( multiChoiceOrMultiObjectFieldId, [relativityObject1, relativityObject2] );

convenienceApi.fieldHelper.setValue( numberFieldId, 1000 );

convenienceApi.fieldHelper.setValue( dateField, "1999-02-01T10:05:00" );
```

#### getHtmlElement(identifier: String|Number|Object)

Retrieves the HTML element associated with a field. It returns a promise that resolves to the HTML element of the field and resolves to null if the get operation does not succeed.

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier to use to look up the field.

##### Return type

Promise<HTMLelement|null>

##### Example

Copy

```text
1
2
3
4
5
convenienceApi.fieldHelper.getHtmlElement(identifier).then((element) => {

      if (!!element) {

          element.style.color( "blue" );

      }

 });
```

#### setIsEditMode(identifier: String|Number |Object , isEditMode: Boolean)

Enables or disables edit mode for a field. This method returns a Promise that resolves to the new edit mode value for the field after the operation completes. It resolves to null if the operation doesn't succeed.

If you call the setIsEditMode() mode function with isEditMode = true, and the field wasn’t in edit mode, this function automatically loads additional data for the field. This process only occurs when the field requires additional data, but the data hasn’t loaded yet. The returned Promise won’t resolve until any the additional data has finished loading and been applied to the field. If you defined custom additional data loading behavior via the REPLACE_OBTAIN_ADDITIONAL_DATA event handler, custom loading behavior is used. However, setIsEditMode() function won’t trigger a load pipeline, so it doesn’t trigger additional REPLACE_OBTAIN_ADDITIONAL_DATA and POST_OBTAIN_ADDITIONAL_DATA events.

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier to use to look up the field.

isEditMode: Boolean

Indicates whether to enable edit mode for a field based on these values:

- true - the field is displayed in edit mode.

- false - the field is displayed in view mode. The user won't be able to modify its value through the UI.

##### Return type

Promise<Boolean|null>

##### Example

Copy

```text
1
 convenienceApi.fieldHelper.setIsEditMode(identifier,  false );
```

#### setIsDisabled(identifier: String|Number |Object , isDisabled: Boolean)

Sets the isDisabled property on a given field to a specified value. It returns a promise that resolves to the disabled property of the field, and resolves to null if the set operation does not succeed.

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier to use to look up the field.

isDisabled: Boolean

Indicates whether the field is disabled.

##### Return type

Promise<Boolean|null>

##### Example

Copy

```text
1
  convenienceApi.fieldHelper.setIsDisabled(identifier,  true );
```

#### setIsLoading(identifier: String|Number |Object , isLoading: Boolean)

Sets the isLoading property on a given field to a specified value. It returns a promise that resolves to the value of the isLoading state, and resolves to null if the set operation does not succeed.

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier to use to look up the field.

isLoading: Boolean

Indicates whether the field is loading.

##### Return type

Promise<Boolean|null>

##### Example

Copy

```text
1
   convenienceApi.fieldHelper.setIsLoading(identifier,  true );
```

#### addAdditionalData(identifier: String|Number |Object , additionalData: List<Object>|Object)

Sets the additional data property on a given field to a specified value. It also sets the loading state of the field to false after applying the additional data. Typical usage of this is to set custom options for a set of choices or a dropdown (not pickers); note that this will replace any choices that exist in the targeted field. This method returns a promise that resolves to undefined on completion of the addition of data; it will resolve to null if set did not succeed.

This applies choice-like fields, including the following configurations:

- User field displayed as a dropdown

-

Single choice field displayed as a radio button list or dropdown (i.e. not as a picker)

-

Multiple choice field displayed as a checkbox list (i.e. not as a picker)

-

Single object field displayed as a dropdown (i.e. not as a picker)

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier to use to look up the field.

additionalData: List<Object>|Object

Represents a list of objects containing additional data for the field.

The function expects a List<Object> for User fields and Object for other fields.

When the input is List<Object> , it is an array of dropdown entry objects with the following properties.

-

label: String - label of the choice

-

value: Number - value of the choice (typically an ID representing something)

When the input is Object , it must have the following properties

-

options: List<Object> - array of dropdown entry objects (see above for shape details)

-

limitForUIExceeded: Boolean - indicates whether the limit to display options on the UI has been exceeded; if set to true, the control will change to a picker

##### Return type

Promise<undefined|null>

##### Example

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
// for non-User fields

var data = [

    { label: "Chicago" , value: 1 },

    { label: "Boston" , value: 2 },

    { label: "New York" , value: 3 }

];

convenienceApi.fieldHelper.addAdditionalData(nonUserIdentifier, { options: data, limitForUIExceeded: false });

// for User fields

// values are artifact IDs

var userData = [

    { label: "John Doe", value: 1234567 },

    { label: "Jane Smith", value: 8901234 }

];

convenienceApi.fieldHelper.addAdditionalData(userIdentifier, userData);
```

#### setIsHidden(identifier:String|Number|Object, isHidden: Boolean)

Sets the display property on a given field to a specified value. Hidden fields are also flagged so that they are not used in object updates. This method returns a promise that resolves to the value of the hidden property of the field, and resolves to null if the set operation does not succeed.

##### Parameters

Parameter

Description

identifier:String|Number|Object

The identifier to use to look up the field.

isHidden: Boolean

Indicates whether the field is hidden.

##### Return type

Promise<Boolean|null>

##### Example

Copy

```text
1
   convenienceApi.fieldHelper.setIsHidden(identifier,  false );
```

#### setIsRequired(identifier: String|Number|Object, isRequired: Boolean)

Sets the required property on a given field to a specified value. The method returns a promise that resolves to the value of the required property of the field, and resolves to null if the set operation does not succeed.

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier to use to look up the field.

isRequired: Boolean

Indicates whether the field is required.

##### Return type

Promise<Boolean|null>

##### Example

Copy

```text
1
convenienceApi.fieldHelper.setIsRequired(identifier, true );
```

#### setAriaDescribedBy(fieldId, ariaDescribedby)

Sets the aria-describedby attribute to a given field in a layout. This method returns a promise that resolves to the value of aria-describedby attribute. It resolves to null, if set operation fails.

##### Parameters

Parameter

Description

fieldId: String|Number

Represents an ID of a field with the aria-describedby property that you want to set.

ariaDescribedBy: String

Represents a new value of the aria-describedby property.

##### Return type

Promise<String|null>

##### Example

Copy

```text
1
2
3
4
5
6
const objectTypeFieldId = "ObjectType";

const descriptionTextId = "DescriptionStaticText";

// Setting a description text.

convenienceApi.staticTextHelper.setValue(descriptionTextId, "<span id=\"object-type-description\">Please select Object Type value to see other fields.</span>");

// A description text is used to describe the ObjectType field.

convenienceApi.fieldHelper.setAriaDescribedBy(objectTypeFieldId, "object-type-description");
```

#### setContextualHelpText(identifier: String|Number|Object, contextualHelpText: String)

Sets the contextual help text for a field. This text displays when a user clicks the contextual help icon next to the field. While contextual help is a useful tool for providing additional information about the UI, we encourage you to use it in moderation for a better user experience.

##### Parameters

Parameter

Description

identifier: String|Number|Object

The identifier used to look up a field. For more information, see the identifier description in Parameters .

contextualHelpText: String

The contextual help text to set. The default value is an empty string (""). If this parameter is set to an empty string, no contextual help is displayed, and the contextual help icon is hidden.

##### Return type

- Promise<undefined> - If the set operation succeeds, the promise resolves to undefined.

- Promise<null> - If the set operation fails, the promise resolves to null.

##### Example

The following screenshot illustrates how the contextual help displays in the UI:

This code sample illustrates how to display the contextual help in the previous screen:

Copy

```text
1
2
3
4
5
// Add contextual help to a field

convenienceApi.fieldHelper.setContextualHelpText(

    "Field with help",

    "Some concise text that quickly explains how to use this field"

);
```

## formSettings

Represents an object that contains general settings related to the user viewing a form and the artifact displayed in it.

### Properties

Property

Type

Description

LoggedInUserID

Number

Represents the unique identifier for the currently active user.

ChoiceLimitForUI

Number

Indicates the maximum number of choices or single objects, which can appear in a checkbox, drop-down, or radio button list before the UI is switched to a pop-up picker.

IsLoggedInUserSystemAdmin

Boolean

Indicates whether the currently active user is a system administrator.

IsSystemType

Boolean

Indicates whether the current artifact type is a system type.

IsDynamicType

Boolean

Indicates whether the current artifact type is a dynamic type, such as a RDO.

DownloadHandlerApplicationPath

String

Contains the default URL referencing the code responsible for making downloaded files available to users.

TimeSettings

Object

Contains time settings, including the following:

- IsDST - a <Boolean> that indicates whether the current locale uses Daylight Savings Time (DST).

- ServerTimeOffsetHours - a <number> indicating the difference in hours between the current locale and the server.

- ServerTimeOffsetMinutes - a <number> indicating the difference in minutes between the current locale and the server.

## ItemListDataProviderFactory

### Methods

See the following subsections for information about these methods:

- create(string providerType, Object options);

#### create(string providerType, Object options)

##### Parameters

Parameter

Description

providerType: String

Type of the data provider to create. Accepts the following strings "choice", "object", and "user".

options: Object

Data provider-specific options to be passed to the provider.

options properties for "choice":

Properties

Type

Description

fieldName

String

The name of the Relativity Field to get choices for. This is used by the dataProvider when querying choices. For example, if you want this dataProvider to get choices for a field named 'field 1' that is on the object type: 'custom object type 1', set this to 'field 1'.

fieldArtifactId

Number

The Artifact ID of the field to get data for.

objectTypeName

String

The name of the object type to get choices for. This is used by the dataProvider when querying choices. For example, if you want this dataProvider to get choices for a field named 'field 1' that is on the object type: 'custom object type 1', set this to 'custom object type 1'.

workspaceId

Number

The ID of the Workspace the field is located in.

options properties for "object":

Properties

Type

Description

workspaceId

Number

The Id of the workspace.

fieldArtifactId

Number

Field artifact Id of the object field.

filterInteractiveColumns

Boolean

If true the "edit" column will be hidden.

objectTypeName

String

Object type name of the object type of the field.

fieldName

String

Field name associated with the object field that is showing the list

textIdentifierColumnName

String

The name of the column that is used as the identifier of the row. "Name" is usually the column that should be used.

viewArtifactId

Number

The id of the view that will be used to generate the list.

queryCondition

String

A default relativity query condition that will be used for the relativity object query for getting the items in the list.

See Query Condition.

options properties for "user":

Properties

Type

Description

workspaceId

Number

The Id of the workspace.

fieldArtifactId

Number

Field artifact Id of the user field.

loggedInUserId

Number

The id of the user that is currently logged in.

##### Return type

ItemListDataProvider

##### Example

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
// Use ItemListDataProviderFactory to get an ItemListDataProvider instance that can be customized

const option = {

     objectTypeId: artifactTypeId,

     workspaceId: workspaceID,

     textIdentifierColumnName: "ArtifactID",

     viewArtifactId: viewToDisplayID

};

const customItemListDataProvider = convenienceApi.itemListDataProviderFactory.create("object", option);

// Override the query method to define a custom data source for the list

customItemListDataProvider.query = function customQuery(request){

     const customData = [

          { "col1": "row1 col1 value", "col2": "row1 col2 value" },

          { "col2": "row2 col1 value", "col2": "row2 col2 value" }

     ];

     return {

          Results: customData,

          TotalCount: customData.length;

          CurrentStartIndex: 0

     };

};

// Define the modal for a list picker that references our custom item list data provider

const listPickerModalModel = {

     label: "My custom picker modal",

     itemListDataProvider: customItemListDataProvider

};

// Open the modal

convenienceApi.modalService.open(listPickerModalModel);
```

## itemListHelper

Includes methods for quickly accessing and modifying item lists. Like fieldHelper API, the itemListHelper API doesn't function properly until the hydrateLayoutComplete stage or later.

### Methods

#### setCommandColumnType(itemListIdentifier: String | Number, itemListCommandColumnType: ITEM_LIST_COMMAND_COLUMN_TYPE)

Sets the command column type for an item list. The command column of an item list lets users select items so they can perform operations on them. It usually contains checkboxes or radio buttons, but it may be hidden. You can use the setCommandColumnType method to override the default behavior of the command column.

##### Parameters

Parameter Description

itemListIdentifier: String | Number The identifier used to look up the item list.

- If itemListIdentifier is a String, it should match the name of the item list. It matches the item list title displayed on the layout.

- If itemListIdentifier is a Number, it should match the identifier of the view associated with the item list. Usually, the identifier of a view is its ConnectorFieldArtifactID. However, if the view doesn't have a ConnectorFieldArtifactID, the identifier is the ArtifactID of the view. You can find both of these IDs by looking at the layout data , which can be obtained via the transformLayout event handler.

commandColumnType: ITEM_LIST_COMMAND_COLUMN_TYPE Indicates the ITEM_LIST_COMMAND_COLUMN_TYPE to use. See convenienceApi.constants.ITEM_LIST_COMMAND_COLUMN_TYPE .

##### Return type

- Promise<undefined> - when the operation completes successfully.

- Promise<null> - when the operation fails.

##### Example

The following example illustrates how you ensure a user selects only one object at a time from the item list called Associated Documents .

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
(function(eventNames, convenienceApi) {

    var ASSOCIATED_DOCUMENTS_LIST_NAME = "Associated Documents";

    eventHandlers[eventNames.HYDRATE_LAYOUT_COMPLETE] = function() {

        var itemListHelper = convenienceApi.itemListHelper;

        var ITEM_LIST_COMMAND_COLUMN_TYPE = convenienceApi.constants.ITEM_LIST_COMMAND_COLUMN_TYPE;

        itemListHelper.setCommandColumnType(ASSOCIATED_DOCUMENTS_LIST_NAME, ITEM_LIST_COMMAND_COLUMN_TYPE.SINGLE_SELECTION);

    };

    return eventHandlers;

})(eventNames, convenienceApi);
```

### Constants

Property Type Description

ITEM_LIST_COMMAND_COLUMN_TYPE Object Copy

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
ITEM_LIST_COMMAND_COLUMN_TYPE = {

    /**

     * Allow the user to select up to one item

     */

    SINGLE_SELECTION: "single-selection",

    /**

     * Allow the user to select any number of items

     */

    MULTI_SELECTION: "multi-selection",

    /**

     * Do not allow the user to select items

     */

    NONE: null,

    /**

     * Automatically hide the command column

     * if there are no action buttons above the

     * item list. Otherwise, show the command column

     * in MULTI_SELECTION mode

     */

    AUTO: "auto"

};
```

The item list can have the following settings:

- Single selection command column

- Multi selection command column

- Command column set to NONE

## i18n

Represents an i18n object that contains methods used for application internationalization.

### Methods

See the following subsections for information about these methods:

- tr(key: String)

- getLocale()

- nf(options: Object|null, locale: String)

- df(options: Object|null, locale: String)

- addResources(locale: String, items: Object)

#### tr(key: String)

Looks up a key and returns the localized string for the current locale.

##### Parameters

Parameter

Description

key: String

Indicates the localized string to return.

##### Return type

String

##### Example

Copy

```text
1
2
3
var localizedButtonName = convenienceApi.i18n.tr( "action_bar.edit" );

 console.log(localizedButtonName);  // "Edit" if locale is set to "en-US"

 // "Editar" if locale is set to "es-ES"
```

#### getLocale()

Returns a string for the current browser's language code.

##### Parameters

None

##### Return type

String

##### Example

The following code sample illustrates how to retrieve the browser's language code:

Copy

```text
1
2
var currentLocale = convenienceApi.i18n.getLocale();

 console.log(currentLocale);  // "en"
```

To retrieve the browser's locale, use window.navigator.language instead.

#### nf(options: Object|null, locale: String)

Returns an Intl.NumberFormat object for the given locale, with the specified options applied. The returned object contains a format() method used for number localization. For more information, see Intl.NumberFormat on the MDN web docs site.

##### Parameters

Parameter

Description

options: Object|null

The "options" passed to a NumberFormat constructor, as described in MDN, or null. For a full list of options for number formatting, refer to the "options" description on MDN .

locale: String

Indicates a country, origin, or language setting.

##### Return type

Intl.NumberFormat

##### Example

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
// Get an object that formats to the current locale.

 var numberOptions = {

      style:  "currency" ,

      currency:  "EUR"

 };

 var numberFormatter = convenienceApi.i18n.nf(numberOptions, convenienceApi.i18n.getLocale());

 // Format

 var localizedNumber = numberFormatter.format(123456.123);

 console.log(localizedNumber);  // "€123,456.123" if locale is set to "en-US".

 // "123.456,123 €" if locale is set to "de-DE".
```

#### df(options: Object|null, locale: String)

Returns an Intl.DateTimeFormat object for the given locale, with the specified options applied. The returned object contains a format() method used for date localization. For more information, see Intl.DateTimeFormat on the MDN web docs site.

##### Parameters

Parameter

Description

options: Object|null

The "options" passed to a DateTimeFormat constructor, as described in MDN, or null. For a full list of datetime formatting options, refer to the "options" description on MDN .

locale: String

Indicates a country, origin, or language setting.

##### Return type

Intl.DateTimeFormat

##### Example

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
// Get an object that formats to the current locale.

 var dateOptions = {

      year:  'numeric' ,

      month:  '2-digit' ,

      day:  '2-digit'

 };

 var dateFormatter = convenienceApi.i18n.df(dateOptions, convenienceApi.i18n.getLocale());

 // Format

 var localizedDate = dateFormatter.format( new Date(2017, 5, 1));

 console.log(localizedDate);  // "05/01/2017" if locale is set to "en-US".

 // "01.05.2017" if locale is set to "de-DE".
```

#### addResources(locale: String, items: Object)

Adds custom translations. When this method is used with the tr() method, it eliminates the need for manual locale resolution.

##### Parameters

Parameter

Description

locale: String

Indicates a country, origin, or language setting.

items: Object

Object which is a key-value pair dictionary, where the key is the localization key, and value is the localized string corresponding to the key, for the given locale.

##### Return type

undefined

##### Example

Copy

```text
1
2
3
4
convenienceApi.i18n.addResources( "en" , {

      "console_title" :  "Batch Set" ,

      "console_section_manageBatches.title" :  "Manage Batches"

 });
```

## layout

Modifies layouts.

Although the following methods are available in convenienceApi.Layout, we don't recommended using them. Instead, use the convenienceApi.fieldHelper.getHtmlElement() convenienceApi.fieldHelper. For more information, see fieldHelper .

- getElementByFieldId

- getElementByFieldName

### Methods

#### removeFieldFromLayout(layoutData: Object, id: String|Number)

Removes a given field from a layout. This method returns the field object that was removed, or null if the field wasn't found.

##### Parameters

Parameter

Description

layoutData: Object

An object containing layout information. For more information, see Layout representation for Relativity forms .

id: String|Number

The field id.

##### Return type

Object|null

##### Example

Copy

```text
1
2
3
4
5
6
7
var removedObject = convenienceApi.layout.removeFieldFromLayout( layoutData, "LastModifiedOn");

if(removedObject == null) {

     console.log("Object was not deleted.");

}

else {

      console.log("Object was deleted.");

}
```

## logFactory

Provides a collection of functions that can be used to create loggers.

### Methods

#### getLogger(id: String)

Returns an instance of Aurelia logger.

##### Parameters

Parameter

Description

id: String

This value gets echoed as a prefix on all logging done by the resultant logging object.

##### Return type

Logger

##### Example

Copy

```text
1
2
var logger = convenienceApi.logFactory.getLogger( "arbitrary-log-identifier" );

            logger.info( "Info-level message!" )
```

## modalService

Provides a service that can be used to open various modals in an application.

To refresh the contents of a Relativity Forms page, Relativity recommends using the refreshLayout() method on the this Binding instead of performing a hard reload (i.e. window.location.reload()).

### Methods

See the following subsections for information about these methods:

- confirm(model: Object, openModalHandler: Function)

- openProgressModal(model: Object, openModalHandler: Function)

- openCustomModal(model: Object, openModalHandler: Function)

- openAdvancedConditionModal(model: Object, openModalHandler: Function)

- openDeleteModal(model: Object, openModalHandler: Function)

- openMultiListPickerModal(model: Object, openModalHandler: Function)

- openSingleListPickerModal(model: Object, openModalHandler: Function)

#### confirm(model: Object, openModalHandler: Function)

Opens a confirmation modal. This method returns a dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

This parameter accepts the following properties:

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
{

    title: String,

    message: String,

    acceptText: String?, // defaults to 'Accept'

    cancelText: String?, // defaults to 'Cancel'

    cancelAction: Function?,

    acceptAction: Function?,

    focusEls: {

        cancel: HTMLElement?,

        accept: HTMLElement?

    },

    firstFocusableElementSelector: String?

}
```

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter

Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

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
var model = {

  title: "Confirmation Modal Example",

  acceptAction: function acceptAction() {

    console.log("Accept button was clicked");

  },

  cancelAction: function cancelAction() {

    console.log("Cancel button was clicked");

  }

};

convenienceApi.modalService.confirm(model);
```

#### openProgressModal(model: Object, openModalHandler: Function)

Opens a progress modal. This method returns a dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

This parameter accepts the following properties:

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
{

    title: String,

    errorMessage: String?

    message: String?, // A warning message

    cancelText: String?, // Defaults to 'Cancel'.

    value: Number,

    state: String? // One of the following: "failed", "indeterminate", or null.

    cancelAction: Function?,

    focusEls: {

        cancel: HTMLElement?

    },

    firstFocusableElementSelector: String?

}
```

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter

Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

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
var model = {

     title:  "Progress Modal Example",

     value: 0,

     cancelAction: function cancelAction() {

          console.log( "Cancel button was clicked" );

     }

};

var fakeAfterModalOpeningHandler = function fakeAfterModalOpeningHandler() {

     // This sets the progress value to 100 after 1 second.

     setTimeout(function () {

          model.value = 100;

     }, 1000);

};

convenienceApi.modalService.openProgressModal(model, fakeAfterModalOpeningHandler);
```

#### openCustomModal(model: Object, openModalHandler: Function)

Opens a custom modal. This method returns a dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

This parameter accepts the following properties:

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
{

    title: String,

    isLoading: Boolean, // True if loading layout should be displayed.

    errors: List<String>, // Errors list to be displayed in default error container.

    warningMode: Boolean,  // True if display errors in warning mode.

    noHeader: Boolean, // True if title container should not be displayed.

    noActions: Boolean, // True if actions container should not be displayed.

    theme: String,  // Refer to constants.MODAL_THEMES.

    contentElement: HTMLElement, // HTML element to be displayed in custom modal content.

    actions: List<Object>  // { disabled: Boolean, click: Function, text: String }

    cancelAction: Function?,

    acceptAction: Function?,

    focusEls: {

        cancel: HTMLElement?,

        accept: HTMLElement?

    },

    firstFocusableElementSelector: String?

}
```

- Notes about contentElement

- This DOM element is attached inside the modal content zone once the modal is opened.

- The element that contentElement references should not change after the modal is opened

- If the content is loaded dynamically, it is recommended to pass an empty HTML container for contentElement and modify this container later when the content is ready to be loaded

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter

Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

Other variables

At the time the openModalHandler is called, the model object passed to openCustomModal function is enriched with functions for interacting with the modal when it's opened.

- close(message: String) - closes modal with the message passed for openCustomModal promise resolution as a result. Skips acceptAction call before close.

- cancel(message: String) - closes modal as cancelled with message passed for openCustomModal promise resolution as a result.

- accept(message: String) - closes modal with the message passed for openCustomModal promise resolution as a result.

- enableActions() - enables all modal actions.

- disableActions() - disables all modal actions.

- focusElement() - focuses element in custom modal content.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

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
// Create custom modal content container.

var contentContainer = document.createElement("div");

// Create custom modal model. Initially, display it in loading state.

var model = {

     isLoading: true,

     theme: convenienceApi.constants.MODAL_THEMES.CONFIRMATION,

     contentElement: contentContainer

};

convenienceApi.modalService.openCustomModal(model).then(function (closeResult) {

     if (closeResult.wasCancelled) {

          console.log("Custom modal was cancelled");

     } else {

          console.log("Custom modal was accepted");

     }

     console.log(closeResult);

});

// This section could be an async data load for custom modal content.

setTimeout(function () {

     // Disable loading state.

     model.isLoading = false;

     // Populate DOM content.

     contentContainer.innerText = "Loaded content";

     // Define actions for the custom modal.

     model.actions = [

          {

               text: "Ok" ,

               click: function click() {

                    model.accept("Accept payload");

               }

          },

          {

               text: "Disabled action" ,

               disabled: true

          },

          {

               text: "Cancel" ,

               click: function click() {

                    model.cancel("Cancel payload");

               }

          }

     ];

}, 1000);
```

#### openAdvancedConditionModal(model: Object, openModalHandler: Function)

Opens a modal for entering advanced filtering conditions. This method returns dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

Accepts various properties, such as title and conditions.

Copy

```text
1
2
3
4
5
6
7
{

    //Used to format the full title of the modal, such as "Filter: [title goes here]".

    title: String,

    conditions: Array<Condition>,

    //Combined vertical spacing above the top and below the bottom of the modal in pixels.

    verticalMargin: Number // Defaults to 0.

}
```

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter

Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

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
var modalData = {

     title: "Demo advanced condition",

     conditions: []

};

convenienceApi.modalService.openAdvancedConditionModal(modalData).then(function (action) {

     if (!action.wasCancelled) {

          console.log("Advanced condition entered");

          // Action.output holds an array of Condition objects.

     } else {

          console.log("Advanced condition entering cancelled");

     }

});
```

#### openDeleteModal(model: Object, openModalHandler: Function)

Opens a delete modal. It does not delete anything; it just asks the user if they're sure if they want to delete something. This method returns dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

This parameter accepts the following properties:

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
{

    objectTypeName: String,

    actions: List<Object> // { position: "left"|"right", disabled: Boolean, click: Function, text: String }

    dependencyListPromise: Promise<List<DependencyObject>>?,

    cancelAction: Function?,

    acceptAction: Function?,

    focusEls: {

        cancel: HTMLElement?,

        accept: HTMLElement?

    }

}
```

For more information about DependencyObject, refer to its entry in the Additional Forms API Object page.

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

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
var modalData = {

     objectTypeName: "Object Type Name"

};

convenienceApi.modalService.openDeleteModal(modalData).then(function (action) {

     if (!action.wasCancelled) {

          console.log("Delete the thing here");

     } else {

          console.log("Cancelled, so don't delete the thing");

     }

});
```

#### openMultiListPickerModal(model: Object, openModalHandler: Function)

Opens a multi-list picker modal. This method returns dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

This parameter accepts the following properties:

View properties Copy

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
{

    // Used to format the full title of the modal, such as "Select Items - [label goes here]".

    label: String,

    // A key by which the multi-list picker component stores settings of its inner Item Lists in session storage.

    persistenceKey: String,

    // A key by which the multi-list picker component stores widths of columns of its inner Item Lists in session storage.

    columnsPersistenceKey: String,

    // The name of the property used by a multi-list picker component to uniquely identify data items in the list.

    rowKeyName: String,

    // An array of values that are currently selected in the multi-list picker component. These values must correspond to values of property in data items denoted by "rowKeyName".

    selectedValues: Array<Number>,

    // An object used by the multi-list picker component to retrieve its data. For more information, see the following section.

    itemListDataProvider: Object<ItemListDataProvider>,

    // An object used by the multi-list picker component to retrieve and save settings of its inner Item Lists. For more information, see the following section.

    itemListSettingPersistenceService: Object<ItemListSettingPersistenceService>,

    // A workspace identifier mainly used for data retrieval.

    workspaceId: Number,

    // An identifier for the type of objects being selected.

    objectTypeId: Number,

}
```

For more information about the itemListDataProvider and itemListSettingPersistenceService objects, see the Additional Forms API objects page .

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

The following sample illustrates how to open a multi-list picker modal: (sample in progress)

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
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
var mockData = [

     {

          "Name": "test1 name",

          "ArtifactID": 1039665

     },

     {

          "Name": "test2 name",

          "ArtifactID": 1039666

     }

];

// Create item list data provider instance.

var itemListDataProvider = {

     getFieldMetadata: function (fieldName) {

          // not used in this example, but it is an example of what the return shape looks like

          return {

               artifactID: 0,

               artifactViewFieldID: 0,

               associativeObjectTypeID: 0,

               columnName: "Name",

               fieldTypeID: 0, // fixed length text

               filterType: "None",

               headerName: null,

               itemListType: "Text",

               isSystem: false

          };

     },

     getColumns: function (itemListReloadHandler) {

          var toolbarContentElement = document.createElement("span");

          toolbarContentElement.innerText = "Content of Toolbar Content element";

          var noop = function () {};

          return convenienceApi.promiseFactory.resolve([

               {

                    id: "0",

                    actAsAdvanced: false,

                    defaultWidth: 150,

                    content: {

                         comparer: null,

                         dataLocation: "ArtifactID", // key to look for in each data entry

                         formatDefinition: null,

                         formatters: null

                    },

                    contentAlignment: null,

                    headerContent: {

                         clickable: false,

                         indicators: null,

                         title: null,

                         toolbarContent: toolbarContentElement

                    },

                    highlighted: false,

                    minWidth: 75,

                    resizable: true,

                    separatorVisible: true,

                    title: "Artifact ID",

                    width: 150,

                    wrapped: true,

                    filter: null,

                    filterable: false,

                    filterAdvanced: false,

                    filterOperators: null,

                    filterTitle: null,

                    filterAriaLabel: null,

                    filterOperatorAriaLabel: null,

                    sortable: false,

                    sortDirection: null,

                    sortTitle: null,

                    containerClass: null,

                    prepareForGrid: noop,

                    generateFilterElement: noop

               },

               {

                    id: "1",

                    actAsAdvanced: false,

                    defaultWidth: 150,

                    content: {

                         comparer: null,

                         dataLocation: "Name", // key to look for in each data entry

                         formatDefinition: null,

                         formatters: null

                    },

                    contentAlignment: null,

                    headerContent: {

                         clickable: false,

                         indicators: null,

                         title: null,

                         toolbarContent: toolbarContentElement

                    },

                    highlighted: false,

                    minWidth: 75,

                    resizable: true,

                    separatorVisible: true,

                    title: "Name",

                    width: 150,

                    wrapped: true,

                    filter: null,

                    filterable: false,

                    filterAdvanced: false,

                    filterOperators: null,

                    filterTitle: null,

                    filterAriaLabel: null,

                    filterOperatorAriaLabel: null,

                    sortable: false,

                    sortDirection: null,

                    sortTitle: null,

                    containerClass: null,

                    prepareForGrid: noop,

                    generateFilterElement: noop

               }

          ]);

     },

     getTextIdentifierColumnName: function () {

          return "Name";

     },

     query: function (request, columns) {

          var filteredData = mockData.slice();

          if (request.idsToExclude !== void 0) {

               // exclude certain values from result

               filteredData = filteredData.filter(function (entry) {

                    var includeEntry = true;

                    var i;

                    for (i = 0; i < request.idsToExclude.length; ++i) {

                         if (request.idsToExclude[i] === entry.ArtifactID) {

                              includeEntry = false;

                              break;

                         }

                    }

                    return includeEntry;

               });

          }

          if (request.idsToInclude !== void 0) {

               // include certain values in result

               filteredData = filteredData.filter(function (entry) {

                    var includeEntry = false;

                    var i;

                    for (i = 0; i < request.idsToInclude.length; ++i) {

                         if (request.idsToInclude[i] === entry.ArtifactID) {

                              includeEntry = true;

                              break;

                         }

                    }

                    return includeEntry;

               });

          }

          return convenienceApi.promiseFactory.resolve({

               "Results": filteredData,

               "TotalCount": filteredData.length,

               "CurrentStartIndex": 1

          });

     },

     getValuesByIds: function (ids) {

          // not used in this example; dummy data only to show shape of response

          return convenienceApi.promiseFactory.resolve(mockData.slice());

     }

};

// Create item list setting persistence service.

var itemListSettingPersistenceService = {

     getItemListState: function (itemListKey) {

          // read item list state from persistence based on itemListKey

          return {

               startIndex: 1,

               totalItems: 1,

               pageSize: 10,

               data: [],

               filters: [],

               sorts: [],

               columnWidths: {}

          };

     },

     getItemListStateOrDefault: function (itemListKey, columnWidthsKey) {

          var state = this.getItemListState(itemListKey);

          var columnWidths = this.getItemListColumnWidths(columnWidthsKey);

          if (!state) {

               state = {

                    startIndex: 1,

                    totalItems: 0,

                    pageSize: 10,

                    data: [],

                    filters: [],

                    sorts: [],

                    columnWidths: {}

               };

          }

          state.columnWidths = columnWidths;

          return state;

     },

     setItemListState: function (itemListKey, itemListStateValue) {

          // write item list state to persistence based on itemListKey

     },

     getFiltersVisible: function (itemListKey, workspaceId) {

          // read filters boolean from persistence or remotely based on itemListKey or workspaceId

          return convenienceApi.promiseFactory.resolve(false);

     },

     setFiltersVisible: function (itemListKey, filtersVisibleValue) {

          // write filters boolean to persistence based on itemListKey

     },

     getGridStyle: function () {

          // read grid style from persistence or remotely based on itemListKey

          return convenienceApi.promiseFactory.resolve(false);

     },

     setGridStyle: function (gridStyleValue) {

          // write grid style boolean to persistence

     },

     getItemListColumnWidths: function (columnWidthsKey) {

          // read item list column widths from persistence based on columnWidthsKey

          return {};

     },

     setItemListColumnWidth: function (itemListKey, columnKey, width) {

          // write item list column width to persistence based on itemListKey and columnKey

     }

};

var model = {

     label:  "MLP sample",

     persistenceKey:  "MY_PERSISTENCE_STRING",

     columnsPersistenceKey:  "MY_COLUMN_WIDTH_PERSISTENCE_KEY",

     rowKeyName:  "ArtifactID", // determines the key of each row (used in itemListDataProvider.query)

     selectedValues: [],

     itemListDataProvider: itemListDataProvider,

     itemListSettingPersistenceService: itemListSettingPersistenceService,

     workspaceId: -1,

     objectTypeId: 0

};

// could put this in an onclick event for a button, for example

convenienceApi.modalService.openMultiListPickerModal(model).then(function (action) {

     if (!action.wasCancelled) {

          console.log("Multiple items selected");

          // action.output contains the artifact IDs of selected items.

          console.dir(action.output);

     }  else {

          console.log("Selection of multiple items cancelled");

     }

});
```

#### openSingleListPickerModal(model: Object, openModalHandler: Function)

Opens a single list picker modal. This method returns dialog promise that resolves to the dialog close result. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Parameters

Parameter

Description

model: Object

This parameter accepts the following properties:

View properties Copy

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
{

    // Used to format the full title of the modal, such as "Select Items - [label goes here]".

    label: String,

    // A key by which the single list picker component stores settings of its Item List in session storage.

    persistenceKey: String,

    // A key by which the single list picker component stores widths of columns of its Item List in session storage.

    columnsPersistenceKey: String,

    // The name of the property used by single list picker component to uniquely identify data items in the list.

    rowKeyName: String,

    // A value that is currently selected in the single list picker component. The value must correspond to value of property in data item denoted by "rowKeyName".

    selectedValue: Number,

    // An object which is used by the single list picker component to retrieve its data.

    itemListDataProvider: Object<ItemListDataProvider>,

    // An object used by the single list picker component to retrieve and save settings of its Item List.

    itemListSettingPersistenceService: Object<ItemListSettingPersistenceService>,

    // A workspace identifier mainly used for data retrieval.

    workspaceId: Number,

    // An identifier for the type of objects being selected.

    objectTypeId: Number,

}
```

For more information about the itemListDataProvider and itemListSettingPersistenceService objects, see the Additional Forms API objects page .

openModalHandler: Function

An optional callback function executed immediately after the modal opens.

Parameters

Parameter Description

OpenDialogResult

An object primarily interesting in that it contains the DialogController on its "controller" property. For more information, see Accessing The DialogController API on the Aurelia web site.

##### Return type

Promise<OpenDialogResult.closeResult>

##### Example

The following sample illustrates how to open a single list picker modal:

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
// Create item list data provider instance and item list setting persistence service. (see openMultiListPickerModal sample above for details)

var itemListDataProvider = // ...

var itemListSettingPersistenceService = // ...

var model = {

     label:  "SLP sample",

     persistenceKey:  "MY_PERSISTENCE_STRING",

     columnsPersistenceKey:  "MY_COLUMN_WIDTH_PERSISTENCE_KEY",

     rowKeyName:  "ArtifactID",

     selectedValue: 0,

     itemListDataProvider: itemListDataProvider,

     itemListSettingPersistenceService: itemListSettingPersistenceService,

     workspaceId: -1,

     objectTypeId: 0

};

convenienceApi.modalService.openSingleListPickerModal(model).then(function (action) {

     if (!action.wasCancelled) {

          console.log("Item selected");

          // action.output contains ArtifactID of selected item

          console.log(action.output);

     }  else {

          console.log("Item selection cancelled");

     }

});
```

## permission

Represents a permission object exposed as a part of the Event Handler API. It is used to check actions allowed for an object of a specific object type in a given workspace.

Property

Type

Description

canAdd

Boolean

Indicates whether a create action is allowed.

canDelete

Boolean

Indicates whether a delete action is allowed.

canEdit

Boolean

Indicates whether an edit action is allowed.

canSecure

Boolean

Indicates whether a secure action is allowed.

canView

Boolean

Indicates whether a view action is allowed.

canViewAudit

Boolean

Indicates whether a view audit action is allowed.

## popupService

Provides a service used to open pop-up windows.

### Methods

#### open(url: String, title: String, options: Object)

Opens a pop-up window with the specified options. For more information, see Window.open() on the MDN web docs site.

##### Parameters

Parameter

Description

url: String

The URL of the resource to load in the pop-up window.

title: String

The title of the pop-up window.

options: Object

(Optional) An object containing key-value pairs of window features to apply to the pop-up window. See the Window Features documentation on the WDN web docs site for a full list of how the pop-up window can be configured.

##### Return type

undefined

##### Example

Copy

```text
1
2
3
4
convenienceApi.popupService.open( "https://google.com" ,  "Google" , {

      width: 200,

      height: 200

 });
```

## previewSecurity

Provides a collection of methods for utilizing Preview Security mode. For more information, see Preview security on the Relativity Documentation site.

### Methods

#### openForGroup(groupArtifactId: Number)

Opens the Preview Security page in the same window for a specific group artifact ID.

##### Parameters

Parameter

Description

groupArtifactId: Number

The artifact ID of a specific group.

##### Return type

undefined

##### Example

Copy

```text
1
2
var groupArtifactId = 1015028;

 convenienceApi.previewSecurity.openForGroup(groupArtifactId);
```

## promiseFactory

Provides a factory containing methods for returning promises.

### Methods

See the following subsections for information about these methods:

- all()

- reject()

- resolve()

#### all()

Returns one of the following promises depending on the parameter passed to the method:

- An already resolved promise when it is passed an iterable parameter, such as an array or an object, which is empty.

- Asynchronously resolved promise when the iterable passed contains no promises.

- A pending promise in all other cases.

For more information, see Promise.all() on the MDN web docs site.

##### Parameters

None

##### Return type

promise

##### Example

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
var promise1 = convenienceApi.promiseFactory.resolve(3);

 var promise2 = 42;

 var promise3 =  new Promise(function (resolve, reject) {

    setTimeout(resolve, 100,  'tests' );

 });

 var promise = convenienceApi.promiseFactory.all([promise1, promise2, promise3]);

 promise.then(function (values) {

    console.log(values);  // [3, 42, "tests"]

 });
```

#### reject()

Returns a promise that is rejected with a specific reason. For more information, see Promise.reject() on the MDN web docs site.

##### Parameters

None

##### Return type

promise

##### Example

The following code sample illustrates how to return a rejected promise:

Copy

```text
1
2
3
4
5
6
7
var promise = convenienceApi.promiseFactory.reject( "rejection" );

 promise.then(function(resolvesTo) {

      console.log(resolvesTo);     // Never called.

 }, function(rejectsTo) {

      console.log(rejectsTo);         // "rejection"

 });
```

#### resolve()

Returns a promise that is resolved with a specific value. For more information, see Promise.resolve() on the MDN web docs site.

##### Parameters

None

##### Return type

promise

##### Example

Copy

```text
1
2
3
4
5
var promise = convenienceApi.promiseFactory.resolve( "resolution" );

 promise.then(function(resolvesTo) {

      console.log(resolvesTo);     // "resolution"

 });
```

## relativityFormsPopup

Includes methods for creating pop-up windows running the Relativity Forms API. For additional information about pop-up windows, see the following:

- Communicating between Relativity form pages

- popupControlApi object

- Popup eventHandlerFactory function

### Methods

See the following subsections for information about pop-up windows:

- openAdd()

- openEdit()

- openView()

#### openAdd()

Opens a Relativity Forms API pop-up window for given artifact type in add mode.

##### Syntax

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
openAdd({

   workspaceId: Number,

   artifactTypeId: Number,

   parentArtifactId: Number,

   associatedArtifactId: Number,  // optional

   connectorFieldArtifactId: Number,  // optional

   eventHandlerFactory: Function  // optional

 })
```

##### Parameters

Parameter

Description

workspaceId: Number

The artifact ID of the workspace in which the new object will be created.

artifactTypeId: Number

The artifact ID of the object type to be created.

parentArtifactId: Number

The artifact ID of the object to be used as the parent of the object being created.

associatedArtifactId: Number

The existing object to which the newly created object will be associated.

connectorFieldArtifactId: Number

The artifact ID of the Field (in the object being created) by which the newly created object will be associated to the existing object.

eventHandlerFactory: Function

An optional Function property. See Popup eventHandlerFactory function .

##### Return type

popupControlApi instance

#### openEdit()

Opens a Relativity Forms API pop-up window for a given object in edit mode.

##### Syntax

Copy

```text
1
2
3
4
5
6
openEdit({

   workspaceId: Number,

   artifactTypeId: Number,

   artifactId: Number,

   eventHandlerFactory: Function  // optional

 })
```

##### Parameters

Parameter

Description

workspaceId: Number

The artifact ID of the workspace in which the object being edited resides.

artifactTypeId: Number

The artifact ID of the object type to be edited.

artifactId: Number

The artifact ID of the object to be edited.

eventHandlerFactory: Function

An optional Function property. See Popup eventHandlerFactory function .

##### Return type

popupControlApi instance

#### openView()

Opens a Relativity Forms API pop-up window for a given object in view mode.

##### Syntax

Copy

```text
1
2
3
4
5
6
openView({

   workspaceId: Number,

   artifactTypeId: Number,

   artifactId: Number,

   eventHandlerFactory: Function  // optional

 })
```

##### Parameters

Parameter

Description

workspaceId: Number

The artifact ID of the workspace in which the object being viewed resides .

artifactTypeId: Number

The artifact ID of the object type to be viewed.

artifactId: Number

The artifact ID of the object to be viewed.

eventHandlerFactory: Function

An optional Function property. See Popup eventHandlerFactory function .

##### Return type

popupControlApi instance

## relativityHttpClient

Provides methods for making requests to Relativity REST services hosted by the Relativity instance. All requests are made as the currently logged in user.

### Methods

See the following subsections for information about these methods:

- get(url: String, requestOptions: Object)

- post(url: String, payload: Object, requestOptions: Object)

- put(url: String, payload: Object, requestOptions: Object)

- delete(url: String, requestOptions: Object)

-

keplerGet(url: string, requestOptions?: AxiosRequestConfig<any>, metricKey?: string)

-

keplerPost(url: string, payload: any, requestOptions?: AxiosRequestConfig<any>, metricKey?: string)

-

keplerPut(url: string, payload: any, metricKey?: string)

-

keplerDelete(url: string, metricKey?: string)

-

keplerPatch(url: string, payload: any, requestOptions?: AxiosRequestConfig<any>, metricKey?: string)

-

keplerCallLRP(hub: string, operation: string, payload: any, progressCallback: any, cancellationToken: any, requestOptions?: AxiosRequestConfig<any>, httpMethod?: string, signalRHub?: string, metricKey?: string)

-

getCancellationToken()

- makeRelativityRelativeUrl(url: String)

- makeRelativityBaseRequestOptions(extendWith: Object)

- makeRelativityRestRelativeUrl(url: String)

- makeRelativityRestBaseRequestOptions(extendWith: Object)

-

patch(input: string | Request, payload?: any, requestOptions?: RequestInit)

#### get(url: String, requestOptions: Object)

Makes an HTTP GET request to the given URL.

In general, execute a read operation for a resource by invoking a fetch of a specific URL and a requestOptions object with the GET method. For more information, see WindowOrWorkerGlobalScope.fetch() on the MDN web docs site.

Note: IE11 doesn't natively support Fetch and Promise, but Promise and Response on the MDN web docs site contain accurate information for Relativity Forms and IE11. Relativity Forms uses a polyfill to provide support for this functionality.

##### Parameters

Parameter

Description

url: String

A URL for a request.

requestOptions: Object

Optional request options object. It defaults to an empty object, and the method is overwritten to a GET request.

##### Return type

Promise - resolves to a Fetch API Response object. For more information, see Promise and Response on the MDN web docs site.

##### Example

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
var url = "any/url";

var requestOptions = {

     cache: "no-store",

     headers: {

          "header-name": "header-value"

     }

};

var responseJsonPromise = convenienceApi.relativityHttpClient.get(url, requestOptions)

    .then(function (response) { return response.json(); });
```

#### post(url: String, payload: Object, requestOptions: Object)

Makes an HTTP POST request to the given URL.

In general, create a resource by invoking a fetch of a specific URL and a requestOptions object with the POST method. The request body contains a specified payload. For more information, see WindowOrWorkerGlobalScope.fetch() on the MDN web docs site.

Note: IE11 doesn't natively support Fetch and Promise, but Promise and Response on the MDN web docs site contain accurate information for Relativity Forms and IE11. Relativity Forms uses a polyfill to provide support for this functionality.

##### Parameters

Parameter

Description

url: String

A URL for a request.

payload: Object|Array

A JSON serializable object to send in the request body.

requestOptions: Object

Optional request options object. It defaults to an empty object, and the method is overwritten to a POST request. The body is overwritten with the stringified payload.

##### Return type

Promise - resolves to a Fetch API Response object. For more information, see Promise and Response on the MDN web docs site.

##### Example

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
var url = "any/url";

var payload = {

     any: "parameter"

};

var requestOptions = {

     cache: "no-store",

     headers: {

          "header-name": "header-value"

     }

};

var responseJsonPromise = convenienceApi.relativityHttpClient.post(url, payload, requestOptions)

    .then(function (response) { return response.json(); });
```

#### put(url: String, payload: Object, requestOptions: Object)

Makes an HTTP PUT request to the specified URL.

In general, update a resource by invoking a fetch of a specific URL and a requestOptions object with the PUT method. The request body contains a specified payload. For more information, see WindowOrWorkerGlobalScope.fetch() on the MDN web docs site.

Note: IE11 doesn't natively support Fetch and Promise, but Promise and Response on the MDN web docs site contain accurate information for Relativity Forms and IE11. Relativity Forms uses a polyfill to provide support for this functionality.

##### Parameters

Parameter

Description

url: String

A URL for a request.

payload: Object|Array

A JSON serializable object to send in the request body.

requestOptions: Object

Optional request options object. It defaults to an empty object, and the method is overwritten to a PUT request. The body is overwritten with the stringified payload.

##### Return type

Promise - resolves to a Fetch API Response object. For more information, see Promise and Response on the MDN web docs site.

##### Example

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
var url = "any/url";

var payload = {

    any: "parameter"

};

var requestOptions = {

     cache: "no-store",

     headers: {

          "header-name": "header-value"

     }

};

var responseJsonPromise = convenienceApi.relativityHttpClient.put(url, requestOptions)

    .then(function(response) { return response.json(); });
```

#### delete(url: String, requestOptions: Object)

Makes an HTTP DELETE request to the specified URL.

In general, remove a resource by invoking a fetch of a specific URL and a requestOptions object with the DELETE method. For more information, see WindowOrWorkerGlobalScope.fetch() on the MDN web docs site.

Note: IE11 doesn't natively support Fetch and Promise, but Promise and Response on the MDN web docs site contain accurate information for Relativity Forms and IE11. Relativity Forms uses a polyfill to provide support for this functionality.

##### Parameters

Parameter

Description

url: String

A URL for a request.

requestOptions: Object

Optional request options object. It defaults to an empty object, and the method is overwritten to a DELETE request.

##### Return type

Promise - resolves to a Fetch API Response object. For more information, see Promise and Response on the MDN web docs site.

##### Example

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
var url = "any/url";

var requestOptions = {

     cache: "no-store",

     headers: {

          "header-name": "header-value"

     }

};

var deleteCompletePromise = convenienceApi.relativityHttpClient.delete(url, requestOptions);
```

#### patch(input: string | Request, payload?: any, requestOptions?: RequestInit)

Calls fetch with request method set to PATCH.

##### Parameters

Parameter

Description

input: string | Request

The resource that you wish to fetch. Either a Request object or a string containing the URL of the resource.

payload? : any

requestOptions?: RequestInit

##### Return type

Promise - a Promise for the Response from the fetch request. For more information, see Promise and Response on the MDN web docs site.

#### keplerGet(url: string, requestOptions?: AxiosRequestConfig<any>, metricKey?: string)

Invoke a GET request to a kepler service.

##### Parameters

Parameter

Description

url: string

URL to request

requestOptions?:AxiosRequestConfig<any> Object with request options to keplerjs. See AxiosRequestConfig .

metricKey?: string The key to identify the api call in metrics

##### Return type

Promise<void | T>. On 200 response the promise resolves to the de-serialized JSON object of the response body. On any other response it rejects to an object containing the response details - status code, headers & body.

#### keplerPost(url: string, payload: any, requestOptions?: AxiosRequestConfig<any>, metricKey?: string)

Invoke a POST request to a kepler service.

##### Parameters

Parameter

Description

url: string

URL to request

payload: any JSON serializable object to send in the request body

requestOptions?:AxiosRequestConfig<any> Object with request options to keplerjs. See AxiosRequestConfig .

metricKey?: string The key to identify the api call in metrics

##### Return type

Promise<void | T>. On 200 response the promise resolves to the de-serialized JSON object of the response body. On any other response it rejects to an object containing the response details - status code, headers & body.

#### keplerPut(url: string, payload: any, metricKey?: string)

Invoke a PUT request to a kepler service.

##### Parameters

Parameter

Description

url: string

URL to request

payload: any JSON serializable object to send in the request body

metricKey?: string The key to identify the api call in metrics

##### Return type

Promise<void | T>. On 200 response the promise resolves to the de-serialized JSON object of the response body. On any other response it rejects to an object containing the response details - status code, headers & body.

#### keplerDelete(url: string, metricKey?: string)

Invoke a DELETE request to a kepler service. The request cannot be cancelled and does not report progress.

##### Parameters

Parameter

Description

url: string

URL to request

metricKey?: string The key to identify the api call in metrics

##### Return type

Promise<void | T>. On 200 response the promise resolves to the de-serialized JSON object of the response body. On any other response it rejects to an object containing the response details - status code, headers & body.

#### keplerPatch(url: string, payload: any, requestOptions?: AxiosRequestConfig<any>, metricKey?: string)

Invoke a PATCH request to a kepler service.

##### Parameters

Parameter

Description

url: string

URL to request

payload: any JSON serializable object to send in the request body

requestOptions?:AxiosRequestConfig<any> Object with request options to keplerjs. See AxiosRequestConfig .

metricKey?: string The key to identify the api call in metrics

##### Return type

Promise<void | T>. On 200 response the promise resolves to the de-serialized JSON object of the response body. On any other response it rejects to an object containing the response details - status code, headers & body.

#### keplerCallLRP(hub: string, operation: string, payload: any, progressCallback: any, cancellationToken: any, requestOptions?: AxiosRequestConfig<any>, httpMethod?: string, signalRHub?: string, metricKey?: string)

Call to a kepler service to perform a long running operation

##### Parameters

Parameter

Description

hub: string

Url for the Kepler service

operation: string Name of the method on the Kepler service to call

payload: any The body of the request

progressCallback: any Function called when the long running operation posts a status update. It's called with an object with the type of the IProgress parameter defined in the Kepler endpoint

cancellationToken: any Instance of keplerjs.CancellationToken - returned from the getCancellationToken() function - to cancel the long running operation

requestOptions?:AxiosRequestConfig<any> Object with request options to keplerjs. See AxiosRequestConfig .

httpMethod?: string HTTP method for the call. Defaults to "POST", if omitted

signalRHub?: string The path to the SignalR hub to use (for progress and cancel). If not specified, the default Object Manager hub is used

metricKey?: string The key to identify the api call in metrics

##### Return type

Promise<void | T>: Promise resolves to the result of the long running operation

#### GetCancellationToken

Get a new instance of a keplerjs.CancellationToken. For use when calling the keplerCallLRP function.

##### Return type

CancellationToken: instance of keplerjs.CancellationToken. See CancellationToken

#### makeRelativityRelativeUrl(url: String)

Returns a String, which is the specified relative URL. However, it is prefixed with the base URL of the current Relativity instance.

##### Parameters

Parameter

Description

url: String

A URL for a request.

##### Return type

String

##### Example

Copy

```text
1
var relativityUrl = makeRelativityRelativeUrl( "some/path/and/service.asmx" );
```

#### makeRelativityBaseRequestOptions(extendWith: Object)

Generates a base requestOptions object in calls against services on Relativity.

##### Parameters

Parameter

Description

extendWith: Object

Optional request options object. It defaults to an empty object, and the method is overwritten to a GET request.

##### Return type

Object

##### Example

Copy

```text
1
2
3
4
5
6
7
var requestOptions= makeRelativityBaseRequestOptions({

     cache: "no-store",

     headers: {

          "header-name": "header-value"

     }

});

var responsePromise = convenienceApi.relativityHttpClient.get("any/relativity/url", requestOptions);
```

#### makeRelativityRestRelativeUrl(url: String)

Prefixes the specified URL with the base URL for Relativity.REST.

##### Parameters

Parameter

Description

url: String

A URL for a request.

##### Return type

String

##### Example

Copy

```text
1
var relativityRestUrl = makeRelativityRestRelativeUrl( "/Workspace/3040506/Custodian" );
```

#### makeRelativityRestBaseRequestOptions(extendWith: Object)

Generates a base requestOptions object for use in calls against the Relativity.REST services.

##### Parameters

Parameter

Description

extendWith: Object

Optional request options object. It defaults to an empty object, and the method is overwritten to a GET request.

##### Return type

Object

##### Example

Copy

```text
1
2
3
4
5
6
7
var requestOptions= makeRelativityRestBaseRequestOptions({

     cache: "no-store",

     headers: {

          "header-name": "header-value"

     }

});

var responsePromise = convenienceApi.relativityHttpClient.get("any/relativity/rest/url", requestOptions);
```

## reviewQueueBrowser

Provides functionality similar to the navigational controls on the page. It provides methods to move through the objects of the queue, such as going to first, previous, next, and last objects. It also provides properties for the index of the current object and information about the queue as a whole.

### Properties

Property

Type

Description

currentQueueIndex

Number

The 0-based index of the current review queue object. The value is -1 if the current element isn't present in the queue.

reviewQueueInformation

Object

An object that contains information about the current review queue and the queue itself:

Copy

```text
1
2
3
4
5
6
7

{

      workspaceId: ?Number,

      artifactTypeId: ?Number,

      queueArtifactIds: Array<Number>,

      warnings: Array<String>

 }
```

### Methods

See the following subsections for information about these methods:

- navigate.first()

- navigate.previous()

- navigate.next()

- navigate.last()

- navigate.byIndex(index: Number)

#### navigate.first()

Navigates to the first object in the review queue. This method returns a resolved promise if navigation occurred, and a rejected promise if navigation couldn't be performed.

##### Parameters

None

##### Return type

Promise

##### Example

The following sample illustrates how to navigate to the first object on every page interaction:

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
exampleTypeEventHandlers[eventNames.PAGE_INTERACTION] = function() {

      const reviewQueueBrowser = convenienceApi.reviewQueueBrowser;

      reviewQueueBrowser.navigate.first().then(

          function() { console.log("navigated to the first index") },

          function(err) { console.error(err) }

      );

 };
```

#### navigate.previous()

Navigates to the previous object in the review queue. This method returns a resolved promise if navigation occurred, and a rejected promise if navigation couldn't be performed.

##### Parameters

None

##### Return type

Promise

##### Example

The following sample illustrates how to navigate to the previous object on every page interaction:

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
exampleTypeEventHandlers[eventNames.PAGE_INTERACTION] = function() {

      const reviewQueueBrowser = convenienceApi.reviewQueueBrowser;

      reviewQueueBrowser.navigate.previous().then(

          function() { console.log("navigated to " + reviewQueueBrowser.currentQueueIndex) },

          function(err) { console.error(err) }

      );

 };
```

#### navigate.next()

Navigates to the next object in the review queue. This method returns a resolved promise if navigation occurred, and a rejected promise if navigation couldn't be performed.

##### Parameters

None

##### Return type

Promise

##### Example

The following sample illustrates how to navigate to the next object on every page interaction:

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
exampleTypeEventHandlers[eventNames.PAGE_INTERACTION] = function() {

      const reviewQueueBrowser = convenienceApi.reviewQueueBrowser;

      reviewQueueBrowser.navigate.next().then(

          function() { console.log("navigated to " + reviewQueueBrowser.currentQueueIndex) },

          function(err) { console.error(err) }

      );

 };
```

#### navigate.last()

Navigates to the last object in the review queue. This method returns a resolved promise if navigation occurred, and a rejected promise if navigation couldn't be performed.

##### Parameters

None

##### Return type

Promise

##### Example

The following sample illustrates how to navigate to the last object on every page interaction:

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
exampleTypeEventHandlers[eventNames.PAGE_INTERACTION] = function() {

      const reviewQueueBrowser = convenienceApi.reviewQueueBrowser;

      reviewQueueBrowser.navigate.last().then(

          function() { console.log("navigated to the last index") },

          function(err) { console.error(err) }

      );

 };
```

#### navigate.byIndex(index: Number)

Navigates to a specified object in the review queue. This method returns a resolved promise if navigation occurred, and a rejected promise if navigation couldn't be performed.

##### Parameters

Parameter Description

index: Number A number indicating the location of an object in the review queue.

##### Return type

Promise

##### Example

The following sample illustrates how to navigate to the 3rd object on every page interaction:

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
exampleTypeEventHandlers[eventNames.PAGE_INTERACTION] = function() {

      const reviewQueueBrowser = convenienceApi.reviewQueueBrowser;

      reviewQueueBrowser.navigate.byIndex(2).then(

          function() { console.log("navigated to the 3rd object") },

          function(err) { console.error(err) }

      );

 };
```

## user

Provides properties and methods related to a user.

### Methods

#### getCurrentAclUserId(workspaceId: <Number>)

Retrieves the current access control list (ACL) identifier.

##### Parameters

Parameter Description

workspaceId: <Number> The artifiact ID of a specific workspace.

##### Return type

Promise<Number>

##### Example

Copy

```text
1
   convenienceApi.user.getCurrentAclUserId(workspaceId).then(function (userId) {  someCallback(userId);});
```

## utilities

Includes various utility functions.

### Methods

See the following subsections for information about these methods:

- getHtmlEventTarget(htmlEvent: Object)

- getRelativityPageBaseWindow()

- keyValueArrayToJsonArrayTransformer(arrayToTransform: Array, inputValueKey: String)

- reload()

#### getHtmlEventTarget(htmlEvent: Object)

Gets the target of an HTML element. The target is dependent on the browser. For example, IE uses __target.

##### Parameters

Parameter Description

htmlEvent: Object HTML Event to retrieve the target.

##### Return type

Object|null

##### Example

Copy

```text
1
2
3
4
5
6
var htmlEvent = { target: 1, __target: 2 };

 var target = convenienceApi.utilities.getHtmlEventTarget(htmlEvent);

 console.log(target);

 /* Console output:

   *     2

   */
```

#### getRelativityPageBaseWindow()

Returns the window with the Relativity context. Use this method to access the Relativity window from within a pop-up window.

##### Parameters

None

##### Return type

Window object

##### Example

The following code sample illustrates how to access a function on the Relativity window via the window object returned by getRelativityPageBaseWindow method.

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
var relativityWindow = convenienceApi.utilities.getRelativityPageBaseWindow();

console.log(relativityWindow.GetRelativityApplicationWebResourceFile("some-guid", "latest", "file.txt"));

/* Console output:

 * "/Relativity/RelativityApplicationWebResourceFile/some-guid/latest/file.txt"

 */
```

#### keyValueArrayToJsonArrayTransformer(arrayToTransform: Array, inputValueKey: String)

Converts an array of name-value pairs into an array with values for a specified key.

##### Parameters

Parameter Description

arrayToTransform: Array Array to be transformed into a dictionary.

inputValueKey: String The name of the object of the value key in array elements.

##### Return type

Array

##### Example

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
var someArray = [

      { Order: 1, Letter:  "A" },

      { Order: 2, Letter:  "B" },

      { Order: 3, Letter:  "C" },

      { Order: 4, Letter:  "D" }

 ];

 var arr = convenienceApi.utilities.keyValueArrayToJsonArrayTransformer(someArray,  "Order" );

 console.log(arr);

 /* Console output:

   *     [1, 2, 3, 4]

   */
```

#### reload()

Reloads the form and triggers event handlers.

##### Parameters

None

##### Return type

Undefined

##### Example

Copy

```text
1
   convenienceApi.utilities.reload();
```

## validation

Represents an object used to facilitate the form validation process by creating data structures required by the validationArray.

### Methods

See the following subsections for information about these methods:

- getFailedSummaryObject(validationMessage: String|List<String>)

- getFailedFieldObject(fieldId: String|Number, validationMessage: String)

- getDefaultSummaryErrorForAction(actionName: String)

#### getFailedSummaryObject(validationMessage: String|List<String>)

Creates a summary-level validation error object. This method returns a validation object that represents a summary error.

##### Parameters

Parameter Description

validationMessage: String|List<String> A string specifying a validation message.

##### Return type

##### ValidationObject

An object for representing the result of a validation check in the format expected by the validation service.

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
{

    scope: {                      // an object that will make a validation object show failures against a particular field

        type: const,              // FIELD_VALIDATION_SCOPE

        id:   String or Number,   // id of the field that owns the validation object

    }

    result:   List<String>,       // list of validation messages

    success:  bool,               // result of validation check

    errors:   List<String>        // list of error messages

}
```

##### Example

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
/*

   * 1. Single message example

   */

 function validateSaveHandler(response, validationArray) {

    /*

     * For example, a response from the save request contains error object of the following shape:

     * response = {

     *     success: false,

     *     message: "Name already exists."

     * }

     */

    if (!response.success) {

      var errorSummary = convenienceApi.validation.getFailedSummaryObject(response.message);  // Create a validation object for displaying the given error message below the action bar.

      validationArray.push(errorSummary);  // Append it to the validationArray for the application to display.

    }

 }
```

##### Example Error Message Output - Single error message

The application displays this error message below the action bar:

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
/*

   * 2. Multiple message example

   */

function validateSaveHandler(response, validationArray) {

    var multipleMessages = [ "First error" ,  "Second error" ,  "Third error" ];

   var  errorSummary = convenienceApi.validation.getFailedSummaryObject(multipleMessages);  // Create a validation object for displaying the given error message below the action bar.

    validationArray.push(errorSummary);  // Append it to the validationArray for the application to display.

 }
```

##### Example Error Message Output - Multiple error messages

The application displays this error message below the action bar:

#### getFailedFieldObject(fieldId: String|Number, validationMessage: String)

Creates a field-level validation error object. This method returns a validation object that represents a single-field error.

##### Parameters

Parameter Description

fieldId: String|Number ID of the field that owns the validation object

validationMessage: String Message to display in the field error

##### Return type

##### ValidationObject

An object for representing the result of a validation check in the format expected by the validation service.

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
{

    scope: {                      // an object that will make a validation object show failures against a particular field

        type: const,              // FIELD_VALIDATION_SCOPE

        id:   String or Number,   // id of the field that owns the validation object

    }

    result:   List<String>,       // list of validation messages

    success:  bool,               // result of validation check

    errors:   List<String>        // list of error messages

}
```

##### Example

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
function validateSaveHandler(response, validationArray) {

 /*

  * For example, a response from the save request contains error object of the following shape:

  * response = {

  *     success: false,

  *     messages: [

  *         { propertyName: "Name", message: "Field is mandatory" }

  *     ]

  * }

  */

  if (!response.success) {

    for (var i = 0; i < response.messages.length; i++) {

      var message = response.messages[i];

      var fieldId = this.fieldNameToFieldIdMap.get(message.propertyName);

      var fieldError = convenienceApi.validation.getFailedFieldObject(fieldId, message.message); // Create a validation object for displaying the given error message below a field.

      validationArray.push(fieldError); // Append it to the validationArray for the application to display.

    }

  }

};
```

##### Example Error Message Output - failed field error

The application displays these error messages below the fields they belong to:

#### getDefaultSummaryErrorForAction(actionName: String)

Retrieve a localized default summary error message for a specific action, such as save.

##### Parameters

Parameter Description

actionName: String A string indicating the name of the action. See ACTIONS constant for possible values.

##### Return type

String

##### Example

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
function validateSaveHandler(response, validationArray) {

  if (!response.success) {

    var summaryMessage = convenienceApi.validation.getDefaultSummaryErrorForAction(convenienceApi.constants.ACTIONS.SAVE);

    // When localized to EN, summaryMessage = "Cannot Save."

    // When localized to ES, summaryMessage = "No puede Salvar."

    var errorSummary = convenienceApi.validation.getFailedSummaryObject(summaryMessage); // Create a validation object for displaying the default save error message in the current localization

    validationArray.push(errorSummary); // Append it to the validationArray for the application to display.

  }

}
```
