---
title: "Document conversion troubleshooting"
url: https://help.relativity.com/Server2025/Content/Relativity/Viewer/Document_Conversion_Troubleshooting.htm
collection: user
fetched_at: 2026-06-22T06:16:50+00:00
sha256: 44523206cb595a958d8899032c0675aff96eff78798e3b6609118c5c77849cbb
---

Document conversion troubleshooting Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Document conversion troubleshooting

You can use the following information to troubleshoot and resolve issues that occur when attempting to access a document in the viewer, or when mass converting documents. This troubleshooting information applies to issues that occur when using the Document Viewer service to facilitate conversion requests for the viewer.

Troubleshooting information is provided for each component of the viewer. If an error persists, you may want to review the discussion of performance considerations for larger Relativity environments. You may need to reset the environment, but you should only perform this task as a final troubleshooting measure for all components of document conversion. Since an environment reset requires you to disrupt Relativity access for users, perform it during off-peak hours.

## Document errors

You can use the following information to troubleshoot errors that occur with a document or its native when running the Document Viewer service. Try to view different types of documents in the viewer. If the error appears on only one or a few specific documents, it may be due to scenarios that Relativity doesn't support. You may encounter document errors when using the Conversion agent and the Conversion Complete agent. For more information, see Conversion errors related to agents .

The following scenarios related to documents aren't supported by the viewer:

- The document doesn't have a native, an image, or a production image.

- The document is password protected and the password isn't in the password bank.

- The user doesn't have permissions to view the native, image, or production image.

- The document is corrupted.

- The document’s file type isn’t supported. Because natives are converted for the viewer technology using Oracle’s Outside In Technology, you can always check supported file types. For more information, see the following resources:

- Oracle Outside In Technology 8.5.3 Supported Formats

- Viewer-supported file types

- Upgrade considerations for Relativity

## Viewer errors

Many of the errors you encounter while using the viewer appear in the viewer itself for easier troubleshooting. Other errors in the viewer get logged in the Errors tab for future reference.

You can use the following information to troubleshoot errors that occur when running the Document Viewer service.

### Converted Cache File and downloading document errors

The Converted Cache File table collects information on previously converted files. The table contains the location of the converted file and possible error message. If you find that a document that was previously accessible on the viewer is no longer accessible, verify that the information in the table is accurate.

Error message Solution

Example error messages related to cache entries.

- Click the Retry link that appears when conversion fails while loading the viewer.

- Verify that the document location in the converted cache file table contains the files listed in the table.

- If retrying doesn’t help, refer to the Errors tab for more information.

Cache Entry location path is empty or invalid.

Cache entry location is unreachable or does not exist.

An error occurred when validating the cache entry.

Example error messages related to downloading documents.

An error occurred when downloading the document part. Document does not exist or is unreachable.

### Timeout errors

You may experience timeout errors when attempting to display a document in the viewer. The following section includes the steps for resolving timeout errors for the Document Viewer service.

View steps for resolving timeout errors for the Document Viewer service

For the Document Viewer service, use the following steps to resolve timeout errors:

- Verify that the Conversion agent and the Conversion Complete agent is enabled in the resource pool. If the agent is disabled:

- Re-enable the agent, and then wait for the message column to show Idle. If the message column never changes to Idle, you should check the Errors tab.

- If changes to your instance settings are required, you must restart the Document Viewer application pool, delete, and then recreate your Conversion agents and your Conversion Complete agents. For more information, see Restarting an application pool .

- Ensure the kCura EDDS Agent Manager Windows service is running on the agent server for the Conversion agents and the Conversion Complete agents.

- Ensure the Service Host Manager Windows service is started and running.

- Check the following topics and associated subscriptions exist:

- conversionresponses topic

ConversionCompleteAgent_Priority<#> subscription

- signalr_topic_dvs_<#> topic

<Unique GUID> subscriptions – one for each SignalR hub connected.

- conversions_rp<Resource Pool Artificat ID> topic.

- ConversionAgent_Priority1 subscription

- ConversionAgent_Priority2 subscription

- ConversionAgent_Priority3 subscription

You should have one of these topics for each resource pool that has a Conversion agent in your environment.

- resourcepoolstatus topic

- resourcePoolStatusMonitor_<Conversion Agent Artifact ID> subscription.

You should have one of these subscriptions for each Conversion agent.

Use these troubleshooting steps if any of the above topics or subscriptions are missing:

