---
title: "Object Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Manager/Object_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:10+00:00
sha256: f9ee14033b9781252149b31a475c9b2225d752149652b371e956c71577e6c6d2
---

Object Manager (.NET)

# Object Manager (.NET)

Relativity applications contain system objects and Relativity Dynamic Objects (RDOs). System objects are predefined and included in applications default by default. RDOs are custom objects that you can define for your specific business needs through the UI or programmatically. For information about using objects through the UI, see Relativity Objects .

The Object Manager API provides you with the ability to programmatically work with RDOs and Document objects. It exposes methods for performing the following tasks:

- Create RDOs and set values on their associated fields.

- Update fields on Document objects or RDOs.

- Read fields on Document objects or RDOs.

- Retrieve a list of dependent objects prior to deleting a specific object.

- Perform mass operations to create, update, and delete Document objects or RDOs.

- Query for Workspaces, Documents, RDOs and system types.

- Export objects.

Sample use cases for the Object Manager service include:

- Modifying and saving coding decisions or changes to attorney's notes.

- Searching for object data, which you display in the Relativity UI or use for other purposes in your applications. For example, use this service to populate data that appears in the list views.

You can also use the Object Manager service through REST. However, the REST endpoints do not support cancellation tokens or progress indicators. For more information, see Object Manager (REST) .

## Fundamentals for the Object Manager service

Review the following information to learn about the methods, classes, and exceptions used by the Object Manager service.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

Methods

The Object Manager API includes the following methods available on the IObjectManager interface in the Relativity.ObjectManager.<VersionNumber>.Interfaces namespace:

- CreateAsync() method - creates one or more RDOs with the values set for the existing fields. To create a single RDO, pass a CreateRequest object to the method, which then returns a CreateResult object. To mass create RDOs, pass a MassCreateRequest object to the method, which then returns a MassCreateResult object. See Create an RDO and its specified fields or Mass create RDOs .

- DeleteAsync() method - deletes one or more Documents and their associated files, and RDOs. To delete a single Document object or RDO, pass a DeleteRequest object to the method, which then returns an DeleteResult object. To mass delete, pass a MassDeleteByCriteriaRequest or a MassDeleteByObjectIdentifiersRequest object to determine how the operation is performed, such as by querying for objects to delete or by deleting them based on Artifact IDs or GUIDs. A mass delete operation returns a MassDeleteResult object. See Delete a Document object or RDO or Mass delete Document objects or RDOs .

- GetDependencyListAsync() method - retrieves a list of dependent objects based on a request object containing references to objects selected for deletion. This method takes a DependencyListByObjectIdentifiersRequest object and returns a list of Dependency objects. See Retrieve a list of object dependencies .

- InitializeExportAsync() method - sets up an export job and retrieves a runID used in the RetrieveNextResultsBlockFromExportAsync() and StreamLongTextAsync() methods. This method is called during the first step of the export workflow. It returns an ExportInitializationResults object, which provides information about data that is ready for export. See Set up an export job .

- QueryAsync() method - searches for Workspaces, Documents, RDOs, and system types. This overloaded method also supports functionality for requesting the cancellation of a query, and monitoring progress updates. It returns a QueryResultSet object. See Query for Relativity objects .

- QuerySlimAsync() method - searches for Workspaces, Documents, RDOs, and system types, but returns a smaller payload. It also supports functionality for requesting the cancellation of a query, and monitoring progress updates. It returns a QueryResultSlim object. See Query for Relativity objects .

- ReadAsync() method - retrieves the field values on a Document object or RDO. This overloaded method provides functionality for retrieving a specific subset of fields on these objects. It returns a ReadResult object. See Retrieve field values for a Document object or RDO .

- RetrieveNextResultsBlockFromExportAsync() method - retrieves successive blocks of document fields when it is called repeatedly. This method is called as the second step in the export workflow. See Retrieve objects .

- RetrieveResultsBlockFromExportAsync () method - retrieves a specific block of document fields when provided the block index ID. Call this method as the second step in the export workflow when you want to retrieve a specific block index rather than the next available block. See Retrieve objects .

- StreamLongTextAsync() method - retrieves the text that exceeds the size limit for the data returned by RetrieveNextResultsBlockFromExportAsync() method. This method is called as the third step of the export workflow. See Stream text .

- UpdateAsync() method - updates specified field values on one or more Document objects or RDOs. To update a single Document object or RDO, pass an UpdateRequestobject to the method, which then returns an UpdateResult object. To mass update, pass a MassUpdateByCriteriaRequest, MassUpdateByObjectIdentifiersRequest, or MassUpdatePerObjectsRequest object to determine how the operation is performed, such as by querying for objects to update or by updating them based on Artifact IDs or GUIDs. A mass update operation returns a MassUpdateResult object. See Update field values on a Document object or RDO or Mass update Document objects or RDOs .

- UpdateLongTextFromStreamAsync() method - updates a single long text field that may exceed the length limits of an HTTP request. This method takes a workspace ID, a UpdateLongTextFromStreamRequest object and a stream object. See Update a long text field using an input stream in .NET .

Classes for general functionality

The Object Manager API uses the following classes for general functionality. They are available in the Relativity.ObjectManager.<VersionNumber>.Models namespace.

- CallingContext class - contains information about the web context from which the event handler is being called, such as the originator of the call, the page mode, and the related layout. It is referenced by a property on OperationOptions, UpdateOptions, and ReadOptions objects, which can be passed to various methods.

You must set the CallingContext property on one of these objects if you have event handlers that depend on a layout. The event handlers will not function properly if this property is not set. If your event handlers do not require context information, they must then implement the ICanExecuteWithLimitedContext interface available in the Event Handlers API.

- Choice class - represents a choice used as a value for single or multiple fields in Relativity. Its properties include the ArtifactID, Guids, and Name.

- ChoiceRef class - represents a key or reference to a Choice object. Its properties include ArtifactID and Guid. Use the ChoiceRef class when you update field values on a Choice object.

- CreateRequest class - represents a request to create an RDO. This class has a FieldValues property used to set the new field-value pairs on a RelativityObject instance. It also has properties for setting the parent object and object type. The CreateAsync() method takes an object of this type.

- CreateResult class - represents the results of create operation for an RDO. This class has the EventHandlerStatuses and Object properties. The EventHandlerStatuses property contains objects, which indicate the status of the event handlers that executed during the create operation. The Object property references the RelatvityObject that was created. The CreateAsync() method returns an object of this type.

- DeleteReport class - contains a collection of DeleteItem instances. The DeleteResult class has a property that returns an object of this type.

- DeleteRequest class - represents the request to delete a RelativityObject instance. This class has an Object property that indicates the object to delete. The DeleteAsync() method takes an object of this type.

- DeleteResult class - represents the results of a delete operation on a Document object or RDO. This class has a single property that returns a DeleteReport instance, which contains a list of DeletedItem instances. The DeleteAsync() method returns an object of this type.

- DependencyListByObjectIdentifiersRequest class - represents a request for information about dependent objects based on a list of the RelativityObjectRefs, which are specified in its Object property. The GetDependencyListAsync() method takes an object of this type as an argument.

- EventHandlerStatus class - provides information about the status of an event handler execution. Its properties include a Boolean value indicating whether the execution was successful, and a string with a related message.

- Field class - represents a field used to store document metadata, choices, and other information in Relativity. Its properties include ArtifactID, Name, and Guids used to identify the field. Additionally, the FieldCategory property indicates the specific functionality assigned to a field, the FieldType property indicates whether it is date, single object, or other type, and ViewFieldID property provides an identifier for a view field.

- FieldRef class - represents a key or reference to a Field object. It contains minimal information about a Field object, including the ArtifactID, Guid, and Name properties for a specific field. It is used when assigning values to fields during an update operation, and when executing queries through the Object Manager service.

In addition, you can use this class to access the following specialized fields when performing a query on a Document object or RDO:

- Security field - request this field by specifying a FieldRef object with its Name property set as Security in the Query.Fields list. You can also request it by using an instance of the SecurityFieldRef class in the list. The Security field returns a Security object. It contains a Boolean value indicating whether the requesting user has permission to a specific object and another one indicating whether the security at the item level has been overwritten for the object.

- Edit field - request this field by specifying a FieldRef object with its Name property set to Edit in the Query.Fields list. The field value contains the text Edit when the requesting user has permission to edit a specific object and it is empty when the user does not have permissions.

- FieldRefValuePair - represents a key or reference to a FieldValuePair object. A FieldRefValuePair object is used for passing information to the Object Manager service. It contains the following properties:

- Field property - a property of the type FieldRef. A FieldRef object contains minimal information about an object, such as the ArtifactID, Guids, and Name properties for a specific field.

- Value property - a generic object type. The value type varies by the FieldType.

The following table contains a list of fields and their value types. All primitive types are optional, so null is a valid value for them.

FieldType Expected value type

Fixed-Length Text string

Long Text string

Date DateTime

Whole Number int?

Decimal decimal?

Currency decimal?

Yes/No bool?

Single Choice ChoiceRef

Multiple Choice IEnumerable<ChoiceRef>

User User (The ArtifactID must be set on this object.)

File FileRef

