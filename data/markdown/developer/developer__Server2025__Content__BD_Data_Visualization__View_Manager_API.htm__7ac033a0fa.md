---
title: "View Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/View_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:30+00:00
sha256: 052c1d869f7d971a44dce0121990bb6dbe05b64cefe14148d7f3e4a928e31eb0
---

View Manager (.NET)

# View Manager (.NET)

You can use the View Manager API to create, read, and update Relativity views. It also includes helper methods for retrieving the following information:

- A user's permissions on a view and the fields used in the search conditions on the view.

- A list of workspace users who can be assigned ownership of a view.

- A list of object types in a workspace. When creating a view, you can use this list to assign an object type to a view based on the objects that you want displayed in it.

As a sample use case, you could use the View Manager API to add or modify views used in a custom application or through the Relativity UI. For example, you might want to create a view that uses a specific set of search criteria to display custom objects in an application.

You can also use the View Manager API through REST. For more information, see View Manager (REST) .

## Fundamentals for the View Manager API

The View Manager API contains the following methods and classes.

Methods

The View Manager API exposes the following methods on the IViewManager interface in the Relativity.DataVisualization.<VersionNumber>.View namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new view. This method takes the Artifact ID of the workspace where you want to create the view, and a ViewRequest object, which describes the view to create. It returns the ID of newly created View object. See Create a view in a workspace .

- GetAccessStatusAsync () method - retrieves information about whether a user has View permissions to a view and the fields used in search conditions on the view. This method takes the Artifact ID of the workspace containing the view, and the Artifact ID of the view that you want to check for user access status. It returns ViewAccessStatus object that contains information about the user's ability to access the view. See Retrieve the access status of a user .

- GetEligibleObjectTypesAsync() method - returns list of eligible object types in the workspace as ObjectTypeRef objects. This method takes the Artifact ID of the workspace containing the view. See Retrieve a list of object types in the workspace .

- GetEligibleOwnersAsync() method - returns workspace users who can be assigned ownership of a view. This method takes the Artifact ID of a workspace. It returns a list of DisplayableObjectIdentifier objects, representing users who can be assigned ownership of a view. Users must have View permissions to the view. See Retrieve users for view ownership .

- ReadAsync() method - retrieves the properties for a view. This method takes the Artifact ID of the workspace containing the view and the Artifact ID of the view. It returns a ViewResponse object, which contains information about the view. See Retrieve information about a view .

- UpdateAsync() method - modifies the view properties. This method takes the Artifact ID of the workspace containing the view and a ViewRequest object. It returns a ViewResponse object, which contains information about the updated view. See Update the properties of a view .

Classes

The View Manager API includes the following classes available in the Relativity.Services.DataVisualization.V1.View.Models namespace:

- ViewRequest class - represents the data used to create or update a view.

The following table lists properties on the ViewRequest class:

Name Type Description

ArtifactID int The Artifact ID of the view.

ArtifactTypeID int The Artifact Type ID of the object that the view is assigned to.

Dashboard Securable<DisplayableObjectIdentifier> The dashboard associated with the view.

Fields List<FieldRef> A list of fields included in the view result set.

GroupDefinitionFieldArtifactID int? An identifier indicating the field used for grouping a list. It used only for the Document object type.

IsRelationalFieldView bool Indicates whether the view is used to display relational fields.

IsSystemView bool Indicates whether the view is a system view.

IsVisible bool Indicates whether the view is visible in the system.

Name string The user-friendly name of the view.

Order int The position of the view in the view drop-down list.

Owner Securable<DisplayableObjectIdentifier> The user who owns the view.

QueryHint string A string parameter used to optimize views. Only use the query hint only when instructed by the Relativity Client Services team.

RelativityApplications List<DisplayableObjectIdentifier> A list of Relativity applications associated with the view.

SearchCriteria CriteriaCollection Search criteria specified as a CriteriaCollection object.

Sorts List<Sort> The sort order for view results specified as a collection of Sort objects.

VisibleInDropdown bool Indicates whether the view is visible in the view drop-down list.

- ViewResponse class - represents an existing view.

The following table lists properties on the ViewResponse class:

Name Type Description

Actions List<Action> A list of available actions that can be performed on a view.

CreatedBy Securable<DisplayableObjectIdentifier> The user who created the view.

CreatedOn DateTime? The date and time in UTC when the view was created.

Dashboard Securable<DisplayableObjectIdentifier> The dashboard associated with the view.

Fields SecurableList<FieldRef> A list of fields included in the view result set.

