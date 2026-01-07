/**
 * Scenario 11: API Integration
 * ==============================
 * Build API calls and handle responses with GitHub Copilot.
 *
 * INSTRUCTIONS:
 * 1. Describe the API you want to call in comments
 * 2. Let Copilot generate the fetch/axios code
 * 3. Ask for error handling and retry logic
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
// Create a basic API client using fetch

const API_BASE_URL = 'https://jsonplaceholder.typicode.com';

// Function to fetch all users from /users endpoint
// TODO: Let Copilot generate this function
async function fetchUsers(): Promise<User[]> {

}

// Function to fetch a single user by ID
// TODO: Let Copilot generate this function
async function fetchUserById(id: number): Promise<User> {

}

// Function to fetch posts for a specific user
// TODO: Let Copilot generate this function
async function fetchUserPosts(userId: number): Promise<Post[]> {

}


// =============================================================================
// EXERCISE 2: Error Handling
// =============================================================================

// Custom error class for API errors
// TODO: Let Copilot generate this class
class ApiError extends Error {

}

// Wrapper function that handles errors consistently
// TODO: Let Copilot generate this function
async function apiRequest<T>(
    endpoint: string,
    options?: RequestInit
): Promise<T> {

}


// =============================================================================
// EXERCISE 3: CRUD Operations
// =============================================================================

// Create a new post
// TODO: Let Copilot generate this function
async function createPost(post: Omit<Post, 'id'>): Promise<Post> {

}

// Update an existing post
// TODO: Let Copilot generate this function
async function updatePost(id: number, updates: Partial<Post>): Promise<Post> {

}

// Delete a post
// TODO: Let Copilot generate this function
async function deletePost(id: number): Promise<boolean> {

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
// TODO: Let Copilot generate this function
async function fetchPostsWithParams(params: PostQueryParams): Promise<Post[]> {

}

// Function to search posts by title
// TODO: Let Copilot generate this function
async function searchPosts(query: string): Promise<Post[]> {

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
// TODO: Let Copilot generate this function
async function login(email: string, password: string): Promise<AuthTokens> {

}

// Function to create an authenticated fetch wrapper
// TODO: Let Copilot generate this function
function createAuthenticatedClient(getToken: () => string) {

}

// Function to refresh access token
// TODO: Let Copilot generate this function
async function refreshAccessToken(refreshToken: string): Promise<AuthTokens> {

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
// TODO: Let Copilot generate this function
async function fetchWithRetry<T>(
    url: string,
    options?: RequestInit,
    retryOptions?: Partial<RetryOptions>
): Promise<T> {

}


// =============================================================================
// EXERCISE 7: Request Cancellation
// =============================================================================

// Function that supports request cancellation
// TODO: Let Copilot generate this function
function fetchWithCancel<T>(url: string): {
    promise: Promise<T>;
    cancel: () => void;
} {

}

// Hook-style function for cancellable requests
// TODO: Let Copilot generate this function
function useCancellableFetch() {

}


// =============================================================================
// EXERCISE 8: API Client Class
// =============================================================================

// Complete API client with all features
// TODO: Let Copilot generate this class based on the signature
class ApiClient {
    private baseUrl: string;
    private defaultHeaders: Record<string, string>;
    private authToken?: string;

    constructor(baseUrl: string, options?: { headers?: Record<string, string> }) {
        // TODO: Initialize
    }

    setAuthToken(token: string): void {
        // TODO: Implement
    }

    clearAuthToken(): void {
        // TODO: Implement
    }

    async get<T>(endpoint: string, params?: Record<string, any>): Promise<T> {
        // TODO: Implement
    }

    async post<T>(endpoint: string, data: any): Promise<T> {
        // TODO: Implement
    }

    async put<T>(endpoint: string, data: any): Promise<T> {
        // TODO: Implement
    }

    async patch<T>(endpoint: string, data: any): Promise<T> {
        // TODO: Implement
    }

    async delete<T>(endpoint: string): Promise<T> {
        // TODO: Implement
    }
}


// =============================================================================
// EXERCISE 9: Rate Limiting
// =============================================================================

// Rate limiter for API requests
// TODO: Let Copilot generate this class
class RateLimiter {
    private requestsPerSecond: number;
    private queue: Array<() => void>;
    
    constructor(requestsPerSecond: number) {
        // TODO: Implement
    }

    async throttle<T>(fn: () => Promise<T>): Promise<T> {
        // TODO: Implement
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
// TODO: Let Copilot generate this class
class CachedApiClient {
    private cache: Map<string, { data: any; timestamp: number }>;
    private options: CacheOptions;

    constructor(options: CacheOptions) {
        // TODO: Implement
    }

    async fetch<T>(url: string, options?: RequestInit): Promise<T> {
        // TODO: Implement with caching
    }

    invalidate(pattern?: string): void {
        // TODO: Implement cache invalidation
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
