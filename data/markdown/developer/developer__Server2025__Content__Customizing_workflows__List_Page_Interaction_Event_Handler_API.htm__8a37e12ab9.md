---
title: "List Page Interaction Event Handler API"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/List_Page_Interaction_Event_Handler_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:28+00:00
sha256: aee776eed654ff5cad60f45f5ea72e103d56d58c47338ddb8188750fef2065c4
---

List Page Interaction Event Handler API

# List Page Interaction Event Handler API

Due to the migration of Relativity.ListPage to Relativity.Lists , you may need to migrate List Page Interaction Event Handlers that use a JavaScript code file to call the JavaScript APIs, to use the new file format and APIs. See this post in the developer group for more information.

The List Page Interaction Event Handler API consists of several JavaScript APIs used to customize the behavior and content of list pages in Relativity. When implementing a List Page Interaction event handler, you can write custom JavaScript code that uses these APIs. They provide you with the ability to access the internal functionality of a list page, and to interact with a Relativity application. For example, the New Item Button API supports customizations to the new item button on a list page, while the Events API provides a service for sending and receiving messages.

See these related pages:

- List Page Interaction event handlers

- Page Interaction event handlers

## JavaScript structure for event handlers

Review the following guidelines for structuring your JavaScript code used with List Page Interaction event handlers:

- Implement your custom JavaScript code as an asynchronous module definition (AMD).

- Use the define() function as illustrated in Initializer API details , and pass a factory function to it.

- Note that the factory function should return a pointer on the initializer() function.

For sample code, see Initializer API details .

## Summary of JavaScript APIs

The following tables briefly described the JavaScript APIs supported by the List Page Interaction event handlers.

### Initializer API

The Initializer API contains the initializer() function used to perform any custom initialization steps that you might define, and to initialize objects available through the General APIs. See Initializer API details .

### Event-specific APIs

The event-specific APIs support the interaction of event handlers with specific list pages in a Relativity application. These APIs are passed to a registered event handler. For more information, see Event-specific API details .

The following table lists each of the event-specific APIs.

API name Event API description

Page Navigation API listPageChange(pageNavigationAPI) Contains an event that is fired during the navigation of an item list on a page. It includes a service object called pageApi, which is passed to the listPageChange() function.

New Item Button API newItemButtonInit(buttonAPI) Contains an event used to customize the title and behavior of the new item button. It includes a service object called buttonAPI, which passed to the newItemButtonInit() function.

Cell Formatter API cellFormattersInit(cellFormatterApi) Contains an event used to set a custom format for any field. It includes a service object called cellFormatterApi, which is passed to the cellFormattersInit() function.

Data Source Override API dataSourceInit(dataSourceAPI) Contains an event for overriding a default data source used by item list and Pivot widgets. It includes a service object called dataSourceAPI, which is passed to the dataSourceInit() function.

View API viewChange(viewChangeAPI) Contains an event used to monitor changes in the active view or browser. It includes a service object called viewChangeAPI, which is passed to the viewChange() function.

Widget Menu Customization API widgetMenuCreate(widgetMenuAPI) Contains an event used to examine and modify menu items for a widget. It includes a service object called widgetMenuAPI, which is passed to the widgetMenuCreate() function.

### General APIs

The general APIs are available to event handlers when the api object is passed as a parameter to a top-level function. These APIs provide services that you can use to customize the behavior and UI for list pages. For more information, see General APIs details .

The following table lists each of the general APIs.

API name Service name API description

Promise API api.promise Used for working with JavaScript promises.

Events API api.eventService Supports sending and receiving messages.

Kepler Provider API api.keplerProviderService Exposes APIs for executing Relativity service requests.

Common Utilities API api.commonUtilities Provides event handlers with access to common utilities services for list pages.

Modal API api.modalService Opens a modal window populated with custom contents.

Toolbar API api.toolbarService Used to show and hide toolbars with custom content and buttons.

CustomWidget API api.customWidgetService Creates a dashboard widget populated with custom contents.

## Initializer API details

The Initializer API contains the initializer() function, which takes a single argument, such as the api object, used to access services available in the general APIs. This function returns a object. For more information, see JavaScript structure for event handlers and General APIs details .

The names of the object properties should match the names of the events in the list of Event-specific APIs . Additionally, each property should refer to the implementation of an event handler.

View an example of an event handler module Copy

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
// EventHandler module declaration

define(function handlerFactory() {

  // Illustrates the main EventHandler function initializer. It takes an  api parameter.

  function initializer(api) {

    // Specify a handler for the page change event. It takes pageApi parameter.

    function handlePageChange(pageApi) {

      var info = pageApi.getNavigationInfo();

      if (info.newStart > 100) {

        pageApi.abortNavigation("Can't go that far");

      }

    }

    // Perform any initialization here.

    // Illustrates the main function, which should return an object describing any events of interest.

    return {

      // Set a handler for a page change event.

      listPageChange: handlePageChange

    };

  }

  // Return the main EventHandler function.

  return initializer;

});
```

## Event-specific API details

The event-specific APIs support the interaction of event handlers with specific list pages in a Relativity application. These APIs are passed to a registered event handler. They can only be used only during the event handler execution.

### Page Navigation API

The Page Navigation API includes functionality used by an event handler to monitor changes to an item list page. The event handler can also use this functionality to prevent page changes if necessary, since an event is fired when the user navigates to another page. The Page Navigation API includes the a service object called pageApi, which is passed to the listPageChange() function.

#### Methods

Name Parameter Return value Description

pageApi.getNavigationInfo() None navigation info object Returns an object describing the current navigation event.

pageApi.abortNavigation(message) message - a string displayed to the user. None Cancels the current navigation and displays an error message.

#### navigation info object properties

Property Type Description Required

operation string Represents the current page operation:

- "first" - indicates that the user is navigating to the first page.

- "previous" - indicates that the user is navigating to the previous page.

- "next" - indicates that the user is navigating to the next page.

- "last" - indicates that the user is navigating to the last page.

- "text" - indicates that the user is navigating to the page containing a newStart item.

- "pagesize" - indicates that the user is changing the page size to the newPageSize for the number of items.

Yes

pageSize number Indicates the current page size. Yes

newPageSize number Indicates the new page size. Yes - only required when the operation is "pagesize".

start number Indicates the current number for the first item on the page. Yes

newStart number Indicates a new number for the first item on the page. Yes

View page navigation example Copy

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
describe(function() {

  function sampleHandler(api) {

    // Ilustrates a function that handles page change events. Takes the Page Navigation API as a parameter.

    function handlePageChange(pageApi) {

      // Request the current page navigation information.

      var info = pageApi.getNavigationInfo();

      // Prevents a page change when attempting to go beyond the first 100 items.

      if (info.newStart > 100) {

        pageApi.abortNavigation("Can't go that far!");

      }

    }

    return {

      // Subscribes to the "listPageChange" event.

      listPageChange: handlePageChange

    };

  }

  return sampleHandler;

});
```

### New Item Button API

The New Item Button API includes functionality used by an event handler to customize the new item button at the top of a list page. This event only occurs once during the start up of the list page. The service object called buttonAPI is passed to the newItemButtonInit() function.

#### Methods

Name Parameter Return value Description

buttonApi.getButtons() none array Returns an array of button objects. For more information, see Button object properties .

buttonApi.setButton(button) button - an object describing the new item button. None Adds or replaces the new item button. The button object describes the new button used for this purpose.

