import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(30), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    Planets = relationship("Planets")
    People = relationship("People")
    User = relationship("User")

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    image = Column(String(250))
    height = Column(String(100))
    mass = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(20))
    homeworld = Column(String(100)) 

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    image = Column(String(250))
    climate = Column(String(100))
    diameter = Column(String(100))
    gravity = Column(String(100))
    orbital_period = Column(String(100))
    population = Column(String(100))
    rotation_period = Column(String(100))
    surface_water = Column(String(100))
    terrain = Column(String(100))

    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')