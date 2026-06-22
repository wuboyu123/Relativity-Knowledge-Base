---
title: "Field Mapping (.NET v0)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/v0/Field_Mapping_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:32+00:00
sha256: 94e476894b575b967ce3b9c306e647754f6b8fe33eb78d279f390d95ed82781f
---

Field Mapping (.NET v0)

# Field Mapping (.NET v0)

This content refers to Version 0 of the Processing APIs. For documentation on the latest version of this API, see Get started with the Processing SDK

You can use the Field Mapping service to perform various operations related to mapping fields between Relativity and an external data source. It supports retrieving fields available for mapping from the data source and retrieving fields in Relativity that are already mapped. In addition, it provides methods for updating and reading existing field mappings.

Currently, this service supports managing only the mappings between fields in Relativity and Invariant. This functionality supports the processing feature available in Relativity. For more information, see Processing on the Relativity Documentation site.

When developing an application, you can use the Field Mapping service to return fields used for mapping in a custom UI. For example, you might develop a custom dialog that gets populated with mappable fields. The Relativity UI includes the following dialog that exemplifies this functionality:

You can also use the Field Mapping service through the REST API. For more information, see Field Mapping Manager (REST) .

## Field mapping fundamentals

In the Services API, the Relativity.Services.FieldMapping namespace contains the IFieldMapping interface and other classes required to map fields between Invariant and Relativity. You can use the IFieldMapping interface to access the methods that it provides for working with fields available for mapping. This interface includes the following methods:

- GetAllMappedFieldsAsync() method – retrieves an array of ExternalMapping objects. These objects represent Relativity fields currently mapped to Invariant fields. See Retrieve mapped Relativity fields .

- GetAutomappedFieldGuidsAsync() method – retrieves a list of GUIDs that Invariant uses to identify certain processing system fields, which it automatically maps during a publish operation. See Retrieve GUIDs for automapped fields .

- GetInvariantFieldsAsync() method – retrieves an array of MappableSourceField objects, which represent fields from Invariant that are available for field mapping. See Retrieve Invariant fields available for mapping .

- IsFieldMappingAvailableAsync() method – checks the availability of an external data source. See Check field mapping availability .

- ReadExternalMappingAsync() method – retrieves the external field mapping for a field with a specified Artifact ID as an ExternalMapping object. See Retrieve an external field mapping .

- UpdateExternalMappingAsync() method – modifies or inserts field mapping data. This method returns a Boolean value. See Update an external field mapping .

This is not a recommended API call.

- ClearCachedDataAsync() method – used for testing and for clearing corrupted cache data. See Clear cached data .

In addition, the Relativity.Services.FieldMapping namespace also contains the following classes:

- ExternalMapping class – represents a mapping between a Relativity field and an external data source field. Its properties include the name, Artifact ID, and GUID of the Relativity field. Additional properties include the field name in the external data source, mapping ID, and others. The GetAllMappedFieldsAsync(), ReadExternalMappingAsync(), and UpdateExternalMappingAsync() methods return an object of this type.

- MappableSourceField class – represents a field from an external data source that is available for mapping. For example, it represents an Invariant field that a user can map to a Relativity field. Its properties include a list of Relativity fields mapped to this field, source name, category for the metadata that it represents, data type, and others. The GetInvariantFieldsAsync() method returns an object of this type.

For reference information about these classes and methods, see Class library reference .

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

From Relativity, you can make a call to the IsFieldMappingAvailableAsync() method to check the availability of an external data source. This method returns true when field mapping is available.

When this method returns false, your data source isn't currently available. You may want to contact your system admin to troubleshoot this issue.

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
public async Task<bool> IsFieldmappingAvailable(Client.SamplesLibrary.Helper.IHelper helper, int workspaceArtifactId)

{

      bool isAvailable = false;

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  isAvailable = await proxy.IsFieldMappingAvailableAsync(workspaceArtifactId);

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception,

                        "FieldMapping IsFieldmappingAvailableAsync failed for Workspace ID {0}", workspaceArtifactId);

            }

      }

      return isAvailable;

}
```

## Retrieve mapped Relativity fields

From Invariant, you can call the GetAllMappedFieldsAsync() method to retrieve an array of Relativity fields currently mapped to Invariant fields. You call this method from Invariant by passing the following arguments:

- The Artifact ID of the workspace where the fields reside.

- An optional list of GUIDs specifying Relativity fields that should be appended to the result set. You provide this list of GUIDs only if you want to implement predefined field mappings.

- The Artifact ID of the processing data source. Pass 0 if you don't want to specify a data source or audit the data.

This method returns an ExternalMapping object. See Field mapping fundamentals .

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
public async Task<ExternalMapping[]> GetAllMappedFields(Client.SamplesLibrary.Helper.IHelper helper, int workspaceArtifactId, Guid[] fieldsToAppend, int dataSourceId)

{

      ExternalMapping[] result = null;

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  result = await proxy.GetAllMappedFieldsAsync(workspaceArtifactId, fieldsToAppend, dataSourceId);

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception,

                        "FieldMapping Service GetAllMappedFieldsAsync call failed for Workspace ID {0}, Data Source ID {1}",

                              workspaceArtifactId, dataSourceId);

            }

      }

      return result;

}
```

## Retrieve Invariant fields available for mapping

From Relativity, you can call the GetInvariantFieldsAsync() method to retrieve an array of Invariant fields available for field mapping. This array includes Invariant fields that haven't been mapped to any Relativity fields. You call this method from Relativity by passing the Artifact ID of the workspace that contains the fields for mapping.

