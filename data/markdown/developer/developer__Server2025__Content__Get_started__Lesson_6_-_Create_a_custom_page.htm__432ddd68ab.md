---
title: "Lesson 6 - Create a custom page"
url: https://platform.relativity.com/Server2025/Content/Get_started/Lesson_6_-_Create_a_custom_page.htm
collection: developer
fetched_at: 2026-06-22T06:25:00+00:00
sha256: 7da138f773c139bad1f01589440e3d88b97d6989b382fde6646b5f0b4f349ebf
---

Lesson 6 - Create a custom page

# Lesson 6 - Create a custom page

Custom pages are used to tailor the look and feel of applications that you develop on the Relativity platform. You can develop your own cascading style sheets (CSS), JavaScript, HTML, and images for your custom pages.

In this lesson, you will learn how to complete these tasks:

- Deploy a custom page in Relativity.

- Add a custom page to an application in Relativity.

- Implement a custom page containing client-side JavaScript. In this lesson, the JavaScript includes simple search functionality and the ability to create article categories.

- Debug a custom page in the browser.

- Use Kepler services via the REST API to search for article categories and create them in your instance of Relativity.

- Create Relativity Dynamic Objects (RDOs) by making REST calls through JavaScript to the Object Manager service.

- Create an RDO called Article Category using the Object Manager service.

Estimated completion time - 3 hours

PREVIOUS LESSON

‹‹ Lesson 5 - Build a cron job

NEXT LESSON

Lesson 7 - Use Relativity Forms to enhance the UI ››

## Step 1 - Create a simple custom page

You start creating a simple custom page by adding HTML to an index.html file. As you work through this lesson, you continue building the page by adding JavaScript, CSS, and more HTML. Use the code editor of your choice for working with these technologies in your custom page. This lesson uses Visual Studio Code.

Use the following steps to create a simple custom page:

- Create a directory called HelloWikipedia.CustomPage .

It is the root directory of your project.

- Track this directory using the source control tool of your choice, such as Git.

- Inside the root directory, create a subdirectory called src .

As you build your custom page, add the source files for it to this directory.

- In the src directory, create a file called index.html , and add the following code to the file. Copy

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
<!DOCTYPE html>

<html>

<head>

    <title>HelloWikipedia Categories</title>

</head>

<body>

    <div id="hw-container">Hello World!</div>

</body>

</html>
```

- Open the index.html file in a browser.

Your page should look like the following screen shot. You can now deploy this simple custom page in Relativity.

## Step 2 - Deploy a custom page in Relativity

This section illustrates how to deploy a custom page in Relativity and associate it with a tab. For more information, see Tabs on the Relativity Documentation site.

Use the following steps to deploy a custom page in Relativity:

- In the src directory, select the index.html file.

- Right-click on the file and select Send to > Compressed (zipped) folder .

- Set the name of the .zip file to HelloWikipedia.CustomPage.zip . In this example, you only have a single file, which is index.html. For more complex pages, you may have additional files containing JavaScript or other code. Make sure that you select and include all these files and any directories in the .zip file.

- Log in to your Relativity instance.

- Navigate to the Custom Pages tab.

You can also search for custom pages using the Quick Nav. For more information, see Quick Nav on the Relativity Documentation site.

- Click New Custom Page .

The Custom Page Information dialog appears.

- Click to select Hello Wikipedia , which you created in Lesson 2 - Build an application without any code .

You are going to add your custom page to this application.

- Enter HelloWikipedia Categories in the Name field.

- In the File field, click Choose File to select the .zip file that you created in step 2.

- Click Save .

- Verify that the Custom Page Link field now displays a path.

Record the value displayed in this field because you need to enter it when creating a tab for your custom page.

Your Hello Wikipedia application is now updated with the new custom page. In the following steps, you push your updated application to the Application Library, so that it is available throughout your Relativity instance.

- Push the updated Hello Wikipedia application to the Application Library by completing the following steps:

- Locate the Hello Wikipedia application in the My First Workspace created in Lesson 2 - Build an application without any code .

This workflow updates your application in the application library. Your application must be installed in a workspace. The Push to Library option performs the updates to the application in the library.

- Search on Relativity Applications in the workspace using the Quick Nav.

- Open the Hello Wikipedia application to display its details view.

- Click the Push to Library .

- In the My First Workspace , navigate to the Tabs page.

- Click New Tab . The Tab Information dialog appears.

- Enter the following information:

- Name - HelloWikipedia Categories

- Tab Type - External

- Link - enter the link displayed when you uploaded your custom page in step 9. Append /index.html to the end of the link so it points to your custom page. The GUID in the link will differ from than that in the following screen shots and code samples. See the following sample link: Copy

```text
1
 %applicationPath%/CustomPages/e57fa0fe-59fd-49eb-92ed-895f3e592cd1/index.html
