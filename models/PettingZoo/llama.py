from datetime import date
class Llama:

    def __init__(self, name, species, area, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.area = area
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}"