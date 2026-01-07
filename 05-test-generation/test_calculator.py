"""
Test Calculator Module
======================
Unit tests for the Calculator class.

EXERCISE: Let Copilot help you complete and extend these tests.

INSTRUCTIONS:
1. Each test method has a 'pass' placeholder
2. Delete 'pass' and start typing (e.g., "result = " or "assert")
3. Copilot will use the docstring and method name to suggest the test
4. Or use Ctrl+I (Inline Chat) on the method to ask "implement this test"

TIP: The docstring above each method tells Copilot what to generate!
"""

import pytest
from calculator import Calculator, is_even, factorial, fibonacci


# =============================================================================
# FIXTURE: Create a calculator instance for each test
# =============================================================================

@pytest.fixture
def calc():
    """Create a fresh Calculator instance for each test."""
    return Calculator()


# =============================================================================
# EXERCISE 1: Basic Operation Tests
# =============================================================================
# Delete 'pass' and type "result" or "assert" to trigger Copilot

class TestBasicOperations:
    """Tests for basic arithmetic operations."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # 👇 Delete 'pass', type "result = " or "assert calc.add"
        pass

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_add_mixed_numbers(self, calc):
        """Test adding positive and negative numbers."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting two positive numbers."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying two positive numbers."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_multiply_by_zero(self, calc):
        """Test multiplying by zero."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_divide_positive_numbers(self, calc):
        """Test dividing two positive numbers."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_divide_by_zero_raises_error(self, calc):
        """Test that dividing by zero raises ValueError."""
        # 👇 Delete 'pass', type "with pytest.raises"
        pass


# =============================================================================
# EXERCISE 2: Edge Case Tests
# =============================================================================
# Delete 'pass' and type "assert" to let Copilot complete based on the docstring

class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_power_zero_exponent(self, calc):
        """Test raising to power of zero."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_power_negative_exponent(self, calc):
        """Test raising to negative power."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_sqrt_zero(self, calc):
        """Test square root of zero."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_sqrt_negative_raises_error(self, calc):
        """Test that square root of negative raises ValueError."""
        # 👇 Delete 'pass', type "with pytest.raises"
        pass


# =============================================================================
# EXERCISE 3: Memory Function Tests
# =============================================================================

class TestMemoryFunctions:
    """Tests for memory operations."""

    def test_initial_memory_is_zero(self, calc):
        """Test that memory starts at zero."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_store_and_recall_memory(self, calc):
        """Test storing and recalling a value."""
        # 👇 Delete 'pass', type "calc.memory_store"
        pass

    def test_add_to_memory(self, calc):
        """Test adding to memory."""
        # 👇 Delete 'pass', type "calc"
        pass

    def test_clear_memory(self, calc):
        """Test clearing memory."""
        # 👇 Delete 'pass', type "calc"
        pass


# =============================================================================
# EXERCISE 4: History Tests
# =============================================================================

class TestHistory:
    """Tests for calculation history."""

    def test_history_starts_empty(self, calc):
        """Test that history starts empty."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_operations_added_to_history(self, calc):
        """Test that operations are recorded in history."""
        # 👇 Delete 'pass', type "calc"
        pass

    def test_clear_history(self, calc):
        """Test clearing history."""
        # 👇 Delete 'pass', type "calc"
        pass


# =============================================================================
# EXERCISE 5: Standalone Function Tests
# =============================================================================

class TestStandaloneFunctions:
    """Tests for standalone utility functions."""

    # is_even tests
    def test_is_even_with_even_number(self):
        """Test is_even with an even number."""
        # 👇 Delete 'pass', type "assert is_even"
        pass

    def test_is_even_with_odd_number(self):
        """Test is_even with an odd number."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_is_even_with_zero(self):
        """Test is_even with zero."""
        # 👇 Delete 'pass', type "assert"
        pass

    # factorial tests
    def test_factorial_of_zero(self):
        """Test factorial of zero."""
        # 👇 Delete 'pass', type "assert factorial"
        pass

    def test_factorial_of_five(self):
        """Test factorial of 5."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative raises ValueError."""
        # 👇 Delete 'pass', type "with pytest.raises"
        pass

    # fibonacci tests
    def test_fibonacci_of_zero(self):
        """Test fibonacci of zero."""
        # 👇 Delete 'pass', type "assert fibonacci"
        pass

    def test_fibonacci_of_ten(self):
        """Test fibonacci of 10."""
        # 👇 Delete 'pass', type "assert"
        pass

    def test_fibonacci_negative_raises_error(self):
        """Test that fibonacci of negative raises ValueError."""
        # 👇 Delete 'pass', type "with pytest.raises"
        pass


# =============================================================================
# EXERCISE 6: Parametrized Tests
# =============================================================================
# Type test case tuples inside the list to let Copilot suggest more

class TestParametrized:
    """Parametrized tests for comprehensive coverage."""

    @pytest.mark.parametrize("a, b, expected", [
        # 👇 Type "(1, 2, 3)," and Copilot will suggest more test cases
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        """Test add with multiple inputs."""
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("n, expected", [
        # 👇 Type "(0, 1)," and Copilot will suggest more test cases
    ])
    def test_factorial_parametrized(self, n, expected):
        """Test factorial with multiple inputs."""
        assert factorial(n) == expected


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
✅ Use /tests in Copilot Chat to generate tests quickly
✅ Write descriptive test function names for better suggestions
✅ Ask Copilot for edge case and error handling tests
✅ Use pytest fixtures for test setup
✅ Parametrized tests provide comprehensive coverage

COPILOT CHAT PROMPTS TO TRY:
- "/tests for the Calculator class"
- "Generate edge case tests for divide method"
- "Add parametrized tests for all operations"
- "Generate tests that verify exception messages"
- "Create integration tests for the Calculator"
"""
