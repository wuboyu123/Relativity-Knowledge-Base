---
title: "Field Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Field_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:11+00:00
sha256: 33ada5de9c3760695ce268ea6b49b91d19d3ef2fd2df8ee4ca1e28b665d5adb0
---

Field Manager (.NET)

# Field Manager (.NET)

The Field Manager API provides multiple methods for programmatically working with field types supported by Relativity, including multiple choice, fixed-length text, date, and others. This API supports create, read, update, and delete operations on fields. Additionally, it includes helper methods for retrieving the following information:

- Object types available to create fields on.

- Associative object types for creating single object fields.

- Associative object types for creating multiple object fields.

- Views available for a specific object type.

- Keyboard shortcuts that are currently defined in a workspace.

- Keys that are valid for use in a keyboard shortcut.

- Fields available for use with propagation.

- Order of relational field icons in the Related Items pane of the core reviewer interface.

Sample use cases for the Field Manager API include programmatically adding new fields to a custom application as data requirements change, or creating new keyboard shortcuts for fields to support modified workflows for users.

You can also use the Field Manager API through REST. For more information, see Field Manager (REST) .

## Fundamentals for Field Manager API

The Field Manager API contains the following methods, classes, and enumerations.

Methods

The Field Manager API exposes the following methods on the IFieldManager interface in the Relativity.ObjectModel.<VersionNumber>.Field namespace namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- Create() method for each field type - adds a new field on a specified object type. The parameters for the create methods include the Artifact ID of a workspace, and a request object for the field type. These methods return the Artifact ID of the new field.

Each field type has its own create method and request class. For a complete list of create methods, see Create a field .

- DeleteAsync() method - removes a field from an object type in the specified workspace. Its parameters include the Artifact IDs of the workspace and the field. This method returns a Task. See Delete a field .

- AvailableKeyboardShortcutsAsync() method - retrieves a list of keyboard shortcuts currently defined in a workspace. It takes the Artifact ID of a workspace, and returns a list of KeyboardShortcut objects. See Retrieve keyboard shortcuts .

- AvailableMultiAssociativeObjectTypesAsync() method - retrieves a list of associative object types that you can use when creating a multiple object field. Its parameters include the Artifact ID of a workspace, and a DisplayableObjectTypeIdentifier object. The multiple object field is created on the object type represented by the DisplayableObjectTypeIdentifier object, and the method retrieves other object types compatible with it. The method returns a list of on DisplayableObjectTypeIdentifier objects. See Retrieve object types for a multiple object field .

The DisplayableObjectTypeIdentifier class contains the Artifact ID, Name, and other identifiers for an object. It is available in the Relativity.Shared.<VersionNumber>.Models namespace.

- AvailableObjectTypesAsync() method - retrieves a list of parent object types available in a specific workspace. It takes the Artifact ID of a workspace, and returns a list of ObjectTypeIdentifier objects. See Retrieve available object types .

- AvailableObjectTypeViewsAsync() method - retrieves a list of available views for a specific object type. Its parameters include the Artifact ID of a workspace, and an ObjectTypeIdentifier object. The method returns a list of DisplayableObjectIdentifier objects. See Retrieve available views for an object type .

The DisplayableObjectIdentifier class contains the Artifact ID, Guids, and Name properties. It is available in the Relativity.Shared.{versionNumber}.Models namespace.

- AvailablePropagateToFieldsAsync() method - retrieves a list of fields used for propagation in a workspace. It takes the Artifact ID of a workspace, and returns a list of DisplayableObjectIdentifier objects. See Retrieve available fields for propagation .

- RelationalOrderAsync() method - retrieves information about the order used to display relational field icons in the Related Items pane of the core reviewer interface for a specific workspace. It takes the Artifact ID of a workspace, and returns a list of RelationalFieldOrder objects. See Retrieve the order of relational field icons .

- AvailableSingleAssociativeObjectTypesAsync() method - retrieves a list of associative object types that you can use when creating a single object field. Its parameters include the Artifact ID of a workspace, and an DisplayableObjectTypeIdentifier object. The single object field is created on the object type represented by the DisplayableObjectTypeIdentifier object, and the method retrieves other object types compatible with it. The method returns a list of on DisplayableObjectTypeIdentifier objects. See Retrieve object types for a single object field .

The DisplayableObjectTypeIdentifier class contains the Artifact ID, Name, and other identifiers for an object. It is available in the Relativity.Shared.<VersionNumber>.Models namespace.

- ValidKeys() method - retrieves keys available for use in a keyboard shortcut. It takes the Artifact ID of a workspace, and returns a list of strings representing available keys. See Retrieve valid keys .

- ReadAsync() method - retrieves metadata for a field, such as its name, Artifact ID, associated object type, and other properties. You can also use this overloaded method to return extended metadata, including information about the operations that you have permissions to perform on the field, such as update or delete. This method takes the Artifact IDs of the workspace and field, and two optional Boolean values for extended metadata. It returns a FieldResponse object. See Read a field .

