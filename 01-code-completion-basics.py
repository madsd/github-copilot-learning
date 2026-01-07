"""
Scenario 01: Code Completion Basics
====================================
Learn how GitHub Copilot suggests code as you type.

INSTRUCTIONS:
1. Go to each TODO comment and read what to do
2. Position your cursor on the BLANK LINE below the TODO
3. Start typing the suggested code - Copilot will offer completions
4. Press Tab to accept, Esc to dismiss, or Alt+] to see alternatives

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
# TODO: On the blank line below, type 'full_name = ' and see what Copilot suggests


# =============================================================================
# EXERCISE 2: List Completion
# =============================================================================
# Copilot recognizes patterns and continues them

days_of_week = ["Monday", "Tuesday", "Wednesday"]  # <- Add a comma after the ]
# TODO: Place cursor at the end of the list above, add a comma, press Enter
#       Copilot will suggest the next days of the week


# =============================================================================
# EXERCISE 3: Dictionary Completion
# =============================================================================
# Copilot understands data structures and suggests appropriate keys/values

user = {
    "name": "John Doe",
    "email": "john@example.com",
    # TODO: Place cursor at the end of the email line (after the comma)
    #       Press Enter and start typing a quote " to see field suggestions
}


# =============================================================================
# EXERCISE 4: Function Completion
# =============================================================================
# Copilot can complete entire function bodies based on the name

def calculate_area_of_circle(radius):
    # TODO: Delete 'pass', type 'return' and let Copilot complete
    pass


def is_palindrome(text):
    # TODO: Delete 'pass', type 'return' and let Copilot complete
    pass


# =============================================================================
# EXERCISE 5: Import Statement Completion
# =============================================================================
# Copilot suggests common imports based on your code context

# TODO: On the blank line below, type 'import ' and see common suggestions
#       Or try 'from datetime import ' and see available options



# =============================================================================
# EXERCISE 6: Loop Completion
# =============================================================================
# Copilot recognizes iteration patterns

numbers = [1, 2, 3, 4, 5]

# TODO: On the blank line below, type 'for ' and let Copilot suggest the loop



# =============================================================================
# EXERCISE 7: Class Completion
# =============================================================================
# Copilot can generate class structures

class Rectangle:
    # TODO: Delete 'pass' below, type 'def __init__' and let Copilot complete
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
