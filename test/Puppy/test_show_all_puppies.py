#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app import flask_app

import unittest


class TestShowAllPuppies(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.test_client()
        flask_app.debug = True

    def test_show_all_puppies_webpage(self):
        """ Check contents of show_all_puppies.html webpage """
        response = self.app.get('/show_all_puppies.html')
        assert 'Show all puppies' in response.data
        self.assertEqual(200, response.status_code, 'Status code is not 200')
