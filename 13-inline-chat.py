"""
Scenario 13: Inline Chat
=========================
Use Ctrl+I / Cmd+I for inline code edits with Copilot.

INSTRUCTIONS:
1. Place your cursor in the code or select a section
2. Press Ctrl+I (Windows/Linux) or Cmd+I (Mac)
3. Type your instruction and press Enter
4. Review the diff and Accept or Discard

WHAT YOU'LL LEARN:
- Using inline chat for quick edits
- Making targeted code changes
- Refactoring with inline chat
- Generating code in-place
"""

# =============================================================================
# EXERCISE 1: Generate Code at Cursor
# =============================================================================
# Place your cursor below this line and press Ctrl+I
# Type: "create a function that calculates the factorial of a number"

# YOUR CODE WILL BE INSERTED HERE


# =============================================================================
# EXERCISE 2: Modify Existing Code
# =============================================================================
# Select the function below, press Ctrl+I, and ask to modify it

def greet(name):
    return f"Hello, {name}!"

# TODO: Select the function above, press Ctrl+I, and type:
# "Add an optional greeting parameter with default 'Hello'"


# =============================================================================
# EXERCISE 3: Add Error Handling
# =============================================================================
# Select this function and use inline chat to add error handling

def divide_numbers(a, b):
    return a / b

# TODO: Select the function, press Ctrl+I, and type:
# "Add error handling for division by zero"


# =============================================================================
# EXERCISE 4: Add Type Hints
# =============================================================================
# Select this function and add type hints using inline chat

def process_items(items, filter_func, transform_func):
    result = []
    for item in items:
        if filter_func(item):
            result.append(transform_func(item))
    return result

# TODO: Select the function, press Ctrl+I, and type:
# "Add type hints using typing module"


# =============================================================================
# EXERCISE 5: Refactor Code
# =============================================================================
# Select this code and ask inline chat to refactor it

def get_user_info(user_dict):
    if user_dict is not None:
        if 'name' in user_dict:
            name = user_dict['name']
        else:
            name = 'Unknown'
        if 'email' in user_dict:
            email = user_dict['email']
        else:
            email = 'no-email@example.com'
        if 'age' in user_dict:
            age = user_dict['age']
        else:
            age = 0
        return {'name': name, 'email': email, 'age': age}
    else:
        return {'name': 'Unknown', 'email': 'no-email@example.com', 'age': 0}

# TODO: Select the function, press Ctrl+I, and type:
# "Refactor using dict.get() method"


# =============================================================================
# EXERCISE 6: Convert Code Style
# =============================================================================
# Select this class and convert it using inline chat

class OldStyleClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"OldStyleClass(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        if not isinstance(other, OldStyleClass):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

# TODO: Select the class, press Ctrl+I, and type:
# "Convert to a Python dataclass"


# =============================================================================
# EXERCISE 7: Add Documentation
# =============================================================================
# Select this function and add documentation

def calculate_compound_interest(principal, rate, time, n=12):
    amount = principal * (1 + rate / n) ** (n * time)
    return round(amount - principal, 2)

# TODO: Select the function, press Ctrl+I, and type:
# "Add a detailed docstring with examples"


# =============================================================================
# EXERCISE 8: Optimize Code
# =============================================================================
# Select this function and ask to optimize it

def find_duplicates_slow(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

# TODO: Select the function, press Ctrl+I, and type:
# "Optimize this for better performance using a set"


# =============================================================================
# EXERCISE 9: Generate Test Code
# =============================================================================
# Place cursor below and generate tests inline

def is_valid_email(email):
    """Check if email is valid."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# TODO: Place cursor below, press Ctrl+I, and type:
# "Generate pytest tests for is_valid_email function"


# =============================================================================
# EXERCISE 10: Add Logging
# =============================================================================
# Select this function and add logging

def process_order(order_id, items, customer_id):
    total = sum(item['price'] * item['quantity'] for item in items)
    discount = 0.1 if total > 100 else 0
    final_total = total * (1 - discount)
    return {
        'order_id': order_id,
        'customer_id': customer_id,
        'total': final_total,
        'discount_applied': discount > 0
    }

# TODO: Select the function, press Ctrl+I, and type:
# "Add logging statements using the logging module"


# =============================================================================
# EXERCISE 11: Make Async
# =============================================================================
# Select this function and convert to async

def fetch_user_data(user_id):
    # Simulates a database call
    import time
    time.sleep(0.1)  # Simulate network delay
    return {'id': user_id, 'name': f'User {user_id}'}

def fetch_all_users(user_ids):
    return [fetch_user_data(uid) for uid in user_ids]

# TODO: Select both functions, press Ctrl+I, and type:
# "Convert to async using asyncio"


# =============================================================================
# EXERCISE 12: Multi-Line Generation
# =============================================================================
# Position cursor and generate a complete class

# TODO: Place cursor below, press Ctrl+I, and type:
# "Create a Stack class with push, pop, peek, is_empty, and size methods"


# =============================================================================
# INLINE CHAT TIPS
# =============================================================================
"""
✅ KEYBOARD SHORTCUTS:
   - Ctrl+I / Cmd+I: Open inline chat
   - Enter: Submit instruction
   - Escape: Cancel
   - Ctrl+Enter: Accept changes
   
✅ EFFECTIVE INSTRUCTIONS:
   - Be specific: "Add type hints" vs "improve code"
   - Specify standards: "Using Google docstring format"
   - Mention constraints: "Without external libraries"
   
✅ COMMON USE CASES:
   - Add error handling
   - Add type hints
   - Add documentation
   - Refactor code
   - Convert code style
   - Generate tests
   - Add logging
   - Make async
   
✅ REVIEW CHANGES:
   - Always review the diff before accepting
   - You can edit the instruction and try again
   - Accept partial changes if needed

NEXT: Move on to 14-workspace-context/ to learn about
      using @workspace for project-aware assistance!
"""
