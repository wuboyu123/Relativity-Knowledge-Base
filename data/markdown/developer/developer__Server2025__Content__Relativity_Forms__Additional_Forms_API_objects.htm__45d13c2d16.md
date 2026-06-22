---
title: "Additional Forms API objects"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Additional_Forms_API_objects.htm
collection: developer
fetched_at: 2026-06-22T06:32:06+00:00
sha256: 31c38a3baa206a40dc47d7f833f1bc8adfdf81749c88bd42d72ddd37750c3c43
---

Additional Forms API objects Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Additional Forms API objects

The Relativity Forms API includes objects and functions for pop-up windows. It also includes a class for event names.

## Summary of additional Forms API objects and functions

The following table lists additional Forms API objects and functions.

Object

Description

eventNames object

Represents the event names used in the Relativity Forms API.

popupControlApi object

Provides functionality for closing and accessing properties of a pop-up window.

Popup eventHandlerFactory function

Creates event handlers that run within a pop-up window created by invocations of methods on the convenienceApi.relativityFormsPopup.

ColumnDefinition class

Describes the item list column.

CellContent class

Describes how the item list displays the content of cells in the column

CellContentAlignment enumeration

Defines cell content alignment.

HeaderContent class

Represents a column header definition.

IColumnIndicator interface

Defines an interface of a column indicator.

FieldMetadata class

Contains information about a single field.

Field Type ID enumeration

Defines the number identification for field types.

Field Value The value of a field on the viewModel. The type and structure of this value varies depending on the field type.

Filter Types enumeration

Defines the types of filters that can be used in an item list.

QueryRequest class

Contains request details for a query method.

Filter class

Represents a single filter applied to a request.

Condition class

Represents a single condition of a filter.

Sort class

Represents a sort definition.

QueryResponse class

Represents a response from the Query method.

itemListDataProvider object

Used by single and multiple list picker components to retrieve data.

itemListSettingPersistenceService object

Used by single and multiple list picker components to store and retrieve their item list settings.

ItemListMetadata object

Used by Relativity Forms to determine how to render an item list.

Item List State class

Contains the current state of the item list.

Item List Types enumeration

Defines types of item list columns.

Date Formats Values

Values used to determine how date-time fields should be displayed.

Relativity object

Represents the structure of a Relativity Choice or Object.

ReadData object

Represent the field-value data used to populate the form.

ExitDialog class

Represents the windows alert dialog.

RuntimeConfig class

Represents specific Relativity configurations that are used for communication between the forms application and Relativity.

## Filter

### eventNames object

