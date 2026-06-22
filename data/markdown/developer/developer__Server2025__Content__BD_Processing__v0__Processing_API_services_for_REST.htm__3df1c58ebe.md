---
title: "Processing API services for REST (v0)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/v0/Processing_API_services_for_REST.htm
collection: developer
fetched_at: 2026-06-22T06:30:30+00:00
sha256: ca42feea82292f1032a07fe8f5e9daa6b193ff4760dcfd4d156b4f42d999142c
---

Processing API services for REST (v0) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing API services for REST (v0)

The Processing API provides HTTP services based on .NET interfaces. The Relativity REST API supports these services, which you can use to automate processing by following standard Representational State Transfer (REST) features.

Similar to the .NET interfaces on the Processing API, you can use the following services supported through REST to automate your processing workflows:

- Processing Custodian Manager

- Processing Profile Manager

- Processing Set Manager

- Processing Data Source Manager

- Processing Job Manager

All of these services support create, read, and update operations except for the Processing Job Manager, which supports running inventory, discovery, and publishing jobs. You use the SaveAsync request for create and update operations. Additionally, all of these operations run asynchronously.

You must install the Processing application in your Relativity environment to automate processing workflows with the Processing API. For more information, see Installing and configuring Processing on the Relativity Documentation site.

See these related pages:

- Get started with the Processing API

- Troubleshooting Processing API errors

## Client code sample

You can use the following .NET code as the REST client for performing any of the operations available in the Processing API. The code currently illustrates how to submit a discovery job, but you can modify it as follows to perform other operations:

- Set the url variable to the URL for the operation that you want to perform.

- Set the string represented by QueryInputJSON object to the JSON input required for your operation.

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
//Set up the client.

HttpClient httpClient = new HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");



//Set the required headers.

httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic bXkudXNlckBrY3VyYS5jb206Q250VGNoVGhzMTIzNCE=");



//Call the operation that you want to run.

string url = "Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Job Manager/SubmitDiscoveryJobsAsync”;

StringContent content = new StringContent(QueryInputJSON);

content.Headers.ContentType = new MediaTypeHeaderValue("application/json");

HttpResponseMessage response = httpClient.PostAsync(url, content).Result;

string result = response.Content.ReadAsStringAsync().Result;

bool success = HttpStatusCode.Ok == response.StatusCode;



//Parse the result with Json.NET.

JObject resultObject = JObject.Parse(result);
```

## Custodians

A custodian is a user who's associated with the data included in a processing job. For more information, see Entity object on the Relativity Documentation site.

### Create or update a custodian

Use this URL on the Processing Custodian Manager service to create or update a custodian:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Custodian Manager/SaveAsync
```

You can send a request for a custodian who is an individual or an entity, such as corporation, data location, or other construct.

The request to create or update a custodian who is an individual must contains the following fields:

- DocumentNumberingPrefix – the prefix applied to files when published through processing. For more information, see Processing sets on the Relativity Documentation site.

- FirstName and LastName – the first and last name of the custodian.

- CustodianType – indicates whether the custodian is an individual or an entity. It must be set to "Person" for an individual. Entity object on the Relativity Documentation site.

- workspaceArtifactId – the Artifact ID of the workspace that contains the custodian.

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

   "Custodian":{

      "DocumentNumberingPrefix":"REL",

      "FirstName":"Custodian First Name",

      "LastName":"Custodian Last Name",

      "CustodianType":"Person"

   },

   "workspaceArtifactId":1093143

}
```

The request to create or update a custodian who is an entity contains the following fields:

- DocumentNumberingPrefix – the prefix applied to files when published through processing. For more information, see Processing sets on the Relativity Documentation site.

- Name – the value corresponding to that used in the Full Name field on a Custodian object in Relativity.

- CustodianType – indicates whether the custodian is an individual or an entity. It must be set to "Entity" for a corporation, data location, or other construct.It must be set to "Other" for a corporation, data location, or other construct. For more information, see Entity object on the Relativity Documentation site.

- workspaceArtifactId – the Artifact ID of the workspace that contains the custodian.

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
{

   "Custodian":{

      "DocumentNumberingPrefix":"relativity-",

      "Name":"Relativity ODA LLC",

      "CustodianType":"Other"

   },

   "workspaceArtifactId":1093143

}
```

The response returns the Artifact ID of the custodian that was created or updated, such as the integer 1060372.

### Read a custodian

Use this URL on the Processing Custodian Manager service to retrieve a custodian:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Custodian Manager/ReadAsync
```

The request must include Artifact ID for the custodian and the workspace:

Copy

```text
1
2
3
4
 {

   "ArtifactId":1041433,

   "WorkspaceArtifactId":1093143

}
```

The response for custodian who is an individual contains the following fields:

- DocumentNumberingPrefix – the prefix applied to files when published through processing. For more information, see Processing sets on the Relativity Documentation site.

- FirstName and LastName – the first and last name of the custodian.

- CustodianType – returns "Person" indicating that the custodian is an individual.

- ArtifactId – the Artifact ID of the ProcessingCustodian object.

- Name – the full name of the custodian.

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

"DocumentNumberingPrefix": "Laura-"

"FirstName": "Laura"

"LastName": "Libera"

"CustodianType": "Person"

"ArtifactID": 1038911

"Name": "Libera, Laura"

}
```

