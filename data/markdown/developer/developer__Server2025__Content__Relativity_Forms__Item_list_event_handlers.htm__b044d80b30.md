---
title: "Item list event handlers"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Item_list_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:32:04+00:00
sha256: cc69c1a69e8cef850b4d500d93065e148e8dcc6473dea8907511c97614cfcc1c
---

Item list event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Item list event handlers

The Relativity Forms API includes event handlers and classes used to manipulate item lists.

### Summary of item list event handlers

The following table lists the item list event handlers.

Event handler or class

Description

itemListModifyActions

Modifies the default action buttons for an item list.

itemListModifyColumns

Modifies columns in an item list.

itemListReloaded

Executes each time the item list is reloaded.

### Summary of item list event handler APIs and objects

The following table lists the item list APIs and related objects.

Event handler or class

Description

columnsApi

Provides methods for modifying columns on item list, such as the adding formatters, setting titles, or removing columns.

Item List Action button object

Describes an item list action button.

itemListActionsApi

Modifies action buttons on the item list.

View object

Identifies the current item list.

Visibility Rule class

Indicates the visibility of action buttons for an item list.

## Item List Event Handlers

### itemListModifyActions

This event is executed immediately before the Item List is rendered. It provides the opportunity to modify default action buttons for the Item List. If the event handler does not call the initialize, addAction or the addDefaultActions method on the itemListActionsApi object, the default action buttons will be added to the Item List.

The itemListModifyActions event also provides an opportunity to modify how the item list gets data. If the event handler does not call the setCustomGetDataFunction method on the itemListActionsApi object, the default method or retrieving item list data through the Object Manager API will be used.

The event handler is expected to perform one or more of the following tasks:

- setup the action buttons itself (by calling initialize, addAction or addDefaultActions methods).

- leave the Item List action bar intact (do not call initialize, addAction or addDefaultActions), thus triggering adding the default action buttons by the application.

- define a custom get-data function the item list will use to populate the item list. This will override the default behavior, which uses the Object Manager API to get data.

#### Syntax

Copy

```text
1
   function(itemListActionsApi: < object >, view: < object >)
```

#### Parameters

The following tables lists the input parameters:

Parameter

Description

itemListActionsApi: <object>

Modifies action buttons on the item list. For more information, see itemListActionsApi .

view: <object>

Identifies the current item list.

This object has these fields used for item list identification:

Field

Type

Description

ArtifactID

number

The artifact ID of the view.

Name

string

The name of the view.

ObjectTypeID

number

The artifact type ID of the object displayed in the view.

#### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

#### Example

See code samples for itemListActionsApi .

### itemListModifyColumns

Modifies columns in an item list through the columnsApi . This event is executed once per item list when it is added to the form.

#### Syntax

Copy

```text
1
   function(columnsApi: < object >, view: < object >)
```

#### Parameters

The following tables lists the input parameters:

Parameter

Description

columnsApi: <object>

Provides methods for modifying columns on item list, such as the adding formatters, setting titles, or removing columns. The ColumnsApi is exposed as a part of the event handler API. For more information, see columnsApi .

view: <object>)

Identifies the current item list.

This object has these fields used for item list identification:

Field

Type

Description

ArtifactID

number

The artifact ID of the view.

Name

string

The name of the view.

ObjectTypeID

number

The artifact type ID of the object displayed in the view.

#### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

#### Example

See code samples for columnsApi .

### itemListReloaded

Executes each time the item list is reloaded. The itemListReloaded event handler executes in the view model popup when the item list is reloaded and provides a way to read the results of the item list. For more information, see Popup eventHandlerFactory .

#### Syntax

Copy

```text
1
   function(data:  object )
```

#### Parameters

The following table lists the input parameters:

Parameter

Description

data: object

Describes the new item list startup data

This object has these fields:

Field

Type

Description

CurrentStartIndex

Number

The current starting index (1 is the first result).

Results

Array<object>

Array of item list row objects.

TotalCount

Number

The total amount of results.

#### Ambient variables

Name

Description

this

On execution of the event handler, Relativity Forms binds the value of the " this " keyword to an object which provides data and functionality related to the active form. For more information, see this Binding .

convenienceApi

Globally available to all event handlers is the active application's convenienceAPI object . For more information, see convenienceAPI object .

eventNames

