from models import Animal
# Designate Milksnake as a child class by adding (Animal) after the class name
class Milksnake(Animal):

    # Remove redundant properties from Milksnake's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
