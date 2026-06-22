---
title: "Basic concepts for Relativity API Helpers"
url: https://platform.relativity.com/Server2025/Content/Relativity_API_Helpers/Basic_concepts_for_Relativity_API_Helpers.htm
collection: developer
fetched_at: 2026-06-22T06:31:45+00:00
sha256: 1fc7668d25e7cb0c4833eb4a12d0d79720bd45c71ee1bc3ed21de5567b54f7af
---

Basic concepts for Relativity API Helpers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Basic concepts for Relativity API Helpers

Review these basic concepts to learn about how the Relativity API Helpers can simplify your development tasks. They include interfaces for creating the proxy, obtaining database contexts, and performing tasks through custom pages, event handlers, and agents.

## Reference the Relativity.API.dll in your projects

Add a reference to the Relativity.API.dll available in the SDK installer to Visual Studio before attempting to write code against the API Helper interfaces. The Relativity API Helpers provides several interfaces that you can use with agents, custom pages, and event handlers. The interfaces for use with each of these Relativity components contain similar methods. Consequently, you can write common code for connecting to databases and the Relativity Services API, or performing other tasks.

## Connect to the Services API

Use the CreateProxy() method to instantiate the ObjectManager from custom pages, event handlers, and agents. You call this method on the IServicesMgr object returned by the GetServiceManager() method. This method is available on the Helper classes for these components. To facilitate code reusability when working with the Services API, get the IServicesMgr by calling the GetServicesManager() method, and then pass this object to your data access layer. See the following sample code:

Copy

```text
1
using (IObjectManager objectManager = Relativity.CustomPages.ConnectionHelper.Helper().GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))
```

The CreateProxy() method uses the ExecutionIdentity enumeration to specify the authentication type. This enumeration includes CurrentUser, System, and Manual enums. The following table summarizes the behavior of the CurrentUser and System enums, which differ by the context in which you use them:

Context CurrentUser enum System enum

Agent Logs in as the Service account.

Uses IntegratedAuthCredentials. Logs in as the Service account.

Uses IntegratedAuthCredentials.

Custom page or event handler Logs in as a currently logged in user. Uses TokenCredentials. Logs in as the Service account.

Uses IntegratedAuthCredentials.

For additional information about using the API Helpers, review the code samples for agents , custom pages , and event handlers.

## Obtain a database context

Use the GetDBContext() method of the Helper class to return a database context object. It takes an integer representing ArtifactID of the workspace associated with the context that you want to return. The database context exposes methods for running various database query operations and managing database transactions. To obtain the database context, see the following code sample. The workspace ID is set to -1 to indicate the EDDS database in this sample.

Copy

```text
1
2
3
4
5
Relativity.API.IDBContext eddsDBContext = this.Helper.GetDBContext(-1);

Int32 workspaceCount = eddsDBContext.ExecuteSqlStatementAsScalar<Int32>("SELECT COUNT(*) FROM [Case]");

SqlParameter queueIDParam = new SqlParameter("@queueID", 11223344);

String sql = "SELECT * FROM [PatientProcessingQueue] WHERE [ID] = @queueID";

DataTable returnTable = eddsDBContext.ExecuteSqlStatementAsDataTable(sql, new SqlParameter[] { queueIDParam });
```

Use the database context to manage only an application's own data and schemas. Because schemas managed by Relativity or other applications may change at any time, interact with them through the APIs instead of using the database context.

We don't support interacting with Relativity tables or with other schemas through the database context.

The DefaultSqlCommandTimeout instance configuration setting can determine the value of the int timeoutValue parameter in Execute calls (such as ExecuteNonQuerySQLStatement and ExecuteSqlStatementAsDataSet). If your code passes 0 or less as the timeoutValue parameter, the timeout value will revert to using the value set for the instance configuration setting for DefaultSqlCommandTimeout. Should this configuration setting not exist in your environment, it is possible that the Timeout value will be set to 0.

While the Object Manager API is the preferred way for an application to interact with its data, using the database context may be more efficient in some circumstances, such as the following:

- Retrieving data using complex query logic such as inner or outer joins.

- Managing custom database artifacts such as triggers.

For more information, see the Object Manager (.NET) .

## Obtain user context information

Use the methods available in the UserInfo interface to return the information for the current (logged in) user. The methods include:

Name Description

ArtifactID Gets the user ID.

AuditArtifactID Gets the user ID to use for auditing purposes.

AuditWorkspaceUserArtifactID Gets the user workspace artifact ID to use for auditing purposes.

EmailAddress Gets the email address of the current user.

FirstName Gets the first name of the current user.

FullName Gets the full name of the current user.

LastName Gets the last name of the current user.

WorkspaceUserArtifactID Gets the current user workspace artifact ID.

The following example returns user information from a custom page:

Copy

