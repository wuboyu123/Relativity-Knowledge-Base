---
title: "Add a custom item list to a layout"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Add_a_custom_item_list_to_a_layout.htm
collection: developer
fetched_at: 2026-06-22T06:32:12+00:00
sha256: 36d6ae655ea473268a46b0e4a1591c04be0487e06e1deff72ddee3e9759349f3
---

Add a custom item list to a layout Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Add a custom item list to a layout

The following page explains how to add a custom item list to a layout in the Relativity Forms.

Read a custom item list scenario The business wants to show the audit history of the object the user is looking at in Relativity Forms. How would you show this information in an item list on the layout in Relativity Forms?

There are three main things you will need to do in Relativity Forms to make this work:

- Append a new item list to the layout.

- Define View information, detailing what columns to show in the item list getting added.

- Define a custom data source for the item list that will use the Relativity Audit API to get the relevant history information.

## Adding a new item list & view information

The transformLayout event handler allows you to modify the layout information before it is rendered in the browser. In the code sample below, we add a handler that appends a new category to the user-selected layout, in order to show an item list called "History". To do that, let's append a single-category element containing another element with a View definition. At a minimum, the View definition needs to provide a FieldCollection detailing what fields are in the list. For now, let's define two columns for this layout detailing which user modified it, and when it was modified. Take note how we're following the same format of information as a View defined in Relativity - the View.FieldsIds array values correspond with the FieldCollection[n].AvfID values. The FieldCollection[n].HeaderName values decide what is shown as the column title in the item list.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: "History",

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn", HeaderName: "Modified On" },

                    { AvfID: "ModifiedBy", HeaderName: "Modified By" }

                    ]

                    }

                    ]

                    });

                    };



                    return eventHandlers;



                })(eventNames, convenienceApi);
```

As a result of our above configuration, the event handler appends this item list to the form:

- No FilterType is defined in the FieldCollection, so this item list does not show any filters.

- No IsSortable value is defined in the FieldCollection, so this item list does not support clicking on column titles to apply sorting.

- No custom data source is defined, so the Item List is using Relativity Form's built in behavior to use Object Manager to query for data. Naturally, that is failing.

### Overriding default action bar buttons

In order to restrict the default application behavior of adding action bar buttons, we need to call the itemListActionBarApi.initialize() method in the itemListModifyActions event handler, as illustrated below.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: HISTORY_ITEM_LIST_NAME,

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn", HeaderName: "Modified On" },

                    { AvfID: "ModifiedBy", HeaderName: "Modified By" }

                    ]

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, itemListView) {

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons

                    itemListActionsApi.initialize();



                    // Override item list data source

                    itemListActionsApi.setCustomGetDataFunction(function(category, request) {

                    return {

                    TotalCount: 0,

                    Results: []

                    };

                    });

                    }

                    };



                    return eventHandlers;



                })(eventNames, convenienceApi);
```

### Calling an API to get Item list data

