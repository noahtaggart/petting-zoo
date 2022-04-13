from datetime import date
class Llama:

    def __init__(self, name, species, area, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.area = area
        self.shift = shift
        self.walking = True
        self.date_added = date.today()