- If you are missing any of the ConversionCompleteAgent _Priority subscriptions, delete and recreate the conversion complete agents in the affected resource pool.

- If you are missing the signalr_topic_dvs topic, it's likely that all of your agent services failed. Restart the services and delete and recreate the Conversion agents and Conversion Complete agents to recreate the topic and its subscriptions.

For other timeout errors, refer to the following table for troubleshooting steps:

Error behavior Solution

There are timeout errors on some or occasional documents in the Errors tab.

There may be a large number of requests. Wait and submit requests again.

If the document is too large and repeatedly getting timeout errors, we recommend viewing it outside of Relativity. Increasing the web application timeout interval will not cause the document to load.

If all conversion requests are timing out and you’ve recently upgraded to Relativity 9.4, there may be an issue with the certificates on the web server.

### Retrying conversion

When the viewer encounters an error, you can retry conversion with the retry link. If you are in a state where an error page doesn't load, perform the following steps to manually trigger a fresh conversion job:

- Determine the type of document you are trying to view in the viewer and note its type ID.

Conversion Types

Type ID

Natives

-1

Images

-2

Transcript

-3

Save as PDF

-4

Production Images

The artifact ID of the production set used to create the production images.

- Locate the document in the ConvertedCacheFile table using the document's artifact ID and type ID.

- Find the document’s converted cache file located in the document location column and delete the parent folder. For example, if you see a location like this: …FileShare\cache\2719710\0\903\index.html, delete the folder 903 and all its contents.

- Delete the row in the ConvertedCacheFile that references the document location.

### Resolving other viewer errors

This section provides several errors you could receive in the Relativity HTML viewer and possible resolution steps.

Error message

Solution

Uncaught Type Error: Cannot read property 'index' of undefined

You only see this error if you load the viewer with the browser console open. This is a known issue with Oracle that has since been fixed but has not yet been integrated into the latest version of Relativity.

An error has occurred. A required service is not running.

This error usually means that the Relativity Services API is not running. To troubleshoot this issue:

- Check that the IIS Application pool for Relativity.Services is running. If the application pool is not running, the Start is enabled under the Application Pool Tasks section.

- Go to the Platform Status tab and verify that there are no errors on any of the web processing servers. If there are errors, the diagnostics functionality should help resolve the issue.

500: Internal Server Error

To solve internal server errors, perform one of the following:

- Verify that the Document Viewer application installed without any errors.

- Verify your KeplerServicesUri is correct.

503: Service Unavailable

A 503 Service unavailable error can indicate an error with either the deployment of the Imaging application, Conversion API, or Document Viewer service.

To troubleshoot this issue, verify that the Conversion API and Document Viewer application pools are running for the web server or force redeployment of the custom pages associated with the Conversion API.

How to verify that the conversion API application pool and Document Viewer application pool are running for a web server:

- Locate the list of application pools for Relativity From the IIS Manager.

- Select the c9e4322e-6bd8-4a37-ae9e-c3c9be31776b application pool.

- Click the enabled Start icon to start the application pool on the right-hand side.

- Select the 5725CAB5-EE63-4155-B227-C74CC9E26A76 application pool.

- Click the enabled Start icon to start the application pool on the right-hand side.

How to force redeployment of the custom pages associated with the Conversion API:

- Verify that the Relativity Web Processing service is running on all web servers.

- Run the following query in the Relativity primary database:

UPDATE [edds].[eddsdbo].[ApplicationServer]

SET [State] = 0

WHERE AppGuid IN ('C9E4322E-6BD8-4A37-AE9E-C3C9BE31776B', '5725CAB5-EE63-4155-B227-C74CC9E26A76')

This file was converted with a newer version than what is available on your web server.

You may not have deployed a newer version of Oracle’s Outside In Technology to all components of Relativity. Verify with Customer Support that the correct versions of Relativity, Document Viewer, and imaging are installed in your environment to ensure both versions are up-to-date.

Authorization Error

The specific error message in the viewer reads “An error occurred when checking for authorization”. This message is a catch-all for unhandled errors that occurred when checking for permissions. Contact Customer Support to find a solution.

An error occurred when initializing the viewer.

This is a generic error thrown for unhandled errors while initializing the viewer. It is not tied to a specific document. When this error is thrown, a more detailed exception message should be logged in the Errors tab. If the error message is not helpful, try resetting the environment. If this does not resolve the error, continue on to gather error information and contact Relativity for troubleshooting help.

Could not download this document.

