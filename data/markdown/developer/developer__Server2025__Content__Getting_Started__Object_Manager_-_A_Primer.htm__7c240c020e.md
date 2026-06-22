---
title: "Object Manager Fundamentals"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Object_Manager_-_A_Primer.htm
collection: developer
fetched_at: 2026-06-22T06:21:55+00:00
sha256: 645c863accd3192e932f527662c15a77d96aee3330b048bfcb78f902343a7817
---

Object Manager Fundamentals

# Object Manager Fundamentals

The Object Manager API supports CRUD and query operations on Relativity Dynamic Objects (RDOs). It also includes functionality for executing mass operations, exporting large numbers of objects, progress and cancellation tokens, and interacting with event handlers. Use the information on this page to quickly learn about using the Object Manager API through .NET and the Object Manager service through REST.

See these related pages:

- Object Manager (.NET)

- Object Manager (REST)

- Relativity Application Framework

- Query for resources

- Relativity DevHelp Community

## Sample use cases

You can use the Object Manager service to complete a variety of tasks with Relativity objects as follows:

- Create RDOs and set values on their associated fields. See Create an RDO and its specified fields .

- Update fields on Document objects or RDOs. Modify the field types currently available on a Relativity object, including currency, date, user, and others. See Update field values on a Document object or RDO .

- Retrieve a list of dependent objects before deleting one or more objects. See Retrieve a list of object dependencies .

- Perform mass CRUD operations against Documents or RDOs. See Mass create RDOs , Mass update Document objects or RDOs , or Mass delete Document objects or RDOs .

- Query for Workspaces, Documents, RDOs, and system types. See Query for Relativity objects .

- Export objects. See Export API .

## Required references

The Relativity.ObjectManager.SDK is a NuGet package that contains the necessary references for running Object Manager API outside an extensibility point, such as an agent, custom page, or event handler. To use the Object Manager in Relativity with extensibility points, you need to add the appropriate extensibility point package.

The Object Manager API requires references to the following libraries:

- Relativity.Services.ServiceProxy - contains classes used to connect to Object Manager API to outside extensibility points. Use this reference if you are running your program outside of Relativity.

- kCura.<your extensibility point> - contains helper classes used to connect to the APIs inside extensibility points. Use one or more of the following references for your extensibility point if you are running your program in Relativity:

- kCura.EventHandler.dll

- Relativity.CustomPages.dll

- kCura.Agent.dll

- Relativity.Services.Objects.DataContracts - contains classes used for basic Object Manager API functionality, such as passing data to the APIs.

- Relativity.Services.Objects - contains classes used to establish an instance of Object Manager service.

## Creating a connection to the service

Before creating a connection to the Object Manager service, determine whether your program runs as an external application, or within Relativity extensibility point, such as an agent, custom page, or event handler. If your program runs in an extensibility point, connect to the Object Manager service using the helper class in the kCura library for your extensibility point. See Required references .

Copy

```text
1
2
3
4
5
var serviceManager = ConnectionHelper.Helper().GetServicesManager();

using (IObjectManager objectManager = serviceManager.CreateProxy<IObjectManager>())

{

   // Do work with the objectManager instance.

}
```

If your program runs outside of a Relativity extensibility point, connect to the Object Manager service using a service factory as follows:

- In the sample code, replace the URI, username, and password with values for your environment.

- Use the appropriate authentication for the logging in. See Login Profile Manager (.NET) .

- Verify whether you are using HTTP or HTTPS.

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
Uri restUri = new Uri("https://example.url/Relativity.REST/api");

Credentials credentials = new UsernamePasswordCredentials("exampleusername@relativity.com", "examplepassword");

ServiceFactorySettings settings = new ServiceFactorySettings(restUri, credentials);

ServiceFactory factory = new ServiceFactory(settings);

using (IObjectManager objectManager = factory.CreateProxy<IObjectManager>())

