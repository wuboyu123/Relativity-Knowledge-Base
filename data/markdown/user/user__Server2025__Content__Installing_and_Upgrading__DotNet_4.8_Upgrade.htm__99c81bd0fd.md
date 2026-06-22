---
title: "Upgrading Relativity to .NET 4.8"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/DotNet_4.8_Upgrade.htm
collection: user
fetched_at: 2026-06-22T06:10:55+00:00
sha256: 8eeb1cf2aa9df1ab82f3d26fa7c65dbb988bd8e5ef0409fc8d487231f337d7a3
---

Upgrading Relativity to .NET 4.8

# Upgrading Relativity to .NET 4.8

This topic provides information related to upgrading your Relativity environment to .NET 4.8 or 4.8.1.

We recommend using .NET 4.8 or 4.8.1, even though .NET 4.7.2 is still supported and is the required minimum version.

Regardless of the version you use, updates must be applied to Relativity servers and client machines.

Existing custom applications are compatible with Server 2025 and do not need to be recompiled, but you must upgrade your development environment to use the latest versions of Relativity SDKs.

## All servers

Perform these steps on all servers in your Relativity environment:

- Download the .NET 4.8 or 4.8.1 installer from:

- https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48 for 4.8. The downloaded file name is ndp48-web.exe .

-

https://dotnet.microsoft.com/en-us/download/dotnet-framework/net481 for 4.8.1. The downloaded file name is ndp481-web.exe .

- Run the ndp48-web.exe or ndp481-web.exe executable and follow the instructions in the installation wizard.

- Turn off applications when prompted by the installation wizard.

- Restart the server on completion.

## Client machines

Perform these steps on all systems running Relativity and Invariant client applications, Relativity Desktop Client and Relativity Processing Console:

- If you do not have the Microsoft Visual C++ 2015 Redistributable already installed, download it from https://www.microsoft.com/en-us/download/details.aspx?id=53840. The download provides both 32- and 64-bit options. Select an executable depending on your system word size.

- Run the Microsoft Visual C++ 2015 Redistributable executable and follow the instructions in the installation wizard.

- Download the .NET 4.8 or 4.8.1 installer from https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48 or https://dotnet.microsoft.com/en-us/download/dotnet-framework/net481 .The downloaded file name is ndp48-web.exe or ndp481-web.exe .

- Run the ndp48-web.exe or ndp481-web.exe executable and follow the instructions in the installation wizard.

- Turn off applications when prompted by the installation wizard.

- Restart the machine on completion.

- Download and install the latest version of the RDC.

## Relativity applications

### Backward-compatible applications

Going forward, regardless of current Relativity version, if you install new .NET 4.8 or 4.8.1-based versions of backward-compatible Relativity applications, you must upgrade your environment to .NET 4.8 or 4.8.1 as described above.

Backward-compatible applications include Data Grid, ARM, Relativity User Import, etc.

### Custom applications built with the Relativity SDK

Custom applications that Relativity does not own or maintain can continue to target their current .NET version and will work in the new .NET 4.8 or 4.8.1-based Relativity. You can continue developing with older versions of the Relativity SDKs if you don't need the new features in latest version.

To develop using the latest Relativity SDK, you must update the applications' projects to target .NET 4.8 or 4.8.1. The developers must also update their environment to the .NET 4.8 or 4.8.1 Developer Pack as described below.

## Development environment

If you develop custom Relativity application, you must update your development environment to use the latest version of the SDK:

- Download the Microsoft .NET Framework Developer Pack from:

- https://dotnet.microsoft.com/en-us/download/dotnet-framework/thank-you/net48-developer-pack-offline-installer for 4.8. The file name is ndp48-devpack-enu.exe .

-

https://dotnet.microsoft.com/en-us/download/dotnet-framework/thank-you/net481-developer-pack-offline-installer for 4.8.1. The file name is ndp481-devpack-enu .

- Run the ndp48-devpack-enu.exe or ndp481-devpack-enu executable and follow the instructions in the installation wizard.

- Turn off applications when prompted by the installation wizard.

- Restart the machine on completion.
