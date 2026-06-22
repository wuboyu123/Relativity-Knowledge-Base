---
title: "Re-production Job Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Reproduction_Job_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:27:51+00:00
sha256: f29faa89a0eda32c45c15c49548f2446ce7630fbf128381dcc8e1b3b54a5f1ab
---

Re-production Job Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Re-production Job Manager (.NET)

A re-production job provides you with the ability to select specific documents from a completed production job and re-run them. After a re-production job finishes running, the modified documents are merged into the original production set. These documents overwrite those that were previously produced. For general information, see Re-production on the Relativity Server 2025 Documentation site.

The Re-production Job Manager API supports the following functionality:

- Creating re-production jobs

- Retrieving re-production job IDs

- Retrieving re-production job statuses

You can also use the Re-production Job Manager API through REST. For more information, see Re-production Job Manager (REST) .

See these related pages:

- Production

- Production Manager (.NET)

- Production Data Source Manager (.NET)

- Production Placeholder Manager (.NET)

- Production Queue Manager (.NET)

## Fundamentals for the Re-production Manager API

The Re-production Manager API contains the following methods, classes, and enumerations.

Methods

The Re-production Manager API exposes the following methods on the Services.<VersionNumber>.IReproductionJobManager interface:

- CreateReproductionJobAsync() method - creates a new re-production job. This overloaded method takes a list of document IDs or a mass operation token. See Create a re-production job .

- GetReproductionJobIDsAsync() method - retrieves the IDs for re-production jobs run in a specified workspace. See Retrieve re-production job IDs .

- GetReproductionStatusByReproductionJobIDAsync() method - retrieves the status of a re-production job. See Retrieve the status for a re-production job .

Classes

The Re-production Manager API includes multiple classes. The following list highlights some of the key classes:

- ReplaceDocumentWithPlaceholderOptions - defines options for creating a re-production job when using the re-production mode called ReproduceDocumentWithPlaceholder. The options include:

- Placeholder - specifies the placeholder to use when re-producing documents.

If a produced document has three pages, the document has three placeholders after re-production, one for each page of the originally produced document. This process preserves Bates numbering and avoid gaps.

- NativeReproductionOption - specifies whether to produce native documents when re-producing documents.

- ReplacePlaceholderWithDocumentOptions - defines options for creating a re-production job when using the re-production mode called ReplacePlaceholderWithDocument. The options include:

- Delimiter - specifies the delimiter to use between the original placeholder Bates number and the suffixed page number.

- NumberOfDigits - specifies the number of digits to use for the suffixed page number.

- Suffix - specifies the suffix to append to end of new Bates numbers.

- NativeReproductionOption - specifies whether to produce native documents when running a re-production job.

- BurnRedactions - specifies whether to burn redactions on re-produced images. When using this option, a valid markup set must exist.

- MarkupSet - specifies the markup set to use when burning redactions on re-produced documents.

- ReproduceDocumentOptions - defines options for creating a re-production job when using the re-production mode called ReproduceDocument. The options include:

- NativeReproductionOption - specifies whether to produce native documents when running a re-production job.

- BurnRedactions - a Boolean value specifying whether to burn redactions on re-produced images. When using this option, a valid markup set must exist.

- MarkupSet - the markup set to use when burning redactions on re-produced documents.

- ReproductionJobResult - the result of a re-projection job operation.

- ReproductionJobID - the re-production job ID.

- ProductionsCreated - a list of productions created from the re-production job.

- InnerReproductionJobResult - information about the created production job.

- ProductionID - the production ID of the production.

- ParentProductionID - the production ID of the original production.

- Errors - error messages generated if the production job wasn't created.

- Warnings - warning messages about the production job.

- Messages - informational messages about the production job.

- WasJobCreated - a Boolean value indicating whether the job was created.

- Errors - error messages generated if the production job wasn't created.

- Warnings - warning messages about the re-production job.

- Messages - informational messages about the re-production job.

Enumerations

The Re-production Manager AP includes multiple enumerations. The following list highlights some of the key enumerations:

- ReproductionType - the type of re-production job. A re-production job only has one type. The types include:

- ReproduceDocument - re-produces a document with new branding or markup sets. The re-produced document must have the same number of pages before and after re-production. To further customize the re-production job, use the ReproduceDocumentOptions class.

