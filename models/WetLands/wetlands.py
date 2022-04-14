class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Some fish are minnows, Some are whales. People like dimples, Fish like scales. Some fish are slim, And some are round. They don’t get cold, They don’t get drowned. But every fish wife Fears for her fish. What we call mermaids And they call merfish. "
        self.animals = list()
    
    def addList(self, animal):
        self.animals.append(animal)