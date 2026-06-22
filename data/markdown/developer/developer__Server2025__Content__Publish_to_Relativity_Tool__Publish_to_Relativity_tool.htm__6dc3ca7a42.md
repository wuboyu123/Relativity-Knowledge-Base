---
title: "Publish to Relativity tool"
url: https://platform.relativity.com/Server2025/Content/Publish_to_Relativity_Tool/Publish_to_Relativity_tool.htm
collection: developer
fetched_at: 2026-06-22T06:28:49+00:00
sha256: e50cb4c6d163486c945eda16205616e795cbe3c110554e73cc1d8f555e81b377
---

Publish to Relativity tool

# Publish to Relativity tool

The Publish to Relativity tool simplifies application development by storing a reusable configuration. You can use this configuration to upload custom pages and resource files to Relativity. It eliminates the need to export and reimport applications in order to deploy modifications to your applications. Instead, you can define application and connection settings, which are stored in the app.config file. The tool automatically uses this configuration to upload new or updated files to a Relativity application. You can use the Publish to Relativity tool to perform the following tasks:

- Update an existing custom page in an application.

- Add a new resource file or update an existing one.

## Before you begin

Before you can store a configuration for an application, complete these tasks:

- Download (or search for ) the PublishToRelativity.exe file in the Relativity community site (login is required).

- Obtain the GUIDs for the following components:

- Application GUID - Export your application from Relativity or publish it to the Application Library. You can use either of these processes to create a GUID for your application, which you need to specify configuration settings. To obtain the GUID, use the ArtifactID of the application to query the ArtifactGUID table in the database associated with the workspace where you are developing the application. The ArtifactID is available in the query string that appears when you view or edit an application, or in the Artifact ID column when you add it to the Relativity Applications tab. In Developer mode, you can also obtain the GUID by clicking the Show Component GUIDs link on the application detail view.

- Target workspace GUID - Deploy your application in a workspace. You need to complete this task so that the Publish to Relativity tool can add your custom pages or resource files to it. To obtain the GUID, use the ArtifactID of the workspace to query the ArtifactGUID table in the EDDS database. You can find the ArtifactID of the workspace in the URL bar of your browser after successfully navigating to a workspace. The URL lists the ArtifactID as the AppID. For example, the following URL contains the a workspace artifactID of 1018089: http://Example/Relativity/Case/Mask/EditField.aspx?AppID=1018089.

- Custom pages - To obtain the GUID, use the ArtifactID of the custom page to query the ArtifactGUID table in the workspace database. The ArtifactID is available in the query string that appears when you view or edit a custom page. In Developer mode, you can also obtain the GUID by clicking the Show Component GUIDs link on the application detail view.

## Add a new configuration

Use the following steps to add a new configuration:

- Double-click the PublishToRelativity.exe to launch the tool. See Before you begin .

- Complete the fields in the Application Settings section. See Application settings fields .

- Complete the fields in the Connection Settings section. See Connection settings fields .

- Click Test Connection to verify that the application and connection settings are working properly. See Test application and connection settings .

- Add custom pages or resource files references to the configuration. See Add a custom page or Add a resource file .

- Click Save Configuration . This action saves all the settings currently defined in the Publish to Relativity file tool dialog, including references to any custom pages or resource files that you added.

### Application settings fields

- Configuration Name – the name used for identifying the configuration.

- Application GUID – the identifier assigned to an application when you export it from Relativity or push it to the Application Library. For more information, see Build Relativity applications .

- Workspace GUID – the identifier assigned to the target workspace where you want to add or update custom pages and resource files. You must have already deployed the application in this workspace.

- Export Location – the full path to the exported RAP file. For example, if you want the RAP to be called bookstore.rap, within the PublishToolsExport folder, then you would enter C:\PublishToolsExport\bookstore.rap. Enter the target folder path and the file name with the appropriate extension (.rap). You must specify an Export Location - the Publish to Relativity tool only exports an application when you specify a location.

### Connection settings fields

- Database Username and Database Password – the username and password combination used for logging in to the Relativity database server.

- Database URL – the name or domain\name of the Relativity database server. For example, you might enter MyDatabaseServer or Relativity \ MyDatabaseServer.

- Relativity Username and Relativity Password – the username and password combination used for logging in to the to the Kepler APIs.

- Relativity URL – the URL for the REST API URL in your environment. For example, the URL uses this general format for Relativity Server : Copy

```text
1
https://<host>/Relativity.REST/api
```

## Test application and connection settings

You can test the application and connection settings for a specific configuration. The Publish to Relativity tool includes a text box that displays a confirmation message when the tool successfully connects to the database and Services API. It also displays troubleshooting information when a database connection fails. General error messages may indicate that the connection to the Services API failed. Confirm that you have the correct username, password, and URL for this service. For example, see the error message that appears in the text box under the Connection Settings section:

Click Test Connection buttons in the Application Settings and Connection Settings sections. The appears next to the Test Connection button when the connection succeeds, while appears when the connection fails.

## Add a custom page

You can use the Publish to Relativity tool to update existing custom pages in your application. Follow these steps to add custom pages references to a configuration or remove them as necessary.

- In the Custom Pages section, click Add .

- Complete the fields in the Add Custom Page pop-up. See Custom Page fields . You don't need to add your custom pages to a zipped file before deployment. Instead, choose the publish folder containing your custom pages.

- Click Add to include the custom page in the list box.

- (Optional) To delete a file from the list, highlight it and click Remove .

- Click Save Configuration to update the configuration with your changes.

### Custom Page fields

- Custom Page GUID – the unique ID that Relativity assigned to the custom page. You can use the Publish to Relativity tool to update existing custom pages in your application. See Before you begin .

- Custom Page Folder – the folder path for the custom page that you want to upload. Click Browse to select the file.

## Add a resource file

You can use the Publish to Relativity tool to add new resource files to your application or update existing ones. While you can upload most file types, certain types are restricted, such as .exe files. For a list of restricted types, see Resource files .

Follow these steps to add a resource file:

- In the Resource Files section, click Add . The Resource File pop-up appears.

- To select a file for the File Path field, click Browse . The File Path field displays the location of resource file that you selected.

- Click Add to include the file in the list box.

- (Optional) To delete a file from the list, highlight it and click Remove .

- Click Save Configuration to update the configuration with your changes.

## Publish custom pages and resource files

You can publish custom pages and resource files using the configuration that you have created with the Publish to Relativity tool. When you select a configuration, the tool automatically populates all the setting and file fields with its current values.

If your configuration references custom pages, this tool uploads them to the web server hosting the Relativity instance. The value in the Relativity URL field indicates the location of this instance. See Connection settings fields .

Follow these steps to publish custom pages and resource files:

- Select a configuration from the Configuration drop-down list. You won’t see any configurations listed in this drop-down when you use this tool for the first time. You must save a configuration through the tool in order to see it to the drop-down list.

- If you have added new custom pages or resource files to the configuration, click Save Config File to ensure your updates are included. You don't need to add your custom pages to a zipped file before deployment. Instead, choose the publish folder containing your custom pages.

- Click Publish to upload your files to Relativity. Your application now contains the custom pages and resource files that you published.