```

- Order - 1000

You can set this field to any value. It controls the order that the tab is displayed in the drop-down menu of the parent tab.

- Navigate to the details view for the Hello Wikipedia application to complete these steps:

- Click Unlock Application in the Application console.

- Link the new tab you just created by finding Tabs section and clicking Link .

- Click Push to Library under Manage Application in the Application console.

- Navigate to the HelloWikipedia Categories tab. Your tab should appear like the one in the following screen shot.

After you push the application to the Application Library, it may take several minutes for your page to reload. You may also need to clear your browse cache by performing a hard reload (CTRL + F5).

## Step 3 - Add client-side JavaScript to a custom page

Use the following steps to add client-side JavaScript to a custom page:

- Create a subdirectory called scripts in the src directory.

- In the scripts directory, add the main.js file.

- Add the following code to the main.js file.

This code adds text to the <div> tags on the page. Copy

```text
1
2
3
4
5
6
7
function startApplication() {

    console.info("HelloWikipedia Categories application started");

    const label = document.getElementById("hw-container");

    label.innerText = "Hello from JavaScript!";

}

startApplication();
```

- Add the <script> tag to the index.html file immediately before the closing </body> tag.

This script executes the JavaScript with your page logic. Copy

```text
1
<script src="./scripts/main.js"></script>
```

- Complete the following steps to deploy your custom page:

- Add your custom page files to a .zip file as described in Step 2 - Deploy a custom page in Relativity . Make sure that you add the src directory with the index.html file and scripts sub-directory.

- In Relativity, navigate to the details view of your custom page.

- Click Edit > Clear > Choose File to select the new version of the custom page that you created.

- Navigate to the Hello Wikipedia application in the My First Workspace .

- Open the details view of your application and click Push to Library .

This step updates your application with the changes to your custom page.

- Navigate to the HelloWikipedia Categories tab for your custom page, and verify that the updated text populated by JavaScript appears on your page.

After you push the application to the Application Library, it may take several minutes for your page to reload. You may also need to clear your browse cache by performing a hard reload (CTRL + F5).

## Step 4 - Debug your custom page

After confirming that your custom page is working properly in Relativity, you can begin debugging your JavaScript in the browser. This lesson uses Google Chrome , but you could use other tools for this purpose.

Use the following steps to debug JavaScript in the browser:

- Open your custom page through Relativity in Chrome.

- Press F12 to open the Chrome Developer Tools.

- In the Developer Tools, open the Source tab.

- Click main.js in the left pane.

The source is displayed in the middle pane.

- Click on a line number to set a breakpoint.

Chrome displays a red circle where you set the breakpoint.

- Press F5 to refresh the page.

After refreshing, the JavaScript pauses its execution at the line with breakpoint.

- Control the debugging by using the debug execution control buttons at the top of the right pane. The Console tab in the bottom pane displays the message: HelloWikipedia Categories application started . The JavaScript for your page logged this message.

## Step 5 - Implement functionality for your custom page

In this step, you add functionality to your custom page, which provides users with the ability to search for the categories in Wikipedia using an existing Kepler service. Users should also be able to add categories as RDOs through the Object Manager service. For more information, see Kepler framework and Object Manager Fundamentals .

Your completed custom page should look like the following screen shot after you update the code and deploy it in Relativity. This screen shot illustrates a search on the word science .

Use the following steps to add new functionality to your custom page:

- In your code editor, update the HTML in the index.html the following code.This code includes the following functionality:

- Adds a <head> element containing a link to a styles.css file, which is added later in this section.

- Adds HTML that contains a description in a <span> tag, searching capabilities in an <input> tag, a search button in a <button> tag, and a <div> tag that JavaScript populates with search results.

- Includes elements that contain the required id or class attributes used in JavaScript and in CSS.

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
<!DOCTYPE html>

<html>

<head>

    <title>HelloWikipedia Categories</title>

    <link href="./styles/style.css" rel="stylesheet" type="text/css" />

</head>

<body>

    <div id="hw-container">

        <div id="hw-search-container">

            <span id="hw-search-label">Search Wikipedia for article categories</span>

            <div id="hw-search">

                <input id="hw-search-input" placeholder="Search for category" />

                <button id="hw-category-search-button" class="hw-button" type="button">Search</button>

            </div>

        </div>

        <div id="hw-results-container"></div>

    </div>

    <script type="module" src="./scripts/main.js"></script>

</body>

</html>
```

- In the src directory, create a styles directory.

- In the styles directory, create a style.css file and add the following code to the file. (Optionally, modify it using your own styles.) Copy

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
#hw-container {

     margin: 0;

     padding: 20px;

}

#hw-search-container {

     margin-left: 8px;

}

#hw-results-container {

     display: table;

     width: auto;

     max-width: 800px;

     margin-top: 20px;

}

.hw-results-header {

     color: #0670c1;

}

