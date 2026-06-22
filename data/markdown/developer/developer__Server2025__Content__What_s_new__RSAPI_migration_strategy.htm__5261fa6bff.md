---
title: "RSAPI migration strategy"
url: https://platform.relativity.com/Server2025/Content/What_s_new/RSAPI_migration_strategy.htm
collection: developer
fetched_at: 2026-06-22T06:33:08+00:00
sha256: fda564feb07b5f70a518d4e80981d24d7cc13f2a93d8bb8d36694a171418ba4f
---

RSAPI migration strategy

# RSAPI migration strategy

Use the information on this page to learn more about our migration strategy and API usage, as well as about significant differences between the RSAPI and the newer services available as part of the Relativity platform.

Before you continue reading, review the following information:

- The following information is provided for developers who are familiar with writing applications using the RSAPI. For information on REST calls and the CRUD operations using the Object Manager service, see Basic REST API concepts and Object Manager Fundamentals .

- The deprecation of the RSAPI includes changes to load balancing APIs. For more information, see Upgrade considerations for Relativity .

## Migration strategy and API usage

Our recommended migration strategy is based on considering API usage at a feature-to-feature workflow. For example, the Field DTO in the RSAPI is similar to the functionality provided by the Field Manager service. The following sections on this page describe the design differences between the RSAPI and the newer Services APIs surfaces.

You can find a comparison of these APIs in the API migration matrix . See the following related pages for a complete list of both APIs:

- Relativity Services API (RSAPI) - includes all endpoints in the kCura.Relativity.Client assembly. For details, see the following pages:

- RSAPI reference for .NET

- RSAPI reference for REST

- Services APIs - includes the newer Services APIs. For details, see the following pages:

- Relativity Services in .NET

- Relativity Server APIs

## Transition from RSAPI repositories to the Services APIs interfaces

Review the differences between these RSAPI repositories and the newer Services APIs interfaces:

- RSAPI repositories - The RSAPI utilizes one service proxy that distinguishes between objects using the DTOs contained in repositories within the proxy. Each DTO encapsulates the information for the Relativity object that you are manipulating.

- Services APIs - The newer Services APIs interfaces utilize separate services for each of its surfaces. Relativity objects are distinguished by the contracts passed to the proxy.

The setup for making calls to the proxy is different for RSAPI repositories and the newer Services APIs. For information about how proxies are instantiated, see the following sections:

- Establish a proxy

- Sample code for operations on the Object Manager service

In the newer Services APIs, separating the APIs into different services means that each is independently versioned and owned. Each service also has its own life cycle.

## Contract differences between RSAPI and the Services APIs interfaces

The newer Services APIs interfaces use reference classes to identify objects in Relativity, such as Fields, Object Types, and others. They are described as follows:

- Each Ref class signifies only one Relativity object.

- Ref classes are stored in the Relativity.Services.Objects.DataContracts library.

The following table includes Ref classes commonly used in the newer Services APIs:

Ref class name Description

ObjectTypeRef Reference a single object type. You can create ObjectTypeRefs using Artifact Type IDs, GUIDs, or names.

RelativityObjectRef References a specific instance of a Relativity object using Artifact ID or GUID.

ObjectRefValuesPair Associates an object with a list of field values. This class is often used in mass updates to overlay a list of values on an object.

FieldRef References a field by GUID, name, or Artifact ID.

FieldRefValuePair Combines a FieldRef with a value. It's often used in update and create calls to modify the value of a field.

## Establish a proxy

RSAPI utilizes a single service proxy that distinguishes between endpoints by repositories. The newer Services APIs utilize a separate proxy for each service.

## Use the Object Manager service for CRUDQ operations

The Object Manager service is the primary interface for individual and mass CRUDQ operations on documents and RDOs. It is also the primary interface for querying all objects, not only documents and RDOs. For more information, see the following resources:

- Object Manager Fundamentals - provides a general introduction to using the Object Manager service.

- Sample code for operations on the Object Manager service - contains sample code illustrating how to create a proxy for the newer Services APIs and execute query and create operations through the Object Manager service.

### Query methods

Querying syntax and structure have undergone major changes from RSAPI to the newer Services APIs, which require you to reference the conditions, sorts and fields in new ways. Additionally, the Object Manager service contains the endpoints previously exposed through the RSAPI for querying objects. We recommend using the Object Manager service for querying on any object type. For a sample query using the Object Manager service, see Sample code for operations on the Object Manager service .

Also, see the following resources:

- Query for Relativity objects - provides information about the QueryAsync and QuerySlimAsync endpoints on the Object Manager service and how to use them.

