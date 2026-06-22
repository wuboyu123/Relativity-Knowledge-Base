---
title: "Storing and using external API credentials"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Storing_and_using_external_API_credentials.htm
collection: developer
fetched_at: 2026-06-22T06:24:42+00:00
sha256: 17203885bcc2676502318a71dbcefce61097774a6071b532c596af9827e32b6c
---

Storing and using external API credentials

# Storing and using external API credentials

Use this tutorial to learn how to connect to APIs hosted outside of Relativity from an extensibility point (agent, event handler, Custom Page, or Kepler API) and pass credentials to the external API.

Estimated completion time : 30 minutes

## Before you begin

Understand the authentication that the external API requires. Common examples are API keys or an OAuth2 authentication token generated using a client ID and client secret. This tutorial uses API key authentication with the address validation API provided by Google.

## Create the Relativity Dynamic Object (RDO)

- In a workspace, create a new Object Type called Company .

- Create a new fixed-length text fields on this object called Address , City , and State .

- Update the default Company Layout to include these new fields.

- Add Relativity with no address and Save

-

Create a new Application within the workspace and push it to the Application Library. This application will be used to store our event handler(s).

## Build the extensibility point

In this example we have a basic RDO to store company information. When a new company is created, the public Google address validation API will validate that the address is accurate.

- Begin by creating a pre-save event handler. You will add the API integration in a future step. Copy

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
using kCura.EventHandler;

using System;

namespace CompanyAddressValidator {

  [kCura.EventHandler.CustomAttributes.Description("Company Validation Pre Save EventHandler")]

  [System.Runtime.InteropServices.Guid("292326fe-5815-43b8-98bb-630917e89ee3")]

  public class PreSaveEventHandler: kCura.EventHandler.PreSaveEventHandler {

    public override Response Execute() {

      Response addressValidationResponse = new Response() {

        Success = false,

          Message = String.Empty

      };

      string address = this.ActiveArtifact.Fields["Address"].Value.Value.ToString();

      string city = this.ActiveArtifact.Fields["City"].Value.Value.ToString();

      string state = this.ActiveArtifact.Fields["State"].Value.Value.ToString();

      if (address.Length > 0) {

        try {

          bool isValid = ValidateAddress(address, city, state);

          addressValidationResponse.Success = isValid;

          if (!isValid) {

            addressValidationResponse.Message = "Address not valid.";

          }

        } catch (Exception ex) {

          addressValidationResponse.Message = ex.ToString();

        }

      } else {

        // Address field is empty

        addressValidationResponse.Success = true;

      }

      return addressValidationResponse;

    }

    public bool ValidateAddress(string address, string city, string state) {

      var apiKey = GetApiKey();

      // Validate address here! This will be updated later in the tutorial.

      return false;

    }

    private string GetApiKey() {

      // Get API key here! This will be updated later in the tutorial.

      string apiKey = String.Empty;

      return apiKey;

    }

    public override FieldCollection RequiredFields {

      get {

        FieldCollection fieldList = new FieldCollection();

        fieldList.Add(new Field("Address"));

        fieldList.Add(new Field("City"));

        fieldList.Add(new Field("State"));

        return fieldList;

      }

    }

  }

}
```

- Build the project and upload the CompanyAddressValidator.dll to the Resource Files tab in admin mode. Ensure that it is affiliated with the application that you created and pushed to the library.

- Within the workspace, navigate to Object Types > Company and link the CompanyAddressValidator to the event handlers section.

## Store the credential

There are two options to store credentials for use within an extensibility point: use Secret Store, or use encrypted Instance Settings.

### Using Secret Store

A secret may be written to Secret Store directly using API Helpers. The secret value may only be used by extensibility points within the application that created the secret.

For example: when a Relativity Application is installed, a post-install event handler could create the new secret containing the API key. The following code sample shows how to write an API key from a post-install event handler to ensure that the API key is available to extensibility points:

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
private void WriteApiKey() {

  Secret secret = new Secret() {

    Data = new System.Collections.Generic.Dictionary < string, string > () {

      {

        "apiKey",

        "keyvaluehere"

      }

    }

  };

  this.Helper.GetSecretStore().Set("google/api_key", secret);

}
```

More information and code samples are available in the Relativity API Helpers documentation .

### Using encrypted Instance Settings

An Instance Setting may be used with Encrypt set to true to store API credentials. This can be added via the User Interface, or Instance Setting Manager API. Any application or extensibility point within the Relativity environment could decrypt and use this value but it will not be visible via the UI. This approach is useful for credentials that are less sensitive or have broadly applicable use cases across the environment.

For this tutorial we've added an Instance Setting from the Relativity UI with the Section as CompanyValidator , Name as GoogleApiKey , and Encrypt set to Yes .

## Fetch the API authentication information

Depending which mechanism used to store the credentials, add a method to retrieve the credentials when calling the external API.

Copy Retrieve from Secret Store

```text
1
2
3
4
5
6
private string GetApiKey() {

  Secret apiKeySecret = this.Helper.GetSecretStore().Get("google/api_key");

  string apiKey = String.Empty;

  apiKeySecret.Data.TryGetValue("apiKey", out apiKey);

  return apiKey;

}
```

Copy Retrieve from Instance Settings

```text
1
2
3
4
5
private string GetApiKey() {

  var bundle = Helper.GetInstanceSettingBundle();

  string apiKey = bundle.GetString("CompanyValidator", "GoogleApiKey");

  return apiKey;

}
```

## Call the API with authentication

Add the code to call the external API. In this example, we will implement a ValidateAddress() function.

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
public bool ValidateAddress(string address, string city, string state) {

  var apiKey = GetApiKey();

  HttpClient client = new HttpClient();

  string postPayload = $ "{{\"address\":{{\"addressLines\":[\"{address}\"],\"locality\":\"{city}\"}}}}";

  StringContent postData = new StringContent(postPayload, Encoding.UTF8, "application/json");

  HttpResponseMessage response = client.PostAsync($"https://addressvalidation.googleapis.com/v1:validateAddress?key={HttpUtility.UrlEncode(apiKey)}", postData).ConfigureAwait(false).GetAwaiter().GetResult();

  if (response.IsSuccessStatusCode) {

    string responseContent = response.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter().GetResult();

    dynamic responseObject = JsonConvert.DeserializeObject(responseContent);

    string addressComplete = responseObject.result.verdict.addressComplete;

    if (!String.IsNullOrEmpty(addressComplete)) {

      return Convert.ToBoolean(addressComplete);

    } else {

      return false;

    }

  } else {

    throw new Exception($"{response.StatusCode} {response.ReasonPhrase} {response.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter().GetResult()}");

  }

}
```

The above code sample requires a reference to Newtonsoft.Json. Do not upload this assembly as a Resource File - Relativity provides its own version of this library

Build the project and replace the existing Resource File with the new version.

## Test the validator

Return to the Relativity company added at the beginning of the tutorial. If you attempt to update the address information using incomplete or inaccurate information an error will occur and the save will not be completed:

After adding the proper floor number the API considers this address valid and the save action succeeds:
