---
title: "Change pipeline"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Change_pipeline.htm
collection: developer
fetched_at: 2026-06-22T06:31:56+00:00
sha256: 5595f74c60a17fd1dc203346aa1d1e6c85d7d9885d2aaa16c1478c16c1835524
---

Change pipeline Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Change pipeline

The Change pipeline includes event handlers that you can use to customize user interaction with form fields and to develop your own validation logic for individual fields or the entire form. For example, you might implement an event handler that validates an integer field is even.

## Change pipeline workflow

The Change pipeline represents how interactions occur within Relativity forms, and how modifications to form fields are validated. The following diagram illustrates when specific event handlers in this workflow are executed.

(Click to expand)

### Change pipeline event handlers

The following table lists each of the event handlers used in the Change pipeline.

Event handler

Execution pipeline

Description

pageInteraction

Change

Executes immediately after an interaction with the form occurs.

validation (on change)

Change or Submit

Executes after the standard validation available through an application has completed. For more information, see Submit pipeline .

### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

### pageInteraction

The pageInteraction event handler executes immediately after an interaction with the form occurs, such as a blur or change event on a field.

#### Syntax

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



     eventHandlers[eventNames.PAGE_INTERACTION] = function() {

         console.log( "Inside PAGE_INTERACTION event handler" );

    };



     return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function(modelData, event)
```

The following table lists the input parameters:

Parameter

Description

modelData

An object containing the current information in the form.

event

An object of the form.

For more information, see Event on the MDN web site.

View sample event:

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

    type: <EVENT_TYPE> // EVENT_TYPE = { CHANGE: "change", SUBMIT: "submit" },

    payload: {

        fieldId: Number|String,

        htmlEvent: Event

    }

}
```

### validation

In the Change pipeline, validation failures stop the workflow from proceeding.

Validation failures do not carry over from the Change pipeline to the Submit pipeline, because it is possible that the Change validation would not fail on Submit/Save. Therefore, a fresh validation state is provided for each operation. For more information, see Submit pipeline .

#### Syntax

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

#### Parameters

Copy

```text
1
function(modelData, event, currentValidationState)
```

The following table lists the input parameters:

Parameter

Description

modelData

An object containing the current information in the form.

event

View the parameter for the Change pipeline:

For more information, see Event on the MDN web site.

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

    type: <EVENT_TYPE> // EVENT_TYPE = { CHANGE: "change", SUBMIT: "submit" },

    payload: {

        fieldId: Number|String,

        htmlEvent: Event

    }

}
```

View the parameter for the Submit pipeline:

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

    type: <EVENT_TYPE> // EVENT_TYPE = { CHANGE: "change", SUBMIT: "submit" },

    payload: {

        saveOperation: <SAVE_OPERATIONS>

    }

}
```

currentValidationState

An array containing objects of existing validation failures. The event handler appends to this array if it evaluates the form data as invalid. For sample code, see Validation example .

#### Validation example

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
function validationHandler(modelData, event, currentValidationState) {

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

On this page

- Change pipeline

- Change pipeline workflow

- Change pipeline event handlers

- Ambient variables

- pageInteraction

- validation


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
