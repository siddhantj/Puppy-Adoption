#!/usr/bin/python
# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError, ArgumentError

production_db_string = 'postgresql+psycopg2://testdb:hello@localhost/' \
                       'production_dogshelter'
test_db_string = 'postgresql+psycopg2://testdb:hello@localhost/' \
                       'test_dogshelter'


def get_session(database_connection_string):
    try:
        Base = declarative_base()
        engine = create_engine(database_connection_string)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        connection = session.connection()
        return session
    except OperationalError:
        return None
    except ArgumentError:
        return None

if __name__ == '__main__':
    get_session(production_db_string)
