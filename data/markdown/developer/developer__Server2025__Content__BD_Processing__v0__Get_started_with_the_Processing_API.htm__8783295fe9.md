---
title: "Get started with the Processing API (v0)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/v0/Get_started_with_the_Processing_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:28+00:00
sha256: 2891f039fdff2e3995039a829f47c46522ce49000d8e9aa406416de723fc954f
---

Get started with the Processing API (v0) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Get started with the Processing API (v0)

This content refers to Version 0 of the Processing APIs. For documentation on the latest version of this API, see Get started with the Processing SDK

The Processing API supports the automation of your processing workflows. You can programmatically use this API to create and update custodians, data sources, processing sets, and profiles required for processing. It provides an alternative to manually creating them through the Relativity UI. You also can use the Processing API to run inventory, discovery, and publishing jobs.

Use the information on this page to learn about Processing API fundamentals. It includes prerequisites for developing with this API, and code samples for common operations. Additional resources to help you get started with the Processing API include:

- Field Mapping Manager and Field Mapping Manager (REST) - provides information about the Field Mapping service available through the Relativity Services API and REST API respectively.

- Processing on the Relativity Documentation site - provides general information about how Relativity supports processing.

See these related pages:

- Processing API services for REST

- Troubleshooting Processing API errors

## Processing API fundamentals

The Processing application provides system admins with the ability to ingest raw data directly into a workspace for review. When you set up a processing workflow, you create a processing profile. This profile specifies settings that control how the processing engine ingests the data. You create or reference the following items:

- A custodian who is a user associated with the data included in a processing job.

- A data source that contains the path used to specify the location of the files that you want to discover.

You also create a processing set that links a processing profile to one or more data sources. When you run a discovery job, the processing engine discovers files in the data source based on the values specified in the processing set. For more information, see Processing on the Relativity Documentation site

The Processing API provides interfaces and objects that you can use to automate many of the tasks in a processing workflow. It includes the following interfaces that you can use to access services, which interact with custodian, data source, and processing set objects:

- IProcessingCustodianManager - used to access the Processing Custodian Manager service.

- IProcessingDataSourceManager - used to access the Processing Data Source Manager service.

- IProcessingProfileManager - used to access the Processing Profile Manager service.

- IProcessingSetManager - used to access the Processing Set Manager service.

Each of these interfaces provide a ReadAsync() and SaveAsync() method, which you can use to create, update, or retrieve processing objects. The Processing API includes the ProcessingCustodian, ProcessingDatasource, ProcessingProfile, and ProcessingSet classes. You can set or retrieve properties on these classes by calling the ReadAsync() or SaveAsync() method on their respective interfaces. You must call the SaveAsync() method to add any new or modified objects to the database.

### Common processing workflows

The Processing API also includes the IProcessingJobManager interface. You can use this interface to access the Processing Job Manager service for running inventory, discovery, and publishing jobs. It includes the following methods:

- SubmitInventoryJobsAsync() method – used for excluding irrelevant files from a data set prior to running a discovery job, such as eliminating NIST file types. The InventoryJob class includes properties for the workspace artifact and processing set IDs required to submit a job.

- SubmitDiscoveryJobsAsync() method – used for submitting data sources to the processing engine for discovery. The DiscoveryJob class includes properties for the workspace artifact and processing set IDs required to submit a job.

- SubmitPublishJobsAsync() method – used to publish the processed data to a workspace after discovery, so that reviewers can access it. The PublishJob class includes properties for the workspace artifact and processing set IDs required to submit a job.

Common workflows for processing include inventorying, discovering, and then publishing data, or just discovering and then publishing data. You can only inventory files that haven’t been discovered. Additionally, you can only publish files after Relativity has completed discovery. For more information, see Processing Job Manager and Processing API services for REST .

In Relativity, you want to enable the auto-publish option on the processing profile, so that the discovered files are automatically added to the workspace. See Relativity environment setup .

## Processing API prerequisites

Complete the following prerequisites to begin development with the Processing API:

SDK downloads

You can download the SDKs required for automating processing workflows from the Relativity Community. For more information, see Download the SDKs .

After you download the following SDKs, install or extract their contents to folders on your local machine:

- Relativity SDK

- Processing SDK

Relativity environment setup

- Obtain access to an instance of Relativity Server 2025 used for development purposes.

You must install the Processing application on this Relativity instance.

