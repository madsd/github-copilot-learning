# Scenario 15: Terminal Commands

Learn how to use GitHub Copilot to generate and explain terminal commands.

## 🎯 Learning Objectives

- Generate shell commands with Copilot
- Explain complex command pipelines
- Get help with Git commands
- Learn command-line tools

---

## 🔧 Ways to Get Terminal Help

### 1. Copilot Chat
Ask natural language questions about terminal commands:
```
How do I find all .js files modified in the last 7 days?
```

### 2. @terminal Context
Reference recent terminal output:
```
@terminal What does this error mean?
```

### 3. Inline Terminal Suggestions
Copilot can suggest commands as you type in the integrated terminal.

---

## 🏋️ Exercises

### Exercise 1: File Operations
Ask Copilot to generate commands for these tasks:

**Task 1: Find files**
```
How do I find all Python files larger than 1MB?
```

**Task 2: Bulk rename**
```
How do I rename all .txt files to .md in the current directory?
```

**Task 3: Delete old files**
```
How do I delete all .log files older than 30 days?
```

### Exercise 2: Git Commands
Ask Copilot about Git operations:

**Task 1: Undo changes**
```
How do I undo my last commit but keep the changes?
```

**Task 2: Branch cleanup**
```
How do I delete all merged branches except main?
```

**Task 3: Search history**
```
How do I find commits that modified a specific file?
```

**Task 4: Cherry-pick**
```
How do I apply a specific commit from another branch?
```

### Exercise 3: Process Management
Ask about system processes:

**Task 1: Find process**
```
How do I find which process is using port 3000?
```

**Task 2: Monitor resources**
```
How do I see the top 5 processes using the most memory?
```

**Task 3: Background jobs**
```
How do I run a command in the background and save output to a file?
```

### Exercise 4: Text Processing
Ask about text manipulation:

**Task 1: Search and replace**
```
How do I replace all occurrences of "foo" with "bar" in all .js files?
```

**Task 2: Extract data**
```
How do I extract all email addresses from a log file?
```

**Task 3: Count and sort**
```
How do I count word frequency in a file and show top 10?
```

### Exercise 5: Network Commands
Ask about networking:

**Task 1: Check connectivity**
```
How do I check if a server is reachable and measure response time?
```

**Task 2: Download files**
```
How do I download a file and resume if interrupted?
```

**Task 3: API testing**
```
How do I make a POST request with JSON data using curl?
```

---

## 📋 Common Command Categories

### Git Commands
| Task | Ask Copilot |
|------|-------------|
| Undo commit | "How do I undo my last commit?" |
| Stash changes | "How do I save my changes without committing?" |
| Rebase | "How do I rebase my branch onto main?" |
| View history | "How do I see commit history for a file?" |

### File System
| Task | Ask Copilot |
|------|-------------|
| Find files | "Find all files matching a pattern" |
| Disk usage | "Show disk usage by directory" |
| Compare files | "Compare two directories" |
| Archive files | "Create a compressed archive" |

### Docker
| Task | Ask Copilot |
|------|-------------|
| List containers | "How do I see running containers?" |
| Clean up | "How do I remove unused Docker images?" |
| Logs | "How do I follow logs from a container?" |
| Compose | "How do I run docker-compose in detached mode?" |

### NPM/Node
| Task | Ask Copilot |
|------|-------------|
| Audit | "How do I check for security vulnerabilities?" |
| Outdated | "How do I see which packages need updating?" |
| Scripts | "How do I run a script in a specific directory?" |
| Cache | "How do I clear the npm cache?" |

---

## 💡 Tips for Better Results

### Be Specific
❌ "How do I use grep?"
✅ "How do I search for 'error' in all log files, case-insensitive, showing line numbers?"

### Mention Your OS
```
On Windows, how do I find which process is using port 3000?
```

### Ask for Explanations
```
Explain each part of this command: find . -name "*.py" -exec grep -l "TODO" {} \;
```

### Request Safe Options
```
How do I delete old files? Show me a preview first without actually deleting.
```

---

## 🔍 Understanding Complex Commands

When you encounter a complex command, ask Copilot to explain it:

### Example 1: Find + Exec
```bash
find . -type f -name "*.log" -mtime +30 -exec rm {} \;
```
Ask: "Break down this command and explain what each part does"

### Example 2: Pipes and Redirects
```bash
cat access.log | grep "ERROR" | awk '{print $4}' | sort | uniq -c | sort -rn | head -10
```
Ask: "Explain this pipeline step by step"

### Example 3: Git Magic
```bash
git log --oneline --graph --all --decorate
```
Ask: "What do each of these git log options do?"

---

## ⚠️ Safety Tips

1. **Preview first**: Ask for dry-run or preview options before destructive operations
2. **Understand before running**: Ask Copilot to explain unfamiliar commands
3. **Backup important data**: Before bulk operations on files
4. **Use version control**: Commit before running scripts that modify code

---

## ✅ Key Takeaways

- Ask natural language questions about terminal commands
- Use `@terminal` to reference recent errors
- Be specific about your operating system
- Ask for explanations of complex commands
- Request safe/preview options for destructive operations
- Copilot can help with Git, Docker, npm, and more

---

**NEXT:** Move on to [16-multi-file-editing/](16-multi-file-editing/) to learn about Copilot Edits for multi-file changes!
