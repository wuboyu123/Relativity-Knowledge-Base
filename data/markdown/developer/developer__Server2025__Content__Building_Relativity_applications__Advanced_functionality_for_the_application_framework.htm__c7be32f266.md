---
title: "Advanced functionality for the application framework"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Advanced_functionality_for_the_application_framework.htm
collection: developer
fetched_at: 2026-06-22T06:30:56+00:00
sha256: f86ace47c3c8ac7336d3d09ab6a9087ed16f51ffc44ccba26975c01ea1991c55
---

Advanced functionality for the application framework

# Advanced functionality for the application framework

You can further enhance your applications by learning about how to use advanced functionality, such as versioning. In addition, you can fine-tune your applications with an understanding of other advanced features.

## Hosted and schema component

Relativity applications have two groups of components:

- Hosted components - are installed for the entire instance of Relativity. These include, resource files, agent types, and custom pages.

Hosted components are installed once regardless of the number of workspaces in the instance. They incur near-zero downtime as Relativity loads new versions of event handlers, agents, Kepler endpoints, and custom pages and wraps up current requests before shutting down previous versions. It is safe to update hosted components in a live instance of Relativity.

- Schema component - are installed into workspaces. These include object types, fields, tabs, layouts, etc.

Each workspace has its own copy of these items. Unlike the installation of hosted components, updates to schema component may cause errors due to changes to the data model, tabs, and layouts and performance degradation due to database updates. Workspace installations should only happen during scheduled downtime.

### Schema version

Often a new version of an application only includes updates to hosted components while the schema component (or schema) remain unchanged and do not require workspace installations. Until Relativity 11.2, there was no way to refresh hosted components without also updating the workspaces. The introduction of a schema version fixes this. With the schema version feature, applications can declare two versions in the application.xml file. The first is the existing <Version/> element which is the version of the entire application. Changes to the application version triggers updates to the hosted components. The second is the new <SchemaVersion/> element. It applies only to the schema component. If the incoming schema version is higher than the value in the workspace, the ADS will schedule workspace installations; otherwise they are skipped.

The schema version allows application developers to control when schema component are updated. They can keep the same value to push through updates to hosted components without affecting workspaces resulting in better performance and near-zero downtime.

## Application schema versions

You can use application versions to manage the development, installation, and upgrading of Relativity applications. Relativity uses the format Major.Minor.Build.Revision to version applications. It automatically assigns a version number to an application if you don't specify one during creation. The default version number is 0.0.0.1. See Create an application in Relativity .

You can edit an application version by modifying the major, minor, or build number. The new version number must be greater than the current version. However, you can't change the revision number in a version. During the export, Relativity automatically increments the revision number if the application has undergone any modifications. It increments the revision number if you performed any of the following actions:

- Unlocked the application since the last export.

- Exported your application for the first time. For example, Relativity increments the version number of 0.0.0.1 to 0.0.0.2 when you export the application.

In addition, the following application components use these versioning practices:

- Mass operations currently aren't versioned. When you import an application, Relativity overwrites any existing mass operations that match those in the imported application. Otherwise, it creates a new mass operation based on the components of the imported application.

- Modifying a saved search in a locked application causes Relativity to increment the version when you export the application. For more information, see Locking and unlocking applications on the Relativity Documentation site.

### Upgrades and schema versions

During an upgrade, Relativity uses the following criteria to determine whether to perform a full or incremental installation of an application in a workspace.

#### Full upgrades

Relativity performs a full upgrade when the following conditions are true:

- Unlocked state – Relativity considers unlocked applications to be in an unknown state so it performs a full upgrade.

- applicationIsDirty state – Relativity sets this flag to True when you unlock an application. If you unlock and then lock an application, Relativity considers it to be in an unknown state and performs a full installation.

- Mismatched origin signatures – Relativity determines if application that you are upgrading originates from the same workspace as the application that you are installing. If it detects mismatching origin signatures, then it performs a full installation.

#### Incremental upgrades

Relativity performs an incremental upgrade by installing only new or modified application objects and dissociating obsolete objects. Incremental upgrades run faster because they only perform updates to address changes that exist between the current version of the application and the new version that you are installing.

It performs this type of upgrade when the following conditions are true:

- Schema version number differences – The schema version number of the application being installed is greater than that of the existing application.

- Unlocked state – Target application hasn't been unlocked.

- Matching origin signatures – The source workspace is the same in both the application that you are in stalling and the one being upgraded.

## Tab behavior during installations and upgrades

The following rules control tab behavior during initial installation and upgrades:

- Parent Tabs included in the “ParentTabs” element of the schema will be installed before their child tabs.

- Only two levels of parent tabs are allowed.

- Valid Hierarchy: Parent Tab > Nested Parent Tab > External/Object Ta

- Valid Hierarchy: Parent Tab > External/Object Tab

- Invalid Hierarchy: Parent Tab > Nested Parent Tab > Another Parent Tab

- First-time installations use these rules to control nested tabs:

- The tab’s ParentTabGuid is used to find the parent tab.

- If no parent tab is found by GUID, the tab’s ParentTabName is used to find the parent tab.

- If multiple tabs are found with the same name, the incoming tab will be nested under the Default Application Tab (see next bullet)

- For External and Object Type tabs only: If no parent tab is found by Name, the external/object tab is nested under the Default Application Tab.

- ADS will attempt to find a tab named after the application, this is the Default Application Tab.

- If no existing Default Application Tab is found, one will be created and named after the application.

- If multiple tabs are found with the application’s name, the incoming tab will be nested under the root system artifact (see next bullet).

- If a valid parent tab cannot be found or created for the incoming tab, it will be nested under the All Tabs menu.

- Upgrades use these rules to control tabs:

- No updates will be made to an existing tab's position in order to preserve any customizations by the Relativity administrator.

- This includes: Is Default, Display Order, Is Shown in Sidebar, and the tab’s Parent.

- New tabs will follow the rules above as if they were first-time installations.

If you previously built an application with a parent tab, upgrading to Relativity 6.10 or above automatically removes the tab.

## Object type event handler behavior during upgrades

Depending on the version of Relativity, Relativity treats object type event handlers differently during application upgrades.

Relativity 9.5.219.30 or later

When upgrading an application to a newer version, if the new version of the application no longer contains the event handler (but previously did), Relativity removes the event handler from the object type. You don't have to write custom code to remove the event handler association from the object type.

Before Relativity 9.5.219.30

If the new version of the application no longer contains an object type event handler, the event handler is removed from the application but the object type association persists. You can remove the event handler from the object type by writing a post install event handler .

## Application resource file purge

Before July 2017, the files associated with older versions of applications remained in place following upgrade and required special programming logic to delete. This complicated development and the upgrade process.

Beginning in July 2017, the application upgrade process purges assembly resource files (DLLs) no longer associated to the newer application version:

- Physically deletes all DLL resource files that were part of the original application version.

- Removes event handler associations on objects types such as Document or Custodian.

- Remaps object references in the workspace database to reference the new DLL.

- Eliminates workspace references to resources that no longer exist.

- If an agent of a removed type is currently running, it will complete its work and then self-destruct.

The following application components are not deleted by the upgrade process:

- Object types (for example, fields, views, and layouts)

- Scripts

- Saved searches

- Dashboards

You can also manually delete DLL resource files from the Resource Files tab in Developer Mode without having to unlink your objects from all workspaces.
