"""
Scenario 02: Code Explanation
==============================
Use GitHub Copilot to understand existing code.

INSTRUCTIONS:
1. Select the code you want to understand
2. Use one of these methods:
   - Right-click → Copilot → Explain This
   - Open Copilot Chat (Ctrl+Alt+I) and ask "/explain"
   - Use inline chat (Ctrl+I) and type "explain"

WHAT YOU'LL LEARN:
- How to get explanations for complex code
- Using Copilot Chat for understanding
- Breaking down algorithms step by step
"""

# =============================================================================
# EXERCISE 1: Explain a Simple Algorithm
# =============================================================================
# Select the function below and ask Copilot to explain it

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# TODO: Select the function above
# TODO: Press Ctrl+Alt+I to open Copilot Chat
# TODO: Type "/explain" or ask "What does this function do?"


# =============================================================================
# EXERCISE 2: Explain Complex Logic
# =============================================================================
# This code might look cryptic - ask Copilot to explain it

def mystery_function(n):
    return n & (n - 1) == 0 and n != 0

# TODO: Select the function and ask:
# - "What does this function check?"
# - "How does the bitwise operation work?"
# - "Give me examples of inputs and outputs"


# =============================================================================
# EXERCISE 3: Explain a Regular Expression
# =============================================================================
# Regular expressions can be hard to read - Copilot can help!

import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
    return bool(re.match(email_pattern, email))

# TODO: Select the email_pattern and ask:
# - "Explain this regex pattern"
# - "What emails would this match?"
# - "What are the limitations of this pattern?"


# =============================================================================
# EXERCISE 4: Explain Object-Oriented Code
# =============================================================================
# Understanding class hierarchies and design patterns

class Observer:
    def update(self, *args, **kwargs):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

# TODO: Select both classes and ask:
# - "What design pattern is this?"
# - "How would I use this in practice?"
# - "Can you give me an example implementation?"


# =============================================================================
# EXERCISE 5: Explain List Comprehensions
# =============================================================================
# Python one-liners can be powerful but confusing

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
evens_squared = [x**2 for x in range(20) if x % 2 == 0]
nested_dict = {k: {vk: vv * 2 for vk, vv in v.items()} for k, v in {'a': {'x': 1}, 'b': {'y': 2}}.items()}

# TODO: Select each line and ask Copilot to:
# - Explain what the comprehension does
# - Convert it to regular for loops
# - Describe when to use this pattern


# =============================================================================
# EXERCISE 6: Explain Decorator Pattern
# =============================================================================
# Decorators are a powerful but sometimes confusing Python feature

import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# TODO: Ask Copilot:
# - "How does this decorator work?"
# - "What is @functools.wraps for?"
# - "How can I add parameters to this decorator?"


# =============================================================================
# EXERCISE 7: Explain Async Code
# =============================================================================
# Asynchronous programming can be tricky to understand

import asyncio

async def fetch_data(url, delay):
    print(f"Starting fetch from {url}")
    await asyncio.sleep(delay)  # Simulates network request
    print(f"Completed fetch from {url}")
    return f"Data from {url}"

async def main():
    tasks = [
        fetch_data("api/users", 2),
        fetch_data("api/posts", 1),
        fetch_data("api/comments", 3)
    ]
    results = await asyncio.gather(*tasks)
    return results

# TODO: Ask Copilot:
# - "Explain how async/await works here"
# - "What is asyncio.gather doing?"
# - "In what order will the print statements appear?"


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
✅ Use /explain in Copilot Chat for detailed explanations
✅ Select specific code sections for targeted explanations
✅ Ask follow-up questions to dive deeper
✅ Request examples and alternative implementations
✅ Copilot can explain design patterns, algorithms, and language features

USEFUL PROMPTS:
- "Explain this code step by step"
- "What is the time complexity of this function?"
- "What are the edge cases I should consider?"
- "How can I improve this code?"

NEXT: Move on to 03-comment-driven-development.js to learn 
      how to generate code from natural language comments!
"""
