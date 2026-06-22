---
title: "Uninstalling Relativity"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Uninstalling_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:10:54+00:00
sha256: 212a0a39067a9b8ac6e2826263748bc3a8f56d9ceb68d1680ff880e09fb21da7
---

Uninstalling Relativity

# Uninstalling Relativity

Use the following steps to uninstall Relativity:

- Navigate to the Windows Control Panel .

- Click Uninstall a program under the Programs section.

- Right-click on Relativity and click Uninstall .

You can also use the following script in the command prompt to uninstall Relativity:

```text
start /wait "" "GOLD 13.1.XXX.X Relativity.exe" /uninstall /log UninstallLog.txt
```

Uninstalling Relativity automatically removes following components (if present):

- Relativity Agent —Relativity.Installer.Agent.msi

- Relativity Distributed Database —Relativity.Installer.DistributedDatabase.msi

- Relativity Primary Database —Relativity.Installer.PrimaryDatabase.msi

- Relativity Procuro —Relativity.Installer.Procuro.msi

- Relativity Web —Relativity.Installer.Web.msi