Now that we are able to generate a non-errored item list, let's call the Audit API to get real information to populate in the item list. Let's add this API call to our custom "get data" function. Please note that we're now returning a promise for the data, instead of an object, in our custom function.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: HISTORY_ITEM_LIST_NAME,

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn", HeaderName: "Modified On" },

                    { AvfID: "ModifiedBy", HeaderName: "Modified By" }

                    ]

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, itemListView) {

                    const self = this;

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons

                    itemListActionsApi.initialize();



                    // Override item list data source

                    itemListActionsApi.setCustomGetDataFunction(function(category, request) {

                    const auditApiUrl = convenienceApi.relativityHttpClient.makeRelativityRestRelativeUrl("/API/Relativity.Objects.Audits/workspaces/" + self.workspaceId + "/audits/queryslim");

                    const auditRequest = {

                    request: {

                    objectType: {

                    artifactTypeID: 1000045 // this is the artifact type ID for audit

                    },

                    fields: [

                    { Name: "User Name" },

                    { Name: "Timestamp" }

                    ],

                    condition: "'Object ArtifactID' == " + self.artifactId + "" // define condition for only audits on our specific object instance

                    },

                    start: request.startIndex,  // use the start index as defined in the request

                    length: request.pageSize    // use the page size as defined in the request

                    };



                    const auditApiFieldToColumnNameMap = new Map();

                    auditApiFieldToColumnNameMap.set("User Name", "Modified By");

                    auditApiFieldToColumnNameMap.set("Timestamp", "Modified On");

                    return convenienceApi.relativityHttpClient.post(auditApiUrl, auditRequest).then(function(auditApiResponse) {

                    const rows = [];

                    auditApiResponse.body.Objects.forEach(function(responseObject) {

                    const row = responseObject.Values.reduce(function(rowData, cellValue, columnIndex) {

                    // Get the Audit Api field for which the current value corresponds

                    const auditApiFieldName = response.Fields[columnIndex].Name;

                    // Translate the Audit Api field to our item list column name

                    const columnKey = auditApiFieldToColumnNameMap.get(auditApiFieldName);

                    // Add the column value to the object containing all the values for the row

                    rowData[columnKey] = cellValue;

                    return rowData;

                    });



                    rows.push(row);

                    });

                    return {

                    TotalCount: auditApiResponse.TotalCount,

                    Results: rows

                    };

                    });

                    });

                    }

                    };

                    return eventHandlers;



                })(eventNames, convenienceApi);
```

Now we can see audit data in the item list:

Notice that the 'Modified On' dates are showing as plain text. We want them formatted correctly as dates. We can do that by defining the field as a date field.

### Modifying the view to add field type information

Let's go back to the transformLayout event handler. In the FieldCollection array we defined, we'll need to add a FieldTypeID value and a FormatString value. Let's add a FieldTypeID value of "2", which corresponds to the Date field type, and since we want to show both date and time, lets set a FormatString value of "g".

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: HISTORY_ITEM_LIST_NAME,

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn", HeaderName: "Modified On", FieldTypeID: 2, FormatString: "g" },

                    { AvfID: "ModifiedBy", HeaderName: "Modified By" }

                    ],

                    workspaceId: this.workspaceId

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, itemListView) {

                    const self = this;

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons

                    itemListActionsApi.initialize();



                    // Override item list data source

                    itemListActionsApi.setCustomGetDataFunction(function(category, request) {

                    const auditApiUrl = convenienceApi.relativityHttpClient.makeRelativityRestRelativeUrl("/API/Relativity.Objects.Audits/workspaces/" + self.workspaceId + "/audits/queryslim");

                    const auditRequest = {

                    request: {

                    objectType: {

                    artifactTypeID: 1000045 // this is the artifact type ID for audit

                    },

                    fields: [

                    { Name: "User Name" },

                    { Name: "Timestamp" }

                    ],

                    condition: "'Object ArtifactID' == " + self.artifactId + "" // define condition for only audits on our specific object instance

                    },

                    start: request.startIndex,  // use the start index as defined in the request

                    length: request.pageSize    // use the page size as defined in the request

                    };



                    const auditApiFieldToColumnNameMap = new Map();

                    auditApiFieldToColumnNameMap.set("User Name", "Modified By");

                    auditApiFieldToColumnNameMap.set("Timestamp", "Modified On");

                    return convenienceApi.relativityHttpClient.post(auditApiUrl, auditRequest).then(function(auditApiResponse) {

                    const rows = [];

                    auditApiResponse.body.Objects.forEach(function(responseObject) {

                    const row = responseObject.Values.reduce(function(rowData, cellValue, columnIndex) {

                    // Get the Audit Api field for which the current value corresponds

                    const auditApiFieldName = response.Fields[columnIndex].Name;

                    // Translate the Audit Api field to our item list column name

                    const columnKey = auditApiFieldToColumnNameMap.get(auditApiFieldName);

                    // Add the column value to the object containing all the values for the row

                    rowData[columnKey] = cellValue;

                    return rowData;

                    });



                    rows.push(row);

                    });

                    return {

                    TotalCount: auditApiResponse.TotalCount,

                    Results: rows

                    };

                    });

                    });

                    }

                    };

                    return eventHandlers;



                })(eventNames, convenienceApi);
```

