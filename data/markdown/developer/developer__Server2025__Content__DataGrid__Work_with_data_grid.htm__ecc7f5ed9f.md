---
title: "Work with data grid"
url: https://platform.relativity.com/Server2025/Content/DataGrid/Work_with_data_grid.htm
collection: developer
fetched_at: 2026-06-22T06:30:02+00:00
sha256: fdf08b2e1b11bb14ab606747411f0ab7b0f50707bf24d4aeb290c9112b4be426
---

Work with data grid

# Work with data grid

The Relativity platform provides several methods for programatically interacting with the data stored in the Data Grid. Review the use cases for the APIs to learn how you can use the APIs in your current development.

## Bulk load with Import API

To bulk load document extracted text into Data Grid, use the Import API. For more information, see Get started with the Import API .

## Work with document text data

To work with Data Grid text fields for individual documents, use the Services API and the REST API. Both APIs support these operations of the Data Grid-enabled fields:

- read

- query

- update

### Supported data grid query operators

Use these operators to query Data Grid-enabled fields:

- IS SET

- IS NOT SET

- The IS SET condition operator excludes the Data Grid records where the field is null or has an empty string value.

- IS LIKE operator is not supported.

### Services API query samples

Use the TextCondition class in the kCura.Relativity.Client namespace or the QueryAsync() method of the IObjectQueryManager interface to query Data Grid-enabled fields.

#### TextCondition

##### IS SET

Copy

```text
1
TextCondition condition = new TextCondition("Extracted Text", TextConditionEnum.IsSet);
```

##### IS NOT SET

Copy

```text
1
2
TextCondition condition = new TextCondition("Extracted Text", TextConditionEnum.IsSet);

NotCondition NotCriteria = new NotCondition(criteria);
```

#### ObjectQuery

##### IS SET

Copy

```text
1
var results = QueryAsync(_workspaceArtifactId, _documentObjectType, "'Extracted Text' LIKE 'Jamison'", _indexOfFirstDocumentInResult, _lengthOfResults, _includePermissions, _queryToken);
```

##### IS NOT SET

Copy

```text
1
var results = QueryAsync(_workspaceArtifactId, _documentObjectType, "NOT 'Extracted Text' ISSET", _indexOfFirstDocumentInResult, _lengthOfResults, _includePermissions, _queryToken);
```

### REST API query samples

You can also use the Relativity REST API to query text in the Data Grid. For general REST query information, see Query for resources .

##### IS SET

You can use the IS SET operator with Data Grid-enabled fields in any REST query condition:

Copy

```text
1
2
3
4
"query": {

   "condition":"'Extracted Text' ISSET",

   "fields":["Artifact ID", "Control Number", "Extracted Text"]

}
```

##### IS NOT SET

You can use the IS SET operator with Data Grid-enabled fields in any REST query condition:

Copy

```text
1
2
3
4
"query": {

    "condition":"NOT 'Extracted Text' ISSET",

    "fields":["Artifact ID", "Control Number", "Extracted Text"]

}
```

## Special considerations for updating Data Grid fields

When updating data grid-enabled document fields, note the following:

- Audit records are created for updated Data Grid-enabled fields.

- The oldValue and newValue stored with the Data Grid-enabled field audit details are truncated if they exceed 1,000,000 characters, same as the fields stored in the SQL database.

- If you update both SQL and Data Grid fields, and the SQL portion of the update fails, in most cases the change to Data Grid is successfully committed and an audit record is created, while the SQL fields remains unchanged.
