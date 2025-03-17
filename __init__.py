from flask import Flask
from sqlalchemy.orm import sessionmaker, scoped_session
from blueprints.auth import auth_bp
from blueprints.expense import expense_bp
from models.base import BaseCls, Base
from models.user import User
from models.expense import Expense
from extensions import jwt, bcrypt
import config
from models import storage


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(expense_bp, url_prefix='/expense')
    @app.teardown_appcontext
    def remove_session(exception=None):
        storage.remove_session()
    return app