The viewer doesn’t display some errors, but instead provides a link to a location to where you can read that error’s details.

You can view a more detailed error message by going to the following link:

<Webserver>/Relativity/CustomPages/5725cab5-ee63-4155-b227-c74cc9e26a76/viewers/<worksapceartifactid>/<cacheid>/index

Cannot make conversion request for this viewer type.

A failed conversion request for a viewer type is usually the result of corrupted JavaScript of the Document Viewer custom application. Resolve this error by uninstalling and re-installing the document viewer application.

Conversions are not happening. Log in to the Agent Server and check the Windows Task Manager. Ensure there are oilink.exe processes running. If the oilink.exe processes are not visible, delete your conversion agent and then recreate it.

## Cache location server errors

The Cache Manager agent populates information about the cache location server and is located on the Servers tab. When a document is sent for conversion, the converted file is placed in the cache location server.

Errors related to this server usually involve permissions of the folder or space availability.

We recommend creating separate drives or servers for cache location servers.

### Verifying the Relativity Service Account can access the cache location server

If you find that no information about the cache location server is available on its page, verify that the Relativity Service Account can access the server for a resource pool and that the location hasn’t been renamed.

### Increasing free space in cache location server

If you’re converting a large number of files, you can quickly fill the cache location server. Use the following steps to manage a large volume of conversions in your environment and increase free space for future conversion requests.

### Clearing the cache from the cache location server page

An alert appears if the cache location server is low on disk space. Perform the following steps to free up more disk space.

- Locate the server that is above the upper threshold from the Servers tab.

- Click Clear Cache .

- Wait for a background process to clean up the cache.

The cache location server can be empty while the server itself is low on disk space. Creating a separate drive or server for the cache location will ensure that cache location threshold levels are more accurate.

### Solving errors while clearing the cache

Error behavior

Solution

The Cache Manager Agent doesn’t seem to be clearing the cache.

The Cache Manager Agent only runs once per day during off hours. If you need the agent to run during regular hours, delete the agent, and then re-add it.

Clear Cache button is not available.

If the cache location is above the upper threshold and a cleanup job is running, the clear cache button is not available. Cleanup jobs are tracked in the database by the ResourceServer table’s CacheLocationCleanupStatus column. If this flag is set to 1 and you are confident that a cleanup job is not running, you may change it to 0. This fixes a false flag in the database stating that a job is already running.

### Increasing the cache location upper threshold

By default, the CacheLocationUpperThreshold instance setting is 70. Increasing the number gives you more space. Depending on how quickly the cache location server fills up, increasing the upper threshold may only temporarily resolve file space issues in your environment.

### Increasing the space on the cache location server

Talk to your system admin to increase the disk space of your server.

### Deleting unused conversion files

You may find the cache locations contain more records than are found in the converted cache file tables. This may happen if:

- You manually update the ConvertedCacheFile table so that records are dirty without deleting the corresponding cache location folders. It’s safe to delete files or folders that aren’t referenced.

- The Cache Manager Agent was unable to delete the files. Errors are logged in the DeleteCacheFile table in the case databases.

If you find files that are no longer needed due to either of the reasons above, use the retrying conversion section to guide you through how to properly find and delete a file that is no longer being used.

## Conversion errors related to agents

Relativity communicates about document conversion jobs to the conversion agents. It uses the Conversion agent and the Conversion Complete agent to execute these jobs. Conversion jobs convert a native file to an HTML file to render in the viewer. Images and production images convert to XODs. Many of the errors that occur appear in the Viewer. You can use Relativity Logging, or a third party application that analyzes web requests such as Fiddler , to isolate errors that originate with the Conversion API or the Document Viewer services.

The following table lists errors that may occur when the Conversion agent and the Conversion Complete agent run. Like other agents in Relativity, conversion agents log errors to the Errors tab.

The terms "conversion agent" and "conversion agents" in this section refer to both the Conversion agent and the Conversion Complete agent.

Error message or Error behavior

Solution

Invalid request key.

This error means that a conversion agent sent a response to Relativity about a job that Relativity was no longer tracking. This occurs if IIS or the web application is reset.

No filter available for this file type.

This is an error from a conversion agent that is most likely due to the native file not being supported. When this occurs, verify the file type version. Try another similar document, and if the error occurs again, send a copy of the native to Customer Support for them to test.

Failed to perform file conversion, at least one source is required to perform conversion.

Attempt to convert the jobs again. If this doesn’t resolve the issue, then open a ticket with Customer Support .

