---
title: "Production Queue Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Queue_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:27:47+00:00
sha256: dfde2104b8e47a0ced08797b29c81d929250c71a6a29750cc7a9a3d8570f004c
---

Production Queue Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production Queue Manager (.NET)

The Production Queue contains all production jobs currently running in your Relativity environment. For general information, see Production Queue on the Relativity Documentation site.

The Production Queue Manager API exposes methods used to cancel a single or multiple production jobs, to retry multiple jobs, or to set the priority for them. You can identify the jobs for canceling or retrying by mass operation token or Artifact ID.

You can also use the Production Queue Manager API through REST. For more information, see Production Queue Manager (REST) .

See these related pages:

- Production

- Production Manager (.NET)

- Production Data Source Manager (.NET)

- Production Placeholder Manager (.NET)

- Re-production Job Manager (.NET)

## Fundamentals for the Production Queue Manager API

The Production Queue Manager API contains the following methods and classes.

Methods

The Production Queue Manager API exposes the following methods on the Services.<VersionNumber>.IProductionQueueManager interface:

- CancelJobAsync() method - cancels a single production job. See Cancel a production job .

- MassCancelAsync() method - cancels a collection of production jobs by using mass operation token. This method takes a GUID used to identify a collection of production jobs. See Cancel production jobs by mass operation token .

- MassCancelProductionJobsAsync() method - cancels multiple production jobs. This method takes a list of production IDs to identify the production jobs. See Cancel production jobs by ID .

- MassPrioritizeAsync() method - sets the priority on a collection of production jobs in the queue. See Set the priority on production jobs .

- MassRetryAsync() method - reruns multiple production jobs. This method takes the GUID used to identify a collection of production jobs. See Retry production jobs by mass operation token .

- RetryProductionJobsAsync() method - reruns multiple production jobs. This method takes a list of production IDs to identify the production jobs. See Retry production jobs by ID .

Classes

The Production Queue Manager API contains multiple methods that take objects instantiated from the ProductionJobRef class. This class has the following properties:

- JobID - the Artifact ID of a production job.

- ProductionID - the Artifact ID of a production.

- WorkspaceID - the Artifact ID of the workspace that contains the production.

## Cancel a production job

Use the CancelJobAsync() method to cancel a single production job. Pass a ProductionJobRef object with the following properties to this method:

- WorkspaceID - the Artifact ID of the workspace containing the production job.

