---
title: "Load pipeline"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Load_pipeline.htm
collection: developer
fetched_at: 2026-06-22T06:31:54+00:00
sha256: ea5576be6e9864b3ea50774cb63995ec62f6437a82b286833876ab29725e60a6
---

Load pipeline Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Load pipeline

In the Relativity Forms API, the Load pipeline represents what happens during page loads. This includes full loads and partial reloads caused by layout or object switches. The Load pipeline offers the ability to customize and extend its behaviors by implementing any of the pipeline's event handlers within the JavaScript for your Relativity Forms Page Interaction event handler. For example, overriding the replaceGetNewObjectInstance event handler would allow the definition of default values for new object instances to display within a form.

## Load pipeline workflow

The Load pipeline represents how forms are rendered in the Relativity UI. The following diagram illustrates when specific event handlers are executed in this workflow, and the gray boxes indicate handlers which your JavaScript may implement.

Key for the diagram

- Async returns any time after hydrateLayout is fired and before pageLoadComplete is fired.

- For existing objects, replaceRead fires if registered. Otherwise, the object is read from the startup data.

- For new objects, replaceGetNewObjectInstance fires if registered. Otherwise, the object is read from the startup data.

- replaceObtainAdditionalData fires if registered. Otherwise, the Object Manager service obtains additional data for the relevant fields.

- Partial Loads occur when the Load Pipeline is executed due to switching layouts or navigating another object of the same type as what is currently being viewed, in the same form mode as the present form.

### Load pipeline event handlers

The following table lists each of the event handlers used in the Load pipeline.

Event handler

Description

eventHandlersRegistered

Executes immediately after the event handlers have been registered. It signifies the completion of registering ALL event handlers associated with the object, not just those pertaining to the load pipeline.

By default, RDOs served by forms are read by ObjectManager at the same time as event handler file names are gathered by the page’s load. .NET PreLoad event handlers fire at that point for existing objects, but PreLoad is not fired for NEW object creation.

https://help.relativity.com/LegalHold

front-end event handlers are gathered and registered upon full loads only. Partial loads occur due to page use, or a change of selected value in the layout dropdown. During a partial load, object data is read on page load, and .NET PreLoad event handlers are executed. The front-end eventHandlersRegistered is bypassed on partial loads, leading directly to a check of whether or not a replaceRead handler is implemented.

replaceRead

Retrieves object instance data containing form values to display for existing objects. Executes only if specified and only if the form mode is view or edit, bypassing the stock application object instance data retrieval.

replaceGetNewObjectInstance

Retrieves object instance data containing predefined form values to display for new objects. Executes only if specified and only if the form mode is added, bypassing the stock application object instance data retrieval.

transformLayout

Executes before the layout is hydrated. It provides an opportunity to modify the form layout before it is initialized.

hydrateLayout

Executes immediately before the application renders the form, and after the layout has been transformed.

hydrateLayoutComplete

Executes immediately after the application has rendered the form.

overridePickerDataSource

Provides an opportunity to override the data source for pop-up pickers for fields. For example, this could be used to display a filtered list of choices depending on a user's selection elsewhere in the layout. This event executes between the replaceFileActions and hydrateLayout events.

replaceFileActions

The replaceFileActions event handler allows alterations of the upload and download behaviors for File Fields via additional Field properties. This event executes between transformLayout (TRANSFORM_LAYOUT) and overridePickerDataSource (OVERRIDE_PICKER_DATASOURCE) events.

replaceObtainAdditionalData

Replaces the call to grab extra data for a set of fields. executes from the application's hydration logic (after hydrateLayout but finishes asynchronously from the rest of the pipeline and before pageLoadComplete) for fields that require options or item details to be shown beyond the values in the instance data.

postObtainAdditionalData

Executes after ALL additional data retrievals (including the ones from the replaceObtainAdditionalData event handlers) have completed. It always executes before pageLoadComplete executes.

createActionBar

Executes after the form is rendered. It is responsible for the creation of the action bar. This only executes on full page loads and not partial loads.

If you do not use convenienceApi.actionBar.createDefaultActionBar() to create the default action bar in this event handler, you must also specify an updateActionBar event handler, or updateActionBar will assume the default action bar exists, causing undefined behavior.

updateActionBar

