from models import Animal
# Designate Salmon as a child class by adding (Animal) after the class name
class Salmon(Animal):

    # Remove redundant properties from Salmon's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
