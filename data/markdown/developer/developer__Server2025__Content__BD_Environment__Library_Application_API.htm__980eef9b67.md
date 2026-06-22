---
title: "Library Application (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Library_Application_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:08+00:00
sha256: 71ce4dcd2e675a15ec6bcf62d468cf66098e43a94efc4da46bfa2750cb2dd7fe
---

Library Application (.NET)

# Library Application (.NET)

The Library Application API allows clients to read application metadata and RAP files from the library, upload new applications, and update or delete existing applications.

You can also interact with the Library Application API through the REST API. See Library Application service .

## Guidelines for the Library Application API

Review the following guidelines for working with the Library Application API.

### Admin-level context

The value for the workspaceID parameter in the path should always be -1. Any other value will return an error.

### Permissions

For all endpoints in the ILibraryApplication API, except ReadAsync, users are required to be system administrators in order to have sufficient permissions.

### Sample use cases

The Library Application API can be used by R1 Operations or ISVs to manage third-party applications in their Relativity instances. For example, a provisioning pipeline may update a new environment with supported third-party applications. Note that this API can be used in conjunction with the Application Install API .

### Endpoints

The Library Application API includes the following endpoints. To set up a proxy to interact with the ILibraryApplication API, call the CreateProxy() method on the object returned by the GetServiceManager() method.

Create a proxy using CreateProxy() Copy

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

using (ILibraryApplicationManager libraryApplicationManager = helper.GetServicesManager().CreateProxy<ILibraryApplicationManager>(ExecutionIdentity.User))

