---
title: "Production Data Source Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Data_Source_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:27:37+00:00
sha256: a41e9793a6c3d3062b782398c0fd67d18eb950237ef8b8ea927956c19b1e4c84
---

Production Data Source Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production Data Source Manager (.NET)

A production data source associates a production with a set of documents returned by a saved search. The save search is used to identify the documents to be produced for distribution to legal counsel. For general information, see Production data source on the Relativity Server 2025 Documentation site.

The Production Data Source Manager API supports the following functionality:

- CRUD operations on data sources

- Retrieving default field values for a data source

You can also use the Production Data Source Manager API through REST. For more information, see Production Data Source Manager (REST) .

See these related pages:

- Production

- Production Manager (.NET)

- Production Placeholder Manager (.NET)

- Re-production Job Manager (REST)

- Production Queue Manager (.NET)

## Fundamentals for the Production Data Source Manager API

The Production Data Source Manager API contains the following methods, classes, and enumerations.

Methods

The Production Data Source Manager API exposes the following methods on the Services.<VersionNumber>.IProductionDataSourceManager interface:

- CreateSingleAsync() method - adds a new data source to Relativity. See Create a data source .

- DeleteSingleAsync() method - removes a data source from Relativity. See Delete a data source .

- GetProductionDataSourceDefaultFieldValues() method - retrieves default field values for a production data source in a specific workspace. See Retrieve default field values for a data source .

- ReadSingleAsync() method - retrieves a data source in a specific workspace. See Read a data source .

- UpdateSingleAsync() method - modifies a data source in a specific workspace. See Create a data source .

Classes and enumerations

- ProductionDataSourceRef - represents a reference to a data source. Its properties include the Artifact ID and data source name.

- ProductionDataSource - represents a Relativity production data source. The ReadSingleAsync() method returns an object of this type.

A ProductionDataSource object doesn't contain the information for a production associated with the data source, such as the Artifact ID or name.

The ProductionDataSource class has the following properties:

- ArtifactID - the Artifact ID of the data source.

- ArtifactTypeID - the Relativity artifact type ID of the data source.

- BurnRedactions - indicates whether to burn redactions when producing image type productions.

- MarkupSet - the markup set used with the data source.

- Name - the user-friendly name of the data source.

- Placeholder - a placeholder used with the data source.

The PlaceholderFileData, PlaceholderFileName, PlaceholderFileSize, and PlaceholderFileID properties are read-only. They are available for data sources associated with already produced productions. Their values are set internally during a production run and can't be altered. During a create or update operations, an attempt to set these values on data source object causes an exception.

- PlaceholderFileData - the raw Base64 encoded data for the placeholder image.

- PlaceholderFileName - the file name of the placeholder image.

- PlaceholderFileSize - the size of the placeholder image.

- PlaceholderFileID - the identifier for the placeholder image file.

- ProductionType - the type of production that applies to this data source. The ProductionType enumeration defines valid values for this property.

- SavedSearch - a saved search containing documents to be produced.

- UseImagePlaceholder - indicates when to use an image placeholder. The UseImagePlaceholderOption enumeration defines valid values for this property.

- UseImagePlaceholderOption enumeration - defines valid values for Use Image Placeholder property as follows:

- 0 - NeverUseImagePlaceholder - never use image placeholder.

- 1 - AlwaysUseImagePlaceholder - always use the image placeholder, even if the image exists.

- 2 - WhenNoImageExists - only use the image placeholder when images don't exist.

For reference content, see Class library reference .

## Create a data source

Use the CreateSingleAsync() method to add a new data source to Relativity. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the data source.

- productionID - the Artifact ID of the production associated with it.

- productionDataSource - a ProductionDataSource object specifying the properties used to create the data source.

The operation returns the Artifact ID of the new data source.

You must have the permissions for working with data sources.

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
44
45
46
47
48
public partial class Example

{

    public async Task CreateDataSource_Example()

