---
title: "Auto increment field on object"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Auto_increment_field_on_object.htm
collection: user
fetched_at: 2026-06-22T06:09:42+00:00
sha256: a2b7244726eac1c9b61c4d58d5426022dbe76396de65faa564297eaefd9e6270
---

Auto increment field on object Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Auto increment field on object

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Auto Increment Field on Object solution calculates and adds an incremental value to a field automatically each time a user creates a new record for an object. This solution is not supported for the document object.

## Before you begin

The Auto Increment Field on Object solution calculates and adds an incremental value to a fixed-length text or long text field automatically each time a user creates a new record for an object. The value uses the format < prefix >< padded number >, where prefix is a set of characters that you can optionally specify for the first part of the value. Padded number is the number of digits that you want to pad the second, numeric part of the value with. When you configure the solution, you can also specify the starting value and increment to use when calculating values. To see examples of how the solution calculates values based on various configuration settings, see Creating a configuration record .

### Supported versions

This solution is supported in the following Relativity Server versions and RelativityOne.

Solution version Supported Relativity version

2.5.2.1 10.3.287.3 - Server 2024, RelativityOne

### Components

This solution consists of the following components:

- Event handler

- Custom object

- Relativity application

### Considerations

- This solution calculates and adds an incremental value to a field only when a user creates a record by clicking the Save , Save and Next , or Save and New button in a layout.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Deploying and configuring the solution

To add the solution to the Application Library:

- Navigate to the Application Library tab.

- Click Upload Application .

- Click Select File .

- Navigate to and select the application file included in the solution, then click Open .

- Click Save to upload the file to the Application Library.

If you currently have a previous version of this solution, any previous configurations are updated when you upgrade to a new version.

To add the solution to a workspace:

- In the Workspaces Installed section, click Select to install the application to one or more workspaces.

- Select the workspaces where you want to install the application, and then click the Move selected left to right icon.

- Click Apply .

The application is installed to the selected workspaces. A list of workspaces where the application has been installed displays in the Workspaces Installed section.

## Preparing the workspace

After you add the solution to the Application Library, you're ready to prepare a workspace to use the solution. Preparing a workspace consists of these basic tasks:

- Create a configuration record that specifies how to increment and format values and which field to add those values to.

- Associate the solution with the object type that contains the field you want to add values to.

### Creating a configuration record

After you install the solution in the workspace, the next step is to create a configuration record with settings that define how you want to increment and format values and which field you want to add those values to. The key settings are:

- Starting value - the numeric value used when calculating the value for the first record that a user creates after you start running the solution. This setting also defines an optional standard prefix for all values.

You can't change this value after the configuration record is created.

- Increment by - the numeric increment used when calculating values.

- Padding - the number of digits that you want to pad the second, numeric part of the value with.

The following table provides examples that demonstrate the logic that the solution uses to define the correct incremental value based on various scenarios and sample settings.

Scenario Highest existing value Starting value Increment by Padding Incremented value

The field doesn't contain any existing values for existing records. The solution settings specify a standard prefix ("MyID"), starting value, and padding value. None MyID000001 1 6 MyID000001

The field doesn't contain any existing values for existing records. The solution settings don't specify a standard prefix or starting value but do specify a padding value. None Not set 1 6 000001

To create a configuration record:

- Navigate to the workspace where you installed the solution.

- Click the Configuration tab.

- Click New Auto Increment Configuration .

- Complete the following fields:

- Name - enter a descriptive name for the configuration record.

- Field to populate - click the name of the fixed-length text or long text field that you want to calculate and add incremental values to.

Make a note of the object type for this field. You will use this later when associating the object type.

- Layout artifact Id(s) - type the Artifact ID of the layout to calculate and add incremental values to the field only when the field appears on a specific layout. To specify more than one layout, enter the Artifact ID of each appropriate layout, and separate each ID with a semi-colon (;). To calculate and add values to the field on all layouts, leave this field blank.

- Start value - (optional) type a starting value for the first value that the solution calculates. If you want to include a standard prefix for all the values that the solution calculates, type the prefix followed by the starting value. If you don't specify a value, then 0 is used as the starting value.

For example, you could set the start value to ABC01, the increment value to 2, and the padding to 5. The first RDO field would then be set to ABC00001, the second to ABC00003, and so on.

You can only set the Start value when you create the configuration. After setting this value and saving the configuration, you can't modify it or the Current value field.

- Increment by - enter the numeric increment that you want to use when calculating new values. For example, to increase each value by an increment of "10", type 10 in this field.

- Pad number to - (optional) type the number of digits that you want to pad each value with.

- Click Save .

### Associating the object type

The final step in preparing the workspace is to associate the event handler, which is included in the solution, with the object type that contains the field you want to add incremental values to.

To associate the event handler with the object type:

- In the workspace, navigate to the Object Type tab.

- Click the name of the object type that matches the Field to populate.

If you do not know the object type, return to the Configuration tab, then click on the configuration record you want to use. Click on the Field to populate to view its object type.

- Next to Event Handlers on Object Type , click New .

-

Select the KCD_1042103.AutoIncrement.EventHandlers.PostSave .dll file.

- Click Apply .

## Running the solution

After you complete all the steps for deploying and configuring the solution in a workspace, the solution automatically starts using the settings that you specified to calculate and add incremental values to the field. This occurs each time a user creates a new record by clicking the Save , Save and Next , or Save and New button in an appropriate layout. You don't need to take any additional steps to run the solution.

## Viewing the results

To view the results of running the solution, navigate to any view, layout, or other area containing the field that the solution calculates and adds values to automatically.

On this page

- Auto increment field on object

- Before you begin

- Supported versions

- Components

- Considerations

- Deploying and configuring the solution

- Preparing the workspace

- Creating a configuration record

- Associating the object type

- Running the solution

- Viewing the results


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


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
