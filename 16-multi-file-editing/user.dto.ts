/**
 * User Data Transfer Objects
 * ===========================
 * DTOs for API request/response validation.
 * 
 * EXERCISE:
 * Use Copilot Edits to keep these in sync with the User model.
 */

export interface CreateUserDto {
    email: string;
    username: string;
    password: string;
    firstName: string;
    lastName: string;
    // TODO: Copilot Edits will add new fields here
}

export interface UpdateUserDto {
    email?: string;
    username?: string;
    password?: string;
    firstName?: string;
    lastName?: string;
    isActive?: boolean;
    // TODO: Copilot Edits will add new fields here
}

export interface UserResponseDto {
    id: string;
    email: string;
    username: string;
    firstName: string;
    lastName: string;
    isActive: boolean;
    // TODO: Copilot Edits will add new fields here
}

export interface UserListResponseDto {
    users: UserResponseDto[];
    total: number;
    page: number;
    pageSize: number;
}

export function validateCreateUserDto(dto: CreateUserDto): string[] {
    const errors: string[] = [];
    
    if (!dto.email) {
        errors.push('Email is required');
    }
    
    if (!dto.username) {
        errors.push('Username is required');
    } else if (dto.username.length < 3) {
        errors.push('Username must be at least 3 characters');
    }
    
    if (!dto.password) {
        errors.push('Password is required');
    } else if (dto.password.length < 8) {
        errors.push('Password must be at least 8 characters');
    }
    
    if (!dto.firstName) {
        errors.push('First name is required');
    }
    
    if (!dto.lastName) {
        errors.push('Last name is required');
    }
    
    // TODO: Copilot Edits will add validation for new fields
    
    return errors;
}

export function validateUpdateUserDto(dto: UpdateUserDto): string[] {
    const errors: string[] = [];
    
    if (dto.username !== undefined && dto.username.length < 3) {
        errors.push('Username must be at least 3 characters');
    }
    
    if (dto.password !== undefined && dto.password.length < 8) {
        errors.push('Password must be at least 8 characters');
    }
    
    // TODO: Copilot Edits will add validation for new fields
    
    return errors;
}
