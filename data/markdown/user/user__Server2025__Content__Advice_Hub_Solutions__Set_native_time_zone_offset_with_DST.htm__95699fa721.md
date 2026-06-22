---
title: "Set native time zone offset with DST"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Set_native_time_zone_offset_with_DST.htm
collection: user
fetched_at: 2026-06-22T06:09:46+00:00
sha256: a82b53be695e2003f4b1d566d7c1a091c8c63ecd0c2b43cdecc6dd7fbc7a6abb
---

Set native time zone offset with DST

# Set native timezone offset with Daylight Saving Time

- You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

- The Native Time Zone Offset field controls how the date and time header appears in the viewer for all email messages. It doesn't modify the actual metadata fields associated with these values. So you will have to re-convert documents if documents have been previously viewed. This field also controls the date and time displayed on redacted and annotated images. Therefore, it's important that you review and adjust the UTC accordingly to avoid incorrect time designations on documents you intend to produce, as this could lead to inaccurate productions.

This solution takes a configurable date field value and time zone and updates each newly loaded document’s Relativity Native Time Zone Offset field to account for daylight savings time. The solution also sets the single object Time Zone field on the document object to be used for Imaging Profiles.

## Before you begin

### Compatibility matrix

Click on the latest version of the application that works with your Relativity instance to download the application from the Relativity Community:

After upgrading your Relativity instance, upgrade the Native Time Zone Offset application to the latest version of the application. The application will not work unless you are on the most recent version of the application that works with your instance.

Solution version Supported Relativity version

7.0.3

Server 2022, Server 2023, Server 2024

### Components

This solution consists of the following components:

- Relativity script that runs at the environment level

- Relativity script that runs at the workspace level

- Custom objects

- Custom agent

- Relativity application

- Event handler

### Considerations

The solution supports the following functionality:

- These scripts should only be run by a system admin. If you are not a system admin, we recommend you do not run these scripts.

- Native time zones with the same name should not be set up in a workspace. For example, a workspace with the following time zones will throw an error in the ‘View Status’ script even though they have different pre-pended values:

- (UTC) Pacific Time Zone

- (GTC) Pacific Time Zone

- Only one agent can be set up per Relativity instance.

- Only workspaces where the application is successfully installed will be processed.

- Only workspaces which have an enabled configuration will be successfully processed.

-

If the application is installed into a workspace but there are no enabled configurations, that workspace will be processed with an error.

- Only documents where the selected Date field is set will be updated.

- Only documents where the selected time zone field is not set will be updated.

- Only documents created after the installation of the Relativity Application will be updated.

- There is an optional script which can be used to process the documents created before the application was installed.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Deploying and configuring the solution

These instructions require that you have already configured the Relativity Services API on your agent server. To verify that Relativity Services API is configured correctly, contact Support .

Complete the following steps only for the initial setup.

To deploy and configure the solution, perform the steps included in the following sections.

### Adding the Relativity script

Complete the following steps to add the Relativity script to the Relativity Script Library:

- Log into Relativity.

- Click Home .

- Click on the Relativity Script Library tab.

- Click on the New Relativity Script button.

- Clear out the contents from the Script Body .

- Copy and paste the contents from the file Native Time Zone Offset with DST - View Status.krs into the Script Body .

- Click Save .

### Adding the Relativity application

Complete the following steps to add the Relativity application to the Application Library:

- Click the user drop-down menu in the upper-right corner of Relativity.

- Click Home .

- Click the Applications & Scripts > Application Library tabs.

- Click Upload Application .

- In the Application File field, click Choose File .

- Select the RA_Native_Time_Zone_Offset_with_DST.rap file included in the solution. Click Open .

- Click Save .

### Setting up the Time Zone Agent Errors Relativity group

This step allows you to define the Relativity group that will receive an email when there is an error while running this solution. For example, if no Time Zone configurations are available or when all available configurations are disabled.

Complete the following steps to set up a Relativity group:

- Log in to Relativity.

- Click Home .

- Click the Groups tab.

- If it doesn't exist, add a new group named Time Zone Agent Errors :

- Click New Group.

- Enter Time Zone Agent Errors as the group name. You must enter the group name exactly listed here.

- Click Save .

- In the Users section, click Add .

- Add at least one user to the group.

- If any agent or workspace-level errors occur, all users in this group will receive an email with the error details when the agent completes a run.

## Preparing the workspace

After deploying the solution, you can install it in one or more workspaces.

Complete the following steps to install the solution:

- Click the user drop-down menu in the upper-right corner of Relativity.

- Click Home .

- Click the Applications & Scripts > Application Library tabs.

- Click the name of the Native Time Zone Offset with DST application.

- In the Workspaces Installed section, click Install .

- In the to Workspaces field, click .

