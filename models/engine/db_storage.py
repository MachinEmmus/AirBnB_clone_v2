#!/usr/bin/python3
"""DB storage"""
from models.base_model impor BaseModel, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
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
        """get all
        """
        new_dict = {}
        if cls:
            records = self.__session.query(eval(cls)).all()
            for v in records:
                k = "{}.{}".format(type(v).__name__, v.id)
                new_dict[k] = v

        else:
            models = ["City", "Place", "Review", "State", "User"]
            for model in models:
                records = self.__session.query(eval(model)).all()

                for v in records:
                    k = "{}.{}".format(type(v).__name__, v.id)
                    new_dict[k] = v

        return new_dict

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