The response for custodian that is an entity contains the same fields as a custodian who is a person. However, the CustodianType fields contains "Entity", and "FirstName" and "LastName" don't contain any values.

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

  "DocumentNumberingPrefix": "relativity-"

  "FirstName": "-"

  "LastName": "-"

  "CustodianType": "Entity"

  "ArtifactID": 1038912

  "Name": "Relativity ODA LLC"

}
```

## Processing Profile

The Processing Profile represents a collection of settings used to process documents. Processing profiles are associated with processing sets, so you must provide the Artifact ID of a processing profile when creating or updating a processing set, see Processing Set Manager for more details. The Processing Profile can be updated using the Object Manager API, use the Create endpoint for creating a new profile, the Update endpoint for updating a profile, the Query endpoint for retrieving a profile, and the Delete endpoint for removing a profile from Relativity. Sample methods are provided below for performing all of these actions with a Processing Profile.

### Getting Started With Processing Profile Guids

The Processing Profile has multiple properties for specifying numbering; deNISTing, extraction, and deduplication settings.

You can find more information about processing profile fields on the following pages:

- Processing profiles

- Processing API

Before you can create or update fields within a Processing Profile, the ArtifactID’s will need to be queried. Use the ReadMultipleArtifactIdsAsync endpoint from the Artifact Guid Manager to retrieve the field ArtifactID's that are needed. Once the ArtifactID’s are collected using the corresponding Guid from the list below, they can be used to identify which field values are being set.

View sample API URL Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.ArtifactGuid.IArtifactGuidModule/Artifact%20Guid%20Manager/ReadMultipleArtifactIdsAsync
```

View sample JSON Request Copy

```text
1
{"workspaceId":10636370,"guids":["7161a505-54ed-4eb1-94fe-004bcdc3e988","5f300c10-4660-4a4d-bfa9-e32c9846c3fa"]}
```

View sample C# Example Copy

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
        public async Task<Dictionary<Guid, int>> ReadMultipleArtifactIdsAsync(HttpClient httpClient, int workspaceId, List<Guid> guids)

        {

            var apiUrl = "/Relativity.Rest/API/Relativity.Services.ArtifactGuid.IArtifactGuidModule/Artifact%20Guid%20Manager/ReadMultipleArtifactIdsAsync";

            var payloadObject = new

            {

                workspaceId = workspaceId,

                guids = guids,

            };

            StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

            HttpResponseMessage response = await httpClient.PostAsync(apiUrl, payload);

            string resultString = await response.Content.ReadAsStringAsync();

            var artifactIDs = new Dictionary<Guid, int>();

            if (response.IsSuccessStatusCode)

            {

                dynamic result = JArray.Parse(resultString) as JArray;

                foreach (var obj in result)

                {

                    int artifactID = obj.ArtifactID;

                    Guid guid = obj.Guid;

                    artifactIDs.Add(guid, artifactID);

                }

            }

            return artifactIDs;

        }