Represents the event names used in the Relativity Forms API. For convenience, the event names on the following object are sorted in property order.

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
const EVENT_NAMES = {

    CREATE_ACTION_BAR: "createActionBar",

    CREATE_CONSOLE: "createConsole",

    EVENT_HANDLERS_REGISTERED: "eventHandlersRegistered",

    HYDRATE_LAYOUT: "hydrateLayout",

    HYDRATE_LAYOUT_COMPLETE: "hydrateLayoutComplete",

    ITEM_LIST_MODIFY_ACTIONS: "itemListModifyActions",

    ITEM_LIST_MODIFY_COLUMNS: "itemListModifyColumns",

    ITEM_LIST_RELOADED: "itemListReloaded",<br />    OVERRIDE_PICKER_DATASOURCE: "overridePickerDataSource",

    PAGE_INTERACTION: "pageInteraction",

    PAGE_LOAD_COMPLETE: "pageLoadComplete",

    PAGE_UNLOAD: "pageUnload",

    POST_DELETE: "postDelete",

    POST_OBTAIN_ADDITIONAL_DATA: "postObtainAdditionalData",

    POST_SAVE: "postSave",

    PRE_DELETE: "preDelete",

    PRE_SAVE: "preSave",

    REPLACE_DELETE: "replaceDelete",<br />    REPLACE_FILE_ACTIONS: "replaceFileActions",

    REPLACE_GET_NEW_OBJECT_INSTANCE: "replaceGetNewObjectInstance",

    REPLACE_OBTAIN_ADDITIONAL_DATA: "replaceObtainAdditionalData",

    REPLACE_READ: "replaceRead",

    REPLACE_READ_DELETE_DEPENDENCY_LIST: "replaceReadDeleteDependencyList"

    REPLACE_SAVE: "replaceSave",<span class="span_1">Item List Types enumeration</span>

    TRANSFORM_LAYOUT: "transformLayout",

    UPDATE_ACTION_BAR: "updateActionBar",

    UPDATE_CONSOLE: "updateConsole",

    VALIDATE_SAVE: "validateSave",

    VALIDATION: "validation"

};
```

### popupControlApi object

Provides functionality for closing and accessing properties of a pop-up window.

#### Syntax

Copy

```text
1
2
3
4
5
const popupControlApi = {

     closePopup,          // Function

     isPopupSafeAndLive,  // Function

     popup                // Window

}
```

#### Properties

Property

Description

function closePopup()

Closes the pop-up window referenced by popupControlApi.popup object, when it's safe to do so. This function returns an undefined value.

function isPopupSafeAndLive()

Indicates whether it's safe to the properties of the pop-up window from within the opening or parent Relativity Form. This function returns a Boolean value, which is false if the pop-up window is already closed or if accessing the properties of the pop-up window cause exceptions.

Window popup

Represents the Window object returned by the window.open function called from a relativityFormsPopup method , such as openAdd(), openEdit(), or openView(). For more information, see Window on the MDN web docs site.

### Popup eventHandlerFactory function

Creates event handlers that run within a pop-up window created by invocations of methods on the convenienceApi.relativityFormsPopup.

The Add(), Edit(), and View() methods all take an optional eventHandlerFactory: Function property. This mechanism facilitates communication between the opener and pop-up Relativity Forms applications. It exposes the ability to add event handlers to a pop-up instance of Relativity Forms when the window is opened.

The factory function has the following signature:

Copy

```text
1
function eventHandlerFactory(popupControlApi, popupEventNames, popupConvenienceApi)
```

#### Parameters

Parameter

Description

popupControlApi: Object

Returns a popupControlApi Object instance from the relativityFormsPopup { openAdd, openEdit, openView } call to which this factory function is passed. For more information, see popupControlApi object .

popupEventNames: Object

The eventNames object supplied by the Relativity Forms application for the pop-up window. The contents of this object are identical to those passed to the event handlers IIFE. However, the source of this object is the Relativity Forms application for the pop-up window rather than the opener. For more information, see eventNames object .

popupConvenienceApi: Object

The popup window's Relativity Forms application's instance of a convenienceApi object .

#### Return type

An event handler object. See Relativity Forms API for more information.

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
22
23
24
25
26
27
28
29
(function(eventNames, convenienceApi) {

    var eventHandlers = {};



    eventHandlers[eventNames.PAGE_LOAD_COMPLETE] = function() {

        console.log("main PAGE_LOAD_COMPLETE called");

        var popupMode = "openView";



          // the popup eventHandlerFactory function, passed as a parameter for relativityFormsPopup

        var eventHandlerFactory = function(popupControlApi, popupEventNames, popupConvenienceApi) {

            var popupEventHandlers = {};

            popupEventHandlers[popupEventNames.PAGE_LOAD_COMPLETE] = function() {

                console.log("popup PAGE_LOAD_COMPLETE called");

            };

            return popupEventHandlers;

        };



        var openArgs = {

            workspaceId: this.workspaceId,

            artifactTypeId: <Number>,

            artifactId: <Number>,

            parentArtifactId: <Number>,

            eventHandlerFactory: eventHandlerFactory

        };



        convenienceApi.relativityFormsPopup[popupMode](openArgs);

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

### ColumnDefinition class

The base class that describes a column of data. This object is extended by the ItemListColumn class. If Event Handler code is defining a custom ItemListDataProvider.getColumns function, it will need to return column objects in the format described here.

#### Syntax

See the syntax sample for ItemListColumn .

#### Properties

Property

Type

Description

id

String | Null

The identifier for a column.

actAsAdvanced

Boolean

Set to true if the column acts as advanced, or set to false if it doesn't.

defaultWidth

Number

The default column width.

content

CellContent

The cell content definition.

contentAlignment

CellContentAlignment | Null

The cell content alignment.

headerContent

HeaderContent

The header content.

highlighted

Boolean

Set to true if the column is highlighted, or set to false if it isn't.

minWidth

Number

Minimum column width.

resizable

Boolean

Set to true if the column is resizable, or set to false if it isn't.

separatorVisible

Boolean

Set to true if the right border of the column is visible, set to false if it isn't.

title

String | Null

The column title.

width

Number

The column width.

wrapped

Boolean

Set to true if the content in the column cell is wrapped, or set to false if it isn't.

### ItemListColumn Properties

An ItemListColumn extends the ColumnDefinition class and contains the following additional properties:

Property

Type

Description

filter

Filter

A column filter.

filterable

Boolean

If true, the column can be filtered using the item list's column filters. If false, the column cannot be filtered and the filters will be hidden.

filterAdvanced

Boolean

If true, the column can be filtered using the advanced condition flyout. If false, the column advanced filter option will be hidden.

filterTitle

String | Null

Text that is shown when users hover over a drop-down filter.

sortable

Boolean

If true, the column can be sortable via clicking the column header. If false, the sort of the column can not change.

sortDirection

SortDirection | Null

The sort direction of a column. For more information, see Sort class. If Null the column header will appear as if it was not sorted.

#### Methods

None

### CellContent class

Configuration that describes how the item list displays the content of cells in the column. This may need to be defined in Event Handler code if a custom ItemListDataProvider.getColumns method is being defined since it defines how those columns will show information.

#### Properties

Property

Type

Description

dataLocation

String | Null

The data location property for the column that is in the item list row data.

For example, if the item list is given row data in this format:

Copy

```text
1
{ "col_A": "row_N col_A value", "col_B": "row_N col_B value" }
```

Setting the dataLocation value to "col_A" will mean the item list column will show the value "row_N col_A value" .

formatDefinitions

Array<Object> | Null

(Optional) An array of configuration objects that transform the value of the cell in the item list row data to the content displayed in the cell. Formatting chains can be defined by defining an array of objects here.

There are a number of built-in formatters that can be used on a column in the item list:

- BooleanValue - defines the text displayed for true/false values in the item list data.

- Custom - user-defined formatter that returns either an HTML element or a text string to show in the cell

- DateTime - displays ISO 8601 date-time strings in a user-friendly locale.

- HtmlText - allows HTML strings in the item list data to be shown as HTML elements in the item list.

- Image - shows an image in the cell.

- SingleValue - shows in the cell a single value from the item list data.

- MultipleValue - shows multiple values from the item list data as delimited text in the cell.

- TruncatedText - applies a maximum length to any text shown in the cell.

##### Example

CellContent formatDefinitions examples Copy

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
// No formatting

// input item list data: [{ "col_A": "One" }, { "col_A": "Two" }]

// rendered item list data: "One", "Two"

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: Null

}



// BooleanValues

// input item list data: [{ "col_A": true }, { "col_A": false }]

// rendered item list data: "Yes", "No"

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "BooleanValue",

        options: {

            trueLabel: "Yes",

            falseLabel: "No"

    }]

}



// Custom

// input item list data: [{ "firstName": "Salt", "lastName": "Pepper" }]

// rendered item list data: <span>Salt Pepper</span> element

var cellContent = {

    dataLocation: "firstName",

    formatDefinitions: [{

        name: "BooleanValue",

        options: {

            format: function(content, dataItem) {

                console.log(content);    // "Salt"

                console.log(dataItem);    // { "firstName": "Salt", "lastName": "Pepper" }



                var spanElement = document.createElement("span");

                spanElement.textContent = content + " " + dataItem["lastName"];

                return spanElement;

            }

    }]

}



// DateTime

// input item list data: [{ "col_A": "2009-04-27T18:44:50.217" }]

// rendered item list data: "4/27/2009"

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "DateTime",

        options: {

            includeTime: false,

            locale: "en-US"

    }]

}



// HtmlText

// input item list data: [{ "col_A": "<i>Italic Text</i>" }]

// rendered item list data: "Italic Text" in italics

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "HtmlText",

        options: {}

    ]

}



// Image

// input item list data: [{ "col_A": { "imgSrc": "./my/cat/picture.jpg", "imgAlt": "cute cat picture" }]

// rendered item list data: <img src="./my/cat/picture.jpg" alt="cute cat picture"> element

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "Image",

        options: {

            srcLocation: "imgSrc",

            alt: "imgAlt"

        }

    ]

}



// SingleValue

// input item list data: [{ "col_A": { "Inner Key": "Inner Value" }]

// rendered item list data: "Inner Value"

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "SingleValue",

        options: {

            dataLocation: "Inner Key"

        }

    ]

}



// MultipleValue

// input item list data: [{ "col_A": [{ "id": "1", "value": "One" }, { "id": "2", "value": "Two" }] }]

// rendered item list data: "One;Two"

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "MultipleValue",

        options: {

            dataLocation: "Inner Key",

            idLocation: "",

            delimiter: ";"

        }

    ]

}



// TruncatedText

// input item list data: [{ "col_A": "Very long text" }]

// rendered item list data: "Very..."

var cellContent = {

    dataLocation: "col_A",

    formatDefinitions: [{

        name: "TruncatedText",

        options: {

            maxLength: 7

        }

    ]

}
```

