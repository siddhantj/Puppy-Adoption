#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from app import flask_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


@flask_app.route('/')
@flask_app.route('/index.html', methods=['GET'])
def welcome_page():
    # pdb.set_trace()
    return render_template('index.html')


