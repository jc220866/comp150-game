# Classes used by Entity type Objects
import Helper
import random
import time

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

    def generate_modifiers(self):
        # modifier array should contain: AFFINITY, ELEMENT, ELEMENT_TIER, BONUS MODIFIER, QUALITY, UPGRADE
        # to indicate the lack of a modifier, -1 will be used
        modifiers = [-1, -1, -1, -1, -1, -1]

        modifiers_size = [len(Helper.Affinities), len(Helper.Elements), 3, len(Helper.Modifiers_Bonus), len(Helper.Quality)]    # defines the number of possibilities for each modifier (-1 is added in the call)
        modifiers_min = [-1, -1, 0, -1, 0, 0]   # Minimum values for modifiers: e.g. the QUALITY cannot be non-existent (-1)

        for i in range(0, 4):   # We iterate through the first 4 modifiers
            modifiers[i] = random.randint(modifiers_min[i], modifiers_size[i]-1)    # We assign a random value to each modifier, based on their minimum and maximum values

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

    def generate_name(self, modifiers, weapon_type = random.randint(0, len(Helper.Weapons))):   # We import a modifier array and an OPTIONAL weapon type (if we want a custom item)

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

        name = quality + ' ' + type + element + upgrade

        return name

    def __init__(self, isCustom = False):   # If we want to create a custom item, all we have to do is set isCustom to True
        Item.__init__(self)
        #if not isCustom:
        modifiers = Weapon.generate_modifiers(self)
        weapon_type = random.randint(0, 3)
        self.type = weapon_type
        self.name = Weapon.generate_name(self, modifiers, weapon_type)


def weapon_generator():     # Generates random weapons twice per second
    while True:
        weapon = Weapon()
        print(weapon.name)
        time.sleep(0.5)
