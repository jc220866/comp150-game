import Entity
import Helper
import pygame
import ImageFiles

playerLanes = ['L', 'M', 'R']  # the three lanes-will be referenced with []
playerSurf = ImageFiles.images['Player']
playerRect = playerSurf.get_rect()  # I don't know how rectangles work
# may be useful: https://www.pygame.org/docs/tut/MoveIt.html
playerPos = (Helper.RESOLUTION[0]*0.5 - playerSurf.get_width()*0.5,
             Helper.RESOLUTION[1]*0.2 - playerSurf.get_height()*0.5
             )

currentLane = playerLanes[1]


def player_action(action):
    print(action)
    player_move('move_left', 1)


def player_move(direction, current_lane):  # needs four directions
    if direction == 'move_right' and current_lane < 2:
        pass
    elif direction == 'move_left' and current_lane > 0:
        pass
