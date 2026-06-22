---
title: "Processing Set Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Set_Manager.htm
collection: developer
fetched_at: 2026-06-22T06:27:35+00:00
sha256: 39f943343dd9c729ecbc83e135d757b01fa05d71c816c30a03866258445b0afd
---

Processing Set Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Set Manager

This topic describes the IProcessingSetManager interface, which is used to access the Processing Set Manager service. The Processing Set Manager service supports read and save operations on processing set objects. The ProcessingSet class represents a processing set object that links a processing profile to one or more data sources. For more information, see Processing sets on the Relativity Documentation site.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Create a processing set

- Method

- CreateAsync: Creates a processing set. Returns the artifact id of the processing set

- Parameters

- <int>workspaceID: The workspace artifact ID where this processing set resides

- processingSet: The processing set to be created. This is a ProcessingSet object.

- <List<string>>EmailNotificationRecipients: An optional array of email addresses to be e-mailed when sets are completed

- <int>ProcessingSetID: set this property to 0, indicating that you are creating a new instance

- <string>Name: the name of the processing set

- ProcessingProfileRef: The profile associated with the set

- <int>ProcessingProfileID

- <string>Name

- Returns

- <int>ProcessingSetId: the artifact ID of the processing set that is created

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
ProcessingSet processingSet = new ProcessingSet {

  ProcessingSetID = 0, // Indicates a new ProcessingSet object.

    EmailNotificationRecipients = new List<string>() {

      "johnSmith@domain.com",

      "adamJohnson@domain.com"

    },

    Name = "Test Set",

    Profile = new ProcessingProfileRef(processingProfileArtifactId) // The Artifact ID of the processing profile.

};

using (IProcessingSetManager proxy = _servicesMgr.CreateProxy <IProcessingSetManager>(ExecutionIdentity.CurrentUser)) {

  int processingSetId = await proxy.CreateAsync(data.WorkspaceId, result).ConfigureAwait(false);

}
```

## Read a processing set

Read the values for the properties on a ProcessingSet object by calling the ReadAsync() method on the IProcessingSetManager. The ReadAsync() method requires that you pass the Artifact IDs of the ProcessingSet object and the workspace as arguments.

- Method

- ReadAsync: Reads a processing set. Returns the processing set belonging to the artifact id passed in

- Parameters

- <int>workspaceID: The workspace artifact ID where this processing set resides

- <int>processingSetID - ID of the processing set you want to read

- Returns

-

ProcessingSet object

Copy

```text
1
2
3
4
5
6
using (IProcessingSetManager proxy = _servicesMgr.CreateProxy<IProcessingSetManager>(ExecutionIdentity.CurrentUser)) {

  //Read the ProcessingSet object.

  ProcessingSet set = await proxy.ReadAsync(data.WorkspaceId, processingSetID).ConfigureAwait(false);

  //get the profile id of the set

  string profileId = $ "{processingSet.Profile.ProcessingProfileID}";

}
```

## Update a processing set

When updating a ProcessingSet instance, you call the ReadAsync() method on the proxy created with the IProcessingSetManager interface. Next, set the properties on the instance to their new values, and then call the UpdateAsync() method to persist your changes.

- Method

- UpdateAsync

- Parameters

- <int>workspaceID: The workspace that the processing set resides in

- <int>processingSetID: The artifact Id of this processing set

- processingSet: The processing set to be updated. This is a ProcessingSet object

- Returns

- <int>ProcessingSetId: the artifact ID of the set that is updated

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
using (IProcessingSetManager proxy = _servicesMgr.CreateProxy<IProcessingSetManager>(ExecutionIdentity.CurrentUser)) {

  //Read the ProcessingSet object.

  ProcessingSet processingSet = await proxy.ReadAsync(data.WorkspaceId, processingSetID);

  //Modify the list of email recipients list and the name of the processing set.

  processingSet.EmailNotificationRecipients = new List<string>() {

    "johnSmith@domain.com"

  };

  processingSet.Name = "Test Set";

  //Update the ProcessingSet object

  await proxy.UpdateAsync(data.WorkspaceId, processingSetID, processingSet).ConfigureAwait(false);

}
```

