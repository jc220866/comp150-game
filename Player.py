import Entity
import Helper
import pygame
import ImageFiles


class Player:

    playerLanes = ['L', 'M', 'R']  # the three lanes-will be referenced with []
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = (Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 )  # (311.0, 202.8 for 750x1334 resolution)
    moveDistance = Helper.MOVE_DISTANCE
    currentLane = playerLanes[1]

    def __init__(self):
        pass


def player_action(action):
    '''For now, this always fires player move - this is just for testing'''
    print(action)
    player_move('move_left', 1)


def player_move(direction, current_lane):  # needs four directions
    if direction == 'move_right' and current_lane < 2:
        player_dest = Player.playerPos[0] + Player.moveDistance
        while Player.playerPos[0] < player_dest:  # needs a loop in the "Main" script..?
            Player.playerPos += 5
    elif direction == 'move_left' and current_lane > 0:
        pass