- ProductionID - the Artifact ID of the production.

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

    public async Task CancelJob_Example()

    {

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionQueueManager productionQueueManager = serviceFactory.CreateProxy<IProductionQueueManager>())

        {

            try

            {

                var jobRef = new ProductionJobRef

                {

                    WorkspaceID = 123,

                    ProductionID = 456

                };

                CancelJobResult result = await productionQueueManager.CancelJobAsync(jobRef);



                // Do something, like display results

                if (result.CancelSuccessfullySent)

                {

                    Console.WriteLine("Successfully canceled job ID {0} for production ID {1} in workspace ID {2}",

                        result.JobID, result.ProductionID, result.WorkspaceID);

                }

                else

                {

                    Console.WriteLine("Error(s) occurred when canceling job ID {0} for production ID {1} in workspace ID {2}",

                        result.JobID, result.ProductionID, result.WorkspaceID);

                    Console.WriteLine("Errors: {0}", string.Join("; ", result.Errors));

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

## Cancel production jobs by mass operation token

Use the MassCancelAsync() method to cancel a collection of production jobs by using mass operation token. This token is a GUID that represents the collection of jobs.

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
public partial class Example

{

    public async Task MassCancel_Example()

    {

        string databaseToken = "1e51ae24-bbcb-4b61-aafb-1f91859d9891"; // GUID representing the collection of selected production jobs for the mass operation



        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionQueueManager productionQueueManager = serviceFactory.CreateProxy<IProductionQueueManager>())

        {

            try

            {

                MassProductionQueueResult result =

                    await productionQueueManager.MassCancelAsync(databaseToken);



                // Do something, like display information about result of the mass operation.

                Console.WriteLine("Out of {0} jobs requested to cancel, {1} were successful.",

                    result.TotalJobsRequested,

                    result.TotalJobsSuccessful);

                Console.WriteLine("Errors for the overall mass operation: {0}",

                    string.Join("; ", result.Errors));

                foreach (ProductionQueueResult jobResult in result.ProductionQueueResults)

                {

                    if (jobResult.RequestSent)

                    {

                        Console.WriteLine("Successfully canceled job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when canceling job ID {0} for production ID {1} in workspace ID {2}",

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

## Cancel production jobs by ID

Use the MassCancelProductionJobsAsync() method to cancel multiple production jobs by production ID. Pass a list of ProductionJobRef objects with the following properties to this method:

- WorkspaceID - the Artifact ID of the workspace containing the production job.

- ProductionID - the Artifact ID of the production.

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
public partial class Example

{

    public async Task MassCancelProductionJobs_Example()

    {

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionQueueManager productionQueueManager = serviceFactory.CreateProxy<IProductionQueueManager>())

        {

            try

            {

                List<ProductionJobRef> productionJobRefs = new List<ProductionJobRef>

                {

                    new ProductionJobRef

                    {

                        WorkspaceID = 100,

                        ProductionID = 200

                    },

                    new ProductionJobRef

                    {

                        WorkspaceID = 101,

                        ProductionID = 201

                    }

                };

                MassCancelResult result =

                    await productionQueueManager.MassCancelProductionJobsAsync(productionJobRefs);



                // Do something, like display results

                Console.WriteLine("Out of {0} jobs requested to cancel, {1} were successful.",

                    result.NumberOfJobsRequestedForCancel,

                    result.NumberOfJobsCancelWasRequestedSuccessfully);

                Console.WriteLine("Errors for the overall mass operation: {0}",

                    string.Join("; ", result.Errors));

                foreach (CancelJobResult jobResult in result.CancelJobResults)

                {

                    if (jobResult.CancelSuccessfullySent)

                    {

                        Console.WriteLine("Successfully canceled job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when canceling job ID {0} for production ID {1} in workspace ID {2}",

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

## Set the priority on production jobs

Use the MassPrioritizeAsync() method to set the priority on a collection of production jobs in the queue by using a mass operation token. This token is a GUID that represents the collection of jobs.

Pass the following arguments to this method:

- databaseToken - a GUID representing a collection of production jobs in the queue.

- priority - an integer value representing the new priority to assign to the jobs.

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

    public async Task MassPrioritize_Example()

    {

        string databaseToken = "1e51ae24-bbcb-4b61-aafb-1f91859d9891"; // GUID representing the collection of selected production jobs for the mass operation

        int priority = 10; // New priority value to assign to selected production jobs

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password

        var relativityRestUri = "http://localhost/relativity.rest/api";

        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);

        using (IProductionQueueManager productionQueueManager = serviceFactory.CreateProxy<IProductionQueueManager>())

        {

            try

            {

                MassProductionQueueResult result =

                    await productionQueueManager.MassPrioritizeAsync(databaseToken, priority);

                // Do something, like display information about result of the mass operation.

                Console.WriteLine("Out of {0} jobs requested to prioritize, {1} were successful.",

                    result.TotalJobsRequested,

                    result.TotalJobsSuccessful);

                Console.WriteLine("Errors for the overall mass operation: {0}",

                    string.Join("; ", result.Errors));

                foreach (ProductionQueueResult jobResult in result.ProductionQueueResults)

                {

                    if (jobResult.RequestSent)

                    {

                        Console.WriteLine("Successfully set priority for job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when setting priority for job ID {0} for production ID {1} in workspace ID {2}",

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

## Retry production jobs by mass operation token

Use the MassRetryAsync() method to rerun multiple production jobs by using a mass operation token. This token is a GUID that represents the collection of jobs.

Pass a GUID representing a collection of production jobs that you want to retry to this method.

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
public partial class Example

{

    public async Task MassRetry_Example()

    {

        string databaseToken = "1e51ae24-bbcb-4b61-aafb-1f91859d9891"; // GUID representing the collection of selected production jobs for the mass operation



        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionQueueManager productionQueueManager = serviceFactory.CreateProxy<IProductionQueueManager>())

        {

            try

            {

                MassProductionQueueResult result =

                    await productionQueueManager.MassRetryAsync(databaseToken);



                // Do something, like display information about result of the mass operation.

                Console.WriteLine("Out of {0} jobs requested to retry, {1} were successful.",

                    result.TotalJobsRequested,

                    result.TotalJobsSuccessful);

                Console.WriteLine("Errors for the overall mass operation: {0}",

                    string.Join("; ", result.Errors));

                foreach (ProductionQueueResult jobResult in result.ProductionQueueResults)

                {

                    if (jobResult.RequestSent)

                    {

                        Console.WriteLine("Successfully retried job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when retrying job ID {0} for production ID {1} in workspace ID {2}",

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

## Retry production jobs by ID

Use the RetryProductionJobsAsync() method to rerun multiple production jobs by ID. Pass a list of ProductionJobRef objects with the following properties to this method:

- WorkspaceID - the Artifact ID of the workspace containing the production job.

- ProductionID - the Artifact ID of the production job.

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
public partial class Example

{

    public async Task RetryProductionJobs_Example()

    {

        var userEmail = "user@test.com"; // User login

        var password = "abc123456!"; // User password



        var relativityRestUri = "http://localhost/relativity.rest/api";



        var usernamePasswordCredentials = new UsernamePasswordCredentials(userEmail, password);

        ServiceFactorySettings settings = new ServiceFactorySettings(

            new Uri(relativityRestUri),

            usernamePasswordCredentials);

        ServiceFactory serviceFactory = new ServiceFactory(settings);



        using (IProductionQueueManager productionQueueManager = serviceFactory.CreateProxy<IProductionQueueManager>())

        {

            try

            {

                List<ProductionJobRef> productionJobRefs = new List<ProductionJobRef>

                {

                    new ProductionJobRef

                    {

                        WorkspaceID = 100,

                        ProductionID = 200

                    },

                    new ProductionJobRef

                    {

                        WorkspaceID = 101,

                        ProductionID = 201

                    }

                };

                MassRetryResult result =

                    await productionQueueManager.RetryProductionJobsAsync(productionJobRefs);



                // Do something, like display results

                Console.WriteLine("Out of {0} jobs requested to retry, {1} were successful.",

                    result.NumberOfJobsRequestedForRetry,

                    result.NumberOfJobsRetryWasRequestedSuccessfully);

                Console.WriteLine("Errors for the overall mass operation: {0}",

                    string.Join("; ", result.Errors));

                foreach (RetryJobResult jobResult in result.RetryJobResults)

                {

                    if (jobResult.RetrySuccessfullySent)

                    {

                        Console.WriteLine("Successfully retried job ID {0} for production ID {1} in workspace ID {2}",

                            jobResult.JobID, jobResult.ProductionID, jobResult.WorkspaceID);

                    }

                    else

                    {

                        Console.WriteLine("Error(s) occurred when retrying job ID {0} for production ID {1} in workspace ID {2}",

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

On this page

- Production Queue Manager (.NET)

- Fundamentals for the Production Queue Manager API

- Cancel a production job

- Cancel production jobs by mass operation token

- Cancel production jobs by ID

- Set the priority on production jobs

- Retry production jobs by mass operation token

- Retry production jobs by ID


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