- Update() method for each field type - modifies the properties of a field. The parameters for the update methods include the Artifact IDs of the workspace and the field, a request object for the field type, and an optional DateTime object to restrict the update to the date last modified. These methods return a Task. See Update a field .

Each field type has its own update method, and request class. For a complete list of create methods, see Update a field .

Classes and enumerations

The Field Manager API includes the following classes and enumerations available in the Relativity.Services.Interfaces.Field.Models namespace:

- Request class for each field type - represents the data used to create or update an object type. Each create and update method takes an object of this type.

- FieldResponse class - represents the results of a read operation. Its properties include the user-friendly name for the field, a Boolean value indicating whether the field is required, the keyboard shortcut when assigned to the field, and other properties.

- FieldType enumeration - provides a of list integer values that represent field types supported by Relativity, such as Currency, User, FixedLength, and others.

- FilterType enumeration - provides a of list integer values that represent types of filters for lists, such as filters for Booelan values, pop-up pickers, and others.

- Formatting enumeration - provides formatting options for date, currency, whole number, and decimal fields.

- KeyboardShortcut class - represents the key combination and behavior of a keyboard shortcut. Its properties include the action performed by the shortcut, its key combination, and others.

- OverlayBehavior enumeration - indicates whether the values in multiple object or multiple choice fields are replaced or merged when imported from a load file.

- PaneIcon class - represents an icon displayed in the Related Items pane of the reviewer interface. Its properties include the file name and a string representing the Base64 encoding of the icon.

- RelationalFieldOrder class - represents the position of a relational field icon in the Related Items pane of the core reviewer interface. Its properties include the name and type of the relational field, and an integer value indicating the display order of the field icon. The RelationalOrderAsync() method returns a list of objects with this type.

## Guidelines for the Field Manager API

Review the following guidelines for working with this API.

### Supported field types

Use the Field Manager service to work with the same field types available through the Relativity UI. For general information about fields, see Fields on the Relativity Documentation site. View a list of available field types

- Currency

- Date

- Decimal

- File

- Fixed-length text

- Long text

- Multiple choice

- Multiple object

- Single choice

- Single object

- User

- Whole number

- Yes/No

### Helper methods

Use the helper methods to facilitate creating fields. View a table with examples of helper methods used when creating fields

Field type Links to helper method information

Date

- Retrieve keyboard shortcuts

Fixed-length text field

- Retrieve keyboard shortcuts

- Retrieve available views for an object type

- Retrieve object types for a multiple object field

- Retrieve available object types

- Retrieve the order of relational field icons

Multiple choice

- Retrieve keyboard shortcuts

Single object

- Retrieve keyboard shortcuts

- Retrieve available fields for propagation

- Retrieve available views for an object type

- Retrieve object types for a single object field

### Relational fields

To edit properties for relational fields, the IsRelational field must be set to true. You can then edit the FriendlyName, ImportBehavior, PaneIcon, Order, and RelationalView properties. Set these fields as follows:

- Set the ImportBehavior property to one of the following values:

- None - indicates that no import behavior is specified.

- LeaveBlankValuesUnchanged - indicates that the values for the fields are imported as blank.

- ReplaceBlankValuesWithIdentifier - indicates that blank relational fields are updated with an identifier.

- Set the properties on a PaneIcon object as follows:

- Optionally, set the value for the FileName field for the pane icon.

- Set the ImageBase64 property to the base64 format.

### Overlay behavior

Set the value for the OverlayBehavior property to one of the following values. For more information, see the OverlayBehavior enumeration in the Relativity.ObjectModel.V1.Field.Models namespace.

- ReplaceValues - replaces existing field values with the new ones from the load file.

- MergeValues - merges existing values with the new ones from the load file.

### Filter types

Set the FilterType property to one of the following values. For more information, see the FilterType enumeration in the Relativity.ObjectModel.V1.Field.Models namespace.

- None - used for all field types.

- List - used for currency, decimal, fixed-length text, multiple choice, single choice, user, and whole number field types.

- MultiList - used for single choice, multiple choice, and multi-object field types.

- Popup - used for single choice, multiple choice, single object, and multiple object field types. Only usable when the FilterType property is set to Popup.

- Boolean - used for Yes/No field types.

- TextBox - used for currency, date, decimal, fixed-length text, long text, single object, multiple object, and whole number field types.

- Custom - used for currency, date, decimal, fixed-length text and whole number field types.

- DatePicker - used for date field types.

#### Filter types for date and user fields

The Field Manager API currently sets the filter type for the date and user fields as follows. See the following descriptions:

- Date field - You can now set the FilterType for this field to DatePicker through the API. However, the field type displays a TextBox filter when you access it.

- User field - You can now set the FilterType for this field to MultiList through the API. However, the field type displays a List filter when you access it.

### Source property

Only use the Source property for mapping processing fields on the Document object.

### Formatting fields

Set the Formatting property to one of the following values. For more information, see the Formatting enumeration in the Relativity.ObjectModel.V1.Field.Models namespace.

