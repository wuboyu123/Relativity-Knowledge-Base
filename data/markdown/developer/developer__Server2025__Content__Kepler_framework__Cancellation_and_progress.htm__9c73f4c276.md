---
title: "Cancellation and progress"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Cancellation_and_progress.htm
collection: developer
fetched_at: 2026-06-22T06:31:09+00:00
sha256: ae4110374b6318f50eef3cb44ab289f30d4b43a75208839cb348dc920eb40e9c
---

Cancellation and progress

# Cancellation and progress

The Kepler framework supports cancellation and progress functionality for service calls that run for an extended time. You can implement your service calls so that they can be canceled after reaching a specific time threshold. Additionally, you can return progress information on calls as they execute.

## Cancellation

The Kepler framework supports the cancellation of requests have long running times. To use this functionality, pass a CancellationToken object as an argument to your service method. See the following sample code:

Copy

```text
1
Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj, CancellationToken cancel);
```

The following code samples illustrates how cancel a call to the DataRequestAsync() method when it takes longer than 2500 milliseconds to complete. When the IsCancellationRequested property on the toke returns try, the method call returns null. For this example, the CancellationToken object is used as follows by the client and the server:

- Server-side code - the IsCancellationRequested property must return true to cancel the call. Copy

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
public async Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj, CancellationToken cancel)

{

    for (int i = 1; i <= count; i++)

    {

        ARandomObject obj = await DoRandomAsyncStuff(requestObj);

        if (cancel.IsCancellationRequested)

        {

            return null;

        }

    }

    ResponseDTO response = mapper.map(obj);

    return response;

}
```

- Client-side code - the CancellationTokenSource object generates a cancellation token, which is passed to service method as follows: Copy

```text
1
2
3
4
5
var proxy = factory.CreateProxy<IExampleService>();

int cancelAfterMS = 2500;

var cts = new CancellationTokenSource(cancelAfterMS);

// The CancellationTokenSource object generates  CancellationToken by accessing the Token property.

ResponseDTO response = proxy.DataRequestAsync(request, cts.Token);
```

## Progress

Through the Kepler framework, you can also obtain progress reports from endpoints that perform long running operations (LRP) as they continue executing. To use this functionality,

- On the server-side, optionally pass an object that implements the IProgress<T> interface to your service method. T is an object that reports execution progress back to the calling client.For more information, see Progress<T> Class on the Microsoft website.

- On the client-side, subscribe to progress reporting by passing object of the same type as defined on the server to your service method. The Progress object contains an Action<T> event handler that the client uses to act on reported progress.

The following code samples illustrates add progress reporting to the DataRequestAsync() method on a Kepler service:

- Server-side code - an object of type IProgess<string> is passed to the DataRequestAsync() method on the server. Copy

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
// Add IProgress<T> parameter to service endpoint.

public Task<ResponseDT> DataRequestAsync(RequestDTO requestObj, IProgess<string> progress)

{

    var response = new ResponseDTO();

    response.Data = "ABC";

    response.ID = 42;

    /// Test for a long running operation.

    ...

    if (progress != null) {

        progress.Report("progress message");

    }

    ...

    ///

    return Task.FromResult(response);

}
```

- Client-side code - a progress object of the same type as defined on the server is instantiated, and passed to the DataRequestAsync()method. Copy

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
// Handle progress reports.

var progress = new Progress<string>;(msg =>; {

    // Actions taken in the event handler should be thread-safe.

    Console.WriteLine(msg);

    // Print a progress message.

};

// Create a proxy to access the services.

var proxy = factory.CreateProxy<IExampleService>()

var request = new RequestDTO() {

    Name = "name",

    ID = 6

};

Try {

    var result = await proxy.DataRequestAsync(request, progress);

}

Finally {

    proxy.Dispose();

}
```

## Long running process (LRP) vs Remote procedure call (RPC)

In the Kepler framework, LRP functionality is used in conjunction with the cancellation and progress features. It enhances a RPC call made by a Kepler service, which may take a long time to run. The Kepler framework checks whether a method signature on a given service contains either or both IProgress<T> or CancellationToken objects.

When the RPC call ends due to completion or a timeout, the LRP portion of the call also ends.

The following code samples illustrate these method calls:

- LRP method Copy

```text
1
Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj, IProgress<string> progress, CancellationToken token);
```

- RPC method Copy

```text
1
Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj);
```

## Disposition of the proxy for progress and cancellation

When using the progress and cancellation features, you need to continue using the proxy until the call has completed satisfactorily or ended with an exception. Don't dispose of the proxy until one of these states is reached.

- Correct disposition of the proxy - the Dispose() method was called when the call was done. Copy

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
int eventCount= 0;

var progress = new Progress<string>(msg =>

{

  Interlocked.Increment(ref eventCount)

});

var proxy = factory.CreateProxy<IExampleService>()

ResponseDTO response = null;

try

{

  response = await proxy.DataRequestAsync(requestObj, progress, token);

  while (eventCount < 5)

  {

    Task.Delay(5);

  }

}

finally

{

  proxy.Dispose();

}
```

- Incorrect disposition of the proxy - the Dispose() method was called too early. Copy

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
int eventCount= 0;

var progress = new Progress<string>(msg =>

{

  Interlocked.Increment(ref eventCount)

});

using (var proxy = factory.CreateProxy<IExampleService>())

{

  response = await proxy.DataRequestAsync(requestObj, progress, token);

}

while (eventCount < 5)

{

  Task.Delay(5);

}
```