- Query for resources - describes how to write complex query conditions.

### Mass update methods

The workflows for mass updates have been modified to include these methods:

- MassUpdateByCriteria() method - updates any objects that meet the specified criteria.

- MassUpdateByObjectIdentifiers() method - takes a list of objects and updates them with the specified values. Each object is populated with the same values. This endpoint doesn't allow different values per object.

- MassUpdatePerObject() method - functions similarly to the MassUpdateByObjectIdentifiers() method, except that you can provide different values for each object. By supporting a unique list of values for each object, this endpoint offers finer control over the updates to each field.

For more information and code samples, see Mass update Document objects or RDOs .

### Mass create method

The mass create operation has been substantially improved since RSAPI. Migrating to the newer Services APIs involves a significant change in the data contracts and workflows used to interact with them.

The CreateAsync() method takes a list of fields and nested lists of values that are arranged in the same order as the field list. See the following resources:

- Sample code for operations on the Object Manager service - contains a sample create operation using the Object Manager service.

- Mass create RDOs - contains detailed information about how to use the CreateAsync() method.

## Sample code for operations on the Object Manager service

The following sample code illustrates how to perform the following operations with the newer Services APIs and the Object Manager service:

- Create objects from different types of Ref classes.

- Return a new ServiceFactory object for creating proxies.

- Perform queries using the QueryAsync() method on the Object Manager service.

- Create multiple RDOs in a mass operation through the Object Manager service.

- Create a single RDO through the Object Manager service.

To download a copy of the .CS file with this sample code, click ObjectManagerServiceSamples.zip .

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
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
using System;

using System.Collections.Generic;

using System.Linq;

using System.Threading.Tasks;

using Relativity.Services.Objects;

using Relativity.Services.Objects.DataContracts;

using Relativity.Services.ServiceProxy;

namespace Services_API_Samples

{

    class ObjectManagerServiceSamples

    {

        static async void Main()

        {

            ServiceFactory _serviceFactory = GetNewServiceFactory();

            using (IObjectManager objectManager = _serviceFactory.CreateProxy<IObjectManager>())

            {

                await SampleQuery(objectManager, 1234567);

                await SampleMassCreate(objectManager, 1234567);

                await SampleSingleCreate(objectManager, 1234567);

            }

        }

        private static readonly Guid _myObjectGuid = new Guid("5e61283e-34ca-4903-8c04-dfd3553aeaec");

        private static readonly Guid _myNameFieldGuid = new Guid("9427DDDB-1096-4192-8085-302B3268AB22");

        private static readonly Guid _mySampleWholeNumberFieldGuid = new Guid("123e4567-e89b-12d3-a456-426614174000");

        private static readonly Guid _mySampleSingleObjectFieldGuid = new Guid("f684e5f3-250b-4d91-8114-261da7e535d1");

        private static readonly Guid _myDateFieldGuid = new Guid("0D4C634A-20C8-4201-9EDB-587534D00582");

        // Create ObjectTypeRef for the Object Type to target with operations, see "Major Contract Differences"

        static ObjectTypeRef myArtifactType = new ObjectTypeRef { Guid = _myObjectGuid};

        // Create FieldRefs for the fields to utilize, see "Major Contract Differences"

        static FieldRef myNameFieldRef = new FieldRef { Guid = _myNameFieldGuid };

        static FieldRef myWholeNumberFieldRef = new FieldRef { Guid = _mySampleWholeNumberFieldGuid };

        static FieldRef mySingleObjectRef = new FieldRef { Guid = _mySampleSingleObjectFieldGuid };

        static FieldRef myDateFieldRef = new FieldRef { Guid = _myDateFieldGuid };

        // Helper function to return a new Service Factory

        public static ServiceFactory GetNewServiceFactory()

        {

            String restServerAddress = "{my_company_name}/Relativity.Rest/Api";

            string servicesAddress = "{my_company_name}/Relativity.Services";

            Uri keplerUri = new Uri(restServerAddress);

            Uri servicesUri = new Uri(servicesAddress);

            ServiceFactorySettings settings = new ServiceFactorySettings(

                servicesUri, keplerUri, new Relativity.Services.ServiceProxy.UsernamePasswordCredentials("username", "password"));

            Relativity.Services.ServiceProxy.ServiceFactory serviceFactory = new ServiceFactory(settings);

            return serviceFactory;

        }

        public static async Task<bool> SampleQuery(IObjectManager objectManager, int workspaceId)