GroupDefinitionFieldArtifactID int? An identifier indicating the field used for grouping a list. It used only for the Document object type.

IsRelationalFieldView bool Indicates whether the view is used to display relational fields.

IsSystemView bool Indicates whether the view is a system view.

IsVisible bool Indicates whether the view is visible in the system.

LastModifiedBy Securable<DisplayableObjectIdentifier> The user who last modified the view.

LastModifiedOn DateTime? The date and time in UTC when the view was last modified.

Meta Meta Meta information representing a list of read-only and unsupported fields.

Name string The user-friendly name of the view.

ObjectIdentifier int The Artifact ID of the view.

ObjectType int The Artifact Type ID of the object that the view is assigned to.

Order int The position of the view in the view drop-down list.

Owner Securable<DisplayableObjectIdentifier> The user who owns the view.

QueryHint string A string parameter used to optimize views. Only use the query hint only when instructed by the Relativity Client Services team.

RelativityApplications SecurableList<DisplayableObjectIdentifier> A list of Relativity applications associated with the view.

SearchCriteria CriteriaCollection Search criteria specified as a CriteriaCollection object.

To search for data, you can use a variety of query options, including conditions, fields, sorts, and relational fields. These query options have a specific syntax for defining the for defining query conditions. For information about query conditions and options, see Query for resources .

Sorts List<Sort> The sort order for view results specified as a collection of Sort objects.

VisibleInDropdown bool Indicates whether the view is visible in the view drop-down list.

## Create a view in a workspace

Use the CreateAsync() method to add a new view to a Relativity workspace. When calling this method, pass the Artifact ID of the workspace where you want to create the view, and a ViewRequest object. This method returns the Artifact ID of the newly created view.

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
public async Task<bool> CreateAsync(IHelper helper)

{

    bool success = false;

    using (IViewManager proxy = helper.GetServicesManager().CreateProxy<IViewManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            ViewRequest viewRequest = new ViewRequest();

            viewRequest.ArtifactTypeID = (int)ArtifactType.Document;

            viewRequest.Name = "My View";

            viewRequest.Owner = new DisplayableObjectIdentifier { Name = "Public", ArtifactID = 0 } viewRequest.Fields.Add(

                  new FieldRef("Control Number"));

            viewRequest.Fields.Add(new FieldRef("File Size"));

            Criteria fileSizeCriteria = new Criteria();

            fileSizeCriteria.Condition = new CriteriaCondition()

            { FieldIdentifier = new FieldRef("File Size"), Operator = CriteriaConditionEnum.GreaterThan, Value = 2000 };

            viewRequest.SearchCriteria.Conditions.Add(fileSizeCriteria);

            Services.DataVisualization.V1.View.Models.Sort fileSizeSort =

                new Services.DataVisualization.V1.View.Models.Sort()

                {

                    FieldIdentifier = new FieldRef("File Size"),

                    Direction = Services.DataVisualization.V1.View.Models.SortEnum.Descending,

                    Order = 1

                };

            viewRequest.Sorts.Add(fileSizeSort);

            viewRequest.Order = 100;

            viewRequest.VisibleInDropdown = true;

            viewRequest.Dashboard = new DisplayableObjectIdentifier { ArtifactID = this.SampleDashboardArtifact_ID };

            int viewId = await proxy.CreateAsync(this.SampleWorkspace_ID, viewRequest);

            if (viewId != 0)

            {

                success = true;

                logger.LogInformation($"CreateAsync succeeded. ArtifactID is {viewId}.");

            }

            else

            {

                logger.LogError("CreateAsync failed");

            }

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

        return success;

    }

}
```

## Retrieve information about a view

Use the ReadAsync() method to retrieve information about a view. When calling this method, pass the Artifact ID of the workspace containing the view, and the Artifact ID of the view. This method returns a ViewResponse object.

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
public async Task<bool> ReadAsync(IHelper helper, int viewToReadArtifactID)

{

    bool success = false;

    using (IViewManager proxy = helper.GetServicesManager().CreateProxy<IViewManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            ViewResponse viewResponse = await proxy.ReadAsync(this.SampleWorkspace_ID, viewToReadArtifactID);

            logger.LogInformation(

                $"ReadAsync succeeded. View ArtifactID is {viewResponse.ObjectIdentifier.ArtifactID}, Name is {viewResponse.ObjectIdentifier.Name}.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

    return success;

}
```

## Update the properties of a view