{

    // Do work with the objectManager instance.

}
```

## Object Manager service in .NET versus REST

You can use the Object Manager service exposes many of the same features through .NET and REST. Review the following considerations for using the Object Manager service:

- Use the service through .NET if you are comfortable with this technology. You can use C# or VB.Net for coding your projects.

- Use the service through .NET if you want to access tokens for controlling the progress of long operations. The REST service does not support this functionality.

- Use the service through REST if you are developing applications for mobile environments or if you need platform or language independence.

## CRUDQ operations in Object Manager service

The Object Manager service supports the following operations:

- Create - use the CreateAsync() method for creating single objects. It supports creating single objects and firing PreSave and PostSave event handlers. The results contain the status of every fired event handler. The Object Manager API is the method for managing and aggregating the responses for all associated event handlers.

- Read - ReadAsync() method returns the values for specified fields on an object. The result includes all PreLoad event handler statues and an ObjectVersionToken used in overwrite protection.

- Update - UpdateAsync() method alters specified fields. The results of this method include all statuses of any PreSave and PostSave event handlers fired.

- Delete - The DeleteAsync() method deletes an object and its child objects, and unlinks all associations created through single or multiple object fields. To preview the changes resulting from a delete operation, make a call using the GetDependencyListAsync() method. This method fires PreCascadeDelete event handlers before PreDelete handlers. See Retrieve a list of object dependencies .

- Query - The QueryAsync() and QuerySlimAsync() methods both retrieve objects based on a set of conditions. For more information, see Calls to QueryAsync() versus QuerySlimAsync() methods .

## Calls to QueryAsync() versus QuerySlimAsync() methods

The Object Manager service exposes the Query() and QuerySlim() methods through .NET and REST. These methods take identical inputs and return a set of objects from Relativity. They differ by the amount and formatting the data returned. Review these suggestions for determining when to use each method:

- Query() method - returns detailed information about the field-value pairs in the results. You can understand each object in its entirety without any additional context, which results in the Field definitions being repeated across each element. Use this method under the following conditions:

- You are processing the return objects.

- You require the GUIDs associated with each object.

- You are using the .NET proxy then the QueryAsync endpoint is preferable.

- QuerySlim() method - returns less information about the returned field-value pairs. For performance reasons, it is often the preferred method for consumption via HTTP. Use this method under the following conditions:

- Your application is sensitive to payload size.

- You want to use the query in the UI.

- You are making REST calls then the QuerySlimAsyc endpoint is preferable.

For more information, see Object Manager (.NET) and Object Manager (REST) .

## Sample .NET and REST calls

Review the sample code in this section to learn about making calls through .NET and REST to endpoints on the Object Manager service. These examples use the QueryAsync endpoint to return a list of RDOs that satisfy a compound condition. The query specifies three fields on the RDOs to return. The list is sorted in descending order by name.

For reference purposes, these examples pass the fields to the API by using their associated GUID, Artifact ID, and Name. While you can use any of these identifiers, we recommend using GUIDs for application development because they are constant across all Relativity instances and support exporting applications.

### .NET coding sample

- Create a function to hold your asynchronous calls.

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
    class Program

    {

        static void Main(string[] args)

        {

            try

            {

                MainAsync(args).Wait();

            }

            catch(exception e)

            {

                Console.WriteLine(e);

            }

        }

        public static async Task MainAsync(string[] args)

        {

            // Call your asynchronous functions here!

            CRUDQSamples objectManager = new CRUDQSamples();

            var result = await objectManager.QueryAsync();

        }

      }
```

- Create a helper function to return a service factory used to connect to Object Manager service.

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
using System;

using System.Net.Http;

using Relativity.Services.ServiceProxy;

class HttpRequests

{

    public ServiceFactory getNewServiceFactory()

