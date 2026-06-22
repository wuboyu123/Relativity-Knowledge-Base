---
title: "Object Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Manager/Object_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:24:13+00:00
sha256: c1dd482d40bdb9d7182bdf9a2036a08e477e1092a142b3f855436041b4ae9b33
---

Object Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Object Manager (REST)

Relativity applications contain system objects and Relativity Dynamic Objects (RDOs). System objects are predefined and included in applications default by default. RDOs are custom objects that you can define for your specific business needs through the UI or programmatically. For information about using objects through the UI, see Relativity Objects .

The Object Manager service provides you with the ability to programmatically work with RDOs and Document objects. It exposes endpoints for performing the following tasks:

- Create RDOs and set values on their associated fields.

- Update fields on Document objects or RDOs. Modify the field types currently available on a Relativity object, including currency, date, user, and others.

- Read fields on Document objects or RDOs.

- Retrieve a list of dependent objects prior to deleting a specific object.

- Perform mass operations to create RDOs, and to update and delete Document objects or RDOs.

- Query for Workspaces, Documents, RDOs, system types, and all Relativity Objects.

- Export objects.

Sample use cases for the Object Manager service include:

- Modifying and saving coding decisions or changes to attorney's notes.

- Searching for object data, which you display in the Relativity UI or use for other purposes in your applications. For example, use this service to populate data that appears in the list views.

You can also use the Object Manager service through .NET, which supports the use of progress indicators and cancellation tokens for queries. For more information, see Object Manager (.NET) .

## Guidelines for the Object Manager service

Review the following guidelines for working with this service.

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the service. To download the sample file, click Object Manager Postman file .

Click to view more information.

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

You interact with the Object Manager service by sending an HTTP request that uses the POST method. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/
```

You can use the following .NET code samples as the REST client for making calls with the Object Manager service.

View sample code

This sample code illustrates how to perform the following tasks for an update operation:

- Instantiate an HttpClient object for sending requests using the URL for the Object Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Initialize variables with values required for updating a field.

- Set the url variable to the URL for the update operation.

- Set the JSON input required for the update operation.

- Use the PostAsync() method to send a post request.

- Return the results of the request and deserialize it.

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
public async Task<UpdateResult> UpdateExample()

{

    UpdateResult result = null;

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization",

            "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/");



        var workspaceId = 1016847;

        var objectArtifactID = 1039331;

        var fieldArtifactID = 1039320;

        var valueToUpdate = "New Value";



        string inputJSON = $"{{\"request\":{{\"Object\":{\"{artifactId\":{objectArtifactID}}},\"FieldValues\":[{{\"Field\":{{\"ArtifactID\":{fieldArtifactID}}},\"Value\":\"{valueToUpdate}\"}}]}}}}}}";



        var url = $"workspace/{workspaceId}/object/update";

        var response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<UpdateResult>(content);

    }

    return result;

}
```

## Create an RDO

To create an RDO with a specific set of fields, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/create
```

View field descriptions for a request

The body of the request for creating an RDO must contain the following fields:

- request - a request object for the create operation with the required fields set.

- ObjectType - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- FieldValues - an array of field value pairs, which contain an identifier for the required field, and a value for it. This field contains the following:

- Field - the Artifact ID, GUID, or name of the required field.

- Value - a value for the field. The type of field determines the requirements for the value that you can assign to it.

- ParentObject - the Artifact ID of the parent object of the for the new RelativityObject.

If you do not specify a parent object, Relativity defaults to the System object as the parent.

View sample JSON request Copy

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
{

   "request":{

      "ObjectType":{

         "ArtifactTypeID":1000042

      },

      "ParentObject":{

         "ArtifactID":1049257

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1039343

            },

            "Value":"Third"

         },

         {

            "Field":{

               "ArtifactID":1039338

            },

            "Value":{

               "ArtifactID":1039441

            }

         },

         {

            "Field":{

               "ArtifactID":1039345

            },

            "Value":[

               {

                  "ArtifactID":1039346

               },

               {

                  "ArtifactID":1039347

               },

               {

                  "ArtifactID":1039350

               }

            ]

         }

      ]

   }

}
```

View field descriptions for a response

The response contains the following fields:

- Object - an instance of a RelatvityObject containing the fields and their values that were created.

- ParentObject - the Artifact ID of the parent object of the newly created RelativityObject. If you did not specify a parent object, Relativity defaults to the System object as the parent.

- FieldValues - an array containing FieldValuePair objects.

- Field - a field associated with a specific value. The Field object contains the following:

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

- ViewFieldID - a unique identifier used to reference a view field.

- Value - the data assigned to a field, represented as an Object type. It contains the following:

- ArtifactID - a unique identifier for the object, which is represented as an integer.

- Guids - an array of GUIDs used to identify the object.

- Name - a user-friendly name for the object.

- ArtifactID - a unique identifier for the RelativityObject instance, which is represented as an integer.

- Guids - an array of GUIDs used to identify the RelativityObject.

- EventHandlerStatuses - an array of EventHandlerStatus objects if any were executed. Each object contains a Boolean value indicating whether the execution was successful, and a string with a related message.

View a sample JSON response Copy

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
{

   "Object":{

      "ParentObject":{

         "ArtifactID":1003663

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1039343,

               "FieldCategory":"Generic",

               "FieldType":"FixedLengthText",

               "Guids":[

               ],

               "Name":"FixedLengthTextField",

               "ViewFieldID":0

            },

            "Value":"Third"

         },

         {

            "Field":{

               "ArtifactID":1039338,

               "FieldCategory":"Generic",

               "FieldType":"SingleObject",

               "Guids":[

               ],

               "Name":"SingleObjectField",

               "ViewFieldID":0

            },

            "Value":{

               "ArtifactID":1039441,

               "Guids":[

               ],

               "Name":"Custom Object 1"

            }

         },

         {

            "Field":{

               "ArtifactID":1039345,

               "FieldCategory":"Generic",

               "FieldType":"MultipleChoice",

               "Guids":[

               ],

               "Name":"MultiChoiceField",

               "ViewFieldID":0

            },

            "Value":[

               {

                  "ArtifactID":1039346,

                  "Guids":[

                  ],

                  "Name":"MultiChoiceField_Choice1"

               },

               {

                  "ArtifactID":1039347,

                  "Guids":[

                  ],

                  "Name":"MultiChoiceField_Choice2"

               },

               {

                  "ArtifactID":1039350,

                  "Guids":[

                  ],

                  "Name":"MultiChoiceField_Choice3"

               }

            ]

         }

      ],

      "ArtifactID":1039443,

      "Guids":[

      ]

   },

   "EventHandlerStatuses":[

   ]

}
```

## Mass create RDOs

You can mass create multiple RDOs of the same type and specify the values set on the fields that they contain. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/create
```

If you specify an identifier that’s already in the database, an exception will not be thrown. Instead, the Success field in the JSON response is set to false. Always check the value of the Success field in the JSON response as a best practice.

View field descriptions for a request

The request must include the following fields:

- massRequest - a request to create multiple RDOs.

- ParentObject - the parent of the RelativityObject instances that you want to create. It contains an ArtifactID field, which uniquely identifies the parent object.

If you do not specify a parent object, Relativity defaults to the System object as the parent.

- ObjectType - indicates the type of objects that you want to create. It contains an ArtifactTypeID field, which contains the Artifact ID used to uniquely identify the object type.

- Fields - an array of Artifact IDs for the Field objects that you want set when the new RelativityObject instances are created. It contains an ArtifactID field for each Field object.

- ValueLists - an array of objects that contain the values used to update the fields on the RelativityObject instances. The order of the values corresponds to the order of the Field objects. In addition to the specified values, each object contains an Artifact ID used to identify it.

