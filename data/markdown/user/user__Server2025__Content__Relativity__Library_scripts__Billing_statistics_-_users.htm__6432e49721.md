---
title: "Billing statistics - users"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Billing_statistics_-_users.htm
collection: user
fetched_at: 2026-06-22T06:15:11+00:00
sha256: 1021b8cb6a3090f112f51d7f2e169fa6973742eaff93a41566652b4e9d43c81a
---

Billing statistics - users Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Billing statistics - users

To help optimize performance, we don't store all historical data in Case Statistics tables. The Billing Statistics - Case Rollup only stores data for 13 months by default to ensure high performance. If you need to store this data for a longer period of time, edit the BillingDataRetentionPeriodInMonths instance setting to your desired value. Note the minimum value is 13 months.

This script is a billing script that reports on all users who had their Relativity access enabled, and belonged to a group which was assigned to a workspace during a specific month. The data is taken as a snap shot daily when the Billing Agent runs. This script can be run at any time from Home.

## Inputs

After clicking Run on the Script console, enter values for the following inputs:

- Usage Period Year (YYYY) is the year you wish to report on.

- Usage Period Month (MM) is the month you wish to report on.

- Replace User Name With Hash Value determines whether the username portions of user e-mail addresses are replaced by a hash value.

- Hide Case Names determines whether the case names are hidden in the report.

## Results

After you run the script, the Billing Statistics - Users report displays.

The report includes the following columns:

Column Definition

Case Name The name given to the workspace in Relativity.

Case Artifact ID The unique Artifact ID associated with the workspace specific to that environment.

Usage ID The usage ID given to the workspace. This is a unique workspace and month identifier which combines Instance, Case Artifact ID, Year, and Month.

Case User ID The unique identifier for that workspace, user, and month which combines Usage ID and User Artifact ID.

User Artifact ID The unique system-level Artifact ID associated with the user.

Relativity Case User Name The user's name as entered in the Relativity workspace.

Original Email Address The original e-mail address of the user if changed during the month.

Flag Indicates whether the user e-mail associated with that account, changed during the month.

Is System Admin Indicates whether the user is associated to the System Administrators group.

Logged In This Month If a user accesses the instance, a 1 appears in this column.

Last Login Date on which the user last logged into the system.

Last Login UTC The time the user last logged into relativity in UTC time.

Replace User Name With Hash Indicates whether the username portions of user e-mail addresses are replaced by a hash value.

Time Executed Date on which the report was generated.

Time Executed UTC The UTC time when the report was generated.

## Retrieving historical data

When you upgrade to Relativity 9.7 or above, the roll-up script pulls information for the following columns from a table that is pre-populated with data from the month that you upgrade as well as the previous month:

- Last Login UTC

- Last Login

- Logged In This Month

If you want to use this script to pull older historical data, contact our Support team for the Billing statistics – users script version 11, which supports this functionality. Additionally, verify that your Audit table contains the historical data that you need.

On this page

- Billing statistics - users

- Inputs

- Results

- Retrieving historical data


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
