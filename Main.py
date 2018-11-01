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

DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
DISPLAY_SURFACE.fill(Helper.darkBrown)
player = Player.Player()
MapGenerator.run_separator()

# game loop
running = True

game_state = 'Main_Menu'

is_paused = False

while running:

    while game_state == 'Main_Menu':
        game_state = Menu.menu_update()
        DISPLAY_SURFACE.blit(ImageFiles.images['Player'], (0, 0))

    while game_state == 'New_Game' and running and not is_paused:
        # game loop event handling section
        if not is_paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_state = 'Main_Menu'
                        break
                    elif event.key == K_a:
                        player.player_action('move_left', player)
                    elif event.key == K_d:
                        player.player_action('move_right', player)
                    elif event.key == K_i:
                        player.inventoryIsOpen = player.inventory_update(
                            'switch_inv'
                        )
                        print('toggling inventory')
                elif \
                        event.type == MOUSEBUTTONDOWN \
                        and not \
                        Player.Player.inventoryIsOpen:
                    action = Inputs.read_mouse_movements(event.pos, player)
                    player.player_action(action, player)
                    player.inventoryIsOpen = player.inventory_update(action)
                elif \
                        event.type == MOUSEBUTTONDOWN \
                        and \
                        Player.Player.inventoryIsOpen:
                    action = Inputs.read_mouse_movements(event.pos, player)
                    player.inventoryIsOpen = player.inventory_update(action)
                else:
                    player.player_action('idle', player)

            # game loop action section

            # game loop display section

            DISPLAY_SURFACE.blit(ImageFiles.images['Background'], (0, 0))
            DISPLAY_SURFACE.blit(player.playerSurf, player.playerPos)

            if Player.Player.inventoryIsOpen:
                DISPLAY_SURFACE.blit(
                    ImageFiles.images['UI']['Inventory_Background'],
                    Helper.INVENTORY_POSITION
                )

            pygame.display.flip()
        else:
            print('GAME IS PAUSED')
            pygame.time.delay(300)

    if game_state == 'Quit':
        running = False

    # cap fps
    FPS_CLOCK.tick(refreshRate)

MapGenerator.run_remover()

pygame.quit()
sys.exit()
