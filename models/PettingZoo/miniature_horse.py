from models import Animal
# Designate Miniature_Horse as a child class by adding (Animal) after the class name
class Miniature_Horse(Animal):

    # Remove redundant properties from Miniature_Horse's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Miniature_Horse because not all animals have shifts
        self.walking = True