View a sample JSON request Copy

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
{

   "massRequest":{

      "ParentObject":{

         "ArtifactID":1003663

      },

      "ObjectType":{

         "ArtifactTypeID":1000043

      },

      "Fields":[

         {

            "ArtifactID":1040132

         },

         {

            "ArtifactID":1041596

         },

         {

            "ArtifactID":1041597

         },

         {

            "ArtifactID":1041598

         }

      ],

      "ValueLists":[

         [

            "Identifier field value 0",

            "dummy value 0",

            25,

            {

               "ArtifactID":1253334

            }

         ],

         [

            "Identifier field value 1",

            "dummy value 0",

            56,

            {

               "ArtifactID":1253324

            }

         ],

         [

            "Identifier field value 2",

            "dummy value 0",

            90,

            {

               "ArtifactID":1253335

            }

         ],

         [

            "Identifier field value 3",

            "dummy value 0",

            14,

            {

               "ArtifactID":1253330

            }

         ],

         [

            "Identifier field value 4",

            "dummy value 0",

            7,

            {

               "ArtifactID":1253322

            }

         ],

         [

            "Identifier field value 5",

            "dummy value 0",

            23,

            {

               "ArtifactID":1253315

            }

         ]

      ]

   }

}
```

View field descriptions for a response

The response contains the following fields:

- Success - a Boolean value indicating whether the operation completed without any errors.

- Message - explanatory information provided when an error occurs.

- Objects - an array of RelativityObjectRef instances constructed by a mass create operation.

- ArtifactID - the unique identifier for a RelativityObject instance.

View a sample JSON response Copy

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
{

   "Success":true,

   "Message":"Created 5 objects.",

   "Objects":[

      {

         "ArtifactID":1238950

      },

      {

         "ArtifactID":1238951

      },

      {

         "ArtifactID":1238952

      },

      {

         "ArtifactID":1238953

      },

      {

         "ArtifactID":1238954

      }

   ]

}
```

## Retrieve field values for a Document object or RDO

To read a specified subset of field values on a Document object or an RDO, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/read
```

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

- Request - a request object for the read operation with the required fields set.

- Object - represents minimal information needed to identify a RelativityObject. It contains the following:

- ArtifactID - the unique identifier for the RelativityObject instance, which contains the fields that you want to retrieve.

- Fields - an array of identifiers for the group of fields that you want to read. It contains the following:

- ArtifactID - a unique identifier for a field, which is represented as an integer. This field is optional if you identify the field by name or GUID.

- Name - the user-friendly name of the field. This field is optional if you identify the field by Artifact ID or GUID.

- Guids - a unique identifier for a field. This field is optional if you identify the field by Artifact ID or name.

- ReadOptions - an optional field that may specify the calling context, the behavior and number of characters for long text fields, and other settings.

- FieldTypesToReturnAsString - a list of object type values which should be returned as strings.

- LongTextBehavior - indicates whether the default or tokenized behavior is used for long text fields that exceed the maximum number of characters set in the MaxCharactersForLongTextValues property. To avoid inadvertently truncating of long text fields, we recommend setting this property to 1 for tokenized behavior when you are reading or querying on long text fields, and then later performing an update operation on the returned values. You can use the default behavior for other operations, such as displaying data in a grid. Before implementing the query operation on a long text field, review the following best practices in Use tokens with long text fields .

View a JSON sample using Artifact IDs to identify fields Copy

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
{

   "Request":{

      "Object":{

         "ArtifactID":1038163

      },

      "Fields":[

         {

            "ArtifactID":1003667

         },

         {

            "ArtifactID":1003668

         },

         {

            "ArtifactID":1003669

         },

         {

            "ArtifactID":1003671

         },

         {

            "ArtifactID":1003672

         }

      ]

   }

}
```

View a JSON sample using names to identify fields Copy

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
{

   "Request":{

      "Object":{

         "ArtifactID":1038163

      },

      "Fields":[

         {

            "Name":"Nonrequired Fixed Length"

         }

      ]

   }

}
```

View a JSON sample using the ReadOptions field Copy

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
{

   "Request":{

      "Object":{

         "ArtifactID":1040284

      },

      "Fields":[

         {

            "ArtifactID":1040299

         },

         {

            "ArtifactID":1040286

         }

      ]

   },

   "ReadOptions":{

      "FieldTypesToReturnAsString":[

         "Decimal",

         "Currency"

      ]

   }

}
```

View field descriptions for a response

The response contains the following fields:

- Message - a string returned by a Pre Load event handler.

- Object - an instance of a RelatvityObject containing fields and their values that were read. It contains the following:

- ParentObject - contains the Artifact ID of the parent object associated with the RelativityObject specified by the read operation.

- ArtifactID - a unique identifier for the object, which is represented as an integer.

- Guid - a unique identifier for the object, which is represented as a GUID.

- Name - the user-friendly name of the RelativityObject.

- FieldValues - an array containing FieldValuePair objects. See Object Manager (.NET) . It contains the following:

- Field - a field associated with a specific value. The Field object includes:

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

- ViewFieldID - a unique identifier used to reference a view field.

- Value - the data assigned to a field, represented as an Object type. It may contain one or more of the following:

- ArtifactID - a unique identifier for the object, which is represented as an integer.

- Guids - an array of GUIDs used to identify the object.

- Name - a user-friendly name for the object.

- ArtifactID - a unique identifier for the RelativityObject instance, which is represented as an integer.

- Guids - an array of GUIDs used to identify the RelativityObject instance.

- ObjectType - contains information about the type of object returned from the read operation. It contains the following fields:

- ArtifactID - a unique identifier for the ObjectType instance, which is represented as an integer.

- Name - a user-friendly name for the object type, such as Document, Field, and others.

- Guids - an array of GUIDs used to identify the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ObjectVersionToken - the version token of the RelativityObject. You can pass this value to an update request to enable record overwrite protection.

View a JSON response with Artifact IDs identifying fields Copy

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

