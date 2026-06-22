---
title: "key"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/key.htm
collection: developer
fetched_at: 2026-06-22T06:32:42+00:00
sha256: 61197e22a3ed01a15d91c3fc3aaa30b84537c585ce8ea02378cd42ffdf562892
---

key

# key

A key is a mechanism used to lock a script within Relativity. If a script has an associated key tag, then it will be locked. You can preview a locked script, but you can't modify it in any way regardless of your permissions. Once a script has been locked, it's no longer possible to edit it. On upgrade to a new version of Relativity, the installer may attempt to deploy new scripts in your Relativity environment. Any new scripts with a higher version and the same key as those in your current instance may be overwritten.

### Hierarchy

- script

- key

### Syntax

Copy

```text
1
2
3
4

<key>

     <!-- string value -->

</key>
```

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

<script>

     <name>Key Example</name>

     <description>This is an example script for using the key element</description>

     <category></category>

     <key>1234-key-456</key>

     <input orientation="horizontal" />

     <display type="itemlist" />

     <action returns="table"><![CDATA[]]></action>

</script>
```

### Edit a locked script

If you want to edit a locked script, preview the script and copy the body. Make your required edits then paste the body into a new script. Make sure you remove the key before saving if you want the script to be editable.
