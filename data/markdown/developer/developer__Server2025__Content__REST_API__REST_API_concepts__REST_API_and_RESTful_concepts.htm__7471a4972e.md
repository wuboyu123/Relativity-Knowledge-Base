---
title: "Basic REST API concepts"
url: https://platform.relativity.com/Server2025/Content/REST_API/REST_API_concepts/REST_API_and_RESTful_concepts.htm
collection: developer
fetched_at: 2026-06-22T06:29:07+00:00
sha256: 398d6e609bb8448dad2b6eb01ffc3d3edca5460131796f8bad851d1a777e49d2
---

Basic REST API concepts

# REST API overview

The REST API simplifies development by supporting standard HTTP methods, error handling, and other RESTful conventions. It also exposes resources through template URLs. You can use this lightweight platform provided by the REST API to take your software projects to the next level with the development of mobile applications that support common user interactions with Relativity.

See this related page:

- Relativity Server APIs

## REST API features

The RelativityREST API exposes the same functionality available through the Services API, offering a rich feature set that includes:

- Functionality for retrieving files from File fields in RelativityDynamic Objects (RDOs).

- Support for create, read, update, delete, and query operations on workspaces, saved searches, documents, RDOs, and other object types.

- Secure access to resources using flexible authentication methods, such as HTTPS and Active Directory.

- Language independence made possible by adherence to RESTful architectural standards, providing you with the option to choose a programming language based on application requirements.

- Implementation of standard HTTP methods and JSON resource representations.

## RESTful concepts

The Relativity REST API conforms to standard architectural principles defined by Representational State Transfer (REST). It supports these key architectural concepts common to RESTful services:

- Uses stateless interactions – The Relativity REST service doesn’t use login sessions or store other state information on the server. Instead, the client maintains this information about each resource, which makes the REST service easier to use across load-balanced servers. For general introduction, see Representational state transfer at https://en.wikipedia.org/wiki/Representational_state_transfer .

- Communicates over HTTP – The REST service uses common HTTP methods following standard RESTful principles:

- GET - reads data and doesn’t change application state

- POST - creates resources and queries for data using conditions

- PUT - updates resources

- DELETE - removes resources from the database

- Uses standard HTTP status codes – These status codes represent the results of operations that you perform against the REST service. They are divided into these major categories:

- 200 - Success

- 300 - Redirection

- 400 - User error

- 500 - Server error

See HTTP status codes . For a general introduction, see Status Code Definitions at http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html .

- Manipulates resources – The REST service represents the objects exposed in Relativity as resources. A unique URL identifies each resource so that you can manipulate it with standard HTTP methods. Other entities not generally identified as objects are also represented as resources. For example, search results are a resource that you can read or browse using paging.

- Provides a hypermedia-driven API – The REST API returns responses that include links to resources available in Relativity. For example, the response for a workspace query returns a list of each matching workspaces. It represents each workspace in a simplified format that contains a link to further details about the resource.

## Unique implementation details

The REST API accommodates the data model and scaling requirements of Relativity, while also supporting common RESTful principles. When consuming the REST API, you need to consider the following requirements that are unique to its implementation:

- Use paged lists of data – The REST API requires clients to page through all search results. When you initially make a request, the number of resources that will be returned can’t be immediately determined, so all lists of data must be paged to support large result sets.

The best pagination size varies depending on your situation. In general, we recommend testing out a moderate value, such as 10,000 documents, then adjusting up or down based on performance.

- Specify additional fields to return – The REST API returns only the default set of fields for a resource unless you provide a query string that specifies additional fields or all fields on the object. You can improve performance by retrieving only default fields or those additional fields that you need.

- Use queries to filter data – You can filter a list of resources by performing a query, which is a request that uses the POST method and contains conditions in a JSON representation. After the REST API returns the search result resource, you can page through the list of resources returned in it. You can’t use a query string to filter a collection of resources. See Query for resources .

- Provide required headers – You must include authentication credentials and an empty CSRF header in every request that you make to the REST API. See HTTP headers .
