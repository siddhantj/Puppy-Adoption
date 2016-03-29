#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import flask_app
from app.Utilities.util import test_db_string, get_session
from app.database_setup import Shelter

import pdb

from flask import render_template


@flask_app.route('/show_all_shelters/')
# @flask_app.route('/show_all_shelters.html/')
def show_all_shelters():
    # pdb.set_trace()
    # shelters = get_all_shelters()
    session = get_session(test_db_string)
    shelters = session.query(Shelter).all()
    if shelters.__len__() != 0:
        return render_template('show_all_shelters.html', result='Yes', shelters=shelters)
    else:
        return render_template('show_all_shelters.html', result='No')

