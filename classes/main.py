import numpy as np
import random
import pygame
from player import Player
from menu import Menu
from PlayerView import PlayerView 

m = Menu()
#initialisation de pygame, nécessaire pour faire fonctionner les modules
pygame.init()
#on créé le screen qui sur lequel seront inserrés les images
screen = pygame.display.set_mode((960, 540))
pv = PlayerView(screen)
pygame.display.set_caption("Test")

#on créé les paths vers les cartes et leurs nombres
cards = ["images/PathCards/URDL.jpg", "images/PathCards/URDL.jpg", "images/PathCards/URDL.jpg", "images/PathCards/URDL.jpg", "images/PathCards/URDL.jpg",
"images/PathCards/URD.jpg", "images/PathCards/URD.jpg", "images/PathCards/URD.jpg", "images/PathCards/URD.jpg", "images/PathCards/URD.jpg",
 "images/PathCards/URL.jpg", "images/PathCards/URL.jpg", "images/PathCards/URL.jpg", "images/PathCards/URL.jpg", "images/PathCards/URL.jpg",
"images/PathCards/UR.jpg", "images/PathCards/UR.jpg", "images/PathCards/UR.jpg", "images/PathCards/UR.jpg", "images/PathCards/UR.jpg", 
"images/PathCards/UL.jpg", "images/PathCards/UL.jpg", "images/PathCards/UL.jpg", "images/PathCards/UL.jpg",
"images/PathCards/UD.jpg", "images/PathCards/UD.jpg", "images/PathCards/UD.jpg", "images/PathCards/UD.jpg", 
"images/PathCards/RL.jpg", "images/PathCards/RL.jpg", "images/PathCards/RL.jpg", 
"images/PathCards/URDLx.jpg", "images/PathCards/URDx.jpg", "images/PathCards/URLx.jpg", "images/PathCards/URx.jpg", "images/PathCards/ULx.jpg",
"images/PathCards/UDx.jpg", "images/PathCards/RLx.jpg", "images/PathCards/Ux.jpg", "images/PathCards/Rx.jpg", 
"images/object_cards/Li.jpg", "images/object_cards/Li.jpg", "images/object_cards/Lix.jpg", "images/object_cards/Lix.jpg", "images/object_cards/LIx.jpg",
"images/object_cards/P.jpg", "images/object_cards/P.jpg", "images/object_cards/Px.jpg", "images/object_cards/Px.jpg", "images/object_cards/Px.jpg", 
"images/object_cards/W.jpg", "images/object_cards/W.jpg", "images/object_cards/Wx.jpg", "images/object_cards/Wx.jpg", "images/object_cards/Wx.jpg", 
"images/object_cards/LiP.jpg", "images/object_cards/LiW.jpg", "images/object_cards/PW.jpg", 
"images/object_cards/MAP.jpg", "images/object_cards/MAP.jpg", "images/object_cards/MAP.jpg", "images/object_cards/MAP.jpg", "images/object_cards/MAP.jpg", "images/object_cards/MAP.jpg",
"images/object_cards/RoF.jpg", "images/object_cards/RoF.jpg", "images/object_cards/RoF.jpg"]

random.shuffle(cards)

#on créé 10 joueurs qu'on met dans la liste players
player1 = Player("","",[])
player2 = Player("","",[])
player3 = Player("","",[])
player4 = Player("","",[])
player5 = Player("","",[])
player6 = Player("","",[])
player7 = Player("","",[])
player8 = Player("","",[])
player9 = Player("","",[])
player10 = Player("","",[])

players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]

name_players = []
name = []
done = False
pv.menu("images/accueil0.jpg")
while not done:
    nb_players = pv.input_box(378,354)
    #check le nb de joueurs et et si l'utilisateur entre des caractères ou non + créé un tableau avec le nom des joueurs
    if nb_players.isnumeric() == True and int(nb_players) > 2 and int(nb_players) < 11: 
        for i in range(int(nb_players)):
            pv.menu("images/accueil_name.jpg")
            text = f"Player {i+1}" 
            text_box = pygame.Rect(390, 320, 140, 32)
            txt_surface = pygame.font.Font(None, 32).render(text, True, pygame.Color("white"))
            screen.blit(txt_surface, (text_box.x+5, text_box.y+5))
            pygame.display.flip()
            name = pv.input_box(378,354)  
            name_players.append(name)
        print(name_players) 
        done = True  
    else:
        pv.entree_button("images/accueil_fail_number.jpg")

#choix de le pos du gold
gold_pos = [(3,10), (5, 10), (7, 10)]
x_coord_gold, y_coord_gold = random.choice(gold_pos)
print(x_coord_gold, y_coord_gold)

 #on met les noms des joueurs dans le tableau
nb_players = int(nb_players)
for i in range(nb_players):
    players[i].__name = name_players[i]
#on attribut les rôles aux joueuers
if nb_players <= 4:
    j = random.randrange(nb_players)
    for i in range(nb_players):
        if i == j:
            players[i].__role = "S"
            continue
        players[i].__role = "C"
elif nb_players <= 6:
    j = random.randrange(nb_players)
    k = random.randrange(nb_players)
    if j == k:
        k=(k+1)%nb_players
    for i in range(nb_players):
        if i == j or i == k:
            players[i].__role = "S"
            continue
        players[i].__role = "C"
elif nb_players <= 9:
    j = random.randrange(nb_players)
    k = random.randrange(nb_players)
    l = random.randrange(nb_players)
    if j == k:
        k =(k+1)%nb_players
    if j == l:
        l=(l+1)%nb_players
    if l == k:
        l =(l+1)%nb_players
    for i in range(nb_players):
        if i == j or i == k or i == l:
            players[i].__role = "S"
            continue
        players[i].__role = "C"
else :
    j = random.randrange(nb_players)
    k = random.randrange(nb_players)
    l = random.randrange(nb_players)
    m = random.randrange(nb_players)
    if j == k:
        k =(k+1)%nb_players
    if j == l:
        l=(l+1)%nb_players
    if l == k:
        l =(l+1)%nb_players
    if m == j:
        m =(m+1)%nb_players
    if m == k:
        m =(m+1)%nb_players
    if m ==l:
        m =(m+1)%nb_players
    for i in range(nb_players):
        if i == j or i == k or i == l or i == m:
            players[i].__role = "S"
            continue
        players[i].__role = "C"

#on fait piocher des cartes en fonction du nombre de joueurs
if nb_players < 6:
    for i in range(nb_players):
        for _ in range(6):
            players[i].hand.append(cards.pop())

elif nb_players < 8:
    for i in range(nb_players):
        for _ in range(5):
            players[i].hand.append(cards.pop())
else:
    for i in range(nb_players):
        for _ in range(4):
            players[i].hand.append(cards.pop())

pv.menu("images/board_arena.jpg")    
turn = 0 
#déroulement du tour
while True:
    pv.display_joueurs(name_players) #affiche le nom des joueurs
    pv.display_name(name_players[turn]) #affichage le nom du joueur courrant
    hand = players[turn].hand #on donne une main au joueur
    pv.player_hand(hand) #on affiche la main
    card = pv.pick_card(hand) 
    pv.play_card(card)  #on fait jouer une carte sur le plateau
    


    turn = (turn + 1) % nb_players