{

    // Add your custom code ...

}
```

## CreateAsync

The following code samples illustrate how to create a library application using the CreateAsync() method of the ILibraryApplicationManager interface.

Create Library Application Copy

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
public async Task Create(ILibraryApplicationManager libraryApplicationManager, string rapFilePath)

{

    try

    {

        using (System.IO.Stream stream = System.IO.File.OpenRead(rapFilePath))

        {

            CreateLibraryApplicationResponse response = await libraryApplicationManager.CreateAsync(ADMIN_WORKSPACE_ID, new KeplerStream(stream));

            string info = string.Format($"The file located at {rapFilePath} is uploading to the application library.");

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

Create Library Application with Package GUID Copy

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
public async Task Create(ILibraryApplicationManager libraryApplicationManager, Guid packageGuid)

{

    try

    {

        CreateLibraryApplicationResponse response = await libraryApplicationManager.CreateAsync(ADMIN_WORKSPACE_ID, packageGuid);

        string info = string.Format($"The package with GUID {packageGuid} is uploading to the application library.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## ReadAsync

The following code samples illustrate how to retrieve the metadata for an application in the library using the ReadAsync() methods of the ILibraryApplicationManager interface.

Read Library Application with ArtifactID Copy

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
public async Task Read(ILibraryApplicationManager libraryApplicationManager, int artifactID)

{

    try

    {

        LibraryApplicationResponse response = await libraryApplicationManager.ReadAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Library Application with ArtifactID {artifactID} successfully read -- Name: {response.FileName}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Read Library Application with GUID Copy

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
public async Task Read(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid)

{

    try

    {

        LibraryApplicationResponse response = await libraryApplicationManager.ReadAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Library Application with Application Guid {applicationGuid} successfully read -- Name: {response.FileName}, Version: {response.Version}");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Read Library Application with ArtifactID and Options Copy

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
public async Task Read(ILibraryApplicationManager libraryApplicationManager, int artifactID, bool includeMetadata, bool includeActions)

{

    try

    {

        LibraryApplicationResponse response = await libraryApplicationManager.ReadAsync(ADMIN_WORKSPACE_ID, artifactID, includeMetadata, includeActions);

        string info = string.Format($"Library Application with ArtifactID {artifactID} successfully read -- Name: {response.FileName}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Read Library Application with GUID and Options Copy

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
public async Task Read(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid, bool includeMetadata, bool includeActions)

{

    try

    {

        LibraryApplicationResponse response = await libraryApplicationManager.ReadAsync(ADMIN_WORKSPACE_ID, applicationGuid, includeMetadata, includeActions);

        string info = string.Format($"Library Application with Application Guid {applicationGuid} successfully read -- Name: {response.FileName}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## ReadAllAsync

The following code samples illustrate how to retrieve the metadata for all applications in the library using the ReadAllAsync() methods of the ILibraryApplicationManager interface.

Read All Library Applications Copy

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
public async Task ReadAll(ILibraryApplicationManager libraryApplicationManager)

{

    try

    {

        List<LibraryApplicationResponse> response = await libraryApplicationManager.ReadAllAsync(ADMIN_WORKSPACE_ID);

        string info = string.Format($"{response.Count} Library Applications were successfully read.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Read All Library Applications with Options Copy

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
public async Task ReadAll(ILibraryApplicationManager libraryApplicationManager, bool includeMetadata, bool includeActions)

{

    try

    {

        List<LibraryApplicationResponse> response = await libraryApplicationManager.ReadAllAsync(ADMIN_WORKSPACE_ID, includeMetadata, includeActions);

        string info = string.Format($"{response.Count} Library Applications were successfully read.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## ReadApplicationContentsAsync

The following code samples illustrate how to retrieve the RAP file for an application in the library using the ReadApplicationContentsAsync() methods of the ILibraryApplicationManager interface.

Read Library Application Contents with ArtifactID Copy

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
public async Task ReadApplicationContents(ILibraryApplicationManager libraryApplicationManager, int artifactID, string filePath)

{

    try

    {

        IKeplerStream response = await libraryApplicationManager.ReadApplicationContentsAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Library Application with ArtifactID {artifactID} successfully retrieved as RAP file.");

        Console.WriteLine(info);

        // Save the returned file stream to disk at provided file path.

        Console.WriteLine(@"Attempting to save the RAP file to disk at the provided filepath.");

        Stream stream = await response.GetStreamAsync();

        using (FileStream fileStream = System.IO.File.Create(filePath))

        {

            stream.Seek(0, SeekOrigin.Begin);

            stream.CopyTo(fileStream);

        }

        Console.WriteLine($@"RAP file successfully saved to disk at the filepath {filePath}.");

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Read Library Application Contents with GUID Copy

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
public async Task ReadApplicationContents(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid, string filePath)

{

    try

    {

        IKeplerStream response = await libraryApplicationManager.ReadApplicationContentsAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Library Application with Application Guid {applicationGuid} successfully retrieved as RAP file.");

        Console.WriteLine(info);

        // Save the returned file stream to disk at provided file path.

        Console.WriteLine(@"Attempting to save the RAP file to disk at the provided filepath.");

        Stream stream = await response.GetStreamAsync();

        using (FileStream fileStream = System.IO.File.Create(filePath))

        {

            stream.Seek(0, SeekOrigin.Begin);

            stream.CopyTo(fileStream);

        }

        Console.WriteLine($@"RAP file successfully saved to disk at the filepath {filePath}.");

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## UpdateAsync

The following code samples illustrate how to update the Application Library using the UpdateAsync() method of the ILibraryApplicationManager interface.

If CreateIfMissing= true and an application with a matching Guid already exists, then it will be updated. If no application exists with the Guid, a new application will be created. If CreateIfMissing= false and an application with a matching Guid already exists, then it will be updated. If no application exists with the Guid, an error will occur.

Update Library Application Copy

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
public async Task Update(ILibraryApplicationManager libraryApplicationManager, string rapFilePath)

{

    try

    {

        using (Stream stream = System.IO.File.OpenRead(rapFilePath))

        {

            UpdateLibraryApplicationRequest request = new UpdateLibraryApplicationRequest

            {

                FileName = null,

                IgnoreVersion = true,

                RefreshCustomPages = true,

                CreateIfMissing = true

            };

            UpdateLibraryApplicationResponse response = await libraryApplicationManager.UpdateAsync(ADMIN_WORKSPACE_ID, new KeplerStream(stream), request);

            string info = string.Format($"The file located at {rapFilePath} is uploading to the application library.");

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

Update Library Application with Package GUID Copy

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
public async Task Update(ILibraryApplicationManager libraryApplicationManager, Guid packageGuid)

{

    try

    {

        UpdateLibraryApplicationRequest request = new UpdateLibraryApplicationRequest

        {

            FileName = null,

            IgnoreVersion = true,

            RefreshCustomPages = true,

            CreateIfMissing = true

        };

        UpdateLibraryApplicationResponse response = await libraryApplicationManager.UpdateAsync(ADMIN_WORKSPACE_ID, packageGuid, request);

        string info = string.Format($"The package with GUID {packageGuid} is uploading to the application library.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## DeleteAsync

The following code samples illustrate how to delete an application from the Application Library using the DeleteAsync() method of the ILibraryApplicationManager interface.

Delete with ArtifactID Copy

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
public async Task Delete(ILibraryApplicationManager libraryApplicationManager, int artifactID)

{

    try

    {

        await libraryApplicationManager.DeleteAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Library Application with ArtifactID {artifactID} is being deleted.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Delete with GUID Copy

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
public async Task Delete(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid)

{

    try

    {

        await libraryApplicationManager.DeleteAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Library Application with Guid {applicationGuid} is being deleted.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## GetLibraryInstallStatusAsync

The following code samples illustrate how to get status information about the most recent install to the Application Library for the specified application using the GetLibraryInstallStatusAsync() method of the ILibraryApplicationManager interface. This endpoint allows clients to query for the status of an update to the application library. A status of Completed indicates the application was created or updated successfully and is ready to be installed into one or more workspaces. A status of Failed indicates a problem with the installation. Once the issue has been resolved, clients can invoke RetryLibraryInstallAsync to retry the library installation.

Get Library Install Status with ArtifactID Copy

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
public async Task GetLibraryInstallStatus(ILibraryApplicationManager libraryApplicationManager, int artifactID)

{

    try

    {

        GetInstallStatusResponse response = await libraryApplicationManager.GetLibraryInstallStatusAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Library Installation record for the Library Application with ArtifactID {artifactID} was successfully read -- " +

                                    $"Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Library Install Status with Application GUID Copy

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
public async Task GetLibraryInstallStatus(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid)

{

    try

    {

        GetInstallStatusResponse response = await libraryApplicationManager.GetLibraryInstallStatusAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Library Installation record for Library Application with GUID {applicationGuid} was successfully read -- " +

                                    $"Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Library Install Status with ArtifactID and Actions Copy

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
public async Task GetLibraryInstallStatus(ILibraryApplicationManager libraryApplicationManager, int artifactID, bool includeActions)

{

    try

    {

        GetInstallStatusResponse response = await libraryApplicationManager.GetLibraryInstallStatusAsync(ADMIN_WORKSPACE_ID, artifactID, includeActions);

        string info = string.Format($"Library Installation record for the Library Application with ArtifactID {artifactID} was successfully read -- " +

                                    $"Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Get Library Install Status with Application Guid and Actions Copy

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
public async Task GetLibraryInstallStatus(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid, bool includeActions)

{

    try

    {

        GetInstallStatusResponse response = await libraryApplicationManager.GetLibraryInstallStatusAsync(ADMIN_WORKSPACE_ID, applicationGuid, includeActions);

        string info = string.Format($"Library Installation record for Library Application with GUID {applicationGuid} was successfully read -- " +

                                    $"Status: {response.InstallStatus.Code}, Version: {response.Version}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## RetryLibraryInstallAsync

This endpoint allows clients to retry a failed library installation for an application. Library installations are initiated when a new application is added to the library or an existing application is updated. Sometimes they can fail, and the application cannot be installed into any workspaces until the failure is resolved. The following code samples illustrate how to retry a failed application install for an application using the RetryLibraryInstallAsync() method of the ILibraryApplicationManager interface.

Retry Library Install by ArtifactID Copy

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
public async Task RetryLibraryInstall(ILibraryApplicationManager libraryApplicationManager, int artifactID)

{

    try

    {

        RetryLibraryInstallResponse response = await libraryApplicationManager.RetryLibraryInstallAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Queuing an installation for the Library Application with ArtifactID {artifactID}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Retry Library Install by GUID Copy

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
public async Task RetryLibraryInstall(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid)

{

    try

    {

        RetryLibraryInstallResponse response = await libraryApplicationManager.RetryLibraryInstallAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Queuing an installation for the Library Application with Guid {applicationGuid}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## CancelLibraryInstallAsync

This endpoint cancels the pending library installation for the specified application. If the installation is already in progress or complete, the operation response will indicate an unsuccessful cancellation with a message explaining why.The following code samples illustrate how to cancel the pending library install for a specified application using the CancelLibraryInstallAsync() method of the ILibraryApplicationManager interface.

Cancel Library Install With Application Artifact ID Copy

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
public async Task CancelLibraryInstall(ILibraryApplicationManager libraryApplicationManager, int artifactID)

{

    try

    {

        CancelLibraryInstallResponse response = await libraryApplicationManager.CancelLibraryInstallAsync(ADMIN_WORKSPACE_ID, artifactID);

        if (response.IsSuccessful)

        {

            string info = string.Format($"The Library Application Installation with application installation ID {response.ApplicationInstallID} was successfully canceled.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"The Library Application Installation could not be canceled: {response.Message}");

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

Cancel Library Install With Application GUID Copy

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
public async Task CancelLibraryInstall(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid)

{

    try

    {

        CancelLibraryInstallResponse response = await libraryApplicationManager.CancelLibraryInstallAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        if (response.IsSuccessful)

        {

            string info = string.Format($"The Library Application Installation with application installation ID {response.ApplicationInstallID} was successfully canceled.");

            Console.WriteLine(info);

        }

        else

        {

            string info = string.Format($"The Library Application Installation could not be canceled: {response.Message}");

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

## UploadPackageAsync

This endpoint uploads a RAP or XML file to a temporary location in Relativity and returns a unique file identifier along with the metadata for the application. If the file is not in a valid format, a validation exception is thrown. This endpoint is used in conjunction with CreateAsync and UpdateAsync to implement workflows where an application's details need to be displayed first for final confirmation before actually installing the application.

Upload a RAP Package Copy

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
public async Task<Guid> UploadPackage(ILibraryApplicationManager libraryApplicationManager, string rapFilePath)

{

    Guid packageGuid = new Guid();

    try

    {

        using (System.IO.Stream stream = System.IO.File.OpenRead(rapFilePath))

        {

            PackageDetailsResponse response = await libraryApplicationManager.UploadPackageAsync(ADMIN_WORKSPACE_ID, new KeplerStream(stream));

            packageGuid = response.PackageGUID;

            string info = string.Format($"The file located at {rapFilePath} has been transferred to the server. " +

                                        $"An application can be installed or updated using the following package GUID: {response.PackageGUID}.");

            Console.WriteLine(info);

        }

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

    return packageGuid;

}
```

