import models
from datetime import datetime
from uuid import uuid4
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
import uuid
Base = declarative_base()

class BaseCls:
    """sets the id and creation time of instance"""
    id = Column(String(50), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow().date())

    def __init__(self, *args, **kwargs):
        """Imitiates the models"""
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key,value)
        
    def save(self):
        """saves new instance to the database"""
        models.storage.add(self)
        models.storage.save()

    def delete(self):
        """delete the instance"""
        models.storage.delete(self)
 
    def __repr__(self):
        """model repesentation"""
        return '{}-{}'.format(self.__class__.__name__, self.id)