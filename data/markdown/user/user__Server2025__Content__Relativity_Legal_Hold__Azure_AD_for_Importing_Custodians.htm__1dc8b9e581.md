---
title: "Integrating Azure AD for Importing Custodians"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Azure_AD_for_Importing_Custodians.htm
collection: user
fetched_at: 2026-06-22T06:12:38+00:00
sha256: 786b6becc96159024ae92c6e7e087f29f323b13c60b5d4d912b3ef6db490b98a
---

Integrating Azure AD for Importing Custodians Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Integrating Azure AD for Importing Custodians

To import custodians into Relativity, you also need the following applications to be installed in your workspace:

- Integration Points

- Integration Points AAD provider

- Relativity Legal Hold

- At least one Integration Points agent configured.

For more information, see Importing hold data to Relativity Legal Hold .

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Registering an Azure application and credentials

Integrating Azure AD for Importing Custodians requires a reference to a dedicated Azure application that has the appropriate permission. This needs to be done on the client side by an Azure user with sufficient rights.

Register the Relativity application to gain access to Microsoft Azure AD. Access to Azure AD gives Relativity the ability to complete multiple tasks.

Start registering your app by following the steps below:

The application registration process needs to be done by an Azure Administrator with sufficient privileges.

- Open your Azure Portal .

- In the left-navigation menu, click App registrations .

- Click New Registration .

This will open the Register an application page.

- Enter an application name in the Name field.

- Select Accounts in this organizational directory only as the supported account type.

- Click Register .

For more information on registering an application in Azure, see Microsoft's documentation or How to authenticate an EWS application by using OAuth ..

## Creating a client secret

A client secret from Microsoft Azure AD is needed to integrate Microsoft and Relativity.

To create a client secret:

-

In the left-navigation menu, click Certificates & secrets .

-

Navigate to the Client secrets tab.

-

Click the New Client Secret button.

Do not navigate away from the page once the client secret is created.

-

Populate the Description and Expires fields. You can leave the default, or recommended, values.

-

Click the Add button.

If the client secret was successfully created, you will see the Client Secret displayed on the table and the Value field should be displayed in plain text.

-

Copy the Value field and store it safely.

If you leave the page and comeback to get the value the Value field will be masked and you will not be able to copy it

You can repeat steps 4-5 to generate a new client secret.

## Adding permissions

The permissions of the Azure application you registered needs to be updated for the AAD provider.

To update the permissions:

-

In the left navigation menu, click the API permissions link.

-

Click Add a Permission .

-

In the side menu, select Microsoft Graph .

-

Select Application Permissions .

-

Add the following permissions:

-

Directory - Read.All

-

Group - Read.All

-

User - Read.All

-

Click Add permissions .

Clicking this button returns you to the API permissions page.

-

Click Grant Admin consent for Relativity .

-

In the confirmation window, click Yes .

## AAD Provider setup and run

For more information, see Importing from Microsoft Entra ID .

This part is not needed for the setup, but is recommended to ensure that the entities match the information that is in Azure Active Directory.

On this page

- Integrating Azure AD for Importing Custodians

- Registering an Azure application and credentials

- Creating a client secret

- Adding permissions

- AAD Provider setup and run


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
