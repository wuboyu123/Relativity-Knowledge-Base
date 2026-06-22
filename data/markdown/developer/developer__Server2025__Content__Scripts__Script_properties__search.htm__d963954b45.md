---
title: "search"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/search.htm
collection: developer
fetched_at: 2026-06-22T06:32:38+00:00
sha256: b473b5e519e701378832c6bfa8c879b101e61d8fd44c409f82f68d2c6e9942a9
---

search Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# search

This tag, if used, populates a drop-down list of saved searches in the inputs section. The selected search is then converted into the FROM clause of its respective saved search.

### Hierarchy

- script

- input

- search

### Syntax

Copy

```text
1
2
3
4

<search id = string

     name = string>

</search>
```

### Attributes

Name Description Data Type Required

id determines how the field is referenced in the SQL action section of the script. string yes

name determines how the field appears to the user when the Relativity script runs. string yes

### Input

The search input allows you to enter a drop-down list of saved searches. Each search input must be assigned a search ID and name.

In Relativity, all saved searches get turned in SQL statements and those SQL statement are run to retrieve document results. When you select a saved search in the input, the replace value in the scripts turns into the FROM clause in the generated SQL associated with the search.

### Example

The following script illustrates how you can use a saved search in a Relativity script:

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
<script>

                <name>Sample Relativity Script with Saved Search</name>

                <version>1</version>

                <description>This Relativity Script demonstrates how to retrieve values from a selected Saved Search.</description>

                <category>Case Functionality</category>

                <input>

                                <search id="savedSearch" name="Saved Search:" />

                                <field id="identifierField" name="Identifier Field:" required="true">

                                                <filters>

                                                                <category>2</category>

                                                </filters>

                                </field>

                                <field id="updateField" name="Field to Update:" required="true">

                                                <filters>

                                                                <type>0</type>

                                                </filters>

                                </field>

                                <constant id="updateValue" name="Updated Value:" type="text" required="true" />

                                <constant id="artifactIdStart" name="Starting Artifact ID:" type="number" required="true" />

                                <constant id="artifactIdEnd" name="Ending Artifact ID:" type="number" required="true" />

                </input>

                <action returns="table" timeout="1200"><![CDATA[



                --Check for temp table existance

                IF NOT OBJECT_ID('EDDSDBO.RelativityTempTable') IS NULL

                                BEGIN

                                                DROP TABLE EDDSDBO.RelativityTempTable

                                END



                --Create temp table

                CREATE TABLE EDDSDBO.RelativityTempTable

                (

                                DocumentArtifactID INT,

                                #identifierField# varchar(200)

                )

                --Insert all Document Artifact ID's from selected Saved Search

                INSERT INTO

                                EDDSDBO.RelativityTempTable

                SELECT

                                [Document].ArtifactID,

                                NULL

                #savedSearch# AND [Document].ArtifactID BETWEEN #artifactIdStart# AND #artifactIdEnd#

                --Update temp table with Control Number

                UPDATE RT

                SET RT.#identifierField# = DD.#identifierField#

                FROM EDDSDBO.RelativityTempTable RT

                INNER JOIN EDDSDBO.Document DD ON RT.DocumentArtifactID = DD.ArtifactID



                --Update the Fixed Length Field in the temp table for Control Numbers between certain values

                UPDATE D

                SET D.#updateField# = '#updateValue#'

                FROM EDDSDBO.Document D

                INNER JOIN EDDSDBO.RelativityTempTable RTT ON D.ArtifactID = RTT.DocumentArtifactID

                SELECT 'Fields Updated...'



                --Drop temp table

                IF NOT OBJECT_ID('EDDSDBO.RelativityTempTable') IS NULL

                                BEGIN

                                                DROP TABLE EDDSDBO.RelativityTempTable

                                END

                                ]]></action>

</script>
```

When run, a drop-down menu contains a list of all saved searches in the system.

- Select a saved search, an identifier field, a text field to be updated, and specify a string value that the field will be updated to and range of document Artifact IDs.

- The script checks if the EDDSDBO.RelativityTempTable already exists, and if it does, drops it.

- Creates the temp table with Artifact ID and CHAR identifier fields.

- Inserts the Artifact IDs from the saved search and NULL into the temp table based on a range of provided document Artifact IDs.

- Updates the character field in the temp table with the selected identifier field based on a join with the EDDSDBO.Document table.

- Updates the selected character field in the EDDSDBO.Document table to the specified string value based on a joint with the temp table.

- Drops the temp table and displays a confirmation message to the end user.

On this page

- search

-

- Hierarchy

- Syntax

- Attributes

- Input

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
