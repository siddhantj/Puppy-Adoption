#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Utilities.util import database_connection_string
from app.database_setup import Shelter

import pdb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from flask import render_template
from app import flask_app


def get_session():
    Base = declarative_base()
    engine = create_engine(database_connection_string)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


@flask_app.route('/show_all_shelters')
@flask_app.route('/show_all_shelters.html')
def show_all_shelters():
    # pdb.set_trace()
    session = get_session()
    shelters = session.query(Shelter).all()
    if shelters.__len__() != 0:
        return render_template('show_all_shelters.html', result='Yes', shelters=shelters)
    else:
        return render_template('show_all_shelter.html', result='No')


def add_shelter():
    session = get_session()
    session.connection()
    shelter = Shelter('Hope for Paws', '2611 Monmouth Avenue',
                      'Los Angeles', 'CA', 94583, 'hopeforpaws.org',
                      'contact_us@hopeforpaws.org', 0, 10)
    session.add(shelter)
    session.commit()