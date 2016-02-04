#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from app import flask_app


@flask_app.route('/')
@flask_app.route('/index.html', methods=['GET'])
def welcome_page():
    # pdb.set_trace()
    return render_template('index.html')

