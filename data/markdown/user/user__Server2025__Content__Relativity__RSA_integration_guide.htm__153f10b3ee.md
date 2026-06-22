---
title: "RSA integration guide"
url: https://help.relativity.com/Server2025/Content/Relativity/RSA_integration_guide.htm
collection: user
fetched_at: 2026-06-22T06:17:46+00:00
sha256: 3cbe35995f3718831ff32e5a7439747fe67d93a4325bf8db56312d40cc352825
---

RSA integration guide Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# RSA integration guide

Relativity provides you with the option to configure RSA authentication for users. You can use the RSA SecurID, which requires that users enter a username and RSA passcode, such as a PIN, followed by a token code. When the Relativity users provide this information, RSA gives them access to the system. The Relativity login page serves as a repository for RSA credentials, so no additional RSA dialogs are required.

## System requirements

Before you integrate RSA SecurID with Relativity, you must complete the following tasks:

- Make sure that your web server has a 64-bit version of the Windows operating system.

- Install Relativity, and verify that it is working properly.

- Set up the RSA Authentication Manager server. Server 2025 supports RSA Authentication Manager 8.1.

Relativity isn't certified to work with any version of RSA Authentication Agent for Web for Internet Information Services .

- Set up the Authentication agent on the RSA Authentication Manager server. You can add this agent through the RSA Security Console, where you must set the Agent Type field to Standard Agent . The RSA Authentication Manager server uses this setting to communicate with Relativity. For more information, see the documentation provided for your RSA Authentication Manager server.

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

## Configuring Relativity user information with RSA

Within Relativity, you configure RSA authentication at the user level. Make sure that you have copied the required configuration files to the Relativity web server before you begin. See RSA integration guide .

Use the following procedure to configure a user for RSA authentication:

- Log in to Relativity with system admin credentials.

- Select Home from the user drop-down menu.

- Click the Users tab.

- Click the Edit link next to an existing username, or create a new user. See Creating and editing a user .

-

In the Login Method section, click New to open the Login Method Information form.

- Select the RSA Provider for your system.

- In the RSA Subject field, enter < RSA login name > or <email address> . Replace < RSA login name > with the default RSA login name for the user.

- If the RSA login name for the user is jsmith , then you would enter jsmith in the in the RSA Subject field. This setting now indicates that the user must be authenticated with RSA SecurID using the RSA login of jsmith , as well as with any tokens associated with this user.

- If the RSA login is an email address, then enter the email address in the RSA Subject field.

- Click Save .

The user can now use RSA authentication to log in to Relativity.

## Logging in to Relativity with RSA credentials

If your Relativity user information is configured with RSA, you can log in with the following credentials:

- A valid Relativity account username, which is an email address.

- An RSA passcode, which is a PIN, followed by an RSA token code.

If you are logging in with RSA authentication, don't enter a Relativity password in the Password field. This action results in an Invalid Credentials message.

Enter your email address and password on the Relativity login dialog.

After you log in, Relativity displays RSA related prompts determined by the state of your token. For example, you may see these additional dialogs:

- User-defined new pin:

- Login dialog displayed after you change the pin:

- System-generated new pin:

- Next tokencode:

On this page

- RSA integration guide

- System requirements

- Copying RSA configuration files to the web server

- Configuring Relativity user information with RSA

- Logging in to Relativity with RSA credentials


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
