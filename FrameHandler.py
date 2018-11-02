# this should only have one function in, this function can be moved elsewhere
import pygame
import Inputs
import Helper
import Entity
import Player
import ImageFiles
import EnemyAttacks
from pygame.locals import *


def event_handler(game_state, player):
    player_action = 'idle'
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state = 'Quit'
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state = 'Main_Menu'
            if event.key == K_g and Entity.Enemy.numberOfOnscreenEnemies < 3:
                for i in range(0, 3):
                    Entity.enemy_list.append(Entity.Enemy())
        elif event.type == MOUSEBUTTONDOWN:
            player_action = Inputs.read_mouse_movements(event.pos, player)
    return player_action, game_state


def update(player, player_action):
    if 'idle' in player_action and player.is_moving:
        player_action = player.move_direction
    player.player_action(player, player_action)


def renderer():  # to be called every frame to render every image in a list

    Helper.DISPLAY_SURFACE.blit(ImageFiles.images['Background'], (0, 0))
    Helper.DISPLAY_SURFACE.blit(Player.Player.playerSurf, Player.Player.playerPos)

    for projectile in EnemyAttacks.attackSprites:
        Helper.DISPLAY_SURFACE.blit(projectile.sprite, (projectile.sprite.pos_x, projectile.sprite.pos_y))

    for enemy in Entity.enemy_list:
        Helper.DISPLAY_SURFACE.blit(enemy.sprite, enemy.pos)

    if Player.Player.inventoryIsOpen:
        Helper.DISPLAY_SURFACE.blit(
            ImageFiles.images['UI']['Inventory_Background'],
            Helper.INVENTORY_POSITION
        )
    pygame.time.Clock().tick(Helper.REFRESH_RATE)
    pygame.display.flip()

