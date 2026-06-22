---
title: "Field Mapping Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Field_Mapping_API.htm
collection: developer
fetched_at: 2026-06-22T06:26:14+00:00
sha256: 6039f7998311270b6d44e459e420a258484f79734bbaf2b7903e4489c4f55446
---

Field Mapping Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Field Mapping Manager

You can use the Field Mapping service to perform various operations related to mapping fields between Relativity and an external data source. It supports retrieving fields available for mapping from the data source and retrieving fields in Relativity that are already mapped. In addition, it provides methods for updating and reading existing field mappings.

Currently, this service supports managing only the mappings between fields in Relativity and Invariant. This functionality supports the processing feature available in Relativity. For more information, see Processing on the Relativity Documentation site.

When developing an application, you can use the Field Mapping service to return fields used for mapping in a custom UI. For example, you might develop a custom dialog that gets populated with mappable fields. The Relativity UI includes the following dialog that exemplifies this functionality:

You can also use the Field Mapping service through the REST API. For more information, see Field Mapping Manager (REST) .

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Field mapping fundamentals

The Relativity.Services.FieldMapping namespace contains the IFieldMapping interface and other classes required to map fields between Invariant and Relativity. You can use the IFieldMapping interface to access the methods that it provides for working with fields available for mapping. This interface includes the following methods:

- GetAllMappedFieldsAsync() : retrieves an array of ExternalMapping objects. These objects represent Relativity fields currently mapped to Invariant fields. See Retrieve mapped Relativity fields .

- GetCatalogFieldsAsync() : See Retrieve the contents of the Catalog Field table

- GetAutomappedFieldGuidsAsync() : retrieves a list of GUIDs that Invariant uses to identify certain processing system fields, which it automatically maps during a publish operation. See Retrieve GUIDs for automapped fields .

- GetInvariantFieldsAsync() : retrieves an array of MappableSourceField objects, which represent fields from Invariant that are available for field mapping. See Retrieve Invariant fields available for mapping .

- GetInvariantFieldsPaginatedAsync() : See Retrieve Invariant fields available for mapping (paginated)

- GetMetadataFieldsAsync() : see Retrieve metadata fields

- GetOtherFieldsAsync() : See Retrieve non-metadata fields

- GetMappableSourceFieldAsync() : See Retrieve field given source name

- IsFieldMappingAvailableAsync() : checks the availability of an external data source. See Check field mapping availability .

- ReadExternalMappingAsync() : retrieves the external field mapping for a field with a specified Artifact ID as an ExternalMapping object. See Retrieve an external field mapping .

- UpdateExternalMappingAsync() : modifies or inserts field mapping data. This method returns a Boolean value. See Update an external field mapping .

In addition, the Relativity.Services.FieldMapping namespace also contains the following classes:

- ExternalMapping class – represents a mapping between a Relativity field and an external data source field. Its properties include the name, Artifact ID, and GUID of the Relativity field. Additional properties include the field name in the external data source, mapping ID, and others. The GetAllMappedFieldsAsync(), ReadExternalMappingAsync(), and UpdateExternalMappingAsync() methods return an object of this type.

- MappableSourceField class – represents a field from an external data source that is available for mapping. For example, it represents an Invariant field that a user can map to a Relativity field. Its properties include a list of Relativity fields mapped to this field, source name, category for the metadata that it represents, data type, and others. The GetInvariantFieldsAsync() method returns an object of this type.

### Common field mapping workflow

A common workflow for field mapping includes the following steps:

- Call the GetInvariantFieldsAsync() method to retrieve all the fields that Invariant has available for mapping.

- Display the Invariant fields in the Relativity UI. Users can set the field mapping by selecting the fields in Relativity that they want mapped to the Invariant fields.

- Optionally, implement predefined mappings. Call the GetAllMappedFieldsAsync() method to return a list of GUIDs that specify Relativity fields already mapped.

- Call the UpdateExternalMappingAsync() method to set the new field mappings.

### Code samples for the Field Mapping service

Review the code samples to learn about using the Field Mapping service to perform retrieval, update, and other operations. These code samples illustrate how to perform the following general tasks, and how to call specific methods on the Field Mapping service:

- Use helper classes to create the proxy and select an appropriate authentication type. See Relativity API Helpers .

- Create the Services API proxy within a using block in your code.

- Call specific methods on the Field Mapping service within a try-catch block.

- Use await/async design pattern.

