---
title: "Troubleshooting Processing SDK errors"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Troubleshooting_Processing_API_errors.htm
collection: developer
fetched_at: 2026-06-22T06:30:27+00:00
sha256: f29f45368ad273e74840c6762e182ada638e3f223de47eab4ecc32818dd2950f
---

Troubleshooting Processing SDK errors

# Troubleshooting Processing SDK errors

You can use the following information to troubleshoot your custom processing workflows implemented with the Processing API.

## IProcessingJobManager method call errors

Job submission in progress

Error Message Job submission is currently in progress for processing set <Processing set identifier>.

Description Relativity returns this error when you attempt to run a job that has already been submitted for discovery.

Resolution To avoid seeing this error when programmatically creating and submitting processing sets, ensure that you don't submit them for discovery at or near the same time.

API call IProcessingJobManager.SubmitDiscoveryJobsAsync() method

Can't run processing set

Error Message You can't run a processing set that has no data sources.

Description A discovery job for a processing set must not have data sources associated with it.

Resolution Add a data source to the processing set and then begin discovery.

API call IProcessingJobManager.SubmitDiscoveryJobsAsync() method

Can't access worker manager server

Error Message The worker manager server isn't accessible.

Description Relativity can’t connect to the worker manager server, which is the Invariant queue manager.

Resolution Check the Servers tab in Relativity to verify that the worker manager server is active.

API call IProcessingJobManager.SubmitDiscoveryJobsAsync() method

Processing set already discovered

Error Message The processing set has already been discovered.

Description After a processing set completes discovery, you can't run additional discovery jobs on it. You can only run one discovery job per processing set.

Resolution To rediscover the files, create a new processing set for them.

API call IProcessingJobManager.SubmitDiscoveryJobsAsync() method

Processing set canceled

Error Message This processing set has been canceled. Please create a new processing set.

Description You can't run a discovery job on a canceled processing set.

Resolution To discover these files, create a new processing set.

API call IProcessingJobManager.SubmitDiscoveryJobsAsync() method

Can't retrieve processing set

Error Message Unable to retrieve the processing set.

Description Relativity can't locate the processing set based on the Artifact IDs provided for the workspace and processing set.

Resolution Ensure that the Artifact IDs for the workspace and processing set are correct.

API call IProcessingJobManager.SubmitDiscoveryJobsAsync() method or IProcessingJobManager.SubmitCancelJobAsync() method.

Can't cancel a processing set that has no data sources

Error Message You can't cancel a processing set that has no data sources.

Description

If no data sources have been created for a processing set, then there is no job to cancel.

Resolution Delete the processing set or don't take any action.

API call IProcessingJobManager.SubmitCancelJobAsync() method

## IProcessingSetManager method call errors

Can't access worker manager server

Error Message The worker manager server is not accessible.

Description Relativity can’t connect to the worker manager server that is the Invariant queue manager.

Resolution Check the Servers tab in Relativity to verify that the worker manager server is active.

API call IProcessingSetManager.SaveAsync() method

Can't update a canceled processing set

Error Message You can't update a canceled processing set.

Description You can't update a canceled processing set.

Resolution To discover these files, create a new processing set.

API call IProcessingSetManager.SaveAsync() method

Can't change processing profile

Error Message You can't change the Processing Profile once a job has been run.

Description After the discovery job has started to run, you can't modify its processing profile .

Resolution To use a different processing profile for a group of files, create a new processing set and add the files to it as data sources.

API call IProcessingSetManager.SaveAsync() method

Can't edit a processing set

Error Message You can't edit a processing set while it is running.

Description You are attempting to edit a discovery job that is in progress.

Resolution Wait for the discovery job to finish, and then edit the processing set.

API call IProcessingSetManager.SaveAsync() method

## IProcessingDataSourceManager method call errors

Can't add data source - no resource pool association

Error Message You can't add this data source because it is not associated with the resource pool.

Description The resource pool in a workspace must have access to the path used when creating a data source.

Resolution Add the path in the Processing Source Location field for the resource pool associated with the workspace.

API call IProcessingDataSourceManager.SaveAsync() method

Can't add data source - processing set canceled

Error Message You can't add a data source because the processing set has been canceled.

Description You can't add a data source to a canceled processing set.

Resolution Create a new processing set.

API call IProcessingDataSourceManager.SaveAsync() method

Can't edit data source

Error Message You can't edit the data source because a job is already in the queue for the processing set.

Description After a processing job is added to the queue, the data source can't be modified.

Resolution Wait for the processing job to finish, and then update the data source.

API call IProcessingDataSourceManager.SaveAsync() method

Can only edit data source name

Error Message You can only edit the Name field on this data source because the processing set has already been published.

Description After a data source is published, you only edit its Name field.

Resolution Edit only the name of the data source.

API call IProcessingDataSourceManager.SaveAsync() method

Can only edit name, numbering prefix, destination folder, and order

Error Message You can only edit the Name, Document numbering prefix, Destination folder, or Order field on this data source because the processing set has already been discovered.

Description After the data source is discovered, you can only edit Name, Document Numbering Prefix, Destination Folder, and Order fields.

Resolution Edit only the Name, Document Numbering Prefix, Destination Folder, or Order fields.

API call IProcessingDataSourceManager.SaveAsync() method

Can't add data source - job in queue

Error Message You can't add a data source because a job is already in the queue for the processing set.

Description When a processing set has a running job, you can't add a data source to it.

Resolution Create a new processing set, and then add the data source to this set.

API call IProcessingDataSourceManager.SaveAsync() method

Can't add data source - processing set already discovered

Error Message You can't add a data source because the processing set has already been discovered.

Description After a processing set has finished discovery, you can't add a data source to it.

Resolution Create a new processing set, and then add a data source to it.

API call IProcessingDataSourceManager.SaveAsync() method

Can't reset IsStartNumberVisible property due to data source setting

Error Message IsStartNumberVisible must be set to true because the data source was previously saved with IsStartNumberVisible set to true.

Description After you set IsStartNumberVisible property on a data source to true, you can't update the value on this property to false. This requirement ensures that Relativity consistently displays the Start Number field in the UI after you initially added it.

Resolution None

API call IProcessingDataSourceManager.SaveAsync() method

Can't reset IsStartNumberVisible property due to StartNumber setting

Error Message When StartNumber has a value, IsStartNumberVisible must be set to true.

Description When creating or editing a data source, you can't set the IsStartNumberVisible property to false or null if the StartNumber property contains a value.

Resolution None

API call IProcessingDataSourceManager.SaveAsync() method

Can't set StartNumber to negative number

Error Message When StartNumber has a value, the value must be greater than zero.

Description You can't set the StartNumber number property to zero or a negative number

Resolution Change the value in the StartNumber property to a positive number.

API call IProcessingDataSourceManager.SaveAsync() method

StartNumber property contains too many digits

Error Message StartNumber must fit in NumberOfDigits. This DataSource uses a ProcessingProfile with NumberOfDigits = {<value>}

Description The number in the StartNumber property exceeds the value specified in theNumberOfDigits property on the processing profile. In the Relativity UI, you can set the Number of Digits field on the Processing Profile layout. For more information, see Processing profiles on the Relativity Documentation site.

Resolution We recommend using auto numbering. You can also clear the number from the Start Number field in the Relativity UI, or set the StartNumber property to null through the Processing API.

API call IProcessingDataSourceManager.SaveAsync() method
