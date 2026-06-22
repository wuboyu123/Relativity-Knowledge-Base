---
title: "Adding email settings"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Adding_email_settings.htm
collection: user
fetched_at: 2026-06-22T06:12:43+00:00
sha256: 23fac0159564b11b29897eda082476b98aea9f7eed6693aa372f1ca52d1686b8
---

Adding email settings Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Adding email settings

To complete the Legal Hold Settings, you need to add the email settings. The email settings provide the information so communications can be sent and received from your legal hold instance. When using the Graph API, you need to register your application in Microsoft Azure AD and set the permissions. For more information, see Using the Graph API for communications .

## Collecting required email settings information

If you are intending to use Relativity Legal Hold, you need to add the required credential information below. This information will then be used in the Adding email settings section.

Information label Description of required information Required information

User Name for SMTP The username for the account on the SMTP server used for sending emails. This can be an email address or domain\username depending on the server settings. Even if your SMTP server is configured for anonymous authentication, you must input a value. For example, anonymous .

Password for SMTP The password for the account on the SMTP server that Legal Hold uses for sending emails. Even if your SMTP server is configured for anonymous authentication, you must input a value. For example, anonymous .

Domain The SMTP domain address. For example, smtp.office365.com .

SMTP Port The SMTP port number.

Legal hold outgoing emails are designed to work with the SMTP protocol. This protocol runs on universally defined ports. We block most SMTP ports except 587. You must contact Relativity Support to open any other SMTP ports (25, 465, 587, 2525).

SSL (Y or N) The Secure Sockets Layer. Select Yes to use Secure Sockets Layer security for SMTP. You should consult with your IT department if you are unsure whether your SMTP server uses SSL.

From Email Address The display name and/or email address you want to appear when sending communications from Relativity Legal Hold. When a custodian receives a project communication, it will appear as if it was sent from the display name and/or address. For example, use the following verbiage - Display name <email@domain.com> .

Reply to Email Address The reply to email address. When a custodian clicks reply to a project communication, their reply is sent to this address. See the From Email Address example above.

Email Processor Type Email services can use one of several options to interact with third-party applications. Consult with your IT department if you are unsure which email processor type to use alongside your mail server. IMAP - Internet Message Access Protocol POP3 - Post Office Protocol 3

## Adding Outgoing Email settings

This section needs your SMTP information that you should have already collected before using Relativity Legal Hold. For more information, see Collecting required email settings information . The outgoing email settings must be entered on the Legal Hold Settings page prior to sending communications.

(Click to open)

To update the outgoing email settings on the Legal Hold Settings page, follow the steps below.

-

Click Edit .

-

Locate the Outgoing Email section.

-

Enter information in the fields. See Outgoing email fields for more information.

-

Update another section or click Save .

## Outgoing email fields

The outgoing email settings must be entered on the Legal Hold Settings page prior to sending communications. The fields you need to complete depend on the selected email processor type. See the fields below.

- Override Email Settings for Legal Hold

-

Select Yes to configure unique email settings you want Legal Hold to use. Legal Hold can have unique email settings compared to Relativity as a whole. The settings are User Name, Password, Domain, Port, Use SSL for SMTP.

-

Select No to use the existing server information.

- Email Processor Type —enter the type of email sent via Relativity Legal Hold—SMTP, or Graph API. When using the Graph API, you need to register your application in Microsoft Azure AD and set the permissions. For more information, see Using the Graph API for communications .

- Select SMTP and complete the following fields:

- View reasons to use your own SMTP .

-

Using your own SMTP for Legal Hold communications:

-

Legal Hold communications come from your trusted domain. An employee is more likely to interact with email from your domain.

-

Send communications from company's account. Using a different domain for the Send As results in emails getting flagged for spam.

- User Name —enter the user name for the account on the SMTP server used for sending emails. This can be an email address or domain\user name depending on the server settings. Even if your SMTP server is configured for anonymous authentication, you must input a value. For example, anonymous .

- Password —enter the password for the account on the SMTP server that Legal Hold uses for sending emails. Even if your SMTP server is configured for anonymous authentication, you must input a value. For example, anonymous .

- Domain —enter the SMTP domain address. For example, smtp.office365.com .

Enter smtp.office365.com when using Microsoft 365 for outgoing email.

- Port —enter the SMTP port number.

- Use SSL for SMTP

- Select Yes to use Secure Sockets Layer security for SMTP. You should consult with your IT department if you are unsure whether your SMTP server uses SSL.

Select Yes when using Microsoft 365 for outgoing email.

- Select No to disable SSL for SMTP.

- From Email Address —enter the display name or email address you want to appear when sending communications from Legal Hold.

When using the Graph API, the From Email Address will be the address associated to the account that was used to authenticate to Microsoft. When a custodian receives a project communication, it will appear as if it was sent from the account that authenticated to Microsoft.

-

- Reply to Email Address —enter the reply to email address. When a custodian clicks reply to a project communication, their reply is sent to this address. See the From Email Address example above.

- If Graph API is selected, complete the following fields. When using the Graph API, you must first register your application in Microsoft Azure AD and set the permissions. After registering your application, then you must click the Authenticate with Microsoft (Outgoing) button in the Settings console to authenticate your application ID and password with Microsoft. For more information, see Using the Graph API for communications .

-

Application Client ID —enter the Application Client ID created during registering the Legal Hold application in Microsoft 365.

-

Application Client Secret —enter the Application Client Secret created during registering the Legal Hold application in Microsoft 365.

-

Tenant ID/Domain —enter the Domain name of the Microsoft 365 tenant the collection is intended for.

- From Email Address —enter the display name or email address you want to appear when sending communications from Legal Hold.

