#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app import flask_app
from app.Utilities.util import test_db_string

import mock
import unittest
import pdb


class TestShowAllShelters(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    @mock.patch('app.Shelter.show_all_shelters.get_session')
    @mock.patch('app.Shelter.show_all_shelters.Shelter')
    def test_show_all_shelters_webpage(self, mock_shelter, mock_get_session):
        """ Checks if clicking on 'All Shelters' button navigates to
            show_all_shelter.html web page.
        """
        response = self.app.get('/show_all_shelters.html/')
        # pdb.set_trace()
        assert '<title>Show All Shelter</title>' in response.data
        self.assertEqual(200, response.status_code, 'Status code is not 200')
        assert mock_get_session.called_once_with(test_db_string)
        mock_session = mock_get_session.return_value
        mock_session.query.assert_called_once_with(mock_shelter)


if __name__ == '__main__':
    unittest.main()
