#!/usr/bin/python3
"""DB storage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """Class that take SQL
    """
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        config = "{}+{}://{}:{}@{}:{}/{}".format(
            'mysql', 'mysqldb', os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'), os.getenv('HBNB_MYSQL_HOST'),
            3306, os.getenv('HBNB_MYSQL_DB')
        )

        self.__engine = create_engine(config, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add obj
        """
        self.__session.add(obj)

    def save(self):
        """save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete
        """
        self.__session.delete(obj)

    def reload(self):
        """reload
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )

        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close
        """
        self.__session.close()
