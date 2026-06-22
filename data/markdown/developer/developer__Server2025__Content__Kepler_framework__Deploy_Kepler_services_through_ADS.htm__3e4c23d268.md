---
title: "Deploy Kepler services through ADS"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Deploy_Kepler_services_through_ADS.htm
collection: developer
fetched_at: 2026-06-22T06:31:14+00:00
sha256: 66a0e0487b0bb6990cab09112908aba0263cbe10fc286142e2ddefa222bedba8
---

Deploy Kepler services through ADS

# Deploy Kepler services through ADS

To consume your custom services, you need to deploy them to Relativity through the Application Deployment System (ADS). The ADS framework supports updating existing applications and exporting applications for use in other Relativity environments. When you want to update your Kepler services, you need to upload new assemblies through the ADS framework, and you can also export your services as part of an ADS application.

## Deploy a Kepler service

Use the following steps to deploy your service assemblies (.dll files) to Relativity through the ADS framework.

If you are updating a service, delete the legacy assemblies, and then add the new assemblies as described in steps 7 through 11.

- Open the Relativity instance used for development.

- Create a new workspace to deploy the application containing your service. You can also use an existing workspace to deploy this application. For more information, see Workspaces on the Relativity Documentation site.

- Click the Relativity Applications tab.

- Click New Relativity Application .

- For the Application Type, select one of the following options:

- Create new Application - use this option if you want to add a new application for your service. Complete these steps:

- Enter a name in New Application Name field.

- Click Save . The application details page now appears. Go to step 6.

- Select from Application Library - use this option if you want to modify an existing application. Complete these steps:

- Click to select an application.

- Click Import .

- Click Application details . The application details page now appears. Go to step 6.

- Import from File - use this option if you have a .rap file for your application and want to add it to the workspace. Complete these steps:

- Click Choose File .

- Enter the application information in the required fields. For more information, see Installing applications in the Relativity Documentation site.

- Click Import .

- Click Application details . The application details page now appears. Go to step 6.

- Click Publish to Library .

- Navigate to the Resource Files tab. For more information, see Resource files on the in the Relativity Documentation site.

- Click New Resource File . The resource files layout appears.

- In the Application field, click to select your application in the pop-up window.

- In the Resource File field, click Choose File .

- Add each of the assemblies (.dll files) for your Kepler service interfaces and implementation. Also, add any third-party dependencies used by your application, which aren't automatically deployed by the ADS framework.

You may experience a short delay before your application with the Kepler services is deployed. After this process completes, you can make calls against the service endpoints through REST or the .NET proxy. For more information, see Client-side interactions with a Kepler service and Proxies and authentication .

## Export a RAP with Kepler services

You can export an ADS application as .rap file, which you can install in other Relativity environments. For more information, see Exporting applications in the Relativity Documentation site.

To export an application, complete the following steps:

- Navigate to the applications detail view in the workspace where you added the application.

- To add updated resource files to it, click Unlock Application. For more information, see Locking and unlocking applications in the Relativity Documentation site.

- Upload your updated resource files. For more information, see Resource files on the in the Relativity Documentation site.

- To download the .rap file, navigate to the applications detail view, and click Export Application . For more information, see Exporting applications in the Relativity Documentation site.

## Upgrade an application

When you want to update and then version your application, review the steps in Upgrading applications in the Relativity Documentation site.

Additionally, review the following information about versioning services and applications:

- Versioning for Kepler APIs

- Application schema versions
