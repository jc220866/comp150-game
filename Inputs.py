import pygame
from pygame.locals import *

pygame.init()

# variables
swipeDistance = 100  # distance needed to swipe for input to be recognised
# as a swipe, rather than a tap (maybe should be in helper.py?)

# def character_action(action):
# ^ this should probably exist on the player script, not the inputs script


def read_mouse_movements(mouse_down_x, mouse_down_y):

    input_command = 'none'

    reading_mouse_change = True
    while reading_mouse_change:  # while loop to read mouse/swipe movements

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                mouse_up_x, mouse_up_y = event.pos
                input_distance_h = mouse_up_x - mouse_down_x
                input_distance_v = mouse_up_y - mouse_down_y
                reading_mouse_change = False

                if input_distance_h >= swipeDistance:
                    input_command = 'move_right'
                elif input_distance_h <= -swipeDistance:
                    input_command = 'move_left'
                elif input_distance_v >= swipeDistance:
                    input_command = 'close_inv?'
                elif input_distance_v <= -swipeDistance:
                    input_command = 'open_inv'
                elif abs(input_distance_h) < swipeDistance\
                        and\
                        abs(input_distance_v) < swipeDistance:
                    input_command = 'attack'

                # character_action(input_command)
                    # ^ call the action (move, attack, etc.)
                    # uncomment when this is implemented

