---
title: "Layout Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/Layout_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:36+00:00
sha256: f3659516fb3641b79afab0a73ff630887f8c652f1a6609f1e0090bb5b4e0ee53
---

Layout Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Layout Manager (.NET)

In Relativity, a layout is a web-based coding form that you can use to view and edit document and other fields. For general information, see Layouts on the Relativity Documentation site.

The Layout Manager API exposes CRUD operations that you can use to programmatically manipulate layouts in your Relativity environment. In addition to the CRUD operations, this API includes a helper function used to retrieve a list of users with permissions necessary to own layouts.

Sample use cases for the Layout Manager API include:

- Developing an application that supports specific operations, which users can perform on the layouts included in it.

- Programmatically updating properties of layouts in Relativity.

You can also use the Layout Manager API through REST. For more information, see Layout Manager (REST) .

## Fundamentals for the Layout Manager API

The Layout Manager API contains the following methods.

Methods

The Layout Manager API exposes the following methods on the ILayoutManager interface in the Relativity.Services.Interfaces.DataVisualization.<VersionNumber>.Layout namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - creates a new layout. It takes a LayoutRequest object and returns a LayoutResponse object that represents the newly created layout. See Create a layout .

- DeleteAsync() method - removes a layout from Relativity. It takes an Artifact ID for a layout. It doesn't return a value. See Delete a layout .

- GetEligibleOwnersAsync() method - returns a list of users who have permissions required to be layout owners. See Retrieve users for layout ownership .

- ReadAsync() method - retrieves metadata for the requested layout. It takes the Artifact ID for a layout and returns a LayoutResponse object. See Read a layout .

- UpdateAsync() method - modifies a layout based on the properties set on the LayoutRequest object. It takes this LayoutRequest object and the Artifact ID for a layout to make the required updates. It returns a LayoutResponse object. See Update a layout .

## Create a layout

Use the CreateAsync() method to create a single layout. This method takes two arguments:

- A workspace ID

- A layoutRequest object specifying the properties of the layout to create

It returns a LayoutResponse object that represents the newly created layout.

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
public async Task CreateLayoutAsync(IHelper helper, int workspaceID) {

        using(ILayoutManager layoutManagerProxy = helper.GetServicesManager().CreateProxy < ILayoutManager > (ExecutionIdentity.User)) {

                try {

                    var layoutRequest = new LayoutRequest();

                    layoutRequest.Name = "New Layout";

                    layoutRequest.ObjectType = new Relativity.Services.Interfaces.Shared.Securable < ObjectTypeIdentifier > () {

                        Secured = false,

                            Value = new ObjectTypeIdentifier() {

                                Name = "Document"

                            }

                    };

                    layoutRequest.Order = "3";

                    layoutRequest.OverwriteProtection = false;

                    layoutRequest.Keywords = "Sample Keywords Go Here...";

                    layoutRequest.Notes = "Sample Notes Go Here...";

                    LayoutResponse layoutResponse = await layoutManagerProxy.CreateAsync(workspaceId, layoutRequest);

                    Console.WriteLine($ "Created Layout with Artifact ID {layoutResponse.ArtifactID}.");

                } catch (Exception ex) {

                    Console.WriteLine($ "A Layout could not be created. An error occurred: {ex.Message}");

                }
```

## Read a layout

Use the ReadAsync() method to retrieve metadata for a layout. This method takes two arguments:

- A workspace ID

- A layout ID

It returns a LayoutResponse object that represents a layout.

You can use the overloaded ReadAsync() method to retrieve additional metadata and actions by passing the includeMetadata and includeActions arguments:

Copy

```text
1
return await layoutManagerProxy.ReadAsync(workspaceID, layoutID, includeMetadata, includeActions);
```

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
public async Task<LayoutResponse> ReadLayoutAsync(IHelper helper, int workspaceID, int layoutID, bool includeMetadata, bool includeActions)

{

    using (ILayoutManager layoutManagerProxy = helper.GetServicesManager().CreateProxy<ILayoutManager>(ExecutionIdentity.User))

    {

        try

        {

            return await layoutManagerProxy.ReadAsync(workspaceID, layoutID, includeMetadata, includeActions);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("A Layout could not be read. An error occurred: {0}", ex.Message));

        }

    }

    return null;

}
```

## Update a layout

Use the UpdateAsync() method to modify the properties of a layout. This method takes three arguments:

- A workspace ID

- A layout ID

- A LayoutRequest object that contains properties for the modified layout.

It returns a LayoutResponse object that represents the modified layout.

You can use the overloaded UpdateAsync() method to restrict the update of a layout to the date when it was last modified. Pass the lastModifiedOn property as an argument to the method.

Copy

```text
1
await layoutManagerProxy.UpdateAsync(workspaceID, layoutID, layoutRequest, lastModifiedOn);
```

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
public async Task UpdateLayoutAsync(IHelper helper, int workspaceID, int layoutID, string newName)

{

    using (ILayoutManager layoutManagerProxy = helper.GetServicesManager().CreateProxy<ILayoutManager>(ExecutionIdentity.User))

    {

        try

        {

            LayoutResponse layoutResponse = await layoutManagerProxy.ReadAsync(workspaceID, layoutID);

            var layoutRequest = new LayoutRequest(layoutResponse);

            layoutRequest.Name = newName;

            await layoutManagerProxy.UpdateAsync(workspaceID, layoutID, layoutRequest);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("A Layout could not be updated. An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete a layout

Use the DeleteAsync() method to remove a layout from Relativity. This method takes two arguments:

- A workspace ID

- A layout ID

This method doesn't return a value.

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
public async Task DeleteLayoutAsync(IHelper helper, int workspaceID, int layoutID)

{

    using (ILayoutManager layoutManagerProxy = helper.GetServicesManager().CreateProxy<ILayoutManager>(ExecutionIdentity.User))

    {

        try

        {

            await layoutManagerProxy.DeleteAsync(workspaceID, layoutID);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("A Layout could not be deleted. An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve users for layout ownership

Use the GetEligibleOwnersAsync() method to retrieve a list of users eligible to be layout owners. This method takes only a workspace ID as an argument. It returns a list of DisplayableObjectIdentifier objects that represent eligible users.

When calling the CreateAsync() or the UpdateAsync() method, you can assign each of the returned users to a layout as an owner on the LayoutRequest object.

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
public async Task<List<DisplayableObjectIdentifier>> GetEligibleOwnersAsync(IHelper helper, int workspaceID)

{

    using (ILayoutManager layoutManagerProxy = helper.GetServicesManager().CreateProxy<ILayoutManager>(ExecutionIdentity.User))

    {

        try

        {

            return await layoutManagerProxy.GetEligibleOwnersAsync(workspaceID);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("Eligible Layout owners could not be retrieved. An error occurred: {0}", ex.Message));

        }

    }

    return null;

}
```

On this page

- Layout Manager (.NET)

- Fundamentals for the Layout Manager API

- Create a layout

- Read a layout

- Update a layout

- Delete a layout

- Retrieve users for layout ownership


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
