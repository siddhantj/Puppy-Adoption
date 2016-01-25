import sys
sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/Shelter')
from show_all_shelters import show_all_shelters

import unittest
import pdb

class TestShowAllShelter(unittest.TestCase):

    def setUp(self):
        self.app = show_all_shelters.app.test_client()
        self.app.testing = True

    def test_show_all_shelter(self):
        """ Test contents of show_all_shelter_webpage """
        response = self.app.get('/show_all_shelter')
        assert 'Show all shelters' in response.data
        self.assertEqual(200, response.status_code, 'Status code is not 200')