buttonApi.setButtons(buttons) buttons - an array of objects describing the buttons. None Adds or replaces the new item button with a drop-down button. The buttons array describes this drop-down button.

#### Button object properties

Property Type Description Example

text string Represents the button title. "Create new project"

eventName string Represents the name of an event emitted when a button is clicked. "rlh_create_project_click"

eventArgs any Represents any data passed along with an event object. (void 0)

View new item button example Copy

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
describe(function() {

  function sampleHandler(api) {

    // Illustrates aA function that handles page change events. It takes the Page Navigation API as a parameter.

    function handleNewItemButtomCustomizeEvent(buttonApi) {

      buttonApi.setButton({

        text: "Open my custom modal",

        eventName: "show_my_modal"

      });

    }

    return {

      // Subscribe to the "newItemButtonInit" event.

      newItemButtonInit: handleNewItemButtomCustomizeEvent

    };

  }

  return sampleHandler;

});
```

### Cell Formatter API

Use the Cell Formatter API to customize the cell for any field by setting a custom formatter. The cell formatter initialization event only occurs during the initialization of the item list before the grid columns are constructed. The service object called formatterApi is passed to an cellFormattersInit() function. You can register any custom formatter for any item list column. However, only one formatter can be registered per column.

#### Methods

Name Parameter Return value Description

formatterApi.fields None array of fields Returns an array of fields.

formatterApi.setFormatter(columnName, formatter) columnName - the name of the column to format.

formatter - the formatter function. None Sets a formatter for the provided column name. The formatter function should return a string. See Custom formatter function parameters .

View an example of the cell formatter function Copy

```text
1
2
3
formatterApi.setFormatter("columnName", function (defaultValue, columnOptions, rowData, api) {

  return api.getCellData(defaultValue);

}
```

#### Custom formatter function parameters

The following table includes the type and description of the parameters for the formatter function.

Parameter Type Description

defaultValue any Specifies a cell value.

columnOptions object Represents an object with the properties of a column. See View an example showing how to format columns .

rowData object Represents the key/value collection object for row data. For more information, see itemListDataSourceParams object .

api object Represents the Helper api. For more information, see Helper API methods .

View an example showing how to format columns Copy

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
{

    // Value alignment

       align:"left",

    // Current column name

       columnName:"File Type",

    // Column display name

    friendlyLabelName:"File Type",

    // Indicates whether the column is visible.

       hidden:false,

    // Indicates whether the column label is hidden.

       hideColumnLabel:false,

    // Default column width

       initialWidth:150,

    // Indicates whether the column is a key column.

       key:false,

    // Full name of the column

       label:"File Type",

    // Column width

       minWidth:75,

    // Indicates whether the column is sortable.

       sortable:true,

    // Column width

       width:194,

    // Indicates whether the column can wrap.

       wrapping:true,

}
```

#### Helper API methods

The Helper API methods are passed as an api parameter to the formatter function. See Custom formatter function parameters .

Name Parameter Return value Description

getCellData(defaultValue) defaultValue - any value. A data (or value) in a cell, such as a string for a text field, an array of objects for a multiple choice field, and so on. Returns a cell value. If the value is null, it returns the defaultValue.

A returned string can be malicious HTML, such as '<script>alert("hacked");</script>'. Since the formatter function returns HTML, you can sanitize any string data that is returned with escapeString or other custom solution for this purpose.

getOnClickForModal(modalId) modalId - the identifier for a modal to display. A string (onclick="<js code>") that can be added inside an <a> element. This link opens a created modal when it is clicked. Generates an onclick string for the anchor element. These strings can be added as an attribute of the anchor element. The modalId parameter is the return value of modalService.createModal.

escapeString(str) str - a string. An escaped string Escapes a string that was passed to the method.

View cell formatter example Copy

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
define(function() {

     "use strict";

     function testHandler(api) {

          var api = api;

          // FORMATTING TEXT EXAMPLE

          function subjectFormatter(cellValue, options, rowObject, formatterApi) {

               var data,

                    resultHtml;

               data = formatterApi.getCellData(cellValue) || "";

               data = formatterApi.escapeString(data);

               if (options.colModel.gridFormatter.isLinked) {

                    resultHtml = "<a target='_top' href='"+rowObject["viewUrl"]+"'>Name: "+data+"</a>"

               } else {

                    resultHtml = "Name: "+data;

               }

               resultHtml = "<span style='color: #0b3e6f'>"+resultHtml+"</span><hr><span>Another Line</span>";

               return resultHtml;

          }

          // OPEN MODAL EXAMPLE

          function authorFormatter(cellValue, options, rowObject, formatterApi) {

               var valueText, resultHtml, modalId, modalContent;

               valueText = formatterApi.getCellData(cellValue) || "";

                   valueText = formatterApi.escapeString(valueText);

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

                    return field.displayName === "Subject";

               });

               if (fieldSubject) {

                    formatterApi.setFormatter(fieldSubject.columnName, subjectFormatter);

               }

               fieldAuthor = formatterApi.fields.find(function (field) {

                    return field.columnName === "1001306";

               });

               if (fieldAuthor) {

                    formatterApi.setFormatter(fieldAuthor.columnName, authorFormatter);

               }

          }

          return {

               cellFormattersInit: cellFormattersInit

          };

     }

     return testHandler;

});
```

### Data Source Override API

The Data Source Override API includes functionality used by event handlers to override a default data source for item list and Pivot widgets. This event only occurs once during the start up of the list page. The event handler needs to subscribe to the dataSourceInit event and use the overrideApi to set up a custom data source.

This section contains the following information:

- Methods for the Data Source Override API

- Override an ItemList data source

- itemListDataSourceParams object

- Override a Pivot data source

- Override an ObjectField data source

#### Methods for the Data Source Override API

Name Parameter Return value Description

overrideApi.setItemListDataSource(dataSourceFactory) dataSourceFactory - a factory function for the construction of an ItemList data source. None Sets a custom data source factory function for a ItemList widget.

overrideApi.setPivotDataSource(dataSourceFactory) dataSourceFactory - a factory function for the construction of a Pivot data source. None Sets a custom data source factory function for a Pivot widget.

overrideApi.setObjectFieldDataSource(dataSourceFactory) dataSourceFactory - a factory function for the construction of an ObjectField data source. None Sets a custom data source factory function for an ObjectField widget, such as a single or multiple object picker.

#### Override an ItemList data source

To override an ItemList data source, pass an ItemList data source factory function to the overrideApi.setItemListDataSource method.

View an example showing how to override a ItemList data source Copy

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
overrideApi.setItemListDataSource(function(itemListDataSourceParams) {

  return {

    getData: {

      method: function(payload) {

        // ...

      }

    },

    inboundTransformer: {

      method: function(data) {

        // ...

      }

    },

    outboundTransformer: {

      method: function(data) {

        // ...

      }

    }

  };

});
```

See the following subsections for more information about overriding an ItemList data source:

- itemListDataSourceParams object

- Data source object

- ItemList data source request

- Filter object

- FilterTree object

- FieldFilter object

- Condition object

##### itemListDataSourceParams object

The itemListDataSourceParams object passed to a factory function contains the properties listed in the following table:

Property Description

workspaceId The ID of the current workspace

artifactType The current Artifact Type ID

folderId The Artifact ID of the current folder

