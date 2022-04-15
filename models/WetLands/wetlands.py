class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "scaley, swift swimming, specimens"
        self.animals = list()
    
    def addList(self, animal):
        self.animals.append(animal)
        
    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'