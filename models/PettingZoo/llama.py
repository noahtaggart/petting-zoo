from datetime import date

from models import Animal, Walking

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal, Walking):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        Walking.__init__(self)
        
    def feed(self):
        return (f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')