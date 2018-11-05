import random
import pygame
import Helper
import Entity
import ImageFiles

# Classes used by Room type Objects


class Room:
    room_index = 0

    # create dictionary for lane positions

    def __init__(self):
        self.index = Room.room_index
        Room.room_index += 1


class RoomTutorial(Room):

    current_stage = 0
    tutorial_stages = 3

    def __init__(self):
        Room.__init__(self)
        self.texture = ImageFiles.images['Rooms']['Tutorial']
        # Use this in the regular enemy and boss rooms
        self.lanes = dict()
        self.lanes['left'] = Lane(150, 150, 'left')
        self.lanes['centre'] = Lane(375, 150, 'centre')
        self.lanes['right'] = Lane(600, 150, 'right')

    @staticmethod
    def create_tutorial_room(enemies=random.randint(1, 3)):
        room = RoomTutorial()

        if enemies > 0:
            room.lanes['centre'].occupy_lane(Entity.Enemy)
            enemies -= 1

        if enemies > 0:
            room.lanes['left'].occupy_lane(Entity.Enemy)
            enemies -= 1

        if enemies > 0:
            room.lanes['right'].occupy_lane(Entity.Enemy)
            enemies -= 1


class Lane():
    def __init__(self, origin_x, origin_y, key, is_occupied=False):
        self.occupied = is_occupied
        self.occupant = None
        self.origin = (origin_x, origin_y)
        self.key = key

    def occupy_lane(self, occupant):
        self.occupant = occupant
        self.occupied = True


class RoomEncounter(Room):
    def __init__(self, room_type = random.randint(1, 4)):
        Room.__init__(self)


class RoomEnemy(Room):

    def __init__(self):
        Room.__init__(self)


class RoomBoss(Room):

    def __init__(self):
        Room.__init__(self)

