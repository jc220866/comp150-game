# this should only have one function in, this function can be moved elsewhere
import pygame
import Helper
import Entity
import Player
import ImageFiles
import EnemyAttacks


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

    pygame.display.flip()