- ReplaceDocumentWithPlaceholder - replaces a document with a placeholder. To further customize the re-production job, use the ReplaceDocumentWithPlaceholderOptions class.

- ReplacePlaceholderWithDocument - replaces a placeholder with the original document. To further customize the re-production job, use the ReplacePlaceholderWithDocumentOptions class.

- ReproductionStatus - the status of a re-production job. The statuses include:

- Created - the re-production job was been created, but not yet run.

-

Running - the re-production job is currently running without errors.

A production status of Staged results in a re-production status of Running because it between the New and Produced production states.

- RunningWithErrors - the re-production job is currently running but some productions have errored.

- Completed - the re-production job has completed all productions successfully.

- CompletedWithErrors - the re-production job has completed all productions, but some have errored.

- DoesNotExist - an invalid re-production job. If all productions in the job have been deleted, a status of DoesNotExist is returned.

For reference content, see Class library reference .

## Create a re-production job

Use the CreateReproductionJobAsync() method to create a new re-production job. This method is overloaded as follows:

- Pass a list of document IDs

Copy

```text
1
2
3
4
ReproductionJobResult result = await reproductionJobManager.CreateReproductionJobAsync(int workspaceArtifactID,

    ReproductionOptions reproductionOptions,

    List<ProductionRef> productions,

    List<int> documents);
```

- Pass a mass operation token

Copy

```text
1
2
3
4
ReproductionJobResult result = await reproductionJobManager.CreateReproductionJobAsync(int workspaceArtifactID,

    ReproductionOptions reproductionOptions,

    List<ProductionRef> productions,

    Guid massOperationToken);
```

View parameter descriptions for the CreateReproductionJobAsync() method

The CreateReproductionJobAsync() method has the following parameters. You can pass a database token or document IDs to this overloaded method.

- workspaceArtifactID - the Artifact ID of a workspace.

- reproductionOptions - a ReproductionOptions object, which defines the type and settings for the re-production job. Each re-production type must match its corresponding options class. If you select ReproduceDocument for the ReproductionType, populate ReproduceDocumentOptions on the ReproductionOptions object. See Classes for more information about these options:

- ReplaceDocumentWithPlaceholderOptions class

- ReplacePlaceholderWithDocumentOptions class

- ReproduceDocumentOptions class

- productions - a list of ProductionRef objects. The re-production job modifies the productions in this list.

- databaseToken - a GUID representing the database token of a custom mass operation. Only document mass operations are supported.

- documentIDs - a list of Artifact IDs representing the documents to be re-produced.

Guidelines for creating re-production jobs

Review these general guidelines before creating re-production jobs:

- The CreateReproductionJobAsync() method doesn't run re-production jobs. To run these jobs, use the stage and run method or the mass stage and run method. See Production Manager (.NET) .

- You must have the document view permission and the production view, edit, and add permissions to use this method.

- You can only re-produce images and placeholders. You can choose to export natives in a re-production job, but natives can't be re-produced.

- We recommend creating re-production jobs with under 10,000 documents. If you want to create a larger job, split the requests into batches.

- If the documents selected for re-production aren't included in the original production job, they won' be re-produced. For example, a production contains documents A and B. You attempt to include documents B and C for re-production. Only document B is re-produced because document C doesn't exist in the production.

- A re-production job can only use one set of options to further customize it. The following types of re-productions include:

- ReproduceDocument - re-produce a document with new branding or markup sets. The re-produced document must have the same number of pages before and after re-production.

- ReplaceDocumentWithPlaceholder - replace a document with a placeholder.

- ReplacePlaceholderWithDocument - replace a placeholder with the original document.

- The CreateReproductionJobAsync() method returns a ReproductionJobResult object. It contains the ReproductionJobID, a list of the created productions, errors, messages, and warnings. For each requested re-production, the InnerReproductionJobResult object provides specific information about errors that occurred for the given re-production.

View code sample using document IDs

The following code sample illustrates how to use the document IDs to create a re-production job.

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
public async Task CreateReproductionJob_WithDocumentIds_Example()

