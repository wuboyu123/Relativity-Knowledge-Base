---
title: "Legal Hold SMTP information"
url: https://help.relativity.com/Server2025/Content/Recipes/Legal_Hold/Legal_Hold_SMTP_information.htm
collection: user
fetched_at: 2026-06-22T06:17:28+00:00
sha256: 8de6531f5e48d024bf89a7378bd0bb4a199066765d7339ca50a97a0b47dd2ff2
---

Legal Hold SMTP information

# Legal Hold SMTP information

When working in Relativity Legal Hold, there is a need for adding a SMTP login.

## What is Relativity Legal Hold?

Relativity Legal Hold is a tracking software that allows information governance by tracking users and their content. Hold notices can be sent to people notifying them of impending or active litigation and the need to retain data. The acknowledgement of this notification allows them to verify the company complying with the litigation request. There is also the ability to preserve and in some versions collect data from Microsoft Office 365 clients.

## Requirements for Relativity Legal Hold

If you are intending to use Relativity Legal Hold, you need to add the required credential information below.

Information label Description of required information Required information

User Name for SMTP The username for the account on the SMTP server used for sending emails. This can be an email address or domain\username depending on the server settings. Even if your SMTP server is configured for anonymous authentication, you must input a value. For example, “anonymous".

Password for SMTP The password for the account on the SMTP server that Legal Hold uses for sending emails. Even if your SMTP server is configured for anonymous authentication, you must input a value. For example, "anonymous".

Domain The SMTP domain address. For example, “smtp.office365.com”

SMTP Port The SMTP port number. NOTE: Legal hold outgoing emails are designed to work with SMTP and EWS protocol, these protocols run on universally defined ports. SMTP ports (25, 465, 587, 2525)and EWS ports (443) but RelativityOne being security conscious blocks most of these ports except 587 and 443. So if a client wants to use other ports then they must request Relativity to open that port on their RelativityOne instance.

SSL (Y or N) The Secure Sockets Layer. Select Yes to use Secure Sockets Layer security for SMTP. You should consult with your IT department if you are unsure whether your SMTP server uses SSL.

From Email Address The display name and/or email address you want to appear when sending communications from Relativity Legal Hold. When a custodian receives a project communication, it will appear as if it was sent from the display name and/or address. For example, use the following verbiage "Display name <email@domain.com>".

Reply to Email Address The reply to email address. When a custodian clicks reply to a project communication, their reply is sent to this address. See the From Email Address example above.

Email Processor Type Email services can use one of several options to interact with third-party applications. Consult with your IT department if you are unsure which email processor type to use alongside your mail server. EWS - Exchange Web Services IMAP - Internet Message Access Protocol POP3 - Post Office Protocol 3

Field Field description

Name Enter in the name to identify the data source.

Domain Name Enter the Microsoft Office 365 Tenant Domain.

Domain Name URL This URL is the connection to Microsoft Office 365 Protection Services utilized by Relativity Legal Hold (read only).

Account User

Enter in the username of the account used to access Office 365. This account must be assigned the eDiscovery Manager role in Office 365, which is required to create and remove preservation holds.

Account Password Enter in the password for the account user.

Resolve SharePoint Site Permissions

Select Yes or No to temporarily grant the required permissions to the Account User in order to obtain the list of custodians that have access to a given site during the target discovery process.
