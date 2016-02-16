#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from app.database_setup import Shelter, Puppy, Adopter, PuppyAdopter
import unittest

import pdb
from app.Utilities.util import get_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class TestDatabaseSetup(unittest.TestCase):
    def get_test_session(self):
        Base = declarative_base()
        engine = create_engine(self.test_connection_string)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session

    def setUp(self):
        self.test_connection_string = 'postgresql+psycopg2://testdb:' \
                                      'hello@localhost/test_dogshelter'
        self.test_session = self.get_test_session()

    def test_check_table_names(self):
        my_tables = set()
        my_tables.add('shelter')
        my_tables.add('puppy')
        my_tables.add('adopter')
        my_tables.add('puppy_adopter')

        Base = declarative_base()
        engine = create_engine(self.test_connection_string)
        Base.metadata.bind = engine
        tables = engine.table_names()
        # pdb.set_trace()
        for table in tables:
            my_tables.remove(table)

        self.assertEqual(my_tables.__len__(), 0,
                         'All tables were not found')

        # test table columns
        # test shelter columns

    def test_table_shelter(self):
        # pdb.set_trace()
        columns = Shelter.__table__.columns
        my_columns = set()
        my_columns.add('shelter_id')
        my_columns.add('name')
        my_columns.add('street')
        my_columns.add('city')
        my_columns.add('state')
        my_columns.add('zipcode')
        my_columns.add('website')
        my_columns.add('email')
        my_columns.add('current_occupancy')
        my_columns.add('maximum_occupancy')
        for column in columns:
            my_columns.remove(column.key)

        # my_columns should be empty
        self.assertEqual(my_columns.__len__(), 0, 'Shelter Table columns not '
                                                  ' properly created')

    def test_table_puppy(self):
        columns = Puppy.__table__.columns
        my_columns = set()
        my_columns.add('puppy_id')
        my_columns.add('name')
        my_columns.add('date_of_birth')
        my_columns.add('breed')
        my_columns.add('gender')
        my_columns.add('age')
        my_columns.add('picture')
        my_columns.add('shelter_id')
        for column in columns:
            my_columns.remove(column.key)

        # my_columns should be empty
        self.assertEqual(my_columns.__len__(), 0, 'Puppy table not properly '
                                                  'created')

    def test_puppy_adopter_table(self):
        # pdb.set_trace()
        columns = PuppyAdopter.__table__.columns
        my_columns = set()
        my_columns.add('serial_no')
        my_columns.add('puppy_id')
        my_columns.add('adopter_id')
        for column in columns:
            my_columns.remove(column.key)
        # my_columns should be empty
        self.assertEqual(my_columns.__len__(), 0, 'Puppy Adopter table '
                                                  'not properly created')

    def test_adopter_table(self):
        columns = Adopter.__table__.columns
        my_columns = set()
        my_columns.add('adopter_id')
        my_columns.add('adopter_name')
        my_columns.add('adopter_phone')
        my_columns.add('street')
        my_columns.add('city')
        my_columns.add('state')
        my_columns.add('zipcode')
        my_columns.add('puppy_id')
        for column in columns:
            my_columns.remove(column.key)
        # my_columns should be empty
        self.assertEqual(my_columns.__len__(), 0, 'Adopter table not '
                                                  'properly created')

if __name__ == '__main__':
    unittest.main()






