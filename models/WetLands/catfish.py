from models import Animal, Swimming

# Designate Catfish as a child class by adding (Animal) after the class name
class Catfish(Animal, Swimming):

    # Remove redundant properties from Catfish's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
