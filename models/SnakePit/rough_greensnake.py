# import the python datetime module to help us create a timestamp
from datetime import date

class Rough_Greensnake:
    def __init__(self, name, species, area, food):
        self.name = name
        self.species = species
        self.area = area
        self.food = food
        self.slithering = True
        self.date_added = date.today()
    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"