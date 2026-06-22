---
title: "Configuring Windows server"
url: https://help.relativity.com/Server2025/Content/System_Guides/Environment_Optimization_Guide/Configuring_the_Windows_server.htm
collection: user
fetched_at: 2026-06-22T06:17:52+00:00
sha256: a7a43d7198eff12048b283e59f36eae6db2b7023ddd7f0f2c1c577a5a0d337e2
---

Configuring Windows server Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Configuring Windows server

Use the following guidelines to configure your Windows Server for optimum performance with Relativity. Some of these configuration options are one-time settings, while others require intermittent updating as your hardware or database sizes change.

These guidelines are applicable to all SQL Servers in the environment, including the Worker Manager SQL Server and the workers.

## Microsoft Windows server service packs

Install the latest Microsoft Windows Server Service Pack on all Relativity servers.

However, compatibility for higher .NET versions is not guaranteed. We do not recommend installing higher .NET versions than what is listed as required by your Relativity version. Furthermore, install any smaller security patches, Windows updates, and anything else at your own discretion. We only test major service packs, not every Microsoft update. Deploy any patches to your test instance of Relativity first. Ensure that a rollback plan is in place if you discover any issues during deployment.

Ensure you disable the option to Install updates automatically on all Relativity servers. Apply any required updates during a planned maintenance window.

## Windows visual effects

Windows includes standard visual effects to make the user experience more enjoyable. These effects aren't required and consume CPU resources. We recommend disabling these effects on all Relativity servers.

- Select the Performance Options dialog by clicking Settings in the Performance panel.

- Select the Visual Effects tab in the Performance Options dialog.

- Select the Adjust for best performance option, and then click OK .

## Windows processor scheduling

Application performance is related to processor scheduling caching options that you set for Windows Server. Processor scheduling determines the responsiveness of applications you run interactively (as opposed to background applications that may be running on the system as services). We recommend that you select background services on all Relativity servers.

- Select Settings in the Performance panel.

- Select the Advanced tab in the Performance Options dialog.

- In the Processor Scheduling panel, you have the following options:

- Programs - give the active application the best response time and the greatest share of available resources. Use this option only on development servers.

- Background Services - give background applications a better response time than the active application. Use this option for production servers.

- Select Background Services , and then click OK .

## Windows NTFS fragmentation

Install an automatic disk defragmentation tool on all Relativity Web, SQL, Search, and File servers. There are a number of tools available to defragment your hard drives and optimize performance.

- Some of the latest products are proactive and prevent much of the fragmentation from ever occurring. Research the available tools to decide which is best for you. Unlike the available Windows task to defragment your physical disks, these tools work automatically in the background. These tools use only idle resources to ensure nothing is negatively impacted. Most current SAN and NAS devices include technologies to avoid or limit fragmentation on the block level. Windows sees the data logically from the software level, outside of the storage realm. If Windows detects a file in hundreds of pieces, SAN performance may be affected.

Work with your storage vendor to see if they recommend installing a defragmenting tool.

- If you don't virtualize the Relativity roles, there will likely be a mirrored array housing the OS and required Relativity components (unless you’re also booting from the storage device). If these disks are heavily fragmented, roles including the web servers (IIS) may experience poor performance. This can impact Review.

## Configuring virtual memory

RAM is a limited resource, whereas virtual memory is, for most practical purposes, unlimited. There can be many processes, each one having its own 2 GB of private virtual address space. When the memory that's in use by all existing processes exceeds the amount of available RAM, the operating system moves pages (4 KB pieces) of one or more virtual address spaces to the hard disk. This frees that RAM frame for other uses. Windows stores these "paged out" pages in one or more files. The name of the file is pagefile.sys. You can find this file in the root of a partition. One pagefile.sys file can exist in each disk partition.

You can configure the location and size of the page file in the Control Panel. To set these values, click System > Advanced system settings , and then click Settings under Performance.

By default, Windows Server puts the paging file on the boot partition where the operating system is installed. Windows Server creates a default size of the paging file that is 1.5 times the physical RAM, up to a maximum of 4095 MB.

Consider the following:

- For all Relativity servers, manually set the size of the paging file to 4095 MB. We recommend the size of the paging file since OS volume has only enough room for requirements. OS volume can't support a page file size of 1.5 times the amount of physical RAM.

- For servers with a large amount of RAM installed (16GB+) and more than just the OS volume, create a second page file. Place this page file onto a drive other than the one housing the OS. Set this second page file to a size of 1.5 times the amount of physical RAM. This should be no greater than 50 GB. Microsoft has no specific recommendations about performance gains for page files larger than 50 GB. An example of this server type might include the Analytics server.

- SQL Server shouldn’t use the page file for memory on correctly configured servers. There should be no need to create a second page file on the SQL Server. SQL Server memory configurations are detailed in the SQL Server setup section of this guide.

