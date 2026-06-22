---
title: "Serialization and streaming"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Serialization_and_streaming.htm
collection: developer
fetched_at: 2026-06-22T06:31:11+00:00
sha256: 32a0a28a2d284ab0d23c67d3942aa5e70c473b1930436f52229440a42978e3a0
---

Serialization and streaming Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Serialization and streaming

The Kepler framework includes functionality necessary for converting data to formats that can easily be transferred between client and server. It provides a default serializer that uses JSON for HTTP requests, while also offering options to implement custom serializers and deserializers for your specific data model. Additionally, the Kepler framework offers options for custom streaming implementations.

## Serialization

The Kepler framework supports serializing objects as JSON representations using the JsonMediaTypeFormatter class available through .NET. This class uses the Json.NET library to perform serialization, so it handles only JSON formatted data. The default serializer provided by the Kepler framework is designed to meet the needs of most use cases. For more information, see JSON Media-Type Formatter on the Microsoft website and Json.NET in the Json.NET Documentation site.

### Custom serializers

You can implement custom serializers specifically for data models in your Kepler service. You need to include it in the assembly for your Kepler service implementation or interface. Your custom serializer must implement the IModelSerializer<T> interface, where T represents the type requiring custom serialization. The Kepler framework automatically detects any classes that implement the IModelSerializer<T> interface, and adds them to its media-type formatter.

This example illustrates how to implement custom serializer for the ResponseDTO model. See the following code sample illustrating the data model.

Copy

```text
1
2
3
4
5
6
7
public Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj)

{

    var response = new ResponseDTO();

    response.Data = "ABC";

    response.ID = 42;

    return Task.FromResult(response);

}
```

Through the Kepler framework, the default JSON serializer converts the ResponseDTO model to the following JSON:

Copy

```text
1
2
3
4
{

    "Data":"ABC",

    "ID":42

}
```

However, you can implement a serializer that converts the same ResponseDTO to the following JSON:

Copy

```text
1
2
3
{

    "ABC|42"

}
```

The following code sample illustrates how to implement the TransformForSerialize() method on the IModelSerializer interface for your custom serializer:

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
// Namespace containing the IModelSerializer<T> interface.

using Relativity.Kepler.Serialization;

// The IModelSerializer interfaces require you to implement

// the object TransformForSerialize(T model) and the

// T TransformForDeserialize(object data) methods.

public class ResponseDTOSerializer : IModelSerializer<ResponseDTO>

{

    // Custom serialization

    public object TransformForSerialize(ResponseDTO model)

    {

        string name = model.Name;

        int id = model.ID;

        string customSerialization = String.Format("{0}|{1}", name, id);

        return customSerialization;

    }

    // Because this model is only sent from the server and

    // never received, you don't need to handle deserialization.

    public ResponseDTO TransformForDeserialize(object data)

    {

        throw new NotImplementedException();

    }

}
```

### Custom deserializer

Additionally, you can implement a custom deserializer for your specific data model. The following code sample illustrates a custom deserializer for the RequestDTO model. It handles the custom deserialization of our RequestDTO on the server-side. See the code sample for the data model:

Copy

```text
1
2
3
4
5
6
// Request DTO from the reference service

public class RequestDTO

{

     string Name;

     int ID;

}
```

The client serializer converts the RequestDTO to the following JSON

Copy

```text
1
2
3
{

     "Name|ID"

}
```

The following code sample illustrates how to implement the TransformForDeserialize() method for your custom deserializer:

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
public class RequestDTOSerializer : IModelSerializer<RequestDTO>

{

    // Since this data model is only received by the server

    // and never sent, you don't need to handle serialization.

    public object TransformForSerialize(RequestDTO model)

    {

        throw new NotImplementedException();

    }

    // Custom deserialization

    public RequestDTO TransformForDeserialize(object data)

    {

        string modelData = (String)data;

        string[] values = modelData.Split('|');

        var model = new RequestDTO();

        model.Name = values[0];

        model.ID = Int.Parse(values[1]);

        return model;

    }

}
```

## Streaming

You can add I/O streams to a service by using the KeplerStream class, which derives from IKeplerStream interface. With this implementation, your Kepler service can return a System.IO.Stream object or take a System.IO.Stream object as a parameter. For more information, see Stream Class on the Microsoft website.

The following code sample illustrates the KeplerStream class with its constructors, properties, and method:

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
public class KeplerStream : IKeplerStream

{

    public KeplerStream(System.IO.Stream sendStream)

    {

    }

    public KeplerStream(Func<System.IO.Stream, Task> sendStream)

    {

    }

    public async Task<System.IO.Stream> GetStreamAsync()

    {

    }

    public string ContentType { get; set; }

    public string ContentDisposition { get; set; }

