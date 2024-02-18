#!/usr/bin/python3
"""Module define state class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """class inherit from Base to create states table"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
