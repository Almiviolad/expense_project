from models.base import BaseCls, Base
from models.expense import Expense
from models.user import User
from sqlalchemy import create_engine, Integer, String, Time
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {'User': User, 'Expense': Expense}
class DBstorage:
    """Database class"""
    __engine = None
    __session = None
    def __init__(self):
        """Instantiate the database storage class"""
        self.__engine = create_engine('mysql://root:almiviolad@localhost/trackxpense', echo=True)

    def add(self, obj):
        """add new obj to the database session"""
        self.__session.add(obj)

    def save(self):
        """saves the new objs or changes to DB"""   
        self.__session.commit()
    
    def reload(self):
        """Reloads objs from FB and starts session"""
        with self.__engine.connect() as connection:
            Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
    def all(self, cls):
        """returns all instances of a cls or all instance in DB"""
        all_obj = {}
        for clss in classes:
            if not cls or cls in classes or cls is clss:
                objs = self.__session.query(classes[clss]).all()          
                for obj in objs:
                    all_obj[obj] = obj.__dict__
        return all_obj
        
    def get_user(self, method, user_info):
        """gets an object from the DB isomg id"""
        return self.__session.query(User).filter(getattr(User, method) == user_info).first()
    
    def get_user_expenses(self, uid):
        """gets all the expenses of a user"""
        return self.__session.query(Expense).filter_by(user_id = uid)
    
    def get_expense(self, expense_id):
        return self.__session.query(Expense).filter_by(id = expense_id)
    
    def delete(self, obj):
        """delete the obj passed as arg from the DB"""
        self.__session.delete(obj)
        self.save()

    def remove_session(self):
        self.__session.remove()
