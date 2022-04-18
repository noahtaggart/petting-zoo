from areas import varmint_village, slither_inn, dire_dire_docks
from animals import Obi, Bob, Snappy

print(Obi.feed())
print(Bob.feed())
varmint_village.add_animal(Snappy)
varmint_village.add_animal_type_check(Snappy)

Bob.run()
Bob.swim()


areaList = []
areaList.append(varmint_village)
areaList.append(slither_inn)
areaList.append(dire_dire_docks)


print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(dire_dire_docks.last_critter_added)

for area in areaList:
    print(f"{area.attraction_name} is where you'll find {area.description} like")
    for animal in area.animals:
        print(f"    • {animal.name} the {animal.species}")
        
for animal in varmint_village.animals:
    print(animal)
