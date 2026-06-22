---
title: "ARM (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_ARM/ARM_API.htm
collection: developer
fetched_at: 2026-06-22T06:25:26+00:00
sha256: 46039dff9057dd2afd010daa28107eaf7f78362ae5e84c4954e802f2c55c38a0
---

ARM (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# ARM (.NET)

The ARM API supports multiple operations required to archive, restore, and move Relativity workspace data. You can also use to view information on currently running ARM jobs or to list available workspaces or ARM archives. For example, you could use this service to populate a custom dialog in your application with scheduled ARM archive jobs.

You can also interact with the ARM API through the REST API. See ARM API service .

For more information on the ARM application, see Arm Overview on the Relativity documentation site.

## Fundamentals for the ARM API

Review the following guidelines for working with the ARM API.

### Sample use cases

A typical use case would be building a custom ARM client or automating the creation or execution of ARM jobs.

A typical workflow requires these steps:

- Create ARM job (Archive, Restore, Database Restore, or Move)

- Run the job

- Read job status to get information about the job execution and whether it has completed.

## Create

The following code sample illustrates how to create the service proxy factory, which is then used to create an ARM API proxy. This proxy can also be created using the IHelper interface from the Relativity API Helper library.

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
// This method is only to illustrate one way to create the service proxy factory, which is then used to create an ARM API proxy.

// This proxy could also be created using the IHelper interface from the Relativity API Helper library.

public void InitializeServiceFactory() {

  String restServerAddress = "http://localhost/relativity.rest/api";

  Uri keplerUri = new Uri(restServerAddress);

  Relativity.Services.ServiceProxy.ServiceFactorySettings settings = new Relativity.Services.ServiceProxy.ServiceFactorySettings(

    keplerUri, new Relativity.Services.ServiceProxy.UsernamePasswordCredentials("ExampleUsername.com", "ExamplePassword1!"));

  _serviceFactory = new Relativity.Services.ServiceProxy.ServiceFactory(settings);

}

// This method creates an Archive job and returns the ID of the new job.

public async Task<int> CreateARMArchiveJob(int workspaceId, string archivePath) {

  using (var archiveJobManager = _serviceFactory.CreateProxy<IArmArchiveJobManager>()) {

    ArchiveJobRequest request = new ArchiveJobRequest() {

      WorkspaceID = workspaceId,

        ArchiveDirectory = archivePath

    };

    return await archiveJobManager.CreateAsync(request);

  }

}
```

## Run

The following code sample illustrates how to run the job in the IArmJobStatusManager interface.

Copy

```text
// This method runs the job.

public async Task RunARMJob(int jobId) {

    using (var armJobActionManager = _serviceFactory.CreateProxy<IArmJobActionManager>()) {

        await armJobActionManager.RunAsync(jobId);

    }

}
```

## Read

The following code sample illustrates how to read the job status and exits when a job has completed successfully or with errors using ProcessARMJob in the IArmJobStatusManager interface.

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
// This method reads job status and exits when job has completed successfully or with errors.

public async Task ProcessARMJob(int jobId) {

  using (var proxy = _serviceFactory.CreateProxy<IArmJobStatusManager>()) {

    ArmJobStatusResponse response;

    while (response.JobState != JobState.Complete) {

      response = await proxy.ReadAsync(jobId);

      if (response.JobState == JobState.Errored) {

        // handle error

        // ...

        break;

      }

      Task.Delay(5000); // wait some time, 5 seconds in this case

    }

  }

}
```

On this page

- ARM (.NET)

- Fundamentals for the ARM API

- Sample use cases

- Create

- Run

- Read


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
