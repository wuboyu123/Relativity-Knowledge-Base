---
title: "Object Rule Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/Object_Rule_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:22:50+00:00
sha256: 472d62984c171fb6851ab5a32a78e45373a69db298ed31cfac1174da677363a2
---

Object Rule Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Object Rule Manager (.NET)

You can use object rules to further customize the behavior of the object types that you create. The Object Rule Manager service simplifies this process by supporting CRUD operations on object rules. It also provides helper methods for retrieving information about associative objects, layouts, choices and choice fields used when creating or updating an object rule.

You can also use the Object Rule Manager and other related services through the REST API. For more information, see Object Rule Manager (REST) .

## Fundamentals for managing object rules

Click the following drop-down links to learn about the methods and classes used by the Object Rule Manager.

Object Rule Manager API

The Object Rule Manager API contains the following methods and classes.

#### Methods

The Object Rule Manager API exposes the following methods on the IObjectRuleManager interface in the Relativity.DataVisualization.{versionNumber}.ObjectRules namespace:

-

Create method for each object rule type - adds a new object rule to the specified object type.

Each type of object rule has its own create method, and request class. For a complete list of create methods, see Create an object rule .

- DeleteAsync() method - removes an object rule from an object type in the specified workspace. Its parameters include the Artifact IDs of the workspace and the object rule. This method returns a Task. See Delete an object rule .

- GetAvailableAssociatedObjectsAsync() method - retrieves a list of associated objects that can be used with an object rule on a specific object type. See Retrieve choices, choice fields, layouts, or associated objects .

- GetAvailableChoiceFieldsAsync() method - retrieves a list of choice fields that can be associated with an object rule on a specific object type. See Retrieve choices, choice fields, layouts, or associated objects .

- GetAvailableChoicesAsync() method - retrieves a list of choices that can be associated with an object rule on a specific object type. See Retrieve choices, choice fields, layouts, or associated objects .

- GetAvailableLayoutsAsync() method - retrieves a list of layouts that can be associated with an object rule on a specific object type. See Retrieve choices, choice fields, layouts, or associated objects .

- GetAvailableSingleChoiceFieldsAsync() method - retrieves a list of single choices fields that can be associated with an object rule on a specific object type. See Retrieve choices, choice fields, layouts, or associated objects .

- MassDeleteAsync() method - removes multiple object rules across different object types. See Delete multiple object rules .

- ReadAsync() method - retrieves information about an object rule, including its name, the object type associated with the rule, and other properties.

- Update method for each object rule type - modifies the properties of an object rule, such as its name, associated object type, and others.

Each type of object rule has its own update method, and request class. For a complete list of update methods, see Update an object rule .

#### Classes

The Object Rule Manager API includes the following classes and enumeration available in the Relativity.DataVisualization.{versionNumber}.ObjectRules.Models namespace:

- Request class for each object rule type - represents the data used to create or update an object type. Each create and update method takes an object of this type.

- ObjectRuleResponse class - represents the results of a read operation. Its properties include name, the object type associated with the rule, and others.

## Guidelines for the Object Rule Manager API

Review the following guidelines for the Object Rule Manager service:

- Use the Object Rule Manager service to work with the same object rule types available through the Relativity UI. For general information about object rules, see Adding an object rule . View a list of available object rules

- Choice behavior - controls whether the users can add, delete, or rename choices for fields.

- Custom single object add link visibility - controls the availability of the Add link button used to add RDO instances to existing custom single objects from a layout.

- Default layout - determines whether the user sees the default or any layout for the object type.

- Default layout on new - determines the layout displayed when a user creates a new custom object.

- Global button visibility - controls the visibility of specific buttons or action options for an object type.

- Mass action visibility - controls the visibility of buttons for the mass operations for an object type.

- New button override - override the page displayed when the New button is clicked by specifying a custom button label and page URL.

- Sub-list button visibility - controls the display of the buttons for child and associative object lists.

- Override edit link URL - override the page displayed when the Edit link is clicked by specifying custom link text and a page URL.

- Override view link URL - override the page displayed when the View link is clicked by specifying custom link text and a page URL.

- Use the helper methods to retrieve information that you need when creating or updating an object rule. See the following table for suggested uses.

Create or update this object rule Use these helper methods Compares to this UI field

Choice Behavior

Choice field methods Field

Default Layout

Layout methods Action

Choice field methods Field

Choice method Value

Default Layout on New

Layout methods Action

