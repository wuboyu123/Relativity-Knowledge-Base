---
title: "Basic concepts for custom pages"
url: https://platform.relativity.com/Server2025/Content/Customizing_the_UI/Basic_concepts_for_custom_pages.htm
collection: developer
fetched_at: 2026-06-22T06:31:17+00:00
sha256: 96de358c3f394bfeeb4e169d3276b95dbf31c9b9ba10304eb186741b1da760bb
---

Basic concepts for custom pages Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Basic concepts for custom pages

Review these basic concepts to learn about custom page deployment, page linking, and other functionality. For additional information, see Best practices for custom pages .

See this related page:

- Publish and upload custom pages

## Connect to the Services API with the client-side proxy

You can log in to the Services API with the client-side proxy and authenticate with the System or other account. Use the methods on ICPHelper class in the Relativity API Helpers to return a connection to the Services API. Reference the Relativity.API.dll when you create a new custom page. For more information, see Use Relativity API Helpers for establishing Services API connections and Using Relativity API Helpers.

The following code sample illustrates how to log in to the Services API using System account and the Relativity API helper class.

Copy

```text
1
2
3
4
5
using (IObjectManager objectManager = Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

{

  // Proxy created.

  // Add your custom code for working with the ObjectManager.

}
```

## Obtain user and other context information with API Helpers

The Relativity API Helpers contain methods that you can call from your custom pages to facilitate obtaining context and other information. These helpers include interfaces that you can develop against to perform common programming tasks from your custom pages. You can call methods on the Relativity API Helpers to obtain the following context information:

- Database context

- User context information

- Workspace IDs

- Artifact GUIDs

For code samples and other information, see Basic concepts for Relativity API Helpers .

## Custom page deployment

When you deploy custom pages in your Relativity environment, the services and other infrastructure components support them:

- Custom Page Deployment Manager Agent – runs on the kCura Relativity Web Processing Windows Service. It checks for any new versions of an application installed on the LibraryApplication table. It polls the LibraryApplication and ApplicationServer tables in the EDDS database in 30 second intervals. When it discovers a new version, this agent installs the updated application on the web server. Additionally, it updates the ApplicationServer table in the EDDS with the new version number.

- IIS Application Pool – created for an application when you deploy a Relativity application that contains a custom page to a web server. An IIS application pool is created on each web server, where the Custom Page Deployment Manager agent deploys all custom pages. Name is GUID of application

- IIS Application – a component in IIS created for an application that contains custom pages. Each application is linked to a directory that contains all its custom pages. The directory name is your application GUID, which is deployed under the CustomPages folder in Windows Explorer.

- CustomPageManagerIsOffHoursAgent instance setting – controls off hour behavior of the agent as follows:

- When you set this value to True , applications containing custom components are deployed between the hours set in the AgentOffHourStartTime and AgentOffHourEndTime instance settings. If an application is being deployed when the AgentOffHourEndTime elapse, the current deployment completes. No new deployments occur until the next AgentOffHourStartTime.

- When you set this value to False , the Custom Page Deployment Manager agent runs normally and applications containing custom components are deployed as usual.

- Custom Pages Assembly (Relativity.CustomPages.dll) – added to the bin directory of the application when you include custom pages in it. The following .dlls are also added to this directory:

- kCura.Config.dll

- kCura.Crypto.dll

- kCura.Data.RowDataGateway.dll

- kCura.Relativity.Client.dll

- Relativity.API.dll

- Relativity.CustomPages.dll

- RequestModule – intercepts each HTTP request for a custom page directory and authenticates the user based on the ASP.NET_SessionId cookie.

## Supported file types for custom pages

The development of custom pages supports most file types except for those designated as restricted. You can create custom pages using any file type that the IIS can host. For information about restricted file types, see Best practices for custom pages .

You can also use a template to create a custom page. For more information, see Visual Studio templates for Relativity .

## Use URLs as links to custom pages

You can use a URL to link to a custom page that you created for your application. Use the following convention to define custom page URLs:

Copy

```text
1
2

<protocol>://<Host>/<RelativityBasePath>/custompages/<Application Guid>/<custom page path>
```

### Obtain the application GUID

To obtain the application GUID, use the ArtifactID property of the application to query the ArtifactGUID table in the database associated with the workspace where you are developing the application. You can get the ArtifactID from the query string that appears when you view or edit the application. You can also add the Artifact ID column to the view on the Relativity Applications tab to obtain this identifier.

To access a custom page in an application, you must first package your custom pages and link them to an application. Next, export the application and import it into your testing environment through the Application Library tab.

### Deploy the custom page

When you install or import an application, the Custom Pages Deployment Manager agent picks up the custom pages. It extracts and deploys to the appropriate location on the web server. If the application isn't deployed, you can't access the custom pages that it contains. For more information, see Publish and upload custom pages .

If you receive a 404 error code when attempting to access the page, your Custom Page Deployment Manager agent may not be running.

## Use external tabs as links to custom pages

You can use an external tab to create a link to a custom page. When you link a custom page to an external tab, it loads in an IFrame.

You can’t directly use an external tab to open a new window for a custom page. If you want to open a new window for a custom page, you need to write JavaScript code. This code must create a new window that directs to the custom page.

