# Scenario 14: Workspace Context

Learn how to use `@workspace` and other context providers for project-aware assistance.

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `app.py` | Main Flask application |
| `models.py` | Database models |
| `services.py` | Business logic layer |
| `config.py` | Configuration settings |

## 🎯 Learning Objectives

- Use `@workspace` for project-wide context
- Reference specific files with `#file`
- Use other context providers (`@vscode`, `@terminal`)
- Ask questions that span multiple files

## 📝 Context Providers

### @workspace
Use `@workspace` to ask questions about your entire project:

```
@workspace What is the overall architecture of this project?
```

```
@workspace How is authentication implemented?
```

```
@workspace Find all usages of the User model
```

### #file
Reference specific files for targeted context:

```
#file:models.py How can I add a new field to the User model?
```

```
#file:app.py #file:config.py How is the database configured?
```

### @vscode
Ask about VS Code features and settings:

```
@vscode How do I set up debugging for Python?
```

```
@vscode What keyboard shortcuts are available for refactoring?
```

### @terminal
Reference recent terminal output:

```
@terminal What does this error mean?
```

```
@terminal How can I fix the issue from the last command?
```

## 🏋️ Exercises

### Exercise 1: Project Overview
Ask Copilot to explain this mini-project:
```
@workspace Give me an overview of this Flask application
```

### Exercise 2: Cross-File Understanding
Ask about relationships between files:
```
@workspace How do models.py and services.py work together?
```

### Exercise 3: Finding Patterns
Ask Copilot to find patterns in the codebase:
```
@workspace What error handling patterns are used in this project?
```

### Exercise 4: Adding Features
Ask Copilot how to add a new feature:
```
@workspace How would I add a new endpoint to delete users?
```

### Exercise 5: Code Review
Ask for a project-wide code review:
```
@workspace Are there any security concerns in this code?
```

## 💡 Tips

- Start with `@workspace` for broad questions
- Use `#file` when you need specific file context
- Combine context providers for complex questions
- Ask follow-up questions for deeper understanding

## ⚠️ Limitations

- Very large workspaces may have limited context
- Binary files and large data files are excluded
- Some generated/build files may be ignored
