#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from app import flask_app


@flask_app.route('/show_all_puppies')
@flask_app.route('/show_all_puppies.html')
def show_all_puppies():
    return render_template('show_all_puppies.html')
