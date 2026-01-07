/**
 * Scenario 04: Function Generation with TypeScript
 * ==================================================
 * Create complete functions from signatures and types.
 *
 * INSTRUCTIONS:
 * 1. The function signatures are already defined with TypeScript types
 * 2. Place your cursor on the line after the TODO comment
 * 3. Start typing (e.g., "return" or "const") to trigger Copilot
 * 4. Press Tab to accept the suggestion
 *
 * TIP: You can also select the entire function and use Ctrl+I (Inline Chat)
 * to ask Copilot to "implement this function"
 *
 * WHAT YOU'LL LEARN:
 * - How TypeScript types improve Copilot suggestions
 * - Generating implementations from interfaces
 * - Using generics with Copilot
 */

// =============================================================================
// EXERCISE 1: Basic Function Signatures
// =============================================================================
// Define the signature, let Copilot fill in the body

function capitalize(str: string): string {
    // 👇 Type "return" below and let Copilot complete

}

function sum(numbers: number[]): number {
    // 👇 Type "return" below and let Copilot complete

}

function findMax(numbers: number[]): number | undefined {
    // 👇 Type "if" or "return" below and let Copilot complete

}


// =============================================================================
// EXERCISE 2: Working with Interfaces
// =============================================================================
// Types give Copilot context about data structures

interface User {
    id: string;
    name: string;
    email: string;
    age: number;
    isActive: boolean;
}

interface CreateUserInput {
    name: string;
    email: string;
    age: number;
}

function createUser(input: CreateUserInput): User {
    // 👇 Type "return" below - Copilot knows the User interface!

}

function filterActiveUsers(users: User[]): User[] {
    // 👇 Type "return" below

}

function findUserByEmail(users: User[], email: string): User | undefined {
    // 👇 Type "return" below

}

function sortUsersByAge(users: User[], ascending: boolean = true): User[] {
    // 👇 Type "return" below

}


// =============================================================================
// EXERCISE 3: Generic Functions
// =============================================================================
// Copilot understands generics and type constraints

function first<T>(array: T[]): T | undefined {
    // 👇 Type "return" below

}

function last<T>(array: T[]): T | undefined {
    // 👇 Type "return" below

}

function unique<T>(array: T[]): T[] {
    // 👇 Type "return" below

}

function groupBy<T, K extends keyof T>(array: T[], key: K): Record<string, T[]> {
    // 👇 Type "const result" or "return" below

}

function pluck<T, K extends keyof T>(array: T[], key: K): T[K][] {
    // 👇 Type "return" below

}


// =============================================================================
// EXERCISE 4: Complex Types and Utility Types
// =============================================================================

interface Product {
    id: string;
    name: string;
    price: number;
    category: string;
    inStock: boolean;
    tags: string[];
}

type ProductUpdate = Partial<Omit<Product, 'id'>>;

function updateProduct(product: Product, updates: ProductUpdate): Product {
    // 👇 Type "return" below

}

function filterProducts(
    products: Product[],
    filters: {
        category?: string;
        minPrice?: number;
        maxPrice?: number;
        inStock?: boolean;
    }
): Product[] {
    // 👇 Type "return products.filter" below

}


// =============================================================================
// EXERCISE 5: Async Functions with Types
// =============================================================================

interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}

interface PaginatedResponse<T> {
    items: T[];
    total: number;
    page: number;
    pageSize: number;
    hasMore: boolean;
}

async function fetchUser(id: string): Promise<ApiResponse<User>> {
    // 👇 Type "return" below for a mock implementation

}

async function fetchPaginatedUsers(
    page: number,
    pageSize: number
): Promise<PaginatedResponse<User>> {
    // 👇 Type "return" below

}


// =============================================================================
// EXERCISE 6: Class with Full Type Definitions
// =============================================================================

interface CacheOptions {
    maxSize: number;
    ttlMs: number;
}

interface CacheEntry<T> {
    value: T;
    expiresAt: number;
}

class Cache<T> {
    private cache: Map<string, CacheEntry<T>>;
    private options: CacheOptions;

    constructor(options: CacheOptions) {
        // 👇 Type "this.cache" below

    }

    set(key: string, value: T): void {
        // 👇 Type "const entry" or "this.cache.set" below

    }

    get(key: string): T | undefined {
        // 👇 Type "const entry" below

    }

    has(key: string): boolean {
        // 👇 Type "const entry" or "return" below

    }

    delete(key: string): boolean {
        // 👇 Type "return" below

    }

    clear(): void {
        // 👇 Type "this.cache" below

    }

    private isExpired(entry: CacheEntry<T>): boolean {
        // 👇 Type "return" below

    }

    private evictExpired(): void {
        // 👇 Type "for" or "this.cache.forEach" below

    }
}


// =============================================================================
// EXERCISE 7: Union Types and Type Guards
// =============================================================================

type Shape =
    | { kind: 'circle'; radius: number }
    | { kind: 'rectangle'; width: number; height: number }
    | { kind: 'triangle'; base: number; height: number };

function calculateArea(shape: Shape): number {
    // 👇 Type "switch" or "if" below - Copilot will use type narrowing!

}

function isCircle(shape: Shape): shape is { kind: 'circle'; radius: number } {
    // 👇 Type "return" below

}


// =============================================================================
// EXERCISE 8: Error Handling with Types
// =============================================================================

type Result<T, E = Error> =
    | { success: true; data: T }
    | { success: false; error: E };

function parseJSON<T>(json: string): Result<T> {
    // 👇 Type "try" below

}

function divide(a: number, b: number): Result<number, string> {
    // 👇 Type "if" below

}

async function fetchWithTimeout<T>(
    url: string,
    timeoutMs: number
): Promise<Result<T>> {
    // 👇 Type "try" below

}


// =============================================================================
// KEY TAKEAWAYS
// =============================================================================
/**
 * ✅ TypeScript types provide strong context for Copilot
 * ✅ Interfaces define the shape of expected data
 * ✅ Generics work well with Copilot's type inference
 * ✅ Return types guide the implementation
 * ✅ Complex types lead to more accurate suggestions
 *
 * BEST PRACTICES:
 * - Define interfaces before implementing functions
 * - Use specific types rather than 'any'
 * - Include JSDoc comments for additional context
 * - Leverage utility types (Partial, Pick, Omit, etc.)
 *
 * NEXT: Move on to 05-test-generation/ to learn
 *       how to generate unit tests with Copilot!
 */