Globally available to all event handlers is the active application's eventNames object . For more information, see eventNames object in Additional Forms API objects .

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
30
(function(eventNames, convenienceApi) {

     var eventHandlers = [];





     eventHandlers[eventNames.ITEM_LIST_RELOADED] = function(data) {

          console.log("Inside ITEM_LIST_RELOADED event handler");

          console.log(data);

          /*

               {

                    "CurrentStartIndex": 1,

                    "Results": [

                         {

                              "column1_name": "row1_column1_value",

                              "column2_name": "row1_column2_value"

                         },

                         {

                              "column1_name": "row2_column1_value",

                              "column2_name": "row2_column2_value"

                         }, ...

                    ],

                    "TotalCount": 20

               }

          */

          var buttonToDisable = document.getElementById("my-button");

          buttonToDisable.disabled = !data.TotalCount; // disable button when there are is at least one result in the item list.

     };





     return eventHandlers;

}(eventNames, convenienceApi));
```

## Item list APIs and Related Objects

### columnsApi

Provides methods for modifying columns on item list, such as the adding formatters, setting titles, or removing columns. The columnsApi is only available in the itemListModifyColumns event handler.

#### Methods

See the following subsections for information about these methods:

- setColumnTitle(columnName: string, title: string)

- setCustomFormatter(columnName: string, formatterAction: function)

- setLinkFormatter(columnName: string, option: object)

- removeColumn(columnName: string)

##### setColumnTitle(columnName: string, title: string)

Sets the title of a specified column.

###### Parameters

Parameter

Description

columnName: string

The name of the column on which to set the title. The column name comes from the name of the Field in the View the item list is displaying.

title: string

The title to set on the column.

###### Return type

undefined

###### Example

Copy

```text
1
2
3
4
5
6
eventHandlers[eventNames.ITEM_LIST_MODIFY_COLUMNS] = function(columnsApi, view) {

     // Check for a specific a specific item list in the layout

     if (view.ObjectTypeID !== convenienceApi.constants.ARTIFACT_TYPE.USER) { return ; }



     columnsApi.setColumnTitle("Preview Security", "Preview User Security");

};
```

##### setCustomFormatter(columnName: string, formatterAction: function)

Sets custom formatter with the specified format action for the column.

###### Parameters

Parameter

Description

columnName: string

The name of the column on which to set the formatter set. The column name comes from the name of the Field in the View the item list is displaying.

formatterAction: function

A function used to format the column. It has the following parameters:

- content <String|Number> - the item list cell content to format.

- rowDataItem <Object> - the related data item for the row of data in the item list.

Copy

```text
1
2
3
4
{

    "col_1": "row_n col_1 value",

    "col_2": "row_n col_2 value"

}
```

It is expected to return either an HTML element or a string value to display in the cell.

###### Return type

undefined

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
/**

 * Example 1

 * Say we have item list row data of the format { "LinkName": "Google", "LinkUrl": "https://google.com" }

 * and want to display only a single column in the table of link elements.

 */

eventHandlers[eventNames.ITEM_LIST_MODIFY_COLUMNS] = function(columnsApi, view) {

    // Check for a specific a specific item list in the layout

    if (view.Name !== "Hyperlinks") { return ; }



    function cellContentFormatter(content, rowDataItem) {

        // content: "Google"

        // rowDataItem: { "LinkName": "Google", "LinkUrl": "https://google.com" }

        var anchor = document.createElement("a");

        anchor.innerText = content;

        anchor.href = rowDataItem["LinkUrl"];

        return anchor;

    }



    columnsApi.setCustomFormatter("LinkName", cellContentFormatter);

};





/**

 * Example 2

 * Say we have item list row data of the format { "FirstName": "Salt", "LastName": "Pepper" }

 * and want to display only a single column with the full name.

 */

eventHandlers[eventNames.ITEM_LIST_MODIFY_COLUMNS] = function(columnsApi, view) {

    // Check for a specific a specific item list in the layout

    if (view.Name !== "Full Names") { return ; }



    function cellContentFormatter(content, rowDataItem) {

        // content: "Salt"

        // rowDataItem: { "FirstName": "Salt", "LastName": "Pepper" }

        return rowDataItem["FirstName"] + " " + rowDataItem["LastName"];

    }



    columnsApi.setCustomFormatter("FirstName", cellContentFormatter);

};
```

##### setLinkFormatter(columnName: string, option: object)

Sets link formatter with the specified options for the column.

###### Parameters

Parameter

Description

columnName: string

The name of the column on which to set the formatter. The column name comes from the name of the Field in the View the item list is displaying.

option: object

This object parameter can be provided with the following property values:

- onClick <function> - an action executed for an onclick event. This function has the following parameter:

- rowDataItem <object> - a related data item that is passed to the onClick function as the first parameter.

Copy

```text
1
2
3
4
{

    "col_1": "row_n col_1 value",

    "col_2": "row_n col_2 value"

}
```

- getContent <function> - an optional function expected to return a string value for the text of the link. If this is not defined, the value for the column in rowDataItem is used.

###### Return type

