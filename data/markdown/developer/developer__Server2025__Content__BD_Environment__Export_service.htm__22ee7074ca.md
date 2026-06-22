---
title: "Export (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Export_service.htm
collection: developer
fetched_at: 2026-06-22T06:26:09+00:00
sha256: a3a4be7c00bc32f7bd091152021d1cea659dc75a837d99b3fc73a2a341bfd522
---

Export (REST)

# Export (REST)

Through the REST API, the Export API allows clients to export applications as a RAP file or schema file.

## Client code sample

To use the Export service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.REST/API/relativity-application/v1/workspaces/{workspaceID}/applications/
```

Code sample for the base URL Copy

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
public async Task<IKeplerStream> ExportApplication(int applicationID, int workspaceID, string hostUrl, string adminUsername, string adminPassword)

{

    IKeplerStream response = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", string.Empty);

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes($"{adminUsername}:{adminPassword}")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri(hostUrl);

        string url = $"/Relativity.REST/API/relativity-application/v1/workspaces/{workspaceID}/applications/{applicationID}/rapfile";

        System.Net.Http.HttpResponseMessage httpResponse = await client.GetAsync(url);

        httpResponse.EnsureSuccessStatusCode();

        string content = await httpResponse.Content.ReadAsStringAsync();

        response = JsonConvert.DeserializeObject<IKeplerStream>(content);

    }

    return response;

}
```

## ExportAsync

You must be a System Admin to call this endpoint.

To export an application as a RAP file, send a GET request for one of the following URLs:

Copy

```text
1
2
https://<host>/Relativity.REST/API/relativity-application/v1/workspaces/{workspaceID:int}/applications/{applicationID:int}/rapfile

https://<host>/Relativity.REST/API/relativity-application/v1/workspaces/{workspaceID:int}/applications/{applicationGUID:guid}/rapfile
```

The raw JSON response will not be human-readable.

## ExportSchemaAsync

You must be a System Admin to call this endpoint.

To export an application as a RAP file, send a GET request for one of the following URLs:

Copy

```text
1
2
https://<host>/Relativity.REST/API/relativity-application/v1/workspaces/{workspaceID:int}/applications/{applicationID:int}/schema

https://<host>/Relativity.REST/API/relativity-application/v1/workspaces/{workspaceID:int}/applications/{applicationGUID:guid}/schema
```

The raw JSON response will not be human-readable.
