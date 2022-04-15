from models import Animal
# Designate Scarletsnake as a child class by adding (Animal) after the class name
class Scarletsnake(Animal):

    # Remove redundant properties from Scarletsnake's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