```text
1
2
3
4
5
6
String firstName =

      Relativity.CustomPages.ConnectionHelper.Helper()

      .GetAuthenticationManager().UserInfo.FirstName;

String lastName =

      Relativity.CustomPages.ConnectionHelper.Helper()

      .GetAuthenticationManager().UserInfo.LastName;
```

## Obtain workspace ID

You can use the GetActiveCaseID() method of helper interfaces in custom pages and event handlers to return the workspace ID:

Copy

```text
1
workspaceArtifactIDParam.Value = this.Helper.GetActiveCaseID();
```

For additional information about using GetActiveCaseID(), review the code samples for custom pages and event handlers.

## Obtain the artifact GUID

You can use the GetGUID() method to return the GUID of a Relativity artifact based on the specified workspace ID and artifact ID from agents, custom pages, and event handlers.

Agent code sample Copy

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
using System;

namespace GetGuidSample

{

    [kCura.Agent.CustomAttributes.Name("Agent")]

    [System.Runtime.InteropServices.Guid("f14490b7-38cc-4840-b54d-e61d836301ab")]

    public class GetGuidAgent : kCura.Agent.AgentBase

    {

        private const int _EDDS_WORKSPACE_ARTIFACT_ID = -1;

        public override void Execute()

        {

            try

            {

                Guid kCuraStarterTemplateWorkspaceGuid = this.Helper.GetGuid(_EDDS_WORKSPACE_ARTIFACT_ID, 1014823);

                this.RaiseMessage(string.Format("The workspace GUID is: {0}", kCuraStarterTemplateWorkspaceGuid), 10);

            }

            catch (System.Exception ex)

            {

                //Your Agent caught an exception

                this.RaiseError(ex.Message, ex.Message);

            }

        }

        /**

         * Returns the name of agent

         */

        public override string Name

        {

            get

            {

                return "GetGuidAgent";

            }

        }

    }

}
```

Custom page code sample (web forms)

For more information about the starter template, see Starter template on the Relativity Server 2025 Documentation site.

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
using System;

namespace GetGuidCustomPage

{

    public partial class Default : System.Web.UI.Page

    {

        private const int _EDDS_WORKSPACE_ARTIFACT_ID = -1;

        protected void Page_Load(object sender, EventArgs e)

        {

            Guid kCuraStarterTemplateWorkspaceGuid = Relativity.CustomPages.ConnectionHelper.Helper().GetGuid(_EDDS_WORKSPACE_ARTIFACT_ID, 1014823);

            _workspaceGuid.Text = String.Format("kCura Starter Template Workspace GUID is: {0}", kCuraStarterTemplateWorkspaceGuid);

        }

    }

}

<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="GetGuidCustomPage.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head runat="server">

    <title></title>

</head>

<body>

    <form id="form1" runat="server">

     <div style="border: solid;border-color:#005C8A;width:400px;border-width:thick;text-align:center;font-family:Calibri;">

                  <h2 style="color:#EF922D;">

                        <asp:Label ID="_workspaceGuid" runat="server" Text="Workspace GUID: "></asp:Label>

                  </h2>

    </div>

    </form>

</body>

</html>
```

Event handler code sample (post-save) Copy

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
using System;

namespace GetGuidSample

{

    [kCura.EventHandler.CustomAttributes.Description("Post Save EventHandler")]

    [System.Runtime.InteropServices.Guid("bbfe4977-5e55-42c4-9c53-6ce8b22600f6")]

    public class GetGuidPostSaveEH : kCura.EventHandler.PostSaveEventHandler

    {

        private const int _EDDS_WORKSPACE_ARTIFACT_ID = -1;

        public override kCura.EventHandler.Response Execute()

        {

            //Construct a response object with default values.

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            retVal.Message = String.Empty;

            try

            {

                Guid kCuraStarterTemplateWorkspaceGuid = this.Helper.GetGuid(_EDDS_WORKSPACE_ARTIFACT_ID, this.Helper.GetActiveCaseID());

                //return a resonse of success false with the workspace's GUID

                retVal.Success = false;

                retVal.Message = String.Format("The current workspace's GUID is: {0}", kCuraStarterTemplateWorkspaceGuid);

            }

            catch (System.Exception ex)

            {

                //Change the response Success property to false to let the user know an error occurred

                retVal.Success = false;

                retVal.Message = ex.ToString();

            }

            return retVal;

        }

        /// <summary>

        /// The RequiredFields property tells Relativity that your event handler needs to access specific fields that you return in this collection property

        /// regardless if they are on the current layout or not. These fields are returned in the ActiveArtifact.Fields collection just like other fields that are on

        /// the current layout when the event handler is executed.

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get

