import numpy as np
import random





class menu(object):

    def __init__(self):  # Property
        self.__number = 0
        self.__players_name = []
        self.__bot = []
        self.__roles = []
    
    #Methodes
    def __aff_wel(self):  # Affichage du début
        print("+--------------------------------------------------------------------+")
        print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
        print("+--------------------------------------------------------------------+")

    def __get_number(self):  # Nombre de joueurs
        print("How many players?")
        etat = False
        while (etat == False):
            self.__number = input()
            if (len(self.__number)==1 or len(self.__number)==2):
                if (self.__number.isdecimal()==True):
                    self.__number=int(self.__number)
                    if (self.__number > 2 and self.__number < 11):
                        print("There is", self.__number, "players")
                        etat = True
                    else:
                        print("Please choose a number between 3 and 10")
                else:
                    print('Please write a correct number')
            else:
                print('Please write a number')


    def __players(self):  # Configuration des joueurs
        for k in range(self.__number):
            print('Please enter the name of player', k + 1 )
            print('')
            joueur = 0
            joueur = input()
            self.__players_name.append(joueur)
            print('The name of the player is:', self.__players_name[k])
            print('Please press 0 if the player is an AI and press 1 if the player is an Human')
            etat = False
            bot = []
            while (etat == False):
                bot = input()
                if (bot == '1'):
                    self.__bot.append("Human")
                    etat = True

                elif (bot == '0'):
                    self.__bot.append("AI")
                    etat = True
                else:
                    print("Please select 0 (AI) or 1 (Human):")
                    etat = False

    def __cartes_roles(self):  # Saboteur or Digger
        personnage=[]
        if (self.__number == 3):
            personnage = ['S', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 3)
        elif (self.__number == 4):
            personnage = ['S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 4)
        elif (self.__number == 5):
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 5)
        elif (self.__number == 6):
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 6)
        elif (self.__number == 7):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 7)
        elif (self.__number == 8):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 8)
        elif (self.__number == 9):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 9)
        elif (self.__number == 10):
            personnage = ['S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 10)

    def __affichage_debut_fin(self):
        total=[]
        for k in range (self.__number-1):
            total.append(self.__players_name[k] + '(' + self.__bot[k]+'),')
        total.append(self.__players_name[self.__number-1] + '(' + self.__bot[self.__number-1]+')')
        total = ' '.join(total)
        print('---------------------')
        print('The', self.__number, 'players are:', total)

    def start_game(self):
        self.__aff_wel() 
        self.__get_number() 
        self.__players() 
        self.__cartes_roles()
        self.__affichage_debut_fin()

    @property
    def number(self):
        return self.__number

    @property
    def players_name(self):
        return self.__players_name

    @property
    def bot(self):
        return self.__bot

    @property
    def roles(self):
        return self.__roles

    


