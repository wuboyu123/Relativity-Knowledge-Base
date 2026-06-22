---
title: "Testing custom applications"
url: https://platform.relativity.com/Server2025/Content/Relativity_Platform/Testing_custom_applications.htm
collection: developer
fetched_at: 2026-06-22T06:29:32+00:00
sha256: eeecd3aa7b00dc67f602d3b933829feada97489f4c47100909d5f6f1a7ad9021
---

Testing custom applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Testing custom applications

By writing testable code and automating your testing workflow, you can increase your efficiency when deploying custom applications. You can use testing to ensure that your existing applications remain compatible with new releases of Relativity and robustly respond to this evolving platform. For example, you can develop flexible application testing to meet these demands:

- Testing your new and existing applications against specific Relativity releases within a limited time frame, including the following:

- Running tests against specific versions of Relativity when new code is deployed.

- Running existing code against new releases of Relativity.

- Updating an immature or developing a new automation framework.

- Minimizing long regression cycles.

- Eliminating testing business logic through the UI, and time-consuming manual testing.

This page contains information about how you can implement testing for new and existing custom applications that shorten your regression cycles and efficiently deploy applications into production. It also discusses the importance of writing testable code that uses automation in this process.

## Types of tests for custom applications

It is time consuming, inefficient and non-sustainable to run tests manually for every release of Relativity. Testable code and automation make regression cycles much shorter. If your software is available in the cloud, you don't have control over the release cycle. By testing your code quickly and on schedule, you can efficiently deploy it into production.

### Unit tests

Unit tests are used to independently test a unit of code to evaluate proper operation. They are easy to maintain and can be run at any time. As a best practice, they should only take a few seconds to run. For more information, see Steps for writing unit tests .

Unit tests use mock objects that simulate the behavior of an external component. They isolate the code under test and help to identify whether a single code change has any effects on the code base. The following tools support unit testing with mock objects:

- Moq

- NSubstitute

- Rhinomocks

For example, you might use Moq as a mocking framework, and the NUnit 3.6.0 or above to write unit tests.

The disadvantage of unit tests is that they only test the functionality of a single unit. They may not catch system-wide errors, or integration errors that result from interactions with other parts of the system.

### Integration tests

Integration tests check two or more units of code as a group. Unlike unit tests that check a unit of work in your code, integration tests analyze the integration of your code with other components within your application. They may fail due to a defect in your code even though the unit tests passed.

As a best practice, write integration tests to check the integration of your application with other modules, and to verify that your application interacts properly with Relativity. You can use integration tests to fully automate your functional tests, and eliminate any dependency on the UI.

An integration test has one or more of the following characteristics:

- Can’t be fully automated.

- Communicates directly with a database.

- Communicates across a network.

- Interacts with the file system.

- Requires special modifications to the environment to run it.

- Doesn't isolate dependencies by only testing the unit of code under test.

- Can’t run at the same time as any other unit tests.

- Must run in a specific order if it's part of other tests.

- Doesn't return the same result every time that you run it. For example, a unit test might run using random numbers and produce different results for each run.

- Tests more than a single logical concept.

- Doesn't run fast.

### Continuous integration testing

To facilitate implementing and upgrading custom applications, consider writing unit and integration tests that you can easily push through a continuous integration (CI) pipeline. CI is an engineering practice that involves committing and merging code several times a day. This workflow ensures that you get rapid feedback on your code and catch defects quickly.

To use CI efficiently, implement a test for each code change that you push to your production environment. This practice helps you quickly identify the exact time of a failure and the change that caused it. As Relativity releases production code more frequently, using a CI workflow can simplify the process of deploying custom applications.

The Google Testing Blog illustrates the benefits of using CI to improve software quality with less risk. The Google code base undergoes over 20 code changes per minute, resulting in changes to 50% of its files every month. Google engineers develop and release each product from the head , relying on automated tests to verify the product behavior. The release frequency varies from multiple times per day to once every few weeks as determined by the product team. The shorter feedback cycles improve productivity by starting with changes being pushed to merge, and then adding them to staging without any manual intervention. They also help keep the focus on building new features rather than fixing defects.

