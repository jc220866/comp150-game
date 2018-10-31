import pygame
import sys
import ImageFiles
import Helper
import Menu
import Inputs
import Player
import MapGenerator
from pygame.locals import *

pygame.init()


# variables
refreshRate = 60

displaySurface = Helper.displaySurface
clock = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
displaySurface.fill(Helper.darkBrown)
player = Player.Player()
MapGenerator.run_separator()

# game loop
running = True


game_state = 'Main_Menu'
is_paused = False

while running:

    while game_state == 'Main_Menu' and running:
        game_state = Menu.menu_update()

    while game_state == 'New_Game' and running:
        # game loop event handling section
        if is_paused == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == MOUSEBUTTONDOWN:  # start to read swipe input
                    player.player_action(Inputs.read_mouse_movements(event.pos, player), player)
                else:
                    player.player_action('idle', player)

            # game loop action section

            # game loop display section
            displaySurface.blit(ImageFiles.images['Background'], (0, 0))
            displaySurface.blit(player.playerSurf, player.playerPos)
            pygame.display.flip()
        else:
            print('GAME IS PAUSED')
            pygame.time.delay(300)

    # cap fps
    clock.tick(refreshRate)

MapGenerator.run_remover()

pygame.quit()
sys.exit()
