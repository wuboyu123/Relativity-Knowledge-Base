---
title: "Script properties"
url: https://platform.relativity.com/Server2025/Content/Scripts/Script_properties/Script_properties.htm
collection: developer
fetched_at: 2026-06-22T06:32:19+00:00
sha256: 3bd3bcde2316516c77dfba6e65470b2881b48319dc82c0e55213a034e90c73d4
---

Script properties

# Script properties

Properties are the metadata XML tag attributes used to populate the script information, including the name, description, category, and version. Enter any of these metadata values directly into your XML script. If you don't give a value to the property, it's blank.

The following table lists the available script properties.

Name Type Description

script element the top XML element in the Relativity script body.

name element names (and populates the Name column of) the script.

category element helps you define the script type.

description element used to populate the description column of the script.

key element a key is a mechanism used to lock a script within Relativity.

security element enables you to reference the current user ACL lists in your scripts.

acl element pulls back a list of ACL ID's for the current user based on the attributes values so you can reference them inside a script.

id attribute the ID for the field you want to reference inside the Relativity script.

typeartifactid attribute the Artifact ID for the object type that the ACL ID's are referencing.

typeartifactguid attribute the Artifact Guid for the object that the ACL ID's are referencing.

type attribute the permission type for the ACL ID's.

action element pulls back more than one data table from SQL.

timeout attribute defines how long the script can run. This value is in seconds and defaults to 30 seconds.

returns attribute defines how query results are returned.

displaywarning attribute allows a pop-up warning message to appear when running the script.

allowhtmltagsinoutput attribute allows HTML tags to be interpreted by the browser instead of rendered as markup.

name attribute the name used to reference the scripts in the item list drop-down menu as well as to populate the subreport header when displayed as a report.

version element tracks the internal script version.

display element gives you a place holder to add child attributes like "Assembly", which gives you the ability to add attributes to the overall script.

settings element defines certain attributes about your report. Currently you can define reporttitle.

type attribute declares what data type the output should be when the script is executed.

input element allows you to define the orientation of your report as well as define various attributes about your report.

orientation attribute allows you to determine how the Relativity script's run page's layout renders. Valid values:

constant element values (either static or user input) that get passed into the SQL action section.

id attribute defines how the field or constant is referenced in the script's SQL action section.

name attribute defines how the field or constant appears to the user when the Relativity script runs.

type attribute determines what sorts of input field(s) render on the script run screen.

option attribute limits the available inputs of the constant to the list of options specified. Its entry in the input section is rendered as a drop-down list.

value attribute defines the display value (label) for the option if it is different from the actual value.

required attribute the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required.

sql element populates a drop-down menu with the return value of an inline SQL statement.

id attribute defines how the field is referenced in the SQL action section of the script.

name attribute defines how the field appears to the user when the Relativity script runs.

required attribute the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required.

field element allows you to reference Relativity case fields.

id attribute determines how the field is referenced in the SQL action section of the script.

name attribute determines how the field appears to the user when the Relativity script runs.

required attribute the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required.

filters element the types of fields in the drop-down menu are designated by a filter.

type element defines which Relativity field types appear in the drop-down menu.

category element allows you to narrow the field type to a sub-set, based on a specific attribute.

search element populates a drop-down list of saved searches in the inputs section.

id attribute determines how the field is referenced in the SQL action section of the script.

name attribute determines how the field appears to the user when the Relativity script runs.

required attribute the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required.

searchprovider element populates a drop-down list of search providers in the case.

id attribute determines how the field is referenced in the SQL action section of the script.

name attribute determines how the field appears to the user when the Relativity script runs.

required attribute the acceptable values for this attribute are true and false. If not set, the script interprets it as true. If the input is marked as required, its input section field is rendered as required.

object element populates the specified display type with the current instances of the specified object type.

id attribute determines how the field is referenced in the SQL action section of the script.

name attribute determines how the field appears to the user when the Relativity script runs.

required attribute controls whether or not the object field is required for the script to run.

typeartifactid attribute the Artifact ID of the object field that you want to use inside of the Relativity script

rdoviewartifactid attribute the Artifact ID of the view for the object field that you want to appear inside the Relativity script.

displaytype attribute controls how the object renders inside the Relativity script.

typeartifactguid attribute specifies the object type's Artifact GUID.

rdoviewartifactguid attribute specifies the view's Artifact GUID.
