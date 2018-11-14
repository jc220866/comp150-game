import pygame
import sys
import FrameHandler
import Entity
import AudioFiles
import ImageFiles
import Helper
import Menu
import Inputs
import Player
import MapGenerator
from pygame.locals import *

pygame.init()


# variables

REFRESH_RATE = Helper.REFRESH_RATE
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
DISPLAY_SURFACE.fill((79, 51, 44))
player = Player.Player()
MapGenerator.run_separator()
AudioFiles.generate_userinterface_sounds()

game_state = 'Main_Menu'
prev_game_state = ''
is_paused = False
running = True

while running:

    while game_state == 'Main_Menu':
        game_state = Menu.menu_update()

    while game_state == 'Settings':
        game_state = Menu.settings_menu_update()

    while game_state == 'New_Game':
        # event handling section
        player_action, game_state = FrameHandler.event_handler(
            game_state,
            player)

        # action handling section
        FrameHandler.update(player, player_action)

        # display handling section
        FrameHandler.renderer()

    if game_state == 'Quit':
        running = False

    # cap fps
    FPS_CLOCK.tick(REFRESH_RATE)

MapGenerator.run_remover()  # cleans generated tiles from Resources/Tiles

pygame.quit()
sys.exit()
