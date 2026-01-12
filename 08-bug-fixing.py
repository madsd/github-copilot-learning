"""
Scenario 08: Bug Fixing
========================
Identify and fix bugs with GitHub Copilot assistance.

INSTRUCTIONS:
1. Each function below contains one or more bugs
2. Select the buggy code and ask Copilot to help
3. Use Copilot Chat or inline chat (Ctrl+I)
4. Ask: "Find and fix the bugs in this code"

WHAT YOU'LL LEARN:
- How Copilot identifies common bugs
- Using /fix command in Copilot Chat
- Understanding bug explanations
- Preventing similar bugs
"""

# =============================================================================
# EXERCISE 1: Off-by-One Error
# =============================================================================
# This function should return the last n elements of a list

def get_last_n_elements(lst, n):
    """Return the last n elements of a list."""
    if n <= 0:
        return []
    return lst[len(lst) - n + 1:]  # BUG: Off-by-one error

# Test it:
# print(get_last_n_elements([1, 2, 3, 4, 5], 3))  # Expected: [3, 4, 5]

# TODO: Select the function and ask Copilot: "/fix"


# =============================================================================
# EXERCISE 2: Type Mismatch
# =============================================================================
# This function calculates the average but has a bug

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # BUG: What if numbers is empty?

# Test it:
# print(calculate_average([]))  # This will crash!

# TODO: Ask Copilot to fix the division by zero bug


# =============================================================================
# EXERCISE 3: Incorrect Loop Logic
# =============================================================================
# This function should remove all occurrences of a value

def remove_all(lst, value):
    """Remove all occurrences of value from list."""
    for i in range(len(lst)):  # BUG: Modifying list while iterating
        if lst[i] == value:
            lst.pop(i)
    return lst

# Test it:
# print(remove_all([1, 2, 2, 3, 2, 4], 2))  # Expected: [1, 3, 4]

# TODO: Ask Copilot to identify and fix the bug


# =============================================================================
# EXERCISE 4: Reference vs Value Bug
# =============================================================================
# This function should create a matrix without shared references

def create_matrix(rows, cols, default_value=0):
    """Create a matrix filled with default value."""
    row = [default_value] * cols
    matrix = [row] * rows  # BUG: All rows reference the same list!
    return matrix

# Test it:
# m = create_matrix(3, 3)
# m[0][0] = 1
# print(m)  # Unexpected: All rows are modified!

# TODO: Ask Copilot: "Why does modifying one row affect all rows?"


# =============================================================================
# EXERCISE 5: String Manipulation Bug
# =============================================================================
# This function should properly escape HTML

def escape_html(text):
    """Escape HTML special characters."""
    text = text.replace("&", "&amp")  # BUG: Incomplete entity
    text = text.replace("<", "&lt")    # BUG: Incomplete entity
    text = text.replace(">", "&gt")    # BUG: Incomplete entity
    text = text.replace('"', "&quot")  # BUG: Incomplete entity
    return text

# TODO: Ask Copilot to fix the HTML entities


# =============================================================================
# EXERCISE 6: Scope Bug
# =============================================================================
# This function has a variable scope issue

def count_words_by_length(text):
    """Count words grouped by their length."""
    words = text.split()
    counts = {}
    
    for word in words:
        length = len(word)
        if length not in counts:
            count = 0  # BUG: Should be counts[length] = 0
        counts[length] = count + 1  # BUG: count is not updated correctly
    
    return counts

# Test it:
# print(count_words_by_length("the quick brown fox"))

# TODO: Ask Copilot to find and fix the scope bug


# =============================================================================
# EXERCISE 7: Floating Point Bug
# =============================================================================
# This function compares floating point numbers incorrectly

def are_equal(a, b):
    """Check if two floating point numbers are equal."""
    return a == b  # BUG: Direct comparison of floats

def calculate_total(prices, tax_rate):
    """Calculate total with tax."""
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # Verify our math
    expected = subtotal * (1 + tax_rate)
    if total != expected:  # BUG: Float comparison
        print("Warning: Calculation mismatch!")
    
    return total

# Test it:
# print(are_equal(0.1 + 0.2, 0.3))  # Expected True, but returns False!

# TODO: Ask Copilot how to properly compare floating point numbers


# =============================================================================
# EXERCISE 8: Async/Threading Bug (Conceptual)
# =============================================================================
# This class has a race condition

class Counter:
    """A simple counter class with a bug."""
    
    def __init__(self):
        self.count = 0
    
    def increment(self):
        """Increment the counter."""
        current = self.count  # BUG: Race condition in multi-threaded context
        self.count = current + 1
    
    def get_count(self):
        return self.count

# TODO: Ask Copilot how to make this thread-safe


# =============================================================================
# EXERCISE 9: Logic Bug in Validation
# =============================================================================
# This password validation has logical errors

def validate_password(password):
    """
    Validate password meets requirements:
    - At least 8 characters
    - Contains uppercase
    - Contains lowercase
    - Contains digit
    """
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit  # Is this complete?

# TODO: Ask Copilot to review this validation logic


# =============================================================================
# EXERCISE 10: Memory Bug (Conceptual)
# =============================================================================
# This recursive function may cause issues

def flatten_nested(nested_list, result=[]):  # BUG: Mutable default argument!
    """Flatten a nested list."""
    for item in nested_list:
        if isinstance(item, list):
            flatten_nested(item, result)
        else:
            result.append(item)
    return result

# Test it multiple times:
# print(flatten_nested([1, [2, 3]]))  # [1, 2, 3]
# print(flatten_nested([4, [5, 6]]))  # Expected [4, 5, 6], but gets more!

# TODO: Ask Copilot about the mutable default argument bug


# =============================================================================
# EXERCISE 11: Find All Bugs Challenge
# =============================================================================
# This function has multiple bugs - find them all!

def process_user_data(users):
    """Process user data and return summary."""
    result = {
        "total": len(users),
        "active": 0,
        "inactive": 0,
        "average_age": 0,
        "emails": []
    }
    
    ages = []
    
    for user in users:
        # Count active/inactive
        if user["status"] == "active":
            result["active"] =+ 1  # BUG 1: =+ instead of +=
        else:
            result["inactive"] += 1
        
        # Collect ages
        if user["age"]:  # BUG 2: What if age is 0?
            ages.append(user["age"])
        
        # Collect emails (avoiding duplicates)
        if user["email"] not in result["emails"]:
            result["emails"].append(user["emails"])  # BUG 3: Wrong key
    
    # Calculate average age
    result["average_age"] = sum(ages) / len(ages)  # BUG 4: Division by zero
    
    return result

# TODO: Ask Copilot to find ALL bugs in this function


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
✅ Use /fix command in Copilot Chat for quick fixes
✅ Ask Copilot to explain WHY something is a bug
✅ Request best practices to prevent similar bugs
✅ Copilot can identify common bug patterns
✅ Always test the suggested fixes!

COMMON BUG PATTERNS COPILOT CATCHES:
- Off-by-one errors
- Null/None reference issues
- Type mismatches
- Floating point comparison
- Mutable default arguments
- Race conditions
- Logic errors

USEFUL PROMPTS:
- "/fix"
- "Find all bugs in this code"
- "Why isn't this working as expected?"
- "What edge cases am I missing?"
- "How can I prevent this type of bug?"

NEXT: Move on to 09-security-vulnerability-detection.py to learn
      how to finding security vulnerabilities!
"""
