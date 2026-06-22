---
title: "Post-Install Verification for Monitoring Agents"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Post-Install_Verification_for_Monitoring_Agents.htm
collection: user
fetched_at: 2026-06-22T06:11:53+00:00
sha256: 84c337d442eb82f6a80f6500f280d55eaf2d7896b4d5fcfbce69a727b87e3417
---

Post-Install Verification for Monitoring Agents Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Post-Install Verification for Monitoring Agents

## Verify Monitoring Agent dashboard exists

Ensure the Monitoring Agent dashboard is present.

Steps:

- Login to Kibana.

- Navigate to Dashboards

- Use the search bar to search for Monitoring Agents .

Expected Result:

- Monitoring Agent is listed.

Screenshot:

## Verify Monitoring Agents dashboard tags

Ensure the correct tags are assigned to the dashboard.

Steps:

- Login to Kibana.

- Navigate to Dashboards .

- Use the search bar to search for Monitoring Agents and open the dashboard.

Expected Result:

- Tags:

- Relativity Environment Watch

- FeatureDomain: Monitoring

Screenshot:

## Verify dashboard filters populate with data

Ensure filter dropdowns are populated with available data.

Steps:

- Login to Kibana.

- Navigate to Observability | Dashboard .

- Click on the dashboard and open each filter dropdown.

Expected Result:

- Filter dropdowns show available values.

Filters may take a few minutes to populate after initial data collection begins.

Screenshot:

## Verify data population by changing filters and time ranges

Ensure the dashboard data is loading correctly.

Steps:

- Login to Kibana.

- Open the Monitoring Agent dashboard.

- To change the time range, use the time filter at the top right, select the desired range (e.g., 15 minutes, 1 hour, 12 hours, 24 hours), and apply changes.

- Adjust filters to see if data updates accordingly.

Expected Result:

- All panels are populated with data.

Screenshot:

## Verify Hosts and Agent versions

Ensure hosts and agent versions are correctly displayed.

Steps:

- Login to Kibana.

- Open the "Monitoring Agent" dashboard.

Expected Result:

- Host column lists multiple hosts.

- Agent Version is the same for all hosts.

- Last Modified Date column shows timestamp to verify installation time.

Verify that the agent version is consistent across all nodes to ensure uniform monitoring capabilities.

Screenshot:

## Verify data in Discover

Ensure dashboard data is reflected in Discover.

Steps:

- Login to Kibana.

- Open the dashboard and hover over the top right corner of the Monitoring Agents table to reveal the Explore in Discover option.

- Click Explore in Discover .

Expected Result:

- Data is visible in Discover.

Screenshot:

On this page

- Post-Install Verification for Monitoring Agents

- Verify Monitoring Agent dashboard exists

- Verify Monitoring Agents dashboard tags

- Verify dashboard filters populate with data

- Verify data population by changing filters and time ranges

- Verify Hosts and Agent versions

- Verify data in Discover


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
