#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
flask_app = Flask(__name__)  # Always in this order otherwise app won't be imported

# import sys
# sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/app')

# sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/app/Shelter')

# sys.path.append('/home/siddhant/PycharmProjects/DogShelter/myapp/app/Puppy')


import app.main
import app.Shelter.show_all_shelters
import app.Puppy.show_all_puppies
import app.Adopter.show_all_adopters