```

#### Processing Profile Guids List

To access Processing Profile fields via the Relativity API, enter the following IDs:

NAME_FIELD: "7161A505-54ED-4EB1-94FE-004BCDC3E988"

- DEFAULT_DOCUMENT_NUMBERING_PREFIX - 4FEAC495-C466-4A6E-BD78-26FA0240E47C

- NUMBERING_TYPE - D56E0890-1BCE-4E72-8691-BE976596B50D

- LEVEL_TWO_NUMBER_OF_DIGITS - BC3BC259-69E3-48C2-BCEF-10F0900514AE

- LEVEL_THREE_NUMBER_OF_DIGITS - BADD3B6D-59AC-4CBE-A94C-CA16D5D3C57F

- LEVEL_FOUR_NUMBER_OF_DIGITS - FEA7B097-7290-4448-987C-A4B29E0010E8

- DEFAULT_START_NUMBER - E62617E9-77C0-4D4F-B36F-3237FDA22E61

- NUMBER_OF_DIGITS - 802A933B-2287-4A29-9E2B-4252674E2B6B

- PARENT_CHILD_NUMBERING - 3F806580-8579-46A0-B7A6-410EA364375E

- DELIMITER - D2D7B514-1418-479C-8D5F-C3D27CB39788

Inventory & Discovery Settings

- DENIST_FIELD - 04AB3BCA-1A74-4541-92CA-FD6F6D741EEA

- DENIST_MODE_FIELD - 8029F9CE-D603-4B37-A808-B4731CD40348

- DEFAULT_OCR_LANGUAGE_FIELD - 5F300C10-4660-4A4D-BFA9-E32C9846C3FA

- D EFAULT_TIMEZONE_FIELD - 8FE787D3-473C-4945-8846-F0D1DAE2D5A7

Extraction Settings

- EXTRACT_CHILDREN_FIELD - 410AC62F-DB2A-41E2-AA96-CCDB3AD10C85

- WHILE_EXTRACTING_CHILDREN_DO_NOT_EXTRACT_FIELD - C466468B-18BC-4079-ADC7-675077C41321

- USEALTERNATIVE_EMAIL_TYPE_FIELD - F577A90E-F802-4C0A-8799-68A13DB366A5

- EXCEL_HEADERFOOTER_EXTRACTION_FIELD - E41C0890-0ECF-4EDF-AA0B-B1392DDE57BB

- EXCEL_TEXT_EXTRACTION_METHOD_FIELD - E12594BC-9FBD-419C-91BB-4F2E264440C0

- POWERPOINT_TEXT_EXTRACTION_METHOD_FIELD - a657bb3e-4f95-4eb4-b949-2cec59dfeb65

- WORD_TEXT_EXTRACTION_METHOD_FIELD - 1d36e81e-b735-4a12-b52a-d61c5ac2310f

- OCR_ENGINE_FIELD- B5973A8C -3FAA-40C8-84BC-5AD0D7044745

- OCR_ACCURACY_FIELD- CBA95742 -DAAD-49E5-B7CE-52556FD687EF

- OCR_TEXT_SEPERATOR_FIELD - BF1BB914-A13F-4817-ADB9-556F6DC5B8FF

OCR Accuracy Choices

- OCR_ACCURACY_CHOICE_HIGH - A2F05DDE-8F4B-45FF-A36B-0020086276E4

- OCR_ACCURACY_CHOICE_MEDIUM - 6BA1160B-1079-4B91-8735-BACE6431AEE6

- OCR_ACCURACY_CHOICE_LOW - 858B1CD8-BBB0-44B7-9715-51A635371845

Deduplication Settings

- DEDUPE_METHOD_FIELD - 289AAA6A-6EC1-484F-BC68-3636EF5A5F3F

- PROPAGATE_METADATA_FIELD - B74FFB86-5A38-4FDF-872C-A25FA5F7B0C1

Publish Settings

- DESTINATION_FOLDER_FIELD - E387C847-FEED-47C6-AD0C-C7A1BB406617

- DO_YOU_WANT_TO_USE_SOURCE_FOLDER_STRUCTURE_FIELD - F326E5F0-BA0F-463D-A171-1446367F0DF4

- AUTO_PUBLISH_SET_FIELD - A13AEE24-CA34-48D0-ADFA-18C737DBDD1E

Inclusion/Exclusion Settings

- INCLUSION_EXCLUSION_FIELD - CEB4559C-EA94-44F2-9FD6-0251BF83b5A2

- INCLUSION_EXCLUSION_MODE_FIELD - 2308196F-822C-441D-9873-1B0D8B622EA6

- INCLUSION_EXCLUSION_FILE_EXTENSION_LIST_FIELD - CF4473C3-7BF0-44CE-BF35-A6B3779B0DAA

- INCLUSION_EXCLUSION_SELECTION_FIELD - 2A723B28-1043-4385-9311-045BA35BA0DD

- NUMBERING_AUTONUMBER_CHOICE - 476242D4-CEA6-44FC-9E0F-8E8C50D953DE

- NUMBERING_DEFINE_START_NUMBER_CHOICE - 94F2B0AA-B862-48F4-AC16-0834CA0E9C0F

- NUMBERING_LEVEL_NUMBERING - 3A10A8A8-DC40-4E7E-B71D-CC6A1A19AE39

Number of Digits

- NUMBER_OF_DIGITS_1 - A3A49DEC-0978-4279-AE51-DDCFE4A4C465

- NUMBER_OF_DIGITS_2 - 0BE05451-7F69-4663-890A-A2E8A30698AD

- NUMBER_OF_DIGITS_3 - 191CF64A-2784-4E96-B766-8BDB1E33B8C6

- NUMBER_OF_DIGITS_4 - A3562A49-C787-4B6E-AA00-0D3AE5CE4A8A

- NUMBER_OF_DIGITS_5 - 1529CCD1-5909-443A-8B62-50C11F76ADB3

- NUMBER_OF_DIGITS_6 - 5D7FE7F1-543B-4271-9978-D5C6309423AB

- NUMBER_OF_DIGITS_7 - D49E883B-E5BD-4743-8085-72A7E34B7C79

- NUMBER_OF_DIGITS_8 - 17D643B0-CE10-41A1-9221-52F433700E34

- NUMBER_OF_DIGITS_9 - 05D32CCB-7DDB-42F9-9E89-B3C3627B5B81

- NUMBER_OF_DIGITS_10 - 961215D6-1A29-43E8-88F0-48072B93BEF5

Alternative email type

- ALTERNATIVE_EMAIL_MSG - 85E42F0A-12A8-41C2-B8D1-75CF637EB4C8

- ALTERNATIVE_EMAIL_MHT - D3F591FB-4623-4361-9CA7-C3189066FF78

Level 2 Number of Digits field's choice Guids

- LEVEL_2_NUMBER_OF_DIGITS_2 - 633C2762-0FD4-4682-B783-07834A829CBD

- LEVEL_2_NUMBER_OF_DIGITS_3 - 38C64451-8492-4585-BB93-983FEDE77012

- LEVEL_2_NUMBER_OF_DIGITS_4 - 9481D1E9-2CC5-4FC3-94CA-664ADA1857F1

- LEVEL_2_NUMBER_OF_DIGITS_5 - 432AE52E-5750-42D8-B1A5-B5F0A0A7B98D

Level 3 Number of Digits field's choice Guids

- LEVEL_3_NUMBER_OF_DIGITS_2 - 5F377AD1-6762-4AFB-A5B5-7660080A4658

- LEVEL_3_NUMBER_OF_DIGITS_3 - 1526B9DD-69DC-4465-91E5-978EAE1B3FAF

- LEVEL_3_NUMBER_OF_DIGITS_4 - A3621C20-E120-4F5B-8E68-EA8D215E9638

- LEVEL_3_NUMBER_OF_DIGITS_5 - 9E841857-7826-473D-BB2B-21D2BBBD1EC4

Level 4 Number of Digits field's choice Guids

- LEVEL_4_NUMBER_OF_DIGITS_2 - 5F899E20-32C9-46CC-A9B1-D950D05A580A

- LEVEL_4_NUMBER_OF_DIGITS_3 - 4EA1080E-91E5-4628-AE00-ED62BA011E27

- LEVEL_4_NUMBER_OF_DIGITS_4 - 7D3DC831-24EA-443B-8B28-1BE009A921D5

- LEVEL_4_NUMBER_OF_DIGITS_5 - ADBFF454-777E-4B29-B9FA-94A1AA857657

Parent Child Numbering

- SUFFIX_ALWAYS - 00B235F2-E122-483E-A63B-F7F8C830A563

- CONTINUOUS_ALWAYS - 9946A1D3-DF02-4DD4-93B0-09C80B1E57B1

- CONTINUOUS_SUFFIX_ON_RETRY - FC803906-7081-4B00-844A-6959FE47402F

Delimiters

- DELIMITER_PERIOD - D817672D-1271-4EE4-B77C-B86C41EE782D

- DELIMITER_HYPHEN - 7E8DE86C-C932-4EC6-A3A6-F82ABCC59B6B

- DELIMITER_UNDERSCORE - 4C5F4D6A-5B48-406A-BE58-6B985D34368B

Denist Modes

- DENIST_MODE_DENIST_ALL_FILES - A269EADF-BDD3-40E2-A1D4-EBB5B2933487

- DENIST_MODE_DONOT_BREAK_PARENT_CHILD_GROUPS - D39D4BC8-DA56-4CC0-ACD4-AA931C51C44D

### Create a Processing Profile

To create a processing profile in a workspace, set the required fields using their ArtifactID’s queried from the Guid list above and the value. Call the Object Manager Create endpoint by passing it the new Processing Profile values and the Artifact ID of a Workspace object.

View sample API URL Copy

```text
1
<host>/Relativity.REST/api/Relativity.Objects/Workspace/{workspaceId}/Object/Create
```

View sample JSON Request Copy

```text
1
{"request":{"ObjectType":{"ArtifactTypeID":1000041},"FieldValues":[{"Field":{"ArtifactID":1039245},"Value":"Processing Profile Name"},{"Field":{"ArtifactID":1039459},"Value":[{"ArtifactID":1039609,"Name":"Afrikaans","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null},{"ArtifactID":1039610,"Name":"Albanian","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}]},{"Field":{"ArtifactID":1039460},"Value":{"ArtifactID":1037893,"Name":"(UTC-06:00) Central Time (US & Canada)","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1039461},"Value":{"ArtifactID":1039463,"Name":"Global","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1039465},"Value":true},{"Field":{"ArtifactID":1039466},"Value":"000001"},{"Field":{"ArtifactID":1039467},"Value":true},{"Field":{"ArtifactID":1039468},"Value":true},{"Field":{"ArtifactID":1039469},"Value":[{"ArtifactID":1039472,"Name":null,"Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}]},{"Field":{"ArtifactID":1039473},"Value":false},{"Field":{"ArtifactID":1039474},"Value":{"ArtifactID":1346192,"Name":"Ring L0001 (201010)","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1039475},"Value":{"ArtifactID":1039476,"Name":"DeNIST all files","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1039478},"Value":true},{"Field":{"ArtifactID":1039479},"Value":{"ArtifactID":1039480,"Name":"High (Slowest Speed)","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1039483},"Value":true},{"Field":{"ArtifactID":1039484},"Value":{"ArtifactID":1039486,"Name":"Extract and place at end","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1039488},"Value":{"ArtifactID":1272519,"Name":"Relativity","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1042412},"Value":{"ArtifactID":1042414,"Name":". (period)","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1042416},"Value":{"ArtifactID":1042423,"Name":"7","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1042427},"Value":{"ArtifactID":1042428,"Name":"Auto Number","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1042430},"Value":{"ArtifactID":1042431,"Name":null,"Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1043873},"Value":{"ArtifactID":1272521,"Name":null,"Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1043876},"Value":{"ArtifactID":1272522,"Name":null,"Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1043879},"Value":true},{"Field":{"ArtifactID":1046224},"Value":{"ArtifactID":1046225,"Name":"MSG","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1272523},"Value":true},{"Field":{"ArtifactID":1272524},"Value":{"ArtifactID":1272525,"Name":"All Files","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1272527},"Value":{"ArtifactID":1272529,"Name":"Exclusion","Guids":[],"FieldType":0,"FieldCategory":0,"SubObjectFields":[],"Value":null}},{"Field":{"ArtifactID":1272530},"Value":"txt pdf"}]}}
```

View sample C# Example Copy

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
        public async Task<int?> CreateProcessingProfile(HttpClient httpClient, int workspaceId)

        {

            var objType = new ObjectType() { ArtifactTypeID = 1000041 }; // ArtifactTypeID 1000041 is the Processing Profile ArtifactTypeID

            var fieldList = new List<FieldValue>() {

                new FieldValue() { ArtifactID = 1039245, Value = "Processing Profile Name" },

                new FieldValue() { ArtifactID = 1039459, Value = new List<FieldValue>() { new FieldValue() { ArtifactID = 1039609, Name = "Afrikaans" }, new FieldValue() { ArtifactID = 1039610, Name = "Albanian" } } },

                new FieldValue() { ArtifactID = 1039460, Value = new FieldValue() { ArtifactID = 1037893, Name = "(UTC-06:00) Central Time (US & Canada)" } },

                new FieldValue() { ArtifactID = 1039461, Value = new FieldValue() { ArtifactID = 1039463, Name = "Global" } },

                new FieldValue() { ArtifactID = 1039465, Value = true },

                new FieldValue() { ArtifactID = 1039466, Value = "000001" },

                new FieldValue() { ArtifactID = 1039467, Value = true },

                new FieldValue() { ArtifactID = 1039468, Value = true },

                new FieldValue() { ArtifactID = 1039469, Value = new List<FieldValue>() { new FieldValue() { ArtifactID = 1039472 } } },

                new FieldValue() { ArtifactID = 1039473, Value = false },

                new FieldValue() { ArtifactID = 1039474, Value = new FieldValue() { ArtifactID = 1346192, Name = "Ring L0001 (201010)" } },

                new FieldValue() { ArtifactID = 1039475, Value = new FieldValue() { ArtifactID = 1039476, Name = "DeNIST all files" } },

                new FieldValue() { ArtifactID = 1039478, Value = true },

                new FieldValue() { ArtifactID = 1039479, Value = new FieldValue() { ArtifactID = 1039480, Name = "High (Slowest Speed)" } },

                new FieldValue() { ArtifactID = 1039483, Value = true },

                new FieldValue() { ArtifactID = 1039484, Value = new FieldValue() { ArtifactID = 1039486, Name = "Extract and place at end" } },

                new FieldValue() { ArtifactID = 1039488, Value = new FieldValue() { ArtifactID = 1272519, Name = "Relativity" } },

                new FieldValue() { ArtifactID = 1042412, Value = new FieldValue() { ArtifactID = 1042414, Name = ". (period)" } },

                new FieldValue() { ArtifactID = 1042416, Value = new FieldValue() { ArtifactID = 1042423, Name = "7" } },

                new FieldValue() { ArtifactID = 1042427, Value = new FieldValue() { ArtifactID = 1042428, Name = "Auto Number" } },

                new FieldValue() { ArtifactID = 1042430, Value = new FieldValue() { ArtifactID = 1042431 } },

                new FieldValue() { ArtifactID = 1043873, Value = new FieldValue() { ArtifactID = 1272521 } },

                new FieldValue() { ArtifactID = 1043876, Value = new FieldValue() { ArtifactID = 1272522 } },

                new FieldValue() { ArtifactID = 1043879, Value = true },

                new FieldValue() { ArtifactID = 1046224, Value = new FieldValue() { ArtifactID = 1046225, Name = "MSG" } },

                new FieldValue() { ArtifactID = 1272523, Value = true },

                new FieldValue() { ArtifactID = 1272524, Value = new FieldValue() { ArtifactID = 1272525, Name = "All Files" } },

                new FieldValue() { ArtifactID = 1272527, Value = new FieldValue() { ArtifactID = 1272529, Name = "Exclusion" } },

                new FieldValue() { ArtifactID = 1272530, Value = "txt pdf" },

            };

            var APIUrl = "/Relativity.Rest/API/Relativity.Objects/workspace";

            var payloadObject = new

            {

                request = new

                {

                    ObjectType = new

                    {

                        ArtifactTypeID = objType?.ArtifactTypeID

                    },

                    FieldValues = fieldList?.Select(fv => new

                    {

                        Field = new

                        {

                            ArtifactID = fv.ArtifactID,

                        },

                        Value = fv.Value

                    }),

                },

            };

            StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

            HttpResponseMessage response = await httpClient.PostAsync($"{APIUrl}/{workspaceId}/object/create", payload);

            string resultString = await response.Content.ReadAsStringAsync();

            int? outId = null;

            if (response.IsSuccessStatusCode)

            {

                dynamic result = JObject.Parse(resultString) as JObject;

                int.TryParse((string)result["Object"]["ArtifactID"], out int id);

                outId = id;

            }

            return outId;

        }
```

### Query a Processing Profile

Use the Object Manager Query endpoint to retrieve a list of processing profiles from Relativity if passing in the ArtifactTypeId or pass in the ArtifactId of the specific Processing Profile to retrieve child FieldValues.

View sample API URL Copy

```text
1
<host>/Relativity.REST/api/Relativity.ObjectManager/v1/Workspace/{workspaceId}/Object/Query
```

View sample JSON Request Copy

```text
1
2
3
4
5
6
{"request":

    {"ObjectType":

        {"ArtifactTypeID":1000041},"Condition":"","Sorts":"","Fields":""},

    "start":0,

    "length":10

}
```

View sample C# Example Copy

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
        public async Task<string> QueryProcessingProfile(HttpClient httpClient, int workspaceId)

        {

            var artifactTypeId = 1000041;

            var APIUrl = "/Relativity.Rest/API/Relativity.ObjectManager/v1";

            var payloadObject = new

            {

                request = new

                {

                    ObjectType = new

                    {

                        ArtifactTypeID = artifactTypeId

                    },

                    Condition = "",

                    Sorts = "",

                    Fields = "",

                },

                start = 0,

                length = 10,

            };

            StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

            HttpResponseMessage response = await httpClient.PostAsync($"{APIUrl}/workspace/{workspaceId}/object/query", payload);

            return await response.Content.ReadAsStringAsync();

        }
```

### Update a Processing Profile

To update a processing profile, modify the profile fields as necessary by passing in the ArtifactID and Value of the field along with the Processing Profile ArtifactID and then pass this object to the Object Manager Update endpoint.

View sample API URL Copy

```text
1
<host>/Relativity.REST/api/Relativity.Objects/Workspace/{workspaceId}/Object/Update
```

View sample JSON Request Copy

```text
1
2
3
4
5
{"request":

    {"Object":

        {"ArtifactID":1395130},"FieldValues":[{"Field":{"ArtifactID":1039245},"Value":"NewProfileName"}]

    }

}
```

View sample C# Example Copy

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
        public async Task<string> UpdateProcessingProfile(HttpClient httpClient, int workspaceId)

        {

            int artifactId = 1395130; // Processing Profile ArtifactId

            var fieldList = new List<FieldValue>() {

                new FieldValue() { ArtifactID = 1039245, Value = "New Profile Name" } // Name field ArtifactId and Value

            };

            var APIUrl = "/Relativity.Rest/API/Relativity.Objects/workspace";

            var payloadObject = new

            {

                request = new

                {

                    Object = new

                    {

                        ArtifactID = artifactId

                    },

                    FieldValues = fieldList?.Select(fv => new

                    {

                        Field = new

                        {

                            ArtifactID = fv.ArtifactID,

                        },

                        Value = fv.Value

                    }),

                },

            };

            StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

            HttpResponseMessage response = await httpClient.PostAsync($"{APIUrl}/{workspaceId}/object/update", payload);

            return await response.Content.ReadAsStringAsync();

        }
```

### Delete a Processing Profile

Use the Object Manager Delete endpoint to remove a processing profile from Relativity by passing in the Processing Profile ArtifactId and WorkspaceId.

View sample API URL Copy

```text
1
<host>/Relativity.REST/api/Relativity.Objects/Workspace/{workspaceId}/Object/Delete
```

View sample JSON Request Copy

```text
1
2
3
4
5
{"request":

    {"Object":

        {"ArtifactID":1395122}

    }

}
```

View sample C# Example Copy

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
        public async Task<string> DeleteProcessingProfile(HttpClient httpClient, int workspaceId)

        {

            int artifactId = 1395122; // Processing Profile ArtifactId

            string APIUrl = "/Relativity.Rest/API/Relativity.Objects/Workspace";

            var payloadObject = new

            {

                request = new

                {

                    Object = new

                    {

                        ArtifactID = artifactId

                    },

                },

            };

            StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

            HttpResponseMessage response = await httpClient.PostAsync($"{APIUrl}/{workspaceId}/object/delete", payload);

            return await response.Content.ReadAsStringAsync();

        }
```

## Processing data sources

A data source contains the path used to specify the location of the files that you want to discover during processing. For more information, see Processing sets on the Relativity Documentation site.

### Create or update a data source

Use this URL on the Processing Data Source Manager service to update or create a data source:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Data Source Manager/SaveAsync
```

The request must contain an InputPath field that specifies a file path, which the resource pool in the workspace can access. For more information, see Resource Pools on the Relativity Server 2025 Documentation site. It may also contain the StartNumber and IsStartNumberVisible properties.

StartNumber should not be used if the Processing Profile has Level Numbering selected for Numbering Type. If Level Numbering is selected for Numbering Type, set LevelTwoStartNumber to the value used to begin numbering for the second level (box number) of Level Numbering when publishing documents from a specific data source. Set LevelThreeStartNumber to the value used to begin numbering for the third level (folder number) of Level Numbering when publishing documents from a specific data source. Set LevelFourStartNumber to the value used to begin numbering for the fourth level (document number) of Level Numbering when publishing documents from a specific data source.

For more information, see Processing data sources .

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

   "processingDataSource": {

      "Custodian":1038885,

      "DestinationFolder":1003697,

      "DocumentNumberingPrefix":"REL",

      "InputPath":"\\\\localhost\\FileShare\\My Documents\\History of English.msg",

      "OcrLanguages":[

         "English"

      ],

      "Order":123,

      "ProcessingSet":{

         "ArtifactID":1038907

      },

      "TimeZone":1036905,

      "IsStartNumberVisible":true,

      "StartNumber":8,

      "ArtifactID":1038908,

      "Name":"1038908 - History of English"

   },

   "workspaceArtifactId":1378006

}
```

The response returns the Artifact ID of the data source that was created or updated, such as the integer 1046822.

### Read a data source

Use this URL on the Processing Data Source Manager service to retrieve a data source:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Data Source Manager/ReadAsync
```

