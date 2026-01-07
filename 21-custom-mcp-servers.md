# Scenario 21: Custom MCP Servers

Learn how to create and use custom Model Context Protocol (MCP) servers to extend Copilot's capabilities.

## 🎯 Learning Objectives

- Understand MCP server architecture
- Configure existing MCP servers
- Create simple custom MCP servers
- Connect external tools to Copilot

---

## 📝 What are MCP Servers?

MCP servers are external services that provide:
- **Tools**: Actions Copilot can perform
- **Resources**: Data Copilot can access
- **Prompts**: Pre-defined prompt templates

### Built-in MCP Servers
- **Playwright**: Browser automation
- **GitHub**: Repository operations
- **Azure**: Cloud resource management
- **File System**: Local file operations

### Custom MCP Servers
You can create servers for:
- Internal APIs
- Databases
- Custom tools
- Third-party services

---

## 🔧 Configuration

### VS Code Settings

Add MCP servers in `.vscode/settings.json`:

```json
{
  "github.copilot.chat.mcpServers": {
    "my-custom-server": {
      "command": "node",
      "args": ["./mcp-servers/my-server.js"],
      "env": {
        "API_KEY": "${env:MY_API_KEY}"
      }
    },
    "database-server": {
      "command": "python",
      "args": ["./mcp-servers/db-server.py"],
      "env": {
        "DATABASE_URL": "${env:DATABASE_URL}"
      }
    }
  }
}
```

### User Settings (Global)

For MCP servers available in all projects:

```json
{
  "github.copilot.chat.mcpServers": {
    "global-tool": {
      "command": "npx",
      "args": ["-y", "@my-org/mcp-tool"]
    }
  }
}
```

---

## 🏋️ Exercises

### Exercise 1: Configure an Existing MCP Server

Add the Fetch MCP server for web requests:

```json
{
  "github.copilot.chat.mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-fetch"]
    }
  }
}
```

Then use it:
```
Use the fetch tool to get the content from https://api.github.com/zen
```

### Exercise 2: Database MCP Server

Configure a SQLite MCP server:

```json
{
  "github.copilot.chat.mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-sqlite", "./data/app.db"]
    }
  }
}
```

Then query your database:
```
Show me all tables in the database
```

```
Query the users table and show the top 10 users
```

### Exercise 3: Create a Simple MCP Server (Node.js)

Create `mcp-servers/weather-server.js`:

```javascript
#!/usr/bin/env node
/**
 * Simple Weather MCP Server
 * 
 * This demonstrates a basic MCP server structure.
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server(
  {
    name: 'weather-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Define available tools
server.setRequestHandler('tools/list', async () => {
  return {
    tools: [
      {
        name: 'get_weather',
        description: 'Get current weather for a city',
        inputSchema: {
          type: 'object',
          properties: {
            city: {
              type: 'string',
              description: 'City name',
            },
          },
          required: ['city'],
        },
      },
      {
        name: 'get_forecast',
        description: 'Get 5-day weather forecast',
        inputSchema: {
          type: 'object',
          properties: {
            city: {
              type: 'string',
              description: 'City name',
            },
          },
          required: ['city'],
        },
      },
    ],
  };
});

// Handle tool calls
server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;

  if (name === 'get_weather') {
    // In real implementation, call weather API
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            city: args.city,
            temperature: 72,
            condition: 'Sunny',
            humidity: 45,
          }),
        },
      ],
    };
  }

  if (name === 'get_forecast') {
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            city: args.city,
            forecast: [
              { day: 'Monday', high: 75, low: 60 },
              { day: 'Tuesday', high: 73, low: 58 },
              { day: 'Wednesday', high: 70, low: 55 },
            ],
          }),
        },
      ],
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Exercise 4: Create a Database Query Server (Python)

Create `mcp-servers/db-server.py`:

```python
#!/usr/bin/env python3
"""
Database Query MCP Server

Provides tools for querying a SQLite database.
"""

import json
import sqlite3
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("database-server")

DATABASE_PATH = "./data/app.db"