.hw-category-row {

     display: table-row;

}

.hw-category-cell {

     display: table-cell;

     padding: 8px;

     border-bottom: 1px solid #e2ebf3;

     text-align: left;

}

.hw-button-cell {

     display: table-cell;

     padding-left: 12px;

}

#hw-search {

     margin-top: 10px;

}

#hw-search-input {

     width: 300px;

     margin-right: 5px;

     padding: 5px;

     border-radius: 3px;

     border: .0625rem solid #acbfd6;

     line-height: 1.4rem;

}

#hw-search-label {

     color: #0670c1;

}

.hw-button {

     background-color: #0075e0;

     border: none;

     border-radius: 3px;

     display: inline-block;

     cursor: pointer;

     color: #fff;

     padding: 9px 23px;

     text-decoration: none;

}

.hw-button:hover {

     background-color: #0670c1;

}
```

- Add logic to file for calling Kepler services by creating a services directory in the scripts directory.

- In the services directory, create an apiFetchClient.js file, and add the following code to this file. The ApiFetchClient class contains the following functionality:

- Facilitates sending HTTPS requests, including GET and POST.

- Ensures all the required headers are set in POST requests.

- Adds the API base path to the required API endpoint passed as a parameter.

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
export class ApiFetchClient {

    constructor(globalObjectService) {

        this.globalObjectService = globalObjectService;

    }

    async get(apiEndpoint) {

        const response = await this.globalObjectService.getWindow().fetch(this._getFullApiPath(apiEndpoint));

        this._validateResponse(response);

        return await response.json();

    }

    async post(apiEndpoint, body) {

        const response = await this.globalObjectService.getWindow().fetch(this._getFullApiPath(apiEndpoint), this._getPostRequestInit(body));

        this._validateResponse(response);

        return await response.json();

    }

    _getPostRequestInit(payload) {

        return {

            method: 'POST',

            headers: {

                'Content-Type': 'application/json',

                'X-CSRF-Header': '-'

            },

            body: JSON.stringify(payload)

        };

    }

    _validateResponse(response) {

        if (!response.ok) {

            throw new Error(response.statusText);

        }

    }

    _getFullApiPath(apiEndpoint) {

        return this.globalObjectService.getTopWindow().GetKeplerApplicationPath() + apiEndpoint;

    }

}
```

- Add a service for category searches by creating the wikiCategorySearchService.js file in the services directory, and adding to this file.Because the ApiFetchClient class simplifies calling Kepler services via HTTPS, you can now create the WikiCategorySearchService class, which searches for categories.

This class contains the following functionality:

- Calls the wikipedia-service through the Kepler service by using the fetchClient class. This class passes the API path for the Kepler service with a prefix query parameter set to the categoryName that is used for the search.

- Has a dependency on the ApiFetchClient service class which is provided in the constructor. This mechanism is called dependency injection. It is used to decouple the logic and to simplify writing tests for this class.

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
export class WikiCategorySearchService {

    constructor(fetchClient) {

        this.fetchClient = fetchClient;

    }