The request must include Artifact ID for the data source that you want to read, and the workspace where the data source resides:

Copy

```text
1
2
3
4
{

   "ArtifactId":1038908,

   "workspaceArtifactId":1378006

}
```

The response for a read operation returns a JSON object with the following fields. The Name field for the processing set is always an empty string, while the Name field for the data source usually contains its Artifact ID.

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
{

  "Custodian": 1038885,

  "DestinationFolder": 1003697,

  "DocumentNumberingPrefix": "REL-",

  "InputPath": "\\localhost\FileShare\My Documents\History of English.msg",

  "IsNew": false,

  "OcrLanguages": [

    "English"

  ],

  "Order": 123,

  "ProcessingSet": {

    "ArtifactID": 1038907,

    "Name": ""

  },

  "TimeZone": 1036905,

  "StartNumber": 8,

  "IsStartNumberVisible": true,

  "ArtifactID": 1038908,

  "Name": "1038908 - History of English"

}
```

### Validate deletion of a data source

You can use the ValidDeleteAsync endpoint to check if the specified processing data source is safe to be deleted. For example, if the processing set is already discovered or canceled. Use this URL on the Processing Data Source Manager service for deletion validation of the processing sets with the criteria specified in the JSON request:

Copy

```text
1
<host>/relativity.rest/api/Relativity.Processing.Services.IProcessingModule/workspace/{workspaceId}/processing-data-sources/{processingDataSourceId}/validate-delete
```

The request must include the following fields:

- WorkspaceId – the Artifact ID of the workspace containing processing sets for deletion validation.

- ProcessingDataSourceId – the Artifact ID of the processing data source.

The response includes the following fields:

- CanDelete – returns true if the data source can be deleted.

- Reasons – the reason(s) why the data source cannot be deleted. This will be empty if the data source is able to be deleted.

Copy

```text
1
2
3
4
5
6
{

            "CanDelete": false,

            "Reasons": [

            "You can't delete the data source because the processing set has already been discovered."

            ]

        }
