---
title: "Processing Custodian Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Custodian_Manager_REST.htm
collection: developer
fetched_at: 2026-06-22T06:27:23+00:00
sha256: 26410989875fcba301c9e69463f8ccce67802f614c43927260246c86676393e6
---

Processing Custodian Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Custodian Manager (REST)

This topic describes the custodians endpoint, which is used to access the Processing Custodian Manager service. The Processing Custodian Manager service supports read and save operations on custodian objects. A custodian is a user who's associated with the data included in a processing job. For more information, see Entity object on the Relativity Documentation site.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Create a processing custodian

To create a processing custodian, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/custodians
```

Request Body Example (entity type Individual)

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
{

    "custodian":

    {

        "DocumentNumberingPrefix":"test",

        "FirstName":"Test",

        "LastName":"User",

        "CustodianType":"Person"

    }

}
```

Request Body Example (entity type Other)

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
{

    "custodian":

    {

        "DocumentNumberingPrefix":"test",

        "Name":"test other",

        "CustodianType":"Other"

    }

}
```

- DocumentNumberingPrefix : the prefix applied to files when published through processing. For more information, see Processing sets on the Relativity Documentation site.

- FirstName and LastName : the first and last name of the custodian (for custodians of type Individual)

- Name : the name of the custodian (for custodians of type Other)

- CustodianType : indicates whether the custodian is an individual or an entity. It must be set to "Person" for an individual, or "Other" for a corporation, data location, or other construct. See Entity object on the Relativity Documentation site.

The response returns the Artifact ID of the custodian that was created or updated, such as the integer 1060372.

## Read a processing custodian

To read a processing custodian, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/custodians/{your custodian Artifact ID}
```

The response for custodian who is an individual contains the following fields:

- DocumentNumberingPrefix : the prefix applied to files when published through processing. For more information, see Processing sets on the Relativity Documentation site.

- FirstName and LastName : the first and last name of the custodian.

- CustodianType : returns "Person" indicating that the custodian is an individual.

- ArtifactId : the Artifact ID of the ProcessingCustodian object.

- Name : the full name of the custodian.

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

{

"DocumentNumberingPrefix": "Laura-"

"FirstName": "Laura"

"LastName": "Libera"

"CustodianType": "Person"

"ArtifactID": 1038911

"Name": "Libera, Laura"

}
```

The response for custodian that is an entity contains the same fields as a custodian who is a person. However, the CustodianType fields contains "Entity", and "FirstName" and "LastName" don't contain any values.

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

{

  "DocumentNumberingPrefix": "relativity-"

  "FirstName": "-"

  "LastName": "-"

  "CustodianType": "Entity"

  "ArtifactID": 1038912

  "Name": "Relativity ODA LLC"

}
```

## Update a processing custodian

To update a processing custodian, send a PUT request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/custodians/{your custodian Artifact ID}
```

Request Body Example (entity type Individual)

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
{

    "custodian":

    {

        "DocumentNumberingPrefix":"test",

        "FirstName":"Test",

        "LastName":"User",

        "CustodianType":"Person"

    }

}
```

Request Body Example (entity type Other)

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
{

    "custodian":

    {

        "DocumentNumberingPrefix":"test",

        "Name":"test other",

        "CustodianType":"Other"

    }

}
```

- DocumentNumberingPrefix : the prefix applied to files when published through processing. For more information, see Processing sets on the Relativity Documentation site.

- FirstName and LastName : the first and last name of the custodian (for custodians of type Individual)

- Name : the name of the custodian (for custodians of type Other)

- CustodianType : indicates whether the custodian is an individual or an entity. It must be set to "Person" for an individual, or "Other" for a corporation, data location, or other construct. See Entity object on the Relativity Documentation site.

The response returns the Artifact ID of the custodian that was created or updated, such as the integer 1060372.

On this page

- Processing Custodian Manager (REST)

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