Single Object RelativityObjectRef

Multiple Object IEnumerable<RelativityObjectRef>

- FieldType enumeration - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- FieldUpdateBehavior enumeration - contains the members called Merge and Replace, which indicate how multiple choice and multiple object fields should be updated:

- Merge - adds the values that you pass into the service to the current values for the choice or object field.

- Replace - overwrites the current values for the choice or object field with those that you pass into the service.

- FieldValuePair class - represents the field and the value currently assigned to it. The Object Manager service returns a FieldValuePair object. It is a fully hydrated object that contains the following properties:

- Field property - a property of the type FieldRef. A FieldRef object contains minimal information about an object, such as the ArtifactID, Guids, and Name properties for a specific field.

- Value property - a generic object type. The value type varies by the FieldType.

The following table contains a list of fields and their value types. All primitive types are optional, so null is a valid value for them.

FieldType Expected value type

Fixed-Length Text string

Long Text string

Date DateTime

Whole Number int?

Decimal decimal?

Currency decimal?

Yes/No bool?

Single Choice Choice

Multiple Choice List<Choice>

User UserRef

File FileRef

Single Object RelativityObjectValue

Multiple Object List<RelativityObjectValue>

- LayoutRef class - represents a key or reference to a Layout object. Its properties include ArtifactID and Guid.

- ObjectType class - represents a custom object type added to a workspace.

- ObjectTypeRef class - represents a key or reference to an ObjectType object. Its properties include ArtifactID, ArtifactTypeID, and Guid, and Name. The ArtifactTypeID property is an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- OperationOptions class - contains information about how the operation for a request is being called. It has a property that references a CallingContext instance. The CreateAsync() and ReadAsync() methods take an object of this type.

- QueryRequest class - represents the settings for the search that you want to run. This class includes the QueryHint property, which you can set to optimize the view. For example, you can use the hashjoin setting with the value of true or false, or you can use the waitfor setting with a value, such as waitfor:5. The QueryAsync() and the QuerySlimAsync() methods take an object of this type as a parameter.

- QueryResult class - represents the results of a search for a Workspace, Document, RDO, or a system type. Its properties contain information about the result set, including a list of result items, the total number of Artifacts returned, an indicator about the success of the operation, and others. The QueryAsync() and QuerySlimAsync() methods return an object of this type.

- QueryResultSlim class - represents the results of a search for a Workspace, Document, RDO, or a system type returned by the QuerySlimAsync() method. It has the same properties as the QueryResult class and includes the Fields property. This property is a List of Field objects associated with the query results. Additionally, the Objects property contains a List of RelativityObjectSlim objects.

- ReadOptions class - represents information about how long text fields are handled during read operations. It has the FieldTypesToReturnAsString property, which represents a list of object type values that should be returned as strings; the LongTextBehavior property, which controls the behavior used when a long text field exceeds the configured character limit; and the MaxCharactersForLongTextValues property, which controls the maximum number of characters returned in the query results for long text fields. Additionally, this class has a property that references a CallingContext instance.

- ReadRequest class - represents the request for a read operation on Document objects and RDOs. This class has a Fields property that indicates the fields to retrieve, and an Object property that indicates the RelativityObject instance associated with these fields. The ReadAsync() method takes an object of this type.

- ReadResult class - represents the results of a read operation on Document objects and RDOs. This class has the Message, Object, and ObjectType properties. The Message property is only populated if there is a Pre Load event handler that returns a message. Otherwise, this property is empty. The Object property references the RelativityObject that was read, while the ObjectType indicates whether it was a Document or RDO. The ReadAsync() method returns an object of this type.

- RelativityObject class - represents any Relativity object type, and the fields contained on the object. The Object Manager service uses this object type to communicate the fields that need to be updated or read on Document objects and RDOs. It includes the FieldValues property, which contains a list of fields and their respective values. Additionally, this class defines indexers that return FieldValuePair objects. The indexers consume either the GUID, Artifact ID, or Name of a Field object. They use this information to return the corresponding FieldValuePair object.

You can reference RelativityObject objects and FieldValuePair objects by GUID instead of Artifact ID during update and read operations.

- RelativityObjectRef class - represents a key or reference to a RelativityObject. Its properties include ArtifactID and Guid.

- RelativityObjectSlim class - represents a streamlined RelativityObject. This class has only an ArtifactID property, and a Values property, which contains a list of values returned in a result set. The order of these values corresponds to the fields returned in the results from the QuerySlimAsync() method.

- RelativityObjectValue class - represents the value for a field. An object of this type is returned for single object fields, while a List of these objects is returned for multiple object fields.

- UpdateLongTextFromStreamRequest class - represents a request to update a single long text field that exceeds the length limits of an HTTP request. The UpdateLongTextFromStreamAsync() method takes an object of this type. For more information, see Update a long text field using an input stream in .NET .

- UpdateOptions class - contains information about the web context from which this operation is called. It also contains an UpdateBehavior property, which indicates whether to replace or merge field values. For more information, see Update field values on a multiple object .

- UpdateRequest class - represents the request to update a Document object or RDO. This class has a FieldValue property that indicates the fields to update, and an Object property that indicates the RelativityObject instance associated with these fields. The UpdateAsync() method takes an object of this type.

- UpdateResult class - represents the results of an update to Document objects and RDOs. This class has only the EventHandlerStatuses property, which contains a list of EventHandlerStatus objects. Each object represents the status of an event handler that executed during the update. The UpdateAsync() method returns an object of this type.

- User class - contains the ArtifactID, EmailAddress, and Name properties for a User object. Use this class when you update field values on a User object.

Classes for retrieving dependency lists

The Object Manager API uses the following class for retrieving dependency lists. It is available in the Relativity.ObjectManager.<VersionNumber>.Models namespace.

- Dependency class - represents an object dependent on another object selected for deletion. Its properties indicate the relationship between the objects, the action to be taken on a dependent object and other information. The GetDependencyListAsync() method returns an object of this type.

Classes for mass operations

The Object Manager API uses the following classes for mass operations. They are available in the Relativity.ObjectManager.<VersionNumber>.Models namespace.

- Relativity.ObjectManager.<VersionNumber>.Models namespace - classes used for mass operations

- MassCreateRequest - represents a request to create a multiple RDOs. This class has properties for the parent object type, the object type that you are creating, the fields to set, and the values to use for this purpose. The CreateAsync() method takes an object of this type.

- MassCreateResult - represents the results of a mass create operation. The properties on this class indicate whether the operation was successful, provide an error message, and contain references to the objects that were created. The CreateAsync() method returns an object of this type.

- MassDeleteByCriteriaRequest - represents a request to mass delete all objects that meet a specified set of conditions. The DeleteAsync() method takes an object of this type.

- MassDeleteByObjectIdentifiersRequest - represents a request to mass delete all objects with the specified Artifact IDs or GUIDs. The DeleteAsync() method takes an object of this type.

- MassDeleteResult - represents the results of a mass delete operation. The properties on this class indicate whether the operation was successful, provide an error message, and include the total number of objects updated. The UpdateAsync() method returns an object of this type.

- MassOperationsStateProgress - represents the progress object for mass operations processes. This class has a property used to indicate the percentage of the operation that has completed.

- MassUpdateByCriteriaRequest - represents a request to mass update all objects that meet a specified set of conditions. The UpdateAsync() method takes an object of this type.

- MassUpdateByObjectIdentifiersRequest - represents a request to mass update all objects with the specified Artifact IDs or GUIDs. The UpdateAsync() method takes an object of this type.

- MassUpdateOptions - represents information about how a mass update request is performed by replacing or merging field values.

- MassUpdatePerObjectsRequest - represents a request to perform a mass update operation on a list of objects by modifying each of the specified object fields with a distinct value. The UpdateAsync() method takes an object of this type.

- MassUpdateResult - represents the results of a mass update operation. The properties on this class indicate whether the operation was successful, provide an error message, and reference a report of deleted items. The DeleteAsync() method returns an object of this type.

- ObjectIdentificationCriteria - represents a set of query conditions used to identify a RelativityObjectRef object.

- ObjectRefValuesPair - represents a key or reference to a pair of RelativityObjectRefs objects and their associated field values.

Classes for working with hydrated objects

The Object Manager API uses the following class for working with hydrated objects. They are available in the Relativity.ObjectManager.<VersionNumber>.Extensions namespace.

For example, you can use the ToRef() method on one of these classes to convert a fully hydrated object to a ref class. This ref class can then be used when instantiating a request object. Each of the following classes have a ToRef() method:

- ChoiceExtensions

- ExpandoObjectExtensions

- FieldExtensions

- GuidListExtensions

- LayoutExtensions

- RelativityObjectExtensions

Classes used for export operations

The Object Manager API uses the following class for export operations. It is available in the Relativity.ObjectManager.<VersionNumber>.Models namespace.

- ExportInitializationResults class - represents the results of an initialization operation and provides information about the data ready for export. The InitializeExportAsync() method returns an object of this type. See Set up an export job .

Exceptions

The Object Manager service throws several different exception types as follows:

- Event handler exceptions - the Object Manager service invokes all associated event handlers. If an error occurs and the event handler throws an exception, the service rethrows it as an EventHandlerFailedException. The InnerException property on this exception type contains the Exception instance for the error. The EventHandlerFailedException class is available in the Relativity.ObjectManager.<VersionNumber>.Exceptions namespace.

- Service exceptions - thrown when an error occurs during a service call. For example, a ServiceException is thrown when you do not have access to the object type being queried. It contains the following message: "An error occurred while executing query."

- Validation exceptions - thrown when invalid data is passed to the service. For example, you may have passed a fixed-length text field that is longer than its specified length, attempted to save a choice to the wrong field type, or passed a string value to a whole number field. A ValidationException is also thrown if you do not set the Behavior property on a MultipleChoiceFieldUpdateValue or MultipleObjectFieldUpdateValue when attempting an update operation.

- Unauthorized exceptions - thrown when you do not have edit permissions on an object and then attempt to update it. Additionally, an unauthorized exception is thrown when attempting to read an object that you do not have permissions to view.

## Guidelines for using the Object Manager service

Use the following guidelines when working with the Object Manager service:

### Use tokens with long text fields

Use tokens when you are reading or querying on long text fields, and then later performing an update operation on the returned values. This best practice ensures that a long text field is not inadvertently truncated when performing these operations. You can use the default behavior for other operations, such as displaying data in a grid.

To use tokenized behavior, call the read or query methods as follows:

- Read operations - set the LongTextBehavior property to 1 on the ReadOptions object passed to the ReadAsync() method. See Retrieve field values for a Document object or RDO .

- Query operations - set the LongTextBehavior property to 1 on the QueryRequest object passed to the QueryAsync() or QuerySlimAsync() methods. See Query for Relativity objects .

Avoid using the default behavior for LongTextBehavior property for read or query operations when you want to later perform an update operation on the returned values. The tokenized behavior prevents the characters in long text fields from being truncated.

Additional information about properties on the ReadOptions and QueryRequest classes

The following information is provided about the ReadOptions and QueryRequest classes to further explain the properties for long text fields.

#### ReadOptions class

The ReadOptions class includes the following properties for long text fields:

- LongTextBehavior - indicates whether the default or tokenized behavior is used for long text fields that exceed the maximum number of characters set in the MaxCharactersForLongTextValues property.

The LongTextBehavior enumeration includes the following values:

- 1 - indicates tokenized behavior, which returns a token when the maximum number is exceeded.

- 0 - indicates the default behavior, which truncates characters that exceed the maximum number.

- MaxCharactersForLongTextValues - the maximum number of characters returned from a read operation for long text fields. If you set the MaxCharactersForLongTextValues property on the ReadOptions object, it determines the maximum number of characters by overriding limit set by the MaximumNumberOfCharactersSupportedByLongText instance setting. When a long text field exceeds maximum number of characters allowed, the default behavior truncates the field.

When this property is not set, the value in the MaximumNumberOfCharactersSupportedByLongText instance setting determines the maximum length. The default value for the instance setting is 100,000 characters. For more information, see Instance settings' descriptions on the Relativity Documentation site.

The Object Manager service currently does not support retrieving all the text in a long text field for a read operation when it exceeds the maximum length except through the use of tokens or streaming. For information on the streaming API to retrieve all the data stored in a long text field, see Stream text .

#### QueryRequest class

The QueryRequest class includes the following properties for long text fields:

- LongTextBehavior - indicates whether the default or tokenized behavior is used for long text fields that exceed the maximum number of characters set in the MaxCharactersForLongTextValues property.

The LongTextBehavior enumeration includes the following values:

- 1 - indicates tokenized behavior, which returns a token when the maximum number is exceeded.

- 0 - indicates the default behavior, which truncates characters that exceed the maximum number.

- MaxCharactersForLongTextValues - the maximum number of characters returned in the query results for long text fields up to the maximum of 1000.

If you set the MaxCharactersForLongTextValues property on the QueryRequest object, it determines the maximum number of characters by overriding limit set by the MaximumNumberOfCharactersSupportedByLongText instance setting up to up to the maximum of 1000. When a long text field exceeds maximum number of characters allowed, the default behavior truncates the field.

The Object Manager service currently does not support retrieving all the text in a long text field for a query operation when it exceeds the maximum length except through the use of tokens or streaming. For information on the streaming API to retrieve all the data stored in a long text field, see Stream text .

### IObjectManager instance

You can create an IObjectManager instance through a ServiceFactory instance or the Relativity API Helpers. If you want to access the service from a custom page or event handler, use the Relativity API Helpers. For more information, see Relativity API Helpers .

View sample code Copy

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
//Creates and initializes a ServiceFactory instance.

public void InitializeServiceFactory()

{

    String restServerAddress = "http://localhost/relativity.rest/api";

    Uri keplerUri = new Uri(restServerAddress);

    Relativity.Services.ServiceProxy.ServiceFactorySettings settings = new Relativity.Services.ServiceProxy.ServiceFactorySettings(

       keplerUri, new Relativity.Services.ServiceProxy.UsernamePasswordCredentials("ExampleUsername.com", "ExamplePassword1!"));

    _serviceFactory = new Relativity.Services.ServiceProxy.ServiceFactory(settings);

}

//Creates an IObjectManager instance through the ServiceFactory instance.

public async Task PerformWorkWithObjectManager()

{

    using (IObjectManager objectManager = _serviceFactory.CreateProxy<IObjectManager>())

    {

        // Do work with the objectManager instance.

    }

}

//Creates an IObjectManager instance through the Relativity API Helpers.

public async Task PerformWorkWithConnectionHelperObjectManager()

{

    var serviceManager = ConnectionHelper.Helper().GetServicesManager();

    using (IObjectManager objectManager = serviceManager.CreateProxy<IObjectManager>(Relativity.API.ExecutionIdentity.System))

    {

        // Do work with the objectManager instance.

    }

}
```

### Supported field types

The Object Manager API supports create , read , update , delete , and query operations on the following field types.

View list of field types

- Currency

- Multiple object

- Date

- Single choice

- Decimal

- Single object

- Fixed-length text

- User

- Long text

- Whole number

- Multiple choice

- Yes/No

For file field, the Object Manager API supports read , delete , and query operations. To update file fields, follow the workflow described in the File Field Manager Service .

### Propagation

The Object Manager service updates fields on a Document object, which are enabled for propagation. It also updates the enabled fields on all Document objects related to this initially updated object.

### Event handlers

The Object Manager API supports interacting with event handlers. Review the following guidelines for using the Object Manager API in event handlers. For more information, see Event Handlers .

Event handlers executed per API call

Create Mass create Read Query/QuerySlim/Export Update Mass update Delete Mass delete Dependency report

PreLoad X X X X X X X X

PreSave X X X X X X X

PostSave X X X X X X X

PreDelete X X X X X X X

PreCascadeDelete X X X X X X X

PreMassDelete X X X X X X X

Event handler responses

The TBD

- PreSave and PostSave - When a create or update operation succeeds, you can determine the results of all executed PreSave/PostSave event handlers by examining the EventHanderStatuses property on the CreateResult or UpdateResult objects. The EventHandlerStatus object contains the Message and Success properties provided by the kCura.EventHandler.Response object returned by each event handler after execution. Any unhandled exceptions within the event handler execution causes the entire operation to fail. The create and update operations return an HTTP 500 status code.

- PreLoad - When a read operation succeeds, the ReadResult object contains a single Message property. This property consists of a concatenated Message properties returned from every PreLoad EventHandler that fired.

- PreCascadeDelete, PreDelete, and PreMassDelete - While the delete endpoints fire these event handlers, they only provide success or failure responses.

The Object Manager service rethrows an event handler exception as EventHandlerFailedException. For more information, see Object Manager (.NET) .

ICanExecuteWithLimitedContext interface for event handlers

By default, PreLoad , PreSave , and PostSave event handlers only trigger if the appropriate Create, Read, or Update operation is provided with a CallingContext. If a developer wants their EventHandler to fire when no CallingContext information is provided, they can implement the ICanExecuteWithLimitedContext interface on their EventHandler class. This signals to the Object Manager service that the EventHandlers are safe to run regardless of whether a context is provided.

When an EventHandler that has implemented ICanExecuteWithLimitedContext is invoked without CallingContext , the following context-related properties on the EventHandler class are impacted:

- ActiveLayout is set to NULL

- PageMode is set to Unknown

- Application.ApplicationUrl is set to an empty string.

For more information about event handlers, see Develop object type event handlers .

### Indexers on the RelativityObject class

You can access FieldValuePair objects returned from a read or query operation by using the indexers on the RelativityObject class. The indexers consume either the GUID, Artifact ID, or Name of a Field object. They then use the specified identifier for a Field to return the corresponding FieldValuePair object.

The following sample code illustrates how to use an indexer to access a FieldValuePair object returned in the results from a read operation.

View sample code Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.FieldValuePair> ReadField(IHelper helper, int workspaceId, int objectArtifactID, string fieldName)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var readRequest = new ReadRequest

            {

                Object = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID },

                Fields = new List<Relativity.ObjectManager.{versionNumber}.Models.FieldRef> { new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { Name = fieldName } }

            };

            Relativity.ObjectManager.{versionNumber}.Models.ReadResult result = await objectManager.ReadAsync(workspaceId, readRequest);

            return result.Object[fieldName];

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object or Fields are not valid for reading.");

        }

    }

    return null;

}
```

