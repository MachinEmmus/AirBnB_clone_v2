#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    hbnb_storage = os.getenv("HBNB_TYPE_STORAGE")
    if hbnb_storage == "db":
        state_id = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id
            """
            cities = []
            for k, c in models.storage.all(City).items():
                if c.state_id == self.id:
                    cities.append(city)
            return cities