    async search(categoryName) {

        return await this.fetchClient.get(`wikipedia-management/v1/wikipedia-service/categories?prefix=${categoryName}`);

    }

}
```

- Add the services for adding categories by creating the categoryService.js and the globalObjectService.js files in the services directory, and adding the following code to these files.

The CategoryService class contains the following functionality:

- Creates a category RDO object using Object Manager service in the REST API.

- Creates new categories and returns existing ones.

- Includes a create method that sends a POST request with the required request body to the create endpoint of Object Manager service in the REST API.

- Includes the getCategories() method that sends a POST request with required request body to the queryslim endpoint and processes the response to produce and array of categories. For more information, Object Manager Fundamentals and Object Manager (REST) .

- Ensures that the Object Manager endpoint contains correct Workspace ID, which is parsed from the browser URL. The URL is read from the JavaScript global window object. This code provided by the getWindow() method of globalObjectService class, which dependency injected from the constructor.

Complete these steps to add the code for the CategoryService class:

- View the GUIDs for your application by navigating to the details view of the Hello Wikipedia application and clicking Show Component GUIDs in the Application console.

- Locate the GUIDs for the following entities:

- Article Category object type

- Name field for the Article Category

- Overwrite Article Text field for the Article Category

- Automatic Updates Enabled field for the Article Category

- Update the code for the appConstants in the constructor with the GUIDs from step 1. See the following code sample.

- Added the following code with the updated GUIDs to the categoryService.js file: Copy

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
78
79
export class CategoryService {

    constructor(fetchClient, globalObjectService) {

        this.fetchClient = fetchClient;

        this.globalObjectService = globalObjectService;

        this.appConstants = {

            articleCategoryObjectTypeGuid: '6B20F149-1B17-4E9C-8403-439E98E8BFD2',

            articleCategoryNameFieldGuid: '16D8A362-2923-45B7-8444-7339C57B3AF0',

            overwriteArticleTextFieldGuid: '042E0329-1467-4993-8188-66615E103DE3',

            automaticUpdatesEnabledFieldGuid: 'F365DE2E-A641-428F-9188-A3970A7C308F'

        };

    }

    create(categoryName) {

        const request = {

            'request': {

                'ObjectType': {

                    'Guid': this.appConstants.articleCategoryObjectTypeGuid

                },

                'FieldValues': [{

                        'Field': {

                            'Guid': this.appConstants.articleCategoryNameFieldGuid

                        },

                        'Value': categoryName

                    },

                    {

                        'Field': {

                            'Guid': this.appConstants.overwriteArticleTextFieldGuid

                        },

                        'Value': false

                    },

                    {

                        'Field': {

                            'Guid': this.appConstants.automaticUpdatesEnabledFieldGuid

                        },

                        'Value': true

                    }

                ]

            }

        };

        return this.fetchClient.post(this._getObjectManagerMethodPath('create'), request);

    }

    async getCategories() {

        const request = {

            'request': {

                'ObjectType': {

                    'Guid': this.appConstants.articleCategoryObjectTypeGuid

                },

                'Condition': '',

                'Fields': [{

                    'Guid': this.appConstants.articleCategoryNameFieldGuid

                }]

            },

            'start': 1,

            'length': 99999

        };

        const result = await this.fetchClient.post(this._getObjectManagerMethodPath('queryslim'), request);

        const mappedCategories = result.Objects.map(object => {

            return object.Values[0];

        });

        return mappedCategories;

    }

    _getWorkspaceId() {

        const windowObject = this.globalObjectService.getTopWindow();

        const url = new URL(windowObject.location.href);

        return url.searchParams.get('AppID');

    }

    _getObjectManagerMethodPath(methodName) {

        const workspaceId = this._getWorkspaceId();

        return `Relativity.Objects/workspace/${workspaceId}/object/${methodName}`;

    }

                    }
```

- Add the following code to the globalObjectService.js file: Copy

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
export class GlobalObjectService {

    getTopWindow() {

        return window.top;

    }

    getWindow() {

        return window;

    }

    getDocument() {

        return document;

    }

}
```

- Implement the presentation layer for displaying results by creating the elementFactory.js file in the scripts directory and adding the following code to it.The ElementFactory class facilitates the creation of HTML elements, such as <div>, <span>, and <button> elements. Add the following code to the elementFactory.js file: Copy

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
export class ElementFactory {

    constructor(globalObjectService) {

        this.globalObjectService = globalObjectService;

    }

    createDiv(className) {

        const div = this._createElement('div');

        div.className = className;

        return div;

    }

    createSpan(className) {

        const span = this._createElement('span');

        span.className = className;

        return span;

    }

    createButton(buttonText, className) {

        const button = this._createElement('button');

        button.setAttribute('type', 'button');

        button.innerText = buttonText;

        button.className = className;

        return button;

    }

    _createElement(tagName) {

        const documentObject = this.globalObjectService.getDocument();

        return documentObject.createElement(tagName);

    }

}
```

- Facilitate the creation of a single search result element by creating a categoryResultElementFactory.js file in the scripts directory and adding the following code to this file.The CategoryService class contains the following functionality:

- Facilitates the creation of the category name and a button used for adding a category.

- Includes the createHtmlElement() method, which creates an HTML element representing the category search result.

- Adds a <span> HTML element containing the category name.

- Adds a Create button for a category only when it doesn't already exist. When you click this button, an event is triggered that removes the button and prevents it from firing a second time. It makes a call to the createCategory() function, which is provided as dependency in the constructor.

Add the following code to the categoryResultElementFactory.js file: Copy

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
export class CategoryResultElementFactory {

    constructor(elementFactory, createCategory) {

        this.elementFactory = elementFactory;

        this.createCategory = createCategory;

    }

    createHtmlElement(category) {

        const row = this.elementFactory.createDiv('hw-category-row');

        const categoryName = this.elementFactory.createSpan('hw-category-cell');

        categoryName.innerText = category.name;

        row.appendChild(categoryName);

        if (!category.exists) {

            const buttonDiv = this.elementFactory.createDiv('hw-button-cell');

            const button = this._createButton('Create', category.name);

            buttonDiv.appendChild(button);

            row.appendChild(buttonDiv);

        }

        return row;

    }

