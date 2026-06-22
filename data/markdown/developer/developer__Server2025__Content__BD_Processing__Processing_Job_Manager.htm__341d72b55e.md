---
title: "Processing Job Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Job_Manager.htm
collection: developer
fetched_at: 2026-06-22T06:27:32+00:00
sha256: c0deb7a2a1b55adc1d1be1ba9185c7c0e50eaa0cb67310a635d14c70c056f3bc
---

Processing Job Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Job Manager

This topic describes the IProcessingJobManager interface, which is used to access the Processing Job Manager service. The Processing Job Manager service includes methods for executing inventory, discovery, and publishing jobs. It also includes a method for canceling any of these jobs for a processing set.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Inventory jobs

The following code illustrates how to run an inventory job by calling the SubmitInventoryJobsAsync() method on the proxy created with the IProcessingJobManager interface.

- Method

- SubmitInventoryJobsAsync: Submits data sources for an inventory job

- Parameters

- <int>workspaceID: ID of workspace that the processing set belongs to.

- <int>processingSetID: ID of processing set

View Sample C# Copy

```text
1
2
3
4
using (IProcessingJobManager proxy = _servicesMgr.CreateProxy<IProcessingJobManager>(ExecutionIdentity.CurrentUser))

{

    await proxy. SubmitInventoryJobsAsync(data.WorkspaceId, processingSetID).ConfigureAwait(false);

}
```

## Discovery jobs

The following code illustrates how to run a discovery job by calling the SubmitDiscoveryJobsAsync() method on the proxy created with the IProcessingJobManager interface.

- Method

- SubmitDiscoveryJobsAsync: Submits data sources for a discovery job

- Parameters

- <int>workspaceID: ID of workspace that the processing set belongs to.

- <int>processingSetID: ID of processing set

View Sample C# Copy

```text
1
2
3
4
using (IProcessingJobManager proxy = _servicesMgr.CreateProxy<IProcessingJobManager>(ExecutionIdentity.CurrentUser))

{

    await proxy. SubmitDiscoveryJobsAsync(data.WorkspaceId, processingSetID).ConfigureAwait(false);

}
```

## Publishing jobs

The following code illustrates how to execute a publishing job by calling the SubmitPublishJobsAsync() method on the proxy created with the IProcessingJobManager interface.

- Method

- SubmitPublishJobsAsync: Submits data sources for a publish job

- Parameters

- <int>workspaceID: ID of workspace that the processing set belongs to.

- <int>processingSetID: ID of processing set

View Sample C# Copy

```text
1
2
3
4
using (IProcessingJobManager proxy = _servicesMgr.CreateProxy<IProcessingJobManager>(ExecutionIdentity.CurrentUser))

{

    await proxy. SubmitPublishJobsAsync(data.WorkspaceId, processingSetID).ConfigureAwait(false);

}
```

## Cancel jobs

You can use the SubmitCancelJobAsync() method to cancel inventory, discovery, and publishing jobs for a specific processing set. The following code illustrates how to execute a cancel job by calling this method on the proxy created with the IProcessingJobManager interface.

- Method

- SubmitCancelJobAsync: Submits a request for canceling a discovery, inventory, or publishing job

- Parameters

- <int>workspaceID: ID of workspace that the processing set belongs to.

- <int>processingSetID: ID of processing set

View Sample C# Copy

```text
1
2
3
4
using (IProcessingJobManager proxy = _servicesMgr.CreateProxy<IProcessingJobManager>(ExecutionIdentity.CurrentUser))

{

    await proxy.SubmitCancelJobAsync(data.WorkspaceId, processingSetID).ConfigureAwait(false);

}
```

On this page

- Processing Job Manager

- Inventory jobs

- Discovery jobs

- Publishing jobs

- Cancel jobs


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
