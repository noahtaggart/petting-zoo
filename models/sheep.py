from datetime import date

class Sheep:
    def __init__(self, name, species, area, shift):
        self.name = name
        self.species = species
        self.area = area
        self.shift = shift
        self.walking = True
        self.date_added = date.today()