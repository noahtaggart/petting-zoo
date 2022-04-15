from areas import varmint_village, slither_inn, dire_dire_docks
from animals import Obi


areaList = []
areaList.append(varmint_village)
areaList.append(slither_inn)
areaList.append(dire_dire_docks)

Obi.chip_num = 12345
print(Obi.chip_num)

print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(dire_dire_docks.last_critter_added)

for area in areaList:
    print(f"{area.attraction_name} is where you'll find {area.description} like")
    for animal in area.animals:
        print(f"    • {animal.name} the {animal.species}")