callbacks An object containing callback functions

reportError A function that displays an error message to a user

loggedInUserId The ID of the logged-in user

dataRetrievalServicePath URL

##### Data source object

The data source factory function should return a data source object. For more information, see Additional information about dataSource objects .

Property Type Description

getData.method function(payload: Object): Promise Performs a query on the server. It passes the payload as a query parameter and returns a promise that resolves into query results.

inboundTransformer.method function(data: Object): Object Transforms a query result from the server format to the ItemList format, if required.

outboundTransformer.method function(payload: Object): Object Transforms query parameters from the ItemList format to the server format, if required.

Property Parameter Return value Description

getData.method function(payload: Object) Promise Performs a query on the server. It passes the payload as a query parameter and returns a promise that resolves into query results.

inboundTransformer.method function(data: Object) Object Transforms a query result from the server format to the ItemList format, if required.

outboundTransformer.method function(payload: Object) Object Transforms query parameters from the ItemList format to the server format, if required.

View an example of a payload object for an outbound transformer Copy

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
{

  "filter": {

    "hidden": {

      "info": {

        "type": 1,

        "data": {

          "field": "Folder Id",

          "conditions": [

            {

              "value": 1003697,

              "operation": "in"

            }

          ],

          "enabled": false,

          "hidden": true,

          "global": true

        }

      }

    }

  },

  "startIndex": 1,

  "pageSize": 25,

  "fields": [

    "Edit",

    "Security",

    "File Icon",

    "Control Number",

    "Author",

    "Custodian - Single Choice",

    "Duplicate",

    "File Type",

    "File Size",

    "Artifact ID"

  ],

  "sorts": [],

  "localSort": {},

  "useQueryToken": true,

  "queryToken": null,

  "activeRowId": null

}
```

View an example of a data object returned by an inbound transformer Copy

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
{

  "items": [

    {

      "fieldData": {

        "Artifact ID": 1039212,

        "editPermission": true,

        "runScriptPermission": true,

        "securityMetadata": {

          "img": {

            "alt": "Locked"

          },

          "anchor": {

            "id": "security_popup_1039212",

            "title": "Change Security Permissions",

            "class": "tabableListLink"

          },

          "permission": true

        },

        "relativityCompareMetadata": {

          "img": {

            "alt": "Compare Document"

          },

          "anchor": {

            "title": "Compare Document",

            "id": "relativity_compare_1039212"

          },

          "permission": true

        },

        "fileIconMetadata": {

          "img": {

            "alt": "Open Stand-Alone Viewer"

          },

          "anchor": {

            "id": "file_icon_1039212",

            "title": "Open Stand-Alone Viewer",

            "class": "tabableListLink"

          },

          "permission": true,

          "enableRedirect": false,

          "windowName": "StandAloneViewer",

          "features": "height=1040,width=1920,location=no,scrollbars=no,menubar=no,toolbar=no,status=no,resizable=yes"

        },

        "editUrl": "/Relativity/Case/Document/Review.aspx?AppID=1019859&ArtifactID=1039212&profilerMode=Edit&ArtifactTypeID=10&SelectedTab=null",

        "viewUrl": "/Relativity/Case/Document/Review.aspx?AppID=1019859&ArtifactID=1039212&ArtifactTypeID=10&profilerMode=View&SelectedTab=null",

        "securityUrl": "/Relativity/Permissions/Edit.aspx?AppID=1019859&ArtifactID=1039212",

        "securityImgSrc": "/Relativity/Images/unlock.gif",

        "fileIconImgSrc": "/Relativity/Images/FileIcons/msg.png",

        "compareUrl": "/Relativity/Case/Document/DocumentComparePopup.aspx?ArtifactID=1039212&AppID=1019859&PageArtifactID=1003663",

        "compareImgSrc": "/Relativity/Images/compare.png",

        "viewerPopupLinkUrl": "/Relativity/Case/Document/DocumentViewerPopup.aspx?AppID=1019859&ArtifactID=1039212",

        "downloadUrl": "/Relativity/Case/Document/DocumentViewerPopup.aspx?AppID=1019859&ArtifactID=1039212",

        "Edit": null,

        "Security": null,

        "File Icon": "EN000019.MSG",

        "Control Number": "EN000019",

        "Author": "phillip.allen@enron.com",

        "Custodian - Single Choice": {

          "Name": "Allen, Paul",

          "Artifact ID": 1038170

        },

        "Duplicate": false,

        "File Type": "E-mail",

        "File Size": "440.00"

      }

    }

  ],

  "currentMinItemIndex": 1,

  "currentMaxItemIndex": 25,

  "grandTotalItems": 73973

}
```

##### ItemList data source request

The following table lists the properties of a payload object for the outbound translation of an ItemList data source.

Property Type Description Required

startIndex int The index of the first item to fetch Yes

pageSize int The number of items to fetch Yes

fields array of strings An array of Field names Yes

sorts array of strings The sort order for the fields, as ascending or descending. For example, use ["FIELD1 ASC", "FIELD2 DESC"]. Yes

activeRowId int The identifier for a highlighted row Optional

filter object A Filter object - see Filter object . Yes

##### Filter object

A Filter object contains information about the filters and conditions currently applied to an item list. The Filter object exposes the following API:

Name Parameter Return value Description

getTreeNames() None object An object with available tree names - see View an example of an object with available tree names .

getFullTree([string]) array of strings object Returns a FilterTree object - see FilterTree object .

View an example of an object with available tree names Copy

```text
1
2
3
4
5
6
7
{

    USER_GLOBAL: "userGlobal",

    HIDDEN: "hidden",

    GLOBAL: "global",

    WIDGET_NATIVE: "widgetNative",

    USER: "user"

}
```

##### FilterTree object

A FilterTree object exposes a method for getting the active filter conditions currently applied to a field.

Name Parameter Return value Description

getAllOperands() None array of objects Returns array of FieldFilter objects - see FieldFilter object .

##### FieldFilter object

A FieldFilter object describes conditions applied to a given field.

Field Type Description Required

field string The name of a field Yes

conditions array of object An array of Condition objects Yes

isMultiSelectTextFilter bool A Boolean value indicating if the filter is used for selecting multiple options. Optional

##### Condition object

A Condition object describes a single condition for a given field.

Field Type Description Required

operation string The name of the operation Yes

value any A value associated with a condition Optional

View table with supported operations by field type

The following table lists the operations supported by different field types. The key for the table is the following: A rtifactID, Whole N umber, B oolean, D ecimal, C urrency, Y es/ N o, F ixedLength T ext, L ong T ext, D a t e, U ser, S ingle C hoice, S ingle O bject, M ulti C hoice, and M ulti O bject.

Operation A N B D C Y/N FT LT Dt U SC SO MC MO Description

is set ü ü ü ü ü ü ü ü ü ü ü ü ü ü The field isn't null.

is not set ü ü ü ü ü ü ü ü ü ü ü ü ü ü The field is null.

is ü ü ü ü ü ü ü ü ü ü ü The field value equals the specified value.

is not ü ü ü ü ü ü ü ü ü ü ü The field value doesn't equal the specified value.

is like ü ü ü ü ü ü ü ü The field value is like the specified value.

is not like ü ü ü ü ü ü ü ü The field value isn't like the specified value.

is greater than ü ü ü ü ü ü ü ü The field value > the specified value.

is less than ü ü ü ü ü ü ü ü The field value < the specified value.