{

   "Message":"",

   "Object":{

      "ParentObject":{

         "ArtifactID":1038155

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1003667,

               "FieldCategory":"Generic",

               "FieldType":"FixedLengthText",

               "Guids":[

                  "2a3f1212-c8ca-4fa9-ad6b-f76c97f05438"

               ],

               "Name":"Control Number",

               "ViewFieldID":0

            },

            "Value":"AZIPPER_0007300"

         },

         {

            "Field":{

               "ArtifactID":1003668,

               "FieldCategory":"Generic",

               "FieldType":"LongText",

               "Guids":[

                  "58d35076-1b1d-43b4-bff4-d6c089de51b2"

               ],

               "Name":"Extracted Text",

               "ViewFieldID":0

            },

            "Value":"From:  Piper  Greg <Greg.Piper@ENRON.com>\r\nSent:  Monday, May 21, 2001 8:25 PM\r\nTo:  Zipper  Andy <Andy.Zipper@ENRON.com>\r\nSubject:  RE: EOL Team Connection to Operations\r\n\r\nI am confident this will work out.\r\n\r\nThanks.\r\n\r\nGP\r\n\r\n -----Original Message-----\r\nFrom: \tZipper, Andy  \r\nSent:\tMonday, May 21, 2001 5:54 PM\r\nTo:\tPiper, Greg\r\nSubject:\tFW: EOL Team Connection to Operations\r\n\r\n\r\nFYI\r\n -----Original Message-----\r\nFrom: \tBeck, Sally  \r\nSent:\tMonday, May 21, 2001 5:39 PM\r\nTo:\tZipper, Andy\r\nSubject:\tEOL Team Connection to Operations\r\n\r\nI left you a couple of messages with two different assistants today for you to call - am sure that it is a busy Monday.  I will send this note so that I don't forget the purpose.  With Savita assuming the role previously played by Sheri with regard to the Product Control group, I wanted to underscore the importance of a free flow of information between the EOL team and my operations team.  One of the roles that Sheri's team fulfilled was keeping my risk and operations teams apprised of any changes within EOL that can have an impact on bridging to our legacy systems.  I may have met Savita once in passing.  I checked with Jeff Gossett and Stacey White, risk leads over gas and power, respectively, and neither one has heard of or met Savita.  Although Jennifer Denney will play an active role, I know that she will be out on maternity leave soon, so it is important for Savita to know the right players on the operations team and for them to know her.  I will contact Savita directly to make the appropriate introductions.  I just wanted your support and encouragement for Savita in making the right connections within operations.  --Sally \r\n\r\nagree\r\n\r\ncontracts\r\n\r\n***********\r\n\r\n***********"

         },

         {

            "Field":{

               "ArtifactID":1003669,

               "FieldCategory":"Generic",

               "FieldType":"FixedLengthText",

               "Guids":[

                  "a426bc5e-3420-47b4-a293-4c4848a237d7"

               ],

               "Name":"MD5 Hash",

               "ViewFieldID":0

            },

            "Value":"5D53A6828FDA554B7E756396E3E54533"

         },

         {

            "Field":{

               "ArtifactID":1003671,

               "FieldCategory":"Generic",

               "FieldType":"FixedLengthText",

               "Guids":[

                  "1f036749-a691-4aa8-8cf7-5eeb80c36caf"

               ],

               "Name":"Group Identifier",

               "ViewFieldID":0

            },

            "Value":"AZIPPER_0007300"

         },

         {

            "Field":{

               "ArtifactID":1003672,

               "FieldCategory":"Generic",

               "FieldType":"SingleChoice",

               "Guids":[

                  "2baaca72-790c-4b87-a7d8-c18c45cac63d"

               ],

               "Name":"Has Images",

               "ViewFieldID":0

            },

            "Value":{

               "ArtifactID":1034244,

               "Guids":[

               ],

               "Name":"No"

            }

         }

      ],

      "ArtifactID":1038166,

      "Guids":[

      ]

   },

   "ObjectType":{

      "ArtifactID":1035231,

      "Name":"Document",

      "Guids":[

         "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ],

      "ArtifactTypeID":10

   }

}
```

View a JSON response with the ReadOptions field Copy

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
{

   "Object":{

      "ParentObject":{

         "ArtifactID":1003663,

         "Guid":"00000000-0000-0000-0000-000000000000"

      },

      "Name":"Test",

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1040286,

               "FieldCategory":"Generic",

               "FieldType":"Decimal",

               "Guids":[

               ],

               "Name":"Decimal",

               "ViewFieldID":0

            },

            "Value":"123456789.99"

         },

         {

            "Field":{

               "ArtifactID":1040299,

               "FieldCategory":"Generic",

               "FieldType":"Currency",

               "Guids":[

               ],

               "Name":"Currency",

               "ViewFieldID":0

            },

            "Value":"123456789.99"

         }

      ],

      "ArtifactID":1040284,

      "Guids":[

      ]

   },

   "ObjectType":{

      "ArtifactID":1040282,

      "Name":"RDO",

      "Guids":[

      ],

      "ArtifactTypeID":1000046

   },

   "ObjectVersionToken":"636806505690930000"

}
```

## Update fields on a Document object or RDO

To update field values on a Document object or RDO, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/update
```

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

The body of the request for updating field values on a Document object or RDO must contain the following fields:

- request - a request object for the update operation with the required fields set.

- Object - contains an identifier for the object with fields that you want to update. It contains the following:

- artifactId - a unique identifier for the object, which is represented as an integer.

- FieldValues - an array containing FieldValuePair objects. See Object Manager (.NET) . It contains the following:

- Field - contains an identifier for the field that you want to update.

- ArtifactID - a unique identifier for the Field object, which is represented as an integer.

- Value - a value for the field. The type of field determines the requirements for the value that you can assign to it.

- OperationOptions - contains information about how the update operation for this request is being called. It includes the following:

- UpdateBehavior - indicates whether you want to replace or merge a choice or object. These options are available for only multiple choice and multiple object fields. See the following sample JSON for these fields.

- CallingContext - information about the web context from which the event handler is being called, such as the originator of the call, the page mode, and the related layout. See Object Manager (.NET) .

You can set the callingContext field to null if your event handlers do not need any context information, but you must include it in the JSON request. Your event handlers must then implement the ICanExecuteWithLimitedContext interface available in the Event Handlers API.

- Layout - contains an identifier for the layout where the update call originates.

- ArtifactID - a unique identifier for the layout, which is represented as an integer.

Click a field type in the following list to view sample JSON and information about the field values.

Currency

For currency fields, the value may contain commas and two decimal places. Currently, the currency field supports only the culture English (United States).

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1039465

            },

            "Value":"5,025.30"

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Date

For date fields, the values must contain dates in the ISO 8601 format listed in the following JSON sample. When you do not explicitly provide an offset, date fields are saved in the database with an offset relative to server location.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1039477

            },

            "Value":"2017-01-22T18:00:00-07:00"

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Decimal

For decimal fields, the values are rounded to the nearest hundredth of a number. Currently, the decimal field supports only the culture English (United States).

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1039489

            },

            "Value":1.05

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

File field

The request must include following fields:

- field - a reference to the field that you want associated with the uploaded file. It contains this field:

- ArtifactID - the Artifact ID of the field.

- objectRef - a reference to the object that contains the uploaded file. It contains this field:

- ArtifactID - the Artifact ID of the object.

- fileName - the name of the uploaded file.

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
{

   "field":{

      "ArtifactID":1098145

   },

   "objectRef":{

      "ArtifactID":1001637

   },

   "fileName":"Sample File"

},
```

Fixed-length text or long text

If you need to update a long text field that exceeds the length limits of an HTTP request, use the updatelongtextfromstream endpoint. For more information, see Update a long text field using an input stream .

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
{

    "request": {

        "Object": {

            "artifactId": 1037989

        },

        "FieldValues": [{

            "Field": {

                "ArtifactID": 1039519

            },

            "Value": "Hello World!"

        }]

    },

    "OperationOptions": {

        "CallingContext": {

            "Layout": { "ArtifactID": 1042963 }

        }

    }

}
```

Multiple choice

When you update a child choice field, its ancestors are also updated. The Behavior field indicates whether you are merging or replacing choices as follows:

- Merge - adds the values that you pass into the service to the current values for the choice field.

- Replace - overwrites the current values for the choice field with those that you pass into the service.

If you do not set the Behavior field, the service throws a ValidationException when attempting an update operation.

The update operation for field values on a multiple object works the same way on a multiple choice field.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1039527

            },

            "Value":[

               {

                  "ArtifactID":1068132

               },

               {

                  "ArtifactID":1068137

               }

            ]

         }

      ]

   },

   "OperationOptions":{

      "UpdateBehavior":"Replace",

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Multiple object

You can either merge or replace multiple objects. The Behavior field indicates whether you are merging or replacing the object field as follows:

- Merge - adds the values that you pass into the service to the current values for the object field.

- Replace - overwrites the current values for the object field with those that you pass into the service.

If you do not set the Behavior field, the service throws a ValidationException when attempting an update operation.

The update operation for field values on a multiple object works the same way on a multiple choice field.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1042109

            },

            "Value":[

               {

                  "ArtifactID":1041033

               },

               {

                  "ArtifactID":1041034

               }

            ]

         }

      ]

   },

   "OperationOptions":{

      "UpdateBehavior":"Replace",

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Single choice

For a single choice field, the value may be defined by an Artifact ID or GUID. It may also be null.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1041044

            },

            "Value":{

               "ArtifactID":1041033

            }

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Single object

For a single object field, the value may be defined by an Artifact ID or GUID. It may also be null.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1041044

            },

            "Value":{

               "ArtifactID":1041033

            }

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

User Copy

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1042069

            },

            "Value":{

               "ArtifactID":1018788

            }

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Whole number

For a whole number field, the value cannot contain decimal places.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1041044

            },

            "Value":1

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

Yes/No

For a Yes/No field, the value may be true, false, or null.

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
{

   "request":{

      "Object":{

         "artifactId":1037989

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1041044

            },

            "Value":true

         }

      ]

   },

   "OperationOptions":{

      "CallingContext":{

         "Layout":{

            "ArtifactID":1042963

         }

      }

   }

}
```

