---
title: "field"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/field.htm
collection: developer
fetched_at: 2026-06-22T06:32:31+00:00
sha256: 2017bfe9eb606dc0c1a29a183e65c3254f5bf2158acfd5dc723811eaa58ad296
---

field Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# field

This tag allows you to reference Relativity case fields.

### Hierarchy

- script

- input

- field

### Syntax

Copy

```text
1
2
3
4
5

<field id = string

     name = string>

     <!-- children -->

 </field>
```

### Attributes

Name Description Data Type Required

id determines how the field is referenced in the SQL action section of the script. string yes

name determines how the field appears to the user when the Relativity script runs. string yes

required the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required. Boolean no

### Children

Name Description

filters the types of fields in the drop-down menu are designated by a filter. This allows you to easily select the correct case field.

### Remarks

The field input allows you to reference the Relativity work space fields. Each field input must be assigned a name and an ID attribute.

Each field in the input is entered using XML. It contains two attributes and a filter sub-element.

### Example

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
<script>

    <name>Populate Parent ID to Child</name>

      <version>2</version>

      <key>F385B552-70E1-A9B8-9DC1-9AE9309EDF49</key>

    <description>This is a workspace-level Relativity script that propagates the Document ID of the parent document to any children of that document.</description>

    <category>Case Functionality</category>

    <input>

        <field id="GROUP_ID" name="Group Identifier field:">

            <filters>

                <category>5</category>

            </filters>

        </field>

        <field id="UPDATE_FLAG" name="Document to be updated flag:">

            <filters>

                <type>3</type>

                <category>0</category>

            </filters>

        </field>

        <field id="ITEM_ID" name="Parent ID source:">

            <filters>

                <type>0</type>

                <type>1</type>

            </filters>

        </field>

        <field id="FIELD_PROPAGATE" name="Parent ID destination:">

            <filters>

                <type>0</type>

                <type>1</type>

            </filters>

        </field>

    </input>

    <action returns="table" timeout="indefinite"><![CDATA[



    --do not allow user to select artifact id to overwrite

    IF '#FIELD_PROPAGATE#' = '[ArtifactID]'

        RAISERROR ('ArtifactID can not be overwritten.', 16, 1)

    ELSE IF '#FIELD_PROPAGATE#' = '#ITEM_ID#'

        RAISERROR ('Item ID can not be overwritten. Please choose seperate field for propagation.', 16, 1)

  ELSE

    BEGIN

           Select A.ArtifactID as ArtifactID, A.#GROUP_ID# AS GroupIdentifier, A.#ITEM_ID# as DocumentIdentifier

        INTO #SASPopulateParentIdTable

        From Document A

        Where 1 = 0

        INSERT INTO #SASPopulateParentIdTable (ArtifactID, GroupIdentifier,DocumentIdentifier)

        SELECT MIN(A.ArtifactID) as ArtifactID, A.#GROUP_ID# AS GroupIdentifier,''''

        FROM eddsdbo.DOCUMENT A (NOLOCK)

        WHERE A.#UPDATE_FLAG# = 1

        GROUP BY A.#GROUP_ID#

        update t

        Set t.DocumentIdentifier = D.#ITEM_ID#

        FROM #SASPopulateParentIdTable t (NOLOCK)

        INNER JOIN Document D (NOLOCK) on D.ArtifactID = t.ArtifactID

        CREATE UNIQUE CLUSTERED INDEX IX_PopulateParentID_GroupIDArtifactID ON #SASPopulateParentIdTable ([GroupIdentifier] ASC,[ArtifactID] ASC)

        UPDATE D

        SET D.#FIELD_PROPAGATE# = K.DocumentIdentifier

        FROM Document D (NOLOCK)

        INNER JOIN #SASPopulateParentIdTable K ON D.#GROUP_ID# = K.GroupIdentifier

        WHERE K.ArtifactID != D.ArtifactID



        SELECT D.ArtifactID, D.#ITEM_ID#, D.#GROUP_ID#, D.#FIELD_PROPAGATE#

        FROM Document D (NOLOCK) INNER JOIN #SASPopulateParentIdTable K ON D.#GROUP_ID# = K.GroupIdentifier

        ORDER BY D.#GROUP_ID#, D.#ITEM_ID#



    END



]]></action>

</script>
```

On this page

- field

-

- Hierarchy

- Syntax

- Attributes

- Children

- Remarks

- Example


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
