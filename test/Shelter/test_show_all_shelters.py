#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app import flask_app

import unittest


class TestShowAllShelters(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_show_all_shelters_webpage(self):
        """ Checks if clicking on 'All Shelters' button navigates to
            show_all_shelter.html web page.
        """
        response = self.app.get('/show_all_shelters.html')
        assert 'Show all shelters' in response.data
        self.assertEqual(200, response.status_code, 'Status code is not 200')