Now we see the 'Modified On' values formatted correctly as date and times:

### Turning on sorting

The business wants the user to be able to sort the list on the value of 'Modified On' so that they can easily see the earliest and most recent updates to the object. This requires two small changes to our current setup:

- transformLayout event handler must define the 'Modified On' column as sortable.

- The custom "get data" function defined in itemListModifyActions takes the applied sorts in the list and includes that information in the request to the Audit API.

View example Copy

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

                    (function (eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function (layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: HISTORY_ITEM_LIST_NAME,

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn", HeaderName: "Modified On", FieldTypeID: 2, FormatString: "g", IsSortable: true },

                    { AvfID: "ModifiedBy", HeaderName: "Modified By" }

                    ],

                    workspaceId: this.workspaceId

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function (itemListActionsApi, itemListView) {

                    const self = this;

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons

                    itemListActionsApi.initialize();



                    // Override item list data source

                    itemListActionsApi.setCustomGetDataFunction(function (category, request) {

                    // translate item list sort direction -> Audit Api sort direction

                    const itemlistToAuditApiSortMap = new Map();

                    itemlistToAuditApiSortMap.set("asc", 0);

                    itemlistToAuditApiSortMap.set("desc", 1);



                    // translate item list column -> Audit Api field

                    const itemListColumnToAuditApiFieldMap = new Map();

                    itemListColumnToAuditApiFieldMap.set("Modified By", "User Name");

                    itemListColumnToAuditApiFieldMap.set("Modified On", "Timestamp");



                    // translate Audit Api field -> item list column

                    const auditApiFieldToItemListColumnMap = new Map();

                    auditApiFieldToItemListColumnMap.set("User Name", "Modified By");

                    auditApiFieldToItemListColumnMap.set("Timestamp", "Modified On");



                    const requestSorts = request.sorts.map(function (itemListSort) {

                    return {

                    Direction: itemlistToAuditApiSortMap.get(itemListSort.direction),

                    FieldIdentifier: {

                    Name: itemListColumnToAuditApiFieldMap.get(itemListSort.column)

                    }

                    };

                    });



                    const auditApiUrl = convenienceApi.relativityHttpClient.makeRelativityRestRelativeUrl("/API/Relativity.Objects.Audits/workspaces/" + self.workspaceId + "/audits/queryslim");

                    const auditRequest = {

                    request: {

                    objectType: {

                    artifactTypeID: 1000045 // this is the artifact type ID for audit

                    },

                    fields: [

                    { Name: "User Name" },

                    { Name: "Timestamp" }

                    ],

                    sorts: requestSorts,

                    condition: "'Object ArtifactID' == " + self.artifactId + "" // define condition for only audits on our specific object instance

                    },

                    start: request.startIndex,  // use the start index as defined in the request

                    length: request.pageSize    // use the page size as defined in the request

                    };

                    return convenienceApi.relativityHttpClient.post(auditApiUrl, auditRequest).then(function(auditApiResponse) {

                    const rows = [];

                    auditApiResponse.body.Objects.forEach(function (responseObject) {

                    const row = responseObject.Values.reduce(function (rowData, cellValue, columnIndex) {

                    // Get the Audit Api field for which the current value corresponds

                    const auditApiFieldName = response.Fields[columnIndex].Name;

                    // Translate the Audit Api field to our item list column name

                    const columnKey = auditApiFieldToItemListColumnMap.get(auditApiFieldName);

                    // Add the column value to the object containing all the values for the row

                    rowData[columnKey] = cellValue;

                    return rowData;

                    });



                    rows.push(row);

                    });

                    return {

                    TotalCount: auditApiResponse.TotalCount,

                    Results: rows

                    };

                    });

                    });

                    }

                    };

                    return eventHandlers;



                })(eventNames, convenienceApi);
