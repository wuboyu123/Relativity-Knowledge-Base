---
title: "Production Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:47+00:00
sha256: 4d557ad88a31389e79a29c71d896847c18784f2dc6d5b0055ac211b62e36f417
---

Production Manager (.NET)

# Production Manager (.NET)

A production is a group of non-privileged documents delivered to opposing counsel as part of a legal proceeding. Relativity uses a production set to define the markup set for redactions, numbering, and other settings applied to the documents during a production job. For general information, see Production and Production sets on the Relativity Server 2025 Documentation site.

The Production Manager API exposes methods that provide the following functionality for productions:

- Creating, deleting, staging, running, and performing other tasks with production sets

- Retrieving default fields on a production

- Setting and removing production restrictions defined in a workspace

- Retrieving information about production jobs, such as status, progress, and production results

- Retrieving information about production errors and document conflicts

- Retrieving, running, staging, and canceling re-production jobs

You can also use the Production Manager API through REST. For more information, see Production Manager (REST) .

See these related pages:

- Production

- Production Data Source Manager (.NET)

- Production Placeholder Manager (.NET)

- Re-production Job Manager (REST)

- Production Queue Manager (.NET)

## Fundamentals for the Production Manager API

The Production Manager API contains the multiple methods used for manipulating productions as described in this section.

Methods

- CancelReproductionJobAsync() method - cancels jobs for a re-production. This method cancels all production jobs for the re-production. See Cancel jobs for a re-production .

- CreateSingleAsync() method - adds a new production set to a Relativity workspace. See Create a production set .

- DeleteDocumentConflictsAsync() method - removes documents from a production that conflict with the restrictions set on a workspace. See Remove documents conflicting with production restrictions .

- DeleteSingleAsync() method - removes a production set from Relativity. See Delete a production set .

- DocumentConflictsAsync() method - retrieves documents conflicting with the production restrictions defined for the workspace. See Retrieve documents conflicting with production restrictions .

- GetAllAsync() method - retrieves all productions in a workspace. See Retrieve all productions in a workspace .

- GetBrandingErrorsAsync() method - retrieves a specified number of branding errors for a production. See Retrieve branding errors for a production .

- GetJobStatus() method - retrieves the job status of a production. See Retrieve the job status of a production .

- GetProducedProductionsFromDocumentsAsync() method - retrieves produced productions for documents by using document IDs or a mass operation token. See Retrieve produced productions for documents .

- GetProductionDefaultFieldValues() method - retrieves default field values for a production. See Retrieve default field values for a production .

- GetProductionImagesAsync() method - retrieves information about produced image files. See Retrieve results for produced image files .

- GetProductionImagesTokenAsync() method - retrieves a unique token for paging through images. See Retrieve a token for paging through images .

- GetProductionRestrictionAsync() method - retrieves the Artifact ID of a save search used for production restrictions in a workspace. See Retrieve the ID of a save search used for production restrictions .

- GetProductionsEligibleForReproductionAsync() method - retrieves productions eligible for re-production based on the production type. See Retrieve productions eligible for re-production .

- GetReproductionsAsync() method - retrieves re-productions performed for a specific production. See Retrieve re-productions for a specific production .

- MassStageAndRunAsync() method - stages and runs multiple productions in a workspace. See Stage and run multiple productions .

- MassStageAndRunProductionsAsync() method - stages and runs a re-production job, and retrieves job details. See Stage and run a re-production job .

- ProductionRunCheckAsync() method - retrieves document conflicts, production errors, and information about whether the production can be run. See Retrieve conflicts, errors, and other production information .

- ProgressAsync() method - retrieves progress details for a production. See Retrieve progress details for a production .

- ReadSingleAsync() method - retrieves a production set. See Retrieve a production set .

- RerunProductionAsync() method - re-runs a production. See Re-run a production .

- RunProductionAsync() method - runs a production job. See Run a production job .

- SetProductionRestrictionsAsync() method - adds a production restriction to a workspace. See Set production restrictions on a workspace .

- StageProductionAsync() method - stages a production. See Stage a production .

- StagingErrorsAsync() method - retrieves staging errors and duplicate documents for a production. See Retrieve staging errors for a production .

## Production sets and jobs

This section contains code samples that illustrate how to create, stage, run, and perform other tasks with productions.

### Create a production set

Use the CreateSingleAsync() method to add a new production set to a Relativity workspace.

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
public partial class Example

{

    public async Task CreatePageLevelProduction_Example()

