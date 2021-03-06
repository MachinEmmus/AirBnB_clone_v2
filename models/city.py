#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    hbnb_storage = os.getenv("HBNB_TYPE_STORAGE")
    if hbnb_storage == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        state_id = ""
        name = ""