## Create an RDO and its specified fields

Use the CreateAsync() method to create an RDO with the values set for the existing fields on it. You call this method by passing the following parameters:

- The Artifact ID of the workspace where you want to create the RDO.

- A CreateRequest object with the following properties set:

- FieldValues - a list of field-value pairs that you want to set on the new RDO.

- ObjectType - the Artifact Type ID of the ObjectType for the RDO that you want to create. For example, the Artifact Type ID for a Document object is 10.

- ParentObject - the Artifact ID of the parent object of the for the new RelativityObject.

If you do not specify a parent object, Relativity defaults to the System object as the parent.

- An OperationOptions instance that references a CallingContext instance. The CallingContext instance provides information about the web context from which the event handler is being called, such as the originator of the call, the page mode, and the related layout.

You must set the CallingContext property on OperationOptions object if you have event handlers that depend on a layout. The event handlers will not function properly when this property is not set. If your event handlers do not require context information, they must then implement the ICanExecuteWithLimitedContext interface available in the Event Handlers API.

The following code sample illustrates the information that you need to provide to create an RDO, and to set a group of specified fields.

View sample code Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.CreateResult> Create(IHelper helper, int workspaceID, int objectTypeID, IEnumerable<Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair> fieldValuePairs)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var createRequest = new Relativity.ObjectManager.{versionNumber}.Models.CreateRequest();

            createRequest.ObjectType = new Relativity.ObjectManager.{versionNumber}.Models.ObjectTypeRef { ArtifactTypeID = objectTypeID }; //this sets the object type of the RDO you are creating

            createRequest.ParentObject = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = SampleWorkspaceRootFolderID }; //the parent of the artifact only needs to be specified if the parent is not system

            createRequest.FieldValues = fieldValuePairs;

            var callingContext = new Relativity.ObjectManager.{versionNumber}.Models.CallingContext //this sets up a calling context to provide any additional information eventhandlers may need

            {

                Layout = new Relativity.ObjectManager.{versionNumber}.Models.LayoutRef { ArtifactID = SampleLayoutID },

                PageMode = Relativity.ObjectManager.{versionNumber}.Models.PageMode.Edit

            };

            var createOptions = new Relativity.ObjectManager.{versionNumber}.Models.OperationOptions

            {

                CallingContext = callingContext

            };

            return await objectManager.CreateAsync(workspaceID, createRequest, createOptions);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object could not be created.");

        }

    }

    return null;

}
```

## Mass create RDOs

You can mass create multiple RDOs of the same type, and you can specify the values set on the fields that they contain.

If you specify an identifier that is already in the database, an exception will not be thrown. Instead, the Success property on the MassCreateResult object is set to false. Always check the value of the Success property on the results object as a best practice.

To mass create RDOs, pass a MassCreateRequest object as an argument to the CreateAsync() method. This object contains properties for the parent object type, the object type that you are creating, the fields to set, and the values to use for this purpose.

If you do not specify a parent object, Relativity defaults to the System object as the parent.

The overloaded CreateAsync() method supports progress reporting, and cancellation requests for mass update operations. See the following code sample.

View sample code Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.MassCreateResult> MassCreate(IHelper helper, int workspaceID, int objectTypeID, IReadOnlyList<Relativity.ObjectManager.{versionNumber}.Models.FieldRef> fields, IReadOnlyList<IReadOnlyList<object>> fieldValues)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var massCreateRequest = new Relativity.ObjectManager.{versionNumber}.Models.MassCreateRequest();

            // Sets the object type of the RDO that you you want to create.

            massCreateRequest.ObjectType = new Relativity.ObjectManager.{versionNumber}.Models.ObjectTypeRef { ArtifactTypeID = objectTypeID };

            // Sets the fields to populate.

            massCreateRequest.Fields = fields;

            // Sets the values in the order that the fields provided.

            massCreateRequest.ValueLists = fieldValues;

            return await objectManager.CreateAsync(workspaceID, massCreateRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object could not be created.");

        }

    }

    return null;

}
```

## Retrieve field values for a Document object or RDO

Use the ReadAsync() method to retrieve the field values on a Document object or RDO. The method returns fields that you can add to a layout in your custom application.

You call this method by passing the required combination of the following parameters:

- The Artifact ID of the workspace containing the Document object or RDO that you want to read.

- ReadRequest object - contains information about the fields to retrieve, and the RelativityObject instance associated with these fields.

- An optional ReadOptions or OperationOptions object that has a CallingContext and other properties. You can use the ReadOptions class to specify the calling context, the behavior and number of characters for long text fields, and other settings.

The following list highlights key properties on the ReadOptions class, and suggested setting for them:

- CallingContext - The CallingContext object provides information about the web context from which the event handler is being called, such as the originator of the call, the page mode, and the related layout.

You must set the CallingContext property on ReadOptions or OperationOptions object if you have event handlers that depend on a layout. The event handlers will not function properly when this property is not set. If your event handlers do not require context information, they must then implement the ICanExecuteWithLimitedContext interface available in the Event Handlers API.

- FieldTypesToReturnAsString - a list of object type values which should be returned as strings.

- LongTextBehavior - indicates whether the default or tokenized behavior is used for long text fields that exceed the maximum number of characters set in the MaxCharactersForLongTextValues property. To avoid inadvertently truncating of long text fields, we recommend setting this property to 1 for tokenized behavior when you are reading or querying on long text fields, and then later performing an update operation on the returned values. You can use the default behavior for other operations, such as displaying data in a grid. Before implementing the read operation on a long text field, review the following best practices in Use tokens with long text fields .

The following code sample illustrates how to read a specified subset of fields.

