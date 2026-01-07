"""
Scenario 06: Documentation Generation
======================================
Create docstrings and documentation with GitHub Copilot.

INSTRUCTIONS:
1. Place cursor inside a function without documentation
2. Type triple quotes (''') or (\"\"\") and press Enter
3. Let Copilot generate the docstring
4. Or use Copilot Chat: /doc

WHAT YOU'LL LEARN:
- Generating docstrings in various formats
- Creating README content
- Documenting APIs and classes
- Using /doc command in Copilot Chat
"""

# =============================================================================
# EXERCISE 1: Basic Docstrings
# =============================================================================
# Place cursor after the function definition and type """ to trigger docstring

def calculate_discount(price, discount_percent, max_discount=None):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    
    if max_discount is not None and discount_amount > max_discount:
        discount_amount = max_discount
    
    return price - discount_amount

# TODO: Add a docstring to this function
# TIP: Place cursor on line after 'def' and type """


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

# TODO: Add a docstring explaining the algorithm


# =============================================================================
# EXERCISE 2: Different Docstring Formats
# =============================================================================
# Copilot can generate various docstring styles

# Google Style
def fetch_user_data(user_id, include_metadata=False):
    # TODO: Add a Google-style docstring
    # TIP: Type """ and start with "Fetches user data..."
    pass


# NumPy Style
def calculate_statistics(data):
    # TODO: Add a NumPy-style docstring
    # TIP: Include Parameters, Returns, and Examples sections
    pass


# Sphinx/reStructuredText Style
def process_transaction(amount, currency, description=None):
    # TODO: Add a Sphinx-style docstring with :param and :returns:
    pass


# =============================================================================
# EXERCISE 3: Class Documentation
# =============================================================================
# Document this class using Copilot

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

# TODO: Add class docstring and method docstrings
# TIP: Select the class and use /doc in Copilot Chat


# =============================================================================
# EXERCISE 4: API Documentation
# =============================================================================
# Document these API-style functions

def create_user(username, email, password, role="user"):
    # TODO: Document with API-style docstring including:
    # - Endpoint description
    # - Parameters with types
    # - Return value
    # - Possible errors
    # - Example usage
    pass


def update_user_profile(user_id, updates):
    # TODO: Document this API endpoint
    pass


def delete_user(user_id, soft_delete=True):
    # TODO: Document this API endpoint
    pass


# =============================================================================
# EXERCISE 5: Complex Function Documentation
# =============================================================================
# This function needs comprehensive documentation

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
    """
    👇 Delete this docstring, type triple quotes, and let Copilot generate:
    - Description
    - All parameters with types and defaults
    - Return value structure
    - Examples
    - Raises section
    """
    pass


# =============================================================================
# EXERCISE 6: Module-Level Documentation
# =============================================================================
# Create a module docstring for a hypothetical module

"""
TODO: Generate a module docstring that includes:
- Module name and purpose
- Main classes and functions
- Usage examples
- Dependencies
- Author information

TIP: Ask Copilot Chat: "Generate a module docstring for a data processing module"
"""


# =============================================================================
# EXERCISE 7: Generate README Content
# =============================================================================
# Ask Copilot Chat to generate README content for this code

# TIP: Select all the code and ask:
# "Generate README.md content for this module including:
# - Overview
# - Installation
# - Usage examples
# - API reference
# - Contributing guidelines"


# =============================================================================
# EXERCISE 8: Type Hints + Documentation
# =============================================================================
# Combine type hints with docstrings

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
    """
    👇 Delete this docstring, type triple quotes, and let Copilot generate
    The type hints will help it understand the structure
    """
    pass


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
✅ Type \"\"\" or ''' to trigger docstring generation
✅ Use /doc in Copilot Chat for quick documentation
✅ Copilot adapts to different docstring styles
✅ Type hints improve documentation quality
✅ Select code and ask Chat to document it

DOCSTRING STYLES:
- Google Style: Args, Returns, Raises sections
- NumPy Style: Parameters, Returns, Examples
- Sphinx: :param:, :returns:, :raises:

COPILOT CHAT PROMPTS:
- "/doc"
- "Add Google-style docstrings to this class"
- "Generate comprehensive API documentation"
- "Create a README for this module"

NEXT: Move on to 07-code-refactoring.js to learn
      how to improve code quality with Copilot!
"""
