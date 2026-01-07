/**
 * Scenario 09: Regex Generation
 * ===============================
 * Create complex regular expressions with GitHub Copilot.
 *
 * INSTRUCTIONS:
 * 1. Read the comment describing what the regex should match
 * 2. Place cursor after the = "" and delete the ""
 * 3. Type / to start a regex and let Copilot complete the pattern
 * 4. Use Copilot Chat to explain complex patterns
 *
 * TIP: You can also use Copilot Chat: "Generate a regex to match X"
 *
 * WHAT YOU'LL LEARN:
 * - Generating regex from natural language
 * - Getting explanations for complex patterns
 * - Testing and validating regex patterns
 */

// =============================================================================
// EXERCISE 1: Basic Pattern Generation
// =============================================================================
// Delete "" and type "/" to let Copilot generate the regex

// Regex to match a valid email address
// 👇 Delete "" and type "/"
const emailPattern = "";

// Regex to match a US phone number (formats: 123-456-7890, (123) 456-7890, 1234567890)
// 👇 Delete "" and type "/"
const phonePattern = "";

// Regex to match a URL (http or https)
// 👇 Delete "" and type "/"
const urlPattern = "";


// =============================================================================
// EXERCISE 2: Date and Time Patterns
// =============================================================================

// Regex to match a date in format YYYY-MM-DD
const dateYMDPattern = "";

// Regex to match a date in format MM/DD/YYYY
const dateMDYPattern = "";

// Regex to match time in 24-hour format (HH:MM or HH:MM:SS)
const time24Pattern = "";

// Regex to match time in 12-hour format (e.g., 3:45 PM, 11:30 AM)
const time12Pattern = "";


// =============================================================================
// EXERCISE 3: Password Validation
// =============================================================================

// Regex to validate password with:
// - At least 8 characters
// - At least one uppercase letter
// - At least one lowercase letter
// - At least one digit
// - At least one special character (@$!%*?&)
const strongPasswordPattern = "";

// Test function
function validatePassword(password) {
    const regex = new RegExp(strongPasswordPattern);
    return regex.test(password);
}

// TODO: Test with these examples:
// console.log(validatePassword("Weak1!")); // false (too short)
// console.log(validatePassword("StrongPass1!")); // true


// =============================================================================
// EXERCISE 4: Credit Card Patterns
// =============================================================================

// Regex to match Visa card (starts with 4, 16 digits)
const visaPattern = "";

// Regex to match MasterCard (starts with 51-55 or 2221-2720, 16 digits)
const mastercardPattern = "";

// Regex to match American Express (starts with 34 or 37, 15 digits)
const amexPattern = "";

// Combined pattern for any major credit card
const creditCardPattern = "";


// =============================================================================
// EXERCISE 5: Text Extraction
// =============================================================================

// Regex to extract hashtags from text (e.g., #coding, #JavaScript)
const hashtagPattern = "";

// Regex to extract mentions from text (e.g., @username)
const mentionPattern = "";

// Regex to extract all numbers from text (including decimals)
const numberPattern = "";

// Function to extract all matches
function extractMatches(text, pattern) {
    const regex = new RegExp(pattern, 'g');
    return text.match(regex) || [];
}

// Test it:
// const tweet = "Learning #JavaScript with @CopilotChat! Score: 95.5 points #coding";
// console.log(extractMatches(tweet, hashtagPattern));
// console.log(extractMatches(tweet, mentionPattern));
// console.log(extractMatches(tweet, numberPattern));


// =============================================================================
// EXERCISE 6: IP Address and Network Patterns
// =============================================================================

// Regex to match IPv4 address (e.g., 192.168.1.1)
const ipv4Pattern = "";

// Regex to match IPv6 address
const ipv6Pattern = "";

// Regex to match MAC address (e.g., 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E)
const macAddressPattern = "";


// =============================================================================
// EXERCISE 7: HTML/Code Patterns
// =============================================================================

// Regex to match HTML tags (e.g., <div>, <p class="text">, </span>)
const htmlTagPattern = "";

// Regex to match HTML comments (<!-- comment -->)
const htmlCommentPattern = "";

// Regex to match JavaScript single-line comments (// comment)
const jsCommentPattern = "";

// Regex to match JavaScript multi-line comments (/* comment */)
const jsMultilineCommentPattern = "";


// =============================================================================
// EXERCISE 8: Text Replacement
// =============================================================================

// Function to censor profanity (replace with asterisks)
// Words to censor: "bad", "ugly", "awful"
function censorText(text) {
    // 👇 Delete "" and type "/" to let Copilot generate the pattern
    const pattern = "";
    return text.replace(new RegExp(pattern, 'gi'), match => '*'.repeat(match.length));
}

// Function to convert markdown bold to HTML (**text** to <strong>text</strong>)
function markdownBoldToHTML(text) {
    // 👇 Type "return text.replace(/" to let Copilot complete
    return text;
}

// Function to convert URLs in text to clickable links
function linkifyURLs(text) {
    // 👇 Type "return text.replace(/" to let Copilot complete
    return text;
}


// =============================================================================
// EXERCISE 9: Advanced Patterns
// =============================================================================

// Regex to match a valid JSON string (basic)
const jsonStringPattern = "";

// Regex to match camelCase words
const camelCasePattern = "";

// Regex to match PascalCase words
const pascalCasePattern = "";

// Regex to match snake_case words
const snakeCasePattern = "";

// Regex to validate a semantic version (e.g., 1.0.0, 2.3.4-beta.1)
const semverPattern = "";


// =============================================================================
// EXERCISE 10: Explain Complex Regex
// =============================================================================
// Ask Copilot Chat to explain these complex patterns

const mysteryPattern1 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
// TODO: Select this and ask Copilot Chat: "Explain this regex"

const mysteryPattern2 = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
// TODO: Ask Copilot: "What does this regex match? Give examples."

const mysteryPattern3 = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
// TODO: Ask Copilot: "What are the limitations of this email regex?"


// =============================================================================
// EXERCISE 11: Regex Utility Functions
// =============================================================================
// Type the function body to let Copilot help you build these utilities

/**
 * Escape special regex characters in a string
 * @param {string} string - The string to escape
 * @returns {string} - The escaped string
 */
function escapeRegex(string) {
    // 👇 Type "return string.replace" below

}

/**
 * Create a regex that matches any of the given words
 * @param {string[]} words - Array of words to match
 * @returns {RegExp} - The combined regex
 */
function matchAnyWord(words) {
    // 👇 Type "return new RegExp" below

}

/**
 * Test if a regex is valid
 * @param {string} pattern - The pattern to test
 * @returns {boolean} - Whether the pattern is valid
 */
function isValidRegex(pattern) {
    // 👇 Type "try" below

}


// =============================================================================
// KEY TAKEAWAYS
// =============================================================================
/**
 * ✅ Describe what you want to match in plain English
 * ✅ Ask Copilot to explain complex regex patterns
 * ✅ Test patterns with multiple examples
 * ✅ Request validation for edge cases
 * ✅ Use named groups for readability
 *
 * COPILOT CHAT PROMPTS:
 * - "Create a regex to match [description]"
 * - "Explain what this regex does"
 * - "What are the edge cases for this regex?"
 * - "Make this regex more strict/lenient"
 * - "Convert this regex to use named groups"
 *
 * REGEX TIPS:
 * - Use regex101.com to test patterns
 * - Consider edge cases (empty strings, special chars)
 * - Be specific about what should NOT match
 * - Document complex patterns with comments
 *
 * NEXT: Move on to 10-code-translation/ to learn
 *       how to convert code between languages!
 */
