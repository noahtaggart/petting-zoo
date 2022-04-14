class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slimy, slithery, and bitey things"
        self.animals = list()
    
    def addList(self, animal):
        self.animals.append(animal)