- Enable Developer mode in your development instance of Relativity to simplify troubleshooting.

- In the Relativity UI, ensure that the Auto-publish set field is set to Yes on the processing profile that the processing set references in your code. For more information about this field, see Processing profiles in the Relativity Documentation site.

Required Artifact IDs

You need to obtain the Artifact IDs of several items that the classes in the Processing API reference. Use these steps to obtain this information from the workspace database:

- Log in to Relativity.

- On the Workspace tab, locate the workspace that you want to use for automating a processing workflow. Note the Case Artifact ID for the workspace.

- On your database server for Relativity, open Microsoft SQL Server Management Studio.

- In the Object Explorer, expand Databases .

- Use the Case Artifact ID with the prefix EDDS to find the database for your workspace, such as EDDS1014823.

- Expand your workspace to display a list of tables. Reference these tables to obtain the required Artifact IDs:

- EDDSDBO.Folder – Locate the Artifact ID for the destination folder that you want your data source to reference. See Create a ProcessingDataSource object.

- EDDSDBO.ProcessingProfile – Locate the Artifact ID for the processing profile that you want your processing set to reference. See Create a ProcessingSet object .

- EDDSDBO.RelativityTimeZone – Locate the Artifact ID for the time zone that you want your data source to reference. See Create a ProcessingDataSource object.

You must install the Processing application in your Relativity environment in order to view the table for time zones and processing profiles.

## Development guidelines for the Processing API

Use these guidelines when automating workflows with the Processing API:

- Add the following DLL references to your Visual Studio project. For additional information, see Prerequisites for Processing API development .

- Relativity.Processing.Services.Interfaces.dll (in the Processing API SDK)

- kCura.Relativity.Client.dll (in the Relativity SDK)

- Relativity.Kepler.dll (in the Relativity SDK)

- Use the Relativity API helpers to establish a connection with the Processing API and set the context used for your code execution. All code samples on this page illustrate how to use the helper classes to connect with the Processing API. For more information, see Using Relativity API Helpers.

- Call the SaveAsync() method on any processing object that you create or modify. Your changes won't be added to the database until you make this call.

- Use a try-catch block around your code for creating, updating, and reading objects. Also, use it when submitting jobs. Catch any ServiceExceptions raised by your code as exemplified in the following code samples.

- Use logging to help troubleshoot your code as exemplified in the following code samples.

## Processing Custodian Manager

The Processing Custodian Manager service supports read and save operations on custodian objects. The ProcessingCustodian class represents a custodian associated with the files that you want to process. For more information, see Entity object on the Relativity Documentation site.

### Create a ProcessingCustodian

To create a ProcessingCustodian instance, invoke the constructor and then initialize the following properties:

- ArtifactID – set this property to 0, indicating that you are creating a new instance.

- DocumentNumberingPrefix – set this property to a prefix that you want applied to files when the processing engine publishes them to a workspace. The default value is REL.

- FirstName – set this property to the custodian's first name.

- LastName – set this property to the custodian's last name.

Next, call the SaveAsync() method on the proxy created with the IProcessingCustodianManager interface to access the service. You must then pass this method the initialized ProcessingCustodian instance and the workspace Artifact ID.

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

