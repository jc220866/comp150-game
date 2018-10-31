import Entity
import Helper
import pygame
import ImageFiles


class Player:
    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 ]  # (311.0, 202.8 for 750x1334 resolution)
    moveDistance = Helper.MOVE_DISTANCE

    def __init__(self):
        self.name = 'player'

    @staticmethod
    def player_action(action):
        """For now, this always fires player move - this is just for testing"""
        print(action)
        Player.player_move(action)

    @staticmethod
    def player_move(direction):  # needs four directions
        if direction == 'move_right' and Player.currentLane < 1:
            player_destination = Player.playerPos[0] + Player.moveDistance
            Player.currentLane += 1
            print (Player.currentLane)
            while Player.playerPos[0] < player_destination:
                Player.playerPos[0] += 5  # needs a loop in the "Main" script..?
        elif direction == 'move_left' and Player.currentLane > -1:
            player_destination = Player.playerPos[0] - Player.moveDistance
            Player.currentLane -= 1
            print (Player.currentLane)
            while Player.playerPos[0] > player_destination:
                Player.playerPos[0] -= 5  # needs a loop in the "Main" script..?


