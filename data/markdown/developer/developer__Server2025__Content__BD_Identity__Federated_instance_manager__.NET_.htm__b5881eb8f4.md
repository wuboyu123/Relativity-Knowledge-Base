---
title: "Federated Instance Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Federated_instance_manager__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:26:11+00:00
sha256: 87dfe41e705b8881cbf0f057ff6a4580e94c4b5bf2e66f8fae394475ac11b143
---

Federated Instance Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Federated Instance Manager (.NET)

Federated instances enable users to easily switch between different Relativity environments using single sign-on. Relativity admins can manage the list of links to other environments displayed to the user in the UI. For more information, see Federated instances in the Relativity Documentation site.

The Federated Instance Manager API supports CRUD operations on federated instances. You can use this API after configuring a Relativity environment to use federated instances. For example, you can retrieve a list of all federated instances defined for a Relativity environment.

You can also use the Federated Instance Manager API through REST. For more information, see Federated Instance Manager (REST) .

## Fundamentals for the Federated Instance Manager API

Review the following information to learn about the methods and classes used by the Federated Instance Manager API.

Methods

The Federated Instance Manager API includes the following methods available on the IFederatedInstanceManager interface in the Relativity.Identity.<VersionNumber>.Services namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - creates new federated instance. This method takes FederatedInstance object. It returns a validation exception when the required fields are not populated or a federated instance with the same name already exists.

- DeleteAsync() method - removes a federated instance. This method takes the name of a federated instance. It returns a validation exception when the federated instance does not exist.

- ReadAllAsync() method - retrieves all federated instances defined for a Relativity instance. This method returns a IReadOnlyCollection of federated instances. If no federated instances exist, it returns an empty list.

- ReadAsync() method - retrieves a single federated instance by name. This method takes the name of an instance. It returns a FederateInstance object, or it returns a validation exception when the federated instance does not exist.

- UpdateAsync() method - modifies a federated instance. It returns a validation exception when the required fields are not populated, the federated instance does not exist, or federated instance with the name used for modifying the instance already exists.

Classes

- FederatedInstance class - contains the following properties:

- Name - a string representing the name of the federated instance. A federated instance name must be unique and may only contain alphanumeric characters and spaces. This value is not displayed to users.

- InstanceUrl - a System.Uri object representing the URL to the external Relativity instance. The URL must include the prefix for the http or https protocol.

## Guidelines for the Federated Instance Manager API

Review the following guidelines for the Federated Instance Manager API.

### Calls to the UpdateAsync() method

Use these steps when modifying a federated instance:

- Update the InstanceUrl property on the FederatedInstance object. This code sample uses the HRD URL parameter to redirect the user to an Integrated Authentication provider:

Copy

```text
1
fedInstance.InstanceUrl = "http://myRelativity.com/Relativity?HRD=integrated"
```

You cannot update the name of an existing federated instance.

- Call the UpdateAsync() method and pass it the updated object:

Copy

```text
1
await fedInstanceManager.UpdateAsync(fedInstance);
```

## Code sample

The following code sample illustrated how to create a federated instance and add a HRD redirect to the URL.

The Relativity user accessing the API must have the permissions for working with federated instance objects.

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
using (IFederatedInstanceManager federatedInstanceManager = new ServiceFactory(settings).CreateProxy<IFederatedInstanceManager>())

{

    IReadOnlyCollection<FederatedInstance> federatedInstances = await federatedInstanceManager.ReadAllAsync();

    FederatedInstance expectedInstance = new FederatedInstance() {

        Name = "Other Instance",

        InstanceUrl = new Uri("https://otherInstance.com/Relativity") }

    ;

    if (!federatedInstances.ToList().Exists(x => x.Name.Equals(expectedInstance.Name)))

    {



        await federatedInstanceManager.CreateAsync(expectedInstance);

    }

}
```

On this page

- Federated Instance Manager (.NET)

- Fundamentals for the Federated Instance Manager API

- Guidelines for the Federated Instance Manager API

- Calls to the UpdateAsync() method

- Code sample


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
