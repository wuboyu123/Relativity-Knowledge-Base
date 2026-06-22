---
title: "this Binding"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/this_Binding.htm
collection: developer
fetched_at: 2026-06-22T06:32:02+00:00
sha256: a3cacaf531080504b14d538c009085057ee6b1f89f1cf1b5131a7e25328cc4b2
---

this Binding Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# this Binding

### Methods

The following table lists the methods for this binding.

Method

Return value

Description

clearErrorSummary()

undefined

Clears all errors from the errorContainer object.

clearModelData() undefined Clears backingModelData and volatileModelData. This function clears any stored in-process revision that the user has made to the form. This update isn't reflected in the UI.

handleApplicationError(error: Object)

undefined

Acts as a handler for irrecoverable errors. It deactivates any open ExitDialog instance, writes the error using the logger, and redirects to the error page for an application.

setErrorSummary(messages: Array<String>, expand: Boolean)

undefined

Updates the errorContainer object with error metadata.

handlePermissionDeniedError undefined Acts as a handler for permission denied errors. It deactivates any open ExitDialog instance and redirects to the permission denied error page for an application. It is useful for handling custom authorization rules in event handlers.

refreshLayout()

undefined

Refreshes page layout executing needed event handlers.

The function is running a subset of the logic of Load Pipeline.

List of event handlers that are run during refresh layout:

- REPLACE_READ or REPLACE_GET_NEW_OBJECT_INSTANCE

- TRANSFORM_LAYOUT

- REPLACE_FILE_ACTIONS

- OVERRIDE_PICKER_DATASOURCE

- HYDRATE_LAYOUT

- REPLACE_OBTAIN_ADDITIONAL_DATA

- POST_OBTAIN_ADDITIONAL_DATA

- HYDRATE_LAYOUT_COMPLETE

- PAGE_LOAD_COMPLETE

To refresh the contents of a Relativity Forms page, Relativity recommends using the refreshLayout() method on the this Binding instead of performing a hard reload (i.e. window.location.reload()).

### Properties

The following table lists the properties for this binding.

Property

Type

Description

artifactId

number

The artifact identifier of the view-model. Available for View and Edit modes only.

artifactTypeId

number

The artifact type identifier of the view-model.

associatedArtifactId

number

When objectB is being created, and immediately associated to objectA, (particularly when launched from a "New" button in a child or associative item list on objectA's Layout) the asociatedArtifactId is the ArtifactID of the existing objectA.

backingModelData

object

A copy of the view-model data fetched from the server. It is populated with client-validated values from the volatileModelData object before it is sent to the server during a save operation.

connectorFieldArtifactId

number

When objectB is being created, and immediately associated to objectA, (particularly when launched from a "New" button in a child or associative item list on objectA's Layout) the connectorFieldArtifactId is the ArtifactID of the Field on the objectB Layout which should point to (be pre-populated with) the existing objectA.

exitDialog

object

An injected instance of the ExitDialog class that appears when a user leaves a form. It is activated only in Edit and Add modes.

fieldNameToFieldIdMap

map

Contains mappings of field names to field ids. Used by the LayoutApi. This is not defined until the hydrateLayoutComplete stage.

fieldGuidToFieldIdMap map Contains mappings of field guids to field ids. Used by the fieldHelper API. This is not defined until the hydrateLayoutComplete stage.

getFieldIdForField(identifier: Number|String|Object) number Gets the field id for the field that matches the given identifier. Used by the fieldHelper API. For more information about the identifier parameter, see the identifier parameter documentation.

formViewModelTypeId

number

An ID fetched from the routeConfig settings representing the FORM_VIEW_MODEL_TYPE of the view-model. Possible values include VIEW (0), ADD (1), and EDIT (2). For more information, see constants.FORM_VIEW_MODEL_TYPE in convenienceAPI .

isNew

boolean

A boolean that determines if the current view-model is an Add view-model depending on viewModelName.

lastVisitedArtifactId

number

A routing parameter used for redirection when Edit or Add operations are canceled or when a user clicks the Save and New button.

layoutId

number

A layout identifier for the view-model. A user manually adds this value to the URL. It is not revised through the code.

parentArtifactId

number

The parent artifact identifier of the view-model. Available for Add mode only.

runtimeConfig

RuntimeConfig

An injected instance of the RuntimeConfig class. The config is read only and is used to view Relativity specific properties.

viewModelName

string

A string representing the name of the view-model populated in the activate() method. It is derived from the name property of the routeConfig for the view-model. The name originates from VIEW_MODEL_NAME. For more information, see constants.VIEW_MODEL_NAME in convenienceAPI .

volatileModelData

object

A copy of the backingModelData that houses the in-process user revisions to the field components of a view-model. It is used to repopulate the backingModelData on create and update calls for the view-model.

workspaceId

number

The workspace identifier of the view-model. Available in all Edit, View, and Add modes.

On this page

- this Binding

-

- Methods

- Properties


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
