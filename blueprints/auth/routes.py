from blueprints import auth
from blueprints.auth import auth_bp
from flask import request, jsonify
import models
from models import storage
from models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token


@auth_bp.route('/login', methods={'POST'})
def login():
    """sign the user in andgenerate sesion JWT token"""
    data = request.get_json()
    if 'email' and 'password' in data:
        email = data['email']
        password = data['password']
    else:
        return jsonify({'error': 'Email and password are required'}), 400
    user = storage.get_user('email', email)
    if not user or not user.verify_password(password):
        return jsonify({'error': 'Invalid credentials'}), 400
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 201

@auth_bp.route('/signup', methods={'POST'})
def signup():
    """register new user"""
    data = request.get_json()
    if 'email' and 'password' in data:
        email = data['email']
        password = data['password']
    else:
        return jsonify({'error': 'Email and password are required'}), 400
    # get user details
    user_exists = storage.get_user('email', email)
    if user_exists:
        return jsonify({'error': 'You have an account with us, please sign in'}), 400
    try:
        #Try to add new user with the details
        new_user = User(username=data['username'], password=data['password'], email=data['email'], monthly_income=data['monthly_income'], currency=data['currency'])
    except KeyError as err:
        return jsonify({'error': str(err)})    
    storage.add(new_user)
    storage.save()
    return jsonify({'message': 'Registration successful. You can now login with your details'}), 201