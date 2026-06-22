---
title: "Production queue"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_queue.htm
collection: user
fetched_at: 2026-06-22T06:06:13+00:00
sha256: 5ff4557950ba67096bb893a1ddc304c4da5eaf5dd38cf35906d80ffdc8c94abb
---

Production queue Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production queue

The Production Queue tab displays all current production jobs running in your environment, and any jobs in error status. A job remains in this queue until the completion of branding and other processing.

You can view the production queue from Home. Select the Queue Management tab, and then click Production Queue .

## Change job priority

To change the priority of a job, click Change Priority at the bottom of the view. Enter a new integer value in the Priority field, and then click Update . Only one job runs at a time, the lower numbered job runs first and the higher numbered job runs last.

During a production job, Relativity sends a job to the branding queue for the stamping of redactions, headers, or other modifications. Any change to the priority of a job in the production queue changes its priority in the branding queue.

## Retry Production Job mass operation

### Security Configuration

You must configure certain instance level permissions to use Retry Production Job.

To configure the security permissions:

- Navigate to the Instance Details tab.

- Click Manage Permissions .

- Click Edit Permissions for a group on the Group Management tab.

- Enable the following security permissions:

Object Security Tab Visibility Admin Operations

- N/A

- Queue Management (parent)

- Production Queue (child)

- Change Queue Priority

- View Admin Repository

As long as you have the listed security permissions, you do not need view permissions to the workspaces or the production jobs to use Retry Production Job.

### Retrying production jobs

To retry production jobs from the Production Queue tab:

- Navigate to the Production Queue tab.

- Select the productions jobs that you want to cancel.

- Click Retry Production Job from the mass operations bar. The Retry production job window opens.

- Click Ok .

## Cancel Production Job mass operation

To cancel productions jobs from the Production Queue tab, use the Cancel Production Job mass operation.

### Security Configuration

You must configure certain instance level permissions to use Cancel Production Job.

To configure the security permissions:

- Navigate to the Instance Details tab.

- Click Manage Permissions .

- Click Edit Permissions for a group on the Group Management tab.

- Enable the following security permissions:

Object Security Tab Visibility Admin Operations

- N/A

- Queue Management (parent)

- Production Queue (child)

- Change Queue Priority

- View Admin Repository

As long as users have the listed security permissions, they do not need view permissions to the workspaces or the production jobs to use Cancel Production Job.

### Canceling multiple production jobs

To cancel multiple production jobs from the Production Queue tab:

- Navigate to the Production Queue tab.

- Select the productions jobs that you want to cancel.

- Click Cancel Production Job from the mass operations bar. The Cancel production job window opens.

- Click Ok .

## Production queue fields

The Production Queue displays the following fields:

- Workspace - the workspace that contains the production set used for a job.

- Production Name - the production set used for the job.

- Artifact ID - the unique identifier for the production set.

- Status - the current stage of the production job.

- Priority - the order in which the production job is run. Relativity sends jobs to the production engine by priority, and then orders them by submitted date and time. The default value is 100.

- Submitted Date - the date and time when a production job was submitted, or an attempt was made to resolve errors in a job. (In the Production Set Console, the user clicked Run , or Resolve Errors .)

- Submitted By - the user who initiated the job. You can use this information to prioritize production jobs by user.

On this page

- Production queue

- Change job priority

- Retry Production Job mass operation

- Security Configuration

- Retrying production jobs

- Cancel Production Job mass operation

- Security Configuration

- Canceling multiple production jobs

- Production queue fields


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
