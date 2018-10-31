import pygame
import sys
import ImageFiles
import Helper
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
while running:

    # game loop event handling section
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:  # start to read swipe input
            player.player_action(Inputs.read_mouse_movements(event.pos, player), player)
        # else:
            # Player.player_action('idle', player)

    # game loop action section

    # game loop display section
    displaySurface.blit(ImageFiles.images['Background'], (0, 0))
    displaySurface.blit(player.playerSurf, player.playerPos)
    pygame.display.flip()

    # cap fps
    clock.tick(refreshRate)

MapGenerator.run_remover()

pygame.quit()
sys.exit()
