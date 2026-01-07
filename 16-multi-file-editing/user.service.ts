/**
 * User Service
 * =============
 * Business logic layer for user operations.
 * 
 * EXERCISE:
 * Use Copilot Edits to update this service when the model changes.
 */

import { User, UserWithoutPassword, toUserWithoutPassword, createUserId } from './user.model';
import { CreateUserDto, UpdateUserDto } from './user.dto';

// In-memory storage (replace with actual database in production)
const users: Map<string, User> = new Map();

// Simple password hashing (use bcrypt in production)
function hashPassword(password: string): string {
    return `hashed_${password}`;
}

export class UserService {
    
    async findAll(page: number = 1, pageSize: number = 10): Promise<{
        users: UserWithoutPassword[];
        total: number;
    }> {
        const allUsers = Array.from(users.values())
            .filter(u => u.isActive);
        
        const start = (page - 1) * pageSize;
        const paginatedUsers = allUsers
            .slice(start, start + pageSize)
            .map(toUserWithoutPassword);
        
        return {
            users: paginatedUsers,
            total: allUsers.length
        };
    }
    
    async findById(id: string): Promise<UserWithoutPassword | null> {
        const user = users.get(id);
        if (!user || !user.isActive) {
            return null;
        }
        return toUserWithoutPassword(user);
    }
    
    async findByEmail(email: string): Promise<UserWithoutPassword | null> {
        const user = Array.from(users.values())
            .find(u => u.email === email && u.isActive);
        
        if (!user) {
            return null;
        }
        return toUserWithoutPassword(user);
    }
    
    async findByUsername(username: string): Promise<UserWithoutPassword | null> {
        const user = Array.from(users.values())
            .find(u => u.username === username && u.isActive);
        
        if (!user) {
            return null;
        }
        return toUserWithoutPassword(user);
    }
    
    async create(dto: CreateUserDto): Promise<UserWithoutPassword> {
        // Check if email already exists
        const existingEmail = await this.findByEmail(dto.email);
        if (existingEmail) {
            throw new Error('Email already exists');
        }
        
        // Check if username already exists
        const existingUsername = await this.findByUsername(dto.username);
        if (existingUsername) {
            throw new Error('Username already exists');
        }
        
        const user: User = {
            id: createUserId(),
            email: dto.email,
            username: dto.username,
            passwordHash: hashPassword(dto.password),
            firstName: dto.firstName,
            lastName: dto.lastName,
            isActive: true,
            // TODO: Copilot Edits will add new fields here
        };
        
        users.set(user.id, user);
        return toUserWithoutPassword(user);
    }
    
    async update(id: string, dto: UpdateUserDto): Promise<UserWithoutPassword | null> {
        const user = users.get(id);
        if (!user || !user.isActive) {
            return null;
        }
        
        // Check email uniqueness if changing
        if (dto.email && dto.email !== user.email) {
            const existingEmail = await this.findByEmail(dto.email);
            if (existingEmail) {
                throw new Error('Email already exists');
            }
        }
        
        // Check username uniqueness if changing
        if (dto.username && dto.username !== user.username) {
            const existingUsername = await this.findByUsername(dto.username);
            if (existingUsername) {
                throw new Error('Username already exists');
            }
        }
        
        // Update fields
        if (dto.email !== undefined) user.email = dto.email;
        if (dto.username !== undefined) user.username = dto.username;
        if (dto.password !== undefined) user.passwordHash = hashPassword(dto.password);
        if (dto.firstName !== undefined) user.firstName = dto.firstName;
        if (dto.lastName !== undefined) user.lastName = dto.lastName;
        if (dto.isActive !== undefined) user.isActive = dto.isActive;
        // TODO: Copilot Edits will add new field updates here
        
        users.set(id, user);
        return toUserWithoutPassword(user);
    }
    
    async delete(id: string): Promise<boolean> {
        const user = users.get(id);
        if (!user) {
            return false;
        }
        
        // Soft delete
        user.isActive = false;
        users.set(id, user);
        return true;
    }
    
    async hardDelete(id: string): Promise<boolean> {
        return users.delete(id);
    }
}

export const userService = new UserService();
