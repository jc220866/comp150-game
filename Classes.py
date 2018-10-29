# Classes used by Entity type Objects
import Helper
import random
import pygame

# screen = pygame.Surface((400, 400), pygame.SRCALPHA, 32)
# pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 400), 0)

screen_width = int(750/3)
screen_height = int(1334/3)

screen = pygame.display.set_mode((screen_width, screen_height))


class Entity:

    # index is used to keep track of entities
    entity_index = 0    # Declaration of static Index
    entity_alignment = ('Aggressive', 'Passive', 'Friendly')    # Declaration of static alignment for all Entities

    def __init__(self):
        subname = 'Entity' + str(Entity.entity_index)    # subname is a unique identifier that uses the index
        name = 'Placeholder name'
        index = Entity.entity_index     # Importing index into the Entity-specific variable

        Entity.entity_index += 1    # Incrementing the index of all entities

        on_encounter = False    # defining where the entity is encountered (by default, nowhere)
        on_battle = False

        alignment = Entity.entity_alignment[1]  # setting alignment to passive as a default

        # To do: define states, as to specify what images and animations to incorporate into lists


class Player(Entity):

    def __init__(self): # hi
        Entity.__init__(self)


class Enemy(Entity):

    def __init__(self):
        Entity.__init__(self)


class EnemyBoss(Enemy):

    def __init__(self):
        Enemy.__init__(self)

# Classes used by Room type Objects


class Room:

    room_index = 0

    def __init__(self):
        Index = Room.room_index
        Room.room_index += 1


class RoomEncounter(Room):
    def __init__(self):
        Room.__init__(self)


class RoomEnemy(Room):

    def __init__(self):
        Room.__init__(self)


class RoomBoss(Room):

    def __init__(self):
        Room.__init__(self)

# Classes used by Item type Objects


class Item:

    item_index = 0

    def __init__(self):
        index = Item.item_index
        Item.item_index += 1


