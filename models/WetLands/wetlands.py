from models import Attraction, Swimming

class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
        
    def add_animal_type_check(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.attraction_name} attraction.')    
        