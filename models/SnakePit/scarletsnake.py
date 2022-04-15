from models import Animal, Slithering
# Designate Scarletsnake as a child class by adding (Animal) after the class name
class Scarletsnake(Animal, Slithering):

    # Remove redundant properties from Scarletsnake's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
