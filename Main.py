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

# colours
darkBrown = (79, 51, 44)
lightBrown = (107, 74, 55)
darkYellow = (124, 91, 51)
lightYellow = (147, 117, 53)
black = (0, 0, 0)
darkGrey = (63, 63, 63)
midGrey = (127, 127, 127)
lightGrey = (191, 191, 191)

displaySurface = pygame.display.set_mode(Helper.RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
displaySurface.fill(darkBrown)
player = Player.Player()

# game loop
running = True
MapGenerator.run_separator()

while running:

    # game loop event handling section
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:  # start to read swipe input
            Inputs.read_mouse_movements(event.pos, player, displaySurface)

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