class Weapon(Item):

    # static values for reference
    weapon_width = 168
    weapon_height = 24

    @staticmethod
    def generate_modifiers():

        # modifier array should contain: AFFINITY, ELEMENT, ELEMENT_TIER, BONUS MODIFIER, QUALITY, UPGRADE
        # to indicate the lack of a modifier, -1 will be used

        modifiers = [-1, -1, -1, -1, -1, -1]

        modifiers_size = [len(Helper.Affinities), len(Helper.Elements), 3, len(Helper.Modifiers_Bonus), len(Helper.Quality)]    # defines the number of possibilities for each modifier (-1 is added in the call)
        modifiers_min = [-1, -1, 0, -1, 0, 0]   # Minimum values for modifiers: e.g. the QUALITY cannot be non-existent (-1)

        for i in range(0, 3):   # We iterate through the first 4 modifiers
            modifiers[i] = random.randint(modifiers_min[i], modifiers_size[i]-1)    # We assign a random value to each modifier, based on their minimum and maximum values

        bonus_roll = random.random()  # We select a random value between 0 and 1 for our bonus

        if bonus_roll <= .85:     # For each percentage threshold we assign a possible outcome
            bonus = -1
        elif bonus_roll <= .95:
            bonus = 0
        else:
            bonus = 1

        modifiers[3] = bonus

        quality_roll = random.random()  # We select a random value between 0 and 1 for our quality
        quality = 0     # Quality is initialised as 0

        if quality_roll <= .10:     # For each percentage threshold we assign a possible outcome
            quality = 0
        elif quality_roll <= .25:
            quality = 1
        elif quality_roll <= .75:
            quality = 2
        elif quality_roll <= .90:
            quality = 3
        elif quality_roll <= 1:
            quality = 4

        modifiers[4] = quality  # We assign the quality value to the modifier array

        upgrade_roll = random.random()  # Random value between 0 and 1 is selected
        upgrade = 0     # Upgrade level is initialised as 0

        if upgrade_roll <= .70:     # For each percentage threshold we assign a possible outcome
            upgrade = 0
        elif upgrade_roll <= .85:
            upgrade = 1
        elif upgrade_roll <= .93:
            upgrade = 2
        elif upgrade_roll <= .97:
            upgrade = 3
        elif upgrade_roll <= .99:
            upgrade = 4
        elif upgrade_roll <= 1:
            upgrade = 5
        modifiers[5] = upgrade  # We assign the upgrade level to the modifier array

        return modifiers    # We return the modifier array

    def generate_name(self, modifiers, weapon_type=random.randint(0, len(Helper.Weapons))):   # We import a modifier array and an OPTIONAL weapon type (if we want a custom item)

        quality = Helper.Quality[modifiers[4]]  # We select the corresponding string from the Helper script

        type = Helper.Weapons[weapon_type]  # Weapon type is assigned the corresponding string

        if modifiers[1] >= 0:   # If the weapon has elemental attributes
            element = ' of '
            if modifiers[2] == 0:   # Based on the tier of the Elemental enchantment, we assign a corresponding string
                element = element + Helper.Modifiers_Elemental_T1[modifiers[1]]
            elif modifiers[2] == 1:
                element = element + Helper.Modifiers_Elemental_T2[modifiers[1]]
            elif modifiers[2] == 2:
                element = element + Helper.Modifiers_Elemental_T3[modifiers[1]]
        else:
            element = ''    # If there is no elemental attribute, we assign an empty string

        if modifiers[3] != -1:  # If the weapon has bonus attributes
            bonus = ' (' + Helper.Modifiers_Bonus[modifiers[3]] + ')'
        else:
            bonus = ''

        upgrade = ' ' + Helper.Upgrades[modifiers[5]]

        name = quality + ' ' + type + element + upgrade + bonus

        return name

    # thing about this function is, in order for it to work, a pygame.display must be set. However, how can we do that
    # in a separate script?

    @staticmethod
    def generate_blade(blade, modifiers):
        for x in range(0, blade.get_width()):
            for y in range(0, blade.get_height()):
                new_colour = blade.get_at((x, y))
                if new_colour.a > 0:
                    new_colour.r = max(min((new_colour.r + (modifiers[4] - 2) * 10), 255), 0)
                    new_colour.g = max(min((new_colour.g + (modifiers[4] - 2) * 10), 255), 0)
                    new_colour.b = max(min((new_colour.b + (modifiers[4] - 2) * 10), 255), 0)
                    if modifiers[1] > -1:
                        if modifiers[1] == 0:
                            new_colour.b = min((new_colour.b + (modifiers[2] + 1) * 10), 255)
                        elif modifiers[1] == 1:
                            new_colour.b = min((new_colour.b + (modifiers[2] + 1) * 10), 255)
                            new_colour.g = min((new_colour.g + (modifiers[2] + 1) * 10), 255)
                        elif modifiers[1] == 2:
                            new_colour.g = min((new_colour.g + (modifiers[2] + 1) * 10), 255)
                        elif modifiers[1] == 3:
                            new_colour.r = min((new_colour.r + (modifiers[2] + 1) * 10), 255)
                blade.set_at((x, y), new_colour)
        return blade

    @staticmethod
    def generate_bonus(bonus, modifiers):
        for x in range(0, bonus.get_width()):
            for y in range(0, bonus.get_height()):
                new_colour = bonus.get_at((x, y))
                if modifiers[3] == -1:
                    new_colour.a = 0
                elif modifiers[3] == 1:
                    aux = new_colour.g
                    new_colour.g = new_colour.b
                    new_colour.b = aux
                bonus.set_at((x, y), new_colour)
        return bonus

    @staticmethod
    def generate_texture(modifiers, handle, blade, bonus):

        texture = pygame.Surface((168, 24))
        texture.blit(Weapon.generate_bonus(bonus, modifiers), (0, 0))
        texture.blit(Weapon.generate_blade(blade, modifiers), (0, 0))
        texture.blit(handle, (0, 0))

        return texture

    def __init__(self, is_custom = False):   # If we want to create a custom item we have to set isCustom to True
        Item.__init__(self)

        # if not isCustom:
        modifiers = Weapon.generate_modifiers()
        weapon_type = random.randint(0, 3)
        self.weapon_texture = Weapon.generate_texture(
                                                    modifiers,
                                                    pygame.image.load(Helper.handle_path).convert_alpha(),
                                                    pygame.image.load(Helper.blade_path).convert_alpha(),
                                                    pygame.image.load(Helper.bonus_path).convert_alpha()
                                                    )   # not entirely sure how I should pass the parameters
        self.type = weapon_type
        self.modifiers = modifiers
        self.name = Weapon.generate_name(self, modifiers, weapon_type)


def generate_weapon():     # Generates random weapons twice per second
    weapon = Weapon()
    print('Generated: ' + weapon.name)
    screen.blit(weapon.weapon_texture, (0, 0))
    pygame.display.flip()
    # time.sleep(1.5)
