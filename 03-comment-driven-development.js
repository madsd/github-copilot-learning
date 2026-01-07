/**
 * Scenario 03: Comment-Driven Development
 * =========================================
 * Generate code from natural language comments.
 *
 * INSTRUCTIONS:
 * 1. Write a descriptive comment explaining what you want
 * 2. Press Enter and wait for Copilot suggestions
 * 3. Accept with Tab or cycle through alternatives with Alt+]
 *
 * WHAT YOU'LL LEARN:
 * - How to write effective prompts in comments
 * - Generating functions from descriptions
 * - The importance of specific, clear comments
 */

// =============================================================================
// EXERCISE 1: Simple Function Generation
// =============================================================================

// Function that takes a string and returns it reversed
// TODO: Press Enter after this comment and let Copilot generate the function


// Function that checks if a number is prime
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 2: Specific Requirements
// =============================================================================
// The more specific your comment, the better the code

// Function that formats a phone number from "1234567890" to "(123) 456-7890"
// TODO: Let Copilot generate this function


// Function that converts Celsius to Fahrenheit using the formula F = C * 9/5 + 32
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 3: Working with Data Structures
// =============================================================================

// Function that takes an array of objects with 'name' and 'age' properties
// and returns only the objects where age is 18 or older
// TODO: Let Copilot generate this function


// Function that groups an array of objects by a specified property
// Example: groupBy([{type: 'a', val: 1}, {type: 'b', val: 2}, {type: 'a', val: 3}], 'type')
// Returns: { a: [{type: 'a', val: 1}, {type: 'a', val: 3}], b: [{type: 'b', val: 2}] }
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 4: DOM Manipulation (Browser)
// =============================================================================

// Function that creates a button element with text, class name, and click handler
// TODO: Let Copilot generate this function


// Function that toggles dark mode by adding/removing 'dark-mode' class on document body
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 5: API and Async Operations
// =============================================================================

// Async function that fetches user data from an API endpoint
// and returns the parsed JSON response
// Handles errors and returns null if the request fails
// TODO: Let Copilot generate this function


// Async function that fetches data with retry logic
// Retries up to 3 times with exponential backoff (1s, 2s, 4s delays)
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 6: Validation Functions
// =============================================================================

// Function that validates a password meets these requirements:
// - At least 8 characters
// - Contains at least one uppercase letter
// - Contains at least one lowercase letter
// - Contains at least one number
// - Contains at least one special character (!@#$%^&*)
// Returns an object with { isValid: boolean, errors: string[] }
// TODO: Let Copilot generate this function


// Function that validates a credit card number using the Luhn algorithm
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 7: Date and Time
// =============================================================================

// Function that takes a date and returns a human-readable relative time
// Examples: "just now", "5 minutes ago", "2 hours ago", "yesterday", "3 days ago"
// TODO: Let Copilot generate this function


// Function that calculates the number of business days between two dates
// (excludes weekends)
// TODO: Let Copilot generate this function


// =============================================================================
// EXERCISE 8: Class Generation
// =============================================================================

// Class representing a shopping cart with methods:
// - addItem(product, quantity)
// - removeItem(productId)
// - updateQuantity(productId, quantity)
// - getTotal()
// - clear()
// Each product has: id, name, price
// TODO: Let Copilot generate this class


// =============================================================================
// BONUS: Try Different Comment Styles
// =============================================================================

/*
 * Function that converts a number to its Roman numeral representation
 * Examples: 1 -> "I", 4 -> "IV", 9 -> "IX", 42 -> "XLII"
 */
// TODO: Let Copilot generate this function


/**
 * Debounce function that limits how often a callback can be called
 * @param {Function} callback - The function to debounce
 * @param {number} delay - The delay in milliseconds
 * @returns {Function} - The debounced function
 */
// TODO: Let Copilot generate this function


// =============================================================================
// KEY TAKEAWAYS
// =============================================================================
/**
 * ✅ Be specific and descriptive in your comments
 * ✅ Include input/output examples for complex logic
 * ✅ Mention data types when relevant
 * ✅ Describe edge cases and error handling requirements
 * ✅ Use JSDoc-style comments for better suggestions
 *
 * TIPS FOR BETTER RESULTS:
 * - Start with "Function that..." or "Class that..."
 * - Include examples: "Example: input -> output"
 * - Specify parameter types and return types
 * - Mention frameworks or libraries if applicable
 *
 * NEXT: Move on to 04-function-generation.ts to learn
 *       about TypeScript-specific code generation!
 */
