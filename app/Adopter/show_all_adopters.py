#!/usr/bin/python
# -*- coding:utf-8 -*-

from app import flask_app
from flask import render_template


@flask_app.route('/show_all_adopters')
@flask_app.route('/show_all_adopters.html')
def show_all_adopters():
    return render_template('show_all_adopters.html')

