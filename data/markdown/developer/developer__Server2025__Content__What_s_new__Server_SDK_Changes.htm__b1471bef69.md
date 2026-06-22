---
title: "Relativity Server SDK and API Packages Changes"
url: https://platform.relativity.com/Server2025/Content/What_s_new/Server_SDK_Changes.htm
collection: developer
fetched_at: 2026-06-22T06:29:16+00:00
sha256: e811cf51b1c154a096faca2775c02f1f88b4e90555c9325e078498da3edcafce
---

Relativity Server SDK and API Packages Changes Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Server SDK and API Packages Changes

Effective with the Relativity Server 2023 release, the NuGet packages required to extend core functionality and implement custom applications for Relativity Server are published and maintained separately from the SDKs hosted on the Relativity NuGet Gallery (nuget.org). The latest SDKs for Relativity Server will be hosted on a regional Relativity Server Artifactory Feed, while the Relativity NuGet Gallery will continue to host the RelativityOne packages. Separating the RelativityOne and Relativity Server packages provides for a more stable and reliable developer experience as each platform evolves.

The Relativity Server Artifactory Feed packages can be accessed from the following URLs:

- Use the URLs below to explore the available packages (these are effectively an equivalent to using nuget.org with a web browser to explore packages):

- United States: https://relativitypackageseastus.jfrog.io/ui/native/server-nuget-remote/

- Europe: https://relativitypackageswesteurope.jfrog.io/ui/native/server-nuget-remote/

- Use the URLs below when configuring a package manager (within Windows or Visual Studio, for example)

- United States: https://relativitypackageseastus.jfrog.io/artifactory/api/nuget/v3/server-nuget-virtual

- Europe: https://relativitypackageswesteurope.jfrog.io/artifactory/api/nuget/v3/server-nuget-virtual

- To guarantee that the correct packages are consumed it is strongly recommended to use the provided nuget.config file to set up Visual Studio 2022 with the appropriate package source URL.

You are not required to recompile your custom application against the Relativity Server Artifactory Feed-hosted packages for your application to work on Relativity Server 2025. However, we do recommend recompiling to consume the Relativity Server Artifactory Feed packages if it is a viable option, to ensure that your application is running against the latest Relativity Server SDKs. Moving forward, Relativity Server SDK packages will only be updated and enhanced on the Relativity Server Artifactory Feed sites. Custom applications compiled against the packages hosted on the NuGet Gallery may continue to work on future Relativity Server releases, but we recommend adopting the new Server packages as soon as possible, and strongly advise against updating any Server applications to consume new or updated versions of packages from nuget.org moving forward.

To ensure long-term compatibility, stability, and supportability of the Relativity Server platform, Relativity has recommended the use of Relativity Server SDKs and the Relativity Server Artifactory Feed for custom application development since Relativity Server 2023.

Beginning with Relativity Server 2026 GA, this guidance will be reinforced through support policy enforcement.

Relativity strongly recommends that all custom Relativity Server applications (RAPs) be built using Relativity’s supported Relativity Server Artifactory Feed packages and a new application building tool that Relativity intends to release in 2026.

While alternative build approaches will not be blocked for Server 2026, RAPs that are not built and validated using the supported building tool and Artifactory Feed will be considered unsupported. Accordingly, Relativity Support and Engineering will not provide troubleshooting assistance for issues related to third-party RAPs that:

- Are built against RelativityOne code paths

- Use custom or unmanaged dependency configurations

- Are compiled outside of Relativity’s supported building tool and Artifactory Feed

Any RAP deployed to Relativity Server without being built using Relativity’s supported application building tool and the Relativity Server Artifactory Feed will fall outside of Relativity’s support policy starting in Relativity Server 2026.

See the topic Relativity Server SDK and API Packages Changes for information on SDKs for Relativity Server 2025, and comparing the available SDKs from the Relativity Server Artifactory repository and the Relativity One repository at nuget.org.

Using RelativityOne packages in Relativity Server 2024/2025 is not recommended, and doing so is at your own risk.

## Server SDK Support Policy

While using the dedicated Server SDKs hosted in Artifactory is recommended for Server 2023, Server 2024 and Server 2025, it will be required and enforced starting with Server 2026. This section establishes the support policy and expectations for the Relativity Server SDK packages.

- Starting with Server 2023 Release, SDK packages will be published to new Server-specific, public Artifactory NuGet and NPM feeds

- relativitypackageseastus

- nuget

- npm

- relativitypackageswesteurope

- nuget

- npm

- No Server packages will be published to nuget.org

- Naming conventions

- All SDK package identifiers use the Relativity.Server.* prefix

- example: Relativity.Server.Agent.SDK

- Kepler-based SDK package identifiers append the .Interfaces.SDK suffix

- example: Relativity.Telemetry.MetricsCollection.Interface → Relativity.Server.Telemetry.MetricsCollection.Interface.SDK

- Library-based SDK package identifiers append the .SDK suffix

- example: Relativity.Server.Application.SDK

- Assembly filenames are not required to follow the package identifier, but are recommended for new SDKs

- example Relativity.Server.Agent.SDK continues to include kCura.Agent.dll

- Versioning

- SDK packages will continue using Semantic Versioning strategy

- To identify Relativity version compatibility, PackageTags are used.

- Compatibility

