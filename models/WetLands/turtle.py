from models import Animal
# Designate Turtle as a child class by adding (Animal) after the class name
class Turtle(Animal):

    # Remove redundant properties from Turtle's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
        self.walking = True
