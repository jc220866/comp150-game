import pygame
import ImageFiles
import Helper

pygame.init()
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE

attackSprites = []


def enemy_attack(lane):

    attackSprites.append(enemy_attack_sprite(lane))
    pass


class enemy_attack_sprite:

    projectile_speed = 10  # Put in Helper at a later point

    def __init__(self, lane):
        self.sprite = ImageFiles.images['Enemy_Attack']
        self.rect = self.sprite.get_rect()
        self.lane = lane

        self.pos_y = -10

        if lane == 'MiddleLane':
            self.pos_x = 375 - int(self.rect.width/2)

    def update_position(self):

        collision_with_player = False
        if self.pos_y < 1334 and collision_with_player is False:
            self.pos_y += enemy_attack_sprite.projectile_speed
        # add case for colliding with player
