---
title: "Processing Job Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Job_Manager_REST.htm
collection: developer
fetched_at: 2026-06-22T06:27:33+00:00
sha256: f3845419c8dbc07722b24f0a5c5309f2e60fd5953437395b8fbc5de01e14fae1
---

Processing Job Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Job Manager (REST)

This topic describes the processing-jobs endpoint, which is used to access the Processing Job Manager service. The Processing Job Manager service includes methods for executing inventory, discovery, and publishing jobs. It also includes a method for canceling any of these jobs for a processing set.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Client code sample

You can use the following .NET code as a sample client for submitting a discovery job.

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
public void SubmitDiscoveryJob(int workspaceId, int processingSetID)

{

    string endpoint = $"relativity-processing/v1/workspaces/{workspaceId}/processing-jobs/{processingSetID}/discover";

    HttpResponseMessage response = SendProcessingKeplerPostRequest(endpoint);

    if (!response.IsSuccessStatusCode)

    {

        string genericErrorMessage = "Failed to update external mapping.";

        throw ConstructHttpException(genericErrorMessage, response);

    }

}

private HttpResponseMessage SendProcessingKeplerPostRequest(string apiEndpoint)

{

    string relativityRestApi = ExtensionPointServiceFinder.ServiceUriProvider.RestUri().AbsoluteUri;

    string fullEndpoint = $"{relativityRestApi}/{apiEndpoint}";

    HttpClient client = new HttpClient();

    Credentials credentials = new BearerTokenCredentials(ClaimsPrincipal.Current.Claims.AccessToken());

    string credentialParameter = credentials.GetAuthenticationHeaderValue().Replace("Bearer ", "");

    client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", credentialParameter);

    client.DefaultRequestHeaders.Add(Constants.CSRF_HEADER_NAME, "");

    return SendPostRequest(client, fullEndpoint);

}

private HttpResponseMessage SendPostRequest(HttpClient client, string fullEndpoint)

{

    HttpResponseMessage response = client.PostAsync(fullEndpoint, null).ConfigureAwait(false).GetAwaiter().GetResult();

    if (response.StatusCode == HttpStatusCode.NotFound)

    {

        throw new System.Web.HttpException("Unable to complete POST Processing request, service is not up or unreachable.");

    }

    return response;

}
```

## Submit a discovery job

After you create a processing set and add a data source to it, you can initiate a discovery or processing job. During a job run, the processing engine discovers files in the data source based on the values specified in the processing set. For more information, see Processing on the Relativity Documentation site.

To submit a discovery job, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-jobs/{your processing set Artifact ID}/ discover
```

## Submit a inventory job

Before you run a discovery job, you may want to exclude irrelevant raw files from your data set, such as eliminating NIST file types. You can perform this task by executing an inventory job. You can only run an inventory job on processing sets that haven't been discovered. If you want to apply filtering to your data, set your filters through the Relativity UI after the inventory job completes. For more information, see Inventory on the Relativity Documentation site.

To submit a inventory job, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-jobs/{your processing set Artifact ID}/inventory
```

## Submit a publish job

Use the SubmitPublishJobsAsync endpoint to run publishing jobs. You can provide reviewers in Relativity with access to process data by publishing it to a workspace after it has been discovered. You must run a discovery job on the data before you can run a publishing job on it. For more information, see Publishing files on the Relativity Documentation site.

To submit a publish job, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-jobs/{your processing set Artifact ID}/publish
```

## Cancel job

You can use the cancel endpoint to cancel inventory, discovery, and publishing jobs for a specific processing set.

To cancel a job, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-jobs/{your processing set Artifact ID}/cancel
```

On this page

- Processing Job Manager (REST)

- Client code sample

- Submit a discovery job

- Submit a inventory job

- Submit a publish job

- Cancel job


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
