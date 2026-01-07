"""
Scenario 17: Agent Mode
========================
Use GitHub Copilot's Agent Mode for autonomous multi-step tasks.

INSTRUCTIONS:
1. Open Copilot Chat
2. Select "Agent" mode from the dropdown (or type @agent)
3. Describe a complex task and let Copilot work autonomously

WHAT YOU'LL LEARN:
- When to use Agent mode vs. regular chat
- How Agent mode executes multiple steps
- Reviewing and approving agent actions
- Best practices for agent prompts
"""

# =============================================================================
# UNDERSTANDING AGENT MODE
# =============================================================================
"""
Agent Mode allows Copilot to:
- Break down complex tasks into steps
- Execute terminal commands
- Create and edit multiple files
- Make decisions based on results
- Iterate until the task is complete

WHEN TO USE AGENT MODE:
✅ Setting up new projects
✅ Implementing features across multiple files
✅ Running and fixing tests iteratively
✅ Debugging complex issues
✅ Refactoring large codebases
✅ Build and deployment tasks

WHEN NOT TO USE:
❌ Simple code completions
❌ Quick explanations
❌ Single-file edits
❌ When you need full control of each step
"""


# =============================================================================
# EXERCISE 1: Project Setup
# =============================================================================
"""
Use Agent mode to set up a new project.

PROMPT TO TRY:
"Create a new Python FastAPI project with:
- A users endpoint with CRUD operations
- SQLAlchemy with SQLite
- Pydantic models for validation
- Basic authentication
- pytest tests
- A requirements.txt file"

Agent will:
1. Create project structure
2. Generate all necessary files
3. Install dependencies
4. Run initial tests
"""


# =============================================================================
# EXERCISE 2: Bug Investigation
# =============================================================================
"""
Let Agent mode investigate and fix a bug.

PROMPT TO TRY:
"The tests in test_calculator.py are failing. Investigate why,
fix the issues, and make sure all tests pass."

Agent will:
1. Run the tests to see failures
2. Analyze the error messages
3. Examine the relevant code
4. Make fixes
5. Re-run tests to verify
"""

# Sample code with bugs for the agent to fix
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b  # Bug: should handle None values
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b  # Bug: no zero check


# =============================================================================
# EXERCISE 3: Feature Implementation
# =============================================================================
"""
Use Agent mode to implement a complete feature.

PROMPT TO TRY:
"Add a caching layer to the user service:
- Use Redis for caching
- Cache user lookups for 5 minutes
- Invalidate cache on updates
- Add configuration for Redis connection
- Write tests for the caching behavior"

Agent will:
1. Analyze existing code structure
2. Plan the implementation
3. Create/modify necessary files
4. Add dependencies
5. Write tests
6. Verify everything works
"""


# =============================================================================
# EXERCISE 4: Code Migration
# =============================================================================
"""
Let Agent mode handle a code migration.

PROMPT TO TRY:
"Migrate this project from JavaScript to TypeScript:
- Convert all .js files to .ts
- Add proper type annotations
- Set up tsconfig.json
- Update package.json scripts
- Fix any type errors"

Agent will iterate through files, convert them,
and resolve type errors until the migration is complete.
"""


# =============================================================================
# EXERCISE 5: Performance Optimization
# =============================================================================
"""
Use Agent mode for performance analysis and fixes.

PROMPT TO TRY:
"Analyze this codebase for performance issues:
- Find slow database queries
- Identify N+1 query problems
- Look for missing indexes
- Suggest and implement optimizations
- Add performance logging"
"""


# =============================================================================
# AGENT MODE BEST PRACTICES
# =============================================================================
"""
1. BE SPECIFIC ABOUT GOALS
   ❌ "Make the code better"
   ✅ "Refactor the user service to use dependency injection,
       add proper error handling, and ensure 80% test coverage"

2. SET BOUNDARIES
   ❌ "Fix everything"
   ✅ "Fix the failing tests in the auth module without
       changing the public API"

3. REVIEW EACH STEP
   - Agent will ask for approval on significant actions
   - Review terminal commands before execution
   - Check file changes before accepting

4. PROVIDE CONTEXT
   - Mention relevant files: "Look at config.py for settings"
   - Specify conventions: "Follow the existing code style"
   - Note constraints: "Don't modify the database schema"

5. ITERATE
   - If the first attempt isn't perfect, provide feedback
   - "The tests pass but the error messages aren't helpful,
      please improve them"
"""


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
✅ Agent mode is for complex, multi-step tasks
✅ It can run commands, create files, and iterate
✅ Always review actions before approval
✅ Be specific about goals and constraints
✅ Use for project setup, debugging, migrations, and refactoring

NEXT: Move on to 18-plan-mode.md to learn about
      planning complex tasks before execution!
"""
