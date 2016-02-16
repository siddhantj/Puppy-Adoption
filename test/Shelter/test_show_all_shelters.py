#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app import flask_app
from app.database_setup import Shelter
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Utilities.my_utils import get_test_session


import unittest
import pdb


class TestShowAllShelters(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True
        self.session = get_test_session
        self.shelter1 = Shelter('name1', 'street1', 'city1', 'state1', 00000,
                                'website1', 'email1', 0, 5)
        self.shelter2 = Shelter('name2', 'street2', 'city2', 'state2', 00001,
                                'website2', 'email2', 0, 5)

    def test_show_all_shelters_webpage(self):
        """ Checks if clicking on 'All Shelters' button navigates to
            show_all_shelter.html web page.
        """
        # response = self.app.get('/show_all_shelters.html/')
        # pdb.set_trace()
        # assert '<title>Show All Shelter</title>' in response.data
        # self.assertEqual(200, response.status_code, 'Status code is not 200')
        pass


if __name__ == '__main__':
    unittest.main()