### CellContentAlignment enumeration

Defines cell content alignment.

#### Enums

Name

Value

Description

LEFT

0

Indicates left alignment.

CENTER

1

Indicates center alignment.

RIGHT

2

Indicates right alignment.

### HeaderContent class

Represents a column header definition. When creating your own ItemListDataProvider.getColumns method and need to fill in this field, it is recommended to set the indicators parameter to Null , as IColumnIndicator instances cannot be created manually.

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
var toolbarHeaderContentElement = document.getElementById("header");





var headerContent = {

    clickable: true,

    indicators: Null,

    title: "Title",

    toolbarContent: toolbarHeaderContentElement

};
```

#### Properties

Property

Type

Description

clickable

Boolean

Set to true if the column header is clickable, or set to false if it isn't clickable.

indicators

Array<IColumnIndicator> | Null

A list of column indicators.

title

String | Null

The header cell title.

toolbarContent

Element

The column header toolbar content.

#### Methods

None

### IColumnIndicator interface

Defines an interface of a column indicator. Column indicators are typically used to add indicator icons to column headers, such as sort and filter icons. This cannot be manually created by users, but it is detailed here for when you're creating your own ItemListDataProvider.getColumns method. Instead, it is used internally to generate sort and filter icons for column headers for applicable item lists.

#### Methods

##### render()

Returns an indicator element as a value suitable for the consumption of Hyperscript function of SkateJS.

##### Parameters

None

##### Return type

String | HTMLElement | Array | Null

### FieldMetadata class

Contains information about a single field.

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
var fieldMetadata = {

     artifactID: 0,

     artifactViewFieldID: 0,

     associativeObjectTypeID: 0,

     columnName: "Name",

     fieldTypeID: 0, // fixed length text

     filterType: "Choice",

     headerName: "Header",

     itemListType: "Text",

     isSystem: false

};
```

#### Properties

Property

Type

Description

artifactID

Number | Null

The artifact ID of a field.

artifactViewFieldID

Number | Null

The artifact ID of the view field.

associativeObjectTypeID

Number | Null

The object type ID of an associated object. It is used for single or multiple object fields.

columnName

String | Null

The name of a column.

fieldTypeID

Number | Null

