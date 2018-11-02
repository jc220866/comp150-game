import pygame
import ImageFiles
import Helper
import Player

pygame.init()
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE

attackSprites = []


class enemy_attack_sprite:

    projectile_speed = 10  # Put in Helper at a later point

    def __init__(self, lane, parent_enemy):
        self.sprite = ImageFiles.images['Enemy_Attack']
        self.rect = self.sprite.get_rect()
        self.lane = lane
        self.damage = parent_enemy.damage

        print('this will deal ' + str(self.damage) + ' to the player with ' + str(Player.Player.health) + 'hp')

        self.pos_y = self.rect.y = Helper.LANES[lane][0][1] - int(self.rect.height/2)
        self.pos_x = self.rect.x = Helper.LANES[lane][0][0] - int(self.rect.width/2)

        attackSprites.append(self)

    def update(self):

        collision_with_player = False

        if self.rect.colliderect(Player.Player.playerRect):
            collision_with_player = True
            Player.Player.is_hit(self.damage)

        if self.pos_y < 1334 and collision_with_player is False:
            self.pos_y += enemy_attack_sprite.projectile_speed
            self.rect.y += enemy_attack_sprite.projectile_speed
        elif self.pos_y >= 1334 and collision_with_player is False:
            attackSprites.remove(self)
        elif collision_with_player is True:
            attackSprites.remove(self)
            del self
