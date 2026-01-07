"""
Configuration Module
====================
Application configuration settings.

EXERCISE:
Open Copilot Chat and ask:
- "@workspace How is configuration used across the application?"
- "#file:config.py How would I add Redis configuration?"
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class."""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    # Server settings
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///app.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = DEBUG
    
    # Pagination defaults
    DEFAULT_PAGE_SIZE = 10
    MAX_PAGE_SIZE = 100
    
    # Security settings
    BCRYPT_LOG_ROUNDS = 12
    TOKEN_EXPIRATION_HOURS = 24
    
    # CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    
    # Override with production-specific settings
    BCRYPT_LOG_ROUNDS = 14


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get configuration based on environment."""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])


# TODO: Ask Copilot with @workspace:
# "What other configuration options might this application need?"
# "How should I handle secrets in production?"
