import random
import numpy as np
class Menu():
    import random

    def aff_wel():
        print("+--------------------------------------------------------------------+")
        print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
        print("+--------------------------------------------------------------------+")

    def __init__(self):
        self.number=0
        self.personnage=[]
        self.total_personnage=[]
        self.joueur=[]
        self.bot=[]
        self.total=[]
    def get_number(self):
        print("How many players?")
        etat=False
        while (etat==False):
            self.number = int(input())
            if (self.number >2 and self.number<11):
                print("There is", self.number, "players")
                etat=True
            else:
                print("Please choose a number between 3 and 10")
                etat=False
    def players(self):
        for k in range(self.number):
            print('Please enter the name of player',k+1,' and its status (IA: 0, Human: 1):')
            print('')
            self.joueur=input()
            self.total.append('self.joueur')
            print('The name of the player is:',self.joueur[k])
            print('Press 0 if the player is an IA and Press 1 if the player is an Human')
            self.bot=int(input())
    def cartes_roles(self):
        if(self.number==3):
            self.personnage=['S','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 3)
        elif(self.number==4):
            self.personnage=['S','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 4)
        elif(self.number==5):
            self.personnage=['S','S','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 5)
        elif(self.number==6):
            self.personnage=['S','S','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 6)
        elif(self.number==7):
            self.personnage=['S','S','S','C','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 7)
        elif(self.number==8):
            self.personnage=['S','S','S','C','C','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 8)
        elif(self.number==9):
            self.personnage=['S','S','S','C','C','C','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 9)
        elif(self.number==10):
            self.personnage=['S','S','S','S','C','C','C','C','C','C','C']
            self.total_personnage=self.random.sample(self.personnage, 10)
            print(self.random.sample(self.personnage, 10))


Menu.aff_wel()
menu = Menu()
menu.get_number()
menu.players()