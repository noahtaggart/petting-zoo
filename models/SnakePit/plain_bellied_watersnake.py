from models import Animal, Slithering
# Designate Plain_Bellied_Watersnake as a child class by adding (Animal) after the class name
class Plain_Bellied_Watersnake(Animal, Slithering):

    # Remove redundant properties from Plain_Bellied_Watersnake's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