- Use the logging framework for troubleshooting and debugging purposes. See Log from a Relativity application .

## Check field mapping availability

From Relativity, you can make a call to the IsFieldMappingAvailableAsync() method to check the availability of an external data source. This method returns true when field mapping is available. When this method returns false, your data source isn't currently available. You may want to contact your system admin to troubleshoot this issue.

- Method

-

IsFieldMappingAvailableAsync: Returns a boolean flag indicating whether or not Field Mapping functionality is available

- Parameters

- <int>workspaceID: The workspace artifact identifier

- Returns

- boolean flag indicating whether or not Field Mapping functionality is available

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    bool fieldMappingAvailable = await proxy.IsFieldMappingAvailableAsync(data.WorkspaceId).ConfigureAwait(false);

}
```

## Retrieve mapped Relativity fields

From Invariant, you can call the GetAllMappedFieldsAsync() method to retrieve an array of Relativity fields currently mapped to Invariant fields.

- Method

- GetAllMappedFieldsAsync: Returns a list of mapped Relativity fields

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <int> dataSourceID: The Artifact ID of the processing data source used to populate the mapped fields. Set this value only if you want an audit of the mapped fields added to the corresponding data source in Relativity. In all other cases, pass the integer 0 as the parameter.

- <List<Guid>>fieldsToAppend: An optional list of GUIDs corresponding to Relativity fields, which have field data returned for them regardless of whether are mapped to a data source. Only Invariant currently uses this field. For general use, send in the empty list for this parameter

- Returns

- List of ExternalMapping objects

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    List<ExternalMapping> mappings = await proxy.GetAllMappedFieldsAsync(data.WorkspaceId, dataSourceID, new List<Guid>()).ConfigureAwait(false);

}
```

## Retrieve the contents of the Catalog Field table

- Method

- GetCatalogFieldsAsync: Returns the contents of the Catalog Field table

- Parameters

- • <int>workspaceID: The workspace artifact identifier

- Returns

-

Array of CatalogField objects

- <Guid>CatalogFieldGuid: The unique identifier of the Catalog Field

- <string>FieldName: The name of the Catalog Field, i.e. "Author", "Last Updated"

- <string>Description: Description of the nature of the data that the Catalog Field is intended to contain

- <string>FieldType: Relativity Field Type of the field

- <int>Length: The maximum length of the field. Only applies to Fixed Length (FieldType.Varchar) fields.

- <string>Category: Category of the field

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    CatalogField[] catalogFields = await proxy.GetCatalogFieldsAsync(data.WorkspaceId).ConfigureAwait(false);

}
```

## Retrieve Invariant fields available for mapping

From Relativity, you can call the GetInvariantFieldsAsync() method to retrieve an array of Invariant fields available for field mapping. This array includes Invariant fields that haven't been mapped to any Relativity fields.

- Method

- GetInvariantFieldsAsync: Retrieves a list of fields from Invariant that are available for field mapping

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <bool>catalogFieldsOnly: A flag indicating whether only Catalog fields should be returned. The Field Catalog is a collection of industry best practice fields used with processing. It currently includes 127 fields consistently populated with document metadata. For more information, see Mapping processing fields on the Documentation site.

- Returns

- list of MappableSourceField objects

- <string>Category: The category of the metadata stored in the field.

- <string>SourceName: The name of the field used by the external data source.

- <string>FriendlyName: The "user-friendly" name of the source field.

- <string>Description: A verbose description of the data represented by the source field.

- <string>DataType: The type of data stored in the field. Common data types are String, Int32, DateTime, Boolean, or Collection.

- <List<string>>MappedFields: A list of Relativity fields currently mapped to this field.

- <int>Length: The minimum acceptable length for a fixed-length text source field

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    List<MappableSourceField> sourceFields = await proxy.GetInvariantFieldsAsync(data.WorkspaceId, false).ConfigureAwait(false);

}
```

## Retrieve Invariant fields available for mapping (paginated)

- Method

- GetInvariantFieldsPaginatedAsync: Retrieves an array of fields from Invariant that are available for field mapping and then paginated for performance

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <int>skip: The starting index to retrieve mappable fields.

- <int>top: The number of mappable fields to retrieve.

- fieldMappingRequest: object of type FieldMappingRequest

- Filter: object of type FieldFilter, properties to filter Invariant fields.

- <string>NameFilter

- <string>DataTypeFilter

- <string>DescriptionFilter

- <string>RelativityFieldNameFilter

