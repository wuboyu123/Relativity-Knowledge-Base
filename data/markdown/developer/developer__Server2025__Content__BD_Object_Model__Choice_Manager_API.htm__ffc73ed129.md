---
title: "Choice Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Choice_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:07+00:00
sha256: 8a1ff74a47ced5acc9dbfac6282cd9508364163d27b8438f219c0ae82c929c35
---

Choice Manager (.NET)

# Choice Manager (.NET)

In Relativity, choices are predetermined values of single and multi-choice list fields. You can perform operations on admin and workspace choices. For more general information, see Choices in the Relativity Documentation site.

The Choice Manager API exposes multiple operations you can use to programmatically manage choices in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations and mass operations on choices.

- Provides helper endpoints used to sort choices, move choices in lists, and retrieve highlight colors and parent choices or fields.

As a sample use case, you could use the Choice Manager API to create choices used to perform specific operations in a custom application.

You can also use the Choice Manager API through REST. For more information, see Choice Manager (REST) .

## Fundamentals for the Choice Manager API

Review the following information to learn about the methods, classes, and enumerations used by the Choice Manager API.

Methods

The Choice Manager API includes the following methods available on the IChoiceManager interface in the Relativity.ObjectModel.<VersionNumber>.Choice namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new choice to a Relativity environment. To create a choice, pass a ChoiceRequest object to the method. It returns the Artifact ID of the new choice. To mass create choices, pass a MassCreateChoiceRequest object to the method. It returns a MassCreateChoiceResponse object.

- ReadAsync() method - retrieves information about a choice. To retrieve a choice, pass a valid choice Artifact ID or GUID. It returns a ChoiceResponse object.

- UpdateAsync() method - modifies one or more choices. To update a choice, pass a ChoiceRequest object and valid choice Artifact ID or GUID to the method. To mass update choices, pass a MassUpdateChoiceRequest object to the method. It returns a MassActionChoiceResponse object.

- DeleteAsync() method - removes one or more choices from Relativity. To delete a choice, pass a valid choice Artifact ID or GUID to the method. To mass delete choices, pass a MassDeleteChoiceRequest object to the method. It returns a MassActionChoiceResponse object.

- AvailableParentsListAsync() method - retrieves a list of available parents for a specific choice or field.

- GetColorsListAsync() method - retrieves a list of colors that can be assigned to a choice.

- SortAsync() method - sorts a list of choices. To alphabetically sort all choices in a field, pass a valid field Artifact ID and a ChoiceReorderTypeEnum object. It returns a MassActionChoiceResponse object.

- MoveAsync() method - moves one or more choices in a list. To move a choice(s) to the beginning or end, pass a valid field Artifact ID, a list of ObjectIdentifier, and a ChoiceMoveTypeEnum object. To move a choice(s) after a specific choice, pass a valid field Artifact ID, a list of ObjectIfentifier, and an ObjectIdentifier object that represents the specific choice. It returns a MassActionChoiceResponse object.

Classes and enumerations

The Choice Manager API includes the following classes and enumerations:

- ChoiceMoveType enum - identifies the position in the list of choices for a field where a subset of choices is relocated.

- ChoiceRequest class - used to specify information for creating or updating a choice.

- Field - identifies the field associated with the choice.

- Name - a string representing the user-friendly name of the choice.

- Color -the color of field.

- Order - an integer used to determine order in which multiple choices are listed in UI. Lower values are listed first.

- ChoiceResponse class - represents the results of a read operation on a choice.

- Color class - represents a highlight color for a choice.

- MassActionChoiceResponse class - represents the result summary of both a massive delete or a massive update of choices.

- MassCreateChoiceHierarchy class - represents a choice abstraction used to define hierarchy of choices created when a mass create operation is performed.

- MassCreateChoiceModel class - represents data model for choice information of a massive create operation.

- MassCreateChoiceRequest class - represents the request to create multiple choices at once.

