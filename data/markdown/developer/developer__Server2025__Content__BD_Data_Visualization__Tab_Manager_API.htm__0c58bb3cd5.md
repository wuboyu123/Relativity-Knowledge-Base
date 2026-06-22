---
title: "Tab Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/Tab_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:01+00:00
sha256: f439e5f16f978c808c836e80da45de795939067d80a79927189c9fbdba4c9653
---

Tab Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Tab Manager (.NET)

The Tab Manager API supports programmatically managing tabs in Relativity. It includes the following features:

- Supports create, read, update, and delete operations on tabs.

- Provides helper methods that simplify working with tabs. You can use these methods to retrieve information about the display order of tabs, parent tabs, and available object types that can be associated with tabs. Additionally, you can also retrieve workspace-level metadata for admin and system tabs.

As a sample use case, you might use the Tab Manager service to add specialized tab functionality to custom pages in a Relativity application developed for your organization.

You can also use the Tab Manager API through REST. For more information, see Tab Manager (REST) .

## Fundamentals for managing tabs

Review the following information to learn about the methods, classes, and other entities used by the Tab Manager API.

Methods

The Tab Manager API includes the following methods available on the ITabManager interface in the Relativity.Services.Interfaces.DataVisualization.<VersionNumber>.Tab namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new tab to Relativity. This method takes the Artifact ID of a workspace and a TabRequest object as arguments. It returns a TabResponse object representing the new Tab. See Create a tab .

- DeleteAsync() method - removes a tab from Relativity. This method takes the Artifact IDs of a workspace and a tab as arguments. See Delete a tab .

- GetAllNavigationTabs() method - retrieves a list of all tabs in a specified workspace that the calling user can navigate to. It returns a list of NavigationTabResponse objects. See Retrieve all tabs for navigation .

- GetEligibleObjectTypesAsync() method - retrieves a list of object types that can be associated with a tab when you are creating it. It takes the Artifact ID of a workspace. The method returns a list of all available object types. See Retrieve object types for a tab .

- GetEligibleParentTabsAsync() method - retrieves a list of all available parent tabs in a workspace, which you can associate with a new tab. See Retrieve eligible parent tabs .

- GetMetaAsync() method - retrieves workspace-level metadata about admin and system tabs. This method takes a workspace ID of -1 to indicate the admin-level context for system and admin tabs. See Retrieve workspace-level metadata for admin and system tabs .

- GetViewOrderListAsync() method - retrieves a list of all tabs and the order assigned to them in a specific workspace. The order determines the position of a tab in the Relativity UI. This method returns a list of TabViewOrder objects. See Retrieve tab orders .

- ReadAsync() method - retrieves metadata for a tab, including its name, order, link type, and other properties. You can also use this overloaded method to return extended metadata, including information about the operations that you have permissions to perform on the tab, such as update or delete. This method returns a TabResponse object. See Retrieve tab metadata .

- UpdateAsync()method - modifies the properties of a tab, such as its name, order, and others. You can also use this overloaded method to restrict the update of a tab based on the date that it was last modified. See Update a tab .

Classes and enumerations

The Tab Manager API uses the following classes and enumerations:

- TabRequest class - represents the data used to create or update a tab, including its name, order, visibility, and other properties. The CreateAsync() and UpdateAsync() methods take an object of this type as an argument.

- TabResponse class - represents information about a tab, including its name, order, visibility, and other properties. The ReadAsync(), CreateAsync() and UpdateAsync() methods return an object of this type.

- TabViewOrder class - contains information about the location of the tab in the Relativity UI. Its properties include the tab name, parent tab, order, and others. The Order property is a numerical value indicating the position of the tab relative to other tabs in the UI. The GetViewOrderListAsync() method returns an object of this type. See Retrieve tab orders .

- TabLinkTypeEnum enumeration - indicates type of link associated with the tab. For example, a parent type indicates that the tab can have child tabs, an external type indicates the tab links to a URL, and an object type indicates the tab links to a Relativity object.

- ParentTabResponse class - contains information about a parent tab with a list of possible child link types.

- NavigationTabResponse class - represents navigation information about a tab, including its URL as well as its name, order, visibility, parent, and other properties. The GetAllNavigationTabsAsync() method returns a list of objects of this type.

## Guidelines for using the Tab Manager service

Review the following guidelines for working with the Tab Manager service.

### Access the Tab Manager service

You can access the Tab Manager service by creating a client proxy, and then instantiating a TabManager object.

View code sample Copy

