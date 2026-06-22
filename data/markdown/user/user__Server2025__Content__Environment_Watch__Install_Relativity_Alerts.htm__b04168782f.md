---
title: "Install Relativity Alerts"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Install_Relativity_Alerts.htm
collection: user
fetched_at: 2026-06-22T06:11:29+00:00
sha256: 62c7b280216775842c7e95b431918f45ccd97432449c0f9088e982877868f97d
---

Install Relativity Alerts Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Install Relativity Alerts

This step is required for Environment Watch.

## Summary

The Relativity Alerts application is a new application as part of the Relativity Environment Watch suite. Its main functionality is to alert Relativity System Administrators to a variety of Environmental and Application related issues on a Relativity instance within Relativity web interface. It replaces a previous "Legacy Alerts" functionality with a new Open Telemetry based implementation with Elastic Stack backend. It allows in real time to notify Relativity System Administrators about issues, redirect them to easily readable dashboards with performance and health information, as well as accompanied by a comprehensive resolution guidelines.

## Permissions

- To install the application, access it, and receive alerts, the user must be part of the Relativity System Administrators Group.

- To access Kibana dashboards and saved searches a new account must be created for each user and be assigned to the custom Kibana role which is installed during the Environment Watch CLI setup. See Create Kibana Users for Dashboard Access for more information.

## Installation

To install the Relativity Alerts application on your Relativity instance:

-

Log in to Relativity as a System Administrator.

-

Navigate to the Application Library tab.

-

Click Upload Application

-

Click Select File .

-

The Environment Watch bundle contains a RAPs folder with subfolders organized by Relativity Server version. Each subfolder Server202X contains the corresponding Relativity Alerts RAP file for that Relativity Server version.

Navigate to the subfolder that matches your Relativity Server version, select the Relativity Alerts RAP file, and then click Open .

-

Click Save to upload the file to the Application Library.

A list of common install issues and their resolutions are available at the troubleshooting guide .

## Verification

-

Navigate to the Alerts tab, you should see all alerts available in Kibana.

-

Navigate to Logs & Dashboards tab, you should see all Environment Watch dashboards and saved searches available in Kibana.

-

When on Logs & Dashboards tab, find **Alerts Overview88 dashboard and click the link. A new web browser tab will be created and you should be redirected to "Alerts Overview" dashboard in Kibana. If you have not logged in into Kibana yet, you will be prompted with a Kibana login page. Please login with your Kibana user account with privileges.

-

To confirm that the alerting functionality is operational, please do the following:

-

Go to the Agents tab

-

Select File Deletion Manager agent and disable it.

-

Within the next 30-60 seconds, the bell icon, in the top-right corner, will indicate that there is a new Alert.

-

Click on the bell icon, and you should be able to see the active One or more agents are disabled alert in the alert flyout.

-

Click on the question mark icon next to the One or more agents are disabled alert, and you will be redirected to the resolution guidance for this alert in a new tab of your web browser.

-

Return to the previous tab in Relativity, then click on the bell icon in the top-right corner. When the alert flyout opens, click on the 'One or more agents are disabled' alert, and you will be redirected to a filtered list of disabled agents in the Agents tab within Relativity.

-

While on Agents tab, please remember to enable the File Deletion Manager agent.

If any of the previous steps have failed, or any errors were displayed, please see troubleshooting guide for more information.

## Create Kibana Users and Assign Roles

To access Kibana dashboards and saved searches, a new account must be created for each user and be assigned to the custom Kibana role that was installed during the Environment Watch CLI setup.

### Creating Kibana Users with Dashboard Access

To create a Kibana user and assign the custom Kibana role:

- Log in to Kibana as a user with administrative privileges.

- Navigate to Stack Management > Security > Users .

- Click Create user .

- Fill out the following:

- Username : A unique login name (e.g., alerts_dashboard_user ).

- Password : Set a strong password.

- Full name / Email address : Optional but recommended.

- Under Roles , search for and assign the relativity_dashboard_user role. Optionally, also assign the monitoring_user to enable access to Stack Monitoring.

- Click Create user to save.

Users must log in with this account to access the Kibana dashboards and saved searches provided by Environment Watch.

### Congratulations!

You have reached the end of the setup process. If you are still running into any issues, please refer to the Troubleshooting Guides for further assistance.

## Next Step

Click here for the next step

On this page

- Install Relativity Alerts

- Summary

- Permissions

- Installation

- Verification

- Create Kibana Users and Assign Roles

- Creating Kibana Users with Dashboard Access

- Congratulations!

- Next Step


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
