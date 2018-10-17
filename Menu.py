import pygame
from pygame.locals import *

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURFACE = pygame.display.set_mode((750, 1000), 0, 32)
pygame.display.set_caption('S E K A I SAVIOR')

BLACK = (0, 0, 0)                # currently used for the background
BACKGROUNDGOLD = (124, 91, 51)   # currently unused
BUTTONGOLD = (147, 117, 53)      # colour of the buttons
HIGHLIGHT = (150, 120, 100, 20)  # colour of the highlight, not sure how to get alpha working but we won't bother

buttonNewGame = pygame.Rect(50, 600, 300, 150)
buttonContinue = pygame.Rect(400, 600, 300, 150)
buttonSettings = pygame.Rect(50, 800, 300, 150)
buttonQuit = pygame.Rect(400, 800, 300, 150)


def drawmenu():  # Draws rectangles to represent the 'buttons'
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonNewGame)
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonContinue)
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonSettings)
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonQuit)


def checkbuttons():  # Checks which 'button' was clicked, can assign functions to each separate button
    if buttonNewGame.collidepoint(clickPos):
        print("Button clicked: New Game")
    if buttonContinue.collidepoint(clickPos):
        print("Button clicked: Continue")
    if buttonSettings.collidepoint(clickPos):
        print("Button clicked: Settings")
    if buttonQuit.collidepoint(clickPos):
        print("Button clicked: Quit")


def highlightbuttons(mx, my):  # Draws a highlight over a button when moused over
    if buttonNewGame.collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonNewGame)
    if buttonContinue.collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonContinue)
    if buttonSettings.collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonSettings)
    if buttonQuit.collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonQuit)


while True:
    DISPLAYSURFACE.fill(BLACK)
    drawmenu()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos  # stores most recent mouse movement in two variables
        elif event.type == MOUSEBUTTONUP:
            clickPos = pygame.mouse.get_pos()
            checkbuttons()              # when the mouse button is clicked, we check if a button was clicked

    highlightbuttons(mousex, mousey)
    pygame.display.update()
    fpsClock.tick(FPS)
