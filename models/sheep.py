from datetime import date

class Sheep:
    def __init__(self, name, species, area, shift, food):
        self.name = name
        self.species = species
        self.area = area
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()
        
    def feed(self):
        return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"