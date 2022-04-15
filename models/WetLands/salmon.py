from models import Animal, Swimming
# Designate Salmon as a child class by adding (Animal) after the class name
class Salmon(Animal, Swimming):

    # Remove redundant properties from Salmon's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
