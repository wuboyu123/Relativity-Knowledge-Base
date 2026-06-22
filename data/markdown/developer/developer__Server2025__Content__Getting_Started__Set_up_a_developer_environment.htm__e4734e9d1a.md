---
title: "Set up a developer environment"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Set_up_a_developer_environment.htm
collection: developer
fetched_at: 2026-06-22T06:21:59+00:00
sha256: 201c7dba839f4313d714b7773c5060a4accbc5a8fdf2de6a0ac6637dcd1a9d45
---

Set up a developer environment

# Set up a developer environment

Use the steps in the following sections to set up your developer environment using a DevVM. Plan the following time for completing these tasks:

- Setup time for Community accounts, which may take at least 1-2 business days for the approval process. You need to complete this process to download your DevVM.

- Download time for a DevVM depends on the speed of your internet connection.

- Setup time for Hyper-V is 30 minutes.

## System requirements for the Host machine for Hyper-V

Your DevVM will be running as a Hyper-V virtual machine. The Hyper-V host machine (the machine that Hyper-V is running on) must meet the minimum requirements listed below.

Minimum configuration Recommended configuration

Operating system

Windows 10/11 or Windows Server 2016 with Hyper-V Version 6.2 or above

Storage space 140 GB free 256 GB free

Processing cores 8 12

RAM 32 GB 64 GB

Relativity version 12.3.857.3

Visual Studio 2022

## Step 1 - Install the Relativity Visual Studio templates

At time of writing (September 2024), Relativity Server 2023 (and later) templates are available from the open source server-relativity-templates GitHub repository. Please see the README file in the repository for instructions on how to install and use the templates. We intend to add the Relativity Server 2023 (and later) templates to the Visual Studio Marketplace in the near future.

Use these steps to install the Relativity templates through Visual Studio:

- Open Visual Studio.

- Click Extensions > Manage Extensions in the menu bar.

- In the Manage Extensions dialog, complete these steps:

- Click Online in the left pane, if it isn't selected.

- Enter Relativity Templates in the search bar on the right pane.

- Click Download on the matching extension.

- Close Visual Studio. The VSIX installer automatically opens.

- Complete the steps in the VSIX installer to install the templates.

## Step 2 - Set up Relativity Community and DevHelp accounts

Begin your Relativity development experience by setting up the following accounts:

- Relativity Developer Community - set up a Community account to interact with the Relativity Developer community.

You can also download a DevVM through the Relativity Developer Community.

- Relativity DevHelp Community - set up an account to ask questions, obtain suggestions from other Relativity Developers, and stay updated about Relativity news.

Use the following steps to create your accounts:

- Create a Relativity Developer Community account by completing these steps:

- Fill out the Relativity Developer Community account form.

- Click the password change link and set your password.

- Log in to the Relativity Community portal.

- Click Groups in the navigation bar to join the Relativity Developer Group.

- Click Relativity Developer Group .

- Click + Join Group to be added to the group.

After your Relativity Developer Community account is approved, you can use the Relativity DevHelp Community and download a DevVM. Allow at least 1-2 business days for the approval process.

- Create a Relativity DevHelp Community account by completing these steps:

- Go to the Relativity DevHelp Community page.

- Click Sign Up to create a new account.

- Complete the create account form.

Be sure to enter the same email address in form as you used when creating your Relativity Developer Community account.

## Step 3 - Download a DevVM

After your Relativity Community account is approved, you can download a DevVM.

A DevVM is approximately 40 GB. The amount of time to download a DevVM varies by the speed of your internet connection.

Use the following steps to download a DevVM:

- Log in to the Relativity Community .

- Search for a knowledge base article for a recent DevVM version using the format: DevVM - <version number> .

For example, you enter DevVM - 12.3.857.3 .

- Locate the Download Files section at the bottom of page.

- Click the link to download DevVM.

- Set up the DevVM using the steps in Set up the DevVM in Hyper-V .

## Step 4 - Set up the DevVM in Hyper-V

You need to set up your DevVM in Hyper-V because it uses this software to run the Relativity instance.

Use the following steps to set up your DevVM:

- Complete these steps to verify that Hyper-V is installed on your local machine:

- Navigate to Programs and Features .

- Click Turn Windows features on or off .

- Verify that the Hyper-V checkbox is selected as illustrated in the following screen shot. If necessary, add this feature. (The image below reflects the Windows 10 version of this dialog)

- Click OK .

- Extract the contents of the zip file downloaded from the Relativity Community.

See Download a DevVM .

- Copy the RelativityDevVm folder to the C: drive on your machine.

- Open the Hyper-V Manager application.

- Select your local machine under Hyper-V Manager in the tree.

- In the Actions pane, click Virtual Switch Manager .

- Complete these steps if you don't have a internal network switch:

- Click New Virtual Network Switch under Virtual Switches.

- Select Internal for the switch type.

- Click Create Virtual Switch .

- Enter a friendly name, such as RelativityDevVmSwitch .

- Click Apply .

- If a warning message appears, click Yes .

- Click OK to create a new virtual switch.

- Import the VM by clicking Import Virtual Machine in the Hyper-V Manager.

- Click Next .

- Click Locate Folder .

