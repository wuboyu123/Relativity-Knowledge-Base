---
title: "Instance Setting Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Instance_Setting_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:22:58+00:00
sha256: a3a8a60ea0009b25f59d75c0c70c8f03cd6ca8408f886d3084f333385012daf4
---

Instance Setting Manager (.NET)

# Instance Setting Manager (.NET)

The Instance Setting Manager API supports create, read, update, and delete operations in a Relativity environment. With the create method, you can set the value for the instance setting, and its initial or default value. For general information, see Instance settings on the Relativity Documentation site.

Sample use cases for the Instance Setting Manager API include:

- Updating instance setting values to support behavior implemented by a custom application. You might implement a custom application that sends out email notifications and want to programmatically update the From and To fields on the messages by setting the EmailFrom and EmailTo instance settings.

- Updating instance setting values to modify or customize existing Relativity behavior. For example, you might want to programmatically change the time frame for running off hour agents by updating the AgentOffHourEndTime and AgentOffHourStartTime instance settings.

You can also use the Instance Setting Manager service through REST. For more information, see Instance Setting Manager (REST) .

## Fundamentals for the Instance Settings Manager API

The Instance Setting Manager API contains the following methods, classes, and enumerations.

Methods

The Instance Setting Manager API exposes the following methods on the IInstanceSettingManager interface in the Relativity.Services.Environment.<VersionNumber>.InstanceSetting namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new instance setting to a Relativity environment. This method takes an InstanceSettingRequest object as an argument. It returns the Artifact ID of the new instance setting. See Create an instance setting .

- DeleteAsync() method - removes an instance setting from a Relativity environment. It takes the Artifact ID of an instance setting. This method returns a task. See Delete an instance setting .

- ReadAsync() method - retrieves the properties for an instance setting. This method takes the Artifact ID of an instance setting as an argument. It returns a InstanceSettingResponse object. See Read an instance setting .

- UpdateAsync() method - modifies Machine, Value, Encrypted, Keywords and Notes properties on an instance setting. This method takes an InstanceSettingRequest object, and an optional DateTime object to restrict the update to the date last modified. This method returns a task. See Update an instance setting .

Classes and enumerations

The Instance Setting Manager API includes the following classes and enumeration:

- InstanceSettingRequest class - represents the data used to create or update an instance setting. Its properties include the name of the instance setting, its value and a default value, and others. The CreateAsync() and UpdateAsync() methods take an object of this type.

- InstanceSettingResponse class - represents the response from a read operation. Its properties include the name of an instance setting, its Artifact ID, the section of the Instance settings table where it exists, and others. See InstanceSettingResponse Class .

- InstanceSettingValueTypeEnum enumeration - indicates the value type of an instance setting, such as text, Integer32, TrueFalse, or other. See InstanceSettingValueTypeEnum Enumeration .

## Create an instance setting

Instance settings are used to control specific behavior in Relativity, such as query time outs, time frames for running certain agents, and other configuration options. For more information and a list of available settings, see Instance settings on the Relativity Documentation site.

To create an instance setting, call the CreateAsync() method by passing an InstanceSettingRequest object to it. The method returns the Artifact ID of the new instance setting.

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for the instance setting set at the instance level. See Instance security on the Relativity Documentation site.

View code sample Copy

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
public async Task<bool> Create(Relativity.Environment.V1.InstanceSetting.IInstanceSettingManager instanceSettingManagerProxy)

