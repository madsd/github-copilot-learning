/**
 * Scenario 03: Comment-Driven Development
 * =========================================
 * Generate code from natural language comments.
 *
 * INSTRUCTIONS:
 * 1. Read the descriptive comment above each exercise
 * 2. On the blank line below, start typing: function or const
 * 3. Copilot will suggest code based on the comment context
 * 4. Press Tab to accept, or Alt+] to see alternatives
 *
 * KEY INSIGHT: Copilot reads the comments ABOVE your cursor to understand
 * what you want. The comment is the "prompt" - your typing triggers the suggestion.
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
// 👇 Type "function reverse" on the blank line and let Copilot complete it


// Function that checks if a number is prime
// 👇 Type "function isPrime" below


// =============================================================================
// EXERCISE 2: Specific Requirements
// =============================================================================
// The more specific your comment, the better the code

// Function that formats a phone number from "1234567890" to "(123) 456-7890"
// 👇 Type "function formatPhone" below


// Function that converts Celsius to Fahrenheit using the formula F = C * 9/5 + 32
// 👇 Type "function celsiusTo" below


// =============================================================================
// EXERCISE 3: Working with Data Structures
// =============================================================================

// Function that takes an array of objects with 'name' and 'age' properties
// and returns only the objects where age is 18 or older
// 👇 Type "function filterAdults" below


// Function that groups an array of objects by a specified property
// Example: groupBy([{type: 'a', val: 1}, {type: 'b', val: 2}, {type: 'a', val: 3}], 'type')
// Returns: { a: [{type: 'a', val: 1}, {type: 'a', val: 3}], b: [{type: 'b', val: 2}] }
// 👇 Type "function groupBy" below


// =============================================================================
// EXERCISE 4: DOM Manipulation (Browser)
// =============================================================================

// Function that creates a button element with text, class name, and click handler
// 👇 Type "function createButton" below


// Function that toggles dark mode by adding/removing 'dark-mode' class on document body
// 👇 Type "function toggleDark" below


// =============================================================================
// EXERCISE 5: API and Async Operations
// =============================================================================

// Async function that fetches user data from an API endpoint
// and returns the parsed JSON response
// Handles errors and returns null if the request fails
// 👇 Type "async function fetchUser" below


// Async function that fetches data with retry logic
// Retries up to 3 times with exponential backoff (1s, 2s, 4s delays)
// 👇 Type "async function fetchWithRetry" below


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
// 👇 Type "function validatePassword" below


// Function that validates a credit card number using the Luhn algorithm
// 👇 Type "function validateCard" below


// =============================================================================
// EXERCISE 7: Date and Time
// =============================================================================

// Function that takes a date and returns a human-readable relative time
// Examples: "just now", "5 minutes ago", "2 hours ago", "yesterday", "3 days ago"
// 👇 Type "function getRelativeTime" below


// Function that calculates the number of business days between two dates
// (excludes weekends)
// 👇 Type "function getBusinessDays" below


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
// 👇 Type "class ShoppingCart" below


// =============================================================================
// BONUS: Try Different Comment Styles
// =============================================================================

/*
 * Function that converts a number to its Roman numeral representation
 * Examples: 1 -> "I", 4 -> "IV", 9 -> "IX", 42 -> "XLII"
 */
// 👇 Type "function toRoman" below


/**
 * Debounce function that limits how often a callback can be called
 * @param {Function} callback - The function to debounce
 * @param {number} delay - The delay in milliseconds
 * @returns {Function} - The debounced function
 */
// 👇 Type "function debounce" below


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
