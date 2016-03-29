#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import flask_app
from app.Utilities.util import test_db_string, get_session
from app.database_setup import Shelter
import bleach

import pdb

from flask import render_template, request, redirect, url_for


@flask_app.route('/show_all_shelters/add_shelter', methods=['POST', 'GET'])
# @flask_app.route('/show_all_shelters/add_shelter.html', methods=['POST', 'GET'])
def add_shelter():
    if request.method == 'POST':
        # print 'I got POST response'  # protect code from sql and code injection
        name = bleach.clean(request.form['shelter_name'])
        street = bleach.clean(request.form['shelter_street'])
        city = bleach.clean(request.form['shelter_city'])
        state = bleach.clean(request.form['shelter_state'])
        zipcode = int(bleach.clean((request.form['shelter_zipcode'])))
        website = bleach.clean(request.form['shelter_website'])
        email = bleach.clean(request.form['shelter_email'])
        current_occupancy = int(bleach.clean(request.form['shelter_curroccupancy']))
        max_occupancy = int(bleach.clean(request.form['shelter_maxoccupancy']))
        shelter = Shelter(name, street, city, state, zipcode, website,
                          email, current_occupancy, max_occupancy)
        session = get_session(test_db_string)
        session.add(shelter)
        # Get that object
        session.commit()
        return redirect(url_for('show_all_shelters'))
    else:
        return render_template('add_shelter.html')