## DownloadPackageAsync

This endpoint downloads a RAP or XML file previously uploaded using the UploadPackageAsync endpoint. It takes the unique file identifier as an argument in the URL path and returns a stream of bytes.

Download a RAP Package Copy

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
public async Task<Stream> DownloadPackage(ILibraryApplicationManager libraryApplicationManager, Guid fileIdentifier)

{

    try

    {

        IKeplerStream keplerStream =

            await libraryApplicationManager.DownloadPackageAsync(ADMIN_WORKSPACE_ID, fileIdentifier);

        return await keplerStream.GetStreamAsync();

    }

    catch (Relativity.Services.Exceptions.NotFoundException)

    {

        Console.WriteLine($"The file with identifier {fileIdentifier} does not exist.");

        throw;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

        throw;

    }

}
```

## DeletePackageAsync

This endpoint allows clients to delete an RAP file that has been uploaded to a temporary storage location.

Delete Package Copy

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
public async Task DeletePackage(ILibraryApplicationManager libraryApplicationManager, Guid packageGuid)

{

    try

    {

        await libraryApplicationManager.DeletePackageAsync(ADMIN_WORKSPACE_ID, packageGuid);

        string info = string.Format($"The file with identifier {packageGuid} has been deleted.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## GetApplicationHostingStatusAsync

This endpoint retrieves the hosting status of a specified application and indicates the status of the application's hosted components, such as custom pages. An example use case of this endpoint is determining if the application's custom page has been redeployed and is healthy.

GetApplicationHostingStatus With Application ID Copy

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
public async Task GetApplicationHostingStatus(ILibraryApplicationManager libraryApplicationManager, int applicationID)

{

    try

    {

        ApplicationHostingStatusResponse response = await libraryApplicationManager.GetApplicationHostingStatusAsync(ADMIN_WORKSPACE_ID, applicationID);

        string info = string.Format($"The application with identifier {applicationID} has an overall status of {response.State} and returns the following HTTPStatusCode for its custom page: {response.CustomPages[0].StatusCode}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

GetApplicationHostingStatus With Application GUID Copy

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
public async Task GetApplicationHostingStatus(ILibraryApplicationManager libraryApplicationManager, Guid applicationGuid)

{

    try

    {

        ApplicationHostingStatusResponse response = await libraryApplicationManager.GetApplicationHostingStatusAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"The application with identifier {applicationGuid} has an overall status of {response.State} and returns the following HTTPStatusCode for its custom page: {response.CustomPages[0].StatusCode}.");

        Console.WriteLine(info);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## Workflow-Based code samples

For more information on how the Application Install API and Library Application API endpoints can be used together, see Workflow-Based code samples.

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
