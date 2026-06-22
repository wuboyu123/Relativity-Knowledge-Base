---
title: "Advanced functionality for custom pages"
url: https://platform.relativity.com/Server2025/Content/Customizing_the_UI/Advanced_functionality_for_custom_pages.htm
collection: developer
fetched_at: 2026-06-22T06:31:21+00:00
sha256: a68263a0010d48da02f429847e105506ebc2f6be22df86598d6f6bae72aade67
---

Advanced functionality for custom pages Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Advanced functionality for custom pages

You can enhance custom pages that you develop by incorporating advanced functionality in them. For example, you might want to use Forms or Windows authentication methods in your custom pages.

## Custom authentication

You can configure applications that contain custom pages to use their own authentication systems. With custom authentication, you can create Relativity applications that use specialized access to application components. Relativity supports Forms Authentication or Windows Authentication methods.

Use the following steps when incorporating these authentication methods in your custom pages:

Applications with custom pages can use Forms or Windows Authentication methods. They can also run in Anonymous mode.

### Manually enable Forms or Windows Authentication in IIS

- Locate the IIS application for your custom pages current deployment. See Find a custom page's physical deployment , for more information.

- Disable Anonymous authentication and enable your chosen authentication method (Forms or Windows) via IIS.

manual configuration will need to done each time your custom page is redeployed due to your application or relativity upgrading.

### Enable Forms or Windows Authentication via your custom page's web.config

IIS must be configured to allow applications to change their own authentication methods.

- Navigate to Feature Delegation at the root of the IIS server and set Authentication - Anonymous, Authentication - Windows, and/or Authentication - Forms to Read/Write.

- Insert the following sections into your Custom Page's web.config as desired:

- To disable anonymous authentication:

Copy

```text
1
2
3
4
5
6
7
<system.webServer>

    <security>

        <authentication>

            <anonymousAuthentication enabled="false" />

        </authentication>

    </security>

</system.webServer>
```

- To enable Forms authentication:

Copy

```text
1
2
3
<system.web>

    <authentication mode="Forms" />

</system.web>
```

- To enable Windows Authentication:

Copy

```text
1
2
3
<system.web>

    <authentication mode="Windows" />

</system.web>
```

- Values set via your web.config will automatically deploy with your Custom Page after each upgrade, and do not require further manual intervention.

On this page

- Advanced functionality for custom pages

- Custom authentication

- Manually enable Forms or Windows Authentication in IIS

- Enable Forms or Windows Authentication via your custom page's web.config


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use