    {

        String restServerAddress = $"http://{yourURL}/relativity.rest/api";

        Uri keplerUri = new Uri(restServerAddress);

        ServiceFactorySettings settings = new ServiceFactorySettings(

           keplerUri, new Relativity.Services.ServiceProxy.UsernamePasswordCredentials("username", "password"));

        Relativity.Services.ServiceProxy.ServiceFactory _serviceFactory = new Relativity.Services.ServiceProxy.ServiceFactory(settings);

        return _serviceFactory;

    }

}
```

- Construct your query and pass it to the Object Manager service.

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
using System;

using System.Collections.Generic;

using System.Threading.Tasks;

using Relativity.Services.ServiceProxy;

using Relativity.Services.Objects.DataContracts;

using Relativity.Services.Objects;

class CRUDQSamples

{

    HttpRequests createClients = new HttpRequests();

    //This query performs an asynchronous operation when it sends the QueryRequest to Relativity.  To accommodate this, we will describe our function as ‘async’ and it will return a Task. Remember to await this function when you invoke it.

    public async Task<Relativity.Services.Objects.DataContracts.QueryResult> QueryAsync()

    {

        ServiceFactory _serviceFactory = createClients.getNewServiceFactory();

        // Set up the primary parameters of the search

        int workspaceId = 1017385;

        // Pass the artifact type ID. This is not the same number as the ArtifactID! It is the ID for object type (Documents are always artifact typeID 10)

        var artifactTypeId = new Relativity.Services.Objects.DataContracts.ObjectTypeRef { ArtifactTypeID = 1000043 };

        const int indexOfFirstDocumentInResult = 1;

        const int lengthOfResults = 100;

        // Conditions are passed in a SQL like string that allows for composite queries. This queries text, whole number and User field types.

        string condition = "('Name' LIKE 'SampleString' AND 'SampleWholeNumberField' == 4) OR ('UserField' LIKE USER 'Last, First')";

        var sort = new global::Relativity.Services.Objects.DataContracts.Sort()

        {

            Direction = global::Relativity.Services.Objects.DataContracts.SortEnum.Descending,

            FieldIdentifier = new FieldRef { Guid = new Guid("DB7A78AC-44C1-4E45-9A49-AED1D1CE24B0") }

        };

        // Create a request object with the parameters

        var queryRequest = new QueryRequest()

        {

            Condition = condition,

            // FieldRef objects can identify which fields to return by Guid, ArtifactID, or Name

            Fields = new List<FieldRef> {

                        new FieldRef { Guid = new Guid("9427DDDB-1096-4192-8085-302B3268AB22") },

                        new FieldRef { ArtifactID = 1039519 },

                        new FieldRef { Name = "FieldName" }

                    },

            RelationalField = null,

            ObjectType = artifactTypeId,

            Sorts = new List<Relativity.Services.Objects.DataContracts.Sort> { sort },

        };

        try

        {

            // Pass your parameters to Object Manager in the data access layer

            using (IObjectManager objectManager = _serviceFactory.CreateProxy<IObjectManager>())

            {

                return await objectManager.QueryAsync(workspaceId, queryRequest, indexOfFirstDocumentInResult, lengthOfResults);

            }

        }

        catch (Exception e)

        {

            Console.Write(e);

            return null;

        }

    }

}
```

### REST coding sample

- Set the endpoint to make a query request. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/{your Relativity URI}/Relativity.REST/api/Relativity.Objects/workspace/{target WorkspaceID}/object/query
```

- Add the required headers to your request. For more information, see HTTP headers or Basic REST API concepts .

- Authorization header - this header uses Base64 encoding of your username and password in the format, which requires a colon:

Copy

```text
1
Username:Password
```

- X-CSRF-header - Leave this header blank.

- Content-Type header - set this header to application/json .

- Construct the request body using a JSON object that contains your parameters.

The sort direction represented by 1 is descending and 0 is ascending.

View request body Copy

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
{

   "Request":{

      "ObjectType":{

         "Guid":"60A89BD1-87D7-46B3-B8FD-0C701FE379BD"

      },

      "fields":[

         {

            "Guid":"9427DDDB-1096-4192-8085-302B3268AB22"

         },

         {

            "ArtifactID":1039519

         },

         {

            "Name":"Winner"

         }

      ],

      "condition":"('Name' LIKE 'SampleString' AND 'SampleWholeNumberField' == 4) OR ('UserField' LIKE USER 'LastName, FirstName')",

      "sorts":[

         {

            "Direction":1,

            "FieldIdentifier":{

               "Guid":"DB7A78AC-44C1-4E45-9A49-AED1D1CE24B0"

            }

         }

      ]

   },

   "start":0,

   "length":100

}
```
