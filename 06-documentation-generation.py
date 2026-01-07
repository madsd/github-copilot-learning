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
# Each function has a blank line after 'def' where you should type """

def calculate_discount(price, discount_percent, max_discount=None):
    ""
    # 👆 Place cursor on the blank line ABOVE this comment, type """ and Enter
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    
    if max_discount is not None and discount_amount > max_discount:
        discount_amount = max_discount
    
    return price - discount_amount


def merge_sorted_lists(list1, list2):
    # 👆 Place cursor on blank line above, type """ and Enter
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

# Google Style - type """ on the blank line below def
def fetch_user_data(user_id, include_metadata=False):
    # 👆 Type """ above, then start with "Fetches user data from..."
    pass


# NumPy Style - type """ then write "Parameters" and Copilot continues
def calculate_statistics(data):
    # 👆 Type """ above, then type "Calculate" and let Copilot continue
    pass


# Sphinx/reStructuredText Style
def process_transaction(amount, currency, description=None):
    # 👆 Type """ above, then type ":param amount:" and Copilot continues
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
# Type """ on the blank line after each def, then describe the API endpoint

def create_user(username, email, password, role="user"):
    # 👆 Type """ above, then start: "Create a new user account..."
    pass


def update_user_profile(user_id, updates):
    # 👆 Type """ above
    pass


def delete_user(user_id, soft_delete=True):
    # 👆 Type """ above
    pass


# =============================================================================
# EXERCISE 5: Complex Function Documentation
# =============================================================================
# Functions with many parameters benefit most from Copilot docs

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
    # 👆 Type """ on the blank line above this comment
    # Copilot will generate comprehensive docs for all parameters
    pass


# =============================================================================
# EXERCISE 6: Type Hints + Documentation
# =============================================================================
# Type hints help Copilot generate better docstrings

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
    # 👆 Type """ on the blank line above this comment
    # Type hints help Copilot understand types and generate better docs
    pass


# =============================================================================
# EXERCISE 7: Using Copilot Chat for Documentation
# =============================================================================
# Sometimes Chat is easier than inline docstrings

# TRY THESE COPILOT CHAT COMMANDS:
#
# 1. Select any function above, press Ctrl+I, type: /doc
#
# 2. Select the TaskManager class, press Ctrl+I, type:
#    "Add Google-style docstrings to all methods"
#
# 3. Select multiple functions, press Ctrl+I, type:
#    "Add NumPy-style docstrings"
#
# 4. Open Chat panel (Ctrl+Alt+I), type:
#    "Generate README documentation for this file"


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
TWO WAYS TO GENERATE DOCSTRINGS:

1. INLINE METHOD:
   - Go to blank line after 'def function_name():'
   - Type \"\"\" and press Enter
   - Copilot suggests the docstring
   - Press Tab to accept

2. COPILOT CHAT METHOD (often easier):
   - Select the function or class
   - Press Ctrl+I (inline) or Ctrl+Alt+I (panel)
   - Type: /doc
   - Copilot adds docstrings

DOCSTRING STYLES:
- Google Style: Args, Returns, Raises sections
- NumPy Style: Parameters, Returns, Examples
- Sphinx: :param:, :returns:, :raises:

TIP: Start typing the style you want after \"\"\" and Copilot will follow it!

NEXT: Move on to 07-code-refactoring.js to learn
      how to improve code quality with Copilot!
"""
