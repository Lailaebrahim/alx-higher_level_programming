#!/usr/bin/python3
"""Module define state class
Where there is a ont to many relationship between state and city class
where each state can have many cities connected to it
also all, delete-orphan automatically delete all the cities related toa
A state when this state is deleted"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """class inherit from Base to create states table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
