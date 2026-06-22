---
title: "Submit pipeline"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Submit_pipeline.htm
collection: developer
fetched_at: 2026-06-22T06:31:57+00:00
sha256: b03a89ac672eb41267f2e99cc5b1130715c2e628dc24ec087ea6a08087563159
---

Submit pipeline

# Submit pipeline

The Submit pipeline includes event handlers that control the workflow for saving changes to a form. It contains two event handlers for handling validation: one that executes when the form is updated, and another that executes before the form is saved to Relativity. Additionally, you have the option to implement an event handler that uses custom logic for saving data or to use the standard event handler for this operation provided in Relativity.

For example, you might want to implement a custom event handler that performs custom validation of the data before it saves or performs cleanup after the data is saved.

## Submit pipeline workflow

The Submit pipeline represents the process for saving changes to a Relativity form. The following diagram illustrates when specific event handlers in this workflow are executed, and the gray boxes indicate handlers which your JavaScript may implement. For more information about creating or editing objects, see Object Manager API .

### Submit pipeline event handlers

The following table lists each of the event handlers used in the Submit pipeline.

Event handler

Execution pipeline

Description

preSave

Submit

Executes after the form is submitted and before any validation occurs. (This represents a handler which can be implemented in JavaScript, rather than the .NET PreSave handler).

validation (on submit)

Submit or Change

Executes after the standard validation available through an application has completed. For more information, see Change pipeline.

replaceSave

Submit

Executes after form validation has occurred. This event handler is invoked in place of the event handler in the stock application for saving object instance data.

(If a handler is not implemented for replaceSave , the ObjectManager will be used. It is at that time that any .NET PreSave and PostSave event handlers are executed.)

validateSave

Submit

Executes after an attempt to save data is made. The response object from the save operation is passed to this event handler, which validates whether the operation was successful.

postSave

Submit

Executes after the data has been successfully validated. (This represents a handler which can be implemented in JavaScript, rather than the .NET PostSave handler).

pageUnload

Submit

Executes immediately before the current form data is cleaned up, and the application navigates to the route or external URL determined by the submit types, such as Save, Save & New, or others.

### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

## preSave

The preSave event handler executes after the form is submitted, and before any validation occurs. It is the first event handler to execute in the Submit pipeline.

### Syntax

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.PRE_SAVE] = function(modelData, event) {

          console.log( "Inside PRE_SAVE event handler" );

     };

     return eventHandlers;

}(eventNames, convenienceApi));
```

### Parameters

Copy

```text
1
   function(modelData, event )
```

The following table lists the input parameters:

Parameter

Description

modelData

An object containing the current information in the form.

event

An object of the form

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
{

    type: <EVENT_TYPE>  // EVENT_TYPE = { CHANGE: "change", SUBMIT: "submit" }

    payload: {

        saveOperation: <SAVE_OPERATIONS>

            //SAVE_OPERATIONS = { SAVE: 0,

            // SAVE_AND_NEW: 1, SAVE_AND_BACK: 2,

            // SAVE_AND_CONTINUE: 3, SAVE_AND_NEXT: 4,

            // SAVE_AND_PREVIOUS: 5 }

    }

}
```

The PRE_SAVE event handler accepts modelData and event as parameters. If you encounter an error like Uncaught TypeError: a.map is not a function , check that you are passing the correct values. You may be inadvertently passing layoutData instead of modelData .

## validation (on submit)

The validation event handler executes after the standard validation available through an application has completed. The application updates the form containing any fields that are identified as invalid by the standard validation rules. Standard validation includes rules that the current layout sets, such as a field marked as required. It also includes validation event handlers.

Review the following guidelines for the validation event handler:

- Use validation event handlers to perform any specialized validation on the form data outside of the standard validation completed by the application.

- When the form data is valid, a validation event handler does not return a value.

- When the form data is invalid, a validation event handler appends an object to the currentValidationState parameter with the following:

- The field containing invalid information.

- A string providing a message to the user about how to fix the validation issue.