## Code coverage

Code coverage measures the test coverage and test quality that is used to check the functionality of specific features. Use these guidelines for code coverage:

- Provide 80% to 90% code coverage with unit tests for any new code.

- Aim for the maximum amount of coverage with the smallest number of quality unit tests. High code coverage doesn't necessarily mean that you have written quality tests.

- Consider writing golden flow integration tests for legacy code that doesn’t have many unit tests, because you may find it difficult to write unit tests for legacy code.

## Testable code

To facilitate custom application development, write testable code that is iterative and simple to refactor. You can then easily create automated tests for it. Review the following guidelines for writing testable code:

- Move the business logic for your extensibility point code into a general class. For example, if you have an agent call called Manager, you might create a ManagerJob class for this purpose. This ManagerJob class has all of your agent business logic.

- Allow parameters to be mocked.

- Specify interfaces instead of object instances in method parameters.

"New is glue" - In a strongly-typed language like C#, the new keyword is used to instantiate an object. For a flexible implementation of your code, introduce an interface to keep your code loosely-coupled, rather than bind your class to another one using the new keyword.

For example, the Relativity Manager-Worker Agent template demonstrates the manager and worker concepts used for Relativity agents. The manager agent creates a job record and the worker agent iterates through the job records in batches to make the application scalable and performant. For more information, see Relativity Manager-Worker Agent template .

View an example of code difficult to test

The following code sample illustrates code that isn't readily testable:

Review the following implementation details that make this code difficult to test:

- Limitations of the agent framework - The agent framework is written in a manner that doesn’t let you write a test, which presents a challenge when you are trying to add test coverage. In the above example, the Manager class implements the Agent base class. A new instance of SqlQueryHelper is created in order to call SQL methods. When the current Agent executes during off-hours, it processes the Manager job. Otherwise, the Manager agent displays a message indicating that it isn’t off-hours.

- Can't mock parameters - The code doesn't support controlling or mocking parameters through a test. Its framework doesn't isolate the code so you can test the logic because the SQLQueryHelper and AgentHelper exist as external dependencies. This implementation is tightly-coupled reducing the flexibility and reusability of the code.

This code sample also illustrates the challenges that you might experience writing tests for legacy code. To simplify your implementation and write testable code, consider using the Relativity Manager-Worker Agent template . For more information, see Visual Studio templates .

View an example of testable code

The following code sample illustrates how to write a ManagerJob class, which you can use to easily test your business logic:

Review the following steps used to ensure that this code is testable:

- Move the business logic - To make the agent code testable, move the business logic from the Manager class to a separate class called ManagerJob. You can now easily write tests for the ManagerJob class like any other class.

- Make the code mockable - Supply dependencies through the class constructor. Inject the AgentHelper and SQLQueryHelper dependencies from outside the class. The dependencies are passed as interfaces through the constructor and stored as private variables, which means you can fake or mock them.

- Use interfaces - To make your code testable, use interfaces to provide different types of implementations, and ensure that your code is loosely-coupled. The ManagerJob class now functions without dependencies on the AgentHelper and SQLQueryHelper classes.

The Admin Migration Utility also exemplifies how to implement the Agent Manager - Worker template with testable code. This application imports and exports users from an instance of Relativity. For more samples, see the Relativity repository on GitHub.

#### Why is this code better?

You are making your code testable because interfaces provide different types of implementations and your code is loosely coupled. The ManagerJob class functions without depending on the AgentHelper and SQLQueryHelper. The advantage of this code is that you can write a test around the ManagerJob class and easily test your business logic.

## Steps for writing unit tests

You can set up unit tests for your custom applications by using the steps outlined in this section. When writing an NUnit test, you can use attributes to identify different parts of it. For more information, see NUnit documentation on the NUnit website.

The sample code used here references the agent manager example in Testable code . Use the following steps to set up mocks for a test:

- Declare mocks - These mocks help create the data for the test:

- Instantiate the mocks - Instantiate the mocks on the interfaces. The System Under Test (SUT) object creates a new instance of ManagerJob class and takes the MockAgentHelper and MockSQLQueryHelper dependencies that are mocked:

