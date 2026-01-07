/**
 * Scenario 04: Function Generation with TypeScript
 * ==================================================
 * Create complete functions from signatures and types.
 *
 * INSTRUCTIONS:
 * 1. Define function signatures with proper TypeScript types
 * 2. Let Copilot generate the implementation
 * 3. Types help Copilot understand your intent better
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
    // TODO: Let Copilot generate the implementation
}

function sum(numbers: number[]): number {
    // TODO: Let Copilot generate the implementation
}

function findMax(numbers: number[]): number | undefined {
    // TODO: Let Copilot generate the implementation
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
    // TODO: Let Copilot generate - it knows the User interface!
}

function filterActiveUsers(users: User[]): User[] {
    // TODO: Let Copilot generate
}

function findUserByEmail(users: User[], email: string): User | undefined {
    // TODO: Let Copilot generate
}

function sortUsersByAge(users: User[], ascending: boolean = true): User[] {
    // TODO: Let Copilot generate
}


// =============================================================================
// EXERCISE 3: Generic Functions
// =============================================================================
// Copilot understands generics and type constraints

function first<T>(array: T[]): T | undefined {
    // TODO: Let Copilot generate
}

function last<T>(array: T[]): T | undefined {
    // TODO: Let Copilot generate
}

function unique<T>(array: T[]): T[] {
    // TODO: Let Copilot generate
}

function groupBy<T, K extends keyof T>(array: T[], key: K): Record<string, T[]> {
    // TODO: Let Copilot generate
}

function pluck<T, K extends keyof T>(array: T[], key: K): T[K][] {
    // TODO: Let Copilot generate
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
    // TODO: Let Copilot generate
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
    // TODO: Let Copilot generate
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
    // TODO: Let Copilot generate a mock implementation
}

async function fetchPaginatedUsers(
    page: number,
    pageSize: number
): Promise<PaginatedResponse<User>> {
    // TODO: Let Copilot generate
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
        // TODO: Let Copilot generate
    }

    set(key: string, value: T): void {
        // TODO: Let Copilot generate
    }

    get(key: string): T | undefined {
        // TODO: Let Copilot generate
    }

    has(key: string): boolean {
        // TODO: Let Copilot generate
    }

    delete(key: string): boolean {
        // TODO: Let Copilot generate
    }

    clear(): void {
        // TODO: Let Copilot generate
    }

    private isExpired(entry: CacheEntry<T>): boolean {
        // TODO: Let Copilot generate
    }

    private evictExpired(): void {
        // TODO: Let Copilot generate
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
    // TODO: Let Copilot generate - it will use type narrowing!
}

function isCircle(shape: Shape): shape is { kind: 'circle'; radius: number } {
    // TODO: Let Copilot generate
}


// =============================================================================
// EXERCISE 8: Error Handling with Types
// =============================================================================

type Result<T, E = Error> =
    | { success: true; data: T }
    | { success: false; error: E };

function parseJSON<T>(json: string): Result<T> {
    // TODO: Let Copilot generate
}

function divide(a: number, b: number): Result<number, string> {
    // TODO: Let Copilot generate
}

async function fetchWithTimeout<T>(
    url: string,
    timeoutMs: number
): Promise<Result<T>> {
    // TODO: Let Copilot generate
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
