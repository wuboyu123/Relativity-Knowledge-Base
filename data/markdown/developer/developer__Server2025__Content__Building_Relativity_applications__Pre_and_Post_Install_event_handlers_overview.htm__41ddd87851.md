---
title: "Pre and Post Install event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Pre_and_Post_Install_event_handlers_overview.htm
collection: developer
fetched_at: 2026-06-22T06:31:36+00:00
sha256: 5fc35c6cfc595293211b18c3ecdd0b63740f4b61bf26534f0148b202bb540129
---

Pre and Post Install event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre and Post Install event handlers

Pre and Post Install event handlers provide you with the ability to perform custom actions during the deployment of an application. For example, you can develop Pre Install event handlers that set default values on specific fields during installation. You can also develop Post Install event handlers that update fields immediately after an application is installed in a workspace.

See these related pages:

- Pre Install event handlers

- Post Install event handlers

## Run Pre and Post Install event handlers

You can run Pre and Post Install event handlers from these entry points used to install applications:

- Agents – Add an application to the queue in Library Application on EDDS database, and click Install . Your custom event handlers run as part of the installation process.

- Procuro – Add a custom application to the required application or library folder in your Relativity installation. Run Procuro, which executes your custom event handlers.

- Relativity Web UI – Install an application through the Relativity Application tab on a workspace. Your custom Pre and Post Install event handlers execute as part of the application installation.

- Services API – Use the InstallApplication() method on the proxy to install the application and execute the event handlers.

Use Windows Authentication when logging in to Relativity from a Pre or Post Install event handler. When Procuro executes these event handlers, the account that it runs under must have valid credentials for Windows Authentication and system admin rights to the Relativity instance. For sample code, see Pre Install event handlers .

In addition, Pre and Post Install event handlers provide the following functionality that you can customize:

- Execution type – You can use the RunOnce class to identify a Pre or Post Install event handler that is run only when the application is initially installed in a workspace. If the installation fails, these event handlers are re-executed until the application is successfully installed, and then no longer run.

You can add this class as an attribute to the header of an event handler class file. The RunOnce class is available in the kCura.EventHandler.CustomAttributes namespace. See Event Handlers API .

- Execution order – You can specify the order used to run a group of Pre or Post Install event handlers when you add them to an application through the Relativity UI. This functionality provides you with the ability to include multiple install event handlers in an application while controlling how they are executed. The Relativity Applications tab displays the execution type and order for each Pre and Post Install event handler in the Install Event Handlers associative list. See Create an application in Relativity .

- Logging messages – Pre and Post Install event handlers also provide you with the ability to return custom status messages about their execution. This information appears on the status page in the Relativity UI. For more information, see Log messages for Pre and Post Install event handlers .

## Log messages for Pre and Post Install event handlers

As a best practice, you should log messages about the execution of Pre and Post Install event handlers that you add to an application. These messages are listed on the status page that appears immediately after an application is installed or through the Application Library tab as shown in the following illustration.

You can log this custom status information by setting the Message property on the Response object returned by a Pre or Post Install event handler. In addition, you can provide troubleshooting information about a known exception by customizing the information contained in the Message property. We recommend using the IAPILog interface to obtain verbose and process-oriented information. The following code exemplifies how to log messages for Pre and Post Install event handlers.

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
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
using System;

using Relativity.API;

using kCura.EventHandler;

using Relativity.Services.Objects;

namespace Relativity.Samples.EventHandlers { [kCura.EventHandler.CustomAttributes.Description("Performs a custom operation using best practices.")][kCura.EventHandler.CustomAttributes.RunOnce(true)][System.Runtime.InteropServices.Guid("6afd07dc-c0c1-4afc-bcd5-433260a30c77")]

  class BestPracticePreInstall: PreInstallEventHandler {

    /// <summary>

    /// This code sample illustrates best practices for logging a status message from an Pre

    /// or Post Install event handler.

    /// </summary>

    /// <returns>Response Object with information about the execution of the event handler. The contents

    /// of the Message property is displayed in the application.</returns>

    /// <remarks></remarks>

    public override Response Execute() {

      Response response = new Response();

      IAPILog logger = Helper.GetLoggerFactory().GetLogger();

      try {

        logger.LogDebug("Started Event Handler Logic.");

        //Create an instance of the Object Manager using the context of the current user logged into the system.

        using (IObjectManager objectManager = Helper.GetServicesManager().CreateProxy < IObjectManager > (ExecutionIdentity.CurrentUser)) {

          logger.LogDebug("Performing custom logic with Object Manager");

          // CUSTOM CODE

        }

        //Clean up.

        //Set a successful return message that appears in the application.

        response.Success = true;

        response.Message = "Best Practice Pre Load Event Handler ran successfully";

      }

      //If you can identify an exception, provide a message that explains how to resolve the issue.

      catch(CustomException ex) {

        response.Success = false;

        response.Exception = ex;

        //Display information about resolving the issue to the user.

        response.Message = "The environment needs to be fixed in the following ways: ....";

      }

      catch(Exception ex) //Unknown exception

      {

        response.Success = false;

        response.Exception = ex;

        response.Message = ex.Message;

      }

      return response;

    }

  } //End BestPracticePreInstall.

  public class CustomException: System.Exception {

    public CustomException() : base("This is a custom Exception") {}

  }

}
```

On this page

- Pre and Post Install event handlers

- Run Pre and Post Install event handlers

- Log messages for Pre and Post Install event handlers


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