            {

                kCura.EventHandler.FieldCollection retVal = new kCura.EventHandler.FieldCollection();

                return retVal;

            }

        }

    }

}
```

## Work with the Secret Store

Relativity API helpers provide an interface for the Secret Store. For general information, see Secret Store , see Relativity Server 2025 Documentation site.

Secrets written by your custom ADS application are stored in a dedicated area of the Secret Store.

### ISecretStore interface

Use the GetSecretStore() method to instantiate a helper object that implements the ISecretStore interface from custom pages, event handlers, and agents.

Copy

```text
1
2
3
4
5
//Get the ISecretStore interface using a helper from an agent or event handler

ISecretStore secretStore = this.Helper.GetSecretStore();



//Get the ISecretStore interface from a custom page helper

ISecretStore secretStore = Relativity.CustomPages.ConnectionHelper.Helper().GetSecretStore();
```

The ISecretStore interface provides synchronous and asynchronous methods for listing secret paths, reading secrets, setting secret data, and deleting secrets:

- Delete – deletes a secret at the given path.

- DeleteAsync – asynchronously deletes a secret the given path.

- Get – retrieves a secret for the given path.

- GetAsync – asynchronously retrieves a secret for the given path.

- List – gets the list of all secrets and sub-paths at the specified path.

- ListAsync – asynchronously gets the list of all secrets and sub-paths at the specified path.

- Set – writes a secret at the given path.

- SetAsync – asynchronously writes a secret at the given path.

In most cases, we recommend that you use asynchronous methods with await-async pattern with ConfigureAwait(false) method.

Copy

```text
1
await _secretStore.DeleteAsync("a/b").ConfigureAwait(false);
```

### Secret class

The Secret class represents a Relativity secret in the store. The Data property of the Secret class is the secret value stored as a dictionary.

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
//Instantiate a Secret object

Secret secretToWrite = new Secret();

//Instantiate the Data property of the secret as a Dictionary

secretToWrite.Data = new Dictionary<string, string>();

//Set the username value

secretToWrite.Data.Add("sqlUsername", "username");

//Set the password value

secretToWrite.Data.Add("sqlPassword", "password");
```

### Secret path

The secret is identified by a logical path, for example, 'database/credentials/user'. The path is not included as a property on the Secret object, but it can be retrieved using the list() and listAsync() methods. The methods retrives an array of paths as directory names (directories that have child secrets in them with an appended '/' character).

Copy

```text
1
string[] paths = secretStore.List(“database/credentials”);
```

The list methods return only the one directory level of the logical path. You can list all base directories for all secrets in the store by passing in ‘/’ as a logical root.To traverse the path from root to the secret, it may be necessary to call the list methods recursively.

Assume you have secrets with the following paths in your store:

- database/credentials

- database/credentials/sa

- database/credentials/user

If you pass the '/' as the list method parameter, it returns this list:

- database

- database/

If you pass 'database' as input parameter, it returns this list:

- database/credentials/sa

- database/credentials/user

### Secret store example

This example shows how to add a database username and password to the Secret Store, and then read and delete it:

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
//Get the Secret Store interface using a helper

ISecretStore secretStore = this.Helper.GetSecretStore();

//Instantiate a Secret object

Secret secretToWrite = new Secret();

//Instantiate the Data property of the secret as a Dictionary

secretToWrite.Data = new Dictionary<string, string>();

//Set the username value

secretToWrite.Data.Add("sqlUsername", "username");

//Set the password value

secretToWrite.Data.Add("sqlPassword", "password");

//Write the secret to the Secret Store

secretStore.Set("database/credentials", secretToWrite);

//Read the newly-added secret from the secret store

Secret secret = secretStore.Get("database/credentials");

//Delete the secret

secretStore.Delete("database/credentials");
```

## Work with instance settings

Relativity API helpers also provide an interface for accessing instance settings. For example, if your applications sends email notifications, it can read the SMTP instance settings values, such as SMTP host and password. For background information about instance settings, see Relativity Documentation site.

### InstanceSettingsBundle interface

Use the GetInstanceSettingBundle() method to instantiate a helper object that implements the InstanceSettingsBundle interface from custom pages, event handlers, and agents.

Copy

```text
1
2
3
4
5
6

//Get the instance settings interface using a helper from an agent or event handler

InstanceSettingsBundle instanceSettingsBundle = this.Helper.GetInstanceSettingBundle();



//Get the interface interface from a custom page helper

