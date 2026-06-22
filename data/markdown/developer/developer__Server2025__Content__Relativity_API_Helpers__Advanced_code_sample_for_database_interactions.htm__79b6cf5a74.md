---
title: "Advanced code sample for database interactions"
url: https://platform.relativity.com/Server2025/Content/Relativity_API_Helpers/Advanced_code_sample_for_database_interactions.htm
collection: developer
fetched_at: 2026-06-22T06:31:46+00:00
sha256: c006646918c8f998a3354d93626ff6309d5597eccb3f50e3654677c2a593d72a
---

Advanced code sample for database interactions Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Code sample for database interactions

You can use the IDBContext interface in the Relativity Helpers API to run queries, manage database transactions, and perform common database operations. You can reference this context from agents, custom pages, and event handlers. You must add a reference to the Relativity.API.dll to your Visual Studio project to use this the IDBContext interface.

The DefaultSqlCommandTimeout instance configuration setting can determine the value of the int timeoutValue parameter in Execute calls (such as ExecuteNonQuerySQLStatement and ExecuteSqlStatementAsDataSet). If your code passes 0 or less as the timeoutValue parameter, the timeout value will revert to using the value set for the instance configuration setting for DefaultSqlCommandTimeout. Should this configuration setting not exist in your environment, it is possible that the Timeout value will be set to 0.

You can use the advanced functionality available through this interface. The JobQueries class demonstrates how to query for data, modify it, and then modify database transactions. For a basic code sample, see Basic concepts for Relativity API Helpers .

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
74
75
76
77

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Data;

using System.Data.SqlClient;

using Relativity.API;



namespace Relativity.Samples.Core

{



     public static class JobQueries

     {

          public static Boolean JobExists(IDBContext dbContext, Int32 workspaceArtifactID, Int32 artifactID)

          {

               Boolean retVal = false;

               String sql = "SELECT COUNT(*) AS JobCount

                    FROM [SamplesApp]

                    WHERE [WorkspaceArtifactID] = @WorkspaceArtifactID AND [InstanceArtifactID] = @InstanceArtifactID";



               SqlParameter workspaceArtifactIDParam = new SqlParameter("@WorkspaceArtifactID", SqlDbType.Int);

               workspaceArtifactIDParam.Value = workspaceArtifactID;



               SqlParameter instanceArtifactIDParam = new SqlParameter("@InstanceArtifactID", SqlDbType.Int);

               instanceArtifactIDParam.Value = artifactID;



               retVal = (dbContext.ExecuteSqlStatementAsScalar<Int32>(sql, new SqlParameter[] { workspaceArtifactIDParam, instanceArtifactIDParam }) > 0);

               return retVal;

          }



          public static void InsertJob(IDBContext dbContext, Int32 workspaceArtifactID, Int32 artifactID)

          {

               String sql = "IF NOT EXISTS(SELECT TOP 1 * FROM [SamplesApp]

                         WHERE [WorkspaceArtifactID] = @WorkspaceArtifactID AND [InstanceArtifactID] = @InstanceArtifactID)"

                    + " BEGIN"

                    + " INSERT INTO [SamplesApp] (WorkspaceArtifactID, InstanceArtifactID, Status)"

                    + " Values (@WorkspaceArtifactID, @InstanceArtifactID, 0)"

                    + " END";



               SqlParameter workspaceArtifactIDParam = new SqlParameter("@WorkspaceArtifactID", SqlDbType.Int);

               workspaceArtifactIDParam.Value = workspaceArtifactID;



               SqlParameter instanceArtifactIDParam = new SqlParameter("@InstanceArtifactID", SqlDbType.Int);

               instanceArtifactIDParam.Value = artifactID;



               dbContext.BeginTransaction();

               try

               {

                    dbContext.ExecuteNonQuerySQLStatement(sql, new SqlParameter[] { workspaceArtifactIDParam, instanceArtifactIDParam });

                    dbContext.CommitTransaction();

               }

               catch (Exception ex)

               {

                    dbContext.RollbackTransaction();

                    throw;

               }

          }

                    public static void CreateTableIfNotExists(IDBContext dbContext) {

                         String sql = "IF NOT EXISTS(SELECT 'true' FROM [INFORMATION_SCHEMA].[TABLES] WHERE [TABLE_NAME] = 'SamplesApp')"

                         + " BEGIN "

                         + " CREATE TABLE SamplesApp ([WorkspaceArtifactID] INT NOT NULL, [InstanceArtifactID] INT NOT NULL,

                                   [Status] INT NOT NULL)"

                         + " END";



                         dbContext.BeginTransaction();

                         try {

                              dbContext.ExecuteNonQuerySQLStatement(sql);

                              dbContext.CommitTransaction();

                         }

                         catch (System.Exception ex) {

                              dbContext.RollbackTransaction();

                              throw;

                         }

                    }

     }

}
```

On this page

- Code sample for database interactions


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
