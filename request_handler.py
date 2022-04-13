from models import Alpaca, Catfish, Cottonmouth, Goat, Koi, Llama, Longnose_Gar, Milksnake, Miniature_Horse, Plain_Bellied_Watersnake, Rough_Greensnake, Salmon, Scarletsnake, Sheep, Turtle
        
Pippo = Llama('Pippo', 'Domestic Llama', 'Petting area', 'morning shift' )
Obi = Goat('Obi', 'Domestic Goat', 'Petting area', 'morning shift' )
Zackariah = Sheep('Zackariah', 'Domestic Sheep', 'Petting area', 'midday shift' )
Nana = Alpaca('Nana', 'Domestic Alpaca', 'Petting area', 'evening shift' )
Carr = Miniature_Horse('Carr', 'Domestic Miniature Horse', 'Petting area', 'evening shift' )

Justus = Turtle('Justus', 'Domestic Turtle', 'Pond' )
Brody = Salmon('Brody', 'Domestic Salmon', 'Pond' )
Angelica = Catfish('Angelica', 'Domestic Catfish', 'Pond' )
Joscelin = Longnose_Gar('Joscelin', 'Domestic Longnose Gar', 'Pond' )
Lise = Koi('Lise', 'Domestic Koi', 'Pond' )

Malvina = Milksnake('Malvina', 'Domestic Milksnake', 'Glass Tank')
Phillida = Scarletsnake('Phillida', 'Domestic Scarletsnake', 'Glass Tank')
Konrad = Rough_Greensnake('Konrad', 'Domestic Rough Greensnake', 'Glass Tank')
Clovis = Cottonmouth('Clovis', 'Domestic Cottonmouth', 'Glass Tank')
Heath = Plain_Bellied_Watersnake('Heath', 'Domestic Plain Bellied Watersnake', 'Glass Tank')

print(f'{Obi.name} the {Obi.species} is in the {Obi.area} during the {Obi.shift}')