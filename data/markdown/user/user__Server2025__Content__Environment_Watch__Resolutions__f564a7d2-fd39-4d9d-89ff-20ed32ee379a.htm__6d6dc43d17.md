---
title: "Relativity license has expired. You have less than 7 days before access to your Relativity environment is disabled"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/f564a7d2-fd39-4d9d-89ff-20ed32ee379a.htm
collection: user
fetched_at: 2026-06-22T06:18:28+00:00
sha256: 770846525837865ed083880ac05314e540e22b3aee0514828c42d0d7204a7cec
---

Relativity license has expired. You have less than 7 days before access to your Relativity environment is disabled Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

f564a7d2-fd39-4d9d-89ff-20ed32ee379a

# Relativity license has expired. You have less than 7 days before access to your Relativity environment is disabled

## Description

This alert is triggered when Relativity license expiration date is equal to or greater than the current date. You have less than 7 days before access to your Relativity environment is disabled.

## Resolution Guidance

### Impact When Active

Once the 7-day grace period expires, Relativity users who are not system administrators will not be able to access the instance. Admins who access the instance may not be able to perform actions other than renewing the license. At this stage, Relativity services on servers may not be able to start.

### How To Resolve

To resolve this error, contact Relativity Support or an administrator from your organization to proceed with the license renewal. Steps to apply/ renew the Relativity License.

- Log in to Relativity.

- Navigate to License tab.

- Click on the row labeled Relativity to display the License details page.

- Click Request License Key to display a pop-up with the request key.

- Request Key text, right-click on it, and then click 'Copy' to copy the text to your clipboard.

- Paste the text into an email message and submit it as a support ticket using this link: here . Support will process your request key and send you an email containing your activation key.

- Once you have received your activation key from Relativity, you can apply it through the License details page. Navigate back to the license details page mentioned in step 3.

- Click Apply License Key to display a pop-up window.

- Copy the license activation key received in the email message sent by Customer Support. Paste it into the License Key box in the pop-up window. Ensure there are no unintended spaces or line breaks before or after the license key.

- Click Apply. The display will automatically update with your new license specifications.

Note: If Relativity displays an error message, verify that you copied the activation key correctly.

##### You can also try..

- If the new license key does not apply correctly, verify that the system date and time are accurate on both the application and database servers. License validation may fail if there is a time mismatch.

- If you recently renewed your license but still see the expiration message, try clearing cache and restarting IIS

- If errors persist, notify the Relativity Support contact that issued your license key.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Filter Query labels.application_guid: "BD10A60D-B8EC-4928-84EE-6FC4F30D9612"

Group min

Threshold < 1

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

On this page

- Relativity license has expired. You have less than 7 days before access to your Relativity environment is disabled

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- Alert Details

- Alert Condition Details

- Alert Metric Details


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
