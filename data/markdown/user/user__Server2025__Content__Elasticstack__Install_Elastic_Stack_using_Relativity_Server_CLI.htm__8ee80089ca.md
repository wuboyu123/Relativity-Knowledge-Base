---
title: "Install Elastic Stack using Relativity Server CLI"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Install_Elastic_Stack_using_Relativity_Server_CLI.htm
collection: user
fetched_at: 2026-06-22T06:11:04+00:00
sha256: de05a2af32b42acbb58c16c265d64c1d80c5a9ff52aa98395d92cf00aae27174
---

Install Elastic Stack using Relativity Server CLI

# Install Elastic Stack using Relativity Server CLI

## Install Elastic Stack using Relativity Server CLI

- Elasticsearch data and log directories must not be located on the OS drive (C:) or on temporary storage.

- Use dedicated, persistent, high-performance storage (SSD or NVMe).

- The Elasticsearch data disk must not be shared with the operating system.

- Before extracting any downloaded files on the target machine, see How to Unblock Downloaded Files .

Online - Install Elastic Stack using Relativity Server CLI (Single Node)

Use this option to install Elastic Stack on a single node using the Relativity Server CLI. Packages are downloaded directly from:

Copy

```text
https://artifacts.elastic.co/downloads

```

Installation Steps

Run all commands in an elevated PowerShell window using the relservice or admin account. To skip all interactive prompts, run a single non-interactive command:

Copy

```text
.\relsvr.exe install --elastic-stack-version "9.3.0" --elasticsearch-data-path "D:\elastic-data" --elasticsearch-logs-path "D:\elastic-logs"

```

Or follow the interactive prompts:

-

Open an elevated PowerShell window and run the following command:

Copy

```text
.\relsvr.exe install

```

-

When prompted, select Elastic Stack and confirm the Elastic Stack installation.

-

Select the Elastic Stack version from the list of supported versions.

-

When prompted with Use a custom Elastic package source? , enter n to download packages from the internet.

-

When prompted with Use custom storage paths for Elasticsearch data and logs? , enter y and provide the path, or n to use the defaults.

The installer creates the specified directories automatically if they do not already exist.

-

The installation proceeds automatically.

Sample interactive session Copy

```text
PS C:\elastic\Relativity.Server.Cli.102.0.3\tools> .\relsvr.exe install

Relativity Server CLI - 102.0.3

Copyright (c) 2025, Relativity ODA LLC

Install the Elastic Stack? [y/n] (y): y

The "Open and Free" Elasticsearch product can be installed to support features like

Datagrid/Audit and Environment Watch that search billions of unstructured JSON documents in seconds.

Selected Elastic Stack version: 8.19.8

Recommended distribution source path: \\{server}\BCPPath\EnvironmentWatch\ElasticPackages

Use a custom Elastic package source? [y/n] (n): n

Selected Elastic Stack components to install: Elasticsearch,Kibana,APM Server

Use custom storage paths for Elasticsearch data and logs? [y/n] (n): y

Enter the Elasticsearch data storage path (e.g. D:\elastic-data): (D:\elastic-data): D:\elastic-data

Enter the Elasticsearch logs storage path (e.g. D:\elastic-logs): (D:\elastic-logs): D:\elastic-logs

```

Offline - Install Elastic Stack using Relativity Server CLI (Single Node)

Use this option to install Elastic Stack on a single node in an air-gapped or offline environment using the Relativity Server CLI. Packages are read from a local directory or BCP network share instead of being downloaded from the internet.

Prerequisites

On a machine with internet access, download the required packages and organize them in the following directory structure before transferring to the target environment.

Download locations:

Package Download URL

Elasticsearch https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{version}-windows-x86_64.zip

Kibana https://artifacts.elastic.co/downloads/kibana/kibana-{version}-windows-x86_64.zip

APM Server https://artifacts.elastic.co/downloads/apm-server/apm-server-{version}-windows-x86_64.zip

mapper-size plugin https://artifacts.elastic.co/downloads/elasticsearch-plugins/mapper-size/mapper-size-{version}.zip

RWSM NuGet package https://relativitypackageseastus.jfrog.io/artifactory/api/nuget/server-nuget-virtual/Download/Relativity.Windows.ServiceManager/2.24.0

Example: Replace {version} with the target Elastic Stack version. For example, for version 9.3.0 :

Copy

```text
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-9.3.0-windows-x86_64.zip

https://artifacts.elastic.co/downloads/kibana/kibana-9.3.0-windows-x86_64.zip

https://artifacts.elastic.co/downloads/apm-server/apm-server-9.3.0-windows-x86_64.zip

https://artifacts.elastic.co/downloads/elasticsearch-plugins/mapper-size/mapper-size-9.3.0.zip

```

