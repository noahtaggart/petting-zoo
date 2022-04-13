# import the python datetime module to help us create a timestamp
from datetime import date

class Turtle:
    def __init__(self, name, species, area):
        self.name = name
        self.species = species
        self.area = area
        self.walking = True
        self.swimming = True
        self.date_added = date.today()