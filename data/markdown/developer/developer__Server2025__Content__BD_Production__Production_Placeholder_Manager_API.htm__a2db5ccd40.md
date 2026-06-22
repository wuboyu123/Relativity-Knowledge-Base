---
title: "Production Placeholder Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Placeholder_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:27:44+00:00
sha256: 6a80027588012e29036fdc65544f89601874109d1efdad6d248fc9efea56f52b
---

Production Placeholder Manager (.NET)

# Production Placeholder Manager (.NET)

In Relativity, a placeholder is an image or custom text that you can add to a production. It may indicate that content is withheld due to privilege or it may contain additional information about a document. For general information, see Production placeholders on the Relativity Documentation site.

The Production Placeholder Manager API supports the following functionality:

- CRUD operations on placeholders

- Retrieving default field values for a placeholder

You can also use the Production Placeholder Manager API through REST. For more information, see Production Placeholder Manager (REST) .

See these related pages:

- Production

- Production Manager (.NET)

- Production Data Source Manager (.NET)

- Re-production Job Manager (.NET)

- Production Queue Manager (.NET)

## Fundamentals for the Production Placeholder Manager API

The Production Placeholder Manager API contains the following methods, classes, and enumerations.

Methods

The Production Placeholder Manager API exposes the following methods on the Services.<VersioNumber>.IProductionPlaceholderManager interface:

- CreateSingleAsync() method - adds a new image or custom placeholder to a specific workspace. See Create a placeholder .

- DeleteSingleAsync() method - removes a placeholder from Relativity. See Delete a placeholder .

- GetProductionPlaceholderDefaultFieldValues() method - retrieves default field values for a production placeholder in a workspace. See Retrieve default field values for a placeholder .

- ReadSingleAsync() method - retrieves a production placeholder. See Read a placeholder .

- UpdateSingleAsync() method - modifies an image placeholder or a custom placeholder in a specific workspace. See Update a placeholder .

Classes and enumerations

The Production Placeholder Manager API includes multiple classes and enumerations. The following list highlights key features:

- ProductionPlaceholderRef - represents a reference to a placeholder. The properties on a ProductionRef object include the Artifact ID and placeholder name.

- ProductionPlaceholder - represents a Relativity production placeholder. The ReadSingleAsync() method returns an object of this type. It has the following properties:

- ArtifactID - the artifact ID of the placeholder.

- ArtifactTypeID - the Relativity artifact type ID of the placeholder.

- CustomText - the custom HTML text for the placeholder.

- FileData - the contents of the placeholder image.

- FileID - the internal identifier of the placeholder preview image.

- Filename - the file name of the placeholder image.

- FileSize - the size of the uploaded file.

- Name - a user-friendly name for the placeholder.

- PlaceholderType - the type of the placeholder. The PlaceholderType enumeration defined valid values for this property.

- PlaceholderType - the enumeration defines valid values for placeholder type. Values include:

- 0 - Custom - indicates custom text with formatting.

- 1 - Image - indicates image files. Relativity supports TIF, JPEG, PNG, BMP, and GIF files.

For reference content, see Class library reference .

## Create a placeholder

Use the CreateSingleAsync() method to add an image or custom placeholder to a specific workspace. When you create a production placeholder, you can upload image data for the placeholder as the FileData property, or use HTML-formatted text as the CustomText property. These inputs are converted to a JPG and are stored in a file type field on the ProductionPlaceholder object.

You must have the permissions for working with placeholders.

Pass the following arguments to the CreateSingleAsync() method:

- workspaceID - the Artifact ID of the workspace containing the placeholder.

- placeholder - a ProductionPlaceholder object specifying the properties for the placeholder. Use these guidelines to specify an image or custom placeholder:

- If you set the PlaceholderType property to Custom, you must also set the CustomText property. You can create a blank placeholder by setting the CustomText property to an empty string.

View additional information about the CustomText property

Specify custom text with HTML formatting. You can also add any document field or Bates number field to stamp on the placeholder. The field name is inserted into your custom placeholder. When you start the production, the field name dynamically updates per document. For example, [ControlNumber] updates with the control number field for the document the placeholder corresponds to. Custom type placeholders support document fields with the field name surrounded by brackets: [Document Field Name]. To include a square bracket as part of the placeholder text, you must escape the square bracket with a backslash: \[Document Field Name\].

- If you set the PlaceholderType property to Image, you must also set the FileData and Filename properties. The FileData property must contain raw Base64 encoded image data.

This method returns the Artifact ID of the new placeholder.

View code sample for creating an image placeholder Copy

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
public partial class Example

{