- Pass data and call the Execute() method - Pass the start time, end time, current time, and expected result as different iterations of data. Stub out three methods in the SqlHelper to return the start time, end time, and current time, which are passed as parameters in the test. Call the Execute() method on the SUT, which is an object of type ManagerJob. The expected result passed in as a parameter equals result generated by calling the Execute() method on the SUT.

To simplify the process of creating test data, use the Relativity Test Helpers located in the Relativity repository on GitHub. This code sets up workspaces, users, groups, authentication providers, fields, and other test data, so that you can focus on the business logic of your code.

## Developer test VMs

To test the compatibility of your custom applications with different Relativity versions, you can obtain a copy of a developer test VM. We provide test VMs for Relativity 9.4 and above, which are supported on Windows 10 running Hyper-V. Contact the Developer Experience (DevEx) team to request a test VM copy for download from a secured FTP site.

Review the following guidelines for using the developer test VMs:

- Don't use the test VM to performance test your applications. The system resources aren't equivalent to the suggested production configurations.

- Create a CI cycle using your test VM, and use it as a local environment for debugging. The test VMs also support remotely debug your code.

- Use the logging framework so your application can write logs from any custom agent, custom page and event handler that it contains. You can obtain runtime diagnostic information and troubleshoot application problems using this framework. For more information, see Log from a Relativity application .

## Recommendations for application development

Review the following general recommendations for application development:

- Write code that is testable. Depending on your development goals, you can use the Relativity Agent Manager-Worker template to build your applications and write testable code. For more information, see the Relativity Manager-Worker Agent on Visual Studio Marketplace.

- Write unit tests and integration tests for all of your Relativity applications, especially those that require testing on a recurring regression cycle. Consider using these recommended tools for writing tests. For more information, see Tools for testing in Visual Studio .

- Nunit framework for writing tests

- Moq for writing unit tests

- Relativity APIs for writing integration tests

- Engage with other Relativity developers by visiting the following sites:

- Relativity Community - Review communications and other information posted and shared with customers and developers on this site.

- Developer Group - Join and subscribe to receive Relativity platform news and updates communicated to the developer community through this site.

- Relativity DevHelp Community - Visit the developer forum for Relativity. The following screen shot illustrates the DevHelp category used for posting questions to the community. For more information, Get started with the Relativity DevHelp Community .

### Testing workflow

The following diagram illustrates the recommended testing workflow for your custom applications:

## Tools for testing in Visual Studio

Consider using the following tools for testing in Visual Studio:

- NUnit 3.6 or higher for running all of your unit and integration tests

- Moq latest version for running your unit tests

- Resharper or Visual Studio for identifying compiler errors and runtime errors, and simplifying running tests. It is an extension in Visual Studio.

## Additional testing resources

Review the following list of additional testing resources to learn more about sample projects, testing, and Relativity templates.

### Relativity repository on GitHub

The Relativity repository is an open source repository on GitHub, which contains samples projects that you can reference when building custom applications. It also includes helpers that you can use for creating an automation framework. The following list highlights sample projects and other information available in this repository:

- DbContext Helper - This helper accommodates the removal of the implementation of the IDBContext contract mentioned in this community post.

- Datagrid audit API samples - This project illustrates how you can convert an application so it consumes DataGrid, and how to use the APIs to test an application.

- Test data setup - The Relativity test helpers contain information about how to import data and documents into a workspace.

### Additional NUnit testing information

You can find additional information about unit testing by reviewing the article The Constraint Assertion Model .

### Visual Studio templates

To simplify your development process, use the Visual Studio templates available for Relativity. The Relativity Manager-Worker Agent template on Visual Studio Marketplace or on GitHub provides an example of the templates available for use. For more information, see Visual Studio templates .

On this page

- Testing custom applications

- Types of tests for custom applications

- Unit tests

- Integration tests

- Continuous integration testing

- Code coverage

- Testable code

- Steps for writing unit tests

- Developer test VMs

- Recommendations for application development

- Testing workflow

- Tools for testing in Visual Studio

- Additional testing resources

- Relativity repository on GitHub

- Additional NUnit testing information

- Visual Studio templates


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
