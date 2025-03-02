from sqlalchemy import Column, String, Integer, Time, DateTime
from models.base import BaseCls, Base
from models.expense import Expense
from sqlalchemy.orm import relationship
from extensions import bcrypt

class User(BaseCls, Base):
    __tablename__ = 'users'
    username = Column(String(128), unique=True, nullable=False) 
    email = Column(String(128), unique=True, nullable=False)
    _password = Column(String(120), nullable=False)
    expenses = relationship('Expense', back_populates='user')
    monthly_income = Column(Integer)
    notification_time = Column(DateTime)
    currency = Column(String(120))
    
    @property
    def password(self):
        # password getter shows password cant be read
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, password):
        # stores  the hashed password
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')
    def verify_password(self, password):
        # verifies that the entered password is same as stored one
            return bcrypt.check_password_hash(self._password, password)
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)