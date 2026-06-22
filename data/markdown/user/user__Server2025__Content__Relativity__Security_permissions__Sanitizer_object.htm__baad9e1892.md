---
title: "Sanitizer object"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Sanitizer_object.htm
collection: user
fetched_at: 2026-06-22T06:21:15+00:00
sha256: b74af9c43cb60166ddcb1252c724f0e9ed65a1511995273d5d4f353c7eb04a7a
---

Sanitizer object Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Sanitizer object

The Sanitizer object is a Relativity system object that stores the Sanitizer Whitelist information. The Sanitizer Whitelist is used to parse embedded HTML code in HTML-enabled and custom text fields and labels. The sanitizer object is where you can enable or disable the sanitization process on the Relativity instance. The Sanitizer object is located in the Sanitizer Tab.

The sanitization process parses HTML content located in “Message of the day” page, HTML enabled fields, labels and custom text fields on layouts, when rendered on user interface, strips any HTML markup which is not included in the white list.

Sanitization process is enabled by default.

## Sanitizer Whitelist

Within the Sanitizer tab is the HTML Sanitizer Whitelist. The HTML Sanitizer whitelist policy XML is used to identify and remove any potentially malicious JavaScript, or any other scripting, which might undermine web site security. This xml contains list of allowed HTML tags, attributes, styles and rules. Rules are usually defined as Regular Expression. For optimization, you can reference common attributes and rules throughout xml. Since there are different ways of getting data into Relativity (Relativity UI, RSAPI, RDC, direct SQL access), it's recommended to sanitize HTML on Display and on Save.

### Modifying the white list

In the Sanitizer tab, you can modify the white list, but modify it with caution and at your own risk.

Modifying the white list incorrectly could open your instance to possible cross-site scripting or other risks.

The XML in the white list specifies approved HTML markup that will not get stripped from fields with HTML upon page view.

## Sanitizer tab

The sanitizer admin tab is hidden by default, but the HTML sanitization is on by default. The visibility of the tab in your Relativity instance has no effect on the sanitization process.

Disabling sanitization is a high security risk and is highly discouraged. For any questions, please reach out to Relativity Support .

### Adding the Sanitizer tab

To add the Sanitizer tab at the Admin level:

- Select the Admin Workspace Configuration tab and select Tabs .

- Filter for Sanitizer from the tabs list and select it.

- Click Edit on the Sanitizer tab layout and set the Visible field to enabled.

- Click Save .

On this page

- Sanitizer object

- Sanitizer Whitelist

- Modifying the white list

- Sanitizer tab

- Adding the Sanitizer tab


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
