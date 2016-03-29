#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import flask_app
from app.Utilities.util import get_session, test_db_string
from app.database_setup import Shelter

import pdb

from flask import render_template, request, redirect, url_for


@flask_app.route('/show_all_shelters/<int:shelter_id>', methods=['GET', 'POST', 'DELETE'])
def show_shelter_details(shelter_id):
    if request.method == 'GET':
        pdb.set_trace()
        session = get_session(test_db_string)
        shelter = session.query(Shelter).filter_by(shelter_id=shelter_id).one()
        if shelter is not None:
            render_template('editdelete_shelter.html', hasValue=True,
                            shelter=shelter)
        else:
            render_template('editdelete_shelter.html', hasValue=False)

    if request.method == 'POST':        # edit
        pass

    if request.method == 'DELETE':
        pass
