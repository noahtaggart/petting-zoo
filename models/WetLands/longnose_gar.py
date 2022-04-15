from models import Animal
# Designate Longnose_Gar as a child class by adding (Animal) after the class name
class Longnose_Gar(Animal):

    # Remove redundant properties from Longnose_Gar's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