- <string>SourceNameFilter

- SortingOption: object of type FieldSortingOption

- FieldName: FieldName enum option to sort on. Options are Name, DataType, Description, RelativityFieldName

- SortingDirection: SortingDirection enum to sort on. Options are Asc and Desc

- Returns

- FieldMappingResponse object

- <int> TotalCount: The total count of mappable fields retrieved after filtering.

- <List<MappableSourceField>> MappableFields: The mappable fields retrieved from Invariant after filtering and pagination

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
FieldMappingRequest request = new FieldMappingRequest

{

    Filter = new FieldFilter

    {

        NameFilter = "Hello World",

        DataTypeFilter = null,

        DescriptionFilter = null,

        RelativityFieldNameFilter = null

    },

    SortingOption = new FieldSortingOption

    {

        FieldName = FieldName.Name,

        SortingDirection = SortingDirection.Asc

    }

};

using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    FieldMappingResponse response = await proxy.GetInvariantFieldsPaginatedAsync(data.WorkspaceId, 0, 10, request).ConfigureAwait(false);

}
```

## Retrieve metadata fields

- Method

- GetMetadataFieldsAsync: Retrieves an array of metadata fields from Invariant

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <int>skip: The starting index to retrieve mappable fields.

- <int>top: The number of mappable fields to retrieve.

- fieldMappingRequest: object of type FieldMappingRequest

- Filter: object of type FieldFilter, properties to filter Invariant fields.

- <string>NameFilter

- <string>DataTypeFilter

- <string>DescriptionFilter

- <string>RelativityFieldNameFilter

- <string>SourceNameFilter

- SortingOption: object of type FieldSortingOption

- FieldName: FieldName enum option to sort on. Options are Name, DataType, Description, RelativityFieldName

- SortingDirection: SortingDirection enum to sort on. Options are Asc and Desc

- Returns

- FieldMappingResponse object

- <int> TotalCount: The total count of mappable fields retrieved after filtering.

- <List<MappableSourceField>> MappableFields: The mappable fields retrieved from Invariant after filtering and pagination

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
FieldMappingRequest request = new FieldMappingRequest

{

    Filter = new FieldFilter

    {

        NameFilter = "Metadata Field 1",

        DataTypeFilter = null,

        DescriptionFilter = null,

        RelativityFieldNameFilter = null

    },

    SortingOption = new FieldSortingOption

    {

        FieldName = FieldName.DataType,

        SortingDirection = SortingDirection.Desc

    }

};

using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    FieldMappingResponse response = await proxy.GetMetadataFieldsAsync(data.WorkspaceId, 0, 10, request).ConfigureAwait(false);

}
```

## Retrieve non-metadata fields

- Method

- GetOtherFieldsAsync: Retrieves an array of non-metadata fields from Invariant

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <int>skip: The starting index to retrieve mappable fields.

- <int>top: The number of mappable fields to retrieve.

- fieldMappingRequest: object of type FieldMappingRequest

- Filter: object of type FieldFilter, properties to filter Invariant fields.

- <string>NameFilter

- <string>DataTypeFilter

- <string>DescriptionFilter

- <string>RelativityFieldNameFilter

- <string>SourceNameFilter

- SortingOption: object of type FieldSortingOption

- FieldName: FieldName enum option to sort on. Options are Name, DataType, Description, RelativityFieldName

- SortingDirection: SortingDirection enum to sort on. Options are Asc and Desc

- Returns

- FieldMappingResponse object

- <int> TotalCount: The total count of mappable fields retrieved after filtering.

- <List<MappableSourceField>> MappableFields: The mappable fields retrieved from Invariant after filtering and pagination

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
FieldMappingRequest request = new FieldMappingRequest

{

    Filter = new FieldFilter

    {

        NameFilter = "Other Field 1",

        DataTypeFilter = null,

        DescriptionFilter = null,

        RelativityFieldNameFilter = null

    },

    SortingOption = new FieldSortingOption

    {

        FieldName = FieldName.Name,

        SortingDirection = SortingDirection.Desc

    }

};

using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    FieldMappingResponse response = await proxy.GetOtherFieldsAsync(data.WorkspaceId, 0, 10, request).ConfigureAwait(false);

}
```

## Retrieve field given source name

- Method

- GetMappableSourceFieldAsync: Returns field given source name

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <string>sourceName: Source name of field to return

- Returns

-

MappableSourceField object

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    MappableSourceField field = await proxy.GetMappableSourceFieldAsync(data.WorkspaceId, "MySourceField").ConfigureAwait(false);

}
```