Sub-List Button Visibility

Choice field methods Field

Choice method Value

Associated object methods Associative/Child Object

- If a call to a helper method returns an empty list, you can't create that object rule on that object type.

- To attach an object rule, the object type must be an RDO and non-system object, or a document object type.

- Use -1 for the workspace ID when you want to indicate the admin-level context.

- To retrieve the Artifact ID of an object rule, use the Object Manager Service. For more information, see Object Manager (.NET) .

## Create an object rule

You can create object rules by using the methods available on the IObjectRuleManager interface. For general information about object rules, see Adding an object rule .

Click the following drop-down links to view sample code for sub-list visibility, choices, and layouts rules. For more information about create methods, see the IObjectRuleManager interface in the Relativity.DataVisualization.{versionNumber}.ObjectRules namespace.

View a list of available object rules and their create methods

- Choice behavior Copy

```text
1
Task<int> CreateChoiceBehaviorAsync(int workspaceID, ChoiceBehaviorRuleRequest objectRuleRequest)
```

- Custom single object add link visibility Copy

```text
1
Task<int> CreateCustomSingleObjectAddLinkVisibilityAsync(int workspaceID, CustomSingleObjectAddLinkVisibilityRuleRequest objectRuleRequest)
```

- Default layout Copy

```text
1
Task<int> CreateDefaultLayoutAsync(int workspaceID, DefaultLayoutRuleRequest objectRuleRequest)
```

- Default layout on new Copy

```text
1
Task<int> CreateDefaultLayoutOnNewAsync(int workspaceID, DefaultLayoutOnNewRuleRequest objectRuleRequest)
```

- Global button visibility Copy

```text
1
Task<int> CreateGlobalButtonVisibilityAsync(int workspaceID, GlobalButtonVisibilityRuleRequest objectRuleRequest)
```

- Mass action visibility Copy

```text
1
Task<int> CreateMassActionVisibilityAsync(int workspaceID, MassActionVisibilityRuleRequest objectRuleRequest)
```

- New button override Copy

```text
1
Task<int> CreateNewButtonOverrideAsync(int workspaceID, NewButtonOverrideRuleRequest objectRuleRequest);
```

- Sub-list button visibility Copy

```text
1
Task<int> CreateSubListButtonVisibilityAsync(int workspaceID, SubListButtonVisibilityRuleRequest objectRuleRequest)
```

- Override edit link URL Copy

```text
1
Task<int> CreateOverrideEditLinkAsync(int workspaceID, OverrideEditLinkRuleRequest objectRuleRequest)
```

- Override view link URL Copy

```text
1
Task<int> CreateOverrideViewLinkAsync(int workspaceID, OverrideViewLinkRuleRequest objectRuleRequest)
```

Create a sub-list button visibility rule

The following code sample illustrates how to instantiate a SubListButtonVisibilityRuleRequest object with properties specified for the new object rule. To create the rule, call the CreateSubListButtonVisibilityAsync() method by passing the Artifact ID of workspace where you want to add the rule, and the SubListButtonVisibilityRuleRequest instance.

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
public static async Task CreateSublistButtonVisibilityRule_Async(")"{

   int workspaceId = 1018486;

    int parentArtifactId = 101456834;

    int fieldId = 1035231;

    int choiceId = 1938203;

    int sublistObjectId = 1832739;

    int applicationId = 1035699;



    SubListButtonVisibilityRuleRequest request = new SubListButtonVisibilityRuleRequest{

      "Name =""Test Object Rule Request",

      "ShowNew = false",

      "ShowDelete = false",

      "ShowLink = false",

      "ShowUnlink = true",

      "ObjectType = new DisplayableObjectTypeIdentifier"{

         "ArtifactID = parentArtifactId"

      },

      "Field = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = fieldId"

         }

      },

      "Choice = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = choiceId"

         }

      },

      "SubListObject = new Securable<DisplayableObjectTypeIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = sublistObjectId"

         }

      },

      "RelativityApplications = new List<ObjectIdentifier>"{

         "new ObjectIdentifier"{

            "ArtifactID = applicationId"

         }

      }

   };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>()){

      "try"{

         "int newRuleArtifactId = await objectRuleManager.CreateSubListButtonVisibilityAsync(workspaceId",

         "request);

            string info = string.Format(""Created object rule with Artifact ID {0}",

         "newRuleArtifactId);

            Console.Write(info);"

      }"catch (Exception ex)"{

         "Console.WriteLine(string.Format(""An error occurred: {0}",

         "ex.Message));"

      }

   }

}
```

Create a choice rule

The following code sample illustrates how to instantiate a ChoiceBehaviorRuleRequest object with properties specified for the new object rule. To create the rule, call the CreateChoiceBehaviorAsync() method by passing the Artifact ID of workspace where you want to add the rule, and the ChoiceBehaviorRuleRequest instance.

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
public static async Task CreateChoiceBehavior_Async(")"{

   int workspaceId = 1018486;

    int parentArtifactId = 1456834;

    int fieldId = 1035231;

    int applicationId = 1035699;



    ChoiceBehaviorRuleRequest request = new ChoiceBehaviorRuleRequest{

      "Name =""Test Choice Behavior Rule",

      "ObjectType = new DisplayableObjectTypeIdentifier"{

         "ArtifactID = parentArtifactId"

      },

      "Field = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = fieldId"

         }

      },

      "ShowAdd = true",

      "ShowDelete = false",

      "ShowRename = false",

      "RelativityApplications = new List<Securable<ObjectIdentifier>>"{

         "new ObjectIdentifier"{

            "ArtifactID = applicationId"

         }

      }

   };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>()){

      "try"{

         "int newRuleArtifactId = await objectRuleManager.CreateChoiceBehaviorAsync(workspaceId",

         "request);

            string info = string.Format(""Created object rule with Artifact ID {0}",

         "newRuleArtifactId);

            Console.Write(info);"

      }"catch (Exception ex)"{

         "Console.WriteLine(string.Format(""An error occurred: {0}",

         "ex.Message));"

      }

   }

}
```

