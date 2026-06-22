---
title: "Advanced workflows with Relativity Legal Hold"
url: https://help.relativity.com/Server2025/Content/Recipes/Legal_Hold/Advanced_workflows_with_Relativity_Legal_Hold.htm
collection: user
fetched_at: 2026-06-22T06:17:27+00:00
sha256: 674fab755f4f8aa906c4836220f5d6357c8f84e180d385e5272422200b2871bc
---

Advanced workflows with Relativity Legal Hold Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Advanced workflows with Relativity Legal Hold

When working in Relativity Legal Hold, there may be a need to customize it to fit your unique workflows. In particular, we discuss tracking custodian information (like employee location), tracking custodian response information in real time, and creating custom dashboards to visualize and provide snapshots of your Hold data.

## Recipe Overview

This recipe utilizes the flexibility provided by Relativity to integrate it into the Legal Hold application, gaining the ability to track additional information or obtain information out of Relativity in real time via Dashboards.

## Requirements

- Relativity 9.4 or above

- Relativity Legal Hold v4.1.437.2+

## Directions

Below are some workflow suggestions one can employ to customize Relativity Legal hold to cater to their unique needs and / or for advanced reporting functionality.

### Custom fields

Create custom fields to track additional pieces of information that are unique to your Hold needs or tie in well with your precedent of subsequent workflow. Below are a couple examples of these fields.

Custom fields are on the Projects object to track information about the Department that the hold is associated with. Below is an illustration of what the Custom field and the Custom Layout would look like on a layout.

When creating the custom fields, layouts, or views, keep in mind the following considerations:

- You should not associate custom fields, layouts, or views with the Relativity Legal Hold application.

- You can enable the Open to Association setting to Yes.

- You can enable the Allow Group By and Allow Pivot settings to Yes.

### Custodian related information

The Custodian Status Tab can be unhidden and the view on the object made available. It’s useful to report information about the Custodian’s interactions, such as:

- Number of reminders sent

- Numbers of escalations

- Date / Time the reminder was sent

- Date / Time the last escalation was sent

- Date / Time of the last scheduled escalation

- When questionnaire was completed and submitted

- When the Hold (Communication) Notice was sent

- When the Communication was viewed

- If the Hold notice was acknowledged

To create the Custodian Status Tab, fill out the settings as follows:

- Name - Custodian Status

- Link Type - Object

- Parent - Legal Hold

- Object Type - Custodian Status

To create a new View on the Custodian Status Object, fill out the setting as follows:

- Name - Custom View – Custodian Status

- Object Type - Custodian Status

- Fields - Select the fields of your choice from the following recommendations:

- Project

- Escalation Sent

- Reminders Sent

- Acknowledgment Status

- Questionnaire Status

- Sort Order - Custodian | Project

The Custodian Role Tab can also be unhidden and the view on the object made available. It's useful to report information about the Custodian's interactions, such as:

- Custodian's role on a hold

- When the Custodian was released

To create the Custodian Role Tab, fill out the settings as follows:

- Name - Custodian Role

- Link Type - Object

- Parent - Legal Hold

- Object Type - Custodian Role

To create a new View on the Custodian Role Object, fill out the settings as follows:

- Name - Custom Role – Custodian Status

- Object Type - Custodian Role

- Fields - Select the fields of your choice from the following recommendations:

- Role

- Project

- Release Date

- Custodian:: Email

- Sort Order - Custodian | Project

### Reporting

Dashboards provide a way to make information available in Relativity realtime, providing self-service with very little training. Layering the Dashboards with custom views make it a powerful reporting aid. Below are a few examples of custom Dashboards that address reporting needs.

#### Projects Object - Project Information Dashboard:

Name

Group By

Pivot On

Type

Subject Matter Start Date

Subject Matter Start Date

<Grand Total>

Line Chart

Project Status by External Counsel

External Counsel

Project Status

Table

Department

(Custom field)

Office

<Grand Total>

Bar Chart (OR) Pie Chart

#### Custodian Object - Custodian Information Dashboard:

Name

Group By

Pivot On

Type

Employee Status (Custom field) by Department

Department

<Grand Total>

Bar Chart (OR) Pie Chart

Employment Start Date

Employment Start Date

<Grand Total>

Line Chart

Custodian Office

Office

<Grand Total>

Bar Chart (OR) Pie Chart

#### Question Responses Object - Question Responses Breakdown:

Name

Group By

Pivot On

Type

Answers by Project

Project

Answer Status

Stacked Bar Chart

Custodian by Project

Project

Custodian

Table

#### Mailbox Object - Question Responses Breakdown:

Name

Group By

Pivot On

Type

Message Type

Message Type

<Grand Total>

Pie Chart

Message Status by Project

Project

Message Status

Stacked Bar Chart

Message Sent Date

Sent Date

<Grand Total>

Line Chart

#### Custodian Status Object - Custodian Information Dashboard:

When the Custodian Status tab is available, we can use Pivots and Dashboards to visualize a lot of this information and make it more digestible.

Name

Group By

Pivot On

Type

Escalations by Custodian

Custodian

Escalations Sent

Table

Resolutions by Custodian

Custodian

Resolved By

Table

Reminders by Custodian

Custodian

Reminders Sent

Table

## References

On this page

- Advanced workflows with Relativity Legal Hold

- Recipe Overview

- Requirements

- Directions

- Custom fields

- Custodian related information

- Reporting

- References


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
