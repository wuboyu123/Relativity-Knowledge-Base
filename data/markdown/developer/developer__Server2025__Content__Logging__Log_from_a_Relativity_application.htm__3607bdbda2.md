---
title: "Log from a Relativity application"
url: https://platform.relativity.com/Server2025/Content/Logging/Log_from_a_Relativity_application.htm
collection: developer
fetched_at: 2026-06-22T06:29:35+00:00
sha256: b7b488ccdfa71a20317386925852c612faec349612899d917b5181afa10c24d8
---

Log from a Relativity application

# Log from a Relativity application

You can write logs from your custom applications that use agents, custom pages, and event handlers. Use Relativity API helpers to add loggers to your applications. To capture the data that meets your debugging needs, you can change properties captured for the logged events. You can also change the logging level and configure logging to log only for a specific application, log to a specific sink, or disable logging. For more information, see Configure logging .

You can't log from a standalone console application.

See these related pages:

- Logging

- Configure logging

- Troubleshoot Relativity using logging

- Logging system-subsystem-application matrix

## Before you begin

Before using logging in a custom application, make sure logging is enabled in Relativity to write to an appropriate sink. If you want to use the defaults, make sure the default configuration row in the RelativityLogging.Configuration table is set to True (1) . This enables logging to the EDDSLogging.RelativityLogs table at the Error (4) level. For more information, see Configure logging .

## IAPILog interface

The IAPILog interface included in the Relativity API namespace enables logging functionality. These IAPILog interface methods correspond to the available logging levels:

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
public interface IAPILog {

    void LogVerbose(string messageTemplate, params object[] propertyValues);

    void LogDebug(string messageTemplate, params object[] propertyValues);

    void LogInformation(string messageTemplate, params object[] propertyValues);

    void LogWarning(string messageTemplate, params object[] propertyValues);

    void LogError(string messageTemplate, params object[] propertyValues);

    void LogFatal(string messageTemplate, params object[] propertyValues);

    ...

}
```

When called from the code, the methods logs the events at the specified level and higher when the events occur. For example, the following code logs Debug, Information, Warning, Error, and Fatal-level events. The events may occur when cleaning Kepler Service Host temporary directories.

Copy

```text
1
Logger.LogDebug("Cleaning up any left over files and folders in the Kepler Service Host temporary directories");
```

Each method can also take an exception object. This outputs the exception and stack trace into a separate field in the database to assist with searching.

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
public interface IAPILog {

    ...

    void LogVerbose(Exception exception, string messageTemplate, params object[] propertyValues);

    void LogDebug(Exception exception, string messageTemplate, params object[] propertyValues);

    void LogInformation(Exception exception, string messageTemplate, params object[] propertyValues);

    void LogWarning(Exception exception, string messageTemplate, params object[] propertyValues);

    void LogError(Exception exception, string messageTemplate, params object[] propertyValues);

    void LogFatal(Exception exception, string messageTemplate, params object[] propertyValues);

    ...

}
```

## Add loggers using API helpers

Logging is built into the Relativity infrastructure and can be accessed using the API helpers . You can call the loggers from applications components, such as agents, custom pages, and event handlers.

The following code sample demonstrates how to call a default logger from an agent:

- Instantiate the logger. Copy

```text
1
2
private Relativity.API.IAPILog _logger;

_logger = this.Helper.GetLoggerFactory().GetLogger().ForContext<MyAgent>();
```

It is recommended to always scope a logger to a class using the ForContext<T>() method.

- Call the logger. Copy

```text
1
_logger.LogDebug(“Enabling agent {AgentName}”, Me.Name);
```

The following are examples of logging from an agent, a custom page, and an event handler.

Agent Copy

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
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
[kCura.Agent.CustomAttributes.Name("Patient Notes Processing Agent")]

[System.Runtime.InteropServices.Guid("3dc132a6-ba0f-448a-bc10-1667fa04b7cd")]

public class PatientNotesProcessingAgent : kCura.Agent.AgentBase

{

    private Relativity.API.IAPILog _logger;

    public static readonly String[] SYMPTOMS_TO_FIND = new String[] { "bumps", "fever", "lethargic", "fatigued", "rash", "cough", "headache" };

