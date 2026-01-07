"""
Scenario 01: Code Completion Basics
====================================
Learn how GitHub Copilot suggests code as you type.

INSTRUCTIONS:
1. Place your cursor at the end of each TODO line
2. Start typing or press Enter to see Copilot suggestions
3. Press Tab to accept, Esc to dismiss, or Alt+] to see alternatives

WHAT YOU'LL LEARN:
- Basic code completion
- How Copilot uses context from your code
- Accepting and cycling through suggestions
"""

# =============================================================================
# EXERCISE 1: Variable Name Completion
# =============================================================================
# Copilot learns from variable names and suggests appropriate values

first_name = "Alice"
last_name = "Smith"
# TODO: Start typing 'full_name = ' and see what Copilot suggests


# =============================================================================
# EXERCISE 2: List Completion
# =============================================================================
# Copilot recognizes patterns and continues them

days_of_week = ["Monday", "Tuesday", "Wednesday"]
# TODO: Continue the list - add a comma after Wednesday and press Enter


# =============================================================================
# EXERCISE 3: Dictionary Completion
# =============================================================================
# Copilot understands data structures and suggests appropriate keys/values

user = {
    "name": "John Doe",
    "email": "john@example.com",
    # TODO: Add more fields - what does Copilot suggest?
}


# =============================================================================
# EXERCISE 4: Function Completion
# =============================================================================
# Copilot can complete entire function bodies based on the name

def calculate_area_of_circle(radius):
    # TODO: Let Copilot complete this function
    pass


def is_palindrome(text):
    # TODO: Let Copilot complete this function
    pass


# =============================================================================
# EXERCISE 5: Import Statement Completion
# =============================================================================
# Copilot suggests common imports based on your code context

# TODO: Type 'import ' and see common suggestions
# TODO: Type 'from datetime import ' and see available options


# =============================================================================
# EXERCISE 6: Loop Completion
# =============================================================================
# Copilot recognizes iteration patterns

numbers = [1, 2, 3, 4, 5]

# TODO: Type 'for ' and let Copilot suggest the loop structure


# =============================================================================
# EXERCISE 7: Class Completion
# =============================================================================
# Copilot can generate class structures

class Rectangle:
    # TODO: Let Copilot suggest __init__ and methods
    pass


# =============================================================================
# BONUS CHALLENGE
# =============================================================================
# Try creating your own scenarios! Start typing and see what Copilot suggests:
# - A function to validate an email address
# - A class representing a bank account
# - A list of countries and their capitals

# Your code here:


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
✅ Copilot uses context from your code to make intelligent suggestions
✅ Variable names and function names guide what Copilot suggests
✅ Press Tab to accept, Esc to dismiss, Alt+] to see alternatives
✅ The more context you provide, the better the suggestions
✅ Copilot learns from patterns in your code

NEXT: Move on to 02-code-explanation.py to learn how to understand existing code!
"""
