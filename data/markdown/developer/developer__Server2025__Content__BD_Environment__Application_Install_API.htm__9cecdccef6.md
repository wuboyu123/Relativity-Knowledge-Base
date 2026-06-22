---
title: "Application Install (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Application_Install_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:05+00:00
sha256: 362adc677fee044fada1091512eccc887c59c04330ff7976693dacf2bc447fbe
---

Application Install (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Application Install (.NET)

The Application Install API includes methods for installing applications into one or more workspaces, cancel pending installations, as well as retrieving the status of application installations. Additionally, it supports conflict resolution for failed application installations.

You can also use the Application Install API through REST. For more information, see Application Install service .

## Guidelines for the Application Install API

Review the following guidelines for working with the Application Install API.

### Admin-level context

The value for the workspaceID parameter in the path should always be -1. Any other value will return an error.

### Actions and pagination

The Application Install API has several methods that use on an optional parameter called includeActions . These methods include SearchAsync(), SearchApplicationAsync(), and GetAvailableWorkspacesAsync().

The includeActions parameter controls whether the pagination properties are populated, such as FirstPage, NextPage, and others. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request.

Review these guidelines for setting this includeActions parameter:

- True - When the includeActions parameter is set to true, several objects then include additional properties that you can use as follow-up steps to queries. For example, the InstallStatus objects contain the GetDetailsAction property, which provides detailed information about the installation of a single application.

- False - When the API is called without the parameter, the default value of the includeActions parameter is false.

### Permissions

For all endpoints in the IApplicationInstall API, users are required to be system administrators in order to have sufficient permissions.

### Sample use cases

The Application Install API can be used by R1 Operations or ISVs to manage third-party applications in their Relativity instances. For example, a provisioning pipeline may update a new environment with supported third-party applications. Note that this API can be used in conjunction with the Library Application API .

### Create a proxy

The Application Install API includes the following endpoints. To set up a proxy to interact with the IApplicationInstall API, call the CreateProxy() method on the object returned by the GetServiceManager() method.

View sample code Copy

```text
1
2
3
4
5
6
7
Client.SamplesLibrary.Helper.IHelper helper;



// Create a proxy

using (IApplicationRepository applicationRepository = helper.GetServicesManager().CreateProxy<IApplicationManager>(ExecutionIdentity.User))

{

    // Add your custom code ...

}
```

## Install an application library to specific workspaces

To install an application from the library into one or more workspaces, use the InstallApplicationAsync() method of the IApplicationInstallManager interface. The response reports the installation status for each workspace, and a failure to queue an installation request for one workspace will not prevent the others from being queued.

Install Application by ArtifactID Copy

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
public async Task InstallApplication(IApplicationInstallManager applicationInstallManager, int artifactID, List<int> workspaces, bool unlockApps)

{

    try

    {

        InstallApplicationRequest request = new InstallApplicationRequest

        {

            WorkspaceIDs = workspaces,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAsync(ADMIN_WORKSPACE_ID, artifactID, request);



        if (response.Results.Count == workspaces.Count)

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with ArtifactID {artifactID}.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with ArtifactID {artifactID} " +

                                        $"since one or more workspaces already have the same version of this application installed.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Install Application by GUID Copy

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
public async Task InstallApplication(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, List<int> workspaces, bool unlockApps)

{

    try

    {

        InstallApplicationRequest request = new InstallApplicationRequest

        {

            WorkspaceIDs = workspaces,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAsync(ADMIN_WORKSPACE_ID, applicationGuid, request);



        if (response.Results.Count == workspaces.Count)

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with Guid {applicationGuid}.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with Guid {applicationGuid} " +

                                        $"since one or more workspaces already have the same version of this application installed.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Install Application by ArtifactID with actions Copy

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
public async Task InstallApplication(IApplicationInstallManager applicationInstallManager, int artifactID, List<int> workspaces, bool unlockApps, bool includeActions)

{

    try

    {

        InstallApplicationRequest request = new InstallApplicationRequest

        {

            WorkspaceIDs = workspaces,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAsync(ADMIN_WORKSPACE_ID, artifactID, request, includeActions);



        if (response.Results.Count == workspaces.Count)

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with ArtifactID {artifactID}.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with ArtifactID {artifactID} " +

                                        $"since one or more workspaces already have the same version of this application installed.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Install Application by GUID with actions Copy

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
public async Task InstallApplication(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, List<int> workspaces, bool unlockApps, bool includeActions)

{

    try

    {

        InstallApplicationRequest request = new InstallApplicationRequest

        {

            WorkspaceIDs = workspaces,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAsync(ADMIN_WORKSPACE_ID, applicationGuid, request, includeActions);



        if (response.Results.Count == workspaces.Count)

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with Guid {applicationGuid}.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with Guid {applicationGuid} " +

                                        $"since one or more workspaces already have the same version of this application installed.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Install an application library to all workspaces

To install an application into all workspaces or upgrade all workspaces where the application is already installed, use the InstallApplicationAllAsync() method of the IApplicationInstallManager interface.

Install Application to All Workspaces by ArtifactID Copy

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
public async Task InstallApplicationAll(IApplicationInstallManager applicationInstallManager, int artifactID, bool unlockApps)

{

    try

    {

        InstallApplicationAllRequest request = new InstallApplicationAllRequest

        {

            Mode = ApplicationInstallTargetOption.ForceInstall,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAllAsync(ADMIN_WORKSPACE_ID, artifactID, request);



        if (response.Results.Count > 0)

        {

            string info = string.Format($"Queuing {response.Results.Count} installations for the Library Application with ArtifactID {artifactID}.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Install Application to All Workspaces by GUID Copy

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
public async Task InstallApplicationAll(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, bool unlockApps)

{

    try

    {

        InstallApplicationAllRequest request = new InstallApplicationAllRequest

        {

            Mode = ApplicationInstallTargetOption.ForceInstall,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAllAsync(ADMIN_WORKSPACE_ID, applicationGuid, request);



        if (response.Results.Count > 0)

        {

            string info = string.Format($"Queuing {response.Results.Count} installations for the Library Application with Guid {applicationGuid}.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Install Application to All Workspaces by ArtifactID with Actions Copy

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
public async Task InstallApplicationAll(IApplicationInstallManager applicationInstallManager, int artifactID, bool unlockApps, bool includeActions)

{

    try

    {

        InstallApplicationAllRequest request = new InstallApplicationAllRequest

        {

            Mode = ApplicationInstallTargetOption.ForceInstall,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAllAsync(ADMIN_WORKSPACE_ID, artifactID, request, includeActions);



        if (response.Results.Count > 0)

        {

            string info = string.Format($"Queuing {response.Results.Count} installations for the Library Application with ArtifactID {artifactID}.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Install Application to All Workspaces by GUID with Actions Copy

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
public async Task InstallApplicationAll(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, bool unlockApps, bool includeActions)

{

    try

    {

        InstallApplicationAllRequest request = new InstallApplicationAllRequest

        {

            Mode = ApplicationInstallTargetOption.ForceInstall,

            UnlockApplications = unlockApps

        };



        InstallApplicationResponse response = await applicationInstallManager.InstallApplicationAllAsync(ADMIN_WORKSPACE_ID, applicationGuid, request, includeActions);



        if (response.Results.Count > 0)

        {

            string info = string.Format($"Queuing {response.Results.Count} installations for the Library Application with Guid {applicationGuid}.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Retrieve the installation status of an application

To query for the status of a particular application installation request, use the GetStatusAsync() method of the IApplicationInstallManager interface. After invoking InstallApplicationAsync , clients are required to poll until the installation status reaches a terminal state (completed or failed) before the application can be consumed in the target workspace.

Get Install Status with ArtifactID Copy

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
public async Task GetInstallStatus(IApplicationInstallManager applicationInstallManager, int artifactID, int applicationInstallID)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallID);

        string info = string.Format($"Application Installation record for Library Application with ArtifactID {artifactID} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status with Application GUID Copy

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
public async Task GetInstallStatus(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, int applicationInstallID)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallID);

        string info = string.Format($"Application Installation record for Library Application with Guid {applicationGuid} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status with ArtifactID and Actions Copy

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
public async Task GetInstallStatus(IApplicationInstallManager applicationInstallManager, int artifactID, int applicationInstallID, bool includeActions)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallID, includeActions);

        string info = string.Format($"Application Installation record for Library Application with ArtifactID {artifactID} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status with Application GUID and Actions Copy

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
public async Task GetInstallStatus(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, int applicationInstallID, bool includeActions)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallID, includeActions);

        string info = string.Format($"Application Installation record for Library Application with Guid {applicationGuid} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status by Workspace ID and Artifact ID Copy

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
public async Task GetInstallStatusWithoutInstallID(IApplicationInstallManager applicationInstallManager, int workspaceID, int artifactID)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(workspaceID, artifactID);

        string info = string.Format($"Application Installation record for Library Application with ArtifactID {artifactID} in workspace with ID {workspaceID} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status by Workspace ID and Application GUID Copy

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
public async Task GetInstallStatusWithoutInstallID(IApplicationInstallManager applicationInstallManager, int workspaceID, Guid applicationGuid)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(workspaceID, applicationGuid);

        string info = string.Format($"Application Installation record for Library Application with Guid {applicationGuid} in workspace with ID {workspaceID} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status by Workspace ID and Artifact ID with Actions Copy

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
public async Task GetInstallStatusWithoutInstallID(IApplicationInstallManager applicationInstallManager, int workspaceID, int artifactID, bool includeActions)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(workspaceID, artifactID, includeActions);

        string info = string.Format($"Application Installation record for Library Application with ArtifactID {artifactID} in workspace with ID {workspaceID} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Install Status with Application GUID and Actions Copy

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
public async Task GetInstallStatusWithoutInstallID(IApplicationInstallManager applicationInstallManager, int workspaceID, Guid applicationGuid, bool includeActions)

{

    try

    {

        GetInstallStatusResponse response = await applicationInstallManager.GetStatusAsync(workspaceID, applicationGuid, includeActions);

        string info = string.Format($"Application Installation record for Library Application with Guid {applicationGuid} in workspace with ID {workspaceID} successfully read -- Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Retrieve the number of workspaces with an outdated application

To retrieve the total number of workspaces containing an outdated version of a specified application, use the GetOutdatedWorkspacesCount() method. A version is considered "outdated" if it is lower than the version installed in the Application Library.

Get Outdated Workspaces Count by ArtifactID Copy

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
public async Task GetOutdatedWorkspacesCount(IApplicationInstallManager applicationInstallManager, int applicationID) {

  try {

    GetOutdatedWorkspacesResponse response = await applicationInstallManager.GetOutdatedWorkspacesCount(ADMIN_WORKSPACE_ID, applicationID);

    string info = string.Format($ "Successfully retrieved the number of outdated workspace installations associated with this application: {response.OutdatedWorkspacesCount}");

    Console.WriteLine(info);

  }

  catch(Exception ex) {

    string exception = $ "An error occurred: {ex.Message}";

    Console.WriteLine(exception);

  }

}
```

Get Outdated Workspaces Count by Guid Copy

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
public async Task GetOutdatedWorkspacesCount(IApplicationInstallManager applicationInstallManager, Guid applicationGuid) {

  try {

    GetOutdatedWorkspacesResponse response = await applicationInstallManager.GetOutdatedWorkspacesCount(ADMIN_WORKSPACE_ID, applicationGuid);

    string info = string.Format($ "Successfully retrieved the number of outdated workspace installations associated with this application: {response.OutdatedWorkspacesCount}");

    Console.WriteLine(info);

  }

  catch(Exception ex) {

    string exception = $ "An error occurred: {ex.Message}";

    Console.WriteLine(exception);

  }

}
```

## Cancel pending application installations

To cancel one or more pending application installations, use the CancelAsync() method of the IApplicationInstallManager interface. If an installation is already in progress or complete, its corresponding result object will indicate an unsuccessful cancellation with a message explaining why.

Cancel a Single Application Install With Application Artifact ID Copy

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
public async Task CancelApplicationInstall(IApplicationInstallManager applicationInstallManager, int artifactID, int applicationInstallID)

{

    try

    {

        CancelApplicationInstallResponse response = await applicationInstallManager.CancelAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallID);

        if (response.Results[0].IsSuccessful)

        {

            string info = string.Format($"The Library Application Installation with application installation ID {applicationInstallID} was successfully canceled.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"The Library Application Installation could not be canceled: {response.Results[0].Message}");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Cancel a Single Application Install With Application GUID Copy

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
public async Task CancelApplicationInstall(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, int applicationInstallID)

{

    try

    {

        CancelApplicationInstallResponse response = await applicationInstallManager.CancelAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallID);

        if (response.Results[0].IsSuccessful)

        {

            string info = string.Format($"The Library Application Installation with application installation ID {applicationInstallID} was successfully canceled.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"The Library Application Installation could not be canceled: {response.Results[0].Message}");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Cancel Multiple Application Installs With Application Artifact ID Copy

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
public async Task CancelMultipleInstalls(IApplicationInstallManager applicationInstallManager, int artifactID, List<int> applicationInstallIDs)

{

    try

    {

        CancelApplicationInstallResponse response = await applicationInstallManager.CancelAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallIDs);

        string info = string.Format($"Library Application Installations were successfully canceled -- Number of Canceled Installations: {response.Results.FindAll(r => r.IsSuccessful).Count}, " +

                                    $"Number of Cancel Requests: {applicationInstallIDs.Count}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Cancel Multiple Application Installs With Application GUID Copy

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
public async Task CancelMultipleInstalls(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, List<int> applicationInstallIDs)

{

    try

    {

        CancelApplicationInstallResponse response = await applicationInstallManager.CancelAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallIDs);

        string info = string.Format($"Library Application Installations were successfully canceled -- Number of Canceled Installations: {response.Results.FindAll(r => r.IsSuccessful).Count}, " +

                                    $"Number of Cancel Requests: {applicationInstallIDs.Count}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Retrieve installation details for an application

To retrieve the installation details for a specified application and application installation ID, use the GetApplicationInstallDetailsAsync() method of the IApplicationInstallManager interface.

Get Details of an Application Install With Application Artifact ID Copy

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
public async Task GetApplicationInstallDetails(IApplicationInstallManager applicationInstallManager, int artifactID, int applicationInstallID, int start, int length)

{

    try

    {

        GetApplicationInstallDetailsResponse response = await applicationInstallManager.GetApplicationInstallDetailsAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallID, start, length);

        string info = string.Format($"The installation details for Library Application Installation with ID {response.ApplicationInstallID} were successfully retrieved.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Details of an Application Install With Application GUID Copy

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
public async Task GetApplicationInstallDetails(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, int applicationInstallID, int start, int length)

{

    try

    {

        GetApplicationInstallDetailsResponse response = await applicationInstallManager.GetApplicationInstallDetailsAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallID, start, length);

        string info = string.Format($"The installation details for Library Application Installation with ID {response.ApplicationInstallID} were successfully retrieved.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Details of an Application Install by Artifact ID With Actions Copy

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
public async Task GetApplicationInstallDetails(IApplicationInstallManager applicationInstallManager, int artifactID, int applicationInstallID, int start, int length, bool includeActions)

{

    try

    {

        GetApplicationInstallDetailsResponse response = await applicationInstallManager.GetApplicationInstallDetailsAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallID, start, length, includeActions);

        string info = string.Format($"The installation details for Library Application Installation with ID {response.ApplicationInstallID} were successfully retrieved.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Details of an Application Install by App Guid With Actions Copy

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
public async Task GetApplicationInstallDetails(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, int applicationInstallID, int start, int length, bool includeActions)

{

    try

    {

        GetApplicationInstallDetailsResponse response = await applicationInstallManager.GetApplicationInstallDetailsAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallID, start, length, includeActions);

        string info = string.Format($"The installation details for Library Application Installation with ID {response.ApplicationInstallID} were successfully retrieved.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Generate an installation report

Use the GetApplicationInstallDetailsReportAsync() method to retrieves the the installation details for a specified application and application installation ID and creates a CSV report.

Get Details of an Application Install With Application Artifact ID Copy

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
public async Task GetApplicationInstallDetailsReport(IApplicationInstallManager applicationInstallManager, int artifactID, int applicationInstallID) {

  try {

    IKeplerStream response = await applicationInstallManager.GetApplicationInstallDetailsReportAsync(ADMIN_WORKSPACE_ID, artifactID, applicationInstallID);

    using (System.IO.Stream stream = await response.GetStreamAsync())

    using (FileStream output = new FileStream("report.csv", FileMode.Create, FileAccess.Write)) {

      stream.CopyTo(output);

    }

  }

  catch(Exception ex) {

    string exception = $ "An error occurred: {ex.Message}";

    Console.WriteLine(exception);

  }

}
```

Get Details of an Application Install With Application Install With Application GUID Copy

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
public async Task GetApplicationInstallDetailsReport(IApplicationInstallManager applicationInstallManager, Guid applicationGuid, int applicationInstallID, int start, int length) {

  try {

    IKeplerStream response = await applicationInstallManager.GetApplicationInstallDetailsReportAsync(ADMIN_WORKSPACE_ID, applicationGuid, applicationInstallID);

    using (System.IO.Stream stream = await response.GetStreamAsync())

    using (FileStream output = new FileStream("report.csv", FileMode.Create, FileAccess.Write)) {

      stream.CopyTo(output);

    }

  }

  catch(Exception ex) {

    string exception = $ "An error occurred: {ex.Message}";

    Console.WriteLine(exception);

  }

}
```

## Cancel pending application installations

Use the CancelAllAsync() method to cancel all pending application installs associated with a specified application.

Cancel All Pending Installs With Application Artifact ID Copy

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
public async Task CancelAllPendingInstalls(IApplicationInstallManager applicationInstallManager, int artifactID)

{

    try

    {

        CancelApplicationInstallResponse response = await applicationInstallManager.CancelAllAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Successfully cancelled {response.Results.Count} application installations associated with application with identifier {artifactID}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Cancel All Pending Installs With Application Install With Application GUID Copy

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
public async Task CancelAllPendingInstalls(IApplicationInstallManager applicationInstallManager, Guid applicationGuid)

{

    try

    {

        CancelApplicationInstallResponse response = await applicationInstallManager.CancelAllAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Successfully cancelled {response.Results.Count} application installations associated with application with identifier {applicationGuid}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Retrieve installation status by workspace

Use the SearchAsync() method to returns the installation status of one or more applications by workspace. Callers can provide a condition string (with the same format as Object Manager) and a list of sort fields as search criteria. The results are paged using the provided page start index and length.

The includeActions parameter controls whether the pagination properties are populated. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request. For more information, see Actions and pagination .

### Supported Condition Fields

Field Name Data Type

Application Text

Application Artifact ID Integer

Application GUID GUID

Case Artifact ID Integer

Client Name Text

Completed On Date

Current Application Install ID Integer

Installed By Text

Is Installed Boolean

Library Origin Signature Text

Library Version GUID

Matter Name Text

Message Text

Origin Signature GUID

Started On Date

Status Code Integer

Version Text

Workspace Text

Acceptable values for Status Code are 1 (Pending), 2 (InProgress), 3 (Failed), 4 (Completed), and 5 (Canceled).

Find All Failed Application Installations Copy

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
public async Task<List<int>> FindAllWorkspacesWithFailedInstallationsAsync(IApplicationInstallManager applicationInstallManager)

{

    try

    {

        // Set up query options.

        QueryOptions queryOptions = new QueryOptions();

        queryOptions.Condition = "'Status Code' == 3"; // Failed status code is 3.

        queryOptions.Sorts.Add(new Interfaces.LibraryApplication.Models.Query.Sort()

        {

            FieldName = "Workspace",

            Direction = SortDirection.Ascending

        });



        List<int> workspaceIDs = new List<int>();

        const int pageSize = 50;

        int currentStart = 1;



        // Query for failed installations in 50 item pages.

        ApplicationInstallSearchResponse response;



        do

        {

            response = await applicationInstallManager.SearchAsync(ADMIN_WORKSPACE_ID, queryOptions, currentStart, pageSize, true);



            // Add workspaces to the list.

            workspaceIDs.AddRange(response.Results.Select(x => x.WorkspaceIdentifier.ArtifactID));

            string info = $"Successfully returned {response.Results.Count} failed application installations.";

            Console.WriteLine(info);



            // Query for the next page.

            currentStart = response.CurrentStartIndex + pageSize;

        } while (response.NextPage != null && response.NextPage.IsAvailable);



        return workspaceIDs;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Query for application installations by identifier

The SearchApplicationAsync() method returns the installation status by workspace, but it further filters the results by a supplied application identifier. The application filter is a common use case that warrants its own endpoint. The condition string, sort fields, and paging work like SearchAsync.

The includeActions parameter controls whether the pagination properties are populated. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request. For more information, see Actions and pagination .

Find All Failed Application Installations Copy

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
public async Task<List<int>> FindAllWorkspacesWithFailedInstallationsAsync(IApplicationInstallManager applicationInstallManager, int applicationID)

{

    try

    {

        // Set up query options.

        QueryOptions queryOptions = new QueryOptions();

        queryOptions.Condition = "'Status Code' == 3"; // Failed status code is 3.

        queryOptions.Sorts.Add(new Interfaces.LibraryApplication.Models.Query.Sort()

        {

            FieldName = "Workspace",

            Direction = SortDirection.Ascending

        });



        List<int> workspaceIDs = new List<int>();

        const int pageSize = 50;

        int currentStart = 1;



        // Query for failed installations in 50 item pages.

        ApplicationInstallSearchResponse response;



        do

        {

            response = await applicationInstallManager.SearchApplicationAsync(ADMIN_WORKSPACE_ID, applicationID, queryOptions, currentStart, pageSize, true);



            // Add workspaces to the list.

            workspaceIDs.AddRange(response.Results.Select(x => x.WorkspaceIdentifier.ArtifactID));

            string info = $"Successfully returned {response.Results.Count} failed application installations.";

            Console.WriteLine(info);



            // Query for the next page.

            currentStart = response.CurrentStartIndex + pageSize;

        } while (response.NextPage != null && response.NextPage.IsAvailable);



        return workspaceIDs;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Validate new artifact names

Use IsNameAvailable() method to validates any new names requested for artifacts causing name or friendly name conflicts.

Validate If a Name is Available Copy

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
public async Task IsNameAvailable(IApplicationInstallManager applicationInstallManager, List<NameValidationRequest> nameValidationItems)

{

    try

    {

        List<NameValidationResponse> responses = await applicationInstallManager.IsNameAvailable(ADMIN_WORKSPACE_ID, nameValidationItems);

        string info = string.Format($"Successfully validated {responses.Count} requested names.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Query for application installations with additional fields

Use the GetAvailableWorkspacesAsync() method to retrieve a list of workspaces and indicates whether or not the specified application is installed in each workspace. If the application is installed, the version, status, and other installation information will be populated. This endpoint shares the request and response contracts with the SearchAsync and SearchApplicationAsync endpoints.

The includeActions parameter controls whether the pagination properties are populated. If your workflow requires iterating through pages of results using these properties, you need to include the includeActions parameter in your method call with the value set true on in the request. For more information, see Actions and pagination .

Find All Available Workspaces Copy

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
public async Task<List<int>> FindWorkspacesWhereNotInstalledAsync(IApplicationInstallManager applicationInstallManager, int applicationID)

{

    try

    {

        // Set up query options.

        QueryOptions queryOptions = new QueryOptions();

        queryOptions.Condition = "(NOT ('Case Artifact ID' == -1)) AND ('Is Installed' == 0)"; // Exclude workspaces where the application is already installed

        queryOptions.Sorts.Add(new Interfaces.LibraryApplication.Models.Query.Sort()

        {

            FieldName = "Workspace",

            Direction = SortDirection.Ascending

        });



        List<int> workspaceIDs = new List<int>();

        const int pageSize = 50;

        int currentStart = 1;



        // Query for available workspaces in 50 item pages.

        ApplicationInstallSearchResponse response;



        do

        {

            response = await applicationInstallManager.GetAvailableWorkspacesAsync(ADMIN_WORKSPACE_ID, applicationID, queryOptions, currentStart, pageSize, true);



            // Add workspaces to the list.

            workspaceIDs.AddRange(response.Results.Select(x => x.WorkspaceIdentifier.ArtifactID));

            string info = $"Successfully returned {response.Results.Count} available workspaces.";

            Console.WriteLine(info);



            // Query for the next page.

            currentStart = response.CurrentStartIndex + pageSize;

        } while (response.NextPage != null && response.NextPage.IsAvailable);



        return workspaceIDs;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## Workflow-Based code samples

The following code samples provide example scenarios on how the Application Install API and Library Application API endpoints can be used together.

Waiting for a Library Application Update to Complete Copy

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
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
public async Task WaitUntilUpdateCompletes(ILibraryApplicationManager libraryApplicationManager, string rapFilePath)

{

    try

    {

        // Install an updated application into the Application Library.

        int artifactID = await UpdateLibraryApplication(libraryApplicationManager, rapFilePath);

        Console.WriteLine($@"Queuing a new library installation for the application with artifactID {artifactID}.");

        Console.WriteLine($@"Waiting for installation to reach a terminal state...");



        // The following function will poll for the installation status until the installation reaches a terminal state.

        InstallStatusCode status = PollForTerminalStatus(async () => await libraryApplicationManager.GetLibraryInstallStatusAsync(ADMIN_WORKSPACE_ID, artifactID)).Result;

        Console.WriteLine($@"Installation has terminated with the following status: {status}.");

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}



public async Task<int> UpdateLibraryApplication(ILibraryApplicationManager libraryApplicationManager, string rapFilePathPath)

{

    try

    {

        UpdateLibraryApplicationResponse response;

        using (System.IO.Stream stream = System.IO.File.OpenRead(rapFilePathPath))

        {

            UpdateLibraryApplicationRequest request = new UpdateLibraryApplicationRequest

            {

                FileName = null,

                IgnoreVersion = true,

                RefreshCustomPages = true,

                CreateIfMissing = true

            };



            response = await libraryApplicationManager.UpdateAsync(ADMIN_WORKSPACE_ID, new KeplerStream(stream), request);

            string info = string.Format($"The file located at {rapFilePathPath} was successfully uploaded to the application library.");

            Console.WriteLine(info);

        }



        return response.ApplicationIdentifier.ArtifactID;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}



public async Task<InstallStatusCode> PollForTerminalStatus(Func<Task<GetInstallStatusResponse>> func)

{

    GetInstallStatusResponse result;

    Stopwatch watch = new Stopwatch();

    int refreshInterval = 5;

    bool continuePolling = true;

    watch.Start();



    do

    {

        if (watch.Elapsed.TotalMinutes > DEFAULT_TIMEOUT_VALUE)

        {

            throw new System.Exception($"The terminal status for this application installation could not be obtained. " +

                                       $"Total polling time exceeded timeout value of {DEFAULT_TIMEOUT_VALUE} minutes.");

        }



        result = await func.Invoke();



        switch (result.InstallStatus.Code)

        {

            case InstallStatusCode.Pending:

            case InstallStatusCode.InProgress:

                Console.WriteLine(@"Application installation is pending or in progress.");

                break;



            default:

                continuePolling = false;

                break;

        }



        if (continuePolling)

        {

            await Task.Delay(TimeSpan.FromSeconds(refreshInterval));

        }



    } while (continuePolling);



    watch.Stop();

    return result.InstallStatus.Code;

}
```

Waiting for Multiple Workspace Installations to Complete Copy

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
59
60
61
62
63
64
65
66
67
68
69
70
71
72

public async Task<InstallApplicationResponse> InstallApplicationIntoAllWorkspaces(IApplicationInstallManager applicationInstallManager, int artifactID, bool unlockApps, ApplicationInstallTargetOption mode)

{

    InstallApplicationResponse response = new InstallApplicationResponse();



    try

    {

        InstallApplicationAllRequest request = new InstallApplicationAllRequest

        {

            Mode = mode,

            UnlockApplications = unlockApps

        };



        response = await applicationInstallManager.InstallApplicationAllAsync(ADMIN_WORKSPACE_ID, artifactID, request);



        if (response.Results.Count > 0)

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with ArtifactID {artifactID}.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"Queuing {response.Results.Count} installation(s) for the Library Application with ArtifactID {artifactID} since no workspaces needed an application upgrade.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }



    return response;

}



public async Task PollForTerminalStatuses(Func<Task<GetAllInstallStatusResponse>> func)

{

    GetAllInstallStatusResponse response;

    Stopwatch watch = new Stopwatch();

    int refreshInterval = 10;

    bool continuePolling = true;

    watch.Start();



    do

    {

        if (watch.Elapsed.TotalMinutes > DEFAULT_TIMEOUT_VALUE)

        {

            throw new System.Exception($"The terminal statuses for these application installations could not be obtained. " +

                                $"Total polling time exceeded timeout value of {DEFAULT_TIMEOUT_VALUE} minutes.");

        }



        response = await func.Invoke();



        if (response.Results.Any(x => x.InstallStatus.Code == InstallStatusCode.Pending || x.InstallStatus.Code == InstallStatusCode.InProgress))

        {

            Console.WriteLine(@"One or more application installations are pending or in progress.");

        }

        else

        {

            Console.WriteLine(@"All application installations have ended.");

            continuePolling = false;

        }



        if (continuePolling)

        {

            await Task.Delay(TimeSpan.FromSeconds(refreshInterval));

        }



    } while (continuePolling);



    watch.Stop();

}
```

Test case name Ingestion time Text extraction time

ArgumentException "Workspace ID must be -1" All endpoints require an admin-level context. To resolve this error, ensure that the workspace ID parameter in the path is set to -1.

ArgumentException "You must provide a valid option for the application install target." To resolve this error, ensure that at least one workspace ID is provided in the InstallApplicationAllRequest.

InvalidInputException "The RAP file provided for the Library Application is invalid." When calling Create or Update, ensure that the file sent with the request is a valid Relativity RAP file.

InvalidInputException "The workspace ID is not valid." The workspace ID passed in the request is either invalid or points to a workspace that no longer exists.

InvalidInputException "Global applications cannot be installed into a workspace." The specified application is a global application. Global applications cannot be installed into workspaces if the DeveloperMode instance setting is set to false.

InvalidInputException "You must provide at least one workspace." At least one workspace ID must be provided in the request for the attempted operation.

InvalidInputException "You must provide a valid option for the application install target." The two available application install target options are ForceInstall or UpgradeOnly.

InvalidInputException "There are already pending or in-progress installs for this Library Application." To resolve this error for the attempted operation, ensure that there are no pending or in-progress installations queued for the specified application and workspace.

InvalidInputException "The supplied installation status identifier is out of date for this application." To resolve this error, ensure that the application installation ID passed in the request represent the latest installation of that application.

InvalidInputException "The supplied installation status identifier is not valid for the specified application." The application installation ID passed in the request does not match any installation records associated with the specified application.

InvalidInputException "This value must be greater than zero." For operations that involve pagination, ensure that both the index of the first result and the number of results to return in a single page are set to a value greater than zero.

InvalidOperationException "Unknown value for InstallOutcome ..." If the system is unable to determine whether to proceed or skip queuing an application installation, the system will throw an InvalidOperationException. To resolve this error, ensure that the application has a valid version and origin signature.

NotFoundException "The object does not exist or you do not have permission to access it." As the exception message states, one or more of the objects requested (i.e. a specified workspace, a specified application, a specified application installation ID, a specified validation result ID, etc.) does not exist.

PermissionDeniedException "One or more of the objects requested do not exist or you do not have permission to access them." As the exception message states, either the objects requested (i.e. a specified workspace, a specified application, a specified application installation ID, a specified validation result ID, etc.) do not exist, or the user does not have sufficient permissions to perform the action. The most basic permissions that all users must have include the ViewAdminRepository

On this page

- Application Install (.NET)

- Guidelines for the Application Install API

- Admin-level context

- Actions and pagination

- Permissions

- Sample use cases

- Create a proxy

- Install an application library to specific workspaces

- Install an application library to all workspaces

- Retrieve the installation status of an application

- Retrieve the number of workspaces with an outdated application

- Cancel pending application installations

- Retrieve installation details for an application

- Generate an installation report

- Cancel pending application installations

- Retrieve installation status by workspace

- Supported Condition Fields

- Query for application installations by identifier

- Validate new artifact names

- Query for application installations with additional fields

- Workflow-Based code samples


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
