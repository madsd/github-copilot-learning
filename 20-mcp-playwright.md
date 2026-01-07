# Scenario 20: Playwright MCP for Browser Automation

Learn how to use the Playwright Model Context Protocol (MCP) server for browser automation with Copilot.

## 🎯 Learning Objectives

- Understand MCP (Model Context Protocol)
- Use Playwright MCP for browser automation
- Automate web testing and scraping
- Debug browser interactions

---

## 📝 What is MCP?

**Model Context Protocol (MCP)** allows Copilot to:
- Interact with external tools and services
- Access real-time data and APIs
- Perform actions beyond code generation
- Connect to databases, browsers, and more

### Playwright MCP Specifically
The Playwright MCP server enables:
- Browser navigation and control
- Element interaction (click, type, etc.)
- Screenshots and snapshots
- Form filling and file uploads
- Network request monitoring

---

## 🔧 Setup

### Prerequisites
1. VS Code with GitHub Copilot
2. Playwright MCP extension enabled

### Verify MCP is Available
In Copilot Chat, you should see Playwright tools available when you type `@`.

---

## 🏋️ Exercises

### Exercise 1: Basic Navigation

Use Copilot with Playwright MCP to navigate to a website:

```
Navigate to https://example.com and take a screenshot
```

Copilot will:
1. Open a browser
2. Navigate to the URL
3. Capture and display a screenshot

### Exercise 2: Take an Accessibility Snapshot

Get a structured view of a page:

```
Go to https://github.com and take an accessibility snapshot
of the page. Show me the main navigation elements.
```

The snapshot provides:
- Page structure
- Interactive elements
- ARIA labels
- Form fields

### Exercise 3: Form Interaction

Automate form filling:

```
Navigate to https://httpbin.org/forms/post
Fill in the form with:
- Customer name: John Doe
- Telephone: 555-1234
- Email: john@example.com
Then submit the form and show me the response.
```

### Exercise 4: Web Scraping

Extract data from a website:

```
Go to https://news.ycombinator.com
Extract the top 5 story titles and their point counts
Present them in a table format
```

### Exercise 5: Multi-Page Navigation

Navigate through multiple pages:

```
1. Go to https://github.com/microsoft/vscode
2. Click on the "Issues" tab
3. Take a snapshot of the issues list
4. Tell me how many open issues there are
```

### Exercise 6: Waiting for Content

Handle dynamic content:

```
Navigate to a page and wait for specific text to appear:
1. Go to https://example.com
2. Wait for "Example Domain" text to be visible
3. Confirm the page loaded correctly
```

### Exercise 7: Console and Network Monitoring

Debug web applications:

```
Navigate to https://httpbin.org/get
Show me:
1. Any console messages
2. The network requests made
3. The response data
```

### Exercise 8: Tab Management

Work with multiple tabs:

```
1. Open https://github.com in a new tab
2. List all open tabs
3. Switch between tabs
4. Close a specific tab
```

---

## 📋 Common Playwright MCP Commands

### Navigation
| Action | Example Prompt |
|--------|----------------|
| Open URL | "Navigate to https://example.com" |
| Go back | "Go back to the previous page" |
| Refresh | "Reload the current page" |

### Interaction
| Action | Example Prompt |
|--------|----------------|
| Click | "Click the 'Submit' button" |
| Type | "Type 'hello' into the search box" |
| Select | "Select 'Option 2' from the dropdown" |
| Hover | "Hover over the menu item" |

### Information
| Action | Example Prompt |
|--------|----------------|
| Screenshot | "Take a screenshot of the page" |
| Snapshot | "Take an accessibility snapshot" |
| Console | "Show me console messages" |
| Network | "Show network requests" |

### Waiting
| Action | Example Prompt |
|--------|----------------|
| Wait for text | "Wait for 'Success' to appear" |
| Wait for element | "Wait for the login form" |
| Wait time | "Wait 2 seconds" |

---

## 🔍 Use Cases

### 1. E2E Testing Assistance
```
Help me write an E2E test for the login flow:
1. Navigate to the login page
2. Enter credentials
3. Submit the form
4. Verify the dashboard loads

Use Playwright to demonstrate each step.
```

### 2. Visual Regression
```
Take screenshots of these pages for comparison:
- Homepage
- Products page
- Contact page

Save them for visual regression testing.
```

### 3. Accessibility Auditing
```
Navigate to my website and:
1. Take an accessibility snapshot
2. Identify elements missing ARIA labels
3. Find color contrast issues
4. Check keyboard navigation
```

### 4. API Testing via Browser
```
Use the browser to:
1. Make a POST request to the API
2. Show me the response
3. Verify the status code is 200
```

### 5. Data Extraction
```
Scrape product information from an e-commerce page:
- Product name
- Price
- Availability
- Rating

Format as JSON.
```

---

## 💡 Tips for Effective Use

### 1. Be Specific About Elements
```
❌ "Click the button"
✅ "Click the blue 'Submit' button below the form"
```

### 2. Handle Dynamic Content
```
"Wait for the loading spinner to disappear, 
then take a screenshot"
```

### 3. Use Snapshots for Understanding
```
"Take an accessibility snapshot so I can see 
what elements are available to interact with"
```

### 4. Chain Actions
```
"Navigate to the site, login with test credentials,
go to settings, and take a screenshot"
```

### 5. Error Handling
```
"Try to click the 'Next' button. If it's not found,
take a screenshot and tell me what's on the page"
```

---

## ⚠️ Limitations

1. **Cannot access localhost by default** - May need configuration
2. **Authentication required** - Some sites need login handling
3. **Rate limiting** - Be respectful of website limits
4. **Dynamic content** - May need explicit waits
5. **CAPTCHAs** - Cannot solve them automatically

---

## ✅ Key Takeaways

- Playwright MCP enables browser automation through Copilot
- Use accessibility snapshots to understand page structure
- Chain actions for complex workflows
- Great for E2E testing assistance and web scraping
- Always be respectful of website terms of service

---

**NEXT:** Move on to [21-custom-mcp-servers.md](21-custom-mcp-servers.md) to learn about creating and using custom MCP servers!
