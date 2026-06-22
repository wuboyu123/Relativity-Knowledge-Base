---
title: "Relativity Application Framework"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Relativity_applications.htm
collection: developer
fetched_at: 2026-06-22T06:25:04+00:00
sha256: 0d91df5e91c036bbb920c4cf97d982755a63ed1d861b999b549ac0263d82879d
---

Relativity Application Framework Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Application Framework

The Relativity platform offers versatile options for extending and customizing core functionality. You can tailor Relativity to meet your organizational business needs by developing custom applications. You can install these applications in multiple workspaces on one or more Relativity instances. Depending on your development goals, you can create new objects through the Relativity UI, and then enhance them with your own custom code and UI. The Relativity platform includes support for the development of agents, custom pages, and event handlers that you can easily package in your application. You can then deploy the application in other workspaces or instances.

See these related pages:

- Customize workflows

- Build agents

- Customize the UI

- Use Relativity API helpers

- Develop scripts

- Build applications

- Logging

## Use cases for extending Relativity

You can leverage multiple features available in the Relativity platform to create custom applications that meet the specific needs of your users. Depending on your business goals, you can use these extensibility points to perform diverse operations from validation to database updates. The following use cases focus on various business entities and the type of development projects, which may complement their organizational goals:

- Build simple workflows - the Relativity platform provides functionality to support the needs of your organization without requiring extensive IT resources. Project managers, business analysts, and other users can build simple workflow applications, which track key data points on your cases. For example, you can create custom RDOs that store data about the receipt or shipping of media, custodians associated with a matter, external contractors assigned to a matter, and other project management tasks.

- Add custom objects and code - depending on your industry vertical, you can extend Relativity by developing simple workflows that use Relativity Dynamic Objects (RDOs) to capture business metadata. You can build on these basic applications by adding custom code such as event handlers, which validate data entered by users or pre-populate fields to simplify the data entry process. In addition, you can use these RDOs to customize your litigation workflow by ensuring that the appropriate layout displays for a specific user activity.

- Automate processes - you can customize your Relativity instance to reduce expenditures by automating processes, such as workspace creation or quality assurance tasks. For example, the Relativity platform includes a specialized event handler that you can use to add or modify database tables during workspace creation. You can incorporate these event handlers that contain your custom code into any new applications that you develop.

- Implement advanced applications - you can utilize the power and extensibility of the platform by implementing advanced applications. These applications can provide new functionality to address business needs beyond the scope of the traditional review process. The Relativity platform offers multiple APIs that support the development of unique UIs. These UIs may include custom pages, sophisticated backend processes with agents, and customized user interactions with event handlers. By using the Application Deployment System (ADS), you can package your custom code in applications that users can easily install in their workspaces or instances.

- Create custom reports - you can leverage platform extensibility options by writing scripts and event handlers to enhance the functionality available in Relativity. You can implement scripts that build customized reports, which summarize review statistics or billing data. Additional options include the development of event handlers designed to automate or streamline various stages of the review process by specific user types.

## Sample workflow for building applications

To extend Relativity, you can use any workflow for implementing your application customization that best fits your development needs. You may want to consider the following sample workflow that helps clarify how to build an application using the ADS framework:

- Identify key application features and functionality - determine the business entities that you want your application to manipulate and processes that you want it to perform. Identify the entities that you want represented as objects in your application.

- Create an application - designate a workspace specifically for the development of your application. In the Relativity UI, create a new application to serve as a placeholder for attaching all of your entities and custom business logic. After testing your application, continue to update only your development version of it. This practice simplifies versioning and upgrading as you modify the application and deploy new versions to other workspaces. See Create an application in Relativity .

- Add RDOs and other components - in the Relativity UI, create RDOs for the business entities that you want represented in your application. You can also add new fields, choices, views, layouts, tabs, and scripts through the Relativity UI. While you can continue to complete these tasks at any time during development, you must create your RDOs before you can associate object type event handlers with them. See Relativity objects .

For example, you might create a Judge and a Clerk object for an application designed to track information about pleadings. You might also decide that you want a custom view for displaying a list of Judge instances, which you can configure through the Relativity UI. You might later add an object type event handler that validates the name of Judge entered by a user.

- Develop your custom code - write custom agents, event handlers, or custom pages. As part of this process, you need to install the Relativity SDK and add references to required libraries in your Visual Studio project. You should enable Developer mode because it turns on features in Relativity that simplify application development.

When you finish development, compile your source code so that you can add this new functionality to your application. If you develop custom pages, you need to compile and publish them before you upload them to Relativity. See Publishing and uploading custom pages .

- Upload your assemblies - you must upload your compiled assembles with your custom code to Relativity UI in order to associate them with an application. If you created object type event handlers, you can associate them with RDOs and documents. If you created application event handlers, associate them with applications. You can upload assemblies for event handlers and agents through the Resources tab in Relativity. Custom pages are added through the Custom Pages tab within your development workspace. See Resource files on the Relativity Documentation site.

- Export your application - when all of the customizations to your application are complete, you can then export the application for installation to other workspaces and instances. The export process packages all your customizations into a single file so you can easily transfer and install it in other Relativity instances. If you want to add changes or modify your application, update the original version that resides in your development workspace, and then export it when you are finished. Relativity automatically increments the version on export if the application is unlocked or the application schema has been modified. After you obtain the new package, you can then upgrade other workspaces with the new version. See Exporting applications on the Relativity Documentation site.

On this page

- Relativity Application Framework

- Use cases for extending Relativity

- Sample workflow for building applications


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
