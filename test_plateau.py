from classes import Plateau
from classes import Carte

p=Plateau()
c=Carte(0)
p.add_carte(c, [-7,-10])
p.reset_plateau()

p.affiche()