In the Submit pipeline, validation failures stop the workflow from proceeding and prevent any form data from being submitted.

### Syntax

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.VALIDATION] = function() {

         console.log( "Inside VALIDATION event handler" );

    };

     return eventHandlers;

}(eventNames, convenienceApi));
```

### Parameters

Copy

```text
1
   function(modelData, event , currentValidationState)
```

The following table lists the input parameters:

Parameter

Description

modelData

An object containing the current information in the form.

event

View the parameter for the Submit pipeline Copy

```text
1
2
3
4
5
6
{

      type: <EVENT_TYPE>  // EVENT_TYPE = { CHANGE: "change", SUBMIT: "submit" },

      payload: {

          saveOperation: <SAVE_OPERATIONS>

      }

 }
```

View the parameter for the Change pipeline

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

      type: <EVENT_TYPE>  // EVENT_TYPE = { CHANGE: "change", SUBMIT: "submit" },

      payload: {

          fieldId: Number|String,

          htmlEvent: Event

      }

 }
```

currentValidationState

An array containing objects of existing validation failures. The event handler appends to this array if it evaluates the form data as invalid. For sample code, see Validation example .

### Validation example

You can use convenienceApi.validation to create validation objects for either individual fields or for an entire form. The following code sample illustrates individual field validation. For more information, see convenienceApi object .

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
function validationHandler(modelData, payload, currentValidationState) {

      //This example uses an an integer field that must contain an even number to be valid.

      var someIntegerFieldId = 100001;

      var someIntegerFieldValue = modelData[someIntegerFieldId];

      var isValid = (someIntegerFieldValue % 2 === 0);

      if (!isValid) {

          var errorMessage =  "Integer field value " + someIntegerFieldValue.toString() +  " must be even." ;

          var validationError = convenienceApi.validation.getFailedFieldObject(someIntegerFieldId, errorMessage);

          // This validation error created by the event handler is applied

          // to the form and displayed on the appropriate field when

          // all of the validation event handlers finish executing.

          currentValidationState.push(validationError);

      }

 }
```

## replaceSave

The replaceSave event handler executes after form validation has occurred. This event handler is invoked in place of the event handler in the stock application for saving object instance data. Only register this event handler when the stock application object instance data service doesn't have the functionality to save form data.

Only register one handler function for this event. If you register multiple functions, only the first one is executed, and the others are ignored.

The replaceSave event handler performs the following operations:

- Transforms the object instance data into the form expected by the service.

- Makes requests to the source is providing the object instance data.

- Returns a promise that resolves on a successful save.

- Returns a promise that resolves on an unsuccessful save, which allows for custom error messaging on the failed save.

- Returns replaceSave failed message on failed save.

### Syntax

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.REPLACE_SAVE] = function(objectInstanceData, objectVersionToken) {

         console.log( "Inside REPLACE_SAVE event handler" );

    };

     return eventHandlers;

}(eventNames, convenienceApi));
```

### Parameters

Copy

```text
1
   function(objectInstanceData, objectVersionToken)
```

The following table lists the input parameter:

Parameter

Description

objectInstanceData

An object representing the object instance data to save.

Formatted as comma-separated Field ID: Value pairs. See the Field Value section of the Additional Forms API Objects page for more information.

objectVersionToken

The version token of the object used for record overwrites protection.

The value is null when first saving a brand new object and is not null for later saves.

