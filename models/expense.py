from sqlalchemy import Column, ForeignKey, String, Integer, Enum as sqlalchemyEnum
from models.base import BaseCls, Base
from sqlalchemy.orm import relationship
from enum import Enum
from datetime import datetime


class SpendingCategoryEnum(Enum):
    FOOD = "Food & Groceries"
    HOUSING = "Housing & Rent"
    UTILITIES = "Utilities (Electricity, Water, Gas)"
    TRANSPORTATION = "Transportation (Fuel, Public Transport)"
    HEALTHCARE = "Healthcare & Medical Expenses"
    EDUCATION = "Education & Tuition"
    ENTERTAINMENT = "Entertainment & Leisure"
    CLOTHING = "Clothing & Apparel"
    INSURANCE = "Insurance"
    SAVINGS = "Savings & Investments"
    DEBT = "Debt Repayment"
    GIFTS = "Gifts & Donations"
    TRAVEL = "Travel & Vacations"
    PERSONAL_CARE = "Personal Care (Haircuts, Beauty)"
    SUBSCRIPTIONS = "Subscriptions (Streaming, Magazines)"
    TECHNOLOGY = "Technology (Devices, Software)"
    CHILDCARE = "Childcare & Schooling"
    PET_CARE = "Pet Care"
    MISC = "Miscellaneous"

class Expense(BaseCls, Base):
    __tablename__ = 'expense'
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String(500))
    user = relationship('User', back_populates='expenses')
    category = Column(sqlalchemyEnum(SpendingCategoryEnum), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.created_at,
            'user_id': self.user_id,
            'amount': self.amount,
            'description': self.description,
            'category': self.category.name
        }