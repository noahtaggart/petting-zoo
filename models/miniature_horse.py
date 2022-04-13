# import the python datetime module to help us create a timestamp
from datetime import date

class Miniature_Horse:
    def __init__(self, name, species, area, shift):
        self.name = name
        self.species = species
        self.area = area
        self.shift = shift
        self.walking = True
        self.date_added = date.today()