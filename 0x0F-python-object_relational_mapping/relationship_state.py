#!/usr/bin/python3
"""Module define state class"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """class inherit from Base to create states table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    