The field type ID. For a list of valid values, see Field Type ID enumeration .

filterType

String | Null

A filter type. For a list of valid values, see Filter Types enumeration .

headerName

String | Null

A header name.

itemListType

String | Null

An item list type. For a list of valid values, see Item List Types enumeration .

isSystem

Boolean | Null

Set to true if the field is a system field, or set it to false if it isn't a system field.

#### Methods

None

### Field Type ID enumeration

Defines the number identification for field types.

#### Enums

Name

Value

Description

FIXED_LENGTH_TEXT

0

Fixed length text field

WHOLE_NUMBER

1

Whole number field

DATE

2

Date/time field

BOOLEAN

3

Yes/No field

LONG_TEXT

4

Long text field

SINGLE_CHOICE

5

Single choice field

DECIMAL

6

Decimal field

CURRENCY

7

Currency field

MULTI_CHOICE

8

Multiple choice field

FILE

9

File field

SINGLE_OBJECT

10

Single object field

USER

11

User field

LAYOUT_TEXT

12

Layout text

MULTI_OBJECT

13

Multiple object field

### Field Value

The type and structure of a field's 'value' property varies depending on the field type.

Field Type

FieldValue

Fixed-Length Text

String

Whole Number

Number

Date String

Boolean (Yes/No)

Boolean|Undefined

If the field is not set, FieldValue is undefined

Long Text

String

Do not use the value of this field to save to the database. The value will be truncated if it is longer than the value of the MaximumNumberOfCharactersSupportedByLongText instance setting. The full value must be fetched via an additional API call. We do this because the values of long text fields can be several megabytes or even gigabytes long.

Single Choice Object

Object

Copy

```text
1
2

{ ArtifactID: <number>, ItemSecured: <boolean>, Name: <string> }
```

Decimal String

Currency String

Multiple Choice

Object

Copy

```text
1
{ ItemSecured: <boolean>, Objects: Array<object> [{ArtifactID: <string>, Guids: Array<object>[{}], Name: <string> }]
```

File

Object

Copy

```text
1
{FileID: <number>, FileName: <string>}
```

Single Object

Object

Copy

```text
1
{ArtifactID: <number>, ItemSecured: <boolean>, Name: <string>}
```

User

Object

Copy

```text
1
{ArtifactID: <number>, Name: <string>}
```

Custom Text String

Multiple Object

Object

Copy

```text
1
{ ItemSecured: <boolean>, Objects: Array<object>[{ ArtifactID: <string>, Guids: Array<object>[{}], Name: <string>, ItemSecured: <boolean> }] }
```

### Filter Types enumeration

Defines the types of filters that can be used in an item list.

#### Enums

Name

Value

Description

BOOLEAN

"Boolean"

Boolean filter

CHOICE

"Choice"

Choice filter

CUSTOMONLY

"CustomOnly"

Custom filter only

LIST

"List"

List filter

NONE

"None"

None

POPUP

"Popup"

Popup picker

SEARCH

"Search"

Search

### QueryRequest class

Contains request details for an item list query.

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
var QueryRequest = {

     startIndex: 0,

     pageSize: 0,

     filters: [filter1, filter2],

     sorts: [sort1, sort2],

     idsToInclude: [0, 1, 2],

     idsToExclude: [3, 4, 5]

};
```

#### Properties

Property

Type

Description

startIndex

Number

The index of the first item to return.

pageSize

Number

The number of items to return.

filters

Array<Filter>

A list of filters to apply. See Filter class.

sorts

Array<Sort>

A list of sort properties to apply. See Sort class.

idsToInclude

Array<Number>

The identifiers for items to include in a query.

idsToExclude

Array<Number>

The identifiers for items to exclude from a query.

#### Methods

None

### Filter class

Represents a single filter applied to a request.

#### Syntax

Copy

```text
1
var filter = new rwc.dataManagement.conditions.Filter("advancedText", [condition], true);
```

#### Properties

Property

Type

Description

field

String

A field name.

condition

Condition | Array<Condition>

The filter conditions.

isAdvanced

Boolean

Set to true from an advanced condition modal, or set to false from other modals.

#### Methods

None

### Condition class

Represents a single condition of a filter.

#### Syntax

Copy

```text
1
2
3
4
5
var condition = {

     operator: "is less than",

     value: 10,

     displayValue: "is less than 10"

};
```

#### Properties

Property

Type

Description

operator

String

A condition operator. Possible values:

##### Operators

Value

any of these

none of these

all of these

not all of these

between

is

is not

is set

is not set

is less than

is less than or equal to

is greater than

is greater than or equal to

is like

is not like

is in

value

Number | String | Array<Number | String> | Null

A condition value or a list of values.

displayValue

String | Array<String>

A display value or a list of display values.

#### Methods

None

### Sort class

Represents sort definition.

#### Syntax

Copy

```text
1
2
3
4
var sort = {

     column: "Name",

     direction: "asc"

};
```

#### Properties

Property

Type

Description

column

String

A column name.

direction

String

A sort direction. Valid values:

##### Sort Direction

Value Direction

asc

Ascending Order

desc

Descending Order

#### Methods

None

### QueryResponse class

Represents a response from the Query method. The entries in the Objects field are mapped to the Results field such that every entry has the ArtifactID along with any requested fields (e.g. Name ) as its properties.

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
var queryResponse = {

     Results: [

          {

               "Name": "test1 name",

               "ArtifactID": 1039665

          },

          {

               "Name": "test2 name",

               "ArtifactID": 1039666

          }

     ],

     TotalCount: 2,

     CurrentStartIndex: 1,

};
```

