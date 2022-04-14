from areas import varmint_village, slither_inn, dire_dire_docks

areaList = []
areaList.append(varmint_village)
areaList.append(slither_inn)
areaList.append(dire_dire_docks)

for area in areaList:
    print(f"{area.attraction_name} is where you'll find {area.description} like")
    for animal in area.animals:
        print(f"    • {animal.name} the {animal.species}")