Required directory structure (example for Elastic Stack 8.19.8 and RWSM 2.24.0 ):

The folder names shown below are required, as the installation process relies on this structure.

Copy

```text
C:\elastic-packages\

─ elasticsearch\

│   ─ elasticsearch-8.19.8-windows-x86_64.zip

│   └── plugins\

│       └── mapper-size-8.19.8.zip

─ kibana\

│   └── kibana-8.19.8-windows-x86_64.zip

─ apm-server\

│   └── apm-server-8.19.8-windows-x86_64.zip

└── tools\

    └── relativity.windows.servicemanager.2.24.0.nupkg

```

Transfer the entire directory structure to the offline machine or a BCP network share accessible from the target machine.

Installation Steps

Run all commands in an elevated PowerShell window using the relservice or admin account. To skip all interactive prompts, run a single non-interactive command:

Copy

```text
# Using a local path

.\relsvr.exe install --elastic-stack-version "9.3.0" --distribution-source "C:\elastic-packages" --elasticsearch-data-path "D:\elastic-data" --elasticsearch-logs-path "D:\elastic-logs"

# Using a BCP network path

.\relsvr.exe install --elastic-stack-version "9.3.0" --distribution-source "\\fileserver\elastic-packages" --elasticsearch-data-path "D:\elastic-data" --elasticsearch-logs-path "D:\elastic-logs"

```

Or follow the interactive prompts:

-

Open an elevated PowerShell window and run the following command:

Copy

```text
.\relsvr.exe install

```

-

When prompted, select Elastic Stack for setup and confirm the Elastic Stack installation.

-

Select the Elastic Stack version from the list of supported versions. Verify that the selected version matches the version of the packages you downloaded.

-

When prompted with Use a custom Elastic package source? , enter y .

-

Provide the local path or BCP path to the folder containing the pre-downloaded packages.

-

When prompted with Use custom storage paths for Elasticsearch data and logs? , enter y and provide the path, or n to use the defaults.

-

The installation proceeds automatically.

Sample interactive session Copy

```text
PS C:\elastic\publish-cli> .\relsvr.exe install

Relativity Server CLI - 100.0.28

Copyright (c) 2025, Relativity ODA LLC

Install the Elastic Stack? [y/n] (y): y

The "Open and Free" Elasticsearch product can be installed to support features like

Datagrid/Audit and Environment Watch that search billions of unstructured JSON documents in seconds.

Selected Elastic Stack version: 8.19.8

Recommended distribution source path: \\{server}\BCPPath\EnvironmentWatch\ElasticPackages

Use a custom Elastic package source? [y/n] (n): y

Enter the distribution source path (e.g. \\{server}\BCPPath\EnvironmentWatch\ElasticPackages): (\\{server}\BCPPath\EnvironmentWatch\ElasticPackages): C:\elastic\packages

Distribution source: C:\elastic\packages

Selected Elastic Stack components to install: Elasticsearch,Kibana,APM Server

Use custom storage paths for Elasticsearch data and logs? [y/n] (n): y

Enter the Elasticsearch data storage path (e.g. D:\elastic-data): (D:\elastic-data): D:\elastic-data

Enter the Elasticsearch logs storage path (e.g. D:\elastic-logs): (D:\elastic-logs): D:\elastic-logs

```

Post Install Verification

After installation completes:

-

The auto-generated elastic superuser password is saved to:

Copy

```text
C:\elastic\secrets\elastic-user.txt

```

Record and securely store it immediately according to your organization's credential management policy.

-

Verify Elasticsearch is running by opening a browser and navigating to:

Copy

```text
https://host-name:9200

```

Log in with username elastic and the password from C:\elastic\secrets\elastic-user.txt . A successful response shows basic cluster information in JSON format.

-

Verify Kibana is running by opening a browser and navigating to:

Copy

```text
https://host-name:5601

```

Log in with username elastic and the password from C:\elastic\secrets\elastic-user.txt . A successful response loads the Kibana home dashboard.

-

Verify APM Server is running by opening a browser and navigating to:

Copy

```text
https://host-name:8200

```

A successful response returns a JSON object containing APM Server build information.

-

Once all services are verified and the password is securely stored, delete the password file from disk:

Copy

```text
Remove-Item -Path "C:\elastic\secrets\elastic-user.txt"

```

The password file contains the elastic superuser password in plain text. Delete it after you have securely stored the password according to your organization's credential management policy.