#### Fields

Field

Type

Description

Results

Array<Object>

An array of objects. Each object represents a record in the result set.

TotalCount

Number

The total count of the items returned.

CurrentStartIndex

Number

The index of the first item returned. It starts at one.

#### Properties

None

#### Methods

None

### itemListDataProvider object

The itemListDataProvider is a part of the multi/single-list picker component that is used to retrieve data and provide the information required to render its inner lists.

The intention is for users to construct the object themselves and then use the custom provider to build SingleListPickerModal or MultiListPickerModal .

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
itemListDataProvider = {

     getFieldMetadata,                    // function

     getColumns,                              // function

     getTextIdentifierColumnName,     // function

     query,                                   // function

     getValuesByIds                         // function

}
```

#### Methods

See the following subsections for information about these methods:

- getFieldMetadata(String: fieldName)

- getColumns(Function: itemListReloadHandler)

- getTextIdentifierColumnName()

- query(Object: request, Array<Object>|Null: columns)

- getValuesByIds(Array<Number>: ids)

##### getFieldMetadata(String: fieldName)

This method returns a FieldMetadata object for a given field name. The multi-list picker component uses this method to retrieve information about fields.

###### Parameters

Parameter

Type

Description

fieldName

String

The field name to get the metadata for.

###### Return Type

Promise<FieldMetadata>

###### Syntax

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
var itemListDataProvider = {

     // ...

     getFieldMetadata: function(fieldName) {

          var metaData = {

               artifactID: 0,

               artifactViewFieldID: 0,

               associativeObjectTypeID: 0,

               columnName: "Name",

               fieldTypeID: 0, // fixed length text

               filterType: "None",

               headerName: Null,

               isSystem: false

               itemListType: "Text",

          };

          return convenienceApi.promiseFactory.resolve(metaData);

     },

     // ...

};
```

##### getColumns(Function: itemListReloadHandler)

This method returns an array of ItemListColumn objects. These objects are used by the inner item lists of the multi-list picker component to render columns. The itemListReloadHandler reloads item list data when invoked.

###### Parameters

Parameter

Type

Description

itemListReloadHandler

Function

If defined, this function is intended to reload the item list associated with this data provider. itemListReloadHandler should be called if this ItemListDataProvider needs to reload the item list after getting columns.

###### Return Type

Promise<Array< ItemListColumn >>

###### Syntax

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
var itemListReloadHandler = function() {

     console.log("Reloading item list");

};





var itemListDataProvider = {

     // ...

     getColumns: function(itemListReloadHandler) {

          var toolbarContentElement = document.createElement("span");

        toolbarContentElement.innerText = "Content of Toolbar Content element";

        var noop = function () {};

          var itemListColumn1 = {

               id: "0",

            actAsAdvanced: false,

            defaultWidth: 150,

            content: {

                comparer: Null,

                dataLocation: "ArtifactID", // key to look for in each data entry

                formatDefinition: Null

            },

            contentAlignment: Null,

            headerContent: {

                clickable: false,

                indicators: Null,

                title: Null,

                toolbarContent: toolbarContentElement

            },

            highlighted: false,

            minWidth: 75,

            resizable: true,

            separatorVisible: true,

            title: "Artifact ID",

            width: 150,

            wrapped: true,



            filter: Null,

            filterable: false,

            filterAdvanced: false,

            filterTitle: Null,

            sortable: false,

            sortDirection: Null,

          };



          return convenienceApi.promiseFactory.resolve([

               itemListColumn1,

               // ...

          ]);

     },

     // ...

};
```

###### Example

Copy

```text
1
2
3
4
5
6
7
var itemListReloadHandler = function(value) {

     console.log("itemListReloadHandler called with value: " + JSON.stringify(value));

};



itemListDataProvider.getColumns(itemListReloadHandler).then(function(itemListColumn) {

     console.log("itemListColumn: " + JSON.stringify(itemListColumn));

});
```

##### getTextIdentifierColumnName()

This method returns the name of the column that is the identifier of the row, usually the first column that is seen. For example Name or ArtifactID .

###### Parameters

None

###### Return Type

String

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListDataProvider = {

     // ...

     getTextIdentifierColumnName: function() {

          return "Name";

     },

     // ...

};
```

###### Example

Copy

```text
1
var textIdentifierColumnName = itemListDataProvider.getTextIdentifierColumnName();
```

##### query(Object: request, Array | Null: columns)

This method returns a promise that resolves to an object that has a shape which is the same as QueryResponse . A request variable is an object that represents the body of the query. The columns variable is an array of objects that defines columns to include in the result set.

###### Parameters

Parameter

Type

Description

request

Object< QueryRequest >

The item list data requestQueryRequest that can drive the query logic.

columns

Array< temListColumn > | Null

An array of column data that can be used to drive the query logic.

###### Return Type

Promise< QueryResponse >