    {

        int workspaceId = 12345;                   // ArtifactID of Workspace where Production will be saved

        var userName = "user@test.com";         // User's login

        var userPassword = "abc123456!";            // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userName, userPassword);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                // Construct the production object that you want to create

                var production = new Production

                {

                    Name = "Page Level Production Sample",

                    Details = new Services.Interfaces.V1.DTOs.ProductionDetails

                    {

                        DateProduced = new DateTime(2017, 10, 22),

                        EmailRecipients = "pagelevelnumber@relativity.com; emosewa@gmail.com",

                        ScaleBrandingFont = true,

                        BrandingFontSize = 25,

                        PlaceholderImageFormat = PlaceholderImageFormat.Tiff

                    },

                    Numbering = new PageLevelNumbering

                    {

                        BatesPrefix = "ADBE",

                        BatesSuffix = "DRAFT",

                        BatesStartNumber = 20,

                        NumberOfDigitsForDocumentNumbering = 5

                    },

                    Footers = new ProductionFooters

                    {

                        Left = new HeaderFooter("Left Footer")

                        {

                            Type = HeaderFooterType.FreeText,

                            FreeText = "This is confidential page"

                        }

                    },

                    SortOrder = new List<Sort>()

                {

                    new Sort()

                    {

                        Direction = SortEnum.Ascending,

                        FieldIdentifier = new Shared.V1.Models.FieldRef("First Sort Field"),

                        Order = 0

                    },

                    new Sort()

                    {

                        Direction = SortEnum.Descending,

                        FieldIdentifier = new Shared.V1.Models.FieldRef("Second Sort Field"),

                        Order = 1

                    }

                },

                    Keywords = "PageLevel, Complete Setting",

                    Notes = "Page level numbering production"

                };

                // Save the production into the specified workspace

                int productionId = await productionManager.CreateSingleAsync(workspaceId, production);

                Console.WriteLine("The created production Id is {0}", productionId);

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

### Retrieve a production set

Use the ReadSingleAsync() method to retrieve a production set.

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

    public async Task ReadProduction_Example()

    {

        int workspaceId = 12345;            // Workspace Production exists in

        int productionId = 11111;            // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                Production production = await productionManager.ReadSingleAsync(workspaceId, productionId);

                var productionStatus = production.ProductionMetadata.Status;

                if (productionStatus == ProductionStatus.New)

                {

                    // Do something, like stage this production

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

### Delete a production set

Use the DeleteSingleAsync() method to remove a production set from Relativity.

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

    public async Task DeleteProduction_Example()

    {

        int workspaceId = 12345;         // Workspace Production exists in

        int productionId = 11111;         // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                await productionManager.DeleteSingleAsync(workspaceId, productionId);

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

### Stage a production

Use the StageProductionAsync() method to stage a production.

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
public partial class Example

{

    public async Task StageProduction_Example()

    {

        int workspaceId = 12345; // Workspace Production exists in

        int productionId = 11111; // Production's ArtifactID

        var userEmail = "user@test.com"; // User's login

        var password = "abc123456!"; // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                ProductionJobResult result = await productionManager.StageProductionAsync(workspaceId, productionId);

                bool wasJobCreated = result.WasJobCreated;

                if (!wasJobCreated)

                {

                    Console.WriteLine(result.Errors);

                    Console.WriteLine(result.Warnings);

                    Console.WriteLine(result.Messages);

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

    public async Task StageAndRunProduction_Example()

    {

        int workspaceId = 12345; // Workspace Production exists in

        int productionId = 11111; // Production's ArtifactID

        var userEmail = "user@test.com"; // User's login

        var password = "abc123456!"; // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                //Pass automatically run as true to have production run automatically after staging completed

                ProductionJobResult result = await productionManager.StageProductionAsync(workspaceId, productionId, true);

                bool wasJobCreated = result.WasJobCreated;

                if (!wasJobCreated)

                {

                    Console.WriteLine(result.Errors);

                    Console.WriteLine(result.Warnings);

                    Console.WriteLine(result.Messages);

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

### Run a production job

Use the RunProductionAsync() method to run a production job.

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
49
50
51
52
53
public partial class Example

{

    public async Task RunProduction_Example()

    {

        int workspaceId = 12345;            // Workspace Production exists in

        int productionId = 11111;            // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                ProductionJobResult result = await productionManager.RunProductionAsync(workspaceId, productionId, false);

                bool wasJobCreated = result.WasJobCreated;

                int productionJobId = result.JobID;

                if (!wasJobCreated)

                {

                    Console.WriteLine(result.Errors);

                    Console.WriteLine(result.Warnings);

                    Console.WriteLine(result.Messages);

                    // Okay, so maybe you've looked at the errors and found some document conflicts

                    // and you want to override it anyway.

                    bool overrideConfilcts = true;

                    bool suppressWarnings = true;

                    result = await productionManager.RunProductionAsync(workspaceId, productionJobId, suppressWarnings, overrideConfilcts);

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

### Stage and run multiple productions

Use the MassStageAndRunAsync() method to stage and run multiple productions in a workspace. If the production is already staged, this method only runs it.

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
49
50
51
52
53
54
public partial class Example

{

    public async Task MassStageAndRun_Example()

    {

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                int workspaceId = 12345; // Workspace containing the productions

                List<int> productionIds = new List<int> { 100, 200 };

                List<ProductionJobResult> result =

                    await productionManager.MassStageAndRunAsync(workspaceId, productionIds);

                // Do something, like display results

                foreach (ProductionJobResult jobResult in result)

                {

                    if (jobResult.WasJobCreated)

                    {

                        Console.WriteLine("Successfully created job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when creating job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                        Console.WriteLine("Errors: {0}", string.Join("; ", jobResult.Errors));

                    }

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

### Re-run a production

Use the RerunProductionAsync() method to re-run a production.

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
public partial class Example

{

    public async Task ReRunProduction_Example()

    {

        int workspaceId = 12345;         // Workspace Production exists in

        int productionId = 11111;         // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                // Maybe you have run some productions nightly and get email notification said it got error already

                // Now you have made your fix and decide to rerun it again

                //TODO: Uncomment when we create endpoint for Production create.

                Production prod = await productionManager.ReadSingleAsync(workspaceId, productionId);

                if (prod.ProductionMetadata.Status == ProductionStatus.Error)

                {

                    await productionManager.RerunProductionAsync(workspaceId, productionId);

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

## Default fields and restrictions for productions

This section contains code samples that illustrate how to retrieve default field values, and how to set and remove production restrictions.

### Retrieve default field values for a production

Use the GetProductionDefaultFieldValues() method to retrieve default field values for a production. This method doesn't return empty or null fields.

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
public async Task GetProductionDefaultFieldValues_Example()

{

    int workspaceId = 12345; // Workspace containing the Production

    var userEmail = "user@test.com"; // User login

    var password = "abc123456!"; // User password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(

        new Uri(relativityRestUri),

        usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (var productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            ProductionDefaultFieldValues values = await productionManager.GetProductionDefaultFieldValues(workspaceId);

            Console.WriteLine("Found default choice Artifact ID for BrandingFont field: {0}.", values.BrandingFont.DefaultValue.ID);

            Console.WriteLine("Found default choice name for BrandingFont field: {0}.", values.BrandingFont.DefaultValue.Name);

            Console.WriteLine("Found BrandingFont field GUID: {0}.", values.BrandingFont.Guid);

            Console.WriteLine("Found BrandingFont field Artifact ID: {0}.", values.BrandingFont.ID);

            Console.WriteLine("Found default value for BrandingFontSize field: {0}.", values.BrandingFontSize.DefaultValue);

            Console.WriteLine("Found BrandingFont field GUID: {0}.", values.BrandingFontSize.Guid);

            Console.WriteLine("Found BrandingFont field Artifact ID: {0}.", values.BrandingFontSize.ID);

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
```

### Set production restrictions on a workspace

Use the SetProductionRestrictionsAsync() method to add a production restriction to a workspace. Pass the Artifact ID of a saved search in the workspace if this value isn't already set. If the value is set, this method replaces the current production restriction with a new one.

Use 0 as the ID for a saved search if you want to clean up the current production restriction.

View sample code Copy

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
public class SetProductionRestrictions

{

    public partial class Example

    {

        public async Task SetProductionRestrictions_Example()

        {

            int workspaceId = 12345;            // Workspace production restriction exist in

            int searchId = 456;                 // Saved search to be used as production restriction

            var userEmail = "user@test.com";    // User's login

            var password = "abc123456!";        // User's password

            var relativityRestUri = "http://localhost/relativity.rest/api";

            var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

            ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

            ServiceFactory serviceFactory = new ServiceFactory(settings);

            using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

            {

                try

                {

                    await productionManager.SetProductionRestrictionsAsync(workspaceId, searchId);

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

}
```

### Retrieve the ID of a save search used for production restrictions

Use the GetProductionRestrictionAsync() method to retrieve the Artifact ID of a save search used for production restrictions in a workspace. This method returns 0 if a production restriction hasn't been set.

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
public class GetProductionRestrictions

{

    public partial class Example

    {

        public async Task GetProductionRestrictions_Example()

        {

            int workspaceId = 12345;            // Workspace production restriction exist in

            var userEmail = "user@test.com";    // User's login

            var password = "abc123456!";        // User's password

            var relativityRestUri = "http://localhost/relativity.rest/api";

            var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

            ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

            ServiceFactory serviceFactory = new ServiceFactory(settings);

            using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

            {

                try

                {

                    int savedSearchId = await productionManager.GetProductionRestrictionAsync(workspaceId);

                    if (savedSearchId > 0)

                    {

                        Console.WriteLine($"Production Restriction is using a saved search Id {savedSearchId}");

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

}
```

## Production job status, progress, and other information

This section contains code samples that illustrate how to retrieve information about production jobs, including status, progress, production results, and others.

### Retrieve the job status of a production

Use the GetJobStatus() method to retrieve the job status of a production.

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
49
50
51
52
public partial class Example

{

    public async Task GetJobStatus_Example()

    {

        int workspaceId = 12345;            // Workspace Production(s) exist in

        int productionId = 11111;         // Production's ArtifactID

        bool includePercentages = false; // Include percentage of how complete the production is

        int maxNumberOfBrandingErrors = 10; // Returns the max number of branding errors if there are any.

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                // Get the job status of a given production

                var productionJobStatusResult = await productionManager.GetJobStatus(workspaceId, productionId, includePercentages, maxNumberOfBrandingErrors);

                Console.WriteLine("Production Status: {0}", productionJobStatusResult.Status);

                Console.WriteLine("Production Job Status: {0}", productionJobStatusResult.JobStatus);

                Console.WriteLine("Production Last Run Error: {0}", productionJobStatusResult.LastRunError);

                Console.WriteLine("Production Branding Complete: {0}%", productionJobStatusResult.PercentageImaging);

                Console.WriteLine("Production Producing Complete: {0}%", productionJobStatusResult.PercentageProducing);

                Console.WriteLine("Production Last Run Status message{0}", productionJobStatusResult.LastRunStatus);

                Console.WriteLine("Production Last Error message{0}", productionJobStatusResult.LastRunError);

                Console.WriteLine("There are {0} branding errors. They are", productionJobStatusResult.NumberOfBrandingErrors);

                foreach (var brandingError in productionJobStatusResult.BrandingErrors)

                {

                    Console.WriteLine("Production Last Run Error: {0}", brandingError);

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

### Retrieve progress details for a production

Use the ProgressAsync() method to retrieve progress details for a production.

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
public async Task GetProgress_Example()

{

    int workspaceId = 12345;            // Workspace Production exists in

    int productionId = 11111;            // Production's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            ProductionProgress productionProgress = await productionManager.ProgressAsync(workspaceId, productionId);

            var productionStatus = productionProgress.Status;

            var totalDocuments = productionProgress.TotalDocuments;

            // Do something, like display the metadata of the production

            Console.WriteLine("The current status of the production is: {0}.", productionStatus);

            Console.WriteLine("There are {0} documents total.", totalDocuments);

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
```

### Retrieve production status details

Use the GetProductionStatusDetails() method to retrieve production status details.

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
public partial class Example

{

    public async Task GetProductionStatusDetails_Example()

    {

        int workspaceId = 12345;            // Workspace Production(s) exist in

        int productionId = 11111;         // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                // Get the production status detail of a given production

                var productionStatusDetailsResult = await productionManager.GetProductionStatusDetails(workspaceId, productionId);

                Console.WriteLine("Production Status Detail:");

                foreach (KeyValuePair<string, object> statusDetail in productionStatusDetailsResult.StatusDetails)

                {

                    Console.WriteLine($"{statusDetail.Key}: {statusDetail.Value}");

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

### Retrieve results for produced image files

Use the GetProductionImagesAsync() method to retrieve information about produced image files. This method returns an ImageFilesResult object for each file associated with a specific workspace and production. The list of ImageFilesResult object doesn't have a specific order.

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
91
92
93
94
95
96
97
98
99
100
101
102
public partial class Example

{

    public async Task GetProductionImagesWithDocuments_Example()

    {

        int workspaceId = 12345;          // Workspace Production exists in

        int productionId = 11111;         // Production's ArtifactID

        int documentId1 = 22222;          // ArtifactID of a document in the Production

        int documentId2 = 33333;          // ArtifactID of another document in the Production

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";      // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                List<int> documents = new List<int>()

            {

                documentId1,

                documentId2

            };

                ImageFilesResult result = await productionManager.GetProductionImagesAsync(workspaceId, productionId, documents);

                foreach (ImageFile imageFile in result.ImageFiles)

                {

                    Console.WriteLine($"FileID: {imageFile.FileID}");

                    Console.WriteLine($"FileGuid: {imageFile.FileGuid}");

                    Console.WriteLine($"DocumentID: {imageFile.DocumentID}");

                    Console.WriteLine($"PageNumber: {imageFile.PageNumber}");

                    Console.WriteLine($"HasRedactions: {imageFile.HasRedactions}");

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

    public async Task GetProductionImagesWithPagination_Example()

    {

        int workspaceId = 12345;          // Workspace Production exists in

        int productionId = 11111;         // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";      // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                int top = 1; // StartIndex of the result set.

                int skip = 5; // Number of total results to fetch.

                string token = "1e51ae24-bbcb-4b61-aafb-1f91859d9891"; // Token associated with this call to page through the images.

                PagedImageFilesResult result = await productionManager.GetProductionImagesAsync(workspaceId, productionId, token, top, skip);

                Console.WriteLine($"This is the count of the entire result set: {result.TotalResultSet}.");

                Console.WriteLine($"This is the count of the result set on the current page: {result.ResultCount}.");

                foreach (ImageFile imageFile in result.ImageFiles)

                {

                    Console.WriteLine($"FileID: {imageFile.FileID}");

                    Console.WriteLine($"FileGuid: {imageFile.FileGuid}");

                    Console.WriteLine($"DocumentID: {imageFile.DocumentID}");

                    Console.WriteLine($"PageNumber: {imageFile.PageNumber}");

                    Console.WriteLine($"HasRedactions: {imageFile.HasRedactions}");

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

### Retrieve all productions in a workspace

Use the GetAllAsync() method to retrieve all productions in a workspace.

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
public partial class Example

{

    public async Task GetAllProductions_Example()

    {

        int workspaceId = 12345;            // Workspace Production(s) exist in

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                // Capture list of all productions in workspace for which the user has permissions.

                // List can be iterated over to inspect productions, see which are ready to be produced, etc.

                var productionList = await productionManager.GetAllAsync(workspaceId);

                foreach (var production in productionList)

                {

                    Console.WriteLine("Production Name: {0}", production.Name);

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

### Retrieve produced productions for documents

Use the GetProducedProductionsFromDocumentsAsync() method to retrieve produced productions for documents by using document IDs or a mass operation token.

View code sample using document IDs

Set the ExcludeNonReproducible property if you only want to return non-reproducible productions. The default value is false.

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
91
92
93
94
95
96
97
98
99
100
101
102
103
public async Task GetProducedProductionsFromDocumentIds_Example()

{

    int workspaceId = 12345;         // Workspace Productions exist in

    int documentId1 = 123;           // Document1's ArtifactID

    int documentId2 = 456;           // Document2's ArtifactID

    int documentId3 = 789;           // Document3's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            List<int> documentIds = new List<int>

            {

                documentId1,

                documentId2,

                documentId3

            };

            //This list contains every produced production that contains at least one of the above documents.

            List<Services.Interfaces.V1.DTOs.ProductionSlim> producedProductions = await productionManager.GetProducedProductionsFromDocumentsAsync(workspaceId, documentIds);

            foreach (Services.Interfaces.V1.DTOs.ProductionSlim producedProduction in producedProductions)

            {

                Console.WriteLine($"This is the artifactId of the produced production: {producedProduction.ProductionID}");

                Console.WriteLine($"This is the name of the produced production: {producedProduction.Name}");

                Console.WriteLine($"This is the first bates value of the produced production: {producedProduction.FieldValues["BeginBates"]}");

                Console.WriteLine($"This is the last bates value of the produced production: {producedProduction.FieldValues["EndBates"]}");

                Console.WriteLine($"This is the date produced of the produced production: {producedProduction.FieldValues["DateProduced"]}");

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

public async Task GetProducedProductionsFromDocumentIds_ExcludeNonReproducible_Example()

{

    int workspaceId = 12345;         // Workspace Productions exist in

    int documentId1 = 123;           // Document1's ArtifactID

    int documentId2 = 456;           // Document2's ArtifactID

    int documentId3 = 789;           // Document3's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            List<int> documentIds = new List<int>

            {

                documentId1,

                documentId2,

                documentId3

            };

            //This list contains every produced production that contains at least one of the above documents, and can be re-produced.

            List<Services.Interfaces.V1.DTOs.ProductionSlim> producedProductions = await productionManager.GetProducedProductionsFromDocumentsAsync(workspaceId, documentIds, true);

            foreach (Services.Interfaces.V1.DTOs.ProductionSlim producedProduction in producedProductions)

            {

                Console.WriteLine($"This is the artifactId of the produced production: {producedProduction.ProductionID}");

                Console.WriteLine($"This is the name of the produced production: {producedProduction.Name}");

                Console.WriteLine($"This is the first bates value of the produced production: {producedProduction.FieldValues["BeginBates"]}");

                Console.WriteLine($"This is the last bates value of the produced production: {producedProduction.FieldValues["EndBates"]}");

                Console.WriteLine($"This is the date produced of the produced production: {producedProduction.FieldValues["DateProduced"]}");

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
```

View code sample using a mass operation token

Set the ExcludeNonReproducible property if you only want to return non-reproducible productions. The default value is false.

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
91
92
93
public async Task GetProducedProductionsFromMassOpDatabaseToken_Example()

{

        int workspaceId = 12345; // Workspace Productions exist in

        string databaseToken = "D6F3A251-2B5F-483E-B245-E9E7D5FC9560"; // Database Token retrieved from mass operation.

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                //This list contains every produced production that contains at least one of the above documents.

                List<Services.Interfaces.V1.DTOs.ProductionSlim> producedProductions = await productionManager.GetProducedProductionsFromDocumentsAsync(workspaceId, databaseToken);

                foreach (Services.Interfaces.V1.DTOs.ProductionSlim producedProduction in producedProductions)

                {

                    Console.WriteLine($"This is the artifactId of the produced production: {producedProduction.ProductionID}");

                    Console.WriteLine($"This is the name of the produced production: {producedProduction.Name}");

                    Console.WriteLine($"This is the first bates value of the produced production: {producedProduction.FieldValues["BeginBates"]}");

                    Console.WriteLine($"This is the last bates value of the produced production: {producedProduction.FieldValues["EndBates"]}");

                    Console.WriteLine($"This is the date produced of the produced production: {producedProduction.FieldValues["DateProduced"]}");

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

    /// <summary>

    /// Use this example if you are interested in creating a custom mass operation on the document object involving produced productions.

    /// A primer on custom mass operations: When a user selects documents and presses the custom mass operation button, a database token will

    /// be generated, corresponding to a table in the database that holds all of the selected documents. This API is designed to be used

    /// for these scenarios to avoid a second server trip to retrieve the requested document IDs of the custom mass operation.

    /// </summary>

    /// <returns></returns>

    public async Task GetProducedProductionsFromMassOpDatabaseToken_ExcludeNonReproducible_Example()

    {

        int workspaceId = 12345; // Workspace Productions exist in

        string databaseToken = "D6F3A251-2B5F-483E-B245-E9E7D5FC9560"; // Database Token retrieved from mass operation.

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";     // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                //This list contains every produced production that contains at least of the above documents, and can be re-produced.

                List<Services.Interfaces.V1.DTOs.ProductionSlim> producedProductions = await productionManager.GetProducedProductionsFromDocumentsAsync(workspaceId, databaseToken, true);

                foreach (Services.Interfaces.V1.DTOs.ProductionSlim producedProduction in producedProductions)

                {

                    Console.WriteLine($"This is the artifactId of the produced production: {producedProduction.ProductionID}");

                    Console.WriteLine($"This is the name of the produced production: {producedProduction.Name}");

                    Console.WriteLine($"This is the first bates value of the produced production: {producedProduction.FieldValues["BeginBates"]}");

                    Console.WriteLine($"This is the last bates value of the produced production: {producedProduction.FieldValues["EndBates"]}");

                    Console.WriteLine($"This is the date produced of the produced production: {producedProduction.FieldValues["DateProduced"]}");

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

### Retrieve a token for paging through images

Use the GetProductionImagesTokenAsync() method to retrieve a unique token for paging through images.

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

    public async Task GetProductionImagesToken_Example()

    {

        int workspaceId = 12345;          // Workspace Production exists in

        int productionId = 11111;         // Production's ArtifactID

        var userEmail = "user@test.com";  // User's login

        var password = "abc123456!";      // User's password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                string result = await productionManager.GetProductionImagesTokenAsync(workspaceId, productionId);

                Console.WriteLine($"Produced Images Token: {result}");

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

## Production errors and document conflicts

This section contains code samples that illustrate how to retrieve information about production errors and document conflicts.

### Retrieve conflicts, errors, and other production information

Use the ProductionRunCheckAsync() method to retrieve document conflicts, production errors, and information about whether the production can be run.

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
public async Task ProductionRunCheckAsync_Example()

{

    int workspaceId = 12345;            // Workspace Production exists in

    int productionId = 11111;            // Production's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            ProductionRunCheckResult runCheckResult =

                await productionManager.ProductionRunCheckAsync(workspaceId, productionId);

            // Do something, like display check errors

            Console.WriteLine(runCheckResult.CanContinue

                ? "This production can continue to run"

                : "This production is not able to run with errors");

            if (runCheckResult.ProductionErrors.Count > 0)

            {

                Console.WriteLine("Production Errors:" + Environment.NewLine);

                foreach (var error in runCheckResult.ProductionErrors)

                {

                    Console.WriteLine(error + Environment.NewLine);

                }

            }

            if (runCheckResult.PlaceholderErrors.Count > 0)

            {

                Console.WriteLine("Placeholder Errors:" + Environment.NewLine);

                foreach (var error in runCheckResult.PlaceholderErrors)

                {

                    Console.WriteLine(error + Environment.NewLine);

                }

            }

            Console.WriteLine($"The production continue message is {runCheckResult.ContinueMessage}");

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
```

### Retrieve staging errors for a production

Use the StagingErrorsAsync() method to retrieve staging errors and duplicate documents for a production.

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
public async Task GetStagingErrors_Example()

{

    int workspaceId = 12345; // Workspace containing the Production

    int productionId = 11111; // Production ArtifactID

    var userEmail = "user@test.com"; // User login

    var password = "abc123456!"; // User password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(

        new Uri(relativityRestUri),

        usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            StagingErrors stagingErrors = await productionManager.StagingErrorsAsync(workspaceId, productionId);

            // Do something, like display staging errors for the production

            Console.WriteLine("Found {0} documents with staging errors.",

                stagingErrors.ErroredDocumentCount);

            Console.WriteLine("Production failed during staging with the following error message: {0}",

                stagingErrors.ErrorMessage);

            Console.WriteLine("Found duplicate documents {0} across multiple data sources {1}",

                string.Join(", ", stagingErrors.DuplicateDocuments.Select(x => x.Name).ToList()),

                string.Join(", ", stagingErrors.DuplicateDocuments.Select(x => x.DataSourceNames).ToList()));

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

### Retrieve branding errors for a production

Use the GetBrandingErrorsAsync() method to retrieve a specified number of branding errors for a production. The MaxListItems instance setting controls the number of branding errors returned.

This method returns an empty list if the production isn't in an errored state or if the user doesn't have permission to view the errored documents.

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
public async Task GetBrandingErrors_Example()ta

{

    int workspaceId = 12345;            // Workspace Production exists in

    int productionId = 11111;            // Production's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            List<BrandingError> brandingErrors = await productionManager.GetBrandingErrorsAsync(workspaceId, productionId);

            Console.WriteLine("There are {0} branding errors.", brandingErrors.Count);

            foreach (BrandingError brandingError in brandingErrors)

            {

                // Do something, like display information about the documents and its branding errors

                Console.WriteLine("DocumentID {0} - {1} FileID {2} Error: {3}.", brandingError.DocumentID, brandingError.DocumentName, brandingError.FileID, brandingError.ErrorMessage);

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
```

### Retrieve documents conflicting with production restrictions

Use the DocumentConflictsAsync() method to retrieve documents conflicting with the production restrictions defined for the workspace.

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
public async Task DocumentConflictsAsync_Example()

{

    int workspaceId = 12345;            // Workspace Production exists in

    int productionId = 11111;            // Production's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            ProductionDocumentConflicts documentConflicts =

                await productionManager.DocumentConflictsAsync(workspaceId, productionId);

            // Do something, like display conflicts documents

            Console.WriteLine("There are {0} document(s) have conflicts", documentConflicts.DocumentIDs);

            foreach (var docID in documentConflicts.DocumentIDs)

            {

                Console.WriteLine("Document ArtifactID - {0}", docID);

            }

            // Do something, like display production restrictions information

            Console.WriteLine("Current workspace has production restrictions name {0}", documentConflicts.ProductionRestrictions.SavedSearchName);

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

### Remove documents conflicting with production restrictions

Use the DeleteDocumentConflictsAsync() method to remove documents from a production that conflict with the restrictions set on a workspace. This method deletes documents from a production with a status of Staged or ErrorStartingProduction . The user must have edit permission to the production set.

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
public async Task DeleteDocumentConflictsAsync_Example()

{

    int workspaceId = 12345;            // Workspace Production exists in

    int productionId = 11111;            // Production's ArtifactID

    var userEmail = "user@test.com";  // User's login

    var password = "abc123456!";     // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            await productionManager.DeleteDocumentConflictsAsync(workspaceId, productionId);

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
```

## Re-production jobs

This section contains code samples that illustrate how to retrieve, run, stage, and cancel re-production jobs.

### Retrieve productions eligible for re-production

Use the GetProductionsEligibleForReproductionAsync() method to retrieve productions eligible for re-production based on the production type.

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
public async Task GetProductionsEligibleForReproductionAsync_Example()

{

    int workspaceId = 12345; // Workspace containing the Production

    string databaseToken = "1e51ae24-bbcb-4b61-aafb-1f91859d9891"; // GUID representing the database being used

    int reproductionType = 0; // Reproduction type (reproduce document = 0, replace document With placeholder = 1, replace placeholder with document = 2)

    var userEmail = "user@test.com"; // User login

    var password = "abc123456!"; // User password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(

        new Uri(relativityRestUri),

        usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            IEnumerable<ReproductionCandidate> reproductionCandidates = await productionManager.GetProductionsEligibleForReproductionAsync(workspaceId, databaseToken, reproductionType);

            // Do something, like display information about the eligible reproductions.

            Console.WriteLine("Found the following production(s) {0} with the following Production ID(s) {1} are eligible for reproduction.",

                string.Join(", ", reproductionCandidates.Select(x => x.Name).ToList()),

                string.Join(", ", reproductionCandidates.Select(x => x.ProductionID).ToList()));

            Console.WriteLine("Eligible production(s) have the starting bates number(s) {0} and the ending bates number(s) {1}",

                string.Join(", ", reproductionCandidates.Select(x => x.BeginBates).ToList()),

                string.Join(", ", reproductionCandidates.Select(x => x.EndBates).ToList()));

            Console.WriteLine("Eligible production(s) were produced on the following date(s): {0}",

                string.Join(", ", reproductionCandidates.Select(x => x.DateProduced).ToList()));

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
```

### Retrieve re-productions for a specific production

Use the GetReproductionsAsync() method to retrieve re-productions performed for a specific production. Any re-production that has been deleted has an Artifact ID of -1. The user must have permissions to view a production.

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
public async Task GetReproductions_Example()

{

    int workspaceID = 12345; // Workspace containing the Production

    int productionID = 11111; // Production ArtifactID

    var userEmail = "user@test.com"; // User login

    var password = "abc123456!"; // User password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(

        new Uri(relativityRestUri),

        usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager =

        serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            IEnumerable<ReproductionRef> reproductions = await productionManager.GetReproductionsAsync(workspaceID, productionID);

            foreach (ReproductionRef reproduction in reproductions)

            {

                Console.WriteLine($"This is the re-production name: {reproduction.Name}");

                Console.WriteLine($"This is the re-production artifact ID: {reproduction.ProductionID}");

                Console.WriteLine($"This is the re-production deletion status: {reproduction.IsDeleted}");

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
```

### Stage and run a re-production job

Use the MassStageAndRunProductionsAsync() method to stage and run a re-production job, and to retrieve job details.

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
49
50
51
52
53
54
55
public async Task MassStageAndRunProductionsAsync_Example()

{

    int workspaceId = 12345; // Workspace containing the reproduction job

    int reproductionJobId = 2; // Reproduction job that points to created productions

    var userEmail = "user@test.com"; // User login

    var password = "abc123456!"; // User password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(

        new Uri(relativityRestUri),

        usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

    {

        try

        {

            IEnumerable<ProductionJobResult> jobResults = await productionManager.MassStageAndRunProductionsAsync(workspaceId, reproductionJobId);

            // Do something, like check if all reproductions were successful and display relevant information.

            bool wasSuccess = true;

            foreach (ProductionJobResult result in jobResults)

            {

                wasSuccess &= result.WasJobCreated;

            }

            if (wasSuccess)

            {

                Console.WriteLine("Found the following production(s) {0} were staged and ran.",

                    string.Join(", ", jobResults.Select(x => x.ProductionID).ToList()));

            }

            else

            {

                Console.WriteLine("Some or all productions failed with the following errors: {0}.",

                    string.Join(", ", jobResults.Select(x => x.Errors).ToList()));

            }

            Console.WriteLine("Reproduction finished with the following warnings: {0}",

                string.Join(", ", jobResults.Select(x => x.Warnings).ToList()));

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
```

### Cancel jobs for a re-production

Use the CancelReproductionJobAsync() method to cancel jobs for a re-production. This method cancels all production jobs for the re-production.

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
public partial class Example

{

    public async Task CancelReproductionJob_Example()

    {

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionManager productionManager = serviceFactory.CreateProxy<IProductionManager>())

        {

            try

            {

                int workspaceId = 123; // Workspace containing the re-production

                int reproductionJobId = 456;

                MassCancelResult result =

                    await productionManager.CancelReproductionJobAsync(workspaceId, reproductionJobId);

                // Do something, like display results

                Console.WriteLine("Out of {0} production jobs requested to cancel, {1} were successful.",

                    result.NumberOfJobsRequestedForCancel,

                    result.NumberOfJobsCancelWasRequestedSuccessfully);

                Console.WriteLine("Errors for the overall mass operation: {0}",

                    string.Join("; ", result.Errors));

                foreach (CancelJobResult jobResult in result.CancelJobResults)

                {

                    if (jobResult.CancelSuccessfullySent)

                    {

                        Console.WriteLine("Successfully canceled production job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when canceling production job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                        Console.WriteLine("Errors: {0}", string.Join("; ", jobResult.Errors));

                    }

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