- Choices - a list of choices to be created. For single choice fields, use a flat list of choices without any child choices. For multi-choice fields, the list can be hierarchical. Each choice can have child choices, and each child can its own children. You can only specify the choice name property with mass create.

- ChoiceTemplateData - information to be applied to all the created choices.

- MassCreateChoiceResponse class - represents the result summary of both massive create choices.

- MassCreatedChoice class - represents data model for choice information returned by massive create operation.

- MassDeleteChoiceRequest class - represents a request to delete multiple choices.

- MassUpdateChoiceRequest class - represents data model for choice massive update request.

- SortDirection enum - identifies the sort order applied to a list as either ascending or descending.

### Guidelines for the Choice Manager API

Use these guidelines when working with choice fields:

- Multi-choice fields allow choices to be arranged in a hierarchical fashion. For example, a choice named Important might have child a choice of Critical . Selecting the child choice on a field in the RDO layout also results in the parent choice being selected.

- Single-choice fields do not allow for this arrangement of choices. Some endpoints only apply to multi-choice fields, or choices that are associated with multi-choice fields. Examples of this are the GetAvailableParentListAsync() methods. Requests to these made to these endpoints that reference single-choice fields will result in a status code 422 (unprocessable entity) response. See the method description details below for which methods are multi-choice only.

## Create a single choice

The following code sample illustrates how to create a single choice asynchronously using the CreateAsync() method.

View code sample Copy

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
public async Task CreateSingleChoiceAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int fieldID = 1104632;

        // use helper method to get list of available colors

        List<Color> colors = await choiceManager.GetColorsListAsync(workspaceID);

        ChoiceRequest choiceRequest = new ChoiceRequest()

        {

            Name = "Relevant",

            Field = new ObjectIdentifier() { ArtifactID = fieldID},

            Order = 10,

            Color = colors.FirstOrDefault(color => color.Name == "Green").ID

        };

        int choiceID = await choiceManager.CreateAsync(workspaceID, choiceRequest);

    }

}
```

## Mass create choices

The following code sample illustrates how to mass create choices asynchronously using the CreateAsync() method.

View code sample Copy

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
public async Task CreateMultipleChoicesAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int fieldID = 1104635;

        // This request creates four fields with the following hierarchy:

        //  + Important

        //      + Critical

        //      + Very

        //      + Somewhat

        MassCreateChoiceRequest massCreateRequest = new MassCreateChoiceRequest()

        {

            Choices = new List<MassCreateChoiceHierarchy>()

            {

                new MassCreateChoiceHierarchy

                {

                    Name = "Important",

                    Children = new List<MassCreateChoiceHierarchy>()

                    {

                        new MassCreateChoiceHierarchy() {Name = "Critical"}

                        new MassCreateChoiceHierarchy() {Name = "Very"},

                        new MassCreateChoiceHierarchy() {Name = "Somewhat"},

                    }

                }

            },

            ChoiceTemplateData = new MassCreateChoiceModel()

            {   // Template data applies to all fields created.

                Field = new ObjectIdentifier() { ArtifactID = fieldID },

            }

        };

        MassCreateChoiceResponse choices = await choiceManager.CreateAsync(workspaceID, massCreateRequest);

    }

}
```

## Read a choice

The following code sample illustrates how to read a single choice asynchronously using the ReadAsync() method. (To list the choices for a field, see Object Rule Manager service .)

View code sample Copy

```text
1
2
3
4
5
6
7
using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

{

    int workspaceID = 1022092;

    int choiceID = 1104636;

    ChoiceResponse choiceResponse = await choiceManager.ReadAsync(workspaceID, choiceID);

}
```

## Update a choice without a version check

The following code sample illustrates how to use the UpdateAsync() method modify information on a choice without performing a version check.

After the choice is created, you cannot change the field associated with it.

