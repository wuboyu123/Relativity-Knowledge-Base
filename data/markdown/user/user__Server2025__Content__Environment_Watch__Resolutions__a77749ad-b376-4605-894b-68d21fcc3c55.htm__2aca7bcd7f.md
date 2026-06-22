---
title: "Relativity license will expire soon"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/a77749ad-b376-4605-894b-68d21fcc3c55.htm
collection: user
fetched_at: 2026-06-22T06:18:23+00:00
sha256: ee123a69d09d3e17d604efb9ef1a65ae8edfb8df6100672b21bb34f44018e1c0
---

Relativity license will expire soon

a77749ad-b376-4605-894b-68d21fcc3c55

# Relativity license will expire soon

## Description

This alert is triggered when Relativity license expiration date is 1-30 days greater than current date. The alert is not true when the license is actually expired (expiration occurs when current date is equal to or greater than expiration date); there is a separate alert for the license being expired.

## Resolution Guidance

### Impact When Active

When the "Relativity license will expire soon" alert is active, there is no immediate disruption to the platform and users can continue working as normal. However, if the license is not renewed in time, access to Relativity will be restricted once it expires. Users may be unable to log in, and most functionality in Relativity will become unavailable. To avoid disruption, the license should be renewed and applied before the expiration date.

### How To Resolve

To ensure continued functionality, renew the license before the expiration date by contacting Relativity Support or an administrator from your organizationto initiate the renewal process.

Steps to apply/ renew Relativity License

-

Log in to Relativity.

-

Navigate to License tab.

-

Click on the row labeled Relativity to display the License details page.

-

Click Request License Key to display a pop-up with the request key.

-

Select the Request Key text, right-click on it, and then click Copy to copy the text to your clipboard.

-

Paste the text into an email message and submit it as a support ticket using this link: here . Support will process your request key and send you an email containing your activation key.

-

Once you have received your activation key from Relativity, you can apply it through the License details page. Navigate back to the license details page mentioned in step 3.

-

Click Apply License Key to display a pop-up window.

-

Copy the license activation key received in the email message sent by Customer Support. Paste it into the License Key box in the pop-up window. Ensure there are no unintended spaces or line breaks before or after the license key.

-

Click Apply. The display will automatically update with your new license specifications.

Note: If Relativity displays an error message, verify that you copied the activation key correctly.

##### You can also try..

- If the new license key does not apply correctly, verify that the system date and time are accurate on both the application and database servers. License validation may fail if there is a time mismatch.

- If you recently renewed your license but still see the expiration message, try clearing your browser cache and restarting IIS.

- If errors persist, notify the Relativity Support contact that issued your license key.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Filter Query labels.application_guid: "BD10A60D-B8EC-4928-84EE-6FC4F30D9612"

Group min

Threshold Between 1-30

Time Window 30 min

Frequency 1 min

### Alert Metric Details

Metric Name: relsvr.license.expires_days

Metric Description:

Metric Attributes:

Attribute Name Description

labels.application_name Application Name

labels.application_guid Application GUID

labels.name Metric name

labels.relsvr_system System name

labels.relsvr_subsystem Subsystem name

labels.message Message describes the license expiration details
