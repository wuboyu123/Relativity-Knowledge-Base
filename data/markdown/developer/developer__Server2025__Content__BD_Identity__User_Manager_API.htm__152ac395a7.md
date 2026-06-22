---
title: "User Manager API"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/User_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:28:27+00:00
sha256: 1e6df541b89ae54da181ea04b9ccb86bbd5e51fbbed91f33aebd26b557728491
---

User Manager API Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# User Manager (.NET)

You add users to a Relativity environment to provide individuals with access to it. After creating users, you can add them to groups and assign permissions to the groups in various workspaces. For more information, see Users in the Relativity Documentation site.

The User Manager API exposes methods that provide the following functionality:

- Supports CRUD operations on users.

- Helper methods for retrieving user types and groups to associate with users.

- Helper methods for retrieving and querying on lists of users.

As a sample use case, you might use this API to implement a custom tool for importing users into Relativity. You could retrieve user information for display in a custom application.

You can also use the User Manager API through REST. For more information, see User Manager (REST) .

## Fundamentals for the User Manager API

Review the following information to learn about the methods and classes used by the User Manager API.

Methods

The User Manager API exposes the following methods on the IUserManager interface in the Relativity.Identity.<VersionNumber>.Services namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new user to Relativity. It returns a UserResponse object containing the Artifact ID and other properties of the new user. See Create a user .

- DeleteAsync() method - removes a user from Relativity. This overloaded method takes an optional CancellationToken object. See Delete a user .

- GetAvailableTypesAsync() method - retrieves a list of available choices for the user type. The default values are internal or external, but the Relativity UI supports adding any value. The type is used only for reference. See Retrieve all available types for users .

- QueryEligibleGroupsToAddUsersToAsync() method - retrieves a list of groups that are available for adding at least one of specified users. This method takes a list of user identifiers, and other arguments. You can pass optional CancellationToken and IProgress<ProgressReport> objects to this overloaded method.

- QueryGroupsByUserAsync() method - retrieves a list of groups in which the specified user is a member.

- ReadActiveUsersAsync() method - retrieves a list of all active users in a workspace. If the number of returned users exceeds the ChoiceLimitForUI setting, no users are returned.

- ReadAllUsersAsync() method - retrieves a list of all users in a workspace, including administrators and optionally deleted users.

- ReadAsync() method - retrieves metadata for a user, such as Relativity access, name, email, and other properties. You can also use this overloaded method to return extended metadata, including information about the operations that you have permissions to perform on the user, such as update or delete. See Retrieve metadata for a user .

- ReadSettingsAsync() method - retrieves the information about the current user, including the email, first name, last name, and settings for the user. See Retrieve settings for the current user .

- RetrieveAll() method - retrieves of all users and their information for a specified workspace. See Retrieve all users for a workspace .

- RetrieveAllWithRelativityAccessAsync() method - retrieves a list of users from the specified workspace that have Relativity access. To retrieve users from the admin-level content, set the workspace Artifact ID to -1.

- RetrieveCurrentAsync() method - retrieves the current user in the specified workspace.

- RetrieveUsersBy() method - gets a list of users and their information. This method supports filtering, ordering, and paging through results. See Query for users in a workspace .

The Artifact ID for the same user may be different across workspaces.

- UpdateSettingsAsync() method - modifies the user setting properties of the current user. You can use this overloaded method to restrict the update of a user to the last modification date by passing a DateTime object as an argument. It also takes an optional CancellationToken object. See Update settings for the current user .

- UpdateAsync() method - modifies the properties of a user. You can also use this overloaded method to restrict the update of a user to the last modification date by passing a DateTime object as an argument. It also takes an optional CancellationToken object. See Update properties for a user .

Classes and enumeration

The User Manager API uses the following methods classes and enumerations:

- DocumentViewer enumeration - indicates viewer modes that a user can access when reviewing documents as follows:

- Default

- HTML

- ActiveX

- RelativityReview

- DocumentViewerFileType enumeration - indicates the default viewer mode as follows:

- Default

- Viewer

- Image

- LongText

- Native

- Production

- DocumentViewerProperties class - represents user properties that are related to the document viewer.

- EmailPreference enumeration - indicates the preference for email notifications when adding or deleting users or groups as follows:

- Default

- All

