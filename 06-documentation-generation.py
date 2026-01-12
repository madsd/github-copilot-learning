"""
Scenario 06: Documentation Generation
======================================
Create docstrings and documentation with GitHub Copilot.

HOW TO GENERATE DOCSTRINGS:

Copilot Chat:
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
# Mark the individual functions below and use /doc to generate docstrings

def calculate_discount(price, discount_percent, max_discount=None):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    
    if max_discount is not None and discount_amount > max_discount:
        discount_amount = max_discount
    
    return price - discount_amount


def merge_sorted_lists(list1, list2):
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
# EXERCISE 3: Class Documentation (Use Copilot Chat)
# =============================================================================
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
    pass


def update_user_profile(user_id, updates):
    pass


def delete_user(user_id, soft_delete=True):
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
    
    pass


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""

Use /doc command (RECOMMENDED - more reliable!):
   - Select the entire function (from 'def' to 'pass')
   - Press Ctrl+I (inline chat)
   - Type: /doc
   - Press Enter and accept the changes

Inline typing can also be used, but is currently not reliable!

NEXT: Move on to 07-code-refactoring.js to learn
      how to improve code quality with Copilot!
"""
