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
    puppy = relationship('Puppy', back_populates='shelter')  #uselist=True

    def __init__(self, name=None, street=None, city=None, state=None,
                 zipcode=None, website=None, email=None,
                 current_occupancy=None, maximum_occupancy=None):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.website = website
        self.email = email
        self.current_occupancy = current_occupancy
        self.maximum_occupancy = maximum_occupancy


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
    shelter = relationship('Shelter', uselist=False, back_populates='puppy')
    puppy_adopter = relationship('PuppyAdopter', uselist=False, back_populates='puppy')


class PuppyAdopter(Base):
    __tablename__ = 'puppy_adopter'

    serial_no = Column(Integer, primary_key=True)   # Had to add because
                                                    # sqlalchemy does let
                                                    # create tables without
                                                    # primary key
    puppy_id = Column(Integer, ForeignKey('puppy.puppy_id'))
    puppy = relationship('Puppy', uselist=False, back_populates='puppy_adopter')
    adopter_id = Column(Integer, ForeignKey('adopter.adopter_id'))
    adopter = relationship('Adopter', back_populates='puppy_adopter')  #uselist=True


class Adopter(Base):
    __tablename__ = 'adopter'

    adopter_id = Column(Integer, primary_key=True)
    adopter_name = Column(String(100), nullable=False)
    adopter_phone = Column(String(20), nullable=False)
    street = Column(String(200), nullable=False)
    city = Column(String(200), nullable=False)
    state = Column(String(30), nullable=False)
    zipcode = Column(Integer, nullable=False)
    puppy_id = Column(Integer, ForeignKey('puppy.puppy_id'))
    puppy_adopter = relationship('PuppyAdopter', uselist=False, back_populates='adopter')

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://testdb:hello@localhost/production_dogshelter')

    # Creates tables in the database. If tables are already present, it won't recreate them.
    Base.metadata.create_all(engine)
    


