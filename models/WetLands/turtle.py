from models import Animal, Swimming, Walking
# Designate Turtle as a child class by adding (Animal) after the class name
class Turtle(Animal, Swimming, Walking):

    # Remove redundant properties from Turtle's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