View field descriptions for a response

The response contains the following fields:

- EventHandlerStatuses - contains information about the execution of event handlers during the update operation. It includes a status and an optional string with a related message.

- Success - a Boolean value indicating whether the event handler execution was successful.

View a sample JSON response Copy

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
{

   "EventHandlerStatuses":[

      {

         "Success":true

      },

      {

         "Success":true

      }

   ]

}
```

## Update a long text field using an input stream

You can use the updatelongtextfromstream endpoint to update a single long text field that exceeds the length limits of an HTTP request. This endpoint uses multi-part message for the request, which includes a JSON payload, and a Stream form input. For C# code used to make this request, see Update a long text field using an input stream in .NET .

To call the updatelongtextfromstream endpoint, send a POST request with a URL in the following format:

Copy

```text
1
2

<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/updatelongtextfromstream
```

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

- updateLongTextFromStreamRequest - a request object for the updating a long text field with a stream. It contains the following fields:

- Object - a RelativityObjectRef to be updated. It contains the following:

- ArtifactID - the Artifact ID of an RelativityObjectRef.

- Field - a field to be updated. The Field object contains the following:

- ArtifactID - a unique identifier for the Field object, which is represented as an integer.

- Guid - a GUID used to identify the object.

- Name - the user-friendly name of the field.

- ViewFieldID - a unique identifier used to reference a view field.

View a sample JSON request Copy

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
{

   "updateLongTextFromStreamRequest":{

      "Object":{

         "ArtifactID":1039314

      },

      "Field":{

         "ArtifactID":0,

         "Guid":"",

         "Name":"Extracted Text",

         "ViewFieldID":0

      }

   }

}
```

When the long text field is successfully updated, the response returns the status code of 200.

## Mass update Document objects or RDOs

You can specify the Document objects or RDOs that you want to mass update in the following ways:

- To set the same value on specific fields for a group of objects, perform one of these tasks:

- Use a query to identify the objects that you want to update. Only the objects that match the query conditions are updated. In the Relativity UI, this update operation is equivalent to the user selecting the All option in the mass operations bar on a list page.

To search for data, you can use a variety of query options, including conditions, fields, sorts, and relational fields. These query options have a specific syntax for defining the for defining query conditions. For information about query conditions and options, see Query for resources .

- Provide a list of identifiers for objects that you want to update. Use the Artifact IDs of these objects as identifiers. In the Relativity UI, this update operation is equivalent to the user selecting the Checked or These option in the mass operations bar on a list page.

- To set different values for specific fields on a group of objects, provide a list of fields for updating in the JSON request. This request should also contain a list of Artifact IDs for the objects to be updated, and the respective field values. The values must be in the same order as the fields that you want to update.

Review the following best practices for mass update operations:

- Make sure all the objects in a mass update operation are the same type.

- Use Artifact IDs instead of GUIDs for better performance. In addition, mass update by criteria is the fastest option for updating many objects. See View a JSON request using query conditions .

- Note that the identifier field can’t be updated by any mass update operation.

To execute a mass operation, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/update
```

Click one of the following options to view sample JSON and field descriptions for a mass update operation. For JSON samples showing how to update a specific field type, see Update fields on a Document object or RDO .

View a JSON request using query conditions

The request must contain the following fields:

- massRequestByCriteria - a request to update multiple objects, which match the conditions specified in a query.

- ObjectIdentificationCriteria - contains query conditions and other information used to identify the objects to update:

- ObjectType - contains the Artifact Type ID of an ObjectType. For example, the Artifact Type ID for a Document object is 10.

For a mass update operation, all the objects must be the same type.

- Condition - the search criteria used in the query for items to be updated. For more information, see Query for resources .

- FieldValues - an array of field value pairs, which contain an identifier for the required field, and a value for it. This field contains the following:

- Field - the Artifact ID, GUID, or name of a required field.

- Value - a value for the field. The type of field determines the requirements for the value that you can assign to it.

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
{

   "massRequestByCriteria":{

      "ObjectIdentificationCriteria":{

         "ObjectType":{

            "ArtifactTypeID":1000043

         },

         "Condition":"'ArtifactID' >= 1041396 And 'ArtifactID' < 1041496 "

      },

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1041227

            },

            "Value":23

         }

      ]

   }

}
```

View a JSON request using identifiers

The request must contain the following fields:

- massRequestByObjects - a request to update multiple objects. The request updates the objects based on the identifier that you provide in the Objects field.

- Objects - an array containing the Artifact IDs of Document objects or RDOs for update. The ArtifactID field contains the identifier of an object that you want to update. You can also use GUIDs for this purpose.

For a mass update operation, all the objects must be the same type.

- FieldValues - an array of field value pairs, which contain an identifier for the required field, and a value for it. This field contains the following:

- Field - the Artifact ID, GUID, or name of a required field.

- Value - a value for the field. The type of field determines the requirements for the value that you can assign to it.

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
{

   "massRequestByObjectIdentifiers":{

      "Objects":[

         {

            "ArtifactID":1043610

         },

         {

            "ArtifactID":1043611

         },

         {

            "ArtifactID":1043612

         },

         {

            "ArtifactID":1043613

         },

         {

            "ArtifactID":1043614

         }

      ],

      "FieldValues":[

         {

            "Field":{

               "ArtifactID":1041596

            },

            "Value":"Text field update"

         },

         {

            "Field":{

               "ArtifactID":1041597

            },

            "Value":23

         },

         {

            "Field":{

               "ArtifactID":1041598

            },

            "Value":{

               "ArtifactID":1052345

            }

         }

      ]

   }

}
```

View a JSON request using object identifiers

The request must contain the following fields:

- massRequestPerObjects - a request to update multiple objects. The request updates the objects based on the list of common fields that you identify in the request.

- Fields - an array containing the Artifact IDs of Field objects that you want to update.

- ObjectValues - an array containing the Artifact IDs of objects for updating and the respective values specified in the same order as the Field objects. It contains the following:

- object - the Artifact ID of an object to update.

- values - the values to set on the object's fields.

For a mass update operation, all the objects must be the same type. Make sure that you specify the values in the same order as the Field objects listed in the Fields array.

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
{

   "massRequestPerObjects":{

      "Fields":[

         {

            "ArtifactID":1041596

         },

         {

            "ArtifactID":1041597

         },

         {

            "ArtifactID":1041598

         }

      ],

      "ObjectValues":[

         {

            "object":{

               "ArtifactID":1043610

            },

            "values":[

               "This is Responsive.",

               14,

               {

                  "ArtifactID":1234678

               }

            ]

         },

         {

            "object":{

               "ArtifactID":1043611

            },

            "values":[

               "Witness statement",

               91,

               {

                  "ArtifactID":1234672

               }

            ]

         },

         {

            "object":{

               "ArtifactID":1043612

            },

            "values":[

               "Smoking gun",

               75,

               {

                  "ArtifactID":1234670

               }

            ]

         },

         {

            "object":{

               "ArtifactID":1043613

            },

            "values":[

               "Further review",

               13,

               {

                  "ArtifactID":1234668

               }

            ]

         },

         {

            "object":{

               "ArtifactID":1043614

            },

            "values":[

               "This is Responsive.",

               2,

               {

                  "ArtifactID":1234655

               }

            ]

         }

      ]

   }

}
```