Use the UpdateAsync() method to modify the properties of a view. When calling this method, pass Artifact ID of the workspace containing the view and a ViewRequest object. It returns a ViewResponse object, which contains information about the updated view.

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
public async Task<bool> UpdateAsync(IHelper helper, int viewToUpdateArtifactID)

{

    bool success = false;

    using (IViewManager proxy = helper.GetServicesManager().CreateProxy<IViewManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            ViewResponse view = await proxy.ReadAsync(this.SampleWorkspace_ID, viewToUpdateArtifactID);

            ViewRequest viewRequest = new ViewRequest(view); //create request based on response

            //update fields in request

            viewRequest.Name = $"{view.Name} - updated";

            viewRequest.Fields.Add(new FieldRef("File Type"));

            Criteria fileTypeCriteria = new Criteria();

            fileTypeCriteria.Condition = new CriteriaCondition()

            { FieldIdentifier = new FieldRef("File Type"), Operator = CriteriaConditionEnum.IsLike, Value = "document" };

            viewRequest.SearchCriteria.Conditions.Add(fileTypeCriteria);

            Services.DataVisualization.V1.View.Models.Sort fileTypeSort =

                new Services.DataVisualization.V1.View.Models.Sort()

                {

                    FieldIdentifier = new FieldRef("File Type"),

                    Direction = Services.SortEnum.Ascending,

                    Order = 200

                };

            viewRequest.Sorts.Add(fileTypeSort);

            ViewResponse updatedView = await proxy.UpdateAsync(this.SampleWorkspace_ID, viewRequest);

            logger.LogInformation($"UpdateAsync succeeded.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

}
```

## Retrieve the access status of a user

Use the GetAccessStatusAsync() method to determine whether a user has View permissions to a view and the fields used in the criteria for search conditions on the view.

When calling this method, pass the Artifact ID of the workspace containing the view, and the Artifact ID of the view that you want to check for user access status.

It returns ViewAccessStatus object that contains information about the user's ability to access the view. This object has the CanView and CanViewCriteriaFields properties on it.

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
public async Task<bool> GetAccessStatusAsync(IHelper helper)

{

    bool success = false;

    using (IViewManager proxy = helper.GetServicesManager().CreateProxy<IViewManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            int? viewToGetAccecStatusToArtifactID;

            if (ViewHelper.TryCreate(proxy, this.SampleWorkspace_ID, "My View to Get Access Status to",

                out viewToGetAccecStatusToArtifactID))

            {

                ViewAccessStatus status =

                    await proxy.GetAccessStatusAsync(this.SampleWorkspace_ID, viewToGetAccecStatusToArtifactID.Value);

                logger.LogInformation(

                    $"GetAccessStatusAsync succeeded. Exists is {status.Exists}, CanView is {status.CanView}, CanViewCriteriaFields is {status.CanViewCriteriaFields}");

                success = true;

            }

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

    return success;

}
```

## Retrieve users for view ownership

Use the GetViewOwnersAsync() method to retrieve a list of users in a workspace. You can then use this list to assign owners to a view. To be designated as an owner, a user must have View permissions for views. For more information, see Security and Permissions on the Relativity Documentation site.

Pass the Artifact ID of a workspace containing the view to this method. It returns a list of DisplayableObjectIdentifier objects, representing users who can be assigned ownership of a view.

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
public async Task<bool> GetViewOwnersAsync(IHelper helper)

{

    bool success = false;

    using (IViewManager proxy = helper.GetServicesManager().CreateProxy<IViewManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            List<DisplayableObjectIdentifier> owners = await proxy.GetEligibleOwnersAsync(this.SampleWorkspace_ID);

            logger.LogInformation($"GetViewOwnersAsync succeeded. Count of possible owners is {owners.Count()}");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

    return success;

}
```

## Retrieve a list of object types in the workspace

Use the GetObjectTypesAsync() method to return a list of object types that the workspace contains. You can select an object type that is then used for populating the ObjectType property on the View object.

Call this method by passing Artifact ID of the workspace containing the view. It returns a list of ObjectTypeRef objects.

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
public async Task<bool> GetObjectTypesAsync(IHelper helper)

{

    bool success = false;

    using (IViewManager proxy = helper.GetServicesManager().CreateProxy<IViewManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            List<DisplayableObjectTypeIdentifier> objectTypes =

                await proxy.GetEligibleObjectTypesAsync(this.SampleWorkspace_ID);

            logger.LogInformation(

                $"GetObjectTypesAsync succeeded. Count of available object types is {objectTypes.Count()}");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

    return success;

}
```