- This policy is limited to applications that build against SDK packages published to the new Artifactory public feed

- The SDK release is only guaranteed to be compatible with the current/next release + patches/hotfixes

- The policy is effective starting with Server 2023

- Breaking changes

- Any breaking changes are announced at least 90 days before next EA release

- Publishing cadence

- Pre-release SDK packages are published on or before EA release. Gold SDK packages are published on or before GA release

## Updating your application to use packages from Artifactory

This section outlines how you can start adopting the Relativity Server SDK packages hosted on Relativity Server Artifactory Feed. Advantages of compiling your Relativity Server custom application against the Antifactory packages include:

- Ensuring compatibility with the latest version of Relativity Server

- Enabling you to take advantage of Relativity Server SDK enhancements and fixes

### Custom applications that only target Relativity Server

For custom applications that only target Relativity Server we recommend updating your application to consume the packages hosted on the Relativity Server Artifactory Feed.

Follow these steps to compile your application against the Relativity Server SDK packages:

- Download the sample nuget.config from here (rename file to nuget.config after downloading). Refer to the Microsoft article on Package Source Mapping for more detail on using a nuget.config file.

- Copy the nuget.config file to your project repository root directory.

- Open your project or solution using Visual Studio 2022 or Rider.

- Update the versions used by your project with the latest versions available from the Relativity Server Artifactory Feed (this should also automatically restore them locally). In most cases, the package name will change, but the version will remain the same.

- Rebuild your project or solution.

- Commit your changes if the build was successful.

### Custom applications that target both Relativity Server and RelativityOne (multi-targeting)

Some customers choose to maintain a single version of a custom application for use in Relativity Server and RelativityOne. While we continue to accommodate this strategy, developers will need to update their projects in order to consume the separate Relativity Server and RelativityOne SDK packages.

Follow these steps to update your application to consume the separate Relativity Server and RelativityOne SDK packages:

- Update your build tools to Visual Studio 2022 to enable NuGet 6 source mapping feature ( this step is strongly recommended to guarantee that the correct packages are consumed ).

- Create separate branches for Relativity Server and RelativityOne.

- Switch to your Relativity Server branch.

- Download the nuget.config from here (rename file to nuget.config after downloading). Refer to the Microsoft article on Package Source Mapping for more detail on using a nuget.config file.

- Copy the nuget.config file to the project repository root directory.

- Open your project or solution using Visual Studio 2022 or Rider.

- Update the versions used by your project with the latest versions available from the Relativity Server Artifactory Feed (this should also automatically restore them locally).

- Rebuild your project or solution.

- Commit your changes if the build was successful.

## FAQ

I have a custom application that multi-targets Relativity Server and RelativityOne. Will it continue to work for Relativity Server 2023 if I do not recompile against the Relativity Server Artifactory Feed packages?

Electing to not compile against the Relativity Server Artifactory Feed packages will not in itself prevent a custom application from working on Relativity Server 2023. However, as the Relativity Server and RelativityOne platforms evolve, it is highly recommended that you adopt the new multi-targeting strategy detailed above to ensure compatibility across both platforms.

If I am not able to recompile my application against the new Server SDKs for Server 2023, which versions of the NuGet Gallery RelativityOne SDKs are supported for Server 2023?

You can find a list of supported RelativityOne SDKs for Server 2023 here .

Will Relativity ever institute a hard requirement to recompile custom applications using the Relativity Server Artifactory Feed packages for those applications to work in Relativity Server?

To ensure long-term platform compatibility, Relativity will eventually require Relativity Server custom applications to be compiled against the Relativity Server Artifactory Feed packages. We will communicate a more detailed migration plan and enforcement policy at a later date, and we will provide ample notice before instituting a hard requirement to adopt the Relativity Server Artifactory Feed. See Server SDK Support Policy .

If I compile my application against the Relativity Server Artifactory Feed packages, will it continue to work for older supported versions of Relativity Server?

The SDK packages that are initially published on the Relativity Server Artifactory Feed in September 2023 will work for older supported versions of Relativity Server. Relativity will provide advance notification before introducing any breaking changes that would impact package compatibility with any supported versions of Relativity Server.

Can I recompile my custom Relativity Server application against updated NuGet Gallery packages?

You are not prevented from recompiling a Relativity Server custom application against updated NuGet Gallery packages but Relativity cannot guarantee that breaking changes for Relativity Server have not been introduced, so it is strongly recommended that you avoid this action. If you ever plan to recompile a custom application for Relativity Server in the future you should do so using the Relativity Server Artifactory Feed packages.

I am using 3rd party libraries in my custom Relativity Server solution, and I am seeing missing package errors, what do I do?

Clear your local nuget caches using the Windows terminal with command dotnet nuget locals all --clear . Remove, or comment-out, the clear element from the nuget.config file, save it, and try to rebuild again. Your 3rd party packages should then be found, but be careful not to restore RelativityOne packages coming from nuget.org. Only use Relativity Server packages from the Relativity Server Artifactory Feed. The restore order must be Relativity Server packages first, followed by any others.

On this page

- Relativity Server SDK and API Packages Changes

- Server SDK Support Policy

- Updating your application to use packages from Artifactory

- Custom applications that only target Relativity Server

- Custom applications that target both Relativity Server and RelativityOne (multi-targeting)

- FAQ


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
