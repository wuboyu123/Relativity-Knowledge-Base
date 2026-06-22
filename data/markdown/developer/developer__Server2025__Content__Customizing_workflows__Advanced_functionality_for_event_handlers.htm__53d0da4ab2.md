---
title: "Advanced functionality for event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Advanced_functionality_for_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:42+00:00
sha256: 966524b5b1efc98123e4d996af32a0ca6520d52d77e1e4634774a9a1a774b917
---

Advanced functionality for event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Advanced functionality for event handlers

You can enhance the custom event handlers by incorporating advanced functionality in them.

## Work with Choice field types

You can develop event handlers used to manipulate values that users store in different field types. The following list describes how to handle choice fields:

- The values that the user assigns to choice fields are stored in instances of the ChoiceFieldValue class. This class is a subclass of FieldValue.

- The ChoiceCollection contains only Choice objects representing choices selected by a user in Relativity.

- The IsSelected property on each Choice object is always set to true because only selected Choice objects are returned.

- The Choices property on the ChoiceFieldValue class returns a ChoiceCollection instance. Use the Count property of the ChoiceCollection to determine how many Choices are set on a choice field. If no Choices are set, the Count property returns 0.

### Sample code for Choice fields

These code samples illustrate common uses of choice fields:

- Cast the value of a Choice to the type ChoiceFieldValue: Copy

```text
1
2
3

Guid fieldGuid = new Guid("6bc19a2b-b7d1-4b8f-bf14-9eaed515d2b8");

ChoiceFieldValue choiceFieldValue = (ChoiceFieldValue)ActiveArtifact.Fields[fieldGuid.ToString()].Value;
```

- To clear the choice field, remove all the Choices from ChoiceCollection: Copy

```text
1
2
3
4
5
6
7
8

//Clear the ChoiceCollection.

Guid fieldGuid = new Guid("6bc19a2b-b7d1-4b8f-bf14-9eaed515d2b8");

ChoiceFieldValue choiceFieldValue = (ChoiceFieldValue)ActiveArtifact.Fields[fieldGuid.ToString()].Value;

ChoiceCollection myListOfDesiredChoices = new ChoiceCollection();



//The ChoiceCollection is now cleared.

choiceFieldValue.Choices = myListOfDesiredChoices;
```

- To clear a specific choice from a choice field, remove the Choice instance from a ChoiceCollection: Copy

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

//Clear a specific Choice from a ChoiceCollection using the ArtifactID.

Guid fieldGuid = new Guid("6bc19a2b-b7d1-4b8f-bf14-9eaed515d2b8");

const Int32 choiceArtifactID = 1036982;

ChoiceFieldValue choiceFieldValue = (ChoiceFieldValue)ActiveArtifact.Fields[fieldGuid.ToString()].Value;

ChoiceCollection myListOfDesiredChoices = new ChoiceCollection();



//Because you can't directly remove a Choice, create a new collection that

//contains the desired Choice instances but excludes the Choice

//that you no longer need.

foreach (Choice c in choiceFieldValue.Choices)

{

     if (c.ArtifactID != choiceArtifactID)

     {

          myListOfDesiredChoices.Add(c);

     }

}



//Set the Choices property to the modified collection.

choiceFieldValue.Choices = myListOfDesiredChoices;
```

- To add a selected choice to a choice field, add the Choice to the ChoiceCollection using its ArtifactID: Copy

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

//Add a specific Choice to the ChoiceCollection using its Artifact ID.

Guid fieldGuid = new Guid("6bc19a2b-b7d1-4b8f-bf14-9eaed515d2b8");

const Int32 choiceArtifactID = 1036982;

ChoiceFieldValue choiceFieldValue = (ChoiceFieldValue)ActiveArtifact.Fields[fieldGuid.ToString()].Value;

ChoiceCollection myListOfDesiredChoices = choiceFieldValue.Choices;



//The ArtifactID parameter is used to specify which choice to set, not the name parameter.

//You don't need to set the name parameter to the actual name of the choice, but it must be unique to the collection.

myListOfDesiredChoices.Add(new Choice(choiceArtifactID, choiceArtifactID.ToString()));



//Set the Choices property to the modified collection.

choiceFieldValue.Choices = myListOfDesiredChoices;
```

- Retrieve a Choice by name: Copy

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
//Get a Choice by name.

if (!this.ActiveArtifact.Fields["Choice Field Name"].Value.IsNull)

{

    kCura.EventHandler.ChoiceCollection choiceCollection = (kCura.EventHandler.ChoiceCollection)this.ActiveArtifact.Fields["Choice Field Name"].Value.Value;

    foreach (kCura.EventHandler.Choice choice in choiceCollection)

    {

        if (String.Equals(choice.Name, FEMALE_CHOICE_NAME, StringComparison.OrdinalIgnoreCase))

        {

             //Perform some operation with your choice.

        kCura.EventHandler.Choice myChoice = choice;

            break;

        }

    }

}
```

## Add assembly source information

You can add source information to assemblies to improve troubleshooting. To include company name and copyright metadata, you need to add System.Reflection.AssemblyCompanyAttribute and System.Reflection.AssemblyCopyrightAttribute to the AssemblyInfo.vb/AssemblyInfo.cs file generated with your Visual Studio project.

The following sample code shows how to add the company name and copyright values for an assembly.

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

[assembly: AssemblyTitle("TestAgent")]

[assembly: AssemblyDescription("")]

[assembly: AssemblyConfiguration("")]

[assembly: AssemblyCompany("ACME Inc.")]



[assembly: AssemblyProduct("TestAgent")]

[assembly: AssemblyCopyright("Copyright ©  2012")]



[assembly: AssemblyTrademark("")]

[assembly: AssemblyCulture("")]
```

The Relativity web interface displays fields containing the source information that you specified for your assemblies.

You can't specify a value for the Application field in your source code. Relativity sets the value of this field when you add an assembly through the Resource Files tab. See Resource files on the Relativity Server 2025 Documentation site.

On this page

- Advanced functionality for event handlers

- Work with Choice field types

- Sample code for Choice fields

- Add assembly source information


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
