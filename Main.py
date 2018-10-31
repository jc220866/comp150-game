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

displaySurface = pygame.display.set_mode(Helper.RESOLUTION)
clock = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
displaySurface.fill(Helper.darkBrown)
player = Player.Player()
MapGenerator.run_separator()

# game loop
running = True


def player_action(action, Player):
    """For now, this always fires player move - this is just for testing"""
    print(action)
    if 'move' in action:
        player_move(action, Player)
    elif 'idle' == action:
        pass


def player_move(direction, Player):  # needs four directions
    if direction == 'move_right' and Player.currentLane < 1:
        player_destination = Player.playerPos[0] + Player.moveDistance
        Player.currentLane += 1

        while Player.playerPos[0] < player_destination:
            Player.playerPos[0] += Helper.MOVE_SPEED  # needs a loop in the "Main" script?
            displaySurface.blit(ImageFiles.images['Background'], (0, 0))
            displaySurface.blit(Player.image, (Player.playerPos[0], Player.playerPos[1]))
            pygame.display.flip()

    elif direction == 'move_left' and Player.currentLane > -1:
        player_destination = Player.playerPos[0] - Player.moveDistance
        Player.currentLane -= 1

        while Player.playerPos[0] > player_destination:
            Player.playerPos[0] -= Helper.MOVE_SPEED  # needs a loop in the "Main" script?
            displaySurface.blit(ImageFiles.images['Background'], (0, 0))
            displaySurface.blit(Player.image, (Player.playerPos[0], Player.playerPos[1]))

            pygame.display.flip()


game_state = 'Main_Menu'

while running:

    while game_state == 'Main_Menu' and running:
        game_state = Menu.menu_update()

    while game_state == 'New_Game' and running:
        # game loop event handling section
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:  # start to read swipe input
                player_action(Inputs.read_mouse_movements(event.pos, player), player)
            else:
                player_action('idle', player)

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
