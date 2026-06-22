---
title: "Logging into Relativity"
url: https://help.relativity.com/Server2025/Content/Relativity/Authentication/Logging_in_to_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:12:08+00:00
sha256: d46de15a85c8b5cbb41d1e120a62a9e45fcaf89dd4ab70e161fde6f8ff6b569c
---

Logging into Relativity Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Logging into Relativity

Relativity offers several ways to log in and it is possible to have two or more methods available to you. As a Relativity user, your system admin provides you with all the information you need to log in.

## Logging in to Relativity with a password

- Enter your Username .

- Click Continue .

- Enter your password.

- Click Login .

The Forgot your password? link only displays if the admin enables Allow Password Recovery via Email setting, for more information see Authentication .

## Password

This method uses only a user name and a password. Your system admin provides you with the following:

- Login email address.

- Password request email.

Prior to logging in, if you have not already, create your password. See Creating or resetting a password .

To log in:

- Navigate to the Relativity site.

- Log in with your password. See Logging in to Relativity with a password

## Two-factor authentication

The two-factor authentication method requires a passcode in addition to the user name and password. The system emails you the passcode during login and is different each time. Your system admin provides you with the following:

- Login email address.

- Password request email.

Prior to logging in, if you have not already, create your password. See Creating or resetting a password .

Prior to logging in, if you have not already, download the required two-factor authentication app. When using the authenticator app for the first time, Relativity will need to connect your profile to the app.

When using email for two-factor authentication, your web servers must have access to the SMTP server so it can distribute emails and passwords to authenticate.

To connect your authentication app,

-

Enter your user name.

-

Enter your password.

-

On the Two-Step Verification Required step, click Continue .

-

Open your authenticator app on your device.

-

In your app, tap the button to add a new account.

-

Hold phone up and scan the QR code provided by Relativity.

If you are unable to scan the QR code, click the Can't scan QR code? link below the QR code. Once clicked, a code will appear. Enter the code into your authenticator app on your phone. Once entered into the authenticator app, you can continue to the next step.

-

Click Next .

-

Re-enter your email and password.

-

Enter the authentication code in the app.

-

Click Next .

-

Click Done .

To log in with an authenticator app method:

- Navigate to the Relativity site.

- Log in with your password.

- Follow the instructions on the app or enter the authentication code from the authentication app.

- Click Next .

To log in with the Relativity email method:

- Navigate to the Relativity site.

- Log in with your password. An Authenticate Login dialog appears. The system immediately emails you a passcode, and the passcode will be different each time.

- Enter that value in Passcode .

- Click Login .

## Active Directory

This method uses Microsoft Active Directory Domain Services to log in. You must log in from a computer within a valid domain. Your system admin provides you with the following:

- Login email address.

- An account on a Windows domain.

- Windows network password.

To log in:

- Navigate to the Relativity site.

- Enter your Relativity email address in Username .

- Click Continue .

- Enter your Windows network password in Password .

Contact your system admin or IT department for password requirements.

- Click Login .

## Integrated Authentication

This method uses Integrated Windows Authentication to log in. There are no additional requirements to log in other than having a Windows domain account.

To log in, navigate to the Relativity site. The system automatically logs you in to Relativity. If you are not connected or if the Relativity logon dialog appears, contact your system admin.

## RSA

This method requires an RSA SecurID token along with a username and passcode. Your system admin provides you with the following:

- Username

- RSA SecurID token

- (Optional) PIN

To log in:

- Navigate to the Relativity site.

- Enter your username in Username .

- Click Continue .

- Enter your RSA password in Password in the format set by your system administrator. This password is either:

- The RSA tokencode, the eight-digit number from the RSA SecurID token hardware, if you have not been assigned or created a PIN

- Your combined PIN and RSA tokencode without a space between them

- Click Login .

You may also be asked to create or to reset your PIN. Follow the instructions on those screens.

## OpenID Connect

This method requires you to have an OpenID Connect account. Your system provides you with the following:

- OpenID Connect account user name from the identify provider's side.

- Relativity OpenID Connect button name on the login page.

To log in:

- Navigate to the Relativity site.

- Click the Relativity OpenID Connect button name.

- Enter your user name.

- Click Logon .

- Authenticate with your OpenID provider.

## SAML 2.0

This method requires you to have an account with SAML 2.0 authentication provider set up by your system admin. Your admin provides you with a Relativity account with a SAML 2.0 login method.

To log in:

- Log into the SAML 2.0 provider system.

- Navigate to the Relativity instance using a shortcut in the SAML 2.0 provider interface or a bookmark in your browser. You are automatically logged in.

## Creating or resetting a password

Use this procedure if you are logging in to Relativity for the first time or if you are resetting your password. Your system admin must send you a password reset email. If you forget your password, you can click the Forgot your password link on the login screen if it is available, or contact your system admin. In either case, the system sends you a new password email.

If you are a system admin, the Password Reset Email will not be sent to you. For more information, see Managing user authentication methods .

- Within the password request email, click Reset Password or enter the full URL into your browser.

- Enter a password following the restrictions listed on the screen. You must remember this password to log in. The link within the email is valid for 15 minutes, and you can only use the most recent email. Although, once the password is set, you do not have to log in immediately.

The following non-alpha-numeric characters are not allowed: \, ", <, >, £ in passwords. Users can make up to 10 password reset requests. Beyond that limit, the system will block further requests and guide users to contact their administrator for assistance.

- Click Submit .

- Click Return to Relativity .

On this page

- Logging into Relativity

- Logging in to Relativity with a password

- Password

- Two-factor authentication

- Active Directory

- Integrated Authentication

- RSA

- OpenID Connect

- SAML 2.0

- Creating or resetting a password


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
