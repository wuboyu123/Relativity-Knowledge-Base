---
title: "RabbitMQ"
url: https://help.relativity.com/Server2025/Content/System_Guides/RabbitMQ/RabbitMQ.htm
collection: user
fetched_at: 2026-06-22T06:03:34+00:00
sha256: c8dd0fd7bd577ab8ff0bae77b6ebc77f1c92ca6b297defacfe88901ec26ef81a
---

RabbitMQ Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# RabbitMQ Testing, Certification, and Support Policy

Before installing or upgrading, you must install and configure your environment’s message broker. Next, install or upgrade your primary SQL Server and the Relativity Service Bus. You can find information about your environment’s message broker in Pre-installation overview . For installation instructions, see Relativity installation .

This policy defines how Relativity selects, tests, certifies, and supports RabbitMQ versions for Relativity Server major and patch releases. It also clarifies how certification scope, Erlang/OTP disclosure, version-series support, commercial-only RabbitMQ distributions, and support expectations are handled over time.

## Summary

- Relativity certifies a single RabbitMQ baseline per Relativity Server release, selecting the latest publicly available open-source patch version at an internal cutoff.

- For major Server releases, this version is certified at release.

- For Server patch releases, Relativity tests with intent to certify, but certification may be deferred and completed later via hotfix if issues arise.

- Certification is managed at the RabbitMQ release series level; earlier documented versions in the same RabbitMQ series remain supported unless explicitly excluded.

- Certifying a newer RabbitMQ version does not remove support for previously documented versions for the Relativity Server release and patches.

- Commercial-only RabbitMQ distributions, including VMware Tanzu-only releases, are not tested or certified.

- Relativity may continue supporting documented combinations even if the RabbitMQ version is no longer under community support.

## Full Policy

### RabbitMQ Testing, Certification, and Support Policy

#### Terminology

- RabbitMQ —refers to the publicly available open-source RabbitMQ server distribution.

- Relativity Server release —refers to a Relativity Server major release or patch release.

- Certified —means a RabbitMQ version has been explicitly tested and approved by Relativity for use with a specific Relativity Server release.

- Supported —means a RabbitMQ version remains within Relativity’s documented support scope for a given Relativity Server release.

- Supported does not imply that every downstream or upstream RabbitMQ patch release has been individually tested or re-certified. For example, if we certified the RabbitMQ 4.2 release by conducting internal testing on 4.2.5, assume that we have not tested on every patch version within the 4.2 series including 4.2.2, 4.2.4, and 4.2.6.

#### Scope and Eligibility

- Relativity tests and certifies only RabbitMQ versions that are publicly available in the open-source RabbitMQ distribution.

- Relativity does not test or certify RabbitMQ versions, patches, backports, or artifacts that are available only to commercial license holders.

- This includes VMware Tanzu RabbitMQ releases and any fixes distributed solely through commercial channels.

- An eligible RabbitMQ version is a publicly available release that is available by Relativity’s internal cutoff for testing and certification activities.

- For details on RabbitMQ's version policies, see RabbitMQ Release Information .

#### Internal Cutoff for Certification

- For both Relativity Server major releases and patch releases, Relativity selects the latest eligible RabbitMQ patch release available as of an internal cutoff date for testing and certification.

- If a newer RabbitMQ version is released after this cutoff, but before the official Relativity Server release date, Relativity does not reopen certification testing for that newer version as part of that release cycle.

#### Certification for Relativity Server Major Releases

For each Relativity Server major release, Relativity tests and certifies the latest eligible RabbitMQ patch release in the newest RabbitMQ release series that is under community support as of the internal certification cutoff.

#### Certification for Relativity Server Patch Releases

- For each Relativity Server patch release, Relativity tests the latest eligible RabbitMQ patch release available as of the internal certification cutoff, with the intent to certify that version.

- If issues requiring remediation are identified and cannot be resolved before the scheduled release, certification may be completed after release. In those cases, Relativity will disclose this in a Community Site article that accompanies the published patch.

- If necessary, Relativity may issue a corresponding hotfix.

#### Patch Release Testing Approach Within a RabbitMQ Release Series

- Relativity does not incrementally test each RabbitMQ patch release within a given RabbitMQ release series.

- Unless Relativity documents a patch version-specific exception, all patch versions within the RabbitMQ release series family are within the supported scope for an applicable Relativity Server release. For example, if we certified the RabbitMQ 4.2 release by conducting internal testing on 4.2.5, assume that 4.2.1, 4.2.2, 4.2.4, and 4.2.6 are supported unless otherwise noted.

#### Erlang/OTP Disclosure and Compatibility

- Relativity discloses the Erlang/OTP version used during RabbitMQ certification testing.

- Customers are responsible for validating their RabbitMQ and Erlang/OTP combination against the official RabbitMQ compatibility matrix prior to deployment or upgrade. To learn more, see Erlang Version Requirements .

#### Effect of Newer Certification Baselines

- Certification of a newer RabbitMQ version for a Relativity Server patch release does not remove support for previously certified RabbitMQ versions for the corresponding Relativity Server major release. For example, if RabbitMQ 4.1 is certified for Server 2025 and 4.2 is certified for Server 2025 Patch 1, then RabbitMQ 4.1 remains certified for Server 2025 Patch 1 unless otherwise noted.

- The newly certified version becomes the primary baseline for ongoing validation and future certification activities.

### Relativity Support Versus RabbitMQ Community Support

- There may be scenarios where a RabbitMQ version that remains documented and supported by Relativity for a given Relativity Server release is no longer under RabbitMQ community support.

- Relativity will continue to support any documented combination of Relativity Server and RabbitMQ, regardless of RabbitMQ community support status.

- RabbitMQ itself may no longer provide community support, public patch releases, or backports for that version.

#### Known Issues and Exceptions

- Relativity may publish documented exceptions, advisories, or exclusions for specific RabbitMQ or Erlang/OTP versions.

- Where such an exception is documented, it supersedes the general policy described above.

## RabbitMQ Version Support Matrix

The table below lists the RabbitMQ version tested and certified for Relativity Server 2025 and its subsequent patches, along with the Erlang/OTP version used during testing and any relevant compatibility notes.

Customers are responsible for validating their RabbitMQ and Erlang/OTP combination against the official RabbitMQ compatibility matrix prior to deployment or upgrade. The table below only identifies the version of Erlang that Relativity used for compatibility testing, and whether we are aware of any important, known issues with Erlang-RabbitMQ version compatibility.

For more information about RabbitMQ's versions, Erlang Version Requirements .

Server 2025 Version Certified RabbitMQ version Erlang version tested on Notes

Base 4.1.4 27.3.4.3 Erlang 28 is not compatible with RabbitMQ 4.1.4.

Patch 1 4.2.5 27.3.4.9 Erlang 28 is partially supported by RabbitMQ 4.2.x. Upgrades of clusters running Khepri have a known issue directly related to the breaking changes in Erlang 28.

On this page

- RabbitMQ Testing, Certification, and Support Policy

- Summary

- Full Policy

- RabbitMQ Testing, Certification, and Support Policy

- Relativity Support Versus RabbitMQ Community Support

- RabbitMQ Version Support Matrix


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