Additionally, you can also pass an optional Boolean value indicating whether the method should return only fields included in the Field Catalog. The Field Catalog is a collection of industry best practice fields used with processing. It currently includes 127 fields consistently populated with document metadata. For more information, see Mapping processing fields on the Documentation site.

The GetInvariantFieldsAsync() method returns an array of MappableSourceField objects. See Field mapping fundamentals .

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
public async Task<MappableSourceField[]> GetInvariantFieldsAsync(Client.SamplesLibrary.Helper.IHelper helper, int workspaceArtifactId)

{

      MappableSourceField[] result = null;

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  result = await proxy.GetInvariantFieldsAsync(workspaceArtifactId);

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception, "FieldMapping Service GetInvariantFieldsAsync call failed for Workspace ID {0}", workspaceArtifactId);

            }

      }

      return result;

}
```

## Retrieve an external field mapping

From Relativity, you can call the ReadExternalMappingAsync() method to retrieve the external field mapping for a field with a specified Artifact ID. You call this method by passing the following arguments:

- The Artifact ID of the workspace where the field resides.

- The Artifact ID of the field with the mapping that you want to retrieve.

- The string that identifies the field source. This service currently supports only Invariant as the field source.

If a mapping exists, this method returns an ExternalMapping object. Otherwise, it returns null.

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
public async Task<ExternalMapping> ReadExternalMapping(Client.SamplesLibrary.Helper.IHelper helper, int workspaceArtifactId, int fieldArtifactId, string fieldSource)

{

      ExternalMapping result = null;

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  //Specify Invariant for the fieldSource argument. Currently, this services only supports Invariant as a data source.

                  result = await proxy.ReadExternalMappingAsync(workspaceArtifactId, fieldArtifactId, fieldSource);

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception,

                        "FieldMapping ReadExternalMappingAsync failed for Workspace ID {0}, Field Artifact {1}, Field Source {2}",

                              workspaceArtifactId, fieldArtifactId, fieldSource);

            }

      }

      return result;

}
```

## Update an external field mapping

From Relativity, you can call the UpdateExternalMappingAsync() method to modify or insert field mapping data. You call this method by passing the following arguments:

- The Artifact ID of the workspace containing the mapped fields that you want to update.

- An External Mapping object.

You must set the following properties on an External Mapping object to make a successful UpdateExternalMappingAsync() method call:

- ExternalFieldName - the name of the field in the external data source. Set this property to null if you want to remove the field mapping.

- ExternalFieldSource - the name of the external data source associated with the mapping. Currently, this fields should always be set to "Invariant".

- FieldArtifactId - the Artifact ID of the Relativity field being mapped.

In addition, you should also set specific fields that are used for validation. If you don't set these fields correctly, the field mapping may not update. The following list includes fields used for validation:

- CurrentLength - For fixed-length catalog fields, you must set this property to a minimum field length required for validation. For example, if the CurrentLength property is set to 0 when you attempt to map a fixed-length catalog field, the validation fails.

- FieldTypeId - The service validates the property against the data type that Invariant uses for the field source. For example, you may want to map a source field that Invariant identifies as a Date type. If you set the FieldTypeId property to 0 indicating a fixed-length text field, then the validation fails and the field isn't mapped. The values for this property correspond to the kCura.Relativity.Client.FieldType enumeration.

- ObjectType - You must set this property to 10.

- UseUnicodeEncoding - For text fields, you must set this property to true.

The UpdateExternalMappingAsync() method returns a boolean value that indicates whether the update was successful.

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
public async Task UpdateExternalMapping(Client.SamplesLibrary.Helper.IHelper helper, int workspaceArtifactId, ExternalMapping model)

{

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  await proxy.UpdateExternalMappingAsync(workspaceArtifactId, model);

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = kCura.Relativity.Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception,

                        "FieldMapping UpdateExternalMappingAsync failed for Workspace ID {0}, Mapping: ",

                              workspaceArtifactId, model.ToString());

            }

      }

}
```

## Retrieve GUIDs for automapped fields

You can use the GetAutomappedFieldGuidsAsync() method to retrieve certain processing system fields that Invariant automatically maps during a publish operation. When you call this method, pass the Artifact ID of the workspace where you want to map fields. It returns a list of GUIDs for the corresponding ExternalMapping objects.

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
public async Task<Guid[]> GetAutomappedFieldGuids(Client.SamplesLibrary.Helper.IHelper helper, int workspaceArtifactId)

{

      Guid[] mappedGuids = null;

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  mappedGuids = await proxy.GetAutomappedFieldGuidsAsync(workspaceArtifactId);

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception,

                        "FieldMapping GetAutomappedFieldGuidsAsync failed for Workspace ID {0}", workspaceArtifactId);

            }

      }

      return mappedGuids;

}
```

## Clear cached data

The ClearCachedDataAsync() method removes all cached data from Relativity, Invariant, and the Field Catalog. You can use this method for testing purposes, and for clearing cached data that may be corrupt.

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
public async Task<bool> ClearCachedFieldMappingData(Client.SamplesLibrary.Helper.IHelper helper)

{

      bool success = false;

      using (IFieldMapping proxy = helper.GetServicesManager().CreateProxy<IFieldMapping>(ExecutionIdentity.User))

      {

            try

            {

                  await proxy.ClearCachedDataAsync();

                  success = true;

            }

            catch (ServiceException exception)

            {

                  ISampleLogger _logger = Client.SamplesLibrary.Logging.Log.Logger.ForContext<FieldMappingManager>();

                  _logger.LogError(exception,

                        "FieldMapping ClearCachedDataAsync failed.");

            }

      }

      return success;

}
```
