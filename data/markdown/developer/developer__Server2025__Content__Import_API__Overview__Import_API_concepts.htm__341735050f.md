---
title: "Basic Import API concepts"
url: https://platform.relativity.com/Server2025/Content/Import_API/Overview/Import_API_concepts.htm
collection: developer
fetched_at: 2026-06-22T06:29:57+00:00
sha256: 5d6c564b0f81f8079cfa255e030448e743df73a20badd84bafd0da056f7947ee
---

Basic Import API concepts Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Basic Import API concepts

The Import API provides functionality for creating custom import utilities for documents, images, production sets, and Relativity Dynamic Objects (RDOs).

While you can implement a variety of custom import utilities, the Import API doesn't support calls made to it from within event handlers.

See these related pages:

- ImportAPI class

- ImportBulkArtifactJob class

- Import API events

## Key features

You can develop utilities for importing data from a staging database, eliminating the need to export it to a load file before adding it to Relativity. Data can also be imported from multiple, separate databases into Relativity, or from one Relativity workspace to another. Key classes include:

- ImportAPI class – contains the methods, properties, and other members for developing these utilities.

- ImportBulkArtifactJob and ImageImportBulkArtifactJob classes – support the import of large numbers of RDOs and images respectively.

While the Import API continues to support the DataClientReader, we recommend using the ImportAPI class for all new development projects.

## Authentication

The authentication compatibility matrix summarizes support for authentication methods used by the ImportAPI class:

Authentication methods Custom Page Agent Desktop

Relativity username and password Supported Supported Supported (preferred)

Bearer token authentication Supported (preferred) Supported (preferred) Not supported

Windows authentication Not supported Not supported Not supported

If you have been considering using Windows authentication, we recommend using bearer token authentication instead. See the posts about the Import API on DevHelp. To view the content associated with this link, you must be logged into DevHelp .

### Authentication code samples

The following code samples illustrate how to use the authentication methods listed in the authentication compatibility matrix:

- Relativity username and password – the user must be a member of the System Administrators group in Relativity. These permissions are similar to those required to import a load file through the RelativityDesktop Client. Copy

```text
1
ImportAPI iapi = new ImportAPI(relativityUserName, relativityPassword, relativityWebAPIUrl);
```

The expiration time for authentication with Relativity username and password is 240 minutes, which is the default time limit. The expiration time limit starts as soon the ImportAPI class object is constructed.

- Bearer token – uses the current claims principal token to authenticate and should only be used by Relativity Service Account hosted processes. This is the preferred method for using Import API within an agent or custom page. Copy

```text
1
ImportAPI iapi = ImportAPI.CreateByRsaBearerToken(relativityWebAPIUrl);
```

Bearer tokens are only supported by the ImportAPI.CreateByRsaBearerToken() method, which automatically handles authentication and token expiration. The expiration time for authentication with a bearer token is 4,320 minutes, which is the default time limit. Bearer tokens are automatically refreshed, so they don’t have an expiration time.

When developing custom applications using the Import API, call the CreateByRsaBearerToken() method to create the ImportAPI object. The RSA token is then automatically used for authentication. For sample code, see Bearer token authentication .

Authentication is performed when the ImportAPI class is instantiated because all the services available through this class require it. If authentication fails, an exception is thrown.

## Source table

Your source database table can consist entirely of text fields (such as varchar and nvarchar). The Import API converts these text fields to one of the Relativity data types, such as Boolean, Date, Integer, Currency, or Decimal. Empty text fields in the source table are converted to NULL values.

When working with DataTable objects, use their CreateDataReader() method to retrieve an IDataReader. When executing SQL, use the ExecuteReader() method of the SqlCommand object to retrieve an IDataReader. See the following code samples:

- Import documents with native files

- Import data into RDOs

- Import images

- Import produced images

## Specify folders for import jobs

The Import API provides properties that you can set to specify a folder used during import. The following properties are on classes in the kCura.Relativity.DataReaderClient namespace:

- FolderPathSourceFieldName property – For native files, you can set this property on the Settings class. The Import API handles a folder specified that has this property set as follows:

- If the folder already exists, Relativity imports the documents to it.

- If the folder doesn't exist, Relativity creates the folder and imports the documents to it.

- If you specify a folder path that includes nested folders, as in the following example, Relativity creates all of these folders. Copy

```text
1
2
table.Rows.Add("ImportAPI_Doc1", "ImportAPI-1st Doc loaded", "Relative;Private", "RelativityUser", 12.80, "12/31/1999", "Yes", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "Files\\SampleImport", "C:\\Shared\\ImportingDocs\\Data\\Native\\ImportAPI_Doc1.msg");

table.Rows.Add("ImportAPI_Doc2", "ImportAPI-2nd Doc loaded", "Private", "RelativityUser", 101.00, "Monday January 4 2010", "No", "The quick brown fox jumps over the lazy dog", "Files\\SampleImport", "C:\\Shared\\ImportingDocs\\Data\\Native\\ImportAPI_Doc2.msg");
```

You must use double back-slashes to separate folder names.

When you map a Document field to a folder source setting, then it will be only used for setting the folders and it won’t be considered as a regular Document field, so that field's value will not be updated.

-

ParentObjectIdSourceFieldName – The name of the field that contains a unique identifier for the record of the parent object associated with the current record.

While, technically, both FolderPathSourceFieldName and ParentObjectIdSourceFieldName properties can be set, the values assigned to them must be identical. If they are not equal, then an exception is thrown containing the message “Only set one of ParentObjectIdSourceFieldName and FolderPathSourceFieldName."

- DestinationFolderArtifactID property – available for native files, images, and documents on the ImportSettingsBase class. It represents the ArtifactID of the target folder for the import job, where all native files, images, or documents are added.

If the folder specified by the DestinationFolderArtifactID property doesn’t exist, the import job fails with errors.

On this page

- Basic Import API concepts

- Key features

- Authentication

- Authentication code samples

- Source table

- Specify folders for import jobs


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
