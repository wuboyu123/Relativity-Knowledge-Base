---
title: "Processing Data Source Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Data_Source_Manager.htm
collection: developer
fetched_at: 2026-06-22T06:27:25+00:00
sha256: dd384ed3b3ff13021e920cf6f7ad7767c6cf5c959cc90164284bca461f12d657
---

Processing Data Source Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Data Source Manager

This topic describes the IProcessingDataSourceManager interface, which is used to access the Processing Data Source Manager service. The Processing Data Source Manager service supports read and save operations on data source objects. The ProcessingDataSource class represents a data source that contains the location of the files for discovery during processing. For more information, see Processing sets on the Relativity Documentation site.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Create a processing data source

- Method

- CreateAsync: Creates a processing data source. Returns the artifact id of the new datasource

- Parameters

- <int>workspaceID : The workspace artifact ID where this processing data source resides

- processingDataSource: The datasource to be created. This is a ProcessingDataSource object.

- <int>ProcessingDataSourceID: set this property to 0, indicating that you are creating a new instance

- <string>Name

- <int>Custodian: The artifact id of the custodian associated with this data source

- <int>TimeZone: Artifact ID of the time zone obtained from the workspace database.

- <int>DestinationFolder: Artifact ID obtained from the workspace database.

-

<string>DocumentNumberPrefix : prefix to be used for the documents in the processing data source

- <int>StartNumber: set this property to the value used to begin numbering a sequence of documents published from a specific data source. This field should not be selected if the Processing Profile has Level Numbering selected for Numbering Type. If this value is null, Relativity uses auto-numbering. For more information about numbering type options, see Processing sets on the Relativity Documentation site.

- <bool>IsStartNumberVisible: determines whether Relativity UI displays the Start Number field in the Data Source layout. This field should not be set if the Processing Profile has Level Numbering selected for Numbering Type

- <string>InputPath

- <List<OcrLanguage>>OcrLanguages: List of OcrLanguage, which is an enum consisting of all available OCR languages

- <int>Order

- <int>LevelTwoStartNumber, LevelThreeStartNumber, LevelFourStartNumber

- <ProcessingSetRef>ProcessingSet: the processing set object assigned to the data source

- Returns

- <int>ProcessingDataSourceID: the artifact ID of data source that is created

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
//Build the processing ProcessingDataSource object.

ProcessingDataSource processingDataSource = new ProcessingDataSource {

  ProcessingDataSourceID = 0, // Indicates a new ProcessingDataSource object.

    ProcessingSet = new ProcessingSetRef {

      ProcessingSetID = processingSetId

    },

    Custodian = custodianArtifactId,

    DestinationFolder = destinationFolderArtifactId,

    DocumentNumberingPrefix = "REL",

    InputPath = "@Some/Path",

    Name = "Data Source 1",

    OcrLanguages = new List<OcrLanguage>{

      OcrLanguage.English

    },

    Order = 200,

    TimeZone = timeZoneArtifactId,

    StartNumber = 8,

    IsStartNumberVisible = true,

};

using (IProcessingDataSourceManager proxy = _servicesMgr.CreateProxy <IProcessingDataSourceManager>(ExecutionIdentity.CurrentUser)) {

  //Create the data source object

  int dataSourceId = await proxy.CreateAsync(data.WorkspaceId, processingDataSource).ConfigureAwait(false);

}
```

## Read a processing data source

Read the values for the properties on a ProcessingDataSource object by calling the ReadAsync() method on the proxy created with the IProcessingDataSourceManager interface. The ReadAsync() method requires that you pass the Artifact IDs of the ProcessingDataSource object and the workspace as arguments.

- Method

- ReadAsync: Returns the data source for the artifact id passed in

- Parameters

- <int>workspaceID : The workspace artifact ID where this processing data source resides

- <int>dataSourceID: The data source artifact ID to read.

- Returns

- ProcessingDataSource

Copy

```text
1
2
3
4
5
6
7
using (IProcessingDataSourceManager proxy = _servicesMgr.CreateProxy <IProcessingDataSourceManager>(ExecutionIdentity.CurrentUser)) {

  //Read the ProcessingDataSource object.

  ProcessingDataSource dataSource = await proxy.ReadAsync(data.WorkspaceId, processingDataSourceID);

  //Get the input path.

  string path = dataSource.InputPath;

}
```

## Update a processing data source

When updating a processing data source instance, you call the ReadAsync() method on the proxy created with the IProcessingDataSourceManager interface. Next, set the properties on the instance to their new values, and then call the UpdateAsync() methodto persist your updates to the Processing Data Source.

- Method

- UpdateAsync: Returns the artifact ID of the updated data source

- Parameters

- <int>workspaceID : The workspace artifact ID where this processing data source resides

- <int>dataSourceID: The data source artifact ID to read.

- processingDataSource: The data source to be updated. This is a ProcessingDataSource object

- Returns

- <int>ProcessingDataSourceID: the artifact ID of data source that is created

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
using (IProcessingDataSourceManager proxy = _servicesMgr.CreateProxy<IProcessingDataSourceManager>(ExecutionIdentity.CurrentUser)) {

  //Read the ProcessingDataSource object.

  ProcessingDataSource processingDataSource = await proxy.ReadAsync(data.WorkspaceId, processingDataSourceId);

  //Modify the order and the name of the processing data source.

  processingDataSource.Order = 90;

  processingDataSource.Name = "Test Data Source";

  //Update the ProcessingSet object

  await proxy.UpdateAsync(data.WorkspaceId, processingDataSourceId, processingDataSource).ConfigureAwait(false);

}
```

## Validate a processing data source for deletion

- Method

-

ValidateDeleteAsync: Perform validations when data sources are being deleted

- Parameters

- <int>workspaceID: The workspace artifact ID where this processing data source resides

- <int> processingDataSourceID: The artifact ID of the processing data source to validate for deletion

- Returns

- DataSourceValidateDeleteResponse object

- <bool>CanDelete: Whether or not the data source can be deleted

- <string[]>Reasons - Array of reasons why the data source can not be deleted. Empty if the data source can be deleted.

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
using (IProcessingDataSourceManager proxy = _servicesMgr.CreateProxy<IProcessingDataSourceManager>(ExecutionIdentity.CurrentUser))

{

    DataSourceValidateDeleteResponse response = await proxy.ValidateDeleteAsync(data.WorkspaceId, processingDataSourceId).ConfigureAwait(false);

    // if the data source is not deletable, concatenate all the reasons why it couldn't

    if (!response.CanDelete)

    {

        string reasons = string.Join(", ", response.Reasons);

    }

}
```

## Retrieve processing source location paths

- Method

- RetrieveProcessingDataSourceInputPathsForWorkspaceAsync: Retrieves Processing Source Location paths associated with the Resource Pool for the workspace

- Parameters

- <int>workspaceID: The workspace artifact ID where this processing data source resides

- Returns

- List<string> containing each source location path associated with the resource pool for the given workspace

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
using (IProcessingDataSourceManager proxy = _servicesMgr.CreateProxy <IProcessingDataSourceManager>(ExecutionIdentity.CurrentUser)) {

  List < string > sourcePaths = await proxy.RetrieveProcessingDataSourceInputPathsForWorkspaceAsync(data.WorkspaceId).ConfigureAwait(false);

  // if there are more than zero source paths available, concatenate them into single string

  if (sourcePaths.Any()) {

    string reasons = string.Join(", ", sourcePaths);

  }

}
```

On this page

- Processing Data Source Manager

- Create a processing data source

- Read a processing data source

- Update a processing data source

- Validate a processing data source for deletion

- Retrieve processing source location paths


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