- None - used for all field types except currency or date.

- Formatted - used for decimal and whole number field types.

- Date - used for the date field type.

- DateTime - used for the date field type.

- Currency - used for the currency field type.

## Create a field

You can create fields by using the methods available on the IFieldManager interface. For general information about fields, see on the Relativity Documentation site.

Click the following drop-down links to view sample code for fixed-length text, multiple choice, single object, and date fields.

View a list of available field types and their create methods

- Currency Copy

```text
1
2
3
4
Task<int> CreateCurrencyFieldAsync(

    int workspaceID,

    CurrencyFieldRequest fieldRequest

)
```

- Date Copy

```text
1
2
3
4
Task<int> CreateDateFieldAsync(

    int workspaceID,

    DateFieldRequest fieldRequest

)
```

- Decimal Copy

```text
1
2
3
4
Task<int> CreateDecimalFieldAsync(

    int workspaceID,

    DecimalFieldRequest fieldRequest

)
```

- File Copy

```text
1
2
3
4
Task<int> CreateFileFieldAsync(

    int workspaceID,

    FileFieldRequest fieldRequest

)
```

- Fixed-length text Copy

```text
1
2
3
4
Task<int> CreateFixedLengthFieldAsync(

    int workspaceID,

    FixedLengthFieldRequest fieldRequest

)
```

- Long text Copy

```text
1
2
3
4
Task<int> CreateLongTextFieldAsync(

    int workspaceID,

    LongTextFieldRequest fieldRequest

)
```

- Multiple choice Copy

```text
1
2
3
4
Task<int> CreateMultipleChoiceFieldAsync(

    int workspaceID,

    MultipleChoiceFieldRequest fieldRequest

)
```

- Multiple object Copy

```text
1
2
3
4
Task<int> CreateMultipleObjectFieldAsync(

    int workspaceID,

    MultipleObjectFieldRequest fieldRequest

)
```

- Single choice Copy

```text
1
2
3
4
Task<int> CreateSingleChoiceFieldAsync(

    int workspaceID,

    SingleChoiceFieldRequest fieldRequest

)
```

- Single object Copy

```text
1
2
3
4
Task<int> CreateSingleObjectFieldAsync(

    int workspaceID,

    SingleObjectFieldRequest fieldRequest

)
```

- User Copy

```text
1
2
3
4
Task<int> CreateUserFieldAsync(

    int workspaceID,

    UserFieldRequest fieldRequest

)
```

- Whole number Copy

```text
1
2
3
4
Task<int> CreateWholeNumberFieldAsync(

    int workspaceID,

    WholeNumberFieldRequest fieldRequest

)
```

- Yes/No Copy

```text
1
2
3
4
Task<int> CreateYesNoFieldAsync(

    int workspaceID,

    YesNoFieldRequest fieldRequest

)
```

Create a fixed-length text field

The following code sample illustrates how to instantiate a FixedLengthFieldRequest object with properties specified for the new field. To create the field, call the CreateFixedLengthFieldAsync() method by passing the Artifact ID of workspace where you want to add the field, and the FixedLengthFieldRequest instance.

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
public static async Task CreateFixedLength_Async()