###### Syntax

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
var itemListDataProvider = {

     // ...

     query: function(request, columns) {

          var results = [

               {

                    "Name": "test1 name",

                    "ArtifactID": 1

               },

               {

                    "Name": "test2 name",

                    "ArtifactID": 2

               }

          ];





          return convenienceApi.promiseFactory.resolve({

               "Results": results,

               "TotalCount": results.length,

               "CurrentStartIndex": 1

          });

     },

     // ...

};
```

###### Example

Copy

```text
1
2
3
itemListDataProvider.query(request, columns).then(function(result) {

     console.log("results: " + JSON.stringify(result));

});
```

##### getValuesByIds(Array<Number>: ids)

This method returns a promise that resolves to an array of data items having given identifiers.

###### Parameters

Parameter

Type

Description

ids

Array<Number>

The object identifiers

######

Return Type

Promise<QueryResponse.Results>

###### Syntax

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
var itemListDataProvider = {

     // ...

     getValuesByIds: function(ids) {

          return [

               {

                    "Name": "test1 name",

                    "ArtifactID": 1

               },

               {

                    "Name": "test2 name",

                    "ArtifactID": 2

               }

          ];

     },

     // ...

};
```

###### Example

Copy

```text
1
2
3
itemListDataProvider.getValuesByIds(ids).then(function(values) {

     console.log("values: " + JSON.stringify(values));

});
```

### itemListSettingPersistenceService object

Used by single and multiple list picker components to store and retrieve their item list settings.

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
itemListSettingPersistenceService = {

     getGridStyle,                    // function

     getFiltersVisible,               // function

     getItemListState,               // function

     getItemListStateOrDefault,     // function

     getItemListColumnWidths,     // function

     setGridStyle,                    // function

     setFiltersVisible,               // function

     setItemListState,               // function

     setItemListColumnWidth,          // function

}
```

#### Methods

See the following subsections for information about these methods:

- getGridStyle()

- getFiltersVisible(String: itemListKey, Number: workspaceId)

- getItemListState(String: itemListKey)

- getItemListStateOrDefault(String: itemListKey, String: columnWidthsKey)

- getItemListColumnWidths(String: columnWidthsKey)

- setGridStyle(Boolean: gridStyleValue)

- setFiltersVisible(String: itemListKey, Boolean: filtersVisibleValue)

- setItemListState(String: itemListKey, Object: itemListStateValue)

- setItemListColumnWidth(String: itemListKey, String: columnKey, Number: width)

##### getGridStyle()

Gets the grid style setting for a particular item list.

###### Parameters

None

###### Return type

Promise<Boolean> - returns the grid style setting.

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     getGridStyle: function() {

          return convenienceApi.promiseFactory.resolve(false);

     },

     // ...

};
```

###### Example

Copy

```text
1
2
3
itemListSettingPersistenceService.getGridStyle().then(function(value){

    console.log("The grid style is currently set to" + value);

});
```

##### getFiltersVisible(string itemListKey, number workspaceId)

Gets the filters visible setting for a particular item list.

###### Parameters

Parameter

Type

Description

itemListKey

String

A unique identifier string for the item list.

workspaceId

Number

The current workspace ID.

###### Return type

Promise<Boolean>

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     getFiltersVisible: function(itemListKey, workspaceId) {

          return convenienceApi.promiseFactory.resolve(false);

     },

     // ...

};
```

###### Example

Copy

```text
1
2
3
itemListSettingPersistenceService.getFiltersVisible(itemListKey, this.workspaceId).then(function(value){

    console.log("The filter visibility setting is currently set to " + value);

});
```

##### getItemListState(string itemListKey)

Gets the item list state.

###### Parameters

Parameter

Type

Description

itemListKey

String

A unique identifier string for the item list.

###### Return type

An Item List State object.

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     getItemListState: function(itemListKey) {

          return convenienceApi.promiseFactory.resolve(false);

     },

     // ...

};
```

###### Example

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
var itemListState = itemListSettingPersistenceService.getItemListState(itemListKey);

/*

itemListState = {

     sorts:               Array<Sort>,

     filters:          Array<Filter>,

     data:               Array<Object>,

     startIndex:          Number,

     pageSize:          Number,

     columnWidths:     Number

}

*/
```

##### getItemListStateOrDefault(string itemListKey, string columnWidthsKey)

Gets item list state or a new instance of the state object.

###### Parameters

Parameter

Type

Description

itemListKey

String

A unique identifier string for the item list.

columnWidthsKey

String

A unique identifier string for the persisted columns.

###### Return type

An Item List State object.

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     getItemListStateOrDefault: function(itemListKey, columnWidthsKey) {

          return convenienceApi.promiseFactory.resolve(false);

     },

     // ...

};
```

###### Example

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
var itemListState = itemListSettingPersistenceService.getItemListStateOrDefault(itemListKey, columnWidthsKey);

/*

itemListState = {

     sorts:               Array<Sort>,

     filters:          Array<Filter>,

     data:               Array<Object>,

     startIndex:          Number,

     pageSize:          Number,

     columnWidths:     Number



}

*/
```

##### getItemListColumnWidths(string columnWidthsKey)

Persists item list column width.

###### Parameters

Parameter

Type

Description

columnWidthsKey

String

A unique identifier string for the item list.

###### Return type

Map<String, Number> | Null - returns the column width.

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     getItemListColumnWidths: function(columnWidthsKey) {

          return convenienceApi.promiseFactory.resolve(false);

     },

     // ...

};
```