        {

            //Set up the primary parameters of the search

            const int indexOfFirstDocumentInResult = 1;

            const int lengthOfResults = 100;

            string condition = "('Name' LIKE 'SampleString' AND 'SampleWholeNumberField' == 4) OR ('UserField' LIKE USER 'Last, First')";

            var sort = new Relativity.Services.Objects.DataContracts.Sort()

            {

                Direction = Relativity.Services.Objects.DataContracts.SortEnum.Descending,

                FieldIdentifier = myNameFieldRef

            };

            // Create a request object

            var queryRequest = new QueryRequest()

            {

                Condition = condition,

                // Use FieldRef objects to identify which fields to return

                Fields = new List<FieldRef> {

                        myNameFieldRef, myWholeNumberFieldRef, mySingleObjectRef

            },

                ObjectType = myArtifactType,

                Sorts = new List<Relativity.Services.Objects.DataContracts.Sort> { sort }

            };

            // Pass the QueryRequest to the Object Manager in the data access layer

            try

            {

                Relativity.Services.Objects.DataContracts.QueryResult results = await objectManager.QueryAsync(workspaceId, queryRequest, indexOfFirstDocumentInResult, lengthOfResults);

                Console.Write(String.Format("{0} result(s) returned, beginning at index {1}:\n", results.TotalCount.ToString(), results.CurrentStartIndex.ToString()) + String.Concat(results.Objects.Select(o => o.ArtifactID.ToString() + "\n")));

                return true;

            }

            catch (Exception e)

            {

                Console.Write(e);

                return false;

            }

        }

        public static async Task<bool> SampleMassCreate(IObjectManager objectManager, int workspaceId)

        {

            // Instantiate new mass create request

            MassCreateRequest massCreateRequest = new MassCreateRequest();

            // Specify Object Type to create

            massCreateRequest.ObjectType = myArtifactType;

            // Create list of fields to populate on create

            List<FieldRef> massCreateRequestFieldList = new List<FieldRef>()

            {

                        myNameFieldRef, myWholeNumberFieldRef, myDateFieldRef

            };

            // Set the values for the new RDOs' fields, the helper function below creates your List

            List<List<Object>> massCreateRequestValueList = generateMassCreateRequestValueList();

            massCreateRequest.Fields = massCreateRequestFieldList;

            massCreateRequest.ValueLists = massCreateRequestValueList;

            // Pass your massCreateRequest to the Object Manager in the data access layer

            try

            {

                MassCreateResult results = await objectManager.CreateAsync(workspaceId, massCreateRequest);

                Console.Write(results.Message + "\n" + String.Concat(results.Objects.Select(o => o.ArtifactID.ToString() + "\n")));

                return true;

            }

            catch (Exception e)

            {

                Console.Write(e);

                return false;

            }

        }

        public static async Task<bool> SampleSingleCreate(IObjectManager objectManager, int workspaceId)

        {

            // Instantiate Field Values for Create

            var myDateFieldRefValuePair = new FieldRefValuePair

            {

                Field = myDateFieldRef,

                Value = DateTime.Now

            };

            var myNameFieldRefValuePair = new FieldRefValuePair

            {

                Field = myNameFieldRef,

                Value = "Object Name"

            };

            // Instantiate a CreateRequest

            var createRequest = new CreateRequest();

            // Populate the CreateRequest with Object Type and FieldRefValuePairs

            createRequest.ObjectType = myArtifactType;

            createRequest.FieldValues = new List<FieldRefValuePair> { myDateFieldRefValuePair, myNameFieldRefValuePair };

            // Pass your CreateRequest to the Object Manager in the data access layer

            try

            {

                CreateResult result = await objectManager.CreateAsync(workspaceId, createRequest);

                Console.Write(String.Format("Object successfully created: Artifact ID: {0}",

                result.Object.ArtifactID.ToString()));

            }

            catch (Exception e)

            {

                Console.Write(e);

                return false;

            }

            return true;

        }

        public static List<List<Object>> generateMassCreateRequestValueList()

        {

            //Assign number of RDOs to create

            int numberOfRdosToCreate = 50;

            // Instantiate Value List

            List<List<Object>> ValueListToReturn = new List<List<Object>> { };

            // Populate each row for passing to the mass create request

            for (int i = 0; i < numberOfRdosToCreate; i++)

            {

                List<Object> rdoValueList = new List<object> { };

                rdoValueList.Add($"Name {((char)i).ToString()}");

                rdoValueList.Add(i);

                rdoValueList.Add(DateTime.UtcNow);

                //Append list to mass create request value list, note that the order of field values in this list to create is the same as in the massCreateRequestFieldList above

                ValueListToReturn.Add(rdoValueList);

            }

            return ValueListToReturn;

        }

    }

}
```
