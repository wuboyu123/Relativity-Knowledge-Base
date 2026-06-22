---
title: "Notifications"
url: https://platform.relativity.com/Server2025/Content/BD_Notifications/Notifications.htm
collection: developer
fetched_at: 2026-06-22T06:26:49+00:00
sha256: c04d7ca5c59a353ae1c50eb61a013fbeb234b35ae48969b32d78922bb8078912
---

Notifications

# Notifications

These topics describe the public APIs of the Relativity Notifications application, used to send email or other notifications through Relativity.

## Current Notifications API content

#### .NET API

- Notifications (.NET)

#### REST services

- Notifications (REST)

## Using the Notifications Service

### Prerequisites

In order to call methods in this API:

- The authenticated user has to be part of a group within Relativity with the Send Email Notification admin permission enabled

-

Relativity's internal SMTP server must be properly configured. The SMTP configuration resides in Instance Settings, in the kCura.Notification section.

### Sender

A client of the service has the option to define what email address should be used as a sender. They can do so by providing an email address in the request object ( Sender property). If it is not provided, the service checks for an Instance Setting called EmailFrom . If the instance setting does not exist, the service defaults the Sender value to noreply@relativity.one.

### Sending Email Notifications

If there is more than one recipient requested, each email will be sent as a separate one. The service does not use CC or BCC fields.

Each email address (both sender's and recipient's) is validated based on Microsoft's System.Net.MailAddress class. Note that the address validation could be more forgiving than expected (e.g. address@domain is an acceptable email address according to MailAddress class).

Each email to be sent is processed separately. If sending one email fails (e.g. because of the spelling in recipient's address), others will still be processed. Emails are sent in parallel.

The service supports basic fail-and-retry mechanism. If the initial validation passed successfully (user has proper permission enabled, SMTP is running correctly and the request is not malformed) and sending an email failed for a reason like a network disruption or temporary SMTP issue, it will be retried several times with short interval in between.

In the response, the service returns an array of elements. Each element represents a single email and consists of information about the recipient, flag if an email was successfully sent and a message (if there was an error, more detailed information will be there).

The Notification service works in semi "fire and forget" style when it comes to sending actual emails. This is because there is no guarantee that if SMTP accepts the email and sends it, it will be delivered to the recipient. If you request to send an email to the recipient with wrong email format e.g. MyNickNameWithoutAtgmail.com, it will be immediately returned in a response that email was not sent due to the wrong format. But if you requested to deliver a mail to the recipient that has, for example a full mailbox, the Email Notification service will return in response that the email was sent, even though the recipient will not receive it.

## Troubleshooting

- HTTP 403 status code with PermissionDeniedException in JSON

It means you are trying to send an email notification as a user that is not in a group with Send Email Notifications enabled. Execute a request as a user with mentioned permission enabled.

- HTTP 500 code with ServiceException and a message "Email service is not running"

It means SMTP server is not correctly configured. Ensure that in Instance Settings proper values are set, especially SMTPServer, SMTPPort, SMTPUserName and SMTPPassword

- Even though I received HTTP 200 OK as a response, not all recipients received an email.

There may be several reasons for this behavior. First of all, check the response JSON object; there may be a typo an email address, or maybe an email address is in an unsupported format. If so, the response object should return details in the Message field of the given email status. If there is nothing in the response, perhaps the service successfully sent an email, but it was rejected by anti-spam software, firewall configuration or by the receiver's domain handler - in these cases, the service cannot notify the caller about it since the failure is asynchronous.

## Version History

v24000.2.0

##### Release Notes

- Initial version for Server 2024 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2024 Server 2025

v1.0.3

##### Release Notes

- Initial version for Server 2023 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2023 Server 2024