    public async Task CreateImagePlaceholder_Example()

    {

        var workspaceID = 11111;                // ArtifactID of Workspace where Placeholder exists

        var userName = "user@test.com";      // User's login

        var userPassword = "abc123456!";         // User's password

        var relativityRestUri = @"http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        string fileLocation = @"\\servername\share\Placeholder.jpg";

        string filename = Path.GetFileName(fileLocation);

        byte[] fileData = ReadFully(fileLocation);

        using (IProductionPlaceholderManager productionPlaceholderManager = serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                ProductionPlaceholder placeholder = new ProductionPlaceholder()

                {

                    Name = "Placeholder for excel sheets",

                    PlaceholderType = PlaceholderType.Image,

                    Filename = filename,

                    FileData = fileData

                };

                placeholder.ArtifactID = await productionPlaceholderManager.CreateSingleAsync(workspaceID, placeholder);

            }

            catch (ValidationException e)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", e.Message);

            }

            catch (ServiceException es)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", es.Message);

            }

        }

    }

    private byte[] ReadFully(string fileLocation)

    {

        MemoryStream ms = new MemoryStream();

        byte[] buffer = new byte[16 * 1024];

        int read;

        using (FileStream reader = new FileStream(fileLocation, FileMode.Open))

        {

            while ((read = reader.Read(buffer, 0, buffer.Length)) > 0)

            {

                ms.Write(buffer, 0, read);

            }

        }

        return ms.ToArray();

    }

}
```

View code sample for creating a custom placeholder Copy

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
public partial class Example

{

    public async Task CreateCustomPlaceholder_Example()

    {

        var workspaceID = 11111; // ArtifactID of Workspace where Placeholder exists

        var userName = "user@test.com"; // User's login

        var userPassword = "abc123456!"; // User's password

        var relativityRestUri = @"http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionPlaceholderManager productionPlaceholderManager =

            serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                ProductionPlaceholder placeholder = new ProductionPlaceholder()

                {

                    Name = "Placeholder for excel sheets",

                    PlaceholderType = PlaceholderType.Custom,

                    CustomText = "This is an excel sheet."

                };

                placeholder.ArtifactID =

                    await productionPlaceholderManager.CreateSingleAsync(workspaceID, placeholder);

            }

            catch (ValidationException e)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", e.Message);

            }

            catch (ServiceException es)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", es.Message);

            }

        }

    }

}
```

## Read a placeholder

Use the ReadSingleAsync() method to retrieve a production placeholder. Pass the Artifact IDs of the workspace and the placeholder to this method.

This method returns a ProductionPlaceholder object. You can inspect this object for information such as the PlaceholderType property, which indicates whether the the placeholder is an image or custom text.

View code sample Copy

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
public partial class Example

{

    public async Task ReadPlaceholder_Example()

    {

        int workspaceID = 11111;            // ArtifactID of Workspace where Placeholder exists

        int placeholderID = 22222;            // ArtifactID of Placeholder to read

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password

        var relativityRestUri = @"http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionPlaceholderManager productionPlaceholderManager = serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                ProductionPlaceholder productionPlaceholder = await productionPlaceholderManager.ReadSingleAsync(workspaceID, placeholderID);

                if (productionPlaceholder.PlaceholderType == PlaceholderType.Custom)

                {

                    // Read the custom text

                    var customText = productionPlaceholder.CustomText;

                    Console.WriteLine(customText);

                }

            }

            catch (ValidationException e)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", e.Message);

            }

            catch (ServiceException es)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", es.Message);

            }

        }

    }

}
```

## Update a placeholder

Use the UpdateSingleAsync() method to modify an image placeholder or a custom placeholder in a specific workspace.

You can't modify the PlaceholderType property for an existing placeholder.

View code sample for updating an image placeholder Copy

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
public partial class Example

{

    public async Task UpdateImagePlaceholder_Example()

    {

        var workspaceID = 11111;            // ArtifactID of Workspace where Placeholder exists

        int placeholderID = 33333;            // ArtifactID of Image Placeholder to update

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password

        var relativityRestUri = @"http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        string fileLocation = @"\\servername\share\Placeholder.jpg";

        string filename = Path.GetFileName(fileLocation);

        byte[] fileData = ReadFully(fileLocation);

        using (IProductionPlaceholderManager productionPlaceholderManager = serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                // Read the placeholder you would like to update, so we get the fully filled object

                ProductionPlaceholder placeholder = await productionPlaceholderManager.ReadSingleAsync(workspaceID, placeholderID);

                // Update the placeholder (change the name, change uploaded image)

                fileLocation = @"\\servername\share\ReplacementPlaceholder.jpg";

                filename = Path.GetFileName(fileLocation);

                fileData = ReadFully(fileLocation);

                placeholder.Name = "Placeholder for excel sheets - No redactions";

                placeholder.Filename = filename;

                placeholder.FileData = fileData;

                await productionPlaceholderManager.UpdateSingleAsync(workspaceID, placeholder);

            }

            catch (ValidationException e)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", e.Message);

            }

            catch (ServiceException es)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", es.Message);

            }

        }

    }

    private byte[] ReadFully(string fileLocation)

    {

        MemoryStream ms = new MemoryStream();

        byte[] buffer = new byte[16 * 1024];

        int read;

        using (FileStream reader = new FileStream(fileLocation, FileMode.Open))

        {

            while ((read = reader.Read(buffer, 0, buffer.Length)) > 0)

            {

                ms.Write(buffer, 0, read);

            }

        }

        return ms.ToArray();

    }

}
```