```

Now the column sorting control is enabled in the item list, and correctly applies the sort value to the retrieved audit data shown in the list:

### Enable filtering

The business wants the user to be able to filter the 'Modified On' column in order to see only data from a certain time period. This requires two updates:

- The transformLayout event handler must define the 'Modified On' column as filterable. This can be done by adding the FieldTypeID, FilterType, FormatString, and IsFilterable attributes to the column definition in the FieldCollection array.

- The custom "get data" function defined in itemListModifyActions must take any applied filters and apply them to the data.

The custom "get data" function defined in itemListModifyActions provides filter data in the request object that it passes to the function when it executes. The request object, in turn, contains a filter object and a condition object , both of which contain data on the requested filter.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: HISTORY_ITEM_LIST_NAME,

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn",

                    HeaderName: "Modified On",

                    FieldTypeID: 2,

                    FormatString: "g",

                    FilterType: "Search",

                    IsFilterable: true },

                    { AvfID: "ModifiedBy",

                    HeaderName: "Modified By" }

                    ],

                    workspaceId: this.workspaceId

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, itemListView) {

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons

                    itemListActionsApi.initialize();



                    // Override item list data source

                    itemListActionsApi.setCustomGetDataFunction(function(category, request) {

                    // Example data to display in the item list

                    const exampleData = [

                    {"Modified By": "Test User", "Modified On": "2018-01-01T01:10:00"},

                    {"Modified By": "Test User", "Modified On": "2018-06-01T01:10:00"},

                    {"Modified By": "Test User", "Modified On": "2019-01-01T01:10:00"},

                    {"Modified By": "Test User", "Modified On": "2019-04-01T01:10:00"},

                    {"Modified By": "Test User", "Modified On": "2019-06-01T01:10:00"},

                    {"Modified By": "Test User", "Modified On": "2019-08-01T01:10:00"}

                    ];



                    // Filter the data based on what's in the request object.

                    let filterFunction = function(itemListRow) {return true};

                    let beforeDate;

                    let afterDate;



                    // Check if there's a filter and a condition with it. If so, create the filter function.

                    if (request.filters && request.filters[0] && request.filters[0].condition && request.filters[0].condition[0]) {

                    const filterCondition = request.filters[0].condition[0];

                    if (filterCondition.operator && Array.isArray(filterCondition.value) && filterCondition.value.length >= 2) {

                    if (filterCondition.operator === "is not set") {

                    filterFunction = function(itemListRow) {return false};

                    } else {

                    beforeDate = Date.parse(filterCondition.value[0]) || null;

                    afterDate = Date.parse(filterCondition.value[1]) || null;

                    switch (filterCondition.operator) {

                    case "is":

                    filterFunction = function(itemListRow) {return new Date(itemListRow["Modified On"]) == beforeDate};

                    break;

                    case "is less than":

                    filterFunction = function(itemListRow) {return new Date(itemListRow["Modified On"]) < afterDate};

                    break;

                    case "is less than or equal to":

                    filterFunction = function(itemListRow) {return new Date(itemListRow["Modified On"]) <= afterDate};

                    break;

                    case "is greater than":

                    filterFunction = function(itemListRow) {return new Date(itemListRow["Modified On"]) > beforeDate};

                    break;

                    case "is greater than or equal to":

                    filterFunction = function(itemListRow) {return new Date(itemListRow["Modified On"]) >= beforeDate};

                    break;

                    case "between":

                    filterFunction = function(itemListRow) {return new Date(itemListRow["Modified On"]) > beforeDate && new Date(itemListRow["Modified On"]) < afterDate};

                    break;

                    default:

                    filterFunction = function(itemListRow) {return true};

                    break;

                    }

                    }

                    }

                    }



                    // Filter the data based on the filter function defined above.

                    const filteredData = exampleData.filter(filterFunction);



                    // Return the filtered data.

                    return {

                    TotalCount: filteredData.length,

                    Results: filteredData

                    };

                    });

                    }

                    };

                    return eventHandlers;



                })(eventNames, convenienceApi);
```

