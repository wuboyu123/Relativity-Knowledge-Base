---
title: "Client Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Client_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:25:46+00:00
sha256: 58c0fd8035fd43e3c959916d1f3b2e44efeff59a26898a7e30b2cdba7bf40cf9
---

Client Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Client Manager (.NET)

In Relativity, a client is a company or organization, which is associated with users, matters, groups, and workspaces. For general information, see Clients on the Relativity Server 2025 Documentation site.

The Client Manager API exposes methods that provide the following functionality:

- CRUD operations on clients.

- Helper methods for retrieving lists of available groups, matters, users, and statuses.

- Methods for creating, submitting, and retrying client domain activation keys.

As a sample use case, you can programmatically create multiple clients by using the Client Manager API eliminating the need to manually add them through the Relativity UI.

You can also use the Client Manager API through REST. For more information, see Client Manager (REST) .

## Fundamentals for the Client Manager API

The Client Manager API contains the following methods and classes.

### Methods

The Client Manager API exposes the following methods on the IClientManager interface in the Relativity.Identity.<VersionNumber>.Services namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- ActivateClientDomainAsync() method - reruns a previously failed activation process. This method takes Artifact ID of a client. See Retry activating a client domain .

- CreateAsync() method - adds a new client to Relativity. This method takes a ClientRequest object and returns a ClientResponse object. See Create a client .

- CreateClientDomainRequestKeyAsync() method - creates and returns the client domain activation key required to initiate the activation process. This method takes the Artifact ID of a client and returns a string. See Create client domain activation key .

- DeleteAsync() method - removes a client from Relativity. This method takes the Artifact ID of a client. See Delete a client .

- GetEligibleStatusesAsync() method - retrieves a list of available statuses for a client. This method returns a list of DisplayableObjectIdentifier objects. See Retrieve available statuses .

- QueryGroupsAsync() method - retrieves information about groups associated with a client. This method takes a QueryRequest object, a start index, the number of groups to include in the results, and the Artifact ID of a client. It returns a QueryResultSlim object with a list of associated groups. See Retrieve associated groups .

- QueryMattersAsync() method - retrieves information about the matters associated with a client. This method takes a QueryRequest object, a start index, the number of matters to include in the results, and the Artifact ID of a client. It returns a QueryResultSlim object with a list of associated groups. See Retrieve associated matters .

- QueryUsersAsync() method - retrieves information about the users associated with a client. This method takes a QueryRequest object, a start index, the number of users to include in the results, and the Artifact ID of a client. It returns a QueryResultSlim object with a list of associated users. See Retrieve associated users .

- ReadAsync() method - retrieves basic or extended metadata for a client. Extended metadata includes operations that you have permissions to perform on the client, such as delete or update. This method takes the Artifact ID of a client and optional Boolean values indicating whether to return of extended metadata. This method returns a ClientResponse object. See Retrieve a client .

- SubmitClientDomainActivationKeyAsync() method - submits a client domain activation key and initiates the activation process. This method takes the Artifact ID of a client and the activation key. See Submit a client domain activation key .

- UpdateAsync() method - modifies the properties of a client. This overloaded method also supports restricting the update of a client to the date that it was last modified. It takes the Artifact ID of a client and an optional DateTime object. It returns a ClientResponse object. See Update a client .

### Classes

The Client Manager API includes the following classes available in the Relativity.Identity.Server.<VersionNumber>.ClientModels namespace.

- ClientRequest class - represents the data used to create or update a client.

Properties

Field Type Description

Name string The name of a client.

Number string The number assigned to a client.

Status ObjectIdentifier An object representing the status of a client. It has an ArtifactID property, which is a unique identifier for the status. It also has a list of GUIDs used to identify the status.

Keywords string Words or phrase used to describe a client.

Notes string Additional information about a client.

- ClientResponse class - represents an existing client.

Properties

Field Type Description

ArtifactID int A unique identifier for a client.

Guids List<Guid> A list of GUIDs used to identify a client.

Name string A user-friendly name for a client.

Number string The number assigned to a client.

