import pygame, LoadImages
from pygame.locals import *

pygame.init()

# variables
swipeDistance = 100  # distance needed to swipe for input to be recognised as a swipe, rather than a tap
inputCommand = 'none'

# def character_action(action):
    # ^ this should probably exist on the player script, not the inputs script


def read_mouse_movements(mouse_down_x, mouse_down_y):
    reading_mouse_change = True
    while reading_mouse_change:  # while loop to read mouse/swipe movements

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:
                mouse_up_x, mouse_up_y = event.pos
                input_distance_h = mouse_up_x - mouse_down_x
                input_distance_v = mouse_up_y - mouse_down_y
                reading_mouse_change = False

                if input_distance_h >= swipeDistance:
                    inputCommand = 'move_right'
                elif input_distance_h <= -swipeDistance:
                    inputCommand = 'move_left'
                elif input_distance_v >= swipeDistance:
                    inputCommand = 'close_inv?'
                elif input_distance_v <= -swipeDistance:
                    inputCommand = 'open_inv'
                elif abs(input_distance_h) < swipeDistance and abs(input_distance_v) < swipeDistance:
                    inputCommand = 'attack'

                # character_action(inputCommand)
                    # ^ call the action (move, attack, etc.) uncomment when this is implemented

