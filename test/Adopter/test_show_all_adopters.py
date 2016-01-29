#!/usr/bin/python
# -*- coding:utf-8 -*-


import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app import flask_app


class TestShowAllAdopters(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.test_client()
        flask_app.debug = True

    def test_show_all_adopter_webpage(self):
        """ Check contents of show_all_adopters.html webpage """
        response = self.app.get('/show_all_adopters.html')
        assert 'Show all adopters' in response.data
        self.assertEqual(200, response.status_code, 'Status code is not 200')