in ü ü ü ü ü ü ü ü ü ü The field value is in the list of specified values.

not in ü ü ü ü ü ü ü ü ü ü The field value isn't in the list of specified values.

contains ü ü The field value contains the specified value.

does not contain ü ü The field value doesn't contain the specified value.

any of these ü ü ü ü ü ü The field value is one of the selected values.

none of these ü ü ü ü ü ü The field value isn't one of the selected values.

all of these ü ü Any of the selected values are present in the field.

none of these ü ü None of the selected values is present in the field.

IN VIEW ü The field value represents an item in the view.

is logged in user ü The logged-in user is equal to the field value.

IN SAVED SEARCH ü The field value represents an item in the saved search results.

NOT IN SAVED SEARCH ü The field value doesn't represent an item in the saved search results.

these conditions ü The field value is one of the selected values.

not these conditions ü The field value isn't one of the selected values.

is before ü The field value is before the entered date.

is before or on ü The field value is before or on the entered date.

is after ü The field value is after the entered date.

is after or on ü The field value is on or after the entered date.

between ü The field value is between the two entered dates.

is in ü The field value is within the selected range.

#### ItemList response

The inbound translator for data source should return a correctly formatted Result object, so that the list view can render the data.

See the following subsections for more information about an ItemList response:

- Result object

- DataRow object

- FieldData object

- FileIconMetadata object

- CompareMetadata object

- SecurityMetadata object

- EditMetadata object

- RunScriptMetadata object

- RowAttr object

- Field values

##### Result object

Property Type Description Required

currentMaxItemIndex int The index for the maximum number of items Yes

currentMinItemIndex int The index for the minimum number of items Yes

grandTotalItems int The total number of items Yes

items array of objects An array of DataRow objects - see DataRow object . Yes

##### DataRow object

Each DataRow object describes one fetched data row.

Property Type Description Required

fieldData object A FieldData object - see FieldData object . Yes

##### FieldData object

Property Type Description Required

Artifact ID int The Artifact ID of the current item, such as a document Yes

compareImgSrc string A URL link to an image. It is used to construct the icon field type for the Compare field. Generated

compareUrl string A URL link into the compare service. It is used for static text or icon field formatters. Generated

downloadUrl string A URL link for downloading an item. It is used for the static text. Generated

editPermission bool Indicates whether the user has edit permissions on this item. Optional

editUrl string A URL link for editing an item. It is used for static text field formatters. Generated

fileIconImgSrc string A URL link to an image. It is used to construct the icon field type for the File Icon field. Generated

fileIconMetadata object A FileIconMetadata object - see FileIconMetadata object . Yes

relativityCompareMetadata object A CompareMetadata object - CompareMetadata object Yes

runScriptPermission bool Indicates whether the user has permissions to run a script. Optional

securityImgSrc string A URL link to an image. It is used to construct icon field type for the Security field. Generated

securityMetadata object A SecurityMetadata object - see SecurityMetadata object . Yes

securityUrl string A URL link for changing item Security. It is used for static text field formatters. Generated

viewUrl string A URL link for viewing item metadata. It is used for static text field formatters. Generated

viewerPopupLinkUrl string A URL link for the pop - up viewer. Generated

editMetadata object An EditMetadata object - EditMetadata object . Yes

rowAttr object A RowAttr object - RowAttr object . Optional

<field-name> Determine by data type Field values - see Field values . Properties should exist with the same names as the fields, even if the field value is null. The property is required, but the value isn't.

##### FileIconMetadata object

The FileIconMetadata object describes a file icon.

Property Type Example

anchor object

anchor.id string "file_icon_<row-artifact-id>"

anchor.title string "Open Stand-Alone Viewer"

anchor.class string "tabableListLink

enableRedirect bool FALSE

features string "height=1160,width=1920,location=no,scrollbars=no,menubar=no,toolbar=no,status=no,resizable=yes"

img object

img.alt string "Open Stand-Alone Viewer"

permission bool TRUE

windowName string "StandAloneViewer"

##### CompareMetadata object

Property Type Example

anchor object

anchor.id string "relativity_compare_<row-artifact-id>"

anchor.title string "Compare Document"

img object

img.alt string "Compare Document"

permission bool TRUE

##### SecurityMetadata object

Property Type Example

anchor object

anchor.id string "security_popup_<row-artifact-id>"

anchor.title string "Change Security Permissions"

anchor.class string "tabableListLink

img object

img.alt string "Locked"

permission bool TRUE

childrenCallback function

##### EditMetadata object

Property Type Example

features string "height=385,width=360,location=no,scrollbars=no,menubar=no,toolbar=no,status=no,resizable=yes"

windowName string "batchReview"

enableRedirect bool FALSE

##### RunScriptMetadata object

Property Type Example

features string "height=604,width=882,location=no,scrollbars=no,menubar=no,toolbar=no,status=no,resizable=yes"

windowName string "runScriptWindow"

enableRedirect bool FALSE

##### RowAttr object

Property Type Description

class string Use the string "group-end" to set the current document as the last item in a group.

##### Field values

Process field values according to their data type as illustrated in the following table:

Field type Value Supports multi-reflected fields

FixedLengthText value Yes

WholeNumber value Yes

LongText value Yes

Decimal value Yes

Currency value Yes

Date value Yes

YesNo value Yes

User Copy

```text
1
2
3
4
User{

  "Artifact ID": <artifact-id>,

  "Full Name": "<user-name>"

}
```

Yes

SingleChoice Copy

```text
1
2
3
4
{

  "Artifact ID": <artifact-id>,

  "Name": "<text-value>"

}
```

Yes

SingleObject Copy

```text
1
2
3
4
{

  "Artifact ID": <artifact-id>,

  "Relativity Text Identifier": "<text-value>"

}
```

Yes

MultipleChoice Copy

```text
1
2
3
4
[{

  "Artifact ID": <artifact-id>,

  "Name": "<text-value>"

}]
```

Yes

MultipleObject Copy

```text
1
2
3
4
[{

  "Artifact ID": <artifact-id>,

  "Relativity Text Identifier": "<text-value>"

}]
```

No

File "<filename>" No

Security value No

#### Override a Pivot data source

To override a Pivot data source, pass Pivot data source factory function to the overrideApi.setPivotDataSource method.

