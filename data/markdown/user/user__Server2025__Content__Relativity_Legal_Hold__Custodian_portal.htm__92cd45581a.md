---
title: "Custodian portal"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Custodian_portal.htm
collection: user
fetched_at: 2026-06-22T06:13:15+00:00
sha256: 3786512ac2294963eabc9ee6d1a8538fb7cab2bb04d7f052f63fbfe56cc64b9a
---

Custodian portal

# Custodian portal

Custodians can only access custodian portals via a secure link in a legal hold communication. In the portal, custodians can acknowledge their participation in a hold, answer questionnaires, view all of the active projects they're associated with, and easily address any other outstanding tasks.

## Custodian portal browser compatibility

Access the Custodian portal from the following browsers:

Browser Supported Browser Version

Internet Explorer 9, 10, 11

Chrome 42+

Firefox 37+

Safari on Mac

(OS X 10.9+)

7.1+

To access the portal:

- Click the portal link in the email. This link takes you directly to the acknowledgment or questionnaire in which the portal opens in a separate browser window to the homepage.

Use the email merge field, PORTALLINK, to include the portal URL in the communication. See Email merge fields .

-

From the portal homepage, review any Tasks Requiring Attention, Completed Tasks, and any Active Holds that you're associated with. This includes acknowledgment requests and questionnaire response requests for all projects with which you're associated.

The Active Holds grid only shows projects containing a communication that Legal Hold sent to the custodian with the Is Legal Hold flag set to Yes. See Communication detail layout fields . This differentiates between FYI communications that Legal Hold sends to employees that shouldn't be treated as litigation holds.

The Custodian Portal will not display any projects in which a custodian's role in that project includes the Do Not Notify role tag.

- Click the links to open each outstanding item.

- Once you've acknowledged participation in a project or answered a questionnaire, Legal Hold sends an acknowledgment notification to the project owner.

If you receive a portal link expiration error, your link has expired. Click Send Link for Legal Hold to send you a new link.

Click on any of the holds in the Active Holds grid to view the corresponding communication to the hold. Holds containing multiple communications that Legal Hold sent to the custodian appear as separate entries in the Active Holds grid.

System admins can set the number of times custodians can access the portal link before it becomes invalid. See Installing Legal Hold .

## Customizing the Custodian Portal

System admins can customize the Custodian Portal's for the custodians in Legal Hold projects. To customize the portal, navigate to the Legal Hold Settings tab. Update the portal title, customize the image, the access, and the link expiration in the Custodian Portal section.

Update the Portal Title field to a title that works with the name of the company, the litigation, or the custodian. The limit of characters for the Portal Title is 95 characters by default. To update the number of characters, see Fields . The portal title appears on the top left of the custodian portal.

The system admin can also set the Portal Custom Image in the Custodian Portal section. The portal custom image appears in the top left of the custodian portal next to the portal title. The size of the image is hard coded to be 130px x 28px.

To set the Link Access Limit (Clicks), the number of times a custodian can use the link, add a number between 1 and 100. The Link Expiration (Days) is the number of days the link will be valid. This link can be valid for any number of days and can be set by the system admin.

## SSO for Custodian Portal

Use single-sign on (SSO) for a layer of security of the custodian portal. SSO requires a custodian to authenticate through your organizations SSO provider prior to gaining access to the custodian portal.

Relativity Legal Hold supports OpenID Connect using Microsoft Azure AD.

Use SSO to have custodians access the custodian portal securely by signing into the organization’s identity provider.

Send personalized custodian portal links to custodians. The link contains a token that recognizes authentication. If a custodian isn't authenticated, they are redirected to the organization's sign on page. Once signed into their organization, the custodian is redirected to the portal.

## Accessing the Custodian Portal

Within the Custodian Console, you can send an email containing the link to the Custodian Portal or you can access the Custodian Portal as a specific custodian.

Navigate to the Entities tab and click on a custodian. Select the Legal Hold Custodian view, which contains the Custodian Console. Within the console, click the Send Portal Link button or the Use Portal As button.

-

The Send Portal Link button will send an email with the link to the custodian portal to the custodian.

-

The Use Portal As button will let the admin access the custodian portal as the custodian.