- ErrorOnly

- None

- UserRequest class - represents the data used to create or update a user. The CreateAsync() and UpdateAsync() methods take an object of this type. Its properties include the email, first and last name, user type, and others.

- UserResponse class - represents the results of an operation. The ReadAsync(), CreateAsync() and UpdateAsync() methods return an object of this type. Its properties include the email, first and last name, user type, and others.

- UserSettingRequest class - represents the data used to update the settings of the current user. The UpdateSettingsAsync() method takes an object of this type. Its properties include the email, first and last name, email preference, and others.

- UserSettingResponse class - represents the results of a settings operation. The ReadSettingsAsync() and UpdateSettingsAsync() methods return an object of this type. Its properties include the email, first and last name, email preference, and others.

## Guidelines for the User Manager API

Use the following sample workflow to add users to your Relativity environment:

- Retrieve a list of user types available in a Relativity environment. See Retrieve all available types for users .

- Retrieve a list of available clients. You can use the Object Manager to query for clients.

- Add the user. See Create a user .

## Create a user

View code sample

Before creating a user, you need to identify the client and the user type. The following code sample illustrates how to use the CreateAsync() method to add a single user. It passes the Artifact ID of the client and the user type.

Use Artifact ID 663 for Internal and Artifact ID 672 for External

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
public async Task CreateUserAsync()

