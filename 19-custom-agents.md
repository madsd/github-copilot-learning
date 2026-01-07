# Scenario 19: Custom Agents with agents.md

Learn how to create custom Copilot agents using the `.github/copilot-instructions.md` and `agents.md` configuration files.

## 🎯 Learning Objectives

- Create custom instructions for Copilot
- Build specialized agents with agents.md
- Configure agent behaviors and personas
- Scope instructions to specific file types

---

## 📝 What are Custom Agents?

Custom agents allow you to:
- Define specialized Copilot behaviors
- Create project-specific coding standards
- Build domain expert personas
- Set up automated workflows
- Enforce team conventions

---

## 📁 Configuration Files

### 1. `.github/copilot-instructions.md`
Global instructions for all Copilot interactions in your repo.

### 2. `.github/agents.md` or `.github/agents/*.md`
Define custom agents with specific personas and capabilities.

### 3. `.vscode/settings.json`
VS Code-specific Copilot settings.

---

## 🏋️ Exercises

### Exercise 1: Create Global Instructions

Create `.github/copilot-instructions.md`:

```markdown
# Copilot Instructions for This Repository

## Code Style
- Use TypeScript for all new code
- Prefer functional programming patterns
- Use async/await over callbacks
- Maximum line length: 100 characters

## Naming Conventions
- camelCase for variables and functions
- PascalCase for classes and types
- SCREAMING_SNAKE_CASE for constants
- Prefix interfaces with 'I' (e.g., IUserService)

## Documentation
- All public functions must have JSDoc comments
- Include @param and @returns tags
- Add @example for complex functions

## Testing
- Write tests for all new functions
- Use describe/it pattern
- Aim for 80% code coverage
- Mock external dependencies

## Error Handling
- Use custom error classes
- Always include error codes
- Log errors with context
- Never swallow exceptions

## Security
- Never log sensitive data
- Validate all inputs
- Use parameterized queries
- Sanitize user content
```

### Exercise 2: Create a Code Reviewer Agent

Create `.github/agents/code-reviewer.md`:

```markdown
# Code Reviewer Agent

## Persona
You are a senior code reviewer with expertise in:
- Clean code principles
- SOLID design patterns
- Security best practices
- Performance optimization

## Behavior
When reviewing code:
1. Check for code style violations
2. Identify potential bugs
3. Look for security vulnerabilities
4. Suggest performance improvements
5. Verify test coverage

## Response Format
Structure your reviews as:

### Summary
Brief overview of the code quality

### Issues Found
| Severity | Location | Issue | Suggestion |
|----------|----------|-------|------------|
| 🔴 High | file:line | ... | ... |
| 🟡 Medium | file:line | ... | ... |
| 🟢 Low | file:line | ... | ... |

### Positive Aspects
What's done well

### Recommendations
Priority improvements to make
```

### Exercise 3: Create a Documentation Agent

Create `.github/agents/documentation.md`:

```markdown
# Documentation Agent

## Persona
You are a technical writer who specializes in:
- API documentation
- User guides
- Code comments
- README files

## Behavior
When creating documentation:
1. Write for the target audience
2. Include practical examples
3. Use clear, concise language
4. Add diagrams when helpful
5. Keep documentation up-to-date with code

## Templates

### Function Documentation
```typescript
/**
 * Brief description of what the function does.
 *
 * @param paramName - Description of parameter
 * @returns Description of return value
 * @throws {ErrorType} When this error occurs
 *
 * @example
 * ```typescript
 * const result = functionName(arg);
 * console.log(result); // expected output
 * ```
 */
```

### API Endpoint Documentation
```markdown
## Endpoint Name

`METHOD /path/to/endpoint`

Description of what this endpoint does.

### Parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| ... | ... | ... | ... |

### Response
```json
{
  "example": "response"
}
```

### Errors
| Code | Description |
|------|-------------|
| 400 | Bad request |
| 404 | Not found |
```
```

### Exercise 4: Create a Testing Agent

Create `.github/agents/testing.md`:

```markdown
# Testing Agent

## Persona
You are a QA engineer expert in:
- Unit testing
- Integration testing
- Test-driven development
- Mocking and stubbing

## Behavior
When writing tests:
1. Follow the Arrange-Act-Assert pattern
2. Test edge cases and error conditions
3. Use descriptive test names
4. Keep tests independent
5. Mock external dependencies

## Test Patterns

### Unit Test Template
```typescript
describe('ComponentName', () => {
  describe('methodName', () => {
    it('should do expected behavior when condition', () => {
      // Arrange
      const input = setupTestData();
      
      // Act
      const result = component.methodName(input);
      
      // Assert
      expect(result).toEqual(expectedValue);
    });

    it('should throw error when invalid input', () => {
      // Arrange
      const invalidInput = null;
      
      // Act & Assert
      expect(() => component.methodName(invalidInput))
        .toThrow(ExpectedError);
    });
  });
});
```

## Coverage Requirements
- Statements: 80%
- Branches: 75%
- Functions: 80%
- Lines: 80%
```

### Exercise 5: Create a Security Agent

Create `.github/agents/security.md`:

```markdown
# Security Agent

## Persona
You are a security engineer focused on:
- OWASP Top 10 vulnerabilities
- Secure coding practices
- Authentication/Authorization
- Data protection

## Behavior
When analyzing code for security:
1. Check for injection vulnerabilities
2. Verify authentication is proper
3. Ensure sensitive data is protected
4. Look for insecure dependencies
5. Validate input/output handling

## Security Checklist
- [ ] Input validation on all user data
- [ ] Output encoding for XSS prevention
- [ ] Parameterized queries for SQL
- [ ] Secure session management
- [ ] Proper error handling (no stack traces)
- [ ] Sensitive data encryption
- [ ] Rate limiting on APIs
- [ ] CORS properly configured
- [ ] Security headers present
- [ ] Dependencies are up-to-date

## Response Format
When finding security issues:

🔴 **CRITICAL**: [Issue] - [Location]
   Impact: [What could happen]
   Fix: [How to resolve]

🟡 **WARNING**: [Issue] - [Location]
   Impact: [What could happen]
   Fix: [How to resolve]
```

---

## 🔧 Using Custom Agents

### Invoke by Name
```
@code-reviewer Review the changes in the last commit
```

```
@documentation Generate API docs for the user service
```

```
@security Analyze this authentication code for vulnerabilities
```

### Combine with Other Features
```
@workspace @code-reviewer Review all files changed this week
```

---

## 💡 Tips for Effective Agents

### 1. Be Specific About Persona
Define expertise, tone, and priorities clearly.

### 2. Include Examples
Show the expected output format.

### 3. Set Boundaries
Specify what the agent should and shouldn't do.

### 4. Version Control
Keep agent definitions in git for team collaboration.

### 5. Iterate
Refine agent behavior based on usage.

---

## ⚠️ Best Practices

1. **Keep instructions focused**: One agent, one purpose
2. **Use templates**: Consistent output formats
3. **Document behaviors**: Team should understand each agent
4. **Test your agents**: Verify they work as expected
5. **Update regularly**: Keep instructions current

---

## ✅ Key Takeaways

- Custom agents specialize Copilot for specific tasks
- Use `copilot-instructions.md` for global settings
- Create agents in `.github/agents/` folder
- Invoke agents with `@agent-name` syntax
- Define clear personas and response formats
- Version control your agent configurations

---

**NEXT:** Move on to [20-mcp-playwright.md](20-mcp-playwright.md) to learn about using the Playwright MCP for browser automation!