Error occurred when attempting to convert file(s).

Error occurred when attempting to find the requested job ID.

## Resetting the environment

If the information in the previous sections haven't resolved the viewer issues and you were previously able to view documents in the environment, resetting the environment might resolve your issues. If you’ve never been able to render a document in the viewer, and you’ve recently migrated your Invariant conversion workers to conversion agents, you should check the Errors tab for connection errors.

Resetting your environment requires resetting IIS, which logs off all users in Relativity. Because of this, reset your environment during off-hours. You can follow these steps in any order, but all must be completed to completely reset the environment.

- Restart IIS on webservers.

- Disable your conversion agents, and then remove an lingering messages from the ConversionAgent_Priority# and CAPI-####### subscriptions.

- Restart the kCura EDDS agent manager services on your conversion agent servers.

- Delete the Converted Cache record for the document you are trying to convert.

- Clear the cache location server (accessible from the Servers tab in Relativity).

If after resetting the environment there is no resolution, contact Support .

### Restarting an application pool

You may need to restart the application pools in your environment. The following sections include the steps for this process based on whether you are running the Conversion API or the Document Viewer service.

View the steps for restarting the Conversion API application pool

Use the following steps to restart the Conversion API application pool on a web server:

These steps bring down the Conversion API and should not be performed with active reviewers in the environment.

- Locate the list of application pools for Relativity from the IIS Manager.

- Select the c9e4322e-6bd8-4a37-ae9e-c3c9be31776b application pool.

- Click Stop to stop the application pool on the right-hand side of the screen.

- Wait a few moments, and then click Start to restart the application pool.

These steps only restart the Conversion API application on a particular web server. If you have other web servers, you may need to restart the application pool on those servers as well.

View steps for restarting the Document Viewer service application pool

Use the following steps to restart the Document Viewer application pool on a web server:

These steps bring down the Document Viewer service and shouldn't be performed with active reviewers in the environment.

- Locate the list of application pools for Relativity from the IIS Manager.

- Select the 5725cab5-ee63-4155-b227-c74cc9e26a76 application pool.

- Click Stop to stop the application pool on the right-hand side of the screen.

- Wait a few minutes, and then click Start to restart the application pool.

These steps only restart the Document Viewer application on a particular web server. If you have other web servers, you may need to restart the application pool on those servers as well.

## Performance considerations

There are certain error scenarios that are more prevalent in larger environments or larger conversion requests. The following sections guide you through some configuration changes that may help your environment process larger conversion requests.

### Decreasing the IIS recycling interval

- Open up IIS on each web server.

- Select the application pool with the name: c9e4322e-6bd8-4a37-ae9e-c3c9be31776b on the list of application pools.

- Select the application pool as follows depending on whether you are running the Conversion API or the Document Viewer service:

- Conversion API - select the option with the name c9e4322e-6bd8-4a37-ae9e-c3c9be31776b on the list of application pools.

- Document Viewer service - select the option with the name 5725cab5-ee63-4155-b227-c74cc9e26a76 on the list of application pools.

- Click Advanced Settings under the actions window.

- Change the Regular Time Interval (minutes) to 0 under the Recycling heading.

### Decreasing the number of images loaded in the Image Viewer

You can manually create the MaximumImageCountForViewer instance setting to create a maximum of images the Image Viewer can load which may increase conversion performance. It's recommended to use this instance setting if you have an environment where converting 1000 to 10,000 image documents is causing performance issues. For more information, see MaximumImageCountForViewer

### Resolving Internet browser crashes

If the Text Viewer loads documents slowly in the viewer or if the Internet browser crashes, reduce the following instance settings:

- TextViewerMaxPageSize

- TextViewerPageBufferSize

On this page

- Document conversion troubleshooting

- Document errors

- Viewer errors

- Converted Cache File and downloading document errors

- Timeout errors

- Retrying conversion

- Resolving other viewer errors

- Cache location server errors

- Verifying the Relativity Service Account can access the cache location server

- Increasing free space in cache location server

- Clearing the cache from the cache location server page

- Solving errors while clearing the cache

- Increasing the cache location upper threshold

- Increasing the space on the cache location server

- Deleting unused conversion files

- Conversion errors related to agents

- Resetting the environment

- Restarting an application pool

- Performance considerations

- Decreasing the IIS recycling interval

- Decreasing the number of images loaded in the Image Viewer

- Resolving Internet browser crashes


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


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
