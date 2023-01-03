import sys

sys.path.insert(0, "../PROJETPYTHON")
import classes.fin_partie as test

roles = ['S', 'S', 'C', 'C', 'C']
players = ['Lau', 'Julie', 'Z', 'K', 'S']
c_state = True
c_count = 0
s_count = 0
s_state = False
count = 3
fin = test.fin_manche(roles, players, c_count, s_count)
fin.finito(count, s_state, c_state)