View field descriptions for a response

The response contains the following fields:

- TotalObjectsUpdated - the total number of objects successfully updated.

- Success - a Boolean value indicating whether the operation completed without any errors.

- Message - explanatory information provided when an error occurs.

View a JSON response Copy

```text
1
2
3
4
5
{

   "TotalObjectsUpdated":5,

   "Success":true,

   "Message":""

}
```

## Retrieve a list of object dependencies

The dependency list endpoint retrieves information about Relativity objects dependent on one or more specific objects selected for deletion. It returns information such as the relationship between the objects and whether a dependent object would be deleted or unlinked. For information about the dependency report in the Relativity UI, see Deleting object dependencies .

Sample use cases for this endpoint include:

- Determining whether the delete operation may be blocked by the dependencies on an object selected for deletion.

- Determining how other objects in Relativity may be affected by deleting a one or more objects.

Use these guidelines for calling the dependencylist endpoint:

- Call the endpoint with objects of the same type. If you call the endpoint with objects of different types, it returns an error.

- Call the endpoint only with objects that the user has permission to view. It returns an error if the user does not have view permissions or if any of the objects do not exist.

To call the dependencylist endpoint send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/dependencylist
```

View sample .NET client code

The following .NET code sample illustrates how to make a call to the dependencylist endpoint. Also ,see Client code sample .

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
public async Task<List<Relativity.Shared.{versionNumber}.Models.Dependency>> GetDependencies()

{

    List<Relativity.Shared.{versionNumber}.Models.Dependency> result = null;



    int workspaceArtifactId = 1234567;

    List<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef> objectsToCheck = new List<Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef>

    {

        new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = 2345678 },

        new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = 3456789 },

        new Relativity.ObjectManager.{versionNumber}.Models.RelativityObjectRef { ArtifactID = 4567890 }

    };



    using (HttpClient httpClient = new HttpClient())

    {

        httpClient.BaseAddress = new Uri($"https://localhost/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceArtifactId}/object/");



        // Set the required headers.

        httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");



        string url = "dependencylist";



        var dependencyListRequest = new Relativity.ObjectManager.{versionNumber}.Models.DependencyListByObjectIdentifiersRequest { Objects = objectsToCheck };

        string serializedDependencyListRequestt = Newtonsoft.Json.JsonConvert.SerializeObject(dependencyListRequest);

        string payload = $"{{ \"request\" : {serializedRequest} }}";



        result = await httpClient.PostAsJsonAsync(url, payload);

    }



    return result;

}
```

View field descriptions for a request

The request must include the following fields:

- request - a request for a list of objects dependent on the specified Document objects or RDOs.

- Objects - an array of objects identified by their Artifact IDs.

- ArtifactID -the Artifact ID of an object.

View a sample JSON request Copy

```text
1
2
3
4
5
6
7
8
{

    request: {

        Objects: [

            { ArtifactID: 1234567 },

            { ArtifactID: 1234568 }

        ]

    }

}
```

View field descriptions for a response

The response contains the following fields:

- ObjectType - the type of the Relativity object dependent on the object selected for deletion.

- Secured - indicates whether the current user has permissions to view the setting in the Value field.

- Value - represents a securable value, which is the object type.

- Action - indicates whether a dependent object is deleted or unlinked when a specific object is deleted.

- Count - indicates the number of objects with a dependency on a specific object selected for deletion.

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - represents a securable value, which is the number of dependent objects.

- Connection - indicates whether the object for deletion is a parent, or a field on a single or multiple object field.

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - represents a securable value, which is the type of relationship between the objects. For example, the value is Parent when the dependent object is a child, and Field: {field name} when the dependent object is a field on a single or multiple object field.

- HierarchicLevel - indicates the degree of dependency between object types. For example, you might select an object type for deletion that has a child object type. The fields and views associated with the child object type have a dependency with a hierarchical level of 1.

View a sample JSON response Copy

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
[

   {

      "ObjectType":{

         "Secured":false,

         "Value":"Parent Object Type"

      },

      "Action":"Delete",

      "Count":{

         "Secured":false,

         "Value":2

      },

      "Connection":{

         "Secured":false,

         "Value":"Parent"

      },

      "HierarchicLevel":0

   },

   {

      "ObjectType":{

         "Secured":false,

         "Value":"Child Object Type"

      },

      "Action":"Delete",

      "Count":{

         "Secured":false,

         "Value":3

      },

      "Connection":{

         "Secured":false,

         "Value":"Child of: Parent Object Type"

      },

      "HierarchicLevel":0

   }

]
```

## Delete a Document object or RDO

You can delete a Document object and all its associated files, or an RDO. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/delete
```

View field descriptions for a request

The request must contain the following fields:

- Request - a request object for the delete operation with the required fields set.

- Object - represents minimal information needed to identify a RelativityObject that you want to delete. It contains the following:

- ArtifactID - the unique identifier for a RelativityObject instance.

View a sample JSON request Copy

```text
1
2
3
4
5
6
7
{

   "Request":{

      "Object":{

         "ArtifactID":1051263

      }

   }

}
```

View field descriptions for a response

The response contains the following fields:

- Report - contains a list of one or more DeleteItems objects.

- DeleteItems - information about the items that were removed. The DeleteItems object includes:

- ObjectTypeName - identifies the child or associative object that has a dependency on the object selected for deletion.

- Action - the operation performed to remove the object. Delete is the action for child objects and Unlink is the action for associative objects.

- Count - the number of items removed.

- Connection - indicates a relationship to the object selected for deletion, such as parent, child, and associative object.

View a sample JSON response Copy

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
{

   "Report":{

      "DeletedItems":[

         {

            "ObjectTypeName":"Custom Object",

            "Action":"Delete",

            "Count":1,

            "Connection":"Parent"

         }

      ]

   }

}
```

## Mass delete Document objects or RDOs

You can specify the Document objects or RDOs that you want to mass delete in the following ways:

- Use a query to identify the objects that you want to delete. Only the objects that match the query conditions are deleted.

- Provide a list of identifiers for objects that you want to delete. Use the Artifact IDs of these objects as identifiers.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/delete
```

Click one of the following options to view field descriptions and sample JSON:

View a JSON request using query conditions

The JSON request requires the following fields:

- massRequestByCriteria - a request to update multiple objects, which match the specified query conditions.

- ObjectIdentificationCriteria - contains query conditions and other information used to identify the objects to mass delete:

- ObjectType - contains the Artifact Type ID of an ObjectType. For example, the Artifact Type ID for a Document object is 10.

For a mass delete operation, all the objects must be the same type.

- Condition - the search criteria used in the query for items to be deleted.

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
{

   "massRequestByCriteria":{

      "ObjectIdentificationCriteria":{

         "ObjectType":{

            "ArtifactTypeID":1000043

         },

         "Condition":"'ArtifactID' >= 1041396 And 'ArtifactID' < 1041496"

      }

   }

}
```

View a JSON request using identifiers

The JSON request requires the following fields:

- massRequestByObjectIdentifiers - a request to delete multiple objects, which are specified by their Artifact IDs.

-

Objects - an array containing the Artifact IDs of Document objects or RDOs for deletion. The ArtifactID field contains the identifier of an object that you want to delete. You can also use GUIDs for this purpose.

For a mass delete operation, all the objects must be the same type.

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
{

   "massRequestByObjectIdentifiers":{

      "Objects":[

         {

            "ArtifactID":1042610

         },

         {

            "ArtifactID":1042611

         },

         {

            "ArtifactID":1042612

         },

         {

            "ArtifactID":1042613

         },

         {

            "ArtifactID":1042614

         }

      ]

   }

}
```