Manually setting the size of the paging file provides better performance than the server automatically sizing it. It's a best practice to set the initial minimum and maximum size settings for the paging file to the same value. This ensures no processing resources are lost to the dynamic resizing of the paging file. This is especially true given that this resizing activity typically occurs when the memory resources on the system are already constrained. Setting the same minimum and maximum page file size values also ensure the paging area on a disk is one single, contiguous area. This improves disk seek time.

Microsoft recommends isolating the paging file onto one or more dedicated physical drives. Configure these drives as either RAID-0 (striping) or RAID-1 (mirroring) arrays. Or the paging file should be on single disks without RAID. Redundancy is not normally required for the paging file. Don't configure the paging file on a RAID 5 array. It's not recommended to configure the paging file on a RAID 5. This is because paging file activity is write-intensive and RAID 5 arrays are better suited for read performance than write performance.

## Antivirus directory exclusion list

Configure all antivirus software on any of your Relativity servers to exclude the following areas:

- SQL Servers - all directory values are located in the EDDS database Instance Setting table (excluding the Relativity Program Files and the BCPPath). Relativity is installed in the following location: C:\Program Files\kCura Corporation\Relativity. Adjust the drive location if necessary.

- Directory where the Database files are located.

- Directory where the Log files are located.

- The location of the BCPPath on the SQL Server.

- Directory where the Full Text Indexes are located

- Agent servers

Keep in mind your environment may differ slightly.

- Default: C:\Program Files\kCura Corporation\Relativity

-

C:\Windows\System32\config\systemprofile\AppData\Local\Relativity\TempStorage

- C:\Users\Rel_SVC\AppData\Local\Relativity\TempStorage

- Account running the agent service = Rel_SVC

- Web servers

Keep in mind your environment may differ slightly.

- Default: C:\Program Files\kCura Corporation\Relativity

-

C:\Windows\System32\config\systemprofile\AppData\Local\Relativity\TempStorage

- C:\Users\Rel_SVC\AppData\Local\Relativity\TempStorage

- Account running the agent service = Rel_SVC

- Worker servers

- C:\Program Files\kCura Corporation

- C:\Windows\System32 (\Invariant.hook.dll)

- C:\Windows\SysWOW64 (\Invariant.hook.dll)

- C:\Windows\System32\Tasks\Invariant\Relativity Processing Launcher

- Optional:

- C:\Users\Rel_SVC\AppData\Local\Relativity\TempStorage

-

C:\Windows\System32\config\systemprofile\AppData\Local\Relativity\TempStorage

We recommend that you scan any raw data for malware before introducing it into your Relativity environment. If you perform a scan, you may be comfortable excluding the Temp directories on your worker servers from your antivirus scans as well. This results in better performance and fewer interruptions due to live scans on the temp files that Relativity Processing (Invariant) creates in these directories. Unscanned raw data has potential to introduce harmful files into your environment.

- Analytics indexes - locate a folder named Content Analyst or CAAT; this is the installation directory. The index directory, if different, should also be excluded from Anti-Virus.

- Data Grid Data location - if Elasticsearch is installed, locate this in the Data Grid data node YML file.

- Elasticsearch service - \RelativityDataGrid\elasticsearch-main\bin\elasticsearch-service-x64.exe

- File repositories - any file directory that Relativity uses as a file share.

-

ARM archive locations - directory where the ARM archive locations are located.

-

Cache locations - directory where servers temporarily store converted copies of natives, images, productions, and other file types.

- RabbitMQ - directory where RabbitMQ is located. For recommendations, see RabbitMQ Windows Configuration .

## Management server

Whenever possible, avoid logging in to a production server using remote desktop. Instead, use a management or utility server. This server or virtual machine should have SQL Server Management Studio (SSMS) and the Relativity Desktop Client installed. Use this server to connect to the SQL instances to adjust maintenance plans and query tables. If you have an external hard drive containing data that you want to import into Relativity, connect it to this server and launch the Desktop Client on it to perform the data imports or export.

We also recommend that you install the Marvel cluster to the management server. Use this cluster to monitor and report on the performance and usage of the Data Grid Cluster. The Marvel cluster saves the daily indexes to its own data node. Carefully monitor the drive space used by these indexes so that the drive doesn't run out of space.

When administrators log directly into a production server, navigate and open applications, memory is consumed and processes are wasting CPU cycles. System admins should avoid dragging and dropping files via RDP from the console as this action is cached and may result in no free memory being available to the operating system.

On this page

- Configuring Windows server

- Microsoft Windows server service packs

- Windows visual effects

- Windows processor scheduling

- Windows NTFS fragmentation

- Configuring virtual memory

- Antivirus directory exclusion list

- Management server


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