View an example showing how to override a Pivot data source Copy

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
overrideApi.setPivotDataSource(function(pivotDataSourceParams) {

  return {

    getData: {

      method: function(payload) {

        // ...

      }

    },

    inboundTransformer: {

      method: function(data) {

        // ...

      }

    },

    outboundTransformer: {

      method: function(data) {

        // ...

      }

    }

  };

});
```

See the following subsections for more information about overriding a Pivot data source:

- pivotDataSourceParams object

- Data source object

- Pivot request

- Filter object

- Pivot response

##### pivotDataSourceParams object

The pivotDataSourceParams object is passed to a factory function. This object contains the following properties:

Property Description

workspaceId The ID of the current workspace

artifactTypeId The current Artifact Type ID

parameters Pivot parameters, pivot-type-specific

parameters.groupByField An object that describes a GROUP BY field

parameters.pivotOnField An object that describes a Pivot field

parameters.pivotProfile An object that describes a Pivot profile

fieldCollectionMetaData An array of available item list fields

callbacks Callbacks

reportError A function that displays an error message to a user

dataAggregationServicePath URL

##### Data source object

The data source factory function should return a data source object. This object contains the following properties:

Property Type Description

getData.method function(payload: Object): Promise Performs a query on the server. It passes the payload as a query parameter and returns a promise that resolves into query results.

inboundTransformer.method function(data: Object): Object Transforms a query result from the server format to the Pivot format, if required.

outboundTransformer.method function(data: Object): Promise Transforms query parameters from the Pivot format to the server format, if required.

Property Parameter Return value Description

getData.method function(payload: Object) Promise Performs a query on the server. It passes the payload as a query parameter and returns a promise that resolves into query results.

inboundTransformer.method function(data: Object) Object Transforms a query result from the server format to the Pivot format, if required.

outboundTransformer.method function(data: Object) Promise Transforms query parameters from the Pivot format to the server format, if required.

##### Pivot request

Pivot widget queries a Pivot data source with the following payload object:

Property Type Description Required

filter object A Filter object - see Filter object . Yes

##### Filter object

The Filter object for Pivot is the same as the object for the ItemList. see Filter object .

##### Pivot response

Pivot data source should return an array of objects, one for each pivot element, as illustrated in the following table:

Property Type Description Required

id string An identifier Yes

idNormalized string Contains the string for the groupBy field value. If the groupBy field value is a date type, it should contain the ISO date string. Yes

keyOrderLookup array of string The keys for an item, such as ["case 1", "case 2", "(blank)", "Grand Total"] Yes

label string A text label Yes

objectIdMap object The key/value collection for mapping column values. Yes

value object A map of keys to values for an item, such as {"case 1": 13, "case 2": 1, "(blank)": 4, "Grand Total": 18} Yes

#### Override an ObjectField data source

Single and multiple object picker widgets use ObjectField data sources. To override an ObjectField data source, pass the factory function to the overrideApi.setObjectFieldDataSource method.

View an example showing how to override an ObjectField data source Copy

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
overrideApi.setObjectFieldDataSource(function(objectFieldDataSourceParams) {

  return {

    getData: {

      method: function(payload) {

        // ...

      }

    },

    inboundTransformer: {

      method: function(data) {

        // ...

      }

    },

    outboundTransformer: {

      method: function(data) {

        // ...

      }

    }

  };

});
```

##### objectFieldDataSourceParams object

The objectFieldDataSourceParams object passed to a factory function has the same structure and data as itemListDataSourceParams object. See itemListDataSourceParams object .

View an example of a data override event Copy

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
define(function() {

  function testHandler(api) {

    function handleDataSourceOverrideEvent(overrideApi) {

      // Set a custom data source for ItemList widget.

      // Pass a data source factory function to the overrideApi.setItemListDataSource() function.

      overrideApi.setItemListDataSource(function(itemListDataSourceParams) {

        // The data source factory function receives an itemListDataSourceParams object with query parameters

        // and should return a data source object.

        return {

          getData: {

            method: function(payload) {

              // The getData.method should return a promise, resolving with the data received from server.

              var result = api.promise.defer();

              result.resolve({

                Success: true,

                Data: {

                  ArtifactTypeGuids: ["15c36703-74ea-4ff8-9dfb-ad30ece7530d"],

                  ArtifactTypeId: 10,

                  CurrentStartIndex: 1,

                  DataResults: [{

                    ArtifactGuids: [],

                    ArtifactId: 1039253,

                    ArtifactTypeGuids: ["15c36703-74ea-4ff8-9dfb-ad30ece7530d"],

                    ArtifactTypeId: 10,

                    Fields: [{

                      ArtifactGuids: ["2a3f1212-c8ca-4fa9-ad6b-f76c97f05438"],

                      ArtifactId: 1003667,

                      FieldType: "FixedLengthText",

                      Name: "Control Number",

                      Value: "AMEYERS_0000047"

                    },{

                      ArtifactGuids: ["1f036749-a691-4aa8-8cf7-5eeb80c36caf"],

                      ArtifactId: 1003671,

                      FieldType: "FixedLengthText",

                      Name: "Group Identifier",

                      Value: "AMEYERS_0000047"

                    }],

                    ParentArtifactId: 0,

                    Permissions: [{ID: 4, Name: "Secure"}],

                    WorkspaceId: itemListDataSourceParams.workspaceId

                  },{

                    ArtifactGuids: [],

                    ArtifactId: 1039254,

                    ArtifactTypeGuids: ["15c36703-74ea-4ff8-9dfb-ad30ece7530d"],

                    ArtifactTypeId: 10,

                    Fields: [{

                      ArtifactGuids: ["2a3f1212-c8ca-4fa9-ad6b-f76c97f05438"],

                      ArtifactId: 1003667,

                      FieldType: "FixedLengthText",

                      Name: "Control Number",

                      Value: "AMEYERS_0000048"

                    },{

                      ArtifactGuids: ["1f036749-a691-4aa8-8cf7-5eeb80c36caf"],

                      ArtifactId: 1003671,

                      FieldType: "FixedLengthText",

                      Name: "Group Identifier",

                      Value: "AMEYERS_0000048"

                    }],

                    ParentArtifactId: 0,

                    Permissions: [{ID: 4, Name: "Secure"}],

                    WorkspaceId: itemListDataSourceParams.workspaceId

                  }],

                  NextPage: "",

                  PreviousPage: "",

                  ResultCount: 2,

                  TotalResultCount: 2,

                  Window: [1039253, 1039254],

                  WorkspaceId: itemListDataSourceParams.workspaceId

                }

              });

              return result.promise;

            }

          },

          inboundTransformer: {

            method: function(data) {

              // The inboundTransformer.method should implement a server-to-ItemList data transformation.

              return data;

            }

          },

          outboundTransformer: {

            method: function(data) {

              // The outboundTransformer.method should implement ItemList-to-server data transformation.

              return data;

            }

          }

        };

      });

    }

    return {

      dataSourceInit: handleDataSourceOverrideEvent

    };

  }

  return testHandler;

});
```

### View API

The View API includes functionality that provides an event handler with information when the active view or browser has changed. The event handler needs to subscribe to the viewChange event and the inspecting event data. The changeView event occurs any time the view is modified or when a saved search is selected.

#### Event data object

Property Type Description Example

viewId integer The ID of currently active view 1003684

viewLabel string The name or label for the currently active view "Documents"

browser string The name of the current browser. Currently, this property can be set to one of these values: folder, savedSearch, savedSearchExecute, cluster, fieldTree, or default. "savedSearch"

View an example of a viewChange event Copy

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
define(function() {

    function sampleHandler(api) {

        // A function called when view or browser changes. It gets the data object that has the viewId, viewLabel and browser properties.

        function viewChange(data) {

            var viewId = data.viewId;

            var browser = data.browser;

            if (viewId === 123 && browser !== "savedSearchExecute") {

                // ....

            }

        }

        return {

            // Subscribe to the viewChange event.

            viewChange: viewChange

        }

    }

    return sampleHandler;

});
```

### Widget Menu Customization API

The Widget Menu Customization API provides functionality that provides an event handler with the ability to examine and modify menu items for a widget. The event handler needs to subscribe to the widgetMenuCreate event to receive notifications about changes to the widget menu. This event occurs when retrieving metadata for a new widget.

#### menuApi object

The menuApi object exposes the following methods:

Name Parameter Return value Description

menuApi.getWidgetTypeName() None a string indicating a widget type name Returns the type name of the widget that triggered the notification:

- "pivotWgt" for Pivot

- "fluidItemListWgt" for item list

- "clusterWgt" for cluster

menuApi.getWidgetMenu() None array of menu items Returns menu items that are currently set for this widget. See the following example: Copy

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
[{

  title: "Properties",

  items: [{

    title: "Edit",

    visible: true,

    css: "link",

    icon: "edit",

    onClick: function() { ... }

  }]

}]
```

menuApi.setWidgetMenu(menu) menu - an array of menu categories None Sets passed menu items for a current widget.

View an example showing how to use the menuApi object Copy

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
define(function() {

    function sampleHandler(api) {

        // This function receives notifications about changes in widget menus.

        function handleWidgetMenuCustomizeEvent(menuApi) {

            // To examine and modify menu items for a widget, use the menuApi object.

            if (menuApi.getWidgetTypeName() === "pivotWgt") { // Check if this is a pivot widget.

                var menu = menuApi.getWidgetMenu();

                menu.forEach(function(category) {

                    if (category.title === "Properties") { // Find 'Properties' submenu.

                        category.items.forEach(function(item) {

                            if (item.title === "Edit Pivot") {

                                // Hide 'Edit Pivot' menu item from Pivot menu.

                                item.visible = false;

                            }

                        });

                    }

                });

                menuApi.setWidgetMenu(menu); // Apply menu changes to a widget.

            }

        }

        return {

            // Add the following to receive  notifications about changes in widgets' menu items.

            widgetMenuCreate: handleWidgetMenuCustomizeEvent

        };

    }

    return sampleHandler;

});
```

## General APIs details

The general APIs are available to event handlers when the api object is passed as a parameter to a top-level function. These APIs provide services that you can use to customize the behavior and UI for list pages.

### Initialization information

This section includes a code sample for the initializer() function and field descriptions for the api object passed to this function.

#### initializer(api) function

The following code sample illustrates how the api object is passed to the initializer() function.

Copy

```text
1
2
3
4
5
6
7
function initializer(api) {

  //...

  return {

    cellFormattersInit: cellFormattingHandlerFunction

  }

}

...
```

#### api object properties

The following table lists the properties on the api object:

Field Description

promise Represents a service for working with JavaScript promises.

eventService Represents a service for listening and emitting messages.

dataSourceService Represents a service for making requests to the Relativity server.

inboundTranslationService Represents a service for accessing all predefined inbound translators.

outboundTranslationService Represents a service for accessing all predefined outbound translators. This service may be useful when implementing a custom data source.

keplerProviderService Represents a service for creating custom data sources.

commonUtilities Represents the common utilities service.

modalService Represents a service for creating and populating custom modal windows.

toolbarService Represents a service for showing and displaying custom toolbars.

startupInfo Represents an object containing information obtained from a listPageStartupInformation call.

customWidgetService Represents a service for creating a dashboard widget populated with custom contents.

### startup info object

The startup info object contains the following information obtained from a listPageStartupInformation call. For more information, see the startupInfo field in api object properties .

Field Type Description

isDocumentListPage boolean Set to true if the page is a list page. Otherwise, it is set to false.

workspaceId integer Set to the ID of the currently active workspace.

### Promise API

The Promise API (api.promise) is a service for working with promises.

#### Methods

Name Parameter Return value Description

api.promise.defer() None None Creates a deferred object with a promise, and the methods needed to resolve or reject it.

deferred.resolve(value) value - resolves the promise. None Resolves the promise with the value passed as an argument.

deferred.reject(reason) reason - explanation for rejection of a promise. None Rejects the promise with the reason passed as an argument.

deferred.promise None promise Represents a property that returns the current promise.

promise.then(successCallback, [errorCallback]) successCall back - a function executed when the promise is resolved.

[errorCallback] - a function executed when the promise is rejected. None Creates a continuation on a current promise. The successCallback() function is executed when a promise is resolved, and the errorCallback() function is executed when a promise is rejected.

promise.catch(callback) callback -a function that returns a promise. promise Provides shorthand method for the promise.then(null, callback) method.

### Events API

Events API (api.eventService) is a service for sending and receiving messages.

#### Methods

Name Parameter Return value Description

api.eventService.subscribe(eventName, eventHandler) eventName - a string indicating the name of an event .

eventHandler - the function(event, payload), which is a callback function. uid - the ID of an event handler. Registers an eventHandler callback function so it receives the occurrences of the eventName event.

api.eventService.unsubscribe(uid) uid - the ID of an event handler. None Unregisters a previously registered callback.

api.eventService.emit(eventName, payload, ...) eventName - a string indicating the name of an event to emit.

payload... - arbitrary data to pass to an event handler. None Emits the eventName event with payload data.

View an example showing how to use the api.eventService Copy

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
// eventHandler1.js

define(function() {

  function eventHandler1(api) {

    // Subscribe to a "custom-event" event.

    api.eventService.subscribe("custom-event", handleCustomEvent);

    function handleCustomEvent(event, payload) {

      // On receiving the event, show an alert message with an event payload.

      alert("Got the event from " + payload);

    }

    return {};

  }

  return eventHandler1;

});

// eventHandler2.js

define(function() {

  function eventHandler2(api) {

    // Send a "custom-event" event.

    api.eventService.emit("custom-event", "Event Handler 2");

    return {};

  }

  return eventHandler2;

});
```

### Kepler Provider API

Kepler Provider API (api.keplerProviderService) exposes APIs for executing Relativity service requests.

Field Description

api.keplerProviderService.KeplerProxy An object used for setting up the connection to Relativity service endpoint.

api.keplerProviderService.callLRP Sends Relativity service requests to the server.

View an example showing how to use the api.keplerProviderService Copy

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
var FieldTreeManagerService = function(baseUrl) {

     api.keplerProviderService.KeplerProxy.call(this, baseUrl);

     var proxy = this;

     this.getFieldTreeItems = function(workspaceId, fieldTypeId, parentArtifactId, associatedId, fieldArtifactId)

     {

         var payload = {

             workspaceId: workspaceId,

             fieldTypeId: fieldTypeId,

             parentArtifactId: parentArtifactId,

             associatedId: associatedId,

             fieldArtifactId: fieldArtifactId

         };

         return api.keplerProviderService.callLRP(

            proxy,

            "Relativity.Services.FieldTree.IFieldTreeModule/Field Tree Manager",

            "GetFieldTreeItemsAsync",

            payload, null, null, keplerVersion = 2);

     };

};

var fieldTreeManagerService = new FieldTreeManagerService(api.commonUtilities.applicationPaths.kepler);
```

### Common Utilities API

Common Utilities API (api.commonUtilities) provides event handlers with the ability to access ListPage common utilities services.

The following table lists these services:

Field Description

api.commonUtilities.commonConstantsAndObjects Exposes common constants and enums, such as permission type IDs, Artifact Type IDs, well-known GUIDs, and others. Copy

```text
1
2
var fieldTypeId =

  api.commonUtilities.commonConstantsAndObjects.FIELD_TYPE_IDS.MULTI_CHOICE
```

api.commonUtilities.HrefFactory Represents the class used for generating URLs for document create, view, edit, and other operations. It is useful when implementing custom data sources. Copy

```text
1
2
var href =

  api.commonUtilities.HrefFactory.generateExternalHref("http://www.google.com");
```

