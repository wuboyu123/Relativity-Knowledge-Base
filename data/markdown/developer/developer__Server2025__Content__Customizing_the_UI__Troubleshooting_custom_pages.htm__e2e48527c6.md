---
title: "Troubleshoot custom pages"
url: https://platform.relativity.com/Server2025/Content/Customizing_the_UI/Troubleshooting_custom_pages.htm
collection: developer
fetched_at: 2026-06-22T06:31:23+00:00
sha256: 26e587902f99f949f1c84b5523434e6df5cedf75be8ba0be5fd09278d0021585
---

Troubleshoot custom pages

# Troubleshoot custom pages

You can use the following information to identify causes of deployment errors and to remotely debug custom pages.

## Remotely debug custom pages

Use these instructions to debug custom pages on a Relativity web server from your workstation:

- Configure remote debugging on the Relativity web server. See Remote Debugging on MSDN.

- On the web server, right-click on the Remote Debugging Monitor ( msvmon ) icon and select Run as administrator . The msvmon icon was added to your desktop when you completed the remote debugging setup in step 1.

The Remote Debugging Monitor displays a message containing the name of the server and the port that you use for the connection. It uses the format: <servername>:<port>. . In step 10, enter this information in the Qualifier box.

- Log in to Relativity and open the workspace containing your application.

- Click the Relativity Applications tab, and then click the name of your application to display the details view.

- Click the Unlock Application button to unlock your application, if necessary.

- Add your custom pages and their .pdb files to a zipped file.

- On the Custom Pages tab, load the zipped file into Relativity. This action overwrites your original zipped file containing the custom pages.

- Navigate to the details view of your application, and click the Push To Library button.

- On your workstation, open your custom page project.

- Attach the debugger to the w3wp.exe processes:

- Click Debug and then click Attach to Process .

- Enter <servername>:<port> in the Qualifier box. By default, the port is 4016.

- Select the w3wp.exe processes in the Available Processes box.

- Click Attach .

- On the Relativity server, check the status of the Remote Debugging Monitor in Visual Studio. It should indicate that you are connected.

- After you finish debugging, repeat steps 3 through 8, but don't add the .pdb files to the zipped file for your custom page.

## Custom page installation errors

During custom page deployment, the Windows Service responsible for deploying custom pages to web servers may encounter errors. Examples of potential errors include the following:

- Web server out of memory and can't deploy the files.

- RAP package is corrupt.

- IIS configuration fails.

To view error messages, search on instance details . The Instance Details page displays a section called Alerts , which contains an error message for each application that fails to install on a server.

Complete the following tasks as necessary:

- Click the Error Details link to view the Error Details page. The Error Details page displays the full contents of the error related to the application install failure.

- Click the Try Installing Again link to prompt the service to re-install the application.

## Custom pages not deployed

Your custom pages won't be deployed when the following service and agent aren't running:

- Web Processing Windows Service – If custom pages fail to deploy on a particular server, this Windows Service may be stopped on that server. In the Alerts section of the Instance Details page, a message may display indicating that the agent server isn't responding, and that the kCura Relativity Web Processing Windows Service on this server needs to be restarted.

- Custom Page Deployment Manager agent – If custom pages aren't deployed, confirm that this agent has been added and that it is running in your Relativity installation. For more information about this agent, see Basic concepts for custom pages .

## Readiness check is falling

The readiness check must fulfill certain requirements to be considered successful. For more information, see Readiness check URL.

Additional infrastructural requirements:

- Each web server must allow HTTP traffic over localhost.

- The Require SSL IIS setting is not compatible with readiness checks. To block external HTTP traffic while still allowing readiness checks, we recommend utilizing the following URL rewrite rules on the Relativity site:

Copy

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
<rule name="No redirect on warmup request (request from localhost with warmup user agent)" stopProcessing="true">

    <match url=".*" />

    <conditions>

        <add input="{HTTP_HOST}" pattern="localhost" />

        <add input="{HTTP_USER_AGENT}" pattern="Initialization" />

    </conditions>

    <action type="Rewrite" url="{URL}" />