You can create tabs available within a workspace. You can also create them from Home, which is outside a workspace. To create the link, you can define the URL for the custom page with specific tokens. You can also generate the base URL for a link when you add a custom page to Relativity. See Upload a custom page to Relativity .

In Relativity, the Tabs tab provides you with the options to add new tabs. For more information, see Tabs on the Relativity Server 2025 Documentation site.

### Create tabs available in a workspace

When you want to create an external tab in a workspace, you can enter the URL for the custom page in the New Tab dialog. The format for a generic URL contains a token for the application path:

Copy

```text
1
2

%ApplicationPath%/custompages/<YourApplicationGUID>/<YourFilePath>
```

This example illustrates a URL for a specific custom page in a workspace. It uses the token %ApplicationPath% for the application path and the %AppID% for the current workspace ID:

Copy

```text
1
2

%ApplicationPath%/custompages/736b1c1f-d22f-43cf-9094-cc8acf94c604/default.aspx?%AppID%
```

If you need to use the workspace ID in your custom page code, you can easily retrieve it from the custom page URL:

Copy

```text
1
 String appid = Request.QueryString["AppId"];
```

This is the recommended method of getting the workspace ID. You can also use the GetActiveCaseID() method on the API helper.

Copy

```text
1
 var workspaceID = Helper.GetActiveCaseID();
```

For more information, see Basic concepts for Relativity API Helpers .

You can find a complete list of available tokens and other information on the Tabs page in the Relativity Server 2025 Documentation site.

You can add custom pages available in a workspace to Relativity applications. You must install the Relativity application that includes your custom page to at least one workspace or to the Application Library. This process ensures that the custom page is deployed to the web server. To update a custom page on an application, you click Push to Library in the Relativity Application console after completing any changes to the custom page. For more information, see Relativity Application console .

### Create tabs available from Home

Similar to tabs in workspaces, you can specify a tab available from Home, which is outside of a workspace. The following example illustrates a URL for this type of custom page:

Copy

```text
1
2

CustomPages/60a1d0a3-2797-4fb3-a260-614cbfd3fa0d/MyCustomPage.aspx
```

You can't include a custom page available outside a workspace in a Relativity application.

## Simplify custom page URLs

You can simplify how custom page URLs appear for your users. Enter a value for the User-friendly URL when you create or edit an application. If you enter MyCustomApplication in this field, users see custom page URLs that appear as ~/Relativity/apps/MyCustomApplication. However, you can continue to reference custom pages using the user-friendly URL, and the URL that contains the application GUID, such as ~/Relativity/CustomPages/216ecac1-998b-4b67-980b-ada83b9a0f59.

Suggested use cases include using this URL as an extension point when generating links added to email messages, or when programming with helper classes that provide links to your environment. For more information, see Create an application in Relativity and Helper method for custom page URLs .

## Readiness check URL

The readiness check URL is called by the hosting system before any client traffic is routed to the new version of your custom page. This gives you the opportunity to perform final check if your custom page is functional and setup as expected. It'll also serve as an opportunity for your site to load assemblies into RAM, pre-load caches, etc. This technique will significantly reduces the delay seen by end users when live traffic is routed to the new application process.

- If the readiness check for your application falls, the Relativity instance will still route traffic to the previous working version of your custom page.

- In order to perform the readiness check after the custom page deployment, the EnableCustomPageReadinessCheck instance setting has to be set to TRUE.

- The readiness check URL should be a relative URL hosted by your custom page, e.g. /index.html or /Home/ReadinessCheck.

Readiness check call has to meet the following requirements:

- The readiness check will be an authenticated call using the Relativity Service Account.

- The readiness check call will be an HTTP GET request.

- The readiness check must return a 200 status code if the warmup was successful. All other status codes will indicate the readiness check call failed.

- The readiness check must make no assumption about whether the call is made over HTTP or HTTPS.

- The readiness check must complete within 30 seconds.

- The readiness check may be called multiple times and should be resilient to multiple calls.

- Content may be returned by the endpoint however, this content will not be loaded in a browser, parsed, or used in any way. As a result, there will be no subsequent calls to retrieve files referenced in the content.

## Use console event handlers to access custom pages

You can use console event handlers to access custom pages from an application. When creating a console event handler, you associate a custom page with a button that appears in the application console. Users can click this button to display your custom page. This sample code illustrates how to define the URL for a custom page in a console event handler. For more information, see Console event handlers .

Copy

```text
1
2
String basePath = this.Helper.GetUrlHelper().GetRelativePathToCustomPages(new Guid("0540db69-cbec-48cf-9e55-701004ae922d"));

String fullCustomPagesPath = String.Format(@"{0}Home/Index?WorkspaceArtifactID={1}", basePath, this.Helper.GetActiveCaseID());
```

You may want to reference the RelativityInstanceURL instance setting when creating external links for users to access your application. Your system admin can configure this value for your environment. See Instance setting table and Instance settings' descriptions on the Relativity Server 2025 Documentation site.

On this page

- Basic concepts for custom pages

- Connect to the Services API with the client-side proxy

- Obtain user and other context information with API Helpers

- Custom page deployment

- Supported file types for custom pages

- Use URLs as links to custom pages

- Obtain the application GUID

- Deploy the custom page

- Use external tabs as links to custom pages

- Create tabs available in a workspace

- Create tabs available from Home

- Simplify custom page URLs

- Readiness check URL

- Use console event handlers to access custom pages


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
