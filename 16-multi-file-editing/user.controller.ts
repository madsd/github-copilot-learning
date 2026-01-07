/**
 * User Controller
 * ================
 * API endpoints for user operations.
 * 
 * EXERCISE:
 * Use Copilot Edits to update this controller when adding new features.
 */

import { userService } from './user.service';
import { 
    CreateUserDto, 
    UpdateUserDto, 
    UserResponseDto,
    UserListResponseDto,
    validateCreateUserDto,
    validateUpdateUserDto
} from './user.dto';
import { UserWithoutPassword } from './user.model';

// Simulated Express-like request/response types
interface Request {
    params: Record<string, string>;
    query: Record<string, string>;
    body: any;
}

interface Response {
    status(code: number): Response;
    json(data: any): void;
}

function toResponseDto(user: UserWithoutPassword): UserResponseDto {
    return {
        id: user.id,
        email: user.email,
        username: user.username,
        firstName: user.firstName,
        lastName: user.lastName,
        isActive: user.isActive,
        // TODO: Copilot Edits will add new fields here
    };
}

export class UserController {
    
    /**
     * GET /users
     * List all users with pagination
     */
    async listUsers(req: Request, res: Response): Promise<void> {
        try {
            const page = parseInt(req.query.page || '1', 10);
            const pageSize = parseInt(req.query.pageSize || '10', 10);
            
            const result = await userService.findAll(page, pageSize);
            
            const response: UserListResponseDto = {
                users: result.users.map(toResponseDto),
                total: result.total,
                page,
                pageSize
            };
            
            res.status(200).json(response);
        } catch (error) {
            res.status(500).json({ error: 'Internal server error' });
        }
    }
    
    /**
     * GET /users/:id
     * Get a user by ID
     */
    async getUser(req: Request, res: Response): Promise<void> {
        try {
            const { id } = req.params;
            const user = await userService.findById(id);
            
            if (!user) {
                res.status(404).json({ error: 'User not found' });
                return;
            }
            
            res.status(200).json(toResponseDto(user));
        } catch (error) {
            res.status(500).json({ error: 'Internal server error' });
        }
    }
    
    /**
     * POST /users
     * Create a new user
     */
    async createUser(req: Request, res: Response): Promise<void> {
        try {
            const dto: CreateUserDto = req.body;
            
            // Validate input
            const errors = validateCreateUserDto(dto);
            if (errors.length > 0) {
                res.status(400).json({ errors });
                return;
            }
            
            const user = await userService.create(dto);
            res.status(201).json(toResponseDto(user));
        } catch (error: any) {
            if (error.message === 'Email already exists' || 
                error.message === 'Username already exists') {
                res.status(409).json({ error: error.message });
            } else {
                res.status(500).json({ error: 'Internal server error' });
            }
        }
    }
    
    /**
     * PUT /users/:id
     * Update an existing user
     */
    async updateUser(req: Request, res: Response): Promise<void> {
        try {
            const { id } = req.params;
            const dto: UpdateUserDto = req.body;
            
            // Validate input
            const errors = validateUpdateUserDto(dto);
            if (errors.length > 0) {
                res.status(400).json({ errors });
                return;
            }
            
            const user = await userService.update(id, dto);
            
            if (!user) {
                res.status(404).json({ error: 'User not found' });
                return;
            }
            
            res.status(200).json(toResponseDto(user));
        } catch (error: any) {
            if (error.message === 'Email already exists' || 
                error.message === 'Username already exists') {
                res.status(409).json({ error: error.message });
            } else {
                res.status(500).json({ error: 'Internal server error' });
            }
        }
    }
    
    /**
     * DELETE /users/:id
     * Delete a user (soft delete)
     */
    async deleteUser(req: Request, res: Response): Promise<void> {
        try {
            const { id } = req.params;
            const success = await userService.delete(id);
            
            if (!success) {
                res.status(404).json({ error: 'User not found' });
                return;
            }
            
            res.status(204).json(null);
        } catch (error) {
            res.status(500).json({ error: 'Internal server error' });
        }
    }
}

export const userController = new UserController();


/**
 * Example route registration (Express-like):
 * 
 * router.get('/users', userController.listUsers);
 * router.get('/users/:id', userController.getUser);
 * router.post('/users', userController.createUser);
 * router.put('/users/:id', userController.updateUser);
 * router.delete('/users/:id', userController.deleteUser);
 */