    public string CacheControl { get; set; }

}
```

### Constructors for KeplerStream class

The KeplerStream class includes the following constructors:

- KeplerStream(System.IO.Stream sendStream) - this constructor takes a System.IO.Stream object as an argument to instantiate a basic KeplerStream object. When using this constructor, don't call the Dispose() method on the System.IO.Stream object, that you used to instantiate the KeplerStream object. The Kepler framework automatically closes the stream when you call the Dispose() method on the IKeplerStream object from the client-side. View DownloadStream() method using Stream object in constructor

The following code sample illustrates how to instantiate a KelperStream object by using the constructor that takes a System.IO.Stream object.

Copy

```text
1
2
3
4
5
6
7
public async Task<IKeplerStream> DownloadStream()

{

    // Note that lack of a using statement or explicit Dispose() method call on the original stream object.

    // The Kepler framework calls the Dispose() method when you call IKeplerStream.Dispose() on the client-side.

    Stream s = new MemoryStream(TEST_BYTES);

    return await Task.FromResult(new KeplerStream(s));

}
```

The following code sample illustrates how to test this version of the DownloadStream() method.

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
[Test]

public async Task DownloadStream()

{

    // Using the using statement or calling Dispose() on the IKeplerStream will make sure Dispose() is called on the original .NET Stream object

    using (IKeplerStream download = await _service.DownloadStream())

    {

        string downloadValue = await ConvertStreamToString(await download.GetStreamAsync());

        Assert.AreEqual(TEST_STRING, downloadValue);

    }

}
```

- KeplerStream(Func<System.IO.Stream, Task> sendStream) - this constructor takes a Func delegate to as an argument to instantiate a basic KeplerStream object. The delegate then provides control of the stream. View DownloadStream() method using Func delegate object in constructor

The following code sample illustrates how to instantiate a KelperStream object by using the constructor that takes a Func delegate.

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
public async Task<IKeplerStream> DownloadStream()

{

    // Note the explicit Dispose() call on the original stream object because it uses the Func constructor.

    return await Task.Run(() =>

    {

        Stream s = new MemoryStream(TEST_BYTES);

        return new KeplerStream(async sendStream =>

        {

            int bufferSize = 1;

            byte[] buffer = new byte[bufferSize];

            int read;

            while ((read = await s.ReadAsync(buffer, 0, buffer.Length)) != 0)

            {

                await sendStream.WriteAsync(buffer, 0, read);

                await sendStream.FlushAsync();

            }

            sendStream.Close();

            s.Dispose();

        });

    });

}
```

The following code sample illustrates how to test this version of the DownloadStream() method.

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
[Test]

public async Task DownloadStream()

{

    using (

    Stream stream = new MemoryStream(TEST_BYTES))

    {

        string downloadValuee = await _service.DownloadStream(new KeplerStream(async sendStream =>

        {

            int bufferSize = 1; // Buffer size 1 byte for testing.

            byte[] buffer = new byte[bufferSize];

            int read;

            while ((read = await stream.ReadAsync(buffer, 0, buffer.Length)) != 0)

            {

                await sendStream.WriteAsync(buffer, 0, read);

                await sendStream.FlushAsync();

            }

            sendStream.Close();

        }));

        Assert.AreEqual(TEST_STRING, downloadValue);

    }

}
```

### Properties on KeplerStream class

When you use the KeplerStream class, it also provides the option to the set the ContentType, ContentDispositon, and CacheControl properties used in HTTP headers. See the following content on MDN web docs:

- ContentType

- ContentDisposition

- CacheControl

### Method on KeplerStream class

Because KeplerStream derives from the IKeplerStream interface, it implements the GetStreamAsync() method, which uses the stream provided via the constructors.

### Special considerations for streaming

Review the following special considerations for using steaming when implementing Kepler services:

- The IKeplerStream interface is only supported as an input parameter and a return type.

- The IKeplerStream interface isn't supported within another object as a parameter or return type. See the following example: Copy

```text
1
MyObject() { public IKeplerStream Stream { get; set; } }
```

- The Kepler framework controls the settings for the Content-Type header. It permits only certain content types, such as application/json .

- RESTful routes don't support file paths passed in the URI without a higher level of encoding. We recommend usingbase64 for URL encoding, because it is translated back to the original path by the the server failing your request.

- The IIS may limit the upload time and request length. To increase this values, modify the httpRuntime and maxRequestLength settings in the Relativity.REST web.config file. By default, the maxRequestLength setting is 1GB, while the maximum transfer size is 2GB.

- The default value in Relativity.REST is currently set to 1GB. This has been tested increasing the maximum transfer to 2GB. The current version of IIS appears to cap this setting at 2GB.

- The maximum download size is 100GB.

On this page

- Serialization and streaming

- Serialization

- Custom serializers

- Custom deserializer

- Streaming

- Constructors for KeplerStream class

- Properties on KeplerStream class

- Method on KeplerStream class

- Special considerations for streaming


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
