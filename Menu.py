import pygame
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURFACE = pygame.display.set_mode((750, 1000), 0, 32)
pygame.display.set_caption('S E K A I SAVIOR')

BACKGROUNDGOLD = (124, 91, 51)
BUTTONGOLD = (147, 117, 53)
HIGHLIGHT = (150, 120, 100, 20)
BLACK = (0, 0, 0)

# newgame = pygame.rect((300, 200), BUTTONGOLD, (600, 400), width=100)
buttonNewGame = pygame.Rect(50, 600, 300, 150)
buttonContinue = pygame.Rect(400, 600, 300, 150)
buttonSettings = pygame.Rect(50, 800, 300, 150)
buttonQuit = pygame.Rect(400, 800, 300, 150)

buttonTest = pygame.Rect (250, 250, 250, 250)


def drawmenu():  # Draws rectangles to represent the 'buttons'
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonNewGame)
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonContinue)
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonSettings)
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonQuit)

    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttonTest)


def checkbuttons():  # Checks which 'button' was clicked, can assign functions to each separate button
    if buttonNewGame.collidepoint(clickPos):
        print("Button clicked: New Game")
    if buttonContinue.collidepoint(clickPos):
        print("Button clicked: Continue")
    if buttonSettings.collidepoint(clickPos):
        print("Button clicked: Settings")
    if buttonQuit.collidepoint(clickPos):
        print("Button clicked: Quit")

    if buttonTest.collidepoint(clickPos):
        print("Button clicked: Test")


def highlightbuttons(mx, my):  # Draws a highlight over a button when moused over
    if buttonNewGame.collidepoint(mousex, mousey):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonNewGame)
    if buttonContinue.collidepoint(mousex, mousey):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonContinue)
    if buttonSettings.collidepoint(mousex, mousey):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonSettings)
    if buttonQuit.collidepoint(mousex, mousey):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttonQuit)

    if buttonTest.collidepoint(mx, my):
        print("Hovering over button: Test")
        pygame.draw.rect(DISPLAYSURFACE, BACKGROUNDGOLD, buttonTest)


while True:
    DISPLAYSURFACE.fill(BLACK)
    drawmenu()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            clickPos = pygame.mouse.get_pos()
            checkbuttons()

    highlightbuttons(mousex, mousey)

    pygame.display.update()
    fpsClock.tick(FPS)
