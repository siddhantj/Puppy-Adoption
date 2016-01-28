#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
from os import path

import sys
import os.path
# from os import path
# sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app import flask_app


class TestMain(unittest.TestCase):
    def setUp(self):
        print __file__
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_welcome_page_root(self):
        """ Test the contents of webpage on root directory is accessed """
        #pdb.set_trace()
        response = self.app.get('/')
        assert '<h1> Hello World</h1>' in response.data
        self.assertEqual(200, response.status_code, 'Status code is not 200')

    def test_welcome_page_index_file(self):
        """ Test the contents of webpage when main page is accessed """
        response = self.app.get('/index.html')
        assert '<h1> Hello World</h1>' in response.data
        self.assertEqual(response.status_code, 'Status code is not 200')

    def test_server_up_on_correct_ip_correct_port(self):
        """ Test server is running on designated IP and port number"""
        (host, port) = main.get_connection_info()
        self.assertEqual(host, '0.0.0.0', 'Invalid IP address.')
        self.assertEqual(port, 5000, 'Invalid port number.')

    def test_show_all_shelters_webpage(self):
        """ Checks if clicking on 'All Shelters' button navigates to
            show_all_shelter.html web page.
        """
        response = self.app.get('/show_all_shelters.html')
        assert 'All shelters webpage' in response.data
        self.assertEqual(response.status_code, 'Status code is not 200')

    def test_show_all_puppies_webpage(self):
        """ Check contents of show_all_puppies.html webpage """
        response = self.app.get('/show_all_puppies.html')
        assert 'All puppies webpage' in response.data
        self.assertEqual(response.status_code, 'Status code is not 200')

    def test_show_all_adopter_webpage(self):
        """ Check contents of show_all_adopters.html webpage """
        response = self.app.get('/show_all_adopters.html')
        assert 'All adopters webpage' in response.data
        self.assertEqual(response.status_code, 'Status code is not 200')


if __name__ == '__main__':
    unittest.main()