###### Example

Copy

```text
1
2
3
4
5
6
var columnWidths = itemListSettingPersistenceService.getItemListColumnWidths(columnWidthsKey);

if (!!columnWidths) {

     columnWidths.forEach(function(value, key) {

          console.log("key: " + key + ", value: " + value);

     });

}
```

##### setGridStyle(boolean gridStyleValue)

Persists grid style value for all item lists.

###### Parameters

Parameter

Type

Description

gridStyleValue

Boolean

The grid-style value to persist.

###### Return type

None

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     setGridStyle: function(gridStyleValue) {

          // write grid style value boolean to persistence

     },

     // ...

};
```

###### Example

Copy

```text
1
itemListSettingPersistenceService.setGridStyle(true);
```

##### setFiltersVisible(itemListKey: String, filtersVisibleValue: Boolean)

Persists filter visibility for a specific item list.

###### Parameters

Parameter

Type

Description

itemListKey

String

A unique identifier string for the item list.

filtersVisibleValue

Boolean

The filter visibility value to persist.

###### Return type

None

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     setFiltersVisible: function(itemListKey, filtersVisibleValue) {

          // write filters visible value boolean to persistence based on itemListKey

     },

     // ...

};
```

###### Example

Copy

```text
1
itemListSettingPersistenceService.setFiltersVisible(itemListKey, true);
```

##### setItemListState(string itemListKey, object itemListStateValue)

Persists item list state.

###### Parameters

Parameter

Type

Description

itemListKey

String

A unique identifier string for the item list.

itemListStateValue

Object

An item list state to persist.

###### Return type

None

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     setItemListState: function(itemListKey, itemListStateValue) {

          // write item list state object to persistence based on itemListKey

     },

     // ...

};
```

###### Example

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
var itemListState = {

     filters:     Array<Filter>,

     pageSize:     Number,

     sorts:          Array<Sort>,

     startIndex:     Number

};



itemListSettingPersistenceService.setItemListState(itemListKey, itemListState);
```

##### setItemListColumnWidth(string itemListKey, string columnKey, number width)

Persists item list column width.

###### Parameters

Parameter

Type

Description

itemListKey

String

A unique identifier string for the item list.

columnKey

String

A unique identifier string for the column.

width

Number

The column width.

###### Return type

None

###### Syntax

Copy

```text
1
2
3
4
5
6
7
var itemListSettingPersistenceService = {

     // ...

     setItemListColumnWidth: function(itemListKey, columnKey, width) {

          // write item column width value to persistence based on itemListKey and columnKey

     },

     // ...

};
```

###### Example

Copy

```text
1
itemListSettingPersistenceService.setItemListColumnWidth(itemListKey, columnKey, 10);
```

### ItemListMetadata object

An object that tells Liquid how to render an item list. At minimum, a FieldCollection is required. The other properties are optional.

Property

Type

Description

FieldCollection

Array<ViewField>

Any array of ViewFields to display in the item list. Each ViewField represents a column.

ActiveView

Object | Null

Object describing the active view. The FieldIds: Array<Number> property will be used for setting the visible fields in the item list.

See Layout representation for Relativity forms.

If not set, then only the TextIdentifier field will be shown in the list.

ViewFieldWidthCollection

Object

An object containing ViewField.AvfID : Width key:value pairs.

Example:

Copy

```text
1
2
3
4
5
{

    "143245": 100,

    "143247": 40,

    "100004": 75

}
```

### Item List State class

