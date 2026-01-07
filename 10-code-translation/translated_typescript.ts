/**
 * Translated TypeScript Code
 * ===========================
 * Complete this translation using Copilot.
 *
 * EXERCISE:
 * 1. Open original_python.py
 * 2. Select sections of code
 * 3. Use Copilot Chat: "Convert this to TypeScript with proper types"
 * 4. Paste the translations here
 */

// =============================================================================
// INTERFACES (TypeScript equivalent of Python dataclasses)
// =============================================================================

// TODO: Define User interface


// TODO: Define Product interface


// TODO: Define Order interface


// =============================================================================
// TYPE ALIASES
// =============================================================================

// TODO: Define CurrencyCode type (union type for USD, EUR, GBP, JPY)


// TODO: Define OrderStatus type


// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

// TODO: Translate formatCurrency with proper types


// TODO: Translate calculateDiscount with proper types


// TODO: Translate parseDate with proper types


// =============================================================================
// LIST/ARRAY OPERATIONS
// =============================================================================

// TODO: Translate filterActiveUsers with proper types


// TODO: Translate groupByCategory with proper types


// TODO: Translate findTopProducts with proper types


// TODO: Translate searchProducts with proper types


// =============================================================================
// BUSINESS LOGIC
// =============================================================================

// TODO: Translate ShoppingCart class with proper types


// =============================================================================
// GENERIC FUNCTIONS
// =============================================================================

// TODO: Create generic groupBy function


// TODO: Create generic filter function with type predicates


// =============================================================================
// KEY DIFFERENCES FROM PYTHON
// =============================================================================
/**
 * Notes on translating Python to TypeScript:
 * 
 * 1. Use interfaces instead of dataclasses
 * 2. Optional properties use '?' (property?: type)
 * 3. Use union types for restricted values
 * 4. Generic types use <T> syntax
 * 5. Use 'unknown' for truly unknown types, not 'any'
 * 6. Dict[K, V] becomes Record<K, V> or Map<K, V>
 * 7. List[T] becomes T[] or Array<T>
 * 8. Tuple[A, B] becomes [A, B]
 * 9. Optional[T] becomes T | undefined or T | null
 */

export {};