    public static readonly Guid PATIENT_NOTES_FIELD_GUID = new Guid("5702F31B-48AC-4E2A-9000-A48B3E3ABDBF");

    public static readonly Guid REQUIRES_FURTHER_EVALUATION_FIELD_GUID = new Guid("4B247F25-966D-4BFB-AD6F-2647D93B7DA4");

    public static readonly Guid PATIENT_RDO_GUID = new Guid("EDC3AF33-7D25-4897-8285-6E36EA1D4AAE");

    private static Int32 ErrorCount { get; set; }

    public override void Execute()

    {

        //Get the logger from the helper and set the ForContext to this class.

        _logger = this.Helper.GetLoggerFactory().GetLogger().ForContext<PatientNotesProcessingAgent>();

        //Add a ForContext property called MethodName to a new logger used by this method.

        //This new logger will have the ForContext from the private _logger variable.

        Relativity.API.IAPILog methodLogger = _logger.ForContext("MethodName", "Execute", false);

        //Log a message.

        methodLogger.LogVerbose("Starting Execution of PatientNotesProcessingAgent");

        PatientJobDTO patientToProcessJobDTO = null;

        Int32 keySymptomsFound;

        //Get the current Agent artifactID

        Int32 agentArtifactID = this.AgentID;

        //Get the EDDS database context

        Relativity.API.IDBContext eddsDBContext = this.Helper.GetDBContext(-1);

        try

        {

            //Get the next available job from the queue

            this.RaiseMessage("Looking for the next job in the queue", 10);

            //Other Agent work

            …

        }

    }

}
```

This code sample also demonstrates the use of the RaiseMessage() method of the AgentBase to log information-level events. For more information about AgentBase logging methods, see Basic concepts for agents . For debugging, using IAPILog interface through API helpers is the recommended way of logging from agents.

Custom page Copy

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
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
using System;

using System.Collections.Generic;

using System.Linq;

using System.Web;

using System.Web.Mvc;

namespace PatientTracker.CustomPages.Controllers

{

    /// <summary>

    /// This custom page shows how to use a patient artifactID and current workspace artifactID to retrieve information from the RSAPI, and then display a profile page for the patient.

    /// </summary>

    public class PatientController : Controller

    {

        private Relativity.API.IAPILog _logger;

        public static readonly Guid PATIENT_RDO_GUID = new Guid("EDC3AF33-7D25-4897-8285-6E36EA1D4AAE");

        public static readonly Guid FIRST_NAME_FIELD_GUID = new Guid("EB024552-3A1B-40C1-B4DC-5815C3DD3AD3");

        public static readonly Guid LAST_NAME_FIELD_GUID = new Guid("DA73E11E-9D02-4D29-9D3C-F84E66223B2A");

        public static readonly Guid GENDER_FIELD_GUID = new Guid("04E5F293-A4E1-4DF4-8816-F1E6645AE001");

        public static readonly Guid DATE_OF_BIRTH_FIELD_GUID = new Guid("96BC22AF-F2F6-4C92-AD96-CF08BF9AAB4D");

        public static readonly Guid PATIENT_NOTES_FIELD_GUID = new Guid("5702F31B-48AC-4E2A-9000-A48B3E3ABDBF");

        public static readonly Guid PICTURE_FIELD_GUID = new Guid("006F21C0-66C8-46E0-94B2-EF37C6478C2D");

        public ActionResult Index(Int32 patientArtifactID, Int32 workspaceArtifactID)

        {

            //Get the logger from the helper and set the ForContext to this class.

            _logger = Relativity.CustomPages.ConnectionHelper.Helper().GetLoggerFactory().GetLogger().ForContext<HomeController>();

            PatientTracker.CustomPages.Models.PatientModel patient = new Models.PatientModel();

            kCura.Relativity.Client.DTOs.RDO patientRDO = null;

            try

            {

                //Create an instance of the RSAPIClient so we can pull back information about the patient.

                using (kCura.Relativity.Client.IRSAPIClient client = Relativity.CustomPages.ConnectionHelper.Helper().GetServicesManager().CreateProxy<kCura.Relativity.Client.IRSAPIClient>(Relativity.API.ExecutionIdentity.System))

                {

                    _logger.LogInformation("Attempting to pull patient info for {PatientArtifactID} in workspace {WorkspaceID}", patientArtifactID, workspaceArtifactID);

                    //Set the workspace artifactID.

                    client.APIOptions.WorkspaceID = workspaceArtifactID;

                    //Create an instance of the RDO with the Patient RDO GUID and the patient artifactID.

                    patientRDO = new kCura.Relativity.Client.DTOs.RDO(patientArtifactID);

                    patientRDO.ArtifactTypeGuids.Add(PATIENT_RDO_GUID);

                    patientRDO.Fields = kCura.Relativity.Client.DTOs.FieldValue.AllFields;

                    //Get the patient RDO from the RSAPI.

                    patientRDO = client.Repositories.RDO.Read(patientRDO).Results[0].Artifact;

                    //Set properties on the patient model.

                    patient.FirstName = patientRDO.Fields.Where(x => x.Guids.Contains(FIRST_NAME_FIELD_GUID)).Single().ValueAsFixedLengthText;

                    patient.LastName = patientRDO.Fields.Where(x => x.Guids.Contains(LAST_NAME_FIELD_GUID)).Single().ValueAsFixedLengthText;

                    patient.DateOfBirth = patientRDO.Fields.Where(x => x.Guids.Contains(DATE_OF_BIRTH_FIELD_GUID)).Single().ValueAsDate.Value;

                    patient.PatientNotes = patientRDO.Fields.Where(x => x.Guids.Contains(PATIENT_NOTES_FIELD_GUID)).Single().ValueAsLongText;

                    //Construct a download request used to get a proper download url for the file to be downloaded.

                    kCura.Relativity.Client.DownloadURLRequest pictureFieldDownloadRequest = new kCura.Relativity.Client.DownloadURLRequest(client.APIOptions);

                    Uri currentUrl = Request.Url;

                    pictureFieldDownloadRequest.BaseURI = new Uri(String.Format("{0}://{1}/", currentUrl.Scheme, currentUrl.Host));

                    pictureFieldDownloadRequest.Target.FieldGuid = PICTURE_FIELD_GUID;

                    pictureFieldDownloadRequest.Target.ObjectArtifactId = patientArtifactID;

                    //Set the picture file path on the patient model.

                    patient.PicturePath = client.Repositories.RDO.GetFileFieldDownloadURL(pictureFieldDownloadRequest).URL;

                }

            }

            catch (System.Exception ex)

            {

                patient.PatientNotes = "EXCEPTION: " + ex.ToString();

                //Log an error.

                _logger.LogError(ex, "There was an issue pulling back patient info.");

            }

            return View(patient);

        }

    }

}
```

