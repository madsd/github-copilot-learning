"""
Test Calculator Module
======================
Unit tests for the Calculator class.

EXERCISE: Let Copilot help you complete and extend these tests.

INSTRUCTIONS:
1. Place your cursor after each TODO comment
2. Let Copilot generate the test code
3. Try asking for additional edge case tests in Copilot Chat
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
# Let Copilot generate test implementations

class TestBasicOperations:
    """Tests for basic arithmetic operations."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_add_mixed_numbers(self, calc):
        """Test adding positive and negative numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting two positive numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying two positive numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_multiply_by_zero(self, calc):
        """Test multiplying by zero."""
        # TODO: Let Copilot generate this test
        pass

    def test_divide_positive_numbers(self, calc):
        """Test dividing two positive numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_divide_by_zero_raises_error(self, calc):
        """Test that dividing by zero raises ValueError."""
        # TODO: Let Copilot generate this test
        pass


# =============================================================================
# EXERCISE 2: Edge Case Tests
# =============================================================================
# Ask Copilot Chat: "Generate edge case tests for the Calculator class"

class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # TODO: Let Copilot generate this test
        pass

    def test_power_zero_exponent(self, calc):
        """Test raising to power of zero."""
        # TODO: Let Copilot generate this test
        pass

    def test_power_negative_exponent(self, calc):
        """Test raising to negative power."""
        # TODO: Let Copilot generate this test
        pass

    def test_sqrt_zero(self, calc):
        """Test square root of zero."""
        # TODO: Let Copilot generate this test
        pass

    def test_sqrt_negative_raises_error(self, calc):
        """Test that square root of negative raises ValueError."""
        # TODO: Let Copilot generate this test
        pass


# =============================================================================
# EXERCISE 3: Memory Function Tests
# =============================================================================

class TestMemoryFunctions:
    """Tests for memory operations."""

    def test_initial_memory_is_zero(self, calc):
        """Test that memory starts at zero."""
        # TODO: Let Copilot generate this test
        pass

    def test_store_and_recall_memory(self, calc):
        """Test storing and recalling a value."""
        # TODO: Let Copilot generate this test
        pass

    def test_add_to_memory(self, calc):
        """Test adding to memory."""
        # TODO: Let Copilot generate this test
        pass

    def test_clear_memory(self, calc):
        """Test clearing memory."""
        # TODO: Let Copilot generate this test
        pass


# =============================================================================
# EXERCISE 4: History Tests
# =============================================================================

class TestHistory:
    """Tests for calculation history."""

    def test_history_starts_empty(self, calc):
        """Test that history starts empty."""
        # TODO: Let Copilot generate this test
        pass

    def test_operations_added_to_history(self, calc):
        """Test that operations are recorded in history."""
        # TODO: Let Copilot generate this test
        pass

    def test_clear_history(self, calc):
        """Test clearing history."""
        # TODO: Let Copilot generate this test
        pass


# =============================================================================
# EXERCISE 5: Standalone Function Tests
# =============================================================================

class TestStandaloneFunctions:
    """Tests for standalone utility functions."""

    # is_even tests
    def test_is_even_with_even_number(self):
        """Test is_even with an even number."""
        # TODO: Let Copilot generate this test
        pass

    def test_is_even_with_odd_number(self):
        """Test is_even with an odd number."""
        # TODO: Let Copilot generate this test
        pass

    def test_is_even_with_zero(self):
        """Test is_even with zero."""
        # TODO: Let Copilot generate this test
        pass

    # factorial tests
    def test_factorial_of_zero(self):
        """Test factorial of zero."""
        # TODO: Let Copilot generate this test
        pass

    def test_factorial_of_five(self):
        """Test factorial of 5."""
        # TODO: Let Copilot generate this test
        pass

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative raises ValueError."""
        # TODO: Let Copilot generate this test
        pass

    # fibonacci tests
    def test_fibonacci_of_zero(self):
        """Test fibonacci of zero."""
        # TODO: Let Copilot generate this test
        pass

    def test_fibonacci_of_ten(self):
        """Test fibonacci of 10."""
        # TODO: Let Copilot generate this test
        pass

    def test_fibonacci_negative_raises_error(self):
        """Test that fibonacci of negative raises ValueError."""
        # TODO: Let Copilot generate this test
        pass


# =============================================================================
# EXERCISE 6: Parametrized Tests
# =============================================================================
# Ask Copilot to generate parametrized tests for multiple inputs

class TestParametrized:
    """Parametrized tests for comprehensive coverage."""

    @pytest.mark.parametrize("a, b, expected", [
        # TODO: Let Copilot suggest test cases
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        """Test add with multiple inputs."""
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("n, expected", [
        # TODO: Let Copilot suggest test cases
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
