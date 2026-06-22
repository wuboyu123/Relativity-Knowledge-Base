---
title: "Support for File fields"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Support_for_File_fields.htm
collection: developer
fetched_at: 2026-06-22T06:31:33+00:00
sha256: baf110d711750c1cd8248aefbc5620745b1916709383dae63894f7a2c2587389
---

Support for File fields Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Support for File fields

You can use the event handler framework to read the contents of a file stream associated with a File field, or to provide a new stream to a File field. In the kCura.EventHandler namespace, you can use the FileValue class to modify or read the contents of file input stream. You can use the properties on this class to get a file name, path, or input stream. Additionally, the FileFieldValue class has properties that you can use to get the ID of a file stored in the database, or the FileValue associated with a field. You use properties on this class to return Boolean values, indicating whether a new file was uploaded to the File field, or a field value was modified.

## Read a File field value

In the kCura.EventHandler namespace, the FileValue class contains a FileStream method, which returns a new file stream. When a Pre Save event handler executes and a user uploaded a new file for a field through the UI, you can use the stream to access to file before storing it in Relativity. Otherwise, you can use the stream to access the file on the Relativity file share.

You need to properly dispose of the file stream after you finish using it.

The following code sample illustrates a Pre Save event handler that reads the value of a stream. It assumes that the layout has a File field on it.

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
public class PreSaveFileFieldExample : kCura.EventHandler.PreSaveEventHandler

{

        public override kCura.EventHandler.Response Execute()

        {

                var fileField = ActiveArtifact.Fields.Cast<kCura.EventHandler.Field>().Where(field => field.FieldTypeID == 9).FirstOrDefault();

                if (fileField != null && !fileField.Value.IsNull)

                {

                        var fileFieldValue = (kCura.EventHandler.FileFieldValue)fileField.Value;

                        using (System.IO.Stream stream = fileFieldValue.FileValue.FileStream)

                        {

                                //Read the value of the stream here.

                        }

                }

                return new kCura.EventHandler.Response() { Success = true };

        }

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

                get { return new kCura.EventHandler.FieldCollection(); }

        }

}
```

## Modify a File field value

You can modify a File field by setting a new file on it. For this update, set the Value property on the FileFieldValue object to a new FileValue object. The constructor for the FileValue object takes a friendly name for the file and an input stream. To clear the value on the File field, set the Value property of the FileFieldValue object to null.

The input stream must be readable and its total length can't exceed 1 GB. Additionally, properly dispose of the input file stream after using it.

The type of the event handler determines how you handle updates to the Value property on the FileFieldValue object:

- Pre Load – You can't modify this property during the execution of a Pre Load event handler. If you attempt to modify the Value property, the system generates an error.

- Pre Save or Copy – The system writes the contents of the input stream to disk in the Relativity file share. It also updates the File field so that it points to the new file.

- Other event handlers – The system ignores any changes made to this property.

The following code sample illustrates a Pre Save event handler that modifies the value of a File field. It encodes the characters in the word Test into a sequence of bytes. Next, it writes these bytes to current stream. The FileValue constructor takes a file name and the current input stream. It uses these values to initialize a new instance of the FileFieldValue class. This new object contains properties that store information about the new file created with the word Test in it. This code assumes that the layout has a File field on it.

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
public class PreSaveFileFieldExample : kCura.EventHandler.PreSaveEventHandler

{

        public override kCura.EventHandler.Response Execute()

        {

                var fileField = ActiveArtifact.Fields.Cast<kCura.EventHandler.Field>().Where(field => field.FieldTypeID == 9).FirstOrDefault();

                if (fileField != null)

                {

                        var fileFieldValue = (kCura.EventHandler.FileFieldValue) fileField.Value;

                        using (var memoryStream = new System.IO.MemoryStream())

                        {

                                var byteArray = System.Text.Encoding.UTF8.GetBytes("Test");

                                memoryStream.Write(byteArray, 0, byteArray.Count());

                                var fileValue = new kCura.EventHandler.FileValue("NewFileTest.txt", memoryStream);

                                fileFieldValue.Value = fileValue;

                        }

                }

                return new kCura.EventHandler.Response() { Success = true };

        }

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

                get { return new kCura.EventHandler.FieldCollection(); }

        }

}
```

## Clear a File field value

You can also set the value of a File field to null. The following code assumes that the layout has a File field on it.

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
public class PreSaveFileFieldExample : kCura.EventHandler.PreSaveEventHandler

{

        public override kCura.EventHandler.Response Execute()

        {

                var fileField = ActiveArtifact.Fields.Cast<kCura.EventHandler.Field>().Where(field => field.FieldTypeID == 9).FirstOrDefault();

                if (fileField != null)

                {

                        var fileFieldValue = (kCura.EventHandler.FileFieldValue) fileField.Value;

                        fileFieldValue.Value = null;

                }

                return new kCura.EventHandler.Response() { Success = true };

        }

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

                get { return new kCura.EventHandler.FieldCollection(); }

        }

}
```

On this page

- Support for File fields

- Read a File field value

- Modify a File field value

- Clear a File field value


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
