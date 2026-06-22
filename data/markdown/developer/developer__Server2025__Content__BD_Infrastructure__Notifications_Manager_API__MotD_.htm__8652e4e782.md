---
title: "Notifications Manager (MotD) - (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Infrastructure/Notifications_Manager_API__MotD_.htm
collection: developer
fetched_at: 2026-06-22T06:23:33+00:00
sha256: 2230cac295f660af096c5099652724e716e5e8e068fa6ca1d3c5f987a0aaa3d1
---

Notifications Manager (MotD) - (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Notifications Manager (MotD) - (.NET)

The Message of the Day (MotD) is a message displayed to all users when they log in to Relativity. The MotD is commonly used to inform users of planned system maintenance. For more information, see Adding and editing a Message of the Day on the Relativity Documentation site.

The Notifications Manager API exposes methods for reading, updating, and dismissing the MotD. It also includes methods for determining whether the MotD has been dismissed, and whether it is displayed as plain text or HTML.

You can also use the Notifications Manager service through the REST API. For more information, see Notifications Manager (MotD) - (REST) .

## Fundamentals for the Notifications Manager API

The Notifications Manager API contains the following methods and classes.

### Methods

The Notifications Manager API exposes the following methods on the INotificationsManager interface in the Relativity.Infrastructure.V1.Notifications namespace:

- DismissMotdAsync() method - disables the MotD for a specific user. This method takes the Artifact ID for a user. It doesn't have return value. See Dismiss the MotD .

- HasDismissedMotdAsync() method - indicates whether the user associated with the ID passed to the method previously dismissed the MotD. This method takes the Artifact ID for a user and returns a Boolean value indicating whether the message was dismissed. See Has Dismissed the MotD .

- IsTextOnlyMotdAsync() method - indicates whether the MotD can be displayed only as text or as HTML. It returns a Boolean representation of the MotD text-only instance setting. For more information, see the MOTDTextOnly instance setting in the Instance settings' descriptions page on the Relativity Documentation site. See Display the MotD .

- ReadMotdAsync() method - retrieves information about the MotD. This method returns a MotdResponse object, which contains the properties for the MotD. See Read the MotD .

- UpdateMotdAsync() method - modifies the properties for the MotD. This method takes a MotdRequest object and returns a MotdResponse object, which contains the properties for the MotD. See Update the MotD .

### Classes

The Notifications Manager API includes the following classes available in the Relativity.Infrastructure.V1.Notifications.Models namespace:

- MotdRequest class - represents the data used to create or update the MotD. It has the following properties:

Name Type Description

Message string A message displayed to users at login.

Enabled bool A value indicating whether MotD is enabled.

AllowDismiss bool A value indicating whether MotD can be dismissed.

- MotdResponse class - represents an existing MotD. It has the same properties as the MotdRequest class.

## Read the MotD

Use the ReadMOTDAsync() method to retrieve the properties of the MotD, such as whether it's enabled, whether it was dismissed, and the content of the message. The MotdResponse object is returned by the method and contains these properties.

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
14
15
16
17
18
19
20
public async Task<bool> ReadMotdAsync(IHelper helper)

{

    bool success = false;

    using (INotificationsManager proxy = helper.GetServicesManager().CreateProxy<INotificationsManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            MotdResponse motdResponse = await proxy.ReadMotdAsync();

            logger.LogInformation($"ReadMotdAsync succeeded. Message is {motdResponse.Message}.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }



    return success;

}
```

## Update the MotD

Use the UpdateMOTDAsync() method to enable and modify the MotD.

For more information about formatting the MotD, see the MOTDTextOnly instance setting in the Instance settings' descriptions page on the Relativity Documentation site.

See the following code sample:

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
14
15
16
17
18
19
20
21
public async Task<bool> UpdateMotdAsync(IHelper helper)

{

    bool success = false;

    using (INotificationsManager proxy = helper.GetServicesManager().CreateProxy<INotificationsManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            MotdRequest motdRequest = new MotdRequest { Message = "New Message", AllowDismiss = false, Enabled = true };

            MotdResponse motdResponse = await proxy.UpdateMotdAsync(motdRequest);

            logger.LogInformation($"UpdateMotdAsync succeeded. Message is {motdResponse.Message}.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }



    return success;

}
```

## Dismiss the MotD

Use the DismissMOTDAsync() method to close the MotD. See the following code sample:

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
14
15
16
17
18
19
20
public async Task<bool> DismissMotdAsync(IHelper helper, int userId)

{

    bool success = false;

    using (INotificationsManager proxy = helper.GetServicesManager().CreateProxy<INotificationsManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            await proxy.DismissMotdAsync(userId);

            logger.LogInformation($"DismissMotdAsync succeeded. User is {userId}.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }



    return success;

}
```

## Has Dismissed the MotD

Use the HasDismissedMOTDAsync() method to determine whether a user has previously dismissed the MotD. See the following code sample:

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
14
15
16
17
18
19
20
21
22
public async Task<bool> HasDismissedMotdAsync(IHelper helper, int userId)

{

    bool success = false;

    using (INotificationsManager proxy = helper.GetServicesManager().CreateProxy<INotificationsManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            bool hasDismissed = await proxy.HasDismissedMotdAsync(userId);

            logger.LogInformation(

                $"HasDismissedMotdAsync succeeded. User is {userId}. User has{hasDismissed ? ""

                    :" not"} dismissed the message.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }



    return success;

}
```

## Display the MotD

Use the IsTextOnlyMOTDAsync() method to determine whether the MotD can display HTML or only text.

For more information about formatting the MotD, see the MOTDTextOnly instance setting in the Instance settings' descriptions page on the Relativity Documentation site.

See the following code sample:

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
14
15
16
17
18
19
20
public async Task<bool> IsTextOnlyMotdAsync(IHelper helper)

{

    bool success = false;

    using (INotificationsManager proxy = helper.GetServicesManager().CreateProxy<INotificationsManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        try

        {

            bool isTextOnlyMotd = await proxy.IsTextOnlyMotdAsync();

            logger.LogInformation($"IsTextOnlyMotdAsync succeeded. Message is{isTextOnlyMotd ? "":" not"} text only.");

            success = true;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }



    return success;

}
```

On this page

- Notifications Manager (MotD) - (.NET)

- Fundamentals for the Notifications Manager API

- Methods

- Classes

- Read the MotD

- Update the MotD

- Dismiss the MotD

- Has Dismissed the MotD

- Display the MotD


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
