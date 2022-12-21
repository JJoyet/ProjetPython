import pygame

class PlayerView:
    def __init__(self):
        self.i_factor = 75
        self.j_factor = 50
        self.i_offset = 144
        self.j_offset = 0
        self.field = [[None] * 11] * 9

    def input_box(self, x, y):
        # Create a nb_players input box that lets the user enter a string inside it.
        # The string is then displayed on the screen, and pressing backspace removes the last character from the diplsayed string.
        # The box should have a solid white backgroud and a black border.
        input_box = pygame.Rect(x, y, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            # Add a white backgournd to the text box
            pygame.draw.rect(screen, (255, 255, 255), (input_box.x, input_box.y, input_box.w, input_box.h))
            # Render the current text.
            txt_surface = pygame.font.Font(None, 32).render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)

            pygame.display.flip()

        return None

    def menu(self, img):
        screen.blit(pygame.image.load(img), (0, 0))
        pygame.display.flip()

    def put_card(self, i, j):
        if (self.field[i][j] is None):
            return
        screen.blit(pygame.image.load(self.field[i][j]), (self.i_offset + self.i_factor * i, self.j_offset + self.j_factor * j))
        pygame.display.flip()
	
    def player_hand(self, player):
        coords = [(687, 53), (781, 53), (875, 53), (687, 109), (781, 109), (875, 109)]
        cards = player.hand # a revoir lmao

        for i in range(len(cards)):
            screen.blit(pygame.image.load(cards[i]), coords[i])
        
        pygame.display.flip()


		
pygame.display.flip()

pv = PlayerView()

pygame.init()

screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Test")


pv.menu("images/accueil.jpg")


for i in range(9):
        for j in range(11):
            pv.field[i][j] = "images/PathBack.jpg" # Resize en 74*49
            pv.put_card(i, j)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pv.field[7][7] = "images/PathBack1.jpg"
    pv.put_card(7, 7)