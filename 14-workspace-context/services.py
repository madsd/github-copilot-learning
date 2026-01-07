"""
Service Layer
=============
Business logic for the application.

EXERCISE:
Open Copilot Chat and ask:
- "@workspace How does the service layer interact with models?"
- "#file:services.py #file:app.py How is error handling done?"
"""

from models import User, db
from sqlalchemy.exc import IntegrityError
import re


class UserService:
    """Service class for user operations."""
    
    @staticmethod
    def validate_email(email):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_username(username):
        """Validate username format."""
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        if len(username) > 80:
            return False, "Username must be less than 80 characters"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        return True, None
    
    @staticmethod
    def get_all_users(page=1, per_page=10):
        """Get all users with pagination."""
        return User.query.filter_by(is_active=True).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get a user by their ID."""
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_email(email):
        """Get a user by their email."""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_user_by_username(username):
        """Get a user by their username."""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def create_user(username, email, password):
        """Create a new user."""
        # Validate username
        is_valid, error = UserService.validate_username(username)
        if not is_valid:
            raise ValueError(error)
        
        # Validate email
        if not UserService.validate_email(email):
            raise ValueError("Invalid email format")
        
        # Check if username already exists
        if UserService.get_user_by_username(username):
            raise ValueError("Username already exists")
        
        # Check if email already exists
        if UserService.get_user_by_email(email):
            raise ValueError("Email already exists")
        
        # Create and save user
        try:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Could not create user")
    
    @staticmethod
    def update_user(user_id, data):
        """Update an existing user."""
        user = UserService.get_user_by_id(user_id)
        if not user:
            return None
        
        # Update allowed fields
        if 'username' in data:
            is_valid, error = UserService.validate_username(data['username'])
            if not is_valid:
                raise ValueError(error)
            existing = UserService.get_user_by_username(data['username'])
            if existing and existing.id != user_id:
                raise ValueError("Username already exists")
            user.username = data['username']
        
        if 'email' in data:
            if not UserService.validate_email(data['email']):
                raise ValueError("Invalid email format")
            existing = UserService.get_user_by_email(data['email'])
            if existing and existing.id != user_id:
                raise ValueError("Email already exists")
            user.email = data['email']
        
        if 'password' in data:
            user.set_password(data['password'])
        
        if 'is_active' in data:
            user.is_active = data['is_active']
        
        try:
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Could not update user")
    
    @staticmethod
    def delete_user(user_id, soft_delete=True):
        """Delete a user (soft delete by default)."""
        user = UserService.get_user_by_id(user_id)
        if not user:
            return False
        
        if soft_delete:
            user.is_active = False
            db.session.commit()
        else:
            db.session.delete(user)
            db.session.commit()
        
        return True
    
    @staticmethod
    def search_users(query, page=1, per_page=10):
        """Search users by username or email."""
        search_pattern = f"%{query}%"
        return User.query.filter(
            (User.username.ilike(search_pattern)) |
            (User.email.ilike(search_pattern))
        ).filter_by(is_active=True).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )


# TODO: Ask Copilot with @workspace:
# "What services might we need for the Post model?"
# "How should we handle authentication in this project?"
