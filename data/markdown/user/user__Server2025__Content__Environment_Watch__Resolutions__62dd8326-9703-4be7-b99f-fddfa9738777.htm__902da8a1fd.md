---
title: "Processing License will expire soon"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/62dd8326-9703-4be7-b99f-fddfa9738777.htm
collection: user
fetched_at: 2026-06-22T06:18:25+00:00
sha256: 9e2f5d6f693f5fd532591aeb0b95633d2c6981970eb6abeafc0e6571c96a6d91
---

Processing License will expire soon Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

62dd8326-9703-4be7-b99f-fddfa9738777

# Processing License will expire soon

## Description

This alert is triggered when Processing license expiration date is 1-30 days greater than current date.

## Resolution Guidance

### Impact When Active

When the "Processing license will expire soon" alert is active, there is no immediate disruption to Processing workflows (existing functionality remains available) and jobs can continue to run as normal. However, if the license is not renewed in time, actions such as creating new processing sets, publishing data, or initiating inventory and discovery jobs will no longer be available. Existing processing sets will still appear in the system but will become non-functional. To prevent workflow interruptions, it is important to renew and apply the Processing license before the expiration date.

### How To Resolve

-

Renew the License before the expiration date.

-

Contact Relativity Support or an administrator from your organization to proceed with the renewal.

Steps to apply/renew the Processing License in Relativity

-

Log in to Relativity.

-

Navigate to the License tab.

-

Click on Processing to display the License details page.

-

Click Request License Key to display a pop-up with the request key.

-

Select the Request Key text, right-click on it, and then click Copy to copy the text to your clipboard.

-

Paste the text into an email message and submit it as a support ticket using this link: here . Support will process your request key and send you an email containing your activation key.

-

Once you have received License Key from Relativity, you can apply it through the License details page. Navigate back to the license details page mentioned in step 3.

-

Click Apply License Key to display a pop-up window.

-

Copy the license activation key received in the email message sent by Customer Support. Paste it into the License Key box in the pop-up window. Ensure there are no unintended spaces or line breaks before or after the license key.

-

Click Apply. The display will automatically update with your new license specifications.

Note: If Relativity displays an error message, verify that you copied the activation correctly.

##### You can also try..

- If the new license key does not apply correctly, verify that the system date and time are accurate on both the application and database servers. License validation may fail if there is a time mismatch.

- If you recently renewed your license but still see the expiration message, try clearing cache and restarting IIS.

- If errors persist, notify the Relativity Support contact that issued your license key.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Filter Query labels.application_guid: "ED0E23F9-DA60-4298-AF9A-AE6A9B6A9319"

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

On this page

- Processing License will expire soon

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
