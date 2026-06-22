---
title: "HTTP headers"
url: https://platform.relativity.com/Server2025/Content/REST_API/HTTP_headers.htm
collection: developer
fetched_at: 2026-06-22T06:25:10+00:00
sha256: 712affed0db7ca571b7b73927cc56082b691404ce5f5ac2f5a1cd03f294b990e
---

HTTP headers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# HTTP headers

The Relativity REST API requires certain fields in the HTTP header for a request:

- X-CSRF-Header : The cross-site request forgery (CSRF) field must be included in requests. This field provides basic security by preventing malicious parties from scanning your REST endpoint. Set the X-CSRF-Header to any value except an empty string. Usually, you would set the header value to a dash (-) as in the following example: Copy

```text
1
X-CSRF-Header: -
```

Don't leave this header value blank. If you omit this header field, the request fails.

- Content-Type : you can set this header field to application/json . See the following sample: Copy

```text
1
2

Content-Type: application/json
```

- Authorization : This header field is required if you are using basic or Active Directory authentication. See REST API authentication .

- Accept-Encoding : Set this header field to gzip to automatically compress responses. Any other Accept-Encoding headers are ignored.

On this page

- HTTP headers


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
