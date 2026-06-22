---
title: "Create a nuget.config file"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Create_nuget_config_file.htm
collection: developer
fetched_at: 2026-06-22T06:29:42+00:00
sha256: f0df7cba4eb5ed0d16ae611b6134006460ba7a8d7b5d16b0010ac84be026ddce
---

Create a nuget.config file

# Create a nuget.config file

Starting with Server 2023, Relativity Server nuget packages are maintained separately from RelativityOne nuget packages that are hosted on nuget.org. Relativity Server nuget packages are available through Artifactory, at the following URLs:

- https://relativitypackageseastus.jfrog.io

- https://relativitypackageswesteurope.jfrog.io

## Why create a nuget.config file?

Starting with Visual Studio 2022, you can create a nuget.config file which specifies the nuget source which your projects will use. This file makes it easier for developers to switch between projects that use different nuget sources. This feature of Visual Studio 2022 is called "package source mapping", and you can learn more about it at the following Microsoft pages: Package Source Mapping and Common NuGet configurations .

By adding a nuget.config file, you can switch your solution between the RelativityOne nuget.org repository and the Relativity Server Artifactory nuget repository more easily, allowing you to target your code to RelativityOne packages or Relativity Server packages by adjusting the nuget.config file.

Package Source Mapping also requires NuGet 6. For this reason, Visual Studio 2022 comes with NuGet 6 built in. To see that Visual Studio 2022 is using NuGet 6, you can run this command, in either cmd or powershell

Copy

```text
dotnet nuget --version
```

## Create a nuget.config file

You can add a nuget.config file at the root of the repository, but it can also be in the folder which contains the .sln file, or in any folder that is a parent or ancestor to the .sln file. Below is a sample of a nuget.config file:

Copy

nuget.config example

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
<?xml version="1.0" encoding="utf-8"?>

<configuration>

    <config>

        <add key="globalPackagesFolder" value="%userprofile%\.nuget\packages-server" />

    </config>

    <packageSources>

        <clear />

        <add key="NuGet.org" value="https://api.nuget.org/v3/index.json"/>

        <!-- Use only one of the following public feeds depending on your geographic region. -->

        <add key="ServerArtifactoryNuGet" value="https://relativitypackageseastus.jfrog.io/artifactory/api/nuget/v3/server-nuget-virtual" />

        <!-- <add key="ServerArtifactoryNuGet" value="https://relativitypackageswesteurope.jfrog.io/artifactory/api/nuget/v3/server-nuget-virtual" /> /-->

    </packageSources>

    <packageSourceMapping>

        <!-- ServerArtifactoryNuGet is the preferred source because it has a more specific pattern.

             NuGet.org is a fallback for other packages such as NUnit. -->

        <packageSource key="ServerArtifactoryNuGet">

            <package pattern="Relativity.Server.*" />

        </packageSource>

        <packageSource key="NuGet.org">

            <package pattern="*" />

        </packageSource>

    </packageSourceMapping>

</configuration>
```

If package source mapping is used, each requested package in a project must match at least one defined pattern.