Now the filter control is enabled and it applies to the example data. See below an example of an item list that's filtering between 7/10/2019 and 8/10/2019.

### Add custom action buttons

You can use the Item List Actions API to add a custom button to the item list by utilizing the addAction method. The method returns the Action object for the button, which can be used to customize the button further. The Action object has a title field, which can be used to customize the title of the button, and an action field that can be assigned a specific function to be executed when the button is clicked.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    View: {

                    Name: HISTORY_ITEM_LIST_NAME,

                    FieldsIds: ["ModifiedOn", "ModifiedBy"]

                    },

                    FieldCollection: [

                    { AvfID: "ModifiedOn", HeaderName: "Modified On" },

                    { AvfID: "ModifiedBy", HeaderName: "Modified By" }

                    ]

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, itemListView) {

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons.

                    itemListActionsApi.initialize();



                    // Add an item list action bar button.

                    // The button will open an accept/cancel modal when you click it.

                    const customAction = itemListActionsApi.addAction(convenienceApi.constants.ACTION_TYPES.NEW);

                    customAction.title =  "Create";

                    customAction.action = function() {

                    var model = {

                    title: "Are you sure you want to create?",

                    acceptAction: function acceptAction() {

                    console.log("Accept button was clicked");

                    },

                    cancelAction: function cancelAction() {

                    console.log("Cancel button was clicked");

                    }

                    };

                    convenienceApi.modalService.confirm(model);

                    }

                    // Override item list data source.

                    itemListActionsApi.setCustomGetDataFunction(function(category, request) {

                    return {

                    TotalCount: 0,

                    Results: []

                    };

                    });

                    }

                    };

                    return eventHandlers;



                })(eventNames, convenienceApi);
```

Now that we've modified the above custom function, we can see a new Create button in the item list action bar below. The newly added button will open a Create modal when clicked.

### Custom views

In previous examples on this page, we have shown one way to define a custom view by pushing it to the Layout data in the transformLayout event handler. Then, we defined a custom data source in the itemListModifyActions event handler to override Relativity Form's built in way of pulling data. Then, we overrode the default action bar buttons in the itemListModifyActions event handler by calling the itemListActionBarApi.initialize() method.

There are, however, a few different ways to define a custom view. One such way is to create a view in Relativity, then add a reference to it in the transformLayout event handler. See Creating a View for additional information.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    "View": {

                    "Name": "System Modified By",

                    "ArtifactID": 1039369,// Artifact ID of the view.

                    "FieldsIds": [1038304, 1038305],// Artifact IDs of the fields.

                    "Sorts": [],

                    "RenderLinks": true,

                    "HasConditions": false,

                    "GroupDefinitionFieldName": "",

                    "QueryHint": "",

                    ObjectTypeID: 1000042

                    },

                    "FieldCollection": [

                    { AvfID: 1038304, "IsVisible": true, "ItemListType": "Text", "IsSortable": true, HeaderName: "Artifact ID", ArtifactID: 1038304 },

                    { AvfID: 1038305, "IsVisible": true, "ItemListType": "Text", "IsSortable": true, HeaderName: "Name", ArtifactID: 1038305 }

                    ]

                    }

                    ]

                    });

                    };



                    return eventHandlers;



                })(eventNames, convenienceApi);
```

In this example, 1039369 is the Artifact ID of the new View. The Artifact ID should be listed on the ArtifactID property of the View object, and can be found on the Views tab in your Workspace. If you need to modify the Views tab to get the Artifact ID, a detailed explanation can be found here .

1038304 and 1038305 are the Artifact IDs of the two fields in the new View. These Artifact IDs should be listed in the FieldsIds array of the View object as shown above. They should also be listed in the AvfID and ArtifactID properties of the FieldCollection array as shown above. The Artifact IDs can be found on the Fields tab of your Workspace by searching for the Fields of your Object Type. If you need to modify the Fields tab to get the Artifact ID, a detailed explanation can be found here .

