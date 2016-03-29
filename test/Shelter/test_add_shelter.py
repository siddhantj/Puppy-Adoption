#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app import flask_app

import unittest
import mock
import pdb
from flask import request


class TestAddShelter(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    @mock.patch('app.Shelter.add_shelter.get_session')  # TODO: Not working
    @mock.patch('app.Shelter.add_shelter.Shelter')
    @mock.patch('app.Shelter.add_shelter.test_db_string')
    def test_add_shelter(self, mock_db_string, mock_shelter, mock_get_session):
        response = self.app.post('/show_all_shelters/add_shelter',
                                 data=dict(shelter_name='s_name',
                                           shelter_street='s_street',
                                           shelter_city='s_city',
                                           shelter_state='state',
                                           shelter_zipcode=0,
                                           shelter_website='s_website',
                                           shelter_email='s_email',
                                           shelter_curroccupancy=0,
                                           shelter_maxoccupancy=2))
        pdb.set_trace()
        # assert 'add_shelter.html' in response.data
        self.assertEqual(200, response.status_code, 'Response code not equal')
        mock_shelter_retval = mock_shelter.return_value
        mock_get_session.assert_called_once_with(mock_db_string)
        mock_get_session.return_value.add.called_once_with(mock_shelter_retval)


if __name__ == '__main__':
    unittest.main()
