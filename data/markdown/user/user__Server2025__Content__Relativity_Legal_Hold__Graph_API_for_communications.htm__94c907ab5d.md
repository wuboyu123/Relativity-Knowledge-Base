---
title: "Using the Graph API for communications"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Graph_API_for_communications.htm
collection: user
fetched_at: 2026-06-22T06:12:39+00:00
sha256: 68855e2a3b8f102cdd2251638d03869bead28fce66c143cbf4f66ee0635db074
---

Using the Graph API for communications

# Using the Graph API for communications

To use the Graph API for legal hold communications, you need to register the Relativity Legal Hold application in Azure AD and set your processor type to Graph API in Relativity. For more information on setting your processor type, see Adding email settings .

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Registering an Azure application and credentials

To us the Microsoft Graph API, you need to register the Relativity Legal Hold application. Authentication requires a reference to a dedicate Azure application that has the appropriate permission. This needs to be done on the client side by an Azure user with sufficient rights.

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

## Adding permissions to the registered application

Next, from the app's page, add permissions to the web API by following the steps below:

- Click API Permissions .

- Click Add a permission .

- Click Microsoft Graph .

- Select Delegated Permissions .

- Select the following options from the Delegated Permissions section:

-

Mail – Mail.Send , Mail.ReadWrite

- User – User.Read

-

Click Add Permission .

-

Click Grant Permission .

## Configuring the redirect URL

In Azure Portal, navigate to the Overview page for the application being used for the integration. Follow the steps below.

-

Using the left navigation column, click into the Authentication page.

-

Click the Add a platform button.

-

Click the Web drop-down text.

-

Paste in your Redirect URL .

Replace the bold part of the URL with your organization's subdomain, domain, and top-level domain.

- Format : https:// {RelativityURL}/ Relativity.Rest/API/kCura.LegalHold.Services.ILegalHoldModule/Graph%20Authorization%20Manager/graph-auth-response

- Example : https://yourorganization.relativity.one/Relativity.Rest/API/kCura.LegalHold.Services.ILegalHoldModule/Graph%20Authorization%20Manager/graph-auth-response

-

Click the Configure button.

For more information on adding a redirect URL to Azure, see Microsoft’s documentation .

## Creating a client secret

A client secret from Microsoft Azure AD is needed to integrate Microsoft and Relativity. To create a client secret, follow the steps below.

-

In the left-navigation menu, click Certificates & secrets .

-

Navigate to the Client secrets tab.

-

Click the New Client Secret button.

Don't navigate away from the page once the client secret is created.

-

Populate the Description and Expires fields. You can leave the default, or recommended, values.

-

Click the Add button.

If the client secret was successfully created, you will see the Client Secret displayed on the table and the Value field should be displayed in plain text.

-

Copy the Value field and store it safely.

If you leave the page and comeback to get the value the Value field will be masked and you will not be able to copy it

You can repeat steps 4-5 to generate a new client secret.

After you complete registering your app and have your client secret, you need to add this information to your email settings. For more information, see Adding email settings .
