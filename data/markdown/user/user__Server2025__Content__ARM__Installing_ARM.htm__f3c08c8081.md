---
title: "Installing ARM"
url: https://help.relativity.com/Server2025/Content/ARM/Installing_ARM.htm
collection: user
fetched_at: 2026-06-22T06:17:01+00:00
sha256: 15ad7a8081cae8653506b6831b3aa65ab5bac715df819261615e629a887e48cb
---

Installing ARM Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Installing ARM

- You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

## Download ARM

The ARM application is included in the Relativity installation package available on Community site.

## Install ARM

ARM should be installed only in the Admin Case (on Instance Level). It should NOT be installed in the workspaces.

Perform the following steps to install the ARM application:

- Navigate to the Application Library .

- Click Upload Application .

- Under the Application Information section, select the Choose File button.

- From the dialog, select the ARM application, then click Open .

- Click Save .

Once the application has imported, you will see a new ARM admin tab in the instance.

## Add ARM agent

The ARM agent is responsible for performing the work for each type of function in an ARM job. Only one ARM agent is required; however, it’s a good idea to install more than one, if you are planning on running multiple ARM jobs in parallel. An optimal setup typically consists of no more than 6 ARM agents per agent server, and no more than 24 agents in an environment, when running multiple jobs.

Perform the following steps to install these agents:

- From the Home menu, navigate to the Agents tab, and then click New Agent .

- Click Browse next to Agent Type, and then click the ARM agent radio button.

- Click OK .

- Leave all other settings at their default values, and then click Save .

## Relativity service account

The Relativity service account must be enabled with an integrated authentication provider correctly setup for ARM to login to the WebAPIPath and run ARM jobs.

- First, you must create an authentication provider with the Provider Type set to Integrated Authentication, if one does not already exist.

- When adding the login method to the Relativity Service Account user, select the integrated authentication provider and set the Windows account to the Relativity service account user's Windows username. For example, domain\username or .\username.

## Update BcpShareFolderName instance setting

ARM will automatically retrieve the SQL Server machine name upon install. If your SQL Servers are in a clustered setup, you must update the BcpShareFolderName instance setting.

To do this manually, use the following to directly change the SQL code:

Update [EDDS].[eddsdbo].[InstanceSetting]

Set Value = '\\SQLName\BCPPath'

where name = 'BcpShareFolderName' and section = 'kCura.ARM'

This value can be changed to accommodate larger cases if location does not have enough storage space for the workspace(s) to use as a temporary location.

## Upgrade ARM

Perform the following steps to upgrade the ARM application:

- Do not upgrade while jobs are running, errored, or created. The ARM queue should be clear before upgrading or those jobs will be nonrecoverable.

- You must have valid Relativity Community credentials in order to download any Community file linked to from the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

- ARM is available for download through the Relativity Community or contact Support to request the newest version of ARM that is compatible with your version of Relativity.

- Navigate to the Application Library .

- Click on the currently installed version of ARM. The Application page appears.

- Click Edit .

- Click Clear in the Application File field. The original file is cleared.

- Click Choose File in the Application File field.

- From the dialog, select the newest version of ARM, then click Open .

- Click Save .

On this page

- Installing ARM

- Download ARM

- Install ARM

- Add ARM agent

- Relativity service account

- Update BcpShareFolderName instance setting

- Upgrade ARM


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
