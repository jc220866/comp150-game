import pygame, LoadImages
from pygame.locals import *

pygame.init()

# variables
'''size = (750, 334)  # these are now moot according to Paul, and can be deleted
black = (0, 0, 0)'''
swipeDistance = 100  # distance needed to swipe for input to be recognised as a swipe, rather than a tap
inputCommand = 'none'

'''# guff
controlsSurface = pygame.display.set_mode(size)  # this is moot too
controlsSurface.fill(black)'''

'''def character_action(action):'''
    # ^ this should probably exist on the player script, not the inputs script


def read_mouse_movements(mouse_down_x, mouse_down_y):
    reading_mouse_change = True
    while reading_mouse_change:  # while loop to read mouse/swipe movements

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:  # upon releasing the mouse, calculate distance/direction moved
                mouse_up_x, mouse_up_y = event.pos
                input_distance_h = mouse_up_x - mouse_down_x
                input_distance_v = mouse_up_y - mouse_down_y
                reading_mouse_change = False  # end while loop

                if input_distance_h >= swipeDistance:
                    inputCommand = 'move_right'  # set input command to move right
                    '''print(inputDirection)'''
                elif input_distance_h <= -swipeDistance:
                    inputCommand = 'move_left'  # set input command to move left
                    '''print(inputDirection)'''
                elif input_distance_v >= swipeDistance:
                    inputCommand = 'close_inv?'  # set input command to something, this is just a placeholder
                    '''print(inputDirection)'''
                elif input_distance_v <= -swipeDistance:
                    inputCommand = 'open_inv'  # set input command to open inventory
                    '''print(inputDirection)'''
                elif abs(input_distance_h) < swipeDistance and abs(input_distance_v) < swipeDistance:
                    inputCommand = 'attack'  # set input command to attack

                '''character_action(inputCommand)'''
                    # ^ call the action (move, attack, etc.) uncomment when this is implemented