{

    int workspaceID = 1018486;

    int documentArtifactTypeId = 10;

    string imageBase64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIpSURBVDjLddM9aFRBFIbh98zM3WyybnYVf4KSQjBJJVZBixhRixSaShtBMKUoWomgnaCxsJdgIQSstE4nEhNREgyoZYhpkogkuMa4/3fuHIu7gpLd00wz52POMzMydu/Dy958dMwYioomIIgqDa+VnWrzebNUejY/NV6nQ8nlR4ufXt0fzm2WgxUgqBInAWdhemGbpcWNN9/XN27PPb1QbRdgjEhPqap2ZUv5+iOwvJnweT1mT5djZKjI6Ej/udz+wt1OJzAKYgWyDjJWyFghmzFsbtcY2gsTJwv09/Vc7RTgAEQgsqAKaoWsM8wu/z7a8B7vA8cHD3Fr+ktFgspO3a+vrdVfNEulJ/NT4zWngCBYY1oqSghKI465fvYwW+VAatPX07IZmF7YfrC0uDE8emPmilOFkHYiBKxAxhmSRPlZVVa2FGOU2Ad2ap4zg92MDBXJZczFmdflx05VEcAZMGIIClZASdesS2cU/dcm4sTBArNzXTcNakiCb3/HLRsn4Fo2qyXh3WqDXzUlcgYnam3Dl4Hif82dbOiyiBGstSjg4majEpl8rpCNUQUjgkia0M5GVAlBEBFUwflEv12b/Hig6SmA1iDtzhcsE6eP7LIxAchAtwNVxc1MnhprN/+lh0txErxrPZVdFdRDEEzHT6LWpTbtq+HLSDDiOm2o1uqlyOT37bIhHdKaXoL6pqhq24Dzd96/tUYGwPSBVv7atFglaFIu5KLuPxeX/xsp7aR6AAAAAElFTkSuQmCC";

    int objectViewArtifactId = 1018362;

    FixedLengthFieldRequest request = new FixedLengthFieldRequest

    {

        Name = "Fixed-length Document Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = documentArtifactTypeId },

        Length = 255,

        Source = "",

        IsRequired = true,

        IncludeInTextIndex = false,

        HasUnicode = false,

        AllowHtml = false,

        OpenToAssociations = false,

        IsLinked = false,

        IsRelational = true,

        FriendlyName = "Friendly Name",

        ImportBehavior = ImportBehavior.LeaveBlankValuesUnchanged,

        PaneIcon = new PaneIcon

        {

            FileName = "File Name",

            ImageBase64 = imageBase64

        },

        Order = 150,

        RelationalView = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactTypeId = objectViewArtifactId }),

        "Shortcut": {

            "ModifierKeys": [

                "Alt",

                "Ctrl",

                "Shift"

            ],

            "MainKey": "Home"

        },

        RelativityApplications = new List<ObjectIdentifier>(),

        Keywords = "Keywords",

        Notes = "Notes"

    };

    using (Relativity.ObjectModel.V1.Field fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field>())

    {

        try

        {

            int newfieldArtifactID = await fieldManager.CreateFixedLengthFieldAsync(workspaceID, request);

            string info = string.Format("Created fixed-length field with Artifact ID {0}", newfieldArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Create a multiple choice field

The following code sample illustrates how to instantiate a MultipleChoiceFieldRequest object with properties specified for the new field. To create the field, call the CreateMultipleChoiceFieldAsync() method by passing the Artifact ID of workspace where you want to add the field, and the MultipleChoiceFieldRequest instance.

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
public static async Task CreateMultipleChoiceField_Async()

{

    int workspaceID = 1018486;

    int parentObjectArtifactId = 1456834;

    int relativityApplicationArtifactId1 = 1363829;

    int relativityApplicationArtifactId2 = 1283746;

    MultipleChoiceFieldRequest request = new MultipleChoiceFieldRequest

    {

        Name = "Multiple Choice Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = parentObjectArtifactId },

        Source = "",

        IsRequired = false,

        HasUnicode = true,

        OpenToAssociations = true,

        OverlayBehavior = OverlayBehavior.ReplaceValues,

        IsLinked = false,

        AllowSortTally = true,

        Wrapping = true,

        AllowGroupBy = false,

        AllowPivot = false,

        RelativityApplications = new List<ObjectIdentifier>

        {

            new ObjectIdentifier { ArtifactTypeId = relativityApplicationArtifactId1 },

            new ObjectIdentifier { ArtifactTypeId = relativityApplicationArtifactId2 }

        },

        AutoAddChoices = true,

        Keywords = "Keywords",

        Notes = "Notes"

    };

    using (Relativity.ObjectModel.V1.Field fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field>())

    {

        try

        {

            int newfieldArtifactID = await fieldManager.CreateMultipleChoiceFieldAsync(workspaceID, request);

            string info = string.Format("Created multiple choice field with Artifact ID {0}", newfieldArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Create a single object field

The following code sample illustrates how to instantiate a SingleObjectFieldRequest object with properties specified for the new field. To create the field, call the CreateSingleObjectFieldAsync() method by passing the Artifact ID of workspace where you want to add the field, and the SingleObjectFieldRequest instance.

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
public static async Task CreateSingleObjectField_Async()

{

    int workspaceID = 1018486;

    int documentArtifactTypeId = 10;

    int associativeObjectTypeArtifactId = 1827364;

    int objectViewArtifactId = 1017635;

    int propagateField1 = 1213485;

    int propagateField2 = 1023748;

    SingleObjectFieldRequest request = new SingleObjectFieldRequest

    {

        Name = "Single Object Document Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = documentArtifactTypeId },

        AssociativeObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = associativeObjectTypeArtifactId },

        Source = "",

        IsRequired = false,

        AvailableInFieldTree = true,

        FieldTreeView = new DisplayableObjectTypeIdentifier { ArtifactTypeId = objectViewArtifactId },

        OpenToAssociations = true,

        PropagateTo = new List<ObjectIdentifier>

        {

            new ObjectIdentifier { ArtifactTypeId = propagateField1 },

            new ObjectIdentifier { ArtifactTypeId = propagateField2 }

        },

        IsLinked = false,

        FilterType = FilterType.Popup,

        PopupPickerView = new DisplayableObjectTypeIdentifier { ArtifactTypeId = objectViewArtifactId },

        AllowSortTally = true,

        Width = 50,

        Wrapping = true,

        AllowGroupBy = false,

        AllowPivot = false,

        Keywords = "Keywords",

        Notes = "Notes"

    };

    using (Relativity.ObjectModel.V1.Field fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field>())

    {

        try

        {

            int newfieldArtifactID = await fieldManager.CreateSingleObjectFieldAsync(workspaceID, request);

            string info = string.Format("Created single object field with Artifact ID {0}", newfieldArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Create a date field

The following code sample illustrates how to instantiate a DateFieldRequest object with properties specified for the new field. To create the field, call the CreateDateFieldAsync() method by passing the Artifact ID of workspace where you want to add the field, and the DateFieldRequest instance.

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
public static async Task CreateDateField_Async()

{

    int workspaceID = 1018486;

    int documentArtifactTypeId = 10;

    DateFieldRequest request = new DateFieldRequest

    {

        Name = "Date Document Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeID = documentArtifactTypeId },

        Source = "Source Name",

        IsRequired = false,

        Formatting = Formatting.Date,

        OpenToAssociations = false,

        IsLinked = false,

        FilterType = FilterType.None,

        AllowSortTally = false,

        Width = null,

        AllowGroupBy = false,

        AllowPivot = false,

        Wrapping = false,

        RelativityApplications = new List<ObjectIdentifier>(),

        Keywords = "Keywords",

        Notes = "Notes"

    };

    using (Relativity.ObjectModel.V1.Field fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field>())

    {

        try

        {

            int newfieldArtifactID = await fieldManager.CreateDateFieldAsync(workspaceID, request);

            string info = string.Format("Created date field with Artifact ID {0}", newfieldArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Read a field

You can retrieve basic or extended metadata for a field. The extended metadata also includes operations that user has permissions to perform on the field. If you want to return extended information, use the overloaded method by passing Boolean values set to true for additional metadata and permissions as follows:

Copy

```text
1
FieldResponse response = await fieldManager.ReadAsync(workspaceId, fieldArtifactId, true, true);
```

The following code sample illustrates how to call the ReadAsync() method by passing only the Artifact IDs of the workspace and the field. Consequently, it returns only basic information. For a list of basic and extended properties, see Read a field in Field Manager (REST) .

View code sample Copy

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
public static async Task Read_Async()

{

    int workspaceID = 1018486;

    int fieldArtifactID = 1039509;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            FieldResponse response = await fieldManager.ReadAsync(workspaceID, fieldArtifactID);

            string info = string.Format("Read field {0} with Artifact ID {1}", response.ObjectIdentifier.Name, response.ObjectIdentifier.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update a field

You can update fields by using the methods available on the IFieldManager interface. All field types have an overloaded update method called by passing the Artifact IDs of a workspace and a field, the appropriate request object for the field type, and an optional DateTime object.

When you want to ensure you only update a field if it hasn't been modified since you read it, provide the lastmodifiedby value. The update will fail if the field has been changed in the meantime and return a 409 error. You can get the value of this property from an FieldResponse object, which is returned by the ReadAsync() method.

The MultipleChoiceFieldRequest and SingleChoiceFieldRequest objects have an AutoAddChoices property. If you change this property from No to Yes on a specific field, and applications in your workspace use this field, you must re-add the field to each application to include the choices. The RelativityApplications property on these request objects include a list of the applications containing the field.

Click the following drop-down links to view sample code for fixed-length text, multiple choice, single object, and date fields.

View a list of available field types and their update methods

- Currency Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    CurrencyFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateCurrencyFieldAsync(

    int workspaceID,

    int fieldID,

    CurrencyFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Date Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    DateFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    DateFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Decimal Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    DecimalFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    DecimalFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- File Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    FileFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    FileFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Fixed-length text Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    FixedLengthFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    FixedLengthFieldRequest fieldRequest

)
```

- Long text Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    LongTextFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateLongTextFieldAsync(

    int workspaceID,

    int fieldID,

    LongTextFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Multiple choice Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    MultipleChoiceFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    MultipleChoiceFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Multiple object Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    MultipleObjectFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    MultipleObjectFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Single choice Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    SingleChoiceFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateSingleChoiceFieldAsync(

    int workspaceID,

    int fieldID,

    SingleChoiceFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Single object Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    SingleObjectFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    SingleObjectFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- User Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    UserFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    UserFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Whole number Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    WholeNumberFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateWholeNumberFieldAsync(

    int workspaceID,

    int fieldID,

    WholeNumberFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

- Yes/No Copy

```text
1
2
3
4
5
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    YesNoFieldRequest fieldRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateAsync(

    int workspaceID,

    int fieldID,

    YesNoFieldRequest fieldRequest,

    DateTime lastModifiedOn

)
```

Update a fixed-length text field

The following code sample illustrates how to instantiate FixedLengthFieldRequest object with the properties used for updating the field. To update the field, call the UpdateAsync() method by passing the Artifact IDs of the workspace and field, and the FixedLengthFieldRequest instance.

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
public static async Task UpdateFixedLength_Async()

{

    int workspaceID = 1018486;

    int documentArtifactTypeId = 10;

    string imageBase64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIpSURBVDjLddM9aFRBFIbh98zM3WyybnYVf4KSQjBJJVZBixhRixSaShtBMKUoWomgnaCxsJdgIQSstE4nEhNREgyoZYhpkogkuMa4/3fuHIu7gpLd00wz52POMzMydu/Dy958dMwYioomIIgqDa+VnWrzebNUejY/NV6nQ8nlR4ufXt0fzm2WgxUgqBInAWdhemGbpcWNN9/XN27PPb1QbRdgjEhPqap2ZUv5+iOwvJnweT1mT5djZKjI6Ej/udz+wt1OJzAKYgWyDjJWyFghmzFsbtcY2gsTJwv09/Vc7RTgAEQgsqAKaoWsM8wu/z7a8B7vA8cHD3Fr+ktFgspO3a+vrdVfNEulJ/NT4zWngCBYY1oqSghKI465fvYwW+VAatPX07IZmF7YfrC0uDE8emPmilOFkHYiBKxAxhmSRPlZVVa2FGOU2Ad2ap4zg92MDBXJZczFmdflx05VEcAZMGIIClZASdesS2cU/dcm4sTBArNzXTcNakiCb3/HLRsn4Fo2qyXh3WqDXzUlcgYnam3Dl4Hif82dbOiyiBGstSjg4majEpl8rpCNUQUjgkia0M5GVAlBEBFUwflEv12b/Hig6SmA1iDtzhcsE6eP7LIxAchAtwNVxc1MnhprN/+lh0txErxrPZVdFdRDEEzHT6LWpTbtq+HLSDDiOm2o1uqlyOT37bIhHdKaXoL6pqhq24Dzd96/tUYGwPSBVv7atFglaFIu5KLuPxeX/xsp7aR6AAAAAElFTkSuQmCC";

    int objectViewArtifactId = 1018362;

    int fieldId = 1523633;

    FixedLengthFieldRequest request = new FixedLengthFieldRequest

    {

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = documentArtifactTypeId },

        Length = 300,

        Source = "",

        IsRequired = true,

        IncludeInTextIndex = false,

        HasUnicode = false,

        AllowHtml = true,

        OpenToAssociations = true,

        IsLinked = false,

        AllowSortTally = true,

        Wrapping = true,

        IsRelational = true,

        FriendlyName = "Friendly Name",

        ImportBehavior = ImportBehavior.LeaveBlankValuesUnchanged,

        PaneIcon = new PaneIcon

        {

            FileName = "File Name",

            ImageBase64 = imageBase64

        },

        Order = 200,

        RelationalView = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactTypeId = objectViewArtifactId }),

        "Shortcut": {

            "ModifierKeys": [

                "Alt",

                "Ctrl",

                "Shift"

            ],

            "MainKey": "Home"

        },

        RelativityApplications = new List<ObjectIdentifier>(),

        Keywords = "Updated Keywords",

        Notes = "Updated Notes"

    };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            await fieldManager.UpdateAsync(workspaceID, fieldId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Update a multiple choice field

The following code sample illustrates how to instantiate MultipleChoiceFieldRequest object with the properties used for updating the field. To update the field, call the UpdateAsync() method by passing the Artifact IDs of the workspace and field, and the MultipleChoiceFieldRequest instance.

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
public static async Task UpdateMultipleChoiceField_Async()

{

    int workspaceID = 1018486;

    int parentObjectArtifactId = 1456834;

    int relativityApplicationArtifactId1 = 1363829;

    int relativityApplicationArtifactId2 = 1283746;

    int fieldId = 1523633;

    MultipleChoiceFieldRequest request = new MultipleChoiceFieldRequest

    {

        Name = "Multiple Choice Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = parentObjectArtifactId },

        Source = "",

        IsRequired = true,

        HasUnicode = false,

        OpenToAssociations = true,

        OverlayBehavior = OverlayBehavior.MergeValues,

        IsLinked = true,

        AllowSortTally = true,

        Wrapping = false,

        AllowGroupBy = true,

        AllowPivot = true,

        RelativityApplications = new List<ObjectIdentifier>

        {

            new ObjectIdentifier { ArtifactTypeId = relativityApplicationArtifactId1 },

            new ObjectIdentifier { ArtifactTypeId = relativityApplicationArtifactId2 }

        },

        AutoAddChoices = true,

        Keywords = "Updated Keywords",

        Notes = "Updated Notes"

    };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            await fieldManager.UpdateAsync(workspaceID, fieldId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Update a single object field

The following code sample illustrates how to instantiate SingleObjectFieldRequest object with the properties used for updating the field. To update the field, call the UpdateAsync() method by passing the Artifact IDs of the workspace and field, and the SingleObjectFieldRequest instance.

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
public static async Task UpdateSingleObjectField_Async()

{

    int workspaceID = 1018486;

    int documentArtifactTypeId = 10;

    int associativeObjectTypeArtifactId = 1827364;

    int objectViewArtifactId = 1017635;

    int propagateField1 = 1213485;

    int fieldId = 1523633;

    SingleObjectFieldRequest request = new SingleObjectFieldRequest

    {

        Name = "Single Object Document Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = documentArtifactTypeId },

        AssociativeObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = associativeObjectTypeArtifactId },

        Source = "",

        IsRequired = false,

        AvailableInFieldTree = true,

        FieldTreeView = new DisplayableObjectTypeIdentifier { ArtifactTypeId = objectViewArtifactId },

        OpenToAssociations = true,

        PropagateTo = new List<ObjectIdentifier> { new ObjectIdentifier { ArtifactTypeId = propagateField1 } },

        IsLinked = false,

        FilterType = FilterType.TextBox,

        AllowSortTally = true,

        Width = 150,

        Wrapping = true,

        AllowGroupBy = false,

        AllowPivot = false,

        Keywords = "Updated Keywords",

        Notes = "Updated Notes"

    };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            await fieldManager.UpdateAsync(workspaceID, fieldId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Update a date field

The following code sample illustrates how to instantiate DateFieldRequest object with the properties used for updating the field. To update the field, call the UpdateAsync() method by passing the Artifact IDs of the workspace and field, and the DateFieldRequest instance.

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
public static async Task UpdateDateField_Async()

{

    int workspaceID = 1018486;

    int documentArtifactTypeId = 10;

    int fieldId = 1523633;

    DateFieldRequest request = new DateFieldRequest

    {

        Name = "Date Document Field",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeId = documentArtifactTypeId },

        Source = "Source Name",

        IsRequired = false,

        Formatting = Formatting.DateTime,

        OpenToAssociations = false,

        IsLinked = false,

        FilterType = FilterType.None,

        AllowSortTally = false,

        Width = null,

        AllowGroupBy = false,

        AllowPivot = false,

        Wrapping = false,

        RelativityApplications = new List<ObjectIdentifier>(),

        Keywords = "Updated Keywords",

        Notes = "Updated Notes"

    };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            await fieldManager.UpdateAsync(workspaceID, fieldId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete a field

You can remove a field from an object type by calling the DeleteAsync()method, and passing Artifact IDs of a workspace and a field to it.

View code sample Copy

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

public static async Task Delete_Async()

{

    int workspaceID = 1018486;

    int fieldId = 1039269;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            await fieldManager.DeleteAsync(workspaceID, fieldId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve available object types

You create fields on parent object types available in a workspace. The AvailableObjectTypesAsync() retrieves a list of these objects available in a specified workspace.

View code sample Copy

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
public static async Task GetAvailableObjectTypes_Async()

{

    int workspaceID = 1018486;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<DisplayableObjectTypeIdentifier> response = await fieldManager.AvailableObjectTypesAsync(workspaceID);

            foreach (DisplayableObjectTypeIdentifier objectType in response)

            {

                string info = string.Format("Read objectType {0} with Artifact ID {1}", objectType.Name, objectType.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve available views for an object type

You can retrieve a list of available views for a specific object type that you can then use when creating or updating a new field. The AvailableObjectTypeViewsAsync() method retrieves this information for the field tree, pop-up picker, and relational views. The relational view is available only for documents. For more information, see on the RelativityDocumentation site.

The following code sample illustrates how to call this method by passing the Artifact ID of a workspace. It returns a list of DisplayableObjectIdentifier instances that contain the Artifact ID and other information for each view.

View code sample Copy

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
public static async Task GetAvailableObjectTypeViews_Async()

{

    int workspaceID = 1018486;

    DisplayableObjectTypeIdentifier objectType = new DisplayableObjectTypeIdentifier { ArtifactID = 1425337 };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<Securable<DisplayableObjectIdentifier>> response = await fieldManager.AvailableObjectTypeViewsAsync(workspaceID, objectType);

            foreach (DisplayableObjectIdentifier objectTypeView in response)

            {

                string info = string.Format("Read objectTypeView {0} with Artifact ID {1}", objectTypeView.Name, objectTypeView.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve available fields for propagation

When creating a field, you can control whether coding values propagate to a specific group of related items. For more information about propagation, see on the Relativity Documentation site.

Use the AvailablePropagateToFieldsAsync() method to retrieve a list of fields available for propagation in a specific workspace. The following code sample illustrates how to call this method by the Artifact ID of a workspace. It returns a list of DisplayableObjectIdentifier instances that contain the Artifact ID and other information for each view.

View code sample Copy

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
public static async Task GetAvailablePropagateToFields_Async()

{

    int workspaceID = 1018486;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await fieldManager.AvailablePropagateToFieldsAsync(workspaceID);

            foreach (DisplayableObjectIdentifier field in response)

            {

                string info = string.Format("Read field {0} with Artifact ID {1}", field.Name, field.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve object types for a single object field

A single object field defines a one-to-many relationship between the object type that the field is on, and another object type. For more information about single object fields, see on the Relativity Documentation site.

Use the AvailableSingleAssociativeObjectTypesAsync() method to retrieve a list of compatible object types for a single object field. The following code illustrates how to call this method by passing the Artifact ID of a workspace, and an DisplayableObjectTypeIdentifier instance containing the Artifact ID of the object type that the field is on.

View code sample Copy

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
public static async Task GetAvailableSingleAssociativeObjectTypes_Async()

{

    int workspaceID = 1018486;

    DisplayableObjectTypeIdentifier objectType = new DisplayableObjectTypeIdentifier { ArtifactID = 1523463 };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<DisplayableObjectTypeIdentifier> response = await fieldManager.AvailableSingleAssociativeObjectTypesAsync(workspaceID, objectType);

            foreach (DisplayableObjectTypeIdentifier objectTypeResponse in response)

            {

                string info = string.Format("Read objectType {0} with Artifact ID {1}", objectTypeResponse.Name, objectTypeResponse.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve object types for a multiple object field

A multiple object field defines a many-to-many relationship between the object type that the field is on, and another object type. For more information about multiple object fields, see on the Relativity Documentation site.

Use the AvailableMultiAssociativeObjectTypesAsync() to retrieve a list of compatible object types for a multiple object field. The following code illustrates how to call this method by passing the Artifact ID of a workspace, and an DisplayableObjectTypeIdentifier instance containing the Artifact ID of the object type that the field is on.

View code sample Copy

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
public static async Task GetAvailableMultiAssociativeObjectTypes_Async()

{

    int workspaceID = 1018486;

    DisplayableObjectTypeIdentifier objectType = new DisplayableObjectTypeIdentifier { ArtifactID = 1425337 };

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<DisplayableObjectTypeIdentifier> response = await fieldManager.AvailableMultiAssociativeObjectTypesAsync(workspaceID, objectType);

            foreach (DisplayableObjectTypeIdentifier objectTypeResponse in response)

            {

                string info = string.Format("Read objectType {0} with Artifact ID {1}", objectTypeResponse.Name, objectTypeResponse.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve keyboard shortcuts

You can retrieve a list of keyboard shortcuts currently defined in a workspace. In the Relativity UI, this list is displayed when you click the Keyboard Shortcuts Legend icon. For more information, see Keyboard shortcuts on the Relativity Documentation site.

Use the AvailableKeyboardShortcutsAsync() method to retrieve a list of keyboard shortcuts currently defined in a workspace. The following code sample illustrates how to this method by passing the Artifact ID of a workspace. It returns a list of KeyboardShortcut objects.

View code sample Copy

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
public static async Task GetAvailableKeyboardShortcuts_Async()

{

    int workspaceID = 1018486;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<KeyboardShortcut> response = await fieldManager.AvailableKeyboardShortcutsAsync(workspaceID);

            foreach (KeyboardShortcut shortcut in response)

            {

                string info = string.Format("Read keyboard shortcut {0} with action {1}", shortcut.Shortcut, shortcut.Action);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve valid keys

When creating or updating a field on a Document object, you can assign a keyboard shortcut to it. The shortcut key is a combination of a CTRL, ALT, or SHIFT key, and an alphanumeric or other key. For more information, see on the Relativity Documentation site.

Use the ValidKeysAsync() method to retrieve keys available for use in a keyboard shortcut. The following code sample illustrates how to call this method by passing the Artifact ID of a workspace. It returns a list of strings representing available keys.

View code sample Copy

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
public static async Task GetValidKeys_Async()

{

    int workspaceID = 1018486;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<String> response = await fieldManager.ValidKeys(workspaceID);

            foreach (String key in response)

            {

                string info = string.Format("Read key {0}", key);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve the order of relational field icons

You can retrieve the current order for relational field icons displayed in the Related Items pane of the core reviewer interface. The order assigned to a relational field icon determines its position relative to other icons in the Related Items pane. A relational field icon with a lower order number is displayed on the left, while those with the same order number are sorted alphanumerically.

In the Relativity UI, you can add or edit fields in the Fields layout, which contains the View Order button for relational field properties. Click this button to display the current order for icons in the Related Items pane. For more information, see on the Relativity

Use the RelationalOrderAsync() method to retrieve the current display order for the icons of relational fields available in a specific workspace. The following code sample illustrates how to call this method by passing the Artifact ID of a workspace. It returns a list of RelationalFieldOrder instances that contain the name and type of a relational field, and display order for its icon.

View code sample Copy

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
public static async Task GetRelationalFieldOrder_Async()

{

    int workspaceID = 1018486;

    using (Relativity.ObjectModel.V1.Field.IFieldManager fieldManager = serviceFactory.CreateProxy<Relativity.ObjectModel.V1.Field.IFieldManager>())

    {

        try

        {

            List<RelationalFieldOrder> response = await fieldManager.RelationalOrderAsync(workspaceID);

            foreach (RelationalFieldOrder relationalFieldOrder in response)

            {

                string info = string.Format("Read Relational Field {0} with Type {1} and Order {2}",

                     relationalFieldOrder.Name, relationalFieldOrder.Type, relationalFieldOrder.Order);

                Console.WriteLine(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```