View sample code Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.ReadResult> ReadPartial(IHelper helper, int workspaceID, int objectArtifactID, IEnumerable<Relativity.ObjectManager.{versionNumber}.Models.FieldRef> fieldRefs)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var readRequest = new Relativity.ObjectManager.{versionNumber}.Models.ReadRequest

            {

                Object = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID },

                Fields = fieldRefs

            };

            return await objectManager.ReadAsync(workspaceID, readRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object or Fields are not valid for reading.");

        }

    }

    return null;

}
```

## Update field values on a Document object or RDO

Use the UpdateAsync() method to modify a field on a Document object or RDO. You call this method by passing the following parameters:

- The Artifact ID of the workspace containing the Document object or RDO that you want to update.

- An UpdateRequest object containing information about the fields to update, and the RelativityObject instance associated with these fields.

- An optional UpdateOptions object that has CallingContext and UpdateBehavior properties. The CallingContext property provides information about the web context from which the event handler is being called, such as the originator of the call, the page mode, and the related layout. The UpdateBehavior property indicates whether to merge or replace values when updating multiple choice and multiple object fields.

You must set the CallingContext property on UpdateOptions object if you have event handlers that depend on a layout. The event handlers will not function properly when this property is not set. If your event handlers do not require context information, they must then implement the ICanExecuteWithLimitedContext interface available in the Event Handlers API.

### Update field values on a single object

The following code samples illustrates how to update field values on a single Document object or RDO. The process for updating other field types is like that used for updating a single object:

- Create a new RelativityObject instance and set the ArtifactID property.

- Create a new FieldValuePair instance and set the Field and Value properties on it.

- On the UpdateRequest object, set the Object property to the RelativityObject instance, and the FieldValues property to a list of FieldRefValuePair objects.

- Call the UpdateAsync() method by passing the required parameters.

If you need to update a long text field that exceeds the length limits of an HTTP request, use the UpdateLongTextFromStreamAsync() method. For more information, see Update field values on a multiple object .

View sample for updating fields on a single object Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.UpdateResult> UpdateSingleSingleObject(IHelper helper, int workspaceID, int objectArtifactID, int fieldArtifactID, int singleObjectArtifactID)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var relativityObject = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID };

            var fieldValuePair = new Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair

            {

                Field = new Relativity.ObjectManager.{versionNumber}.Models.FieldRef() { ArtifactID = fieldArtifactID },

                Value = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = singleObjectArtifactID }

            };

            var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.UpdateRequest

            {

                Object = relativityObject,

                FieldValues = new List<Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair> { fieldValuePair }

            };

            return await objectManager.UpdateAsync(workspaceID, updateRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

### Update field values on a multiple object

To updates field values on a multiple object or choice, you follow many of the same steps as those for updating a single object. You can also optionally specify the update behavior on the UpdateOptions object, which is passed to the UpdateAync() method. The FieldUpdateBehavior enumeration is used to specify this behavior. It includes the following options:

- Merge - adds the values that you pass into the service to the current values for the choice or object field.

- Replace - overwrites the current values for the choice or object field with those that you pass into the service.

This behavior is now set for the entire update operation. If you do not pass a UpdateOptions instance to this method, the service replaces the values by default.

The update operation for field values on a multiple object works the same way on a multiple choice field.

View sample for multiple object fields

The following code sample illustrates how to call the UpdateSync()method without passing an UpdateOptions instance to it. Since this code does not specify the update behavior, the field values are replaced by default.

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.UpdateResult> UpdateSingleMultipleObject(IHelper helper, int workspaceID, int objectArtifactID, int fieldArtifactID, IEnumerable<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef> objects)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var relativityObject = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID };

            var fieldValuePair = new Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair

            {

                Field = new Relativity.ObjectManager.{versionNumber}.Models.FieldRef() { ArtifactID = fieldArtifactID },

                Value = objects

            };

            var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.UpdateRequest

            {

                Object = relativityObject,

                FieldValues = new List<Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair> { fieldValuePair }

            };

            return await objectManager.UpdateAsync(workspaceID, updateRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

View sample update multiple object fields using UpdateOptions object

The following code sample illustrates how to specify the update behavior by passing an UpdateOptions instance to the UpdateAsync() method. In this sample, the UpdateBehavior property is set to Merge. You also have the option to set this property to Replace.

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.UpdateResult> UpdateSingleMultipleObjectWithOptions(IHelper helper, int workspaceID, int objectArtifactID, int fieldArtifactID, IEnumerable<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef> objects)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var relativityObject = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID };

            var fieldValuePair = new Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair

            {

                Field = new Relativity.ObjectManager.{versionNumber}.Models.FieldRef() { ArtifactID = fieldArtifactID },

                Value = objects

            };

            var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.UpdateRequest

            {

                Object = relativityObject,

                FieldValues = new List<Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair> { fieldValuePair }

            };

            var updateOptions = new Relativity.ObjectManager.{versionNumber}.Models.UpdateOptions

            {

                UpdateBehavior = Relativity.ObjectManager.{versionNumber}.Models.FieldUpdateBehavior.Merge

            };

            return await objectManager.UpdateAsync(workspaceID, updateRequest, updateOptions);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

## Update a long text field using an input stream in .NET

You can use the UpdateLongTextFromStreamAsync() method to update a single long text field that exceeds the length limits of an HTTP request. This method does not trigger an event handler.

You can use the UpdateAsync() method to update a single long text field with a length less than the HTTP request limits. For more information, see Update field values on a single object .

The following code sample illustrates how to instantiate the UpdateLongTextFromStreamRequest object and required stream objects. It then shows how to pass the workspace ID and these objects to the UpdateLongTextFromStreamAsync() method.

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.UpdateResult> UpdateLongTextFromStream(IHelper helper, int workspaceID, int objectArtifactID, string valueToSet)

{

    Guid kGuidForExtractedTextField = new Guid("58D35076-1B1D-43B4-BFF4-D6C089DE51B2");

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        var relativityObject = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef

        {

            ArtifactID = objectArtifactID

        };

        var extractedTextFieldRef = new Relativity.ObjectManager.{versionNumber}.Models.FieldRef

        {

            Guid = kGuidForExtractedTextField

        };

        var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.UpdateLongTextFromStreamRequest

        {

            Object = relativityObject,

            Field = extractedTextFieldRef

        };

        try

        {

            using (var memoryStream = new System.IO.MemoryStream())

            {

                using (var streamWriter = new System.IO.StreamWriter(memoryStream, new System.Text.UnicodeEncoding()))

                {

                    streamWriter.Write(valueToSet);

                    streamWriter.Flush();

                    memoryStream.Seek(0, System.IO.SeekOrigin.Begin);

                    using (var keplerStream = new Relativity.Kepler.Transport.KeplerStream(memoryStream))

                    {

                        await objectManager.UpdateLongTextFromStreamAsync(workspaceID, updateRequest, keplerStream).ConfigureAwait(false);

                    }

                }

            }

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

## Mass update Document objects or RDOs

Use the overloaded UpdateAsync() method to mass update RDOs. You can mass update Document objects or RDOs in the following ways:

- To set the same value on specific fields for a group of objects, perform one of these tasks:

- Use a query to identify the objects that you want to update. Only the objects that match the query conditions are updated. You can set this information in a MassUpdateByCriteriaRequest object and then pass it as one of the arguments to the UpdateAsync() method. In the Relativity UI, this update operation is equivalent to the user selecting the All option in the mass operations bar on a list page.

- Provide a list of identifiers for objects that you want to update. Use the Artifact IDs or GUIDs of these objects as identifiers. You can set this information in a MassUpdateByObjectIdentifiersRequest object and then pass it as one of the arguments to the UpdateAsync() method. In the Relativity UI, this update operation is equivalent to the user selecting the Checked or These option in the mass operations bar on a list page. See Mass update operation using identifiers .

- To set different values for specific fields on a group of objects, provide a list of fields for updating. Additionally, provide list of Artifact IDs for objects to be updated, and the respective field values. The values must be in the same order as the fields that you want to update. You can set this information in a MassUpdatePerObjectsRequest object and then pass it as one of the arguments to the UpdateAsync() method. See Mass update operation using objects .

Similar to updating a single object, the overloaded UpdateAsync() method supports progress reporting, and cancellation requests for mass update operations.

Review the following best practices for mass update operations:

- Make sure all the objects in a mass update operation are the same type.

- Use Artifact IDs instead of GUIDs for better performance. In addition, mass update by criteria is the fastest option for updating many objects. See Mass update operation using query conditions .

- Note that the identifier field cannot be updated by any mass update operation.

### Mass update operation using query conditions

The following code sample illustrates how to set the ObjectIdentificationCriteria property on the MassUpdateByCriteriaRequest object to mass update objects based on search conditions.

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
23
24
25
public async Task<Relativity.ObjectManager.{versionNumber}.Models.MassUpdateResult> MassUpdate(IHelper helper, int workspaceID, Relativity.ObjectManager.{versionNumber}.Models.ObjectIdentificationCriteria criteria, IEnumerable<Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair> fieldRefValuePairs, Relativity.ObjectManager.{versionNumber}.Models.FieldUpdateBehavior behavior)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.MassUpdateByCriteriaRequest();

            // Run a query for all the items that you want to update.

            updateRequest.ObjectIdentificationCriteria = criteria;

            // Indicate the fields and the values to be set for all the objects provided.

            updateRequest.FieldValues = fieldRefValuePairs;

            var updateOptions = new Relativity.ObjectManager.{versionNumber}.Models.MassUpdateOptions();

            // By default, the behavior is replace.

            updateOptions.UpdateBehavior = behavior;

            return await objectManager.UpdateAsync(workspaceID, updateRequest, updateOptions);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

### Mass update operation using identifiers

The following code sample illustrates how to set theMassUpdateByObjectIdentifiersRequest object to mass update Document objects or RDOs based on a list of RelativityObjectRef instances. The RelativityObjectRef class has properties for the Artifact ID and GUID that you can use to reference an object.

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
23
24
25
public async Task<Relativity.ObjectManager.{versionNumber}.Models.MassUpdateResult> MassUpdate(IHelper helper, int workspaceID, IReadOnlyList<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef> relativityObjectRefs, IEnumerable<Relativity.ObjectManager.{versionNumber}.Models.FieldRefValuePair> fieldRefValuePairs, Relativity.ObjectManager.{versionNumber}.Models.FieldUpdateBehavior behavior)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.MassUpdateByObjectIdentifiersRequest();

            // Represents RelativityObjects to update.

            updateRequest.Objects = relativityObjectRefs;

            // Indicates the fields and the values to be set for all the objects provided.

            updateRequest.FieldValues = fieldRefValuePairs;

            var updateOptions = new Relativity.ObjectManager.{versionNumber}.Models.MassUpdateOptions();

            // By default, the behavior is replace.

            updateOptions.UpdateBehavior = behavior;

            return await objectManager.UpdateAsync(workspaceID, updateRequest, updateOptions);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

### Mass update operation using objects

The following code sample illustrates how to set the Fields and ObjectValues properties on a MassUpdatePerObjectsRequest object. This object is used to mass update Document objects or RDOs by setting different values for specific fields on a group of objects. The fields variable references the list of fields for updating, and the objectRefValuesPairs variable is a combination of the RelativityObjects to be updated and the values used for this purpose. The values must be provided in the same order as the fields that they are used to update.

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
23
24
25
26
public async Task<Relativity.ObjectManager.{versionNumber}.Models.MassUpdateResult> MassUpdate(IHelper helper, int workspaceID, IReadOnlyList<Relativity.ObjectManager.{versionNumber}.Models.FieldRef> fields, IReadOnlyList<Relativity.ObjectManager.{versionNumber}.Models.ObjectRefValuesPair> objectRefValuesPairs, Relativity.ObjectManager.{versionNumber}.Models.FieldUpdateBehavior behavior)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var updateRequest = new Relativity.ObjectManager.{versionNumber}.Models.MassUpdatePerObjectsRequest();

            // The fields updated on each of the objects in the list.

            updateRequest.Fields = fields;

            // The RelativityObjects and the values to be set for all the fields provided.

            updateRequest.ObjectValues = objectRefValuesPairs;

            var updateOptions = new Relativity.ObjectManager.{versionNumber}.Models.MassUpdateOptions();

            // The default behavior is replace.

            updateOptions.UpdateBehavior = behavior;

            return await objectManager.UpdateAsync(workspaceID, updateRequest, updateOptions);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object is not valid for updating.");

        }

    }

    return null;

}
```

