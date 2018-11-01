import pygame
import sys

import Entity
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


game_state = 'Main_Menu'
is_paused = False

running = True
while running:

    while game_state == 'Main_Menu' and running:
        game_state = Menu.menu_update()

    enemy1 = Entity.Enemy()
    enemy1.generate_enemy()

    while game_state == 'New_Game' and running:
        # game loop event handling section
        if not is_paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_a:
                        player.player_action('move_left', player)
                    elif event.key == K_d:
                        player.player_action('move_right', player)
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