{

    int clientID = 1;

    int userTypeID = 1;



    UserRequest request = new UserRequest

    {

        AllowSettingsChange = true,

        Client = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = clientID }),

        DefaultFilterVisibility = true,

        DisableOnDate = new DateTime(2030, 12, 31),

        DocumentViewerProperties = new DocumentViewerProperties

        {

            AllowDocumentSkipPreferenceChange = true,

            AllowDocumentViewerChange = true,

            AllowKeyboardShortcuts = true,

            DefaultSelectedFileType = DocumentViewerFileType.Default,

            DocumentViewer = DocumentViewer.Default,

            SkipDefaultPreference = false

        },

        EmailAddress = "email address",

        EmailPreference = EmailPreference.Default,

        FirstName = "First",

        ItemListPageLength = 25,

        Keywords = string.Empty,

        LastName = "Last",

        Notes = string.Empty,

        RelativityAccess = true,

        SavedSearchDefaultsToPublic = true,

        TrustedIPs = string.Empty,

        Type = new ObjectIdentifier { ArtifactID = userTypeID }

    };



    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            UserResponse response = await userManager.CreateAsync(request);

            string info = string.Format("Created user with Artifact ID {0}", response.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve metadata for a user

View code sample

Use the overloaded ReadAsync() method to retrieve basic metadata for a user or extended metadata, which includes information about the operations that you have permissions to perform on this user. The following code sample illustrates how to call the ReadAsync() method by passing the Artifact ID of the user. If you want to return additional information, use the overloaded method by passing Boolean values set to true for additional metadata and permissions.

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
public async Task ReadUserAsync()

{

    int userArtifactID = 1;



    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            UserResponse response = await userManager.ReadAsync(userArtifactID);

            string info = string.Format("Read user {0} {1} with Artifact ID {2}", response.FirstName, response.LastName, response.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve settings for the current user

View code sample

Use the overloaded ReadSettingsAsync() method to retrieve the settings of the current user or extended metadata, which includes information about the operations that you have permissions to perform on the user settings. The following code sample illustrates how to call the ReadSettingsAsync() method. If you want to return additional information, use the overloaded method by passing Boolean values set to true for additional metadata and permissions.

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
public async Task ReadSettingsAsync()

{

    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            UserSettingResponse response = await userManager.ReadSettingsAsync();

            string info = string.Format("Read settings of user {0} {1}.", response.FirstName, response.LastName);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update properties for a user

View code sample

Use the UpdateAsync() method to modify the properties of a user. The following code sample illustrates how to call this method by passing the Artifact ID of the user, and a UserRequest object. This overloaded method also supports functionality for requesting the cancellation of the update, and monitoring progress.

Additionally, you can also restrict the update of a user to the last modification date by passing the value of LastModifiedOn property as an argument to the overloaded UpdateAsync() method.

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
public async Task UpdateUserAsync()

{

    int userArtifactID = 1;



    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            UserResponse userResponse = await userManager.ReadAsync(userArtifactID);

            UserRequest request = new UserRequest(userResponse);

            request.LastName = "Updated Last Name";

            request.FirstName = "Updated First Name";

            UserResponse updateResponse = await userManager.UpdateAsync(userArtifactID, request);

            string info = string.Format("Updated user with Artifact ID {0}", updateResponse.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update settings for the current user

View code sample

Use the UpdateSettingsAsync() method to modify the setting properties of the current user. The following code sample illustrates how to call this method by passing a UserSettingRequest object. This overloaded method also supports functionality for requesting the cancellation of the update, and monitoring progress. Additionally, you can also restrict the settings update to the last modification date by passing the value of LastModifiedOn property as an argument to the overloaded UpdateSettingsAsync() method.

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
public async Task UpdateUserSettingAsync()

{

    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            UserSettingResponse userResponse = await userManager.ReadSettingsAsync();

            UserSettingRequest request = new UserSettingRequest(userResponse);

            request.LastName = "Updated Last Name";

            request.FirstName = "Updated First Name";

            UserSettingResponse response = await userManager.UpdateSettingsAsync(request);

            string info = string.Format("Updated settings of user {0} {1}.", response.FirstName, response.LastName);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete a user

View code sample

Use the DeleteAsync() method to remove users from Relativity. The following code sample illustrates how to call this method by passing the Artifact ID of the user. This overloaded method also supports functionality for requesting the cancellation of the delete, and monitoring progress.

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
public async Task DeleteUserAsync()

{

    int userArtifactID = 1;



    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            await userManager.DeleteAsync(userArtifactID);

            string info = string.Format("Deleted user with Artifact ID {0}", userArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Helper methods for querying on users

The User Manager service exposes multiple helper methods that you can use to query for information about users.

### Retrieve all available types for users

View code sample

Use the GetAvailableTypesAsync() method to retrieve a list containing all the available choices for the user type. You can call this helper method before creating a user to get the Artifact ID of the user type.

The default values are internal or external, but the Relativity UI supports adding any value. The type is used only for reference.

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
public async Task GetAvailableTypesAsync()

{

    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await userManager.GetAvailableTypesAsync();

            foreach (DisplayableObjectIdentifier identifier in response)

            {

                string info = string.Format("Available user type with Artifact ID {0}.", identifier.ArtifactID);

                Console.WriteLine(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Retrieve all users for a workspace

View code sample

Use the RetrieveAll() method to retrieve a list containing all the users in a workspace.

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
public async Task RetrieveAll()

{

    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            int workspaceID = 1018249;

            List<UserInfo> response = await userManager.RetrieveAll(workspaceID);

            foreach (UserInfo userInfo in response)

            {

                string info = string.Format("Available user {0} with Artifact ID {1}.", userInfo.FullName, userInfo.ArtifactID);

                Console.WriteLine(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

### Query for users in a workspace

View code sample

Use the RetrieveUsersBy() method to query users in a workspace.

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
public async Task RetrieveUsersBy()

{

    using (Relativity.Identity.{versionNumber}.Services.IUserManager userManager = serviceFactory.CreateProxy<Relativity.Identity.{versionNumber}.Services.IUserManager>())

    {

        try

        {

            int workspaceID = 1018249;

            int start = 0;

            int length = 25;



            QueryRequest query = new QueryRequest

            {

                Condition = "'User Type' IN ['Internal']"

            };



            UserInfoQueryResultSet response = await userManager.RetrieveUsersBy(workspaceID, query, start, length);



            if (response.ResultCount > 0)

            {

                foreach (Services.Interfaces.UserInfo.Models.UserInfo userInfo in response.DataResults)

                {

                    string info = string.Format("Available user {0} with Artifact ID {1}.", userInfo.FullName, userInfo.ArtifactID);

                    Console.WriteLine(info);

                }

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

On this page

- User Manager (.NET)

- Fundamentals for the User Manager API

- Guidelines for the User Manager API

- Create a user

- Retrieve metadata for a user

- Retrieve settings for the current user

- Update properties for a user

- Update settings for the current user

- Delete a user

- Helper methods for querying on users

- Retrieve all available types for users

- Retrieve all users for a workspace

- Query for users in a workspace


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
