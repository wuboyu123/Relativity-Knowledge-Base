---
title: "Reminders"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Reminders.htm
collection: user
fetched_at: 2026-06-22T06:13:24+00:00
sha256: 0b9ff28b73b30f87a24ff2c13f2ecb1a2bce1422721d017ab6c74544fe585f99
---

Reminders

# Legal hold reminders

Use Legal Hold reminders to alert entities within all of Relativity or within a specific Legal Hold project that there are tasks for them to complete.

Acknowledgment is required for global reminders and project reminders.

## Reminder types

Use the Relativity Legal Hold reminder functionality to automatically or manually send periodic reminders to entities within all of Relativity or within a specific Legal Hold. While the workflow for the two different reminders are similar there are differences.

### Project reminders

Use the Project Reminder functionality to manually or automatically send periodic reminders to all active, on-hold entities within in the selected legal hold project. This is accessed from the Project Details page or from the Project Reminder tab. In the Projects Console, click the Send Project Reminder button. See Project console for more information.

Project reminders can be sent without requiring acknowledgement.

Only one project reminder per legal hold project.

### Global reminders

Use the Global Reminder functionality to automatically send periodic reminders to all active, on-hold entities to review their hold obligations.

## Enabling reminders

Begin to enable a reminder, whether project or global level, by navigating to the proper reminder page. To enable a global reminder, navigate from the Global Reminder tab. To enable a project reminder, navigate to a Project Details page for a specific project. See Project Details for more information. Once the reminders are scheduled and sent, the entities will receive their emails after they are sent.

### Scheduling a Global Reminder

You can also manually send a one-time Global Reminder. See Global Reminder console .

- Navigate to the Global Reminder tab.

- Select the Global Reminder you wish to update.

- Click Edit .

- On the Enable Reccuring Global Reminder field, select the Yes radio button.

- Click to open the Schedule Email Job modal.

- Enter information in the Scheduling and Email layout fields. See Schedule Email Job and Email layout fields .

- Click Save . The Global Reminder is now scheduled to run.

### Scheduling a Project Reminder

You can also manually send a one-time Project Reminder. See Global Reminder console .

- From the Projects page, click the New Project Reminder button.

- On the Enable Reccurring Project Reminder field, select the Yes radio button.

- Click to open the Schedule Email Job modal.

- Enter information in the Scheduling and Email layout fields. See Schedule Email Job and Email layout fields .

- Click Save .

The Project Reminder is now scheduled to run.

### Schedule Email Job and Email layout fields

The Schedule Email Job and Email layout contains the following fields:

The following example displays the Daily frequency. See the Frequency description below for Weekly and Monthly information.

Scheduling

- Enable Reccuring Global Reminder

- Select Yes to enable the scheduling functionality for the global reminder. See Disabling reminders .

- Select No to disable the scheduling functionality for the global reminder.

Frequency - the interval at which Legal Hold sends the reminder.

- Daily - select this option for Legal Hold to send the reminder once every day.

- Weekly - select the day(s) that you want Legal Hold to send the reminder once every week.

- Reoccur - enter the number of week(s) in which Legal Hold sends the reminder.

- Monthly - select the day of the month that you want Legal Hold to send the reminder once every month.

- Reoccur - enter the number of month(s) in which Legal Hold recurrently syncs.

- Send On

- Day _ the month - select the day of the month that you want Legal Hold to send the reminder.

- The _ Day of the Month - select this option for Legal Hold to send the reminder on the chosen day of every month.

- Quarterly - select the quarter of the year that you want Legal Hold to send the reminder.

- Send On

- Day _ the month - select the day of the month that you want Legal Hold to send the reminder.

- The _ Day of the Week - select this option for Legal Hold to send the reminder on the chosen day of every month.

- Yearly - select the day of the year that you want Legal Hold to send the reminder once every year.

- Send On

- Day _ the month - select the day of the month that you want Legal Hold to send the reminder.

- The _ Day of the Week - select this option for Legal Hold to send the reminder on the chosen day of every month.

- Start Date - the date that you want Legal Hold to start sending the scheduled reminder.

For months with less than 30 days, Legal Hold will send the reminder on the last day of the month.

- End Date - (Optional) the date that you want Legal Hold to stop sending the scheduled reminder. Only set an end date if you want to schedule a reminder to send during a known time period.

- Scheduled Time - the time at which Legal Hold sends the reminder. This time is local to your PC, not to the server.

Email

- Send As - the email address you want to appear when sending a global reminder from Legal Hold. Using this feature, you can send a communication on someone else's behalf. For example, a junior attorney may send the email, but may want the email to appear as coming from the general counsel. If you leave this field blank, Legal Hold uses the default email in the Legal Hold Settings tab.

- Subject - the subject that appears in the email.

- Body - the message that appears in the email. Use the [PortalLink] email merge field to insert a link to the portal, or use the [Entities.Projects] email merge field to list all active projects in the email. See Using the editor window .

Merge fields from other communications can't be used in reminders. For example, merge fields from a Hold Notice can't be used in a Global Reminder.

Status

Last Run Time (UTC) - the time stamp for the last scheduled Global Reminder.

## Reminder consoles

### Global Reminder console

The Global Reminder console contains the following options:

- Send Global Reminder Now - immediately sends the Global Reminder to all active entities.

- Send Test Email - send a test email to a specified email address(es). Separate addresses with a comma.

### Project Reminder console

On the Project Reminder page, after saving your reminder, use the Project Reminder console to send the reminders to all active, on-hold entities in the project to review their hold obligations on a specific project.

The Project Reminder console contains the following options:

- Send Project Reminder Now - immediately sends the Project Reminder to all active entities.

- Send Test Email - send a test email to a specified email address(es). Separate addresses with a comma.

If the button is shaded gray, the action is unavailable or may not appear at all, depending on your permissions. See Securing a project .

## Disabling reminders

No matter which reminder you are disabling, the majority of the process is the same. The only difference between disabling a global reminder and a project reminder is the location. To disable a global reminder, navigate to the Global Reminder tab and select the global reminder you wish to update. To disable a project reminder, navigate to the Project Reminder tab.

In the reminder list:

- Locate the reminder you wish to update.

- Click Edit .

- On the Enable Recurring Reminder field, select No .

- Click Save .

The reminder is now disabled.
