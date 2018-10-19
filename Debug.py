import pygame
import Classes
import time

pygame.init()

windowHeight = 60
windowWidth = 400

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Debugger for weapon generation')

pygame.font.init()
my_font = pygame.font.SysFont('Inverted', 24)

finished = False

def test_weapon_generator():
    screen.fill((0, 0, 0))
    weapon = Classes.Weapon()
    pygame.transform.scale(weapon.weapon_texture, (336, 48))
    screen.blit(weapon.weapon_texture, (0, 0))
    text_surface = my_font.render(weapon.name, False, (255, 255, 255))
    screen.blit(text_surface, (0, 36))


while finished is False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            test_weapon_generator()
        pygame.display.update()

screen.fill((255, 255, 255))

pygame.display.flip()
