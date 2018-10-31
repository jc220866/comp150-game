import pygame
import sys
from pygame.locals import *

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAY_SURFACE = pygame.display.set_mode((750, 1000), 0, 32)
pygame.display.set_caption('Sekai Saviour')

BLACK = (0, 0, 0)                # currently used for the background
BACKGROUND_GOLD = (124, 91, 51)   # currently unused
BUTTON_GOLD = (147, 117, 53)      # colour of the buttons
HIGHLIGHT = (150, 120, 100, 20)  # colour of the highlight, not sure how
#  to get alpha working but we won't bother

buttonNewGame = pygame.Rect(50, 600, 300, 150)
buttonContinue = pygame.Rect(400, 600, 300, 150)
buttonSettings = pygame.Rect(50, 800, 300, 150)
buttonQuit = pygame.Rect(400, 800, 300, 150)


def draw_menu():  # Draws rectangles to represent the 'buttons'
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttonNewGame)
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttonContinue)
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttonSettings)
    pygame.draw.rect(DISPLAY_SURFACE, BUTTON_GOLD, buttonQuit)


def check_buttons(click_pos):
    """
    Checks which 'button' was clicked,
    can assign functions to each separate button
    Args:
        click_pos -- position of the mouse click
    """
    if buttonNewGame.collidepoint(click_pos):
        print("Button clicked: New Game")
        return 'New_Game'
    if buttonContinue.collidepoint(click_pos):
        print("Button clicked: Continue")
        # return 'Continue'
        pass
    if buttonSettings.collidepoint(click_pos):
        print("Button clicked: Settings")
        # return 'Settings'
        pass
    if buttonQuit.collidepoint(click_pos):
        print("Button clicked: Quit")
        # return 'Quit'
        pass
    return 'Main_Menu'


def highlight_buttons(mx, my):  # Draws a highlight over a button on mouse-over
    if buttonNewGame.collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttonNewGame)
    if buttonContinue.collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttonContinue)
    if buttonSettings.collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttonSettings)
    if buttonQuit.collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttonQuit)


def menu_update():
    while True:
        DISPLAY_SURFACE.fill(BLACK)
        draw_menu()

        mouse_x = mouse_y = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # stores most recent mouse movement in two variables
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            # check if a button was clicked on mouse click
            elif event.type == MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                return check_buttons(click_pos)

        highlight_buttons(mouse_x, mouse_y)
        pygame.display.update()
        fpsClock.tick(FPS)
