---
title: "Relativity applications"
url: https://help.relativity.com/Server2025/Content/Relativity/Applications/Relativity_applications.htm
collection: user
fetched_at: 2026-06-22T06:06:29+00:00
sha256: 1d2fb0bafea2cd87bcddf5e6746e9701b5b14f0fb9423bb2e57b1ade1aeeda2b
---

Relativity applications

# Relativity applications

Relativity applications extend core functionality by providing specialized features or workflows. When you install Relativity, your environment is automatically updated with several applications that are called "system secured."

In addition, you may have workflow requirements or other business needs that require custom applications designed specifically for your organization. Business analysts or third-party developers can implement these applications using Relativity Dynamic Objects (RDOs), the Application Deployment System (ADS), and custom code.

The following sections briefly describe the differences between system secured, custom, and Global applications.

- System secured applications

- Relativity custom applications

- Administering Relativity applications

- Global applications

See these related pages:

- Analytics

- Assisted Review

- Case Dynamics

- Processing

- Production

- Exporting applications

- Locking and unlocking applications

- Installing applications

- Troubleshooting installation errors

- Upgrading applications

- Uninstalling and deleting applications

## System secured applications

Relativity comes with several key out-of-box features called system secured applications, which you can find in the Application Library or at the workspace level.

In contrast to custom applications, you can't modify or edit system secured applications.

### Applications installed in the Application Library

The Application Library tab includes these system secured applications:

- Active Learning

Once you install the Active Learning application, you can't uninstall it.

- Analytics

- Analytics Core

The Analytics Core application must be present in all workspaces, and may not be uninstalled.

- Case Dynamics

- ECA and Investigation

- Integration Points

- Processing (requires licensing)

- Production

- Assisted Review

- Relativity Event Handler Express

- Relativity Legal Hold

- Set Extracted Text Size

### Applications installed in workspaces

In a workspace, the Relativity Applications tab includes system secured applications:

- Imaging

- OCR

- Lists

- Search terms reports

## Relativity custom applications

Custom applications extend the existing Relativity functionality by providing new solutions for case management, review processes, specific workflows, or other business needs for your organization. For example, you might want to develop an application to manage tasks and projects or to facilitate a large-scale review of structured data.

You can implement custom applications using the following features in Relativity:

- RDOs - You can develop Relativity dynamic objects that represent real world business entities that your organization uses, such as custodians, contacts, or companies. In addition, you can create custom workflows that use your objects by designing views, layouts, tabs, and other Relativity objects. You don’t need any programming experience just the appropriate security permissions to build these objects. For example, the sample application Media Tracker illustrates how to use RDOs, views, and layouts to track content received from vendors, clients, and opposing counsel. See Building Media Tracker with RDOs .

- ADS - You can use the ADS to package the RDOs, layouts, views, fields, and other Relativity components that you want included in your custom application. The ADS provides you with a framework available through the Relativity UI for packing the components that you create, as well as custom code developed to add advanced functionality to your applications. By using the ADS, you can export your applications for installation across workspaces and on other Relativity instances. You don’t need any programming experience to package your applications with the ADS, but you must have the required security permissions . For more information about the ADS, see Building Relativity applications on the Server 2025 Developers site.

- Custom code - You can add advanced functionality to your custom applications by developing custom code for event handlers, agents, and custom pages. After building files or assemblies with your custom code, you can easily upload them to Relativity for inclusion in your applications. For more information about event handlers, agents, and custom pages, see the Server 2025 Developers site .

## Administering Relativity applications

You can perform various admin tasks with custom applications that use the Application Deployment System (ADS). These administrative tasks include installing applications in your Relativity environment, exporting applications for installation on other Relativity environments or for further customization, and removing them from workspaces or your environment.

You can manage custom applications developed with ADS through the Relativity UI by performing these and other tasks:

- Install applications - Add custom applications to your Relativity environment by installing them in the Application Library or on individual workspaces. In addition, you can push an application installed on a workspace to the Application Library.

- Export applications - Export applications from one workspace for deployment in another workspace. You can also install exported applications in the Application Library on another Relativity instance. In addition, you can export applications for further customization.

- Uninstall or delete applications - Remove applications that you no longer need from a workspace. You can choose to delete just the application or uninstall the applications and its related components.

- Upgrade applications - Add new or updated features to an existing custom application.

## Global applications

Global applications are applications installed on the admin level of a Relativity instance. Their schema versions are not validated, they don't support RDOs, object-type or workspace-based event handlers.

### Viewing global applications

Administrators of production environments can view global applications in the Application Library. They cannot install them into workspaces. Complete the following steps to view which applications are applied to the environment globally:

- Navigate to the Application Library tab.

- In the Views tab in a workspace, click the icon next to All Library Applications.

- On the right side of the newly opened View window, select Is Global Application under Unselected .

- Move the Is Global Application in your view to the right box, Selected . You can move fields between boxes by:

- Double-clicking the field name.

- Using the arrows between the boxes.

- Click Save .

- The Is Global Application column is added to the Application Library.