undefined

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
15
16
/**

 * Say we have item list row data of the format { "FirstName": "Salt", "LastName": "Pepper" } and

 * want to display the first name as a link that, when clicked, shows an alert with the last name.

 */

eventHandlers[eventNames.ITEM_LIST_MODIFY_COLUMNS] = function(columnsApi, view) {

    // Check for a specific a specific item list in the layout

    if (view.Name !== "First Names") { return ; }



    function clickAction(rowDataItem) {    // onClick function is called with the row data item

        alert(rowDataItem["LastName"]);

    }



    columnsApi.setLinkFormatter("FirstName", {

        onClick: clickAction,

    });

};
```

##### removeColumn(columnName: string)

Removes a specific column.

###### Parameters

Parameter

Description

columnName

The name of the column to remove. The column name comes from the name of the Field in the View the item list is displaying.

###### Return type

undefined

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
/**

 * Say we have item list row data of the format { "FirstName": "Salt", "LastName": "Pepper" } and

 * the View the item list uses displays both first and last names. However the item list in the

 * layout should only show last names.

 */

eventHandlers[eventNames.ITEM_LIST_MODIFY_COLUMNS] = function(columnsApi, view) {

    // Check for a specific a specific item list in the layout

    if (view.Name !== "Names") {  return ; }



    columnsApi.removeColumn("FirstName");

}
```

### Item List Action button object

Describes an item list action button.

Field

Type

Description

title

String

The title of an action button.

type

ACTION_TYPES

The type of action button. For more information, see constants .

action

Function

A function that executes when a user clicks the action button.

disabled

Boolean

Set to true to disable the action button, or false to enable it.

order

Number

The order of the action button.

### itemListActionsApi

Modifies action buttons on the item list. The itemListActionsApi is exposed as a part of the event handler API.

#### Methods

Method

Return type

Description

initialize()

undefined

Initializes an empty collection of action buttons.

areActionsInitialized()

bool

Checks to see if the action buttons collection is initialized.

getActions()

array<object>|null

Retrieves the current action buttons collection.

addAction(actionType: ACTION_TYPES|String,clickHandler: Function = null)

Action|null

Adds action of specific type to action buttons collection. Also, it initializes actions collection if it was not initialized before. Returns added action or null, if actionType is not of ACTION_TYPES type and clickHandler is not specified.

Parameters:

- actionType - action type of button to be added to the collection. Pass a value of convenienceApi.constants.ACTION_TYPES enum or a custom string value. For more information, see convenienceApi. constants .

- clickHandler - custom click handler that will be executed when the action button is clicked. Pass a custom function to override standard action click handler or specify the click handler for custom action.

removeActions(actionTypes: array<ACTION_TYPES>)

undefined

Removes each of the specified action types from a collection, if it exists. It has the following parameter:

- actionTypes - an array of action types to be removed. Pass a value of the convenienceApi.constants.ACTION_TYPES enum. For more information, see constants .

addDefaultActions():

undefined

Adds a New, Delete, Link, and Unlink actions to a collection.

differentiateActionsByItemListType()

undefined

Removes actions based on the type of the item list, such as associative or child.

getGlobalVisibilityRules()

VisibilityRule|null

Returns the button visibility rule set for the Item List object type. See Visibility Rule class .

getSublistVisibilityRules()

VisibilityRule|null

Returns sublist button visibility rule set to the layout's object type. See Visibility Rule class .

checkActionsByVisibilityRules()

undefined

Removes action buttons that are disabled by visibility rules. Rules priorities: 1. Sublist button visibility rule, if exists on layout's object type; 2. Buttons visibility rule, if exists on Item List's object type.

checkPermissions()

Promise<undefined>

Checks if a user has permissions for each action and removes actions for which the user does not have permissions. This method returns Promise because it needs to call the backend to get needed information about permissions. This Promise resolves to no value (undefined).

checkRulesAndPermissions()

Promise<undefined>

Checks item list type, visibility rules, permissions and removes actions that shouldn't be shown.

This method returns Promise because it needs to call the backend to get needed information about permissions. This Promise resolves to no value (undefined).

setCustomGetDataFunction(getDataFunction)

Promise<undefined>

Supplies the item list with a getDataFunction function for it to call whenever it needs to get data to show in the list. The getDataFunction is called with the ItemList layout element, and a QueryRequest object with information about what data needs to be retrieved. If the filter and sort conditions are applied, the item list expects getDataFunction to consider these conditions when retrieving data. If you don't want to worry about dealing with filters and conditions, you can turn off the ability to apply filter and sort conditions in the transformLayout stage. To do this, set FilterType to "" and IsSortable to false for each field in the ItemList 's FieldCollection.

