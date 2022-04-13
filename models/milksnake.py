# import the python datetime module to help us create a timestamp
from datetime import date

class Milksnake:
    def __init__(self, name, species, area):
        self.name = name
        self.species = species
        self.area = area
        self.slithering = True
        self.date_added = date.today()