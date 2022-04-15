from models import Animal, Walking
# Designate Sheep as a child class by adding (Animal) after the class name
class Sheep(Animal, Walking):

    # Remove redundant properties from Sheep's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift # stays on Sheep because not all animals have shifts
        Walking.__init__(self)