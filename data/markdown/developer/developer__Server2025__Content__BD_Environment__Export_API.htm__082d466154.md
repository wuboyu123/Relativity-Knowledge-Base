---
title: "Export (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Export_API.htm
collection: developer
fetched_at: 2026-06-22T06:26:07+00:00
sha256: b199db94f37689ebcfb36c785d78b86202b606316e178bb0e07b10f434ae8752
---

Export (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Export (.NET)

The Export API allows clients to export applications as a RAP file or schema file.

You can also interact with the Export API through the REST API. See Export service .

## Guidelines for the Export API

Review the following guidelines for working with the Export API.

### Permissions

For all endpoints in the API, users are required to be system administrators in order to have sufficient permissions.

## ExportAsync

Exports the application from the workspace as a RAP file. If the application is unlocked, it will be locked. The fourth digit of the application's Version number will be auto-incremented with each export if the application is unlocked or the application schema has been modified. The Schema Version will be auto-incremented only if schema changes were made.

Export Application RAP file by ArtifactID Copy

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
public async Task ExportApplicationRapByArtifactID(IApplicationManager applicationManager, int artifactID, string filePath)

{

    try

    {

        IKeplerStream response = await applicationManager.ExportAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Application with Artifact ID {artifactID} successfully exported as RAP file.");

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

Export Application RAP file by Guid Copy

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
public async Task ExportApplicationRapByGuid(IApplicationManager applicationManager, Guid applicationGuid, string filePath)

{

    try

    {

        IKeplerStream response = await applicationManager.ExportAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Application with Application Guid {applicationGuid} successfully exported as RAP file.");

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

## ExportSchemaAsync

Exports the application schema from the workspace as an XML file.If the application is unlocked, it will be locked. The fourth digit of the application's Version number will be auto-incremented with each export if the application is unlocked or the application schema has been modified. The Schema Version will be auto-incremented only if schema changes were made.

Export Application Schema file by ArtifactID Copy

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
public async Task ExportApplicationSchemaByArtifactID(IApplicationManager applicationManager, int artifactID, string filePath)

{

    try

    {

        IKeplerStream response = await applicationManager.ExportSchemaAsync(ADMIN_WORKSPACE_ID, artifactID);

        string info = string.Format($"Application with Artifact ID {artifactID} successfully exported as Schema file.");

        Console.WriteLine(info);



        // Save the returned file stream to disk at provided file path.

        Console.WriteLine(@"Attempting to save the Schema file to disk at the provided filepath.");

        Stream stream = await response.GetStreamAsync();

        using (FileStream fileStream = System.IO.File.Create(filePath))

        {

            stream.Seek(0, SeekOrigin.Begin);

            stream.CopyTo(fileStream);

        }

        Console.WriteLine($@"Schema file successfully saved to disk at the filepath {filePath}.");

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Export Application Schema File by Guid Copy

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
public async Task ExportApplicationSchemaByGuid(IApplicationManager applicationManager, Guid applicationGuid, string filePath)

{

    try

    {

        IKeplerStream response = await applicationManager.ExportSchemaAsync(ADMIN_WORKSPACE_ID, applicationGuid);

        string info = string.Format($"Application with Application Guid {applicationGuid} successfully exported as Schema file.");

        Console.WriteLine(info);



        // Save the returned file stream to disk at provided file path.

        Console.WriteLine(@"Attempting to save the Schema file to disk at the provided filepath.");

        Stream stream = await response.GetStreamAsync();

        using (FileStream fileStream = System.IO.File.Create(filePath))

        {

            stream.Seek(0, SeekOrigin.Begin);

            stream.CopyTo(fileStream);

        }

        Console.WriteLine($@"Schema file successfully saved to disk at the filepath {filePath}.");

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

On this page

- Export (.NET)

- Guidelines for the Export API

- Permissions

- ExportAsync

- ExportSchemaAsync


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
