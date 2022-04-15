from models import Animal
# Designate Llama as a child class by adding (Animal) after the class name
class Alpaca(Animal):

    # Remove redundant properties from Alpaca's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, shift, food, chip_num)
        self.shift = shift # stays on Alpaca because not all animals have shifts
        self.walking = True