Create a layout rule

The following code sample illustrates how to instantiate a DefaultLayoutRuleRequest object with properties specified for the new object rule. To create the rule, call the CreateDefaultLayoutAsync() method by passing the Artifact ID of workspace where you want to add the rule, and the DefaultLayoutRuleRequest instance.

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
public static async Task CreateDefaultLayout_Async(")"{

   int workspaceId = 1018486;

    int parentArtifactId = 1456834;

    int fieldId = 1035231;

    int choiceId = 1938203;

    int layoutId = 1837293;

    int applicationId = 1035699;



    DefaultLayoutRuleRequest request = new DefaultLayoutRuleRequest{

      "Name =""Test Object Rule Request",

      "ObjectType = new DisplayableObjectTypeIdentifier"{

         "ArtifactID = parentArtifactId"

      },

      "AllowLayoutChange = true",

      "Field = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = fieldId"

         }

      },

      "Choice = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = choiceId"

         }

      },

      "Layout = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = layoutId"

         }

      },

      "RelativityApplications = new List<ObjectIdentifier>"{

         "new ObjectIdentifier"{

            "ArtifactID = applicationId"

         }

      }

   };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>()){

      "try"{

         "int newRuleArtifactId = await objectRuleManager.CreateDefaultLayoutAsync(workspaceId",

         "request);

            string info = string.Format(""Created object rule with Artifact ID {0}",

         "newRuleArtifactId);

            Console.Write(info);"

      }"catch (Exception ex)"{

         "Console.WriteLine(string.Format(""An error occurred: {0}",

         "ex.Message));"

      }

   }

}
```

## Read an object rule

You can retrieve basic information about an object rule or extended information, which also includes operations that you have permissions to perform on the object rule. If you want to return extended information, use the overloaded method by passing Boolean values set to true for additional metadata and permissions as follows:

Copy

```text
1
ObjectRuleResponse response = await objectRuleManager.ReadAsync(workspaceId, objectRuleArtifactId, true, true);
```

The following code sample illustrates how to call the ReadAsync() method by passing only the Artifact IDs of the workspace and the object rule. Consequently, it returns only basic information.

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
public static async Task Read_Async()

{

    int workspaceId = 1018486;

    int objectRuleArtifactId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            ObjectRuleResponse response = await objectRuleManager.ReadAsync(workspaceId, objectRuleArtifactId);

            string info = string.Format("Read object rule {0} with Artifact ID {1}", response.Name, response.ArtifactId);

            Console.Write(info);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Update an object rule

You can update object rules by using the methods available on the IObjectRuleManager interface. All object rules have an overloaded update method called by passing the Artifact IDs of a workspace and the object rule, the appropriate request object for the rule type, and an optional DateTime object.

To get the Artifact ID of an object rule, use the ReadAsync() method on the Object Manager (.NET) .

When you want to restrict the update of an object rule to the date that it was last modified, pass the value of LastModifiedOn property as an argument to one of the overloaded update methods. You can get the value of this property from an ObjectRuleResponse object, which is returned by the ReadAsync() method.

Click the following drop-down links to view sample code for sub-list visibility, choices, and layouts rules. For more information about update methods, see the IObjectRuleManager interface in the Relativity.DataVisualization.{versionNumber}.ObjectRules namespace.

View a list of available object rules and their overloaded update methods

You can find general information about available object rules in Adding an object rule .

- Choice behavior Copy

```text
1
2
3
4
5
Task UpdateChoiceBehaviorAsync(

    int workspaceID,

    int objectRuleID,

    ChoiceBehaviorRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateChoiceBehaviorAsync(

    int workspaceID,

    int objectRuleID,

    ChoiceBehaviorRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Custom single object add link visibility Copy

```text
1
2
3
4
5
Task UpdateCustomSingleObjectAddLinkVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    CustomSingleObjectAddLinkVisibilityRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateCustomSingleObjectAddLinkVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    CustomSingleObjectAddLinkVisibilityRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Default layout Copy

```text
1
2
3
4
5
Task UpdateDefaultLayoutAsync(

    int workspaceID,

    int objectRuleID,

    DefaultLayoutRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateDefaultLayoutAsync(

    int workspaceID,

    int objectRuleID,

    DefaultLayoutRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Default layout on new Copy

```text
1
2
3
4
5
Task UpdateDefaultLayoutOnNewAsync(

    int workspaceID,

    int objectRuleID,

    DefaultLayoutOnNewRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateDefaultLayoutOnNewAsync(

    int workspaceID,

    int objectRuleID,

    DefaultLayoutOnNewRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Global button visibility Copy

```text
1
2
3
4
5
Task UpdateGlobalButtonVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    GlobalButtonVisibilityRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateGlobalButtonVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    GlobalButtonVisibilityRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Mass action visibility Copy

```text
1
2
3
4
5
Task UpdateMassActionVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    MassActionVisibilityRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateMassActionVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    MassActionVisibilityRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- New button override Copy

```text
1
2
3
4
5
Task UpdateNewButtonOverrideAsync(

    int workspaceID,

    int objectRuleID,

    NewButtonOverrideRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateNewButtonOverrideAsync(

    int workspaceID,

    int objectRuleID,

    NewButtonOverrideRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Sub-list button visibility Copy

```text
1
2
3
4
5
Task UpdateSubListButtonVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    SubListButtonVisibilityRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateSubListButtonVisibilityAsync(

    int workspaceID,

    int objectRuleID,

    SubListButtonVisibilityRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Override edit link URL Copy

```text
1
2
3
4
5
Task UpdateOverrideEditLinkAsync(

    int workspaceID,

    int objectRuleID,

    OverrideEditLinkRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateOverrideEditLinkAsync(

    int workspaceID,

    int objectRuleID,

    OverrideEditLinkRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

- Override view link URL Copy

```text
1
2
3
4
5
Task UpdateOverrideViewLinkAsync(

    int workspaceID,

    int objectRuleID,

    OverrideViewLinkRuleRequest objectRuleRequest

)
```

Copy

```text
1
2
3
4
5
6
Task UpdateOverrideViewLinkAsync(

    int workspaceID,

    int objectRuleID,

    OverrideViewLinkRuleRequest objectRuleRequest,

    DateTime lastModifiedOn

)
```

Update a sub-list button visibility rule

The following code sample illustrates how to instantiate a SubListButtonVisibilityRuleRequest object with properties used for updating the object rule. To update the rule, call the UpdateSubListButtonVisibilityAsync() method by passing Artifact IDs of the workspace and object rule, and the SubListButtonVisibilityRuleRequest instance.

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
public static async Task UpdateSubListButtonVisibility_Async(")"{

   int workspaceId = 1018486;

    int parentArtifactId = 1456834;

    int fieldId = 1035231;

    int choiceId = 1938203;

    int layoutId = 1837293;

    int applicationId = 1035699;

    int objectRuleId = 1383730;



    SubListButtonVisibilityRuleRequest request = new SubListButtonVisibilityRuleRequest{

      "Name =""Test Object Rule Request",

      "ObjectType = new DisplayableObjectTypeIdentifier"{

         "ArtifactID = parentArtifactId"

      },

      "AllowLayoutChange = true",

      "Field = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = fieldId"

         }

      },

      "Choice = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = choiceId"

         }

      },

      "Layout = new Securable<ObjectIdentifier>"{

         "Secured = false",

         "Value = new DisplayableObjectTypeIdentifier"{

            "ArtifactID = layoutId"

         }

      },

      "RelativityApplications = new List<ObjectIdentifier>"{

         "new ObjectIdentifier"{

            "ArtifactID = applicationId"

         }

      }

   };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>()){

      "try"{

         "await objectRuleManager.UpdateSubListButtonVisibilityAsync(workspaceId",

         "objectRuleId",

         "request);"

      }"catch (Exception ex)"{

         "Console.WriteLine(string.Format(""An error occurred: {0}",

         "ex.Message));"

      }

   }

}
```

Update a choice rule

The following code sample illustrates how to instantiate a ChoiceBehaviorRuleRequest object with properties used for updating the object rule. To update the rule, call the UpdateChoiceBehaviorAsync() method by passing Artifact IDs of the workspace and object rule, and the ChoiceBehaviorRuleRequest instance.

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
30
31
32
33
34
35
36
37
public static async Task UpdateChoiceBehavior_Async()

{

    int workspaceId = 1018486;

    int parentArtifactId = 1456834;

    int fieldId = 1035231;

    int applicationId = 1035699;

    int objectRuleId = 1383730;



    ChoiceBehaviorRuleRequest request = new ChoiceBehaviorRuleRequest

    {

        Name = "Test Choice Behavior Rule Update",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactID = parentArtifactId },

        Field = new Securable<ObjectIdentifier> {

            Secured = false,

            Value = new DisplayableObjectTypeIdentifier { ArtifactID = fieldId }

        },

        ShowAdd = false,

        ShowDelete = true,

        ShowRename = true,

        RelativityApplications = new List<Securable<ObjectIdentifier>>

        {

            new ObjectIdentifier {ArtifactID = applicationId}

        }

    };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            await objectRuleManager.UpdateChoiceBehaviorAsync(workspaceId, objectRuleId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

Update a layout rule

The following code sample illustrates how to instantiate a DefaultLayoutRuleRequest object with properties used for updating the object rule. To update the rule, call the UpdateDefaultLayoutAsync method by passing Artifact IDs of the workspace and object rule, and the DefaultLayoutRuleRequest instance.

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
public static async Task UpdateLayoutBehavior_Async()

{

    int workspaceId = 1018486;

    int parentArtifactId = 1456834;

    int fieldId = 1035231;

    int choiceId = 1938203;

    int layoutId = 1837293;

    int applicationId = 1035699;

    int objectRuleId = 1383730;



    DefaultLayoutRuleRequest request = new DefaultLayoutRuleRequest

    {

        Name = "Test Object Rule Request",

        ObjectType = new DisplayableObjectTypeIdentifier { ArtifactID = parentArtifactId },

        AllowLayoutChange = true,

        Field = new Securable<ObjectIdentifier>

        {

            Secured = false,

            Value = new DisplayableObjectTypeIdentifier { ArtifactID = fieldId }

        },

        Choice = new Securable<ObjectIdentifier>

        {

            Secured = false,

            Value = new DisplayableObjectTypeIdentifier { ArtifactID = choiceId }

        },

        Layout = new Securable<ObjectIdentifier>

        {

            Secured = false,

            Value = new DisplayableObjectTypeIdentifier { ArtifactID = layoutId }

        },

        RelativityApplications = new List<ObjectIdentifier>

        {

            new ObjectIdentifier { ArtifactID = applicationId }

        }

    };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            await objectRuleManager.UpdateDefaultLayoutAsync(workspaceId, objectRuleId, request);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete an object rule

You can remove an object rule from an object type by calling the DeleteAsync()method, and passing Artifact IDs of a workspace and an object rule to it. See the following code sample:

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
public static async Task Delete_Async()

{

    int workspaceId = 1018486;

    int objectRuleId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            await objectRuleManager.DeleteAsync(workspaceId, objectRuleId);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Delete multiple object rules

You can remove multiple object rules across different object types by making a single call to the MassDeleteAsync() method. Pass the Artifact ID of the workspace and a list containing the Artifact ID for each rule that you want to delete to this method. See the following code sample:

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
public static async Task Delete_Async()

{

    int workspaceId = 1018486;

    int objectRuleId1 = 1039509;

    int objectRuleId2 = 1039525;

    int objectRuleId3 = 1039630;



    List<ObjectIdentifiers> objectRulesToDelete = new List<ObjectIdentifiers> = [ objectRuleId1, objectRuleId2, objectRuleId3];



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            await objectRuleManager.MassDeleteAsync(workspaceId, objectRulesToDelete);

        }

        catch (Exception ex)

        {

            Console.WriteLine(string.Format("An error occurred: {0}", ex.Message));

        }

    }

}
```

## Retrieve choices, choice fields, layouts, or associated objects

When you create or update an object rule, you must provide the Artifact ID of any associative objects, layouts, choices and choice fields that it references. The Object Rule Manager service provides several helper methods that you can use to retrieve the Artifact ID, name, and other information about these objects. For most objects, it includes overloaded methods with following signatures:

- Method signature with workspace ID and Artifact ID parameters - use this method if you have the Artifact ID of the object type.

- Method signature with workspace ID and DisplayableObjectTypeIdentifier object parameters - use this method if you have the user-friendly name of the object type, but not its Artifact ID.

Associated object methods

#### Retrieve with Artifact ID

If you have the Artifact ID of the object type, use the following method to retrieve associated objects for it:

Copy

```text
1
Task<List<SubListObjectIdentifier>> GetAvailableAssociatedObjectsAsync(int workspaceID, int objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableAssociatedObjects_Async()

{

    int workspaceId = 1018486;

    int objectTypeId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<SubListObjectIdentifier> response = await objectRuleManager.GetAvailableAssociatedObjectsAsync(workspaceId, objectTypeId);

            foreach (SubListObjectIdentifier subListIdentifier in response)

            {

                string info = string.Format("Read {0} '{1}' with Artifact ID '{2}'",

                    subListIdentifier.ListType, subListIdentifier.Name, subListIdentifier.ArtifactID);

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

#### Retrieve with Artifact ID or name

If you have the name, GUID, artifact ID, or artifact type ID of the object type, use the following method to retrieve choice fields for it:

Copy

```text
1
Task<List<SubListObjectIdentifier>> GetAvailableAssociatedObjectsAsync(int workspaceID, DisplayableObjectTypeIdentifier objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableAssociatedObjects_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1039509;



    DisplayableObjectTypeIdentifier DisplayableObjectTypeIdentifier = new DisplayableObjectTypeIdentifier { ArtifactID = objectTypeArtifactId };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<SubListObjectIdentifier> response = await objectRuleManager.GetAvailableAssociatedObjectsAsync(workspaceId, DisplayableObjectTypeIdentifier);

            foreach (SubListObjectIdentifier subListIdentifier in response)

            {

                string info = string.Format("Read {0} '{1}' with Artifact ID '{2}'",

                    subListIdentifier.ListType, subListIdentifier.Name, subListIdentifier.ArtifactID);

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

Single choice field methods

#### Retrieve with Artifact ID

If you have the Artifact ID of the object type, use the following method to retrieve single choice fields for it:

Copy

```text
1
Task<List<DisplayableObjectIdentifier>> GetAvailableSingleChoiceFieldsAsync(int workspaceID, int objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableSingleChoiceFields_Async(")"{

   int workspaceId = 1018486;

    int objectTypeId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>()){

      "try"{

         "List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableSingleChoiceFieldsAsync(workspaceId",

         "objectTypeId);

            foreach (DisplayableObjectIdentifier singleChoiceField in response)"{

            "string info = string.Format(""Read single choice field {0} with Artifact ID {1}",

            "singleChoiceField.Name",

            "singleChoiceField.ArtifactID);

                Console.Write(info);"

         }

      }"catch (Exception ex)"{

         "Console.WriteLine(string.Format(""An error occurred: {0}",

         "ex.Message));"

      }

   }
```

#### Retrieve with Artifact ID or name

If you have the name, GUID, artifact ID, or artifact type ID of the object type, use the following method to retrieve single choice field methods for it:

Copy

```text
1
CopyTask<List<DisplayableObjectIdentifier>> GetAvailableSingleChoiceFieldsAsync(int workspaceID, DisplayableObjectTypeIdentifier objectTypeID)
```

The following code sample illustrates how to use this method:

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
{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1039509;



    DisplayableObjectTypeIdentifier objectTypeId = new DisplayableObjectTypeIdentifier { ArtifactID = objectTypeArtifactId };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableSingleChoiceFieldsAsync(workspaceId, objectTypeId);

            foreach (DisplayableObjectIdentifier singleChoiceField in response)

            {

                string info = string.Format("Read single choice field {0} with Artifact ID {1}", singleChoiceField.Name, singleChoiceField.ArtifactID);

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

Choice field methods

#### Retrieve with Artifact ID

If you have the Artifact ID of the object type, use the following method to retrieve choice fields for it:

Copy

```text
1
Task<List<DisplayableObjectIdentifier>> GetAvailableChoiceFieldsAsync(int workspaceID, int objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableChoiceFields_Async()

{

    int workspaceId = 1018486;

    int objectTypeId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableChoiceFieldsAsync(workspaceId, objectTypeId);

            foreach (DisplayableObjectIdentifier choiceField in response)

            {

                string info = string.Format("Read choice field {0} with Artifact ID {1}", choiceField.Name, choiceField.ArtifactID);

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

#### Retrieve with Artifact ID or name

If you have the name, GUID, artifact ID, or artifact type ID of the object type, use the following method to retrieve choice fields for it:

Copy

```text
1
Task<List<DisplayableObjectIdentifier>> GetAvailableChoiceFieldsAsync(int workspaceID, DisplayableObjectTypeIdentifier objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableChoiceFields_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1039509;



    DisplayableObjectTypeIdentifier objectTypeId = new DisplayableObjectTypeIdentifier { ArtifactID = objectTypeArtifactId };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableChoiceFieldsAsync(workspaceId, objectTypeId);

            foreach (DisplayableObjectIdentifier choiceField in response)

            {

                string info = string.Format("Read choice field {0} with Artifact ID {1}", choiceField.Name, choiceField.ArtifactID);

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

Choice method

To retrieve a list of choices for an object type, use the following method:

Copy

```text
1
Task<List<DisplayableObjectIdentifier>> GetAvailableChoicesAsync(int workspaceID, int fieldID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableChoices_Async()

{

    int workspaceId = 1018486;

    int fieldId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableChoicesAsync(workspaceId, fieldId);

            foreach (DisplayableObjectIdentifier choice in response)

            {

                string info = string.Format("Read choice {0} with Artifact ID {1}", choice.Name, choice.ArtifactID);

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

Layout methods

#### Retrieve with Artifact ID

If you have the Artifact ID of the object type, use the following method to retrieve layouts for it:

Copy

```text
1
Task<List<DisplayableObjectIdentifier>> GetAvailableLayoutsAsync(int workspaceID, int objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableLayouts_Async()

{

    int workspaceId = 1018486;

    int objectTypeId = 1039509;



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableLayoutsAsync(workspaceId, objectTypeId);

            foreach (DisplayableObjectIdentifier layout in response)

            {

                string info = string.Format("Read layout {0} with Artifact ID {1}", layout.Name, layout.ArtifactID);

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

#### Retrieve with Artifact ID or name

If you have the name, GUID, artifact ID, or artifact type ID of the object type, use the following method to retrieve layouts for it:

Copy

```text
1
Task<List<DisplayableObjectIdentifier>> GetAvailableLayoutsAsync(int workspaceID, DisplayableObjectTypeIdentifier objectTypeID)
```

The following code sample illustrates how to use this method:

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
public static async Task GetAvailableLayouts_Async()

{

    int workspaceId = 1018486;

    int objectTypeArtifactId = 1039509;



    DisplayableObjectTypeIdentifier objectTypeId = new DisplayableObjectTypeIdentifier { ArtifactID = objectTypeArtifactId };



    using (Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager objectRuleManager = serviceFactory.CreateProxy<Relativity.DataVisualization.{versionNumber}.ObjectRules.IObjectRuleManager>())

    {

        try

        {

            List<DisplayableObjectIdentifier> response = await objectRuleManager.GetAvailableLayoutsAsync(workspaceId, objectTypeId);

            foreach (DisplayableObjectIdentifier layout in response)

            {

                string info = string.Format("Read layout {0} with Artifact ID {1}", layout.Name, layout.ArtifactID);

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

On this page

- Object Rule Manager (.NET)

- Fundamentals for managing object rules

- Guidelines for the Object Rule Manager API

- Create an object rule

- Read an object rule

- Update an object rule

- Delete an object rule

- Delete multiple object rules

- Retrieve choices, choice fields, layouts, or associated objects


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
