/**
 * Scenario 07: Code Refactoring
 * ==============================
 * Improve code quality with GitHub Copilot.
 *
 * INSTRUCTIONS:
 * 1. Select the code you want to refactor
 * 2. Use inline chat (Ctrl+I) or Copilot Chat
 * 3. Ask for specific refactoring suggestions
 *
 * WHAT YOU'LL LEARN:
 * - Simplifying complex code
 * - Extracting functions
 * - Improving naming
 * - Applying design patterns
 * - Performance optimization
 */

// =============================================================================
// EXERCISE 1: Simplify Nested Conditionals
// =============================================================================
// This function has too many nested if statements
// Select it and ask Copilot to simplify

function getUserAccessLevel(user) {
    if (user) {
        if (user.isActive) {
            if (user.isAdmin) {
                if (user.isSuperAdmin) {
                    return 'super_admin';
                } else {
                    return 'admin';
                }
            } else {
                if (user.isPremium) {
                    return 'premium';
                } else {
                    return 'basic';
                }
            }
        } else {
            return 'inactive';
        }
    } else {
        return 'guest';
    }
}

// TODO: Select the function and ask Copilot:
// "Refactor this to use early returns and reduce nesting"


// =============================================================================
// EXERCISE 2: Extract Repeated Code
// =============================================================================
// This code has duplicated validation logic

function processUserRegistration(userData) {
    // Validate email
    if (!userData.email) {
        console.error('Email is required');
        return { success: false, error: 'Email is required' };
    }
    if (!userData.email.includes('@')) {
        console.error('Invalid email format');
        return { success: false, error: 'Invalid email format' };
    }
    
    // Validate password
    if (!userData.password) {
        console.error('Password is required');
        return { success: false, error: 'Password is required' };
    }
    if (userData.password.length < 8) {
        console.error('Password must be at least 8 characters');
        return { success: false, error: 'Password must be at least 8 characters' };
    }
    
    // Validate username
    if (!userData.username) {
        console.error('Username is required');
        return { success: false, error: 'Username is required' };
    }
    if (userData.username.length < 3) {
        console.error('Username must be at least 3 characters');
        return { success: false, error: 'Username must be at least 3 characters' };
    }
    
    // Process registration...
    return { success: true };
}

// TODO: Ask Copilot to:
// "Extract validation logic into reusable functions"
// "Use a validation schema pattern"


// =============================================================================
// EXERCISE 3: Improve Variable and Function Names
// =============================================================================
// This code has poor naming - ask Copilot to improve it

function calc(a, b, c) {
    let x = a * b;
    let y = x * (1 - c);
    let z = y + (y * 0.1);
    return z;
}

function proc(d) {
    let r = [];
    for (let i = 0; i < d.length; i++) {
        if (d[i].s === 'a') {
            r.push(d[i]);
        }
    }
    return r;
}

// TODO: Select these functions and ask Copilot:
// "Rename variables and functions to be more descriptive"


// =============================================================================
// EXERCISE 4: Convert Callbacks to Promises/Async
// =============================================================================
// Refactor callback hell to modern async/await

function getUserData(userId, callback) {
    fetchUser(userId, function(err, user) {
        if (err) {
            callback(err, null);
        } else {
            fetchUserPosts(user.id, function(err, posts) {
                if (err) {
                    callback(err, null);
                } else {
                    fetchUserComments(user.id, function(err, comments) {
                        if (err) {
                            callback(err, null);
                        } else {
                            callback(null, {
                                user: user,
                                posts: posts,
                                comments: comments
                            });
                        }
                    });
                }
            });
        }
    });
}

// Mock functions for the example
function fetchUser(id, cb) { cb(null, { id }); }
function fetchUserPosts(id, cb) { cb(null, []); }
function fetchUserComments(id, cb) { cb(null, []); }

// TODO: Ask Copilot to:
// "Convert this to async/await"
// "Use Promise.all where appropriate"


// =============================================================================
// EXERCISE 5: Replace Magic Numbers with Constants
// =============================================================================
// This code has magic numbers scattered throughout

function calculateShipping(weight, distance, isExpress) {
    let cost = 5.99; // Base cost
    
    if (weight > 2) {
        cost += (weight - 2) * 0.5;
    }
    
    if (distance > 100) {
        cost += ((distance - 100) / 50) * 2.5;
    }
    
    if (isExpress) {
        cost *= 1.75;
    }
    
    if (cost > 50) {
        cost = 50;
    }
    
    return Math.round(cost * 100) / 100;
}

// TODO: Ask Copilot to:
// "Extract magic numbers into named constants"
// "Add documentation explaining the calculations"


// =============================================================================
// EXERCISE 6: Apply Design Patterns
// =============================================================================
// This code could benefit from a pattern

const notificationHandlers = [];

function sendNotification(type, message, recipient) {
    if (type === 'email') {
        console.log(`Sending email to ${recipient}: ${message}`);
        // Email sending logic
    } else if (type === 'sms') {
        console.log(`Sending SMS to ${recipient}: ${message}`);
        // SMS sending logic
    } else if (type === 'push') {
        console.log(`Sending push notification to ${recipient}: ${message}`);
        // Push notification logic
    } else if (type === 'slack') {
        console.log(`Sending Slack message to ${recipient}: ${message}`);
        // Slack notification logic
    }
}

// TODO: Ask Copilot to:
// "Refactor this using the Strategy pattern"
// "Make it easy to add new notification types"


// =============================================================================
// EXERCISE 7: Optimize Performance
// =============================================================================
// This code has performance issues

function findDuplicates(array) {
    const duplicates = [];
    for (let i = 0; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] === array[j] && !duplicates.includes(array[i])) {
                duplicates.push(array[i]);
            }
        }
    }
    return duplicates;
}

function findCommonElements(arr1, arr2) {
    const common = [];
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j] && !common.includes(arr1[i])) {
                common.push(arr1[i]);
            }
        }
    }
    return common;
}

// TODO: Ask Copilot to:
// "Optimize these functions for better time complexity"
// "Use Set or Map for better performance"


// =============================================================================
// EXERCISE 8: Modernize Legacy Code
// =============================================================================
// Convert older JavaScript patterns to modern ES6+

var UserManager = (function() {
    var users = [];
    
    function addUser(name, email) {
        var user = {
            id: users.length + 1,
            name: name,
            email: email,
            createdAt: new Date()
        };
        users.push(user);
        return user;
    }
    
    function findUser(id) {
        for (var i = 0; i < users.length; i++) {
            if (users[i].id === id) {
                return users[i];
            }
        }
        return null;
    }
    
    function getAllUsers() {
        return users.slice();
    }
    
    return {
        addUser: addUser,
        findUser: findUser,
        getAllUsers: getAllUsers
    };
})();

// TODO: Ask Copilot to:
// "Convert this to a modern ES6 class"
// "Use const, let, arrow functions, and array methods"


// =============================================================================
// KEY TAKEAWAYS
// =============================================================================
/**
 * ✅ Select code and use Ctrl+I for inline refactoring
 * ✅ Be specific about what refactoring you want
 * ✅ Ask for explanations of why changes improve the code
 * ✅ Request design patterns by name
 * ✅ Ask about performance implications
 *
 * REFACTORING PROMPTS:
 * - "Simplify this code"
 * - "Extract this into smaller functions"
 * - "Apply the [pattern name] pattern"
 * - "Optimize for performance"
 * - "Convert to modern JavaScript/TypeScript"
 * - "Make this more testable"
 * - "Remove code duplication"
 *
 * NEXT: Move on to 08-bug-fixing.py to learn
 *       how to identify and fix bugs with Copilot!
 */
