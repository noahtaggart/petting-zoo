from models import Animal, Slithering
# Designate Rough_Greensnake as a child class by adding (Animal) after the class name
class Rough_Greensnake(Animal, Slithering):

    # Remove redundant properties from Rough_Greensnake's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
