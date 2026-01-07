"""
Original Python Code
====================
This file contains Python code to translate to other languages.

EXERCISE:
1. Select functions from this file
2. Use Copilot Chat to translate to JavaScript, TypeScript, or C#
3. Complete the translation files in this folder
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import json


# =============================================================================
# DATA CLASSES (Translate to target language equivalents)
# =============================================================================

@dataclass
class User:
    """Represents a user in the system."""
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool = True
    role: str = "user"


@dataclass
class Product:
    """Represents a product in the store."""
    id: int
    name: str
    price: float
    category: str
    stock: int
    tags: List[str]


@dataclass
class Order:
    """Represents a customer order."""
    id: int
    user_id: int
    products: List[Tuple[int, int]]  # (product_id, quantity)
    total: float
    status: str
    created_at: datetime


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a number as currency."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price."""
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


def parse_date(date_string: str) -> Optional[datetime]:
    """Parse a date string in various formats."""
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y-%m-%dT%H:%M:%S",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None


# =============================================================================
# LIST/ARRAY OPERATIONS
# =============================================================================

def filter_active_users(users: List[User]) -> List[User]:
    """Filter to only active users."""
    return [user for user in users if user.is_active]


def group_by_category(products: List[Product]) -> Dict[str, List[Product]]:
    """Group products by their category."""
    result: Dict[str, List[Product]] = {}
    for product in products:
        if product.category not in result:
            result[product.category] = []
        result[product.category].append(product)
    return result


def find_top_products(products: List[Product], n: int = 5) -> List[Product]:
    """Find the top n products by price."""
    sorted_products = sorted(products, key=lambda p: p.price, reverse=True)
    return sorted_products[:n]


def search_products(
    products: List[Product],
    query: str,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> List[Product]:
    """Search products with multiple filters."""
    results = products
    
    # Filter by search query
    if query:
        query_lower = query.lower()
        results = [
            p for p in results
            if query_lower in p.name.lower() or 
               any(query_lower in tag.lower() for tag in p.tags)
        ]
    
    # Filter by category
    if category:
        results = [p for p in results if p.category == category]
    
    # Filter by price range
    if min_price is not None:
        results = [p for p in results if p.price >= min_price]
    if max_price is not None:
        results = [p for p in results if p.price <= max_price]
    
    return results


# =============================================================================
# BUSINESS LOGIC
# =============================================================================

class ShoppingCart:
    """Shopping cart with product management."""
    
    def __init__(self):
        self.items: Dict[int, int] = {}  # product_id -> quantity
        self.products: Dict[int, Product] = {}
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if product.id in self.items:
            self.items[product.id] += quantity
        else:
            self.items[product.id] = quantity
            self.products[product.id] = product
    
    def remove_item(self, product_id: int) -> bool:
        """Remove a product from the cart."""
        if product_id in self.items:
            del self.items[product_id]
            del self.products[product_id]
            return True
        return False
    
    def update_quantity(self, product_id: int, quantity: int) -> bool:
        """Update the quantity of a product."""
        if product_id not in self.items:
            return False
        
        if quantity <= 0:
            return self.remove_item(product_id)
        
        self.items[product_id] = quantity
        return True
    
    def get_subtotal(self) -> float:
        """Calculate the subtotal."""
        return sum(
            self.products[pid].price * qty
            for pid, qty in self.items.items()
        )
    
    def get_total(self, tax_rate: float = 0.0, discount: float = 0.0) -> float:
        """Calculate the total with tax and discount."""
        subtotal = self.get_subtotal()
        after_discount = subtotal * (1 - discount / 100)
        with_tax = after_discount * (1 + tax_rate / 100)
        return round(with_tax, 2)
    
    def to_dict(self) -> Dict:
        """Convert cart to dictionary for serialization."""
        return {
            "items": [
                {
                    "product_id": pid,
                    "name": self.products[pid].name,
                    "price": self.products[pid].price,
                    "quantity": qty,
                    "line_total": self.products[pid].price * qty
                }
                for pid, qty in self.items.items()
            ],
            "subtotal": self.get_subtotal(),
            "item_count": sum(self.items.values())
        }


# =============================================================================
# ASYNC-STYLE OPERATIONS (Translate to proper async in target language)
# =============================================================================

def fetch_user_orders(user_id: int, orders: List[Order]) -> List[Order]:
    """Simulate fetching orders for a user."""
    return [order for order in orders if order.user_id == user_id]


def calculate_user_statistics(user_id: int, orders: List[Order]) -> Dict:
    """Calculate statistics for a user's orders."""
    user_orders = fetch_user_orders(user_id, orders)
    
    if not user_orders:
        return {
            "total_orders": 0,
            "total_spent": 0,
            "average_order": 0,
        }
    
    total_spent = sum(order.total for order in user_orders)
    
    return {
        "total_orders": len(user_orders),
        "total_spent": total_spent,
        "average_order": total_spent / len(user_orders),
        "first_order": min(user_orders, key=lambda o: o.created_at).created_at,
        "last_order": max(user_orders, key=lambda o: o.created_at).created_at,
    }


# =============================================================================
# JSON SERIALIZATION
# =============================================================================

def user_to_json(user: User) -> str:
    """Serialize a user to JSON."""
    return json.dumps({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at.isoformat(),
        "is_active": user.is_active,
        "role": user.role,
    })


def user_from_json(json_string: str) -> User:
    """Deserialize a user from JSON."""
    data = json.loads(json_string)
    return User(
        id=data["id"],
        username=data["username"],
        email=data["email"],
        created_at=datetime.fromisoformat(data["created_at"]),
        is_active=data.get("is_active", True),
        role=data.get("role", "user"),
    )


# =============================================================================
# EXERCISE: TRANSLATE ALL OF THE ABOVE
# =============================================================================
"""
Use Copilot to translate this code to:

1. JavaScript (translated_javascript.js)
   - Use ES6+ features
   - Use classes for dataclasses
   - Handle async operations with Promises

2. TypeScript (translated_typescript.ts)
   - Add proper type annotations
   - Use interfaces for data structures
   - Leverage TypeScript features

3. C# (translated_csharp.cs)
   - Use C# classes and records
   - Use LINQ for list operations
   - Follow C# naming conventions

TIPS:
- Ask Copilot to explain language-specific differences
- Request idiomatic code for each target language
- Ask about equivalent libraries/methods
"""
