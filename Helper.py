import pygame

REFRESH_RATE = 100
RESOLUTION = (750, 1334)
DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION)

SWIPE_DISTANCE = 90  # distance moved for input to be registered as a swipe
MOVE_DISTANCE = 160  # distance the onscreen character moves
MOVE_SPEED = 5  # distance for character move steps

INVENTORY_POSITION = (15, 970)
# Colours - Not currently used
darkBrown = (79, 51, 44)
lightBrown = (107, 74, 55)
darkYellow = (124, 91, 51)
lightYellow = (147, 117, 53)
black = (0, 0, 0)
darkGrey = (63, 63, 63)
midGrey = (127, 127, 127)
lightGrey = (191, 191, 191)


# Tuples containing elements for naming items, rooms, entities etc
Affinities = ('Chaos', 'Abyss', 'Void', 'Eldritch')
Elements = ('Water', 'Air', 'Earth', 'Fire')
Modifiers_Elemental_T1 = ('Dew', 'Whistles', 'Pebbles', 'Ashes')
Modifiers_Elemental_T2 = ('Splashes', 'Breezes', 'Rocks', 'Smoulders')
Modifiers_Elemental_T3 = ('Waves', 'Typhoons', 'Boulders', 'Flames')
Modifiers_Bonus = ('Cursed', 'Blessed')
Quality = ('Broken', 'Chipped', 'Mundane', 'Tempered', 'Pristine')
Weapons = ('Nodachi', 'Katana', 'Tekkan', 'Hachiwari')
Upgrades = ('+0', '+1', '+2', '+3', '+4', '+5')


room_tutorial_path = './Resources/Visual/Textures/Rooms/room.png'

# Defining colors for the 4 elements

Modifiers_Elemental_Colours = ((28, 58, 89),
                               (244, 213, 141),
                               (28, 89, 29),
                               (206, 78, 55))

# Usage: Select element from tuples and parse it to generator

# Order: Quality + WEAPON_NAME + 'OF' +  Modifiers_Elemental
# + Upgrade + (Modifier_Bonus)
# Example: Chipped Nodachi of Smoulders +2 (Cursed)

# Room variables:

room_encounter_type = (
                       'ascension',
                       'a shrine',
                       'a fork in the road',
                       'a villager in need',
                       'rubble on the road'
                       )

# Entity variables:

LANES = dict(
    left=[(150, 375), False],
    middle=[(375, 375), False],
    right=[(600, 375), False]
)