View field descriptions for a response

The response contains the following fields:

- Success - a Boolean value indicating whether the operation completed without any errors.

- Message - explanatory information provided when an error occurs.

- Report - contains a list of the DeleteItems objects.

- DeletedItems - see the field descriptions provided in Delete a Document object or RDO .

View a sample JSON response Copy

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
{

   "Success":true,

   "Message":"",

   "Report":{

      "DeletedItems":[

         {

            "ObjectTypeName":"Custom Object",

            "Action":"Delete",

            "Count":5,

            "Connection":"Parent"

         }

      ]

   }

}
```

## Query for Relativity objects

With the Object Manager service, you can query for Workspaces, Documents, RDOs, and system types. This service includes the Query endpoint, which returns detailed information about the field-value pairs returned by the query. The QuerySlim endpoint returns a smaller payload, which saves bandwidth. This endpoint is useful for mobile devices and for displaying tabular data.

To execute a query, send a POST request with a URL in the following format:

- Query endpoint Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/query
```

- QuerySlim endpoint Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/queryslim
```

To search for data, you can use a variety of query options, including conditions, fields, sorts, and relational fields. These query options have a specific syntax for defining the for defining query conditions. For information about query conditions and options, see Query for resources .

View field descriptions for a request

The request must contain the following fields unless specifically identified as optional:

- Request - a request object for the query operation with the required fields set.

- ObjectType - contains information about the type of object that you want to query on. You can identify an object type by its name, Artifact ID, or GUID. It may contain any one of the following fields:

- Guid - a unique identifier for the object type. This field is listed in the sample JSON.

- Name - the user-friendly name of the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- fields - a collection of fields used like a SELECT statement in an SQL query. For a query request, you can identify fields by name, Artifact ID, or GUID. This field is optional.

- Guid - a unique identifier for a field.

- ArtifactID - a unique identifier for the field, which is represented as an integer.

-

Name - a user-friendly name for the field.

See the following example:

Copy

```text
1
2
3
"fields":

{"Name":"*"}
```

- condition - the search criteria used in the query. This field is optional.

- LongTextBehavior - indicates whether the default or tokenized behavior is used for long text fields that exceed the maximum number of characters set in the MaxCharactersForLongTextValues property. To avoid inadvertently truncating of long text fields, we recommend setting this property to 1 for tokenized behavior when you are reading or querying on long text fields, and then later performing an update operation on the returned values. You can use the default behavior for other operations, such as displaying data in a grid. Before implementing the query operation on a long text field, review the following best practices in Use tokens with long text fields .

- sorts - a collection of Sort objects. This field indicates whether the results are sorted in ascending or descending order, and identifies the field used to sort the results by name. This field is optional.

- QueryHint - set a QueryHint field to optimize the view. For example, you can use the hashjoin setting with the value of true or false, or you can use the waitfor setting with a value, such as waitfor:5. This field is optional.

- start - the one-based index of the first artifact in the result set.

- length - the number of items to return in the query result, starting with index in the start field. If you pass in a Length value that is less than or equal to 0, the parameter is set to the PDVDefaultQueryCacheSize instance setting (set to 10,000 by default) for performance reasons. If you need to retrieve a larger result set but do not know the upper bounds of the result set, you can pass in a large integer size as the value for the Length parameter, but be aware that this approach can have significant negative performance impacts, especially when using a very large integer like int.MaxValue . A better approach is to use the InitializeExportAsync, RetrieveNextResultBlockAsync/RetrieveNextBlockAsync, and StreamLongTextAsync sequence of operations to retrieve large result sets.

View a sample JSON request for a Query or QuerySlim endpoint Copy

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
{

   "Request":{

      "ObjectType":{

         "Guid":"2f816b1d-332d-4eb4-b7c0-2d45c3e12dab"

      },

      "fields":[

         {

            "Guid":"6c84e3ee-f3e3-46f6-80c3-28060c2d5eaf"

         },

         {

            "Guid":"5d78c2c7-5a3a-4a62-b192-d4d8b9005ada"

         },

         {

            "Guid":"dd049386-21c1-47de-966c-ba804982e2ca"

         }

      ],

      "condition":"'Single Choice Field' ISSET OR 'Relativity Native Type' LIKE 'Email'",

      "sorts":[

      ]

   },

   "start":1,

   "length":100

}
```

View field descriptions for a response

The information in the response depends on whether you executed the search using the Query or QuerySlim endpoint. It includes information about the number of results returned, the start index in the result set, and the object type that was queried.

The response contains the following fields for Query and QuerySlim endpoints:

- TotalCount - the total number of objects in Relativity that meet the criteria of the query. For example, you may request 100 objects, but 115 objects satisfy the query. The ResultCount is 100, while the TotalCount is 115.

- Objects - an array RelatvityObject containing fields and their values that are returned by the query operation. It contains the following:

- ParentObject - contains the Artifact ID of the parent object associated with RelativityObject returned by the query operation.

- ArtifactID - a unique identifier for the object, which is represented as an integer.

- FieldValues - an array containing FieldValuePair objects. See Object Manager (.NET) . It contains the following:

- Field - a field associated with a specific value. The Field object contains the following:

- ArtifactID - a unique identifier for the field, which is represented as an integer.

- FieldCategory - indicates the specific functionality assigned to a field, such as stores descriptive text, acts as a relational field, represents grouping for batching, and others.

- FieldType - the type of a Relativity field, such as fixed-length text, date, single object, or others.

- Guids - an array of GUIDs used to identify the field.

- Name - a user-friendly name for the field.

- ViewFieldID - a unique identifier used to reference a view field.

- Value - the data assigned to a field, represented as an Object type. It contains the following:

- ArtifactID - a unique identifier for the object, which is represented as an integer.

- Guids - an array of GUIDs used to identify the object.

- Name - a user-friendly name for the object.

- ArtifactID - a unique identifier for the object returned by the query.

- Guids - an array of GUIDs used to identify the object returned by the query.

- CurrentStartIndex - the index of the first artifact in the result set.

- ResultCount - the number of objects returned by the current query. Also, see the description of TotalCount in this list.

- ObjectType - contains information about the type of object returned from the query operation. It contains the following fields:

- ArtifactID - a unique identifier for the ObjectType instance, which is represented as an integer.

- Name - a user-friendly name for the object type, such as Document, Field, and others.

- Guids - an array of GUIDs used to identify the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