## Retrieve a list of object dependencies

The GetDependencyListAsync() method retrieves information about Relativity objects dependent on one or more specific objects selected for deletion. It returns a list of Dependency objects, which contain information such as the relationship between the objects and whether a dependent object would be deleted or unlinked. For more information on the dependency report available through the Relativity UI, see Deleting object dependencies .

Sample use cases for this method include:

- Determining whether the delete operation may be blocked by the dependencies on an object selected for deletion.

- Determining how other objects in Relativity may be affected by deleting a one or more objects.

Use these guidelines for calling the GetDependencyListAsync() method:

- Call the method with objects of the same type. If you call the method with objects of different types, it returns an error.

- Call the method only with objects that the user has permission to view. It returns an error if the user does not have view permissions or if any of the objects do not exist.

View code sample

The following code sample illustrates how to instantiate a DependencyListByObjectIdentifiersRequest object and set its Object property to a list of RelativityObjectRef instances. It then calls the GetDependencyListAsync() method by passing it the Artifact ID of the workspace, and the request object.

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
public async Task<List<Relativity.Shared.{versionNumber}.Models.Dependency>> GetDependencyList(IHelper helper, int workspaceID, int objectArtifactID)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var dependencyRequest = new Relativity.ObjectManager.{versionNumber}.Models.DependencyListByObjectIdentifiersRequest();

            dependencyRequest.Objects = new List<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef>

            {

                new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID }

            };

            return await objectManager.GetDependencyListAsync(workspaceID, dependencyRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "Dependencies for the Relativity Object could not be retrieved.");

        }

        return null;

    }

}
```

## Delete a Document object or RDO

Use the DeleteAsync() method to remove Document objects and all their associated files, and RDOs from Relativity. You call this method by passing the following parameters:

- The Artifact ID of the workspace containing the Document object or RDO that you want to delete.

- A DeleteRequest object containing the Artifact ID or GUID of the RelativityObject instance that you want to delete.

If you use the overloaded DeleteAsync() method, you can also pass the following arguments:

- CancellationToken - used to request the cancellation of a delete operation. This object has the type System.Threading.CancellationTokenSource provided by the .NET framework.

- IProgress<DeleteProcessStateProgress>object - used to define a provider for progress updates.

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

public async Task<Relativity.ObjectManager.{versionNumber}.Models.DeleteResult> Delete(IHelper helper, int workspaceID, int objectArtifactID)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var deleteRequest = new Relativity.ObjectManager.{versionNumber}.Models.DeleteRequest();

            deleteRequest.Object = new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = objectArtifactID };

            return await objectManager.DeleteAsync(workspaceID, deleteRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object could not be deleted.");

        }

        return null;

    }

}
```

## Mass delete Document objects or RDOs

You can use the overloaded DeleteAsync() method to mass delete Document objects or RDOs. All the objects in a mass delete operation must be the same type. Additionally, you can mass delete these objects in the following ways:

- Use a query to identify objects that you want to delete. Only the items that match the query conditions are deleted. You can set this information in a MassDeleteByCriteriaRequest object and then pass it as one of the arguments to the DeleteAsync() method. See Mass delete operation using query conditions .

- Provide a list of identifiers for objects that you want to delete. Use the Artifact IDs or GUIDs of these objects as identifiers. You can set this information in an MassDeleteByObjectIdentifiersRequest object and then pass it as one of the arguments to the DeleteAsync() method. See Mass delete operation using identifiers .

The overloaded DeleteAsync() method supports progress reporting, and cancellation requests for mass delete operations.

### Mass delete operation using query conditions

The following code sample illustrates how to set the ObjectIdentificationCriteria property on the MassDeleteByCriteriaRequest object to mass delete objects based on search conditions.

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.MassDeleteResult> MassDelete(IHelper helper, int workspaceID, Relativity.ObjectManager.{versionNumber}.Models.ObjectIdentificationCriteria criteria)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var deleteRequest = new Relativity.ObjectManager.{versionNumber}.Models.MassDeleteByCriteriaRequest();

            // Run a query for all the items that you want to delete.

            deleteRequest.ObjectIdentificationCriteria = criteria;

            return await objectManager.DeleteAsync(workspaceID, deleteRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object could not be deleted.");

        }

        return null;

    }

}
```

### Mass delete operation using identifiers

The following code sample illustrates how to set the Objects property on the MassDeleteByObjectIdentifiersRequest object to mass delete Document objects or RDOs based on a list of RelativityObjectRef instances. The RelativityObjectRef class has properties for the Artifact ID and GUID that you can use to reference an object.

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.MassDeleteResult> MassDelete(IHelper helper, int workspaceID, IReadOnlyList<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef> relativityObjectRefs)

{

    using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

    {

        try

        {

            var deleteRequest = new Relativity.ObjectManager.{versionNumber}.Models.MassDeleteByObjectIdentifiersRequest();

            // Represents a list of RelativityObjects to be deleted.

            deleteRequest.Objects = relativityObjectRefs;

            return await objectManager.DeleteAsync(workspaceID, deleteRequest);

        }

        catch (ValidationException exception)

        {

            _logger.LogError(exception, "The Relativity Object could not be deleted.");

        }

        return null;

    }

}
```

## Query for Relativity objects

With the Object Manager service, you can query for Workspaces, Documents, RDOs, and system types. This service includes the QueryAsync() method, which returns detailed information about the field-value pairs returned by the query. The QuerySlimAsync() method returns a smaller payload, which saves bandwidth. This method is useful for mobile devices and for displaying tabular data.

View parameter descriptions for query methods

Call the QueryAsync() or QuerySlimAsync() method the by passing the following parameters:

- The ArtifactID of the workspace that you want to query.

- A QueryRequest object represents the settings for the search that you want to run. This following list highlights key properties on this QueryRequest class:

- QueryHint - used to optimize the view. For example, you can use the hashjoin setting with the value of true or false, or you can use the waitfor setting with a value, such as waitfor:5.

- Condition - determines the search criteria.

To search for data, you can use a variety of query options, including conditions, fields, sorts, and relational fields. These query options have a specific syntax for defining the for defining query conditions. For information about query conditions and options, see Query for resources .

- LongTextBehavior - indicates whether the default or tokenized behavior is used for long text fields that exceed the maximum number of characters set in the MaxCharactersForLongTextValues property. To avoid inadvertently truncating of long text fields, we recommend setting this property to 1 for tokenized behavior when you are reading or querying on long text fields, and then later performing an update operation on the returned values. You can use the default behavior for other operations, such as displaying data in a grid. Before implementing the query operation on a long text field, review the following best practices in Use tokens with long text fields .

- Sorts - a list of Sort objects. This list determines the sort order of the results. The Sort class has a Direction property, which can be set to ascending or descending. It also has an Order property, which specifies precedence when multiple sort orders are defined.

- Fields - a collection of fields used like a SELECT statement in an SQL query. For a query request, you can identify fields by name, Artifact ID, or GUID.

- Example :

Copy

```text
1
2
3
4
Fields = new List<FieldRef>()

{

   new FieldRef{ Name = "*"}

}
```

- Start - the one-based index of the first artifact in the result set.

- Length - the number of items to return in the query result, starting with index in the start parameter. If you pass in a Length value that is less than or equal to 0, the parameter is set to the PDVDefaultQueryCacheSize instance setting (set to 10,000 by default) for performance reasons. If you need to retrieve a larger result set but do not know the upper bounds of the result set, you can pass in a large integer size as the value for the Length parameter, but be aware that this approach can have significant negative performance impacts, especially when using a very large integer like int.MaxValue . A better approach is to use the InitializeExportAsync, RetrieveNextResultBlockAsync/RetrieveNextBlockAsync, and StreamLongTextAsync sequence of operations to retrieve large result sets.

If you use one of the overloaded methods, you can also pass the following arguments:

- IProgress<ProgressReport> object - used to define a provider for progress updates. This object has the type System.IProgress provided by the .NET framework.

- CancellationToken - used to request the cancellation of a query executed by the Object Manager service. This object has the type System.Threading.CancellationTokenSource provided by the .NET framework.

The following code samples illustrate how to run a query for Document objects using the Object Manager service. They illustrate how to define the query, call the QueryAsync() method, and return a QueryResult object containing the search results.

View code sample for QueryAsync() method Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.QueryResult> QueryAsync(IHelper helper, int workspaceID)