View code sample Copy

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
public async Task UpdateSingleChoiceAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int fieldID = 1104635;

        int choiceID = 1104640;

        // retrieve available parents

        ObjectIdentifier fieldIdentifier = new ObjectIdentifier() {ArtifactID = fieldID};

        List<DisplayableObjectIdentifier> availableParents = await choiceManager.AvailableParentsListAsync(workspaceID, fieldIdentifier);

        // Get existing choice information

        ChoiceResponse choiceResponse = await choiceManager.ReadAsync(workspaceID, choiceID);

        // Move choice under different parent choice

        ChoiceRequest choiceRequest = new ChoiceRequest()

        {

            Name = choiceResponse.ObjectIdentifier.Name,

            Color = choiceResponse.Color.ID,

            Order = choiceResponse.Order,

            Parent =  availableParents.FirstOrDefault(parent => parent.Name == "Important")

        };

        await choiceManager.UpdateAsync(workspaceID, choiceID, choiceRequest);

    }

}
```

## Update a choice with a version check

The following code sample uses the UpdateAsync() method modify information on a choice. It performs a version check before applying the update. The update succeeds if the version token in the request matches that of the choice object in the environment. If the version tokens do not match, a status code 409 Conflict is returned.

After the choice is created, you cannot change the field associated with it.

View code sample Copy

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
public async Task UpdateSingleChoiceWithVersionCheckAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int choiceID = 1104642;

        // retrieve available parents

        List<DisplayableObjectIdentifier> availableParents = await choiceManager.AvailableParentsListAsync(workspaceID, choiceID);

        // Get existing choice information

        ChoiceResponse choiceResponse = await choiceManager.ReadAsync(workspaceID, choiceID);

        // Move choice under different parent choice

        ChoiceRequest choiceRequest = new ChoiceRequest()

        {

            Name = choiceResponse.ObjectIdentifier.Name,

            Color = choiceResponse.Color.ID,

            Order = choiceResponse.Order,

            Parent = availableParents.Find(parent => parent.Name == "Important")

        };

        // Version token is generated from the last-modified-on time stamp.

        // If the choice object has been modified since we performed

        // the read this updated will fail.

        string versionToken = choiceResponse.LastModifiedOn.Ticks.ToString(CultureInfo.InvariantCulture);

        await choiceManager.UpdateAsync(workspaceID, choiceID, choiceRequest, versionToken);

    }
```

## Update multiple choices

The following code sample illustrates how to use the UpdateAsync() method to modify multiple choices as a mass operation.

View code sample Copy

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
public async Task UpdateMultipleChoicesAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int fieldID = 1104632;

        int choiceID1 = 1104640;

        int choiceID2 = 1104641;

        // Get existing choice information

        ChoiceResponse choice1 = await choiceManager.ReadAsync(workspaceID, choiceID1);

        ChoiceResponse choice2 = await choiceManager.ReadAsync(workspaceID, choiceID2);

        MassUpdateChoiceRequest[] massUpdateRequest = new MassUpdateChoiceRequest[]

        {

            new MassUpdateChoiceRequest()

            {

                ObjectIdentifier = choice1.ObjectIdentifier,

                Name = "Privileged",

                Color = choice1.Color.ID

            },

            new MassUpdateChoiceRequest()

            {

                ObjectIdentifier = choice2.ObjectIdentifier,

                Name = "Confidential",

                Color = choice2.Color.ID

            }

        };

        MassActionChoiceResponse response = await choiceManager.UpdateAsync(workspaceID, massUpdateRequest);

    }

}
```

## Delete a choice

The following code sample illustrates how to delete a single choice asynchronously.

View code sample Copy

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
public async Task DeleteChoiceAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int choiceID = 1104642;

        await choiceManager.DeleteAsync(workspaceID, choiceID);

    }

}
```

## Delete multiple choices

The following code sample illustrates how to mass delete choices asynchronously using the DeleteAsync() method.

View code sample Copy

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
public async Task DeleteMultipleChoicesAsync()

