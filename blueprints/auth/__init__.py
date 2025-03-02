from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)
from blueprints.auth import routes