```text
1
2
3
4
5

Uri keplerEndPoint = new Uri("http://localhost/relativity.rest/api");

Services.ServiceProxy.ServiceFactory serviceFactory = new Services.ServiceProxy.ServiceFactory(new Services.ServiceProxy.ServiceFactorySettings(keplerEndpoint,

       new Services.ServiceProxy.UsernamePasswordCredentials("username", "password")));

Relativity.DataVisualization.V1.Tab.ITabManager proxy = serviceFactory.CreateProxy<Relativity.DataVisualization.V1.Tab.ITabManager>();
```

### Admin-level context

The methods on the Tab Manager API require that you pass an integer representing a workspace ID. You must pass -1 when you want to indicate the admin-level context. For example, you would pass -1 as the workspace ID to retrieve metadata for system or admin tabs. See Retrieve workspace-level metadata for admin and system tabs .

### Retrieve a value from a Task object

When you call a method on the Tab Manager API, it returns a Task object. You can retrieve the data returned in Task object by retrieving an awaiter for the Task object, and then calling the GetResult() method.

View code sample Copy

```text
1
2
3
4
5
List<TabViewOrder> tabViewOrder = tabManager.GetViewOrderListAsync(WorkspaceID).GetAwaiter().GetResult();



List<ParentTabResponse> allParentTabs = tabManager.GetEligibleParentTabsAsync(WorkspaceID).GetAwaiter().GetResult();



TabResponse entitiesTabResponse = tabManager.ReadAsync(WorkspaceID, entitiesTabArtifactID).GetAwaiter().GetResult();
```

### Set ParentID property

When creating a tab, you must the set the Parent property. This property is required for tabs at all levels, including tabs created at the admin-level or as parent tabs. For admin-level tabs, set this property to SystemArtifactId.

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
int systemArtifactID = artifactHelper.RetrieveSystemArtifactId();



return new TabRequest()

{

    Name = Constants.ENTITIES_PARENT_TAB_NAME,

    Order = newEntitiesParentTabOrder,

    LinkType = TabLinkTypeEnum.Parent,

    IsVisible = true,

    Parent = new ObjectIdentifier { ArtifactID = systemArtifactID }

};
```

### Use of response data from read operations

You may want to update a tab by using data obtained from a read operation. In the Tab Manager API, the ReadAsync() method returns a TabResponse object. However, the UpdateAsync() method requires that you pass a TabRequest object to it. To use data obtained from a read operation, you need to translate it from the form provided in the TabResponse object to that required for a TabRequest object.

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
TabResponse entitiesTabResponse = tabManager.ReadAsync(WorkspaceID, entitiesTabArtifactID).GetAwaiter().GetResult();



TabRequest entitiesTabRequest = TranslateTabResponseToTabRequest(entitiesTabResponse);



private TabRequest TranslateTabResponseToTabRequest(TabResponse tabResponse)

{

    TabRequest tabRequest = null;



    if (tabResponse != null)

    {

        tabRequest = new TabRequest

        {

            Name = tabResponse.ObjectIdentifier.Name,

            Order = tabResponse.Order,

            Link = tabResponse.Link,

            IsDefault = tabResponse.IsDefault,

            IsVisible = tabResponse.IsVisible,

            IsShownInSidebar = tabResponse.IsShownInSidebar,

            RelativityApplications = tabResponse.RelativityApplications.ViewableItems.Select(x => new ObjectIdentifier { ArtifactID = x.ArtifactID }).ToList(),

            LinkType = tabResponse.LinkType,

            IconIdentifier = tabResponse.IconIdentifier,

            Parent = new ObjectIdentifier { ArtifactID = tabResponse.Parent.Value.ArtifactID },

            ObjectType = tabResponse.ObjectType

        };

    }



    return tabRequest;

}
```

### IconIdentifier property

The TabRequest class contains the IconIdentifier property, which represents a string identifier for the icon displayed when a tab appears in the sidebar.

View table of IconIdentifier values

The following table lists the available values for the IconIdentifier property:

Icon

String Identifier

Name

sidebar-access

Access

sidebar-analytics

Analytics

sidebar-bar-chart

Bar chart

sidebar-case

Case

sidebar-case-dynamics

Case dynamics

sidebar-configure

Configure

sidebar-data-transfer

Data transfer

sidebar-documents

Documents

sidebar-download

Download

sidebar-export

Export

sidebar-folder

Folder

sidebar-infrastructure

Infrastructure

sidebar-monitor

Monitor

sidebar-page

Page

sidebar-pie-chart

Pie chart

sidebar-processing

Processing

sidebar-production

Production

sidebar-resources

Resources

sidebar-review

Review

sidebar-default-tab

Tag

