---
title: "Instance setting table overview"
url: https://help.relativity.com/Server2025/Content/System_Guides/Instance_Setting_Guide/Instance_setting_table.htm
collection: user
fetched_at: 2026-06-22T06:03:33+00:00
sha256: fcef4e9d55e86b0e636b4172dc620027fe5c81626e77b0d782031d688898f90b
---

Instance setting table overview

# Instance setting table

This guide provides a description of each entry in the Instance setting table, along with each entry’s default value.

For more information about backwards compatibility, see Upgrade considerations for Relativity .

See these related pages:

- Instance settings' descriptions

- Upgrade considerations for Relativity

## Accessing the instance setting table

To access the instance setting table, perform the following steps:

- Access the primary server environment containing all databases, including EDDS.InstanceSetting.

- Connect to the Microsoft SQL Server Management Studio.

- In the Object Explorer tree, expand Databases > EDDS > Tables .

- Right-click the eddsdbo.InstanceSetting table, and select the option Select Top 1000 Rows .

The eddsdbo.InstanceSetting table opens. It displays the Section, Name, MachineName, Value, Description, InitialValue, ArtifactID, and Encrypted columns for all the entries in the table.

If the MachineName field is empty, this is the default value for all machines in the Relativity instance. Otherwise, this value for the setting only applies to the specified machine, overwriting the default value.

- Locate the instance setting you want to change and update the Value column.

-

We recommend creating, updating, and deleting instance settings using the Instance Settings tab. See Instance settings . Using the Instance Settings tab ensures that an audit of changes to an instance setting exists.

You can create, update, and delete instance settings through SQL, however, note that doing so could have a significant effect on the performance and functionality of your Relativity environment.

Refer to Instance settings for a complete list of Relativity instance setting values.

## Adding and deleting instance settings with stored procedures

If the Relativity UI is not available, you can create and delete instance settings using the stored procedures in the Relativity EDDS database. For example, the stored procedures can be used during the initial installation and configuration or when adding new servers.

### CreateInstanceSetting

The CreateInstanceSetting stored procedure creates an instance setting based on specified parameters.

You can't update encrypted instance settings by running the stored procedure. However, you can use the stored procedure to update settings that aren't encrypted.

Parameters :

- @section NVARCHAR(200)

- @name NVARCHAR(200)

- @machineName VARCHAR(200) = ''

- @value NVARCHAR(200) = ''

- @valueType NVARCHAR(200) = 'Text'

- @description NVARCHAR(MAX) = NULL

- @initialValue NVARCHAR(MAX) = NULL

- @createAsSystemArtifact BIT = 0

Only the @section and @name parameters are required. All other parameters have set default values if you choose not to use them.

Instance settings with non-text values should not ever have empty values. The creation of such instance settings will fail.

This example creates the Relativity.Authentication.AccessTokenExtraLifetime for the RelWeb01 server. It has a value of 120 (though we decided to label the installation default value as 240, as a guide to environmental administrators that 240 may be a more recommended value) as is explicitly a nonnegative 32-bit integer.

```text
-- THIS EXAMPLE IS OK.  It will fail if the Instance Setting already exists.

EXEC [eddsdbo].CreateInstanceSetting
    @section = 'Relativity.Authentication', @name = 'AccessTokenExtraLifetime', @machineName = 'RelWeb01',
    @value = '120',
    @description = 'The number of minutes that the authentication cookie is valid.',
    @valueType = 'Nonnegative Integer 32-bit',
    @initialValue = '240'
```

### DeleteInstanceSetting

The DeleteInstanceSetting stored procedure deletes an instance setting based on specified parameters.

Parameters :

- @section NVARCHAR(200)

- @name NVARCHAR(200)

- @machineName VARCHAR(200) = ''

This example demonstrates how to delete the Relativity.Authentication.AccessTokenExtraLifetime for instance setting we created in the first example:

```text
EXEC [eddsdbo].DeleteInstanceSetting @section = 'Relativity.Authentication', @name = 'AccessTokenExtraLifetime', @machineName = 'RelWeb01'
```