```

## Processing sets

A processing set object links a processing profile to one or more data sources. For more information, see Processing sets on the Relativity Documentation site.

### Create or update a processing set

Use this URL on the Processing Set Manager service to create or update a processing set:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Set Manager/SaveAsync
```

The request must include the Artifact ID for the workspace that contains the processing set, and the name and Artifact ID of the processing profile. You can also optionally include a list of recipients who receive email notifications after the creation or update of the processing set completes.

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
{

   "workspaceArtifactId":1093143,

   "ProcessingSet":{

      "EmailNotificationRecipients":[

         "jsmith@relativity.com",

         "bjones@relativity.com"

      ],

      "Name":"Processing Set  Name",

      "Profile":{

         "ArtifactID":1041350

      }

   }

}
```

The response returns the Artifact ID of the processing set that was created or updated, such as the integer 1046784.

### Read a processing set

Use this URL on the Processing Set Manager service to retrieve a processing set:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Set Manager/ReadAsync
```

The request must include Artifact ID for the processing set and the workspace that contains it:

Copy

```text
1
2
3
4
{

   "artifactId":1045777,

   "workspaceArtifactId":1093143

}
```

The response includes the following fields. The Name field for the processing profile is always an empty string.

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

   "Profile":{

      "ArtifactID":1056549,

      "Name":"",

      "IsNew":false

   },

   "ArtifactID":1090382,

   "Name":"My Processing Set"

}
```

### Retrieve aggregate information for processing sets

Use the GetDocumentAggregates endpoint to retrieve document aggregates and other information about processing sets with the status of Completed or Completed with errors in a specific workspace. For more information about the GetDocumentAggregates() method, see Retrieve a list of processing sets and related aggregate information .

Use this URL on the Processing Set Manager service to retrieve the processing sets with the criteria specified in the JSON request:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Processing.Services.IProcessingModule/Processing Set Manager/GetDocumentAggregates
```

