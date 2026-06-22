---
title: "Instance in Developer Mode"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/c9e86198-5be1-4ecd-bfa4-f1a579ea2dff.htm
collection: user
fetched_at: 2026-06-22T06:18:38+00:00
sha256: d09bc9d4b71abce515f9843f6e6f0046253b1dcd113ac4a272e4096a6cb46e13
---

Instance in Developer Mode Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

c9e86198-5be1-4ecd-bfa4-f1a579ea2dff

# Instance in Developer Mode

## Description

Developer Mode in Relativity is a specialized setting that allows technical teams to build and test custom solutions within the platform. It is typically used in non-production environments and is not needed for standard casework or everyday user tasks. This alert is triggered when any of the following instance settings are enabled (True), regardless of the machine name specified:

- kCura.Service.ServiceHost/TestMode

- Relativity.Core/DeveloperMode

- Relativity.Core/DeveloperMachine

## Resolution Guidance

### Impact When Active

Enabling Developer Mode can impact the security and functionality of your environment. When active, it disables certain security protections, such as cross-site request forgery (CSRF) protection in API requests, making the system more vulnerable to unauthorized access. Additionally, it allows the system to display detailed error messages, including stack traces, which can be -useful for debugging but may expose sensitive system information. This setting is designed for development environments only and should not be enabled in production, as it can introduce security risks and expose critical application details. To maintain a secure and stable environment, it is recommended to keep Developer Mode disabled in production.

### How To Resolve

Update the following instance settings to ensure proper configuration:

Section Name Value

kCura.Service.ServiceHost TestMode False

Relativity.Core DeveloperMode False

Relativity.Core DeveloperMode False

To update:

- Log into Relativity

- Go to the Relativity Instance Settings tab

- Filter for Instance settings listed above.

- Update the values to False is they are currently set to True.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.instance.developer_mode : 1

Group Count

Threshold > = 1 Count greater than or equal to 1, alert triggers

Time Window 2 min Verified data for last 2 minute

Frequency 1 min Checks for every 1 min

### Alert Metric Details

Metric Name: relsvr.instance.developer_mode

Metric Attributes:

Attribute Name Description

labels.name Name of the instance setting

relsvr.instance.developer_mode Developer mode settings

On this page

- Instance in Developer Mode

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