View a sample JSON response for the Query endpoint Copy

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
{

   "TotalCount":7,

   "Objects":[

      {

         "ParentObject":{

            "ArtifactID":1003663

         },

         "FieldValues":[

            {

               "Field":{

                  "ArtifactID":1039421,

                  "FieldCategory":"Generic",

                  "FieldType":"FixedLengthText",

                  "Guids":[

                  ],

                  "Name":"FixedLengthTextField",

                  "ViewFieldID":1001625

               },

               "Value":"object 1"

            },

            {

               "Field":{

                  "ArtifactID":1038851,

                  "FieldCategory":"Generic",

                  "FieldType":"SingleChoice",

                  "Guids":[

                  ],

                  "Name":"Single Choice Field",

                  "ViewFieldID":1001385

               },

               "Value":{

                  "ArtifactID":1038858,

                  "Guids":[

                  ],

                  "Name":"Choice 1"

               }

            }

         ],

         "ArtifactID":1039443,

         "Guids":[

         ]

      },

      {

         "ParentObject":{

            "ArtifactID":1003663

         },

         "FieldValues":[

            {

               "Field":{

                  "ArtifactID":1039421,

                  "FieldCategory":"Generic",

                  "FieldType":"FixedLengthText",

                  "Guids":[

                  ],

                  "Name":"FixedLengthTextField",

                  "ViewFieldID":1001625

               },

               "Value":"object 2"

            },

            {

               "Field":{

                  "ArtifactID":1038851,

                  "FieldCategory":"Generic",

                  "FieldType":"SingleChoice",

                  "Guids":[

                  ],

                  "Name":"Single Choice Field",

                  "ViewFieldID":1001385

               },

               "Value":{

                  "ArtifactID":1038859,

                  "Guids":[

                  ],

                  "Name":"Choice 2"

               }

            }

         ],

         "ArtifactID":1039444,

         "Guids":[

         ]

      }

   ],

   "CurrentStartIndex":1,

   "ResultCount":2,

   "ObjectType":{

      "ArtifactID":1039409,

      "Name":"Custom Object Type",

      "Guids":[

      ],

      "ArtifactTypeID":1000043

   }

}
```

View a sample JSON response for the QuerySlim endpoint Copy

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
{

   "TotalCount":7,

   "Objects":[

      {

         "ArtifactID":1039443,

         "Values":[

            "object 1",

            {

               "ArtifactID":1038858,

               "Guids":[

               ],

               "Name":"Choice 1"

            }

         ]

      },

      {

         "ArtifactID":1039444,

         "Values":[

            "object 2",

            {

               "ArtifactID":1038859,

               "Guids":[

               ],

               "Name":"Choice 2"

            }

         ]

      }

   ],

   "CurrentStartIndex":1,

   "ResultCount":2,

   "ObjectType":{

      "ArtifactID":1039409,

      "Name":"Custom Object Type",

      "Guids":[

      ],

      "ArtifactTypeID":1000043

   },

   "Fields":[

      {

         "ArtifactID":1039421,

         "FieldCategory":"Generic",

         "FieldType":"FixedLengthText",

         "Guids":[

         ],

         "Name":"FixedLengthTextField",

         "ViewFieldID":1001625

      },

      {

         "ArtifactID":1038851,

         "FieldCategory":"Generic",

         "FieldType":"SingleChoice",

         "Guids":[

         ],

         "Name":"Single Choice Field",

         "ViewFieldID":1001385

      }

   ]

}
```

## Export API

The Object Manager service supports exporting document fields, including complete long text fields such as extracted text, via the Export API. The Export API uses a multistep workflow with several endpoints:

- Set up an export job - use the InitializeExport endpoint to set up the export job. The response retrieves a runID used by the RetrieveNextResultsBlockFromExport, the RetrieveResultsBlockFromExport, and the StreamLongText endpoints.

- Retrieve objects - use the RetrieveNextResultsBlockFromExport endpoint to retrieve successive blocks of document fields or use the RetrieveResultsBlockFromExport endpoint to retrieve a specific block of document fields from an in-progress export job.

- Stream text - use the StreamLongText endpoint to retrieve the text that exceeds the size limit for the data returned by RetrieveNextResultsBlockFromExport and RetrieveResultsBlockFromExport endpoints. Make requests to this endpoint repeatedly, and optionally, in parallel with requests to the RetrieveNextResultsBlockFromExport or the RetrieveResultsBlockFromExport endpoint, as well as other requests to the StreamLongText endpoint.

### Set up an export job

Use the initializeexport endpoint to set up the export of documents from a workspace based on a query. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/<workspace artifact id>/object/initializeexport
```

View field descriptions for a request

The request must contain the following fields:

- workspaceID - the Artifact ID of the workspace containing the data to export.

- queryRequest - a query that specifies the data set to export. It includes the following fields:

- ObjectType - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- fields - an array containing the Artifact IDs of the fields for export.

- condition - the query used to determine the set of objects for export. The maximum length of text to export can be optionally specified inline. For information about constructing queries, see Query for Relativity objects .

You can use the MaxCharactersForLongTextValues field of the queryRequest object to override the number limit set by the MaximumLongTextSizeForExportInCell instance setting. For more information, see Set up the export job in .NET , and Instance setting descriptions on the Relativity Server 2025 Documentation site.

- start - the zero-based index of a record indicating where to begin the export operation.

View a sample JSON request Copy

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

{

  "queryRequest": {

      "ObjectType": {"ArtifactTypeID":10},

      "fields":[

         {

            "ArtifactID":1003668

         }

      ],

      "condition":"'Extracted Text' ISSET "

   },

  "start":0

}
```

View field descriptions and sample JSON for a response

The response contains the following fields:

- RunID - a unique identifier for the export job.

- RecordCount - the number of records that were exported.

Copy

```text
1
2
3
4
5

{

    "RunID": "60b6d8c2-9475-4fda-80bb-339f4dcad504",

    "RecordCount": 100000

}
```

### Retrieve objects

Call one of the following endpoints to retrieve document fields from the export job:

- RetrieveNextResultsBlockFromExport endpoint - retrieves successive blocks of document fields from an in-progress export job. See Retrieve the next block of records .

- RetrieveResultsBlockFromExport endpoint - retrieves a specific block index of document fields from an in-progress export job. It provides the option to specify a block size and starting point. For example, you may want to use this endpoint to break up the export job into smaller blocks, which simplifies retrying a job for that specific block of records. See Retrieve a specific block of records .

Review the following considerations for these endpoints:

- When the long text field size is greater than the maximum value, the response contains the #KCURA99DF2F0FEB88420388879F1282A55760# token instead of the text. Use a stream for retrieving the text content of a field. See Stream text .

- The request returns null when all the records are retrieved, and the export job is complete.

- They can be called in multiple threads simultaneously, or from multiple processes. It returns sequential, non-overlapping, non-repeating blocks of documents. Use this type of parallelism to achieve high throughput.

#### Retrieve the next block of records

Use the retrievenextresultsblockfromexport endpoint to get the next block of records from an in-progress export job. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/retrievenextresultsblockfromexport
```

View field descriptions for a request

The body of the request must include the following fields:

- workspaceID - the Artifact ID of the workspace containing the data to export.

- runID - the unique identifier for the in-progress export job.

- batchSize - the maximum number of results to return in a single call.

View a sample JSON request Copy

```text
1
2
3
4
5

{

  "runID": "1f485684-e28c-4204-a795-f11dc91c0f3a",

  "batchSize":5

}
```

View a sample JSON response containing a collection

The response contains a collection of objects with the following fields:

- ArtifactID - the Artifact ID of an object.

- Values - the text from the fields included in the export job.

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
[

  {

    "ArtifactID": 1048512,

    "Values": [

      "Test CHINA CLEANS UP FISCAL & TAXATION PREFERENTIAL POLICIES from AsiaInfo Services\r\n\r\nBEIJING, Jun 26, 2002 (AsiaPort via COMTEX) -- Chinese government continues theefforts to clean up completely all kinds of fiscal and taxationpreferential policies and fiscal subsidy policies, abolish fiscaland taxation preferential policies for a few enterprises and areas,and abolish fiscal subsidy styles that do not accord with Chinesegovernment' s commitment and the WTO regulations.\r\n\r\nOn the basis of seriously cleaning up fiscal and taxation laws, rules and systems, Chinese government will continue to revise the contents that do not in accordance with Chinese\r\n"

    ]

  },

  {

    "ArtifactID": 1048513,

    "Values": [

      "Sally International affairs\r\nOvertaxed.\r\n\r\nWorkout Chinese rural taxation in the context of government regulation.\r\nSharing and Collaboration Policies within Government Agencies.\r\nCorporate Sector: Surtax\r\n\r\n"

    ]

  },

  {

    "ArtifactID": 1048519,

    "Values": [

      "Are Government Policies More Important Than Taxation in Attracting FDI?\r\n\r\nThis paper attempts to broaden the existing empirical literature on foreign direct investment by incorporating government expenditure policies, such as investment in infrastructure, and institutional factors that may impact business investment, such as corruption, along with other conventional determinants such as taxes, location factors, and agglomeration effects. We do so in an unbalanced panel data setting, where we use fixed effects to control for country specific idiosyncrasies and also year dummies in some specifications. Our data include both developing and developed countries in different regions of the world. The regression results indicate that better infrastructure and lower taxes attract FDI, with weaker evidence suggesting lower corruption also increases FDI. These results are robust and hold after controlling for fixed country effects, common year effects of FDI, and agglomeration effects. The magnitude of the response of FDI to infrastructure changes is similar to that of taxes in elasticity terms. The results add evidence to previous cross-sectional results and emphasize the importance of a range of government policies in addition to taxation in attracting foreign direct investment."

    ]

  },

  {

    "ArtifactID": 1048520,

    "Values": [

      "Foreign Affairs:\r\n\r\nInternational relations (IR) represents the study of foreign affairs and global issues among states within the international system, including the roles of states, inter-governmental organizations (IGOs), non-governmental organizations (NGOs), and multinational corporations (MNCs). It is both an academic and public policy field, and can be either positive or normative as it both seeks to analyze as well as formulate the foreign policy of particular states. It is often considered a branch of political science.\r\n\r\nApart from political science, IR draws upon such diverse fields as economics, history, law, philosophy, geography, sociology, anthropology, psychology, and cultural studies. It involves a diverse range of issues including but not limited to: globalization, state sovereignty, ecological sustainability, nuclear proliferation, nationalism, economic development, terrorism, organized crime, human security, foreign interventionism and human rights.\r\n"

    ]

  }

]
```

