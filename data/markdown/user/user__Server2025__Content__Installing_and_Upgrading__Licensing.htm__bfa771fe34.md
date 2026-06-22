---
title: "Licensing overview"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Licensing.htm
collection: user
fetched_at: 2026-06-22T06:01:47+00:00
sha256: 3df33bfbd2206b484a220483ff61676716becf27f52c613f4bb0c8bc3c1fbccf
---

Licensing overview Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Licensing

Relativity licensing includes flexible options that you can tailor to the size, type, and other requirements of your organization as part of your contractual agreement with Relativity . After you install Relativity, you can activate a new license, or renew your current license, by requesting and applying an activation key. You must also complete these steps for Processing.

If you are a new client or upgrading from an unlicensed version, Relativity activates a seven-day trial license, which you can temporarily use until obtaining your official license key. If you are an existing client, you enter a seven-day grace period after the expiration of your license. Processing does not provide a trial license.

## Licensing terminology

The License details page displays information about the license currently used by your Relativity installation. See Viewing license details .

### Trial license

When you initially install Relativity, you'll temporarily have a seven-day trial license for an unlimited number of seats. The system applies a seven-day trial license for the current seat count to a Relativity installation after the license expires. The value in the Number of Seats field is displayed as -1. (Processing doesn’t provide a trial license.)

### Grace period

If you have not renewed your Relativity license before the expiration date, you have a seven-day grace period to complete the renewal process. A grace period is not provided for a Processing license. The License details page displays the expiration date for the license, as well as your contractual seating and license type information. After your grace period expires, Relativity displays an error message when users attempt to access the system.

## Relativity alerts and messages

As a system admin, email and alerts notify you when a Relativity or Processing license expires.

You enter a grace period if you did not renew your Relativity license before the expiration date. It provides you with an additional seven days to complete the renewal process. In Relativity, the License details page displays the expiration date for the grace period.

After the expiration date for your trial or existing license, Relativity displays an error message when users attempt to access the system. System admins can access only the License tab, which provides functionality for obtaining an activation key.

Your Relativity and Processing licenses immediately become invalid if you modify the instance setting in the Relativity .LicenseManager section of the instance setting table.

## Viewing license details

On the License details page, you can view information about your Relativity or Processing license. This page also provides you with the options to request and apply a license. See Licensing an application .

You must have system admin permission to view the License tab. Full system admins are the only users able to edit license information. For more information on configuring admin permission settings, see Instance security .

- Click your name in the upper right corner of Relativity, and then click Home .

- Click the License tab.

- Click an application name to display additional information about its license. The following information is available on the details page for Relativity and Processing licenses:

- Relativity license —the details page displays the application name, instance name, expiration date, number of seats, and type.

- Processing license —the details page displays the application name, Relativity instance name, expiration date, as well as the URL for each worker manager server, and the number of workers that it can run. In the following example, a worker manager server URL is net.tcp://mainline-7-inv.testing.corp:6859/Invariant API : #, and the number of workers that it can run is five.

When you apply a new Processing license in your Relativity environment, all jobs in the processing queue must complete before Relativity identifies any additional worker manager servers that you may have purchased as licensed. For more information, see Upgrading a worker manager server installation .

## Licensing an application

You must generate a request key that we use to create an activation key for your license. Next, you apply this activation key to your application. You follow the same process to request a license for Relativity or Processing.

### Generating a license request

After installing Relativity or Processing, you can use these instructions to generate a license request through the License tab.

- Log in to Relativity.

- Select the License tab.

- Click Relativity or another application name to display the License details page.

When you initially install Relativity, you temporarily have a seven-day trial license until you obtain the activation key for your official license. The License details page displays the expiration date for the trial license, and uses the value -1 to indicate an unlimited seat count. For information on Relativity license types, see Licensing terminology .

All Relativity environments require an instance name, which appears in the Instance Name field. During the initial installation of Relativity, this field may display UNSETINSTANCE. Customer Support will work with you to define this name by requesting information about the use of the Relativity instance. For example, you may be using this instance in your production or test environment, as a demo virtual machine (VM), or in some other capacity.

- Click Request License Key to display a pop-up with the request key.

- Select the Request Key text, right-click on it, and then click Copy to copy the text to your clipboard.

- Paste the text into an email message to Relativity Customer Support . Customer Support processes your request key and sends you an email message containing your activation key.

### Applying a license key

After you receive a license key from us, you can apply it to your application through the License details page.

- Navigate to the License tab. See steps 1-3 in Generating a license request .

- Click Apply License Key to display a pop-up window.

- Copy the license activation key received in the email message sent by Customer Support. Paste it into License Key box in the pop-up window.

- Click Apply . The License Details section of the tab automatically displays your contractual information.

If Relativity displays an error message, verify that you copied the activation key correctly. Contact Relativity Customer Support if you have any questions about applying your license key.

On this page

- Licensing

- Licensing terminology

- Trial license

- Grace period

- Relativity alerts and messages

- Viewing license details

- Licensing an application

- Generating a license request

- Applying a license key


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
