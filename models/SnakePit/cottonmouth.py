from models import Animal, Slithering
# Designate Cottonmouth as a child class by adding (Animal) after the class name
class Cottonmouth(Animal):

    # Remove redundant properties from Cottonmouth's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
