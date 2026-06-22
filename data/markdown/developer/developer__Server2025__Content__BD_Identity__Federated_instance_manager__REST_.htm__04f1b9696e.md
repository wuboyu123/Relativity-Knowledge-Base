---
title: "Federated Instance Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Federated_instance_manager__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:26:12+00:00
sha256: b8bdfbec39f5d8b5c94b5ff76a6c0be65f9494aa725efded2291f95cda8f50e3
---

Federated Instance Manager (REST)

# Federated Instance Manager (REST)

Federated instances enable users to easily switch between different Relativity environments using single sign-on. Relativity admins can manage the list of links to other environments displayed to the user in the UI. For more information, see Federated instances in the Relativity Documentation site.

The Federated Instance Manager service supports CRUD operations on federated instances. You can use this service after configuring a Relativity environment to use federated instances. For example, you can retrieve a list of all federated instances defined for a Relativity environment.

You can also use the Federated Instance Manager service through .NET. For more information, see Federated Instance Manager (.NET) .

## Guidelines for the Federated Instance Manager service

Review the following guidelines for working with the Federated Instance Manager service.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 or v2

- Set other path parameters in the URLs as necessary, such as a string for the {federatedInstanceName} .

For example, you can use the following URL to delete a federated instance:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/federated-instances/{federatedInstanceName}
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v2 .

- {federatedInstanceName} to the name of the instance.

### Required permissions

The Relativity user accessing the API must have the permissions for working with federated instance objects.

## Create a federated instance

To create a federated instance, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/federated-instances
```

The body of a request must contain a FederatedInstance object with the following fields:

- Name - a string representing the name of the federated instance.

- InstanceUrl - a string representing the URL to the external Relativity instance. The URL must include the prefix for the http or https protocol.

Copy

```text
1
2
3
4
5
6
{

   "instance":{

      "Name":"Sample Instance",

      "InstanceUrl":"https://sampleInstance.com/Relativity"

   }

}
```

When the federated instance is successfully created, the response returns the status code of 200. It returns 400 if the instance already exists. For more information, see HTTP status codes in Relativity REST APIs .

## Retrieve a single federated instance

To retrieve a single federated instance, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/federated-instances/{federatedInstanceName}
```

The request body is empty.

The response contains a FederatedInstance object with the following fields:

- Name - a string representing the name of the federated instance.

- InstanceUrl - a string representing the URL to the external Relativity instance. The URL must include the prefix for the http or https protocol.

Copy

```text
1
2
3
4
{

   "Name":"Sample Instance",

   "InstanceUrl":"https://sampleInstance.com/Relativity"

}
```

## Retrieve all federated instances

To retrieve all federated instances in a Relativity environment, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/federated-instances
```

The request body is empty.

The response contains a collection of FederatedInstance objects with the following fields:

- Name - a string representing the name of the federated instance.

- InstanceUrl - a string representing the URL to the external Relativity instance. The URL must include the prefix for the http or https protocol.

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
[

   {

      "Name":"Sample Instance",

      "InstanceUrl":"https://sampleInstance.com/Relativity"

   },

   {

      "Name":"Other Sample Instance",

      "InstanceUrl":"https://othersampleinstance.com/Relativity"

   }

]
```

## Update a federated instance

To update a federated instance, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/federated-instances
```

The body of a request must contain a FederatedInstance object with the following fields:

- Name - a string representing the name of the federated instance.

- InstanceUrl - a string representing the URL to the external Relativity instance. The URL must include the prefix for the http or https protocol.

Copy

```text
1
2
3
4
5
6
{

   "instance":{

      "Name":"Sample Instance",

      "InstanceUrl":"https://sampleInstance.com/Relativity"

   }

}
```

When the federated instance is successfully updated, the response returns the status code of 200. It returns 400 if the instance does not exist. For more information, see HTTP status codes in Relativity REST APIs .

## Delete a federated instance

To remove a federated instance from a Relativity environment, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/federated-instances/{federatedInstanceName}
```

The request body is empty.

When the federated instance is successfully deleted, the response returns the status code of 200. It returns 400 if the instance does not exist. For more information, see HTTP status codes in Relativity REST APIs .
