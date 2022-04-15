from models import Animal
# Designate Goat as a child class by adding (Animal) after the class name
class Goat(Animal):

    # Remove redundant properties from Goat's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Goat because not all animals have shifts
        self.walking = True