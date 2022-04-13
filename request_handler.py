from models import Alpaca, Catfish, Cottonmouth, Goat, Koi, Llama, Longnose_Gar, Milksnake, Miniature_Horse, Plain_Bellied_Watersnake, Rough_Greensnake, Salmon, Scarletsnake, Sheep, Turtle
        
Pippo = Llama('Pippo', 'Domestic Llama', 'Petting area', 'morning shift', 'Llama Food' )
Obi = Goat('Obi', 'Domestic Goat', 'Petting area', 'morning shift', 'Goat Chow' )
Zackariah = Sheep('Zackariah', 'Domestic Sheep', 'Petting area', 'midday shift', "Shepherds Pie" )
Nana = Alpaca('Nana', 'Domestic Alpaca', 'Petting area', 'evening shift', "Alpaca Cracka" )
Carr = Miniature_Horse('Carr', 'Domestic Miniature Horse', 'Petting area', 'evening shift', "Horse D'oeuvres" )

Justus = Turtle('Justus', 'Domestic Turtle', 'Pond', "Turtle Tracks" )
Brody = Salmon('Brody', 'Domestic Salmon', 'Pond', "Salmon Snacks" )
Angelica = Catfish('Angelica', 'Domestic Catfish', 'Pond', "Meowmix" )
Joscelin = Longnose_Gar('Joscelin', 'Domestic Longnose Gar', 'Pond', "GAR-lic Bread" )
Lise = Koi('Lise', 'Domestic Koi', 'Pond', "Koi Beans" )

Malvina = Milksnake('Malvina', 'Domestic Milksnake', 'Glass Tank', "Milksnake boiled over hard with a side of the finest Jelly Beans, served raw")
Phillida = Scarletsnake('Phillida', 'Domestic Scarletsnake', 'Glass Tank', "Scarlet Velvet Cake")
Konrad = Rough_Greensnake('Konrad', 'Domestic Rough Greensnake', 'Glass Tank', "Smooth Redcake")
Clovis = Cottonmouth('Clovis', 'Domestic Cottonmouth', 'Glass Tank', "Cotton Candy")
Heath = Plain_Bellied_Watersnake('Heath', 'Domestic Plain Bellied Watersnake', 'Glass Tank', "toast")

print(Obi.feed())
print(f'{Obi.name} the {Obi.species} is in the {Obi.area} during the {Obi.shift}')

print(Obi)
