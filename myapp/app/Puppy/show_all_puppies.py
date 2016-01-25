#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from myapp import app


@app.route('/show_all_puppies')
@app.route('/show_all_puppies.html')
def show_all_puppies():
    return render_template('show_all_puppies.html')
