---
title: "MonthOfCondition"
url: https://platform.relativity.com/Server2025/Content/RSAPI/Searching_Relativity/MonthOfCondition.htm
collection: developer
fetched_at: 2026-06-22T06:33:30+00:00
sha256: f16642c61e61ca0a3f3aded4a7c721d7c1226bc5baedd30aea61e5c96bde7880
---

MonthOfCondition Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

As part of the Relativity Services API (RSAPI) Deprecation, content on this page referring to the RSAPI and the Patient Tracker application is in the process of being deprecated and will no longer be supported. For more information and alternative APIs, see RSAPI deprecation process .

# MonthOfCondition

You can use the MonthOfCondition to query date fields. For example, you can query email where the date sent is in a certain month. It is equivalent to adding this search condition in Relativity UI:

When constructing the query condition, specify the field, the condition operator, and the month value.

- Use the MonthOfConditionEnum.In to specify the operator.

- Use the kCura.Relativity.Client.Month enumeration to specify the month:

Member Name Value Description

NotSet 0 Not Set

January 1 January

February 2 February

March 3 March

April 4 April

May 5 May

June 6 June

July 7 July

August 8 August

September 9 September

October 10 October

November 11 November

December 12 December

The following code sample illustrates how to query using the MonthOfCondition condition to return all email where the sent date is in May.

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
public bool Query_MonthOfCondition_In_Document_DateTimeField(Client.SamplesLibrary.Helper.IHelper helper)

{

    //Get a connection to the API using the API helper classes, available in Event Handlers,

    //Agents, and Custom Pages. They are mocked here for samples purposes

    //NOTE: We are executing under the context of the current user. For more info, see the APIHelper documentation

    using (IRSAPIClient proxy = helper.GetServicesManager().CreateProxy<IRSAPIClient>(ExecutionIdentity.User))

    {

        //Set the ForContext for the method.

        kCura.Relativity.Client.SamplesLibrary.Logging.ISampleLogger logger = _logger.ForContext("MethodName", new StackFrame(0).GetMethod().Name, false);

        //Set the workspace ID

        //NOTE: SampleWorkspace_ID is sample data created for this example

        proxy.APIOptions.WorkspaceID = this.SampleWorkspace_ID;

        //Build the condition

        //The EqualTo keyword will look for exact matches only

        //NOTE: The constructor accepts IDs, Guids, and Field names to identfiy the object

        MonthOfCondition condition = new MonthOfCondition("Date Sent", MonthOfConditionEnum.In, kCura.Relativity.Client.Month.May);

        //Define the Query

        Query<DTOs.Document> query = new Query<Document> {Condition = condition};

        //Create ResultSet for the Query and query for the RDOs in a try/catch

        DTOs.QueryResultSet<DTOs.Document> resultSet = new DTOs.QueryResultSet<DTOs.Document>();

        try

        {

            resultSet = proxy.Repositories.Document.Query(query);

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

            return false;

        }

        //Check the success

        if (resultSet.Success)

        {

            logger.LogDebug("Number of Documents returned: {TotalCount}", resultSet.TotalCount);

            return true;

        }

        else

        {

            logger.LogError(resultSet.Message);

            return false;

        }

    }

}
```

On this page

- MonthOfCondition


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
