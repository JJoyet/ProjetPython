import random
import numpy as np
import os





class Menu(object):
    def __init__(self):  # Property
        self.__number = 0
        self.__players_name = []
        self.__bot = []
        self.__roles = []
        self.__count = []
        self.__sharing_gold = []
        self.__spm = []
        self.__total_score = []
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
                    self.__number = int(self.__number)
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
            os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas
            self.__aff_wel()
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
        for k in range(self.__number-1):
            total.append(self.__players_name[k] + '(' + self.__bot[k]+'),')
        total.append(self.__players_name[self.__number-1] + '(' + self.__bot[self.__number-1]+')')
        total = ' '.join(total)
        print('---------------------')
        print('The', self.__number, 'players are:', total)

    def start_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas
        self.__aff_wel()
        self.__get_number() 
        self.__players() 
        self.__cartes_roles()
        self.__affichage_debut_fin()

    def change_role(self):
        self.__cartes_roles()

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
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self,count):
        self.__count = count
    @property
    def game_start(self):
        return self.__aff_wel(), self.__get_number(), self.__players(), self.__affichage_debut_fin()
    def count_winner(self):
        self.__count = [0, 0]
        for k in range(len(self.__roles)):   #Pour chaque roles je compte le nb de joueurs ayant ce role
            if (self.__roles[k]=='S'):
                self.__count[0] += 1
            elif (self.__roles[k]=='C'):
                self.__count[1] += 1
        print(self.__count)

    def winner(self,state,current_indice):
        self.state = state
        etat = False
        score_manche = np.zeros(self.__number)
        card_pull = 0
        self.__current_indice = current_indice
        if (self.state == 1): #Disons que c'est le cas où les saboteurs ont gagnés == 1
            print('Saboteurs won this game!')
            print('')
            for k in range (self.__number):
                if (self.__count[0] == 1):
                    if (self.__roles[k] == 'S'):  #Un sabotteur, il obtient 4 pts
                        score_manche[k]= 4
                elif(self.__count[0] == 2 or self.__count[0] == 3): #2 ou 3 ils obtiennent 3 pts
                    if (self.__roles[k] == 'S'):
                        score_manche[k] = 3
        elif (self.state == 2):     #Cas ou Mineurs gagnent == 2
            print('Diggers won this game!')
            self.__sharing_gold = np.random.randint(1, 4, size=self.__number)  # Carte d'or valant entre 1 et 3
            self.__sharing_gold = self.__sharing_gold.tolist()
            while (len(self.__sharing_gold) != 0):  # Jusqu'a quand y'a plus de pts a distribuer
                if self.__current_indice == self.__number:
                    self.__current_indice = 0
                if (self.__roles[self.__current_indice] == 'C'):  # Personnes étant Mineur                while (current_indice < self.count[1]):  # Addition des pts des mineurs quand il y a plus de cartes or que de mineurs
                    print("It is the remaining gold cards")
                    print(self.__sharing_gold)
                    print(f"To {self.__players_name[self.__current_indice]} to choose the card he/she wishes")
                    while (etat == False):  # Choix de la carte d'or
                        print(f"Please choose a value between 1 and {self.__number - card_pull}")
                        self.__choice = input()
                        if (self.__choice.isdecimal() == True):
                            self.__choice = int(self.__choice)
                            if (self.__choice > 0 or self.__choice < len(self.__sharing_gold) - card_pull):
                                etat = True
                            else:
                                print("Please choose another value")
                    score_manche[self.__current_indice] += self.__sharing_gold[self.__choice - 1]  # Stockage des scores pour calcuer en fin de partie
                    print(f"{self.__players_name[self.__current_indice]} choose {self.__sharing_gold[(self.__choice) - 1]}")
                    del self.__sharing_gold[self.__choice - 1]  # Enlever la carte d'or choisit
                    self.__current_indice += 1
                    card_pull += 1
                    etat = False
                    if not (self.__sharing_gold):
                        self.__current_indice = 11
                elif self.__roles[self.__current_indice] == 'S':
                    self.__current_indice += 1
            print("Voici la valeur des cartes or")
            print(self.__sharing_gold)
        print(f"The score is {score_manche}")
        self.__spm.append(score_manche)
    def fin_de_manche(self,state,current_indice):
        self.count_winner()
        self.winner(state,current_indice)
    def fin_de_partie(self):

        for i in range(self.__number):
            score_for_one_player = self.__spm[0][i] + self.__spm[1][i] + self.__spm[2][i]
            self.__total_score.append(score_for_one_player)
        print(f' Le score final est de {self.__total_score}')
    @property
    def total_score(self):
        return self.__total_score


    @property
    def spm(self):
        return self.__spm
    @property
    def current_indice(self):
        return self.__current_indice