import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Personajes(Base):
     __tablename__= 'personajes'
     id = Column(Integer, primary_key=True)
     nombre =  Column(String(250), nullable=False)
     estatura = Column(Integer)
     peso = Column(Integer)
     favoritos = relationship("favoritos")

class Planetas(Base):
     __tablename__='planetas'
     id = Column(Integer, primary_key=True)
     nombre = Column(String(250), nullable=False)
     gravedad = Column(Integer)
     clima = Column(String(250), nullable=False)
     favoritos= relationship("favoritos")

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    nombre =  Column(String(250), nullable=False)
    password =  Column(String(250), nullable=False)
    email=  Column(String(250), nullable=False)
    edad=  Column(Integer)
    favoritos= relationship("favoritos")
class Favoritos(Base):
     __tablename__='favoritos'
     id = Column(Integer, primary_key=True)
     user = Column(Integer, ForeignKey("user.id"))
     planetas = Column(Integer, ForeignKey("planetas.id"))
     personajes= Column(Integer, ForeignKey("personajes.id"))



     


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
