---
title: "Delete pipeline"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Delete_pipeline.htm
collection: developer
fetched_at: 2026-06-22T06:31:59+00:00
sha256: 89960337887eb304711d602c8a271f5a4abdbe779d464203ddde935813ad8f8b
---

Delete pipeline Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Delete pipeline

The Delete pipeline includes event handlers that control the process for removing objects from Relativity. It contains an event handler that retrieves a list of objects dependent on the item or items selected for deletion. In addition, it provides you with the option to implement an event handler with custom logic for deletion, or to use the standard event handler for this operation provided in Relativity. For example, you might want to implement a custom event handler that adds additional items to the delete dependency list of the selected items to be deleted.

The Delete pipeline initiates when any of the following actions take place:

- When deleting from a form in the main window.

- When deleting from an item list in the form.

- When deleting from a form in a pop-up.

## Delete pipeline workflow

The Delete pipeline represents the process for removing objects from Relativity. The following diagram illustrates when specific event handlers in this workflow are executed. For more information about deleting objects, see Object Manager API .

### Delete pipeline event handlers

The following table lists each of the event handlers used in the Delete pipeline.

Event handler

Execution pipeline

Description

replaceReadDeleteDependencyList

Delete

Executes after all the event handlers in the Delete pipeline are registered. This event handler is invoked in place of the event handler in the stock application used for retrieving a delete dependency list.

preDelete

Delete

Executes for the deletion of the current object and for the deletion of objects in an item list.

replaceDelete

Delete

Executes after the preDelete event handler has finished executing. This event handler is invoked in place of the event handler in the stock application for deleting an object instance.

postDelete

Delete

Executes after the delete event handler in the stock application, or the replaceDelete event handler finishes executing.

### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

### replaceReadDeleteDependencyList

The replaceReadDeleteDependencyList event handler executes after deletion is requested before the deletion confirmation dialog is shown. It is used to control what information is given to the confirmation dialog in place of the stock application for all deletions, both mass and single. All of the objects are expected to be of the same artifactTypeId, which may not be the same type as the active object in the layout.

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



     eventHandlers[eventNames.REPLACE_READ_DELETE_DEPENDENCY_LIST] = function(workspaceId, artifactTypeId, artifactIds) {

         console.log("Inside REPLACE_READ_DELETE_DEPENDENCY_LIST event handler");



         return [{

            ObjectType: "OBJECT TYPE 1",

            Action: "ACTION 1",

            Count: 1,

            Connection: "CONNECTION 1",

            SecuredItems: []

        }, {

            ObjectType: "OBJECT TYPE 2",

            Action: "ACTION 2",

            Count: 2,

            Connection: "CONNECTION 2",

            SecuredItems: []

        }];

     };



     return eventHandlers;

 }(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
   function(workspaceId, artifactTypeId, artifactIds)
```

The following table lists the input parameters:

Parameter

Description

workspaceId

A number representing the ID of the workspace where the object to be deleted resides.

artifactTypeId

A number representing the type ID of the object to be deleted.

artifactIds

A number or array of numbers (Array<Number>) representing the ID or IDs of the objects to be deleted.

#### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

#### Return Type

Array<DependencyObject>

An error or warning is only displayed when more than one DependencyObject is returned.

##### DependencyObject

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

     ObjectType: String,         // the object type of this dependency

     Action: String,             // the action of this dependency

     Count: Number,              // the count of this dependency type

     Connection: String,         // the connection of this dependency

     SecuredItems: Array<String> // optional, a list of secured items - if set with at least one item then an error is shown, otherwise a warning is shown

}
```

###### Example Warning Message Output - no secured items

The application displays this warning after clicking Delete when there are no secured items defined in any DependencyObject:

###### Example Error Message Output - at least one secured item

The application displays this error after clicking Delete when there is at least one secured item defined in a DependencyObject:

Copy

```text
1
2
3
4
{

     // ...

     SecuredItems: ["This will trigger an error instead of a warning"]

}
```

### preDelete

The preDelete event handler executes after a deletion modal for the selected objects is confirmed. This event handler is executed before, if defined, the replaceDelete event handler is executed. Otherwise, it is executed before the stock delete application is executed.

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.PRE_DELETE] = function(modelData) {

          console.log( "Inside PRE_DELETE event handler" );

     };

     return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
   function(modelData)
```

##### modelData

An object containing the information about an object (or objects) to be deleted.

Copy

```text
1
2
3
4
5
{

    artifactIds: Array<Number>|Number,        // artifact identifiers to delete

    artifactTypeId: Number,                  // artifact type identifier of object to be deleted

    workspaceId: Number                     // workspace identifier

}
```

### replaceDelete

The replaceDelete event handler executes after the preDelete event handler has finished executing. This event handler is invoked in place of the event handler in the stock application for deleting an object instance. It is used to replace the behavior for the deletion of the current object or objects in an item list. This event handler expects a return value in the form of a Promise. The workspaceId, artifactTypeId, and artifactIds can be used to determine which items should be deleted. For more information on making deletion requests, see convenienceApi.relativityHttpClient .

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};

    eventHandlers[eventNames.REPLACE_DELETE] = function(workspaceId, artifactTypeId, artifactIds, progressCallback, cancellationToken) {

        console.log( "Inside REPLACE_DELETE event handler." );

        return convenienceApi.relativityHttpClient.delete(/*  Your delete API's URL  */);

    };

    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
   function(workspaceId, artifactTypeId, artifactIds, progressCallback, cancellationToken)
```

The following table lists the input parameters:

Parameter

Description

workspaceId

A number representing the ID of the workspace where the object to be deleted resides.

artifactTypeId

A number representing the type ID of the object to be deleted.

artifactIds

A number or array of numbers (Array<Number>) representing the ID or IDs of the objects to be deleted.

progressCallback

A callback function invoked when progress occurs within a long-running deletion.

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

    Message: {

        OperationsCompleted: Number,        //Number indicating progress. Should normally be in between 0 and TotalOperations.

        CompletedSteps: Number,             //Number indicating progress. Not necessary if OperationsCompleted is provided. Should normally be in between 0 and TotalSteps.

        TotalOperations: Number,                //Number indicating total number of operations.

        TotalSteps: Number,                 //Number indicating total number of steps. Not necessary if TotalOperations is provided.

        Message: String                     //Message to display on the modal.

    }

}
```

cancellationToken

An object representing a token used to cancel the delete operation. In Relativity, the delete operation may forced to halt, but the system doesn't roll-back any partially executed deletion.

Copy

```text
1
2
3
{

    cancel: Function    //Function used to cancel the operation. This function can be overridden.

}
```

### postDelete

The postDelete event handler executes after the delete event handler in the stock application, or the replaceDelete event handler finishes executing. This can be used for any clean-up work needed following the deletion of one or more objects. The postDelete event handler is used for both singular and mass events, and the type of object being may be different from the type of the active object.

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};

     eventHandlers[eventNames.POST_DELETE] = function(modelData) {

          console.log( "Inside the POST_DELETE event handler." );

     };

     return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
  function(modelData)
```

##### modelData

An object containing the information about an object (or objects) to be deleted.

Copy

```text
1
2
3
4
5
{

    artifactIds: Array<Number>|Number,        // artifact identifiers to delete

    artifactTypeId: Number,                  // artifact type identifier of object to be deleted

    workspaceId: Number                     // workspace identifier

}
```

On this page

- Delete pipeline

- Delete pipeline workflow

- Delete pipeline event handlers

- Ambient variables

- replaceReadDeleteDependencyList

- preDelete

- replaceDelete

- postDelete


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