Status DisplayableObjectIdentifier An object representing the status of a client. It has an ArtifactID property, which is a unique identifier for the status. It also has a list of GUIDs used to identify the status.

IsClientDomain bool A Boolean value indicating whether the client domain is activated for a client.

Keywords string Words or phrase used to describe a client.

Notes string Additional information about a client.

CreatedOn DateTime The date and time when the client was created.

CreatedBy DisplayableObjectIdentifier An object representing the user who created the client. Its properties include the name, the Artifact ID, and a list of GUIDs identifying the user.

LastModifiedBy DisplayableObjectIdentifier An object representing the user who last modified the client. Its properties include the name, the Artifact ID, and a list of GUIDs identifying the user.

LastModifiedOn DateTime The date and time when the client was last modified.

Meta Meta An object representing metadata for the client, including a list of read-only and unsupported fields.

Actions List<Action> A list of available actions that can be performed on the client. The properties for an Action object include the name of a REST operation, a Boolean value indicating whether permissions are required, and a list of reasons for the unavailability of the action.

## Guidelines for the Client Manager API

Review the following guidelines for working with the Client Manager API.

### Create a client proxy

You need to create a client proxy to use the Client Manager service. After creating the proxy, instantiate a ClientManager object as illustrated in the code sample.

Copy

```text
1
2
3
4
Uri keplerEndPoint = new Uri("http://localhost/relativity.rest/api");

Services.ServiceProxy.ServiceFactory serviceFactory = new Services.ServiceProxy.ServiceFactory(new Services.ServiceProxy.ServiceFactorySettings(keplerEndpoint,

  new Services.ServiceProxy.UsernamePasswordCredentials("username", "password")));

IClientManager clientManager = serviceFactory.CreateProxy<IClientManager>();
```

### Retrieve values from Task objects

When you call a method on the Client Manager API, it returns a Task object. To obtain the data in the Task object, retrieve the awaiter for the object, and call the GetResult() method.

Copy

```text
1
2
3
ClientResponse response = clientManager.CreateAsync(ClientRequest).GetAwaiter().GetResult();

List<DisplayableObjectIdentifier> response = clientManager.GetEligibleStatusesAsync().GetAwaiter().GetResult();

ClientResponse response = clientManager.ReadAsync(ClientID).GetAwaiter().GetResult();
```

### Use response data from read operations

You may want to update a client by using data obtained from a read operation. In the Client Manager API, the ReadAsync() method returns a ClientResponse object.

However, the UpdateAsync() method requires that you pass a ClientRequest object to it. You need to translate the data returned in a ClientResponse object from a read operation to the form required for a ClientRequest object as illustrated in the code sample.

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
ClientResponse entitiesClientResponse = clientManager.ReadAsync(ClientID).GetAwaiter().GetResult();

ClientRequest entitiesClientRequest = TranslateClientResponseToClientRequest(entitiesClientResponse);