The request must include the following fields:

- WorkspaceArtifactId – the Artifact ID of the workspace containing processing sets for retrieval.

- PageSize – the number of processing sets returned per page in the results set. The Relativity UI uses this property to support paging and to display results. It determines the number of processing sets returned for each page.

In addition, the request may optionally include these fields:

- Page – the number used to identify a specific page of processing sets that you want returned in the results set. This optional property is set to the first page (0) by default.

- SortColumnName – the name of column used for sorting results. You can set the sort column property to one of the following options:

- "PublishedDocumentCount"

- "PublishedDocumentSizeInBytes"

- "ProcessingSetDateCreated"

- "ProcessingSetName" - name used by default.

- SortDescending – indicates the sort order for the results. Set this property to true for descending order, and to false or null for ascending order. This optional property is set to ascending by default. When this property is null, it uses the ascending sort order based on sort column name.

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

    "request":{

        "WorkspaceArtifactId":1023139,

        "PageSize":15,

        "Page":0,

        "SortColumnName":"PublishedDocumentSizeInBytes",

        "SortDescending":true

    }

}
```

The response includes the following fields:

- TotalPublishedDocuments – the total number of documents from all processing sets with the status of Completed or Complete with Errors published to a workspace.

- TotalPublishedDocumentSizeInBytes – the total number of bytes for documents from all processing sets with the status of Completed or Complete with Errors published to a workspace.

- TotalProcessingSets – the total number of processing sets with the status of Completed or Complete with Errors in a workspace.

- ProcessingSetDocumentInfo – contains information about specific processing sets within a workspace. For additional reference information, see Processing API .

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

  "TotalPublishedDocuments": 15,

  "TotalPublishedDocumentSizeInBytes": 3563255,

  "TotalProcessingSets": 2,

  "ProcessingSetDocumentInfo": [

    {

      "ProcessingSetId": 1038688,

      "ProcessingSetName": "Test 1",

      "ProcessingSetDateCreated": "2016-06-02T19:25:42.547",

      "PublishedDocumentCount": 14,

      "PublishedDocumentSizeInBytes": 3531511

    },

    {

      "ProcessingSetId": 1042347,

      "ProcessingSetName": "Test 2",

      "ProcessingSetDateCreated": "2016-06-09T19:17:27.253",

      "PublishedDocumentCount": 1,

      "PublishedDocumentSizeInBytes": 31744

    }

  ]

}
```

