---
title: "Build applications"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Building_Relativity_applications.htm
collection: developer
fetched_at: 2026-06-22T06:33:12+00:00
sha256: 375397639147276cbabeb2fd5527050512d50724a0167d17af78c18fc49c6475
---

Build applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Build applications

You can build applications that extend Relativity by using the Application Deployment System (ADS). ADS provides a framework for application development by helping you leverage existing functionality in Relativity, such as views, layouts, and other features. It also simplifies the packaging of custom code. You can upload this code to Relativity and associate with an application that you create through the Relativity UI. When you finish developing your application, you can easily export a RAP file for installation on other Relativity instances or in specific workspaces.

See these related pages:

- Create an application in Relativity

- Best practices for building applications

- Advanced functionality for the application framework

- Develop application event handlers

- Loading application resources

- Troubleshoot applications errors

## Use the ADS

You can use ADS to develop applications by creating new components through the Relativity UI and by uploading custom code. You can create these components to provide a unique look and feel for your applications:

- Custom pages – add your own cascading style sheets (CSS), JavaScript, HTML, and images to these pages. See Customize the UI .

- Views – control how item lists are displayed. See Views on the Relativity Documentation site.

- Layouts – provide web-based forms for viewing and editing fields. See Layouts on the Relativity Documentation site.

- Tabs – provide links to custom pages and Relativity object pages. See Tabs on the Relativity Documentation site.

You can use these components to provide additional functionality in your application:

- Relativity Dynamic Objects (RDOs) – create your own business objects and then further define object rules to refine their behavior. See Editing Relativity Objects .

- Fields – store data about an object or store choices. See Fields on the Relativity Documentation site.

- Choices – provide list of predetermined values that users can select in a field. See Choices on the Relativity Documentation site.

- Relativity scripts – link custom SQL and other scripts to your application. See Develop scripts .

- Saved searches – link saved searches that use keyword, dtSearch, and Analytics indexes to your applications. See Saved search on the Relativity Documentation site.

- Dashboards – link custom dashboards to your application. See Dashboards on the Relativity Documentation site.

In addition, you can use the base classes provided for these components to extend Relativity:

- Agents – used to develop back end processes. See Agents .

- Event handlers – used to customize workflows and support events associated with installing, uninstalling, creating, and deleting application components. See Event Handlers and Develop application event handlers .

- Mass Operation handlers – associated with specific object types so that you can select multiple instances and then perform a specific action on them all. See Develop Mass Operation handlers .

## Writing custom code for applications

The main components of a Relativity application generally include event handlers, custom pages and agents. These components can share common code by using interfaces available in the Relativity.API NuGet package. The interfaces provided by Relativity.API Helpers expose functionality used for these operations:

- Interact with the database.

- Retrieve authentication tokens.

- Perform other operations.

In addition, your application should reference the Relativity.Kepler NuGet package which provides an abstraction layer and creates proxies to various extendable parts of the platform. From there, you can reference specialized NuGet packages that define specific API layers that Kepler services, such as Relativity.ObjectManager and Relativity.Services.Interfaces.

On this page

- Build applications

- Use the ADS

- Writing custom code for applications


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
