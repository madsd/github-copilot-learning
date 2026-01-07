"""
Sample Flask Application
========================
This is a sample application for practicing @workspace queries.

EXERCISE:
Open Copilot Chat and ask:
- "@workspace Explain the structure of this application"
- "@workspace How do I add a new endpoint?"
- "@workspace What dependencies does this project need?"
"""

from flask import Flask, jsonify, request
from models import User, db
from services import UserService
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'version': '1.0.0'})


@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users with optional filtering."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    try:
        users = UserService.get_all_users(page=page, per_page=per_page)
        return jsonify({
            'users': [user.to_dict() for user in users.items],
            'total': users.total,
            'pages': users.pages,
            'current_page': users.page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID."""
    try:
        user = UserService.get_user_by_id(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    required_fields = ['username', 'email']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({'error': f'Missing fields: {missing}'}), 400
    
    try:
        user = UserService.create_user(
            username=data['username'],
            email=data['email'],
            password=data.get('password', 'default123')
        )
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        user = UserService.update_user(user_id, data)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# TODO: Ask Copilot with @workspace:
# "How would I add a DELETE endpoint for users?"


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=Config.DEBUG, port=Config.PORT)