### Retrieve summary data for processing sets

Use the summary endpoint to retrieve processing set summary data in a specific workspace to display to console, such as environment errors, discover and publish status, and more. For more information, see Retrieve a list of processing sets and related aggregate information .

Use this URL on the Processing Set Manager service to retrieve the processing sets with the criteria specified in the JSON request:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Processing.Services.IProcessingModule/workspace/{workspaceId}/processing-sets/{processingSetId}/summary
```

The request must include the following fields:

- WorkspaceId – the Artifact ID of the workspace containing processing sets for retrieval.

- ProcessingSetId – the Artifact ID of the processing set.

The response includes the following fields:

- SetState – the job status and other general information about the processing set.

- ArtifactId – the Artifact ID of the processing set.

- InventoryStatus – the inventory status GUID.

- DiscoverStatus – the discover status GUID.

- PublishStatus – the publish status GUID.

- Canceled – returns true if the job is canceled.

- ProcessingProfileId – the Artifact ID of the processing set's assigned processing profile.

- HasRunningJobs – returns true if the processing set has any currently running jobs.

- EnvironmentErrors – any environment errors that the processing set may have encountered in a workspace.

- DataSourceIds – the data source Ids for the processing set.

- DataSourceHasDocumentLevelErrors – returns true if the processing set has document level errors.

- DataSourceHasJobLevelErrors – returns true if the processing set has job level errors.

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
{

    "SetState": {

        "ArtifactId": 1043783,

        "InventoryStatus": "4bab4cc3-a8a8-438c-a649-6fd4e0d111eb",

        "DiscoverStatus": "be180e9d-8abf-41f8-8507-37bd1d22f72e",

        "PublishStatus": "fc78eb19-b905-479c-9c3c-6fc49b95ea08",

        "Canceled": false,

        "ProcessingProfileId": 1040502

    },

    "HasRunningJobs": false,

    "EnvironmentErrors": [],

    "DataSourceIds": [

        1043784

    ],

    "DataSourceHasDocumentLevelErrors": false,

    "DataSourceHasJobLevelErrors": false

}
```

