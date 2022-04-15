# import the python datetime module to help us create a timestamp
from datetime import date
        
class Goat:
    def __init__(self, name, species, area, shift, food, chip_num):
        self.name = name
        self.species = species
        self.area = area
        self.shift = shift
        self.food = food
        self.__chip_num = chip_num
        self.walking = True
        self.date_added = date.today()
        
    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"
    
    @property 
    def chip_num(self):
        return self.__chip_num
    
    @chip_num.setter
    def chip_num(self, number):
        pass