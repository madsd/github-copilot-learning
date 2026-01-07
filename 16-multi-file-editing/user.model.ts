/**
 * User Model
 * ===========
 * TypeScript model for User entity.
 * 
 * EXERCISE:
 * Use Copilot Edits to add new fields and see changes propagate
 * to service, controller, and DTOs.
 */

export interface User {
    id: string;
    email: string;
    username: string;
    passwordHash: string;
    firstName: string;
    lastName: string;
    isActive: boolean;
    // TODO: Use Copilot Edits to add:
    // - phoneNumber?: string
    // - role: 'admin' | 'user' | 'guest'
    // - createdAt: Date
    // - updatedAt: Date
}

export interface UserWithoutPassword {
    id: string;
    email: string;
    username: string;
    firstName: string;
    lastName: string;
    isActive: boolean;
}

export function toUserWithoutPassword(user: User): UserWithoutPassword {
    const { passwordHash, ...userWithoutPassword } = user;
    return userWithoutPassword;
}

export function createUserId(): string {
    return `user_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
}