private ClientRequest TranslateClientResponseToClientRequest(ClientResponse clientResponse) {

  ClientRequest clientRequest = null;

  if (clientResponse != null) {

    clientRequest = new ClientRequest {

      Name = clientResponse.Name,

        Keywords = clientResponse.Keywords,

        Notes = clientResponse.Notes,

        Number = clientResponse.Number,

        Status = clientResponse.Status

    };

  }

  return clientRequest;

}
```

## Create a client

Use the CreateAsync() method to add a new client to Relativity. This method takes a ClientRequest object and returns a ClientResponse object.

Required permissions

To use this endpoint, the caller must have the following:

- Add permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool Create(IHelper helper) {

  bool success = false;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      ClientRequest clientRequest = new ClientRequest {

        Name = "Name",

          Keywords = "Keywords",

          Notes = "Notes",

          Number = "50",

          Status = new ObjectIdentifier {

            ArtifactID = 622,

              Guids = new List < Guid > ()

          }

      };

      ClientResponse response = proxy.CreateAsync(clientRequest).GetAwaiter().GetResult();

      _logger.LogDebug("{ClientID} - {clientRequest.Name}", response.ArtifactID, response.Name);

      success = true;

    } catch (Exception ex) {

      _logger.LogError("Create failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

## Retrieve a client

Use the overloaded ReadAsync() method to retrieve basic or extended metadata for a client. Extended metadata includes operations that you have permissions to perform on the client, such as delete or update.

For basic client metadata, call the ReadAsync() method by passing the Artifact ID of a client. For extended metadata, pass Boolean values for both the includeMetadata and includeActions parameters on the overloaded method. This method returns a ClientResponse object.

Required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool Read(IHelper helper) {

  bool success = false;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      int clientArtifactID = 123123;

      bool includeMetadata = true;

      bool includeActions = true;

      ClientResponse response = proxy.ReadAsync(clientArtifactID, includeMetadata, includeActions).GetAwaiter().GetResult();

      _logger.LogDebug("{ClientID} - {clientRequest.Name}", response.ArtifactID, response.Name);

      success = true;

    } catch (Exception ex) {

      _logger.LogError("Read failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

## Update a client

Use the UpdateAsync() method to modify the properties of a client. This method takes the Artifact ID of a client and returns a ClientResponse object.

This overloaded method also supports restricting the update of a client to the date that it was last modified. To restrict the update, you must pass a DateTime object to the method as well.

The value for the DateTime object must match the LastModifiedOn date for the client stored in Relativity. Otherwise, you receive an error, indicating that the object has been modified.

Required permissions

To use this endpoint, the caller must have the following:

- Edit permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool Update(IHelper helper) {

  bool success = false;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      int clientArtifactID = 123123;

      ClientRequest clientRequest = new ClientRequest {

        Name = "Name",

          Keywords = "Keywords",

          Notes = "Notes",

          Number = "50",

          Status = new ObjectIdentifier {

            ArtifactID = 622,

              Guids = new List < Guid > ()

          }

      };

      ClientResponse response = proxy.UpdateAsync(clientArtifactID, clientRequest).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("Update failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

## Delete a client

Use the DeleteAsync() method to remove a client from Relativity. This method takes the Artifact ID of a client.

Before deleting a client, consider checking for dependent clients using Object Manager API. See Object Manager (.NET) .

Required permissions

To use this endpoint, the caller must have the following:

- Delete permissions for clients set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool Delete(IHelper helper) {

  bool success = false;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      int clientArtifactID = 123123;

      proxy.DeleteAsync(clientArtifactID).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("Delete failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

## Helper methods for CRUD operations

The following helper methods retrieve lists of available groups, matters, users, and statuses, which may be helpful when creating or updating clients. For general information, see Clients on the Relativity Server 2025 Documentation site.

### Retrieve associated groups

Use the QueryGroupsAsync() method to retrieve information about groups associated with a client. This method takes a QueryRequest object, a start index, the number of groups to include in the results, and the Artifact ID of a client. It returns a QueryResultSlim object with a list of associated groups. For more information about QueryResultSlim objects, see Query for Relativity objects .

Required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and groups set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool QueryGroups(IHelper helper) {

  bool success = false;

  int queryResultLimit = 100;

  string requestedGroupName = "GroupName";

  int clientArtifactID = 123123;

  QueryRequest query = new QueryRequest() {

    Condition = $ "'Name' == '{requestedGroupName}'",

      Fields = new [] {

        new FieldRef() {

          Name = "Name",

        },

      },

  };

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      List<DisplayableObjectIdentifier> eligibleStatuses = proxy.QueryGroupsAsync(query, 1, queryResultLimit, clientArtifactID).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("GetEligibleStatuses failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

### Retrieve associated matters

Use the QueryMattersAsync() method to retrieve information about the matters associated with a client. This method takes a QueryRequest object, a start index, the number of matters to include in the results, and the Artifact ID of a client. It returns a QueryResultSlim object with a list of associated matters. For more information about QueryResultSlim objects, see Query for Relativity objects .

Required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and matters set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool QueryMatters(IHelper helper) {

  bool success = false;

  int queryResultLimit = 100;

  int clientArtifactID = 123123;

  QueryRequest query = new QueryRequest() {

    Condition = "",

      Fields = new FieldRef[] {},

  };

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      QueryResultSlim response = proxy.QueryMattersAsync(query, 1, queryResultLimit, clientArtifactID).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("GetEligibleStatuses failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

### Retrieve associated users

Use the QueryUsersAsync() method to retrieve information about the users associated with a client. This method takes a QueryRequest object, a start index, the number of users to include in the results, and the Artifact ID of a client. It returns a QueryResultSlim object with a list of associated users. For more information about QueryResultSlim objects, see Query for Relativity objects .

Required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and users set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool QueryUsers(IHelper helper) {

  bool success = false;

  int queryResultLimit = 100;

  int clientArtifactID = 123123;

  QueryRequest query = new QueryRequest() {

    Condition = "",

      Fields = new FieldRef[] {},

  };

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      QueryResultSlim response = proxy.QueryUsersAsync(query, 1, queryResultLimit, clientArtifactID).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("GetEligibleStatuses failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

### Retrieve available statuses

Use the GetEligibleStatusesAsync() method to retrieve a list of available statuses for a client. This method returns a list of DisplayableObjectIdentifier objects.

Required permissions

To use this endpoint, the caller must have the following:

- View permissions for clients and choices set at the instance level. See Instance security on the Relativity Documentation site.

- View Admin Repository permissions set for Admin Operations at the instance level. Alternatively, the user must be a system admin.

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
public bool GetEligibleStatuses(IHelper helper) {

  bool success = false;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      List<DisplayableObjectIdentifier> eligibleStatuses = proxy.GetEligibleStatusesAsync().GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("GetEligibleStatuses failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

## Methods for client domain activation keys

The following methods support creating, submitting, and retrying client domain activation keys. For general information, see Client domains on the Relativity Documentation site.

### Create client domain activation key

Use the CreateClientDomainRequestKeyAsync() method to create and return the client domain activation key required to initiate the activation process. This method takes the Artifact ID of a client and returns a string, which is the key.

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
public bool CreateClientDomainRequestKey(IHelper helper) {

  bool success = false;

  int clientArtifactID = 123123;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      string response = proxy.CreateClientDomainRequestKeyAsync(clientArtifactID).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("GetEligibleStatuses failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

### Submit a client domain activation key

Use the SubmitClientDomainActivationKeyAsync() method to submit a client domain activation key and initiate the activation process. This method takes the Artifact ID of a client and the activation key.

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
public bool SubmitClientDomainActivationKey(IHelper helper) {

  bool success = false;

  int clientArtifactID = 123123;

  string activationKey = "Key";

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      proxy.SubmitClientDomainActivationKeyAsync(clientArtifactID, activationKey).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("SubmitClientDomainActivationKey failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

### Retry activating a client domain

Use the ActivateClientDomainAsync() method to rerun a previously failed activation process. This method takes Artifact ID of a client.

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
public bool ActivateClientDomain(IHelper helper) {

  bool success = false;

  int clientArtifactID = 123123;

  using (IClientManager proxy = helper.GetServicesManager().CreateProxy<IClientManager> (ExecutionIdentity.System)) {

    try {

      proxy.ActivateClientDomainAsync(clientArtifactID).GetAwaiter().GetResult();

      success = true;

    } catch (Exception ex) {

      _logger.LogError("ActivateClientDomain failed - {message}", ex.Message);

      throw;

    }

  }

  return success;

}
```

On this page

- Client Manager (.NET)

- Fundamentals for the Client Manager API

- Methods

- Classes

- Guidelines for the Client Manager API

- Create a client proxy

- Retrieve values from Task objects

- Use response data from read operations

- Create a client

- Retrieve a client

- Update a client

- Delete a client

- Helper methods for CRUD operations

- Retrieve associated groups

- Retrieve associated matters

- Retrieve associated users

- Retrieve available statuses

- Methods for client domain activation keys

- Create client domain activation key

- Submit a client domain activation key

- Retry activating a client domain


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
