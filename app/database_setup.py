#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    shelter_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    street = Column(String(200), nullable=False)
    city = Column(String(200), nullable=False)
    state = Column(String(30), nullable=False)
    zipcode = Column(Integer, nullable=False)
    website = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    current_occupancy = Column(String(100), nullable=False)
    maximum_occupancy = Column(String(100), nullable=False)
    puppy = relationship('puppy', back_populates='shelter')  #uselist=True


class Puppy(Base):
    __tablename__ = 'puppy'

    puppy_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    date_of_birth = Column(String(200), nullable=False)
    breed = Column(String(200), nullable=False)
    gender = Column(String(6), nullable=False)
    age = Column(Integer, nullable=False)
    picture = Column(String(300), nullable=False)
    shelter_id = Column(Integer, ForeignKey('shelter.shelter_id'))
    shelter = relationship('shelter', uselist=False, back_populates='puppy')
    puppy_adopter = relationship('puppy_adopter', uselist=False, back_populates='puppy')


class PuppyAdopter(Base):
    __tablename__ = 'puppy_adopter'

    serial_no = Column(Integer, primary_key=True)
    puppy_id = Column(Integer, ForeignKey('puppy.puppy_id'))
    puppy = relationship('puppy', uselist=False, back_populates='puppy_profile')
    adopter_id = Column(Integer, ForeignKey('adopter.adopter_id'))
    adopter = relationship('adopter', back_populates='puppy_adopter')  #uselist=True


class Adopter(Base):
    __tablename__ = 'adopter'

    adopter_id = Column(Integer, primary_key=True)
    adopter_name = Column(String(100), nullable=False)
    puppy_id = Column(Integer, ForeignKey('puppy.puppy_id'))
    puppy_adopter = relationship('puppy_adopter', uselist=False, back_populates='adopter')

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://testdb:hello@localhost/production_dogshelter')

    # Creates tables in the database. If tables are already present, it won't recreate them.
    Base.metadata.create_all(engine)
    


