import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favoritecharacterid = Column(Integer, ForeignKey('user.id'))
    favoriteplanetid = Column(Integer, ForeignKey('planet.id'))
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(40), nullable=False)
    email = Column(String(250), nullable=False)
    characters = relationship("Character")
    planets = relationship("Planet")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(10), nullable=False)
    eye_color = Column(String(15), nullable=False)
    hair_color = Column(String(15), nullable=False)


class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(150), nullable=False)
    climate = Column(String(150), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')