Updates the action bar element on a page in response to a modified layout or instance. Any registered event handlers execute during object and layout switch, but not on full page loads.

createConsole

Creates a console panel in the view form and is applicable to View mode layouts only. This only executes on full page loads and not partial loads.

updateConsole

Updates the console element on a page in response to a modified layout or instance. Applicable to View mode layouts only. Any registered event handlers execute during object and layout switch, but not on full page loads.

pageLoadComplete

Executes only after all the other event handlers in the Load pipeline have executed and completed their execution (including all the asynchronous replaceObtainAdditionalData handlers if any were defined).

### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

### eventHandlersRegistered

Any registered eventHandlersRegistered event handlers execute before the selected form view-model is populated with the object instance data. It signifies the completion of registering ALL event handlers associated with the object, not just those pertaining to the load pipeline.

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

    var eventHandlers = {};



    eventHandlers[eventNames.EVENT_HANDLERS_REGISTERED] = function() {

        console.log("Inside EVENT_HANDLERS_REGISTERED event handler");

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

### replaceRead

The replaceRead event handler executes when the object instance data is ready to be retrieved for an existing object and a replaceRead event handler is registered for the object type. It retrieves the object instance data containing the form values to display.

This event handler is used only with existing objects when you are loading a form with a view or edit operation.

As it executes, the event handler performs the following operations:

- Makes the requests to the source providing the object instance data.

- Transforms the object instance data into the following entities:

- The form expected by the application

- The form compatible with the service that saves changes to the object instance. This service may be the replaceSave handler if defined, or the object instance service used by the application.

- Returns a promise that resolves to the transformed object data on a successful retrieval and rejects it on an unsuccessful retrieval.

Review the following guidelines for the replaceRead event handler and the related event:

- Only register a replaceRead event handler if the stock application object instance data retrieval isn't capable of retrieving the data to display in the form.

- A registered replaceRead event handler is invoked in place of the stock application object instance data retrieval.

- Register only one handler function for this event. If you register multiple functions, only the first function is invoked, and any others are ignored.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.REPLACE_READ] = function(

        workspaceId,

        artifactId,

        formViewModelTypeId

    ) {

        var data = {};

        return convenienceApi.promiseFactory.resolve({ modelData: data });

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Property

Type

Description

workspaceId

Number

The identifier of the workspace.

artifactId

Number

The identifier location of the artifact of the forms page.

formViewModelTypeId

Number

A number that maps FORM_VIEW_MODEL_TYPE from the convenienceApi.constants.

#### Returns

Type

Description

Promise<readData>

Returns a promise with a readData Object that represents what values fields contain.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.REPLACE_READ] = function(

        workspaceId,

        artifactId,

        formViewModelTypeId

    ) {

        var isViewMode = convenienceApi.constants.FORM_VIEW_MODEL_TYPE.VIEW === formViewModelTypeId;

        var readDataPromise;



        function someApiCall(workspaceId, artifactId) {

            return convenienceApi.promiseFactory.resolve({

                fieldIdForSomeTextField: "A value from an API call for " + artifactId

            });

        }



        if (isViewMode) {

            // Will receive object data from the someApiCall source

            readDataPromise = someApiCall(workspaceId, artifactId).then(function(objectData) {

                return { modelData: objectData };

            });

        } else {

            // In this example the edit form will always be populated with the following values for the fields.

            // This is just to demonstrate that the only requirement of a custom replace read event handler is that it must return a promise with a readData object

            var data = {

                fieldId1: "1",

                fieldId2: 2,

                fieldId3: true

            };

            readDataPromise = convenienceApi.promiseFactory.resolve({ modelData: data });

        }

        return readDataPromise;

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

### replaceGetNewObjectInstance

The replaceGetNewObjectInstance event handler creates a new object instance data containing predefined form values to display. For example, you would implement replaceGetNewObjectInstance to implement value defaulting in Relativity Forms.

This event handler is used with new objects when you are loading a form via an add operation.

As it executes, the event handler performs the following operations:

- Makes the requests to the source providing the object instance data.

- Transforms the object instance data into the following entities:

- The form expected by the application

- The form compatible with the service that saves changes to the object instance. This service may be the replaceSave handler if defined, or the object instance service used by the application.

- Returns a promise that resolves to the transformed new object data ready for the create form object on a successful retrieval and rejects it on an unsuccessful transformation.

Review the following guidelines for the replaceGetNewObjectInstance event handler and the related event:

- Only register a replaceGetNewObjectInstance event handler if the create form initial object data should be filled with specific values.

- A registered replaceGetNewObjectInstance event handler is invoked in place of the stock application object instance data retrieval for the create form object.

- Register only one handler function for this event. If you register multiple functions, only the first function is invoked, and any others are ignored.

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
(function(eventNames, convenienceApi) {

     var eventHandlers = {};



     eventHandlers[eventNames.REPLACE_GET_NEW_OBJECT_INSTANCE] = function() {

          console.log("Inside REPLACE_GET_NEW_OBJECT_INSTANCE event handler");

          var newObjectData = {};

          return newObjectData;

     };



     return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

### transformLayout

The transformLayout event handler executes before the layout is hydrated. It provides an opportunity to modify the form layout before it is initialized.

If a field is removed from the layout, the application does not know about the field. The field will not be rendered, and the application will not provide any value for that field on form submission.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

        console.log("Inside TRANSFORM_LAYOUT event handler");

        console.log(JSON.stringify(layoutData));

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function(layoutData)
```

The following table lists the input parameters:

Parameter

Description

layoutData

An object containing layout information. For more information, see Layout representation for Relativity forms .

### hydrateLayout

The hydrateLayout event handler executes after the object instance data has been retrieved and the layout data has been transformed, but before the application renders the form.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.HYDRATE_LAYOUT] = function(layoutData, objectInstanceData) {

        console.log("Inside HYDRATE_LAYOUT event handler");

        console.log(JSON.stringify(layoutData));

        console.log(JSON.stringify(objectInstanceData));

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function(layoutData, objectInstanceData)
```

The following table lists the input parameters:

Parameter

Description

layoutData

An object containing layout information. For more information, see Layout representation for Relativity forms .

objectInstanceData

An object containing the object instance data. It is similar to the modelData object in a readData Object , where the object's keys are fieldIds whose values are the fieldId's field values.

### hydrateLayoutComplete

The hydrateLayoutComplete event handler executes immediately after the application has rendered the form.

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

    var eventHandlers = {};



    eventHandlers[eventNames.HYDRATE_LAYOUT_COMPLETE] = function() {

        console.log("Inside HYDRATE_LAYOUT_COMPLETE event handler");

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

### overridePickerDataSource

The overridePickerDataSource event handler provides the opportunity to override the data source for pop-up pickers for fields.

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
eventHandlers[eventName.OVERRIDE_PICKER_DATASOURCE] = function(potentialPickerFields) {

    for (var i = 0; i < potentialPickerFields.length; i++) {

        potentialPickerFields[i].pickerDataSource = {

            customGetDataFunction: function() {

                return convenienceApi.promiseFactory.resolve({

                    TotalCount: 0,

                    Results: []

                });

            }

        }

    }

}
```

#### Parameters

Copy

```text
1
function(potentialPickerFields)
```

Parameter

Type

Description

potentialPickerFields

Array<Field>

A list of Field objects for which a picker could be shown. For example, if there is one single choice field and one multiple-choice field in the layout, there will be 2 fields in this list. To override the data source for any field, modify or replace its pickerDataSource property, which is a PickerDataSource object. The structure for this PickerDataSource object is shown below.

All object/choice/user field's in the layout will be in the list, regardless of the field displayed as a picker. This is because of the ChoiceLimitForUI instance setting. If the amount of available choices for a field exceeds ChoiceLimitForUI, the field will be shown in picker mode regardless of its setting in the layout.

#### The PickerDataSource object

Property

Type

Description

customItemListDataProvider

ItemListDataProvider

Optional. If set, this will replace the entire data provider for the field's picker. See ItemListDataProviders object for more information about creating a custom data provider.

If customItemListDataProvider is set, any other properties on the PickerDataSource object will be ignored.

customGetDataFunction

function(defaultGetDataFunction: function, request: Object, columns: Array<Object>): Promise<QueryResponse>

Optional. If set, this function replaces the default get data function for the field's picker.

##### Parameters

Parameter

Type

Description

defaultGetDataFunction

function(request: Object): Promise<Object>>

This function takes the same request parameter as the customGetDataFunction, and returns a promise containing the query results.

request

QueryRequest

A QueryRequest object describing what data to retrieve.

A list of columns that need data is not provided. To get a list of columns that need data, call this.getColumns() inside of customGetDataFunction. If a custom data provider was not defined, this.getColumns() will call the getColumns() function for the default data provider. For more information about getColumns(), see the ItemListDataProviders object interface.

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

eventHandlers[eventName.OVERRIDE_PICKER_DATASOURCE] = function(potentialPickerFields) {

    for (var i = 0; i < potentialPickerFields.length; i++) {

        potentialPickerFields[i].pickerDataSource = {

            customGetDataFunction: function(defaultGetDataFunction, request) {

                this.getColumns()

                    // This assumes transformColumnsToFieldNames is defined somewhere else

                    .then(transformColumnsToFieldNames)

                    .then(function(fieldNames) {

                        // This assumes that callSomeOtherApi is defined somewhere else

                        return callSomeOtherApi(request, fieldNames);

                    });

            }

        }

    }

}
```

##### Return value

Promise< QueryResponse >: A promise that resolves to an object containing the data to use to populate the rows and columns in the item list.

### Examples

#### Overriding the entire Data Provider

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
eventHandlers[eventName.OVERRIDE_PICKER_DATASOURCE] = function(fields) {

    for (var i = 0; i < fields.length; i++) {

        const field = fields[i];

        const MY_FIELD_ID = <field identifier of the field with the picker>;

        const ARTIFACT_TYPE_ID = <artifact type id of object type in the picker>;

        const VEIW_TO_DISPLAY = <artifact id of the view>;

        switch (field.FieldID) {

            case MY_FIELD_ID:

                const dataProviderOptions = {

                    fieldArtifactId: field.FieldID,

                    fieldName: field.DisplayName,

                    objectTypeId: ARTIFACT_TYPE_ID,

                    textIdentifierColumnName: "Name",

                    viewArtifactId: VEIW_TO_DISPLAY,

                    workspaceId: this.workspaceId

                };

                const dataProvider = convenienceApi.itemListDataProviderFactory.create("object", dataProviderOptions);



                field.pickerDataSource = {

                    customItemListDataProvider: dataProvider

                };

                break;

            default:

                break;

        }

    }

}
```

#### Customizing the stock Data Provider

##### Overriding the get data function

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
eventHandlers[eventName.OVERRIDE_PICKER_DATASOURCE] = function(fields) {

    for (var i = 0; i < fields.length; i++) {

        const field = fields[i];

const MY_FIELD_ID = <field identifier of the field with the picker>;

        switch (field.FieldID) {

            case MY_FIELD_ID:

                field.pickerDataSource = field.pickerDataSource || {}; // Preserve, possibly existing pickerDataSource object from the layout JSON.

                field.pickerDataSource.customGetDataFunction = loadMyFieldData;

                break;

            default:

                break;

        }

    }

}

function loadMyFieldData(defaultQuery, request, columns) {

    // ...

}
```

##### Overriding the getItemListMetadata function

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
eventHandlers[eventName.OVERRIDE_PICKER_DATASOURCE] = function(fields) {

    for (var i = 0; i < fields.length; i++) {

        const field = fields[i];

        const MY_FIELD_ID = <field identifier of the field with the picker>;

        switch (field.FieldID) {

            case MY_FIELD_ID:

                field.pickerDataSource = field.pickerDataSource || {};

                field.pickerDataSource.customGetItemListMetadataFunction = getItemListMetadataForMyField;

                break;

            default:

                break;

        }

    }

}



function getItemListMetadataForMyField(workspaceId, objectTypeId, viewArtifactId) {

    return makeApiCall() // This assumes makeApiCall() is defined somewhere else, and returns data in the correct form

        .then(function(dataFromApi) {

            // Make sure the data returned is in the proper format

            return {

                FieldCollection: dataFromApi.someProperty

                ViewFieldWidthCollection: dataFromApi.someOtherProperty,

                ActiveView: dataFromApi.anotherProperty

            }

        });

}
```

##### Specifying custom ItemListMetadata

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
eventHandlers[eventName.OVERRIDE_PICKER_DATASOURCE] = function(fields) {

    for (var i = 0; i < fields.length;i++) {

        const field = fields[i];

        const MY_FIELD_ID = <field identifier of the field with the picker>;

        switch (field.FieldID) {

            case MY_FIELD_ID :

                field.pickerDataSource = field.pickerDataSource || {};

                field.pickerDataSource.FieldCollection = [ /* ... */ ];

                field.pickerDataSource.ViewFieldWidthCollection = { /* ... */ };

                field.pickerDataSource.View = { /* ... */ };

                break;

            default:

                break;

        }

    }

}
```

### replaceFileActions

If a custom uploadFile method is defined for any field in a layout, a custom replaceSave method must also be defined. This replaceSave method should handle the persistence of the file field's data. If the built-in Relativity Forms save operation is called with the data from a file field with an overridden uploadFile handler, it will fail.

The replaceFileActions event handler allows alterations of the upload and download behaviors for File Fields via additional Field properties. This event executes between transformLayout (TRANSFORM_LAYOUT) and overridePickerDataSource (OVERRIDE_PICKER_DATASOURCE).

This event handler should set up and assign both an uploadFile function to override file upload behavior and a downloadFile function to override file download behavior.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.REPLACE_FILE_ACTIONS] = function(fileFields) {

        var fileField = !!fileFields && !!fileFields.length && fileFields[0];

        if (!!fileField) {

            fileField.uploadFile = myReplacementUploadHandler;

            fileField.downloadFile = myReplacementDownloadHandler;

        }

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function(fileFields)
```

The following table lists the input parameters:

Parameter

Description

fileFields

An Array of File Field objects present in the current layout.

For each File Field, two properties may be added - uploadFile and downloadFile.

Field Property

Description

uploadFile

#### Parameters

Copy

```text
1
function(workspaceId, artifactId, fieldId, file, backendProgressCallback, frontendProgressCallback, cancellationToken)
```

The following table lists the input parameters:

Parameter Type Description

workspaceId Number The ID of the Workspace in which the File Field and the Object to which it belongs reside.

artifactId Number

The Artifact ID of the Object to which the File Field belongs.

fieldId Number The Artifact ID of the File Field itself.

file File The File object containing the data to upload. See, https://developer.mozilla.org/en-US/docs/Web/API/File .

backendProgressCallback Function(payload: BackendProgressPayload): undefined

backendProgressCallback doesn’t need to be called. If backendProgressCallback is never called, the UI will just not display any status updates for backend progress until the file upload has completed.

A function that should be called when your file upload API has sent a status update. This function should be used if your API needs to do some sort of processing after the file has been uploaded, such as converting the file to a different format or compressing it. This function accepts a payload which should be used to indicate the status of the file upload. See the docs below for BackendProgressPayload for more information.

##### BackendProgressPayload

Property Type Description

Message BackendProgressMesssage A message indicating how much of the file upload has completed.

##### BackendProgressMessage

Property Type Description

CompletedSteps Number The number of steps that have been completed so far. This must not be greater than TotalSteps.

TotalSteps Number The total number of steps required to complete the upload.

##### Sample Usage

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
function onProgressUpdate(progressInfo) {

    backendProgressCallback({

        Message: {

            CompletedSteps: progressInfo.percentComplete,

            TotalSteps: 100

        }

    });

}

yourApi.uploadFile(file, ..., onProgressUpdate, ...);
```

frontendProgressCallback Function(event: ProgressEvent | Object) : undefined

frontendProgressCallback doesn't need to be called. If frontendProgressCallback is never called, the UI will not display any status updates for front end progress until the file upload has completed.

A function that should be called when the browser sends a status update on the progress of the upload. If you're using the native XMLHttpRequest API, you can listen for browser status updates, via XMLHttpRequestEventTarget.onprogress. If you're not using XMLHttpRequest, make sure the event you pass in has a 'loaded' and 'total' property that conforms to the ProgressEvent spec. Most HTTP clients support something similar.

##### Sample Usage (XMLHttpRequest)

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
var request = new XMLHttpRequest();

var method = 'POST';

var url = 'https://some.url/and/some/route/';

var async = true;

request.open(method, url, async);

request.onprogress = function (event) {

    frontendProgressCallback(event);

};

request.send(file);
```

##### Sample Usage (custom http client)

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
var requestOptions = {

    onBrowserUploadProgress = function(percentComplete) {

        frontEndProgressCallback({

            loaded: percentComplete,

            total: 100

        });

    }

};

yourApi.uploadFile(file, ..., requestOptions, ...);
```

cancellationToken CancellationToken

A token that can be used by Relativity Forms to cancel this upload. If you need to do something if an upload is canceled, you will need to use this token. This token contains a _promise property that will be rejected if the upload should be canceled. Chain a .catch off this promise to detect when the upload has been canceled.

##### Example

Copy

```text
1
2
3
4
startUpload();

cancellationToken._promise.catch(function() {

    cancelUpload();

});
```

#### Returns

Type

Description

Promise<Object>

A promise that resolves when the file upload has completed. When this promise resolves, the UI will update to indicate that the upload is complete.

This promise should resolve to an Object containing a Filename property. A FileID and/or UploadedFileGuid property may also be included, but neither is required.

Property

Type

Description

Filename

String

The name of the file. This will be displayed immediately on the UI after the promise resolves. This will be provided in the field's value during replaceSave as 'fileName'.

This does not have to match the name property on the File object passed into the uploadFile function by Relativity Forms.

FileID

Number

Optional: A numeric identifier that can be used to look up the file. This will be provided in the field's value during replaceSave as fileId .

UploadedFileGuid

String

Optional : A Guid that can be used to look up the file. This will be provided in the field's value during replaceSave as uploadedFileGuid .

#### Example

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
const FILE_FIELD_ID = 1234 // Replace with the ID of your file field

eventHandlers[eventNames.REPLACE_FILE_ACTIONS] = function(fileFields) {

    fileFields[0].uploadFile = function (workspaceId, artifactId, fieldId, file, backendProgressCallback, frontendProgressCallback, cancellationToken) {

        return convenienceApi.promiseFactory.resolve({Filename: "SomeFileName.some.extension"});

    };

};

// Don't forget to override replace save as the default Relativity Forms save operation will fail if you've defined a custom uploadFile handler

eventHandlers[eventNames.REPLACE_SAVE] = function(objectInstanceData, objectVersionToken) {

    var fileFieldValue = objectInstanceData[FILE_FIELD_ID];

    var transformedData = transformData(objectInstanceData);

    transformedData[FILE_FIELD_ID] = {

        name: fileFieldValue.fileName,

        id: fileFieldValue.fileId,

        guid: fileFieldValue.uploadedFileGuid

    };

    yourApi.saveObject(transformedData);

}
```

downloadFile

#### Parameters

Copy

```text
1
function(workspaceId, artifactId, fieldId, fileName)
```

The following table lists the input parameters:

Parameter

Type

Description

workspaceId

Number

The ID of the Workspace in which the File Field and the Object to which it belongs reside.

artifactId

Number

The Artifact ID of the Object to which the File Field belongs.

fieldId

Number

The Artifact ID of the File Field itself.

fileName

String

The name of the file to be retrieved.

#### Returns

Type Description

Promise<File>

A Promise that resolves to a new File object containing the file's data. See https://developer.mozilla.org/en-US/docs/Web/API/File for more information.

Regardless of the name given to the File object returned, Relativity Forms will rename the file to match the value of the fileName parameter that Relativity Forms passed into downloadFile().

#### Example

Copy

```text
1
2
3
4
5
eventHandlers[eventNames.REPLACE_FILE_ACTIONS] = function(fileFields) {

    fileFields[0].downloadFile = function(workspaceId, artifactId, fieldId, fileName) {

        return convenienceApi.promiseFactory.resolve(new File(["SomeFileContents"], fileName));

    };

};
```

### replaceObtainAdditionalData

Replaces the call to grab extra data for a set of fields. executes from the application's hydration logic (after hydrateLayout but finishes asynchronously from the rest of the pipeline and before pageLoadComplete) for fields that require options or item details to be shown beyond the values in the instance data.

The following can be overridden by this event handler

Fields

- Single Choice

- Multiple Choice

- Single Object

- User

Field Display Types

- Drop-downs

- Lists

The pageLoadComplete event handler only executes after ALL additional data retrievals (including the ones from the replaceObtainAdditionalData event handlers) have completed (and the rest of the pipeline has finished).

#### Example

This example demonstrates the use of convenienceApi.additionalData.getDefaultFactoriesForAdditionalData to override the additional data for just one field.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.REPLACE_OBTAIN_ADDITIONAL_DATA] = function(

        fieldsRequiringAdditionalData,

        workspaceId,

        viewModelName

    ) {

        // Get all the default additional data factories

        // If we return this value without modifying it, the default behavior will be maintained.

        var additionalDataFactories = convenienceApi.additionalData.getDefaultFactoriesForAdditionalData(workspaceId, fieldsRequiringAdditionalData);



        // Override just the factory for the field we're interested in

        // Let's just pretend it's the first factory in the array to make things simpler

        var someFactoryIWantToOverride = additionalDataFactories[0];

        someFactoryIWantToOverride.createAdditionalDataPromise = function() {

            return someApi.getAdditionalData(

                workspaceId,

                someFactoryIWantToOverride.field,

                viewModelName

            );

        };



        return additionalDataFactories;

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function(fieldsRequiringAdditionalData, workspaceId, viewModelName)
```

The following table lists the input parameters:

Parameter

Type

Description

fieldsRequiringAdditionalData

Array<Field>

An array of Fields requiring additional data to load.

workspaceId

Number

The integer identifier of the workspace where the object type displayed in this form exists.

viewModelName

String

The text-based name of the view-model. It is used for the name property in the routing config for a specific route.

#### Output

Sample Output

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
[

    {

        field: fieldsRequiringAdditionalData[0],

        createAdditionalDataPromise: function () {

            // Get additional data for field 0

            convenienceApi.promiseFactory.resolve({

                options: [

                    {

                        label: "Option 1",

                        value: 1001234,

                        order: 10

                    },

                    {

                        label: "Option 2",

                        value: 1004567,

                        order: 0

                    },

                    ...

                ],

                limitForUIExceeded: false

            });

        }

    },

    {

        field: fieldsRequiringAdditionalData[1]

        createAdditionalDataPromise: getAdditionalDataForField1

    },

    ...

]
```

Expected output format:

Type

Description

Array<Object>

Array of objects containing Field ↔ Function pairs that contain instructions for fetching additional data for the given field.

Property

Type

Description

field Field The Field to get additional data for

createAdditionalDataPromise Function: Promise<AdditionalData>

A function that returns a promise that resolves to an AdditionalData object containing information about what data to set for the field.

##### The AdditionalData object

The return value of the AdditionalData object can be either an Array<Option>, or an Object containing an options property and a limitForUIExceeded property. The limitForUIExceeded property can be used to override the default behavior for determining whether or not to display a popup picker for a given field.

##### If AdditionalData is an Array<Option>

If an array is returned, it is expected to contain 0 or more Option objects. See the documentation for the 'Option' object below.

If the number of options returned exceeds the value of the ChoiceLimitForUI instance setting, the value of this array will be ignored, and a popup picker will be used for this field instead.

##### If AdditionalData is an Object

If an object is returned, the value of the ChoiceLimitForUI instance setting will be ignored, and the provided limitForUIExceeded will be used instead.

Property

Type

Description

options Array<Option>

An array of Option objects that will be used to populate the available options for the field to be replaced. See the documentation for the 'Option' object below.

limitForUIExceeded Boolean

If true, this tells Relativity Forms that there are too many choices to easily display inline, so Relativity Forms should use a popup picker instead, regardless of which 'DisplayType' is set for this field. If false, Relativity Forms will not display a popup picker for this field.

If limitForUIExceeded is set to true, the options provided via the 'options' property will be ignored, and the popup picker's default data source will be used to fetch a list of options. If you want to override the behavior of a popup picker, implement an overridePickerDataSource event handler.

##### The Option Object

Property Type Description

label String The display name of the choice to be shown in the UI. This is not used during save, and thus can be whatever you'd like.

value Number | String The value that should be saved to the database when saving this field. For more information about possible values of fields, see the Field Value section of the Additional Forms API Object page.

order Number Optional. The order to display choices in. Lower numbers indicate that the choices should be shown more prominently, such as at the top of a dropdown. Items with the same 'order' value will be shown in alphanumeric order.

### postObtainAdditionalData

A registered postObtainAdditionalData event handler executes:

- when it is defined.

- after ALL additional data retrievals (including the ones from the replaceObtainAdditionalData event handlers) have completed (pageLoadComplete will not happen until this condition is met).

- before the pageLoadComplete event handler executes.

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

    var eventHandlers = {};



    eventHandlers[eventNames.POST_OBTAIN_ADDITIONAL_DATA] = function() {

        console.log("Inside POST_OBTAIN_ADDITIONAL_DATA event handler");

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

### createActionBar

A registered createActionBar event handler executes after the form is rendered. It creates an action bar.

If you do not use convenienceApi.actionBar.createDefaultActionBar() to create the default action bar in this event handler, you must also specify an updateActionBar event handler, or updateActionBar will assume the default action bar exists, causing undefined behavior.

#### Example

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};





    eventHandlers[eventNames.CREATE_ACTION_BAR] = function() {

        console.log("Inside CREATE_ACTION_BAR event handler");

        convenienceApi.actionBar.createDefaultActionBar(); // create default action bar





        var button = document.createElement("button");

        button.id = "testButton";

        button.textContent = "Test Button";

        return convenienceApi.actionBar.containersPromise.then(function(containers) {

            containers.rootElement.appendChild(button); // add an extra button to the action bar

        });

    };





    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

#### Returns

Type

Description

Promise<undefined>

Returns a promise that resolves when elements are finished being added to the action bar.

### updateActionBar

An updateActionBar event handler updates the action bar element on a page in response to a modified layout or instance. Any registered event handlers execute during object and layout switch.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};





    eventHandlers[eventNames.UPDATE_ACTION_BAR] = function() {

        console.log("Inside UPDATE_ACTION_BAR event handler");





        var button = document.getElementById("testButton"); // update the text of the extra button added in CREATE_ACTION_BAR

        button.textContent = "Updated Button";

    };





    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

#### Returns

Type

Description

Promise<undefined>

Returns a promise that resolves when elements are finished being updated on the action bar.

### CreateConsole

The createConsole event handler creates the console panel in the View form. As it executes, the event handler performs the following operations for View mode layouts only:

- Adds controls to console.

- Sets up the handler function invoked when the user interacts with a control.

The Console object is available on the Relativity Event Handler API. For more information, see Event Handlers API on the Relativity API Reference page.

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};





    eventHandlers[eventNames.CREATE_CONSOLE] = function() {

        console.log( "Inside CREATE_CONSOLE event handler" );





        var button = document.createElement("button"); // add a button to the console

        button.id = "testConsoleButton";

        button.textContent = "Test Button";

        return convenienceApi.console.containersPromise.then(function(containers) {

            containers.rootElement.appendChild(button);

        });

    };





    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

#### Returns

Type

Description

Promise<undefined>

Returns a promise that resolves when elements are finished being added to the console area.

### updateConsole

An updateConsole event handler updates the console element on a page in response to a modified layout or instance. Any registered event handlers execute during object and layout switch. This event handler is used only for view mode layouts.

#### Example

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
(function(eventNames, convenienceApi) {

    var eventHandlers = {};





    eventHandlers[eventNames.UPDATE_CONSOLE] = function() {

        console.log( "Inside UPDATE_CONSOLE event handler" );





        var button = document.getElementById("testConsoleButton"); // update the text of the extra button added in CREATE_CONSOLE

        button.textContent = "Updated Button";

    };





    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

#### Returns

Type

Description

Promise<undefined>

Returns a promise that resolves when elements are finished being updated on the console.

### pageLoadComplete

A registered pageLoadComplete event handler executes only after all the other event handlers in the Load pipeline have executed and completed their execution. It will also wait until ALL additional data retrievals (including the ones from the replaceObtainAdditionalData event handlers) have completed before firing. It is the final event handler to execute in the Load pipeline.

#### Example

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



    eventHandlers[eventNames.PAGE_LOAD_COMPLETE] = function() {

        console.log("Inside PAGE_LOAD_COMPLETE event handler");

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

#### Parameters

Copy

```text
1
function()
```

On this page

- Load pipeline

- Load pipeline workflow

- Load pipeline event handlers

- Ambient variables

- eventHandlersRegistered

- replaceRead

- replaceGetNewObjectInstance

- transformLayout

- hydrateLayout

- hydrateLayoutComplete

- overridePickerDataSource

- Examples

- replaceFileActions

- replaceObtainAdditionalData

- postObtainAdditionalData

- createActionBar

- updateActionBar

- CreateConsole

- updateConsole

- pageLoadComplete


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
