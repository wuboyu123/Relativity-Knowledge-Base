---
title: "Relativity compatibility matrix"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/System_requirements/Compatibility_matrix.htm
collection: user
fetched_at: 2026-06-22T06:03:55+00:00
sha256: af8c4a179eaaac2f3e55147a9675f8ffebea88f638b541c4a1d91a23af2bae58
---

Relativity compatibility matrix Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity compatibility matrix

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Relativity system requirements matrix

The following table breaks down the supported operating systems, framework, IIS versions, browsers, versions of SQL Server, and TLS (when applicable) for each of the still-supported versions of Relativity Server. For additional Chrome, Firefox, and Safari supported version details, see End user browser and operating system requirements

Software Server 2023 Server 2024 Server 2025 TLS 1.2 TLS 1.3

Operating systems - Relativity Desktop Client

Windows 10 √ √ √ √

Windows 11 √ √ √ √ √

Operating systems - servers

Windows Server 2016 √ √ √ √

Windows Server 2019 √ √ √ √

Windows Server 2022 √ √ √ √ √

Windows Server 2025 √ √ √

Framework

Microsoft .NET Version 3.5 √ √ √

Microsoft .NET Version 4.6.2

Microsoft .NET Version 4.7

Microsoft .NET Version 4.7.2 √ √ √

Microsoft .NET Version 4.8 √ √ √

Microsoft .NET Version 4.8.1 √ √ √

SQL versions

SQL Server 2017 √ √ √ √

SQL Server 2019 √ √ √ √

SQL Server 2022 √ √ √ √ √

RabbitMQ

4.1.4 √ √ √

3.13.x √ √ √ √

3.12.x √ √ √ √

Secret Server √ √

- You must use RabbitMQ version 4.1.4, as it is the only supported version for Server 2025. RabbitMQ 4.1.4 is only compatible with Erlang 26.2 – 27.x.

- Erlang 28 is not compatible with RabbitMQ 4.1.4.

- Ensure that you're using the 64-bit version of Erlang, or else the system will be constrained to 2GB of memory. For details on RabbitMQ's version policies, see RabbitMQ versions . Review the RabbitMQ upgrade overview beforehand to avoid issues during the upgrade process.

- For compatibility details, see Erlang Version Requirements . To download the latest version of Erlang, see Download Erlang .

## RabbitMQ

To learn more about the RabbitMQ version support policy, see RabbitMQ Testing, Certification, and Support Policy .

RabbitMQ version certified Server 2023 Server 2024 - GA and Patch 1-2 Server 2024 - Patch 3 Server 2025 -GA Server 2025 - Patch 1 TLS 1.2 TLS 1.3

4.2 √ √

4.1 √

3.13 √ √

3.12 √ √

## End user browser and operating system requirements

Support for Internet Explorer (IE) ended with Server 2022. Support for Microsoft Edge began in Server 2022

Software Latest Version Tested by Relativity

Chrome (Windows, Mac OSX) 130.0.6723.59

Edge (Windows, Mac OSX) 130.0.2849.52

Firefox (Windows, Mac OSX) 131.0.3

Safari (Mac OSX) 18.1

Relativity does not currently support the Linux operating system for any browser.

## Supported CAAT version

Software Server 2023 Server 2024 Server 2025

CAAT

4.7.23.A23

CAAT 4.7.23.A23 is the supported Analytics Engine version for Relativity Server 2023.

5.1.0.A1

CAAT 5.1.0.A1 is the supported Analytics Engine version for Relativity Server 2024.

- CAAT 4.x (initial Server 2025 release)

- CAAT 5.1.0.A1

Server 2025 was initially released with CAAT 4.x; CAAT 5.1.0.A1 is also supported.

Jetty 12.1.6 12.1.6 12.1.6

## Relativity release matrix

The following table lists the Invariant, worker manager server, and Outside In versions released with each Relativity release. Along with the Relativity Analytics engine and Secret Store versions compatible with each release of Relativity.

Relativity version Relativity release date Outside In version Invariant version Analytics engine version Secret Store version

25.0.538.3 December 12, 2025 2025.8.0 25.0.375.6 4.7.11.A11 50.2.27.3

On this page

- Relativity compatibility matrix

- Relativity system requirements matrix

- RabbitMQ

- End user browser and operating system requirements

- Supported CAAT version

- Relativity release matrix


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