api.commonUtilities.applicationPaths Exposes APIs for getting URL paths for Relativity, service endpoints, and other purposes. Copy

```text
1
2
keplerPath =

  api.commonUtilities.applicationPaths.applicationPaths.kepler;
```

### Modal API

Modal API (api.modalService) provides functionality used by an event handler to open a modal window populated it with custom contents.

#### Methods

Name Parameter Return value Description

api.modalService.createModal(content) content - an object describing custom content. integer Creates a modal windows described by a content object and returns an integer representing a modal ID.

api.modalService.showModal(modalId) modalId - an integer used to identify a modal window. None Displays a modal window previously created by the createModal() method.

api.modalService.hideModal(id) id - an identifier returned by the createModal() method. None Closes modal window.

api.modalService.destroyModal(id) id - an identifier returned by the createModal() method. None Destroys a modal windows and frees resources.

#### content object properties

Property Type Description Example

title string The title of a modal window "Create New Project"

modalClass string The class of a modal widget "rlh-new-rdo-dialog"

modalName string The name of a modal widget "rlhRdoModalDialog"

template string The custom HTML contents of a modal window "<span>Some sample text</span>"

buttons array of object The buttons in the bottom part of a modal. For each button object, specify name and eventName fields. Copy

```text
1
2
3
4
5
6
7
[{

    name: "Apply",

    eventName: "apply_click"

},{

    name: "Cancel",

    eventName: "cancel_click"

}]
```

init function An initialization callback that is called after compiling a widget and adding it to the DOM. Add internal logic to this function, such as button onClick handlers, data sources, and other operations. The init function takes the following parameters:

- scope - an angular scope of a widget

- el - a compiled DOM element

- ctrl - an angular controller of a widget

Copy

```text
1
2
3
function(scope, el, ctrl) {

    // Initialization

}
```

View an example showing how to use Modal API methods Copy

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
define(function() {

  function sampleHandler(api) {

    function showMyModal() {

      var id = api.modalService.createModal({

        title: "My awesome modal",

        template: "<span>Some text</span>",

        buttons: [{name: "OK", eventName: "awesome_modal_ok_click"}],

        init: function(scope) {

          scope.$on("awesome_modal_ok_click", function() {

            // Close modal on the OK button click.

            api.modalService.hideModal(id);

          });

        }

      });

           api.modalService.showModal(id);

    }

    // Show this modal in 2 seconds.

    setTimeout(showMyModal, 2000);

    return {};

  }

  return sampleHandler;

});
```

### Toolbar API

Toolbar API (api.toolbarService) provides functionality used by event handlers to show and hide toolbars with custom content and buttons.

#### Methods

Name Parameter Return value Description

api.toolbarService.createToolbar(content) content - an object describing custom content. integer Creates a toolbar described by content object and returns an integer representing a toolbarID.

api.toolbarService.showToolbar(toolbarId) toolbarId - an identifier for the created toolbar. None Displays toolbar previously created by createToolbar() method.

api.toolbarService.hideToolbar(toolbarId) toolbarId - an identifier for the created toolbar. None Hides the toolbar that is currently displayed.

#### content object properties

Property Type Description Required

toolbarClass string The class of the toolbar "review-queue-access"

template string The custom HTML contents of a toolbar "<span>Some sample text</span>"

buttons array of object Buttons in the bottom part of a modal. For each button object, specify the name and eventName fields. Copy

```text
1
2
3
4
5
6
7
[{

    name: "Apply",

    eventName: "apply_click"

},{

    name: "Cancel",

    eventName: "cancel_click"

}]
```

init function An initialization callback that is called after compiling a widget and adding it to the DOM. Add internal logic to this function, such as button onClick handlers, data sources, and other operations. The init function takes the following parameters:

- scope - an angular scope of a widget

- el - a compiled DOM element

- ctrl - an angular controller of a widget

Copy

```text
1
2
3
function(scope, el, ctrl) {

    // Initialization

}
```

View an example showing how to use the api.toolbarService Copy

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
define(function() {

    function sampleHandler(api) {

        var toolbarId;

        var api = api;

        // First, create a toolbar.

        toolbarId = api.toolbarService.createToolbar({

            template: "<span>Greetings</span>",

            buttons: [{name: "Close", eventName: "close_toolbar"}],

            init: function(scope) {

                scope.$on("close_toolbar", function() {

                    // on click - hide it

                    api.toolbarService.hideToolbar(toolbarId);

                });

            }

        });

        function viewChange(data) {

            // Next, display it when view changes.

            api.toolbarService.showToolbar(toolbarId);

        }

        return {

            // Subscribe to the "onViewChanged" event.

            viewChange: viewChange

        }

    }

});
```

### CustomWidget API

CustomWidget API (api.customWidgetService) provides functionality used by an event handler to create a dashboard widget populated with custom contents.

#### Methods

Name Parameter Return value Description

api.customWidgetService.createWidget(content) content - an object describing a widget. integer Creates and displays a dashboard widget described by the content object and returns an integer representing a widget ID. The created widget won't be persisted or saved with the dashboard.

api.customWidgetService.removeWidget(widgetId) widgetId - an integer retrieved from createWidget() method. None Removes and destroys a dashboard widget.

api.customWidgetService.isWidgetExists(widgetId) widgetId - an integer retrieved from createWidget() method. boolean Returns true if the widget exists on the dashboard. Otherwise, it returns false.

#### content object properties

Property Type Description Example

template string The custom HTML contents of a widget Copy

```text
1
2
"<div><div ng-repeat=\"row in resultSet\">{{row}}

</div></div>"
```

sizeX integer The initial widget width in columns count. The default value is 5.

sizeY integer The initial widget height in rows count. The default value is 18.

title string The widget title

enableMaximize bool Enables or disables the ability to maximize a menu item of a widget. The default value is false.

enableRemove bool Indicates whether to enable or disable the removal of a menu item in the widget. The default value is false.

enableMenu bool Indicates whether the widget menu is enabled or disabled. The default value is false.

init function An initialization callback that is called after compiling a widget and adding it to the DOM. Add internal logic to this function, such as button onClick handlers, data sources, and other operations. The init function takes customWidgetManager parameter. This parameter is an object of the type EventHandlersCustomWidgetManager, which provides the API with access to the scope, element, and controller. Copy

```text
1
2
3
function(customWidgetManager) {

    // Initialization

}
```

dataSource object A DataSource object used to retrieve a widget data. This property is optional. Copy

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

    getData: {

        method: referenceToGetDataFunction

    },

    inboundTransformer: (void 0),

    outboundTransformer: {

        method: referenceToYourOutboundTransformerFunction

    }

}
```

#### EventHandlersCustomWidgetManager object properties

Property Type Return value Description

scope property object Returns an AngularJS scope object for the created directive.

element property object Returns a JQLite wrapped element for the widget.

ctrl property object Returns an instance of the controller assigned to the widget directive.

errorTypes property TBD Returns an object with error types constants. See the following list of errorTypes: Copy

```text
1
2
3
4
5
{ NO_DATA: 1,

  TOO_MANY_VALUES: 2,

  VALIDATION: 3,

  SERVER: 4,

  CANCEL: 5 }
```

showMessage(messageObject) method None Displays a message as a content of the widget by overlapping other content. See the following example of a messageObject: Copy

```text
1
2
3
4
5
{ message: data.Message,

  type: widgetManager.errorTypes.SERVER,

  icon: data.messageIcon || widgetManager.canceledIcon,

  messageType: "error",

  hideContent: false }
