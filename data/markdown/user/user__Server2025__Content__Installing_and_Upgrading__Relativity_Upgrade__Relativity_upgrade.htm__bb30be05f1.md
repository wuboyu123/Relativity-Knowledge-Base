---
title: "Relativity upgrade overview"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Relativity_upgrade.htm
collection: user
fetched_at: 2026-06-22T06:01:57+00:00
sha256: ac65897ea970948b0eabdd18d2fd8d61a9ef9f9505a51ccf6e3fc3a6a0878276
---

Relativity upgrade overview Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity upgrade

Use the following workflows to upgrade your current Relativity installation to Server 2025.

To begin your upgrade process, address custom solutions and scripts before downloading the Relativity installer. Once you complete the workflow specific to your upgrade path, we recommend completing the post-installation verification tests post-upgrade to confirm that your environment has been upgraded properly.

We recommend preparing for your upgrade process by using the Pre-Upgrade Checklist . You can use this document to discuss an upgrade strategy for your current installation of Relativity with the Customer Support team .

If you are installing Relativity for the first time, contact the Customer Support team for additional information. You may also want to review the information on the Relativity installation page.

## Addressing custom scripts that trigger imaging jobs

Please note that if you use custom scripts that trigger imaging jobs, they may no longer work after upgrading.

This is because the components that those custom scripts rely upon no longer exist due to the changes made to the imaging framework, which are listed below. The imaging operations performed by these custom scripts are not accounted for in the KCD Snapshot Solution script.

- The Imaging Set Manager and Worker agents have been deprecated.

- The Imaging Set Queue table has been deprecated.

- The Imaging API now submits an imaging job directly to Invariant, worker manager server.

## Required pre-upgrade steps for all Relativity versions

Before you begin your upgrade, you must complete the following pre-upgrade steps.

Click to expand required pre-upgrade steps for all Relativity versions

Complete the following steps and verify you have the necessary information required for all upgrades of Relativity. Depending on your upgrade path, you may have additional configuration or other tasks to perform specific to the version of Relativity you're installing.

Make sure you have the appropriate system admin permissions in Relativity before beginning the upgrade. For more information, see Managing security .

Confirm that jobs are not running in any of the queues. If the agents are running, they may attempt to run a job against a database that does not have an upgraded schema and cause serious errors in your Relativity environment.

### Back up your Relativity environment

Back up your SQL databases and your Relativity IIS websites before you begin the upgrade process. You should also back up both the structured analytics sets and analytics indexes before your upgrade to ensure that there is no data loss. This may take a while so it's recommended to run analytics backups either during the week of or the week prior to your upgrade. Usually this data does not change daily, so this helps to mitigate any data loss. For more information, see Moving Analytics indexes .

### Reboot machines with Windows updates

After installing Windows updates, reboot your machines before attempting to install Relativity. Complete this step to ensure that all Relativity components are properly installed. Incomplete Windows updates lock system files, which may cause silent failures and prevent the proper installation of Relativity components.

## Server upgrade workflow

Use the following workflow to upgrade your Relativity instance to Server 2025.

Never upgrade your Relativity version while there are jobs of any type currently in progress in your environment. Doing this leads to inaccurate results when you attempt to finish those jobs after your upgrade is complete. This is especially important for imaging and processing jobs.

- Before you upgrade, verify that you meet all requirements outlined in Pre-installation .

-

The Worker Manager cannot be upgraded until the web server used for the ProcessingWebAPI instance setting/IdentityServerURL in the Invariant.dbo.app Settings table is upgraded. If those links are pointed to a load balancer, then all web servers must be upgraded first.

- Once you've completed upgrading core servers—Secret Store andPrimary SQL—all remaining servers can be upgraded in any order or in parallel.

- Install Secret Store and configure all machines in your environment to access it. This step must be completed before the Relativity upgrade. For more information, see Secret Store . Upgrading Secret Store and having to run the configure-service command will lock Secret Store and impact users.

- Stop RabbitMQ and the following Agent Services: kCura Service Host and kCura EDDS Agent Manager.

- Stop the following Web Services: kCura Service Host, kCura Web Processing, and IIS.

- Stop the Invariant Queue Manager Service, Analytics Service, and Data Grid Elastic Services.

- Run the Relativity installer on your Primary SQL Server to upgrade the EDDS database and install the required library applications. You cannot access your Relativity environment until you complete this step. Depending on what version you're upgrading from, this process may start automatically after the installer is finished running. See Upgrading your SQL Server .

- Run the Relativity Messaging Broker installation on the messaging broker server. See Upgrading your Messaging Broker .

- Run the Relativity installer on all distributed SQL servers if present. See Distributed SQL Server upgrade .

- Run the Relativity installer on the Agent server. See Upgrading your agent server .

- Run the Relativity installer on the Web server. See Upgrading your web server .

- Confirm that the IIS services are now running. If not, start the IIS service.

- (Optional) Log in to Relativity and click the Workspace Upgrade queue . Set the priority or order on the workspaces as necessary. You can monitor your workspaces in the Monitoring upgrades with the Workspace Upgrade queue .

After you run the installer on at least one agent server, the system begins upgrading individual workspaces. You can now log in to Relativity to monitor workspace upgrades through the Workspace Upgrade queue.

- Upgrade your worker manager server. For more information, see the Upgrading a worker manager server installation .

If this is your first upgrade to Server 2025 and above, you must upgrade any worker servers after upgrading your worker manager server.

- Upgrade Relativity Analytics. See Upgrading or installing your Analytics server .

- Apply the latest hotfixes for your Relativity version. For more information, see Applying a Server hot fix or patch .

On this page

- Relativity upgrade

- Addressing custom scripts that trigger imaging jobs

- Required pre-upgrade steps for all Relativity versions

- Back up your Relativity environment

- Reboot machines with Windows updates

- Server upgrade workflow


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
