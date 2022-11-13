import random
import numpy as np


class Menu:
    import random

    def aff_wel(self):  # Affichage du début
        print("+--------------------------------------------------------------------+")
        print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
        print("+--------------------------------------------------------------------+")

    def __init__(self):  # Property
        self.number = 0
        self.personnage = []
        self.total_personnage = []
        self.total_nom=[]
        self.joueur = []
        self.bot = []
        self.total = []
        self.total_bot = []

    def get_number(self):  # Nombre de joueurs
        print("How many players?")

        etat = False
        while (etat == False):
            self.number = input()
            if (len(self.number)==1 or len(self.number)==2):
                if (self.number.isdecimal()==True):
                    self.number=int(self.number)
                    if (self.number > 2 and self.number < 11):
                        print("There is", self.number, "players")
                        etat = True
                    else:
                        print("Please choose a number between 3 and 10")
                else:
                    print('Please write a correct number')
            else:
                print('Please write a number')


    def players(self):  # Configuration des joueurs
        for k in range(self.number):
            print('Please enter the name of player', k + 1 )
            print('')
            self.joueur = input()
            self.total_nom.append(self.joueur)
            print('The name of the player is:', self.total_nom[k])
            print('Please press 0 if the player is an IA and press 1 if the player is an Human')
            etat = False
            while (etat == False):
                self.bot = input()
                if (self.bot == '1'):
                    self.total_bot.append("Human")
                    etat = True

                elif (self.bot == '0'):
                    self.total_bot.append("IA")
                    etat = True
                else:
                    print("Veuillez saisir 0 (IA) ou 1 (Human):")
                    etat = False

    def cartes_roles(self):  # Saboteur ou Mineur
        if (self.number == 3):
            self.personnage = ['S', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 3)
        elif (self.number == 4):
            self.personnage = ['S', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 4)
        elif (self.number == 5):
            self.personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 5)
        elif (self.number == 6):
            self.personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 6)
        elif (self.number == 7):
            self.personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 7)
        elif (self.number == 8):
            self.personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 8)
        elif (self.number == 9):
            self.personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 9)
        elif (self.number == 10):
            self.personnage = ['S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.total_personnage = self.random.sample(self.personnage, 10)
            print(self.random.sample(self.personnage, 10))

    def affichage_debut_fin(self):
        for k in range (self.number):
            self.total.append(self.total_nom[k] + ',(' + self.total_bot[k]+')')
        self.total = ' '.join(self.total)
        print('---------------------')
        print('The', self.number, 'players are:', self.total)
menu = Menu()
menu.aff_wel()
menu.get_number()
menu.players()
menu.affichage_debut_fin()
