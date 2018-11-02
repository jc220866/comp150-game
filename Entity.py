import pygame
import random
import ImageFiles
import Helper
# Classes used by Entity type Objects


pygame.init()
'''
windowHeight = 150
windowWidth = 450

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
'''

enemy_list = []

class Entity:
    # index is used to keep track of entities
    entity_index = 0  # Declaration of static Index
    # Declaration of static alignment for all Entities
    entity_alignment = ('Aggressive', 'Passive', 'Friendly')
    defaultHealth = 100

    def __init__(self):
        # subname is a unique identifier that uses the index
        subname = 'Entity' + str(Entity.entity_index)
        name = 'Placeholder name'
        # Importing index into the Entity-specific variable
        index = Entity.entity_index

        # Incrementing the index of all entities
        Entity.entity_index += 1

        # defining where the entity is encountered (by default, nowhere)
        on_encounter = False
        on_battle = False

        # setting alignment to passive as a default
        alignment = Entity.entity_alignment[1]

        # To do: define states, as to specify what
        # images and animations to incorporate into lists


class Enemy(Entity):

    numberOfOnscreenEnemies = 0
    enemyVisibility = dict(
        left=False,
        centre=False,
        right=False
        )

    def __init__(self):
        Entity.__init__(self)
        self.health = Entity.defaultHealth  # * (enemyLevel * 0.1)
        self.sprite = ImageFiles.images['Enemies'][0]  # [random.randint(0, len(ImageFiles.images) - 1)]
        self.pos = [0, 0]
        enemy_list.append(self)

    def generate_enemy(self, position):  # currently debug only code
        """
        Debug code for rendering enemy
        :param position: Keycode for j, k, or l
        :return:
        """
        if position == 106:
            Enemy.enemyVisibility['left'] = True
        elif position == 107:
            Enemy.enemyVisibility['centre'] = True
        elif position == 108:
            Enemy.enemyVisibility['right'] = True

        self.sprite = ImageFiles.images['Enemies'][0]  # [random.randint(0, len(ImageFiles.images) - 1)]

    def is_hit(self, damage):
        self.health = self.health - damage
        # play_sound(enemy_hit)


class EnemyBoss(Enemy):

    def __init__(self):
        Enemy.__init__(self)
