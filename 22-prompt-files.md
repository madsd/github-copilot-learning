# Scenario 22: Prompt Files (.prompt.md)

Learn how to create reusable prompt templates with `.prompt.md` files for consistent, repeatable Copilot interactions.

## 🎯 Learning Objectives

- Create and organize prompt files
- Use variables and context in prompts
- Share prompts across your team
- Build prompt libraries for common tasks

---

## 📝 What are Prompt Files?

Prompt files (`.prompt.md`) are reusable templates that:
- Define structured prompts for Copilot
- Include variables for customization
- Can reference files and context
- Are shareable and version-controlled

### Benefits
- **Consistency**: Same prompt format every time
- **Efficiency**: No retyping common prompts
- **Collaboration**: Share best prompts with team
- **Documentation**: Prompts serve as process docs

---

## 📁 File Locations

```
your-project/
├── .github/
│   └── prompts/              # Shared team prompts
│       ├── code-review.prompt.md
│       ├── test-generator.prompt.md
│       └── documentation.prompt.md
├── .vscode/
│   └── prompts/              # Project-specific prompts
│       └── api-endpoint.prompt.md
└── prompts/                  # Alternative location
    └── refactor.prompt.md
```

---

## 🔧 Basic Syntax

### Simple Prompt File

Create `.github/prompts/explain-code.prompt.md`:

```markdown
---
name: Explain Code
description: Get a detailed explanation of selected code
---

Explain this code in detail:
- What does it do?
- How does it work step by step?
- What are the inputs and outputs?
- Are there any edge cases to consider?
```

### Prompt with Variables

Create `.github/prompts/create-function.prompt.md`:

```markdown
---
name: Create Function
description: Generate a function with specified parameters
variables:
  - name: functionName
    description: Name of the function to create
  - name: language
    description: Programming language
    default: TypeScript
  - name: description
    description: What the function should do
---

Create a {{language}} function named `{{functionName}}` that:

{{description}}

Requirements:
- Include proper type annotations
- Add error handling
- Write JSDoc/docstring documentation
- Follow best practices for {{language}}
```

### Prompt with File Context

Create `.github/prompts/add-tests.prompt.md`:

```markdown
---
name: Add Tests
description: Generate tests for a file
variables:
  - name: testFramework
    default: jest
---

#file:{{filepath}}

Generate comprehensive tests for this file using {{testFramework}}.

Include:
- Unit tests for each function
- Edge case tests
- Error handling tests
- Mock external dependencies

Follow the existing test patterns in the project.
```

---

## 🏋️ Exercises

### Exercise 1: Create a Code Review Prompt

Create `.github/prompts/code-review.prompt.md`:

```markdown
---
name: Code Review
description: Perform a thorough code review
variables:
  - name: focus
    description: Specific area to focus on
    default: general
---

Review this code with focus on: {{focus}}

Check for:
## Security
- [ ] Input validation
- [ ] SQL injection prevention
- [ ] XSS vulnerabilities
- [ ] Sensitive data exposure

## Performance
- [ ] Unnecessary loops
- [ ] N+1 queries
- [ ] Memory leaks
- [ ] Caching opportunities

## Code Quality
- [ ] Clear naming
- [ ] Single responsibility
- [ ] DRY violations
- [ ] Error handling

## Testing
- [ ] Test coverage
- [ ] Edge cases
- [ ] Mocking strategy

Provide specific line numbers and suggestions for improvements.
```

### Exercise 2: Create an API Endpoint Prompt

Create `.github/prompts/api-endpoint.prompt.md`:

```markdown
---
name: Create API Endpoint
description: Generate a new REST API endpoint
variables:
  - name: method
    description: HTTP method (GET, POST, PUT, DELETE)
  - name: path
    description: Endpoint path
  - name: resource
    description: Resource name
  - name: description
    description: What the endpoint does
---

Create a {{method}} endpoint at `{{path}}` for {{resource}}.

Description: {{description}}

Include:
1. Route handler with proper middleware
2. Request validation (params, query, body)
3. Service layer method
4. Database query/mutation
5. Response formatting
6. Error handling with appropriate status codes
7. OpenAPI/Swagger documentation
8. Unit tests

Follow the existing patterns in:
#file:src/routes/index.ts
#file:src/services/example.service.ts
```

### Exercise 3: Create a Refactoring Prompt

Create `.github/prompts/refactor.prompt.md`:

```markdown
---
name: Refactor Code
description: Refactor code following best practices
variables:
  - name: pattern
    description: Design pattern or technique to apply
  - name: constraints
    description: Any constraints to follow
    default: none
---

Refactor this code applying: {{pattern}}

Constraints: {{constraints}}

Guidelines:
- Maintain existing functionality
- Keep the public API unchanged
- Add/update tests for refactored code
- Document significant changes
- Consider backward compatibility

Show:
1. Before/after comparison
2. Explanation of changes
3. Benefits of the refactoring
4. Any potential risks
```

### Exercise 4: Create a Documentation Prompt

Create `.github/prompts/generate-docs.prompt.md`:

```markdown
---
name: Generate Documentation
description: Create comprehensive documentation
variables:
  - name: docType
    description: Type of documentation (API, README, guide)
  - name: audience
    description: Target audience
    default: developers
---

Generate {{docType}} documentation for {{audience}}.

#file:{{filepath}}

Include:
- Overview and purpose
- Installation/setup instructions
- Usage examples with code snippets
- API reference (if applicable)
- Configuration options
- Troubleshooting common issues
- Contributing guidelines (if README)

Format:
- Use clear headings
- Include code blocks with syntax highlighting
- Add tables for parameters/options
- Link to related documentation
```

### Exercise 5: Create a Bug Fix Prompt

Create `.github/prompts/fix-bug.prompt.md`:

```markdown
---
name: Fix Bug
description: Analyze and fix a bug
variables:
  - name: errorMessage
    description: The error message or bug description
  - name: expectedBehavior
    description: What should happen
  - name: actualBehavior
    description: What is happening
---

## Bug Report

**Error/Issue:** {{errorMessage}}

**Expected:** {{expectedBehavior}}

**Actual:** {{actualBehavior}}

## Analysis Request

1. Identify the root cause of this bug
2. Explain why it's happening
3. Propose a fix with code changes
4. Add a test that would have caught this bug
5. Suggest preventive measures

Consider:
- Edge cases that might be related
- Similar patterns elsewhere in the codebase
- Potential regression risks
```

### Exercise 6: Create a Migration Prompt

Create `.github/prompts/migrate.prompt.md`:

```markdown
---
name: Code Migration
description: Migrate code to new version/framework
variables:
  - name: from
    description: Current version/framework
  - name: to
    description: Target version/framework
  - name: scope
    description: What to migrate
---

Migrate {{scope}} from {{from}} to {{to}}.

Steps:
1. Analyze current implementation
2. Identify breaking changes between versions
3. Create migration plan
4. Update code with new syntax/patterns
5. Update dependencies
6. Add/update tests
7. Document changes

For each change:
- Show before/after code
- Explain the reason for the change
- Note any behavioral differences

Check:
- Deprecated APIs
- Changed defaults
- New required configurations
- Removed features
```

---

## 📋 Using Prompt Files

### From Command Palette
1. `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type "Copilot: Use Prompt"
3. Select your prompt file
4. Fill in variables

### From Chat
```
/prompt code-review focus:security
```

### With File Selection
1. Select code in editor
2. Run prompt from command palette
3. Selected code is included automatically

---

## 💡 Advanced Features

### Conditional Sections

```markdown
---
variables:
  - name: includeTests
    type: boolean
    default: true
---

Create the implementation.

{{#if includeTests}}
## Tests
Also create comprehensive tests including:
- Unit tests
- Integration tests
- Edge cases
{{/if}}
```

### Multiple File Context

```markdown
---
name: Cross-File Refactor
---

Refactor considering these related files:

#file:src/models/user.ts
#file:src/services/user.service.ts
#file:src/controllers/user.controller.ts

Ensure consistency across all layers.
```

### Workspace Context

```markdown
---
name: Project-Aware Generation
---

@workspace

Based on the project structure and existing patterns,
generate code that follows the established conventions.
```

---

## 🗂️ Organizing Prompt Libraries

### By Task Type
```
prompts/
├── generation/
│   ├── function.prompt.md
│   ├── class.prompt.md
│   └── api-endpoint.prompt.md
├── review/
│   ├── code-review.prompt.md
│   ├── security-audit.prompt.md
│   └── performance-review.prompt.md
├── documentation/
│   ├── readme.prompt.md
│   ├── api-docs.prompt.md
│   └── changelog.prompt.md
└── testing/
    ├── unit-tests.prompt.md
    ├── integration-tests.prompt.md
    └── e2e-tests.prompt.md
```

### By Role
```
prompts/
├── frontend/
├── backend/
├── devops/
└── qa/
```

---

## 🤝 Team Sharing

### Repository Prompts
Store in `.github/prompts/` for team-wide access.

### Prompt Packages
Create npm/pip packages with prompt collections:

```json
{
  "name": "@myorg/copilot-prompts",
  "files": ["prompts/"]
}
```

### Documentation
Create a prompt catalog README:

```markdown
# Team Prompt Library

| Prompt | Description | Usage |
|--------|-------------|-------|
| code-review | Standard code review | `/prompt code-review` |
| api-endpoint | Create REST endpoint | `/prompt api-endpoint method:POST` |
```

---

## ⚠️ Best Practices

1. **Be Specific**: Clear, detailed prompts get better results
2. **Use Variables**: Make prompts reusable with parameters
3. **Include Context**: Reference relevant files when needed
4. **Version Control**: Track prompt changes in git
5. **Document Usage**: Add descriptions and examples
6. **Test Prompts**: Verify prompts work as expected
7. **Iterate**: Refine prompts based on results

---

## ✅ Key Takeaways

- Prompt files create reusable, consistent prompts
- Use variables for customization
- Store in `.github/prompts/` for team sharing
- Include file context with `#file:` syntax
- Organize prompts by task or role
- Version control your prompt library

---

**🎉 Congratulations!** You've completed the full GitHub Copilot Learning Path!

Return to the [README](README.md) to review all scenarios.
