"""
Scenario 06: Documentation Generation
======================================
Create docstrings and documentation with GitHub Copilot.

HOW TO GENERATE DOCSTRINGS:

METHOD 1 - Inline Generation:
1. Place cursor on the BLANK LINE right after the function signature (def line)
2. Type three quotes: \"\"\"
3. Press Enter - Copilot will suggest the docstring content
4. Press Tab to accept

METHOD 2 - Copilot Chat:
1. Select the entire function
2. Press Ctrl+I (inline chat) or Ctrl+Alt+I (chat panel)
3. Type: /doc  OR  "add docstring"

WHAT YOU'LL LEARN:
- Generating docstrings in various formats
- Using /doc command in Copilot Chat
- Documenting classes and APIs
"""

# =============================================================================
# EXERCISE 1: Basic Docstrings
# =============================================================================
# On the blank line after each 'def', type """ and press Enter

def calculate_discount(price, discount_percent, max_discount=None):
    """👈 DELETE this line, type """ and press Enter - Copilot will generate!"""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    
    if max_discount is not None and discount_amount > max_discount:
        discount_amount = max_discount
    
    return price - discount_amount


def merge_sorted_lists(list1, list2):
    """👈 DELETE this line, type """ and press Enter"""
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


# =============================================================================
# EXERCISE 2: Different Docstring Formats
# =============================================================================
# Try generating docstrings in different styles

# Google Style - DELETE the placeholder docstring, type """ and Enter
def fetch_user_data(user_id, include_metadata=False):
    """👈 DELETE this, type """ then "Fetches user data" and Enter"""
    pass


# NumPy Style - try starting with "Calculate statistics..."
def calculate_statistics(data):
    """👈 DELETE this, type """ then "Calculate" and Enter"""
    pass


# Sphinx/reStructuredText Style - try starting with ":param"
def process_transaction(amount, currency, description=None):
    """👈 DELETE this, type """ then ":param amount:" and Enter"""
    pass


# =============================================================================
# EXERCISE 3: Class Documentation (Use Copilot Chat)
# =============================================================================
# For classes, using Copilot Chat is easier than inline docstrings
# 
# STEPS:
# 1. Select the ENTIRE class below (from 'class' to the last method)
# 2. Press Ctrl+I (inline chat)
# 3. Type: /doc  OR  "add docstrings to this class"

class TaskManager:
    def __init__(self, max_tasks=100):
        self.tasks = []
        self.max_tasks = max_tasks
        self.completed_count = 0

    def add_task(self, title, priority=1, due_date=None):
        if len(self.tasks) >= self.max_tasks:
            raise RuntimeError("Task limit reached")
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        return task["id"]

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.completed_count += 1
                return True
        return False

    def get_pending_tasks(self):
        return [t for t in self.tasks if not t["completed"]]

    def get_tasks_by_priority(self, priority):
        return [t for t in self.tasks if t["priority"] == priority]


# =============================================================================
# EXERCISE 4: API Documentation
# =============================================================================

def create_user(username, email, password, role="user"):
    """👈 DELETE this, type """ and Enter"""
    pass


def update_user_profile(user_id, updates):
    """👈 DELETE this, type """ and Enter"""
    pass


def delete_user(user_id, soft_delete=True):
    """👈 DELETE this, type """ and Enter"""
    pass


# =============================================================================
# EXERCISE 5: Complex Function Documentation
# =============================================================================

def analyze_text(
    text,
    language="en",
    include_sentiment=True,
    include_entities=True,
    include_keywords=True,
    max_keywords=10,
    entity_types=None,
    custom_dictionary=None
):
    """👈 DELETE this, type """ and Enter - Copilot will document all params!"""
    pass


# =============================================================================
# EXERCISE 6: Type Hints + Documentation
# =============================================================================

from typing import Optional, List, Dict, Union
from datetime import datetime

def search_products(
    query: str,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: str = "relevance",
    limit: int = 20,
    offset: int = 0
) -> Dict[str, Union[List[Dict], int, bool]]:
    """👈 DELETE this, type """ and Enter - type hints improve the docs!"""
    pass


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
TWO METHODS TO GENERATE DOCSTRINGS:

METHOD 1 - Type """ (inline):
   - Delete the placeholder docstring in any function above
   - Type \"\"\" and press Enter
   - Copilot should suggest docstring content
   - Press Tab to accept

METHOD 2 - Use /doc command (RECOMMENDED - more reliable!):
   - Select the entire function (from 'def' to 'pass')
   - Press Ctrl+I (inline chat)
   - Type: /doc
   - Press Enter and accept the changes

If inline typing isn't triggering suggestions, use Method 2!

NEXT: Move on to 07-code-refactoring.js to learn
      how to improve code quality with Copilot!
"""