##### Parameters

Parameter

Type

Description

getDataFunction

function(itemList: ItemList, queryRequest: QueryRequest): Promise<QueryResponse>

A function expected to return a Promise that resolves to a QueryResponse object containing the data to use to populate the item list.

##### getDataFunction Parameters

Parameter

Type

Description

itemList

ItemList

A Relativity Forms ItemList object representing the item list that data should be fetched for.

Example structure:

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
{

    View: {

        Name: "My Item list's View",

        ObjectTypeID: 1234567,

        FieldsIds: [ 2345678, 3456789 ],

        ...

    },

    FieldCollection: [

        {

            AvfID: 2345678,

            HeaderName: "Name of First Column",

            ...

        },

        {

            AvfID: 3456789 ,

            HeaderName: "Name of Second Column",

            ...

        }

    ]

}
```

queryRequest

QueryRequest

A QueryRequest object describing what data to retrieve.

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
eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, view) {

      // To hide all actions it is needed to call initialize method.

      // Otherwise, by default all rules are checked and appropriate buttons shown.

      itemListActionsApi.initialize();

 };

 eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, view) {

      const USERS_LIST_ID =  "usersList" ;



      // Checks whether an action should be added to particular list.

      if (view.ObjectTypeID === convenienceApi.constants.ARTIFACT_TYPE.USER) {

          // Adds Link action and checks all needed rules and permissions.

          itemListActionsApi.initialize();

          itemListActionsApi.addAction(convenienceApi.constants.ACTION_TYPES.LINK);

          return itemListActionsApi.checkRulesAndPermissions();

      }



      return void 0;

 };

 eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, view) {

      // Add default actions buttons, then find "New" and replace its title to "Create".

      itemListActionsApi.addDefaultActions();

      const actions = itemListActionsApi.getActions();

      actions.filter(function(action) {

          return action.type === convenienceApi.constants.ACTION_TYPES.NEW;

      }).forEach(function(action) {

          action.title =  "Create" ;

      });

 };

eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, view) {

    const TITLE_OF_LIST_I_AM_LOOKING_FOR = "List of Items";

    // Checks if custom data source should be defined for particular list

    if (view.Name === TITLE_OF_LIST_I_AM_LOOKING_FOR) {

        // Add a custom data source that shows arbitrary data

        itemListActionsApi.setCustomGetDataFunction(function arbitraryCustomDataGenerator(itemList, request) {

            const columnIDArray = itemList.FieldCollection.map(function getColumnID(field) {

                    return field.HeaderName; // The HeaderName is used by liquid as the column identifier

               });

            const rowDataArray = [];

            const counter = 0;

            // generate arbitrary data for the requested page size

            for(let i = 0; i < request.pageSize; i++) {

                const rowData = {};

                columnIDArray.forEach(function(columnID) {

                    rowData[columnID] = "Cell data:" + counter.toString();

                    counter++;

                });

                rowDataArray.push(rowData);

            }

            return {

                Results: rowDataArray,

                TotalCount: rowDataArray.length

            };

        });

    }



    return void 0;

};

/*

This will make the item list titled 'List of Items' show this data:

|---------------|---------------|---------------|---------------|

| First column  | Second column | Third column  | Fourth column |

|===============|===============|===============|===============|

| Cell data: 1  | Cell data: 2  | Cell data: 3  | Cell data: 4  |

|---------------|---------------|---------------|---------------|

| Cell data: 5  | Cell data: 6  | Cell data: 7  | Cell data: 8  |

|---------------|---------------|---------------|---------------|

| Cell data: 9  | Cell data: 10 | Cell data: 11 | Cell data: 12 |

|---------------|---------------|---------------|---------------|

*/
```

### View object

Identifies the current item list.

This object has these fields used for item list identification:

Field

Type

Description

ArtifactID

number

The artifact ID of the view.

Name

string

The name of the view.

ObjectTypeID

number

The artifact type ID of the object displayed in the view.

### Visibility Rule class

Indicates the visibility of action buttons for an item list.

Field

Type

Description

Delete

Boolean

Set to true to make the Delete button visible, or false to hide it.

Link

Boolean

Set to true to make the Link button visible, or false to hide it.

New

Boolean

Set to true to make the New button visible, or false to hide it.

Unlink

Boolean

Set to true to make the Unlink button visible, or false to hide it.

On this page

- Item list event handlers

-

- Summary of item list event handlers

- Summary of item list event handler APIs and objects

- Item List Event Handlers

- itemListModifyActions

- itemListModifyColumns

- itemListReloaded

- Item list APIs and Related Objects

- columnsApi

- Item List Action button object

- itemListActionsApi

- View object

- Visibility Rule class


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
