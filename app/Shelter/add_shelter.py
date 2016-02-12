#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from app import flask_app
from Utilities.util import production_db_string, test_db_string, get_session
from app.database_setup import Shelter

from flask import render_template


@flask_app.route('/show_all_shelter/add_shelter')
@flask_app.route('/show_all_shelter/add_shelter')
def add_shelter():
    # session = get_session(test_db_string)
    # session.connection()
    # shelter = Shelter('Hope for Paws', '2611 Monmouth Avenue',
    #                   'Los Angeles', 'CA', 94583, 'hopeforpaws.org',
    #                   'contact_us@hopeforpaws.org', 0, 10)
    # session.add(shelter)
    # session.commit()
    return render_template('add_shelter.html')