    _createButton(buttonText, categoryName) {

        const button = this.elementFactory.createButton(buttonText, 'hw-button');

        button.addEventListener('click',

            () => {

                button.parentNode.removeChild(button);

                this.createCategory(categoryName);

            });

        return button;

    }

}
```

- Create a list of multiple search result elements by create the searchResultsPresenter.js file in the scripts directory and adding the following code to this file.The SearchResultsPresenter class contains the following functionality:

- Includes the showSearchResults() method, which displays a list of category names provided as a parameter.

- Calls the CategoryService service, which retrieves information about categories that already exist.

- Removes the content in the <div> tag. Next, it adds a <span> tag with the title called Categories Found , which is displayed above the results.

- Renders all the categories with their associated buttons. It uses the categoryResultElementFactory dependency from the constructor.

Add the following code to the searchResultsPresenter.js file: Copy

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
export class SearchResultsPresenter {

    constructor(

        categoryService,

        elementFactory,

        categoryResultElementFactory,

        globalObjectService) {

        this.categoryService = categoryService;

        this.elementFactory = elementFactory;

        this.categoryResultElementFactory = categoryResultElementFactory;

        this.globalObjectService = globalObjectService;

    }

    async showSearchResults(categories) {

        const existingCategories = await this.categoryService.getCategories();

        const categoriesToRender = categories.map(category => {

            const exists = existingCategories.includes(category.Title);

            return {

                name: category.Title,

                exists: exists

            };

        });

        this._renderCategories(categoriesToRender);

    }

    _renderCategories(categories) {

        const documentObject = this.globalObjectService.getDocument();

        const resultsDiv = documentObject.getElementById('hw-results-container');

        resultsDiv.innerHTML = '';

        this._addResultsTitle(resultsDiv);

        categories.forEach(category => {

            const resultElement = this.categoryResultElementFactory.createHtmlElement(category);

            resultsDiv.appendChild(resultElement);

        });

    }

    _addResultsTitle(resultsDiv) {

        const resultsHeader = this.elementFactory.createDiv('hw-results-header hw-category-row');

        const headerText = this.elementFactory.createSpan('hw-category-cell');

        headerText.innerText = 'Categories Found';

        resultsHeader.appendChild(headerText);

        resultsDiv.appendChild(resultsHeader);

    }

}
```

- Execute a search and delegate the presentation results by creating the searchHandler.js file in the scripts directory and adding the following code to this file.The SearchHandler class executes a query by calling the CategorySearchService and then passes the results to the SearchResultsPresenter class for display.

Add the following code to the searchHandler.js file: Copy

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
export class SearchHandler {

    constructor(categorySearchService, resultsPresenter) {

        this.categorySearchService = categorySearchService;

        this.resultsPresenter = resultsPresenter;

    }

    async executeSearch(categoryPrefix) {

        const result = await this.categorySearchService.search(categoryPrefix);

        await this.resultsPresenter.showSearchResults(result);

    }

}
```

- Finalize the page functionality by update the main.js file in the scripts directory with the following code.The main.js file contains the following functionality:

- Includes all the required classes as imports.

- Instantiates each dependency in the createSearchHandler() function, so that the SearchHandler can be instantiated.

- Adds an action for the click event in the startApplication() function.

- Disables the Search button when the search <input> tag doesn't contain any text.

Add the following code to the main.js file: Copy

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
import { SearchHandler } from './searchHandler.js';

import { WikiCategorySearchService } from './services/wikiCategorySearchService.js';

import { SearchResultsPresenter } from './searchResultsPresenter.js';

import { CategoryService } from './services/categoryService.js';

import { ApiFetchClient } from './services/apiFetchClient.js';

import { CategoryResultElementFactory } from './categoryResultElementFactory.js';

import { ElementFactory } from './elementFactory.js';

import { GlobalObjectService } from './services/globalObjectService.js';

let _searchHandler;

function startApplication() {

    console.info('HelloWikipedia Categories application started');

    const searchButton = _getSearchButton();

    searchButton.addEventListener('click', _onSearchButtonClicked);

    searchButton.setAttribute('disabled', '');

    _getSearchInput().addEventListener('input', _onSearchTextChanged);

}

function _getSearchHandler() {

    if (_searchHandler) {

        return _searchHandler;

    }

    const globalObjectService = new GlobalObjectService();

    const fetchClient = new ApiFetchClient(globalObjectService);

    const categoryService = new CategoryService(fetchClient, globalObjectService);

    const elementFactory = new ElementFactory(globalObjectService);

    const categoryResultElementFactory = new CategoryResultElementFactory(elementFactory, categoryName => categoryService.create(categoryName));

    const resultsPresenter = new SearchResultsPresenter(categoryService, elementFactory, categoryResultElementFactory, globalObjectService);

    const categorySearchService = new WikiCategorySearchService(fetchClient);

    _searchHandler = new SearchHandler(categorySearchService, resultsPresenter);

    return _searchHandler;

}

function _onSearchButtonClicked() {

    const searchHandler = _getSearchHandler();

    searchHandler.executeSearch(_getSearchInput().value);

}

function _onSearchTextChanged() {

    const searchButton = _getSearchButton();

    if (_getSearchInput().value) {

        searchButton.removeAttribute('disabled');

    } else {

        searchButton.setAttribute('disabled', '');

    }

}

function _getSearchButton() {

    return document.getElementById('hw-category-search-button');

}

function _getSearchInput() {

    return document.getElementById('hw-search-input');

}

startApplication();
```

