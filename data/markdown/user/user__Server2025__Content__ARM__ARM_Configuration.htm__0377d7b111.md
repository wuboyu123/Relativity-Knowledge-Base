---
title: "ARM Configuration"
url: https://help.relativity.com/Server2025/Content/ARM/ARM_Configuration.htm
collection: user
fetched_at: 2026-06-22T06:17:03+00:00
sha256: d925d212cdf4cf6f3356ae7d20bb3167e5338a9bbe8c8470c27df2904a9906e2
---

ARM Configuration

# ARM Configuration

- From the ARM tab, select the Configuration subtab to display the Configuration Settings page.

- Click Edit to modify these settings.

### ARM Archive Locations

Click Add to add a new archive location.

You can configure one or many archive locations for use in creating Archive and Restore jobs. These archive locations are configured as UNC paths and must be fully read- and write-accessible by the ARM agents. Each path can be used to store an archive when you create an Archive job. Archives that are stored in these locations will automatically be made available for selection when you create a Restore job. To restore an archive to a Relativity environment different from the archive source, the archive path must be configured on the target environment before it is available for selection in the Restore job.

It is highly recommended the ARM share be located at the root level of any drive on the server. You can allow multiple ARM shares, but it is highly recommended they all be located on the root of the drive. For example: \\SERVERNAME\ARMShare\ .

### Email Notification Settings

You can add event-level notifications for one or multiple users. You can configure each email address individually to receive an email notification when an Archive, Restore, or Move job is started, paused, or canceled, or when a job completes successfully or fails in error.

To create a new email notification setting:

- In the Email field, enter the email address of the person who should receive the notification(s).

- Select the checkboxes for the appropriate actions:

- Started —an email will be sent when the job starts.

- Paused —an email will be sent when the job is paused by a user.

- Cancelled —an email will be sent when the job is canceled by a user.

- Errored —an email will be sent when the job encounters an error from which it can’t recover.

- Succeeded —an email will be sent when the job completes successfully.

- Click Add . The settings you’ve specified appear in the Email Configurations section.
