---
title: "Authentication procedures"
url: https://help.relativity.com/Server2025/Content/Relativity/Authentication/Authentication_procedures.htm
collection: user
fetched_at: 2026-06-22T06:03:51+00:00
sha256: 8c7fbb0b29032161d50fde409d690288850dd55e7fceb5551557361599164429
---

Authentication procedures

# Authentication procedures

The following procedures are used with the setup, installation, or use with authentication.

- Setting IP address range

- Configuring integrated authentication

- Sending Email

- RSA configuration

## Setting IP address range

You define an IP address or addresses as valid locations from which users can log in from in a combination of two settings.

The first uses the instance setting Relativity.Authentication WindowsAuthIpRange to define the valid range for the Relativity instance. The default defines all IP addresses as valid.

The second setting specifies a valid IP address or addresses for each user. This can be an individual address, a range of addresses, or combination of either. The specified range is called the Trusted IPs. Users outside of this range or ranges won't be able to login except by using Password authentication with the Two Factor Mode set to Outside Trusted IPs .

The settings (WindowsAuthIpRange and Trusted IP range) cannot be used to prevent users from logging in if they access Relativity from the same server where it is installed. To secure Relativity login from the server where it is installed, you must disable non-admin user remote access to the server.

To set the user Trusted IP range:

- Select the Users tab.

- Click the user's name.

- Click Edit .

- Enter the IP range in the Trusted IPs field. If you have multiple trusted IPs, enter each IP range on a new line.

Relativity only supports the IPV4 format for Trusted IP addresses. It doesn't support the IPV6 format.

- Click Save .

By default, no value is empty, which indicates any IP address is valid.

In case of setting either WindowsAuthIpRange or the user's Trusted IP range, you can specify an individual address, a range of addresses, or a combination of either, separate each one with a carriage return.

Addresses use the "###.###.###.###" format. The following wildcards are available for both settings:

Description Example

Asterisk (*)

(Asterisk wildcard)

Matches zero or more characters.

192.168.31. * . You can't use this notation with the match range of digits wildcard.

Hash (#)

(Hash wildcard)

Matches any single digit 0-9. 192.168.31. ## . You can't use this notation with the match range of digits wildcard.

[start-end]

(Match range of digits wildcard)

Matches a range of digits.

192.168.31. [0-255] . You can't use this notation with the asterisk and/or hash wildcards.

16-bit mask A 16-bit number that masks an IP address. 192.168.0.0/16 is the same as 192.168.0.0/255.255.0.0.

Network address range is 192.168.0.0-192.168.255.255.

24-bit mask A 24-bit number that masks an IP address. 192.168.31.0/24 is the same as 192.168.31.0/255.255.255.0.

Network address range is 192.168.31.0 - 192.168.31.255.

25-bit mask A 25-bit number that masks an IP address. 192.168.31.0/25 is the same as 192.168.31.0/255.255.255.128.

Network address range is 192.168.31.0 - 192.168.31.127.

## Configuring integrated authentication

Enabling a server to accept integrated authentication log ins must be configured explicitly. You use the UseWindowsAuthentication and WindowsAuthIpRange instance settings to define integrated authentication behavior. Integrated authentication follow these guidelines.

- If UseWindowsAuthentication is False , then integrated authentication can't be used. In this case, Relativity ignores the WindowsAuthIpRange value.

- If UseWindowsAuthentication is True and WindowsAuthIpRange isn't set, then integrated authentication will always be used regardless of IP address.

- If UseWindowsAuthentication is True and WindowsAuthIpRange is an IP address or address range, then Integrated Authentication is used when the computer’s IP address falls within the WindowsAuthIpRange value. If the IP address falls outside the WindowsAuthIpRange , the log in screen displays other assigned log in methods.

You can configure your environment so that some Web servers use Integrated Authentication, while others don't use it. To specify a server to use integrated authentication , create a new instance setting of UseWindowsAuthentication with the following values:

- Set MachineName to the web server name

- Set Value to True .

You must create a new UseWindowsAuthentication instance setting for each server

## Sending Email

Several authentication providers may send email, such as part of a two factor password authentication or a password reset. You will need an SMTP server. Contact your IT system admin for additional details. Use the following instance settings to define the emails addresses and body text.

- AuthenticationEmailFrom - sets the email address that appears in the From field of email messages that contain authentication information for users. For more information, see AuthenticationEmailFrom .

- EmailFrom - sets the email address populated in the "From" field when sending email notifications.

- ForgotPasswordRequestEmailFrom - sets the value in the From field for the forgotten password request email message.

## RSA configuration

Before you integrate RSA SecurID with Relativity, you must complete the following tasks:

- Make sure that your web server has a 64-bit version of the Windows operating system.

- Install Relativity, and verify that it is working properly.

- Set up the RSA Authentication Manager server. Server 2025 supports RSA Authentication Manager 8.1.

Relativity isn't certified to work with any version of RSA Authentication Agent for Web for Internet Information Services .

- Set up the Authentication agent on the RSA Authentication Manager server. You can add this agent through the RSA Security Console, where you must set the Agent Type field to Standard Agent . The RSA Authentication Manager server uses this setting to communicate with Relativity. For more information, see the documentation provided for your RSA Authentication Manager server.

You must add one agent for each web server in your Relativity environment. For example, if there are two web servers, set up two Authentication agents on the RSA Authentication Manager server.

## Copying RSA configuration files to the web server

You must copy the RSA configuration files to your Relativity web server before you configure RSA authentication in Relativity.

Use the following procedure to copy the required RSA configuration files:

- Open the RSA Security Console .

- Locate the sdconf.rec and sdopts.rec configuration files in the console.

- Download the sdconf.rec and sdopts.rec files to your machine.

- Log in to the Relativity web server.

- Copy these files to the RSAConfigFilePath directory. The following is the default path:

```text
%SYSTEMDRIVE%\Program Files\kCura Corporation\Relativity\EDDS\RSA
```

You can use a different location for your RSAConfigFilePath directory.

- Update the value of the RSAConfigFilePath instance setting in the EDDS database with the location where you copied the files in step 5. See Instance setting table .

The RSAConfigFilePath value must include the drive letter. For example,

```text
C:\Program Files\kCura Corporation\Relativity\EDDS\RSA
```

You cannot use the %SYSTEMDRIVE% environment variable.

- Verify that the DOMAIN\EDDSServiceAccount has Write permissions to the RSAConfigFilePath directory. The Relativity application pool runs under the DOMAIN\EDDSServiceAccount account.