InstanceSettingsBundle instanceSettingsBundle = Relativity.CustomPages.ConnectionHelper.Helper().GetInstanceSettingBundle();
```

Instantiating the bundle retrieves both regular and encrypted instance settings from Relativity and creates a cache. The instance settings values are specific to the runtime, i.e., the for the host executing the application code. The instance settings values specific to other Relativity hosts are ignored. The cache is automatically updated.

The interface provides synchronous and asynchronous methods for accessing the instance settings values:

- GetBool – Reads an instance setting value as a boolean.

- GetBoolAsync – Asynchronously reads an instance setting value as a boolean.

- GetInt – Reads an instance setting value as an integer.

- GetIntAsync – Asynchronously reads an instance setting value as an integer.

- GetLong – Reads an instance setting value as a 64-bit integer.

- GetLongAsync – Asynchronously reads an instance setting value as a 64-bit integer.

- GetRawValues – Parses all instance setting values and places them into a dictionary.

- GetRawValuesAsync – Asynchronously parses all instance setting values and places them into a dictionary.

- GetString – Reads an instance setting value as a string.

- GetStringAsync – Asynchronously reads an instance setting value as a string.

- GetUInt – Reads an instance setting value as an unsigned integer.

- GetUIntAsync – Asynchronously reads an instance setting value as an unsigned integer.

- GetULong – Reads an instance setting value as an unsigned 64-bit integer.

- GetULongAsync – Asynchronously reads an instance setting value as an unsigned 64-bit integer.

The GetRawValuesAsync method can be used to create a dictionary that contains all instance settings values. All other get methods can be used to read individual values. The methods take in the instance name and section parameters and return the individual values. If the instance setting specified by section and name does not exist, a null value is returned.

The methods throw a TimeoutException if the bundle is not initialized within a reasonable time. This exception can only be thrown on the initial bundle load. Once a value has been cached, this method is guaranteed to return a value for the duration of the bundle's lifetime. It is recommend to perform a read a value from the bundle at application startup to ensure the cache has been populated.

### Instance settings example

The recommend workflow for interacting with instance settings from a Relativity application is as follows:

- Instantiate the interface: Copy

```text
1
2

InstanceSettingsBundle instanceSettingsBundle = this.Helper.GetInstanceSettingBundle();
```

- Read the values from the bundle using the appropriate get-method. The following example demonstrates how to read raw values into a dictionary and output them to the console, unless the value length exceeds 40 characters: Copy

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
System.Collections.Generic.IReadOnlyDictionary<string, System.Collections.Generic.IReadOnlyDictionary<string, object>> map = instanceSettingsBundle.GetRawValues();

foreach (string section in map.Keys)

{

    foreach (string name in map[section].Keys)

    {

        object currentValue = map[section][name];

        if (currentValue is string && ((string)currentValue).Length > 40)

        {

            currentValue = "<< TOO LARGE TO DISPLAY >>";

        }

        Console.WriteLine($"{section}.{name} = {currentValue}");

    }

}
```

## Use logging

Logging is built into the Relativity infrastructure and can be accessed using the API helpers . You can call the loggers from applications components, such as agents, custom pages, and event handlers.

The following code sample demonstrates how to call a default logger from an agent:

- Instantiate the logger. Copy

```text
1
2
private Relativity.API.IAPILog _logger;

_logger = this.Helper.GetLoggerFactory().GetLogger().ForContext<MyAgent>();
```

It is recommended to always scope a logger to a class using the ForContext<T>() method.

- Call the logger. Copy

```text
1
_logger.LogDebug(“Enabling agent {AgentName}”, Me.Name);
```

For more information, see Logging .

## Build friendly URLs for custom pages

Define the URL for a custom page accessed by an event handler by using the GetUrlHelper() and GetRelativePathToCustomPages() methods in the Relativity API Helpers. See the following code sample, which you could add to a Console event handler:

Copy

```text
1
2
String basePath = this.Helper.GetUrlHelper().GetRelativePathToCustomPages(new Guid("0540db69-cbec-48cf-9e55-701004ae922d"));

String fullCustomPagesPath = String.Format(@"{0}Home/Index?WorkspaceArtifactID={1}", basePath, this.Helper.GetActiveCaseID());
```

You may want to reference the RelativityInstanceURL instance setting when creating external links for users to access your application. Your system admin can configure this value for your environment. See Instance setting table and Instance settings' descriptions on the Relativity Server 2025 Documentation site.

## Use Relativity API Helpers for unit testing

The API Helpers are mockable interfaces that make unit testing easy to perform as illustrated in the following code sample:

Copy

```text
1
2
3
using Rhino.Mocks;

Relativity.API.IDBContext  workspaceDBContext;

workspaceDBContext = MockRepository.GenerateStrictMock<IDBContext>();
```

For more information about unit testing, see googletest .

On this page

- Basic concepts for Relativity API Helpers

- Reference the Relativity.API.dll in your projects

- Connect to the Services API

- Obtain a database context

- Obtain user context information

- Obtain workspace ID

- Obtain the artifact GUID

- Work with the Secret Store

- ISecretStore interface

- Secret class

- Secret path

- Secret store example

- Work with instance settings

- InstanceSettingsBundle interface

- Instance settings example

- Use logging

- Build friendly URLs for custom pages

- Use Relativity API Helpers for unit testing


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
