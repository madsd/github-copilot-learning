# Scenario 12: Copilot Chat Basics

Learn how to have interactive conversations with GitHub Copilot Chat for coding assistance.

## 🎯 Learning Objectives

- Open and navigate Copilot Chat
- Ask effective coding questions
- Use slash commands for quick actions
- Understand chat context and history

---

## 📝 Opening Copilot Chat

### Keyboard Shortcuts
| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Chat Panel | `Ctrl+Alt+I` | `Cmd+Opt+I` |
| Open Inline Chat | `Ctrl+I` | `Cmd+I` |
| Quick Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |

### From Command Palette
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Copilot Chat"
3. Select "GitHub Copilot: Open Chat"

---

## 🔧 Slash Commands

Slash commands are shortcuts for common operations:

| Command | Description | Example |
|---------|-------------|---------|
| `/explain` | Explain selected code | Select code, then `/explain` |
| `/fix` | Fix bugs in selected code | Select buggy code, then `/fix` |
| `/tests` | Generate tests | Select function, then `/tests` |
| `/doc` | Generate documentation | Select code, then `/doc` |
| `/new` | Create a new project | `/new React app with TypeScript` |
| `/newNotebook` | Create a new Jupyter notebook | `/newNotebook data analysis` |
| `/clear` | Clear chat history | `/clear` |
| `/help` | Show available commands | `/help` |

---

## 🏋️ Exercises

### Exercise 1: Basic Questions
Try asking these questions in Copilot Chat:

```
How do I read a file in Python?
```

```
What's the difference between let and const in JavaScript?
```

```
Explain async/await in simple terms
```

### Exercise 2: Code-Specific Questions
1. Open any code file in your project
2. Select some code
3. Ask questions about it:

```
What does this function do?
```

```
How can I make this more efficient?
```

```
Are there any bugs in this code?
```

### Exercise 3: Using Slash Commands
1. Open a code file
2. Select a function
3. Try these commands:

```
/explain
```

```
/tests
```

```
/doc
```

### Exercise 4: Multi-Turn Conversations
Ask follow-up questions to dive deeper:

**You:** How do I sort an array in JavaScript?

**Copilot:** [explains sort()]

**You:** How do I sort by a specific property?

**Copilot:** [explains sorting objects]

**You:** What if I need to sort in descending order?

**Copilot:** [explains reverse sorting]

---

## 💡 Tips for Effective Questions

### Be Specific
❌ "How do I do authentication?"
✅ "How do I implement JWT authentication in a Node.js Express app?"

### Provide Context
❌ "Why isn't this working?"
✅ "This function should return the sum of all numbers, but it returns undefined. What's wrong?"

### Ask for Examples
❌ "Explain promises"
✅ "Explain promises with a practical example of fetching data"

### Request Specific Formats
❌ "How do I validate input?"
✅ "Write a TypeScript function to validate email addresses with proper error messages"

---

## 🔍 Understanding Context

Copilot Chat uses context from:

1. **Currently Open File** - The file you're viewing
2. **Selected Code** - Any text you've highlighted
3. **Recent Files** - Files you've recently edited
4. **Conversation History** - Previous messages in the chat
5. **@mentions** - Specific context you reference

### Using @mentions for Context
```
@workspace How is authentication handled in this project?
```

```
@vscode How do I configure the debugger?
```

```
@terminal What was the last error message?
```

---

## 📋 Common Use Cases

### Getting Started with a New Codebase
```
@workspace Give me an overview of this project structure
```

```
@workspace Where is the main entry point?
```

### Learning New Concepts
```
Explain the Observer pattern with a TypeScript example
```

### Debugging Help
```
I'm getting this error: [paste error]. What's causing it?
```

### Code Review
```
Review this code for security vulnerabilities
```

### Generating Code
```
Write a function that validates a credit card number using the Luhn algorithm
```

---

## ⚠️ Things to Keep in Mind

1. **Copilot may not have current information** - Training data has a cutoff date
2. **Always verify generated code** - Test before using in production
3. **Copilot doesn't have access to external systems** - It can't access your database or APIs
4. **Context is limited** - Large codebases may need specific file references
5. **Regenerate if needed** - You can ask Copilot to try again

---

## 🎓 Practice Prompts

Try these prompts to practice using Copilot Chat:

1. "Create a utility function to deep clone objects in TypeScript"
2. "What are the SOLID principles? Give me examples in Python"
3. "How do I set up ESLint with Prettier in a React project?"
4. "Write a regex to validate phone numbers in multiple formats"
5. "Explain the difference between composition and inheritance"
6. "Generate a README template for an open-source project"
7. "What are common security vulnerabilities in web applications?"
8. "How do I optimize database queries in PostgreSQL?"

---

## ✅ Key Takeaways

- Use keyboard shortcuts for quick access
- Slash commands speed up common tasks
- Be specific in your questions
- Use @mentions for targeted context
- Follow up to dive deeper into topics
- Always verify and test generated code

---

**NEXT:** Move on to [13-inline-chat.py](13-inline-chat.py) to learn about inline code editing with Copilot!
