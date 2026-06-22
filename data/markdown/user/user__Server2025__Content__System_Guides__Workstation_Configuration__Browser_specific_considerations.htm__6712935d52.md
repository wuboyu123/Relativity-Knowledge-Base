---
title: "Browser specific considerations"
url: https://help.relativity.com/Server2025/Content/System_Guides/Workstation_Configuration/Browser_specific_considerations.htm
collection: user
fetched_at: 2026-06-22T06:21:21+00:00
sha256: 310906ce9ea9da43a57f943e876f1b1c783917f23b3cca32e67d2f00f42cc657
---

Browser specific considerations

# Browser-specific considerations

Refer to the following browser specific considerations when using Relativity.

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## End user browser and operating system requirements

Unless otherwise noted, this table lists the version of each browser that was available when Relativity performed testing for a Relativity Server version release. Relativity does not incrementally test new browser versions for compatibility unless a version-specific issue is identified. If we discover any version-specific issues with browser compatibility, both this page and Known Issues will be updated.

Software Latest Version Tested by Relativity

Chrome (Windows, Mac OSX) 130.0.6723.59

Edge (Windows, Mac OSX) 130.0.2849.52

Firefox (Windows, Mac OSX) 131.0.3

Safari (Mac OSX) 18.1

Relativity does not currently support the Linux operating system for any browser.

## Considerations for all browsers

Relativity does not support the following:

- Accessing the same Relativity instance with multiple tabs at the same time.

- Accessing the same Relativity instance with multiple browsers at the same time.

## Changing the language settings in Chrome

Internet Explorer syncs the region and language settings with the operating system. Chrome does not have the same behavior.

You must manually change the language settings in Chrome to keep the language settings in sync with the operating system.

To change the language settings in Chrome, refer to the Chrome documentation .

Make sure to place the selected language at the top of the Languages list, as Chrome uses the first language by default.

## Using single sign-on (SSO) on a Mac in Chrome and Safari

In order for single sign-on (SSO) authentication to work on a Mac in Chrome and Safari, you must use SSO in conjunction with the Mac Keychain application.

- Safari considerations

- Safari prompts for credentials the first time you access Relativity. If you select Remember this password in my Keychain you won't be prompted for credentials again

- If you change your Active Directory password, you are prompted to update your Keychain at log in. This updates the Safari saved password and you are not prompted when accessing Relativity.

- If you manually delete the entry in the Keychain, you are prompted for credentials when accessing Relativity.

- Chrome considerations

- Chrome prompts you for credentials the first time you access Relativity. After you authenticate your machine, click Yes to remember the password and save the password in the Keychain.

- Chrome pre-populates the prompt with credentials.

## Pop-up blockers in Firefox

By default, Firefox blocks some pop-ups in Relativity. Normally, Firefox displays a message near the URL bar stating that a pop-up was blocked and asks whether to allow pop-ups for the website. For certain pop-ups, this message displays but then disappears immediately, before giving you a chance to allow pop-ups.

This error occurs in the Delete button in the action bar of any object's View page. To work around this issue, perform the following steps:

- Navigate to the Firefox browser Options menu.

- Click the Content tab, then under the Block pop-up windows section, click Exceptions .

- Add the URL of Relativity (e.g.,, http://localhost/Relativity).

After performing these steps, Firefox doesn't block any Relativity pop-ups in the environment.

Alternatively, you can disable pop-up blocking for all websites by clearing the Block pop-up windows option in the Content tab.

## Pop-up blockers in Safari

Similar to Firefox, Safari also blocks the Delete pop-up on any object's View page, but Safari never alerts the user. To work around this issue, open the Preferences menu, navigate to the Security tab, and clear the Block pop-up windows option. Safari no longer blocks pop-ups from any website.

## Enable tabbing on a Mac in Safari or Firefox

When working in Relativity using Safari or Firefox on a Mac OS, you must configure the following settings to enable tabbing:

### Safari

- Navigate to the Advanced tab from Safari Preferences, and then select Press Tab to highlight each item on a webpage .

### Firefox

- Click Keyboard from System Preferences, and then navigate to the Shortcuts tab.

- Select All Controls near the bottom of the window in the Full Keyboard access section.

Enabling the All Controls setting can cause a cursor to appear to the right of any items you've highlighted using the Tab key. To stop this cursor from appearing, perform the following steps:

- Navigate to the Advanced tab from System Preferences.

- Click the General subtab if necessary, and then select Always use the cursor keys to navigate within pages .
