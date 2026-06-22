---
title: "Notifications (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Notifications/Notifications__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:26:51+00:00
sha256: cc45c6fe78d15536eb8c45b1bd992852cf148108cf6933ed58f583c7e104bd56
---

Notifications (.NET)

# Notifications (.NET)

The Relativity.Notifications API is used to send email notifications through Relativity. The service uses internal Relativity's SMTP client , which is configured in Instance Settings.

Review the topic Using the Notifications Service for important considerations on interacting with the service.

## Code Samples

To call the service, you will need to pass in a EmailNotificationRequest DTO object with the details of the notification to send.

Copy

EmailNotificationRequest object

```text
1
2
3
4
5
6
7
8
public class EmailNotificationRequest

{

    public string Sender { get; set; }

    public List<string> Recipients { get; set; }

    public string Subject { get; set; }

    public string Body { get; set; }

    public bool IsBodyHtml { get; set; }

}
```

Calling the service

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
using Relativity.Notifications.V1; // requires Relativity.Notifications.SDK nuget package

using Relativity.Notifications.V1.Models; // requires Relativity.Notifications.SDK nuget package

async SendEmailAsync(EmailNotificationRequest request)

{

    using (IEmailNotificationsManager notificationService = new ServiceFactory(settings).CreateProxy<IEmailNotificationsManager>())

    {

        return await notificationService.SendEmailNotificationAsync(request).ConfigureAwait(false);

    }

}

// Note that you might need to cast the following:

// Type of EmailNotificationRequest.Recipients is List<string>

// Type of EmailNotificationResponse.EmailNotifications is List<EmailNotificationStatus>
```

The service returns a EmailNotificationResponse object. The response consists of a list of EmailNotificationStatus objects, each representing a single email request. The IsSent property informs if an email was sent successfully or not. If not, detailed information will be provided in the Message property

Copy

EmailNotificationResponse

```text
public class EmailNotificationResponse

{

    public List<EmailNotificationStatus> EmailNotifications { get; set; }

}

public class EmailNotificationStatus

{

    public string Recipient { get; set; }

    public bool IsSent { get; set; }

    public string Message { get; set; }

}
```