An object that contains the current state of the item list including sort, filter, and pager information.

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
var itemListState = {

     startIndex: 1,

     pageSize: 1,

     filters: [{

          field: "Name",

          condition: {

               operator: "is less than",

               value: 10,

               displayValue: "is less than 10"

          },

          isAdvanced: false

     }],

     sorts: [{

          column: "Column Name",

          direction: "asc"

     }],

     data: [

          {

               "Name": "test1 name",

               "ArtifactID": 1

          },

          {

               "Name": "test2 name",

               "ArtifactID": 2

          }

     ],

     columnWidths: new Map(

          ["one", 100],

          ["two", 200]

     )

};
```

#### Properties

Property

Type

Description

startIndex

Number

The index of the first item to return.

pageSize

Number

The number of items to return.

filters

Array<Filter>

The filters to apply. For more information, see Filter class.

sorts

Array<Sort>

The sort properties to apply. For more information, see Sort class.

data

Array<Object>

An array of data objects to be displayed in the grid.

columnWidths

Map<String, Number>

A map for looking up a column width by its key.

#### Methods

None

### Item List Types enumeration

Defines types of item list columns.

#### Enums

Name

Value

Description

ALCAWARESTATICFIELD

ACLAwareStaticField

The edit column

BOOLEAN

Boolean

Yes/No column

CODETEXT

CodeText

Code text column

DATETTIME

DateTime

Date and time column

DATETIMESYSTEM

DateTimeSystem

Date and time column where the time contains timezone information.

FILE

File

File column

FILEICON

FileIcon

File icon column

FULLTEXT

FullText

Full-text field column

MULTITEXT

MultiText

Multiple text column

MULTIVALUETEXT

MultiValueText

Multiple value text column

NUMBER

Number

Number column

SECURITY

Security

Security column

TEXT

Text

Text column

USER

User

User column

### Date Formats

DateTime items support multiple formats in forms. One letter values correspond to different date formats.

Value

Type

Description

d

String

Short date format, ie "M/d/yyyy".

D

String

Full date format, ie "dddd, MMMM dd, yyyy".

g

String

Short date-time format, ie "M/d/yyyy, h:mm tt".

G

String

Full date-time format, ie "M/d/yyyy, h:mm:ss tt".

t

String

Short time format, ie "h:mm tt".

### Relativity object

Represents the structure of a Relativity Choice or Object.

#### Properties

Property

Type

Description

ArtifactID

Number

Represents the artifact ID of a Relativity Object or Choice.

Name

String|Number|Null

Represents the name that will be displayed for an Object or Choice field value. (Only used in the UI, the name will not be saved).

### ReadData object

Represent the field-value data used to populate the form.

#### Properties

Property

Type

Description

modelData

Object

A key-value Object where the Object's keys are fieldIds whose values are the fieldId's field values.

For example, if you were to use the Object Manager REST API to fetch information, you would take every entry in the Object.FieldValues property and create an object where the key is a Field's ArtifactID and the value is the Field's Value. For more information about Fields in the Object Manager, see the sample JSON responses in Retrieve field values for a Document object or RDO from Object Manager API in REST.

The end result should look like this:

Copy

```text
1
2
3
4
5
{

    1234567: "Some value", // field ID referencing a fixed length field

    8901234: [1, 2, 3], // field ID referencing a multiple choice field

    5678901: 10 // field ID referencing a whole number field

}
```

#### Item Security

For single and multiple object fields, if the value or one of the values is an object the current user does not have access to, it will have the property "ItemSecured" with a value of true. So if your modelData looks similar to the following data, the value of that field will display as "[Item Secured]" for Single Object fields and "[Items(s) Secured]" (in addition to any items you do have access to) for Multiple Object fields. In edit mode, if a multi-object field has secured items, it will not be editable.

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
{

    2345678: { // some single object field

        "ArtifactID": 0,

        "Guids": [],

        "ItemSecured": true

    },

    9012345: [ // some multi object field

        {

            // the name of this object will appear

            "ArtifactID": 6789012,

            "Guids": [],

            "Name": "An unsecured item",

            "ItemSecured": false

        },

        {

            "ArtifactID": 0,

            "Guids": [],

            "ItemSecured": true

        },

        {

            "ArtifactID": 0,

            "Guids": [],

            "ItemSecured": true

        }

    ]

}
```

### ExitDialog class

Represents the window alert dialog that is displayed when navigating away from and edit/add form that contains unsaved changes.

#### Methods

See the following subsections for information about these methods:

- activate(string message)

- trigger(string message)

##### activate(message: String)

Sets an ExitDialog with a message that will be displayed when the user navigates from edit/add form page with unsaved data on it. This uses the activate Aurelia hook.

###### Parameters

Parameter

Description

message: String

The text that the dialog will display.

###### Return type

Void

###### Example

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

       this.exitDialog.activate("Unsaved Data!!! Continue?");

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

##### trigger(message: String)

Displays the browser's confirmation dialog on the page and returns whether or not the user clicked the confirmation button in the dialog. The execution of JavaScript is stopped until the user confirms or cancels the dialog.

###### Parameters

Parameter

Description

message: String

The text that the dialog will display.

###### Return type

Boolean

###### Example

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



    eventHandlers[eventNames.PAGE_LOAD_COMPLETE] = function() {

       var continue = this.exitDialog.trigger("Error Occurred. Do you wish to continue??");

       if(continue)

       {

          // Do something to try to resolve error.

          console.log("Error Resolved");

       }

    };



    return eventHandlers;

}(eventNames, convenienceApi));
```

### RuntimeConfig class

Represents specific Relativity configurations that are used for communication between the forms application and Relativity. These properties are read-only.

#### Properties

Property

Type

Description

restBaseUrl

String

The base path for Relativity.Rest service endpoints. This does not include the hostname. For most environments, this will be /Relativity.Rest/

relativityBaseUrl

String

The base path for all of Relativity. This does not include the hostname. For most environments, this will be /Relativity/

csrfTokenFromPage

String

The CSRF (Cross-Site Request Forgery prevention) token. This should be used as the "X-CSRF-Header" when making HTTP requests to Relativity APIs

currencySymbol

String

The symbol that will be shown next to currency values. For example, '$' or ' €'

On this page

- Additional Forms API objects

- Summary of additional Forms API objects and functions

- Filter

- eventNames object

- popupControlApi object

- Popup eventHandlerFactory function

- ColumnDefinition class

- ItemListColumn Properties

- CellContent class

- CellContentAlignment enumeration

- HeaderContent class

- IColumnIndicator interface

- FieldMetadata class

- Field Type ID enumeration

- Field Value

- Filter Types enumeration

- QueryRequest class

- Filter class

- Condition class

- Sort class

- QueryResponse class

- itemListDataProvider object

- itemListSettingPersistenceService object

- ItemListMetadata object

- Item List State class

- Item List Types enumeration

- Date Formats

- Relativity object

- ReadData object

- ExitDialog class

- RuntimeConfig class


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
