/**
 * Scenario 11: API Integration
 * ==============================
 * Build API calls and handle responses with GitHub Copilot.
 *
 * INSTRUCTIONS:
 * 1. Function signatures and types are already defined
 * 2. Place cursor inside the function body
 * 3. Start typing (e.g., "const response = " or "return") to trigger Copilot
 * 4. Copilot uses the types and function names to generate appropriate code
 *
 * TIP: Use Ctrl+I on a function to ask "implement this function"
 *
 * WHAT YOU'LL LEARN:
 * - Generating API client code
 * - Handling responses and errors
 * - Building typed API wrappers
 * - Working with authentication
 */

// =============================================================================
// TYPES AND INTERFACES
// =============================================================================

interface User {
    id: number;
    name: string;
    email: string;
    username: string;
}

interface Post {
    id: number;
    userId: number;
    title: string;
    body: string;
}

interface Comment {
    id: number;
    postId: number;
    name: string;
    email: string;
    body: string;
}

interface ApiResponse<T> {
    data: T;
    status: number;
    message: string;
}

interface PaginatedResponse<T> {
    data: T[];
    page: number;
    totalPages: number;
    totalItems: number;
}


// =============================================================================
// EXERCISE 1: Basic API Client
// =============================================================================
// Type inside each function to let Copilot generate the implementation

const API_BASE_URL = 'https://jsonplaceholder.typicode.com';

// Function to fetch all users from /users endpoint
async function fetchUsers(): Promise<User[]> {
    // 👇 Type "const response = await fetch" below

}

// Function to fetch a single user by ID
async function fetchUserById(id: number): Promise<User> {
    // 👇 Type "const response" below

}

// Function to fetch posts for a specific user
async function fetchUserPosts(userId: number): Promise<Post[]> {
    // 👇 Type "const response" below

}


// =============================================================================
// EXERCISE 2: Error Handling
// =============================================================================

// Custom error class for API errors
class ApiError extends Error {
    // 👇 Type "constructor" below

}

// Wrapper function that handles errors consistently
async function apiRequest<T>(
    endpoint: string,
    options?: RequestInit
): Promise<T> {
    // 👇 Type "const response = await fetch" below

}


// =============================================================================
// EXERCISE 3: CRUD Operations
// =============================================================================

// Create a new post
async function createPost(post: Omit<Post, 'id'>): Promise<Post> {
    // 👇 Type "const response = await fetch" below

}

// Update an existing post
async function updatePost(id: number, updates: Partial<Post>): Promise<Post> {
    // 👇 Type "const response" below

}

// Delete a post
async function deletePost(id: number): Promise<boolean> {
    // 👇 Type "const response" below

}


// =============================================================================
// EXERCISE 4: Query Parameters and Filtering
// =============================================================================

interface PostQueryParams {
    userId?: number;
    _page?: number;
    _limit?: number;
    _sort?: string;
    _order?: 'asc' | 'desc';
}

// Function to fetch posts with query parameters
async function fetchPostsWithParams(params: PostQueryParams): Promise<Post[]> {
    // 👇 Type "const searchParams" or "const url" below

}

// Function to search posts by title
async function searchPosts(query: string): Promise<Post[]> {
    // 👇 Type "return fetch" below

}


// =============================================================================
// EXERCISE 5: Authentication
// =============================================================================

interface AuthTokens {
    accessToken: string;
    refreshToken: string;
    expiresIn: number;
}

// Function to login and get tokens
async function login(email: string, password: string): Promise<AuthTokens> {
    // 👇 Type "const response = await fetch" below

}

// Function to create an authenticated fetch wrapper
function createAuthenticatedClient(getToken: () => string) {
    // 👇 Type "return async" below

}

// Function to refresh access token
async function refreshAccessToken(refreshToken: string): Promise<AuthTokens> {
    // 👇 Type "const response" below

}


// =============================================================================
// EXERCISE 6: Retry Logic
// =============================================================================

interface RetryOptions {
    maxRetries: number;
    baseDelay: number;
    maxDelay: number;
    retryOn: number[]; // HTTP status codes to retry on
}

// Function with exponential backoff retry
async function fetchWithRetry<T>(
    url: string,
    options?: RequestInit,
    retryOptions?: Partial<RetryOptions>
): Promise<T> {
    // 👇 Type "const { maxRetries" or "let retries" below

}


// =============================================================================
// EXERCISE 7: Request Cancellation
// =============================================================================

// Function that supports request cancellation
function fetchWithCancel<T>(url: string): {
    promise: Promise<T>;
    cancel: () => void;
} {
    // 👇 Type "const controller" below

}

// Hook-style function for cancellable requests
function useCancellableFetch() {
    // 👇 Type "const controller" below

}


// =============================================================================
// EXERCISE 8: API Client Class
// =============================================================================

// Complete API client with all features
class ApiClient {
    private baseUrl: string;
    private defaultHeaders: Record<string, string>;
    private authToken?: string;

    constructor(baseUrl: string, options?: { headers?: Record<string, string> }) {
        // 👇 Type "this.baseUrl" below

    }

    setAuthToken(token: string): void {
        // 👇 Type "this.authToken" below

    }

    clearAuthToken(): void {
        // 👇 Type "this.authToken" below

    }

    async get<T>(endpoint: string, params?: Record<string, any>): Promise<T> {
        // 👇 Type "const url" below

    }

    async post<T>(endpoint: string, data: any): Promise<T> {
        // 👇 Type "const response" below

    }

    async put<T>(endpoint: string, data: any): Promise<T> {
        // 👇 Type "const response" below

    }

    async patch<T>(endpoint: string, data: any): Promise<T> {
        // 👇 Type "const response" below

    }

    async delete<T>(endpoint: string): Promise<T> {
        // 👇 Type "const response" below

    }
}


// =============================================================================
// EXERCISE 9: Rate Limiting
// =============================================================================

// Rate limiter for API requests
class RateLimiter {
    private requestsPerSecond: number;
    private queue: Array<() => void>;
    
    constructor(requestsPerSecond: number) {
        // 👇 Type "this.requestsPerSecond" below

    }

    async throttle<T>(fn: () => Promise<T>): Promise<T> {
        // 👇 Type "return new Promise" below

    }
}


// =============================================================================
// EXERCISE 10: Caching
// =============================================================================

interface CacheOptions {
    ttl: number; // Time to live in milliseconds
    maxSize: number;
}

// Cached API client
class CachedApiClient {
    private cache: Map<string, { data: any; timestamp: number }>;
    private options: CacheOptions;

    constructor(options: CacheOptions) {
        // 👇 Type "this.cache" below

    }

    async fetch<T>(url: string, options?: RequestInit): Promise<T> {
        // 👇 Type "const cacheKey" or "const cached" below

    }

    invalidate(pattern?: string): void {
        // 👇 Type "if (pattern)" or "this.cache" below

    }
}


// =============================================================================
// KEY TAKEAWAYS
// =============================================================================
/**
 * ✅ Describe the API structure in comments and interfaces
 * ✅ Ask for specific error handling patterns
 * ✅ Request authentication and security features
 * ✅ Ask for retry logic and rate limiting
 * ✅ Use types to guide API response handling
 *
 * COPILOT PROMPTS:
 * - "Create a fetch wrapper with error handling"
 * - "Add retry logic with exponential backoff"
 * - "Implement request caching"
 * - "Add authentication header handling"
 * - "Create a rate limiter for API requests"
 *
 * NEXT: Move on to 12-copilot-chat-basics.md to learn
 *       about interactive conversations with Copilot Chat!
 */

export {};
