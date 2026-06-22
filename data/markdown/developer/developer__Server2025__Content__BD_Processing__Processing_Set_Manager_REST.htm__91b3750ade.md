---
title: "Processing Set Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Set_Manager_REST.htm
collection: developer
fetched_at: 2026-06-22T06:27:36+00:00
sha256: 7d9f470f8065073a3225cf25729a411c64de0d2824d2c81f779cf2f29dd6d3ce
---

Processing Set Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Set Manager (REST)

This topic describes the processing-sets endpoint, which is used to access the Processing Set Manager service. The Processing Set Manager service supports read and save operations on processing set objects.A processing set object links a processing profile to one or more data sources. For more information, see Processing sets on the Relativity Documentation site.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Create a processing set

To create a processing set, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-sets
```

Request Body Example

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
"processingSet":

    {

        "EmailNotificationRecipients":["test@test.com"],

        "Profile":{

            "ProcessingProfileID":1041234

        },

        "Name":"mytestset"

    }
```

The response returns the Artifact ID of the processing set that was created or updated, such as the integer 1046784.

## Read a processing set

To read a processing set, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-sets/{your set Artifact ID}
```

## Update a processing set

To update a processing set, send a PUT request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-sets/{your set Artifact ID}
```

Request Body Example

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
"processingSet":

    {

        "EmailNotificationRecipients":["test@test.com"],

        "Profile":{

            "ProcessingProfileID":1041234

        },

        "Name":"update set name"

    }
```

## Retrieve document aggregates

To retrieve document aggregates and other information about processing sets with the status of Completed or Completed with errors in a specific workspace, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-sets/documents?skip=0&top=10&sortColumnName={sort column name, for example ProcessingSetName}&sortDescending={true or false}
```

## Retrieve processing set summary data

To retrieve processing set summary data in a specific workspace (such as environment errors, discover and publish status) send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/processing-sets/{your set Artifact ID}/summary
```

On this page

- Processing Set Manager (REST)

- Create a processing set

- Read a processing set

- Update a processing set

- Retrieve document aggregates

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