```

clearMessage() method None Clears a message.

hideLoading() method None Hides a loading spinner.

View an example showing how to create a custom widget Copy

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
define(function () {

    "use strict";

    function testHandler(api) {

        var _api = api, _widgetId, _viewIdToShow = 1188142,

        _workspaceId = 1017106, _fieldArtifactId = 1112594,

        _widgetOptions = {

            title: "My custom widget",

            template: "<div style='merge: 10px; padding: 10px'>" +

                "<div ng-show='noData'> NO DATA </div>" +

                "<div ng-hide='noData'>Data recieved from server.</div>" +

                "<div><div ng-repeat=\"row in resultSet\">"+

                "{{row}}"+

                "</div></div>"+

                "</div>",

            sizeX: 6,

            sizeY: 10,

            enableMaximize: false,

            enableRemove: true,

            enabledMenu: true,

            dataSource: getDataSource(),

            init: initWidget

        };

        var reviewQueues, viewId;

        function initWidget(widgetManager) {

            var scope = widgetManager.scope;

            scope.noData = true;

            function checkAndSetErrorFromServer(data) {

                var hasError = false;

                if(data.Message && (data.Message !== "SUCCESS" || !data.Success || !data.Results)) {

                    widgetManager.showMessage({

                        message: data.Message,

                        type: widgetManager.errorTypes.SERVER,

                        icon: data.messageIcon || widgetManager.canceledIcon,

                        messageType: "error",

                        hideContent: false

                    });

                    hasError = true;

                }

                return hasError;

            }

            // Called by EventHandler, triggers watcher

            scope.metaData.setData = function (data) {

                /// <summary>Sets the data for the Pivot widget to use.</summary>

                /// <param name="data" type="Object">Data object to set.</param>

                scope.noData = true;

                scope.resultSet = [];

                scope.metaData.fullDataSet = [];

                if (!data) {

                    widgetManager.showMessage({

                        message: "This chart did not return any results.",

                        type: widgetManager.errorTypes.NO_DATA,

                        icon: widgetManager.canceledIcon,

                        messageType: "info"

                    });

                } else {

                    if (checkAndSetErrorFromServer(data)) {

                        return;

                    } else {

                        widgetManager.clearMessage();

                    }

                    scope.metaData.fullDataSet = data;

                    scope.$broadcast("reload_options");

                }

                scope.noData = false;

                scope.resultSet = data.Results || [];

                widgetManager.hideLoading();

            };

        }

        function viewChange(activeView) {

            widgetViewChanged(activeView);

        }

        function widgetViewChanged(activeView) {

            if (activeView && activeView.browser === "folder" && activeView.viewId === _viewIdToShow) {

                _widgetId = _api.customWidgetService.createWidget(_widgetOptions);

            } else if (!!_widgetId) {

                _api.customWidgetService.removeWidget(_widgetId);

                _widgetId = (void 0);

            }

        }

        function getData() {

            var settings =

                {

                    dataAggregationServicePath: "Relativity.Services.Pivot.IPivotModule/Pivot Manager"

                };

            return {

                method: function (payload) {

                    return _api.dataSourceService.kepler.pivot.getDataWithSettings(payload, settings);

                }

            };

        }

        function getDataSource(parameters) {

            return {

                getData: getData(),

                outboundTransformer: outboundTransformer(),

                onFailure: {

                    method: function () { }

                }

            }

        }

        function outboundTransformer() {

            return {

                method: function (payload) {

                    var treeNames,

                        filterTree,

                        filters,

                        rowFilterTree,

                        translatedFilters,

                        conditions,

                        rowConditions,

                        relationalField,

                        folderCondition;

                    if (typeof payload.filter.getFullTree === "function") {

                        treeNames = payload.filter.getTreeNames();

                        filterTree = payload.filter.getFullTree([treeNames.USER_GLOBAL, treeNames.HIDDEN, treeNames.GLOBAL, treeNames.USER]);

                        rowFilterTree = payload.filter.getFullTree([treeNames.WIDGET_NATIVE]);

                    }

                    filters = filterTree ? filterTree.getAllOperands() : [];

                    // WARNING: find() method doesn't supproted by IE11. Used only for testing purposes in chrome

                    folderCondition = filters.find(function (row) { return !!row && row.field === "Folder Id"; });

                    return _api.promise.when({

                        groupByField: {

                            id: _fieldArtifactId,

                            ArtifactID: _fieldArtifactId,

                            ViewFieldID: 0,

                            Guids: [],

                            label: "Custodian - Object",

                            title: "Custodian - Object",

                            value: _fieldArtifactId,

                            fieldTypeID: 10,

                            artifactTypeId: 1000036,

                            fieldAxisType: "category"

                        },

                        pivotOnField: {

                            title: "<Grand Total>",

                            id: -1

                        },

                        artifactTypeId: 10,

                        conditions: "(('Folder Name' IN [" + (folderCondition ? folderCondition.conditions[0].value : 0).toString() + "]))",

                        rowConditions: "",

                        searchProviderCondition: null,

                        relationalField: null,

                        workspaceId: _workspaceId,

                        sampleParameters: null

                    });

                }

            };

        }

        return {

            viewChange: viewChange

        };

    }

    return testHandler;

});
```

## Additional information about dataSource objects

The dataSource object is part of the metadate information required when registering a widget that has an event manager. The following code outlines the general structure of the dataSource metadata:

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
dataSource: {

    getData: {

        method: referenceToGetDataFunction

    },

    // Optional callback

    onSuccess: {

        method: referenceToSuccessfulDataRetrievalFunction

    },

    // Optional callback

    onFailure: {

        method: referenceToApplicationErrorHandlingFunction

    },

    inboundTransformer: {

        // The following line of code  is optional, but the inboundTransformer object is required.

        method: referenceToYourInboundTransformerFunction

    },

    outboundTransformer: {

        // This following line of code is optional, but the outboundTransformer object is required.

        method: referenceToYourOutboundTransformerFunction

    }

}
```

### dataSource.inboundTransformer

An inbound transformer converts incoming data returned from a dataSource. It is an optional entity for a dataSource. However, an inbound transformer must meet the following requirements when it is used:

- It must be a single synchronous function.

- It must convert the data payload returned from a dataSource into a form acceptable to the widget being populated.

Since a transformation is specific to the interfaces and return values exposed in the APIs for a data source, the following code illustrates a general example of an inbound transformer.

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
dataSource: {

   ...

   inboundTransformer: {

   // The following line of code is the only optional one.

    method: referenceToYourTransformerFunction

   },

   ...

}
```

### dataSource.outboundTransformer

An outbound transformer converts a data payload into a form acceptable to a dataSource. It is an optional entity for a dataSource. However, an outbound transformer must meet the following requirements when it is used:

- The method for the outbound transformer must be a single function.

- The outbound transformer must expect a single, plain JavaScript object.

- It must output a promise or data in a form expected by a specific dataSource.

Since a transformation is specific to the interfaces and return values exposed in the APIs for a data source, the following code illustrates a general example of outbound transformer metadata.

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
dataSource: {

   ...

   outboundTransformer: {

    // The following line of code is the only optional one. It may be either a sync method or a promise generator.

    method: referenceToYourTransformerFunction

   },

   ...

}
```