Event handler Copy

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
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
namespace PatientTracker.EventHandlers {

    /// <summary>

    /// This event handler will execute before the page loads and will populate the Co-Pay field with a default value

    /// </summary>

    [kCura.EventHandler.CustomAttributes.Description("Patient pre-load event handler")]

    [System.Runtime.InteropServices.Guid("CB6ED881-F432-4F9A-8187-B87B1FA89D50")]

    class PatientPreLoadEventHandler : kCura.EventHandler.PreLoadEventHandler

    {

        Relativity.API.IAPILog _logger;

        private const Decimal DEFAULT_CO_PAY = 25.0M;

        public static readonly Guid CO_PAY_FIELD_GUID = new Guid("24402D3C-4EAF-4C33-B244-A145EEB7C6C1");

        public override kCura.EventHandler.Response Execute() {

            //Get the logger from the helper and set the ForContext to this class.

            _logger = this.Helper.GetLoggerFactory().GetLogger().ForContext<PatientPreLoadEventHandler>();

            //Construct a response object with default values

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            retVal.Message = String.Empty;

            try {

                //Ensure that this is a new artifact

                if (this.ActiveArtifact.IsNew) {

                    //Find the Co-Pay field and populate with a default value

                    this.ActiveArtifact.Fields[CO_PAY_FIELD_GUID.ToString()].Value.Value = DEFAULT_CO_PAY;

                   _logger.LogVerbose("Copay field {Guid} value changed to {DefaultCoPay}", CO_PAY_FIELD_GUID.ToString(), DEFAULT_CO_PAY);

                }

            }

            catch (System.Exception ex) {

                retVal.Success = false;

                retVal.Message = ex.ToString();

            }

            return retVal;

        }