## Retrieve an external field mapping

From Relativity, you can call the ReadExternalMappingAsync() method to retrieve the external field mapping for a field with a specified Artifact ID.

- Method

- ReadExternalMappingAsync: Retrieves an External Field Mapping for the given field ID, if one exists

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <int>fieldID: Artifact ID of the field with the mapping that you want to retrieve.

- <string>fieldSource: The field source name (e.g. "Invariant").

- Returns

-

ExternalMapping object

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    ExternalMapping mapping = await proxy.ReadExternalMappingAsync(data.WorkspaceId, fieldID, fieldSource).ConfigureAwait(false);

}
```

## Update an external field mapping

From Relativity, you can call the UpdateExternalMappingAsync() method to modify or insert field mapping data.

- Method

- UpdateExternalMappingAsync: Modifies or inserts a single field mapping record

- Parameters

- <int>workspaceID: The workspace artifact identifier.

- <int> fieldID: Target Field ID for the field mapping.

- <ExternalMapping>model: An ExternalMapping object with the updated data.

- Several properties such as FieldID, RelativityFieldName, ExternalFieldName (Invariant name), ExternalFieldSource, FriendlyName, and more. You must set the following properties on an External Mapping object to make a successful UpdateExternalMappingAsync() method call:

- ExternalFieldName - the name of the field in the external data source. Set this property to null if you want to remove the field mapping.

- ExternalFieldSource - the name of the external data source associated with the mapping. Currently, this fields should always be set to "Invariant".

- FieldArtifactId - the Artifact ID of the Relativity field being mapped.

In addition, you should also set specific fields that are used for validation. If you don't set these fields correctly, the field mapping may not update. The following list includes fields used for validation:

- CurrentLength - For fixed-length catalog fields, you must set this property to a minimum field length required for validation. For example, if the CurrentLength property is set to 0 when you attempt to map a fixed-length catalog field, the validation fails.

- FieldTypeId - The service validates the property against the data type that Invariant uses for the field source. For example, you may want to map a source field that Invariant identifies as a Date type. If you set the FieldTypeId property to 0 indicating a fixed-length text field, then the validation fails and the field isn't mapped. The values for this property correspond to the kCura.Relativity.Client.FieldType enumeration.

- ObjectType - You must set this property to 10.

- UseUnicodeEncoding - For text fields, you must set this property to true.

- <bool>validation – whether validation is enabled or not. Defaults to true

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
ExternalMapping model = new ExternalMapping

{

    FieldID = fieldID,

    ExternalFieldName = "FieldName",

    ExternalFieldSource = "Invariant"

};

using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    await proxy.UpdateExternalMappingAsync(data.WorkspaceId, fieldID, model).ConfigureAwait(false);

}
```

## Retrieve GUIDs for automapped fields

You can use the GetAutomappedFieldGuidsAsync() method to retrieve certain processing system fields that Invariant automatically maps during a publish operation. When you call this method, pass the Artifact ID of the workspace where you want to map fields. It returns a list of GUIDs for the corresponding ExternalMapping objects.

- Method

- GetAutoMappedFieldGuidsAsync: Returns a list of Guids corresponding to the Relativity fields that are automatically mapped by Invariant

- Parameters

- <int>workspaceID: The workspace artifact identifier

- Returns

- list of Guids corresponding to the Relativity fields that are automatically mapped by Invariant

Copy

```text
1
2
3
4
using (IFieldMappingManager proxy = _servicesMgr.CreateProxy<IFieldMappingManager>(ExecutionIdentity.CurrentUser))

{

    List<Guid> autoMappedFieldGuids = await proxy.GetAutoMappedFieldGuidsAsync(data.WorkspaceId).ConfigureAwait(false);

}
```

On this page

- Field Mapping Manager

- Field mapping fundamentals

- Common field mapping workflow

- Code samples for the Field Mapping service

- Check field mapping availability

- Retrieve mapped Relativity fields

- Retrieve the contents of the Catalog Field table

- Retrieve Invariant fields available for mapping

- Retrieve Invariant fields available for mapping (paginated)

- Retrieve metadata fields

- Retrieve non-metadata fields

- Retrieve field given source name

- Retrieve an external field mapping

- Update an external field mapping

- Retrieve GUIDs for automapped fields


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