- Select the checkbox for the workspace where you want to install the solution. Select multiple checkboxes to install the solution in more than one workspace.

- Click OK .

- Click Save .

## Setting up the custom agent

Complete the following steps to set up the custom agent:

- Log in to Relativity.

- Click Home .

- Click the Agents tab.

- Click New Agent .

- Next to Agent Type, click

- Select the agent Native Time Zone Offset with DST - KCD_1035967 .

- Click OK .

- In the Agent Server section, click

- Select the agent server where you want the agent to run, and click OK .

- Set the Run Interval to the desired interval. We recommend having this agent run on an hourly or daily basis.

- Set the Logging level to the desired logging level.

- Set Enabled to Yes .

- Click Save .

You should see an agent in the Agents tab called Native Time Zone Offset with DST - KCD_1035967.

Only one agent can be installed per Relativity instance.

## Running the solution

After updating the workspace, you can configure and run the solution.

Complete the following steps to run the solution:

- Navigate to the workspace where you installed the Relativity application.

- Click the Configuration tab.

- Click New Configuration and complete the following fields:

- Name - Provide a name for the configuration.

- Time Zone - Select the desired time zone.

- Date Field - Select the Date field.

- Native Imaging Time Zone Field - Select the field that stores the time zone for imaging profiles.

Native Imaging Time Zone Field will only affect the imaging of RSMF, EML, and MSG files.

- Enabled - Select Yes or No . You can create multiple configuration records. However, you can have only one enabled configuration in each workspace.

- Click Save .

### Viewing workspaces and their statuses

Workspaces are processed in the order they are created.

Complete the following steps to view all workspaces and their statuses:

- Click the user drop-down menu in the upper-right corner of Relativity.

- Click Home .

- Click the Applications & Script > Relativity Script Library tabs.

- Click the Native Time Zone Offset with DST - View Status script.

- Click Run Script .

- Click Run .

## Viewing the results

When the agent runs, it retrieves all workspaces where the Native Time Zone Offset with DST application is installed. It process each workspace with an enabled configuration record. The solution processes workspaces with an earlier creation dates first.

When the agent runs for the first time, it retrieves all documents created since the application was installed. During subsequent runs, the agent retrieves all documents created since it last ran successfully. You can view the agent last run date for each workspace by executing the script or by completing these steps:

- Navigate to the workspace.

- Click the Configuration tab.

- Click the Status button.

The following illustration displays an example of a workspace status record:

The status record includes the following information:

- Status - the status of the workspace.

- Last Checked - the last processed date for the workspace.

- Messages - a description of the agent’s last run. Any errors that occurred display here.

Once the agent finishes processing the workspaces, if any errors were detected, it sends an email to each user included in the Time Zone Agent Errors group. The following screen shot provides a sample email:

### Viewing the returned output

The script was configured with the following values:

- Name - Eastern

- Time Zone - Eastern Standard Time

- Date Field - Date Last Modified

- Native Imaging Time Zone Field - Time Zone Field

Native Imaging Time Zone Field will only affect the imaging of RSMF, EML, and MSG files.

- Enabled - Yes

The following illustration displays an example of the results generated by the agent:

- The document with the control number of EN000006 is set to a Relativity Native Time Zone Offset of -4.00, since Eastern Standard Time has an offset of -5.00, but the Sent Date of 6/5/2001 12:00 AM falls in daylight savings time.

- The document with the control number of EN000009 is set to a Relativity Native Time Zone Offset of -5.00, since Eastern Standard Time has an offset of -5.00, and the Sent Date of 11/23/2001 12:00 AM does not fall within daylight savings time.

### Optionally resetting the last checked date

By default, the agent only processes documents created in Relativity after the application was installed in the workspace. To process all documents in the workspace, reset the last checked date. You can use any date before the documents were loaded in the workspace.

Complete the following steps to reset the date:

- Navigate to the Scripts tab in the workspace.

- Run the Reset Last Checked Date for Native Time Zone Offset script.

After the script executes, it updates the LastCheckedUTC field. It adds a date that occurred before the first document was loaded to the workspace. This update prompts the agent to process any documents loaded before the application was installed.

### Table of time zones

For information about international time zones and Greenwich Mean Time (GMT), see http://www.greenwichmeantime.com/ .

### Support

For additional assistance, contact Support .

### Disclaimer

This script is intended for use only in the Relativity versions specified in this document and run under the guidelines presented. While each solution is carefully built and thoroughly tested to work on the versions of Relativity specified in this document, this script is not a core feature of Relativity and is not eligible for the same level of support as the Relativity platform.

In addition, custom components may not exhibit the same performance and behavior as native Relativity features. Custom solutions do not specify permission settings unless explicitly requested by the client.