- Click Browse to locate the RelativityDevVm folder.

- Click Select Folder .

- Click Next .

- On the Select Virtual Machine window, verify that the Hyper-V VM is displayed, and click Next . (If you don't see your machine listed, see Create a VM from the Virtual Disk below.)

- On the Choose Import Type window, select Register the virtual machine in-place , and use the existing unique ID. In Connect Network section, a warning may appear if the DevVM requires a different virtual switch. Choose a valid virtual switch from the Connection drop-down list.

- Click Next .

- Click Finish to import the new Hyper-V VM. You should now see the imported VM in the Virtual Machines section.

- Right-click VM instance and then click Start .

After you start your DevVM, it may take several minutes for all the services to begin running.

Create a VM from the Virtual Disk

- In the Action menu, pick Action > New > Virtual Machine

- For Specify Name and Location , enter a name with no spaces (to simplify access using tools like SSMS).

- For Specify Generation , select Generation 1

- In Assign Memory , enter a value that is compatible with the amount of memory on your machine. 20,000MB is recommended

- In Configure Networking , select the virtual switch you created

- In Connect Virtual Hard Disk , enter the location of the saved .vhdx file

## Step 5 - Obtain your credentials and Relativity license

Complete these tasks to obtain your credentials and Relativity license:

### Credentials for a DevVM

Obtain the credentials for a DevVM on the Relativity Community site at Where can I access DevVM Credentials? You use these credentials to interact with various features of the DevVM.

### Relativity license

When you initially log in to the Relativity instance on your DevVM, you are prompted enter a license key. See Connect to a Relativity instance on a DevVM .

Contact Relativity Support to request a license key for your DevVM:

- Select Relativity Server as the Product and Other for the Instance and Topic fields, and Service Request as the nature of your request. In the ticket description, indicate that you are requesting a license for a Relativity instance on a DevVM.

- Copy the key displayed when you first attempt to log in to Relativity and attach the request key to the support ticket as a text file. The following screen shot illustrates how this key is displayed:

If you can't log in to your Relativity instance, make sure that the kCura Service Host Manager service is running within the DevVM. See the following screen shot.

The kCura EDDS services may not be running yet, this is because you need a valid Relativity license to start those services. After you have updated the license key with the key provided by Relativity support, return to service manager and start the two kCura EDDS services.

## Additional information about DevVMs

Review the following information to simplify working with your DevVM.

### Saving versus stopping your DevVM

Save your DevVM instead of shutting it down. This action puts the DevVM in a hibernated state. When starting the DevVM after saving it, you won't have to start the services again, because the state of your DevVM is preserved. It also reduces the time necessary to set up the DevVM when you restart it. To save your DevVM, right-click on the DevVM in the Hyper-V Manager and click Save .

### Connect to a Relativity instance on a DevVM

Use the following steps to connect to the Relativity instance on your DevVM:

- Locate the IP address for your DevVM in the Hyper-V Manager.

- Replace 9.9.9.9 in the following URL with the IP address from your machine.

You can then use this URL to connect to your Relativity instance in the web browser.

Copy

```text
1
http://9.9.9.9/Relativity
```

- Obtain your credentials for logging in to your Relativity instance from the Relativity Community. For more information, see Credentials for a DevVM .

### Select a network profile type

When you connect to a new network on a Windows Server VM, Windows prompts you to select a network profile type (network location): Public or Private . This will happen the first time you remote into your new DevVM. This is part of the Windows Defender Firewall with Advanced Security and allows you to apply different firewall rules depending on the type of network your computer is connected to. We recommend that when prompted, you choose Public .

See the following resources for more information:

- https://learn.microsoft.com/en-us/powershell/module/netconnection/set-netconnectionprofile?view=windowsserver2019-ps

- https://woshub.com/how-to-change-a-network-type-from-public-to-private-in-windows/

### Update resources for a DevVM

Even though you can adjust the system resources, we don't recommend using these environments for performance testing, gathering metrics, or other similar purposes.

Use the following steps to update the resources for a DevVM:

- Shutdown the DevVM.

- In the Hyper-V Manager, right-click on the DevVM and click Settings .

- Increase the number of processor cores by clicking the Processor link in the Hardware section, and enter a value in the Number of virtual processors field.

- Increase the RAM by clicking the Memory link in the Hardware section and enter a value in the RAM field.

-

Click Apply > OK after configuring the VM hardware.

### Windows licensing

A DevVM has a Windows license for up to 180 days. If you continue using the DevVM beyond this timeframe, you must extend the evaluation license , or activate a Windows license on the machine. According to the Windows Server 2019 page , you can extend the license for up to 3 years.

Use these steps to activate a license:

- Start your DevVM and log in to it with your credentials. See Step 5 - Obtain your credentials and Relativity license .

- Click on the taskbar in your DevVM to run PowerShell as an administrator.

- Run the following command: Copy

```text
1
DISM /online /Set-Edition:ServerStandard /ProductKey:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX /AcceptEula
```

Add your Windows Server 2019 license key to the command by replacing the placeholder value in the ProductKey field.

You must obtain your own Windows Server 2019 license key. See this Microsoft page for more information on upgrading license keys.