- Deploy a new version of your custom page by adding the index.html file, and the scripts and styles directories to a .zip file. See Step 2 - Deploy a custom page in Relativity .

- Verify that a search on the word science returns results like those in the following screen shot:

## Step 6 - Add tests for your custom page logic

After deploying your updated custom page, you can begin writing tests for it. In this step, you use a JavaScript testing framework called Jasmine . Review the Getting Started page on the Jasmine website for more information.

Use the following steps to add tests to the project:

- Download and install Node.js from nodejs.org .

This lesson uses version 14.8.0. This JavaScript runtime environment includes the node package manager called npm , which is used to install Jasmine.

- Navigate to the root directory of your project.

This directory is one level above the src folder created in Step 3 - Add client-side JavaScript to a custom page .

- Run the following commands in PowerShell from your project root directory.

These commands initialize npm and install Jasmine in the project: Copy

```text
1
2
3
4
5
6
7
8
// Run following command to initialize npm. This command creates package.json file in your project.

npm init -y

// Then run following command to install jasmine package. This command adds jasmine dependency to package.json.

npm install jasmine --save-dev

// Then run following command to initialize jasmine. This command adds jasmine configuration file.

npx jasmine init
```

- Update the files created by running these commands by completing the following tasks:

- Update the properties in the package.json file.

(Your version of Jasmine may differ from the one listed in this file.) Copy

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
{

    "name": "hellowikipedia-custompage",

    "version": "1.0.0",

    "description": "",

    "private": true,

    "scripts": {

        "test": "jasmine"

    },

    "keywords": [],

    "author": "",

    "license": "ISC",

    "devDependencies": {

        "jasmine": "^3.6.1"

    }

}
```

- Update your jasmine.json file located in the \spec\support\ directory as follows: Copy

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
{

    "spec_dir": "src/tests",

    "spec_files": [

        "**/*[sS]pec.js"

    ],

    "helpers": [

        "helpers/**/*.js"

    ],

    "stopSpecOnExpectationFailure": false,

    "random": true

}
```

- Create a tests subdirectory in the src directory to add a test to the project.

- Create the categoryService.spec.js file in the tests directory and add the following test code for the CategoryService class to this file.The following code illustrates how you can implement tests for your classes. You can optionally write your own tests for the code. For information about writing tests, see introduction.js on the Jasmine website. In the following code sample, update the GUIDs for the appConstants to match the GUIDs that you defined in categoryService.js. The GUIDs in categoryService.js are defined by your application hosted on the Relativity instance.

Add the following code to the categoryService.spec.js file: Copy

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
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
import { CategoryService } from '../scripts/services/categoryService.js';

import { createWindowMock, createGlobalObjectServiceMock, createApiFetchClientMock } from './utils/mockFactory';

describe('CategoryService', () => {

    const workspaceId = 12345;

    const topWindowObject = createWindowMock({ href: `https://localhost/endpoint?AppID=${workspaceId}` });

    const globalObjectService = createGlobalObjectServiceMock({ topWindowObject });

    const appConstants = {

        articleCategoryObjectTypeGuid: '6B20F149-1B17-4E9C-8403-439E98E8BFD2',

        articleCategoryNameFieldGuid: '16D8A362-2923-45B7-8444-7339C57B3AF0',

        overwriteArticleTextFieldGuid: '042E0329-1467-4993-8188-66615E103DE3',

        automaticUpdatesEnabledFieldGuid: 'F365DE2E-A641-428F-9188-A3970A7C308F'

    };

    describe('getCategories', () => {

        it('should return array of categories for workspace', async () => {

            // Arrange

            const fetchClient = createApiFetchClientMock({

                postResult: {

                    'Objects': [

                        {

                            'Values': [

                                'Movie'

                            ]

                        },

                        {

                            'Values': [

                                'Sport'

                            ]

                        }

                    ]

                }

            });

            const sut = new CategoryService(fetchClient, globalObjectService);

            // Act

            const categories = await sut.getCategories();

            // Assert

            expect(categories).toEqual(['Movie', 'Sport']);

            expect(fetchClient.post).toHaveBeenCalledWith('Relativity.Objects/workspace/12345/object/queryslim', {

                request: {

                    ObjectType: {

                        Guid: appConstants.articleCategoryObjectTypeGuid

                    },

                    Condition: '',

                    Fields: [

                        {

                            Guid: appConstants.articleCategoryNameFieldGuid,

                        },

                    ],

                },

                start: 1,

                length: 99999,

            });

        });

    });

    describe('create', () => {

        it('should create article category', async () => {

            // Arrange

            const categoryName = 'sport';

            const fetchClient = createApiFetchClientMock({});

            const sut = new CategoryService(fetchClient, globalObjectService);

            // Act

            await sut.create(categoryName);

            // Assert

            expect(fetchClient.post).toHaveBeenCalledWith('Relativity.Objects/workspace/12345/object/create', {

                request: {

                    ObjectType: {

                        Guid: appConstants.articleCategoryObjectTypeGuid

                    },

                    FieldValues: [

                        {

                            Field: {

                                Guid: appConstants.articleCategoryNameFieldGuid

                            },

                            Value: categoryName

                        },

                        {

                            Field: {

                                Guid: appConstants.overwriteArticleTextFieldGuid

                            },

                            Value: false

                        },

                        {

                            Field: {

                                Guid: appConstants.automaticUpdatesEnabledFieldGuid

                            },

                            Value: true

                        }

                    ]

                }

            });

        });

    });

});
```

- Create a subdirectory called fakes in the tests directory. In the following steps, you add mock classes to the fakes subdirectory.

- Create documentFake.js and htmlElementFake.js files in the fakes directory. These files help create the mock classes used in the categoryService.spec.js tests.

Add the following code for the documentFake.js class

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
import { HtmlElementFake } from './htmlElementFake';

export class DocumentFake {

    constructor() {

        this.children = [];

    }

    createElement(tagName) {

        return new HtmlElementFake(tagName);

    }

    appendChild(newChild) {

        newChild.parentNode = this;

        this.children.push(newChild);

    }

    getElementById(id) {

        return this.children.find(x => x.id === id);

    }

}
```