1000042 is the Artifact Type ID of the Object Type to be displayed. It should be listed on the ObjectTypeID property of the View object as shown above. The Artifact Type ID can be found in the Object Type tab in your Workspace. If you need to modify the Object Type tab to get the Artifact Type ID, a detailed explanation can be found here .

Documentation for the fields in the layoutData can be found here .

### Refreshing the item list

To refresh the item list, we can dispatch a reloadItemListData event to the item list. We can build off of what we did in the Custom Views section to create a button that will refresh the item list.

View example Copy

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
(function(eventNames, convenienceApi) {



                    const eventHandlers = {};

                    const HISTORY_ITEM_LIST_NAME = "History";



                    eventHandlers[eventNames.TRANSFORM_LAYOUT] = function(layoutData) {

                    layoutData.push({

                    Elements: [

                    {

                    "View": {

                    "Name": HISTORY_ITEM_LIST_NAME,

                    "ArtifactID": 1039369,// Artifact ID of the view.

                    "FieldsIds": [1038304, 1038305],// Artifact IDs of the fields.

                    "Sorts": [],

                    "RenderLinks": true,

                    "HasConditions": false,

                    "GroupDefinitionFieldName": "",

                    "QueryHint": "",

                    ObjectTypeID: 1000042

                    },

                    "FieldCollection": [

                    { AvfID: 1038304, "IsVisible": true, "ItemListType": "Text", "IsSortable": true, HeaderName: "Modified By", ArtifactID: 1038304 },

                    { AvfID: 1038305, "IsVisible": true, "ItemListType": "Text", "IsSortable": true, HeaderName: "Modified On", ArtifactID: 1038305 }

                    ]

                    }

                    ]

                    });

                    };



                    eventHandlers[eventNames.ITEM_LIST_MODIFY_ACTIONS] = function(itemListActionsApi, itemListView) {

                    const self = this;

                    if (itemListView.Name === HISTORY_ITEM_LIST_NAME) {

                    // Override default item list action bar buttons to show no buttons

                    itemListActionsApi.initialize();



                    // Add an item list action bar button to refresh the item list

                    const customAction = itemListActionsApi.addAction(convenienceApi.constants.ACTION_TYPES.NEW);

                    customAction.title =  "Refresh";

                    customAction.action = function() {

                    const historyItemListFieldId = self.fieldNameToFieldIdMap.get(HISTORY_ITEM_LIST_NAME);



                    convenienceApi.fieldHelper.getHtmlElement(historyItemListFieldId).then(function(itemListElement) {

                    const refreshEvent = document.createEvent("Event");

                    refreshEvent.initEvent("reloadItemListData", true, true);

                    itemListElement.dispatchEvent(refreshEvent);

                    });

                    }



                    // Override item list data source

                    itemListActionsApi.setCustomGetDataFunction(function(category, request) {

                    // Create some example data to show in the item list with the current date.

                    // That way the Modified On time will update to the current time when the item list refreshes.

                    const currentDate = new Date();

                    const exampleData = [

                    {"Modified By": "Test User", "Modified On": currentDate.toString()}

                    ];



                    return {

                    TotalCount: exampleData.length,

                    Results: exampleData

                    };

                    });

                    }

                    };

                    return eventHandlers;



                })(eventNames, convenienceApi);
```

Notice the HeaderName values of the FieldCollection array were changed in the transformLayout event handler to match the example data in the itemListModifyActions event handler. It may be helpful to note that the most critical aspect of the above code sample is where the Refresh button is defined in the itemListModifyActions event handler. This code defines an action for the button that dispatches a reloadItemListData event.

It creates a row with the current date and time to put in the item list. That way, the Modified On time will update every time the item list refreshes.

On this page

- Add a custom item list to a layout

- Adding a new item list & view information

- Overriding default action bar buttons

- Calling an API to get Item list data

- Modifying the view to add field type information

- Turning on sorting

- Enable filtering

- Add custom action buttons

- Custom views

- Refreshing the item list


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