@app.list_tools()
async def list_tools():
    return [
        {
            "name": "query",
            "description": "Execute a SELECT query on the database",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "SQL SELECT query to execute",
                    },
                },
                "required": ["sql"],
            },
        },
        {
            "name": "list_tables",
            "description": "List all tables in the database",
            "inputSchema": {
                "type": "object",
                "properties": {},
            },
        },
        {
            "name": "describe_table",
            "description": "Get schema of a table",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name",
                    },
                },
                "required": ["table"],
            },
        },
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:
        if name == "query":
            sql = arguments["sql"]
            # Security: Only allow SELECT queries
            if not sql.strip().upper().startswith("SELECT"):
                return {"error": "Only SELECT queries are allowed"}
            
            cursor.execute(sql)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            return {
                "columns": columns,
                "rows": rows,
                "count": len(rows),
            }

        elif name == "list_tables":
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
            tables = [row[0] for row in cursor.fetchall()]
            return {"tables": tables}

        elif name == "describe_table":
            table = arguments["table"]
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            return {
                "table": table,
                "columns": [
                    {
                        "name": col[1],
                        "type": col[2],
                        "nullable": not col[3],
                        "primary_key": bool(col[5]),
                    }
                    for col in columns
                ],
            }

    finally:
        conn.close()


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Exercise 5: API Integration Server

Create a server that connects to your internal API:

```javascript
// mcp-servers/internal-api-server.js
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const API_BASE = process.env.INTERNAL_API_URL;
const API_KEY = process.env.INTERNAL_API_KEY;

const server = new Server({
  name: 'internal-api',
  version: '1.0.0',
}, {
  capabilities: { tools: {} },
});

server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'get_users',
      description: 'Get users from internal system',
      inputSchema: {
        type: 'object',
        properties: {
          department: { type: 'string' },
          active: { type: 'boolean' },
        },
      },
    },
    {
      name: 'create_ticket',
      description: 'Create a support ticket',
      inputSchema: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          description: { type: 'string' },
          priority: { 
            type: 'string',
            enum: ['low', 'medium', 'high'],
          },
        },
        required: ['title', 'description'],
      },
    },
  ],
}));

server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  const response = await fetch(`${API_BASE}/${name}`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(args),
  });
  
  const data = await response.json();
  return {
    content: [{ type: 'text', text: JSON.stringify(data, null, 2) }],
  };
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

---

## 📋 MCP Server Components

### Tools
Actions that Copilot can perform:
- Execute queries
- Call APIs
- Transform data
- Trigger workflows

### Resources
Data that Copilot can read:
- Database tables
- Configuration files
- API schemas
- Documentation

### Prompts
Pre-built prompt templates:
- Common queries
- Standard operations
- Best practice patterns

---

## 💡 Best Practices

### 1. Security First
```javascript
// Validate inputs
if (!isValidQuery(args.sql)) {
  throw new Error('Invalid query');
}

// Use parameterized queries
cursor.execute('SELECT * FROM users WHERE id = ?', [args.id]);

// Limit permissions
// Only expose necessary operations
```

### 2. Error Handling
```javascript
try {
  const result = await performOperation(args);
  return { success: true, data: result };
} catch (error) {
  return { 
    success: false, 
    error: error.message,
    code: error.code 
  };
}
```

### 3. Rate Limiting
```javascript
const rateLimiter = new RateLimiter({
  maxRequests: 100,
  windowMs: 60000,
});

if (!rateLimiter.allow()) {
  throw new Error('Rate limit exceeded');
}
```

### 4. Logging
```javascript
console.error(`[${new Date().toISOString()}] Tool called: ${name}`);
console.error(`Arguments: ${JSON.stringify(args)}`);
```

---

## 🔍 Debugging MCP Servers

### Check Server Output
```bash
# Run server directly to see output
node ./mcp-servers/my-server.js
```

### VS Code Output Panel
View MCP server logs in the Output panel:
1. View → Output
2. Select "GitHub Copilot Chat" from dropdown

### Test Tools Manually
```
List available tools from the my-custom-server
```

---

## ⚠️ Common Issues

1. **Server not starting**: Check command path and permissions
2. **Tools not appearing**: Verify server capabilities export
3. **Connection errors**: Check environment variables
4. **Timeout errors**: Increase timeout in settings
5. **Permission denied**: Check file/network access

---

## ✅ Key Takeaways

- MCP servers extend Copilot with custom tools
- Configure in VS Code settings.json
- Tools define actions, resources provide data
- Security and error handling are critical
- Use logging for debugging
- Start simple, add complexity as needed

---

**NEXT:** Congratulations! You've completed the GitHub Copilot Learning Path! 🎉

Review all scenarios and practice regularly to become a Copilot power user.
