---
title: "Troubleshoot event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Troubleshooting_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:43+00:00
sha256: 167d00707da858ffba5e70afaf42c887cf17c23a3530c95575a1924cc302109b
---

Troubleshoot event handlers

# Troubleshoot event handlers

Use these instructions to debug event handlers on a Relativity web server from your workstation:

- Configure remote debugging on the Relativity web server. See How to: Set Up Remote Debugging on MSDN.

- On the web server, right-click on the Remote Debugging Monitor ( msvmon ) icon. Select Run as administrator . The msvmon icon was added to your desktop when you completed the remote debugging setup in step 1.

The Remote Debugging Monitor displays a message containing the name of the server and the port that you use for the connection. It uses the format: <servername>:<port> . In step 6, enter this information in the Qualifier box.

- In Relativity, upload a copy of your event handler .dll through the Resource Files tab. See Resource files on the Relativity Server 2025 Documentation site.

- Locate the Symbol files (.pdb) in the bin or other folder in your project, and upload them on the Resource Files tab as described in step 3.

- On your workstation, open your event handler project in Visual Studio.

- Attach the debugger to the w3wp.exe processes:

- Click Debug and then click Attach to Process .

- Enter <servername>:<port> in the Qualifier box. By default, the port is 4016. The system prompts you for the Windows credentials of an admin on the server, if you aren't one.

- Select the w3wp.exe processes in the Available Processes box.

- Click Attach .

- On the Relativity server, check the status of the Remote Debugging Monitor in Visual Studio. It should indicate that you are connected.

- After you finish debugging, delete the the .pdb files from the Resource Files tab in Relativity.
