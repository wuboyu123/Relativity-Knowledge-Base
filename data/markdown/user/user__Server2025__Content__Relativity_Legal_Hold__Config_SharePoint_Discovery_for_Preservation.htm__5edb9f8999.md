---
title: "Setting up SharePoint Discovery for preservation holds"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Config_SharePoint_Discovery_for_Preservation.htm
collection: user
fetched_at: 2026-06-22T06:13:22+00:00
sha256: 961f54b6e6aa66930a04aae9f7a5b551b435167d55b66244ea88d70d9e4fd62d
---

Setting up SharePoint Discovery for preservation holds

# Setting up SharePoint Discovery for preservation holds

This section explains how to configure SharePoint Discovery to use modern authentication via the CSOM API when executed from a RelativityOne Legal Hold project. This configuration will create an Enterprise Application in Azure.

We use SharePoint Discovery to identify SharePoint sites that a given custodian has access to. This differs from manually doing so in Microsoft because you no longer need to know exact URLs to preserve (via copy and paste). Configuring this process reduces the need to manually look up SharePoint sites for each custodian or to only use custodian interviews, plus it helps eliminate errors from copying and pasting the information. By leveraging this set up, we're able to pass the details about a user to Microsoft and identify many of the SharePoint sites that a custodian has access to and also enable you to later select from a list of SharePoint sites to add to your preservation case.

For further reference, see Microsoft's documentation for information on granting access using SharePoint App-Only to set up an app-only principal with tenant permissions.

## Configuring SharePoint Discovery

Follow the steps below to configure SharePoint Discovery.

- Register a new principal as follows:

- Navigate to a site in your tenant and call the AppRegNew.aspx page. For example, https://relativitytest.sharepoint.com/_layouts/15/appregnew.aspx .

- On the AppRegNew.aspx page, click the Generate button next to the Client ID and Client Secret fields to generate both values.

Be sure to store the principal Client ID and Client Secret values because you'll need them when entering information into the Preservation Hold Settings page in step 3.

- Enter a Title for the new principal. For example, RelativityTest App Principal .

- Enter an App Domain URL value. This is the fully qualified domain name. For example, www.relativitytest.com .

- Enter a Redirect URL value. For example, https://{RELATIVITY_URL}/Relativity.Rest/API/kCura.LegalHold.Services.ILegalHoldModule/GraphAuthorizationManager/graph-auth-response .

- Grant permissions to the newly created principal as follows:

- Navigate to the AppInv.aspx page on the tenant administration site. For example, https://relativitytest-admin.sharepoint.com/_layouts/15/appinv.aspx .

- Enter your Client ID and click Lookup to locate and select the principal created in step 1.

- Enter the following in the Permission Request XML text box to grant permissions:

<AppPermissionRequests AllowAppOnlyPolicy="true">

<AppPermissionRequest Scope="http://sharepoint/content/tenant" Right="Manage" />

</AppPermissionRequests>

- Click Create .

- When the permission consent dialog appears, click Trust It to grant the permissions.

- Enter Legal Hold Preservation settings as follows:

- Navigate to Preservation Hold Settings in RelativityOne.

- Enter the Principal Client ID that you stored in Step 1 above.

- Enter the Principal Client Secret that you stored in Step 1 above.

- Select the Enable SharePoint CSOM checkbox.

- Click Save .

SharePoint Discovery holds will now use modern authentication via the CSOM API when executed from a Legal Hold Project.

## Limitations of SharePoint Discovery

The time it takes and success rate for a SharePoint Discovery job can vary greatly depending on a number of factors, including how many custodians are assigned to the project, how many SharePoint sites a Microsoft O365 tenant has, how large those SharePoint sites are, and how many integrations your O365 environment has. Essentially, the more custodians in a project and the more SharePoint sites to discover, the longer the job will take.

The SharePoint Discovery job is a resource intensive process and can also be throttled heavily by Microsoft depending on how "busy" the Microsoft environment is (such as, the many applications that integrate with an O365 instance). It is recommended to run SharePoint Discovery after already putting Exchange Mailboxes on hold, as the discovery job could block those from finishing if run concurrently. We have seen success running the discovery job for up to 30,000 SharePoint sites on a Microsoft Purview instance and finishing within 3-5 days. The less custodians and SharePoint sites, the faster the job will go.
