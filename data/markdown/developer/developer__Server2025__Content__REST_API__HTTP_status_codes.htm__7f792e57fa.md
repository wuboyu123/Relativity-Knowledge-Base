---
title: "HTTP status codes in Relativity REST APIs"
url: https://platform.relativity.com/Server2025/Content/REST_API/HTTP_status_codes.htm
collection: developer
fetched_at: 2026-06-22T06:29:47+00:00
sha256: f63eb916ebc0ee92a628a01292e67f99edd39959adb7326564ba3f3775d2da7b
---

HTTP status codes in Relativity REST APIs

# HTTP status codes in Relativity REST APIs

The Relativity REST APIs return the following status codes in HTTP responses. For additional information, see HTTP response status codes on the MDN web site.

Status code Description

200 OK A successful request.

201 Created A resource has been created.

202 Accepted The request has been accepted but it hasn't been completed. Returned when an asynchronous operation is performed, and provides a URL for status monitoring.

302 Found The request has been redirected. The resource has been found at another URL location.

400 Bad Request The request couldn't be understood by the server due to malformed syntax. Returned when a condition field or sort on a query couldn't be parsed, or when an error occurs in a URL, a JSON representation, or an HTTP header.

401 Unauthorized The authentication header is missing or that header contains invalid credentials.

404 Not Found A resource matching the request doesn't exist. This response code is also returned when the CSRF header is missing.

405 Method Not Allowed The requested operation is not supported on the specified Artifact type by the Services API.

409 Conflict This status code may be returned if you try to update an object while it is undergoing an asynchronous operation.

For example, you may be attempting to update a batch set that the system is using for the creation of batches.

500 Internal Server Error An unhandled exception occurred on the server. To troubleshoot this error, return a stack trace by setting CustomErrors to Off in the REST API web.config file.