View code sample for updating a custom placeholder Copy

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
public partial class Example

{

    public async Task UpdateCustomPlaceholder_Example()

    {

        var workspaceID = 11111;               // ArtifactID of Workspace where Placeholder exists

        int placeholderID = 22222;               // ArtifactID of Custom Placeholder to update

        var userName = "user@test.com";     // User's login

        var userPassword = "abc123456!";        // User's password

        var relativityRestUri = @"http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionPlaceholderManager productionPlaceholderManager = serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                // Read the placeholder you would like to update, so we get the fully filled object

                ProductionPlaceholder placeholder = await productionPlaceholderManager.ReadSingleAsync(workspaceID, placeholderID);

                // Update the placeholder (change the name, change the custom text)

                placeholder.Name = "Placeholder for excel sheets - No redactions";

                placeholder.CustomText = "<P><B>This is an excel sheet for document: [Control Number].</B></P>";

                await productionPlaceholderManager.UpdateSingleAsync(workspaceID, placeholder);

            }

            catch (ValidationException e)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", e.Message);

            }

            catch (ServiceException es)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", es.Message);

            }

        }

    }

}
```

## Delete a placeholder

Use the DeleteSingleAsync() method to remove a placeholder from Relativity. Pass the Artifact IDs of the workspace and the placeholder to this method.

You can delete placeholders that are currently in use by data sources.

View code sample Copy

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
public partial class Example

{

    public async Task DeletePlaceholder_Example()

    {

        int workspaceID = 11111;            // ArtifactID of Workspace where Placeholder exists

        int placeholderID = 22222;            // ArtifactID of Placeholder to delete

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password

        var relativityRestUri = @"http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionPlaceholderManager productionPlaceholderManager = serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                await productionPlaceholderManager.DeleteSingleAsync(workspaceID, placeholderID);

                // Delete is successful if exception was not thrown

            }

            catch (ValidationException e)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", e.Message);

            }

            catch (ServiceException es)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", es.Message);

            }

        }

    }

}
```

## Retrieve default field values for a placeholder

Use the GetProductionPlaceholderDefaultFieldValues() method to retrieve default field values for a production placeholder in a specific workspace. This method doesn't return empty or null fields.

Pass the Artifact ID of the workspace containing the placeholder to this method.

View code sample Copy

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
public partial class Example

{

    public async Task GetProductionPlaceholderDefaultFieldValues_Example()

    {

        int workspaceId = 12345; // Workspace containing the Production Placeholder

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password

        var relativityServicesUri = "http://localhost/relativity.services";

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityServicesUri),

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionPlaceholderManager productionPlaceholderManager = serviceFactory.CreateProxy<IProductionPlaceholderManager>())

        {

            try

            {

                ProductionPlaceholderDefaultFieldValues values = await productionPlaceholderManager.GetProductionPlaceholderDefaultFieldValues(workspaceId);

                Console.WriteLine("Found default Choice Artifact ID for Type field: {0}.", values.Type.DefaultValue.ID);

                Console.WriteLine("Found default Choice Name for Type field: {0}.", values.Type.DefaultValue.Name);

                Console.WriteLine("Found Type field GUID: {0}.", values.Type.Guid);

                Console.WriteLine("Found Type field Artifact ID: {0}.", values.Type.ID);

            }

            catch (ValidationException ex)

            {

                // Log validation exception details

                Console.WriteLine("There were validation errors: {0}", ex.Message);

            }

            catch (ServiceException ex)

            {

                // Log service exception details

                Console.WriteLine("There were errors: {0}", ex.Message);

            }

        }

    }

}
```
