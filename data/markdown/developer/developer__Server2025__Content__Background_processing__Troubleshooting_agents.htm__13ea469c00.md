---
title: "Troubleshoot agents"
url: https://platform.relativity.com/Server2025/Content/Background_processing/Troubleshooting_agents.htm
collection: developer
fetched_at: 2026-06-22T06:31:04+00:00
sha256: 544661de96a58def7df7e135bdcde2cadf2f45eaf986adf99f420d82a5ec45d1
---

Troubleshoot agents

# Troubleshoot agents

Use the following information to remotely debug agents and to identify the causes of agent errors.

## Remotely debug agents

Use these instructions to debug agents on a Relativity agent server from your workstation. The server and workstation must be running on the same network.

- Configure remote debugging on the Relativity agent server. See How to: Set Up Remote Debugging on MSDN.

- On the agent server, right-click on the Remote Debugging Monitor ( msvmon ) icon and select Run as administrator . The msvmon icon was added to your desktop when you completed the remote debugging setup in step 1.

The Remote Debugging Monitor displays a message containing the name of the server and the port that you use for the connection. It uses the format: <servername>:<port> . In step 6, enter this information in the Qualifier box.

- Locate the Symbol files (.pdb) in the bin or other folder in your project, and upload them on the Resource Files tab. See Resource files on the Relativity Documentation site.

- In Relativity, add the assemblies associated with the .pdb files from step 3 to the Resource Files tab. After you complete this step, the agents cycle to create a new folder with the copied .pdb files and the agent assembly.

- On your workstation, open your agent project in Visual Studio.

- Attach the debugger to the kCuraAgentManager.exe process:

- Click Tools and then click Attach to Process .

- Enter <servername>:<port> in the Qualifier box. By default, the port is 4016. The system prompts you for the Windows credentials of an admin on the server, if you aren't one.

- Select the kCuraAgentManager.exe process.

- Click Attach .

- On the Relativity server, check the status of the Remote Debugging Monitor in Visual Studio. It should indicate that you are connected.

- After you finish debugging, delete the .pdb files from the Resource Files tab in Relativity.

## Check event logs for errors

If your agent fails to run, check the Windows event log on the agent server for errors. The Windows event log records Failed to load errors, which you can resolve by editing the agent.

Use the following steps to resolve these errors:

- Open Relativity.

- Click the Agents tab to display the list view.

- Click on the name of the agent with the error.

- On the detail view, click Edit and then Save .

- On the Agents tab, click Restart Disabled Agents .
