from models import PettingZoo, SnakePit, Wetlands
from animals import Obi, Pippo, Zackariah, Nana, stinky, Carr, Malvina, Phillida, Konrad, Clovis, Heath, Justus, Brody, Angelica, Joscelin, Lise, Bob, Snappy

varmint_village = PettingZoo("Varmint Village", "cute, cuddly creatures")

varmint_village.add_animal_type_check(Obi)
varmint_village.add_animal_type_check(Pippo)
varmint_village.add_animal_type_check(Zackariah)
varmint_village.add_animal_type_check(Nana)
varmint_village.add_animal_type_check(stinky)
varmint_village.add_animal_type_check(Carr)
varmint_village.add_animal_type_check(Bob)


slither_inn = SnakePit("Slither Inn", "slimy, slithery, scary snakes")

slither_inn.add_animal_type_check(Malvina)
slither_inn.add_animal_type_check(Phillida)
slither_inn.add_animal_type_check(Konrad)
slither_inn.add_animal_type_check(Clovis)
slither_inn.add_animal_type_check(Heath)

dire_dire_docks = Wetlands("Dire, Dire Docks", "scaley, swift swimming specimens")

dire_dire_docks.add_animal_type_check(Justus)
dire_dire_docks.add_animal_type_check(Brody)
dire_dire_docks.add_animal_type_check(Angelica)
dire_dire_docks.add_animal_type_check(Joscelin)
dire_dire_docks.add_animal_type_check(Lise)







