import random
import pygame
import Helper
import ImageFiles

# Classes used by Room type Objects


class Room:
    room_index = 0

    def __init__(self):
        self.index = Room.room_index
        Room.room_index += 1

    @staticmethod
    def generate_tutorial():
        rooms_tutorial = [RoomTutorial()]


class RoomTutorial(Room):

    def __init__(self):
        Room.__init__(self)
        self.texture = ImageFiles.images['Rooms']['Tutorial']


class RoomEncounter(Room):
    def __init__(self, room_type = random.randint(1, 4)):
        Room.__init__(self)


class RoomEnemy(Room):

    def __init__(self):
        Room.__init__(self)


class RoomBoss(Room):

    def __init__(self):
        Room.__init__(self)

