from models import Animal, Swimming, Walking
# from models.Movements.swimming import Swimming
# from models.Movements.walking import Walking

class Goose(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        self.shift = shift
        Walking.__init__(self)
        Swimming.__init__(self)

        
    def honk(self):
        return f"The goose honks. A lot."
    
    def run(self):
        print(f"{self} waddles")
    
    def __str__(self):
        return f'{self.name} the Goose'