        /// <summary>

        /// Ensure that we always have access to these fields in the ActiveArtifact.Fields collection regardless if they are on the current layout or not

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields {

            get {

                kCura.EventHandler.FieldCollection retVal = new kCura.EventHandler.FieldCollection();

                retVal.Add(new kCura.EventHandler.Field(CO_PAY_FIELD_GUID));

                return retVal;

            }

        }

    }

}
```

## Add custom metadata to loggers

In many cases, you may need to record additional details for your events, for example, to make them easier to identify. With Relativity you can add custom properties (metadata) to your logs. This can be done in the following ways:

- Create a logger scoped for a class to add the class properties to the metadata. Copy

```text
1
var myClassLogger = _logger.ForContext<MyClass>();
```

- Pass an arbitrary string key-value pair to identify messages from a specific logger. Copy

```text
1
var myLogger = _logger.ForContext(“CodeLocation”, “ZiggyStation”);
```

- Associate a code block with a logger through using statement. The following example demonstrates how to add a JobID property to the messages logged by the code running inside the using statement block. Copy

```text
1
2
3
4
5
using (_logger.LogContextPushProperty("JobId", 12345))

{

    _logger.LogWarning("Any usage of _logger

    within this using context will now have the JobID property.");

}
```

## Best practices

The following are the recommended best practices when using logging in your applications:

- Create a scoped logger for each class. See examples in Add loggers using API helpers .

- Always prefer structured data over string concatenation. Relativity logging events are associated with message templates.

Treating the string parameter to log methods as a message, as in the example below, will degrade performance and consume cache memory.

Copy

```text
1
2
// Don't:

Relativity.Logging.Log.Logger.LogDebug("Enabling agent" + Me.Name);
```

Instead, always use template properties to include variables in messages. Properties are passed in enclosed in braces:

Copy

```text
1
2
// Do:

Relativity.Logging.Log.Logger.LogDebug("Enabling agent {AgentName}", Me.Name);
```

- If you have an object where all properties can be displayed in a log, you can use the @ symbol to declare a message param as a destructured object. Examples of properties that must never be displayed in the logs are passwords or decrypted text that is normally encrypted. A destructured object in a message template will deserialize the object into JSON and put the results in the message output and in the metadata.

This example shows what happens when you destructure a class object. Any objects that implement IEnumerable, like arrays, lists, tuples, dictionaries, etc., are destructured to JSON even without the @ symbol. Destructuring data types like strings or integers does not deserialize to a JSON string.

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
 //Sample class

namespace MySampleNamespace

{

    public class MyObject

    {

        public string Description { get; set; }

        public int Value { get; set; }

    }

}

//Sample Logging Code

MyObject testObject = new MyObject()

{

    Description = "This is my object",

    Value = 100

};

//To get a destructured object put the @ symbol before the name of your message param name: {@...}

Relativity.Logging.Log.Logger.LogDebug("Testing MyObject destructured - {@DeserializedMyObject}", testObject);

//If you do not put the @ symbol the object will be outputted as if you did testObject.ToString()

Relativity.Logging.Log.Logger.LogDebug("Testing MyObject not destructured - {NonDeserializedMyObject}", testObject);

//Destructuring simple data types results in a non JSON serialized output, just like if

string myString = "My Test String";

Relativity.Logging.Log.Logger.LogDebug("Testing myString destructured - {@MyString}", myString);
```

This is the output of the code:

Copy

```text
1
2
3
4
5
6
7

With the @ symbol

Message: Testing MyObject destructured - MyObject { Description: "This is my object", Value: 100 }

Without the @ symbol

Message: Testing MyObject destructured - "MySampleNamespace.MyObject"

Simple data type with the @ symbol

Message: Testing myString destructured - "My Test String"
```

- Log all exceptions by adding loggers to try-catch statements.

- Log all calls to Relativity REST services.

- Log all calls when using the service interfaces instantiated through ServiceFactory, for example, permissions and saved search APIs.

- Log any direct SQL access.

- Pay attention to the logging levels and don’t overuse logging. Logging can have a significant impact on your disk, database, processor, and network resources.