View a sample JSON response containing a token

The following JSON response contains the #KCURA99DF2F0FEB88420388879F1282A55760# token instead of the text.

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
[

  {

    "ArtifactID": 1048512,

    "Values": [

      "#KCURA99DF2F0FEB88420388879F1282A55760#"

    ]

  },

  {

    "ArtifactID": 1048513,

    "Values": [

      "#KCURA99DF2F0FEB88420388879F1282A55760#"

    ]

  },

  {

    "ArtifactID": 1048515,

    "Values": [

      "#KCURA99DF2F0FEB88420388879F1282A55760#"

    ]

  },

  {

    "ArtifactID": 1048517,

    "Values": [

      "#KCURA99DF2F0FEB88420388879F1282A55760#"

    ]

  },

  {

    "ArtifactID": 1048518,

    "Values": [

      "#KCURA99DF2F0FEB88420388879F1282A55760#"

    ]

  }

]
```

#### Retrieve a specific block of records

Use the RetrieveResultsBlockFromExport endpoint to get a specific block of records from an in-progress export job. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/RetrieveResultsBlockFromExport
```

View field descriptions for a request

The request must contain the following fields:

- runID - the unique identifier for the in-progress export job.

- resultsBlockSize - the maximum number of results to return in one call.

The actual number of results returned may be less than the maximum number requested.

- exportIndexID - the export block index ID of a batch.

View a sample JSON request Copy

```text
1
2
3
4
5
{

   "runID":"310a6c13-3619-45fd-8723-bfaad86dfa45",

   "resultsBlockSize":4,

   "exportIndexID":0

}
```

View field descriptions for a response

The response contains a collection of objects with the following fields:

- ArtifactID - the Artifact ID of an object.

- Values - the text from the fields included in the export job.

View a sample JSON response Copy

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
[

  {

    "ArtifactID": 1048512,

    "Values": [

      "Test CHINA CLEANS UP FISCAL & TAXATION PREFERENTIAL POLICIES from AsiaInfo Services\r\n\r\nBEIJING, Jun 26, 2002 (AsiaPort via COMTEX) -- Chinese government continues theefforts to clean up completely all kinds of fiscal and taxationpreferential policies and fiscal subsidy policies, abolish fiscaland taxation preferential policies for a few enterprises and areas,and abolish fiscal subsidy styles that do not accord with Chinesegovernment' s commitment and the WTO regulations.\r\n\r\nOn the basis of seriously cleaning up fiscal and taxation laws, rules and systems, Chinese government will continue to revise the contents that do not in accordance with Chinese\r\n"

    ]

  },

  {

    "ArtifactID": 1048513,

    "Values": [

      "Sally International affairs\r\nOvertaxed.\r\n\r\nWorkout Chinese rural taxation in the context of government regulation.\r\nSharing and Collaboration Policies within Government Agencies.\r\nCorporate Sector: Surtax\r\n\r\n"

    ]

  },

  {

    "ArtifactID": 1048519,

    "Values": [

      "Are Government Policies More Important Than Taxation in Attracting FDI?\r\n\r\nThis paper attempts to broaden the existing empirical literature on foreign direct investment by incorporating government expenditure policies, such as investment in infrastructure, and institutional factors that may impact business investment, such as corruption, along with other conventional determinants such as taxes, location factors, and agglomeration effects. We do so in an unbalanced panel data setting, where we use fixed effects to control for country specific idiosyncrasies and also year dummies in some specifications. Our data include both developing and developed countries in different regions of the world. The regression results indicate that better infrastructure and lower taxes attract FDI, with weaker evidence suggesting lower corruption also increases FDI. These results are robust and hold after controlling for fixed country effects, common year effects of FDI, and agglomeration effects. The magnitude of the response of FDI to infrastructure changes is similar to that of taxes in elasticity terms. The results add evidence to previous cross-sectional results and emphasize the importance of a range of government policies in addition to taxation in attracting foreign direct investment."

    ]

  },

  {

    "ArtifactID": 1048520,

    "Values": [

      "Foreign Affairs:\r\n\r\nInternational relations (IR) represents the study of foreign affairs and global issues among states within the international system, including the roles of states, inter-governmental organizations (IGOs), non-governmental organizations (NGOs), and multinational corporations (MNCs). It is both an academic and public policy field, and can be either positive or normative as it both seeks to analyze as well as formulate the foreign policy of particular states. It is often considered a branch of political science.\r\n\r\nApart from political science, IR draws upon such diverse fields as economics, history, law, philosophy, geography, sociology, anthropology, psychology, and cultural studies. It involves a diverse range of issues including but not limited to: globalization, state sovereignty, ecological sustainability, nuclear proliferation, nationalism, economic development, terrorism, organized crime, human security, foreign interventionism and human rights.\r\n"

    ]

  }

]
```

### Stream text

Use streamlongtext endpoint to retrieve a stream of text for long text fields marked as exceeding exceeds the size limit for the data returned by the RetrieveNextResultsBlockFromExport or RetrieveResultsBlockFromExport endpoint. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.ObjectManager/{versionNumber}/workspace/{workspaceID}/object/streamlongtext
```

View field descriptions for a request

The body of the request must include the following fields:

- workspaceID - the Artifact ID of the workspace containing the object to be retrieved.

- exportObject - a RelativityObjectRef of the document that contains the text to be streamed.

- longTextField - a FieldRef of the long text field that contains the text to be streamed.

View a sample JSON request Copy

```text
1
2
3
4
5
6
7
8
{

  "exportObject": {

    "ArtifactID": 1048519

  },

  "longTextField": {

    "ArtifactID": 1003668

  }

}
```

The response is a text stream of the content from a specific field. For unicode-enabled fields, the stream is encoded as UTF-16.

On this page

- Object Manager (REST)

- Guidelines for the Object Manager service

- Postman sample file

- Client code sample

- Create an RDO

- Mass create RDOs

- Retrieve field values for a Document object or RDO

- Update fields on a Document object or RDO

- Update a long text field using an input stream

- Mass update Document objects or RDOs

- Retrieve a list of object dependencies

- Delete a Document object or RDO

- Mass delete Document objects or RDOs

- Query for Relativity objects

- Export API

- Set up an export job

- Retrieve objects

- Stream text


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