</rule>

<rule name="HTTP to HTTPS redirect" stopProcessing="true">

    <match url="(.*)" />

    <conditions>

        <add input="{HTTPS}" pattern="off" ignoreCase="true" />

    </conditions>

<action type="Redirect" url="https://{HTTP_HOST}/{R:1}" redirectType="Permanent" />

</rule>
```

Complete the following steps to troubleshoot the readiness check:

- Hit the endpoint manually, the endpoint for your custom page readiness check should be formatted as followed:

Copy

```text
1
<protocol>://<Host>/<RelativityBasePath>/custompages/<Application Guid>/<your readiness check path>
```

For more information about Custom Page URL, see Custom Page URL .

- Ensure the endpoint is passing all necessary requirements:

- returning 200 OK status

- completed within 30 seconds

- a GET request

- makes no assumption whether the call is made over HTTP or HTTPS

- Click the Errors tab for details, if there is an error coming from the Agent - Application Manager . A descriptive message of why Custom Page deployment failed will display.

## ApplicationServer table out-of-date

If you delete the CustomPages subfolder from the EDDS folder on a web server, the ApplicationServer table becomes out-of-date if custom pages are deployed. If you attempt to reinstall the web component of Relativity, the Custom Page Deployment Manager agent runs but won't deploy any custom pages due to discrepancies in the ApplicationServer table.

To resolve this issue, clear the entries from the ApplicationServer table for the web server.

## Mismatched versions of .dll files

When a custom assembly is loaded for an event handler, agent, or custom page, common .dll files (such as kCura.Relativity.Client.dll) are automatically copied into the domain from the lib folder. If you set the Specific Version option in Visual Studio, it may not match the version of the .dll files installed on the environment. This mismatch may prevent your application from executing properly, if at all.

## Can't access custom page

When using applications with custom pages, you should keep a Relativity window open in the background throughout your session. This will maintain a connection to let the system know that your session is active. If you don't leave a Relativity window open in the background and another user views the User Status list, you can't access the custom page after closing your main Relativity window.

## Can't upload custom pages published through Visual Studio 2015 and higher

If you implement a custom page through Visual Studio 2015 and higher, you may receive error messages when uploading it to Relativity. Visual Studio automatically adds a folder called roslyn in the bin directory when Roslyn compilation is enabled in an ASP.NET application. The roslyn folder contains executables that you can’t upload to Relativity through the ADS.

To resolve this issue, remove the following NuGet packages from your Visual Studio project:

- Microsoft.CodeDom.Providers.DotNetCompilerPlatform

- Microsoft.Net.Compilers

Recompile and publish your custom page. You can now upload your custom page to Relativity.

## Find a custom page's physical deployment

Each upgrade or redeployment of a custom page is deployed to a newly created IIS Application and physical directory named via a randomly generated GUID. The constant URL / IIS Application named via the Relativity Application's GUID utilizes a URL rewrite rule to direct traffic to the current deployment. This deployment model is used to reduce user disruption during Custom Page upgrades.

There are two main methods that can be used to determine the current deployment location:

- Files system / IIS

- SQL

### Files system / IIS

Complete the following steps to determine the current deployment location via the files system / IIS:

- Navigate to the appropriate routing folder for the Custom Page on the file system located at: Copy

```text
1
<YourRelativityInstallationPath>\EDDS\CustomPages\Routing\<YourApplicationGUID>
```

- Open the web.config in the directory of a text editor and note the value of the URL rewrite.

-

The URL rewrite value can then be used to determine the current deployment's:

- Physical Path: <YourRelativityInstallationPath>\EDDS\CustomPages\<DeploymentGuid>

- IIS Application: CustomPages\<DeploymentGuid>

### SQL

Complete the following to determine the current deployment location via SQL:

Copy

```text
1
2
3
SELECT [DeployedPath]

  FROM [EDDS].[eddsdbo].[ApplicationServer]

  Where AppGuid = '<YourApplicationGUID>
```
