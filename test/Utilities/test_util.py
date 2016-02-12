#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from app.Utilities.util import get_session

import mock
import unittest
from mock import sentinel

from sqlalchemy.exc import OperationalError, ArgumentError


class TestUtilMock(unittest.TestCase):
    @mock.patch('app.Utilities.util.create_engine')  # mention the whole path
    @mock.patch('app.Utilities.util.sessionmaker')
    @mock.patch('app.Utilities.util.declarative_base')
    def test_get_session1(self, mock_delarative_base, mock_sessionmaker,
                         mock_create_engine):
        # mock_create_engine.return_value = sentinel.engine
        # instance = mock_create_engine.return_value
        # get_session('any_path')
        # mock_delarative_base.called
        # mock_create_engine.assert_called_once_with('any_path')
        # mock_sessionmaker.assert_called_once_with(sentinel.engine)
        pass


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.valid_connection_str = 'postgresql+psycopg2://testdb:hello@' \
                                       'localhost/production_dogshelter'
        self.invalid_connection_str = 'postgresql+psycopg2://testdb:hello@' \
                                       'localhost/no_database'
        self.unparsable_db_str = 'invalid_db_str'

    def test_get_session(self):
        self.assertRaises(OperationalError, get_session(
            self.invalid_connection_str))
        self.assertRaises(ArgumentError, get_session(self.unparsable_db_str))
        self.assertIsNotNone(get_session(self.valid_connection_str),
                             'Session object cannot be None')