sidebar-upload

Upload

sidebar-workspaces

Workspaces

## Create a tab

To create a tab, call the CreateAsync() method by passing the Artifact ID of the workspace and a TabRequest object to it.

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
public bool Create(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            string tabName = "Sample_Tab";

            TabRequest request = new TabRequest

            {

                Name = tabName,

                Order = 100,

                LinkType = TabLinkTypeEnum.Object,

                IsVisible = true,

                Parent = new ObjectIdentifier { ArtifactID = 1003663 }

            };



            TabResponse response = proxy.CreateAsync(SampleWorkspace_ID, request).GetAwaiter().GetResult();

            _logger.LogDebug("{TabID} - {TabName}", response.ObjectIdentifier.ArtifactID, response.ObjectIdentifier.Name);

        }

        catch (Exception ex)

        {

            _logger.LogError("Create failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Retrieve tab metadata

Use the overloaded ReadAsync() method to retrieve basic or extended metadata for a tab. Extended metadata includes operations that you have permissions to perform on the tab, such as delete or update.

For basic tab metadata, call the ReadAsync() method by passing the Artifact IDs of the workspace and the tab. For extended metadata, you can pass Boolean values for both the includeMetadata and includeActions parameters on the overloaded method.

View code sample for retrieving basic metadata Copy

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
public bool Read(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            TabResponse response = proxy.ReadAsync(SampleWorkspace_ID, SampleTab_ID).GetAwaiter().GetResult();

            _logger.LogDebug("{TabID} - {TabName}", response.ObjectIdentifier.ArtifactID, response.ObjectIdentifier.Name);

            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Read failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Update a tab

To modify the properties of a tab, call the UpdateAsync() method by passing Artifact ID of the workspace and a TabRequest object to it. This overloaded method also supports restricting the update of a tab to the date when it was last modified. To restrict the update, you must pass a DateTime object to the method as well.

The value for the DateTime object must match the LastModifiedOn date for the tab stored in Relativity. Otherwise, you receive an error, indicating that the object has been modified.

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
public bool Update(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            string tabName = "Sample_Tab";

            TabRequest request = new TabRequest

            {

                Name = tabName,

                Order = 100,

                LinkType = TabLinkTypeEnum.Object,

                IsVisible = true,

                Parent = new ObjectIdentifier { ArtifactID = 1003663 },

                ObjectType = new DisplayableObjectTypeIdentifier { ArtifactTypeID = 10 }

            };



            proxy.UpdateAsync(SampleWorkspace_ID, request).GetAwaiter().GetResult();

            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Update failed - {message}", ex.Message);

            throw;

        }



    }



    return success;

}
```

## Delete a tab

Use the DeleteAsync() method to remove a tab from Relativity. You must have the permissions to perform a delete operation. For more information, see Security and permissions in the Relativity Documentation site.

Before you delete a tab, consider checking for other dependent tabs using Object Manager API. See Object Manager (.NET) .

Remove a tab by passing the Artifact IDs of the workspace and the existing tab to the DeleteAsync() method.

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
public bool Delete(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            proxy.DeleteAsync(SampleWorkspace_ID, SampleTab_ID).GetAwaiter().GetResult();

            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Delete failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Retrieve object types for a tab

When creating an object link type tab, you must associate it with an object. Use the GetEligibleObjectTypesAsync() method to obtain a list of available object types before executing a create operation. It retrieves a list of all object types in a workspace available for creating a tab.

Pass the Artifact ID of a workspace to the GetEligibleObjectTypesAsync() method.

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
public bool GetAvailableObjectTypes(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            List<DisplayableObjectTypeIdentifier> response = proxy.GetEligibleObjectTypesAsync(SampleWorkspace_ID).GetAwaiter().GetResult();

            _logger.LogDebug("All available object types for workspace {WorkspaceID}", SampleWorkspace_ID);



            foreach (DisplayableObjectTypeIdentifier identifier in response)

            {

                _logger.LogDebug("{Name} - {ArtifactTypeID} - {ArtifactID}", identifier.Name, identifier.ArtifactTypeID, identifier.ArtifactID);

            }



            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Get all available object types failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Retrieve eligible parent tabs

Use the GetEligibleParentTabsAsync() method to retrieve a list of parent tabs, which you can associate with a tab when you add or edit it. In the Relativity UI, a parent tab displays a drop-down list containing child tabs.

Pass this method the Artifact ID of the workspace where you want to add the tab or where it currently exists.

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
public bool GetAvailableParents(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            List<ParentTabResponse> response = proxy.GetEligibleParentTabsAsync(SampleWorkspace_ID).GetAwaiter().GetResult();

            _logger.LogDebug("All available parent tabs for workspace {WorkspaceID}", SampleWorkspace_ID);



            foreach (ParentTabResponse tab in response)

            {

                _logger.LogDebug("{Name} - {ArtifactID}", tab.ObjectIdentifier.Name, tab.ObjectIdentifier.ArtifactID);

            }



            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Get all available parents failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Retrieve workspace-level metadata for admin and system tabs

You can retrieve workspace-level metadata about admin and system tabs. This metadata includes fields that can't be updated and those that aren't supported for a specific tab. In general, the following guidelines apply to this metadata:

- Admin tabs - Because these tabs are supported only for workspaces, the RelativityApplications field is always returned as an unsupported field by the GetMetaAsync() method.

- System tabs - Because these tabs are part of the core Relativity application, most of their fields can't be updated, and are returned by GetMetaAsync() method as read-only fields, such the Name, Link, and RelativityApplications fields. For example, the fields on the Errors tab are read-only.

Call the GetMetaAsync() method by passing -1 to indicate the admin-level context. See Admin-level context .

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
public bool GetMeta(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            Meta response = proxy.GetMetaAsync(SampleWorkspace_ID).GetAwaiter().GetResult();

            _logger.LogDebug("Tab Meta for workspace {WorkspaceID}", SampleWorkspace_ID);



            foreach (String unsupportedMeta in response.Unsupported)

            {

                _logger.LogDebug("Unsupported - {UnsupportedMeta}", unsupportedMeta);

            }



            foreach (String readOnlyMeta in response.ReadOnly)

            {

                _logger.LogDebug("ReadOnly - {ReadOnlyMeta}", readOnlyMeta);

            }



            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Get workspace level metadata failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Retrieve tab orders

The order assigned to a tab determines its position in the Relativity UI. Tabs with a lower order number are displayed on the left, while those with higher order numbers are displayed on the right. For more information, see Tabs on the Relativity Documentation site.

Use the GetViewOrderList() method to retrieve the current order for tabs in a specific workspace. Call this method with the Artifact ID of a workspace. For the order of system or admin tabs, pass -1 instead of an Artifact ID. See Admin-level context .

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
public bool GetViewOrderList(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            List<TabViewOrder> response = proxy.GetViewOrderListAsync(SampleWorkspace_ID).GetAwaiter().GetResult();

            _logger.LogDebug("List of all tabs and their view order for workspace {WorkspaceID}", SampleWorkspace_ID);



            foreach (TabViewOrder viewOrder in response)

            {

                _logger.LogDebug("{Name} - {ArtifactID} - {Order}", viewOrder.ObjectIdentifier.Name, viewOrder.ObjectIdentifier.ArtifactID, viewOrder.Order);

            }



            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("Get view order list failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

## Retrieve all tabs for navigation

Use the GetAllNavigationTabs() method to retrieve basic information about each tab the calling user can navigate to in a specific workspace. This method returns a URL for navigating to each tab and tab metadata like the tab's name, order, visibility, parent, and other properties.

Call the GetAllNavigationTabs() method by passing the Artifact ID of the workspace.

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
public bool GetAllNavigationTabs(IHelper helper)

{

    bool success = false;



    using (ITabManager proxy = helper.GetServicesManager().CreateProxy<ITabManager>(ExecutionIdentity.System))

    {

        try

        {

            List<NavigationTabResponse> response = proxy.GetAllNavigationTabsAsync(SampleWorkspace_ID).GetAwaiter().GetResult();



            foreach (NavigationTabResponse navigationTabResponse in response)

            {

                _logger.LogDebug("{Name} - {Order} - {URL}", navigationTabResponse.ObjectIdentifier.Name, navigationTabResponse.Order, navigationTabResponse.Url);

            }



            success = true;

        }

        catch (Exception ex)

        {

            _logger.LogError("GetAllNavigationTabs failed - {message}", ex.Message);

            throw;

        }

    }



    return success;

}
```

On this page

- Tab Manager (.NET)

- Fundamentals for managing tabs

- Guidelines for using the Tab Manager service

- Access the Tab Manager service

- Admin-level context

- Retrieve a value from a Task object

- Set ParentID property

- Use of response data from read operations

- IconIdentifier property

- Create a tab

- Retrieve tab metadata

- Update a tab

- Delete a tab

- Retrieve object types for a tab

- Retrieve eligible parent tabs

- Retrieve workspace-level metadata for admin and system tabs

- Retrieve tab orders

- Retrieve all tabs for navigation


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
