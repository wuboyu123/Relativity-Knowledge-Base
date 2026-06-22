---
title: "Processing Custodian Manager"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Custodian_Manager.htm
collection: developer
fetched_at: 2026-06-22T06:27:22+00:00
sha256: 1e035ff3beb738b090103d2f93a1bd2f3b87f141a9419634137972a102280fd6
---

Processing Custodian Manager Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Custodian Manager

This topic describes the IProcessingCustodianManager interface, which is used to access the Processing Custodian Manager service. The Processing Custodian Manager service supports read and save operations on custodian objects. The ProcessingCustodian class represents a custodian associated with the files that you want to process. For more information, see Entity object on the Relativity Documentation site.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Create a processing custodian

- Method

- CreateAsync: Creates a custodian and returns the artifact id of the custodian.

- Parameters

- <int>workspaceID : The workspace that the custodian resides in.

- custodian: The custodian to be saved. This is a ProcessingCustodian object.

- Returns

- <int>CustodianId: The artifactID of the custodian that is created.

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
//Build the ProcessingCustodian object.

ProcessingCustodian custodian = new ProcessingCustodian {

  CustodianID = 0, // Indicates a new ProcessingCustodian object.

    DocumentNumberingPrefix = "REL",

    FirstName = "John",

    LastName = "Smith"

};

using (IProcessingCustodianManager proxy = _servicesMgr.CreateProxy<IProcessingCustodianManager>(ExecutionIdentity.CurrentUser)) {

  //Create the ProcessingCustodian object

  int custodianID = await proxy.CreateAsync(data.WorkspaceId, custodian).ConfigureAwait(false);

}
```

## Read a processing custodian

Read the values for the properties on a ProcessingCustodian object by calling the ReadAsync() method on the proxy created with IProcessingCustodianManager interface. The ReadAsync() method requires that you pass the Artifact IDs of the ProcessingCustodian object and the workspace as arguments.

- Method

- ReadAsync: Returns the custodian for the artifact ID passed in.

- Parameters

- <int>workspaceID : The workspace that the custodian resides in.

- <int>custodianID: artifactID of the custodian you want to read.

- Returns

- ProcessingCustodian object

- <List<int>>Classifications: The Custodian classifications

- <string>DocumentNumberPrefix

- <string>FirstName

- <string>LastName

- <string>Notes

- <enum>CustodianType: NotSet, Other, or Person

- <int>CustodianID: custodian artifact ID

- <string>Name: corresponds to FullName

Copy

```text
1
2
3
4
5
6
7
using (IProcessingCustodianManager proxy = _servicesMgr.CreateProxy<IProcessingCustodianManager>(ExecutionIdentity.CurrentUser)) {

  //Read the ProcessingCustodian object

  ProcessingCustodian custodian = await proxy.ReadAsync(data.WorkspaceId, custodianID).ConfigureAwait(false);

  //Convert the last and first name of the custodian to a concatenated local string

  string fullName = $ "{custodian.LastName}, {custodian.FirstName}";

}
```

## Update a processing custodian

When updating a processing custodian, call the ReadAsync() method on the proxy created with the IProcessingCustodianManager interface. Next, set the properties on the instance to their new values, and then call the UpdateAsync() method to commit your updates.

- Method

- UpdateAsync: Updates the Custodian object and returns the artifact id of the custodian.

- Parameters

- <int>workspaceID : The workspace that the custodian resides in.

- <int>custodianID: artifactID of the custodian you want to update.

- custodian: The custodian to be updated. This is a ProcessingCustodian object.

- Returns

- <int>CustodianId: The artifactID of the custodian that is updated.

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
using (IProcessingCustodianManager proxy = _servicesMgr.CreateProxy<IProcessingCustodianManager>(ExecutionIdentity.CurrentUser)) {

  //Read the ProcessingSet object.

  ProcessingCustodian custodian = await proxy.ReadAsync(data.WorkspaceId, custodianID);

  //Modify the notes and first name of the custodian

  custodian.Notes = "updated notes";

  custodian.FirstName = "Test";

  //Update the ProcessingCustodian object. The service returns the Artifact ID of the object.

  await proxy.UpdateAsync(data.WorkspaceId, custodianID, custodian).ConfigureAwait(false);

}
```

On this page

- Processing Custodian Manager

- Create a processing custodian

- Read a processing custodian

- Update a processing custodian


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
