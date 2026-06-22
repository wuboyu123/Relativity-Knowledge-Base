---
title: "Pre Install event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Pre_Install_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:29:00+00:00
sha256: 61e5824f31c38a67234bdf56b509d68382340a64bebfc1be1da9bb12dca9138e
---

Pre Install event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre Install event handlers

Pre Install event handlers provide you with the ability to develop custom code that executes during the installation of an application. You can use Pre Install event handlers to create database tables or perform other tasks that you must complete before fully deploying an application. You can identify the execution type of these event handlers and the order in which you want them to run. Before executing a Pre Install event handler, you can also check the version of the application that you want to update or modify. For more information, see Pre and Post Install event handlers

## Guidelines for Pre Install event handlers

Use these guidelines when developing Pre Install event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PreInstallEventHandler class – ensure that you extend the PreInstallEventHandler base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Pre Install event handler

Review the following sample code for the DependencyCheckPreInstallEventHandler class. It illustrates how to initialize a service proxy, in this case the ObjectManager service, that can be used elsewhere in your solution.

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

using System;



using kCura.EventHandler;

using Relativity.API;

using Relativity.Services.Objects;



namespace Relativity_PreInstallEventHandler1

{

    [kCura.EventHandler.CustomAttributes.RunOnce(true)]

    [kCura.EventHandler.CustomAttributes.RunTarget(kCura.EventHandler.Helper.RunTargets.Workspace)]

    [kCura.EventHandler.CustomAttributes.Description("Dependency Check Pre-Install EventHandler")]

    [System.Runtime.InteropServices.Guid("ba357f30-44b3-477a-b0f0-9c7faaab80ec")]

    public class DependencyCheckPreInstallEventHandler : kCura.EventHandler.PreInstallEventHandler

    {

        public override Response Execute()

        {

            // Construct a response object with default values.

            Response retVal = new Response

            {

                Success = true,

                Message = string.Empty

            };

            try

            {

                using (IObjectManager objectManager = this.Helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

                {

                    CustomDependencyChecker dependencyChecker = new CustomDependencyChecker(objectManager);

                    dependencyChecker.EnsureAllDependencies();



                    retVal.Success = true;

                }

            }

            catch (Exception ex)

            {

                //Change the response Success property to false to let the user know an error occurred

                retVal.Success = false;

                retVal.Message = $"Failed checking dependencies: {ex}";

            }



            return retVal;

        }

    }

}
```

On this page

- Pre Install event handlers

- Guidelines for Pre Install event handlers

- Code sample for a Pre Install event handler


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