### Example

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};

    eventHandlers[eventNames.REPLACE_SAVE] = function(objectInstanceData, objectVersionToken) {

        console.log( "Inside REPLACE_SAVE event handler" );

        // Transform objectInstanceData into a form expected by some API

        var transformedObjectInstanceData = transformObjectInstanceData(objectInstanceData);

        // Make the API call and send objectInstanceData as the payload

        var returnPromise;

        if (this.isNew) {

            returnPromise = convenienceApi.relativityHttpClient.post("some API URL", transformedObjectInstanceData);

        } else {

            returnPromise = convenienceApi.relativityHttpClient.put("some API URL", transformedObjectInstanceData);

        }

        // Return a promise that resolves on a successful save and rejects on an unsuccessful save

        return returnPromise;

    };

    return eventHandlers;

}(eventNames, convenienceApi));
```

## validateSave

The validateSave executes after an attempt to save data is made. The response object from the save operation is passed to this event handler, which validates whether the operation was successful.

Depending on the outcome of the save operation, the validateSave event handler responds as follows:

- For a successful save operation, the event handler does not return any value or modify any of its arguments. If the event handler needs to do asynchronous work to validate the operation, it should return a promise that resolves after the work is completed.

- For an unsuccessful save that a user can correct by editing the form, the handler appends one or more validation messages to the validationArray argument. These messages are displayed to the user.

- For an unsuccessful save that cannot be corrected, the event handler returns a rejected promise for redirecting the user to the error page.

### Syntax

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

     var eventHandlers = {};

     eventHandlers[eventNames.VALIDATE_SAVE] = function() {

          console.log( "Inside VALIDATE_SAVE event handler" );

     };

     return eventHandlers;

}(eventNames, convenienceApi));

```

### Parameters

Copy

```text
1
   function(response, validationArray)
```

The following table lists the input parameters:

Parameter

Description

response

The response object is what was returned from the replaceSave event.

If there is no overwritten replaceSave event handler the response object has the following behavior:

- For a successful save the response, the variable is the de-serialized JSON object of the response body.

- For an unsuccessful save the response, the variable contains information about the status code, headers, request information, and error data.

validationArray

An empty array where the event handler adds any validation objects. These objects contain messages for display to the user as errors. In the validation namespace, the utilities API exposes functions for constructing these objects. The messages can target a specific field or the error summary that is shown below the action bar. See validation in the convenienceAPI.

### Example

You can use the validateSave event handler to display messages to the user when an error occurs. The following code sample illustrates how to create a validation object, provide a validation message for display to the user, and redirect a user to an error page.

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
function validateSaveHandler(response, validationArray) {

      /*

       * Response from the save request contains this error:

       *  response = {

       *      success: false,

       *      message: "Name already exists."

       *  }

       */

      var saveValidationPromise = convenienceApi.promiseFactory.resolve();

      if (!response.success) {

          if(!response.message) {

             // Sets the return promise to reject if the error message cannot be read.

               saveValidationPromise = convenienceApi.promiseFactory.reject("Unreadable error from save validation!");

          } else {

             // Create a validation object used to display an error message below the action bar.

             var errorSummary = convenienceApi.validation.getFailedSummaryObject(response.message);

             // Append a validation message to the validationArray for the application to display.

             validationArray.push(errorSummary);

      }

      return saveValidationPromise;

 }

```

#### Example Error Message Output

The application displays this error message below the action bar:

## postSave

The postSave event handler executes after the data has been successfully validated.

### Syntax

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.POST_SAVE] = function() {

          console.log("Inside POST_SAVE event handler");

     };

     return eventHandlers;

}(eventNames, convenienceApi));
```

### Parameters

Copy

```text
1
   function(artifactId)
```

The following table lists the input parameters:

Parameter

Description

artifactId

The artifact identifier of the object being saved.

## pageUnload

The pageUnload event handler executes immediately before the current form data is cleaned up, and the application navigates to the route or external URL determined by the submit types, such as Save, Save & New, or others.

### Syntax

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.PAGE_UNLOAD] = function() {

          console.log("Inside PAGE_UNLOAD event handler");

     };

     return eventHandlers;

}(eventNames, convenienceApi));
```

### Parameters

Copy

```text
1
   function()
```

### Example

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
function pageUnloadHandler = function() {

     // redirect a user to a custom page after saving

     if (window.confirm("Would you like to go directly to the CUSTOM_PAGE?")) {

          location.href = "/Relativity/CustomPages/CUSTOM_PAGE_GUID/CUSTOM_PAGE_PATH";

     }

}
```
