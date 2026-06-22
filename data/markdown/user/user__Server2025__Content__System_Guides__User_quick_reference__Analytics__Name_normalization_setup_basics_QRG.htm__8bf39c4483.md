---
title: "Name normalization setup basics"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Analytics/Name_normalization_setup_basics_QRG.htm
collection: user
fetched_at: 2026-06-22T06:10:39+00:00
sha256: 675179fdbe94615c469efe3dbe3a3a029a1d3c3d8657148e1bd3efad69b3b0c8
---

Name normalization setup basics Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Name normalization setup basics

This quick reference guide contains a basic workflow for setting up name normalization. For more detailed information, see Analytics .

## Name normalization setup

The setup for running name normalization has three parts:

- Saved search

- Analytics profile

- Structured analytics set

### 1. Saved search setup

Use the following conditions and fields to create the saved search used for name normalization. You do not need to set a sort order on this search.

#### Search Name

There is no recommendation for the saved search name. Follow your team’s normal protocol for naming searches.

#### Conditions

- From is set*

- Parent Document ID is not set**

- Include Families

*You can use any condition here which means “document is an email”. Other common choices are based on the Relativity Native File Type or file extension.

**Generally, the Parent ID field is empty for parent emails. However, there may be situations where it is populated with its own control number. In that case, you may omit this condition and name normalization will ignore emails that are attachments.

#### Fields

Any fields are acceptable. As a QC step, we recommend including the fields that will be mapped on the analytics profile as there may be fields that are named similarly that could lead to errors.

- Email From

- Email To

- Email CC

- Email BCC

Name Normalization also looks through the body of the email, but it’s not necessary to expose the extracted text field as one of the fields on the saved search.

### 2. Analytics profile setup

The analytics profile is where you map the fields containing input information for name normalization. Note that while you can use the same profile that you use for email threading, name normalization only considers the Email From, Email To, Email CC, and Email BCC fields from the Analytics Profile.

Map the fields as follows:

Profile field name

Mapped document object field

Email from field Email From

Email to field Email To

Email cc field Email CC

Email bcc field Email BCC

Email subject field Email Subject

Email date sent field Email Date/Time Sent

Parent document ID field Parent Document ID

Attachment name field File Name

Conversation ID field (Do not map)

### 3. Structured analytics set

Here are the steps and choices for creating a structured analytics set. For more information on these settings, see Running structured analytics .

#### Structured Analytics Set Information

- Name —enter a name for the structured analytics set.

- Prefix —keep the default prefix or add your own prefix. Shorter prefixes, even just two characters, such as “E1,” take up less space in your views.

- Operations to run —select Name normalization .

- Data source —select the saved search you created above.

#### Name normalization fields

- Analytics profile —select the profile you created above.

- Analyze topmost email only —set this to Enabled .

- Use email header fields —set this to Enabled .

- Languages —select any language used in email headers in your extracted text. We recommend that you always include English, even for data sets in other languages.

#### Optional Settings

-

Analytics server —choose the appropriate Analytics server.

- Enable additional domain filtering —set this to Enabled . This gives you more options for how to sort and filter domain names extracted from the email fields.

On this page

- Name normalization setup basics

- Name normalization setup

- 1. Saved search setup

- 2. Analytics profile setup

- 3. Structured analytics set


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
