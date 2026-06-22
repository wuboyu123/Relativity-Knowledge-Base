---
title: "Adding custodian portal settings"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Adding_custodian_portal_settings.htm
collection: user
fetched_at: 2026-06-22T06:12:46+00:00
sha256: a9b85bac89cf74b0dbf7c2d7a61bde97dc551d70f6f3596f3db5c0ce41a66788
---

Adding custodian portal settings

# Adding custodian portal settings

Update the fields in the Custodian Portal. Define how the Custodian Portal will look and act to the custodian interacting with it. Add the URL, title, and a custom image to the portal.

To update the Custodian Portal settings on the Legal Hold Settings page, follow the steps below:

-

Click Edit .

-

Locate the Custodian Portal section.

-

Enter information in the fields. See Custodian Portal settings fields for more information.

-

Update another section or click Save .

## Custodian Portal settings fields

The custodian portal settings must be entered on the Legal Hold Settings page prior to starting a legal hold project.

- Portal URL - the Legal Hold Portal URL where your organization is hosting this application web page.

This URL must be:

- Externally exposed if anyone outside your network needs to access the Portal. See Custodian portal .

- A Relativity site using Forms authentication, not Windows authentication.

When using the ARM feature to restore a workspace, the Portal URL is removed in order to not point to the old server, preventing communications from being sent. The Portal URL will need to be updated before resuming sending communications. Locate the updated Portal URL in Legal Hold Settings.

- Portal Title - enter customized text that appears at the top of the Portal page.

- Portal Custom Image - upload a custom image that appears at the top of the Portal page. If there is no uploaded image, the Relativity logo appears as the default.

- The image shouldn't exceed 130 x 28 pixels.

- Legal Hold permits any common image file; however, we recommend a transparent .png for best results.

- Link Access Limit (Clicks) - number of times the custodian can access the Portal from the link sent in the communication email.

- Link Expiration (Days) - number of days the link sent in the communication email is valid.
