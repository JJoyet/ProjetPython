import random
import numpy as np
import os


class Menu(object):
    """Allow to get information
    about the game"""

    def __init__(self):  # Property
        self.__number = 0
        self.__players_name = []
        self.__bot = []
        self.__roles = []
        self.__count = []
        self.__sharing_gold = []
        self.__spm = []
        self.__total_score = []

    # Methodes
    def __aff_wel(self):
        """Show the welcome screen"""
        print("+--------------------------------------------------------------------+")
        print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
        print("+--------------------------------------------------------------------+")

    def __get_number(self):
        """Put the number of players"""
        print("How many players?")
        state = False
        while state == False:
            self.__number = input()
            if (len(self.__number) == 1 or len(self.__number) == 2):
                if self.__number.isdecimal() == True:
                    self.__number = int(self.__number)
                    if (self.__number > 2 and self.__number < 11):
                        print("There is", self.__number, "players")
                        state = True
                    else:
                        print("Please choose a number between 3 and 10")
                else:
                    print('Please write a correct number')
            else:
                print('Please write a number')

    def __players(self):
        """Define the list of players"""
        for k in range(self.__number):
            # Clears the content of the console, we check if we are on Windows
            os.system('cls' if os.name == 'nt' else 'clear')
            self.__aff_wel()
            print('Please enter the name of player', k + 1)
            print('')
            player = input()
            self.__players_name.append(player)
            print('The name of the player is:', self.__players_name[k])
            print('Please press 0 if the player is an AI and press 1 if the player is an Human')
            state = False
            while state == False:
                bot = input()
                if bot == '1':
                    self.__bot.append("Human")
                    state = True

                elif bot == '0':
                    self.__bot.append("AI")
                    state = True
                else:
                    print("Please select 0 (AI) or 1 (Human):")
                    state = False

    def __cards_roles(self):  # Saboteur or Digger
        """Role of each player"""
        personnage = []
        if self.__number == 3:
            personnage = ['S', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 3)
        elif self.__number == 4:
            personnage = ['S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 4)
        elif self.__number == 5:
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 5)
        elif self.__number == 6:
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 6)
        elif self.__number == 7:
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 7)
        elif self.__number == 8:
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 8)
        elif self.__number == 9:
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 9)
        elif self.__number == 10:
            personnage = ['S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 10)

    def __display_start_end(self):
        """Show the total number of players"""
        total = []
        for k in range(self.__number - 1):
            total.append(self.__players_name[k] + '(' + self.__bot[k] + '),')
        total.append(self.__players_name[self.__number - 1] + '(' + self.__bot[self.__number - 1] + ')')
        total = ' '.join(total)
        print('---------------------')
        print('The', self.__number, 'players are:', total)

    def count_winner(self):
        """Count the number of diggers and saboteurs"""
        self.__count = [0, 0]
        for k in range(len(self.__roles)):  # For each role, we count the number of players having this role
            if self.__roles[k] == 'S':
                self.__count[0] += 1
            elif self.__roles[k] == 'C':
                self.__count[1] += 1

    def winner(self, state, current_indice):
        """state = 1 : Saboteurs won the set
        Calculate golds (points) for each saboteur
            state = 2: Digger won the set
        Calculate golds (points) for each digger """
        self.__state = state
        state = False
        score_round = np.zeros(self.__number)
        card_pull = 0
        self.__current_indice = current_indice
        if self.__state == 1:  # Case where the saboteurs won == 1
            print('Saboteurs won this round!')
            print('')
            for k in range(self.__number):
                if (self.__count[0] == 1 and self.__roles[k] == 'S'):
                    score_round[k] = 4  # 1 Saboteur = 4 points
                elif (self.__count[0] == 2 or self.__count[0] == 3):
                    if self.__roles[k] == 'S':  # 2 or 3 Saboteurs = 3 points
                        score_round[k] = 3
        elif (self.__state == 2):  # Case where Diggers won == 2
            print('Diggers won this round!')
            self.__sharing_gold = np.random.randint(1, 4, size=self.__number)  # Gold card worth between 1 and 3
            self.__sharing_gold = self.__sharing_gold.tolist()
            while len(self.__sharing_gold) != 0:  # Until when there are more pts to give away
                if self.__current_indice == self.__number:
                    self.__current_indice = 0
                if self.__roles[self.__current_indice] == 'C':
                    print("It is the remaining gold cards")
                    print(self.__sharing_gold)
                    print(f"To {self.__players_name[self.__current_indice]} to choose the card he/she wishes")
                    for k in range(self.__number):
                        if self.bot[k] == "Human":
                            while state == False:  # Choice of gold card
                                print("")
                                print(self.__sharing_gold)
                                print(f"Please choose a value between 1 and {self.__number - card_pull}")
                                self.__choice = input()
                                if self.__choice.isdecimal() == True:
                                    self.__choice = np.abs(int(self.__choice))
                                if 0 < self.__choice <= self.__number - card_pull:
                                    state = True
                                else:
                                    print("Please choose another value")
                            score_round[self.__current_indice] += self.__sharing_gold[self.__choice - 1]  # Storage of scores to calculate at the end of the game
                            print(f"{self.__players_name[self.__current_indice]} choose {self.__sharing_gold[self.__choice - 1]}")
                            del self.__sharing_gold[self.__choice - 1]  # Remove the gold card chooses
                            self.__current_indice += 1
                            card_pull += 1
                            state = False
                        elif self.__bot[k] == "AI":
                            score_round[self.__current_indice] += max(self.__sharing_gold)
                            self.__choice = self.__sharing_gold.remove(max(self.__sharing_gold))
                            self.__current_indice += 1
                            print(f"{self.__players_name[current_indice]} took his points")
                            card_pull += 1
                        if not self.__sharing_gold:
                            self.__current_indice = 11
                elif self.__roles[self.__current_indice] == 'S':
                    self.__current_indice += 1
            print("Here are the values of the gold cards")
            print(self.__sharing_gold)
        print(f"The score of this round is {score_round}")
        self.__spm.append(score_round)

    def start_game(self):
        """Used in SABOOTERS.py to get information before the start"""
        # Clears the content of the console, we check if we are on Windows
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__aff_wel()
        self.__get_number()
        self.__players()
        self.__cards_roles()
        self.__display_start_end()

    def end_round(self, state, current_indice):
        """Used in SABOOTTERS.py to get the score of each set"""
        self.count_winner()
        self.winner(state, current_indice)

    def end_game(self):
        """Used in SABOOTTERS.py to get the final score"""
        for i in range(self.__number):
            score_for_one_player = self.__spm[0][i] + self.__spm[1][i] + self.__spm[2][i]
            self.__total_score.append(score_for_one_player)
        print(f' The final score of this game is  {self.__total_score}')
        print('')
        max = np.max(self.__total_score)
        for k in range(len(self.__total_score)):
            if self.__total_score[k] == max:
                k_max = k
                print(f"The winner of this game is {self.__players_name[k_max]} with {max} points")
        for k in range(len(self.__total_score)):
            print(f"{self.__players_name[k]}'s score is {self.__total_score[k]} points")

    def change_role(self):
        """Assigning roles to players"""
        self.__cards_roles()

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
    def state(self):
        return self._state
    @property
    def roles(self):
        return self.__roles

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    @property
    def game_start(self):
        return self.__aff_wel(), self.__get_number(), self.__players(), self.__display_start_end()

    @property
    def total_score(self):
        return self.__total_score

    @property
    def spm(self):
        return self.__spm

    @property
    def current_indice(self):
        return self.__current_indice
