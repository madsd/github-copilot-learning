# Scenario 18: Plan Mode

Learn how to use Plan Mode to create and review execution plans before making changes.

## 🎯 Learning Objectives

- Understand when to use Plan mode
- Create detailed implementation plans
- Review and modify plans before execution
- Use plans for complex refactoring

---

## 📝 What is Plan Mode?

Plan Mode tells Copilot to **think before acting**:
1. Analyze the request thoroughly
2. Create a step-by-step plan
3. Show you the plan for review
4. Execute only after your approval

### When to Use Plan Mode

| Use Plan Mode | Use Regular Mode |
|---------------|------------------|
| Large refactoring | Quick fixes |
| Multi-file changes | Single file edits |
| Architectural decisions | Simple completions |
| When you want oversight | When speed matters |
| Learning new codebases | Familiar code |

---

## 🔧 How to Use Plan Mode

### Method 1: Ask for a Plan
```
Create a plan to implement user authentication with JWT tokens.
Don't execute yet, just show me the plan.
```

### Method 2: Use Think Mode
```
Think through how we should refactor this monolithic service 
into microservices, then present a plan.
```

### Method 3: Step-by-Step Request
```
I want to add caching to this application. First, analyze the 
current architecture and propose a plan before making any changes.
```

---

## 🏋️ Exercises

### Exercise 1: Feature Planning

Ask Copilot to plan a new feature:

```
Plan the implementation of a notification system that:
- Supports email, SMS, and push notifications
- Has configurable templates
- Includes rate limiting
- Logs all notifications

Show me the plan with:
1. Files to create/modify
2. Dependencies needed
3. Database schema changes
4. Implementation order
```

### Exercise 2: Refactoring Plan

Get a plan for refactoring:

```
Create a detailed plan to refactor the user authentication 
from session-based to JWT-based authentication.

Include:
- Security considerations
- Migration strategy for existing users
- Backward compatibility approach
- Testing strategy
```

### Exercise 3: Migration Plan

Plan a technology migration:

```
Plan the migration of this Express.js application to Fastify:
- Identify all Express-specific code
- Map Express patterns to Fastify equivalents
- Create a phased migration approach
- Define rollback procedures

Show the plan without executing.
```

### Exercise 4: Architecture Plan

Get architectural guidance:

```
Analyze this codebase and create a plan to implement 
the repository pattern for data access:
- Current state analysis
- Proposed structure
- Interfaces to create
- Files to modify
- Step-by-step implementation order
```

### Exercise 5: Testing Plan

Plan a testing strategy:

```
Create a comprehensive testing plan for this project:
- Unit test coverage gaps
- Integration tests needed
- E2E test scenarios
- Test data strategy
- CI/CD integration

Prioritize by impact and effort.
```

---

## 📋 Plan Template

When asking for plans, request this structure:

```
## Overview
Brief description of what will be accomplished

## Prerequisites
- Dependencies needed
- Environment setup
- Required access/permissions

## Files to Change
| File | Action | Description |
|------|--------|-------------|
| ... | Create/Modify/Delete | ... |

## Step-by-Step Plan
1. Step one with details
2. Step two with details
...

## Testing Strategy
How to verify each step

## Rollback Plan
How to undo if needed

## Risks and Mitigations
Potential issues and solutions
```

---

## 💡 Tips for Effective Planning

### 1. Request Alternatives
```
Plan three different approaches to implement caching, 
with pros and cons of each.
```

### 2. Ask for Justification
```
Explain why you chose this approach over alternatives.
```

### 3. Set Constraints
```
Plan this implementation with the constraint that we 
cannot change the public API or database schema.
```

### 4. Request Estimates
```
Include rough time estimates for each step.
```

### 5. Ask About Dependencies
```
What steps can be done in parallel? What must be sequential?
```

---

## 🔍 Reviewing Plans

### Questions to Ask
- Does this match my expectations?
- Are there any missing steps?
- Is the order optimal?
- Are the risks acceptable?
- Is the testing strategy sufficient?

### Modifying Plans
```
I like the plan, but:
- Move step 3 before step 2
- Add error handling to step 4
- Include a step for documentation
```

### Approving Execution
```
The plan looks good. Proceed with step 1 only.
```

Or:
```
Execute the full plan.
```

---

## ⚠️ Common Pitfalls

1. **Plans too vague**: Ask for more detail
2. **Missing edge cases**: Request edge case handling
3. **No rollback strategy**: Always ask for rollback plans
4. **Underestimating scope**: Ask about hidden complexity
5. **Forgetting tests**: Include testing in every plan

---

## ✅ Key Takeaways

- Plan mode helps you think before acting
- Request structured, detailed plans
- Review plans carefully before execution
- Ask for alternatives and trade-offs
- Include testing and rollback strategies
- Modify plans as needed before proceeding

---

**NEXT:** Move on to [19-custom-agents.md](19-custom-agents.md) to learn about creating custom Copilot agents!
