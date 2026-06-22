---
title: "Notifications (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Notifications/Notifications__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:26:54+00:00
sha256: 6a93c6db55e5c1a5465f7c28b1e28cadab82fb9372be1abb164ca819d03dc5f2
---

Notifications (REST)

# Notifications (REST)

The Notifications Service is used to send email notifications through Relativity. The service uses internal Relativity's SMTP client , which is configured in Instance Settings. Review the topic Using the Notifications Service for important considerations on interacting with the service.

This service resides at the following URL:

Copy

```text
<host>/Relativity.REST/api/relativity-notifications/v1/workspaces/-1/notifications/email
```

## Code Samples

To send a notification, issue a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-notifications/v1/workspaces/-1/notifications/email
```

Copy Sample JSON Request Body (note invalid email in recipients)

```text
{

    "request": {

        "recipients":["name.surname@relativity.com", "namesurnamegmail.com"],

        "subject": "Email Notification Test",

        "body": "Body of the email."

    }

}
```

Copy Sample JSON Response

```text
{

    "EmailNotifications": [

        {

            "Recipient": "name.surname@relativity.com",

            "IsSent": true,

            "Message": "Email has been sent."

        },

        {

            "Recipient": "namesurnamegmail.com",

            "IsSent": false,

            "Message": "Recipient's or sender's email format is invalid.\" FormatException: The specified string is not in the form required for an e-mail address."

        }

    ]

}
```
