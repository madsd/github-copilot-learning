# Scenario 05: Test Generation

This scenario demonstrates how to use GitHub Copilot to generate unit tests for existing code.

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `calculator.py` | Sample code to test - a Calculator class |
| `test_calculator.py` | Generated tests using Copilot |
| `string_utils.py` | Additional sample code for practice |
| `test_string_utils.py` | Practice file for you to complete |

## 🎯 Learning Objectives

- Generate test cases from existing code
- Use Copilot Chat's `/tests` command
- Write test descriptions that guide test generation
- Generate tests for edge cases

## 📝 Instructions

### Method 1: Using Copilot Chat `/tests` Command

1. Open `calculator.py`
2. Select the code you want to test
3. Open Copilot Chat (Ctrl+Alt+I)
4. Type `/tests` to generate tests

### Method 2: Comment-Driven Test Generation

1. Open `test_calculator.py`
2. Write a comment describing what to test
3. Let Copilot generate the test code

### Method 3: Inline Chat

1. Select code in `calculator.py`
2. Press Ctrl+I (or Cmd+I on Mac)
3. Type "write tests for this"

## 🏋️ Exercises

1. **Basic Tests**: Generate tests for the Calculator class
2. **Edge Cases**: Ask Copilot to generate tests for edge cases
3. **Error Handling**: Generate tests that verify exceptions are raised
4. **Practice**: Complete the tests in `test_string_utils.py`

## 💡 Tips

- Ask for specific types of tests: "unit tests", "integration tests", "edge case tests"
- Request specific frameworks: "using pytest", "using unittest"
- Ask for mocking: "mock the database connection"
- Request fixtures: "create pytest fixtures for setup"