{

    int workspaceId = 12345;            // Workspace Productions exist in

    int production1Id = 11111;          // Production 1's ArtifactID

    int production2Id = 22222;          // Production 2's ArtifactID

    int production3Id = 33333;          // Production 3's ArtifactID

    int document1Id = 44444;            // Document 1's ArtifactID

    int document2Id = 55555;            // Document 2's ArtifactID

    int document3Id = 66666;            // Document 3's ArtifactID

    int markupSetId = 77777;            // MarkupSet ArtifactID

    var userEmail = "user@test.com";    // User's login

    var password = "abc123456!";        // User's password

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IReproductionJobManager reproductionJobManager = serviceFactory.CreateProxy<IReproductionJobManager>())

    {

        try

        {

            List<int> documentIds = new List<int>()

        {

            document1Id,

            document2Id,

            document3Id

        };

            ReproductionOptions reproductionOptions = new ReproductionOptions()

            {

                ReproductionType = ReproductionType.ReproduceDocument,

                ReproduceDocumentOptions = new ReproduceDocumentOptions()

                {

                    BurnRedactions = true,

                    MarkupSetID = markupSetId,

                    IncludeNatives = true

                }

            };

            List<ProductionRef> productions = new List<ProductionRef>()

        {

            new ProductionRef(){ProductionID = production1Id},

            new ProductionRef(){ProductionID = production2Id},

            new ProductionRef(){ProductionID = production3Id}

        };

            ReproductionJobResult result = await reproductionJobManager.CreateReproductionJobAsync(workspaceId, reproductionOptions, productions, documentIds);

            int reproductionJobId = result.ReproductionJobID;

            List<int> productionsCreated = result.ProductionsCreated;

            bool wasJobCreated = result.WasJobCreated;

            if (!wasJobCreated)

            {

                Console.WriteLine(result.Errors);

                Console.WriteLine(result.Warnings);

                Console.WriteLine(result.Messages);

            }

            // To get a more detailed breakdown of the productions created.

            foreach (InnerReproductionJobResult innerResult in result.Results)

            {

                Console.WriteLine(innerResult.ProductionID);

                Console.WriteLine(innerResult.ParentProductionID);

                Console.WriteLine(innerResult.Errors);

                Console.WriteLine(innerResult.Warnings);

                Console.WriteLine(innerResult.Messages);

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

The following code sample illustrates how to create a re-production job and retrieve related details for it. Before you can create the job, you must generate a database token that is passed to the CreateReproductionJobAsync() method.

Use the following steps to generate a database token for select documents:

- Create a custom mass operation. See Develop Mass Operation handlers .

- In Relativity, navigate to the Resource Files tab and add the custom mass operation by clicking New Resource File .

- Navigate to the Object Type tab and link the custom mass operation to the Document object. See Adding a custom mass operation .

- Navigate to the Documents tab within a workspace.

- Select the documents that you want to retrieve produced production information for.

-

In the mass operations bar, click the custom mass operation. A database token is generated that corresponds to a table in the database that holds the selected documents. The database token is at the end of the URL on the page that opens.

Passing a database token eliminates a second server trip to retrieve the requested document IDs of the custom mass operation.

The following code sample illustrates how to use the database token generated in the previous steps to create a re-production job.

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
public async Task CreateReproductionJob_WithMassOperationToken_Example()

{

    int workspaceId = 12345; // Workspace containing the Production

    string databaseToken = "1e51ae24-bbcb-4b61-aafb-1f91859d9891"; // GUID corresponding to the current re-produce mass operation

    var userEmail = "user@test.com"; // User login

    var password = "abc123456!"; // User password

    ReproductionOptions reproductionOptions = new ReproductionOptions() // options for the given reproduction

    {

        ReproductionType = (ReproductionType)2, // Reproduction type (reproduce document = 0, replace document With placeholder = 1, replace placeholder with document = 2)

        ReproduceDocumentOptions = null, // left null because this isn't the reproduction type selected

        ReplaceDocumentWithPlaceholderOptions = null, // left null because this isn't the reproduction type selected

        ReplacePlaceholderWithDocumentOptions = new ReplacePlaceholderWithDocumentOptions() // options for replacing the placeholder with a document

        {

            Delimiter = "_", // character after bates number ([Bates#]_0001)

            NumberOfDigits = 4, // number of digits after bates number ([Bates#]_0001)

            IncludeNatives = true, // option to include natives

            BurnRedactions = true, // option to burn redactions

            MarkupSetID = 6789 // ID of markup set for redactions, if chosen

        }

    };

    IEnumerable<ProductionRef> productions = new List<ProductionRef>() // productions to be reproduced

    {

        new ProductionRef()

        {

            ProductionID = 1 // production ID to be reproduced

        },

        new ProductionRef()

        {

            ProductionID = 2 // production ID to be reproduced

        }

    };

    var relativityRestUri = "http://localhost/relativity.rest/api";

    var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

    ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

    ServiceFactory serviceFactory = new ServiceFactory(settings);

    using (IReproductionJobManager reproductionJobManager = serviceFactory.CreateProxy<IReproductionJobManager>())

    {

        try

        {

            ReproductionJobResult reproductionJobResult = await reproductionJobManager.CreateReproductionJobAsync(workspaceId, reproductionOptions, productions, databaseToken);

            // Do something, like display information about the created reproduction job.

            if (reproductionJobResult.WasJobCreated == true)

            {

                Console.WriteLine("A reproduction job with the ID {0} was created.", reproductionJobResult.ReproductionJobID);

                Console.WriteLine("The following productions were created: {0}.", string.Join(", ", reproductionJobResult.ProductionsCreated.ToList()));

            }

            else

            {

                Console.WriteLine("Failed to create reproduction job.");

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

## Retrieve re-production job IDs

Use the GetReproductionJobIDsAsync() method to retrieve the IDs for re-production jobs run in a specified workspace. Pass the Artifact ID of the workspace to this method.

You must have view permissions for productions to retrieve re-production job IDs.

This method returns a list of integers representing re-production job IDs.

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

    public async Task GetReproductionJobIDs_Example()

    {

        int workspaceId = 12345;            // Workspace Re-productions exist in



        var userEmail = "user@test.com";    // User's login

        var password = "abc123456!";        // User's password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IReproductionJobManager reproductionJobManager = serviceFactory.CreateProxy<IReproductionJobManager>())

        {

            try

            {

                List<int> reproductionJobIds = await reproductionJobManager.GetReproductionJobIDsAsync(workspaceId);

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

## Retrieve the status for a re-production job

Use the GetReproductionStatusByReproductionJobIDAsync() method to retrieve the status of a re-production job. For example, you might call this method to determine whether a job has completed after creating and running it.

Pass the following arguments to this method:

- workspaceArtifactID - the Artifact ID of the workspace containing the re-production job.

- reproductionJobID - the Artifact ID of the re-production job.

This method returns ReproductionStatusResult object, which includes errors, warnings, and messages. It also includes a ProductionStatus object with properties for Artifact ID and status of each production included in the re-production job. For re-production statuses, see Fundamentals for the Re-production Manager API

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
public partial class Example

{

    public async Task GetReproductionStatusByReproductionJobID_Example()

    {

        int workspaceId = 12345;            // Workspace Re-productions exist in

        int reproductionJobId = 123;        // Re-production JobID



        var userEmail = "user@test.com";    // User's login

        var password = "abc123456!";        // User's password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(new Uri(relativityRestUri), usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IReproductionJobManager reproductionJobManager = serviceFactory.CreateProxy<IReproductionJobManager>())

        {

            try

            {

                ReproductionStatusResult reproductionStatusResult = await reproductionJobManager.GetReproductionStatusByReproductionJobIDAsync(workspaceId, reproductionJobId);



                Console.WriteLine(reproductionStatusResult.ReproductionStatus);

                Console.WriteLine(reproductionStatusResult.Errors);

                Console.WriteLine(reproductionStatusResult.Warnings);

                Console.WriteLine(reproductionStatusResult.Messages);



                foreach (ProductionStatusResult result in reproductionStatusResult.ProductionStatusResults)

                {

                    Console.WriteLine(result.ArtifactID); //Production ArtifactID

                    Console.WriteLine(result.Status); //Production Status

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

On this page

- Re-production Job Manager (.NET)

- Fundamentals for the Re-production Manager API

- Create a re-production job

- Retrieve re-production job IDs

- Retrieve the status for a re-production job


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
