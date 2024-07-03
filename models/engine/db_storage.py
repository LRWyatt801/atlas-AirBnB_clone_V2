"""Database storage module"""

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, create_engine

from models.base_model import Base


class DBStorage:
    """Class for database storage"""
    
    __engine = None
    __session = None
    
    def __init__(self) -> None:
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Returns dict of all cls"""
        new_dict = {}
        for classs in classes:
            if cls is None:
                obj = self.__session.query(classes[classs]).all()
                for objs in obj:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