## Retrieve a list of processing sets and related aggregate information

You can use the GetDocumentAggregates() method to retrieve document totals and other information about processing sets in a specific workspace. To retrieve this information, the process sets must have the statuses of Completed or Completed with errors. If you wanted to create a custom dashboard for reporting purposes, use this method to populate it with information about completed processing sets. For example, Relativity uses the GetDocumentAggregates() method to populate the Early Case Assessment dashboard with processing set data.

- Method

- GetDocumentAggregates: Returns an object containing information about the processing sets retrieved from a specified workspace

- Parameters

- <int>workspaceID - The workspace that the processing set lives in

- <int>skip - Specifies the number used to identify a specific page of processing sets to return in the results set

- <int>top - The number of processing sets returned per page in the results set

- <string>sortColumnName - The name of column used for sorting results

- Valid options are as follows:

- PublishedDocumentCount

- PublishedDocumentSizeInBytes

- ProcessingSetDateCreated

- ProcessingSetName - the name used by default.

- <bool>sortDescending - Indicates the sort order for the results

- Returns

- ProcessingSetDocumentInfoSummary object

- <Int64>TotalPublishedDocuments: The total number of documents from all processing sets with the status of Completed or Complete with errors published to a workspace.

- <decimal>TotalPublishedDocumentSizeInBytes: The total number of bytes for documents from all processing sets with the status of Completed or Complete with errors published to a workspace.

- <int>TotalProcessingSets: The total number of processing sets with the status of Completed or Complete with errors in a workspace.

- ProcessingSetDocumentInfo: An array of ProcessingSetDocumentInfo objects.

- ProcessingSetId

- ProcessingSetName

- ProcessingSetDateCreated

- PublishedDocumentCount

- PublishedDocumentSizeInBytes

Copy

```text
1
2
3
using (IProcessingSetManager proxy = _servicesMgr.CreateProxy<IProcessingSetManager>(ExecutionIdentity.CurrentUser)) {

  ProcessingSetDocumentInfoSummary infoSummary = await proxy.GetDocumentAggregates(data.WorkspaceId, 0, 10, "ProcessingSetName", false).ConfigureAwait(false);

}
```

## Retrieve processing set summary data

- Method

- GetSummaryDataAsync

- Parameters

- <int>workspaceID: The workspace that the processing set resides in

- <int>processingSetID: The processing set to get summary data for

- Returns

- ProcessingSetSummaryData object

- SetState - ProcessingSetState object

- <int>ProcessingSetID

- <Guid>InventoryStatus

- <Guid>DiscoverStatus

- <Guid>PublishStatus

- <bool>Canceled

- <int>ProcessingProfileID

- <bool>HasRunningJobs

- <List<string>>EnvironmentErrors: the list of processing environment errors for the workspace

- <List<int>>DataSourceIDs: the array of data source Ids for the set

- <bool>DataSourceHasDocumentLevelErrors

- <bool>DataSourceHasJobLevelErrors - true or false

- <bool>HasValidProcessingProfile - true or false

- <bool>IsStoreValid - true or false

Copy

```text
1
2
3
using (IProcessingSetManager proxy = _servicesMgr.CreateProxy<IProcessingSetManager>(ExecutionIdentity.CurrentUser)) {

  ProcessingSetSummaryData summaryData = await proxy.GetSummaryDataAsync(data.WorkspaceId, processingSetID).ConfigureAwait(false);

}
```

On this page

- Processing Set Manager

- Create a processing set

- Read a processing set

- Update a processing set

- Retrieve a list of processing sets and related aggregate information

- Retrieve processing set summary data


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