{

    try

    {

        //Prepare parameters for query call

        const int documentArtifactTypeID = 10; //target artifact type to query (Document is always 10)

        const int indexOfFirstDocumentInResult = 1; //1-based index of first document in query results to retrieve

        const int lengthOfResults = 100; //max number of results to return in this query call.

        var sort = new Relativity.ObjectManager.{versionNumber}.Models.Sort()

        {

            Direction = Relativity.ObjectManager.{versionNumber}.Models.SortEnum.Ascending,

            FieldIdentifier = new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = this.SampleField_FixedLengthText_ID }

        };

        var queryRequest = new Relativity.ObjectManager.{versionNumber}.Models.QueryRequest()

        {

            ObjectType = new Relativity.ObjectManager.{versionNumber}.Models.ObjectTypeRef { ArtifactTypeID = documentArtifactTypeID },

            Condition = "('Email From' IN ['Test0@Test.com','Test1@Test.com'])", //query condition syntax is used to build query condtion.  See Relativity's developer documentation for more details

            Fields = new List<Relativity.ObjectManager.{versionNumber}.Models.FieldRef>() //array of fields to return.  ArtifactId will always be returned.

            {

                new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = SampleField_FixedLengthText_ID },

                new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = SampleChoice_ID },

                new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = SampleField_MultiObject_ID }

            },

            IncludeIDWindow = false,

            RelationalField = null, //name of relational field to expand query results to related objects

            SampleParameters = null,

            SearchProviderCondition = null, //see documentation on building search providers

            Sorts = new List<Relativity.ObjectManager.{versionNumber}.Models.Sort> { sort }, //an array of Fields with sorting order

            QueryHint = "waitfor:5"

        };

        using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.CurrentUser))

        {

            return await objectManager.QueryAsync(workspaceID, queryRequest, indexOfFirstDocumentInResult, lengthOfResults);

        }

    }

    catch (Exception ex)

    {

        _logger.LogError(ex, "Error: ObjectManager.QueryAsync was not successful");

    }

    return null;

}
```

View code sample for QuerySlimAsync() method Copy

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
public async Task<Relativity.ObjectManager.{versionNumber}.Models.QueryResultSlim> QuerySlimAsync(IHelper helper, int workspaceID)

{

    try

    {

        //Prepare parameters for query call

        const int documentArtifactTypeId = 10; //target artifact type to query (Document is always 10)

        const int indexOfFirstDocumentInResult = 1; //1-based index of first document in query results to retrieve

        const int lengthOfResults = 100; //max number of results to return in this query call.

        var sort = new Relativity.ObjectManager.{versionNumber}.Models.Sort()

        {

            Direction = Relativity.ObjectManager.{versionNumber}.Models.SortEnum.Ascending,

            FieldIdentifier = new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = this.SampleField_FixedLengthText_ID }

        };

        var queryRequest = new Relativity.ObjectManager.{versionNumber}.Models.QueryRequest()

        {

            ObjectType = new Relativity.ObjectManager.{versionNumber}.Models.ObjectTypeRef { ArtifactTypeID = documentArtifactTypeId },

            Condition = "('Email From' IN ['Test0@Test.com','Test1@Test.com'])", //query condition syntax is used to build query condtion.  See Relativity's developer documentation for more details

            Fields = new List<Relativity.ObjectManager.{versionNumber}.Models.FieldRef>()  //array of fields to return.  ArtifactId will always be returned.

            {

                new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = SampleField_FixedLengthText_ID },

                new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = SampleChoice_ID },

                new Relativity.ObjectManager.{versionNumber}.Models.FieldRef { ArtifactID = SampleField_MultiObject_ID }

            },

            IncludeIDWindow = false,

            RelationalField = null, //name of relational field to expand query results to related objects

            SampleParameters = null,

            SearchProviderCondition = null, //see documentation on building search providers

            Sorts = new List<Relativity.ObjectManager.{versionNumber}.Models.Sort> { sort }, //an array of Fields with sorting order

            QueryHint = "waitfor:5"

        };

        using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

        {

            return await objectManager.QuerySlimAsync(workspaceID, queryRequest, indexOfFirstDocumentInResult, lengthOfResults);

        }

    }

    catch (Exception ex)

    {

        _logger.LogError(ex, "Error: ObjectManager.QueryAsync was not successful");

    }

    return null;

}
```

## Export API

The Object Manager API supports exporting document fields, including complete long text fields such as extracted text, via a set of endpoints collectively called the Export API. This export functionality differs in the following ways from the standard document access performed by the Object Manager API:

- During the initialization method, the complete document list to be returned is generated from the query provided. This allows the API to guarantee that each document’s data is only returned once.

- The complete text of long text fields is available.

- Methods to access the data and long text may be safely called concurrently by different threads or processes, allowing for high throughput.

See the following subsections for more information:

- Export API workflow

- Set up an export job

- Retrieve objects

- Stream text

- Export API code sample

- Export API Helper library

### Export API workflow

The export process is multiple step workflow that uses several methods on the IObjectManager interface:

- Set up an export job - use the InitializeExportAsync() method to set up the export job. It also retrieves a runID used in the RetrieveNextResultsBlockFromExportAsync() and RetrieveResultsBlockFromExportAsync() methods.

- Retrieve objects - use the RetrieveNextResultsBlockFromExportAsync() method to retrieve successive blocks of document fields or use the RetrieveResultsBlockFromExportAsync() method to retrieve a specific block of document fields from an in-progress export job.

- Stream text - use the StreamLongTextAsync() method to retrieve the text that exceeds the size limit for the data returned by RetrieveNextResultsBlockFromExportAsync() and RetrieveResultsBlockFromExportAsync() methods. Call this method repeatedly, and optionally, in parallel with the RetrieveNextResultsBlockFromExportAsync(), RetrieveResultsBlockFromExportAsync(), and other StreamLongTextAsync() method calls.

For an example of this workflow, see Export API code sample .

### Set up an export job

Use the InitializeExportAsync() method to set up the export of documents from a workspace based on a query. You call this method by passing the following parameters:

- workspaceID - the Artifact ID of the workspace containing the data to export.

-

queryRequest - the query that defines the data set to export, including ObjectType and Fields, query condition, and an optional maximum text length to export inline. For more information, see Query for Relativity objects .

You can use the MaxCharactersForLongTextValues field of the queryRequest object to override the number limit set by the MaximumLongTextSizeForExportInCell instance setting. For more information, see Instance settings' descriptions on the Relativity Documentation site.

The semantics of MaxCharactersForLongTextValues field is slightly different than other Object Manager API uses:

- It sets the size limit to text that is retrieved inline as part of the results of RetrieveNextResultsBlockFromExportAsync() and RetrieveResultsBlockFromExportAsync() methods.

- It does not truncate the text that exceeds the size limit. If the long text is less than the size limit, it is added to the field. If it exceeds the size limit, a short marker is added to the field. This marker indicates that the full long text should be retrieved through StreamLongTextAsync() method. For more information, see Stream text .

- start - the zero-based index of a record indicating where to begin the export operation.

This method returns an instance of ExportInitializationResults class, which contains the following:

- A GUID runId used with the RetrieveNextResultsBlockFromExportAsync() method.

After an export job is initialized, the export RunID only valid for seven days. The export job then expires and is no longer available for retrieving blocks of documents.

- A count of type long, which indicates the number of documents to be exported.

- A List of FieldMetadata information about the requested fields, including the field type. This information simplifies identifying LongText fields that require special processing.

For the complete code, see Export API code sample .

Copy

```text
1
2
3

ExportInitializationResults exportInitializationResults =

    objectManager.InitializeExportAsync(workspaceId, queryRequest, 0).Result;
```

### Retrieve objects

Call one of the following methods to retrieve document fields from the export job:

- RetrieveNextResultsBlockFromExportAsync() method - retrieves successive blocks of document fields from an in-progress export job. See Retrieve the next block of records .

- RetrieveResultsBlockFromExportAsync() method - retrieves a specific block index of document fields from an in-progress export job. It provides the option to specify a block size and starting point. For example, you may want to use the RetrieveResultsBlockFromExportAsync() method to break up the export job into smaller blocks, which simplifies retrying a job for that specific block of records. See Retrieve a specific block of records .

Review the following considerations for these methods:

- They retrieve long text fields up to the size limit specified during initialization. Long text fields larger than the size set by MaxCharactersForLongTextValues property on the QueryRequest object contain the text value #KCURA99DF2F0FEB88420388879F1282A55760# . This value indicates that the text in the long text field should be retrieved using the StreamLongTextAsync() method.

- They return null when all the records are retrieved, and the export job is complete.

- They can be called in multiple threads simultaneously, or from multiple processes. It returns sequential, non-overlapping, non-repeating blocks of documents. Use this type of parallelism to achieve high throughput.

#### Retrieve the next block of records

Use the RetrieveNextResultsBlockFromExportAsync() method to get the next block of records from an in-progress export job. You call this method by passing the following parameters:

- workspaceID - the Artifact ID of the workspace containing the data to export.

- runID - the in-progress export ID.

- batchSize - the maximum number of results to return in one call.

The returned RelativityObjectSlim array contains the data for multiple documents, up to and including batchSize. The fields for each document appear in the order defined in the QueryRequest object during initialization.

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
23
24
25
// Get blocks of documents until none are left.

RelativityObjectSlim[] currentBlock = null;

bool done = false;

while (!done)

