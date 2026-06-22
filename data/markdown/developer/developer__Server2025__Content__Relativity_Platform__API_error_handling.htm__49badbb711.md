---
title: "Relativity API error handling"
url: https://platform.relativity.com/Server2025/Content/Relativity_Platform/API_error_handling.htm
collection: developer
fetched_at: 2026-06-22T06:23:59+00:00
sha256: 5feb9698ef53122206f8c83395495fe3e8c1db2c2ea6717b745fd22b212c9b36
---

Relativity API error handling

# API error handling

The Relativity APIs include error handling options that you can use to build resilient applications, which effectively handle errors. By implementing applications with proper error handling, you can provide a better experience for your users.

All APIs return errors, which may be generally categorized as follows:

- Errors occurring as expected behavior, such as when a request has invalid arguments.

- Errors originating from within Relativity itself.

Use the guidelines on this page to learn about the types of errors raised by Relativity APIs and how your application code should respond to them.

## Errors in RESTful services

RESTful services use the HTTP response status codes to communicate the success or failure of a request. Relativity APIs rely on the following major classes of HTTP response codes:

- 2XX status codes - indicate that the request was accepted by the API.

- 4XX status codes - indicate that a problem occurred with the request when it was submitted. These status codes indicate that the arguments supplied to a service were invalid. When a 400-level errors occurs, you can re-submit your request usually with updated arguments, and the call may succeed.

- 5XX status codes - indicate that a problem occurred on the server while processing the request. These generic errors indicate a problem with Relativity. An application can't perform any action to correct a 500-level error returned from a Relativity API.

For more information, see HTTP response status codes on the MDN web site.

### Handling errors

Use the class of the status codes to determine the appropriate action for the calling application. The following examples illustrate error handling options for different classes of status codes:

- 4XX status codes - A call was submitted with invalid arguments that resulted a 400-level error in the response. The application must resolve this issue by providing the appropriate arguments and then submitting the call again.

- 5XX status codes - A call was submitted that returned a 500-level error due to a problem in a Relativity API. Follow these guidelines:

- Open a bug report with Relativity. Contact Support with information about the error.

- Don't attempt to update your application to compensate for 500-level errors in business logic. Instead, treat any 500 error as though the service is completely down.

Additionally, HTTP errors usually return a JSON body with details about the issue that occurred. You can log these error payloads and use them for troubleshooting. They may contain field-level detail about the failure of a request, allowing the application to render errors on an HTML form being completed by a user.

## Error handling in .NET

In Relativity, the .NET SDKs are wrappers around the RESTful APIs. The Relativity APIs translate all non-success HTTP status codes, such as 400 and 500 codes, into .NET exceptions. They can be handled using standard .NET exception handling techniques. The Relativity SDKs define the following common exception types:

Status code Exception type* Description

500 ServiceException The base class for any exception from a service. Inherit from this class and override the status code.

400 ServiceSerializationException An exception thrown for a serialization or deserialization error.

400 ValidationException An exception that occurs during data validation.

403 NotAuthorizedException An exception that occurs during scope validation.

404 NotFoundException An exception that occurs when a resource isn't found.

404 ServiceNotFoundException An exception raised when the service endpoint can't be found.

409 DataConcurrencyException An exception indicating that the request can't be completed because of a conflict on the server.

409 ConflictException An exception indicating that the request can't be completed because of a conflict on the server.

*The exceptions listed in this table reside in the Relativity.Services.Exceptions namespace.

Some exceptions may contain field-level detail about the failure of a request, such as the ValidationException. In addition to the exceptions listed in the table, individual SDKs may define their own exceptions that provide more details about the failure of a request.

Every exception listed in the table inherits from the ServiceException base type. Due to this implementation, applications can wrap API calls in a try-catch statement with the ServiceException listed as the final block:

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
try

{

    await client.CallOperationAsync(...);

}

catch (ValidationException valEx)

{

    // Inform the user that the request needs to be fixed.

}

catch (ServiceException ex)   // Catches all other API-related errors

{

    // Log the error.

    // Display a generic failure message to the user or re-throw the error.

}
```

## Error code changes over time

Enhancements to individual APIs may include returning new HTTP response codes and exception types that provide better information about a failure. Implement your application so that it can accommodate the following changes:

- Error codes updated from a generic error to a more specific error, such as 500 to 4XX, 500 to 5XX, and 400 to 4XX.

- Status code changes that don't affect the business semantics or workflow of the API.

Use the best practices for error handling to ensure that your applications can accommodate these changes. See Best practices for error handling .

## Best practices for error handling

Use the following best practices when implementing your error handling strategy:

- Always order error handling logic from the most to least specific. See the following recommendations:

- REST calls - provide generic error handling for 4XX and 5XX errors at the end of an API call.

- .NET calls - provide an exception handler that catches the ServiceException type and logs the call failure.

- Don't try to interpret or recover from 500 errors or base ServiceExceptions.

Treat these top-level exceptions as though the call failed for an unknown reason. If the error is due to a defect in a service, open a ticket with Relativity instead of trying to interpret and compensate for the error. Contact Support with this error information.

- Consolidate your error-handling logic.

Avoid bugs by reusing generic error handling logic. Most programming languages offer libraries and techniques to write general-purpose error handling that can be shared across the code base of an application.

- Always use the Is Operator in .NET instead of directly checking types. Copy

```text
// DO THIS

if (ex is ValidationException) { ... }

// DO THIS

catch (ServiceException ex) { ... }

// DO NOT DO THIS

if (typeof(ex) == ValidationException) { ... }
```
