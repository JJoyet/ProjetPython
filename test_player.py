from classes import Player
from classes import Carte
from classes import Plateau
from classes import Human

p=Human("Julien","S",3)
pioche=[]
pioche.append(Carte(0))
pioche.append(Carte(0))
pioche.append(Carte(0))

p.piocher_carte(pioche)
p.piocher_carte(pioche)
p.piocher_carte(pioche)

pl=Plateau()
choix=p.choix_action(pl)