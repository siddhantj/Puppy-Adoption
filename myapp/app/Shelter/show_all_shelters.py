#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import render_template
from myapp import app


@app.route('/show_all_shelters')
@app.route('/show_all_shelters.html')
def show_all_shelters():
    return render_template('show_all_shelters.html')
