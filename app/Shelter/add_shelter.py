#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import flask_app
from app.Utilities.util import test_db_string, get_session
from app.database_setup import Shelter

import pdb

from flask import render_template, request, redirect, url_for


@flask_app.route('/show_all_shelters/add_shelter', methods=['POST', 'GET'])
@flask_app.route('/show_all_shelters/add_shelter', methods=['POST', 'GET'])
def add_shelter():
    if request.method == 'POST':
        # pdb.set_trace()
        print 'I got POST response'  # protect code from sql and code injection
        name = request.form['shelter_name']
        street = request.form['shelter_street']
        city = request.form['shelter_city']
        state = request.form['shelter_state']
        zipcode = int(request.form['shelter_zipcode'])
        website = request.form['shelter_website']
        email = request.form['shelter_email']
        current_occupancy = int(request.form['shelter_curroccupancy'])
        max_occupancy = int(request.form['shelter_maxoccupancy'])
        shelter = Shelter(name, street, city, state, zipcode, website,
                          email, current_occupancy, max_occupancy)
        session = get_session(test_db_string)
        session.add(shelter)
        # Get that object
        shelters = session.query(Shelter).all()
        for ind_shelter in shelters:
            print "%s %s" % (ind_shelter.name, ind_shelter.street)
        # session.commit()
        return redirect(url_for('show_all_shelters'))
    else:
        return render_template('add_shelter.html')
