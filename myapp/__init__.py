#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)  # Always in this order otherwise app won't be imported

import sys
sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/app')
import main

sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/app/Shelter')
import show_all_shelters

sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/app/Puppy')
import show_all_puppies

sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/test')
import test_main