    {

        var workspaceID = 11111;            // ArtifactID of Workspace where Data source will be saved

        var productionID = 22222;            // ArtifactID of Production to add the new data source to

        var placeholderID = 33333;            // ArtifactID of Placeholder to use with this data source

        var savedSearchID = 44444;            // ArtifactID of Saved Search containing documents for this data source

        var markupSetID = 55555;            // ArtifactID of Markup Set to use for burning redactions

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password



        var relativityRestUri = @"http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionDataSourceManager productionDataSourceManager = serviceFactory.CreateProxy<IProductionDataSourceManager>())

        {

            try

            {

                ProductionDataSource dataSource = new ProductionDataSource()

                {

                    Name = "Excel Sheets",

                    SavedSearch = new SavedSearchRef(savedSearchID),

                    ProductionType = ProductionType.ImagesAndNatives,

                    UseImagePlaceholder = UseImagePlaceholderOption.WhenNoImageExists,

                    Placeholder = new ProductionPlaceholderRef(placeholderID),

                    BurnRedactions = true,

                    MarkupSet = new MarkupSetRef(markupSetID)

                };

                await productionDataSourceManager.CreateSingleAsync(workspaceID, productionID, dataSource);



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

## Read a data source

Use the ReadSingleAsync() method to retrieve a data source in a specific workspace. Pass the Artifact IDs of the workspace and the data source to this method. You can also pass an optional parameter called withPlaceholderImage to return placeholder images for a data source as follows:

- withPlaceholderImage = true - populates values for read-only placeholder image properties on the data source. The placeholder image is available only for data sources with produced productions.

- withPlaceholderImage = false - doesn't populate any placeholder image properties. The default setting is false.

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

    public async Task ReadDataSource_Example()

    {

        int workspaceID = 11111;            // ArtifactID of Workspace where Data source exists

        int dataSourceID = 22222;            // ArtifactID of DataSource to read

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password



        var relativityRestUri = @"http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionDataSourceManager productionDataSourceManager = serviceFactory.CreateProxy<IProductionDataSourceManager>())

        {

            try

            {

                ProductionDataSource productionDataSource = await productionDataSourceManager.ReadSingleAsync(workspaceID, dataSourceID);



                if (productionDataSource.UseImagePlaceholder == UseImagePlaceholderOption.WhenNoImageExists)

                {

                    // Read the placeholder, etc

                    var placeholderObj = productionDataSource.Placeholder;

                    Console.WriteLine(placeholderObj.Name);

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

## Update a data source

Use the UpdateSingleAsync() method to modify a data source in a specific workspace. Pass the following arguments to this method:

- workspaceID - the Artifact ID of the workspace containing the data source.

- productionID - the Artifact ID of the production associated with it.

- productionDataSource - a ProductionDataSource object specifying the properties that you want to update.

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

    public async Task UpdateDataSource_Example()

    {

        var workspaceID = 11111;            // ArtifactID of Workspace where Data source will be saved

        var productionID = 22222;            // ArtifactID of Production to add the new data source to

        var dataSourceID = 33333;            // ArtifactID of DataSource to update

        var savedSearchID = 44444;            // ArtifactID of Saved Search containing documents for this data source

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password



        var relativityRestUri = @"http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionDataSourceManager productionDataSourceManager = serviceFactory.CreateProxy<IProductionDataSourceManager>())

        {

            try

            {

                // Read in DataSource that you would like to update

                ProductionDataSource productionDataSource = await productionDataSourceManager.ReadSingleAsync(workspaceID, dataSourceID);



                // Change DataSource properties to desired updated values

                productionDataSource.Name = "Updated datasource name";

                productionDataSource.SavedSearch = new SavedSearchRef(savedSearchID);

                await productionDataSourceManager.UpdateSingleAsync(workspaceID, productionID, productionDataSource);



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

## Delete a data source

Use the DeleteSingleAsync() method to remove a data source from Relativity. Pass the Artifact IDs of the workspace and the data source to this method.

You can't delete data sources from productions already produced.

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
public partial class Example

{

    public async Task DeleteDataSource_Example()

    {

        int workspaceID = 11111;            // ArtifactID of Workspace where Data source exists

        int dataSourceID = 22222;            // ArtifactID of DataSource to delete

        var userName = "user@test.com";  // User's login

        var userPassword = "abc123456!";     // User's password



        var relativityRestUri = @"http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionDataSourceManager productionDataSourceManager = serviceFactory.CreateProxy<IProductionDataSourceManager>())

        {

            try

            {

                await productionDataSourceManager.DeleteSingleAsync(workspaceID, dataSourceID);

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

## Retrieve default field values for a data source

Use the GetProductionDataSourceDefaultFieldValues() method to retrieve default field values for a data source. This method doesn't return empty or null fields.

Pass the Artifact ID of the workspace containing the data source to this method.

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

    public async Task GetProductionDataSourceDefaultFieldValues_Example()

    {

        int workspaceId = 12345; // Workspace containing the Production Data Source

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings( new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionDataSourceManager productionDataSourceManager = serviceFactory.CreateProxy<IProductionDataSourceManager>())

        {

            try

            {

                ProductionDataSourceDefaultFieldValues values = await productionDataSourceManager.GetProductionDataSourceDefaultFieldValues(workspaceId);

                Console.WriteLine("Found default Choice Artifact ID for UseImagePlaceholder field: {0}.", values.UseImagePlaceholder.DefaultValue.ID);

                Console.WriteLine("Found default Choice Name for UseImagePlaceholder field: {0}.", values.UseImagePlaceholder.DefaultValue.Name);

                Console.WriteLine("Found UseImagePlaceholder field GUID: {0}.", values.UseImagePlaceholder.Guid);

                Console.WriteLine("Found UseImagePlacholder field Artifact ID: {0}.", values.UseImagePlaceholder.ID);

                Console.WriteLine("Found default value for BurnRedactions field: {0}.", values.BurnRedactions.DefaultValue);

                Console.WriteLine("Found BurnRedactions field GUID: {0}.", values.BurnRedactions.Guid);

                Console.WriteLine("Found BurnRedactions field Artifact ID: {0}.", values.BurnRedactions.ID);

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

On this page

- Production Data Source Manager (.NET)

- Fundamentals for the Production Data Source Manager API

- Create a data source

- Read a data source

- Update a data source

- Delete a data source

- Retrieve default field values for a data source


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
