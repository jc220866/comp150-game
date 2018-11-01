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

        # To do: define states, as to specify what images and animations to incorporate into lists


class Enemy(Entity):

    def __init__(self):
        Entity.__init__(self)
        self.health = Entity.defaultHealth  # * (enemyLevel * 0.1)
        self.sprite = ImageFiles.images['Enemies'][0]  # [random.randint(0, len(ImageFiles.images) - 1)]

    @staticmethod
    def generate_enemy():
        Helper.displaySurface.blit(Enemy.sprite, (200, 200))


class EnemyBoss(Enemy):

    def __init__(self):
        Enemy.__init__(self)