{

    try

    {

        currentBlock = objectManager.RetrieveNextResultsBlockFromExportAsync(workspaceId, runId, blockSize).Result;

    }

    catch (Exception exception)

    {

        Console.WriteLine(exception.Message);

        return;

    }

    if (currentBlock == null || !currentBlock.Any())

    {

        done = true;

        break;

    }

    Console.WriteLine("Got block of " + currentBlock.Count() + " documents");

    Console.WriteLine();
```

#### Retrieve a specific block of records

Use the RetrieveResultsBlockFromExportAsync() method to get a specific block of records from an in-progress export job. You call this method by passing the following parameters:

- workspaceID - the Artifact ID of the workspace containing the data to export.

- runID - the in-progress export ID.

- resultsBlockSize - the maximum number of results to return in one call.

The actual number of results returned may be less than the maximum number requested.

- exportIndexID - the export block index ID of the batch.

The returned RelativityObjectSlim array contains the data for multiple documents, up to and including the resultsBlockSize, or it may include less the maximum number requested. The fields for each document appear in the order defined in the QueryRequest object during export initialization.

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
ExportInitializationResults exportInitResults = await objectManager.InitializeExportAsync(workspaceArtifactID, queryRequest, 0).ConfigureAwait(false);

Guid exportID = exportInitResults.RunID;

int totalNumberOfRecords = exportInitResults.RecordCount;

int exportIndexID = 0;

int resultsBlockSize = totalNumberOfRecords;

RelativityObjectSlim[] currentBlock = await objectManager.RetrieveResultsBlockFromExportAsync(workspaceArtifactID, exportID, resultsBlockSize, exportIndexID).ConfigureAwait(false);

exportIndexID += currentBlock.Length;

resultsBlockSize -= currentBlock.Length;

return currentBlock;
```

### Stream text

Use the StreamLongTextAsync() method to retrieve a stream of text for long text fields marked as exceeding the size limit for the data returned by the RetrieveNextResultsBlockFromExportAsync() or the RetrieveResultsBlockFromExportAsync() method. For more information, see Retrieve objects .

You call the StreamLongTextAsync() method by passing the following parameters:

- workspaceID - the Artifact ID of the workspace containing the object to be retrieved.

- exportObject - a RelativityObjectRef of the document that contains the text to be streamed.

- longTextField - a FieldRef of the long text field that contains the text to be streamed.

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
23
24
25
26
27
// Check to determine if the long text field needs to be streamed.

if (longTextIds.Contains(i))

{

    if (ros.Values[i].Equals(_SHIBBOLETH))

    {

        Console.WriteLine("Text is too long, it must be streamed");

        Console.WriteLine();

        RelativityObjectRef documentObjectRef = new RelativityObjectRef { ArtifactID = ros.ArtifactID };

        using (IKeplerStream keplerStream = objectManager.StreamLongTextAsync(workspaceId, documentObjectRef, queryRequest.Fields.ElementAt(i)).Result)

        {

            using (Stream realStream = keplerStream.GetStreamAsync().Result)

            {

                StreamReader reader = new StreamReader(realStream, Encoding.Unicode);

                String line;

                while ((line = reader.ReadLine()) != null)

                {

                    Console.Write(line);

                }

                Console.WriteLine();

            }

        }

    }

}
```

The resulting stream is encoded using UTF-16 and begins with a Unicode Byte Order Mark. We recommend that you look for the UTF-8 Byte Order Mark (0xEF,0xBB,0xBF), when one of the two UTF-16 Byte Order Marks (0xFF 0xFE or 0xFE 0xFF) is not found because that encoding may be used in the future.

### Export API code sample

The Export API code sample illustrates how to export the extracted text fields on Document objects.

View code sample

When running this code sample, make sure to include the required using statements. For example, the call to call Array.Any() requires a using System.Linq statement.

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
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
using Relativity.Kepler.Transport;

using Relativity.ObjectManager.{versionNumber}.Interfaces;

using Relativity.ObjectManager.{versionNumber}.Models;

using Relativity.Services.ServiceProxy;

using System;

using System.Collections.Generic;

using System.IO;

using System.Linq;

using System.Net;

using System.Text;

namespace Relativity.Sample

{

    class Program

    {

        // Provide an indicator that the text is not present and needs to be streamed.

        private const string _SHIBBOLETH = "#KCURA99DF2F0FEB88420388879F1282A55760#";

        // Set the URL for the Relativity instance.

        private static Uri relativityUrl = new Uri("https://relativity.mycompany.com");

        // Set the ID of the Workspace.

        private static int workspaceID = 1234567;

        // Provide an Object Manager query.

        private static QueryRequest queryRequest = new QueryRequest()

        {

            Fields = new FieldRef[]

            {

                new FieldRef {Name = "Control Number"},

                new FieldRef {Name = "Extracted Text"}

            },

            MaxCharactersForLongTextValues = 1024 * 10,

            ObjectType = new ObjectTypeRef { ArtifactTypeID = 10 } // Document

        };

        // Count of the number of documents to return per call to RetrieveNextResultsBlock() method.

        private static int blockSize = 1000;

        // Provide credentials. Production environments should use a secure credential type.

        private static Credentials credentials = new UsernamePasswordCredentials("me@mycompany.com", "Password goes here");

        static void Main(string[] args)

        {

            try

            {

                // Get an instance of the Object Manager.

                IObjectManager objectManager;

                try

                {

                    objectManager = GetKeplerServiceFactory(relativityUrl, credentials).CreateProxy<IObjectManager>();

                }

                catch (Exception exception)

                {

                    Console.WriteLine(exception.Message);

                    return;

                }

                // Initialize Export API using the properties set above.

                Guid runID;

                long recordCount;

                List<FieldMetadata> fieldData;

                int[] longTextIds;

                try

                {

                    ExportInitializationResults exportInitializationResults =

                        objectManager.InitializeExportAsync(workspaceID, queryRequest, 0).Result;

                    // Save infomation about this "run".

                    runID = exportInitializationResults.RunID;

                    recordCount = exportInitializationResults.RecordCount;

                    fieldData = exportInitializationResults.FieldData;

                    // Find indexes of all long text fields.

                    List<int> longTextIdList = new List<int>();

                    for (int i = 0; i < exportInitializationResults.FieldData.Count; i++)

                    {

                        if (exportInitializationResults.FieldData[i].FieldType == FieldType.LongText)

                        {

                            longTextIdList.Add(i);

                        }

                    }

                    longTextIds = longTextIdList.ToArray();

                }

                catch (Exception exception)

                {

                    Console.WriteLine(exception.Message);

                    return;

                }

                Console.WriteLine("RunId " + runID + " will return " + recordCount + " documents");

                Console.WriteLine();

                // Get blocks of documents until none are left.

                RelativityObjectSlim[] currentBlock = null;

                bool done = false;

                while (!done)

                {

                    try

                    {

                        currentBlock = objectManager.RetrieveNextResultsBlockFromExportAsync(workspaceID, runID, blockSize).Result;

                    }

                    catch (Exception exception)

                    {

                        Console.WriteLine(exception.Message);

                        return;

                    }

                    if (currentBlock == null || !currentBlock.Any())

                    {

                        done = true;

                        break;

                    }

                    Console.WriteLine("Got block of " + currentBlock.Count() + " documents");

                    Console.WriteLine();

                    // Print out the fields for each document.

                    foreach (RelativityObjectSlim ros in currentBlock)

                    {

                        for (int i = 0; i < fieldData.Count; i++)

                        {

                            Console.WriteLine(fieldData[i].Name + ": " + ros.Values[i]);

                            // Check to determine if the long text field needs to be streamed.

                            if (longTextIds.Contains(i))

                            {

                                if (ros.Values[i].Equals(_SHIBBOLETH))

                                {

                                    Console.WriteLine("Text is too long, it must be streamed");

                                    Console.WriteLine();

                                    RelativityObjectRef documentObjectRef = new RelativityObjectRef { ArtifactID = ros.ArtifactID };

                                    using (IKeplerStream keplerStream = objectManager.StreamLongTextAsync(workspaceID, documentObjectRef, queryRequest.Fields.ElementAt(i)).Result)

                                    {

                                        using (Stream realStream = keplerStream.GetStreamAsync().Result)

                                        {

                                            StreamReader reader = new StreamReader(realStream, Encoding.Unicode);

                                            String line;

                                            while ((line = reader.ReadLine()) != null)

                                            {

                                                Console.Write(line);

                                            }

                                            Console.WriteLine();

                                        }

                                    }

                                }

                            }

                        }

                        Console.WriteLine();

                    }

                    Console.WriteLine("Block complete");

                    Console.WriteLine();

                }

                Console.WriteLine("All blocks complete");

                Console.WriteLine();

            }

            catch (Exception exception)

            {

                Console.WriteLine(exception.Message);

                return;

            }

        }

        private static ServiceFactory GetKeplerServiceFactory(Uri relativityUrl, Credentials credentials)

        {

            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;

            ServicePointManager.DefaultConnectionLimit = 128;

            Uri restUri = new Uri(relativityUrl, "Relativity.REST/api");

            Uri servicesUri = new Uri(relativityUrl, "Relativity.REST/api/Relativity.ObjectManager");

            ServiceFactorySettings settings = new ServiceFactorySettings(servicesUri, restUri, credentials);

            ServiceFactory factory = new ServiceFactory(settings);

            return factory;

        }

    }

}
```

### Export API Helper library

You can use the Export API in multiple threads to achieve high throughput. To simplify this process, a helper library is available. It also functions as an example illustrating how to run your own concurrent implementation. For more information, see relativitydev/export-api-helper on GitHub.