Add the following code for the htmlElementFake.js class

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
export class HtmlElementFake {

    constructor(tagName) {

        this.tagName = tagName;

        this.id = (void 0);

        this.className = (void 0);

        this.type = (void 0);

        this.innerText = (void 0);

        this.parentNode = (void 0);

        this.children = [];

        this.eventActions = {};

    }

    appendChild(newChild) {

        newChild.parentNode = this;

        this.children.push(newChild);

    }

    removeChild(child) {

        const index = this.children.indexOf(child);

        if (index > -1) {

            this.children.splice(index, 1);

            child.parentNode = null;

        }

    }

    setAttribute(name, value) {

        this[name] = value;

    }

    addEventListener(eventName, eventAction) {

        this.eventActions[eventName] = eventAction;

    }

    raiseEvent(eventName) {

        this.eventActions[eventName]();

    }

}
```

- Create a subdirectory called utils in the tests directory.

- Create the mockFactory.js file in the utils directory. This file helps generate the mock classes for the categoryService.spec.js tests. Add the following code for the mockFactory.js class

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
78
79
80
81
82
83
84
85
86
87
import { HtmlElementFake } from '../fakes/htmlElementFake';

import { DocumentFake } from '../fakes/documentFake';

export function createGlobalObjectServiceMock(mockParams) {

    return {

        getTopWindow: function () {

            return mockParams.topWindowObject;

        },

        getWindow: function () {

            return mockParams.windowObject;

        },

        getDocument: function () {

            return mockParams.documentObject;

        }

    };

}

export function createWindowMock(mockParams) {

    return {

        location: {

            href: mockParams.href

        },

        fetch: mockParams.fetch,

        GetKeplerApplicationPath: jasmine.createSpy().and.returnValue(mockParams.keplerApplicationPath)

    };

}

export function createDocumentMock() {

    return new DocumentFake();

}

export function createFetchMock(fetchResponses) {

    return jasmine.createSpy().and.callFake(function (input) {

        const response = fetchResponses[input];

        return Promise.resolve({

            ok: response.ok,

            json: function () {

                return Promise.resolve(response.data);

            },

            statusText: response.statusText

        });

    });

}

export function createApiFetchClientMock(mockParams) {

    return {

        get: jasmine.createSpy().and.returnValue(Promise.resolve(mockParams.getResult)),

        post: jasmine.createSpy().and.returnValue(Promise.resolve(mockParams.postResult))

    };

}

export function createCategorySearchServiceMock(mockParams) {

    return {

        search: jasmine.createSpy().and.returnValue(Promise.resolve(mockParams.searchResult))

    };

}

export function createSearchResultsPresenterMock() {

    return {

        showSearchResults: jasmine.createSpy()

    };

}

export function createElementFactoryMock() {

    return {

        createDiv: function (className) {

            const div = new HtmlElementFake('div');

            div.className = className;

            return div;

        },

        createSpan: function (className) {

            const span = new HtmlElementFake('span');

            span.className = className;

            return span;

        },

        createButton: function (buttonText, className) {

            const button = new HtmlElementFake('button');

            button.className = className;

            button.innerText = buttonText;

            button.type = 'button';

            return button;

        }

    };

}
```