When using the Graph API, the From Address will be the address associated to the account that was used to authenticate to Microsoft. When a custodian receives a project communication, it will appear as if it was sent from the account that authenticated to Microsoft.

- Reply to Email Address —enter the reply to email address. When a custodian clicks reply to a project communication, their reply is sent to this address. See the From Email Address example above.

### Testing the Outgoing Email settings

To test, follow the steps below.

-

To setup and test the email functionality you will need:

-

At least one Relativity Legal Hold Agent enabled.

-

The Legal Hold Security Admin Group assigned to Relativity User.

-

No Inbound blocking rules for emails on the clients network.

-

The correct credentials supplied by the client's IT department.

-

To confirm the settings, and that the client's network accepts incoming emails correctly, click the Test Outgoing Email Settings button.

If this button is not visible, the Relativity user is missing the Legal Hold Security Admin Group.

Once clicked the following message will be displayed, but it doesn't mean that the email has been successfully sent or received.

When successful, the following test email will be sent from the user account to the Reply to Email Address.

If the email isn't received within minutes, check that the Relativity Legal Hold Agent's completed processing it (Job Type SendTestEmail). If it has completed, then check the Relativity Errors and move onto the Troubleshooting section of this page.

## Adding Incoming Email settings

Update the fields in the Incoming Email section. The Incoming Email section is used to allow Legal Hold emails that are replied to by Custodians to be ingested into Legal Hold. If this functionality is not needed, it can be disabled by changing the Frequency to Check field to Select ...

To update the Incoming Email settings on the Legal Hold Settings page, follow the steps below:

-

Click Edit .

-

Click the Incoming Email tab.

-

Enter information in the fields. See Incoming email fields for more information.

-

Update another section or click Save .

Whatever mailbox is selected for the incoming mailbox setting should be only used for Relativity Legal Hold. The Legal Hold agent checks this mailbox for Legal Hold replies, imports any messages it finds, and then deletes all emails in the mailbox.

## Incoming email fields

The incoming email settings must be entered on the Legal Hold Settings page prior to receiving communications.

- Frequency to Check —select how often you want the Relativity Legal Hold agent checks the mailbox for custodian replies to communications in order to pull them into the system.

If Frequency is selected and the other fields are not populated with valid credentials, then the following error will be logged in the Errors tab (constantly if Immediate is select, every hour or once a day for the other values):

- Email Processor Type —select the email service you want to use to interact with third-party applications. Consult with your IT department if you are unsure which email processor type to use alongside your mail server.

- Select IMAP (Internet Message Access Protocol) or POP3 (Post Office Protocol 3) and complete the following fields:

- Mail Username —enter the mail username, specified by email address or domain\username depending on server settings, which will receive the custodian email replies.

- Application ID

- Mail Password —enter the password for the Mail Username address. This Mail Password field is case sensitive.

- Mail Domain —enter the fully qualified mail server name or IP address. For example, demo.testing.corp .

- Mail Port —enter the mail port number.

- Mailbox —enter the actual name of the folder containing the custodian replies to Legal Hold communications. For example, Inbox . This Mailbox field is case sensitive.

- Select Graph API and complete the following fields:

- Application Client ID —enter the Application Client ID created during registering the Legal Hold application in Microsoft 365.

-

Application Client Secret —enter the Application Client Secret created during registering the Legal Hold application in Microsoft 365.

-

Tenant ID/Domain —enter the Domain name of the Microsoft 365 tenant the collection is intended for.

- Mailbox (Optional)—enter the actual name of the folder containing the custodian replies to Legal Hold communications. For example, Inbox . This Mailbox field is case sensitive.

### Testing your Incoming Email settings

To test outgoing mail, follow the steps below.

To setup and test the email functionality you will need:

-

At least one Relativity Legal Hold Agent enabled.

-

The Legal Hold Security Admin Group assigned to Relativity User.

-

No Inbound blocking rules for emails on the clients network.

-

The correct credentials supplied by the client's IT department.

To confirm the settings, and that the client's network accepts incoming emails correctly, click the Test Outgoing Email Settings button in the Settings console.

If these buttons are not visible, you are not in the Legal Hold Security Admin Group.

Once clicked the following message will be displayed, but it doesn't mean that the email has been successfully sent or received.

When successful, the following test email will be sent from the user account to the Reply to Email Address.

If the email isn't received within minutes, check that the Relativity Legal Hold Agent's completed processing it (Job Type SendTestEmail). If it has completed, then check the Relativity Errors and move onto the Troubleshooting section of this page.

## Troubleshooting email settings

The following messages from Relativity Errors can indicate specific problems with the entered Outgoing email settings:

Error Cause Resolution

SendAsDeniedException

If the User Account does not allow for another email account to send on its behalf (i.e. the From Email address is not the same as the User Account) then the following message may be shown: "Could not connect to the email server with the provided credentials."

Resolve this issue by using a different email account or update the existing email's settings.

Incorrect User Name/Password

The remote name could not be resolved.

Resolve this issue by correcting the name and password in the Outgoing email settings.

Incorrect Domain

A connection attempt failed because the connected party did not properly respond or the connection failed because the connected host has failed to respond.

Resolve this issue by correcting the domain URL in the Outgoing email settings.

Incorrect Port

The email failed to send because the mail port number is incorrect.

Resolve this issue by correct the port number in the Outgoing email settings.

STARTLLS is required to send mail

The email failed to send because the SSL is set to No

Resolve this issue by setting the SSL field to Yes in the Outgoing settings.

On this page

- Adding email settings

- Collecting required email settings information

- Adding Outgoing Email settings

- Outgoing email fields

- Testing the Outgoing Email settings

- Adding Incoming Email settings

- Incoming email fields

- Testing your Incoming Email settings

- Troubleshooting email settings


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
