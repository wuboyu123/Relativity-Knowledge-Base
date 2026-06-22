---
title: "Processing FAQs"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Processing_FAQs.htm
collection: user
fetched_at: 2026-06-22T06:13:41+00:00
sha256: f5d06c26378960d251922e5dc6c911c1a5ee9bda76a7ece4d68f66d4f92b447a
---

Processing FAQs

# Processing FAQs

If you have a question about processing, consult the following FAQs:

Can file names be appended after discovery?

There's currently not a way to append a file name after discovery but prior to publishing.

Can images be reprocessed if they have errors?

As long as the set hasn't been published, if the image reports an error, you can retry the image and/or make corrections to the native and then retry the error.

Does Relativity allow the use of a custom NIST?

There's no official support for a custom NIST list.

Does Relativity process password protected PST or OST files?

Passwords on PST and OST files are bypassed automatically by Relativity.

How do you fix an error after a document is published?

In Relativity 8 and above, you can retry the file again.

For a version of Relativity prior to 8.0, fix the file and then ingest it in its own processing set.

How does processing work with errors?

If you publish a processing set, even documents that have an error associated with them will get a record entered in the Document object/tab, with the Control Number field populated at the very least, even if Relativity was unable to determine anything else about the document. In other words, just because a document has an error during processing doesn't mean that it won't be displayed in the Document list with a control number when you publish the processing set. The only way this doesn't happen is if the error occurs during ingestion and either Relativity is unable to extract the document from a container or the source media is corrupt.

How does Relativity handle calendar metadata?

The processing engine captures all the dates of calendar items. If there is not a field for it in Relativity, this data will end up in the "OtherProps" field.

How does Relativity process audio and video?

Audio and video files are identified, but no metadata (other than basic metadata) or text is extracted from them. They will be marked as unprocessable.

How does processing handle regional setting changes?

To change the worker regional setting (worker time zone/culture), it is best to have no processing jobs running. If a job is running and the regional setting changes, it may affect how imaging and text extraction interpret things such as dates, currency formats, and deduplication on the jobs that are in progress.

How does processing handle time zones?

Discovery is performed on all natives in UTC. Processing uses the timezone as defined in the processing set settings to convert metadata dates and times into the selected timezone. For Daylight Savings, there is a table called dbo.TimeZone in the Invariant database that is used to account for Daylight Savings Time on a year-by-year basis. This way, we always use the accurate DST rule for the given year.

For example, a change to how we observe DST went into effect in 1996, and we have this stored. The TimeZone table also keeps track of all of the half-hour time zones, i.e. parts of India.

Once files are published, are they deleted from the processing source location?

No, there is no alteration to the processing source location. Relativity reads from this intermediate location and copies the files to the Relativity workspace file repository.

What files display in the DeNIST report?

The DeNIST report displays only attachments. You can look at the INVXXXXX database in the DeNIST table to see the individual files.