- Run the following command to install the required Babel modules for using Jasmine with the import and export features of JavaScript ES6. (For more information, see What is Babel? on the Babel website.) Copy

```text
1
npm install  @babel/core @babel/register @babel/preset-env --save-dev
```

- Update your jasmine.json file located in the \spec\support\ directory with the following properties: Copy

```text
1
2
3
4
5
6
...

"helpers": [

    "../../node_modules/regenerator-runtime/runtime.js",

    ...

  ],

...
```

- Create the babel.config.json file in the root directory of your project.

- Add the following property to the babel.config.json file: Copy

```text
1
2
3
4
5
{

    "presets": [

        "@babel/preset-env"

    ]

}
```

- Use the following command to run the test: Copy

```text
1
npm run test
```

## Step 7 - Make your custom page production ready

This step illustrates how to make your custom page ready for deployment in a production environment. Use these guidelines when publishing a custom page:

- Bundle the code for the custom page into a single package file for use in the browser. In this step, you use module bundler called webpack . For more information, see Getting Started on the webpack website.

- Verify that your custom page works on all supported browsers, such as Internet Explorer 11, and others.

Use the following steps to prepare the page for a production environment:

- Enter the following command to install the required webpack modules: Copy

```text
1
npm install webpack webpack-cli --save-dev
```

- Create the dist subdirectory in the root directory of your project.

- Move the index.html file from the src directory to the dist directory.

- Update the index.html file in the dist directory by replacing the <script> reference and removing the <link> to the style.css file.

- Verify that your index.html is updated as follows: Copy

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
<!DOCTYPE html>

<html>

<head>

    <title>HelloWikipedia Categories</title>

</head>

<body>

    <div id="hw-container">

        <div id="hw-search-container">

            <span id="hw-search-label">Search Wikipedia for article categories</span>

            <div id="hw-search">

                <input id="hw-search-input" placeholder="Search for category" />

                <button id="hw-category-search-button" class="hw-button" type="button">Search</button>

            </div>

        </div>

        <div id="hw-results-container"></div>

    </div>

    <script src="bundle.js"></script>

</body>

</html>
```

- Enter the following command to install modules for CSS bundling: Copy

```text
1
npm install style-loader css-loader --save-dev
```

- Add the following import statement to the end of the import section in the main.js file located in the ../src/scripts directory: Copy

```text
1
2
...

import '../styles/style.css';
```

- Create a webpack.config.js file in the root directory of your project.

- Add the following properties to configure the webpack.config.js file. Copy

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
const path = require('path');

module.exports = {

    entry: [

        path.resolve(__dirname, "src/scripts/main.js"),

    ],

    output: {

        filename: 'bundle.js',

        path: path.resolve(__dirname, 'dist'),

    },

    module: {

        rules: [

            {

                test: /\.css$/,

                use: [

                    'style-loader',

                    'css-loader',

                ],

            }

        ],

    },

};
```

- Complete the configuration of webpack by locating the package.json file, and adding build to the scripts property: Copy

```text
1
2
3
4
"scripts": {

    "test": "jasmine",

    "build": "webpack"

}
```

- Enter the following command to build the project: Copy

```text
1
npm run build
```

- Verify that the bundle.js file is created in the dist directory.

In previous step, you updated the index.html file in the dist directory. The bundle file contains JavaScript that dynamically inserts your CSS into the HTML page.

- Ensure that the custom page runs in all supported browsers by adding the following modules:

- Enter the following command to install the required modules: Copy

```text
1
npm install babel-loader core-js whatwg-fetch --save-dev
```

- Update the babel.config.json as follows: Copy

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
{

    "presets": [

        [

            "@babel/preset-env",

            {

                "useBuiltIns": "entry",

                "corejs": 3

            }

        ]

    ]

}
```

- Update the webpack.config.js file as illustrated in the following code. The following modifications add the babel-loader and polyfill modules into the entry property list. Copy

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
const path = require('path');

module.exports = {

    entry: [

        "core-js/stable",

        "regenerator-runtime/runtime",

        "whatwg-fetch",

        path.resolve(__dirname, "src/scripts/main.js"),

    ],

    output: {

        filename: 'bundle.js',

        path: path.resolve(__dirname, 'dist'),

    },

    module: {

        rules: [

            {

                test: /\.css$/,

                use: [

                    'style-loader',

                    'css-loader',

                ],

            },

            {

                test: /\.m?js$/,

                exclude: /node_modules/,

                use: {

                    loader: 'babel-loader'

                }

            }

        ],

    },

};
```

- Verify that the project structure for your custom page matches the following screen shot.

- Rebuild and deploy your custom page.

When deploying your bundled custom page, you only need to add the contents in the dist directory to the HelloWikipedia.CustomPage.zip file. No other files or directories are required.

- Verify that your custom page runs properly in all supported browsers.
