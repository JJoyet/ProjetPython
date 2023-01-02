import numpy as np
import random 

from .deck import Deck
from .menu import Menu
from .player import Player
from .hand import Hand
from .card import Carte
from .board import Plateau
from .human import Human






class SABOOTERS(object):
    def __init__(self):
        self.__menu=Menu()
        self.__deck=Deck()
        self.__pioche=[]
        self.__defausse=[]
        self.__joueurs=[]
        self.__plateau=Plateau()

    def __initpartie(self):
        #initialisation du menu
        self.__menu.start_game()

        #initialisation des joueurs
        for i in range(0,self.__menu.number):
            self.__joueurs.append(Human(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))


    def __initmanche(self):
        #initialisation de la manche

        #On melange les cartes
        self.__deck.random_cartes()

        #On defini les positions des cartes "END"
        set_pos_gold=random.sample([[0,2],[2,2],[4,2]], 3)

        #repartition des cartes
        k=0
        for i in range(0,len(self.__deck.cartes)):
            #On place les cartes arrive/depart sur le plateau
            if self.__deck.cartes[i].typ == 3 or self.__deck.cartes[i].typ == 4 or self.__deck.cartes[i].typ == 5:
                if self.__deck.cartes[i].typ==3:
                    self.__plateau.add_carte(self.__deck.cartes[i],[2,0],1)
                else:
                    self.__plateau.add_carte(self.__deck.cartes[i],set_pos_gold[k],1)
                    k=k+1
            #On cree la pioche avec les cartes action et chemin
            else :
                self.__pioche.append(self.__deck.cartes[i])
        
        #Les joueurs piochent leurs cartes
        for i in range(self.__menu.number):
            for j in range(self.__joueurs[i].hand.hand_size):
                self.__joueurs[i].piocher_carte(self.__pioche)

    def __manche(self):
        #On initialise la manche
        self.__initmanche()


        #Variable permettant de déterminer si les joueurs ont encore des cartes en main
        nb_card_player=0

        #Variable permettant de déterminer si l'or a été trouvé
        gold_found=0

        #Compteur de carte
        nb_card_player=1
        
        #Tant que l'or n'est pas trouvé et qu'il y a toujours des cartes en main
        while nb_card_player!=0 and gold_found==0 :
            nb_card_player=0
            #On parcour les joueurs
            for joueur in self.__joueurs:
                #Tour du joueur
                joueur.tourjoueur(self.__plateau,self.__pioche,self.__defausse,self.__joueurs)
                #On compte les cartes
                nb_card_player= nb_card_player + len(joueur.hand.cards)
                #On verifie si l'or a été trouvé
                gold_found=self.__plateau.gold_found
                #Si l'or a été trouvé c'est la fin de la manche, les mineurs gagne
                if gold_found==1:
                    #self.__menu.fin_de_manche(joueur.name,self.joueurs)
                    break
        #Si l'or n'a pas été trouvé les sabooters gagne
        if gold_found==0: pass
            #self.__menu.fin_de_manche("SABOOTERS",self.joueurs)

        #On vide la pioche et la defausse
        self.__pioche=[]
        self.__defausse=[]

        #On enlève les cartes du plateau
        self.__plateau.reset_plateau()
        


    def start_game(self):
        #On initialise la partie
        self.__initpartie()

        #La partie se déroule en trois manches
        for i in range(3):
            #On affiche sur le plateau à quelle manche on est
            self.__plateau.no_manche=i+1
            #Une manche se déroule
            self.__manche()
        
            
            



    # def tour_pour_rien(self):
    #     for i in range(3):
    #         self.__joueurs[0].tourjoueur(self.__plateau, self.__pioche, self.__defausse)
        