{

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        MassDeleteChoiceRequest massDelete = new MassDeleteChoiceRequest()

        {

            ChoiceIDs = new List<ObjectIdentifier>()

            {

                new ObjectIdentifier() {ArtifactID = 1104641},

                new ObjectIdentifier() {ArtifactID = 1104642},

                new ObjectIdentifier() {ArtifactID = 1104643},

            }

        };

        await choiceManager.DeleteAsync(workspaceID, massDelete);

    }

}
```

## Sort choices

The following code sample illustrates how to sort choices under the specified field in the specified direction using the SortAsync () method.

View code sample Copy

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
public async Task SortChoicesAsync()

{

    // Assuming the choices under this field are organized as follows:

    // + Privileged

    // + Important

    //      + Critical

    //      + Very

    //      + Somewhat

    //

    // After this ascending sort request they will be organized as follows:

    // + Important

    //      + Critical

    //      + Somewhat

    //      + Very

    // + Privileged

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int choiceID = 1104635;

        MassActionChoiceResponse sortResponse = await choiceManager.SortAsync(workspaceID, choiceID, sortType: SortDirection.Ascending);

    }

}
```

## Move choices to start or end of list

The following code sample illustrates how to move a set of choices to either the start or end of the list of choices under a specific field using the MoveAsync() method by passing it the WorkspaceID, ChoiceObjectIdentifiers, and MoveListTo parameters.

View code sample Copy

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

public async Task MoveChoiceListAsync()

{

    // Assuming the choices under this field were organized as follows:

    // + Privileged

    // + Important

    // + A

    // + B

    // + C

    //

    // After this sort request they will be organized as follows:

    // + C

    // + B

    // + A

    // + Privileged

    // + Important

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int fieldID = 1104635;

        ObjectIdentifier[] choicesToMove = new ObjectIdentifier[]

        {

            new ObjectIdentifier() {ArtifactID = 1104650}, // Choice "A"

            new ObjectIdentifier() {ArtifactID = 1104651}, // Choice "B"

            new ObjectIdentifier() {ArtifactID = 1104652}, // Choice "C"

        };

        MassActionChoiceResponse sortResponse = await choiceManager.MoveAsync(workspaceID, fieldID, choicesToMove, ChoiceMoveType.Beginning);

    }

}
```

## Move choices after a specific choice in a list

The following code sample illustrates how to move a choice after a specific choice in a list of choices using the MoveAsync() method by passing it the WorkspaceID, ChoiceObjectIdentifiers, and ChoiceID parameters.

View code sample Copy

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
public async Task MoveChoiceListAsync()

{

    // Assuming the choices under this field were organized as follows:

    // + C

    // + B

    // + A

    //

    // After this sort request they will be organized as follows:

    // + A

    // + B

    // + C

    using (IChoiceManager choiceManager = _serviceFactory.CreateProxy<IChoiceManager>())

    {

        int workspaceID = 1022092;

        int fieldID = 1104635;

        ObjectIdentifier choiceIdentifier = new ObjectIdentifier() {ArtifactID = 1104650 }; // Choice "A"

        ObjectIdentifier[] choicesToMove = new ObjectIdentifier[]

        {

            new ObjectIdentifier() {ArtifactID = 1104651}, // Choice "B"

            new ObjectIdentifier() {ArtifactID = 1104652}, // Choice "C"

        };

        MassActionChoiceResponse sortResponse = await choiceManager.MoveAsync(workspaceID, fieldID, choicesToMove, choiceIdentifier);

    }

}
```

## Retrieve a list of available parents

You can retrieve a list of available parents as follows:

- Retrieve parents for a specific choice by passing the AvailableParentsListAsync() method a WorkspaceID, ChoiceGuid, and ChoiceID. See the code sample for Update a choice without a version check .

- Retrieve parents for a specific field by passing the AvailableParentsListAsync() method a WorkspaceID and FieldIdentifier. See the code sample for Update a choice without a version check .

## Retrieve a list of available colors

Use the GetColorsListAsync() method to retrieve a list of colors that can be assigned to choices. See the code sample for Create a single choice .
