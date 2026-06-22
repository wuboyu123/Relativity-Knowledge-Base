---
title: "Matter Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Matter_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:27+00:00
sha256: 4a8ab250ff5e41b6a3b7abed7eade317c37d371319a1246162edc3d641c339ec
---

Matter Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Matter Manager (.NET)

In Relativity, a matter is a legal case, such as a dispute or other action during which a law firm acts as a representative of a client. For general information, see Matters on the Relativity Documentation site.

The Matter Manager API exposes multiple methods for programmatically managing matters in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations on matters.

- Provides helper methods used to retrieve available clients and statuses. Use these helper methods when creating and updating matters.

You can also interact with the Matter Manager API through REST. For more information, see Matter Manager (REST) .

## Retrieve a list of available clients

Use the the GetEligibleClientsAsync() method to retrieve a list of the available clients that you can associate with a matter.

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
public static async Task GetEligibleClientsAsync()

{

    using (Relativity.Environment.V1.Matter.IMatterManager matterManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Matter.IMatterManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await matterManager.GetEligibleClientsAsync();

            foreach (DisplayableObjectIdentifier client in response)

            {

                string info = string.Format("Read client {0} with Artifact ID {1}", client.Name, client.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve a list of matter statuses

Use GetEligibleStatusesAsync() method to get a list of the available statuses for matters.

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
public static async Task GetEligibleStatusesAsync()

{

    using (Relativity.Environment.V1.Matter.IMatterManager matterManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Matter.IMatterManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await matterManager.GetEligibleStatusesAsync();

            foreach (DisplayableObjectIdentifier status in response)

            {

                string info = string.Format("Read status {0} with Artifact ID {1}", status.Name, status.ArtifactID);

                Console.Write(info);

            }

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Create a matter

Use the CreateAsync() method to add a new matter.

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
23
24
25
26
27
28
29
public static async Task CreateAsync()

{

    int clientId = 1015253;

    int statusId = 1016892;



    MatterRequest request = new MatterRequest

    {

        Name = "New Matter",

        Number = "10",

        Keywords = "keywords",

        Notes = "notes",

        Client = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = clientId }),

        Status = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = statusId })

    };



    using (Relativity.Environment.V1.Matter.IMatterManager matterManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Matter.IMatterManager>())

    {

        try

        {

            int newMatterArtifactId = await matterManager.CreateAsync(request);

            string info = string.Format("Created matter with Artifact ID {0}", newMatterArtifactId);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve metadata for a matter

Use ReadAsync() method to retrieve the metadata for a matter.

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
public static async Task ReadAsync()

{

    int matterArtifactId = 1016911;



    using (Relativity.Environment.V1.Matter.IMatterManager matterManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Matter.IMatterManager>())

    {

        try

        {

            MatterResponse response = await matterManager.ReadAsync(matterArtifactId);

            string info = string.Format("Read matter {0} with Artifact ID {1}", response.Name, response.ArtifactID);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update a matter

Use the UpdateAsync() method to modify the properties of a matter.

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
23
24
25
26
27
28
public static async Task UpdateAsync()

{

    int matterArtifactId = 1016911;

    int clientId = 1015253;

    int statusId = 1016892;



    MatterRequest request = new MatterRequest

    {

        Name = "New Matter",

        Number = "10",

        Keywords = "keywords",

        Notes = "notes",

        Client = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = clientId }),

        Status = new Securable<ObjectIdentifier>(new ObjectIdentifier { ArtifactID = statusId })

    };



    using (Relativity.Environment.V1.Matter.IMatterManager matterManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Matter.IMatterManager>())

    {

        try

        {

            await matterManager.UpdateAsync(matterArtifactId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete a matter

Use the DeleteAsync() method to remove a matter from Relativity.

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
public static async Task DeleteAsync()

{

    int matterArtifactId = 1016911;



    using (Relativity.Environment.V1.Matter.IMatterManager matterManager = serviceFactory.CreateProxy<Relativity.Environment.V1.Matter.IMatterManager>())

    {

        try

        {

            await matterManager.DeleteAsync(matterArtifactId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

On this page

- Matter Manager (.NET)

- Retrieve a list of available clients

- Retrieve a list of matter statuses

- Create a matter

- Retrieve metadata for a matter

- Update a matter

- Delete a matter


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
