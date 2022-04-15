from models import Animal
# Designate Plain_Bellied_Watersnake as a child class by adding (Animal) after the class name
class Plain_Bellied_Watersnake(Animal):

    # Remove redundant properties from Plain_Bellied_Watersnake's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