{

    bool success = false;

    try

    {

        InstanceSettingRequest request = GetRequestTemplate("SampleName", "SampleSection");

        request.ValueType = InstanceSettingValueTypeEnum.Text;

        request.Value = "Sample Text Value";

        request.InitialValue = "Sample Text Initial Value";

        int artifactID = await instanceSettingManagerProxy.CreateAsync(request);

        if (artifactID != 0)

        {

            _logger.LogDebug("Instance Setting has been created");

            success = true;

        }

    }

    catch (Exception ex)

    {

        _logger.LogError(ex, "Exception while creating Instance Setting");

        throw;

    }

    return success;

}
```

## Read an instance setting

Use the ReadAsync() method to retrieve the properties for an instance setting. Pass the Artifact ID of an instance setting to this method. It returns an InstanceSettingResponse object.

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for instance settings set at the instance level. See Instance security on the Relativity Documentation site.

View code sample

The following code sample illustrates how to create an instance setting, and then read its properties.

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
public async Task<bool> Read(Relativity.Environment.V1.InstanceSetting.IInstanceSettingManager instanceSettingManagerProxy, int artifactID)

{

    bool success = false;

    try

    {

        InstanceSettingResponse response = await instanceSettingManager.ReadAsync(artifactID);

        if (response != null && response.ArtifactID == artifactID)

        {

            _logger.LogDebug(string.Format("Retrieved an Instance Setting: section: '{0}', name: '{1}'", response.Section, response.Name));

            success = true;

        }

    }

    catch (Exception ex)

    {

        _logger.LogError(ex, "Exception while reading Instance Setting");

        throw;

    }

    return success;

}
```

## Update an instance setting

You can update the Machine, Value, Encrypted, Keywords and Notes properties of an instance setting. To update an instance setting, call the UpdateAsync() method by passing an InstanceSettingRequest object to it.

Additionally, you can restrict the update of an instance setting to the date that it was last modified, Pass the value of LastModifiedOn property as an argument to one of the overloaded update methods. You can get the value of this property from an InstanceSettingResponse object, which is returned by the ReadAsync() method.

View required permissions

To use this endpoint, the caller must have the following:

- Edit permissions for instance settings set at the instance level. See Instance security on the Relativity Documentation site.

View code sample Copy

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
public async Task<bool> Update(Relativity.Environment.V1.InstanceSetting.IInstanceSettingManager instanceSettingManagerProxy, int artifactID)

{

    bool success = false;

    try

    {

        InstanceSettingRequest request = GetRequestTemplate("SampleName", "SampleSection");

        request.ValueType = InstanceSettingValueTypeEnum.Text;

        request.Value = "Modified Text Value";

        request.ArtifactID = artifactID;

        await instanceSettingManager.UpdateAsync(request);

        _logger.LogDebug("Updated an Instance Setting");

        success = true;

    }

    catch (Exception ex)

    {

        _logger.LogError(ex, "Exception while updating Instance Setting");

    }

    return success;

}
```

## Delete an instance setting

To delete an instance setting, call the DeleteAsync() method by passing the Artifact ID of an instance setting to it.

View required permissions

To use this endpoint, the caller must have the following:

- Delete permissions for instance settings set at the instance level. See Instance security on the Relativity Documentation site.

View code sample

The following code sample illustrates how to create and then delete an instance setting.

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
public async Task<bool> Delete(Relativity.Environment.V1.InstanceSetting.IInstanceSettingManager instanceSettingManagerProxy, int artifactID)

{

    bool success = false;

    try

    {

        await instanceSettingManager.DeleteAsync(artifactID);

        _logger.LogDebug("Deleted an Instance Setting");

        success = true;

    }

    catch (Exception ex)

    {

        _logger.LogError(ex, "Exception while deleting Instance Setting");

        throw;

    }

    return success;

}
```

## Helper method in code samples

The code samples for the Instance Setting Manager API use the GetRequestTemplate() method as a helper for demonstrating calls to this service. This method sets general properties for a sample instance setting.

View code sample Copy

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
private static InstanceSettingRequest GetRequestTemplate(string name, string section)

{

    return new InstanceSettingRequest

    {

        Name = name,

        Section = section,

        Machine = "",

        Encrypted = false,

        Description = "Sample Description",

        Keywords = "Sample Keywords",

        Notes = "Sample Notes"

    };

}
```