## Inventory jobs

Use the SubmitInventoryJobsAsync endpoint to run an inventory job. Before you run a discovery job, you may want to exclude irrelevant raw files from your data set, such as eliminating NIST file types. You can perform this task by executing an inventory job. You can only run an inventory job on processing sets that haven't been discovered. If you want to apply filtering to your data, set your filters through the Relativity UI after the inventory job completes. For more information, see Inventory on the Relativity Documentation site.

Use this URL on the Processing Job Manager service to run an inventory job:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Job Manager/SubmitInventoryJobsAsync
```

The request must include Artifact ID for the processing set and the workspace where it resides:

Copy

```text
1
2
3
4
5
6
{

   "InventoryJob":{

      "ProcessingSetId":1046785,

      "WorkspaceArtifactId":1093143

   }

}
```

The response returns the status code of 200 when the job completes successfully.

## Discovery jobs

After you create a processing set and add a data source to it, you can initiate a discovery or processing job. During a job run, the processing engine discovers files in the data source based on the values specified in the processing set. For more information, see Processing on the Relativity Documentation site.

Use this URL on the Processing Job Manager service to run a discovery job:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Job Manager/SubmitDiscoveryJobsAsync
```

The request must include Artifact ID for the processing set and the workspace where it resides:

Copy

```text
1
2
3
4
5
6
{

   "DiscoveryJob":{

      "ProcessingSetId":1046785,

      "WorkspaceArtifactId":1093143

   }

}
```

The response returns the status code of 200 when the job completes successfully.

## Publishing jobs

Use the SubmitPublishJobsAsync endpoint to run publishing jobs. You can provide reviewers in Relativity with access to process data by publishing it to a workspace after it has been discovered. You must run a discovery job on the date before you can run a publishing job on it. For more information, see Publishing files on the Relativity Documentation site.

Use this URL on the Processing Job Manager service to run an publishing job:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Job Manager/SubmitPublishJobsAsync
```

The request must include Artifact ID for the processing set and the workspace where it resides:

Copy

```text
1
2
3
4
5
6
{

   "PublishJob":{

      "ProcessingSetId":1046785,

      "WorkspaceArtifactId":1093143

   }

}
```

The response returns the status code of 200 when the job completes successfully.

## Cancel jobs

You can use the SubmitCancelJobAsync endpoint to cancel inventory, discovery, and publishing jobs for a specific processing set. Use this URL on the Processing Job Manager service to cancel a job:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Processing.Services.IProcessingModule/Processing Job Manager/SubmitCancelJobAsync
```

The request must include Artifact ID for the processing set and the workspace where it resides:

Copy

```text
1
2
3
4
5
6
{

   "CancelJob":{

      "ProcessingSetId":1046785,

      "WorkspaceArtifactId":1093143

   }

}
```

The response returns the status code of 200 when the job is submitted successfully. However, this return value doesn't indicate that the job has been canceled. Multiple factors influence when a worker picks up a cancel job and how long the job takes to execute. For example, the amount of data and system state can affect this outcome.

The submission of cancel job returns successfully when the job associated with a processing set has already been canceled.

On this page

- Processing API services for REST (v0)

- Client code sample

- Custodians

- Create or update a custodian

- Read a custodian

- Processing Profile

- Getting Started With Processing Profile Guids

- Create a Processing Profile

- Query a Processing Profile

- Update a Processing Profile

- Delete a Processing Profile

- Processing data sources

- Create or update a data source

- Read a data source

- Validate deletion of a data source

- Processing sets

- Create or update a processing set

- Read a processing set

- Retrieve aggregate information for processing sets

- Retrieve summary data for processing sets

- Inventory jobs

- Discovery jobs

- Publishing jobs

- Cancel jobs


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