public async Task<bool> ProcessingCustodianManager_Create_SaveAsync(IHelper helper)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingCustodianManager proxy = helper.GetServicesManager().CreateProxy<IProcessingCustodianManager>(ExecutionIdentity.User))

   {

      try

      {

         //Build the ProcessingCustodian object.

         ProcessingCustodian processingCustodian = new ProcessingCustodian

         {

            ArtifactID = 0, // Indicates a new ProcessingCustodian object.

            DocumentNumberingPrefix = "REL",

            FirstName = "John",

            LastName = "Smith"

         };

         //Create the ProcessingCustodian object. The service returns the Artifact ID of the object.

         int artifactId = await proxy.SaveAsync(processingCustodian, WorkspaceId);

         if (artifactId != 0)

         {

            success = true;

         }

         else

         {

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingCustodianManager_Create_SaveAsync), "Create failed", this.GetType().Name);

         }

      }

      catch (Exception exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingCustodianManager_Create_SaveAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Read a ProcessingCustodian

Read the values for the properties on a ProcessingCustodian object by calling the ReadAsync() method on the proxy created with IProcessingCustodianManager interface. The ReadAsync() method requires that you pass the Artifact IDs of the ProcessingCustodian object and the workspace as arguments.

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

public async Task<bool> ProcessingCustodianManager_ReadAsync(IHelper helper, int processingCustodianArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingCustodianManager proxy = helper.GetServicesManager().CreateProxy<IProcessingCustodianManager>(ExecutionIdentity.User))

   {

      try

      {

         //Read the ProcessingCustodian object.

         ProcessingCustodian processingCustodian = await proxy.ReadAsync(processingCustodianArtifactId, WorkspaceId);

         //Display the last and first name of the custodian.

         string fullName = $"{processingCustodian.LastName}, {processingCustodian.FirstName}";

         Logger.LogMessage(LogLevel.Debug, nameof(ProcessingCustodianManager_ReadAsync), fullName, this.GetType().Name);

         success = true;

      }

      catch (Exception exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingCustodianManager_ReadAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Update a ProcessingCustodian

When updating a ProcessingCustodian instance, you call the AsyncRead() method on the proxy created with the IProcessingCustodianManager interface. Next, set the properties on the instance to their new values, and then call the SaveAsync() method. You must call the SaveAsync() method in order for your changes to be added to the database.

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
public async Task<bool> ProcessingCustodianManager_Update_SaveAsync(IHelper helper, int processingCustodianArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingCustodianManager proxy = helper.GetServicesManager().CreateProxy<IProcessingCustodianManager>(ExecutionIdentity.User))

   {

      try

      {

         //Read the ProcessingCustodian object.

         ProcessingCustodian processingCustodian = await proxy.ReadAsync(processingCustodianArtifactId, WorkspaceId);

         //Modify the document numbering prefix and first name.

         processingCustodian.DocumentNumberingPrefix = "ECA";

         processingCustodian.FirstName = "Sam";

         processingCustodian.Name = $"{processingCustodian.LastName}, {processingCustodian.FirstName}";

         //Update the ProcessingCustodian object. The service returns the Artifact ID of the object.

         int artifactId = await proxy.SaveAsync(processingCustodian, WorkspaceId);

         if (artifactId != 0)

         {

            success = true;

         }

         else

         {

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingCustodianManager_Update_SaveAsync), "Update failed", this.GetType().Name);

         }

      }

      catch (Exception exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingCustodianManager_Update_SaveAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

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

## Processing Data Source Manager

The Processing Data Source Manager service supports read and save operations on data source objects. The ProcessingDataSource class represents a data source that contains the location of the files for discovery during processing. For more information, see Processing sets on the Relativity Documentation site.

### Create a ProcessingDataSource

To create a ProcessingDataSource instance, invoke the constructor and initialize the following properties:

- ArtifactID – set this property to 0, indicating that you are creating a new instance.

- Custodian – set this property to the Artifact ID associated with this data source.

- TimeZone – set this property to the Artifact ID that you obtained from the workspace database. See Required Artifact IDs .

- DestinationFolder – set this property to the Artifact ID that you obtained from the workspace database. See Required Artifact IDs .

- StartNumber – set this property to the value used to begin numbering a sequence of documents published from a specific data source. This field should not be selected if the Processing Profile has Level Numbering selected for Numbering Type.

You can set this property to null. When it is null, Relativity uses auto-numbering. For more information about numbering type options, see Processing sets on the Relativity Documentation site.

- IsStartNumberVisible – determines whether Relativity UI displays the Start Number field in the Data Source layout. This field should not be selected if the Processing Profile has Level Numbering selected for Numbering Type.

- Other properties – set them to their required values. The following code sample uses the default values.

Call the SaveAsync() method on the proxy created with the IProcessingDataSourceManager interface. You must then pass this method the initialized ProcessingDataSource instance and the workspace Artifact ID as illustrated in the following code.

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
public async Task<bool> ProcessingDataSourceManager_Create_SaveAsync(IHelper helper, int custodianArtifactId, int destinationFolderArtifactId, int timeZoneArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingDataSourceManager proxy = helper.GetServicesManager().CreateProxy<IProcessingDataSourceManager>(ExecutionIdentity.User))

   {

      try

      {

         //Build the processing ProcessingDataSource object.

         ProcessingDataSource processingDataSource = new ProcessingDataSource

         {

            ArtifactID = 0, // Indicates a new ProcessingDataSource object.

            ProcessingSet = new ProcessingSetRef { ArtifactID = ProcessingSetId },

            Custodian = custodianArtifactId,

            DestinationFolder = destinationFolderArtifactId,

            DocumentNumberingPrefix = "REL",

            InputPath = "@Some/Path",

            Name = "Data Source 1",

            OcrLanguages = new[] { OcrLanguage.English },

            Order = 200,

            TimeZone = timeZoneArtifactId,

            StartNumber = 8,

            IsStartNumberVisible = true,

         };

         //Create the ProcessingDataSource object. The service returns the Artifact ID for the object.

         int artifactId = await proxy.SaveAsync(processingDataSource, WorkspaceId);

         if (artifactId != 0)

         {

            success = true;

         }

         else

         {

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingDataSourceManager_Create_SaveAsync), "Create failed", this.GetType().Name);

         }

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingDataSourceManager_Create_SaveAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Read a ProcessingDataSource

Read the values for the properties on a ProcessingDataSource object by calling the ReadAsync() method on the proxy created with the IProcessingDataSourceManager interface. The ReadAsync() method requires that you pass the Artifact IDs of the ProcessingDataSource object and the workspace as arguments.

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
public async Task<bool> ProcessingDataSourceManager_ReadAsync(IHelper helper, int processingDataSourceArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingDataSourceManager proxy = helper.GetServicesManager().CreateProxy<IProcessingDataSourceManager>(ExecutionIdentity.User))

   {

      try

      {

         //Read the ProcessingSet object.

         ProcessingDataSource processingDataSource = await proxy.ReadAsync(processingDataSourceArtifactId, WorkspaceId);

         //Display the input path.

         Logger.LogMessage(LogLevel.Debug, nameof(ProcessingDataSourceManager_ReadAsync), processingDataSource.InputPath, this.GetType().Name);

         success = true;

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingDataSourceManager_ReadAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Update a ProcessingDataSource

When updating a ProcessingDataSource instance, you call the AsyncRead() method on the proxy created with the IProcessingDataSourceManager interface. Next, set the properties on the instance to their new values, and then call the SaveAsync() method. You must call the SaveAsync() method in order for your changes to be added to the database.

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
public async Task<bool> ProcessingDataSourceManager_Update_SaveAsync(IHelper helper, int processingDataSourceArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingDataSourceManager proxy = helper.GetServicesManager().CreateProxy<IProcessingDataSourceManager>(ExecutionIdentity.User))

   {

      try

      {

         //Read the ProcessingDataSource object.

         ProcessingDataSource processingDataSource = await proxy.ReadAsync(processingDataSourceArtifactId, WorkspaceId);

         //Modify the input path and destination folder.

         processingDataSource.InputPath = "@Some/Other/Path";

         processingDataSource.DestinationFolder = 99; // Artifact Id of the destination folder

         //Update the processing data source object. The service returns the Artifact ID of the object.

         int artifactId = await proxy.SaveAsync(processingDataSource, WorkspaceId);

         if (artifactId != 0)

         {

            success = true;

         }

         else

         {

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingDataSourceManager_Update_SaveAsync), "Update failed", this.GetType().Name);

         }

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingDataSourceManager_Update_SaveAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

## Processing Set Manager

The Processing Set Manager service supports read and save operations on processing set objects. The ProcessingSet class represents a processing set object that links a processing profile to one or more data sources. For more information, see Processing sets on the Relativity Documentation site.

### Create a ProcessingSet

To create a ProcessingSet instance, invoke the constructor and then initialize the following properties:

- ArtifactID – set this property to 0, indicating that you are creating a new instance.

- EmailNotificationRecipients – set this optional property to an array of email addresses.

- Name – set this property to the name of the processing set.

- Profile – set this property to the Artifact ID of the processing profile that you obtained from your workspace database table. See Required Artifact IDs .

Call the SaveAsync() method on the proxy created with the IProcessingSetManager interface. You must then pass the initialized ProcessingSet object and workspace Artifact ID to this method.

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
public async Task<bool> ProcessingSetManager_Create_SaveAsync(IHelper helper, int processingProfileArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingSetManager proxy = helper.GetServicesManager().CreateProxy<IProcessingSetManager>(ExecutionIdentity.User))

   {

      try

      {

         //Build the ProcessingSet object.

         ProcessingSet processingSet = new ProcessingSet

         {

            ArtifactID = 0, // Indicates a new ProcessingSet object.

            EmailNotificationRecipients = new[] { "johnSmith@domain.com", "adamJohnson@domain.com" },

            Name = "Test Set",

            Profile = new ProcessingProfileRef(processingProfileArtifactId)  // The Artifact ID of the processing profile.

         };

         //Create the ProcessingSet object. The service returns the Artifact ID of the object.

         int artifactId = await proxy.SaveAsync(processingSet, WorkspaceId);

         if (artifactId != 0)

         {

            success = true;

         }

         else

         {

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingSetManager_Create_SaveAsync), "Create failed", this.GetType().Name);

         }

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingSetManager_Create_SaveAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Read a ProcessingSet

Read the values for the properties on a ProcessingSet object by calling the ReadAsync() method on the IProcessingSetManager. The ReadAsync() method requires that you pass the Artifact IDs of the ProcessingSet object and the workspace as arguments.

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
public async Task<bool> ProcessingSetManager_ReadAsync(IHelper helper, int processingSetArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingSetManager proxy = helper.GetServicesManager().CreateProxy<IProcessingSetManager>(ExecutionIdentity.User))

   {

      try

      {

         //Read the ProcessingSet object.

         ProcessingSet processingSet = await proxy.ReadAsync(processingSetArtifactId, WorkspaceId);

         //Display the Artifact ID of the processing profile.

         string profileId = $"{processingSet.Profile.ArtifactID}";

         Logger.LogMessage(LogLevel.Debug, nameof(ProcessingSetManager_ReadAsync), profileId, this.GetType().Name);

         success = true;

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingSetManager_ReadAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Update a ProcessingSet

When updating a ProcessingSet instance, you call the AsyncRead() method on the proxy created with the IProcessingSetManager interface. Next, set the properties on the instance to their new values, and then call the SaveAsync() method. You must call the SaveAsync() method in order for your changes to be added to the database.

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
public async Task<bool> ProcessingSetManager_Update_SaveAsync(IHelper helper, int processingSetArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingSetManager proxy = helper.GetServicesManager().CreateProxy<IProcessingSetManager>(ExecutionIdentity.User))

   {

      try

      {

         //Read the ProcessingSet object.

         ProcessingSet processingSet = await proxy.ReadAsync(processingSetArtifactId, WorkspaceId);

         //Modify the list of email recipients list and the name of the processing set.

         processingSet.EmailNotificationRecipients = new[] { "johnSmith@domain.com" };

         processingSet.Name = "Test Set";

         //Update the ProcessingSet object. The service returns the Artifact ID of the object.

         int artifactId = await proxy.SaveAsync(processingSet, WorkspaceId);

         if (artifactId != 0)

         {

            success = true;

         }

         else

         {

            Logger.LogMessage(LogLevel.Error, nameof(ProcessingSetManager_Update_SaveAsync), "Update failed", this.GetType().Name);

         }

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingSetManager_Update_SaveAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Retrieve a list of processing sets and related aggregate information

You can use the GetDocumentAggregates() method to retrieve document totals and other information about processing sets in a specific workspace. To retrieve this information, the process sets must have the statuses of Completed or Completed with errors. If you wanted to create a custom dashboard for reporting purposes, use this method to populate it with information about completed processing sets. For example, Relativity uses the GetDocumentAggregates() method to populate the Early Case Assessment dashboard with processing set data.

Use the following classes in conjunction with the GetDocumentAggregates() method. For additional reference information, see Processing API .

GetDocumentAggregatesRequest class

When calling the GetDocumentAggregates() method, pass a GetDocumentAggregatesRequest object as an argument. The GetDocumentAggregatesRequest class is a request object. It contains criteria for retrieving processing sets available in a specific workspace. It has the following properties:

- WorkspaceArtifactId – the Artifact ID of the workspace containing processing sets for retrieval.

- PageSize – the number of processing sets returned per page in the results set. The Relativity UI uses this property to support paging and to display results. It determines the number of processing sets returned for each page.

- Page – indicates the number used to identify a specific page of processing sets that you want returned in the results set. This optional property is set to the first page (0) by default.

- SortColumnName – the name of column used for sorting results. You can set the sort column property to one of the following options:

- "PublishedDocumentCount"

- "PublishedDocumentSizeInBytes"

- "ProcessingSetDateCreated"

- "ProcessingSetName" - the name used by default.

The following code sample uses "ProcessingSetName" as the setting for SortColumnName property.

- SortDescending – indicates the sort order for the results. This optional property is set to ascending by default. Set this property to true for descending order, and to false or null for ascending order. When this property is null, it uses the ascending sort order based on sort column name.

ProcessingSetDocumentInfoSummary class

The GetDocumentAggregates() method returns a ProcessingSetDocumentInfoSummary object, which contains information about processing sets retrieved from a specific workspace. This class has the following properties:

- ProcessingSetDocumentInfo – represents an object that contains information about specific processing sets within a workspace. For additional reference information, see Processing API or Retrieve aggregate information for processing sets for the REST API.

- TotalProcessingSets – the total number of processing sets with the status of Completed or Complete with errors in a workspace. Use this information in conjunction with paging available through the Relativity UI.

- TotalPublishedDocuments – the total number of documents from all processing sets with the status of Completed or Complete with errors published to a workspace.

- TotalPublishedDocumentSizeInBytes – the total number of bytes for documents from all processing sets with the status of Completed or Complete with errors published to a workspace.

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
public async Task<ProcessingSetDocumentInfoSummary> ProcessingSetManager_GetDocumentAggregatesAsync(IHelper helper, int workspaceArtifactId)

{

   // Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   // agents, and custom Pages. They are mocked in these samples.

   // This sample code executes under the context of the current user.

   using (IProcessingSetManager proxy = helper.GetServicesManager().CreateProxy<IProcessingSetManager>(ExecutionIdentity.User))

   {

      try

      {

         // Build the GetDocumentAggregatesRequest object.

         GetDocumentAggregatesRequest request = new GetDocumentAggregatesRequest

         {

            Page = 0,

            PageSize = 15,

            SortColumnName = "ProcessingSetName",

            SortDescending = true,

            WorkspaceArtifactId = workspaceArtifactId

         };

         // Submit the request. The service returns information for all 'Completed' and 'Completed with Errors'

         // Processing Sets in the given workspace.

         ProcessingSetDocumentInfoSummary processingSetDocumentInfoSummary = await proxy.GetDocumentAggregates(request);

         return processingSetDocumentInfoSummary;

      }

      catch (ServiceException serviceException)

      {

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingSetManager_GetDocumentAggregatesAsync), serviceException.Message, this.GetType().Name);

         throw;

      }

   }

}
```

## Processing Job Manager

The Processing Job Manager service includes methods for executing inventory, discovery, and publishing jobs. It also includes a method for canceling any of these jobs for a processing set. This service is available through the IProcessingJobManager interface. For more information, see Common processing workflows .

### Inventory jobs

The following code illustrates how to run an inventory job by calling the SubmitInventoryJobsAsync() method on the proxy created with the IProcessingJobManager interface. You must pass an initialized InventoryJob instance to this method. This instance has the Artifact ID of the processing set that you want to use for the job, and the Artifact ID of the workspace where it resides.

If you want to use filtering on your inventory job, apply filters through Relativity after you programmatically run your inventory job. For more information, see Inventory on the Relativity Documentation site.

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
public async Task<bool> ProcessingJobManager_InventoryAsync(IHelper helper, int processingSetArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingJobManager proxy = helper.GetServicesManager().CreateProxy<IProcessingJobManager>(ExecutionIdentity.User))

   {

      try

      {

         //Create an inventory job object.

         InventoryJob inventoryJob = new InventoryJob

         {

            ProcessingSetId = processingSetArtifactId,

            WorkspaceArtifactId = WorkspaceId

         };

         //Submit the job for inventory.

         await proxy.SubmitInventoryJobsAsync(inventoryJob);

         success = true;

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingJobManager_InventoryAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Discovery jobs

The following code illustrates how to run a discovery job by calling the SubmitDiscoveryJobsAsync() method on the proxy created with the IProcessingJobManager interface. You must pass an initialized DiscoveryJob instance to this method. The DiscoveryJob instance represents a processing job that you want to run. This instance has the Artifact ID of the processing set that you want to use for the job, and the Artifact ID of the workspace where it resides. For more information, see Processing on the Relativity Documentation site

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
public async Task<bool> ProcessingJobManager_DiscoveryAsync(IHelper helper, int processingSetArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user. For more information, see the documentation for Relativity API Helpers.

   using (IProcessingJobManager proxy = helper.GetServicesManager().CreateProxy<IProcessingJobManager>(ExecutionIdentity.User))

   {

      try

      {

         //Create a discovery job object.

         DiscoveryJob discoveryJob = new DiscoveryJob

         {

            ProcessingSetId = processingSetArtifactId,

            WorkspaceArtifactId = WorkspaceId

         };

         //Submit the job for discovery.

         await proxy.SubmitDiscoveryJobsAsync(discoveryJob);

         success = true;

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingJobManager_DiscoveryAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Publishing jobs

The following code illustrates how to execute a publishing job by calling the SubmitPublishJobsAsync() method on the proxy created with the IProcessingJobManager interface. You must pass an initialized PublishJob instance to this method. This instance has the Artifact ID of the processing set that you want to use for the job, and the Artifact ID of the workspace where it resides.

Similar to the Relativity UI, you can resubmit a publishing job with processing errors by calling the SubmitPublishJobsAsync() method again. For more information, see Publishing files on the Relativity Documentation site.

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
public async Task<bool> ProcessingJobManager_PublishAsync(IHelper helper, int processingSetArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingJobManager proxy = helper.GetServicesManager().CreateProxy<IProcessingJobManager>(ExecutionIdentity.User))

   {

      try

      {

         //Create a publish job object.

         PublishJob publishJob = new PublishJob

         {

            ProcessingSetId = processingSetArtifactId,

            WorkspaceArtifactId = WorkspaceId

         };

         //Submit the job for discovery.

         await proxy.SubmitPublishJobsAsync(publishJob);

         success = true;

      }

      catch (ServiceException exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingJobManager_PublishAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

### Cancel jobs

You can use the SubmitCancelJobAsync() method to cancel inventory, discovery, and publishing jobs for a specific processing set. The following code illustrates how to execute a cancel job by calling this method on the proxy created with the IProcessingJobManager interface. You must pass an initialized CancelJob instance to this method. This instance has the Artifact ID of the processing set associated with the job that you want to cancel, and the Artifact ID of the workspace where it resides.

This sample code returns a Boolean value called success after the cancel job has been successfully submitted. However, this return value doesn't indicate that the job has been canceled. Multiple factors influence when a worker picks up a cancel job and how long the job takes to execute. For example, the amount of data and system state can affect this outcome.

The submission of cancel job returns successfully when the job associated with a processing set has already been canceled.

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
public async Task<bool> ProcessingJobManager_CancelAsync(IHelper helper, int processingSetArtifactId)

{

   bool success = false;

   //Get a connection to the API using the Relativity API Helper classes, available on event handlers,

   //agents, and custom Pages. They are mocked in these samples.

   //This sample code executes under the context of the current user.

   using (IProcessingJobManager proxy = helper.GetServicesManager().CreateProxy<IProcessingJobManager>(ExecutionIdentity.User))

   {

      try

      {

         //Create a cancel job object.

         CancelJob cancelJob = new CancelJob

         {

            ProcessingSetId = processingSetArtifactId,

            WorkspaceArtifactId = WorkspaceId

         };

         //Submit a job to cancel a processing set.

         await proxy.SubmitCancelJobAsync(cancelJob);

         success = true;

      }

      catch (Exception exception)

      {

         //The service returns exceptions of type ServiceException.

         Logger.LogMessage(LogLevel.Error, nameof(ProcessingJobManager_CancelAsync), exception.Message, this.GetType().Name);

      }

   }

   return success;

}
```

On this page

- Get started with the Processing API (v0)

- Processing API fundamentals

- Common processing workflows

- Processing API prerequisites

- Development guidelines for the Processing API

- Processing Custodian Manager

- Create a ProcessingCustodian

- Read a ProcessingCustodian

- Update a ProcessingCustodian

- Processing Profile

- Getting Started With Processing Profile Guids

- Create a Processing Profile

- Query a Processing Profile

- Update a Processing Profile

- Delete a Processing Profile

- Processing Data Source Manager

- Create a ProcessingDataSource

- Read a ProcessingDataSource

- Update a ProcessingDataSource

- Processing Set Manager

- Create a ProcessingSet

- Read a ProcessingSet

- Update a ProcessingSet

- Retrieve a list of processing sets and related aggregate information

- Processing Job Manager

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
