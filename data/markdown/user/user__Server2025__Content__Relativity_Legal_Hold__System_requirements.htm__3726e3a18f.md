---
title: "System requirements"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/System_requirements.htm
collection: user
fetched_at: 2026-06-22T06:04:07+00:00
sha256: 0a2447aa6a9d8106b81a633220547f0737b0364bae69723e3b5851d7afc340f3
---

System requirements

# System requirements

For Legal Hold instances, the below single-server specifications apply. These requirements support a base installation of the Relativity product update to run the Legal Hold application.

## Email notification specifications

The following components are required to enable email notifications in Legal Hold:

- SMTP access

- EWS, POP3, or IMAP access to a dedicated Legal Hold mailbox on an email server

## Workstations (system admin PCs)

In Relativity Legal Hold, system admins must log onto the web interface with one of the below browsers. Custodians viewing hold information on the Portal may access the Custodian Portal on tablets and phones in addition to the below browsers and operating systems.

Software Versions

Browsers

- Google Chrome latest version (on both PC and Mac)

-

Apple Safari v11+ (Mac OS X 10.9)

-

Apple Safari v11+ (Mac OS X 10.10)

-

Firefox latest version (on both PC and Mac)*

Operating Systems

- Windows 10

- Windows 8 Desktop Mode (PC)

- Windows 7

- Windows XP Windows Server 2012 R2

## Scalability

In addition to adding more RAM and CPU cores to the Legal Hold server, you can add the following new servers as application usage grows:

- Separate Web Server - scale when Custodian Portal activity begins overutilizing the Legal Hold server RAM or CPU.

- Separate Background Processing Server (not common) - scale when Legal Hold sends continuous communications and begins overutilizing the Legal Hold server RAM or CPU.

- Separate Database Server (not common) - scale when many system admins are accessing the application simultaneously and running complex queries that overutilize the Legal Hold server RAM or CPU.
