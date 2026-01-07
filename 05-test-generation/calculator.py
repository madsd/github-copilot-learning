"""
Calculator Module
=================
A simple calculator class for demonstrating test generation.

EXERCISE: Use Copilot to generate tests for this class.

Methods to test:
1. Select a method and use /tests in Copilot Chat
2. Ask for edge case tests
3. Ask for error handling tests
"""


class Calculator:
    """A basic calculator with memory functionality."""

    def __init__(self):
        """Initialize calculator with memory set to 0."""
        self.memory = 0
        self.history = []

    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result."""
        result = a + b
        self._add_to_history("add", a, b, result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        result = a - b
        self._add_to_history("subtract", a, b, result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and return the result."""
        result = a * b
        self._add_to_history("multiply", a, b, result)
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history("divide", a, b, result)
        return result

    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent."""
        result = base ** exponent
        self._add_to_history("power", base, exponent, result)
        return result

    def sqrt(self, n: float) -> float:
        """
        Calculate the square root of n.
        
        Raises:
            ValueError: If n is negative.
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = n ** 0.5
        self._add_to_history("sqrt", n, None, result)
        return result

    def store_in_memory(self, value: float) -> None:
        """Store a value in memory."""
        self.memory = value

    def recall_memory(self) -> float:
        """Recall the value stored in memory."""
        return self.memory

    def clear_memory(self) -> None:
        """Clear the memory (set to 0)."""
        self.memory = 0

    def add_to_memory(self, value: float) -> None:
        """Add a value to the current memory."""
        self.memory += value

    def get_history(self) -> list:
        """Return the calculation history."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history = []

    def _add_to_history(self, operation: str, a: float, b: float | None, result: float) -> None:
        """Add an operation to the history."""
        self.history.append({
            "operation": operation,
            "operands": (a, b) if b is not None else (a,),
            "result": result
        })


# Additional functions to test

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calculate the factorial of n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
